import abc
from fuzzer.core.datatype import DataTypeLookup

"""Base classes for fuzzer generator generation code"""


class Fuzzable(abc.ABC):
    "Class that acts as a registry for mapping types to generators"
    __REGISTRY = DataTypeLookup()

    def registry(self):
        """returns the static __REGISTRY to be used across child classes"""
        return Fuzzable.__REGISTRY

    def add_mapping(self, type_name, target_type):
        """Inserts a type mapping into the registry"""
        Fuzzable.__REGISTRY.insert(type_name, target_type)

    @abc.abstractclassmethod
    def generate(self):
        pass


class FuzzableMidl(Fuzzable):
    """Fuzzable MIDL concepts"""

    pass
