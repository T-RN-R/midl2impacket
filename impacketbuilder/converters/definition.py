from .base import Converter
from .constants import MidlConstantConverter
from .interface import MidlInterfaceConverter
from midl import *
from io import StringIO
class MidlDefinitionConverter(Converter):
    def convert(self, definition : MidlDefinition) -> str:
        const_converter = MidlConstantConverter(self.io, tab_level=self.tab_level)
        interface_converter = MidlInterfaceConverter(self.io, tab_level=self.tab_level)

        self.__header_comment_block()
        self.__default_imports()
        if len(definition.interfaces) > 1:
            raise Exception("ImpacketBuilder cannot handle MIDL files with multiple interface definitions")
        for td in definition.typedefs:
            interface_converter.handle_typedef(td)
        if len(definition.interfaces) >= 1:
            self.__banner_comment("CONSTANTS")
            self.__uuid(definition.interfaces[0])
            for const in definition.instantiation:
                const_converter.convert(const)
            interface_converter.convert(definition.interfaces[0])
        return self.io.getvalue()

    def __uuid(self, interface : MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"

        io.write(f"{int_name} = uuidtup_to_bin(('{interface.attributes['uuid']}','0.0'))\n")

    def __banner_comment(self,  comment:str):
        self.__sl_comment("#"*80)
        self.__sl_comment( comment)
        self.__sl_comment("#"*80)

    def __sl_comment(self, comment:str):
        self.write(f"#{comment}\n")

    def __default_imports(self):
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
DWORD64 = LONGLONG
__INT64 = DWORD64
LPCWSTR = LPWSTR
LCID = DWORD
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
"""
        self.write(imports)

    def __header_comment_block(self):
        comment = '"""Generated from MIDL2Impacket.py"""\n' 
        self.write(comment)
