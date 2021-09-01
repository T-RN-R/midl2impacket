from .base import Converter
from .typing import IDL_TO_NDR
from .comments import MidlCommentWriter


class MidlStaticConverter(Converter):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.HAS_RUN = False
    def convert(self):
        if not self.HAS_RUN:
            comment_writer = MidlCommentWriter(self.io, self.tab_level)
            comment_writer.comment_block("Generated from MIDL2Impacket.py")
            self.base_imports()
            self.type_mapping()
            self.HAS_RUN = True

    def base_imports(self):
        imports = """
# pylint: disable=C0103,C0302,W0614
from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import STR, LPSTR, WSTR, LPWSTR
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

from impacket import system_errors
class DCERPCSessionError(DCERPCException):
    def __init__(self, error_string=None, error_code=None, packet=None):
        DCERPCException.__init__(self, error_string, error_code, packet)

    def __str__( self ):
        key = self.error_code
        if key in system_errors.ERROR_MESSAGES:
            error_msg_short = system_errors.ERROR_MESSAGES[key][0]
            error_msg_verbose = system_errors.ERROR_MESSAGES[key][1] 
            return 'SessionError: code: 0x%x - %s - %s' % (self.error_code, error_msg_short, error_msg_verbose)
        return 'SessionError: unknown error code: 0x%x' % self.error_code

class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
"""
        self.write(imports)

    def type_mapping(self):
        for idl_name, py_name in IDL_TO_NDR.items():
            canonicalized_name, _ = self.mapper.canonicalize(idl_name)
            if canonicalized_name != py_name:
                self.write(f"{canonicalized_name} = {py_name}")
            self.mapper.add_type(canonicalized_name)

