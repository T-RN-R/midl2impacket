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
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#type_scard_pack Definition
#################################################################################
MSRPC_UUID_TYPE_SCARD_PACK = uuidtup_to_bin(('A35AF600-9F4-11D-A076-080022D711','0.0'))
class DATA_REDIR_SCARDCONTEXT(NDRUniConformantArray):
	item = BYTE


class PTR_REDIR_SCARDCONTEXT(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_REDIR_SCARDCONTEXT
			)
		)


class REDIR_SCARDCONTEXT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbContext',
			UNSIGNED_LONG
			),
			(
			'pbContext',
			PTR_REDIR_SCARDCONTEXT
			)
		)


class DATA_REDIR_SCARDHANDLE(NDRUniConformantArray):
	item = BYTE


class PTR_REDIR_SCARDHANDLE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_REDIR_SCARDHANDLE
			)
		)


class REDIR_SCARDHANDLE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cbHandle',
			UNSIGNED_LONG
			),
			(
			'pbHandle',
			PTR_REDIR_SCARDHANDLE
			)
		)


class LONG_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			)
		)


class DATA_LISTREADERGROUPS_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_LISTREADERGROUPS_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LISTREADERGROUPS_RETURN
			)
		)


class LISTREADERGROUPS_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'msz',
			PTR_LISTREADERGROUPS_RETURN
			)
		)


class CONTEXT_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			)
		)


class CONTEXTANDSTRINGA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'sz',
			CONST_CHAR
			)
		)


class CONTEXTANDSTRINGW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'sz',
			CONST_WCHAR_T
			)
		)


class CONTEXTANDTWOSTRINGA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'sz1',
			CONST_CHAR
			),
			(
			'sz2',
			CONST_CHAR
			)
		)


class CONTEXTANDTWOSTRINGW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'sz1',
			CONST_WCHAR_T
			),
			(
			'sz2',
			CONST_WCHAR_T
			)
		)


class ESTABLISHCONTEXT_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwScope',
			UNSIGNED_LONG
			)
		)


class ESTABLISHCONTEXT_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'Context',
			REDIR_SCARDCONTEXT
			)
		)


class LISTREADERGROUPS_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'fmszGroupsIsNULL',
			LONG
			),
			(
			'cchGroups',
			UNSIGNED_LONG
			)
		)


class DATA_LISTREADERS_CALL(NDRUniConformantArray):
	item =  BYTE


class PTR_LISTREADERS_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LISTREADERS_CALL
			)
		)


class LISTREADERS_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'mszGroups',
			PTR_LISTREADERS_CALL
			),
			(
			'fmszReadersIsNULL',
			LONG
			),
			(
			'cchReaders',
			UNSIGNED_LONG
			)
		)


class READERSTATE_COMMON_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwCurrentState',
			UNSIGNED_LONG
			),
			(
			'dwEventState',
			UNSIGNED_LONG
			),
			(
			'cbAtr',
			UNSIGNED_LONG
			),
			(
			'rgbAtr',
			BYTE
			)
		)


class READERSTATEA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szReader',
			CONST_CHAR
			),
			(
			'Common',
			READERSTATE_COMMON_CALL
			)
		)


class READERSTATEW(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szReader',
			CONST_WCHAR_T
			),
			(
			'Common',
			READERSTATE_COMMON_CALL
			)
		)


class READERSTATE_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwCurrentState',
			UNSIGNED_LONG
			),
			(
			'dwEventState',
			UNSIGNED_LONG
			),
			(
			'cbAtr',
			UNSIGNED_LONG
			),
			(
			'rgbAtr',
			BYTE
			)
		)


class DATA_GETSTATUSCHANGEA_CALL(NDRUniConformantArray):
	item = READERSTATEA


class PTR_GETSTATUSCHANGEA_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_GETSTATUSCHANGEA_CALL
			)
		)


class GETSTATUSCHANGEA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'dwTimeOut',
			UNSIGNED_LONG
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_GETSTATUSCHANGEA_CALL
			)
		)


class DATA_LOCATECARDSA_CALL(NDRUniConformantArray):
	item = READERSTATEA


class PTR_LOCATECARDSA_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LOCATECARDSA_CALL
			)
		)


class LOCATECARDSA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'mszCards',
			 BYTE
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_LOCATECARDSA_CALL
			)
		)


class DATA_LOCATECARDSW_CALL(NDRUniConformantArray):
	item = READERSTATEW


class PTR_LOCATECARDSW_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LOCATECARDSW_CALL
			)
		)


class LOCATECARDSW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'mszCards',
			 BYTE
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_LOCATECARDSW_CALL
			)
		)


class LOCATECARDS_ATRMASK(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbAtr',
			UNSIGNED_LONG
			),
			(
			'rgbAtr',
			BYTE
			),
			(
			'rgbMask',
			BYTE
			)
		)


class DATA_LOCATECARDSBYATRA_CALL(NDRUniConformantArray):
	item = READERSTATEA


class PTR_LOCATECARDSBYATRA_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LOCATECARDSBYATRA_CALL
			)
		)


class LOCATECARDSBYATRA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cAtrs',
			UNSIGNED_LONG
			),
			(
			'rgAtrMasks',
			LOCATECARDS_ATRMASK
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_LOCATECARDSBYATRA_CALL
			)
		)


class DATA_LOCATECARDSBYATRW_CALL(NDRUniConformantArray):
	item = READERSTATEW


class PTR_LOCATECARDSBYATRW_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LOCATECARDSBYATRW_CALL
			)
		)


class LOCATECARDSBYATRW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'cAtrs',
			UNSIGNED_LONG
			),
			(
			'rgAtrMasks',
			LOCATECARDS_ATRMASK
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_LOCATECARDSBYATRW_CALL
			)
		)


class DATA_LOCATECARDS_RETURN(NDRUniConformantArray):
	item = READERSTATE_RETURN


class PTR_LOCATECARDS_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LOCATECARDS_RETURN
			)
		)


class LOCATECARDS_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_LOCATECARDS_RETURN
			)
		)


class DATA_GETSTATUSCHANGEW_CALL(NDRUniConformantArray):
	item = READERSTATEW


class PTR_GETSTATUSCHANGEW_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_GETSTATUSCHANGEW_CALL
			)
		)


class GETSTATUSCHANGEW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'dwTimeOut',
			UNSIGNED_LONG
			),
			(
			'cReaders',
			UNSIGNED_LONG
			),
			(
			'rgReaderStates',
			PTR_GETSTATUSCHANGEW_CALL
			)
		)


class CONNECT_COMMON(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'dwShareMode',
			UNSIGNED_LONG
			),
			(
			'dwPreferredProtocols',
			UNSIGNED_LONG
			)
		)


class CONNECTA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szReader',
			CONST_CHAR
			),
			(
			'Common',
			CONNECT_COMMON
			)
		)


class CONNECTW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szReader',
			CONST_WCHAR_T
			),
			(
			'Common',
			CONNECT_COMMON
			)
		)


class CONNECT_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwActiveProtocol',
			UNSIGNED_LONG
			)
		)


class RECONNECT_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwShareMode',
			UNSIGNED_LONG
			),
			(
			'dwPreferredProtocols',
			UNSIGNED_LONG
			),
			(
			'dwInitialization',
			UNSIGNED_LONG
			)
		)


class RECONNECT_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'dwActiveProtocol',
			UNSIGNED_LONG
			)
		)


class HCARDANDDISPOSITION_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwDisposition',
			UNSIGNED_LONG
			)
		)


class STATE_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'fpbAtrIsNULL',
			LONG
			),
			(
			'cbAtrLen',
			UNSIGNED_LONG
			)
		)


class DATA_STATE_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_STATE_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_STATE_RETURN
			)
		)


class STATE_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'dwState',
			UNSIGNED_LONG
			),
			(
			'dwProtocol',
			UNSIGNED_LONG
			),
			(
			'cbAtrLen',
			UNSIGNED_LONG
			),
			(
			'rgAtr',
			PTR_STATE_RETURN
			)
		)


class STATUS_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'fmszReaderNamesIsNULL',
			LONG
			),
			(
			'cchReaderLen',
			UNSIGNED_LONG
			),
			(
			'cbAtrLen',
			UNSIGNED_LONG
			)
		)


class DATA_STATUS_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_STATUS_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_STATUS_RETURN
			)
		)


class STATUS_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cBytes',
			UNSIGNED_LONG
			),
			(
			'mszReaderNames',
			PTR_STATUS_RETURN
			),
			(
			'dwState',
			UNSIGNED_LONG
			),
			(
			'dwProtocol',
			UNSIGNED_LONG
			),
			(
			'pbAtr',
			BYTE
			),
			(
			'cbAtrLen',
			UNSIGNED_LONG
			)
		)


class DATA_SCARDIO_REQUEST(NDRUniConformantArray):
	item = BYTE


class PTR_SCARDIO_REQUEST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SCARDIO_REQUEST
			)
		)


class SCARDIO_REQUEST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwProtocol',
			UNSIGNED_LONG
			),
			(
			'cbExtraBytes',
			UNSIGNED_LONG
			),
			(
			'pbExtraBytes',
			PTR_SCARDIO_REQUEST
			)
		)


class DATA_TRANSMIT_CALL(NDRUniConformantArray):
	item =  BYTE


class PTR_TRANSMIT_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TRANSMIT_CALL
			)
		)


class TRANSMIT_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'ioSendPci',
			SCARDIO_REQUEST
			),
			(
			'cbSendLength',
			UNSIGNED_LONG
			),
			(
			'pbSendBuffer',
			PTR_TRANSMIT_CALL
			),
			(
			'pioRecvPci',
			SCARDIO_REQUEST
			),
			(
			'fpbRecvBufferIsNULL',
			LONG
			),
			(
			'cbRecvLength',
			UNSIGNED_LONG
			)
		)


class DATA_TRANSMIT_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_TRANSMIT_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TRANSMIT_RETURN
			)
		)


class TRANSMIT_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'pioRecvPci',
			SCARDIO_REQUEST
			),
			(
			'cbRecvLength',
			UNSIGNED_LONG
			),
			(
			'pbRecvBuffer',
			PTR_TRANSMIT_RETURN
			)
		)


class GETTRANSMITCOUNT_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			)
		)


class GETTRANSMITCOUNT_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cTransmitCount',
			UNSIGNED_LONG
			)
		)


class DATA_CONTROL_CALL(NDRUniConformantArray):
	item =  BYTE


class PTR_CONTROL_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CONTROL_CALL
			)
		)


class CONTROL_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwControlCode',
			UNSIGNED_LONG
			),
			(
			'cbInBufferSize',
			UNSIGNED_LONG
			),
			(
			'pvInBuffer',
			PTR_CONTROL_CALL
			),
			(
			'fpvOutBufferIsNULL',
			LONG
			),
			(
			'cbOutBufferSize',
			UNSIGNED_LONG
			)
		)


class DATA_CONTROL_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_CONTROL_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_CONTROL_RETURN
			)
		)


class CONTROL_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cbOutBufferSize',
			UNSIGNED_LONG
			),
			(
			'pvOutBuffer',
			PTR_CONTROL_RETURN
			)
		)


class GETATTRIB_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwAttrId',
			UNSIGNED_LONG
			),
			(
			'fpbAttrIsNULL',
			LONG
			),
			(
			'cbAttrLen',
			UNSIGNED_LONG
			)
		)


class DATA_GETATTRIB_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_GETATTRIB_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_GETATTRIB_RETURN
			)
		)


class GETATTRIB_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cbAttrLen',
			UNSIGNED_LONG
			),
			(
			'pbAttr',
			PTR_GETATTRIB_RETURN
			)
		)


class DATA_SETATTRIB_CALL(NDRUniConformantArray):
	item =  BYTE


class PTR_SETATTRIB_CALL(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SETATTRIB_CALL
			)
		)


class SETATTRIB_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hCard',
			REDIR_SCARDHANDLE
			),
			(
			'dwAttrId',
			UNSIGNED_LONG
			),
			(
			'cbAttrLen',
			UNSIGNED_LONG
			),
			(
			'pbAttr',
			PTR_SETATTRIB_CALL
			)
		)


class READCACHE_COMMON(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'CardIdentifier',
			UUID
			),
			(
			'FreshnessCounter',
			UNSIGNED_LONG
			),
			(
			'fPbDataIsNULL',
			LONG
			),
			(
			'cbDataLen',
			UNSIGNED_LONG
			)
		)


class READCACHEA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szLookupName',
			CHAR
			),
			(
			'Common',
			READCACHE_COMMON
			)
		)


class READCACHEW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szLookupName',
			WCHAR_T
			),
			(
			'Common',
			READCACHE_COMMON
			)
		)


class DATA_READCACHE_RETURN(NDRUniConformantArray):
	item = BYTE


class PTR_READCACHE_RETURN(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_READCACHE_RETURN
			)
		)


class READCACHE_RETURN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReturnCode',
			LONG
			),
			(
			'cbDataLen',
			UNSIGNED_LONG
			),
			(
			'pbData',
			PTR_READCACHE_RETURN
			)
		)


class DATA_WRITECACHE_COMMON(NDRUniConformantArray):
	item = BYTE


class PTR_WRITECACHE_COMMON(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_WRITECACHE_COMMON
			)
		)


class WRITECACHE_COMMON(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Context',
			REDIR_SCARDCONTEXT
			),
			(
			'CardIdentifier',
			UUID
			),
			(
			'FreshnessCounter',
			UNSIGNED_LONG
			),
			(
			'cbDataLen',
			UNSIGNED_LONG
			),
			(
			'pbData',
			PTR_WRITECACHE_COMMON
			)
		)


class WRITECACHEA_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szLookupName',
			CHAR
			),
			(
			'Common',
			WRITECACHE_COMMON
			)
		)


class WRITECACHEW_CALL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'szLookupName',
			WCHAR_T
			),
			(
			'Common',
			WRITECACHE_COMMON
			)
		)


OPNUMS = {}
