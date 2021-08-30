from fuzzer.base import FuzzableMidl
from fuzzer.midl import In, Out, InOut
import fuzzer.config as config

random = config.rand
server = None
template = None
class Fuzzer:
    def __init__(self, server_path, template_path):
        server = __import__(server_path)
    def fuzz_one(self):
        iters = config.ITERATION_COUNT
        Interface.generate(iters, self.server, self.template) # Make an NdrCall!

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
        
    def generate(iters = 10):
        #CONNECT HERE
        connection_handle = None
        interface = random.choice(Interface.INSTANCES)
        for i in range(0, iters):
            method = random.choice(interface.methods)
            method.invoke(connection_handle)

class Method(FuzzableMidl):
    """A class whose instances represent Midl procudure invocation generator defintion"""

    def __init__(self, name, *parameters, **kwargs):
        self.name = name
        self.arguments = parameters

    def get_resp_str(self):
        return f"{self.name}Response"
    def generate():
        pass
    def invoke(self, dc):
        # dynamically import the class name.
        args = self.get_arguments()
        print("ASDSADASD")
        assert(server is not None)
        pass

    def get_arguments(self):
        out_args = {}
        for arg in self.arguments:
            if isinstance(arg, (In,InOut)):
                out_args[arg[1]] = arg[0].generate()
        return out_args

