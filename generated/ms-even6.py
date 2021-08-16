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
DWORD__ENUM = DWORD
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
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
CONST_UNSIGNED_LONG = NDRULONG
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER

#################################################################################
#"ms-dtyp.idl"
#################################################################################
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
	align = 1
	structure = (
			(
			'dwLowDateTime',
			DWORD
			),
			(
			'dwHighDateTime',
			DWORD
			)
		)


class PFILETIME(NDRPOINTER):
	referent = (
			(
			'Data',
			FILETIME
			)
		)


class LPFILETIME(NDRPOINTER):
	referent = (
			(
			'Data',
			FILETIME
			)
		)


class GUID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Data1',
			UNSIGNED_LONG
			),
			(
			'Data2',
			UNSIGNED_SHORT
			),
			(
			'Data3',
			UNSIGNED_SHORT
			),
			(
			'Data4',
			BYTE
			)
		)


UUID = GUID
class PGUID(NDRPOINTER):
	referent = (
			(
			'Data',
			GUID
			)
		)


class LARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'QuadPart',
			SIGNED___INT64
			)
		)


class PLARGE_INTEGER(NDRPOINTER):
	referent = (
			(
			'Data',
			LARGE_INTEGER
			)
		)


class EVENT_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Id',
			USHORT
			),
			(
			'Version',
			UCHAR
			),
			(
			'Channel',
			UCHAR
			),
			(
			'Level',
			UCHAR
			),
			(
			'Opcode',
			UCHAR
			),
			(
			'Task',
			USHORT
			),
			(
			'Keyword',
			ULONGLONG
			)
		)


class PEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_DESCRIPTOR
			)
		)


class PCEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_DESCRIPTOR
			)
		)


class S0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'KernelTime',
			ULONG
			),
			(
			'UserTime',
			ULONG
			)
		)


class U0(NDRUNION):
	union = {1 : (
		's0',
		S0
		),2 : (
		'ProcessorTime',
		ULONG64
		)}


class EVENT_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			USHORT
			),
			(
			'HeaderType',
			USHORT
			),
			(
			'Flags',
			USHORT
			),
			(
			'EventProperty',
			USHORT
			),
			(
			'ThreadId',
			ULONG
			),
			(
			'ProcessId',
			ULONG
			),
			(
			'TimeStamp',
			LARGE_INTEGER
			),
			(
			'ProviderId',
			GUID
			),
			(
			'EventDescriptor',
			EVENT_DESCRIPTOR
			),
			(
			'u0',
			U0
			),
			(
			'ActivityId',
			GUID
			)
		)


class PEVENT_HEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_HEADER
			)
		)


LCID = DWORD
class LUID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LowPart',
			DWORD
			),
			(
			'HighPart',
			LONG
			)
		)


class PLUID(NDRPOINTER):
	referent = (
			(
			'Data',
			LUID
			)
		)


class MULTI_SZ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Value',
			WCHAR_T
			),
			(
			'nChar',
			DWORD
			)
		)


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
	item = WCHAR


class PTR_RPC_UNICODE_STRING(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_UNICODE_STRING
			)
		)


class RPC_UNICODE_STRING(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_SHORT
			),
			(
			'MaximumLength',
			UNSIGNED_SHORT
			),
			(
			'Buffer',
			PTR_RPC_UNICODE_STRING
			)
		)


class SERVER_INFO_100(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv100_platform_id',
			DWORD
			),
			(
			'sv100_name',
			WCHAR_T
			)
		)


class PSERVER_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_100
			)
		)


class LPSERVER_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_100
			)
		)


class SERVER_INFO_101(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv101_platform_id',
			DWORD
			),
			(
			'sv101_name',
			WCHAR_T
			),
			(
			'sv101_version_major',
			DWORD
			),
			(
			'sv101_version_minor',
			DWORD
			),
			(
			'sv101_version_type',
			DWORD
			),
			(
			'sv101_comment',
			WCHAR_T
			)
		)


class PSERVER_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_101
			)
		)


class LPSERVER_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_101
			)
		)


class SYSTEMTIME(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wYear',
			WORD
			),
			(
			'wMonth',
			WORD
			),
			(
			'wDayOfWeek',
			WORD
			),
			(
			'wDay',
			WORD
			),
			(
			'wHour',
			WORD
			),
			(
			'wMinute',
			WORD
			),
			(
			'wSecond',
			WORD
			),
			(
			'wMilliseconds',
			WORD
			)
		)


class PSYSTEMTIME(NDRPOINTER):
	referent = (
			(
			'Data',
			SYSTEMTIME
			)
		)


class UINT128(NDRSTRUCT):
	align = 1
	structure = (
			(
			'lower',
			UINT64
			),
			(
			'upper',
			UINT64
			)
		)


class PUINT128(NDRPOINTER):
	referent = (
			(
			'Data',
			UINT128
			)
		)


class ULARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'QuadPart',
			UNSIGNED___INT64
			)
		)


class PULARGE_INTEGER(NDRPOINTER):
	referent = (
			(
			'Data',
			ULARGE_INTEGER
			)
		)


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Value',
			BYTE
			)
		)


ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK
class OBJECT_TYPE_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			WORD
			),
			(
			'Remaining',
			ACCESS_MASK
			),
			(
			'ObjectType',
			GUID
			)
		)


class POBJECT_TYPE_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			OBJECT_TYPE_LIST
			)
		)


class ACE_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AceType',
			UCHAR
			),
			(
			'AceFlags',
			UCHAR
			),
			(
			'AceSize',
			USHORT
			)
		)


class PACE_HEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			ACE_HEADER
			)
		)


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Header',
			ACE_HEADER
			),
			(
			'Mask',
			ACCESS_MASK
			),
			(
			'SidStart',
			DWORD
			)
		)


class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
	referent = (
			(
			'Data',
			SYSTEM_MANDATORY_LABEL_ACE
			)
		)


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Policy',
			DWORD
			)
		)


class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
	referent = (
			(
			'Data',
			TOKEN_MANDATORY_POLICY
			)
		)


class MANDATORY_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AllowedAccess',
			ACCESS_MASK
			),
			(
			'WriteAllowed',
			BOOLEAN
			),
			(
			'ReadAllowed',
			BOOLEAN
			),
			(
			'ExecuteAllowed',
			BOOLEAN
			),
			(
			'MandatoryPolicy',
			TOKEN_MANDATORY_POLICY
			)
		)


class PMANDATORY_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			MANDATORY_INFORMATION
			)
		)


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			DWORD
			),
			(
			'OctetString',
			BYTE
			)
		)


class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
	referent = (
			(
			'Data',
			CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE
			)
		)


class VALUES(NDRUNION):
	union = {1 : (
		'pInt64',
		PLONG64
		),2 : (
		'pUint64',
		PDWORD64
		),3 : (
		'ppString',
		PWSTR
		),4 : (
		'pOctetString',
		PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE
		)}


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			DWORD
			),
			(
			'ValueType',
			WORD
			),
			(
			'Reserved',
			WORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'ValueCount',
			DWORD
			),
			(
			'Values',
			VALUES
			)
		)


class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
	referent = (
			(
			'Data',
			CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
			)
		)


SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD
class RPC_SID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Revision',
			UNSIGNED_CHAR
			),
			(
			'SubAuthorityCount',
			UNSIGNED_CHAR
			),
			(
			'IdentifierAuthority',
			RPC_SID_IDENTIFIER_AUTHORITY
			),
			(
			'SubAuthority',
			UNSIGNED_LONG
			)
		)


class PRPC_SID(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_SID
			)
		)


class PSID(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_SID
			)
		)


class ACL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AclRevision',
			UNSIGNED_CHAR
			),
			(
			'Sbz1',
			UNSIGNED_CHAR
			),
			(
			'AclSize',
			UNSIGNED_SHORT
			),
			(
			'AceCount',
			UNSIGNED_SHORT
			),
			(
			'Sbz2',
			UNSIGNED_SHORT
			)
		)


class PACL(NDRPOINTER):
	referent = (
			(
			'Data',
			ACL
			)
		)


class SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Revision',
			UCHAR
			),
			(
			'Sbz1',
			UCHAR
			),
			(
			'Control',
			USHORT
			),
			(
			'Owner',
			PSID
			),
			(
			'Group',
			PSID
			),
			(
			'Sacl',
			PACL
			),
			(
			'Dacl',
			PACL
			)
		)


class PSECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			SECURITY_DESCRIPTOR
			)
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
MSRPC_UUID_IEVENTSERVICE = uuidtup_to_bin(('f6beaff7-119-4bb-98-b89e2018337c','0.0'))
PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION = VOID
PCONTEXT_HANDLE_LOG_QUERY = VOID
PCONTEXT_HANDLE_LOG_HANDLE = VOID
PCONTEXT_HANDLE_OPERATION_CONTROL = VOID
PCONTEXT_HANDLE_PUBLISHER_METADATA = VOID
PCONTEXT_HANDLE_EVENT_METADATA_ENUM = VOID
class RPCINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_error',
			DWORD
			),
			(
			'm_subErr',
			DWORD
			),
			(
			'm_subErrParam',
			DWORD
			)
		)


class DATA_BOOLEANARRAY(NDRUniConformantArray):
	item = BOOLEAN


class PTR_BOOLEANARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_BOOLEANARRAY
			)
		)


class BOOLEANARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'ptr',
			PTR_BOOLEANARRAY
			)
		)


class DATA_UINT32ARRAY(NDRUniConformantArray):
	item = DWORD


class PTR_UINT32ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_UINT32ARRAY
			)
		)


class UINT32ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'ptr',
			PTR_UINT32ARRAY
			)
		)


class DATA_UINT64ARRAY(NDRUniConformantArray):
	item = DWORD64


class PTR_UINT64ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_UINT64ARRAY
			)
		)


class UINT64ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'ptr',
			PTR_UINT64ARRAY
			)
		)


class DATA_STRINGARRAY(NDRUniConformantArray):
	item = LPWSTR


class PTR_STRINGARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_STRINGARRAY
			)
		)


class STRINGARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'ptr',
			PTR_STRINGARRAY
			)
		)


class DATA_GUIDARRAY(NDRUniConformantArray):
	item = GUID


class PTR_GUIDARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_GUIDARRAY
			)
		)


class GUIDARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'ptr',
			PTR_GUIDARRAY
			)
		)


EvtRpcVariantType = DWORD__ENUM
EvtRpcVarTypeNull = 0
EvtRpcVarTypeBoolean = 0
EvtRpcVarTypeUInt32 = 0
EvtRpcVarTypeUInt64 = 0
EvtRpcVarTypeString = 0
EvtRpcVarTypeGuid = 0
EvtRpcVarTypeBooleanArray = 0
EvtRpcVarTypeUInt32Array = 0
EvtRpcVarTypeUInt64Array = 0
EvtRpcVarTypeStringArray = 0
EvtRpcAssertConfigFlags = DWORD__ENUM
EvtRpcChannelPath = 0
EvtRpcPublisherName = 1
class U0(NDRUNION):
	union = {EvtRpcVarTypeNull : (
		'nullVal',
		INT
		),EvtRpcVarTypeBoolean : (
		'booleanVal',
		BOOLEAN
		),EvtRpcVarTypeUInt32 : (
		'uint32Val',
		DWORD
		),EvtRpcVarTypeUInt64 : (
		'uint64Val',
		DWORD64
		),EvtRpcVarTypeString : (
		'stringVal',
		LPWSTR
		),EvtRpcVarTypeGuid : (
		'guidVal',
		GUID
		),EvtRpcVarTypeBooleanArray : (
		'booleanArray',
		BOOLEANARRAY
		),EvtRpcVarTypeUInt32Array : (
		'uint32Array',
		UINT32ARRAY
		),EvtRpcVarTypeUInt64Array : (
		'uint64Array',
		UINT64ARRAY
		),EvtRpcVarTypeStringArray : (
		'stringArray',
		STRINGARRAY
		),EvtRpcVarTypeGuidArray : (
		'guidArray',
		GUIDARRAY
		)}


class EVTRPCVARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'type',
			EVTRPCVARIANTTYPE
			),
			(
			'flags',
			DWORD
			),
			(
			'u0',
			U0
			)
		)


class DATA_EVTRPCVARIANTLIST(NDRUniConformantArray):
	item = EVTRPCVARIANT


class PTR_EVTRPCVARIANTLIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_EVTRPCVARIANTLIST
			)
		)


class EVTRPCVARIANTLIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'count',
			DWORD
			),
			(
			'props',
			PTR_EVTRPCVARIANTLIST
			)
		)


class EVTRPCQUERYCHANNELINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'name',
			LPWSTR
			),
			(
			'status',
			DWORD
			)
		)


class EvtRpcRegisterRemoteSubscription(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'bookmarkXml',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRegisterRemoteSubscriptionResponse(NDRCALL):
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'bookmarkXml',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRemoteSubscriptionNextAsync(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRemoteSubscriptionNextAsyncResponse(NDRCALL):
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRemoteSubscriptionNext(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'timeOut',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRemoteSubscriptionNextResponse(NDRCALL):
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'timeOut',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRemoteSubscriptionWaitAsync(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			)
		)


class EvtRpcRemoteSubscriptionWaitAsyncResponse(NDRCALL):
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION
			)
		)


class EvtRpcRegisterControllableOperation(NDRCALL):
	OPNUM = 4
	structure = (

		)


class EvtRpcRegisterControllableOperationResponse(NDRCALL):
	structure = (

		)


class EvtRpcRegisterLogQuery(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRegisterLogQueryResponse(NDRCALL):
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcClearLog(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'channelPath',
			LPCWSTR
			),
			(
			'backupPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcClearLogResponse(NDRCALL):
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'channelPath',
			LPCWSTR
			),
			(
			'backupPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcExportLog(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'channelPath',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'backupPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcExportLogResponse(NDRCALL):
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'channelPath',
			LPCWSTR
			),
			(
			'query',
			LPCWSTR
			),
			(
			'backupPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcLocalizeExportLog(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'logFilePath',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcLocalizeExportLogResponse(NDRCALL):
	structure = (
			(
			'control',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			),
			(
			'logFilePath',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcMessageRender(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'pubCfgObj',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'sizeEventId',
			DWORD
			),
			(
			'eventId',
			BYTE
			),
			(
			'messageId',
			DWORD
			),
			(
			'values',
			EVTRPCVARIANTLIST
			),
			(
			'flags',
			DWORD
			),
			(
			'maxSizeString',
			DWORD
			)
		)


class EvtRpcMessageRenderResponse(NDRCALL):
	structure = (
			(
			'pubCfgObj',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'sizeEventId',
			DWORD
			),
			(
			'eventId',
			BYTE
			),
			(
			'messageId',
			DWORD
			),
			(
			'values',
			EVTRPCVARIANTLIST
			),
			(
			'flags',
			DWORD
			),
			(
			'maxSizeString',
			DWORD
			)
		)


class EvtRpcMessageRenderDefault(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'sizeEventId',
			DWORD
			),
			(
			'eventId',
			BYTE
			),
			(
			'messageId',
			DWORD
			),
			(
			'values',
			EVTRPCVARIANTLIST
			),
			(
			'flags',
			DWORD
			),
			(
			'maxSizeString',
			DWORD
			)
		)


class EvtRpcMessageRenderDefaultResponse(NDRCALL):
	structure = (
			(
			'sizeEventId',
			DWORD
			),
			(
			'eventId',
			BYTE
			),
			(
			'messageId',
			DWORD
			),
			(
			'values',
			EVTRPCVARIANTLIST
			),
			(
			'flags',
			DWORD
			),
			(
			'maxSizeString',
			DWORD
			)
		)


class EvtRpcQueryNext(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'logQuery',
			PCONTEXT_HANDLE_LOG_QUERY
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'timeOutEnd',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcQueryNextResponse(NDRCALL):
	structure = (
			(
			'logQuery',
			PCONTEXT_HANDLE_LOG_QUERY
			),
			(
			'numRequestedRecords',
			DWORD
			),
			(
			'timeOutEnd',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcQuerySeek(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'logQuery',
			PCONTEXT_HANDLE_LOG_QUERY
			),
			(
			'pos',
			__INT64
			),
			(
			'bookmarkXml',
			LPCWSTR
			),
			(
			'timeOut',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcQuerySeekResponse(NDRCALL):
	structure = (
			(
			'logQuery',
			PCONTEXT_HANDLE_LOG_QUERY
			),
			(
			'pos',
			__INT64
			),
			(
			'bookmarkXml',
			LPCWSTR
			),
			(
			'timeOut',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcClose(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'handle',
			CONTEXT_HANDLE
			)
		)


class EvtRpcCloseResponse(NDRCALL):
	structure = (
			(
			'handle',
			CONTEXT_HANDLE
			)
		)


class EvtRpcCancel(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			)
		)


class EvtRpcCancelResponse(NDRCALL):
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_OPERATION_CONTROL
			)
		)


class EvtRpcAssertConfig(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcAssertConfigResponse(NDRCALL):
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRetractConfig(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcRetractConfigResponse(NDRCALL):
	structure = (
			(
			'path',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcOpenLogHandle(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'channel',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcOpenLogHandleResponse(NDRCALL):
	structure = (
			(
			'channel',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetLogFileInfo(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'logHandle',
			PCONTEXT_HANDLE_LOG_HANDLE
			),
			(
			'propertyId',
			DWORD
			),
			(
			'propertyValueBufferSize',
			DWORD
			)
		)


class EvtRpcGetLogFileInfoResponse(NDRCALL):
	structure = (
			(
			'logHandle',
			PCONTEXT_HANDLE_LOG_HANDLE
			),
			(
			'propertyId',
			DWORD
			),
			(
			'propertyValueBufferSize',
			DWORD
			)
		)


class EvtRpcGetChannelList(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetChannelListResponse(NDRCALL):
	structure = (
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetChannelConfig(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetChannelConfigResponse(NDRCALL):
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcPutChannelConfig(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			),
			(
			'props',
			EVTRPCVARIANTLIST
			)
		)


class EvtRpcPutChannelConfigResponse(NDRCALL):
	structure = (
			(
			'channelPath',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			),
			(
			'props',
			EVTRPCVARIANTLIST
			)
		)


class EvtRpcGetPublisherList(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherListResponse(NDRCALL):
	structure = (
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherListForChannel(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'channelName',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherListForChannelResponse(NDRCALL):
	structure = (
			(
			'channelName',
			LPCWSTR
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherMetadata(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'publisherId',
			LPCWSTR
			),
			(
			'logFilePath',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherMetadataResponse(NDRCALL):
	structure = (
			(
			'publisherId',
			LPCWSTR
			),
			(
			'logFilePath',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherResourceMetadata(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'propertyId',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetPublisherResourceMetadataResponse(NDRCALL):
	structure = (
			(
			'handle',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'propertyId',
			DWORD
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetEventMetadataEnum(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'pubMetadata',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'flags',
			DWORD
			),
			(
			'reservedForFilter',
			LPCWSTR
			)
		)


class EvtRpcGetEventMetadataEnumResponse(NDRCALL):
	structure = (
			(
			'pubMetadata',
			PCONTEXT_HANDLE_PUBLISHER_METADATA
			),
			(
			'flags',
			DWORD
			),
			(
			'reservedForFilter',
			LPCWSTR
			)
		)


class EvtRpcGetNextEventMetadata(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'eventMetaDataEnum',
			PCONTEXT_HANDLE_EVENT_METADATA_ENUM
			),
			(
			'flags',
			DWORD
			),
			(
			'numRequested',
			DWORD
			)
		)


class EvtRpcGetNextEventMetadataResponse(NDRCALL):
	structure = (
			(
			'eventMetaDataEnum',
			PCONTEXT_HANDLE_EVENT_METADATA_ENUM
			),
			(
			'flags',
			DWORD
			),
			(
			'numRequested',
			DWORD
			)
		)


class EvtRpcGetClassicLogDisplayName(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'logName',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


class EvtRpcGetClassicLogDisplayNameResponse(NDRCALL):
	structure = (
			(
			'logName',
			LPCWSTR
			),
			(
			'locale',
			LCID
			),
			(
			'flags',
			DWORD
			)
		)


OPNUMS = {0 : (
	EvtRpcRegisterRemoteSubscription,
	EvtRpcRegisterRemoteSubscriptionResponse
	),1 : (
	EvtRpcRemoteSubscriptionNextAsync,
	EvtRpcRemoteSubscriptionNextAsyncResponse
	),2 : (
	EvtRpcRemoteSubscriptionNext,
	EvtRpcRemoteSubscriptionNextResponse
	),3 : (
	EvtRpcRemoteSubscriptionWaitAsync,
	EvtRpcRemoteSubscriptionWaitAsyncResponse
	),4 : (
	EvtRpcRegisterControllableOperation,
	EvtRpcRegisterControllableOperationResponse
	),5 : (
	EvtRpcRegisterLogQuery,
	EvtRpcRegisterLogQueryResponse
	),6 : (
	EvtRpcClearLog,
	EvtRpcClearLogResponse
	),7 : (
	EvtRpcExportLog,
	EvtRpcExportLogResponse
	),8 : (
	EvtRpcLocalizeExportLog,
	EvtRpcLocalizeExportLogResponse
	),9 : (
	EvtRpcMessageRender,
	EvtRpcMessageRenderResponse
	),10 : (
	EvtRpcMessageRenderDefault,
	EvtRpcMessageRenderDefaultResponse
	),11 : (
	EvtRpcQueryNext,
	EvtRpcQueryNextResponse
	),12 : (
	EvtRpcQuerySeek,
	EvtRpcQuerySeekResponse
	),13 : (
	EvtRpcClose,
	EvtRpcCloseResponse
	),14 : (
	EvtRpcCancel,
	EvtRpcCancelResponse
	),15 : (
	EvtRpcAssertConfig,
	EvtRpcAssertConfigResponse
	),16 : (
	EvtRpcRetractConfig,
	EvtRpcRetractConfigResponse
	),17 : (
	EvtRpcOpenLogHandle,
	EvtRpcOpenLogHandleResponse
	),18 : (
	EvtRpcGetLogFileInfo,
	EvtRpcGetLogFileInfoResponse
	),19 : (
	EvtRpcGetChannelList,
	EvtRpcGetChannelListResponse
	),20 : (
	EvtRpcGetChannelConfig,
	EvtRpcGetChannelConfigResponse
	),21 : (
	EvtRpcPutChannelConfig,
	EvtRpcPutChannelConfigResponse
	),22 : (
	EvtRpcGetPublisherList,
	EvtRpcGetPublisherListResponse
	),23 : (
	EvtRpcGetPublisherListForChannel,
	EvtRpcGetPublisherListForChannelResponse
	),24 : (
	EvtRpcGetPublisherMetadata,
	EvtRpcGetPublisherMetadataResponse
	),25 : (
	EvtRpcGetPublisherResourceMetadata,
	EvtRpcGetPublisherResourceMetadataResponse
	),26 : (
	EvtRpcGetEventMetadataEnum,
	EvtRpcGetEventMetadataEnumResponse
	),27 : (
	EvtRpcGetNextEventMetadata,
	EvtRpcGetNextEventMetadataResponse
	),28 : (
	EvtRpcGetClassicLogDisplayName,
	EvtRpcGetClassicLogDisplayNameResponse
	)}
