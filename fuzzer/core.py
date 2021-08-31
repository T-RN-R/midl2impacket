from fuzzer.base import FuzzableMidl, Testcase
from fuzzer.midl import In, Out, InOut
import fuzzer.config as config

random = config.rand
template = None

class TypeLookup:
    def __init__(self):
        self.map = {}

    def __contains__(self, item):
        return item in self.map

    def get_one(self, type_info):
        return random.choice(self.map[type_info])
    
    def insert(self, type_info, data):
        if type_info in self.map:
            self.map[type_info].extend([data])
        else:
            self.map[type_info] = [data]

class Fuzzer:
    server = None
    var_count = 0
    lookup_mapper = TypeLookup()

    def __init__(self, count, server_path, template_path):
        __import__(template_path)
        self.count = count
    def run(self):
        for i in range(0, self.count):
            self.fuzz_one()

    def fuzz_one(self):
        iters = config.ITERATION_COUNT
        testcase = Interface.generate(iters)  # Make an NdrCall!
        print(testcase)

    def get_var_name():
        Fuzzer.var_count += 1
        return f"v{Fuzzer.var_count}"

    def get_of_type(testcase, type_info):
        if type_info not in Fuzzer.lookup_mapper:
            return Fuzzer.generate_of_type(testcase, type_info)
        else:
            r = random.randint(0,100)
            if r > config.USE_EXISTING:
                return Fuzzer.lookup_mapper.get_one(type_info)
            else:
                return Fuzzer.generate_of_type(testcase, type_info)

    def generate_of_type(testcase, type_info):
        var = Fuzzer.get_var_name()
        generated_type = type_info.generate(None)[1]
        testcase.add(VariableInstantiation(var, generated_type))
        Fuzzer.lookup_mapper.insert(type_info,var)
        return var

    def clear_state():
        """Clears the fuzzing state."""
        Fuzzer.var_count = 0
        Fuzzer.lookup_mapper = TypeLookup()

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

class VariableInstantiation:
    def __init__(self, var_name:str, rhs:str):
        self.var_name = var_name
        self.rhs = rhs

    def __str__(self):
        return f"{self.var_name} = {self.rhs}\n"
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
        return testcase

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
                out_args[arg.param[1]] = Fuzzer.get_of_type(testcase, arg.param[0])
        return out_args
