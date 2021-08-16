from re import L, M

from impacketbuilder.ndrbuilder.io import PythonWriter
from midltypes import MidlDefinition
from .converters.definition import MidlDefinitionConverter
from .converters.static import MidlStaticConverter
from .converters.typing import TypeMapper, IDL_TYPES


class ImpacketBuilder:
    """Converts a MIDL Definition into a Python module"""
    def __init__(self):
        self.__midl_def = None

    def midl_def(self, definition: MidlDefinition):
        self.__midl_def = definition
        return self

    def import_dir(self, dir: str):
        self.__import_dir = dir
        return self

    def build(self):
        assert self.__midl_def != None
        io = PythonWriter()
        tm = TypeMapper(IDL_TYPES)
        tabs = 0
        static_converter = MidlStaticConverter(io, tabs, mapper=tm)
        static_converter.convert()

        python_code = MidlDefinitionConverter(io, tabs, mapper=tm).convert(
            self.__midl_def, self.__import_dir
        )
        return python_code
