import abc
from fuzzer.datatype import DataTypeLookup
from fuzzer.config import rand as random

"""Base classes for fuzzer generator generation code
"""


class Fuzzable(abc.ABC):
    "Class that acts as a registry for mapping types to generators"
    __REGISTRY = DataTypeLookup()

    def registry(self):
        """returns the static __REGISTRY to be used across child classes"""
        return Fuzzable.__REGISTRY

    def add_mapping(self, type_name, target_type):
        """Inserts a type mapping into the registry"""
        Fuzzable.__REGISTRY.insert(type_name, target_type)

    @abc.abstractmethod
    def generate(self):
        pass

    def get_one_of_type(self, requested_type):
        # TODO: Add a coinflip here to decided whether to generate a new isntance of the given type,
        #  or to do a lookup through previous defined variables and objects to find and instance
        pass


class NDRINTERFACE:
    INSTANCES = []

    def __init__(self, uuid, version, methods):
        """Rpc Interface class"""
        self.uuid = uuid
        self.version = version
        self.methods = methods
        NDRINTERFACE.INSTANCES.append(self)

    @classmethod
    def generate(cls, iters, fuzzer):
        """Generate an invocation of a function from one interface"""
        # CONNECT HERE
        interface = random.choice(NDRINTERFACE.INSTANCES)
        testcase = Testcase()
        for i in range(0, iters):
            method = random.choice(interface.methods)
            testcase.add(method.generate(testcase, fuzzer))
        return testcase


class Testcase:
    def __init__(self):
        # holds variable definitions and invocations
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def __str__(self):
        out = ""
        for s in self.statements:
            out += str(s) + "\n"
        return out
