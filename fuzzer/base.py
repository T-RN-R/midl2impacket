import abc
from fuzzer.datatype import DataTypeLookup

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
class FuzzableMidl(Fuzzable):
    """Fuzzable MIDL concepts"""
