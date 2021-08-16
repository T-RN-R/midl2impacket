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


class ANONYMOUS19(NDRUNION):
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
			'Anonymous19',
			ANONYMOUS19
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
BYTE = BYTE
DataCollectorType = DWORD__ENUM
plaPerformanceCounter = 0
plaTrace = 1
plaConfiguration = 2
plaAlert = 3
plaApiTrace = 4
FileFormat = DWORD__ENUM
plaCommaSeparated = 0
plaTabSeparated = 1
plaSql = 2
plaBinary = 3
AutoPathFormat = DWORD__ENUM
plaNone = 0
plaPattern = 1
plaComputer = 2
plaMonthDayHour = 256
plaSerialNumber = 512
plaYearDayOfYear = 1024
plaYearMonth = 2048
plaYearMonthDay = 4096
plaYearMonthDayHour = 8192
plaMonthDayHourMinute = 16384
DataCollectorSetStatus = DWORD__ENUM
plaStopped = 0
plaRunning = 1
plaCompiling = 2
plaPending = 3
plaUndefined = 4
ClockType = DWORD__ENUM
plaTimeStamp = 0
plaPerformance = 1
plaSystem = 2
plaCycle = 3
StreamMode = DWORD__ENUM
plaFile = 1
plaRealTime = 2
plaBoth = 3
plaBuffering = 4
CommitMode = DWORD__ENUM
plaCreateNew = 1
plaModify = 2
plaCreateOrModify = 3
plaUpdateRunningInstance = 16
plaFlushTrace = 32
plaValidateOnly = 4096
ValueMapType = DWORD__ENUM
plaIndex = 1
plaFlag = 2
plaFlagArray = 3
plaValidation = 4
WeekDays = DWORD__ENUM
plaRunOnce = 0
plaSunday = 1
plaMonday = 2
plaTuesday = 4
plaWednesday = 8
plaThursday = 16
plaFriday = 32
plaSaturday = 64
plaEveryday = 127
ResourcePolicy = DWORD__ENUM
plaDeleteLargest = 0
plaDeleteOldest = 1
DataManagerSteps = DWORD__ENUM
plaCreateReport = 1
plaRunRules = 2
plaCreateHtml = 4
plaFolderActions = 8
plaResourceFreeing = 16
FolderActionSteps = DWORD__ENUM
plaCreateCab = 1
plaDeleteData = 2
plaSendCab = 4
plaDeleteCab = 8
plaDeleteReport = 16
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#IDataCollectorSet Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDataManager Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IFolderAction Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IFolderActionCollection Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IPerformanceCounterDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ITraceDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IConfigurationDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IAlertDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IApiTracingDataCollector Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDataCollectorCollection Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDataCollectorSetCollection Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ITraceDataProvider Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ITraceDataProviderCollection Definition
#################################################################################
OPNUMS = {}
#################################################################################
#ISchedule Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IScheduleCollection Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IValueMapItem Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IValueMap Definition
#################################################################################
OPNUMS = {}
#################################################################################
#IDataCollectorSet Definition
#################################################################################
MSRPC_UUID_IDATACOLLECTORSET = uuidtup_to_bin(('03837520-098b-11d8-9414-505054503030','0.0'))
class DataCollectors(NDRCALL):
	OPNUM = 0
	structure = (

		)


class DataCollectorsResponse(NDRCALL):
	structure = (

		)


class Duration(NDRCALL):
	OPNUM = 1
	structure = (

		)


class DurationResponse(NDRCALL):
	structure = (

		)


class Duration(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class DurationResponse(NDRCALL):
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class Description(NDRCALL):
	OPNUM = 3
	structure = (

		)


class DescriptionResponse(NDRCALL):
	structure = (

		)


class Description(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'description',
			BSTR
			)
		)


class DescriptionResponse(NDRCALL):
	structure = (
			(
			'description',
			BSTR
			)
		)


class DescriptionUnresolved(NDRCALL):
	OPNUM = 5
	structure = (

		)


class DescriptionUnresolvedResponse(NDRCALL):
	structure = (

		)


class DisplayName(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DisplayNameResponse(NDRCALL):
	structure = (

		)


class DisplayName(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'DisplayName',
			BSTR
			)
		)


class DisplayNameResponse(NDRCALL):
	structure = (
			(
			'DisplayName',
			BSTR
			)
		)


class DisplayNameUnresolved(NDRCALL):
	OPNUM = 8
	structure = (

		)


class DisplayNameUnresolvedResponse(NDRCALL):
	structure = (

		)


class Keywords(NDRCALL):
	OPNUM = 9
	structure = (

		)


class KeywordsResponse(NDRCALL):
	structure = (

		)


class Keywords(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'keywords',
			SAFEARRAY
			)
		)


class KeywordsResponse(NDRCALL):
	structure = (
			(
			'keywords',
			SAFEARRAY
			)
		)


class LatestOutputLocation(NDRCALL):
	OPNUM = 11
	structure = (

		)


class LatestOutputLocationResponse(NDRCALL):
	structure = (

		)


class LatestOutputLocation(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'path',
			BSTR
			)
		)


class LatestOutputLocationResponse(NDRCALL):
	structure = (
			(
			'path',
			BSTR
			)
		)


class Name(NDRCALL):
	OPNUM = 13
	structure = (

		)


class NameResponse(NDRCALL):
	structure = (

		)


class OutputLocation(NDRCALL):
	OPNUM = 14
	structure = (

		)


class OutputLocationResponse(NDRCALL):
	structure = (

		)


class RootPath(NDRCALL):
	OPNUM = 15
	structure = (

		)


class RootPathResponse(NDRCALL):
	structure = (

		)


class RootPath(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'folder',
			BSTR
			)
		)


class RootPathResponse(NDRCALL):
	structure = (
			(
			'folder',
			BSTR
			)
		)


class Segment(NDRCALL):
	OPNUM = 17
	structure = (

		)


class SegmentResponse(NDRCALL):
	structure = (

		)


class Segment(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'segment',
			VARIANT_BOOL
			)
		)


class SegmentResponse(NDRCALL):
	structure = (
			(
			'segment',
			VARIANT_BOOL
			)
		)


class SegmentMaxDuration(NDRCALL):
	OPNUM = 19
	structure = (

		)


class SegmentMaxDurationResponse(NDRCALL):
	structure = (

		)


class SegmentMaxDuration(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class SegmentMaxDurationResponse(NDRCALL):
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class SegmentMaxSize(NDRCALL):
	OPNUM = 21
	structure = (

		)


class SegmentMaxSizeResponse(NDRCALL):
	structure = (

		)


class SegmentMaxSize(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class SegmentMaxSizeResponse(NDRCALL):
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class SerialNumber(NDRCALL):
	OPNUM = 23
	structure = (

		)


class SerialNumberResponse(NDRCALL):
	structure = (

		)


class SerialNumber(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'index',
			UNSIGNED_LONG
			)
		)


class SerialNumberResponse(NDRCALL):
	structure = (
			(
			'index',
			UNSIGNED_LONG
			)
		)


class Server(NDRCALL):
	OPNUM = 25
	structure = (

		)


class ServerResponse(NDRCALL):
	structure = (

		)


class Status(NDRCALL):
	OPNUM = 26
	structure = (

		)


class StatusResponse(NDRCALL):
	structure = (

		)


class Subdirectory(NDRCALL):
	OPNUM = 27
	structure = (

		)


class SubdirectoryResponse(NDRCALL):
	structure = (

		)


class Subdirectory(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'folder',
			BSTR
			)
		)


class SubdirectoryResponse(NDRCALL):
	structure = (
			(
			'folder',
			BSTR
			)
		)


class SubdirectoryFormat(NDRCALL):
	OPNUM = 29
	structure = (

		)


class SubdirectoryFormatResponse(NDRCALL):
	structure = (

		)


class SubdirectoryFormat(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'format',
			AUTOPATHFORMAT
			)
		)


class SubdirectoryFormatResponse(NDRCALL):
	structure = (
			(
			'format',
			AUTOPATHFORMAT
			)
		)


class SubdirectoryFormatPattern(NDRCALL):
	OPNUM = 31
	structure = (

		)


class SubdirectoryFormatPatternResponse(NDRCALL):
	structure = (

		)


class SubdirectoryFormatPattern(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'pattern',
			BSTR
			)
		)


class SubdirectoryFormatPatternResponse(NDRCALL):
	structure = (
			(
			'pattern',
			BSTR
			)
		)


class Task(NDRCALL):
	OPNUM = 33
	structure = (

		)


class TaskResponse(NDRCALL):
	structure = (

		)


class Task(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskResponse(NDRCALL):
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskRunAsSelf(NDRCALL):
	OPNUM = 35
	structure = (

		)


class TaskRunAsSelfResponse(NDRCALL):
	structure = (

		)


class TaskRunAsSelf(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'RunAsSelf',
			VARIANT_BOOL
			)
		)


class TaskRunAsSelfResponse(NDRCALL):
	structure = (
			(
			'RunAsSelf',
			VARIANT_BOOL
			)
		)


class TaskArguments(NDRCALL):
	OPNUM = 37
	structure = (

		)


class TaskArgumentsResponse(NDRCALL):
	structure = (

		)


class TaskArguments(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskArgumentsResponse(NDRCALL):
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskUserTextArguments(NDRCALL):
	OPNUM = 39
	structure = (

		)


class TaskUserTextArgumentsResponse(NDRCALL):
	structure = (

		)


class TaskUserTextArguments(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'UserText',
			BSTR
			)
		)


class TaskUserTextArgumentsResponse(NDRCALL):
	structure = (
			(
			'UserText',
			BSTR
			)
		)


class Schedules(NDRCALL):
	OPNUM = 41
	structure = (

		)


class SchedulesResponse(NDRCALL):
	structure = (

		)


class SchedulesEnabled(NDRCALL):
	OPNUM = 42
	structure = (

		)


class SchedulesEnabledResponse(NDRCALL):
	structure = (

		)


class SchedulesEnabled(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'enabled',
			VARIANT_BOOL
			)
		)


class SchedulesEnabledResponse(NDRCALL):
	structure = (
			(
			'enabled',
			VARIANT_BOOL
			)
		)


class UserAccount(NDRCALL):
	OPNUM = 44
	structure = (

		)


class UserAccountResponse(NDRCALL):
	structure = (

		)


class Xml(NDRCALL):
	OPNUM = 45
	structure = (

		)


class XmlResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 46
	structure = (

		)


class SecurityResponse(NDRCALL):
	structure = (

		)


class Security(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'bstrSecurity',
			BSTR
			)
		)


class SecurityResponse(NDRCALL):
	structure = (
			(
			'bstrSecurity',
			BSTR
			)
		)


class StopOnCompletion(NDRCALL):
	OPNUM = 48
	structure = (

		)


class StopOnCompletionResponse(NDRCALL):
	structure = (

		)


class StopOnCompletion(NDRCALL):
	OPNUM = 49
	structure = (
			(
			'Stop',
			VARIANT_BOOL
			)
		)


class StopOnCompletionResponse(NDRCALL):
	structure = (
			(
			'Stop',
			VARIANT_BOOL
			)
		)


class DataManager(NDRCALL):
	OPNUM = 50
	structure = (

		)


class DataManagerResponse(NDRCALL):
	structure = (

		)


class SetCredentials(NDRCALL):
	OPNUM = 51
	structure = (

		)


class SetCredentialsResponse(NDRCALL):
	structure = (

		)


class Query(NDRCALL):
	OPNUM = 52
	structure = (
			(
			'name',
			BSTR
			),
			(
			'server',
			BSTR
			)
		)


class QueryResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			),
			(
			'server',
			BSTR
			)
		)


class Commit(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'name',
			BSTR
			),
			(
			'server',
			BSTR
			)
		)


class CommitResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			),
			(
			'server',
			BSTR
			)
		)


class Delete(NDRCALL):
	OPNUM = 54
	structure = (

		)


class DeleteResponse(NDRCALL):
	structure = (

		)


class Start(NDRCALL):
	OPNUM = 55
	structure = (
			(
			'Synchronous',
			VARIANT_BOOL
			)
		)


class StartResponse(NDRCALL):
	structure = (
			(
			'Synchronous',
			VARIANT_BOOL
			)
		)


class Stop(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'Synchronous',
			VARIANT_BOOL
			)
		)


class StopResponse(NDRCALL):
	structure = (
			(
			'Synchronous',
			VARIANT_BOOL
			)
		)


class SetXml(NDRCALL):
	OPNUM = 57
	structure = (
			(
			'xml',
			BSTR
			)
		)


class SetXmlResponse(NDRCALL):
	structure = (
			(
			'xml',
			BSTR
			)
		)


class SetValue(NDRCALL):
	OPNUM = 58
	structure = (

		)


class SetValueResponse(NDRCALL):
	structure = (

		)


class GetValue(NDRCALL):
	OPNUM = 59
	structure = (

		)


class GetValueResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	DataCollectors,
	DataCollectorsResponse
	),1 : (
	Duration,
	DurationResponse
	),2 : (
	Description,
	DescriptionResponse
	),3 : (
	DescriptionUnresolved,
	DescriptionUnresolvedResponse
	),4 : (
	DisplayName,
	DisplayNameResponse
	),5 : (
	DisplayNameUnresolved,
	DisplayNameUnresolvedResponse
	),6 : (
	Keywords,
	KeywordsResponse
	),7 : (
	LatestOutputLocation,
	LatestOutputLocationResponse
	),8 : (
	Name,
	NameResponse
	),9 : (
	OutputLocation,
	OutputLocationResponse
	),10 : (
	RootPath,
	RootPathResponse
	),11 : (
	Segment,
	SegmentResponse
	),12 : (
	SegmentMaxDuration,
	SegmentMaxDurationResponse
	),13 : (
	SegmentMaxSize,
	SegmentMaxSizeResponse
	),14 : (
	SerialNumber,
	SerialNumberResponse
	),15 : (
	Server,
	ServerResponse
	),16 : (
	Status,
	StatusResponse
	),17 : (
	Subdirectory,
	SubdirectoryResponse
	),18 : (
	SubdirectoryFormat,
	SubdirectoryFormatResponse
	),19 : (
	SubdirectoryFormatPattern,
	SubdirectoryFormatPatternResponse
	),20 : (
	Task,
	TaskResponse
	),21 : (
	TaskRunAsSelf,
	TaskRunAsSelfResponse
	),22 : (
	TaskArguments,
	TaskArgumentsResponse
	),23 : (
	TaskUserTextArguments,
	TaskUserTextArgumentsResponse
	),24 : (
	Schedules,
	SchedulesResponse
	),25 : (
	SchedulesEnabled,
	SchedulesEnabledResponse
	),26 : (
	UserAccount,
	UserAccountResponse
	),27 : (
	Xml,
	XmlResponse
	),28 : (
	Security,
	SecurityResponse
	),29 : (
	StopOnCompletion,
	StopOnCompletionResponse
	),30 : (
	DataManager,
	DataManagerResponse
	),31 : (
	SetCredentials,
	SetCredentialsResponse
	),32 : (
	Query,
	QueryResponse
	),33 : (
	Commit,
	CommitResponse
	),34 : (
	Delete,
	DeleteResponse
	),35 : (
	Start,
	StartResponse
	),36 : (
	Stop,
	StopResponse
	),37 : (
	SetXml,
	SetXmlResponse
	),38 : (
	SetValue,
	SetValueResponse
	),39 : (
	GetValue,
	GetValueResponse
	)}
#################################################################################
#IDataManager Definition
#################################################################################
MSRPC_UUID_IDATAMANAGER = uuidtup_to_bin(('03837541-098b-11d8-9414-505054503030','0.0'))
class Enabled(NDRCALL):
	OPNUM = 0
	structure = (

		)


class EnabledResponse(NDRCALL):
	structure = (

		)


class Enabled(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'fEnabled',
			VARIANT_BOOL
			)
		)


class EnabledResponse(NDRCALL):
	structure = (
			(
			'fEnabled',
			VARIANT_BOOL
			)
		)


class CheckBeforeRunning(NDRCALL):
	OPNUM = 2
	structure = (

		)


class CheckBeforeRunningResponse(NDRCALL):
	structure = (

		)


class CheckBeforeRunning(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'fCheck',
			VARIANT_BOOL
			)
		)


class CheckBeforeRunningResponse(NDRCALL):
	structure = (
			(
			'fCheck',
			VARIANT_BOOL
			)
		)


class MinFreeDisk(NDRCALL):
	OPNUM = 4
	structure = (

		)


class MinFreeDiskResponse(NDRCALL):
	structure = (

		)


class MinFreeDisk(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'MinFreeDisk',
			ULONG
			)
		)


class MinFreeDiskResponse(NDRCALL):
	structure = (
			(
			'MinFreeDisk',
			ULONG
			)
		)


class MaxSize(NDRCALL):
	OPNUM = 6
	structure = (

		)


class MaxSizeResponse(NDRCALL):
	structure = (

		)


class MaxSize(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'ulMaxSize',
			ULONG
			)
		)


class MaxSizeResponse(NDRCALL):
	structure = (
			(
			'ulMaxSize',
			ULONG
			)
		)


class MaxFolderCount(NDRCALL):
	OPNUM = 8
	structure = (

		)


class MaxFolderCountResponse(NDRCALL):
	structure = (

		)


class MaxFolderCount(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'ulMaxFolderCount',
			ULONG
			)
		)


class MaxFolderCountResponse(NDRCALL):
	structure = (
			(
			'ulMaxFolderCount',
			ULONG
			)
		)


class ResourcePolicy(NDRCALL):
	OPNUM = 10
	structure = (

		)


class ResourcePolicyResponse(NDRCALL):
	structure = (

		)


class ResourcePolicy(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'Policy',
			RESOURCEPOLICY
			)
		)


class ResourcePolicyResponse(NDRCALL):
	structure = (
			(
			'Policy',
			RESOURCEPOLICY
			)
		)


class FolderActions(NDRCALL):
	OPNUM = 12
	structure = (

		)


class FolderActionsResponse(NDRCALL):
	structure = (

		)


class ReportSchema(NDRCALL):
	OPNUM = 13
	structure = (

		)


class ReportSchemaResponse(NDRCALL):
	structure = (

		)


class ReportSchema(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'ReportSchema',
			BSTR
			)
		)


class ReportSchemaResponse(NDRCALL):
	structure = (
			(
			'ReportSchema',
			BSTR
			)
		)


class ReportFileName(NDRCALL):
	OPNUM = 15
	structure = (

		)


class ReportFileNameResponse(NDRCALL):
	structure = (

		)


class ReportFileName(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'pbstrFilename',
			BSTR
			)
		)


class ReportFileNameResponse(NDRCALL):
	structure = (
			(
			'pbstrFilename',
			BSTR
			)
		)


class RuleTargetFileName(NDRCALL):
	OPNUM = 17
	structure = (

		)


class RuleTargetFileNameResponse(NDRCALL):
	structure = (

		)


class RuleTargetFileName(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'Filename',
			BSTR
			)
		)


class RuleTargetFileNameResponse(NDRCALL):
	structure = (
			(
			'Filename',
			BSTR
			)
		)


class EventsFileName(NDRCALL):
	OPNUM = 19
	structure = (

		)


class EventsFileNameResponse(NDRCALL):
	structure = (

		)


class EventsFileName(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'pbstrFilename',
			BSTR
			)
		)


class EventsFileNameResponse(NDRCALL):
	structure = (
			(
			'pbstrFilename',
			BSTR
			)
		)


class Rules(NDRCALL):
	OPNUM = 21
	structure = (

		)


class RulesResponse(NDRCALL):
	structure = (

		)


class Rules(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'bstrXml',
			BSTR
			)
		)


class RulesResponse(NDRCALL):
	structure = (
			(
			'bstrXml',
			BSTR
			)
		)


class Run(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'Steps',
			DATAMANAGERSTEPS
			),
			(
			'bstrFolder',
			BSTR
			)
		)


class RunResponse(NDRCALL):
	structure = (
			(
			'Steps',
			DATAMANAGERSTEPS
			),
			(
			'bstrFolder',
			BSTR
			)
		)


class Extract(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'CabFilename',
			BSTR
			),
			(
			'DestinationPath',
			BSTR
			)
		)


class ExtractResponse(NDRCALL):
	structure = (
			(
			'CabFilename',
			BSTR
			),
			(
			'DestinationPath',
			BSTR
			)
		)


OPNUMS = {0 : (
	Enabled,
	EnabledResponse
	),1 : (
	CheckBeforeRunning,
	CheckBeforeRunningResponse
	),2 : (
	MinFreeDisk,
	MinFreeDiskResponse
	),3 : (
	MaxSize,
	MaxSizeResponse
	),4 : (
	MaxFolderCount,
	MaxFolderCountResponse
	),5 : (
	ResourcePolicy,
	ResourcePolicyResponse
	),6 : (
	FolderActions,
	FolderActionsResponse
	),7 : (
	ReportSchema,
	ReportSchemaResponse
	),8 : (
	ReportFileName,
	ReportFileNameResponse
	),9 : (
	RuleTargetFileName,
	RuleTargetFileNameResponse
	),10 : (
	EventsFileName,
	EventsFileNameResponse
	),11 : (
	Rules,
	RulesResponse
	),12 : (
	Run,
	RunResponse
	),13 : (
	Extract,
	ExtractResponse
	)}
#################################################################################
#IFolderAction Definition
#################################################################################
MSRPC_UUID_IFOLDERACTION = uuidtup_to_bin(('03837543-098b-11d8-9414-505054503030','0.0'))
class Age(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AgeResponse(NDRCALL):
	structure = (

		)


class Age(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'ulAge',
			ULONG
			)
		)


class AgeResponse(NDRCALL):
	structure = (
			(
			'ulAge',
			ULONG
			)
		)


class Size(NDRCALL):
	OPNUM = 2
	structure = (

		)


class SizeResponse(NDRCALL):
	structure = (

		)


class Size(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'ulAge',
			ULONG
			)
		)


class SizeResponse(NDRCALL):
	structure = (
			(
			'ulAge',
			ULONG
			)
		)


class Actions(NDRCALL):
	OPNUM = 4
	structure = (

		)


class ActionsResponse(NDRCALL):
	structure = (

		)


class Actions(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'Steps',
			FOLDERACTIONSTEPS
			)
		)


class ActionsResponse(NDRCALL):
	structure = (
			(
			'Steps',
			FOLDERACTIONSTEPS
			)
		)


class SendCabTo(NDRCALL):
	OPNUM = 6
	structure = (

		)


class SendCabToResponse(NDRCALL):
	structure = (

		)


class SendCabTo(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'bstrDestination',
			BSTR
			)
		)


class SendCabToResponse(NDRCALL):
	structure = (
			(
			'bstrDestination',
			BSTR
			)
		)


OPNUMS = {0 : (
	Age,
	AgeResponse
	),1 : (
	Size,
	SizeResponse
	),2 : (
	Actions,
	ActionsResponse
	),3 : (
	SendCabTo,
	SendCabToResponse
	)}
#################################################################################
#IFolderActionCollection Definition
#################################################################################
MSRPC_UUID_IFOLDERACTIONCOLLECTION = uuidtup_to_bin(('03837544-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
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


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Add(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 4
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 6
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class CreateFolderAction(NDRCALL):
	OPNUM = 7
	structure = (

		)


class CreateFolderActionResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Add,
	AddResponse
	),4 : (
	Remove,
	RemoveResponse
	),5 : (
	Clear,
	ClearResponse
	),6 : (
	AddRange,
	AddRangeResponse
	),7 : (
	CreateFolderAction,
	CreateFolderActionResponse
	)}
#################################################################################
#IDataCollector Definition
#################################################################################
MSRPC_UUID_IDATACOLLECTOR = uuidtup_to_bin(('038374ff-098b-11d8-9414-505054503030','0.0'))
class DataCollectorSet(NDRCALL):
	OPNUM = 0
	structure = (

		)


class DataCollectorSetResponse(NDRCALL):
	structure = (

		)


class Opnum8NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (

		)


class Opnum8NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class DataCollectorType(NDRCALL):
	OPNUM = 2
	structure = (

		)


class DataCollectorTypeResponse(NDRCALL):
	structure = (

		)


class FileName(NDRCALL):
	OPNUM = 3
	structure = (

		)


class FileNameResponse(NDRCALL):
	structure = (

		)


class FileName(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'name',
			BSTR
			)
		)


class FileNameResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			)
		)


class FileNameFormat(NDRCALL):
	OPNUM = 5
	structure = (

		)


class FileNameFormatResponse(NDRCALL):
	structure = (

		)


class FileNameFormat(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'format',
			AUTOPATHFORMAT
			)
		)


class FileNameFormatResponse(NDRCALL):
	structure = (
			(
			'format',
			AUTOPATHFORMAT
			)
		)


class FileNameFormatPattern(NDRCALL):
	OPNUM = 7
	structure = (

		)


class FileNameFormatPatternResponse(NDRCALL):
	structure = (

		)


class FileNameFormatPattern(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'pattern',
			BSTR
			)
		)


class FileNameFormatPatternResponse(NDRCALL):
	structure = (
			(
			'pattern',
			BSTR
			)
		)


class LatestOutputLocation(NDRCALL):
	OPNUM = 9
	structure = (

		)


class LatestOutputLocationResponse(NDRCALL):
	structure = (

		)


class LatestOutputLocation(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'path',
			BSTR
			)
		)


class LatestOutputLocationResponse(NDRCALL):
	structure = (
			(
			'path',
			BSTR
			)
		)


class LogAppend(NDRCALL):
	OPNUM = 11
	structure = (

		)


class LogAppendResponse(NDRCALL):
	structure = (

		)


class LogAppend(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'append',
			VARIANT_BOOL
			)
		)


class LogAppendResponse(NDRCALL):
	structure = (
			(
			'append',
			VARIANT_BOOL
			)
		)


class LogCircular(NDRCALL):
	OPNUM = 13
	structure = (

		)


class LogCircularResponse(NDRCALL):
	structure = (

		)


class LogCircular(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'circular',
			VARIANT_BOOL
			)
		)


class LogCircularResponse(NDRCALL):
	structure = (
			(
			'circular',
			VARIANT_BOOL
			)
		)


class LogOverwrite(NDRCALL):
	OPNUM = 15
	structure = (

		)


class LogOverwriteResponse(NDRCALL):
	structure = (

		)


class LogOverwrite(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'overwrite',
			VARIANT_BOOL
			)
		)


class LogOverwriteResponse(NDRCALL):
	structure = (
			(
			'overwrite',
			VARIANT_BOOL
			)
		)


class Name(NDRCALL):
	OPNUM = 17
	structure = (

		)


class NameResponse(NDRCALL):
	structure = (

		)


class Name(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'name',
			BSTR
			)
		)


class NameResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			)
		)


class OutputLocation(NDRCALL):
	OPNUM = 19
	structure = (

		)


class OutputLocationResponse(NDRCALL):
	structure = (

		)


class Index(NDRCALL):
	OPNUM = 20
	structure = (

		)


class IndexResponse(NDRCALL):
	structure = (

		)


class Opnum28NotUsedOnWire(NDRCALL):
	OPNUM = 21
	structure = (

		)


class Opnum28NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Xml(NDRCALL):
	OPNUM = 22
	structure = (

		)


class XmlResponse(NDRCALL):
	structure = (

		)


class SetXml(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'Xml',
			BSTR
			)
		)


class SetXmlResponse(NDRCALL):
	structure = (
			(
			'Xml',
			BSTR
			)
		)


class Opnum31NotUsedOnWire(NDRCALL):
	OPNUM = 24
	structure = (

		)


class Opnum31NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	DataCollectorSet,
	DataCollectorSetResponse
	),1 : (
	Opnum8NotUsedOnWire,
	Opnum8NotUsedOnWireResponse
	),2 : (
	DataCollectorType,
	DataCollectorTypeResponse
	),3 : (
	FileName,
	FileNameResponse
	),4 : (
	FileNameFormat,
	FileNameFormatResponse
	),5 : (
	FileNameFormatPattern,
	FileNameFormatPatternResponse
	),6 : (
	LatestOutputLocation,
	LatestOutputLocationResponse
	),7 : (
	LogAppend,
	LogAppendResponse
	),8 : (
	LogCircular,
	LogCircularResponse
	),9 : (
	LogOverwrite,
	LogOverwriteResponse
	),10 : (
	Name,
	NameResponse
	),11 : (
	OutputLocation,
	OutputLocationResponse
	),12 : (
	Index,
	IndexResponse
	),13 : (
	Opnum28NotUsedOnWire,
	Opnum28NotUsedOnWireResponse
	),14 : (
	Xml,
	XmlResponse
	),15 : (
	SetXml,
	SetXmlResponse
	),16 : (
	Opnum31NotUsedOnWire,
	Opnum31NotUsedOnWireResponse
	)}
#################################################################################
#IPerformanceCounterDataCollector Definition
#################################################################################
MSRPC_UUID_IPERFORMANCECOUNTERDATACOLLECTOR = uuidtup_to_bin(('03837506-098b-11d8-9414-505054503030','0.0'))
class DataSourceName(NDRCALL):
	OPNUM = 0
	structure = (

		)


class DataSourceNameResponse(NDRCALL):
	structure = (

		)


class DataSourceName(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'dsn',
			BSTR
			)
		)


class DataSourceNameResponse(NDRCALL):
	structure = (
			(
			'dsn',
			BSTR
			)
		)


class PerformanceCounters(NDRCALL):
	OPNUM = 2
	structure = (

		)


class PerformanceCountersResponse(NDRCALL):
	structure = (

		)


class PerformanceCounters(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'counters',
			SAFEARRAY
			)
		)


class PerformanceCountersResponse(NDRCALL):
	structure = (
			(
			'counters',
			SAFEARRAY
			)
		)


class LogFileFormat(NDRCALL):
	OPNUM = 4
	structure = (

		)


class LogFileFormatResponse(NDRCALL):
	structure = (

		)


class LogFileFormat(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'format',
			FILEFORMAT
			)
		)


class LogFileFormatResponse(NDRCALL):
	structure = (
			(
			'format',
			FILEFORMAT
			)
		)


class SampleInterval(NDRCALL):
	OPNUM = 6
	structure = (

		)


class SampleIntervalResponse(NDRCALL):
	structure = (

		)


class SampleInterval(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'interval',
			UNSIGNED_LONG
			)
		)


class SampleIntervalResponse(NDRCALL):
	structure = (
			(
			'interval',
			UNSIGNED_LONG
			)
		)


class SegmentMaxRecords(NDRCALL):
	OPNUM = 8
	structure = (

		)


class SegmentMaxRecordsResponse(NDRCALL):
	structure = (

		)


class SegmentMaxRecords(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'records',
			UNSIGNED_LONG
			)
		)


class SegmentMaxRecordsResponse(NDRCALL):
	structure = (
			(
			'records',
			UNSIGNED_LONG
			)
		)


OPNUMS = {0 : (
	DataSourceName,
	DataSourceNameResponse
	),1 : (
	PerformanceCounters,
	PerformanceCountersResponse
	),2 : (
	LogFileFormat,
	LogFileFormatResponse
	),3 : (
	SampleInterval,
	SampleIntervalResponse
	),4 : (
	SegmentMaxRecords,
	SegmentMaxRecordsResponse
	)}
#################################################################################
#IConfigurationDataCollector Definition
#################################################################################
MSRPC_UUID_ICONFIGURATIONDATACOLLECTOR = uuidtup_to_bin(('03837514-098b-11d8-9414-505054503030','0.0'))
class FileMaxCount(NDRCALL):
	OPNUM = 0
	structure = (

		)


class FileMaxCountResponse(NDRCALL):
	structure = (

		)


class FileMaxCount(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'count',
			UNSIGNED_LONG
			)
		)


class FileMaxCountResponse(NDRCALL):
	structure = (
			(
			'count',
			UNSIGNED_LONG
			)
		)


class FileMaxRecursiveDepth(NDRCALL):
	OPNUM = 2
	structure = (

		)


class FileMaxRecursiveDepthResponse(NDRCALL):
	structure = (

		)


class FileMaxRecursiveDepth(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'depth',
			UNSIGNED_LONG
			)
		)


class FileMaxRecursiveDepthResponse(NDRCALL):
	structure = (
			(
			'depth',
			UNSIGNED_LONG
			)
		)


class FileMaxTotalSize(NDRCALL):
	OPNUM = 4
	structure = (

		)


class FileMaxTotalSizeResponse(NDRCALL):
	structure = (

		)


class FileMaxTotalSize(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class FileMaxTotalSizeResponse(NDRCALL):
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class Files(NDRCALL):
	OPNUM = 6
	structure = (

		)


class FilesResponse(NDRCALL):
	structure = (

		)


class Files(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'Files',
			SAFEARRAY
			)
		)


class FilesResponse(NDRCALL):
	structure = (
			(
			'Files',
			SAFEARRAY
			)
		)


class ManagementQueries(NDRCALL):
	OPNUM = 8
	structure = (

		)


class ManagementQueriesResponse(NDRCALL):
	structure = (

		)


class ManagementQueries(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'Queries',
			SAFEARRAY
			)
		)


class ManagementQueriesResponse(NDRCALL):
	structure = (
			(
			'Queries',
			SAFEARRAY
			)
		)


class QueryNetworkAdapters(NDRCALL):
	OPNUM = 10
	structure = (

		)


class QueryNetworkAdaptersResponse(NDRCALL):
	structure = (

		)


class QueryNetworkAdapters(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'network',
			VARIANT_BOOL
			)
		)


class QueryNetworkAdaptersResponse(NDRCALL):
	structure = (
			(
			'network',
			VARIANT_BOOL
			)
		)


class RegistryKeys(NDRCALL):
	OPNUM = 12
	structure = (

		)


class RegistryKeysResponse(NDRCALL):
	structure = (

		)


class RegistryKeys(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'query',
			SAFEARRAY
			)
		)


class RegistryKeysResponse(NDRCALL):
	structure = (
			(
			'query',
			SAFEARRAY
			)
		)


class RegistryMaxRecursiveDepth(NDRCALL):
	OPNUM = 14
	structure = (

		)


class RegistryMaxRecursiveDepthResponse(NDRCALL):
	structure = (

		)


class RegistryMaxRecursiveDepth(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'depth',
			UNSIGNED_LONG
			)
		)


class RegistryMaxRecursiveDepthResponse(NDRCALL):
	structure = (
			(
			'depth',
			UNSIGNED_LONG
			)
		)


class SystemStateFile(NDRCALL):
	OPNUM = 16
	structure = (

		)


class SystemStateFileResponse(NDRCALL):
	structure = (

		)


class SystemStateFile(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'FileName',
			BSTR
			)
		)


class SystemStateFileResponse(NDRCALL):
	structure = (
			(
			'FileName',
			BSTR
			)
		)


OPNUMS = {0 : (
	FileMaxCount,
	FileMaxCountResponse
	),1 : (
	FileMaxRecursiveDepth,
	FileMaxRecursiveDepthResponse
	),2 : (
	FileMaxTotalSize,
	FileMaxTotalSizeResponse
	),3 : (
	Files,
	FilesResponse
	),4 : (
	ManagementQueries,
	ManagementQueriesResponse
	),5 : (
	QueryNetworkAdapters,
	QueryNetworkAdaptersResponse
	),6 : (
	RegistryKeys,
	RegistryKeysResponse
	),7 : (
	RegistryMaxRecursiveDepth,
	RegistryMaxRecursiveDepthResponse
	),8 : (
	SystemStateFile,
	SystemStateFileResponse
	)}
#################################################################################
#IAlertDataCollector Definition
#################################################################################
MSRPC_UUID_IALERTDATACOLLECTOR = uuidtup_to_bin(('03837516-098b-11d8-9414-505054503030','0.0'))
class AlertThresholds(NDRCALL):
	OPNUM = 0
	structure = (

		)


class AlertThresholdsResponse(NDRCALL):
	structure = (

		)


class AlertThresholds(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'alerts',
			SAFEARRAY
			)
		)


class AlertThresholdsResponse(NDRCALL):
	structure = (
			(
			'alerts',
			SAFEARRAY
			)
		)


class EventLog(NDRCALL):
	OPNUM = 2
	structure = (

		)


class EventLogResponse(NDRCALL):
	structure = (

		)


class EventLog(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'log',
			VARIANT_BOOL
			)
		)


class EventLogResponse(NDRCALL):
	structure = (
			(
			'log',
			VARIANT_BOOL
			)
		)


class SampleInterval(NDRCALL):
	OPNUM = 4
	structure = (

		)


class SampleIntervalResponse(NDRCALL):
	structure = (

		)


class SampleInterval(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'interval',
			UNSIGNED_LONG
			)
		)


class SampleIntervalResponse(NDRCALL):
	structure = (
			(
			'interval',
			UNSIGNED_LONG
			)
		)


class Task(NDRCALL):
	OPNUM = 6
	structure = (

		)


class TaskResponse(NDRCALL):
	structure = (

		)


class Task(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskResponse(NDRCALL):
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskRunAsSelf(NDRCALL):
	OPNUM = 8
	structure = (

		)


class TaskRunAsSelfResponse(NDRCALL):
	structure = (

		)


class TaskRunAsSelf(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'RunAsSelf',
			VARIANT_BOOL
			)
		)


class TaskRunAsSelfResponse(NDRCALL):
	structure = (
			(
			'RunAsSelf',
			VARIANT_BOOL
			)
		)


class TaskArguments(NDRCALL):
	OPNUM = 10
	structure = (

		)


class TaskArgumentsResponse(NDRCALL):
	structure = (

		)


class TaskArguments(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskArgumentsResponse(NDRCALL):
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskUserTextArguments(NDRCALL):
	OPNUM = 12
	structure = (

		)


class TaskUserTextArgumentsResponse(NDRCALL):
	structure = (

		)


class TaskUserTextArguments(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'task',
			BSTR
			)
		)


class TaskUserTextArgumentsResponse(NDRCALL):
	structure = (
			(
			'task',
			BSTR
			)
		)


class TriggerDataCollectorSet(NDRCALL):
	OPNUM = 14
	structure = (

		)


class TriggerDataCollectorSetResponse(NDRCALL):
	structure = (

		)


class TriggerDataCollectorSet(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'name',
			BSTR
			)
		)


class TriggerDataCollectorSetResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			)
		)


OPNUMS = {0 : (
	AlertThresholds,
	AlertThresholdsResponse
	),1 : (
	EventLog,
	EventLogResponse
	),2 : (
	SampleInterval,
	SampleIntervalResponse
	),3 : (
	Task,
	TaskResponse
	),4 : (
	TaskRunAsSelf,
	TaskRunAsSelfResponse
	),5 : (
	TaskArguments,
	TaskArgumentsResponse
	),6 : (
	TaskUserTextArguments,
	TaskUserTextArgumentsResponse
	),7 : (
	TriggerDataCollectorSet,
	TriggerDataCollectorSetResponse
	)}
#################################################################################
#ITraceDataCollector Definition
#################################################################################
MSRPC_UUID_ITRACEDATACOLLECTOR = uuidtup_to_bin(('0383750b-098b-11d8-9414-505054503030','0.0'))
class BufferSize(NDRCALL):
	OPNUM = 0
	structure = (

		)


class BufferSizeResponse(NDRCALL):
	structure = (

		)


class BufferSize(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class BufferSizeResponse(NDRCALL):
	structure = (
			(
			'size',
			UNSIGNED_LONG
			)
		)


class BuffersLost(NDRCALL):
	OPNUM = 2
	structure = (

		)


class BuffersLostResponse(NDRCALL):
	structure = (

		)


class Opnum35NotUsedOnWire(NDRCALL):
	OPNUM = 3
	structure = (

		)


class Opnum35NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class BuffersWritten(NDRCALL):
	OPNUM = 4
	structure = (

		)


class BuffersWrittenResponse(NDRCALL):
	structure = (

		)


class Opnum37NotUsedOnWire(NDRCALL):
	OPNUM = 5
	structure = (

		)


class Opnum37NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class ClockType(NDRCALL):
	OPNUM = 6
	structure = (

		)


class ClockTypeResponse(NDRCALL):
	structure = (

		)


class ClockType(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'clock',
			CLOCKTYPE
			)
		)


class ClockTypeResponse(NDRCALL):
	structure = (
			(
			'clock',
			CLOCKTYPE
			)
		)


class EventsLost(NDRCALL):
	OPNUM = 8
	structure = (

		)


class EventsLostResponse(NDRCALL):
	structure = (

		)


class Opnum41NotUsedOnWire(NDRCALL):
	OPNUM = 9
	structure = (

		)


class Opnum41NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class ExtendedModes(NDRCALL):
	OPNUM = 10
	structure = (

		)


class ExtendedModesResponse(NDRCALL):
	structure = (

		)


class ExtendedModes(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'mode',
			UNSIGNED_LONG
			)
		)


class ExtendedModesResponse(NDRCALL):
	structure = (
			(
			'mode',
			UNSIGNED_LONG
			)
		)


class FlushTimer(NDRCALL):
	OPNUM = 12
	structure = (

		)


class FlushTimerResponse(NDRCALL):
	structure = (

		)


class FlushTimer(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class FlushTimerResponse(NDRCALL):
	structure = (
			(
			'seconds',
			UNSIGNED_LONG
			)
		)


class FreeBuffers(NDRCALL):
	OPNUM = 14
	structure = (

		)


class FreeBuffersResponse(NDRCALL):
	structure = (

		)


class Opnum47NotUsedOnWire(NDRCALL):
	OPNUM = 15
	structure = (

		)


class Opnum47NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Guid(NDRCALL):
	OPNUM = 16
	structure = (

		)


class GuidResponse(NDRCALL):
	structure = (

		)


class Guid(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'guid',
			GUID
			)
		)


class GuidResponse(NDRCALL):
	structure = (
			(
			'guid',
			GUID
			)
		)


class IsKernelTrace(NDRCALL):
	OPNUM = 18
	structure = (

		)


class IsKernelTraceResponse(NDRCALL):
	structure = (

		)


class MaximumBuffers(NDRCALL):
	OPNUM = 19
	structure = (

		)


class MaximumBuffersResponse(NDRCALL):
	structure = (

		)


class MaximumBuffers(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class MaximumBuffersResponse(NDRCALL):
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class MinimumBuffers(NDRCALL):
	OPNUM = 21
	structure = (

		)


class MinimumBuffersResponse(NDRCALL):
	structure = (

		)


class MinimumBuffers(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class MinimumBuffersResponse(NDRCALL):
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class NumberOfBuffers(NDRCALL):
	OPNUM = 23
	structure = (

		)


class NumberOfBuffersResponse(NDRCALL):
	structure = (

		)


class NumberOfBuffers(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class NumberOfBuffersResponse(NDRCALL):
	structure = (
			(
			'buffers',
			UNSIGNED_LONG
			)
		)


class PreallocateFile(NDRCALL):
	OPNUM = 25
	structure = (

		)


class PreallocateFileResponse(NDRCALL):
	structure = (

		)


class PreallocateFile(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'allocate',
			VARIANT_BOOL
			)
		)


class PreallocateFileResponse(NDRCALL):
	structure = (
			(
			'allocate',
			VARIANT_BOOL
			)
		)


class ProcessMode(NDRCALL):
	OPNUM = 27
	structure = (

		)


class ProcessModeResponse(NDRCALL):
	structure = (

		)


class ProcessMode(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'process',
			VARIANT_BOOL
			)
		)


class ProcessModeResponse(NDRCALL):
	structure = (
			(
			'process',
			VARIANT_BOOL
			)
		)


class RealTimeBuffersLost(NDRCALL):
	OPNUM = 29
	structure = (

		)


class RealTimeBuffersLostResponse(NDRCALL):
	structure = (

		)


class Opnum62NotUsedOnWire(NDRCALL):
	OPNUM = 30
	structure = (

		)


class Opnum62NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class SessionId(NDRCALL):
	OPNUM = 31
	structure = (

		)


class SessionIdResponse(NDRCALL):
	structure = (

		)


class Opnum64NotUsedOnWire(NDRCALL):
	OPNUM = 32
	structure = (

		)


class Opnum64NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class SessionName(NDRCALL):
	OPNUM = 33
	structure = (

		)


class SessionNameResponse(NDRCALL):
	structure = (

		)


class SessionName(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'name',
			BSTR
			)
		)


class SessionNameResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			)
		)


class SessionThreadId(NDRCALL):
	OPNUM = 35
	structure = (

		)


class SessionThreadIdResponse(NDRCALL):
	structure = (

		)


class Opnum68NotUsedOnWire(NDRCALL):
	OPNUM = 36
	structure = (

		)


class Opnum68NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class StreamMode(NDRCALL):
	OPNUM = 37
	structure = (

		)


class StreamModeResponse(NDRCALL):
	structure = (

		)


class StreamMode(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'mode',
			STREAMMODE
			)
		)


class StreamModeResponse(NDRCALL):
	structure = (
			(
			'mode',
			STREAMMODE
			)
		)


class TraceDataProviders(NDRCALL):
	OPNUM = 39
	structure = (

		)


class TraceDataProvidersResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	BufferSize,
	BufferSizeResponse
	),1 : (
	BuffersLost,
	BuffersLostResponse
	),2 : (
	Opnum35NotUsedOnWire,
	Opnum35NotUsedOnWireResponse
	),3 : (
	BuffersWritten,
	BuffersWrittenResponse
	),4 : (
	Opnum37NotUsedOnWire,
	Opnum37NotUsedOnWireResponse
	),5 : (
	ClockType,
	ClockTypeResponse
	),6 : (
	EventsLost,
	EventsLostResponse
	),7 : (
	Opnum41NotUsedOnWire,
	Opnum41NotUsedOnWireResponse
	),8 : (
	ExtendedModes,
	ExtendedModesResponse
	),9 : (
	FlushTimer,
	FlushTimerResponse
	),10 : (
	FreeBuffers,
	FreeBuffersResponse
	),11 : (
	Opnum47NotUsedOnWire,
	Opnum47NotUsedOnWireResponse
	),12 : (
	Guid,
	GuidResponse
	),13 : (
	IsKernelTrace,
	IsKernelTraceResponse
	),14 : (
	MaximumBuffers,
	MaximumBuffersResponse
	),15 : (
	MinimumBuffers,
	MinimumBuffersResponse
	),16 : (
	NumberOfBuffers,
	NumberOfBuffersResponse
	),17 : (
	PreallocateFile,
	PreallocateFileResponse
	),18 : (
	ProcessMode,
	ProcessModeResponse
	),19 : (
	RealTimeBuffersLost,
	RealTimeBuffersLostResponse
	),20 : (
	Opnum62NotUsedOnWire,
	Opnum62NotUsedOnWireResponse
	),21 : (
	SessionId,
	SessionIdResponse
	),22 : (
	Opnum64NotUsedOnWire,
	Opnum64NotUsedOnWireResponse
	),23 : (
	SessionName,
	SessionNameResponse
	),24 : (
	SessionThreadId,
	SessionThreadIdResponse
	),25 : (
	Opnum68NotUsedOnWire,
	Opnum68NotUsedOnWireResponse
	),26 : (
	StreamMode,
	StreamModeResponse
	),27 : (
	TraceDataProviders,
	TraceDataProvidersResponse
	)}
#################################################################################
#IApiTracingDataCollector Definition
#################################################################################
MSRPC_UUID_IAPITRACINGDATACOLLECTOR = uuidtup_to_bin(('0383751a-098b-11d8-9414-505054503030','0.0'))
class LogApiNamesOnly(NDRCALL):
	OPNUM = 0
	structure = (

		)


class LogApiNamesOnlyResponse(NDRCALL):
	structure = (

		)


class LogApiNamesOnly(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'logapinames',
			VARIANT_BOOL
			)
		)


class LogApiNamesOnlyResponse(NDRCALL):
	structure = (
			(
			'logapinames',
			VARIANT_BOOL
			)
		)


class LogApisRecursively(NDRCALL):
	OPNUM = 2
	structure = (

		)


class LogApisRecursivelyResponse(NDRCALL):
	structure = (

		)


class LogApisRecursively(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'logrecursively',
			VARIANT_BOOL
			)
		)


class LogApisRecursivelyResponse(NDRCALL):
	structure = (
			(
			'logrecursively',
			VARIANT_BOOL
			)
		)


class ExePath(NDRCALL):
	OPNUM = 4
	structure = (

		)


class ExePathResponse(NDRCALL):
	structure = (

		)


class ExePath(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'exepath',
			BSTR
			)
		)


class ExePathResponse(NDRCALL):
	structure = (
			(
			'exepath',
			BSTR
			)
		)


class LogFilePath(NDRCALL):
	OPNUM = 6
	structure = (

		)


class LogFilePathResponse(NDRCALL):
	structure = (

		)


class LogFilePath(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'logfilepath',
			BSTR
			)
		)


class LogFilePathResponse(NDRCALL):
	structure = (
			(
			'logfilepath',
			BSTR
			)
		)


class IncludeModules(NDRCALL):
	OPNUM = 8
	structure = (

		)


class IncludeModulesResponse(NDRCALL):
	structure = (

		)


class IncludeModules(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'includemodules',
			SAFEARRAY
			)
		)


class IncludeModulesResponse(NDRCALL):
	structure = (
			(
			'includemodules',
			SAFEARRAY
			)
		)


class IncludeApis(NDRCALL):
	OPNUM = 10
	structure = (

		)


class IncludeApisResponse(NDRCALL):
	structure = (

		)


class IncludeApis(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'includeapis',
			SAFEARRAY
			)
		)


class IncludeApisResponse(NDRCALL):
	structure = (
			(
			'includeapis',
			SAFEARRAY
			)
		)


class ExcludeApis(NDRCALL):
	OPNUM = 12
	structure = (

		)


class ExcludeApisResponse(NDRCALL):
	structure = (

		)


class ExcludeApis(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'excludeapis',
			SAFEARRAY
			)
		)


class ExcludeApisResponse(NDRCALL):
	structure = (
			(
			'excludeapis',
			SAFEARRAY
			)
		)


OPNUMS = {0 : (
	LogApiNamesOnly,
	LogApiNamesOnlyResponse
	),1 : (
	LogApisRecursively,
	LogApisRecursivelyResponse
	),2 : (
	ExePath,
	ExePathResponse
	),3 : (
	LogFilePath,
	LogFilePathResponse
	),4 : (
	IncludeModules,
	IncludeModulesResponse
	),5 : (
	IncludeApis,
	IncludeApisResponse
	),6 : (
	ExcludeApis,
	ExcludeApisResponse
	)}
#################################################################################
#ITraceDataProvider Definition
#################################################################################
MSRPC_UUID_ITRACEDATAPROVIDER = uuidtup_to_bin(('03837512-098b-11d8-9414-505054503030','0.0'))
class DisplayName(NDRCALL):
	OPNUM = 0
	structure = (

		)


class DisplayNameResponse(NDRCALL):
	structure = (

		)


class DisplayName(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'name',
			BSTR
			)
		)


class DisplayNameResponse(NDRCALL):
	structure = (
			(
			'name',
			BSTR
			)
		)


class Guid(NDRCALL):
	OPNUM = 2
	structure = (

		)


class GuidResponse(NDRCALL):
	structure = (

		)


class Guid(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'guid',
			GUID
			)
		)


class GuidResponse(NDRCALL):
	structure = (
			(
			'guid',
			GUID
			)
		)


class Level(NDRCALL):
	OPNUM = 4
	structure = (

		)


class LevelResponse(NDRCALL):
	structure = (

		)


class KeywordsAny(NDRCALL):
	OPNUM = 5
	structure = (

		)


class KeywordsAnyResponse(NDRCALL):
	structure = (

		)


class KeywordsAll(NDRCALL):
	OPNUM = 6
	structure = (

		)


class KeywordsAllResponse(NDRCALL):
	structure = (

		)


class Properties(NDRCALL):
	OPNUM = 7
	structure = (

		)


class PropertiesResponse(NDRCALL):
	structure = (

		)


class FilterEnabled(NDRCALL):
	OPNUM = 8
	structure = (

		)


class FilterEnabledResponse(NDRCALL):
	structure = (

		)


class FilterEnabled(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'FilterEnabled',
			VARIANT_BOOL
			)
		)


class FilterEnabledResponse(NDRCALL):
	structure = (
			(
			'FilterEnabled',
			VARIANT_BOOL
			)
		)


class FilterType(NDRCALL):
	OPNUM = 10
	structure = (

		)


class FilterTypeResponse(NDRCALL):
	structure = (

		)


class FilterType(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'ulType',
			ULONG
			)
		)


class FilterTypeResponse(NDRCALL):
	structure = (
			(
			'ulType',
			ULONG
			)
		)


class FilterData(NDRCALL):
	OPNUM = 12
	structure = (

		)


class FilterDataResponse(NDRCALL):
	structure = (

		)


class FilterData(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'pData',
			SAFEARRAY
			)
		)


class FilterDataResponse(NDRCALL):
	structure = (
			(
			'pData',
			SAFEARRAY
			)
		)


class Query(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'bstrName',
			BSTR
			),
			(
			'bstrServer',
			BSTR
			)
		)


class QueryResponse(NDRCALL):
	structure = (
			(
			'bstrName',
			BSTR
			),
			(
			'bstrServer',
			BSTR
			)
		)


class Resolve(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pFrom',
			IDISPATCH
			)
		)


class ResolveResponse(NDRCALL):
	structure = (
			(
			'pFrom',
			IDISPATCH
			)
		)


class SetSecurity(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'Sddl',
			BSTR
			)
		)


class SetSecurityResponse(NDRCALL):
	structure = (
			(
			'Sddl',
			BSTR
			)
		)


class GetSecurity(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'SecurityInfo',
			ULONG
			)
		)


class GetSecurityResponse(NDRCALL):
	structure = (
			(
			'SecurityInfo',
			ULONG
			)
		)


class GetRegisteredProcesses(NDRCALL):
	OPNUM = 18
	structure = (

		)


class GetRegisteredProcessesResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	DisplayName,
	DisplayNameResponse
	),1 : (
	Guid,
	GuidResponse
	),2 : (
	Level,
	LevelResponse
	),3 : (
	KeywordsAny,
	KeywordsAnyResponse
	),4 : (
	KeywordsAll,
	KeywordsAllResponse
	),5 : (
	Properties,
	PropertiesResponse
	),6 : (
	FilterEnabled,
	FilterEnabledResponse
	),7 : (
	FilterType,
	FilterTypeResponse
	),8 : (
	FilterData,
	FilterDataResponse
	),9 : (
	Query,
	QueryResponse
	),10 : (
	Resolve,
	ResolveResponse
	),11 : (
	SetSecurity,
	SetSecurityResponse
	),12 : (
	GetSecurity,
	GetSecurityResponse
	),13 : (
	GetRegisteredProcesses,
	GetRegisteredProcessesResponse
	)}
#################################################################################
#ISchedule Definition
#################################################################################
MSRPC_UUID_ISCHEDULE = uuidtup_to_bin(('0383753a-098b-11d8-9414-505054503030','0.0'))
class StartDate(NDRCALL):
	OPNUM = 0
	structure = (

		)


class StartDateResponse(NDRCALL):
	structure = (

		)


class StartDate(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'start',
			VARIANT
			)
		)


class StartDateResponse(NDRCALL):
	structure = (
			(
			'start',
			VARIANT
			)
		)


class EndDate(NDRCALL):
	OPNUM = 2
	structure = (

		)


class EndDateResponse(NDRCALL):
	structure = (

		)


class EndDate(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'end',
			VARIANT
			)
		)


class EndDateResponse(NDRCALL):
	structure = (
			(
			'end',
			VARIANT
			)
		)


class StartTime(NDRCALL):
	OPNUM = 4
	structure = (

		)


class StartTimeResponse(NDRCALL):
	structure = (

		)


class StartTime(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'start',
			VARIANT
			)
		)


class StartTimeResponse(NDRCALL):
	structure = (
			(
			'start',
			VARIANT
			)
		)


class Days(NDRCALL):
	OPNUM = 6
	structure = (

		)


class DaysResponse(NDRCALL):
	structure = (

		)


class Days(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'days',
			WEEKDAYS
			)
		)


class DaysResponse(NDRCALL):
	structure = (
			(
			'days',
			WEEKDAYS
			)
		)


OPNUMS = {0 : (
	StartDate,
	StartDateResponse
	),1 : (
	EndDate,
	EndDateResponse
	),2 : (
	StartTime,
	StartTimeResponse
	),3 : (
	Days,
	DaysResponse
	)}
#################################################################################
#ITraceDataProviderCollection Definition
#################################################################################
MSRPC_UUID_ITRACEDATAPROVIDERCOLLECTION = uuidtup_to_bin(('03837510-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'index',
			VARIANT
			)
		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Add(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 4
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 6
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class CreateTraceDataProvider(NDRCALL):
	OPNUM = 7
	structure = (

		)


class CreateTraceDataProviderResponse(NDRCALL):
	structure = (

		)


class GetTraceDataProviders(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'server',
			BSTR
			)
		)


class GetTraceDataProvidersResponse(NDRCALL):
	structure = (
			(
			'server',
			BSTR
			)
		)


class GetTraceDataProvidersByProcess(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'Server',
			BSTR
			),
			(
			'Pid',
			ULONG
			)
		)


class GetTraceDataProvidersByProcessResponse(NDRCALL):
	structure = (
			(
			'Server',
			BSTR
			),
			(
			'Pid',
			ULONG
			)
		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Add,
	AddResponse
	),4 : (
	Remove,
	RemoveResponse
	),5 : (
	Clear,
	ClearResponse
	),6 : (
	AddRange,
	AddRangeResponse
	),7 : (
	CreateTraceDataProvider,
	CreateTraceDataProviderResponse
	),8 : (
	GetTraceDataProviders,
	GetTraceDataProvidersResponse
	),9 : (
	GetTraceDataProvidersByProcess,
	GetTraceDataProvidersByProcessResponse
	)}
#################################################################################
#IScheduleCollection Definition
#################################################################################
MSRPC_UUID_ISCHEDULECOLLECTION = uuidtup_to_bin(('0383753d-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'index',
			VARIANT
			)
		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Add(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 4
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 6
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class CreateSchedule(NDRCALL):
	OPNUM = 7
	structure = (

		)


class CreateScheduleResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Add,
	AddResponse
	),4 : (
	Remove,
	RemoveResponse
	),5 : (
	Clear,
	ClearResponse
	),6 : (
	AddRange,
	AddRangeResponse
	),7 : (
	CreateSchedule,
	CreateScheduleResponse
	)}
#################################################################################
#IDataCollectorCollection Definition
#################################################################################
MSRPC_UUID_IDATACOLLECTORCOLLECTION = uuidtup_to_bin(('03837502-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'index',
			VARIANT
			)
		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Add(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 4
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 6
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class CreateDataCollectorFromXml(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'bstrXml',
			BSTR
			)
		)


class CreateDataCollectorFromXmlResponse(NDRCALL):
	structure = (
			(
			'bstrXml',
			BSTR
			)
		)


class CreateDataCollector(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'Type',
			DATACOLLECTORTYPE
			)
		)


class CreateDataCollectorResponse(NDRCALL):
	structure = (
			(
			'Type',
			DATACOLLECTORTYPE
			)
		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Add,
	AddResponse
	),4 : (
	Remove,
	RemoveResponse
	),5 : (
	Clear,
	ClearResponse
	),6 : (
	AddRange,
	AddRangeResponse
	),7 : (
	CreateDataCollectorFromXml,
	CreateDataCollectorFromXmlResponse
	),8 : (
	CreateDataCollector,
	CreateDataCollectorResponse
	)}
#################################################################################
#IDataCollectorSetCollection Definition
#################################################################################
MSRPC_UUID_IDATACOLLECTORSETCOLLECTION = uuidtup_to_bin(('03837524-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'index',
			VARIANT
			)
		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Add(NDRCALL):
	OPNUM = 3
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 4
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 6
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class GetDataCollectorSets(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'server',
			BSTR
			),
			(
			'filter',
			BSTR
			)
		)


class GetDataCollectorSetsResponse(NDRCALL):
	structure = (
			(
			'server',
			BSTR
			),
			(
			'filter',
			BSTR
			)
		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Add,
	AddResponse
	),4 : (
	Remove,
	RemoveResponse
	),5 : (
	Clear,
	ClearResponse
	),6 : (
	AddRange,
	AddRangeResponse
	),7 : (
	GetDataCollectorSets,
	GetDataCollectorSetsResponse
	)}
#################################################################################
#IValueMapItem Definition
#################################################################################
MSRPC_UUID_IVALUEMAPITEM = uuidtup_to_bin(('03837533-098b-11d8-9414-505054503030','0.0'))
class Description(NDRCALL):
	OPNUM = 0
	structure = (

		)


class DescriptionResponse(NDRCALL):
	structure = (

		)


class Description(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'description',
			BSTR
			)
		)


class DescriptionResponse(NDRCALL):
	structure = (
			(
			'description',
			BSTR
			)
		)


class Enabled(NDRCALL):
	OPNUM = 2
	structure = (

		)


class EnabledResponse(NDRCALL):
	structure = (

		)


class Enabled(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'enabled',
			VARIANT_BOOL
			)
		)


class EnabledResponse(NDRCALL):
	structure = (
			(
			'enabled',
			VARIANT_BOOL
			)
		)


class Key(NDRCALL):
	OPNUM = 4
	structure = (

		)


class KeyResponse(NDRCALL):
	structure = (

		)


class Key(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'key',
			BSTR
			)
		)


class KeyResponse(NDRCALL):
	structure = (
			(
			'key',
			BSTR
			)
		)


class Value(NDRCALL):
	OPNUM = 6
	structure = (

		)


class ValueResponse(NDRCALL):
	structure = (

		)


class Value(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'Value',
			VARIANT
			)
		)


class ValueResponse(NDRCALL):
	structure = (
			(
			'Value',
			VARIANT
			)
		)


class ValueMapType(NDRCALL):
	OPNUM = 8
	structure = (

		)


class ValueMapTypeResponse(NDRCALL):
	structure = (

		)


class ValueMapType(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'type',
			VALUEMAPTYPE
			)
		)


class ValueMapTypeResponse(NDRCALL):
	structure = (
			(
			'type',
			VALUEMAPTYPE
			)
		)


OPNUMS = {0 : (
	Description,
	DescriptionResponse
	),1 : (
	Enabled,
	EnabledResponse
	),2 : (
	Key,
	KeyResponse
	),3 : (
	Value,
	ValueResponse
	),4 : (
	ValueMapType,
	ValueMapTypeResponse
	)}
#################################################################################
#IValueMap Definition
#################################################################################
MSRPC_UUID_IVALUEMAP = uuidtup_to_bin(('03837534-098b-11d8-9414-505054503030','0.0'))
class Count(NDRCALL):
	OPNUM = 0
	structure = (

		)


class CountResponse(NDRCALL):
	structure = (

		)


class Item(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'index',
			VARIANT
			)
		)


class ItemResponse(NDRCALL):
	structure = (
			(
			'index',
			VARIANT
			)
		)


class _NewEnum(NDRCALL):
	OPNUM = 2
	structure = (

		)


class _NewEnumResponse(NDRCALL):
	structure = (

		)


class Description(NDRCALL):
	OPNUM = 3
	structure = (

		)


class DescriptionResponse(NDRCALL):
	structure = (

		)


class Description(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'description',
			BSTR
			)
		)


class DescriptionResponse(NDRCALL):
	structure = (
			(
			'description',
			BSTR
			)
		)


class Value(NDRCALL):
	OPNUM = 5
	structure = (

		)


class ValueResponse(NDRCALL):
	structure = (

		)


class Value(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'Value',
			VARIANT
			)
		)


class ValueResponse(NDRCALL):
	structure = (
			(
			'Value',
			VARIANT
			)
		)


class ValueMapType(NDRCALL):
	OPNUM = 7
	structure = (

		)


class ValueMapTypeResponse(NDRCALL):
	structure = (

		)


class ValueMapType(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'type',
			VALUEMAPTYPE
			)
		)


class ValueMapTypeResponse(NDRCALL):
	structure = (
			(
			'type',
			VALUEMAPTYPE
			)
		)


class Add(NDRCALL):
	OPNUM = 9
	structure = (

		)


class AddResponse(NDRCALL):
	structure = (

		)


class Remove(NDRCALL):
	OPNUM = 10
	structure = (

		)


class RemoveResponse(NDRCALL):
	structure = (

		)


class Clear(NDRCALL):
	OPNUM = 11
	structure = (

		)


class ClearResponse(NDRCALL):
	structure = (

		)


class AddRange(NDRCALL):
	OPNUM = 12
	structure = (

		)


class AddRangeResponse(NDRCALL):
	structure = (

		)


class CreateValueMapItem(NDRCALL):
	OPNUM = 13
	structure = (

		)


class CreateValueMapItemResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	Count,
	CountResponse
	),1 : (
	Item,
	ItemResponse
	),2 : (
	_NewEnum,
	_NewEnumResponse
	),3 : (
	Description,
	DescriptionResponse
	),4 : (
	Value,
	ValueResponse
	),5 : (
	ValueMapType,
	ValueMapTypeResponse
	),6 : (
	Add,
	AddResponse
	),7 : (
	Remove,
	RemoveResponse
	),8 : (
	Clear,
	ClearResponse
	),9 : (
	AddRange,
	AddRangeResponse
	),10 : (
	CreateValueMapItem,
	CreateValueMapItemResponse
	)}
