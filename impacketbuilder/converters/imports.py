import pathlib
from midlparser import parse_idl
from impacketbuilder.converters.typing import IDL_TYPES
from midl import MidlImport
from .base import *
from .typing import *

class MidlImportsConverter(Converter):
    def convert(self, imports:list[MidlImport], import_dir:str, def_converter):
        #TODO add imports here
        self.base_imports()
        self.type_mapping()
        for _import in imports:
            in_file = pathlib.Path(import_dir+_import.file.replace("\"",""))
            def_converter.convert(parse_idl(in_file), import_dir)

    def base_imports(self):
        imports = """
from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
"""
        self.write(imports)

    def type_mapping(self):
        mapping = ""
        for t in IDL_TYPES:
            mapping += f"{self.mapper.canonicalize(t)} = {IDL_TO_NDR[t]}\n"
        self.write(mapping)