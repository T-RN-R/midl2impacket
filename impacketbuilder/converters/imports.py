import pathlib
from midlparser import parse_idl
from impacketbuilder.converters.typing import IDL_TYPES
from midl import MidlImport
from .base import *
from .typing import *

class MidlImportsConverter(Converter):
    def convert(self, imports:list[MidlImport], import_dir:str, def_converter):
        #TODO add imports here
        for _import in imports:
            in_file = pathlib.Path(import_dir+_import.file.replace("\"",""))
            def_converter.convert(parse_idl(in_file), import_dir)