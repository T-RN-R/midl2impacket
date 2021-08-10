from re import L, M
from io import StringIO


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
        io = StringIO()
        python_code = MidlDefinitionConverter(io, tab_level=0).convert(self.__midl_def)
        return python_code