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
#"ms-oaut.idl"
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
#"ms-dcom.idl"
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
CLSID = GUID
IID = GUID
ID = UNSIGNED_HYPER
OXID = UNSIGNED_HYPER
OID = UNSIGNED_HYPER
SETID = UNSIGNED_HYPER
IPID = GUID
CID = GUID
REFIPID =  GUID
class COMVERSION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'MajorVersion',
			UNSIGNED_SHORT
			),
			(
			'MinorVersion',
			UNSIGNED_SHORT
			)
		)


class ORPC_EXTENT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'id',
			GUID
			),
			(
			'size',
			UNSIGNED_LONG
			),
			(
			'data',
			BYTE
			)
		)


class DATA_ORPC_EXTENT_ARRAY(NDRUniConformantArray):
	item = ORPC_EXTENT


class PTR_ORPC_EXTENT_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_ORPC_EXTENT_ARRAY
			)
		)


class ORPC_EXTENT_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'size',
			UNSIGNED_LONG
			),
			(
			'reserved',
			UNSIGNED_LONG
			),
			(
			'extent',
			PTR_ORPC_EXTENT_ARRAY
			)
		)


class ORPCTHIS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'version',
			COMVERSION
			),
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'reserved1',
			UNSIGNED_LONG
			),
			(
			'cid',
			CID
			),
			(
			'extensions',
			ORPC_EXTENT_ARRAY
			)
		)


class ORPCTHAT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'extensions',
			ORPC_EXTENT_ARRAY
			)
		)


class DUALSTRINGARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wNumEntries',
			UNSIGNED_SHORT
			),
			(
			'wSecurityOffset',
			UNSIGNED_SHORT
			),
			(
			'aStringArray',
			UNSIGNED_SHORT
			)
		)


tagCPFLAGS = DWORD__ENUM
CPFLAG_PROPAGATE = 1
CPFLAG_EXPOSE = 2
CPFLAG_ENVOY = 4
class MINTERFACEPOINTER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ulCntData',
			UNSIGNED_LONG
			),
			(
			'abData',
			BYTE
			)
		)


PMINTERFACEPOINTER = MINTERFACEPOINTER
class ERROROBJECTDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwVersion',
			DWORD
			),
			(
			'dwHelpContext',
			DWORD
			),
			(
			'iid',
			IID
			),
			(
			'pszSource',
			WCHAR_T
			),
			(
			'pszDescription',
			WCHAR_T
			),
			(
			'pszHelpFile',
			WCHAR_T
			)
		)


class STDOBJREF(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'cPublicRefs',
			UNSIGNED_LONG
			),
			(
			'oxid',
			OXID
			),
			(
			'oid',
			OID
			),
			(
			'ipid',
			IPID
			)
		)


class REMQIRESULT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hResult',
			HRESULT
			),
			(
			'std',
			STDOBJREF
			)
		)


class REMINTERFACEREF(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ipid',
			IPID
			),
			(
			'cPublicRefs',
			UNSIGNED_LONG
			),
			(
			'cPrivateRefs',
			UNSIGNED_LONG
			)
		)


PREMQIRESULT = REMQIRESULT
PMINTERFACEPOINTERINTERNAL = MINTERFACEPOINTER
class COSERVERINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwReserved1',
			DWORD
			),
			(
			'pwszName',
			WCHAR_T
			),
			(
			'pdwReserved',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			)
		)


class DATA_CUSTOMREMOTE_REQUEST_SCM_INFO(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_CUSTOMREMOTE_REQUEST_SCM_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CUSTOMREMOTE_REQUEST_SCM_INFO
			)
		)


class CUSTOMREMOTE_REQUEST_SCM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientImpLevel',
			DWORD
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'pRequestedProtseqs',
			PTR_CUSTOMREMOTE_REQUEST_SCM_INFO
			)
		)


class CUSTOMREMOTE_REPLY_SCM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Oxid',
			OXID
			),
			(
			'pdsaOxidBindings',
			DUALSTRINGARRAY
			),
			(
			'ipidRemUnknown',
			IPID
			),
			(
			'authnHint',
			DWORD
			),
			(
			'serverVersion',
			COMVERSION
			)
		)


class DATA_INSTANTIATIONINFODATA(NDRUniConformantArray):
	item = IID


class PTR_INSTANTIATIONINFODATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_INSTANTIATIONINFODATA
			)
		)


class INSTANTIATIONINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'classId',
			CLSID
			),
			(
			'classCtx',
			DWORD
			),
			(
			'actvflags',
			DWORD
			),
			(
			'fIsSurrogate',
			LONG
			),
			(
			'cIID',
			DWORD
			),
			(
			'instFlag',
			DWORD
			),
			(
			'pIID',
			PTR_INSTANTIATIONINFODATA
			),
			(
			'thisSize',
			DWORD
			),
			(
			'clientCOMVersion',
			COMVERSION
			)
		)


class LOCATIONINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'machineName',
			WCHAR_T
			),
			(
			'processId',
			DWORD
			),
			(
			'apartmentId',
			DWORD
			),
			(
			'contextId',
			DWORD
			)
		)


class ACTIVATIONCONTEXTINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clientOK',
			LONG
			),
			(
			'bReserved1',
			LONG
			),
			(
			'dwReserved1',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			),
			(
			'pIFDClientCtx',
			MINTERFACEPOINTER
			),
			(
			'pIFDPrototypeCtx',
			MINTERFACEPOINTER
			)
		)


class DATA_CUSTOMHEADER(NDRUniConformantArray):
	item = DWORD


class PTR_CUSTOMHEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CUSTOMHEADER
			)
		)


class CUSTOMHEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'totalSize',
			DWORD
			),
			(
			'headerSize',
			DWORD
			),
			(
			'dwReserved',
			DWORD
			),
			(
			'destCtx',
			DWORD
			),
			(
			'cIfs',
			DWORD
			),
			(
			'classInfoClsid',
			CLSID
			),
			(
			'pclsid',
			CLSID
			),
			(
			'pSizes',
			PTR_CUSTOMHEADER
			),
			(
			'pdwReserved',
			DWORD
			)
		)


class DATA_PROPSOUTINFO(NDRUniConformantArray):
	item = MINTERFACEPOINTER


class PTR_PROPSOUTINFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_PROPSOUTINFO
			)
		)


class PROPSOUTINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cIfs',
			DWORD
			),
			(
			'piid',
			IID
			),
			(
			'phresults',
			HRESULT
			),
			(
			'ppIntfData',
			PTR_PROPSOUTINFO
			)
		)


class SECURITYINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwAuthnFlags',
			DWORD
			),
			(
			'pServerInfo',
			COSERVERINFO
			),
			(
			'pdwReserved',
			DWORD
			)
		)


class SCMREQUESTINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pdwReserved',
			DWORD
			),
			(
			'remoteRequest',
			CUSTOMREMOTE_REQUEST_SCM_INFO
			)
		)


class SCMREPLYINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pdwReserved',
			DWORD
			),
			(
			'remoteReply',
			CUSTOMREMOTE_REPLY_SCM_INFO
			)
		)


class INSTANCEINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'fileName',
			WCHAR_T
			),
			(
			'mode',
			DWORD
			),
			(
			'ifdROT',
			MINTERFACEPOINTER
			),
			(
			'ifdStg',
			MINTERFACEPOINTER
			)
		)


SPD_FLAGS = DWORD__ENUM
SPD_FLAG_USE_CONSOLE_SESSION = 1
SPD_FLAG_USE_DEFAULT_AUTHN_LVL = 2
class SPECIALPROPERTIESDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwSessionId',
			UNSIGNED_LONG
			),
			(
			'fRemoteThisSessionId',
			LONG
			),
			(
			'fClientImpersonating',
			LONG
			),
			(
			'fPartitionIDPresent',
			LONG
			),
			(
			'dwDefaultAuthnLvl',
			DWORD
			),
			(
			'guidPartition',
			GUID
			),
			(
			'dwPRTFlags',
			DWORD
			),
			(
			'dwOrigClsctx',
			DWORD
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'Reserved1',
			DWORD
			),
			(
			'Reserved2',
			UNSIGNED___INT64
			),
			(
			'Reserved3',
			DWORD
			)
		)


class SPECIALPROPERTIESDATA_ALTERNATE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwSessionId',
			UNSIGNED_LONG
			),
			(
			'fRemoteThisSessionId',
			LONG
			),
			(
			'fClientImpersonating',
			LONG
			),
			(
			'fPartitionIDPresent',
			LONG
			),
			(
			'dwDefaultAuthnLvl',
			DWORD
			),
			(
			'guidPartition',
			GUID
			),
			(
			'dwPRTFlags',
			DWORD
			),
			(
			'dwOrigClsctx',
			DWORD
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'Reserved3',
			DWORD
			)
		)


#################################################################################
#CONSTANTS
#################################################################################
MIN_ACTPROP_LIMIT = 1
MAX_ACTPROP_LIMIT = 10
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#IActivation Definition
#################################################################################
MSRPC_UUID_IACTIVATION = uuidtup_to_bin(('4d9f4ab8-7d1c-11cf-861e-0020af6e7c57','0.0'))
MAX_REQUESTED_INTERFACES = CONST_UNSIGNED_LONG
MAX_REQUESTED_PROTSEQS = CONST_UNSIGNED_LONG
class RemoteActivation(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'ORPCthis',
			ORPCTHIS
			),
			(
			'Clsid',
			GUID
			),
			(
			'pwszObjectName',
			WCHAR_T
			),
			(
			'pObjectStorage',
			MINTERFACEPOINTER
			),
			(
			'ClientImpLevel',
			DWORD
			),
			(
			'Mode',
			DWORD
			),
			(
			'Interfaces',
			DWORD
			),
			(
			'pIIDs',
			IID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'aRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


class RemoteActivationResponse(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'ORPCthis',
			ORPCTHIS
			),
			(
			'Clsid',
			GUID
			),
			(
			'pwszObjectName',
			WCHAR_T
			),
			(
			'pObjectStorage',
			MINTERFACEPOINTER
			),
			(
			'ClientImpLevel',
			DWORD
			),
			(
			'Mode',
			DWORD
			),
			(
			'Interfaces',
			DWORD
			),
			(
			'pIIDs',
			IID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'aRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


OPNUMS = {0 : (
	RemoteActivation,
	RemoteActivationResponse
	)}
#################################################################################
#IRemoteSCMActivator Definition
#################################################################################
MSRPC_UUID_IREMOTESCMACTIVATOR = uuidtup_to_bin(('000001A0-0000-0000-C000-000000000046','0.0'))
class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (

		)


class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (

		)


class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum2NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (

		)


class Opnum2NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RemoteGetClassObject(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'rpc',
			HANDLE_T
			),
			(
			'orpcthis',
			ORPCTHIS
			),
			(
			'pActProperties',
			MINTERFACEPOINTER
			)
		)


class RemoteGetClassObjectResponse(NDRCALL):
	structure = (
			(
			'rpc',
			HANDLE_T
			),
			(
			'orpcthis',
			ORPCTHIS
			),
			(
			'pActProperties',
			MINTERFACEPOINTER
			)
		)


class RemoteCreateInstance(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'rpc',
			HANDLE_T
			),
			(
			'orpcthis',
			ORPCTHIS
			),
			(
			'pUnkOuter',
			MINTERFACEPOINTER
			),
			(
			'pActProperties',
			MINTERFACEPOINTER
			)
		)


class RemoteCreateInstanceResponse(NDRCALL):
	structure = (
			(
			'rpc',
			HANDLE_T
			),
			(
			'orpcthis',
			ORPCTHIS
			),
			(
			'pUnkOuter',
			MINTERFACEPOINTER
			),
			(
			'pActProperties',
			MINTERFACEPOINTER
			)
		)


OPNUMS = {0 : (
	Opnum0NotUsedOnWire,
	Opnum0NotUsedOnWireResponse
	),1 : (
	Opnum1NotUsedOnWire,
	Opnum1NotUsedOnWireResponse
	),2 : (
	Opnum2NotUsedOnWire,
	Opnum2NotUsedOnWireResponse
	),3 : (
	RemoteGetClassObject,
	RemoteGetClassObjectResponse
	),4 : (
	RemoteCreateInstance,
	RemoteCreateInstanceResponse
	)}
#################################################################################
#IObjectExporter Definition
#################################################################################
MSRPC_UUID_IOBJECTEXPORTER = uuidtup_to_bin(('99fcfec4-5260-101b-bbcb-00aa0021347a','0.0'))
class ResolveOxid(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pOxid',
			OXID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'arRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


class ResolveOxidResponse(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pOxid',
			OXID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'arRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


class SimplePing(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pSetId',
			SETID
			)
		)


class SimplePingResponse(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pSetId',
			SETID
			)
		)


class ComplexPing(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pSetId',
			SETID
			),
			(
			'SequenceNum',
			UNSIGNED_SHORT
			),
			(
			'cAddToSet',
			UNSIGNED_SHORT
			),
			(
			'cDelFromSet',
			UNSIGNED_SHORT
			),
			(
			'AddToSet',
			OID
			),
			(
			'DelFromSet',
			OID
			)
		)


class ComplexPingResponse(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pSetId',
			SETID
			),
			(
			'SequenceNum',
			UNSIGNED_SHORT
			),
			(
			'cAddToSet',
			UNSIGNED_SHORT
			),
			(
			'cDelFromSet',
			UNSIGNED_SHORT
			),
			(
			'AddToSet',
			OID
			),
			(
			'DelFromSet',
			OID
			)
		)


class ServerAlive(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hRpc',
			HANDLE_T
			)
		)


class ServerAliveResponse(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			)
		)


class ResolveOxid2(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pOxid',
			OXID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'arRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


class ResolveOxid2Response(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			),
			(
			'pOxid',
			OXID
			),
			(
			'cRequestedProtseqs',
			UNSIGNED_SHORT
			),
			(
			'arRequestedProtseqs',
			UNSIGNED_SHORT
			)
		)


class ServerAlive2(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'hRpc',
			HANDLE_T
			)
		)


class ServerAlive2Response(NDRCALL):
	structure = (
			(
			'hRpc',
			HANDLE_T
			)
		)


OPNUMS = {0 : (
	ResolveOxid,
	ResolveOxidResponse
	),1 : (
	SimplePing,
	SimplePingResponse
	),2 : (
	ComplexPing,
	ComplexPingResponse
	),3 : (
	ServerAlive,
	ServerAliveResponse
	),4 : (
	ResolveOxid2,
	ResolveOxid2Response
	),5 : (
	ServerAlive2,
	ServerAlive2Response
	)}
#################################################################################
#IUnknown Definition
#################################################################################
MSRPC_UUID_IUNKNOWN = uuidtup_to_bin(('00000000-0000-0000-C000-000000000046','0.0'))
class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (

		)


class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (

		)


class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum2NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (

		)


class Opnum2NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Opnum0NotUsedOnWire,
	Opnum0NotUsedOnWireResponse
	),1 : (
	Opnum1NotUsedOnWire,
	Opnum1NotUsedOnWireResponse
	),2 : (
	Opnum2NotUsedOnWire,
	Opnum2NotUsedOnWireResponse
	)}
#################################################################################
#IRemUnknown Definition
#################################################################################
MSRPC_UUID_IREMUNKNOWN = uuidtup_to_bin(('00000131-0000-0000-C000-000000000046','0.0'))
class RemQueryInterface(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ripid',
			REFIPID
			),
			(
			'cRefs',
			UNSIGNED_LONG
			),
			(
			'cIids',
			UNSIGNED_SHORT
			),
			(
			'iids',
			IID
			)
		)


class RemQueryInterfaceResponse(NDRCALL):
	structure = (
			(
			'ripid',
			REFIPID
			),
			(
			'cRefs',
			UNSIGNED_LONG
			),
			(
			'cIids',
			UNSIGNED_SHORT
			),
			(
			'iids',
			IID
			)
		)


class RemAddRef(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'cInterfaceRefs',
			UNSIGNED_SHORT
			),
			(
			'InterfaceRefs',
			REMINTERFACEREF
			)
		)


class RemAddRefResponse(NDRCALL):
	structure = (
			(
			'cInterfaceRefs',
			UNSIGNED_SHORT
			),
			(
			'InterfaceRefs',
			REMINTERFACEREF
			)
		)


class RemRelease(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'cInterfaceRefs',
			UNSIGNED_SHORT
			),
			(
			'InterfaceRefs',
			REMINTERFACEREF
			)
		)


class RemReleaseResponse(NDRCALL):
	structure = (
			(
			'cInterfaceRefs',
			UNSIGNED_SHORT
			),
			(
			'InterfaceRefs',
			REMINTERFACEREF
			)
		)


OPNUMS = {0 : (
	RemQueryInterface,
	RemQueryInterfaceResponse
	),1 : (
	RemAddRef,
	RemAddRefResponse
	),2 : (
	RemRelease,
	RemReleaseResponse
	)}
#################################################################################
#IRemUnknown2 Definition
#################################################################################
MSRPC_UUID_IREMUNKNOWN2 = uuidtup_to_bin(('00000143-0000-0000-C000-000000000046','0.0'))
class RemQueryInterface2(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ripid',
			REFIPID
			),
			(
			'cIids',
			UNSIGNED_SHORT
			),
			(
			'iids',
			IID
			)
		)


class RemQueryInterface2Response(NDRCALL):
	structure = (
			(
			'ripid',
			REFIPID
			),
			(
			'cIids',
			UNSIGNED_SHORT
			),
			(
			'iids',
			IID
			)
		)


OPNUMS = {0 : (
	RemQueryInterface2,
	RemQueryInterface2Response
	)}
#################################################################################
#TYPEDEFS
#################################################################################
BYTE = BYTE
SCODE = LONG
REFIID = IID
REFGUID = GUID
LPOLESTR = WCHAR_T
LPCOLESTR = CONST_WCHAR_T
ULONG_PTR = UNSIGNED___INT3264
PULONG_PTR = UNSIGNED___INT3264
PVOID = VOID
LPVOID = VOID
PSAFEARRAY = SAFEARRAY
LPSAFEARRAY = SAFEARRAY
class VARIANT(NDRSTRUCT):
	align = 1
	structure = (

		)


VARENUM = DWORD__ENUM
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29
VT_LPSTR = 30
VT_LPWSTR = 31
VT_RECORD = 36
VT_INT_PTR = 37
VT_UINT_PTR = 38
VT_ARRAY = 8192
VT_BYREF = 16384
ADVFEATUREFLAGS = DWORD__ENUM
FADF_AUTO = 1
FADF_STATIC = 2
FADF_EMBEDDED = 4
FADF_FIXEDSIZE = 16
FADF_RECORD = 32
FADF_HAVEIID = 64
FADF_HAVEVARTYPE = 128
FADF_BSTR = 256
FADF_UNKNOWN = 512
FADF_DISPATCH = 1024
FADF_VARIANT = 2048
SF_TYPE = DWORD__ENUM
SF_ERROR = VT_ERROR
SF_I1 = VT_I1
SF_I2 = VT_I2
SF_I4 = VT_I4
SF_I8 = VT_I8
SF_BSTR = VT_BSTR
SF_UNKNOWN = VT_UNKNOWN
SF_DISPATCH = VT_DISPATCH
SF_VARIANT = VT_VARIANT
SF_RECORD = VT_RECORD
SF_HAVEIID = 32768
CALLCONV = DWORD__ENUM
CC_CDECL = 1
CC_PASCAL = 2
CC_STDCALL = 4
FUNCFLAGS = DWORD__ENUM
FUNCFLAG_FRESTRICTED = 1
FUNCFLAG_FSOURCE = 2
FUNCFLAG_FBINDABLE = 4
FUNCFLAG_FREQUESTEDIT = 8
FUNCFLAG_FDISPLAYBIND = 16
FUNCFLAG_FDEFAULTBIND = 32
FUNCFLAG_FHIDDEN = 64
FUNCFLAG_FUSESGETLASTERROR = 128
FUNCFLAG_FDEFAULTCOLLELEM = 256
FUNCFLAG_FUIDEFAULT = 512
FUNCFLAG_FNONBROWSABLE = 1024
FUNCFLAG_FREPLACEABLE = 2048
FUNCFLAG_FIMMEDIATEBIND = 4096
FUNCKIND = DWORD__ENUM
FUNC_PUREVIRTUAL = 1
FUNC_STATIC = 3
FUNC_DISPATCH = 4
IMPLTYPEFLAGS = DWORD__ENUM
IMPLTYPEFLAG_FDEFAULT = 1
IMPLTYPEFLAG_FSOURCE = 2
IMPLTYPEFLAG_FRESTRICTED = 4
IMPLTYPEFLAG_FDEFAULTVTABLE = 8
INVOKEKIND = DWORD__ENUM
INVOKE_FUNC = 1
INVOKE_PROPERTYGET = 2
INVOKE_PROPERTYPUT = 4
INVOKE_PROPERTYPUTREF = 8
PARAMFLAGS = DWORD__ENUM
PARAMFLAG_NONE = 0
PARAMFLAG_FIN = 1
PARAMFLAG_FOUT = 2
PARAMFLAG_FLCID = 4
PARAMFLAG_FRETVAL = 8
PARAMFLAG_FOPT = 16
PARAMFLAG_FHASDEFAULT = 32
PARAMFLAG_FHASCUSTDATA = 64
TYPEFLAGS = DWORD__ENUM
TYPEFLAG_FAPPOBJECT = 1
TYPEFLAG_FCANCREATE = 2
TYPEFLAG_FLICENSED = 4
TYPEFLAG_FPREDECLID = 8
TYPEFLAG_FHIDDEN = 16
TYPEFLAG_FCONTROL = 32
TYPEFLAG_FDUAL = 64
TYPEFLAG_FNONEXTENSIBLE = 128
TYPEFLAG_FOLEAUTOMATION = 256
TYPEFLAG_FRESTRICTED = 512
TYPEFLAG_FAGGREGATABLE = 1024
TYPEFLAG_FREPLACEABLE = 2048
TYPEFLAG_FDISPATCHABLE = 4096
TYPEFLAG_FPROXY = 16384
TYPEKIND = DWORD__ENUM
TKIND_ENUM = 0
TKIND_RECORD = 1
TKIND_MODULE = 2
TKIND_INTERFACE = 3
TKIND_DISPATCH = 4
TKIND_COCLASS = 5
TKIND_ALIAS = 6
TKIND_UNION = 7
VARFLAGS = DWORD__ENUM
VARFLAG_FREADONLY = 1
VARFLAG_FSOURCE = 2
VARFLAG_FBINDABLE = 4
VARFLAG_FREQUESTEDIT = 8
VARFLAG_FDISPLAYBIND = 16
VARFLAG_FDEFAULTBIND = 32
VARFLAG_FHIDDEN = 64
VARFLAG_FRESTRICTED = 128
VARFLAG_FDEFAULTCOLLELEM = 256
VARFLAG_FUIDEFAULT = 512
VARFLAG_FNONBROWSABLE = 1024
VARFLAG_FREPLACEABLE = 2048
VARFLAG_FIMMEDIATEBIND = 4096
VARKIND = DWORD__ENUM
VAR_PERINSTANCE = 0
VAR_STATIC = 1)
VAR_CONST = 1)
VAR_DISPATCH = 1)
LIBFLAGS = DWORD__ENUM
LIBFLAG_FRESTRICTED = 1
LIBFLAG_FCONTROL = 2
LIBFLAG_FHIDDEN = 4
LIBFLAG_FHASDISKIMAGE = 8
SYSKIND = DWORD__ENUM
SYS_WIN32 = 1
SYS_WIN64 = 3
DESCKIND = DWORD__ENUM
DESCKIND_NONE = 0
DESCKIND_FUNCDESC = 1
DESCKIND_VARDESC = 2
DESCKIND_TYPECOMP = 3
DESCKIND_IMPLICITAPPOBJ = 4
class FLAGGED_WORD_BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'clSize',
			UNSIGNED_LONG
			),
			(
			'asData',
			UNSIGNED_SHORT
			)
		)


BSTR = FLAGGED_WORD_BLOB
class CURRENCY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'int64',
			__INT64
			)
		)


DATE = DOUBLE
class DECIMAL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wReserved',
			WORD
			),
			(
			'scale',
			BYTE
			),
			(
			'sign',
			BYTE
			),
			(
			'Hi32',
			ULONG
			),
			(
			'Lo64',
			ULONGLONG
			)
		)


VARIANT_BOOL = SHORT
class DATA_WIREBRECORDSTR(NDRUniConformantArray):
	item = BYTE


class PTR_WIREBRECORDSTR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_WIREBRECORDSTR
			)
		)


class WIREBRECORDSTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'fFlags',
			ULONG
			),
			(
			'clSize',
			ULONG
			),
			(
			'pRecInfo',
			MINTERFACEPOINTER
			),
			(
			'pRecord',
			PTR_WIREBRECORDSTR
			)
		)


class BRECORD(NDRSTRUCT):
	align = 1
	structure = (

		)


class _VARUNION(NDRUNION):
	union = {VT_I8 : (
		'llVal',
		LONGLONG
		),VT_I4 : (
		'lVal',
		LONG
		),VT_UI1 : (
		'bVal',
		BYTE
		),VT_I2 : (
		'iVal',
		SHORT
		),VT_R4 : (
		'fltVal',
		FLOAT
		),VT_R8 : (
		'dblVal',
		DOUBLE
		),VT_BOOL : (
		'boolVal',
		VARIANT_BOOL
		),VT_ERROR : (
		'scode',
		HRESULT
		),VT_CY : (
		'cyVal',
		CURRENCY
		),VT_DATE : (
		'date',
		DATE
		),VT_BSTR : (
		'bstrVal',
		BSTR
		),VT_UNKNOWN : (
		'punkVal',
		IUNKNOWN
		),VT_DISPATCH : (
		'pdispVal',
		IDISPATCH
		),VT_ARRAY : (
		'parray',
		PSAFEARRAY
		),VT_RECORD : (
		'brecVal',
		BRECORD
		),VT_UI1|VT_BYREF : (
		'pbVal',
		BYTE
		),VT_I2|VT_BYREF : (
		'piVal',
		SHORT
		),VT_I4|VT_BYREF : (
		'plVal',
		LONG
		),VT_I8|VT_BYREF : (
		'pllVal',
		LONGLONG
		),VT_R4|VT_BYREF : (
		'pfltVal',
		FLOAT
		),VT_R8|VT_BYREF : (
		'pdblVal',
		DOUBLE
		),VT_BOOL|VT_BYREF : (
		'pboolVal',
		VARIANT_BOOL
		),VT_ERROR|VT_BYREF : (
		'pscode',
		HRESULT
		),VT_CY|VT_BYREF : (
		'pcyVal',
		CURRENCY
		),VT_DATE|VT_BYREF : (
		'pdate',
		DATE
		),VT_BSTR|VT_BYREF : (
		'pbstrVal',
		BSTR
		),VT_UNKNOWN|VT_BYREF : (
		'ppunkVal',
		IUNKNOWN
		),VT_DISPATCH|VT_BYREF : (
		'ppdispVal',
		IDISPATCH
		),VT_ARRAY|VT_BYREF : (
		'pparray',
		PSAFEARRAY
		),VT_VARIANT|VT_BYREF : (
		'pvarVal',
		VARIANT
		),VT_I1 : (
		'cVal',
		CHAR
		),VT_UI2 : (
		'uiVal',
		USHORT
		),VT_UI4 : (
		'ulVal',
		ULONG
		),VT_UI8 : (
		'ullVal',
		ULONGLONG
		),VT_INT : (
		'intVal',
		INT
		),VT_UINT : (
		'uintVal',
		UINT
		),VT_DECIMAL : (
		'decVal',
		DECIMAL
		),VT_I1|VT_BYREF : (
		'pcVal',
		CHAR
		),VT_UI2|VT_BYREF : (
		'puiVal',
		USHORT
		),VT_UI4|VT_BYREF : (
		'pulVal',
		ULONG
		),VT_UI8|VT_BYREF : (
		'pullVal',
		ULONGLONG
		),VT_INT|VT_BYREF : (
		'pintVal',
		INT
		),VT_UINT|VT_BYREF : (
		'puintVal',
		UINT
		),VT_DECIMAL|VT_BYREF : (
		'pdecVal',
		DECIMAL
		)}


class WIREVARIANTSTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clSize',
			DWORD
			),
			(
			'rpcReserved',
			DWORD
			),
			(
			'vt',
			USHORT
			),
			(
			'wReserved1',
			USHORT
			),
			(
			'wReserved2',
			USHORT
			),
			(
			'wReserved3',
			USHORT
			),
			(
			'_varUnion',
			_VARUNION
			)
		)


class SAFEARRAYBOUND(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cElements',
			ULONG
			),
			(
			'lLbound',
			LONG
			)
		)


class LPSAFEARRAYBOUND(NDRPOINTER):
	referent = (
			(
			'Data',
			SAFEARRAYBOUND
			)
		)


class DATA_SAFEARR_BSTR(NDRUniConformantArray):
	item = BSTR


class PTR_SAFEARR_BSTR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_BSTR
			)
		)


class SAFEARR_BSTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'aBstr',
			PTR_SAFEARR_BSTR
			)
		)


class DATA_SAFEARR_UNKNOWN(NDRUniConformantArray):
	item = IUNKNOWN


class PTR_SAFEARR_UNKNOWN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_UNKNOWN
			)
		)


class SAFEARR_UNKNOWN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'apUnknown',
			PTR_SAFEARR_UNKNOWN
			)
		)


class DATA_SAFEARR_DISPATCH(NDRUniConformantArray):
	item = IDISPATCH


class PTR_SAFEARR_DISPATCH(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_DISPATCH
			)
		)


class SAFEARR_DISPATCH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'apDispatch',
			PTR_SAFEARR_DISPATCH
			)
		)


class DATA_SAFEARR_VARIANT(NDRUniConformantArray):
	item = VARIANT


class PTR_SAFEARR_VARIANT(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_VARIANT
			)
		)


class SAFEARR_VARIANT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'aVariant',
			PTR_SAFEARR_VARIANT
			)
		)


class DATA_SAFEARR_BRECORD(NDRUniConformantArray):
	item = BRECORD


class PTR_SAFEARR_BRECORD(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_BRECORD
			)
		)


class SAFEARR_BRECORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'aRecord',
			PTR_SAFEARR_BRECORD
			)
		)


class DATA_SAFEARR_HAVEIID(NDRUniConformantArray):
	item = IUNKNOWN


class PTR_SAFEARR_HAVEIID(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SAFEARR_HAVEIID
			)
		)


class SAFEARR_HAVEIID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			ULONG
			),
			(
			'apUnknown',
			PTR_SAFEARR_HAVEIID
			),
			(
			'iid',
			IID
			)
		)


class DATA_BYTE_SIZEDARR(NDRUniConformantArray):
	item = BYTE


class PTR_BYTE_SIZEDARR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_BYTE_SIZEDARR
			)
		)


class BYTE_SIZEDARR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clSize',
			UNSIGNED_LONG
			),
			(
			'pData',
			PTR_BYTE_SIZEDARR
			)
		)


class DATA_WORD_SIZEDARR(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_WORD_SIZEDARR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_WORD_SIZEDARR
			)
		)


class WORD_SIZEDARR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clSize',
			UNSIGNED_LONG
			),
			(
			'pData',
			PTR_WORD_SIZEDARR
			)
		)


class DATA_DWORD_SIZEDARR(NDRUniConformantArray):
	item = UNSIGNED_LONG


class PTR_DWORD_SIZEDARR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DWORD_SIZEDARR
			)
		)


class DWORD_SIZEDARR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clSize',
			UNSIGNED_LONG
			),
			(
			'pData',
			PTR_DWORD_SIZEDARR
			)
		)


class DATA_HYPER_SIZEDARR(NDRUniConformantArray):
	item = HYPER


class PTR_HYPER_SIZEDARR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_HYPER_SIZEDARR
			)
		)


class HYPER_SIZEDARR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'clSize',
			UNSIGNED_LONG
			),
			(
			'pData',
			PTR_HYPER_SIZEDARR
			)
		)


class ANONYMOUS3(NDRUNION):
	union = {SF_BSTR : (
		'BstrStr',
		SAFEARR_BSTR
		),SF_UNKNOWN : (
		'UnknownStr',
		SAFEARR_UNKNOWN
		),SF_DISPATCH : (
		'DispatchStr',
		SAFEARR_DISPATCH
		),SF_VARIANT : (
		'VariantStr',
		SAFEARR_VARIANT
		),SF_RECORD : (
		'RecordStr',
		SAFEARR_BRECORD
		),SF_HAVEIID : (
		'HaveIidStr',
		SAFEARR_HAVEIID
		),SF_I1 : (
		'ByteStr',
		BYTE_SIZEDARR
		),SF_I2 : (
		'WordStr',
		WORD_SIZEDARR
		),SF_I4 : (
		'LongStr',
		DWORD_SIZEDARR
		),SF_I8 : (
		'HyperStr',
		HYPER_SIZEDARR
		)}


class SAFEARRAYUNION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sfType',
			UNSIGNED_LONG
			),
			(
			'Anonymous3',
			ANONYMOUS3
			)
		)


class SAFEARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cDims',
			USHORT
			),
			(
			'fFeatures',
			USHORT
			),
			(
			'cbElements',
			ULONG
			),
			(
			'cLocks',
			ULONG
			),
			(
			'uArrayStructs',
			SAFEARRAYUNION
			),
			(
			'rgsabound',
			SAFEARRAYBOUND
			)
		)


class RECORDINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'libraryGuid',
			GUID
			),
			(
			'verMajor',
			DWORD
			),
			(
			'recGuid',
			GUID
			),
			(
			'verMinor',
			DWORD
			),
			(
			'Lcid',
			DWORD
			)
		)


DISPID = LONG
class DATA_DISPPARAMS(NDRUniConformantArray):
	item = DISPID


class PTR_DISPPARAMS(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DISPPARAMS
			)
		)


class DISPPARAMS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'rgvarg',
			VARIANT
			),
			(
			'rgdispidNamedArgs',
			PTR_DISPPARAMS
			),
			(
			'cArgs',
			UINT
			),
			(
			'cNamedArgs',
			UINT
			)
		)


class EXCEPINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wCode',
			WORD
			),
			(
			'wReserved',
			WORD
			),
			(
			'bstrSource',
			BSTR
			),
			(
			'bstrDescription',
			BSTR
			),
			(
			'bstrHelpFile',
			BSTR
			),
			(
			'dwHelpContext',
			DWORD
			),
			(
			'pvReserved',
			ULONG_PTR
			),
			(
			'pfnDeferredFillIn',
			ULONG_PTR
			),
			(
			'scode',
			HRESULT
			)
		)


MEMBERID = DISPID
HREFTYPE = DWORD
class LPTDESC(NDRSTRUCT):
	align = 1
	structure = (

		)


class LPADESC(NDRSTRUCT):
	align = 1
	structure = (

		)


class _TDUNION(NDRUNION):
	union = {VT_USERDEFINED : (
		'*lptdesc',
		LPTDESC
		),VT_USERDEFINED : (
		'*lpadesc',
		LPADESC
		),VT_USERDEFINED : (
		'hreftype',
		HREFTYPE
		)}


class TYPEDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'_tdUnion',
			_TDUNION
			),
			(
			'vt',
			USHORT
			)
		)


class ARRAYDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tdescElem',
			TYPEDESC
			),
			(
			'cDims',
			USHORT
			),
			(
			'rgbounds',
			SAFEARRAYBOUND
			)
		)


class PARAMDESCEX(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cBytes',
			ULONG
			),
			(
			'varDefaultValue',
			VARIANT
			)
		)


class PARAMDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pparamdescex',
			PARAMDESCEX
			),
			(
			'wParamFlags',
			USHORT
			)
		)


class ELEMDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tdesc',
			TYPEDESC
			),
			(
			'paramdesc',
			PARAMDESC
			)
		)


class DATA_FUNCDESC(NDRUniConformantArray):
	item = ELEMDESC


class PTR_FUNCDESC(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_FUNCDESC
			)
		)


class FUNCDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'lReserved1',
			SCODE
			),
			(
			'lprgelemdescParam',
			PTR_FUNCDESC
			),
			(
			'funckind',
			FUNCKIND
			),
			(
			'invkind',
			INVOKEKIND
			),
			(
			'callconv',
			CALLCONV
			),
			(
			'cParams',
			SHORT
			),
			(
			'cParamsOpt',
			SHORT
			),
			(
			'oVft',
			SHORT
			),
			(
			'cReserved2',
			SHORT
			),
			(
			'elemdescFunc',
			ELEMDESC
			),
			(
			'wFuncFlags',
			WORD
			)
		)


class _VDUNION(NDRUNION):
	union = {VAR_PERINSTANCE : (
		'oInst',
		ULONG
		),VAR_CONST : (
		'lpvarValue',
		VARIANT
		)}


class VARDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'lpstrReserved',
			LPOLESTR
			),
			(
			'_vdUnion',
			_VDUNION
			),
			(
			'elemdescVar',
			ELEMDESC
			),
			(
			'wVarFlags',
			WORD
			),
			(
			'varkind',
			VARKIND
			)
		)


class LPVARDESC(NDRPOINTER):
	referent = (
			(
			'Data',
			VARDESC
			)
		)


class TYPEATTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'guid',
			GUID
			),
			(
			'lcid',
			LCID
			),
			(
			'dwReserved1',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			),
			(
			'dwReserved3',
			DWORD
			),
			(
			'lpstrReserved4',
			LPOLESTR
			),
			(
			'cbSizeInstance',
			ULONG
			),
			(
			'typekind',
			TYPEKIND
			),
			(
			'cFuncs',
			WORD
			),
			(
			'cVars',
			WORD
			),
			(
			'cImplTypes',
			WORD
			),
			(
			'cbSizeVft',
			WORD
			),
			(
			'cbAlignment',
			WORD
			),
			(
			'wTypeFlags',
			WORD
			),
			(
			'wMajorVerNum',
			WORD
			),
			(
			'wMinorVerNum',
			WORD
			),
			(
			'tdescAlias',
			TYPEDESC
			),
			(
			'dwReserved5',
			DWORD
			),
			(
			'wReserved6',
			WORD
			)
		)


class LPTYPEATTR(NDRPOINTER):
	referent = (
			(
			'Data',
			TYPEATTR
			)
		)


class TLIBATTR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'guid',
			GUID
			),
			(
			'lcid',
			LCID
			),
			(
			'syskind',
			SYSKIND
			),
			(
			'wMajorVerNum',
			UNSIGNED_SHORT
			),
			(
			'wMinorVerNum',
			UNSIGNED_SHORT
			),
			(
			'wLibFlags',
			UNSIGNED_SHORT
			)
		)


class LPTLIBATTR(NDRPOINTER):
	referent = (
			(
			'Data',
			TLIBATTR
			)
		)


class CUSTDATAITEM(NDRSTRUCT):
	align = 1
	structure = (
			(
			'guid',
			GUID
			),
			(
			'varValue',
			VARIANT
			)
		)


class DATA_CUSTDATA(NDRUniConformantArray):
	item = CUSTDATAITEM


class PTR_CUSTDATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CUSTDATA
			)
		)


class CUSTDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cCustData',
			DWORD
			),
			(
			'prgCustData',
			PTR_CUSTDATA
			)
		)


#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#IDispatch Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ITypeLib Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ITypeInfo Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDispatch Definition
#################################################################################
MSRPC_UUID_IDISPATCH = uuidtup_to_bin(('00020400-0000-0000-C000-000000000046','0.0'))
DISPATCH_METHOD =  DWORD
DISPATCH_PROPERTYGET =  DWORD
DISPATCH_PROPERTYPUT =  DWORD
DISPATCH_PROPERTYPUTREF =  DWORD
DISPATCH_zeroVarResult =  DWORD
DISPATCH_zeroExcepInfo =  DWORD
DISPATCH_zeroArgErr =  DWORD
DISPID_VALUE =  DISPID
DISPID_UNKNOWN =  DISPID
DISPID_PROPERTYPUT =  DISPID
DISPID_NEWENUM =  DISPID
LPDISPATCH = IDISPATCH
class GetTypeInfoCount(NDRCALL):
	OPNUM = 0
	structure = (

		)


class GetTypeInfoCountResponse(NDRCALL):
	structure = (

		)


class GetTypeInfo(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'iTInfo',
			UINT
			),
			(
			'lcid',
			LCID
			)
		)


class GetTypeInfoResponse(NDRCALL):
	structure = (
			(
			'iTInfo',
			UINT
			),
			(
			'lcid',
			LCID
			)
		)


class GetIDsOfNames(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'riid',
			REFIID
			),
			(
			'rgszNames',
			LPOLESTR
			),
			(
			'cNames',
			UINT
			),
			(
			'lcid',
			LCID
			)
		)


class GetIDsOfNamesResponse(NDRCALL):
	structure = (
			(
			'riid',
			REFIID
			),
			(
			'rgszNames',
			LPOLESTR
			),
			(
			'cNames',
			UINT
			),
			(
			'lcid',
			LCID
			)
		)


class Invoke(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'dispIdMember',
			DISPID
			),
			(
			'riid',
			REFIID
			),
			(
			'lcid',
			LCID
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'pDispParams',
			DISPPARAMS
			),
			(
			'cVarRef',
			UINT
			),
			(
			'rgVarRefIdx',
			UINT
			),
			(
			'rgVarRef',
			VARIANT
			)
		)


class InvokeResponse(NDRCALL):
	structure = (
			(
			'dispIdMember',
			DISPID
			),
			(
			'riid',
			REFIID
			),
			(
			'lcid',
			LCID
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'pDispParams',
			DISPPARAMS
			),
			(
			'cVarRef',
			UINT
			),
			(
			'rgVarRefIdx',
			UINT
			),
			(
			'rgVarRef',
			VARIANT
			)
		)


OPNUMS = {0 : (
	GetTypeInfoCount,
	GetTypeInfoCountResponse
	),1 : (
	GetTypeInfo,
	GetTypeInfoResponse
	),2 : (
	GetIDsOfNames,
	GetIDsOfNamesResponse
	),3 : (
	Invoke,
	InvokeResponse
	)}
#################################################################################
#IEnumVARIANT Definition
#################################################################################
MSRPC_UUID_IENUMVARIANT = uuidtup_to_bin(('00020404-0000-0000-C000-000000000046','0.0'))
class Next(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'celt',
			ULONG
			)
		)


class NextResponse(NDRCALL):
	structure = (
			(
			'celt',
			ULONG
			)
		)


class Skip(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'celt',
			ULONG
			)
		)


class SkipResponse(NDRCALL):
	structure = (
			(
			'celt',
			ULONG
			)
		)


class Reset(NDRCALL):
	OPNUM = 2
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Clone(NDRCALL):
	OPNUM = 3
	structure = (

		)


class CloneResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Next,
	NextResponse
	),1 : (
	Skip,
	SkipResponse
	),2 : (
	Reset,
	ResetResponse
	),3 : (
	Clone,
	CloneResponse
	)}
#################################################################################
#ITypeComp Definition
#################################################################################
MSRPC_UUID_ITYPECOMP = uuidtup_to_bin(('00020403-0000-0000-C000-000000000046','0.0'))
class Bind(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'szName',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			),
			(
			'wFlags',
			WORD
			)
		)


class BindResponse(NDRCALL):
	structure = (
			(
			'szName',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			),
			(
			'wFlags',
			WORD
			)
		)


class BindType(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'szName',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			)
		)


class BindTypeResponse(NDRCALL):
	structure = (
			(
			'szName',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			)
		)


OPNUMS = {0 : (
	Bind,
	BindResponse
	),1 : (
	BindType,
	BindTypeResponse
	)}
#################################################################################
#ITypeInfo Definition
#################################################################################
MSRPC_UUID_ITYPEINFO = uuidtup_to_bin(('00020401-0000-0000-C000-000000000046','0.0'))
class GetTypeAttr(NDRCALL):
	OPNUM = 0
	structure = (

		)


class GetTypeAttrResponse(NDRCALL):
	structure = (

		)


class GetTypeComp(NDRCALL):
	OPNUM = 1
	structure = (

		)


class GetTypeCompResponse(NDRCALL):
	structure = (

		)


class GetFuncDesc(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'index',
			UINT
			)
		)


class GetFuncDescResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetVarDesc(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'index',
			UINT
			)
		)


class GetVarDescResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetNames(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'cMaxNames',
			UINT
			)
		)


class GetNamesResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'cMaxNames',
			UINT
			)
		)


class GetRefTypeOfImplType(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'index',
			UINT
			)
		)


class GetRefTypeOfImplTypeResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetImplTypeFlags(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'index',
			UINT
			)
		)


class GetImplTypeFlagsResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class Opnum10NotUsedOnWire(NDRCALL):
	OPNUM = 7
	structure = (

		)


class Opnum10NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum11NotUsedOnWire(NDRCALL):
	OPNUM = 8
	structure = (

		)


class Opnum11NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class GetDocumentation(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDocumentationResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDllEntry(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'invKind',
			INVOKEKIND
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDllEntryResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'invKind',
			INVOKEKIND
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetRefTypeInfo(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'hRefType',
			HREFTYPE
			)
		)


class GetRefTypeInfoResponse(NDRCALL):
	structure = (
			(
			'hRefType',
			HREFTYPE
			)
		)


class Opnum15NotUsedOnWire(NDRCALL):
	OPNUM = 12
	structure = (

		)


class Opnum15NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class CreateInstance(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'riid',
			REFIID
			)
		)


class CreateInstanceResponse(NDRCALL):
	structure = (
			(
			'riid',
			REFIID
			)
		)


class GetMops(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'memid',
			MEMBERID
			)
		)


class GetMopsResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			)
		)


class GetContainingTypeLib(NDRCALL):
	OPNUM = 15
	structure = (

		)


class GetContainingTypeLibResponse(NDRCALL):
	structure = (

		)


class Opnum19NotUsedOnWire(NDRCALL):
	OPNUM = 16
	structure = (

		)


class Opnum19NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum20NotUsedOnWire(NDRCALL):
	OPNUM = 17
	structure = (

		)


class Opnum20NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum21NotUsedOnWire(NDRCALL):
	OPNUM = 18
	structure = (

		)


class Opnum21NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	GetTypeAttr,
	GetTypeAttrResponse
	),1 : (
	GetTypeComp,
	GetTypeCompResponse
	),2 : (
	GetFuncDesc,
	GetFuncDescResponse
	),3 : (
	GetVarDesc,
	GetVarDescResponse
	),4 : (
	GetNames,
	GetNamesResponse
	),5 : (
	GetRefTypeOfImplType,
	GetRefTypeOfImplTypeResponse
	),6 : (
	GetImplTypeFlags,
	GetImplTypeFlagsResponse
	),7 : (
	Opnum10NotUsedOnWire,
	Opnum10NotUsedOnWireResponse
	),8 : (
	Opnum11NotUsedOnWire,
	Opnum11NotUsedOnWireResponse
	),9 : (
	GetDocumentation,
	GetDocumentationResponse
	),10 : (
	GetDllEntry,
	GetDllEntryResponse
	),11 : (
	GetRefTypeInfo,
	GetRefTypeInfoResponse
	),12 : (
	Opnum15NotUsedOnWire,
	Opnum15NotUsedOnWireResponse
	),13 : (
	CreateInstance,
	CreateInstanceResponse
	),14 : (
	GetMops,
	GetMopsResponse
	),15 : (
	GetContainingTypeLib,
	GetContainingTypeLibResponse
	),16 : (
	Opnum19NotUsedOnWire,
	Opnum19NotUsedOnWireResponse
	),17 : (
	Opnum20NotUsedOnWire,
	Opnum20NotUsedOnWireResponse
	),18 : (
	Opnum21NotUsedOnWire,
	Opnum21NotUsedOnWireResponse
	)}
#################################################################################
#ITypeInfo2 Definition
#################################################################################
MSRPC_UUID_ITYPEINFO2 = uuidtup_to_bin(('00020412-0000-0000-C000-000000000046','0.0'))
class GetTypeKind(NDRCALL):
	OPNUM = 0
	structure = (

		)


class GetTypeKindResponse(NDRCALL):
	structure = (

		)


class GetTypeFlags(NDRCALL):
	OPNUM = 1
	structure = (

		)


class GetTypeFlagsResponse(NDRCALL):
	structure = (

		)


class GetFuncIndexOfMemId(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'invKind',
			INVOKEKIND
			)
		)


class GetFuncIndexOfMemIdResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'invKind',
			INVOKEKIND
			)
		)


class GetVarIndexOfMemId(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'memid',
			MEMBERID
			)
		)


class GetVarIndexOfMemIdResponse(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			)
		)


class GetCustData(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetCustDataResponse(NDRCALL):
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetFuncCustData(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetFuncCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetParamCustData(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'indexFunc',
			UINT
			),
			(
			'indexParam',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetParamCustDataResponse(NDRCALL):
	structure = (
			(
			'indexFunc',
			UINT
			),
			(
			'indexParam',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetVarCustData(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetVarCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetImplTypeCustData(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetImplTypeCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			),
			(
			'guid',
			REFGUID
			)
		)


class GetDocumentation2(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'lcid',
			LCID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDocumentation2Response(NDRCALL):
	structure = (
			(
			'memid',
			MEMBERID
			),
			(
			'lcid',
			LCID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetAllCustData(NDRCALL):
	OPNUM = 10
	structure = (

		)


class GetAllCustDataResponse(NDRCALL):
	structure = (

		)


class GetAllFuncCustData(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'index',
			UINT
			)
		)


class GetAllFuncCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetAllParamCustData(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'indexFunc',
			UINT
			),
			(
			'indexParam',
			UINT
			)
		)


class GetAllParamCustDataResponse(NDRCALL):
	structure = (
			(
			'indexFunc',
			UINT
			),
			(
			'indexParam',
			UINT
			)
		)


class GetAllVarCustData(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'index',
			UINT
			)
		)


class GetAllVarCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetAllImplTypeCustData(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'index',
			UINT
			)
		)


class GetAllImplTypeCustDataResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


OPNUMS = {0 : (
	GetTypeKind,
	GetTypeKindResponse
	),1 : (
	GetTypeFlags,
	GetTypeFlagsResponse
	),2 : (
	GetFuncIndexOfMemId,
	GetFuncIndexOfMemIdResponse
	),3 : (
	GetVarIndexOfMemId,
	GetVarIndexOfMemIdResponse
	),4 : (
	GetCustData,
	GetCustDataResponse
	),5 : (
	GetFuncCustData,
	GetFuncCustDataResponse
	),6 : (
	GetParamCustData,
	GetParamCustDataResponse
	),7 : (
	GetVarCustData,
	GetVarCustDataResponse
	),8 : (
	GetImplTypeCustData,
	GetImplTypeCustDataResponse
	),9 : (
	GetDocumentation2,
	GetDocumentation2Response
	),10 : (
	GetAllCustData,
	GetAllCustDataResponse
	),11 : (
	GetAllFuncCustData,
	GetAllFuncCustDataResponse
	),12 : (
	GetAllParamCustData,
	GetAllParamCustDataResponse
	),13 : (
	GetAllVarCustData,
	GetAllVarCustDataResponse
	),14 : (
	GetAllImplTypeCustData,
	GetAllImplTypeCustDataResponse
	)}
#################################################################################
#ITypeLib Definition
#################################################################################
MSRPC_UUID_ITYPELIB = uuidtup_to_bin(('00020402-0000-0000-C000-000000000046','0.0'))
class GetTypeInfoCount(NDRCALL):
	OPNUM = 0
	structure = (

		)


class GetTypeInfoCountResponse(NDRCALL):
	structure = (

		)


class GetTypeInfo(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			UINT
			)
		)


class GetTypeInfoResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetTypeInfoType(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'index',
			UINT
			)
		)


class GetTypeInfoTypeResponse(NDRCALL):
	structure = (
			(
			'index',
			UINT
			)
		)


class GetTypeInfoOfGuid(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetTypeInfoOfGuidResponse(NDRCALL):
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetLibAttr(NDRCALL):
	OPNUM = 4
	structure = (

		)


class GetLibAttrResponse(NDRCALL):
	structure = (

		)


class GetTypeComp(NDRCALL):
	OPNUM = 5
	structure = (

		)


class GetTypeCompResponse(NDRCALL):
	structure = (

		)


class GetDocumentation(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'index',
			INT
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDocumentationResponse(NDRCALL):
	structure = (
			(
			'index',
			INT
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class IsName(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'szNameBuf',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			)
		)


class IsNameResponse(NDRCALL):
	structure = (
			(
			'szNameBuf',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			)
		)


class FindName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'szNameBuf',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			),
			(
			'pcFound',
			USHORT
			)
		)


class FindNameResponse(NDRCALL):
	structure = (
			(
			'szNameBuf',
			LPOLESTR
			),
			(
			'lHashVal',
			ULONG
			),
			(
			'pcFound',
			USHORT
			)
		)


class Opnum12NotUsedOnWire(NDRCALL):
	OPNUM = 9
	structure = (

		)


class Opnum12NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	GetTypeInfoCount,
	GetTypeInfoCountResponse
	),1 : (
	GetTypeInfo,
	GetTypeInfoResponse
	),2 : (
	GetTypeInfoType,
	GetTypeInfoTypeResponse
	),3 : (
	GetTypeInfoOfGuid,
	GetTypeInfoOfGuidResponse
	),4 : (
	GetLibAttr,
	GetLibAttrResponse
	),5 : (
	GetTypeComp,
	GetTypeCompResponse
	),6 : (
	GetDocumentation,
	GetDocumentationResponse
	),7 : (
	IsName,
	IsNameResponse
	),8 : (
	FindName,
	FindNameResponse
	),9 : (
	Opnum12NotUsedOnWire,
	Opnum12NotUsedOnWireResponse
	)}
#################################################################################
#ITypeLib2 Definition
#################################################################################
MSRPC_UUID_ITYPELIB2 = uuidtup_to_bin(('00020411-0000-0000-C000-000000000046','0.0'))
class GetCustData(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetCustDataResponse(NDRCALL):
	structure = (
			(
			'guid',
			REFGUID
			)
		)


class GetLibStatistics(NDRCALL):
	OPNUM = 1
	structure = (

		)


class GetLibStatisticsResponse(NDRCALL):
	structure = (

		)


class GetDocumentation2(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'index',
			INT
			),
			(
			'lcid',
			LCID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetDocumentation2Response(NDRCALL):
	structure = (
			(
			'index',
			INT
			),
			(
			'lcid',
			LCID
			),
			(
			'refPtrFlags',
			DWORD
			)
		)


class GetAllCustData(NDRCALL):
	OPNUM = 3
	structure = (

		)


class GetAllCustDataResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	GetCustData,
	GetCustDataResponse
	),1 : (
	GetLibStatistics,
	GetLibStatisticsResponse
	),2 : (
	GetDocumentation2,
	GetDocumentation2Response
	),3 : (
	GetAllCustData,
	GetAllCustDataResponse
	)}
#################################################################################
#TYPEDEFS
#################################################################################
class BOID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'rgb',
			UNSIGNED_CHAR
			)
		)


class XACTTRANSINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'uow',
			BOID
			),
			(
			'isoLevel',
			LONG
			),
			(
			'isoFlags',
			ULONG
			),
			(
			'grfTCSupported',
			DWORD
			),
			(
			'grfRMSupported',
			DWORD
			),
			(
			'grfTCSupportedRetaining',
			DWORD
			),
			(
			'grfRMSupportedRetaining',
			DWORD
			)
		)


XACTTC = DWORD__ENUM
XACTTC_NONE = 0
XACTTC_SYNC_PHASEONE = 1
XACTTC_SYNC_PHASETWO = 2
XACTTC_SYNC = 2
XACTTC_ASYNC_PHASEONE = 4
XACTTC_ASYNC = 4
MQCALG = DWORD__ENUM
MQMSG_CALG_MD2 = 32769
MQMSG_CALG_MD4 = 32770
MQMSG_CALG_MD5 = 32771
MQMSG_CALG_SHA = 32772
MQMSG_CALG_SHA1 = 32772
MQMSG_CALG_MAC = 32773
MQMSG_CALG_RSA_SIGN = 9216
MQMSG_CALG_DSS_SIGN = 8704
MQMSG_CALG_RSA_KEYX = 41984
MQMSG_CALG_DES = 26113
MQMSG_CALG_RC2 = 26114
MQMSG_CALG_RC4 = 26625
MQMSG_CALG_SEAL = 26626
MQTRANSACTION = DWORD__ENUM
MQ_NO_TRANSACTION = 0
MQ_MTS_TRANSACTION = 1
MQ_XA_TRANSACTION = 2
MQ_SINGLE_MESSAGE = 3
RELOPS = DWORD__ENUM
REL_NOP = 0
REL_EQ = 0
REL_NEQ = 0
REL_LT = 0
REL_GT = 0
REL_LE = 0
MQCERT_REGISTER = DWORD__ENUM
MQCERT_REGISTER_ALWAYS = 1
MQCERT_REGISTER_IF_NOT_EXIST = 2
MQMSGCURSOR = DWORD__ENUM
MQMSG_FIRST = 0
MQMSG_CURRENT = 1
MQMSG_NEXT = 2
MQMSGCLASS = DWORD__ENUM
MQMSG_CLASS_NORMAL = 0
MQMSG_CLASS_REPORT = 1
MQMSG_CLASS_ACK_REACH_QUEUE = 2
MQMSG_CLASS_ACK_RECEIVE = 16384
MQMSG_CLASS_NACK_BAD_DST_Q = 32768
MQMSG_CLASS_NACK_PURGED = 32769
MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT = 32770
MQMSG_CLASS_NACK_Q_EXCEED_QUOTA = 32771
MQMSG_CLASS_NACK_ACCESS_DENIED = 32772
MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED = 32773
MQMSG_CLASS_NACK_BAD_SIGNATURE = 32774
MQMSG_CLASS_NACK_BAD_ENCRYPTION = 32775
MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT = 32776
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q = 32777
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG = 32778
MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER = 32779
MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED = 32780
MQMSG_CLASS_NACK_Q_DELETED = 49152
MQMSG_CLASS_NACK_Q_PURGED = 49153
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT = 49154
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER = 49155
MQMSGDELIVERY = DWORD__ENUM
MQMSG_DELIVERY_EXPRESS = 0
MQMSG_DELIVERY_RECOVERABLE = 1
MQMSGACKNOWLEDGEMENT = DWORD__ENUM
MQMSG_ACKNOWLEDGMENT_NONE = 0
MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL = 1
MQMSG_ACKNOWLEDGMENT_POS_RECEIVE = 2
MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL = 4
MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE = 8
MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE = 4
MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE = 5
MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE = 12
MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE = 14
MQMSGJOURNAL = DWORD__ENUM
MQMSG_JOURNAL_NONE = 0
MQMSG_DEADLETTER = 1
MQMSG_JOURNAL = 2
MQMSGTRACE = DWORD__ENUM
MQMSG_TRACE_NONE = 0
MQMSG_SEND_ROUTE_TO_REPORT_QUEUE = 1
MQMSGSENDERIDTYPE = DWORD__ENUM
MQMSG_SENDERID_TYPE_NONE = 0
MQMSG_SENDERID_TYPE_SID = 1
MQMSGPRIVLEVEL = DWORD__ENUM
MQMSG_PRIV_LEVEL_NONE = 0
MQMSG_PRIV_LEVEL_BODY_BASE = 1
MQMSG_PRIV_LEVEL_BODY_ENHANCED = 3
MQMSGAUTHLEVEL = DWORD__ENUM
MQMSG_AUTH_LEVEL_NONE = 0
MQMSG_AUTH_LEVEL_ALWAYS = 1
MQMSG_AUTH_LEVEL_MSMQ10 = 2
MQMSG_AUTH_LEVEL_SIG10 = 2
MQMSG_AUTH_LEVEL_MSMQ20 = 4
MQMSG_AUTH_LEVEL_SIG20 = 4
MQMSG_AUTH_LEVEL_SIG30 = 8
MQMSGIDSIZE = DWORD__ENUM
MQMSG_MSGID_SIZE = 20
MQMSG_CORRELATIONID_SIZE = 20
MQMSG_XACTID_SIZE = 20
MQMSGMAX = DWORD__ENUM
MQ_MAX_MSG_LABEL_LEN = 249
MQMSGAUTHENTICATION = DWORD__ENUM
MQMSG_AUTHENTICATION_NOT_REQUESTED = 0
MQMSG_AUTHENTICATION_REQUESTED = 1
MQMSG_AUTHENTICATED_SIG10 = 1
MQMSG_AUTHENTICATION_REQUESTED_EX = 3
MQMSG_AUTHENTICATED_SIG20 = 3
MQMSG_AUTHENTICATED_SIG30 = 5
MQMSG_AUTHENTICATED_SIGXML = 9
MQSHARE = DWORD__ENUM
MQ_DENY_NONE = 0
MQ_DENY_RECEIVE_SHARE = 1
MQACCESS = DWORD__ENUM
MQ_RECEIVE_ACCESS = 1
MQ_SEND_ACCESS = 2
MQ_PEEK_ACCESS = 32
MQ_ADMIN_ACCESS = 128
MQJOURNAL = DWORD__ENUM
MQ_JOURNAL_NONE = 0
MQ_JOURNAL = 1
MQTRANSACTIONAL = DWORD__ENUM
MQ_TRANSACTIONAL_NONE = 0
MQ_TRANSACTIONAL = 1
MQAUTHENTICATE = DWORD__ENUM
MQ_AUTHENTICATE_NONE = 0
MQ_AUTHENTICATE = 1
MQPRIVLEVEL = DWORD__ENUM
MQ_PRIV_LEVEL_NONE = 0
MQ_PRIV_LEVEL_OPTIONAL = 1
MQ_PRIV_LEVEL_BODY = 2
MQPRIORITY = DWORD__ENUM
MQ_MIN_PRIORITY = 0
MQ_MAX_PRIORITY = 7
MQMAX = DWORD__ENUM
MQ_MAX_Q_NAME_LEN = 124
MQ_MAX_Q_LABEL_LEN = 124
QUEUE_TYPE = DWORD__ENUM
MQ_TYPE_PUBLIC = 0
MQ_TYPE_PRIVATE = 1
MQ_TYPE_MACHINE = 2
MQ_TYPE_CONNECTOR = 3
FOREIGN_STATUS = DWORD__ENUM
MQ_STATUS_FOREIGN = 0
MQ_STATUS_NOT_FOREIGN = 1
XACT_STATUS = DWORD__ENUM
MQ_XACT_STATUS_XACT = 0
MQ_XACT_STATUS_NOT_XACT = 1
QUEUE_STATE = DWORD__ENUM
MQ_QUEUE_STATE_LOCAL_CONNECTION = 0
MQ_QUEUE_STATE_DISCONNECTED = 1
MQ_QUEUE_STATE_WAITING = 2
MQ_QUEUE_STATE_NEEDVALIDATE = 3
MQ_QUEUE_STATE_ONHOLD = 4
MQ_QUEUE_STATE_NONACTIVE = 5
MQ_QUEUE_STATE_CONNECTED = 6
MQ_QUEUE_STATE_DISCONNECTING = 7
MQDEFAULT = DWORD__ENUM
DEFAULT_M_PRIORITY = 3
DEFAULT_M_DELIVERY = 0
DEFAULT_M_ACKNOWLEDGE = 0
DEFAULT_M_JOURNAL = 0
DEFAULT_M_APPSPECIFIC = 0
DEFAULT_M_PRIV_LEVEL = 0
DEFAULT_M_AUTH_LEVEL = 0
DEFAULT_M_SENDERID_TYPE = 1
DEFAULT_Q_JOURNAL = 0
DEFAULT_Q_BASEPRIORITY = 0
DEFAULT_Q_QUOTA = 4294967295
DEFAULT_Q_JOURNAL_QUOTA = 4294967295
DEFAULT_Q_TRANSACTION = 0
DEFAULT_Q_AUTHENTICATE = 0
DEFAULT_Q_PRIV_LEVEL = 1
DEFAULT_M_LOOKUPID = 0
MQERROR = DWORD__ENUM
MQ_ERROR = 3222142977
MQ_ERROR_PROPERTY = 3222142978
MQ_ERROR_QUEUE_NOT_FOUND = 3222142979
MQ_ERROR_QUEUE_NOT_ACTIVE = 3222142980
MQ_ERROR_QUEUE_EXISTS = 3222142981
MQ_ERROR_INVALID_PARAMETER = 3222142982
MQ_ERROR_INVALID_HANDLE = 3222142983
MQ_ERROR_OPERATION_CANCELLED = 3222142984
MQ_ERROR_SHARING_VIOLATION = 3222142985
MQ_ERROR_SERVICE_NOT_AVAILABLE = 3222142987
MQ_ERROR_MACHINE_NOT_FOUND = 3222142989
MQ_ERROR_ILLEGAL_SORT = 3222142992
MQ_ERROR_ILLEGAL_USER = 3222142993
MQ_ERROR_NO_DS = 3222142995
MQ_ERROR_ILLEGAL_QUEUE_PATHNAME = 3222142996
MQ_ERROR_ILLEGAL_PROPERTY_VALUE = 3222143000
MQ_ERROR_ILLEGAL_PROPERTY_VT = 3222143001
MQ_ERROR_BUFFER_OVERFLOW = 3222143002
MQ_ERROR_IO_TIMEOUT = 3222143003
MQ_ERROR_ILLEGAL_CURSOR_ACTION = 3222143004
MQ_ERROR_MESSAGE_ALREADY_RECEIVED = 3222143005
MQ_ERROR_ILLEGAL_FORMATNAME = 3222143006
MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL = 3222143007
MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION = 3222143008
MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR = 3222143009
MQ_ERROR_SENDERID_BUFFER_TOO_SMALL = 3222143010
MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL = 3222143011
MQ_ERROR_CANNOT_IMPERSONATE_CLIENT = 3222143012
MQ_ERROR_ACCESS_DENIED = 3222143013
MQ_ERROR_PRIVILEGE_NOT_HELD = 3222143014
MQ_ERROR_INSUFFICIENT_RESOURCES = 3222143015
MQ_ERROR_USER_BUFFER_TOO_SMALL = 3222143016
MQ_ERROR_MESSAGE_STORAGE_FAILED = 3222143018
MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL = 3222143019
MQ_ERROR_INVALID_CERTIFICATE = 3222143020
MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE = 3222143021
MQ_ERROR_INTERNAL_USER_CERT_EXIST = 3222143022
MQ_ERROR_NO_INTERNAL_USER_CERT = 3222143023
MQ_ERROR_CORRUPTED_SECURITY_DATA = 3222143024
MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE = 3222143025
MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION = 3222143027
MQ_ERROR_BAD_SECURITY_CONTEXT = 3222143029
MQ_ERROR_COULD_NOT_GET_USER_SID = 3222143030
MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO = 3222143031
MQ_ERROR_ILLEGAL_MQCOLUMNS = 3222143032
MQ_ERROR_ILLEGAL_PROPID = 3222143033
MQ_ERROR_ILLEGAL_RELATION = 3222143034
MQ_ERROR_ILLEGAL_PROPERTY_SIZE = 3222143035
MQ_ERROR_ILLEGAL_RESTRICTION_PROPID = 3222143036
MQ_ERROR_ILLEGAL_MQQUEUEPROPS = 3222143037
MQ_ERROR_PROPERTY_NOTALLOWED = 3222143038
MQ_ERROR_INSUFFICIENT_PROPERTIES = 3222143039
MQ_ERROR_MACHINE_EXISTS = 3222143040
MQ_ERROR_ILLEGAL_MQQMPROPS = 3222143041
MQ_ERROR_DS_IS_FULL = 3222143042
MQ_ERROR_DS_ERROR = 3222143043
MQ_ERROR_INVALID_OWNER = 3222143044
MQ_ERROR_UNSUPPORTED_ACCESS_MODE = 3222143045
MQ_ERROR_RESULT_BUFFER_TOO_SMALL = 3222143046
MQ_ERROR_DELETE_CN_IN_USE = 3222143048
MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER = 3222143049
MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE = 3222143050
MQ_ERROR_QUEUE_NOT_AVAILABLE = 3222143051
MQ_ERROR_DTC_CONNECT = 3222143052
MQ_ERROR_TRANSACTION_IMPORT = 3222143054
MQ_ERROR_TRANSACTION_USAGE = 3222143056
MQ_ERROR_TRANSACTION_SEQUENCE = 3222143057
MQ_ERROR_MISSING_CONNECTOR_TYPE = 3222143061
MQ_ERROR_STALE_HANDLE = 3222143062
MQ_ERROR_TRANSACTION_ENLIST = 3222143064
MQ_ERROR_QUEUE_DELETED = 3222143066
MQ_ERROR_ILLEGAL_CONTEXT = 3222143067
MQ_ERROR_ILLEGAL_SORT_PROPID = 3222143068
MQ_ERROR_LABEL_TOO_LONG = 3222143069
MQ_ERROR_LABEL_BUFFER_TOO_SMALL = 3222143070
MQ_ERROR_MQIS_SERVER_EMPTY = 3222143071
MQ_ERROR_MQIS_READONLY_MODE = 3222143072
MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL = 3222143073
MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL = 3222143074
MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL = 3222143075
MQ_ERROR_ILLEGAL_OPERATION = 3222143076
MQ_ERROR_WRITE_NOT_ALLOWED = 3222143077
MQ_ERROR_WKS_CANT_SERVE_CLIENT = 3222143078
MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW = 3222143079
MQ_CORRUPTED_QUEUE_WAS_DELETED = 3222143080
MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE = 3222143081
MQ_ERROR_UNSUPPORTED_OPERATION = 3222143082
MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED = 3222143083
MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR = 3222143084
MQ_ERROR_CERTIFICATE_NOT_PROVIDED = 3222143085
MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED = 3222143086
MQ_ERROR_CANT_CREATE_CERT_STORE = 3222143087
MQ_ERROR_CANNOT_CREATE_CERT_STORE = 3222143087
MQ_ERROR_CANT_OPEN_CERT_STORE = 3222143088
MQ_ERROR_CANNOT_OPEN_CERT_STORE = 3222143088
MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION = 3222143089
MQ_ERROR_CANNOT_GRANT_ADD_GUID = 3222143090
MQ_ERROR_CANNOT_LOAD_MSMQOCM = 3222143091
MQ_ERROR_NO_ENTRY_POINT_MSMQOCM = 3222143092
MQ_ERROR_NO_MSMQ_SERVERS_ON_DC = 3222143093
MQ_ERROR_CANNOT_JOIN_DOMAIN = 3222143094
MQ_ERROR_CANNOT_CREATE_ON_GC = 3222143095
MQ_ERROR_GUID_NOT_MATCHING = 3222143096
MQ_ERROR_PUBLIC_KEY_NOT_FOUND = 3222143097
MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST = 3222143098
MQ_ERROR_ILLEGAL_MQPRIVATEPROPS = 3222143099
MQ_ERROR_NO_GC_IN_DOMAIN = 3222143100
MQ_ERROR_NO_MSMQ_SERVERS_ON_GC = 3222143101
MQ_ERROR_CANNOT_GET_DN = 3222143102
MQ_ERROR_CANNOT_HASH_DATA_EX = 3222143103
MQ_ERROR_CANNOT_SIGN_DATA_EX = 3222143104
MQ_ERROR_CANNOT_CREATE_HASH_EX = 3222143105
MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX = 3222143106
MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS = 3222143107
MQ_ERROR_NO_MQUSER_OU = 3222143108
MQ_ERROR_CANNOT_LOAD_MQAD = 3222143109
MQ_ERROR_CANNOT_LOAD_MQDSSRV = 3222143110
MQ_ERROR_PROPERTIES_CONFLICT = 3222143111
MQ_ERROR_MESSAGE_NOT_FOUND = 3222143112
MQ_ERROR_CANT_RESOLVE_SITES = 3222143113
MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS = 3222143114
MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER = 3222143115
MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS = 3222143116
MQ_ERROR_MULTI_SORT_KEYS = 3222143117
MQ_ERROR_GC_NEEDED = 3222143118
MQ_ERROR_DS_BIND_ROOT_FOREST = 3222143119
MQ_ERROR_DS_LOCAL_USER = 3222143120
MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED = 3222143121
MQ_ERROR_BAD_XML_FORMAT = 3222143122
MQ_ERROR_UNSUPPORTED_CLASS = 3222143123
MQ_ERROR_UNINITIALIZED_OBJECT = 3222143124
MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS = 3222143125
MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS = 3222143126
MQWARNING = DWORD__ENUM
MQ_INFORMATION_PROPERTY = 1074659329
MQ_INFORMATION_ILLEGAL_PROPERTY = 1074659330
MQ_INFORMATION_PROPERTY_IGNORED = 1074659331
MQ_INFORMATION_UNSUPPORTED_PROPERTY = 1074659332
MQ_INFORMATION_DUPLICATE_PROPERTY = 1074659333
MQ_INFORMATION_OPERATION_PENDING = 1074659334
MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL = 1074659337
MQ_INFORMATION_INTERNAL_USER_CERT_EXIST = 1074659338
MQ_INFORMATION_OWNER_IGNORED = 1074659339
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#ITransaction Definition
#################################################################################
MSRPC_UUID_ITRANSACTION = uuidtup_to_bin(('0fb15084-af41-11ce-bd2b-204c4f4f5020','0.0'))
class Commit(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'fRetaining',
			SHORT
			),
			(
			'grfTC',
			DWORD
			),
			(
			'grfRM',
			DWORD
			)
		)


class CommitResponse(NDRCALL):
	structure = (
			(
			'fRetaining',
			SHORT
			),
			(
			'grfTC',
			DWORD
			),
			(
			'grfRM',
			DWORD
			)
		)


class Abort(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'pboidReason',
			BOID
			),
			(
			'fRetaining',
			SHORT
			),
			(
			'fAsync',
			SHORT
			)
		)


class AbortResponse(NDRCALL):
	structure = (
			(
			'pboidReason',
			BOID
			),
			(
			'fRetaining',
			SHORT
			),
			(
			'fAsync',
			SHORT
			)
		)


class GetTransactionInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class GetTransactionInfoResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Commit,
	CommitResponse
	),1 : (
	Abort,
	AbortResponse
	),2 : (
	GetTransactionInfo,
	GetTransactionInfoResponse
	)}
#################################################################################
#IEnumConnections Definition
#################################################################################
MSRPC_UUID_IENUMCONNECTIONS = uuidtup_to_bin(('B196B287-BAB4-101-B69C-00A00341D07','0.0'))
PENUMCONNECTIONS = IENUMCONNECTIONS
LPENUMCONNECTIONS = IENUMCONNECTIONS
class CONNECTDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pUnk',
			IUNKNOWN
			),
			(
			'dwCookie',
			DWORD
			)
		)


class PCONNECTDATA(NDRSTRUCT):
	align = 1
	structure = (

		)


class LPCONNECTDATA(NDRSTRUCT):
	align = 1
	structure = (

		)


class Next(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class NextResponse(NDRCALL):
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class Skip(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class SkipResponse(NDRCALL):
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class Reset(NDRCALL):
	OPNUM = 2
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Clone(NDRCALL):
	OPNUM = 3
	structure = (

		)


class CloneResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Next,
	NextResponse
	),1 : (
	Skip,
	SkipResponse
	),2 : (
	Reset,
	ResetResponse
	),3 : (
	Clone,
	CloneResponse
	)}
#################################################################################
#IConnectionPointContainer Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IConnectionPoint Definition
#################################################################################
MSRPC_UUID_ICONNECTIONPOINT = uuidtup_to_bin(('B196B286-BAB4-101-B69C-00A00341D07','0.0'))
PCONNECTIONPOINT = ICONNECTIONPOINT
LPCONNECTIONPOINT = ICONNECTIONPOINT
class GetConnectionInterface(NDRCALL):
	OPNUM = 0
	structure = (

		)


class GetConnectionInterfaceResponse(NDRCALL):
	structure = (

		)


class GetConnectionPointContainer(NDRCALL):
	OPNUM = 1
	structure = (

		)


class GetConnectionPointContainerResponse(NDRCALL):
	structure = (

		)


class Advise(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'pUnkSink',
			IUNKNOWN
			)
		)


class AdviseResponse(NDRCALL):
	structure = (
			(
			'pUnkSink',
			IUNKNOWN
			)
		)


class Unadvise(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'dwCookie',
			DWORD
			)
		)


class UnadviseResponse(NDRCALL):
	structure = (
			(
			'dwCookie',
			DWORD
			)
		)


class EnumConnections(NDRCALL):
	OPNUM = 4
	structure = (

		)


class EnumConnectionsResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	GetConnectionInterface,
	GetConnectionInterfaceResponse
	),1 : (
	GetConnectionPointContainer,
	GetConnectionPointContainerResponse
	),2 : (
	Advise,
	AdviseResponse
	),3 : (
	Unadvise,
	UnadviseResponse
	),4 : (
	EnumConnections,
	EnumConnectionsResponse
	)}
#################################################################################
#IEnumConnectionPoints Definition
#################################################################################
MSRPC_UUID_IENUMCONNECTIONPOINTS = uuidtup_to_bin(('B196B285-BAB4-101-B69C-00A00341D07','0.0'))
PENUMCONNECTIONPOINTS = IENUMCONNECTIONPOINTS
LPENUMCONNECTIONPOINTS = IENUMCONNECTIONPOINTS
class Next(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class NextResponse(NDRCALL):
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class Skip(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class SkipResponse(NDRCALL):
	structure = (
			(
			'cConnections',
			ULONG
			)
		)


class Reset(NDRCALL):
	OPNUM = 2
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Clone(NDRCALL):
	OPNUM = 3
	structure = (

		)


class CloneResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Next,
	NextResponse
	),1 : (
	Skip,
	SkipResponse
	),2 : (
	Reset,
	ResetResponse
	),3 : (
	Clone,
	CloneResponse
	)}
#################################################################################
#IConnectionPointContainer Definition
#################################################################################
MSRPC_UUID_ICONNECTIONPOINTCONTAINER = uuidtup_to_bin(('B196B284-BAB4-101-B69C-00A00341D07','0.0'))
PCONNECTIONPOINTCONTAINER = ICONNECTIONPOINTCONTAINER
LPCONNECTIONPOINTCONTAINER = ICONNECTIONPOINTCONTAINER
class EnumConnectionPoints(NDRCALL):
	OPNUM = 0
	structure = (

		)


class EnumConnectionPointsResponse(NDRCALL):
	structure = (

		)


class FindConnectionPoint(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'riid',
			REFIID
			)
		)


class FindConnectionPointResponse(NDRCALL):
	structure = (
			(
			'riid',
			REFIID
			)
		)


OPNUMS = {0 : (
	EnumConnectionPoints,
	EnumConnectionPointsResponse
	),1 : (
	FindConnectionPoint,
	FindConnectionPointResponse
	)}
#################################################################################
#IMSMQQuery Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfo Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfo2 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfo3 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfo4 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueue Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueue2 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueue3 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueue4 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQMessage Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfos Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfos2 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfos3 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQueueInfos4 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQEvent Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQEvent2 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQEvent3 Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQTransaction Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQCoordinatedTransactionDispenser Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQTransactionDispenser Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IMSMQQuery Definition
#################################################################################
MSRPC_UUID_IMSMQQUERY = uuidtup_to_bin(('D7D6E072-DCCD-110-AA4B-0060970EBAE','0.0'))
class LookupQueue(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class LookupQueueResponse(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


OPNUMS = {0 : (
	LookupQueue,
	LookupQueueResponse
	)}
#################################################################################
#IMSMQQuery2 Definition
#################################################################################
MSRPC_UUID_IMSMQQUERY2 = uuidtup_to_bin(('eba96b0e-2168-113-898-00020746','0.0'))
class LookupQueue(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class LookupQueueResponse(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	LookupQueue,
	LookupQueueResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQQuery3 Definition
#################################################################################
MSRPC_UUID_IMSMQQUERY3 = uuidtup_to_bin(('eba96b19-2168-113-898-00020746','0.0'))
class LookupQueue_v2(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class LookupQueue_v2Response(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class LookupQueue(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			),
			(
			'MulticastAddress',
			VARIANT
			),
			(
			'RelMulticastAddress',
			VARIANT
			)
		)


class LookupQueueResponse(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			),
			(
			'MulticastAddress',
			VARIANT
			),
			(
			'RelMulticastAddress',
			VARIANT
			)
		)


OPNUMS = {0 : (
	LookupQueue_v2,
	LookupQueue_v2Response
	),1 : (
	Properties,
	PropertiesResponse
	),2 : (
	LookupQueue,
	LookupQueueResponse
	)}
#################################################################################
#IMSMQQuery4 Definition
#################################################################################
MSRPC_UUID_IMSMQQUERY4 = uuidtup_to_bin(('eba96b24-2168-113-898-00020746','0.0'))
class LookupQueue_v2(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class LookupQueue_v2Response(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class LookupQueue(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			),
			(
			'MulticastAddress',
			VARIANT
			),
			(
			'RelMulticastAddress',
			VARIANT
			)
		)


class LookupQueueResponse(NDRCALL):
	structure = (
			(
			'QueueGuid',
			VARIANT
			),
			(
			'ServiceTypeGuid',
			VARIANT
			),
			(
			'Label',
			VARIANT
			),
			(
			'CreateTime',
			VARIANT
			),
			(
			'ModifyTime',
			VARIANT
			),
			(
			'RelServiceType',
			VARIANT
			),
			(
			'RelLabel',
			VARIANT
			),
			(
			'RelCreateTime',
			VARIANT
			),
			(
			'RelModifyTime',
			VARIANT
			),
			(
			'MulticastAddress',
			VARIANT
			),
			(
			'RelMulticastAddress',
			VARIANT
			)
		)


OPNUMS = {0 : (
	LookupQueue_v2,
	LookupQueue_v2Response
	),1 : (
	Properties,
	PropertiesResponse
	),2 : (
	LookupQueue,
	LookupQueueResponse
	)}
#################################################################################
#IMSMQMessage Definition
#################################################################################
MSRPC_UUID_IMSMQMESSAGE = uuidtup_to_bin(('D7D6E074-DCCD-110-AA4B-0060970EBAE','0.0'))
class Class(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ClassResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class AuthLevel(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AuthLevelResponse(NDRCALL):
	structure = (

		)


class AuthLevel(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class AuthLevelResponse(NDRCALL):
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class IsAuthenticated(NDRCALL):
	OPNUM = 5
	structure = (

		)


class IsAuthenticatedResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DeliveryResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class DeliveryResponse(NDRCALL):
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class Trace(NDRCALL):
	OPNUM = 8
	structure = (

		)


class TraceResponse(NDRCALL):
	structure = (

		)


class Trace(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class TraceResponse(NDRCALL):
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class Priority(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PriorityResponse(NDRCALL):
	structure = (

		)


class Priority(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class PriorityResponse(NDRCALL):
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 14
	structure = (

		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class AppSpecific(NDRCALL):
	OPNUM = 16
	structure = (

		)


class AppSpecificResponse(NDRCALL):
	structure = (

		)


class AppSpecific(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class AppSpecificResponse(NDRCALL):
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class SourceMachineGuid(NDRCALL):
	OPNUM = 18
	structure = (

		)


class SourceMachineGuidResponse(NDRCALL):
	structure = (

		)


class BodyLength(NDRCALL):
	OPNUM = 19
	structure = (

		)


class BodyLengthResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 20
	structure = (

		)


class BodyResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class BodyResponse(NDRCALL):
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 22
	structure = (

		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (

		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class Id(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 25
	structure = (

		)


class CorrelationIdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class CorrelationIdResponse(NDRCALL):
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class Ack(NDRCALL):
	OPNUM = 27
	structure = (

		)


class AckResponse(NDRCALL):
	structure = (

		)


class Ack(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'lAck',
			LONG
			)
		)


class AckResponse(NDRCALL):
	structure = (
			(
			'lAck',
			LONG
			)
		)


class Label(NDRCALL):
	OPNUM = 29
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 31
	structure = (

		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 33
	structure = (

		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class HashAlgorithm(NDRCALL):
	OPNUM = 35
	structure = (

		)


class HashAlgorithmResponse(NDRCALL):
	structure = (

		)


class HashAlgorithm(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class HashAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 37
	structure = (

		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (

		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class SentTime(NDRCALL):
	OPNUM = 39
	structure = (

		)


class SentTimeResponse(NDRCALL):
	structure = (

		)


class ArrivedTime(NDRCALL):
	OPNUM = 40
	structure = (

		)


class ArrivedTimeResponse(NDRCALL):
	structure = (

		)


class DestinationQueueInfo(NDRCALL):
	OPNUM = 41
	structure = (

		)


class DestinationQueueInfoResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 42
	structure = (

		)


class SenderCertificateResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderCertificateResponse(NDRCALL):
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderId(NDRCALL):
	OPNUM = 44
	structure = (

		)


class SenderIdResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 45
	structure = (

		)


class SenderIdTypeResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class SenderIdTypeResponse(NDRCALL):
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class Send(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'DestinationQueue',
			IMSMQQUEUE
			),
			(
			'Transaction',
			VARIANT
			)
		)


class SendResponse(NDRCALL):
	structure = (
			(
			'DestinationQueue',
			IMSMQQUEUE
			),
			(
			'Transaction',
			VARIANT
			)
		)


class AttachCurrentSecurityContext(NDRCALL):
	OPNUM = 48
	structure = (

		)


class AttachCurrentSecurityContextResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Class,
	ClassResponse
	),1 : (
	PrivLevel,
	PrivLevelResponse
	),2 : (
	AuthLevel,
	AuthLevelResponse
	),3 : (
	IsAuthenticated,
	IsAuthenticatedResponse
	),4 : (
	Delivery,
	DeliveryResponse
	),5 : (
	Trace,
	TraceResponse
	),6 : (
	Priority,
	PriorityResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	ResponseQueueInfo,
	ResponseQueueInfoResponse
	),9 : (
	AppSpecific,
	AppSpecificResponse
	),10 : (
	SourceMachineGuid,
	SourceMachineGuidResponse
	),11 : (
	BodyLength,
	BodyLengthResponse
	),12 : (
	Body,
	BodyResponse
	),13 : (
	AdminQueueInfo,
	AdminQueueInfoResponse
	),14 : (
	Id,
	IdResponse
	),15 : (
	CorrelationId,
	CorrelationIdResponse
	),16 : (
	Ack,
	AckResponse
	),17 : (
	Label,
	LabelResponse
	),18 : (
	MaxTimeToReachQueue,
	MaxTimeToReachQueueResponse
	),19 : (
	MaxTimeToReceive,
	MaxTimeToReceiveResponse
	),20 : (
	HashAlgorithm,
	HashAlgorithmResponse
	),21 : (
	EncryptAlgorithm,
	EncryptAlgorithmResponse
	),22 : (
	SentTime,
	SentTimeResponse
	),23 : (
	ArrivedTime,
	ArrivedTimeResponse
	),24 : (
	DestinationQueueInfo,
	DestinationQueueInfoResponse
	),25 : (
	SenderCertificate,
	SenderCertificateResponse
	),26 : (
	SenderId,
	SenderIdResponse
	),27 : (
	SenderIdType,
	SenderIdTypeResponse
	),28 : (
	Send,
	SendResponse
	),29 : (
	AttachCurrentSecurityContext,
	AttachCurrentSecurityContextResponse
	)}
#################################################################################
#IMSMQMessage2 Definition
#################################################################################
MSRPC_UUID_IMSMQMESSAGE2 = uuidtup_to_bin(('D9933BE0-A567-112-B0F3-00020746','0.0'))
class Class(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ClassResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class AuthLevel(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AuthLevelResponse(NDRCALL):
	structure = (

		)


class AuthLevel(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class AuthLevelResponse(NDRCALL):
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class IsAuthenticated(NDRCALL):
	OPNUM = 5
	structure = (

		)


class IsAuthenticatedResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DeliveryResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class DeliveryResponse(NDRCALL):
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class Trace(NDRCALL):
	OPNUM = 8
	structure = (

		)


class TraceResponse(NDRCALL):
	structure = (

		)


class Trace(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class TraceResponse(NDRCALL):
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class Priority(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PriorityResponse(NDRCALL):
	structure = (

		)


class Priority(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class PriorityResponse(NDRCALL):
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 14
	structure = (

		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class AppSpecific(NDRCALL):
	OPNUM = 16
	structure = (

		)


class AppSpecificResponse(NDRCALL):
	structure = (

		)


class AppSpecific(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class AppSpecificResponse(NDRCALL):
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class SourceMachineGuid(NDRCALL):
	OPNUM = 18
	structure = (

		)


class SourceMachineGuidResponse(NDRCALL):
	structure = (

		)


class BodyLength(NDRCALL):
	OPNUM = 19
	structure = (

		)


class BodyLengthResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 20
	structure = (

		)


class BodyResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class BodyResponse(NDRCALL):
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 22
	structure = (

		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class Id(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 25
	structure = (

		)


class CorrelationIdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class CorrelationIdResponse(NDRCALL):
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class Ack(NDRCALL):
	OPNUM = 27
	structure = (

		)


class AckResponse(NDRCALL):
	structure = (

		)


class Ack(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'lAck',
			LONG
			)
		)


class AckResponse(NDRCALL):
	structure = (
			(
			'lAck',
			LONG
			)
		)


class Label(NDRCALL):
	OPNUM = 29
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 31
	structure = (

		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 33
	structure = (

		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class HashAlgorithm(NDRCALL):
	OPNUM = 35
	structure = (

		)


class HashAlgorithmResponse(NDRCALL):
	structure = (

		)


class HashAlgorithm(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class HashAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 37
	structure = (

		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (

		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class SentTime(NDRCALL):
	OPNUM = 39
	structure = (

		)


class SentTimeResponse(NDRCALL):
	structure = (

		)


class ArrivedTime(NDRCALL):
	OPNUM = 40
	structure = (

		)


class ArrivedTimeResponse(NDRCALL):
	structure = (

		)


class DestinationQueueInfo(NDRCALL):
	OPNUM = 41
	structure = (

		)


class DestinationQueueInfoResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 42
	structure = (

		)


class SenderCertificateResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderCertificateResponse(NDRCALL):
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderId(NDRCALL):
	OPNUM = 44
	structure = (

		)


class SenderIdResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 45
	structure = (

		)


class SenderIdTypeResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class SenderIdTypeResponse(NDRCALL):
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class Send(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'DestinationQueue',
			IMSMQQUEUE2
			),
			(
			'Transaction',
			VARIANT
			)
		)


class SendResponse(NDRCALL):
	structure = (
			(
			'DestinationQueue',
			IMSMQQUEUE2
			),
			(
			'Transaction',
			VARIANT
			)
		)


class AttachCurrentSecurityContext(NDRCALL):
	OPNUM = 48
	structure = (

		)


class AttachCurrentSecurityContextResponse(NDRCALL):
	structure = (

		)


class SenderVersion(NDRCALL):
	OPNUM = 49
	structure = (

		)


class SenderVersionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 50
	structure = (

		)


class ExtensionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ExtensionResponse(NDRCALL):
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 52
	structure = (

		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (

		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class TransactionStatusQueueInfo(NDRCALL):
	OPNUM = 54
	structure = (

		)


class TransactionStatusQueueInfoResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 55
	structure = (

		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class Signature(NDRCALL):
	OPNUM = 57
	structure = (

		)


class SignatureResponse(NDRCALL):
	structure = (

		)


class Signature(NDRCALL):
	OPNUM = 58
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class SignatureResponse(NDRCALL):
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 59
	structure = (

		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 60
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 61
	structure = (

		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 62
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class SenderId(NDRCALL):
	OPNUM = 63
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class SenderIdResponse(NDRCALL):
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class MsgClass(NDRCALL):
	OPNUM = 64
	structure = (

		)


class MsgClassResponse(NDRCALL):
	structure = (

		)


class MsgClass(NDRCALL):
	OPNUM = 65
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class MsgClassResponse(NDRCALL):
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class Properties(NDRCALL):
	OPNUM = 66
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class TransactionId(NDRCALL):
	OPNUM = 67
	structure = (

		)


class TransactionIdResponse(NDRCALL):
	structure = (

		)


class IsFirstInTransaction(NDRCALL):
	OPNUM = 68
	structure = (

		)


class IsFirstInTransactionResponse(NDRCALL):
	structure = (

		)


class IsLastInTransaction(NDRCALL):
	OPNUM = 69
	structure = (

		)


class IsLastInTransactionResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 70
	structure = (

		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 71
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 72
	structure = (

		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (

		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class ReceivedAuthenticationLevel(NDRCALL):
	OPNUM = 74
	structure = (

		)


class ReceivedAuthenticationLevelResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Class,
	ClassResponse
	),1 : (
	PrivLevel,
	PrivLevelResponse
	),2 : (
	AuthLevel,
	AuthLevelResponse
	),3 : (
	IsAuthenticated,
	IsAuthenticatedResponse
	),4 : (
	Delivery,
	DeliveryResponse
	),5 : (
	Trace,
	TraceResponse
	),6 : (
	Priority,
	PriorityResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	ResponseQueueInfo_v1,
	ResponseQueueInfo_v1Response
	),9 : (
	AppSpecific,
	AppSpecificResponse
	),10 : (
	SourceMachineGuid,
	SourceMachineGuidResponse
	),11 : (
	BodyLength,
	BodyLengthResponse
	),12 : (
	Body,
	BodyResponse
	),13 : (
	AdminQueueInfo_v1,
	AdminQueueInfo_v1Response
	),14 : (
	Id,
	IdResponse
	),15 : (
	CorrelationId,
	CorrelationIdResponse
	),16 : (
	Ack,
	AckResponse
	),17 : (
	Label,
	LabelResponse
	),18 : (
	MaxTimeToReachQueue,
	MaxTimeToReachQueueResponse
	),19 : (
	MaxTimeToReceive,
	MaxTimeToReceiveResponse
	),20 : (
	HashAlgorithm,
	HashAlgorithmResponse
	),21 : (
	EncryptAlgorithm,
	EncryptAlgorithmResponse
	),22 : (
	SentTime,
	SentTimeResponse
	),23 : (
	ArrivedTime,
	ArrivedTimeResponse
	),24 : (
	DestinationQueueInfo,
	DestinationQueueInfoResponse
	),25 : (
	SenderCertificate,
	SenderCertificateResponse
	),26 : (
	SenderId,
	SenderIdResponse
	),27 : (
	SenderIdType,
	SenderIdTypeResponse
	),28 : (
	Send,
	SendResponse
	),29 : (
	AttachCurrentSecurityContext,
	AttachCurrentSecurityContextResponse
	),30 : (
	SenderVersion,
	SenderVersionResponse
	),31 : (
	Extension,
	ExtensionResponse
	),32 : (
	ConnectorTypeGuid,
	ConnectorTypeGuidResponse
	),33 : (
	TransactionStatusQueueInfo,
	TransactionStatusQueueInfoResponse
	),34 : (
	DestinationSymmetricKey,
	DestinationSymmetricKeyResponse
	),35 : (
	Signature,
	SignatureResponse
	),36 : (
	AuthenticationProviderType,
	AuthenticationProviderTypeResponse
	),37 : (
	AuthenticationProviderName,
	AuthenticationProviderNameResponse
	),38 : (
	MsgClass,
	MsgClassResponse
	),39 : (
	Properties,
	PropertiesResponse
	),40 : (
	TransactionId,
	TransactionIdResponse
	),41 : (
	IsFirstInTransaction,
	IsFirstInTransactionResponse
	),42 : (
	IsLastInTransaction,
	IsLastInTransactionResponse
	),43 : (
	ResponseQueueInfo,
	ResponseQueueInfoResponse
	),44 : (
	AdminQueueInfo,
	AdminQueueInfoResponse
	),45 : (
	ReceivedAuthenticationLevel,
	ReceivedAuthenticationLevelResponse
	)}
#################################################################################
#IMSMQMessage3 Definition
#################################################################################
MSRPC_UUID_IMSMQMESSAGE3 = uuidtup_to_bin(('eba96b1a-2168-113-898-00020746','0.0'))
class Class(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ClassResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class AuthLevel(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AuthLevelResponse(NDRCALL):
	structure = (

		)


class AuthLevel(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class AuthLevelResponse(NDRCALL):
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class IsAuthenticated(NDRCALL):
	OPNUM = 5
	structure = (

		)


class IsAuthenticatedResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DeliveryResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class DeliveryResponse(NDRCALL):
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class Trace(NDRCALL):
	OPNUM = 8
	structure = (

		)


class TraceResponse(NDRCALL):
	structure = (

		)


class Trace(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class TraceResponse(NDRCALL):
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class Priority(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PriorityResponse(NDRCALL):
	structure = (

		)


class Priority(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class PriorityResponse(NDRCALL):
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 14
	structure = (

		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class AppSpecific(NDRCALL):
	OPNUM = 16
	structure = (

		)


class AppSpecificResponse(NDRCALL):
	structure = (

		)


class AppSpecific(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class AppSpecificResponse(NDRCALL):
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class SourceMachineGuid(NDRCALL):
	OPNUM = 18
	structure = (

		)


class SourceMachineGuidResponse(NDRCALL):
	structure = (

		)


class BodyLength(NDRCALL):
	OPNUM = 19
	structure = (

		)


class BodyLengthResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 20
	structure = (

		)


class BodyResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class BodyResponse(NDRCALL):
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 22
	structure = (

		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class Id(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 25
	structure = (

		)


class CorrelationIdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class CorrelationIdResponse(NDRCALL):
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class Ack(NDRCALL):
	OPNUM = 27
	structure = (

		)


class AckResponse(NDRCALL):
	structure = (

		)


class Ack(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'lAck',
			LONG
			)
		)


class AckResponse(NDRCALL):
	structure = (
			(
			'lAck',
			LONG
			)
		)


class Label(NDRCALL):
	OPNUM = 29
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 31
	structure = (

		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 33
	structure = (

		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class HashAlgorithm(NDRCALL):
	OPNUM = 35
	structure = (

		)


class HashAlgorithmResponse(NDRCALL):
	structure = (

		)


class HashAlgorithm(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class HashAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 37
	structure = (

		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (

		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class SentTime(NDRCALL):
	OPNUM = 39
	structure = (

		)


class SentTimeResponse(NDRCALL):
	structure = (

		)


class ArrivedTime(NDRCALL):
	OPNUM = 40
	structure = (

		)


class ArrivedTimeResponse(NDRCALL):
	structure = (

		)


class DestinationQueueInfo(NDRCALL):
	OPNUM = 41
	structure = (

		)


class DestinationQueueInfoResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 42
	structure = (

		)


class SenderCertificateResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderCertificateResponse(NDRCALL):
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderId(NDRCALL):
	OPNUM = 44
	structure = (

		)


class SenderIdResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 45
	structure = (

		)


class SenderIdTypeResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class SenderIdTypeResponse(NDRCALL):
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class Send(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'DestinationQueue',
			IDISPATCH
			),
			(
			'Transaction',
			VARIANT
			)
		)


class SendResponse(NDRCALL):
	structure = (
			(
			'DestinationQueue',
			IDISPATCH
			),
			(
			'Transaction',
			VARIANT
			)
		)


class AttachCurrentSecurityContext(NDRCALL):
	OPNUM = 48
	structure = (

		)


class AttachCurrentSecurityContextResponse(NDRCALL):
	structure = (

		)


class SenderVersion(NDRCALL):
	OPNUM = 49
	structure = (

		)


class SenderVersionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 50
	structure = (

		)


class ExtensionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ExtensionResponse(NDRCALL):
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 52
	structure = (

		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (

		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class TransactionStatusQueueInfo(NDRCALL):
	OPNUM = 54
	structure = (

		)


class TransactionStatusQueueInfoResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 55
	structure = (

		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class Signature(NDRCALL):
	OPNUM = 57
	structure = (

		)


class SignatureResponse(NDRCALL):
	structure = (

		)


class Signature(NDRCALL):
	OPNUM = 58
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class SignatureResponse(NDRCALL):
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 59
	structure = (

		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 60
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 61
	structure = (

		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 62
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class SenderId(NDRCALL):
	OPNUM = 63
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class SenderIdResponse(NDRCALL):
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class MsgClass(NDRCALL):
	OPNUM = 64
	structure = (

		)


class MsgClassResponse(NDRCALL):
	structure = (

		)


class MsgClass(NDRCALL):
	OPNUM = 65
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class MsgClassResponse(NDRCALL):
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class Properties(NDRCALL):
	OPNUM = 66
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class TransactionId(NDRCALL):
	OPNUM = 67
	structure = (

		)


class TransactionIdResponse(NDRCALL):
	structure = (

		)


class IsFirstInTransaction(NDRCALL):
	OPNUM = 68
	structure = (

		)


class IsFirstInTransactionResponse(NDRCALL):
	structure = (

		)


class IsLastInTransaction(NDRCALL):
	OPNUM = 69
	structure = (

		)


class IsLastInTransactionResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v2(NDRCALL):
	OPNUM = 70
	structure = (

		)


class ResponseQueueInfo_v2Response(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v2(NDRCALL):
	OPNUM = 71
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class ResponseQueueInfo_v2Response(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfo_v2(NDRCALL):
	OPNUM = 72
	structure = (

		)


class AdminQueueInfo_v2Response(NDRCALL):
	structure = (

		)


class AdminQueueInfo_v2(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfo_v2Response(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class ReceivedAuthenticationLevel(NDRCALL):
	OPNUM = 74
	structure = (

		)


class ReceivedAuthenticationLevelResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 75
	structure = (

		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 76
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO3
			)
		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO3
			)
		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 77
	structure = (

		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (

		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 78
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO3
			)
		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO3
			)
		)


class ResponseDestination(NDRCALL):
	OPNUM = 79
	structure = (

		)


class ResponseDestinationResponse(NDRCALL):
	structure = (

		)


class ResponseDestination(NDRCALL):
	OPNUM = 80
	structure = (
			(
			'pdestResponse',
			IDISPATCH
			)
		)


class ResponseDestinationResponse(NDRCALL):
	structure = (
			(
			'pdestResponse',
			IDISPATCH
			)
		)


class Destination(NDRCALL):
	OPNUM = 81
	structure = (

		)


class DestinationResponse(NDRCALL):
	structure = (

		)


class LookupId(NDRCALL):
	OPNUM = 82
	structure = (

		)


class LookupIdResponse(NDRCALL):
	structure = (

		)


class IsAuthenticated2(NDRCALL):
	OPNUM = 83
	structure = (

		)


class IsAuthenticated2Response(NDRCALL):
	structure = (

		)


class IsFirstInTransaction2(NDRCALL):
	OPNUM = 84
	structure = (

		)


class IsFirstInTransaction2Response(NDRCALL):
	structure = (

		)


class IsLastInTransaction2(NDRCALL):
	OPNUM = 85
	structure = (

		)


class IsLastInTransaction2Response(NDRCALL):
	structure = (

		)


class AttachCurrentSecurityContext2(NDRCALL):
	OPNUM = 86
	structure = (

		)


class AttachCurrentSecurityContext2Response(NDRCALL):
	structure = (

		)


class SoapEnvelope(NDRCALL):
	OPNUM = 87
	structure = (

		)


class SoapEnvelopeResponse(NDRCALL):
	structure = (

		)


class CompoundMessage(NDRCALL):
	OPNUM = 88
	structure = (

		)


class CompoundMessageResponse(NDRCALL):
	structure = (

		)


class SoapHeader(NDRCALL):
	OPNUM = 89
	structure = (
			(
			'bstrSoapHeader',
			BSTR
			)
		)


class SoapHeaderResponse(NDRCALL):
	structure = (
			(
			'bstrSoapHeader',
			BSTR
			)
		)


class SoapBody(NDRCALL):
	OPNUM = 90
	structure = (
			(
			'bstrSoapBody',
			BSTR
			)
		)


class SoapBodyResponse(NDRCALL):
	structure = (
			(
			'bstrSoapBody',
			BSTR
			)
		)


OPNUMS = {0 : (
	Class,
	ClassResponse
	),1 : (
	PrivLevel,
	PrivLevelResponse
	),2 : (
	AuthLevel,
	AuthLevelResponse
	),3 : (
	IsAuthenticated,
	IsAuthenticatedResponse
	),4 : (
	Delivery,
	DeliveryResponse
	),5 : (
	Trace,
	TraceResponse
	),6 : (
	Priority,
	PriorityResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	ResponseQueueInfo_v1,
	ResponseQueueInfo_v1Response
	),9 : (
	AppSpecific,
	AppSpecificResponse
	),10 : (
	SourceMachineGuid,
	SourceMachineGuidResponse
	),11 : (
	BodyLength,
	BodyLengthResponse
	),12 : (
	Body,
	BodyResponse
	),13 : (
	AdminQueueInfo_v1,
	AdminQueueInfo_v1Response
	),14 : (
	Id,
	IdResponse
	),15 : (
	CorrelationId,
	CorrelationIdResponse
	),16 : (
	Ack,
	AckResponse
	),17 : (
	Label,
	LabelResponse
	),18 : (
	MaxTimeToReachQueue,
	MaxTimeToReachQueueResponse
	),19 : (
	MaxTimeToReceive,
	MaxTimeToReceiveResponse
	),20 : (
	HashAlgorithm,
	HashAlgorithmResponse
	),21 : (
	EncryptAlgorithm,
	EncryptAlgorithmResponse
	),22 : (
	SentTime,
	SentTimeResponse
	),23 : (
	ArrivedTime,
	ArrivedTimeResponse
	),24 : (
	DestinationQueueInfo,
	DestinationQueueInfoResponse
	),25 : (
	SenderCertificate,
	SenderCertificateResponse
	),26 : (
	SenderId,
	SenderIdResponse
	),27 : (
	SenderIdType,
	SenderIdTypeResponse
	),28 : (
	Send,
	SendResponse
	),29 : (
	AttachCurrentSecurityContext,
	AttachCurrentSecurityContextResponse
	),30 : (
	SenderVersion,
	SenderVersionResponse
	),31 : (
	Extension,
	ExtensionResponse
	),32 : (
	ConnectorTypeGuid,
	ConnectorTypeGuidResponse
	),33 : (
	TransactionStatusQueueInfo,
	TransactionStatusQueueInfoResponse
	),34 : (
	DestinationSymmetricKey,
	DestinationSymmetricKeyResponse
	),35 : (
	Signature,
	SignatureResponse
	),36 : (
	AuthenticationProviderType,
	AuthenticationProviderTypeResponse
	),37 : (
	AuthenticationProviderName,
	AuthenticationProviderNameResponse
	),38 : (
	MsgClass,
	MsgClassResponse
	),39 : (
	Properties,
	PropertiesResponse
	),40 : (
	TransactionId,
	TransactionIdResponse
	),41 : (
	IsFirstInTransaction,
	IsFirstInTransactionResponse
	),42 : (
	IsLastInTransaction,
	IsLastInTransactionResponse
	),43 : (
	ResponseQueueInfo_v2,
	ResponseQueueInfo_v2Response
	),44 : (
	AdminQueueInfo_v2,
	AdminQueueInfo_v2Response
	),45 : (
	ReceivedAuthenticationLevel,
	ReceivedAuthenticationLevelResponse
	),46 : (
	ResponseQueueInfo,
	ResponseQueueInfoResponse
	),47 : (
	AdminQueueInfo,
	AdminQueueInfoResponse
	),48 : (
	ResponseDestination,
	ResponseDestinationResponse
	),49 : (
	Destination,
	DestinationResponse
	),50 : (
	LookupId,
	LookupIdResponse
	),51 : (
	IsAuthenticated2,
	IsAuthenticated2Response
	),52 : (
	IsFirstInTransaction2,
	IsFirstInTransaction2Response
	),53 : (
	IsLastInTransaction2,
	IsLastInTransaction2Response
	),54 : (
	AttachCurrentSecurityContext2,
	AttachCurrentSecurityContext2Response
	),55 : (
	SoapEnvelope,
	SoapEnvelopeResponse
	),56 : (
	CompoundMessage,
	CompoundMessageResponse
	),57 : (
	SoapHeader,
	SoapHeaderResponse
	),58 : (
	SoapBody,
	SoapBodyResponse
	)}
#################################################################################
#IMSMQMessage4 Definition
#################################################################################
MSRPC_UUID_IMSMQMESSAGE4 = uuidtup_to_bin(('eba96b23-2168-113-898-00020746','0.0'))
class Class(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ClassResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class AuthLevel(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AuthLevelResponse(NDRCALL):
	structure = (

		)


class AuthLevel(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class AuthLevelResponse(NDRCALL):
	structure = (
			(
			'lAuthLevel',
			LONG
			)
		)


class IsAuthenticated(NDRCALL):
	OPNUM = 5
	structure = (

		)


class IsAuthenticatedResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DeliveryResponse(NDRCALL):
	structure = (

		)


class Delivery(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class DeliveryResponse(NDRCALL):
	structure = (
			(
			'lDelivery',
			LONG
			)
		)


class Trace(NDRCALL):
	OPNUM = 8
	structure = (

		)


class TraceResponse(NDRCALL):
	structure = (

		)


class Trace(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class TraceResponse(NDRCALL):
	structure = (
			(
			'lTrace',
			LONG
			)
		)


class Priority(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PriorityResponse(NDRCALL):
	structure = (

		)


class Priority(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class PriorityResponse(NDRCALL):
	structure = (
			(
			'lPriority',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 14
	structure = (

		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v1(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class ResponseQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO
			)
		)


class AppSpecific(NDRCALL):
	OPNUM = 16
	structure = (

		)


class AppSpecificResponse(NDRCALL):
	structure = (

		)


class AppSpecific(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class AppSpecificResponse(NDRCALL):
	structure = (
			(
			'lAppSpecific',
			LONG
			)
		)


class SourceMachineGuid(NDRCALL):
	OPNUM = 18
	structure = (

		)


class SourceMachineGuidResponse(NDRCALL):
	structure = (

		)


class BodyLength(NDRCALL):
	OPNUM = 19
	structure = (

		)


class BodyLengthResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 20
	structure = (

		)


class BodyResponse(NDRCALL):
	structure = (

		)


class Body(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class BodyResponse(NDRCALL):
	structure = (
			(
			'varBody',
			VARIANT
			)
		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 22
	structure = (

		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (

		)


class AdminQueueInfo_v1(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class AdminQueueInfo_v1Response(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO
			)
		)


class Id(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 25
	structure = (

		)


class CorrelationIdResponse(NDRCALL):
	structure = (

		)


class CorrelationId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class CorrelationIdResponse(NDRCALL):
	structure = (
			(
			'varMsgId',
			VARIANT
			)
		)


class Ack(NDRCALL):
	OPNUM = 27
	structure = (

		)


class AckResponse(NDRCALL):
	structure = (

		)


class Ack(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'lAck',
			LONG
			)
		)


class AckResponse(NDRCALL):
	structure = (
			(
			'lAck',
			LONG
			)
		)


class Label(NDRCALL):
	OPNUM = 29
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 31
	structure = (

		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReachQueue(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReachQueueResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReachQueue',
			LONG
			)
		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 33
	structure = (

		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (

		)


class MaxTimeToReceive(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class MaxTimeToReceiveResponse(NDRCALL):
	structure = (
			(
			'lMaxTimeToReceive',
			LONG
			)
		)


class HashAlgorithm(NDRCALL):
	OPNUM = 35
	structure = (

		)


class HashAlgorithmResponse(NDRCALL):
	structure = (

		)


class HashAlgorithm(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class HashAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lHashAlg',
			LONG
			)
		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 37
	structure = (

		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (

		)


class EncryptAlgorithm(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class EncryptAlgorithmResponse(NDRCALL):
	structure = (
			(
			'lEncryptAlg',
			LONG
			)
		)


class SentTime(NDRCALL):
	OPNUM = 39
	structure = (

		)


class SentTimeResponse(NDRCALL):
	structure = (

		)


class ArrivedTime(NDRCALL):
	OPNUM = 40
	structure = (

		)


class ArrivedTimeResponse(NDRCALL):
	structure = (

		)


class DestinationQueueInfo(NDRCALL):
	OPNUM = 41
	structure = (

		)


class DestinationQueueInfoResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 42
	structure = (

		)


class SenderCertificateResponse(NDRCALL):
	structure = (

		)


class SenderCertificate(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderCertificateResponse(NDRCALL):
	structure = (
			(
			'varSenderCert',
			VARIANT
			)
		)


class SenderId(NDRCALL):
	OPNUM = 44
	structure = (

		)


class SenderIdResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 45
	structure = (

		)


class SenderIdTypeResponse(NDRCALL):
	structure = (

		)


class SenderIdType(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class SenderIdTypeResponse(NDRCALL):
	structure = (
			(
			'lSenderIdType',
			LONG
			)
		)


class Send(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'DestinationQueue',
			IDISPATCH
			),
			(
			'Transaction',
			VARIANT
			)
		)


class SendResponse(NDRCALL):
	structure = (
			(
			'DestinationQueue',
			IDISPATCH
			),
			(
			'Transaction',
			VARIANT
			)
		)


class AttachCurrentSecurityContext(NDRCALL):
	OPNUM = 48
	structure = (

		)


class AttachCurrentSecurityContextResponse(NDRCALL):
	structure = (

		)


class SenderVersion(NDRCALL):
	OPNUM = 49
	structure = (

		)


class SenderVersionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 50
	structure = (

		)


class ExtensionResponse(NDRCALL):
	structure = (

		)


class Extension(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ExtensionResponse(NDRCALL):
	structure = (
			(
			'varExtension',
			VARIANT
			)
		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 52
	structure = (

		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (

		)


class ConnectorTypeGuid(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class ConnectorTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidConnectorType',
			BSTR
			)
		)


class TransactionStatusQueueInfo(NDRCALL):
	OPNUM = 54
	structure = (

		)


class TransactionStatusQueueInfoResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 55
	structure = (

		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (

		)


class DestinationSymmetricKey(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class DestinationSymmetricKeyResponse(NDRCALL):
	structure = (
			(
			'varDestSymmKey',
			VARIANT
			)
		)


class Signature(NDRCALL):
	OPNUM = 57
	structure = (

		)


class SignatureResponse(NDRCALL):
	structure = (

		)


class Signature(NDRCALL):
	OPNUM = 58
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class SignatureResponse(NDRCALL):
	structure = (
			(
			'varSignature',
			VARIANT
			)
		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 59
	structure = (

		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderType(NDRCALL):
	OPNUM = 60
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderTypeResponse(NDRCALL):
	structure = (
			(
			'lAuthProvType',
			LONG
			)
		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 61
	structure = (

		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (

		)


class AuthenticationProviderName(NDRCALL):
	OPNUM = 62
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class AuthenticationProviderNameResponse(NDRCALL):
	structure = (
			(
			'bstrAuthProvName',
			BSTR
			)
		)


class SenderId(NDRCALL):
	OPNUM = 63
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class SenderIdResponse(NDRCALL):
	structure = (
			(
			'varSenderId',
			VARIANT
			)
		)


class MsgClass(NDRCALL):
	OPNUM = 64
	structure = (

		)


class MsgClassResponse(NDRCALL):
	structure = (

		)


class MsgClass(NDRCALL):
	OPNUM = 65
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class MsgClassResponse(NDRCALL):
	structure = (
			(
			'lMsgClass',
			LONG
			)
		)


class Properties(NDRCALL):
	OPNUM = 66
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class TransactionId(NDRCALL):
	OPNUM = 67
	structure = (

		)


class TransactionIdResponse(NDRCALL):
	structure = (

		)


class IsFirstInTransaction(NDRCALL):
	OPNUM = 68
	structure = (

		)


class IsFirstInTransactionResponse(NDRCALL):
	structure = (

		)


class IsLastInTransaction(NDRCALL):
	OPNUM = 69
	structure = (

		)


class IsLastInTransactionResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v2(NDRCALL):
	OPNUM = 70
	structure = (

		)


class ResponseQueueInfo_v2Response(NDRCALL):
	structure = (

		)


class ResponseQueueInfo_v2(NDRCALL):
	OPNUM = 71
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class ResponseQueueInfo_v2Response(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfo_v2(NDRCALL):
	OPNUM = 72
	structure = (

		)


class AdminQueueInfo_v2Response(NDRCALL):
	structure = (

		)


class AdminQueueInfo_v2(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class AdminQueueInfo_v2Response(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO2
			)
		)


class ReceivedAuthenticationLevel(NDRCALL):
	OPNUM = 74
	structure = (

		)


class ReceivedAuthenticationLevelResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 75
	structure = (

		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (

		)


class ResponseQueueInfo(NDRCALL):
	OPNUM = 76
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO4
			)
		)


class ResponseQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoResponse',
			IMSMQQUEUEINFO4
			)
		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 77
	structure = (

		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (

		)


class AdminQueueInfo(NDRCALL):
	OPNUM = 78
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO4
			)
		)


class AdminQueueInfoResponse(NDRCALL):
	structure = (
			(
			'pqinfoAdmin',
			IMSMQQUEUEINFO4
			)
		)


class ResponseDestination(NDRCALL):
	OPNUM = 79
	structure = (

		)


class ResponseDestinationResponse(NDRCALL):
	structure = (

		)


class ResponseDestination(NDRCALL):
	OPNUM = 80
	structure = (
			(
			'pdestResponse',
			IDISPATCH
			)
		)


class ResponseDestinationResponse(NDRCALL):
	structure = (
			(
			'pdestResponse',
			IDISPATCH
			)
		)


class Destination(NDRCALL):
	OPNUM = 81
	structure = (

		)


class DestinationResponse(NDRCALL):
	structure = (

		)


class LookupId(NDRCALL):
	OPNUM = 82
	structure = (

		)


class LookupIdResponse(NDRCALL):
	structure = (

		)


class IsAuthenticated2(NDRCALL):
	OPNUM = 83
	structure = (

		)


class IsAuthenticated2Response(NDRCALL):
	structure = (

		)


class IsFirstInTransaction2(NDRCALL):
	OPNUM = 84
	structure = (

		)


class IsFirstInTransaction2Response(NDRCALL):
	structure = (

		)


class IsLastInTransaction2(NDRCALL):
	OPNUM = 85
	structure = (

		)


class IsLastInTransaction2Response(NDRCALL):
	structure = (

		)


class AttachCurrentSecurityContext2(NDRCALL):
	OPNUM = 86
	structure = (

		)


class AttachCurrentSecurityContext2Response(NDRCALL):
	structure = (

		)


class SoapEnvelope(NDRCALL):
	OPNUM = 87
	structure = (

		)


class SoapEnvelopeResponse(NDRCALL):
	structure = (

		)


class CompoundMessage(NDRCALL):
	OPNUM = 88
	structure = (

		)


class CompoundMessageResponse(NDRCALL):
	structure = (

		)


class SoapHeader(NDRCALL):
	OPNUM = 89
	structure = (
			(
			'bstrSoapHeader',
			BSTR
			)
		)


class SoapHeaderResponse(NDRCALL):
	structure = (
			(
			'bstrSoapHeader',
			BSTR
			)
		)


class SoapBody(NDRCALL):
	OPNUM = 90
	structure = (
			(
			'bstrSoapBody',
			BSTR
			)
		)


class SoapBodyResponse(NDRCALL):
	structure = (
			(
			'bstrSoapBody',
			BSTR
			)
		)


OPNUMS = {0 : (
	Class,
	ClassResponse
	),1 : (
	PrivLevel,
	PrivLevelResponse
	),2 : (
	AuthLevel,
	AuthLevelResponse
	),3 : (
	IsAuthenticated,
	IsAuthenticatedResponse
	),4 : (
	Delivery,
	DeliveryResponse
	),5 : (
	Trace,
	TraceResponse
	),6 : (
	Priority,
	PriorityResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	ResponseQueueInfo_v1,
	ResponseQueueInfo_v1Response
	),9 : (
	AppSpecific,
	AppSpecificResponse
	),10 : (
	SourceMachineGuid,
	SourceMachineGuidResponse
	),11 : (
	BodyLength,
	BodyLengthResponse
	),12 : (
	Body,
	BodyResponse
	),13 : (
	AdminQueueInfo_v1,
	AdminQueueInfo_v1Response
	),14 : (
	Id,
	IdResponse
	),15 : (
	CorrelationId,
	CorrelationIdResponse
	),16 : (
	Ack,
	AckResponse
	),17 : (
	Label,
	LabelResponse
	),18 : (
	MaxTimeToReachQueue,
	MaxTimeToReachQueueResponse
	),19 : (
	MaxTimeToReceive,
	MaxTimeToReceiveResponse
	),20 : (
	HashAlgorithm,
	HashAlgorithmResponse
	),21 : (
	EncryptAlgorithm,
	EncryptAlgorithmResponse
	),22 : (
	SentTime,
	SentTimeResponse
	),23 : (
	ArrivedTime,
	ArrivedTimeResponse
	),24 : (
	DestinationQueueInfo,
	DestinationQueueInfoResponse
	),25 : (
	SenderCertificate,
	SenderCertificateResponse
	),26 : (
	SenderId,
	SenderIdResponse
	),27 : (
	SenderIdType,
	SenderIdTypeResponse
	),28 : (
	Send,
	SendResponse
	),29 : (
	AttachCurrentSecurityContext,
	AttachCurrentSecurityContextResponse
	),30 : (
	SenderVersion,
	SenderVersionResponse
	),31 : (
	Extension,
	ExtensionResponse
	),32 : (
	ConnectorTypeGuid,
	ConnectorTypeGuidResponse
	),33 : (
	TransactionStatusQueueInfo,
	TransactionStatusQueueInfoResponse
	),34 : (
	DestinationSymmetricKey,
	DestinationSymmetricKeyResponse
	),35 : (
	Signature,
	SignatureResponse
	),36 : (
	AuthenticationProviderType,
	AuthenticationProviderTypeResponse
	),37 : (
	AuthenticationProviderName,
	AuthenticationProviderNameResponse
	),38 : (
	MsgClass,
	MsgClassResponse
	),39 : (
	Properties,
	PropertiesResponse
	),40 : (
	TransactionId,
	TransactionIdResponse
	),41 : (
	IsFirstInTransaction,
	IsFirstInTransactionResponse
	),42 : (
	IsLastInTransaction,
	IsLastInTransactionResponse
	),43 : (
	ResponseQueueInfo_v2,
	ResponseQueueInfo_v2Response
	),44 : (
	AdminQueueInfo_v2,
	AdminQueueInfo_v2Response
	),45 : (
	ReceivedAuthenticationLevel,
	ReceivedAuthenticationLevelResponse
	),46 : (
	ResponseQueueInfo,
	ResponseQueueInfoResponse
	),47 : (
	AdminQueueInfo,
	AdminQueueInfoResponse
	),48 : (
	ResponseDestination,
	ResponseDestinationResponse
	),49 : (
	Destination,
	DestinationResponse
	),50 : (
	LookupId,
	LookupIdResponse
	),51 : (
	IsAuthenticated2,
	IsAuthenticated2Response
	),52 : (
	IsFirstInTransaction2,
	IsFirstInTransaction2Response
	),53 : (
	IsLastInTransaction2,
	IsLastInTransaction2Response
	),54 : (
	AttachCurrentSecurityContext2,
	AttachCurrentSecurityContext2Response
	),55 : (
	SoapEnvelope,
	SoapEnvelopeResponse
	),56 : (
	CompoundMessage,
	CompoundMessageResponse
	),57 : (
	SoapHeader,
	SoapHeaderResponse
	),58 : (
	SoapBody,
	SoapBodyResponse
	)}
#################################################################################
#IMSMQQueue Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUE = uuidtup_to_bin(('D7D6E076-DCCD-110-AA4B-0060970EBAE','0.0'))
class Access(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AccessResponse(NDRCALL):
	structure = (

		)


class ShareMode(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ShareModeResponse(NDRCALL):
	structure = (

		)


class QueueInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class QueueInfoResponse(NDRCALL):
	structure = (

		)


class Handle(NDRCALL):
	OPNUM = 3
	structure = (

		)


class HandleResponse(NDRCALL):
	structure = (

		)


class IsOpen(NDRCALL):
	OPNUM = 4
	structure = (

		)


class IsOpenResponse(NDRCALL):
	structure = (

		)


class Close(NDRCALL):
	OPNUM = 5
	structure = (

		)


class CloseResponse(NDRCALL):
	structure = (

		)


class Receive(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class ReceiveResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotification(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'Event',
			IMSMQEVENT
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotificationResponse(NDRCALL):
	structure = (
			(
			'Event',
			IMSMQEVENT
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Reset(NDRCALL):
	OPNUM = 9
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class ReceiveCurrent(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class ReceiveCurrentResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNextResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrentResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


OPNUMS = {0 : (
	Access,
	AccessResponse
	),1 : (
	ShareMode,
	ShareModeResponse
	),2 : (
	QueueInfo,
	QueueInfoResponse
	),3 : (
	Handle,
	HandleResponse
	),4 : (
	IsOpen,
	IsOpenResponse
	),5 : (
	Close,
	CloseResponse
	),6 : (
	Receive,
	ReceiveResponse
	),7 : (
	Peek,
	PeekResponse
	),8 : (
	EnableNotification,
	EnableNotificationResponse
	),9 : (
	Reset,
	ResetResponse
	),10 : (
	ReceiveCurrent,
	ReceiveCurrentResponse
	),11 : (
	PeekNext,
	PeekNextResponse
	),12 : (
	PeekCurrent,
	PeekCurrentResponse
	)}
#################################################################################
#IMSMQQueue2 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUE2 = uuidtup_to_bin(('EF0574E0-068-113-B100-00020746','0.0'))
class Access(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AccessResponse(NDRCALL):
	structure = (

		)


class ShareMode(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ShareModeResponse(NDRCALL):
	structure = (

		)


class QueueInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class QueueInfoResponse(NDRCALL):
	structure = (

		)


class Handle(NDRCALL):
	OPNUM = 3
	structure = (

		)


class HandleResponse(NDRCALL):
	structure = (

		)


class IsOpen(NDRCALL):
	OPNUM = 4
	structure = (

		)


class IsOpenResponse(NDRCALL):
	structure = (

		)


class Close(NDRCALL):
	OPNUM = 5
	structure = (

		)


class CloseResponse(NDRCALL):
	structure = (

		)


class Receive_v1(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotification(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'Event',
			IMSMQEVENT2
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotificationResponse(NDRCALL):
	structure = (
			(
			'Event',
			IMSMQEVENT2
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Reset(NDRCALL):
	OPNUM = 9
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class ReceiveCurrent_v1(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class ReceiveCurrent_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Peek(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrent(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrentResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNext(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrent(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrentResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 18
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Access,
	AccessResponse
	),1 : (
	ShareMode,
	ShareModeResponse
	),2 : (
	QueueInfo,
	QueueInfoResponse
	),3 : (
	Handle,
	HandleResponse
	),4 : (
	IsOpen,
	IsOpenResponse
	),5 : (
	Close,
	CloseResponse
	),6 : (
	Receive_v1,
	Receive_v1Response
	),7 : (
	Peek_v1,
	Peek_v1Response
	),8 : (
	EnableNotification,
	EnableNotificationResponse
	),9 : (
	Reset,
	ResetResponse
	),10 : (
	ReceiveCurrent_v1,
	ReceiveCurrent_v1Response
	),11 : (
	PeekNext_v1,
	PeekNext_v1Response
	),12 : (
	PeekCurrent_v1,
	PeekCurrent_v1Response
	),13 : (
	Receive,
	ReceiveResponse
	),14 : (
	Peek,
	PeekResponse
	),15 : (
	ReceiveCurrent,
	ReceiveCurrentResponse
	),16 : (
	PeekNext,
	PeekNextResponse
	),17 : (
	PeekCurrent,
	PeekCurrentResponse
	),18 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQQueue3 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUE3 = uuidtup_to_bin(('eba96b1b-2168-113-898-00020746','0.0'))
class Access(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AccessResponse(NDRCALL):
	structure = (

		)


class ShareMode(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ShareModeResponse(NDRCALL):
	structure = (

		)


class QueueInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class QueueInfoResponse(NDRCALL):
	structure = (

		)


class Handle(NDRCALL):
	OPNUM = 3
	structure = (

		)


class HandleResponse(NDRCALL):
	structure = (

		)


class IsOpen(NDRCALL):
	OPNUM = 4
	structure = (

		)


class IsOpenResponse(NDRCALL):
	structure = (

		)


class Close(NDRCALL):
	OPNUM = 5
	structure = (

		)


class CloseResponse(NDRCALL):
	structure = (

		)


class Receive_v1(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotification(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'Event',
			IMSMQEVENT3
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotificationResponse(NDRCALL):
	structure = (
			(
			'Event',
			IMSMQEVENT3
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Reset(NDRCALL):
	OPNUM = 9
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class ReceiveCurrent_v1(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class ReceiveCurrent_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Peek(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrent(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrentResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNext(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrent(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrentResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 18
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class Handle2(NDRCALL):
	OPNUM = 19
	structure = (

		)


class Handle2Response(NDRCALL):
	structure = (

		)


class ReceiveByLookupId(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveNextByLookupId(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveNextByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceivePreviousByLookupId(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceivePreviousByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveFirstByLookupId(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveFirstByLookupIdResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveLastByLookupId(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveLastByLookupIdResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekByLookupId(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextByLookupId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekPreviousByLookupId(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekPreviousByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekFirstByLookupId(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekFirstByLookupIdResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekLastByLookupId(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekLastByLookupIdResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Purge(NDRCALL):
	OPNUM = 30
	structure = (

		)


class PurgeResponse(NDRCALL):
	structure = (

		)


class IsOpen2(NDRCALL):
	OPNUM = 31
	structure = (

		)


class IsOpen2Response(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Access,
	AccessResponse
	),1 : (
	ShareMode,
	ShareModeResponse
	),2 : (
	QueueInfo,
	QueueInfoResponse
	),3 : (
	Handle,
	HandleResponse
	),4 : (
	IsOpen,
	IsOpenResponse
	),5 : (
	Close,
	CloseResponse
	),6 : (
	Receive_v1,
	Receive_v1Response
	),7 : (
	Peek_v1,
	Peek_v1Response
	),8 : (
	EnableNotification,
	EnableNotificationResponse
	),9 : (
	Reset,
	ResetResponse
	),10 : (
	ReceiveCurrent_v1,
	ReceiveCurrent_v1Response
	),11 : (
	PeekNext_v1,
	PeekNext_v1Response
	),12 : (
	PeekCurrent_v1,
	PeekCurrent_v1Response
	),13 : (
	Receive,
	ReceiveResponse
	),14 : (
	Peek,
	PeekResponse
	),15 : (
	ReceiveCurrent,
	ReceiveCurrentResponse
	),16 : (
	PeekNext,
	PeekNextResponse
	),17 : (
	PeekCurrent,
	PeekCurrentResponse
	),18 : (
	Properties,
	PropertiesResponse
	),19 : (
	Handle2,
	Handle2Response
	),20 : (
	ReceiveByLookupId,
	ReceiveByLookupIdResponse
	),21 : (
	ReceiveNextByLookupId,
	ReceiveNextByLookupIdResponse
	),22 : (
	ReceivePreviousByLookupId,
	ReceivePreviousByLookupIdResponse
	),23 : (
	ReceiveFirstByLookupId,
	ReceiveFirstByLookupIdResponse
	),24 : (
	ReceiveLastByLookupId,
	ReceiveLastByLookupIdResponse
	),25 : (
	PeekByLookupId,
	PeekByLookupIdResponse
	),26 : (
	PeekNextByLookupId,
	PeekNextByLookupIdResponse
	),27 : (
	PeekPreviousByLookupId,
	PeekPreviousByLookupIdResponse
	),28 : (
	PeekFirstByLookupId,
	PeekFirstByLookupIdResponse
	),29 : (
	PeekLastByLookupId,
	PeekLastByLookupIdResponse
	),30 : (
	Purge,
	PurgeResponse
	),31 : (
	IsOpen2,
	IsOpen2Response
	)}
#################################################################################
#IMSMQQueue4 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUE4 = uuidtup_to_bin(('eba96b20-2168-113-898-00020746','0.0'))
class Access(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AccessResponse(NDRCALL):
	structure = (

		)


class ShareMode(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ShareModeResponse(NDRCALL):
	structure = (

		)


class QueueInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class QueueInfoResponse(NDRCALL):
	structure = (

		)


class Handle(NDRCALL):
	OPNUM = 3
	structure = (

		)


class HandleResponse(NDRCALL):
	structure = (

		)


class IsOpen(NDRCALL):
	OPNUM = 4
	structure = (

		)


class IsOpenResponse(NDRCALL):
	structure = (

		)


class Close(NDRCALL):
	OPNUM = 5
	structure = (

		)


class CloseResponse(NDRCALL):
	structure = (

		)


class Receive_v1(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Peek_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotification(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'Event',
			IMSMQEVENT3
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class EnableNotificationResponse(NDRCALL):
	structure = (
			(
			'Event',
			IMSMQEVENT3
			),
			(
			'Cursor',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Reset(NDRCALL):
	OPNUM = 9
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class ReceiveCurrent_v1(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class ReceiveCurrent_v1Response(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekNext_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class PeekCurrent_v1Response(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			)
		)


class Receive(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Peek(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrent(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveCurrentResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNext(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrent(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekCurrentResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'ReceiveTimeout',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 18
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class Handle2(NDRCALL):
	OPNUM = 19
	structure = (

		)


class Handle2Response(NDRCALL):
	structure = (

		)


class ReceiveByLookupId(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveNextByLookupId(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveNextByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceivePreviousByLookupId(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceivePreviousByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveFirstByLookupId(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveFirstByLookupIdResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveLastByLookupId(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveLastByLookupIdResponse(NDRCALL):
	structure = (
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekByLookupId(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextByLookupId(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekNextByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekPreviousByLookupId(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekPreviousByLookupIdResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekFirstByLookupId(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekFirstByLookupIdResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekLastByLookupId(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class PeekLastByLookupIdResponse(NDRCALL):
	structure = (
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class Purge(NDRCALL):
	OPNUM = 30
	structure = (

		)


class PurgeResponse(NDRCALL):
	structure = (

		)


class IsOpen2(NDRCALL):
	OPNUM = 31
	structure = (

		)


class IsOpen2Response(NDRCALL):
	structure = (

		)


class ReceiveByLookupIdAllowPeek(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


class ReceiveByLookupIdAllowPeekResponse(NDRCALL):
	structure = (
			(
			'LookupId',
			VARIANT
			),
			(
			'Transaction',
			VARIANT
			),
			(
			'WantDestinationQueue',
			VARIANT
			),
			(
			'WantBody',
			VARIANT
			),
			(
			'WantConnectorType',
			VARIANT
			)
		)


OPNUMS = {0 : (
	Access,
	AccessResponse
	),1 : (
	ShareMode,
	ShareModeResponse
	),2 : (
	QueueInfo,
	QueueInfoResponse
	),3 : (
	Handle,
	HandleResponse
	),4 : (
	IsOpen,
	IsOpenResponse
	),5 : (
	Close,
	CloseResponse
	),6 : (
	Receive_v1,
	Receive_v1Response
	),7 : (
	Peek_v1,
	Peek_v1Response
	),8 : (
	EnableNotification,
	EnableNotificationResponse
	),9 : (
	Reset,
	ResetResponse
	),10 : (
	ReceiveCurrent_v1,
	ReceiveCurrent_v1Response
	),11 : (
	PeekNext_v1,
	PeekNext_v1Response
	),12 : (
	PeekCurrent_v1,
	PeekCurrent_v1Response
	),13 : (
	Receive,
	ReceiveResponse
	),14 : (
	Peek,
	PeekResponse
	),15 : (
	ReceiveCurrent,
	ReceiveCurrentResponse
	),16 : (
	PeekNext,
	PeekNextResponse
	),17 : (
	PeekCurrent,
	PeekCurrentResponse
	),18 : (
	Properties,
	PropertiesResponse
	),19 : (
	Handle2,
	Handle2Response
	),20 : (
	ReceiveByLookupId,
	ReceiveByLookupIdResponse
	),21 : (
	ReceiveNextByLookupId,
	ReceiveNextByLookupIdResponse
	),22 : (
	ReceivePreviousByLookupId,
	ReceivePreviousByLookupIdResponse
	),23 : (
	ReceiveFirstByLookupId,
	ReceiveFirstByLookupIdResponse
	),24 : (
	ReceiveLastByLookupId,
	ReceiveLastByLookupIdResponse
	),25 : (
	PeekByLookupId,
	PeekByLookupIdResponse
	),26 : (
	PeekNextByLookupId,
	PeekNextByLookupIdResponse
	),27 : (
	PeekPreviousByLookupId,
	PeekPreviousByLookupIdResponse
	),28 : (
	PeekFirstByLookupId,
	PeekFirstByLookupIdResponse
	),29 : (
	PeekLastByLookupId,
	PeekLastByLookupIdResponse
	),30 : (
	Purge,
	PurgeResponse
	),31 : (
	IsOpen2,
	IsOpen2Response
	),32 : (
	ReceiveByLookupIdAllowPeek,
	ReceiveByLookupIdAllowPeekResponse
	)}
#################################################################################
#IMSMQPrivateEvent Definition
#################################################################################
MSRPC_UUID_IMSMQPRIVATEEVENT = uuidtup_to_bin(('D7AB3341-C9D3-111-BB47-00807520','0.0'))
class Hwnd(NDRCALL):
	OPNUM = 0
	structure = (

		)


class HwndResponse(NDRCALL):
	structure = (

		)


class FireArrivedEvent(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'pq',
			IMSMQQUEUE
			),
			(
			'msgcursor',
			LONG
			)
		)


class FireArrivedEventResponse(NDRCALL):
	structure = (
			(
			'pq',
			IMSMQQUEUE
			),
			(
			'msgcursor',
			LONG
			)
		)


class FireArrivedErrorEvent(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'pq',
			IMSMQQUEUE
			),
			(
			'hrStatus',
			HRESULT
			),
			(
			'msgcursor',
			LONG
			)
		)


class FireArrivedErrorEventResponse(NDRCALL):
	structure = (
			(
			'pq',
			IMSMQQUEUE
			),
			(
			'hrStatus',
			HRESULT
			),
			(
			'msgcursor',
			LONG
			)
		)


OPNUMS = {0 : (
	Hwnd,
	HwndResponse
	),1 : (
	FireArrivedEvent,
	FireArrivedEventResponse
	),2 : (
	FireArrivedErrorEvent,
	FireArrivedErrorEventResponse
	)}
#################################################################################
#IMSMQEvent Definition
#################################################################################
MSRPC_UUID_IMSMQEVENT = uuidtup_to_bin(('D7D6E077-DCCD-110-AA4B-0060970EBAE','0.0'))
OPNUMS = {}
#################################################################################
#IMSMQEvent2 Definition
#################################################################################
MSRPC_UUID_IMSMQEVENT2 = uuidtup_to_bin(('eba96b12-2168-113-898-00020746','0.0'))
class Properties(NDRCALL):
	OPNUM = 0
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQEvent3 Definition
#################################################################################
MSRPC_UUID_IMSMQEVENT3 = uuidtup_to_bin(('eba96b1c-2168-113-898-00020746','0.0'))
OPNUMS = {}
#################################################################################
#IMSMQQueueInfo Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFO = uuidtup_to_bin(('D7D6E07B-DCCD-110-AA4B-0060970EBAE','0.0'))
class QueueGuid(NDRCALL):
	OPNUM = 0
	structure = (

		)


class QueueGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class Label(NDRCALL):
	OPNUM = 3
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class PathName(NDRCALL):
	OPNUM = 5
	structure = (

		)


class PathNameResponse(NDRCALL):
	structure = (

		)


class PathName(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class PathNameResponse(NDRCALL):
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class FormatName(NDRCALL):
	OPNUM = 7
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class FormatName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class FormatNameResponse(NDRCALL):
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class IsTransactional(NDRCALL):
	OPNUM = 9
	structure = (

		)


class IsTransactionalResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class Quota(NDRCALL):
	OPNUM = 14
	structure = (

		)


class QuotaResponse(NDRCALL):
	structure = (

		)


class Quota(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class QuotaResponse(NDRCALL):
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class BasePriority(NDRCALL):
	OPNUM = 16
	structure = (

		)


class BasePriorityResponse(NDRCALL):
	structure = (

		)


class BasePriority(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class BasePriorityResponse(NDRCALL):
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class CreateTime(NDRCALL):
	OPNUM = 18
	structure = (

		)


class CreateTimeResponse(NDRCALL):
	structure = (

		)


class ModifyTime(NDRCALL):
	OPNUM = 19
	structure = (

		)


class ModifyTimeResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 20
	structure = (

		)


class AuthenticateResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class AuthenticateResponse(NDRCALL):
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class JournalQuota(NDRCALL):
	OPNUM = 22
	structure = (

		)


class JournalQuotaResponse(NDRCALL):
	structure = (

		)


class JournalQuota(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class JournalQuotaResponse(NDRCALL):
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class IsWorldReadable(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IsWorldReadableResponse(NDRCALL):
	structure = (

		)


class Create(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class CreateResponse(NDRCALL):
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class Delete(NDRCALL):
	OPNUM = 26
	structure = (

		)


class DeleteResponse(NDRCALL):
	structure = (

		)


class Open(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class OpenResponse(NDRCALL):
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class Refresh(NDRCALL):
	OPNUM = 28
	structure = (

		)


class RefreshResponse(NDRCALL):
	structure = (

		)


class Update(NDRCALL):
	OPNUM = 29
	structure = (

		)


class UpdateResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	QueueGuid,
	QueueGuidResponse
	),1 : (
	ServiceTypeGuid,
	ServiceTypeGuidResponse
	),2 : (
	Label,
	LabelResponse
	),3 : (
	PathName,
	PathNameResponse
	),4 : (
	FormatName,
	FormatNameResponse
	),5 : (
	IsTransactional,
	IsTransactionalResponse
	),6 : (
	PrivLevel,
	PrivLevelResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	Quota,
	QuotaResponse
	),9 : (
	BasePriority,
	BasePriorityResponse
	),10 : (
	CreateTime,
	CreateTimeResponse
	),11 : (
	ModifyTime,
	ModifyTimeResponse
	),12 : (
	Authenticate,
	AuthenticateResponse
	),13 : (
	JournalQuota,
	JournalQuotaResponse
	),14 : (
	IsWorldReadable,
	IsWorldReadableResponse
	),15 : (
	Create,
	CreateResponse
	),16 : (
	Delete,
	DeleteResponse
	),17 : (
	Open,
	OpenResponse
	),18 : (
	Refresh,
	RefreshResponse
	),19 : (
	Update,
	UpdateResponse
	)}
#################################################################################
#IMSMQQueueInfo2 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFO2 = uuidtup_to_bin(('FD174A80-89F-112-B0F2-00020746','0.0'))
class QueueGuid(NDRCALL):
	OPNUM = 0
	structure = (

		)


class QueueGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class Label(NDRCALL):
	OPNUM = 3
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class PathName(NDRCALL):
	OPNUM = 5
	structure = (

		)


class PathNameResponse(NDRCALL):
	structure = (

		)


class PathName(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class PathNameResponse(NDRCALL):
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class FormatName(NDRCALL):
	OPNUM = 7
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class FormatName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class FormatNameResponse(NDRCALL):
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class IsTransactional(NDRCALL):
	OPNUM = 9
	structure = (

		)


class IsTransactionalResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class Quota(NDRCALL):
	OPNUM = 14
	structure = (

		)


class QuotaResponse(NDRCALL):
	structure = (

		)


class Quota(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class QuotaResponse(NDRCALL):
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class BasePriority(NDRCALL):
	OPNUM = 16
	structure = (

		)


class BasePriorityResponse(NDRCALL):
	structure = (

		)


class BasePriority(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class BasePriorityResponse(NDRCALL):
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class CreateTime(NDRCALL):
	OPNUM = 18
	structure = (

		)


class CreateTimeResponse(NDRCALL):
	structure = (

		)


class ModifyTime(NDRCALL):
	OPNUM = 19
	structure = (

		)


class ModifyTimeResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 20
	structure = (

		)


class AuthenticateResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class AuthenticateResponse(NDRCALL):
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class JournalQuota(NDRCALL):
	OPNUM = 22
	structure = (

		)


class JournalQuotaResponse(NDRCALL):
	structure = (

		)


class JournalQuota(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class JournalQuotaResponse(NDRCALL):
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class IsWorldReadable(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IsWorldReadableResponse(NDRCALL):
	structure = (

		)


class Create(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class CreateResponse(NDRCALL):
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class Delete(NDRCALL):
	OPNUM = 26
	structure = (

		)


class DeleteResponse(NDRCALL):
	structure = (

		)


class Open(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class OpenResponse(NDRCALL):
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class Refresh(NDRCALL):
	OPNUM = 28
	structure = (

		)


class RefreshResponse(NDRCALL):
	structure = (

		)


class Update(NDRCALL):
	OPNUM = 29
	structure = (

		)


class UpdateResponse(NDRCALL):
	structure = (

		)


class PathNameDNS(NDRCALL):
	OPNUM = 30
	structure = (

		)


class PathNameDNSResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 31
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 32
	structure = (

		)


class SecurityResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


class SecurityResponse(NDRCALL):
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


OPNUMS = {0 : (
	QueueGuid,
	QueueGuidResponse
	),1 : (
	ServiceTypeGuid,
	ServiceTypeGuidResponse
	),2 : (
	Label,
	LabelResponse
	),3 : (
	PathName,
	PathNameResponse
	),4 : (
	FormatName,
	FormatNameResponse
	),5 : (
	IsTransactional,
	IsTransactionalResponse
	),6 : (
	PrivLevel,
	PrivLevelResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	Quota,
	QuotaResponse
	),9 : (
	BasePriority,
	BasePriorityResponse
	),10 : (
	CreateTime,
	CreateTimeResponse
	),11 : (
	ModifyTime,
	ModifyTimeResponse
	),12 : (
	Authenticate,
	AuthenticateResponse
	),13 : (
	JournalQuota,
	JournalQuotaResponse
	),14 : (
	IsWorldReadable,
	IsWorldReadableResponse
	),15 : (
	Create,
	CreateResponse
	),16 : (
	Delete,
	DeleteResponse
	),17 : (
	Open,
	OpenResponse
	),18 : (
	Refresh,
	RefreshResponse
	),19 : (
	Update,
	UpdateResponse
	),20 : (
	PathNameDNS,
	PathNameDNSResponse
	),21 : (
	Properties,
	PropertiesResponse
	),22 : (
	Security,
	SecurityResponse
	)}
#################################################################################
#IMSMQQueueInfo3 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFO3 = uuidtup_to_bin(('eba96b1d-2168-113-898-00020746','0.0'))
class QueueGuid(NDRCALL):
	OPNUM = 0
	structure = (

		)


class QueueGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class Label(NDRCALL):
	OPNUM = 3
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class PathName(NDRCALL):
	OPNUM = 5
	structure = (

		)


class PathNameResponse(NDRCALL):
	structure = (

		)


class PathName(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class PathNameResponse(NDRCALL):
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class FormatName(NDRCALL):
	OPNUM = 7
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class FormatName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class FormatNameResponse(NDRCALL):
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class IsTransactional(NDRCALL):
	OPNUM = 9
	structure = (

		)


class IsTransactionalResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class Quota(NDRCALL):
	OPNUM = 14
	structure = (

		)


class QuotaResponse(NDRCALL):
	structure = (

		)


class Quota(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class QuotaResponse(NDRCALL):
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class BasePriority(NDRCALL):
	OPNUM = 16
	structure = (

		)


class BasePriorityResponse(NDRCALL):
	structure = (

		)


class BasePriority(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class BasePriorityResponse(NDRCALL):
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class CreateTime(NDRCALL):
	OPNUM = 18
	structure = (

		)


class CreateTimeResponse(NDRCALL):
	structure = (

		)


class ModifyTime(NDRCALL):
	OPNUM = 19
	structure = (

		)


class ModifyTimeResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 20
	structure = (

		)


class AuthenticateResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class AuthenticateResponse(NDRCALL):
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class JournalQuota(NDRCALL):
	OPNUM = 22
	structure = (

		)


class JournalQuotaResponse(NDRCALL):
	structure = (

		)


class JournalQuota(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class JournalQuotaResponse(NDRCALL):
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class IsWorldReadable(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IsWorldReadableResponse(NDRCALL):
	structure = (

		)


class Create(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class CreateResponse(NDRCALL):
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class Delete(NDRCALL):
	OPNUM = 26
	structure = (

		)


class DeleteResponse(NDRCALL):
	structure = (

		)


class Open(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class OpenResponse(NDRCALL):
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class Refresh(NDRCALL):
	OPNUM = 28
	structure = (

		)


class RefreshResponse(NDRCALL):
	structure = (

		)


class Update(NDRCALL):
	OPNUM = 29
	structure = (

		)


class UpdateResponse(NDRCALL):
	structure = (

		)


class PathNameDNS(NDRCALL):
	OPNUM = 30
	structure = (

		)


class PathNameDNSResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 31
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 32
	structure = (

		)


class SecurityResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


class SecurityResponse(NDRCALL):
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


class IsTransactional2(NDRCALL):
	OPNUM = 34
	structure = (

		)


class IsTransactional2Response(NDRCALL):
	structure = (

		)


class IsWorldReadable2(NDRCALL):
	OPNUM = 35
	structure = (

		)


class IsWorldReadable2Response(NDRCALL):
	structure = (

		)


class MulticastAddress(NDRCALL):
	OPNUM = 36
	structure = (

		)


class MulticastAddressResponse(NDRCALL):
	structure = (

		)


class MulticastAddress(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'bstrMulticastAddress',
			BSTR
			)
		)


class MulticastAddressResponse(NDRCALL):
	structure = (
			(
			'bstrMulticastAddress',
			BSTR
			)
		)


class ADsPath(NDRCALL):
	OPNUM = 38
	structure = (

		)


class ADsPathResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	QueueGuid,
	QueueGuidResponse
	),1 : (
	ServiceTypeGuid,
	ServiceTypeGuidResponse
	),2 : (
	Label,
	LabelResponse
	),3 : (
	PathName,
	PathNameResponse
	),4 : (
	FormatName,
	FormatNameResponse
	),5 : (
	IsTransactional,
	IsTransactionalResponse
	),6 : (
	PrivLevel,
	PrivLevelResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	Quota,
	QuotaResponse
	),9 : (
	BasePriority,
	BasePriorityResponse
	),10 : (
	CreateTime,
	CreateTimeResponse
	),11 : (
	ModifyTime,
	ModifyTimeResponse
	),12 : (
	Authenticate,
	AuthenticateResponse
	),13 : (
	JournalQuota,
	JournalQuotaResponse
	),14 : (
	IsWorldReadable,
	IsWorldReadableResponse
	),15 : (
	Create,
	CreateResponse
	),16 : (
	Delete,
	DeleteResponse
	),17 : (
	Open,
	OpenResponse
	),18 : (
	Refresh,
	RefreshResponse
	),19 : (
	Update,
	UpdateResponse
	),20 : (
	PathNameDNS,
	PathNameDNSResponse
	),21 : (
	Properties,
	PropertiesResponse
	),22 : (
	Security,
	SecurityResponse
	),23 : (
	IsTransactional2,
	IsTransactional2Response
	),24 : (
	IsWorldReadable2,
	IsWorldReadable2Response
	),25 : (
	MulticastAddress,
	MulticastAddressResponse
	),26 : (
	ADsPath,
	ADsPathResponse
	)}
#################################################################################
#IMSMQQueueInfo4 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFO4 = uuidtup_to_bin(('eba96b21-2168-113-898-00020746','0.0'))
class QueueGuid(NDRCALL):
	OPNUM = 0
	structure = (

		)


class QueueGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 1
	structure = (

		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (

		)


class ServiceTypeGuid(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class ServiceTypeGuidResponse(NDRCALL):
	structure = (
			(
			'bstrGuidServiceType',
			BSTR
			)
		)


class Label(NDRCALL):
	OPNUM = 3
	structure = (

		)


class LabelResponse(NDRCALL):
	structure = (

		)


class Label(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class LabelResponse(NDRCALL):
	structure = (
			(
			'bstrLabel',
			BSTR
			)
		)


class PathName(NDRCALL):
	OPNUM = 5
	structure = (

		)


class PathNameResponse(NDRCALL):
	structure = (

		)


class PathName(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class PathNameResponse(NDRCALL):
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class FormatName(NDRCALL):
	OPNUM = 7
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class FormatName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class FormatNameResponse(NDRCALL):
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class IsTransactional(NDRCALL):
	OPNUM = 9
	structure = (

		)


class IsTransactionalResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 10
	structure = (

		)


class PrivLevelResponse(NDRCALL):
	structure = (

		)


class PrivLevel(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class PrivLevelResponse(NDRCALL):
	structure = (
			(
			'lPrivLevel',
			LONG
			)
		)


class Journal(NDRCALL):
	OPNUM = 12
	structure = (

		)


class JournalResponse(NDRCALL):
	structure = (

		)


class Journal(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class JournalResponse(NDRCALL):
	structure = (
			(
			'lJournal',
			LONG
			)
		)


class Quota(NDRCALL):
	OPNUM = 14
	structure = (

		)


class QuotaResponse(NDRCALL):
	structure = (

		)


class Quota(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class QuotaResponse(NDRCALL):
	structure = (
			(
			'lQuota',
			LONG
			)
		)


class BasePriority(NDRCALL):
	OPNUM = 16
	structure = (

		)


class BasePriorityResponse(NDRCALL):
	structure = (

		)


class BasePriority(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class BasePriorityResponse(NDRCALL):
	structure = (
			(
			'lBasePriority',
			LONG
			)
		)


class CreateTime(NDRCALL):
	OPNUM = 18
	structure = (

		)


class CreateTimeResponse(NDRCALL):
	structure = (

		)


class ModifyTime(NDRCALL):
	OPNUM = 19
	structure = (

		)


class ModifyTimeResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 20
	structure = (

		)


class AuthenticateResponse(NDRCALL):
	structure = (

		)


class Authenticate(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class AuthenticateResponse(NDRCALL):
	structure = (
			(
			'lAuthenticate',
			LONG
			)
		)


class JournalQuota(NDRCALL):
	OPNUM = 22
	structure = (

		)


class JournalQuotaResponse(NDRCALL):
	structure = (

		)


class JournalQuota(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class JournalQuotaResponse(NDRCALL):
	structure = (
			(
			'lJournalQuota',
			LONG
			)
		)


class IsWorldReadable(NDRCALL):
	OPNUM = 24
	structure = (

		)


class IsWorldReadableResponse(NDRCALL):
	structure = (

		)


class Create(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class CreateResponse(NDRCALL):
	structure = (
			(
			'IsTransactional',
			VARIANT
			),
			(
			'IsWorldReadable',
			VARIANT
			)
		)


class Delete(NDRCALL):
	OPNUM = 26
	structure = (

		)


class DeleteResponse(NDRCALL):
	structure = (

		)


class Open(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class OpenResponse(NDRCALL):
	structure = (
			(
			'Access',
			LONG
			),
			(
			'ShareMode',
			LONG
			)
		)


class Refresh(NDRCALL):
	OPNUM = 28
	structure = (

		)


class RefreshResponse(NDRCALL):
	structure = (

		)


class Update(NDRCALL):
	OPNUM = 29
	structure = (

		)


class UpdateResponse(NDRCALL):
	structure = (

		)


class PathNameDNS(NDRCALL):
	OPNUM = 30
	structure = (

		)


class PathNameDNSResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 31
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 32
	structure = (

		)


class SecurityResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


class SecurityResponse(NDRCALL):
	structure = (
			(
			'varSecurity',
			VARIANT
			)
		)


class IsTransactional2(NDRCALL):
	OPNUM = 34
	structure = (

		)


class IsTransactional2Response(NDRCALL):
	structure = (

		)


class IsWorldReadable2(NDRCALL):
	OPNUM = 35
	structure = (

		)


class IsWorldReadable2Response(NDRCALL):
	structure = (

		)


class MulticastAddress(NDRCALL):
	OPNUM = 36
	structure = (

		)


class MulticastAddressResponse(NDRCALL):
	structure = (

		)


class MulticastAddress(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'bstrMulticastAddress',
			BSTR
			)
		)


class MulticastAddressResponse(NDRCALL):
	structure = (
			(
			'bstrMulticastAddress',
			BSTR
			)
		)


class ADsPath(NDRCALL):
	OPNUM = 38
	structure = (

		)


class ADsPathResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	QueueGuid,
	QueueGuidResponse
	),1 : (
	ServiceTypeGuid,
	ServiceTypeGuidResponse
	),2 : (
	Label,
	LabelResponse
	),3 : (
	PathName,
	PathNameResponse
	),4 : (
	FormatName,
	FormatNameResponse
	),5 : (
	IsTransactional,
	IsTransactionalResponse
	),6 : (
	PrivLevel,
	PrivLevelResponse
	),7 : (
	Journal,
	JournalResponse
	),8 : (
	Quota,
	QuotaResponse
	),9 : (
	BasePriority,
	BasePriorityResponse
	),10 : (
	CreateTime,
	CreateTimeResponse
	),11 : (
	ModifyTime,
	ModifyTimeResponse
	),12 : (
	Authenticate,
	AuthenticateResponse
	),13 : (
	JournalQuota,
	JournalQuotaResponse
	),14 : (
	IsWorldReadable,
	IsWorldReadableResponse
	),15 : (
	Create,
	CreateResponse
	),16 : (
	Delete,
	DeleteResponse
	),17 : (
	Open,
	OpenResponse
	),18 : (
	Refresh,
	RefreshResponse
	),19 : (
	Update,
	UpdateResponse
	),20 : (
	PathNameDNS,
	PathNameDNSResponse
	),21 : (
	Properties,
	PropertiesResponse
	),22 : (
	Security,
	SecurityResponse
	),23 : (
	IsTransactional2,
	IsTransactional2Response
	),24 : (
	IsWorldReadable2,
	IsWorldReadable2Response
	),25 : (
	MulticastAddress,
	MulticastAddressResponse
	),26 : (
	ADsPath,
	ADsPathResponse
	)}
#################################################################################
#IMSMQQueueInfos Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFOS = uuidtup_to_bin(('D7D6E07D-DCCD-110-AA4B-0060970EBAE','0.0'))
class Reset(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Next(NDRCALL):
	OPNUM = 1
	structure = (

		)


class NextResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Reset,
	ResetResponse
	),1 : (
	Next,
	NextResponse
	)}
#################################################################################
#IMSMQQueueInfos2 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFOS2 = uuidtup_to_bin(('eba96b0f-2168-113-898-00020746','0.0'))
class Reset(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Next(NDRCALL):
	OPNUM = 1
	structure = (

		)


class NextResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 2
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Reset,
	ResetResponse
	),1 : (
	Next,
	NextResponse
	),2 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQQueueInfos3 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFOS3 = uuidtup_to_bin(('eba96b1e-2168-113-898-00020746','0.0'))
class Reset(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Next(NDRCALL):
	OPNUM = 1
	structure = (

		)


class NextResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 2
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Reset,
	ResetResponse
	),1 : (
	Next,
	NextResponse
	),2 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQQueueInfos4 Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEINFOS4 = uuidtup_to_bin(('eba96b22-2168-113-898-00020746','0.0'))
class Reset(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ResetResponse(NDRCALL):
	structure = (

		)


class Next(NDRCALL):
	OPNUM = 1
	structure = (

		)


class NextResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 2
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Reset,
	ResetResponse
	),1 : (
	Next,
	NextResponse
	),2 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQTransaction Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTION = uuidtup_to_bin(('D7D6E07F-DCCD-110-AA4B-0060970EBAE','0.0'))
class Transaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class TransactionResponse(NDRCALL):
	structure = (

		)


class Commit(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'fRetaining',
			VARIANT
			),
			(
			'grfTC',
			VARIANT
			),
			(
			'grfRM',
			VARIANT
			)
		)


class CommitResponse(NDRCALL):
	structure = (
			(
			'fRetaining',
			VARIANT
			),
			(
			'grfTC',
			VARIANT
			),
			(
			'grfRM',
			VARIANT
			)
		)


class Abort(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'fRetaining',
			VARIANT
			),
			(
			'fAsync',
			VARIANT
			)
		)


class AbortResponse(NDRCALL):
	structure = (
			(
			'fRetaining',
			VARIANT
			),
			(
			'fAsync',
			VARIANT
			)
		)


OPNUMS = {0 : (
	Transaction,
	TransactionResponse
	),1 : (
	Commit,
	CommitResponse
	),2 : (
	Abort,
	AbortResponse
	)}
#################################################################################
#IMSMQTransaction2 Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTION2 = uuidtup_to_bin(('2CE0C5B0-6E67-11D2-B0E6-00E02C074F6B','0.0'))
class InitNew(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'varTransaction',
			VARIANT
			)
		)


class InitNewResponse(NDRCALL):
	structure = (
			(
			'varTransaction',
			VARIANT
			)
		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	InitNew,
	InitNewResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQTransaction3 Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTION3 = uuidtup_to_bin(('eba96b13-2168-113-898-00020746','0.0'))
class ITransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ITransactionResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	ITransaction,
	ITransactionResponse
	)}
#################################################################################
#IMSMQCoordinatedTransactionDispenser Definition
#################################################################################
MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER = uuidtup_to_bin(('D7D6E081-DCCD-110-AA4B-0060970EBAE','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	)}
#################################################################################
#IMSMQCoordinatedTransactionDispenser2 Definition
#################################################################################
MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER2 = uuidtup_to_bin(('eba96b10-2168-113-898-00020746','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQCoordinatedTransactionDispenser3 Definition
#################################################################################
MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER3 = uuidtup_to_bin(('eba96b14-2168-113-898-00020746','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQTransactionDispenser Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTIONDISPENSER = uuidtup_to_bin(('D7D6E083-DCCD-110-AA4B-0060970EBAE','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	)}
#################################################################################
#IMSMQTransactionDispenser2 Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTIONDISPENSER2 = uuidtup_to_bin(('eba96b11-2168-113-898-00020746','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQTransactionDispenser3 Definition
#################################################################################
MSRPC_UUID_IMSMQTRANSACTIONDISPENSER3 = uuidtup_to_bin(('eba96b15-2168-113-898-00020746','0.0'))
class BeginTransaction(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BeginTransactionResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BeginTransaction,
	BeginTransactionResponse
	),1 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQApplication Definition
#################################################################################
MSRPC_UUID_IMSMQAPPLICATION = uuidtup_to_bin(('D7D6E085-DCCD-110-AA4B-0060970EBAE','0.0'))
class MachineIdOfMachineName(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'MachineName',
			BSTR
			)
		)


class MachineIdOfMachineNameResponse(NDRCALL):
	structure = (
			(
			'MachineName',
			BSTR
			)
		)


OPNUMS = {0 : (
	MachineIdOfMachineName,
	MachineIdOfMachineNameResponse
	)}
#################################################################################
#IMSMQApplication2 Definition
#################################################################################
MSRPC_UUID_IMSMQAPPLICATION2 = uuidtup_to_bin(('12A30900-7300-11D2-B0E6-00E02C074F6B','0.0'))
class RegisterCertificate(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'Flags',
			VARIANT
			),
			(
			'ExternalCertificate',
			VARIANT
			)
		)


class RegisterCertificateResponse(NDRCALL):
	structure = (
			(
			'Flags',
			VARIANT
			),
			(
			'ExternalCertificate',
			VARIANT
			)
		)


class MachineNameOfMachineId(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'bstrGuid',
			BSTR
			)
		)


class MachineNameOfMachineIdResponse(NDRCALL):
	structure = (
			(
			'bstrGuid',
			BSTR
			)
		)


class MSMQVersionMajor(NDRCALL):
	OPNUM = 2
	structure = (

		)


class MSMQVersionMajorResponse(NDRCALL):
	structure = (

		)


class MSMQVersionMinor(NDRCALL):
	OPNUM = 3
	structure = (

		)


class MSMQVersionMinorResponse(NDRCALL):
	structure = (

		)


class MSMQVersionBuild(NDRCALL):
	OPNUM = 4
	structure = (

		)


class MSMQVersionBuildResponse(NDRCALL):
	structure = (

		)


class IsDsEnabled(NDRCALL):
	OPNUM = 5
	structure = (

		)


class IsDsEnabledResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 6
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	RegisterCertificate,
	RegisterCertificateResponse
	),1 : (
	MachineNameOfMachineId,
	MachineNameOfMachineIdResponse
	),2 : (
	MSMQVersionMajor,
	MSMQVersionMajorResponse
	),3 : (
	MSMQVersionMinor,
	MSMQVersionMinorResponse
	),4 : (
	MSMQVersionBuild,
	MSMQVersionBuildResponse
	),5 : (
	IsDsEnabled,
	IsDsEnabledResponse
	),6 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQApplication3 Definition
#################################################################################
MSRPC_UUID_IMSMQAPPLICATION3 = uuidtup_to_bin(('eba96b1f-2168-113-898-00020746','0.0'))
class ActiveQueues(NDRCALL):
	OPNUM = 0
	structure = (

		)


class ActiveQueuesResponse(NDRCALL):
	structure = (

		)


class PrivateQueues(NDRCALL):
	OPNUM = 1
	structure = (

		)


class PrivateQueuesResponse(NDRCALL):
	structure = (

		)


class DirectoryServiceServer(NDRCALL):
	OPNUM = 2
	structure = (

		)


class DirectoryServiceServerResponse(NDRCALL):
	structure = (

		)


class IsConnected(NDRCALL):
	OPNUM = 3
	structure = (

		)


class IsConnectedResponse(NDRCALL):
	structure = (

		)


class BytesInAllQueues(NDRCALL):
	OPNUM = 4
	structure = (

		)


class BytesInAllQueuesResponse(NDRCALL):
	structure = (

		)


class Machine(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'bstrMachine',
			BSTR
			)
		)


class MachineResponse(NDRCALL):
	structure = (
			(
			'bstrMachine',
			BSTR
			)
		)


class Machine(NDRCALL):
	OPNUM = 6
	structure = (

		)


class MachineResponse(NDRCALL):
	structure = (

		)


class Connect(NDRCALL):
	OPNUM = 7
	structure = (

		)


class ConnectResponse(NDRCALL):
	structure = (

		)


class Disconnect(NDRCALL):
	OPNUM = 8
	structure = (

		)


class DisconnectResponse(NDRCALL):
	structure = (

		)


class Tidy(NDRCALL):
	OPNUM = 9
	structure = (

		)


class TidyResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	ActiveQueues,
	ActiveQueuesResponse
	),1 : (
	PrivateQueues,
	PrivateQueuesResponse
	),2 : (
	DirectoryServiceServer,
	DirectoryServiceServerResponse
	),3 : (
	IsConnected,
	IsConnectedResponse
	),4 : (
	BytesInAllQueues,
	BytesInAllQueuesResponse
	),5 : (
	Machine,
	MachineResponse
	),6 : (
	Connect,
	ConnectResponse
	),7 : (
	Disconnect,
	DisconnectResponse
	),8 : (
	Tidy,
	TidyResponse
	)}
#################################################################################
#IMSMQDestination Definition
#################################################################################
MSRPC_UUID_IMSMQDESTINATION = uuidtup_to_bin(('eba96b16-2168-113-898-00020746','0.0'))
class Open(NDRCALL):
	OPNUM = 0
	structure = (

		)


class OpenResponse(NDRCALL):
	structure = (

		)


class Close(NDRCALL):
	OPNUM = 1
	structure = (

		)


class CloseResponse(NDRCALL):
	structure = (

		)


class IsOpen(NDRCALL):
	OPNUM = 2
	structure = (

		)


class IsOpenResponse(NDRCALL):
	structure = (

		)


class IADs(NDRCALL):
	OPNUM = 3
	structure = (

		)


class IADsResponse(NDRCALL):
	structure = (

		)


class IADs(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'pIADs',
			IDISPATCH
			)
		)


class IADsResponse(NDRCALL):
	structure = (
			(
			'pIADs',
			IDISPATCH
			)
		)


class ADsPath(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ADsPathResponse(NDRCALL):
	structure = (

		)


class ADsPath(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'bstrADsPath',
			BSTR
			)
		)


class ADsPathResponse(NDRCALL):
	structure = (
			(
			'bstrADsPath',
			BSTR
			)
		)


class PathName(NDRCALL):
	OPNUM = 7
	structure = (

		)


class PathNameResponse(NDRCALL):
	structure = (

		)


class PathName(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class PathNameResponse(NDRCALL):
	structure = (
			(
			'bstrPathName',
			BSTR
			)
		)


class FormatName(NDRCALL):
	OPNUM = 9
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class FormatName(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class FormatNameResponse(NDRCALL):
	structure = (
			(
			'bstrFormatName',
			BSTR
			)
		)


class Destinations(NDRCALL):
	OPNUM = 11
	structure = (

		)


class DestinationsResponse(NDRCALL):
	structure = (

		)


class Destinations(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'pDestinations',
			IDISPATCH
			)
		)


class DestinationsResponse(NDRCALL):
	structure = (
			(
			'pDestinations',
			IDISPATCH
			)
		)


class Properties(NDRCALL):
	OPNUM = 13
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Open,
	OpenResponse
	),1 : (
	Close,
	CloseResponse
	),2 : (
	IsOpen,
	IsOpenResponse
	),3 : (
	IADs,
	IADsResponse
	),4 : (
	ADsPath,
	ADsPathResponse
	),5 : (
	PathName,
	PathNameResponse
	),6 : (
	FormatName,
	FormatNameResponse
	),7 : (
	Destinations,
	DestinationsResponse
	),8 : (
	Properties,
	PropertiesResponse
	)}
#################################################################################
#IMSMQPrivateDestination Definition
#################################################################################
MSRPC_UUID_IMSMQPRIVATEDESTINATION = uuidtup_to_bin(('eba96b17-2168-113-898-00020746','0.0'))
class Handle(NDRCALL):
	OPNUM = 0
	structure = (

		)


class HandleResponse(NDRCALL):
	structure = (

		)


class Handle(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'varHandle',
			VARIANT
			)
		)


class HandleResponse(NDRCALL):
	structure = (
			(
			'varHandle',
			VARIANT
			)
		)


OPNUMS = {0 : (
	Handle,
	HandleResponse
	)}
#################################################################################
#IMSMQCollection Definition
#################################################################################
MSRPC_UUID_IMSMQCOLLECTION = uuidtup_to_bin(('0188AC2F-ECB3-4173-9779-635CA2039C72','0.0'))
class Item(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'Index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'Index',
			VARIANT
			)
		)


class Count(NDRCALL):
	OPNUM = 1
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Item,
	ItemResponse
	),1 : (
	Count,
	CountResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	)}
#################################################################################
#IMSMQManagement Definition
#################################################################################
MSRPC_UUID_IMSMQMANAGEMENT = uuidtup_to_bin(('BE5F0241-E489-4957-8C4-A452FCF3E23E','0.0'))
class Init(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'Machine',
			VARIANT
			),
			(
			'Pathname',
			VARIANT
			),
			(
			'FormatName',
			VARIANT
			)
		)


class InitResponse(NDRCALL):
	structure = (
			(
			'Machine',
			VARIANT
			),
			(
			'Pathname',
			VARIANT
			),
			(
			'FormatName',
			VARIANT
			)
		)


class FormatName(NDRCALL):
	OPNUM = 1
	structure = (

		)


class FormatNameResponse(NDRCALL):
	structure = (

		)


class Machine(NDRCALL):
	OPNUM = 2
	structure = (

		)


class MachineResponse(NDRCALL):
	structure = (

		)


class MessageCount(NDRCALL):
	OPNUM = 3
	structure = (

		)


class MessageCountResponse(NDRCALL):
	structure = (

		)


class ForeignStatus(NDRCALL):
	OPNUM = 4
	structure = (

		)


class ForeignStatusResponse(NDRCALL):
	structure = (

		)


class QueueType(NDRCALL):
	OPNUM = 5
	structure = (

		)


class QueueTypeResponse(NDRCALL):
	structure = (

		)


class IsLocal(NDRCALL):
	OPNUM = 6
	structure = (

		)


class IsLocalResponse(NDRCALL):
	structure = (

		)


class TransactionalStatus(NDRCALL):
	OPNUM = 7
	structure = (

		)


class TransactionalStatusResponse(NDRCALL):
	structure = (

		)


class BytesInQueue(NDRCALL):
	OPNUM = 8
	structure = (

		)


class BytesInQueueResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Init,
	InitResponse
	),1 : (
	FormatName,
	FormatNameResponse
	),2 : (
	Machine,
	MachineResponse
	),3 : (
	MessageCount,
	MessageCountResponse
	),4 : (
	ForeignStatus,
	ForeignStatusResponse
	),5 : (
	QueueType,
	QueueTypeResponse
	),6 : (
	IsLocal,
	IsLocalResponse
	),7 : (
	TransactionalStatus,
	TransactionalStatusResponse
	),8 : (
	BytesInQueue,
	BytesInQueueResponse
	)}
#################################################################################
#IMSMQOutgoingQueueManagement Definition
#################################################################################
MSRPC_UUID_IMSMQOUTGOINGQUEUEMANAGEMENT = uuidtup_to_bin(('64C478FB-F9B0-4695-8A7F-439AC94326D3','0.0'))
class State(NDRCALL):
	OPNUM = 0
	structure = (

		)


class StateResponse(NDRCALL):
	structure = (

		)


class NextHops(NDRCALL):
	OPNUM = 1
	structure = (

		)


class NextHopsResponse(NDRCALL):
	structure = (

		)


class EodGetSendInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class EodGetSendInfoResponse(NDRCALL):
	structure = (

		)


class Resume(NDRCALL):
	OPNUM = 3
	structure = (

		)


class ResumeResponse(NDRCALL):
	structure = (

		)


class Pause(NDRCALL):
	OPNUM = 4
	structure = (

		)


class PauseResponse(NDRCALL):
	structure = (

		)


class EodResend(NDRCALL):
	OPNUM = 5
	structure = (

		)


class EodResendResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	State,
	StateResponse
	),1 : (
	NextHops,
	NextHopsResponse
	),2 : (
	EodGetSendInfo,
	EodGetSendInfoResponse
	),3 : (
	Resume,
	ResumeResponse
	),4 : (
	Pause,
	PauseResponse
	),5 : (
	EodResend,
	EodResendResponse
	)}
#################################################################################
#IMSMQQueueManagement Definition
#################################################################################
MSRPC_UUID_IMSMQQUEUEMANAGEMENT = uuidtup_to_bin(('7FBE7759-5760-444d-B8A5-5E7AB9A84CCE','0.0'))
class JournalMessageCount(NDRCALL):
	OPNUM = 0
	structure = (

		)


class JournalMessageCountResponse(NDRCALL):
	structure = (

		)


class BytesInJournal(NDRCALL):
	OPNUM = 1
	structure = (

		)


class BytesInJournalResponse(NDRCALL):
	structure = (

		)


class EodGetReceiveInfo(NDRCALL):
	OPNUM = 2
	structure = (

		)


class EodGetReceiveInfoResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	JournalMessageCount,
	JournalMessageCountResponse
	),1 : (
	BytesInJournal,
	BytesInJournalResponse
	),2 : (
	EodGetReceiveInfo,
	EodGetReceiveInfoResponse
	)}
