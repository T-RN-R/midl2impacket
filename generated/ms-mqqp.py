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
#qm2qm Definition
#################################################################################
MSRPC_UUID_QM2QM = uuidtup_to_bin(('1088a980-eae5-11d0-8d9b-00a02453c337','0.0'))
PCTX_RRSESSION_HANDLE_TYPE = VOID
PCTX_REMOTEREAD_HANDLE_TYPE = VOID
REMOTEREADACK = DWORD__ENUM
RR_UNKNOWN = 0
RR_NACK = 1
class DATA_REMOTEREADDESC(NDRUniConformantArray):
	item = BYTE


class PTR_REMOTEREADDESC(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_REMOTEREADDESC
			)
		)


class REMOTEREADDESC(NDRSTRUCT):
	align = 1
	structure = (
			(
			'hRemoteQueue',
			DWORD
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
			'dwSize',
			DWORD
			),
			(
			'dwQueue',
			DWORD
			),
			(
			'dwRequestID',
			DWORD
			),
			(
			'Reserved',
			DWORD
			),
			(
			'dwArriveTime',
			DWORD
			),
			(
			'eAckNack',
			REMOTEREADACK
			),
			(
			'lpBuffer',
			PTR_REMOTEREADDESC
			)
		)


class REMOTEREADDESC2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pRemoteReadDesc',
			REMOTEREADDESC
			),
			(
			'SequentialId',
			ULONGLONG
			)
		)


class RemoteQMStartReceive(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpRemoteReadDesc',
			REMOTEREADDESC
			)
		)


class RemoteQMStartReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpRemoteReadDesc',
			REMOTEREADDESC
			)
		)


class RemoteQMEndReceive(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			PCTX_REMOTEREAD_HANDLE_TYPE
			),
			(
			'dwAck',
			DWORD
			)
		)


class RemoteQMEndReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			PCTX_REMOTEREAD_HANDLE_TYPE
			),
			(
			'dwAck',
			DWORD
			)
		)


class RemoteQMOpenQueue(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'dwMQS',
			DWORD
			),
			(
			'hQueue',
			DWORD
			),
			(
			'pQueue',
			DWORD
			),
			(
			'dwpContext',
			DWORD
			)
		)


class RemoteQMOpenQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pLicGuid',
			GUID
			),
			(
			'dwMQS',
			DWORD
			),
			(
			'hQueue',
			DWORD
			),
			(
			'pQueue',
			DWORD
			),
			(
			'dwpContext',
			DWORD
			)
		)


class RemoteQMCloseQueue(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			PCTX_RRSESSION_HANDLE_TYPE
			)
		)


class RemoteQMCloseQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'pphContext',
			PCTX_RRSESSION_HANDLE_TYPE
			)
		)


class RemoteQMCloseCursor(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			),
			(
			'hCursor',
			DWORD
			)
		)


class RemoteQMCloseCursorResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			),
			(
			'hCursor',
			DWORD
			)
		)


class RemoteQMCancelReceive(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			),
			(
			'pQueue',
			DWORD
			),
			(
			'dwRequestID',
			DWORD
			)
		)


class RemoteQMCancelReceiveResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			),
			(
			'pQueue',
			DWORD
			),
			(
			'dwRequestID',
			DWORD
			)
		)


class RemoteQMPurgeQueue(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			)
		)


class RemoteQMPurgeQueueResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'hQueue',
			DWORD
			)
		)


class RemoteQMGetQMQMServerPort(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwPortType',
			DWORD
			)
		)


class RemoteQMGetQMQMServerPortResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'dwPortType',
			DWORD
			)
		)


class RemoteQmGetVersion(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'hBind',
			HANDLE_T
			)
		)


class RemoteQmGetVersionResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			)
		)


class RemoteQMStartReceive2(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpRemoteReadDesc2',
			REMOTEREADDESC2
			)
		)


class RemoteQMStartReceive2Response(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'lpRemoteReadDesc2',
			REMOTEREADDESC2
			)
		)


class RemoteQMStartReceiveByLookupId(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'lpRemoteReadDesc2',
			REMOTEREADDESC2
			)
		)


class RemoteQMStartReceiveByLookupIdResponse(NDRCALL):
	structure = (
			(
			'hBind',
			HANDLE_T
			),
			(
			'LookupId',
			ULONGLONG
			),
			(
			'lpRemoteReadDesc2',
			REMOTEREADDESC2
			)
		)


OPNUMS = {0 : (
	RemoteQMStartReceive,
	RemoteQMStartReceiveResponse
	),1 : (
	RemoteQMEndReceive,
	RemoteQMEndReceiveResponse
	),2 : (
	RemoteQMOpenQueue,
	RemoteQMOpenQueueResponse
	),3 : (
	RemoteQMCloseQueue,
	RemoteQMCloseQueueResponse
	),4 : (
	RemoteQMCloseCursor,
	RemoteQMCloseCursorResponse
	),5 : (
	RemoteQMCancelReceive,
	RemoteQMCancelReceiveResponse
	),6 : (
	RemoteQMPurgeQueue,
	RemoteQMPurgeQueueResponse
	),7 : (
	RemoteQMGetQMQMServerPort,
	RemoteQMGetQMQMServerPortResponse
	),8 : (
	RemoteQmGetVersion,
	RemoteQmGetVersionResponse
	),9 : (
	RemoteQMStartReceive2,
	RemoteQMStartReceive2Response
	),10 : (
	RemoteQMStartReceiveByLookupId,
	RemoteQMStartReceiveByLookupIdResponse
	)}
