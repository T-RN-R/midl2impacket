"""Generated from MIDL2Impacket.py"""

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
#################################################################################
#CONSTANTS
#################################################################################
MSRPC_UUID_IEVENTSERVICE = uuidtup_to_bin(('uuid(f6beaff7-1e19-4fbb-9f8f-b89e2018337c,)','0.0'))
MAX_PAYLOAD = 2 * 1024 * 1024
MAX_RPC_QUERY_LENGTH = MAX_PAYLOAD / 4
MAX_RPC_CHANNEL_NAME_LENGTH = 512
MAX_RPC_QUERY_CHANNEL_SIZE = 512
MAX_RPC_EVENT_ID_SIZE = 256
MAX_RPC_FILE_PATH_LENGTH = 32768
MAX_RPC_CHANNEL_PATH_LENGTH = 32768
MAX_RPC_BOOKMARK_LENGTH = MAX_PAYLOAD / 4
MAX_RPC_PUBLISHER_ID_LENGTH = 2048
MAX_RPC_PROPERTY_BUFFER_SIZE = MAX_PAYLOAD
MAX_RPC_FILTER_LENGTH = MAX_RPC_QUERY_LENGTH
MAX_RPC_RECORD_COUNT = 1024
MAX_RPC_EVENT_SIZE = MAX_PAYLOAD
MAX_RPC_BATCH_SIZE = MAX_PAYLOAD
MAX_RPC_RENDERED_STRING_SIZE = MAX_PAYLOAD
MAX_RPC_CHANNEL_COUNT = 8192
MAX_RPC_PUBLISHER_COUNT = 8192
MAX_RPC_EVENT_METADATA_COUNT = 256
MAX_RPC_VARIANT_LIST_COUNT = 256
MAX_RPC_BOOL_ARRAY_COUNT = MAX_PAYLOAD / 1
MAX_RPC_UINT32_ARRAY_COUNT = MAX_PAYLOAD / 2
MAX_RPC_UINT64_ARRAY_COUNT = MAX_PAYLOAD / 4
MAX_RPC_STRING_ARRAY_COUNT = MAX_PAYLOAD / 512
MAX_RPC_GUID_ARRAY_COUNT = MAX_PAYLOAD / 16
MAX_RPC_STRING_LENGTH = MAX_PAYLOAD / 4

class CONTEXT_HANDLE_REMOTE_SUBSCRIPTION(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
    )        
        
class CONTEXT_HANDLE_LOG_QUERY(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_LOG_QUERY(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_LOG_QUERY),
    )        
        
class CONTEXT_HANDLE_LOG_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_LOG_HANDLE(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_LOG_HANDLE),
    )        
        
class CONTEXT_HANDLE_OPERATION_CONTROL(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_OPERATION_CONTROL(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_OPERATION_CONTROL),
    )        
        
class CONTEXT_HANDLE_PUBLISHER_METADATA(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_PUBLISHER_METADATA(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_PUBLISHER_METADATA),
    )        
        
class CONTEXT_HANDLE_EVENT_METADATA_ENUM(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class PCONTEXT_HANDLE_EVENT_METADATA_ENUM(NDRPOINTER):
    referent = (
        ('Data', CONTEXT_HANDLE_EVENT_METADATA_ENUM),
    )        
        
class RPCINFO(NDRSTRUCT):
    structure = (
        ('m_error', DWORD),('m_subErr', DWORD),('m_subErrParam', DWORD),
    )
        
class DATA_BOOLEANARRAY(NDRUniConformantArray):
    item = BOOLEAN

class PTR_BOOLEANARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_BOOLEANARRAY),
    )

class BOOLEANARRAY(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('ptr', PTR_BOOLEANARRAY),
    )
        
class DATA_UINT32ARRAY(NDRUniConformantArray):
    item = DWORD

class PTR_UINT32ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT32ARRAY),
    )

class UINT32ARRAY(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('ptr', PTR_UINT32ARRAY),
    )
        
class DATA_UINT64ARRAY(NDRUniConformantArray):
    item = DWORD64

class PTR_UINT64ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT64ARRAY),
    )

class UINT64ARRAY(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('ptr', PTR_UINT64ARRAY),
    )
        
class DATA_STRINGARRAY(NDRUniConformantArray):
    item = LPWSTR

class PTR_STRINGARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_STRINGARRAY),
    )

class STRINGARRAY(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('ptr', PTR_STRINGARRAY),
    )
        
class DATA_GUIDARRAY(NDRUniConformantArray):
    item = GUID

class PTR_GUIDARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_GUIDARRAY),
    )

class GUIDARRAY(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('ptr', PTR_GUIDARRAY),
    )
        
class EVTRPCVARIANTTYPE:
	EvtRpcVarTypeNull = 0,
	EvtRpcVarTypeBoolean = 1,
	EvtRpcVarTypeUInt32 = 2,
	EvtRpcVarTypeUInt64 = 3,
	EvtRpcVarTypeString = 4,
	EvtRpcVarTypeGuid = 5,
	EvtRpcVarTypeBooleanArray = 6,
	EvtRpcVarTypeUInt32Array = 7,
	EvtRpcVarTypeUInt64Array = 8,
	EvtRpcVarTypeStringArray = 9
        
class EVTRPCASSERTCONFIGFLAGS:
	EvtRpcChannelPath = 0
        
class ANONYMOUS1(NDRUNION):
    union = {
        1: ('nullVal',INT),2: ('booleanVal',BOOLEAN),3: ('uint32Val',DWORD),4: ('uint64Val',DWORD64),5: ('stringVal',LPWSTR),6: ('guidVal',GUID),7: ('booleanArray',BOOLEANARRAY),8: ('uint32Array',UINT32ARRAY),9: ('uint64Array',UINT64ARRAY),10: ('stringArray',STRINGARRAY),11: ('guidArray',GUIDARRAY),
    }
        
class EVTRPCVARIANT(NDRSTRUCT):
    structure = (
        ('type', EVTRPCVARIANTTYPE),('flags', DWORD),('Anonymous1', ANONYMOUS1),
    )
        
class DATA_EVTRPCVARIANTLIST(NDRUniConformantArray):
    item = EVTRPCVARIANT

class PTR_EVTRPCVARIANTLIST(NDRPOINTER):
    referent = (
        ('Data', DATA_EVTRPCVARIANTLIST),
    )

class EVTRPCVARIANTLIST(NDRSTRUCT):
    structure = (
        ('count', DWORD),
        ('props', PTR_EVTRPCVARIANTLIST),
    )
        
class EVTRPCQUERYCHANNELINFO(NDRSTRUCT):
    structure = (
        ('name', LPWSTR),('status', DWORD),
    )
        