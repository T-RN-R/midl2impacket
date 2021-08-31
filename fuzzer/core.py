from fuzzer.base import FuzzableMidl, Testcase
from fuzzer.midl import In, Out, InOut
import fuzzer.config as config

random = config.rand
template = None


class Fuzzer:
    server = None

    def __init__(self, count, server_path, template_path):
        self.count = count
        Fuzzer.server = __import__(server_path)

    def run(self):
        for i in range(0, self.count):
            self.fuzz_one()

    def fuzz_one(self):
        iters = config.ITERATION_COUNT
        Interface.generate(iters, Fuzzer.server)  # Make an NdrCall!

    def clear_state(self):
        """Clears the fuzzing state."""


class Interface(FuzzableMidl):
    INSTANCES = []

    def __init__(self, uuid, version, methods):
        """Rpc Interface class"""
        self.uuid = uuid
        self.version = version
        self.methods = methods
        Interface.INSTANCES.append(self)

    def generate(iters=10):
        # CONNECT HERE
        interface = random.choice(Interface.INSTANCES)
        testcase = Testcase()
        for i in range(0, iters):
            # TODO: Generate a bunch of variables here.
            method = random.choice(interface.methods)
            testcase.add(method.generate(testcase))


class MethodInvocation:
    def __init__(self, name: str, arguments: dict):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        # TODO get respons variable name here, and globally assign a type to the name
        out = f"req = {self.name}()\n"
        for arg in self.arguments:
            out += f"req.{arg} = {self.arguments[arg]}\n"
        out += f"resp = dce.request(req)\n"
        return out


class Method(FuzzableMidl):
    """A class whose instances represent Midl procudure invocation generator defintion"""

    def __init__(self, name, *parameters, **kwargs):
        self.name = name
        self.arguments = parameters

    def get_resp_str(self):
        return f"{self.name}Response"

    def generate(self, testcase):
        """Generates an invocation of the testcase

        Args:
            testcase ([type]): testcase object to append to
        """
        args = self.get_arguments(testcase)
        return MethodInvocation(self.name, args)

    def get_arguments(self, testcase):
        out_args = {}
        for arg in self.arguments:
            if isinstance(arg, (In, InOut)):
                out_args[arg[1]] = arg[0].generate(testcase)
        return out_args
