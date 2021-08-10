from .base import Converter
from .constants import MidlConstantConverter
from .interface import MidlInterfaceConverter
from midl import *
from io import StringIO
class MidlDefinitionConverter:
    def convert(definition : MidlDefinition) -> str:
        strIO = StringIO()
        const_converter = MidlConstantConverter(strIO, tab_level=0)
        interface_converter = MidlInterfaceConverter(strIO, tab_level=0)

        MidlDefinitionConverter.__header_comment_block(strIO)
        MidlDefinitionConverter.__default_imports(strIO)
        if len(definition.interfaces) > 1:
            raise Exception("ImpacketBuilder cannot handle MIDL files with multiple interface definitions")
        for td in definition.typedefs:
            interface_converter.handle_typedef(td)
        if len(definition.interfaces) >= 1:
            MidlDefinitionConverter.__banner_comment(strIO,"CONSTANTS")
            MidlDefinitionConverter.__uuid(strIO, definition.interfaces[0])
            for const in definition.instantiation:
                const_converter.convert(const)
            interface_converter.convert(definition.interfaces[0])
        return strIO.getvalue()

    def __uuid(io : StringIO, interface : MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"

        io.write(f"{int_name} = uuidtup_to_bin(('{interface.attributes['uuid']}','0.0'))\n")

    def __banner_comment(io : StringIO, comment:str):
        MidlDefinitionConverter.__sl_comment(io,"#"*80)
        MidlDefinitionConverter.__sl_comment(io, comment)
        MidlDefinitionConverter.__sl_comment(io,"#"*80)

    def __sl_comment(io : StringIO, comment:str):
        io.write(f"#{comment}\n")

    def __default_imports(io : StringIO):
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
        io.write(imports)

    def __header_comment_block(io : StringIO):
        comment = '"""Generated from MIDL2Impacket.py"""\n' 
        io.write(comment)
