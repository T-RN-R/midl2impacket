from .base import Converter
from .struct import MidlStructConverter
from .procedure import MidlProcedureConverter
from midl import *
from .typing import *
from .comments import MidlCommentWriter


class MidlStaticConverter(Converter):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.HAS_RUN=False
    def convert(self, imports:list[MidlImport]):
        if not self.HAS_RUN:
            comment_writer = MidlCommentWriter(self.io, self.tab_level)
            comment_writer.comment_block("Generated from MIDL2Impacket.py")
            self.base_imports()
            self.type_mapping()
            self.HAS_RUN = True

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
HANDLE_T = CONTEXT_HANDLE
class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )
"""
        self.write(imports)

    def type_mapping(self):
        mapping = ""
        for t in IDL_TYPES:
            mapping += f"{self.mapper.canonicalize(t)} = {IDL_TO_NDR[t]}\n"
        self.write(mapping)