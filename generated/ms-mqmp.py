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
#"ms-mqmq.idl"
#################################################################################
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
PROPVARIANT = TAG_INNER_PROPVARIANT
PROPID = UNSIGNED_LONG
VARIANT_BOOL = SHORT
class XACTUOW(NDRSTRUCT):
	align = 1
	structure = (
			(
			'rgb',
			UNSIGNED_CHAR
			)
		)


class DATA_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_BLOB
			)
		)


class BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbSize',
			UNSIGNED_LONG
			),
			(
			'pBlobData',
			PTR_BLOB
			)
		)


class DATA_CAUB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_CAUB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUB
			)
		)


class CAUB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUB
			)
		)


class DATA_CAUI(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_CAUI(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUI
			)
		)


class CAUI(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUI
			)
		)


class DATA_CAL(NDRUniConformantArray):
	item = LONG


class PTR_CAL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAL
			)
		)


class CAL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAL
			)
		)


class DATA_CAUL(NDRUniConformantArray):
	item = UNSIGNED_LONG


class PTR_CAUL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUL
			)
		)


class CAUL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUL
			)
		)


class DATA_CAUH(NDRUniConformantArray):
	item = ULARGE_INTEGER


class PTR_CAUH(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUH
			)
		)


class CAUH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUH
			)
		)


class DATA_CACLSID(NDRUniConformantArray):
	item = GUID


class PTR_CACLSID(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CACLSID
			)
		)


class CACLSID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CACLSID
			)
		)


class DATA_CALPWSTR(NDRUniConformantArray):
	item = WCHAR_T


class PTR_CALPWSTR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CALPWSTR
			)
		)


class CALPWSTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CALPWSTR
			)
		)


class DATA_CAPROPVARIANT(NDRUniConformantArray):
	item = PROPVARIANT


class PTR_CAPROPVARIANT(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAPROPVARIANT
			)
		)


class CAPROPVARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAPROPVARIANT
			)
		)


VARENUM = DWORD__ENUM
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_BOOL = 11
VT_VARIANT = 12
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_LPWSTR = 31
VT_BLOB = 65
VT_CLSID = 72
VT_VECTOR = 4096
VARTYPE = UNSIGNED_SHORT
class _VARUNION(NDRUNION):
	union = {VT_I1 : (
		'cVal',
		CHAR
		),VT_UI1 : (
		'bVal',
		UCHAR
		),VT_I2 : (
		'iVal',
		SHORT
		),VT_UI2 : (
		'uiVal',
		USHORT
		),VT_I4 : (
		'lVal',
		LONG
		),VT_UI4 : (
		'ulVal',
		ULONG
		),VT_I8 : (
		'hVal',
		LARGE_INTEGER
		),VT_UI8 : (
		'uhVal',
		ULARGE_INTEGER
		),VT_BOOL : (
		'boolVal',
		VARIANT_BOOL
		),VT_CLSID : (
		'puuid',
		GUID
		),VT_BLOB : (
		'blob',
		BLOB
		),VT_LPWSTR : (
		'pwszVal',
		WCHAR_T
		),VT_VECTOR|VT_UI1 : (
		'caub',
		CAUB
		),VT_VECTOR|VT_UI2 : (
		'caui',
		CAUI
		),VT_VECTOR|VT_I4 : (
		'cal',
		CAL
		),VT_VECTOR|VT_UI4 : (
		'caul',
		CAUL
		),VT_VECTOR|VT_UI8 : (
		'cauh',
		CAUH
		),VT_VECTOR|VT_CLSID : (
		'cauuid',
		CACLSID
		),VT_VECTOR|VT_LPWSTR : (
		'calpwstr',
		CALPWSTR
		),VT_VECTOR|VT_VARIANT : (
		'capropvar',
		CAPROPVARIANT
		)}


class TAG_INNER_PROPVARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'vt',
			VARTYPE
			),
			(
			'wReserved1',
			UCHAR
			),
			(
			'wReserved2',
			UCHAR
			),
			(
			'wReserved3',
			ULONG
			),
			(
			'_varUnion',
			_VARUNION
			)
		)


class DL_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_DlGuid',
			GUID
			),
			(
			'm_pwzDomain',
			WCHAR_T
			)
		)


class MULTICAST_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_address',
			ULONG
			),
			(
			'm_port',
			ULONG
			)
		)


class OBJECTID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Lineage',
			GUID
			),
			(
			'Uniquifier',
			DWORD
			)
		)


QUEUE_FORMAT_TYPE = DWORD__ENUM
QUEUE_FORMAT_TYPE_UNKNOWN = 0
QUEUE_FORMAT_TYPE_PUBLIC = 1
QUEUE_FORMAT_TYPE_PRIVATE = 2
QUEUE_FORMAT_TYPE_DIRECT = 3
QUEUE_FORMAT_TYPE_MACHINE = 4
QUEUE_FORMAT_TYPE_CONNECTOR = 5
QUEUE_FORMAT_TYPE_DL = 6
QUEUE_FORMAT_TYPE_MULTICAST = 7
QUEUE_FORMAT_TYPE_SUBQUEUE = 8
class U0(NDRUNION):
	union = {QUEUE_FORMAT_TYPE_PUBLIC : (
		'm_gPublicID',
		GUID
		),QUEUE_FORMAT_TYPE_PRIVATE : (
		'm_oPrivateID',
		OBJECTID
		),QUEUE_FORMAT_TYPE_DIRECT : (
		'm_pDirectID',
		WCHAR_T
		),QUEUE_FORMAT_TYPE_MACHINE : (
		'm_gMachineID',
		GUID
		),QUEUE_FORMAT_TYPE_CONNECTOR : (
		'm_GConnectorID',
		GUID
		),QUEUE_FORMAT_TYPE_DL : (
		'm_DlID',
		DL_ID
		),QUEUE_FORMAT_TYPE_MULTICAST : (
		'm_MulticastID',
		MULTICAST_ID
		),QUEUE_FORMAT_TYPE_SUBQUEUE : (
		'm_pDirectSubqueueID',
		WCHAR_T
		)}


class QUEUE_FORMAT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_qft',
			UNSIGNED_CHAR
			),
			(
			'm_SuffixAndFlags',
			UNSIGNED_CHAR
			),
			(
			'm_reserved',
			UNSIGNED_SHORT
			),
			(
			'u0',
			U0
			)
		)


#################################################################################
#"ms-mqrr.idl"
#################################################################################
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
#"ms-mqmq.idl"
#################################################################################
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
PROPVARIANT = TAG_INNER_PROPVARIANT
PROPID = UNSIGNED_LONG
VARIANT_BOOL = SHORT
class XACTUOW(NDRSTRUCT):
	align = 1
	structure = (
			(
			'rgb',
			UNSIGNED_CHAR
			)
		)


class DATA_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_BLOB
			)
		)


class BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbSize',
			UNSIGNED_LONG
			),
			(
			'pBlobData',
			PTR_BLOB
			)
		)


class DATA_CAUB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_CAUB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUB
			)
		)


class CAUB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUB
			)
		)


class DATA_CAUI(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_CAUI(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUI
			)
		)


class CAUI(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUI
			)
		)


class DATA_CAL(NDRUniConformantArray):
	item = LONG


class PTR_CAL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAL
			)
		)


class CAL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAL
			)
		)


class DATA_CAUL(NDRUniConformantArray):
	item = UNSIGNED_LONG


class PTR_CAUL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUL
			)
		)


class CAUL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUL
			)
		)


class DATA_CAUH(NDRUniConformantArray):
	item = ULARGE_INTEGER


class PTR_CAUH(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAUH
			)
		)


class CAUH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAUH
			)
		)


class DATA_CACLSID(NDRUniConformantArray):
	item = GUID


class PTR_CACLSID(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CACLSID
			)
		)


class CACLSID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CACLSID
			)
		)


class DATA_CALPWSTR(NDRUniConformantArray):
	item = WCHAR_T


class PTR_CALPWSTR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CALPWSTR
			)
		)


class CALPWSTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CALPWSTR
			)
		)


class DATA_CAPROPVARIANT(NDRUniConformantArray):
	item = PROPVARIANT


class PTR_CAPROPVARIANT(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CAPROPVARIANT
			)
		)


class CAPROPVARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElems',
			UNSIGNED_LONG
			),
			(
			'pElems',
			PTR_CAPROPVARIANT
			)
		)


VARENUM = DWORD__ENUM
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_BOOL = 11
VT_VARIANT = 12
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_LPWSTR = 31
VT_BLOB = 65
VT_CLSID = 72
VT_VECTOR = 4096
VARTYPE = UNSIGNED_SHORT
class _VARUNION(NDRUNION):
	union = {VT_I1 : (
		'cVal',
		CHAR
		),VT_UI1 : (
		'bVal',
		UCHAR
		),VT_I2 : (
		'iVal',
		SHORT
		),VT_UI2 : (
		'uiVal',
		USHORT
		),VT_I4 : (
		'lVal',
		LONG
		),VT_UI4 : (
		'ulVal',
		ULONG
		),VT_I8 : (
		'hVal',
		LARGE_INTEGER
		),VT_UI8 : (
		'uhVal',
		ULARGE_INTEGER
		),VT_BOOL : (
		'boolVal',
		VARIANT_BOOL
		),VT_CLSID : (
		'puuid',
		GUID
		),VT_BLOB : (
		'blob',
		BLOB
		),VT_LPWSTR : (
		'pwszVal',
		WCHAR_T
		),VT_VECTOR|VT_UI1 : (
		'caub',
		CAUB
		),VT_VECTOR|VT_UI2 : (
		'caui',
		CAUI
		),VT_VECTOR|VT_I4 : (
		'cal',
		CAL
		),VT_VECTOR|VT_UI4 : (
		'caul',
		CAUL
		),VT_VECTOR|VT_UI8 : (
		'cauh',
		CAUH
		),VT_VECTOR|VT_CLSID : (
		'cauuid',
		CACLSID
		),VT_VECTOR|VT_LPWSTR : (
		'calpwstr',
		CALPWSTR
		),VT_VECTOR|VT_VARIANT : (
		'capropvar',
		CAPROPVARIANT
		)}


class TAG_INNER_PROPVARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'vt',
			VARTYPE
			),
			(
			'wReserved1',
			UCHAR
			),
			(
			'wReserved2',
			UCHAR
			),
			(
			'wReserved3',
			ULONG
			),
			(
			'_varUnion',
			_VARUNION
			)
		)


class DL_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_DlGuid',
			GUID
			),
			(
			'm_pwzDomain',
			WCHAR_T
			)
		)


class MULTICAST_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_address',
			ULONG
			),
			(
			'm_port',
			ULONG
			)
		)


class OBJECTID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Lineage',
			GUID
			),
			(
			'Uniquifier',
			DWORD
			)
		)


QUEUE_FORMAT_TYPE = DWORD__ENUM
QUEUE_FORMAT_TYPE_UNKNOWN = 0
QUEUE_FORMAT_TYPE_PUBLIC = 1
QUEUE_FORMAT_TYPE_PRIVATE = 2
QUEUE_FORMAT_TYPE_DIRECT = 3
QUEUE_FORMAT_TYPE_MACHINE = 4
QUEUE_FORMAT_TYPE_CONNECTOR = 5
QUEUE_FORMAT_TYPE_DL = 6
QUEUE_FORMAT_TYPE_MULTICAST = 7
QUEUE_FORMAT_TYPE_SUBQUEUE = 8
class U0(NDRUNION):
	union = {QUEUE_FORMAT_TYPE_PUBLIC : (
		'm_gPublicID',
		GUID
		),QUEUE_FORMAT_TYPE_PRIVATE : (
		'm_oPrivateID',
		OBJECTID
		),QUEUE_FORMAT_TYPE_DIRECT : (
		'm_pDirectID',
		WCHAR_T
		),QUEUE_FORMAT_TYPE_MACHINE : (
		'm_gMachineID',
		GUID
		),QUEUE_FORMAT_TYPE_CONNECTOR : (
		'm_GConnectorID',
		GUID
		),QUEUE_FORMAT_TYPE_DL : (
		'm_DlID',
		DL_ID
		),QUEUE_FORMAT_TYPE_MULTICAST : (
		'm_MulticastID',
		MULTICAST_ID
		),QUEUE_FORMAT_TYPE_SUBQUEUE : (
		'm_pDirectSubqueueID',
		WCHAR_T
		)}


class QUEUE_FORMAT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'm_qft',
			UNSIGNED_CHAR
			),
			(
			'm_SuffixAndFlags',
			UNSIGNED_CHAR
			),
			(
			'm_reserved',
			UNSIGNED_SHORT
			),
			(
			'u0',
			U0
			)
		)


#################################################################################
#TYPEDEFS
#################################################################################
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#RemoteRead Definition
#################################################################################
MSRPC_UUID_REMOTEREAD = uuidtup_to_bin(('1a9134dd-7b39-45ba-ad88-44d01ca47f28','0.0'))
QUEUE_CONTEXT_HANDLE_NOSERIALIZE = VOID
QUEUE_CONTEXT_HANDLE_SERIALIZE = QUEUE_CONTEXT_HANDLE_NOSERIALIZE
SectionType = DWORD__ENUM
stFullPacket = 0
stBinaryFirstSection = 1
stBinarySecondSection = 2
stSrmpFirstSection = 3
stSrmpSecondSection = 4
class DATA_SECTIONBUFFER(NDRUniConformantArray):
	item = BYTE


class PTR_SECTIONBUFFER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SECTIONBUFFER
			)
		)


class SECTIONBUFFER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SectionBufferType',
			SECTIONTYPE
			),
			(
			'SectionSizeAlloc',
			DWORD
			),
			(
			'SectionSize',
			DWORD
			),
			(
			'pSectionBuffer',
			PTR_SECTIONBUFFER
			)
		)


class R_GetServerPort(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'hBind',
			HANDLE_T
			)
		)


class R_GetServerPortResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			)
		)


class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (

		)


class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class R_OpenQueue(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pClientId',
			GUID
			),
			(
			'fNonRoutingServer',
			LONG
			),
			(
			'Major',
			UNSIGNED_CHAR
			),
			(
			'Minor',
			UNSIGNED_CHAR
			),
			(
			'BuildNumber',
			USHORT
			),
			(
			'fWorkgroup',
			LONG
			)
		)


class R_OpenQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pClientId',
			GUID
			),
			(
			'fNonRoutingServer',
			LONG
			),
			(
			'Major',
			UNSIGNED_CHAR
			),
			(
			'Minor',
			UNSIGNED_CHAR
			),
			(
			'BuildNumber',
			USHORT
			),
			(
			'fWorkgroup',
			LONG
			)
		)


class R_CloseQueue(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			QUEUE_CONTEXT_HANDLE_SERIALIZE
			)
		)


class R_CloseQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			QUEUE_CONTEXT_HANDLE_SERIALIZE
			)
		)


class R_CreateCursor(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class R_CreateCursorResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class R_CloseCursor(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'hCursor',
			DWORD
			)
		)


class R_CloseCursorResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'hCursor',
			DWORD
			)
		)


class R_PurgeQueue(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class R_PurgeQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class R_StartReceive(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'hCursor',
			DWORD
			),
			(
			'ulAction',
			DWORD
			),
			(
			'ulTimeout',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			),
			(
			'dwMaxBodySize',
			DWORD
			),
			(
			'dwMaxCompoundMessageSize',
			DWORD
			)
		)


class R_StartReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'hCursor',
			DWORD
			),
			(
			'ulAction',
			DWORD
			),
			(
			'ulTimeout',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			),
			(
			'dwMaxBodySize',
			DWORD
			),
			(
			'dwMaxCompoundMessageSize',
			DWORD
			)
		)


class R_CancelReceive(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwRequestId',
			DWORD
			)
		)


class R_CancelReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwRequestId',
			DWORD
			)
		)


class R_EndReceive(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwAck',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			)
		)


class R_EndReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwAck',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			)
		)


class R_MoveMessage(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContextFrom',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'ullContextTo',
			ULONGLONG
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'pTransactionId',
			XACTUOW
			)
		)


class R_MoveMessageResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContextFrom',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'ullContextTo',
			ULONGLONG
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'pTransactionId',
			XACTUOW
			)
		)


class R_OpenQueueForMove(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pClientId',
			GUID
			),
			(
			'fNonRoutingServer',
			LONG
			),
			(
			'Major',
			UNSIGNED_CHAR
			),
			(
			'Minor',
			UNSIGNED_CHAR
			),
			(
			'BuildNumber',
			USHORT
			),
			(
			'fWorkgroup',
			LONG
			)
		)


class R_OpenQueueForMoveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pClientId',
			GUID
			),
			(
			'fNonRoutingServer',
			LONG
			),
			(
			'Major',
			UNSIGNED_CHAR
			),
			(
			'Minor',
			UNSIGNED_CHAR
			),
			(
			'BuildNumber',
			USHORT
			),
			(
			'fWorkgroup',
			LONG
			)
		)


class R_QMEnlistRemoteTransaction(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pTransactionId',
			XACTUOW
			),
			(
			'cbPropagationToken',
			DWORD
			),
			(
			'pbPropagationToken',
			UNSIGNED_CHAR
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			)
		)


class R_QMEnlistRemoteTransactionResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pTransactionId',
			XACTUOW
			),
			(
			'cbPropagationToken',
			DWORD
			),
			(
			'pbPropagationToken',
			UNSIGNED_CHAR
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			)
		)


class R_StartTransactionalReceive(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'hCursor',
			DWORD
			),
			(
			'ulAction',
			DWORD
			),
			(
			'ulTimeout',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			),
			(
			'dwMaxBodySize',
			DWORD
			),
			(
			'dwMaxCompoundMessageSize',
			DWORD
			),
			(
			'pTransactionId',
			XACTUOW
			)
		)


class R_StartTransactionalReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'hCursor',
			DWORD
			),
			(
			'ulAction',
			DWORD
			),
			(
			'ulTimeout',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			),
			(
			'dwMaxBodySize',
			DWORD
			),
			(
			'dwMaxCompoundMessageSize',
			DWORD
			),
			(
			'pTransactionId',
			XACTUOW
			)
		)


class R_SetUserAcknowledgementClass(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'usClass',
			USHORT
			)
		)


class R_SetUserAcknowledgementClassResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'usClass',
			USHORT
			)
		)


class R_EndTransactionalReceive(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwAck',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			)
		)


class R_EndTransactionalReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'phContext',
			QUEUE_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'dwAck',
			DWORD
			),
			(
			'dwRequestId',
			DWORD
			)
		)


OPNUMS = {0 : (
	R_GetServerPort,
	R_GetServerPortResponse
	),1 : (
	Opnum1NotUsedOnWire,
	Opnum1NotUsedOnWireResponse
	),2 : (
	R_OpenQueue,
	R_OpenQueueResponse
	),3 : (
	R_CloseQueue,
	R_CloseQueueResponse
	),4 : (
	R_CreateCursor,
	R_CreateCursorResponse
	),5 : (
	R_CloseCursor,
	R_CloseCursorResponse
	),6 : (
	R_PurgeQueue,
	R_PurgeQueueResponse
	),7 : (
	R_StartReceive,
	R_StartReceiveResponse
	),8 : (
	R_CancelReceive,
	R_CancelReceiveResponse
	),9 : (
	R_EndReceive,
	R_EndReceiveResponse
	),10 : (
	R_MoveMessage,
	R_MoveMessageResponse
	),11 : (
	R_OpenQueueForMove,
	R_OpenQueueForMoveResponse
	),12 : (
	R_QMEnlistRemoteTransaction,
	R_QMEnlistRemoteTransactionResponse
	),13 : (
	R_StartTransactionalReceive,
	R_StartTransactionalReceiveResponse
	),14 : (
	R_SetUserAcknowledgementClass,
	R_SetUserAcknowledgementClassResponse
	),15 : (
	R_EndTransactionalReceive,
	R_EndTransactionalReceiveResponse
	)}
#################################################################################
#TYPEDEFS
#################################################################################
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#qmcomm Definition
#################################################################################
MSRPC_UUID_QMCOMM = uuidtup_to_bin(('fdb3a030-065-111-bb9b-00024a5525','0.0'))
class CACCREATEREMOTECURSOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCursor',
			DWORD
			),
			(
			'srv_hACQueue',
			DWORD
			),
			(
			'cli_pQMQueue',
			DWORD
			)
		)


TRANSFER_TYPE = DWORD__ENUM
CACTB_SEND = 0
CACTB_RECEIVE = 0
class DATA_CACTRANSFERBUFFERV1(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_CACTRANSFERBUFFERV1(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CACTRANSFERBUFFERV1
			)
		)


class CACTRANSFERBUFFERV1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'uTransferType',
			DWORD
			),
			(
			'u0',
			U0
			),
			(
			'pClass',
			UNSIGNED_SHORT
			),
			(
			'ppMessageID',
			OBJECTID
			),
			(
			'ppCorrelationID',
			UNSIGNED_CHAR
			),
			(
			'pSentTime',
			DWORD
			),
			(
			'pArrivedTime',
			DWORD
			),
			(
			'pPriority',
			UNSIGNED_CHAR
			),
			(
			'pDelivery',
			UNSIGNED_CHAR
			),
			(
			'pAcknowledge',
			UNSIGNED_CHAR
			),
			(
			'pAuditing',
			UNSIGNED_CHAR
			),
			(
			'pApplicationTag',
			DWORD
			),
			(
			'ppBody',
			UNSIGNED_CHAR
			),
			(
			'ulBodyBufferSizeInBytes',
			DWORD
			),
			(
			'ulAllocBodyBufferInBytes',
			DWORD
			),
			(
			'pBodySize',
			DWORD
			),
			(
			'ppTitle',
			WCHAR
			),
			(
			'ulTitleBufferSizeInWCHARs',
			DWORD
			),
			(
			'pulTitleBufferSizeInWCHARs',
			DWORD
			),
			(
			'ulAbsoluteTimeToQueue',
			DWORD
			),
			(
			'pulRelativeTimeToQueue',
			DWORD
			),
			(
			'ulRelativeTimeToLive',
			DWORD
			),
			(
			'pulRelativeTimeToLive',
			DWORD
			),
			(
			'pTrace',
			UNSIGNED_CHAR
			),
			(
			'pulSenderIDType',
			DWORD
			),
			(
			'ppSenderID',
			UNSIGNED_CHAR
			),
			(
			'pulSenderIDLenProp',
			DWORD
			),
			(
			'pulPrivLevel',
			DWORD
			),
			(
			'ulAuthLevel',
			DWORD
			),
			(
			'pAuthenticated',
			UNSIGNED_CHAR
			),
			(
			'pulHashAlg',
			DWORD
			),
			(
			'pulEncryptAlg',
			DWORD
			),
			(
			'ppSenderCert',
			UNSIGNED_CHAR
			),
			(
			'ulSenderCertLen',
			DWORD
			),
			(
			'pulSenderCertLenProp',
			DWORD
			),
			(
			'ppwcsProvName',
			WCHAR
			),
			(
			'ulProvNameLen',
			DWORD
			),
			(
			'pulAuthProvNameLenProp',
			DWORD
			),
			(
			'pulProvType',
			DWORD
			),
			(
			'fDefaultProvider',
			LONG
			),
			(
			'ppSymmKeys',
			UNSIGNED_CHAR
			),
			(
			'ulSymmKeysSize',
			DWORD
			),
			(
			'pulSymmKeysSizeProp',
			DWORD
			),
			(
			'bEncrypted',
			UNSIGNED_CHAR
			),
			(
			'bAuthenticated',
			UNSIGNED_CHAR
			),
			(
			'uSenderIDLen',
			UNSIGNED_SHORT
			),
			(
			'ppSignature',
			UNSIGNED_CHAR
			),
			(
			'ulSignatureSize',
			DWORD
			),
			(
			'pulSignatureSizeProp',
			DWORD
			),
			(
			'ppSrcQMID',
			GUID
			),
			(
			'pUow',
			XACTUOW
			),
			(
			'ppMsgExtension',
			PTR_CACTRANSFERBUFFERV1
			),
			(
			'ulMsgExtensionBufferInBytes',
			DWORD
			),
			(
			'pMsgExtensionSize',
			DWORD
			),
			(
			'ppConnectorType',
			GUID
			),
			(
			'pulBodyType',
			DWORD
			),
			(
			'pulVersion',
			DWORD
			)
		)


class OLD(NDRSTRUCT):
	align = 1
	structure = (

		)


class CACTRANSFERBUFFERV2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'OLD',
			OLD
			),
			(
			'pbFirstInXact',
			UNSIGNED_CHAR
			),
			(
			'pbLastInXact',
			UNSIGNED_CHAR
			),
			(
			'ppXactID',
			OBJECTID
			)
		)


class U0(NDRUNION):
	union = {1 : (
		'pQueueFormat',
		QUEUE_FORMAT
		)}


class OBJECT_FORMAT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ObjType',
			DWORD
			),
			(
			'u0',
			U0
			)
		)


PCTX_OPENREMOTE_HANDLE_TYPE = VOID
RPC_QUEUE_HANDLE = VOID
RPC_INT_XACT_HANDLE = VOID
class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (

		)


class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class R_QMGetRemoteQueueName(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueue',
			DWORD
			),
			(
			'lplpRemoteQueueName',
			WCHAR
			)
		)


class R_QMGetRemoteQueueNameResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueue',
			DWORD
			),
			(
			'lplpRemoteQueueName',
			WCHAR
			)
		)


class R_QMOpenRemoteQueue(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwCallingProcessID',
			DWORD
			),
			(
			'dwDesiredAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'dwMQS',
			DWORD
			)
		)


class R_QMOpenRemoteQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwCallingProcessID',
			DWORD
			),
			(
			'dwDesiredAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'dwMQS',
			DWORD
			)
		)


class R_QMCloseRemoteQueueContext(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'pphContext',
			PCTX_OPENREMOTE_HANDLE_TYPE
			)
		)


class R_QMCloseRemoteQueueContextResponse(NDRCALL):
	structure = (
			(
			'pphContext',
			PCTX_OPENREMOTE_HANDLE_TYPE
			)
		)


class R_QMCreateRemoteCursor(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'ptb1',
			STRUCT CACTRANSFERBUFFERV1
			),
			(
			'hQueue',
			DWORD
			)
		)


class R_QMCreateRemoteCursorResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'ptb1',
			STRUCT CACTRANSFERBUFFERV1
			),
			(
			'hQueue',
			DWORD
			)
		)


class Opnum5NotUsedOnWire(NDRCALL):
	OPNUM = 5
	structure = (

		)


class Opnum5NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class R_QMCreateObjectInternal(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwObjectType',
			DWORD
			),
			(
			'lpwcsPathName',
			 WCHAR
			),
			(
			'SDSize',
			DWORD
			),
			(
			'pSecurityDescriptor',
			UNSIGNED_CHAR
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMCreateObjectInternalResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwObjectType',
			DWORD
			),
			(
			'lpwcsPathName',
			 WCHAR
			),
			(
			'SDSize',
			DWORD
			),
			(
			'pSecurityDescriptor',
			UNSIGNED_CHAR
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMSetObjectSecurityInternal(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'SecurityInformation',
			DWORD
			),
			(
			'SDSize',
			DWORD
			),
			(
			'pSecurityDescriptor',
			UNSIGNED_CHAR
			)
		)


class R_QMSetObjectSecurityInternalResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'SecurityInformation',
			DWORD
			),
			(
			'SDSize',
			DWORD
			),
			(
			'pSecurityDescriptor',
			UNSIGNED_CHAR
			)
		)


class R_QMGetObjectSecurityInternal(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'RequestedInformation',
			DWORD
			),
			(
			'nLength',
			DWORD
			)
		)


class R_QMGetObjectSecurityInternalResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'RequestedInformation',
			DWORD
			),
			(
			'nLength',
			DWORD
			)
		)


class R_QMDeleteObject(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			)
		)


class R_QMDeleteObjectResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			)
		)


class R_QMGetObjectProperties(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMGetObjectPropertiesResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMSetObjectProperties(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMSetObjectPropertiesResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			),
			(
			'cp',
			DWORD
			),
			(
			'aProp',
			DWORD
			),
			(
			'apVar',
			PROPVARIANT
			)
		)


class R_QMObjectPathToObjectFormat(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpwcsPathName',
			 WCHAR
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			)
		)


class R_QMObjectPathToObjectFormatResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpwcsPathName',
			 WCHAR
			),
			(
			'pObjectFormat',
			STRUCT OBJECT_FORMAT
			)
		)


class Opnum13NotUsedOnWire(NDRCALL):
	OPNUM = 13
	structure = (

		)


class Opnum13NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class R_QMGetTmWhereabouts(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'cbBufSize',
			DWORD
			)
		)


class R_QMGetTmWhereaboutsResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'cbBufSize',
			DWORD
			)
		)


class R_QMEnlistTransaction(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pUow',
			XACTUOW
			),
			(
			'cbCookie',
			DWORD
			),
			(
			'pbCookie',
			UNSIGNED_CHAR
			)
		)


class R_QMEnlistTransactionResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pUow',
			XACTUOW
			),
			(
			'cbCookie',
			DWORD
			),
			(
			'pbCookie',
			UNSIGNED_CHAR
			)
		)


class R_QMEnlistInternalTransaction(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pUow',
			XACTUOW
			)
		)


class R_QMEnlistInternalTransactionResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pUow',
			XACTUOW
			)
		)


class R_QMCommitTransaction(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'phIntXact',
			RPC_INT_XACT_HANDLE
			)
		)


class R_QMCommitTransactionResponse(NDRCALL):
	structure = (
			(
			'phIntXact',
			RPC_INT_XACT_HANDLE
			)
		)


class R_QMAbortTransaction(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'phIntXact',
			RPC_INT_XACT_HANDLE
			)
		)


class R_QMAbortTransactionResponse(NDRCALL):
	structure = (
			(
			'phIntXact',
			RPC_INT_XACT_HANDLE
			)
		)


class rpc_QMOpenQueueInternal(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwDesiredAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'hRemoteQueue',
			DWORD
			),
			(
			'lplpRemoteQueueName',
			WCHAR
			),
			(
			'dwpQueue',
			DWORD
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'lpClientName',
			WCHAR
			),
			(
			'dwRemoteProtocol',
			DWORD
			),
			(
			'dwpRemoteContext',
			DWORD
			)
		)


class rpc_QMOpenQueueInternalResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'dwDesiredAccess',
			DWORD
			),
			(
			'dwShareMode',
			DWORD
			),
			(
			'hRemoteQueue',
			DWORD
			),
			(
			'lplpRemoteQueueName',
			WCHAR
			),
			(
			'dwpQueue',
			DWORD
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'lpClientName',
			WCHAR
			),
			(
			'dwRemoteProtocol',
			DWORD
			),
			(
			'dwpRemoteContext',
			DWORD
			)
		)


class rpc_ACCloseHandle(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'phQueue',
			RPC_QUEUE_HANDLE
			)
		)


class rpc_ACCloseHandleResponse(NDRCALL):
	structure = (
			(
			'phQueue',
			RPC_QUEUE_HANDLE
			)
		)


class Opnum21NotUsedOnWire(NDRCALL):
	OPNUM = 21
	structure = (

		)


class Opnum21NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class rpc_ACCloseCursor(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'hCursor',
			DWORD
			)
		)


class rpc_ACCloseCursorResponse(NDRCALL):
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'hCursor',
			DWORD
			)
		)


class rpc_ACSetCursorProperties(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'hProxy',
			RPC_QUEUE_HANDLE
			),
			(
			'hCursor',
			DWORD
			),
			(
			'hRemoteCursor',
			DWORD
			)
		)


class rpc_ACSetCursorPropertiesResponse(NDRCALL):
	structure = (
			(
			'hProxy',
			RPC_QUEUE_HANDLE
			),
			(
			'hCursor',
			DWORD
			),
			(
			'hRemoteCursor',
			DWORD
			)
		)


class Opnum24NotUsedOnWire(NDRCALL):
	OPNUM = 24
	structure = (

		)


class Opnum24NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum25NotUsedOnWire(NDRCALL):
	OPNUM = 25
	structure = (

		)


class Opnum25NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class rpc_ACHandleToFormatName(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'dwFormatNameRPCBufferLen',
			DWORD
			),
			(
			'lpwcsFormatName',
			WCHAR
			),
			(
			'pdwLength',
			DWORD
			)
		)


class rpc_ACHandleToFormatNameResponse(NDRCALL):
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'dwFormatNameRPCBufferLen',
			DWORD
			),
			(
			'lpwcsFormatName',
			WCHAR
			),
			(
			'pdwLength',
			DWORD
			)
		)


class rpc_ACPurgeQueue(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			)
		)


class rpc_ACPurgeQueueResponse(NDRCALL):
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			)
		)


class R_QMQueryQMRegistryInternal(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwQueryType',
			DWORD
			)
		)


class R_QMQueryQMRegistryInternalResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwQueryType',
			DWORD
			)
		)


class Opnum29NotUsedOnWire(NDRCALL):
	OPNUM = 29
	structure = (

		)


class Opnum29NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum30NotUsedOnWire(NDRCALL):
	OPNUM = 30
	structure = (

		)


class Opnum30NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class R_QMGetRTQMServerPort(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'fIP',
			DWORD
			)
		)


class R_QMGetRTQMServerPortResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'fIP',
			DWORD
			)
		)


class Opnum32NotUsedOnWire(NDRCALL):
	OPNUM = 32
	structure = (

		)


class Opnum32NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum33NotUsedOnWire(NDRCALL):
	OPNUM = 33
	structure = (

		)


class Opnum33NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum34NotUsedOnWire(NDRCALL):
	OPNUM = 34
	structure = (

		)


class Opnum34NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Opnum0NotUsedOnWire,
	Opnum0NotUsedOnWireResponse
	),1 : (
	R_QMGetRemoteQueueName,
	R_QMGetRemoteQueueNameResponse
	),2 : (
	R_QMOpenRemoteQueue,
	R_QMOpenRemoteQueueResponse
	),3 : (
	R_QMCloseRemoteQueueContext,
	R_QMCloseRemoteQueueContextResponse
	),4 : (
	R_QMCreateRemoteCursor,
	R_QMCreateRemoteCursorResponse
	),5 : (
	Opnum5NotUsedOnWire,
	Opnum5NotUsedOnWireResponse
	),6 : (
	R_QMCreateObjectInternal,
	R_QMCreateObjectInternalResponse
	),7 : (
	R_QMSetObjectSecurityInternal,
	R_QMSetObjectSecurityInternalResponse
	),8 : (
	R_QMGetObjectSecurityInternal,
	R_QMGetObjectSecurityInternalResponse
	),9 : (
	R_QMDeleteObject,
	R_QMDeleteObjectResponse
	),10 : (
	R_QMGetObjectProperties,
	R_QMGetObjectPropertiesResponse
	),11 : (
	R_QMSetObjectProperties,
	R_QMSetObjectPropertiesResponse
	),12 : (
	R_QMObjectPathToObjectFormat,
	R_QMObjectPathToObjectFormatResponse
	),13 : (
	Opnum13NotUsedOnWire,
	Opnum13NotUsedOnWireResponse
	),14 : (
	R_QMGetTmWhereabouts,
	R_QMGetTmWhereaboutsResponse
	),15 : (
	R_QMEnlistTransaction,
	R_QMEnlistTransactionResponse
	),16 : (
	R_QMEnlistInternalTransaction,
	R_QMEnlistInternalTransactionResponse
	),17 : (
	R_QMCommitTransaction,
	R_QMCommitTransactionResponse
	),18 : (
	R_QMAbortTransaction,
	R_QMAbortTransactionResponse
	),19 : (
	rpc_QMOpenQueueInternal,
	rpc_QMOpenQueueInternalResponse
	),20 : (
	rpc_ACCloseHandle,
	rpc_ACCloseHandleResponse
	),21 : (
	Opnum21NotUsedOnWire,
	Opnum21NotUsedOnWireResponse
	),22 : (
	rpc_ACCloseCursor,
	rpc_ACCloseCursorResponse
	),23 : (
	rpc_ACSetCursorProperties,
	rpc_ACSetCursorPropertiesResponse
	),24 : (
	Opnum24NotUsedOnWire,
	Opnum24NotUsedOnWireResponse
	),25 : (
	Opnum25NotUsedOnWire,
	Opnum25NotUsedOnWireResponse
	),26 : (
	rpc_ACHandleToFormatName,
	rpc_ACHandleToFormatNameResponse
	),27 : (
	rpc_ACPurgeQueue,
	rpc_ACPurgeQueueResponse
	),28 : (
	R_QMQueryQMRegistryInternal,
	R_QMQueryQMRegistryInternalResponse
	),29 : (
	Opnum29NotUsedOnWire,
	Opnum29NotUsedOnWireResponse
	),30 : (
	Opnum30NotUsedOnWire,
	Opnum30NotUsedOnWireResponse
	),31 : (
	R_QMGetRTQMServerPort,
	R_QMGetRTQMServerPortResponse
	),32 : (
	Opnum32NotUsedOnWire,
	Opnum32NotUsedOnWireResponse
	),33 : (
	Opnum33NotUsedOnWire,
	Opnum33NotUsedOnWireResponse
	),34 : (
	Opnum34NotUsedOnWire,
	Opnum34NotUsedOnWireResponse
	)}
#################################################################################
#qmcomm2 Definition
#################################################################################
MSRPC_UUID_QMCOMM2 = uuidtup_to_bin(('76d12b80-3467-11d3-91ff-0090272f9ea3','0.0'))
class QMSendMessageInternalEx(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			),
			(
			'pMessageID',
			OBJECTID
			)
		)


class QMSendMessageInternalExResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pQueueFormat',
			QUEUE_FORMAT
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			),
			(
			'pMessageID',
			OBJECTID
			)
		)


class rpc_ACSendMessageEx(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			),
			(
			'pMessageID',
			OBJECTID
			)
		)


class rpc_ACSendMessageExResponse(NDRCALL):
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			),
			(
			'pMessageID',
			OBJECTID
			)
		)


class rpc_ACReceiveMessageEx(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQMContext',
			DWORD
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			)
		)


class rpc_ACReceiveMessageExResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQMContext',
			DWORD
			),
			(
			'ptb',
			STRUCT CACTRANSFERBUFFERV2
			)
		)


class rpc_ACCreateCursorEx(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'pcc',
			STRUCT CACCREATEREMOTECURSOR
			)
		)


class rpc_ACCreateCursorExResponse(NDRCALL):
	structure = (
			(
			'hQueue',
			RPC_QUEUE_HANDLE
			),
			(
			'pcc',
			STRUCT CACCREATEREMOTECURSOR
			)
		)


OPNUMS = {0 : (
	QMSendMessageInternalEx,
	QMSendMessageInternalExResponse
	),1 : (
	rpc_ACSendMessageEx,
	rpc_ACSendMessageExResponse
	),2 : (
	rpc_ACReceiveMessageEx,
	rpc_ACReceiveMessageExResponse
	),3 : (
	rpc_ACCreateCursorEx,
	rpc_ACCreateCursorExResponse
	)}
