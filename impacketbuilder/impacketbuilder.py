from re import L, M
from midl import *
from .converters.definition import MidlDefinitionConverter



class ImpacketBuilder:
    def __init__(self):
        self.__midl_def = None

    def midl_def(self, definition : MidlDefinition):
        self.__midl_def = definition
        return self

    def build(self):
        assert(self.__midl_def != None)
        python_code = MidlDefinitionConverter.convert(self.__midl_def)
        return python_code