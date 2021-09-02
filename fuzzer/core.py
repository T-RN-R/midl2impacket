from fuzzer.base import  NDRINTERFACE, Testcase
from impacket.dcerpc.v5.ndr import NDRSTRUCT
import fuzzer.config as config

random = config.rand
template = None


class TypeLookup:
    def __init__(self):
        self.map = {}

    def __contains__(self, item):
        return item in self.map.keys()
        
    def get_derived_types(self, type_info):
        types = []
        for k in self.map:
            #This looks through all members of a struct for type_info
            if issubclass(k, NDRSTRUCT):
                for v in self.map[k]:
                    types.extend([v+i for i in k.get_child_fields_of_type(type_info)])
                
        return types

    def get_one(self, type_info):
        choices = self.map[type_info]
        choices += self.get_derived_types(type_info)
        return random.choice(choices)

    def insert(self, type_info, data):
        if type_info in self.map:
            self.map[type_info].extend([data])
        else:
            self.map[type_info] = [data]


class Fuzzer:
    """Core fuzzer class that maintains state information and controls the flow of code generation"""

    server = None
    var_count = 0
    lookup_mapper = TypeLookup()

    def __init__(self, count, server_path):
        __import__(
            server_path
        )  
        self.server = server_path# dynamically import the generated template to populate the fuzzer
        self.count = count  # Number of testcases to generate

    def run(self):
        """Start the fuzzing!"""
        for i in range(0, self.count):
            self.fuzz_one()

    def fuzz_one(self):
        """Does one unit of fuzzing"""
        iters = config.ITERATION_COUNT
        testcase = NDRINTERFACE.generate(iters, self)  # Make an NdrCall!
        import pathlib
        test = pathlib.Path("test.py")
        test.write_text(str(testcase))
        self.execute(testcase)

    def get_var_name(self):
        """Returns a unique variable name"""
        Fuzzer.var_count += 1
        return f"v{Fuzzer.var_count}"

    def get_of_type(self, testcase, type_info):
        """Gets a variable name associated with a type"""
        if type_info not in Fuzzer.lookup_mapper:
            # We haven't generated anything of the given type yet, so generate one
            return self.generate_of_type(testcase, type_info)
        else:
            r = random.randint(0, 100)
            if r < config.USE_EXISTING:
                return Fuzzer.lookup_mapper.get_one(type_info)
            else:
                return self.generate_of_type(testcase, type_info)

    def generate_of_type(self, testcase, type_info):
        """Generates a variable of the given type"""

        var = self.get_var_name()
        extra, generated_type = type_info.generate(var)
        testcase.add(VariableInstantiation(var, generated_type))
        Fuzzer.lookup_mapper.insert(type_info, var)
        return var

    def execute(self, testcase):
        exec(str(testcase))

    def clear_state(self):
        """Clears the fuzzing state."""
        Fuzzer.var_count = 0
        Fuzzer.lookup_mapper = TypeLookup()


class MethodInvocation:
    """Data structure representing the invocation of a method"""

    def __init__(self, name: str, arguments: dict, lhs: str):
        self.name = name
        self.arguments = arguments
        self.lhs = lhs

    def __str__(self):
        out = f"req = {self.name}()\n"
        for arg in self.arguments:
            out += f"req.{arg} = {self.arguments[arg]}\n"
        out += "try:\n"
        out += f"\t{self.lhs} = dce.request(req)\n"
        out+="except Exception as e:\n"
        out+=f"\tprint('Error at: {self.lhs} failing with: ' + str(e))\n"
        out+="\tprint(req.dump())\n"
        return out


class VariableInstantiation:
    """Data structure representing the instantiation of a variable"""

    def __init__(self, var_name: str, rhs: str):
        self.var_name = var_name
        self.rhs = rhs

    def __str__(self):
        return f"{self.var_name} = {self.rhs}\n"
