"""
Generated from MIDL2Impacket.py
"""


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

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG

#################################################################################

#TYPEDEFS

#################################################################################

WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PBOOL = INT
LPBOOL = INT
BYTE = UNSIGNED_CHAR
PBYTE = UNSIGNED_CHAR
LPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PBOOLEAN = BYTE
WCHAR = WCHAR_T
PWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PDWORD = UNSIGNED_LONG
LPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
LPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = CONST_WCHAR_T
LMSTR = WCHAR
LONG = LONG
PLONG = LONG
LPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = __INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PLONG64 = SIGNED___INT64
LPCSTR = CONST_CHAR
LPCVOID = CONST_VOID
LPCWSTR = CONST_WCHAR_T
PSTR = CHAR
LPSTR = CHAR
LPWSTR = WCHAR_T
PWSTR = WCHAR_T
NET_API_STATUS = DWORD
NTSTATUS = LONG
PCONTEXT_HANDLE = VOID
PPCONTEXT_HANDLE = PCONTEXT_HANDLE
QWORD = UNSIGNED___INT64
RPC_BINDING_HANDLE = VOID
STRING = UCHAR
UINT = UNSIGNED_INT
UINT8 = UNSIGNED_CHAR
UINT16 = UNSIGNED_SHORT
UINT32 = UNSIGNED_INT
UINT64 = UNSIGNED___INT64
ULONG = UNSIGNED_LONG
PULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PVOID = VOID
LPVOID = VOID
WORD = UNSIGNED_SHORT
PWORD = UNSIGNED_SHORT
LPWORD = UNSIGNED_SHORT

class FILETIME(NDRSTRUCT):
    structure = (
        ('dwLowDateTime', DWORD),('dwHighDateTime', DWORD),
    )
class PFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    
class LPFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    


class GUID(NDRSTRUCT):
    structure = (
        ('Data1', UNSIGNED_LONG),('Data2', UNSIGNED_SHORT),('Data3', UNSIGNED_SHORT),('Data4', BYTE),
    )
UUID = GUID
class PGUID(NDRPOINTER):
    referent = (
        ('Data', GUID),
    )    


class LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', SIGNED___INT64),
    )
class PLARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', LARGE_INTEGER),
    )    


class EVENT_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Id', USHORT),('Version', UCHAR),('Channel', UCHAR),('Level', UCHAR),('Opcode', UCHAR),('Task', USHORT),('Keyword', ULONGLONG),
    )
class PEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    
class PCEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    


class S0(NDRSTRUCT):
    structure = (
        ('KernelTime', ULONG),('UserTime', ULONG),
    )


class U0(NDRUNION):
    union = {
        1: ('s0',S0),2: ('ProcessorTime',ULONG64),
    }
        

class EVENT_HEADER(NDRSTRUCT):
    structure = (
        ('Size', USHORT),('HeaderType', USHORT),('Flags', USHORT),('EventProperty', USHORT),('ThreadId', ULONG),('ProcessId', ULONG),('TimeStamp', LARGE_INTEGER),('ProviderId', GUID),('EventDescriptor', EVENT_DESCRIPTOR),('u0', U0),('ActivityId', GUID),
    )
class PEVENT_HEADER(NDRPOINTER):
    referent = (
        ('Data', EVENT_HEADER),
    )    

LCID = DWORD

class LUID(NDRSTRUCT):
    structure = (
        ('LowPart', DWORD),('HighPart', LONG),
    )
class PLUID(NDRPOINTER):
    referent = (
        ('Data', LUID),
    )    


class MULTI_SZ(NDRSTRUCT):
    structure = (
        ('Value', WCHAR_T),('nChar', DWORD),
    )


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
    item = WCHAR

class PTR_RPC_UNICODE_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_UNICODE_STRING),
    )

class RPC_UNICODE_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_UNICODE_STRING),

    )
        

class SERVER_INFO_100(NDRSTRUCT):
    structure = (
        ('sv100_platform_id', DWORD),('sv100_name', WCHAR_T),
    )
class PSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    
class LPSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    


class SERVER_INFO_101(NDRSTRUCT):
    structure = (
        ('sv101_platform_id', DWORD),('sv101_name', WCHAR_T),('sv101_version_major', DWORD),('sv101_version_minor', DWORD),('sv101_version_type', DWORD),('sv101_comment', WCHAR_T),
    )
class PSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    
class LPSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    


class SYSTEMTIME(NDRSTRUCT):
    structure = (
        ('wYear', WORD),('wMonth', WORD),('wDayOfWeek', WORD),('wDay', WORD),('wHour', WORD),('wMinute', WORD),('wSecond', WORD),('wMilliseconds', WORD),
    )
class PSYSTEMTIME(NDRPOINTER):
    referent = (
        ('Data', SYSTEMTIME),
    )    


class UINT128(NDRSTRUCT):
    structure = (
        ('lower', UINT64),('upper', UINT64),
    )
class PUINT128(NDRPOINTER):
    referent = (
        ('Data', UINT128),
    )    


class ULARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', UNSIGNED___INT64),
    )
class PULARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', ULARGE_INTEGER),
    )    


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
    structure = (
        ('Value', BYTE),
    )

ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NDRSTRUCT):
    structure = (
        ('Level', WORD),('Remaining', ACCESS_MASK),('ObjectType', GUID),
    )
class POBJECT_TYPE_LIST(NDRPOINTER):
    referent = (
        ('Data', OBJECT_TYPE_LIST),
    )    


class ACE_HEADER(NDRSTRUCT):
    structure = (
        ('AceType', UCHAR),('AceFlags', UCHAR),('AceSize', USHORT),
    )
class PACE_HEADER(NDRPOINTER):
    referent = (
        ('Data', ACE_HEADER),
    )    


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
    structure = (
        ('Header', ACE_HEADER),('Mask', ACCESS_MASK),('SidStart', DWORD),
    )
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
    referent = (
        ('Data', SYSTEM_MANDATORY_LABEL_ACE),
    )    


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
    structure = (
        ('Policy', DWORD),
    )
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
    referent = (
        ('Data', TOKEN_MANDATORY_POLICY),
    )    


class MANDATORY_INFORMATION(NDRSTRUCT):
    structure = (
        ('AllowedAccess', ACCESS_MASK),('WriteAllowed', BOOLEAN),('ReadAllowed', BOOLEAN),('ExecuteAllowed', BOOLEAN),('MandatoryPolicy', TOKEN_MANDATORY_POLICY),
    )
class PMANDATORY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', MANDATORY_INFORMATION),
    )    


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
    structure = (
        ('Length', DWORD),('OctetString', BYTE),
    )
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    )    


class VALUES(NDRUNION):
    union = {
        1: ('pInt64',PLONG64),2: ('pUint64',PDWORD64),3: ('ppString',PWSTR),4: ('pOctetString',PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    }
        

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
    structure = (
        ('Name', DWORD),('ValueType', WORD),('Reserved', WORD),('Flags', DWORD),('ValueCount', DWORD),('Values', VALUES),
    )
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1),
    )    

SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD

class RPC_SID(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('SubAuthorityCount', UNSIGNED_CHAR),('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),('SubAuthority', UNSIGNED_LONG),
    )
class PRPC_SID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    
class PSID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    


class ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('AceCount', UNSIGNED_SHORT),('Sbz2', UNSIGNED_SHORT),
    )
class PACL(NDRPOINTER):
    referent = (
        ('Data', ACL),
    )    


class SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UCHAR),('Sbz1', UCHAR),('Control', USHORT),('Owner', PSID),('Group', PSID),('Sacl', PACL),('Dacl', PACL),
    )
class PSECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', SECURITY_DESCRIPTOR),
    )    

#################################################################################

#TYPEDEFS

#################################################################################

#################################################################################

#CONSTANTS

#################################################################################

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
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IEventService Definition

#################################################################################

MSRPC_UUID_IEVENTSERVICE = uuidtup_to_bin(('f6beaff7-1e19-4fbb-9f8f-b89e2018337c','0.0'))

PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION = VOID
PCONTEXT_HANDLE_LOG_QUERY = VOID
PCONTEXT_HANDLE_LOG_HANDLE = VOID
PCONTEXT_HANDLE_OPERATION_CONTROL = VOID
PCONTEXT_HANDLE_PUBLISHER_METADATA = VOID
PCONTEXT_HANDLE_EVENT_METADATA_ENUM = VOID

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
	('count', DWORD),	('ptr', PTR_BOOLEANARRAY),

    )
        

class DATA_UINT32ARRAY(NDRUniConformantArray):
    item = DWORD

class PTR_UINT32ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT32ARRAY),
    )

class UINT32ARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_UINT32ARRAY),

    )
        

class DATA_UINT64ARRAY(NDRUniConformantArray):
    item = DWORD64

class PTR_UINT64ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT64ARRAY),
    )

class UINT64ARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_UINT64ARRAY),

    )
        

class DATA_STRINGARRAY(NDRUniConformantArray):
    item = LPWSTR

class PTR_STRINGARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_STRINGARRAY),
    )

class STRINGARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_STRINGARRAY),

    )
        

class DATA_GUIDARRAY(NDRUniConformantArray):
    item = GUID

class PTR_GUIDARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_GUIDARRAY),
    )

class GUIDARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_GUIDARRAY),

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
        

class U0(NDRUNION):
    union = {
        1: ('nullVal',INT),2: ('booleanVal',BOOLEAN),3: ('uint32Val',DWORD),4: ('uint64Val',DWORD64),5: ('stringVal',LPWSTR),6: ('guidVal',GUID),7: ('booleanArray',BOOLEANARRAY),8: ('uint32Array',UINT32ARRAY),9: ('uint64Array',UINT64ARRAY),10: ('stringArray',STRINGARRAY),11: ('guidArray',GUIDARRAY),
    }
        

class EVTRPCVARIANT(NDRSTRUCT):
    structure = (
        ('type', EVTRPCVARIANTTYPE),('flags', DWORD),('u0', U0),
    )


class DATA_EVTRPCVARIANTLIST(NDRUniConformantArray):
    item = EVTRPCVARIANT

class PTR_EVTRPCVARIANTLIST(NDRPOINTER):
    referent = (
        ('Data', DATA_EVTRPCVARIANTLIST),
    )

class EVTRPCVARIANTLIST(NDRSTRUCT):
    structure = (
	('count', DWORD),	('props', PTR_EVTRPCVARIANTLIST),

    )
        

class EVTRPCQUERYCHANNELINFO(NDRSTRUCT):
    structure = (
        ('name', LPWSTR),('status', DWORD),
    )


class EvtRpcRegisterRemoteSubscription(NDRCALL):
    opnum = 0
    structure = (
		('CHANNELPATH', LPCWSTR),
		('QUERY', LPCWSTR),
		('BOOKMARKXML', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcRegisterRemoteSubscriptionResponse(NDRCALL):
    structure = (
		('HANDLE', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('CONTROL', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('QUERYCHANNELINFOSIZE', DWORD),
		('QUERYCHANNELINFO', EVTRPCQUERYCHANNELINFO),
		('ERROR', RPCINFO),
    )
        

class EvtRpcRemoteSubscriptionNextAsync(NDRCALL):
    opnum = 1
    structure = (
		('HANDLE', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('NUMREQUESTEDRECORDS', DWORD),
		('FLAGS', DWORD),
    )

class EvtRpcRemoteSubscriptionNextAsyncResponse(NDRCALL):
    structure = (
		('NUMACTUALRECORDS', DWORD),
		('EVENTDATAINDICES', DWORD),
		('EVENTDATASIZES', DWORD),
		('RESULTBUFFERSIZE', DWORD),
		('RESULTBUFFER', BYTE),
    )
        

class EvtRpcRemoteSubscriptionNext(NDRCALL):
    opnum = 2
    structure = (
		('HANDLE', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('NUMREQUESTEDRECORDS', DWORD),
		('TIMEOUT', DWORD),
		('FLAGS', DWORD),
    )

class EvtRpcRemoteSubscriptionNextResponse(NDRCALL):
    structure = (
		('NUMACTUALRECORDS', DWORD),
		('EVENTDATAINDICES', DWORD),
		('EVENTDATASIZES', DWORD),
		('RESULTBUFFERSIZE', DWORD),
		('RESULTBUFFER', BYTE),
    )
        

class EvtRpcRemoteSubscriptionWaitAsync(NDRCALL):
    opnum = 3
    structure = (
		('HANDLE', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
    )

class EvtRpcRemoteSubscriptionWaitAsyncResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcRegisterControllableOperation(NDRCALL):
    opnum = 4
    structure = (

    )

class EvtRpcRegisterControllableOperationResponse(NDRCALL):
    structure = (
		('HANDLE', PCONTEXT_HANDLE_OPERATION_CONTROL),
    )
        

class EvtRpcRegisterLogQuery(NDRCALL):
    opnum = 5
    structure = (
		('PATH', LPCWSTR),
		('QUERY', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcRegisterLogQueryResponse(NDRCALL):
    structure = (
		('HANDLE', PCONTEXT_HANDLE_LOG_QUERY),
		('OPCONTROL', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('QUERYCHANNELINFOSIZE', DWORD),
		('QUERYCHANNELINFO', EVTRPCQUERYCHANNELINFO),
		('ERROR', RPCINFO),
    )
        

class EvtRpcClearLog(NDRCALL):
    opnum = 6
    structure = (
		('CONTROL', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('CHANNELPATH', LPCWSTR),
		('BACKUPPATH', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcClearLogResponse(NDRCALL):
    structure = (
		('ERROR', RPCINFO),
    )
        

class EvtRpcExportLog(NDRCALL):
    opnum = 7
    structure = (
		('CONTROL', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('CHANNELPATH', LPCWSTR),
		('QUERY', LPCWSTR),
		('BACKUPPATH', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcExportLogResponse(NDRCALL):
    structure = (
		('ERROR', RPCINFO),
    )
        

class EvtRpcLocalizeExportLog(NDRCALL):
    opnum = 8
    structure = (
		('CONTROL', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('LOGFILEPATH', LPCWSTR),
		('LOCALE', LCID),
		('FLAGS', DWORD),
    )

class EvtRpcLocalizeExportLogResponse(NDRCALL):
    structure = (
		('ERROR', RPCINFO),
    )
        

class EvtRpcMessageRender(NDRCALL):
    opnum = 9
    structure = (
		('PUBCFGOBJ', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('SIZEEVENTID', DWORD),
		('EVENTID', BYTE),
		('MESSAGEID', DWORD),
		('VALUES', EVTRPCVARIANTLIST),
		('FLAGS', DWORD),
		('MAXSIZESTRING', DWORD),
    )

class EvtRpcMessageRenderResponse(NDRCALL):
    structure = (
		('ACTUALSIZESTRING', DWORD),
		('NEEDEDSIZESTRING', DWORD),
		('STRING', BYTE),
		('ERROR', RPCINFO),
    )
        

class EvtRpcMessageRenderDefault(NDRCALL):
    opnum = 10
    structure = (
		('SIZEEVENTID', DWORD),
		('EVENTID', BYTE),
		('MESSAGEID', DWORD),
		('VALUES', EVTRPCVARIANTLIST),
		('FLAGS', DWORD),
		('MAXSIZESTRING', DWORD),
    )

class EvtRpcMessageRenderDefaultResponse(NDRCALL):
    structure = (
		('ACTUALSIZESTRING', DWORD),
		('NEEDEDSIZESTRING', DWORD),
		('STRING', BYTE),
		('ERROR', RPCINFO),
    )
        

class EvtRpcQueryNext(NDRCALL):
    opnum = 11
    structure = (
		('LOGQUERY', PCONTEXT_HANDLE_LOG_QUERY),
		('NUMREQUESTEDRECORDS', DWORD),
		('TIMEOUTEND', DWORD),
		('FLAGS', DWORD),
    )

class EvtRpcQueryNextResponse(NDRCALL):
    structure = (
		('NUMACTUALRECORDS', DWORD),
		('EVENTDATAINDICES', DWORD),
		('EVENTDATASIZES', DWORD),
		('RESULTBUFFERSIZE', DWORD),
		('RESULTBUFFER', BYTE),
    )
        

class EvtRpcQuerySeek(NDRCALL):
    opnum = 12
    structure = (
		('LOGQUERY', PCONTEXT_HANDLE_LOG_QUERY),
		('POS', __INT64),
		('BOOKMARKXML', LPCWSTR),
		('TIMEOUT', DWORD),
		('FLAGS', DWORD),
    )

class EvtRpcQuerySeekResponse(NDRCALL):
    structure = (
		('ERROR', RPCINFO),
    )
        

class EvtRpcClose(NDRCALL):
    opnum = 13
    structure = (
		('HANDLE', CONTEXT_HANDLE),
    )

class EvtRpcCloseResponse(NDRCALL):
    structure = (
		('HANDLE', CONTEXT_HANDLE),
    )
        

class EvtRpcCancel(NDRCALL):
    opnum = 14
    structure = (
		('HANDLE', PCONTEXT_HANDLE_OPERATION_CONTROL),
    )

class EvtRpcCancelResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcAssertConfig(NDRCALL):
    opnum = 15
    structure = (
		('PATH', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcAssertConfigResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcRetractConfig(NDRCALL):
    opnum = 16
    structure = (
		('PATH', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcRetractConfigResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcOpenLogHandle(NDRCALL):
    opnum = 17
    structure = (
		('CHANNEL', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcOpenLogHandleResponse(NDRCALL):
    structure = (
		('HANDLE', PCONTEXT_HANDLE_LOG_HANDLE),
		('ERROR', RPCINFO),
    )
        

class EvtRpcGetLogFileInfo(NDRCALL):
    opnum = 18
    structure = (
		('LOGHANDLE', PCONTEXT_HANDLE_LOG_HANDLE),
		('PROPERTYID', DWORD),
		('PROPERTYVALUEBUFFERSIZE', DWORD),
    )

class EvtRpcGetLogFileInfoResponse(NDRCALL):
    structure = (
		('PROPERTYVALUEBUFFER', BYTE),
		('PROPERTYVALUEBUFFERLENGTH', DWORD),
    )
        

class EvtRpcGetChannelList(NDRCALL):
    opnum = 19
    structure = (
		('FLAGS', DWORD),
    )

class EvtRpcGetChannelListResponse(NDRCALL):
    structure = (
		('NUMCHANNELPATHS', DWORD),
		('CHANNELPATHS', LPWSTR),
    )
        

class EvtRpcGetChannelConfig(NDRCALL):
    opnum = 20
    structure = (
		('CHANNELPATH', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcGetChannelConfigResponse(NDRCALL):
    structure = (
		('PROPS', EVTRPCVARIANTLIST),
    )
        

class EvtRpcPutChannelConfig(NDRCALL):
    opnum = 21
    structure = (
		('CHANNELPATH', LPCWSTR),
		('FLAGS', DWORD),
		('PROPS', EVTRPCVARIANTLIST),
    )

class EvtRpcPutChannelConfigResponse(NDRCALL):
    structure = (
		('ERROR', RPCINFO),
    )
        

class EvtRpcGetPublisherList(NDRCALL):
    opnum = 22
    structure = (
		('FLAGS', DWORD),
    )

class EvtRpcGetPublisherListResponse(NDRCALL):
    structure = (
		('NUMPUBLISHERIDS', DWORD),
		('PUBLISHERIDS', LPWSTR),
    )
        

class EvtRpcGetPublisherListForChannel(NDRCALL):
    opnum = 23
    structure = (
		('CHANNELNAME', LPCWSTR),
		('FLAGS', DWORD),
    )

class EvtRpcGetPublisherListForChannelResponse(NDRCALL):
    structure = (
		('NUMPUBLISHERIDS', DWORD),
		('PUBLISHERIDS', LPWSTR),
    )
        

class EvtRpcGetPublisherMetadata(NDRCALL):
    opnum = 24
    structure = (
		('PUBLISHERID', LPCWSTR),
		('LOGFILEPATH', LPCWSTR),
		('LOCALE', LCID),
		('FLAGS', DWORD),
    )

class EvtRpcGetPublisherMetadataResponse(NDRCALL):
    structure = (
		('PUBMETADATAPROPS', EVTRPCVARIANTLIST),
		('PUBMETADATA', PCONTEXT_HANDLE_PUBLISHER_METADATA),
    )
        

class EvtRpcGetPublisherResourceMetadata(NDRCALL):
    opnum = 25
    structure = (
		('HANDLE', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('PROPERTYID', DWORD),
		('FLAGS', DWORD),
    )

class EvtRpcGetPublisherResourceMetadataResponse(NDRCALL):
    structure = (
		('PUBMETADATAPROPS', EVTRPCVARIANTLIST),
    )
        

class EvtRpcGetEventMetadataEnum(NDRCALL):
    opnum = 26
    structure = (
		('PUBMETADATA', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('FLAGS', DWORD),
		('RESERVEDFORFILTER', LPCWSTR),
    )

class EvtRpcGetEventMetadataEnumResponse(NDRCALL):
    structure = (
		('EVENTMETADATAENUM', PCONTEXT_HANDLE_EVENT_METADATA_ENUM),
    )
        

class EvtRpcGetNextEventMetadata(NDRCALL):
    opnum = 27
    structure = (
		('EVENTMETADATAENUM', PCONTEXT_HANDLE_EVENT_METADATA_ENUM),
		('FLAGS', DWORD),
		('NUMREQUESTED', DWORD),
    )

class EvtRpcGetNextEventMetadataResponse(NDRCALL):
    structure = (
		('NUMRETURNED', DWORD),
		('EVENTMETADATAINSTANCES', EVTRPCVARIANTLIST),
    )
        

class EvtRpcGetClassicLogDisplayName(NDRCALL):
    opnum = 28
    structure = (
		('LOGNAME', LPCWSTR),
		('LOCALE', LCID),
		('FLAGS', DWORD),
    )

class EvtRpcGetClassicLogDisplayNameResponse(NDRCALL):
    structure = (
		('DISPLAYNAME', LPWSTR),
    )
        
OPNUMS = {
0 : (EvtRpcRegisterRemoteSubscription,EvtRpcRegisterRemoteSubscriptionResponse),
1 : (EvtRpcRemoteSubscriptionNextAsync,EvtRpcRemoteSubscriptionNextAsyncResponse),
2 : (EvtRpcRemoteSubscriptionNext,EvtRpcRemoteSubscriptionNextResponse),
3 : (EvtRpcRemoteSubscriptionWaitAsync,EvtRpcRemoteSubscriptionWaitAsyncResponse),
4 : (EvtRpcRegisterControllableOperation,EvtRpcRegisterControllableOperationResponse),
5 : (EvtRpcRegisterLogQuery,EvtRpcRegisterLogQueryResponse),
6 : (EvtRpcClearLog,EvtRpcClearLogResponse),
7 : (EvtRpcExportLog,EvtRpcExportLogResponse),
8 : (EvtRpcLocalizeExportLog,EvtRpcLocalizeExportLogResponse),
9 : (EvtRpcMessageRender,EvtRpcMessageRenderResponse),
10 : (EvtRpcMessageRenderDefault,EvtRpcMessageRenderDefaultResponse),
11 : (EvtRpcQueryNext,EvtRpcQueryNextResponse),
12 : (EvtRpcQuerySeek,EvtRpcQuerySeekResponse),
13 : (EvtRpcClose,EvtRpcCloseResponse),
14 : (EvtRpcCancel,EvtRpcCancelResponse),
15 : (EvtRpcAssertConfig,EvtRpcAssertConfigResponse),
16 : (EvtRpcRetractConfig,EvtRpcRetractConfigResponse),
17 : (EvtRpcOpenLogHandle,EvtRpcOpenLogHandleResponse),
18 : (EvtRpcGetLogFileInfo,EvtRpcGetLogFileInfoResponse),
19 : (EvtRpcGetChannelList,EvtRpcGetChannelListResponse),
20 : (EvtRpcGetChannelConfig,EvtRpcGetChannelConfigResponse),
21 : (EvtRpcPutChannelConfig,EvtRpcPutChannelConfigResponse),
22 : (EvtRpcGetPublisherList,EvtRpcGetPublisherListResponse),
23 : (EvtRpcGetPublisherListForChannel,EvtRpcGetPublisherListForChannelResponse),
24 : (EvtRpcGetPublisherMetadata,EvtRpcGetPublisherMetadataResponse),
25 : (EvtRpcGetPublisherResourceMetadata,EvtRpcGetPublisherResourceMetadataResponse),
26 : (EvtRpcGetEventMetadataEnum,EvtRpcGetEventMetadataEnumResponse),
27 : (EvtRpcGetNextEventMetadata,EvtRpcGetNextEventMetadataResponse),
28 : (EvtRpcGetClassicLogDisplayName,EvtRpcGetClassicLogDisplayNameResponse),
}

