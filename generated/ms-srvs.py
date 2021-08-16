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
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#srvsvc Definition
#################################################################################
MSRPC_UUID_SRVSVC = uuidtup_to_bin(('4B324FC8-1670-01D3-1278-5A47BF6EE188','0.0'))
SRVSVC_HANDLE = WCHAR_T
class CONNECTION_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'coni0_id',
			DWORD
			)
		)


class PCONNECTION_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECTION_INFO_0
			)
		)


class LPCONNECTION_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECTION_INFO_0
			)
		)


class CONNECT_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPCONNECTION_INFO_0
			)
		)


class PCONNECT_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_INFO_0_CONTAINER
			)
		)


class LPCONNECT_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_INFO_0_CONTAINER
			)
		)


class CONNECTION_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'coni1_id',
			DWORD
			),
			(
			'coni1_type',
			DWORD
			),
			(
			'coni1_num_opens',
			DWORD
			),
			(
			'coni1_num_users',
			DWORD
			),
			(
			'coni1_time',
			DWORD
			),
			(
			'coni1_username',
			WCHAR_T
			),
			(
			'coni1_netname',
			WCHAR_T
			)
		)


class PCONNECTION_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECTION_INFO_1
			)
		)


class LPCONNECTION_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECTION_INFO_1
			)
		)


class CONNECT_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPCONNECTION_INFO_1
			)
		)


class PCONNECT_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_INFO_1_CONTAINER
			)
		)


class LPCONNECT_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_INFO_1_CONTAINER
			)
		)


class CONNECT_ENUM_UNION(NDRUNION):
	union = {0 : (
		'Level0',
		CONNECT_INFO_0_CONTAINER
		),1 : (
		'Level1',
		CONNECT_INFO_1_CONTAINER
		)}


class CONNECT_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'ConnectInfo',
			CONNECT_ENUM_UNION
			)
		)


class PCONNECT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_ENUM_STRUCT
			)
		)


class LPCONNECT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			CONNECT_ENUM_STRUCT
			)
		)


class FILE_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'fi2_id',
			DWORD
			)
		)


class PFILE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_2
			)
		)


class LPFILE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_2
			)
		)


class FILE_INFO_2_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPFILE_INFO_2
			)
		)


class PFILE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_2_CONTAINER
			)
		)


class LPFILE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_2_CONTAINER
			)
		)


class FILE_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'fi3_id',
			DWORD
			),
			(
			'fi3_permissions',
			DWORD
			),
			(
			'fi3_num_locks',
			DWORD
			),
			(
			'fi3_pathname',
			WCHAR_T
			),
			(
			'fi3_username',
			WCHAR_T
			)
		)


class PFILE_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_3
			)
		)


class LPFILE_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_3
			)
		)


class FILE_INFO_3_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPFILE_INFO_3
			)
		)


class PFILE_INFO_3_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_3_CONTAINER
			)
		)


class LPFILE_INFO_3_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO_3_CONTAINER
			)
		)


class FILE_ENUM_UNION(NDRUNION):
	union = {2 : (
		'Level2',
		FILE_INFO_2_CONTAINER
		),3 : (
		'Level3',
		FILE_INFO_3_CONTAINER
		)}


class FILE_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'FileInfo',
			FILE_ENUM_UNION
			)
		)


class PFILE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_ENUM_STRUCT
			)
		)


class LPFILE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_ENUM_STRUCT
			)
		)


class FILE_INFO(NDRUNION):
	union = {2 : (
		'FileInfo2',
		LPFILE_INFO_2
		),3 : (
		'FileInfo3',
		LPFILE_INFO_3
		)}


class PFILE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO
			)
		)


class LPFILE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			FILE_INFO
			)
		)


class SESSION_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sesi0_cname',
			WCHAR_T
			)
		)


class PSESSION_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_0
			)
		)


class LPSESSION_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_0
			)
		)


class SESSION_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSESSION_INFO_0
			)
		)


class PSESSION_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_0_CONTAINER
			)
		)


class LPSESSION_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_0_CONTAINER
			)
		)


class SESSION_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sesi1_cname',
			WCHAR_T
			),
			(
			'sesi1_username',
			WCHAR_T
			),
			(
			'sesi1_num_opens',
			DWORD
			),
			(
			'sesi1_time',
			DWORD
			),
			(
			'sesi1_idle_time',
			DWORD
			),
			(
			'sesi1_user_flags',
			DWORD
			)
		)


class PSESSION_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_1
			)
		)


class LPSESSION_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_1
			)
		)


class SESSION_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSESSION_INFO_1
			)
		)


class PSESSION_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_1_CONTAINER
			)
		)


class LPSESSION_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_1_CONTAINER
			)
		)


class SESSION_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sesi2_cname',
			WCHAR_T
			),
			(
			'sesi2_username',
			WCHAR_T
			),
			(
			'sesi2_num_opens',
			DWORD
			),
			(
			'sesi2_time',
			DWORD
			),
			(
			'sesi2_idle_time',
			DWORD
			),
			(
			'sesi2_user_flags',
			DWORD
			),
			(
			'sesi2_cltype_name',
			WCHAR_T
			)
		)


class PSESSION_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_2
			)
		)


class LPSESSION_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_2
			)
		)


class SESSION_INFO_2_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSESSION_INFO_2
			)
		)


class PSESSION_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_2_CONTAINER
			)
		)


class LPSESSION_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_2_CONTAINER
			)
		)


class SESSION_INFO_10(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sesi10_cname',
			WCHAR_T
			),
			(
			'sesi10_username',
			WCHAR_T
			),
			(
			'sesi10_time',
			DWORD
			),
			(
			'sesi10_idle_time',
			DWORD
			)
		)


class PSESSION_INFO_10(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_10
			)
		)


class LPSESSION_INFO_10(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_10
			)
		)


class SESSION_INFO_10_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSESSION_INFO_10
			)
		)


class PSESSION_INFO_10_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_10_CONTAINER
			)
		)


class LPSESSION_INFO_10_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_10_CONTAINER
			)
		)


class SESSION_INFO_502(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sesi502_cname',
			WCHAR_T
			),
			(
			'sesi502_username',
			WCHAR_T
			),
			(
			'sesi502_num_opens',
			DWORD
			),
			(
			'sesi502_time',
			DWORD
			),
			(
			'sesi502_idle_time',
			DWORD
			),
			(
			'sesi502_user_flags',
			DWORD
			),
			(
			'sesi502_cltype_name',
			WCHAR_T
			),
			(
			'sesi502_transport',
			WCHAR_T
			)
		)


class PSESSION_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_502
			)
		)


class LPSESSION_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_502
			)
		)


class SESSION_INFO_502_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSESSION_INFO_502
			)
		)


class PSESSION_INFO_502_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_502_CONTAINER
			)
		)


class LPSESSION_INFO_502_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_INFO_502_CONTAINER
			)
		)


class SESSION_ENUM_UNION(NDRUNION):
	union = {0 : (
		'Level0',
		SESSION_INFO_0_CONTAINER
		),1 : (
		'Level1',
		SESSION_INFO_1_CONTAINER
		),2 : (
		'Level2',
		SESSION_INFO_2_CONTAINER
		),10 : (
		'Level10',
		SESSION_INFO_10_CONTAINER
		),502 : (
		'Level502',
		SESSION_INFO_502_CONTAINER
		)}


class SESSION_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'SessionInfo',
			SESSION_ENUM_UNION
			)
		)


class PSESSION_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_ENUM_STRUCT
			)
		)


class LPSESSION_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SESSION_ENUM_STRUCT
			)
		)


class DATA_SHARE_INFO_502_I(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SHARE_INFO_502_I(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SHARE_INFO_502_I
			)
		)


class SHARE_INFO_502_I(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi502_netname',
			WCHAR
			),
			(
			'shi502_type',
			DWORD
			),
			(
			'shi502_remark',
			WCHAR
			),
			(
			'shi502_permissions',
			DWORD
			),
			(
			'shi502_max_uses',
			DWORD
			),
			(
			'shi502_current_uses',
			DWORD
			),
			(
			'shi502_path',
			WCHAR
			),
			(
			'shi502_passwd',
			WCHAR
			),
			(
			'shi502_reserved',
			DWORD
			),
			(
			'shi502_security_descriptor',
			PTR_SHARE_INFO_502_I
			)
		)


class SHARE_INFO_503_I(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi503_netname',
			WCHAR
			),
			(
			'shi503_type',
			DWORD
			),
			(
			'shi503_remark',
			WCHAR
			),
			(
			'shi503_permissions',
			DWORD
			),
			(
			'shi503_max_uses',
			DWORD
			),
			(
			'shi503_current_uses',
			DWORD
			),
			(
			'shi503_path',
			WCHAR
			),
			(
			'shi503_passwd',
			WCHAR
			),
			(
			'shi503_servername',
			WCHAR
			),
			(
			'shi503_reserved',
			DWORD
			),
			(
			'shi503_security_descriptor',
			PUCHAR
			)
		)


class PSHARE_INFO_503_I(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_503_I
			)
		)


class LPSHARE_INFO_503_I(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_503_I
			)
		)


class SHARE_INFO_503_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_503_I
			)
		)


class PSHARE_INFO_503_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_503_CONTAINER
			)
		)


class LPSHARE_INFO_503_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_503_CONTAINER
			)
		)


class DATA_SHARE_INFO_1501_I(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SHARE_INFO_1501_I(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SHARE_INFO_1501_I
			)
		)


class SHARE_INFO_1501_I(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi1501_reserved',
			DWORD
			),
			(
			'shi1501_security_descriptor',
			PTR_SHARE_INFO_1501_I
			)
		)


class SHARE_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi0_netname',
			WCHAR_T
			)
		)


class PSHARE_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_0
			)
		)


class LPSHARE_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_0
			)
		)


class SHARE_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_0
			)
		)


class SHARE_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi1_netname',
			WCHAR_T
			),
			(
			'shi1_type',
			DWORD
			),
			(
			'shi1_remark',
			WCHAR_T
			)
		)


class PSHARE_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1
			)
		)


class LPSHARE_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1
			)
		)


class SHARE_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_1
			)
		)


class SHARE_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi2_netname',
			WCHAR_T
			),
			(
			'shi2_type',
			DWORD
			),
			(
			'shi2_remark',
			WCHAR_T
			),
			(
			'shi2_permissions',
			DWORD
			),
			(
			'shi2_max_uses',
			DWORD
			),
			(
			'shi2_current_uses',
			DWORD
			),
			(
			'shi2_path',
			WCHAR_T
			),
			(
			'shi2_passwd',
			WCHAR_T
			)
		)


class PSHARE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_2
			)
		)


class LPSHARE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_2
			)
		)


class SHARE_INFO_2_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_2
			)
		)


class PSHARE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_2_CONTAINER
			)
		)


class LPSHARE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_2_CONTAINER
			)
		)


class SHARE_INFO_501(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi501_netname',
			WCHAR_T
			),
			(
			'shi501_type',
			DWORD
			),
			(
			'shi501_remark',
			WCHAR_T
			),
			(
			'shi501_flags',
			DWORD
			)
		)


class PSHARE_INFO_501(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_501
			)
		)


class LPSHARE_INFO_501(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_501
			)
		)


class SHARE_INFO_501_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_501
			)
		)


class PSHARE_INFO_501_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_501_CONTAINER
			)
		)


class LPSHARE_INFO_501_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_501_CONTAINER
			)
		)


class SHARE_INFO_502_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSHARE_INFO_502_I
			)
		)


class PSHARE_INFO_502_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_502_CONTAINER
			)
		)


class LPSHARE_INFO_502_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_502_CONTAINER
			)
		)


class SHARE_ENUM_UNION(NDRUNION):
	union = {0 : (
		'Level0',
		SHARE_INFO_0_CONTAINER
		),1 : (
		'Level1',
		SHARE_INFO_1_CONTAINER
		),2 : (
		'Level2',
		SHARE_INFO_2_CONTAINER
		),501 : (
		'Level501',
		SHARE_INFO_501_CONTAINER
		),502 : (
		'Level502',
		SHARE_INFO_502_CONTAINER
		),503 : (
		'Level503',
		SHARE_INFO_503_CONTAINER
		)}


class SHARE_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'ShareInfo',
			SHARE_ENUM_UNION
			)
		)


class PSHARE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_ENUM_STRUCT
			)
		)


class LPSHARE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_ENUM_STRUCT
			)
		)


class SHARE_INFO_1004(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi1004_remark',
			WCHAR_T
			)
		)


class PSHARE_INFO_1004(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1004
			)
		)


class LPSHARE_INFO_1004(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1004
			)
		)


class SHARE_INFO_1006(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi1006_max_uses',
			DWORD
			)
		)


class PSHARE_INFO_1006(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1006
			)
		)


class LPSHARE_INFO_1006(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1006
			)
		)


class SHARE_INFO_1005(NDRSTRUCT):
	align = 1
	structure = (
			(
			'shi1005_flags',
			DWORD
			)
		)


class PSHARE_INFO_1005(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1005
			)
		)


class LPSHARE_INFO_1005(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO_1005
			)
		)


class SHARE_INFO(NDRUNION):
	union = {0 : (
		'ShareInfo0',
		LPSHARE_INFO_0
		),1 : (
		'ShareInfo1',
		LPSHARE_INFO_1
		),2 : (
		'ShareInfo2',
		LPSHARE_INFO_2
		),502 : (
		'ShareInfo502',
		LPSHARE_INFO_502_I
		),1004 : (
		'ShareInfo1004',
		LPSHARE_INFO_1004
		),1006 : (
		'ShareInfo1006',
		LPSHARE_INFO_1006
		),1501 : (
		'ShareInfo1501',
		LPSHARE_INFO_1501_I
		),1005 : (
		'ShareInfo1005',
		LPSHARE_INFO_1005
		),501 : (
		'ShareInfo501',
		LPSHARE_INFO_501
		),503 : (
		'ShareInfo503',
		LPSHARE_INFO_503_I
		)}


class PSHARE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO
			)
		)


class LPSHARE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SHARE_INFO
			)
		)


class SERVER_INFO_102(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv102_platform_id',
			DWORD
			),
			(
			'sv102_name',
			WCHAR_T
			),
			(
			'sv102_version_major',
			DWORD
			),
			(
			'sv102_version_minor',
			DWORD
			),
			(
			'sv102_type',
			DWORD
			),
			(
			'sv102_comment',
			WCHAR_T
			),
			(
			'sv102_users',
			DWORD
			),
			(
			'sv102_disc',
			LONG
			),
			(
			'sv102_hidden',
			INT
			),
			(
			'sv102_announce',
			DWORD
			),
			(
			'sv102_anndelta',
			DWORD
			),
			(
			'sv102_licenses',
			DWORD
			),
			(
			'sv102_userpath',
			WCHAR_T
			)
		)


class PSERVER_INFO_102(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_102
			)
		)


class LPSERVER_INFO_102(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_102
			)
		)


class SERVER_INFO_103(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv103_platform_id',
			DWORD
			),
			(
			'sv103_name',
			WCHAR_T
			),
			(
			'sv103_version_major',
			DWORD
			),
			(
			'sv103_version_minor',
			DWORD
			),
			(
			'sv103_type',
			DWORD
			),
			(
			'sv103_comment',
			WCHAR_T
			),
			(
			'sv103_users',
			DWORD
			),
			(
			'sv103_disc',
			LONG
			),
			(
			'sv103_hidden',
			BOOL
			),
			(
			'sv103_announce',
			DWORD
			),
			(
			'sv103_anndelta',
			DWORD
			),
			(
			'sv103_licenses',
			DWORD
			),
			(
			'sv103_userpath',
			WCHAR_T
			),
			(
			'sv103_capabilities',
			DWORD
			)
		)


class PSERVER_INFO_103(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_103
			)
		)


class LPSERVER_INFO_103(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_103
			)
		)


class SERVER_INFO_502(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv502_sessopens',
			DWORD
			),
			(
			'sv502_sessvcs',
			DWORD
			),
			(
			'sv502_opensearch',
			DWORD
			),
			(
			'sv502_sizreqbuf',
			DWORD
			),
			(
			'sv502_initworkitems',
			DWORD
			),
			(
			'sv502_maxworkitems',
			DWORD
			),
			(
			'sv502_rawworkitems',
			DWORD
			),
			(
			'sv502_irpstacksize',
			DWORD
			),
			(
			'sv502_maxrawbuflen',
			DWORD
			),
			(
			'sv502_sessusers',
			DWORD
			),
			(
			'sv502_sessconns',
			DWORD
			),
			(
			'sv502_maxpagedmemoryusage',
			DWORD
			),
			(
			'sv502_maxnonpagedmemoryusage',
			DWORD
			),
			(
			'sv502_enablesoftcompat',
			INT
			),
			(
			'sv502_enableforcedlogoff',
			INT
			),
			(
			'sv502_timesource',
			INT
			),
			(
			'sv502_acceptdownlevelapis',
			INT
			),
			(
			'sv502_lmannounce',
			INT
			)
		)


class PSERVER_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_502
			)
		)


class LPSERVER_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_502
			)
		)


class SERVER_INFO_503(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv503_sessopens',
			DWORD
			),
			(
			'sv503_sessvcs',
			DWORD
			),
			(
			'sv503_opensearch',
			DWORD
			),
			(
			'sv503_sizreqbuf',
			DWORD
			),
			(
			'sv503_initworkitems',
			DWORD
			),
			(
			'sv503_maxworkitems',
			DWORD
			),
			(
			'sv503_rawworkitems',
			DWORD
			),
			(
			'sv503_irpstacksize',
			DWORD
			),
			(
			'sv503_maxrawbuflen',
			DWORD
			),
			(
			'sv503_sessusers',
			DWORD
			),
			(
			'sv503_sessconns',
			DWORD
			),
			(
			'sv503_maxpagedmemoryusage',
			DWORD
			),
			(
			'sv503_maxnonpagedmemoryusage',
			DWORD
			),
			(
			'sv503_enablesoftcompat',
			INT
			),
			(
			'sv503_enableforcedlogoff',
			INT
			),
			(
			'sv503_timesource',
			INT
			),
			(
			'sv503_acceptdownlevelapis',
			INT
			),
			(
			'sv503_lmannounce',
			INT
			),
			(
			'sv503_domain',
			WCHAR_T
			),
			(
			'sv503_maxcopyreadlen',
			DWORD
			),
			(
			'sv503_maxcopywritelen',
			DWORD
			),
			(
			'sv503_minkeepsearch',
			DWORD
			),
			(
			'sv503_maxkeepsearch',
			DWORD
			),
			(
			'sv503_minkeepcomplsearch',
			DWORD
			),
			(
			'sv503_maxkeepcomplsearch',
			DWORD
			),
			(
			'sv503_threadcountadd',
			DWORD
			),
			(
			'sv503_numblockthreads',
			DWORD
			),
			(
			'sv503_scavtimeout',
			DWORD
			),
			(
			'sv503_minrcvqueue',
			DWORD
			),
			(
			'sv503_minfreeworkitems',
			DWORD
			),
			(
			'sv503_xactmemsize',
			DWORD
			),
			(
			'sv503_threadpriority',
			DWORD
			),
			(
			'sv503_maxmpxct',
			DWORD
			),
			(
			'sv503_oplockbreakwait',
			DWORD
			),
			(
			'sv503_oplockbreakresponsewait',
			DWORD
			),
			(
			'sv503_enableoplocks',
			INT
			),
			(
			'sv503_enableoplockforceclose',
			INT
			),
			(
			'sv503_enablefcbopens',
			INT
			),
			(
			'sv503_enableraw',
			INT
			),
			(
			'sv503_enablesharednetdrives',
			INT
			),
			(
			'sv503_minfreeconnections',
			DWORD
			),
			(
			'sv503_maxfreeconnections',
			DWORD
			)
		)


class PSERVER_INFO_503(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_503
			)
		)


class LPSERVER_INFO_503(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_503
			)
		)


class SERVER_INFO_599(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv599_sessopens',
			DWORD
			),
			(
			'sv599_sessvcs',
			DWORD
			),
			(
			'sv599_opensearch',
			DWORD
			),
			(
			'sv599_sizreqbuf',
			DWORD
			),
			(
			'sv599_initworkitems',
			DWORD
			),
			(
			'sv599_maxworkitems',
			DWORD
			),
			(
			'sv599_rawworkitems',
			DWORD
			),
			(
			'sv599_irpstacksize',
			DWORD
			),
			(
			'sv599_maxrawbuflen',
			DWORD
			),
			(
			'sv599_sessusers',
			DWORD
			),
			(
			'sv599_sessconns',
			DWORD
			),
			(
			'sv599_maxpagedmemoryusage',
			DWORD
			),
			(
			'sv599_maxnonpagedmemoryusage',
			DWORD
			),
			(
			'sv599_enablesoftcompat',
			INT
			),
			(
			'sv599_enableforcedlogoff',
			INT
			),
			(
			'sv599_timesource',
			INT
			),
			(
			'sv599_acceptdownlevelapis',
			INT
			),
			(
			'sv599_lmannounce',
			INT
			),
			(
			'sv599_domain',
			WCHAR_T
			),
			(
			'sv599_maxcopyreadlen',
			DWORD
			),
			(
			'sv599_maxcopywritelen',
			DWORD
			),
			(
			'sv599_minkeepsearch',
			DWORD
			),
			(
			'sv599_maxkeepsearch',
			DWORD
			),
			(
			'sv599_minkeepcomplsearch',
			DWORD
			),
			(
			'sv599_maxkeepcomplsearch',
			DWORD
			),
			(
			'sv599_threadcountadd',
			DWORD
			),
			(
			'sv599_numblockthreads',
			DWORD
			),
			(
			'sv599_scavtimeout',
			DWORD
			),
			(
			'sv599_minrcvqueue',
			DWORD
			),
			(
			'sv599_minfreeworkitems',
			DWORD
			),
			(
			'sv599_xactmemsize',
			DWORD
			),
			(
			'sv599_threadpriority',
			DWORD
			),
			(
			'sv599_maxmpxct',
			DWORD
			),
			(
			'sv599_oplockbreakwait',
			DWORD
			),
			(
			'sv599_oplockbreakresponsewait',
			DWORD
			),
			(
			'sv599_enableoplocks',
			INT
			),
			(
			'sv599_enableoplockforceclose',
			INT
			),
			(
			'sv599_enablefcbopens',
			INT
			),
			(
			'sv599_enableraw',
			INT
			),
			(
			'sv599_enablesharednetdrives',
			INT
			),
			(
			'sv599_minfreeconnections',
			DWORD
			),
			(
			'sv599_maxfreeconnections',
			DWORD
			),
			(
			'sv599_initsesstable',
			DWORD
			),
			(
			'sv599_initconntable',
			DWORD
			),
			(
			'sv599_initfiletable',
			DWORD
			),
			(
			'sv599_initsearchtable',
			DWORD
			),
			(
			'sv599_alertschedule',
			DWORD
			),
			(
			'sv599_errorthreshold',
			DWORD
			),
			(
			'sv599_networkerrorthreshold',
			DWORD
			),
			(
			'sv599_diskspacethreshold',
			DWORD
			),
			(
			'sv599_reserved',
			DWORD
			),
			(
			'sv599_maxlinkdelay',
			DWORD
			),
			(
			'sv599_minlinkthroughput',
			DWORD
			),
			(
			'sv599_linkinfovalidtime',
			DWORD
			),
			(
			'sv599_scavqosinfoupdatetime',
			DWORD
			),
			(
			'sv599_maxworkitemidletime',
			DWORD
			)
		)


class PSERVER_INFO_599(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_599
			)
		)


class LPSERVER_INFO_599(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_599
			)
		)


class SERVER_INFO_1005(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1005_comment',
			WCHAR_T
			)
		)


class PSERVER_INFO_1005(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1005
			)
		)


class LPSERVER_INFO_1005(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1005
			)
		)


class SERVER_INFO_1107(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1107_users',
			DWORD
			)
		)


class PSERVER_INFO_1107(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1107
			)
		)


class LPSERVER_INFO_1107(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1107
			)
		)


class SERVER_INFO_1010(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1010_disc',
			LONG
			)
		)


class PSERVER_INFO_1010(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1010
			)
		)


class LPSERVER_INFO_1010(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1010
			)
		)


class SERVER_INFO_1016(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1016_hidden',
			INT
			)
		)


class PSERVER_INFO_1016(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1016
			)
		)


class LPSERVER_INFO_1016(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1016
			)
		)


class SERVER_INFO_1017(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1017_announce',
			DWORD
			)
		)


class PSERVER_INFO_1017(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1017
			)
		)


class LPSERVER_INFO_1017(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1017
			)
		)


class SERVER_INFO_1018(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1018_anndelta',
			DWORD
			)
		)


class PSERVER_INFO_1018(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1018
			)
		)


class LPSERVER_INFO_1018(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1018
			)
		)


class SERVER_INFO_1501(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1501_sessopens',
			DWORD
			)
		)


class PSERVER_INFO_1501(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1501
			)
		)


class LPSERVER_INFO_1501(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1501
			)
		)


class SERVER_INFO_1502(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1502_sessvcs',
			DWORD
			)
		)


class PSERVER_INFO_1502(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1502
			)
		)


class LPSERVER_INFO_1502(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1502
			)
		)


class SERVER_INFO_1503(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1503_opensearch',
			DWORD
			)
		)


class PSERVER_INFO_1503(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1503
			)
		)


class LPSERVER_INFO_1503(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1503
			)
		)


class SERVER_INFO_1506(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1506_maxworkitems',
			DWORD
			)
		)


class PSERVER_INFO_1506(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1506
			)
		)


class LPSERVER_INFO_1506(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1506
			)
		)


class SERVER_INFO_1510(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1510_sessusers',
			DWORD
			)
		)


class PSERVER_INFO_1510(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1510
			)
		)


class LPSERVER_INFO_1510(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1510
			)
		)


class SERVER_INFO_1511(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1511_sessconns',
			DWORD
			)
		)


class PSERVER_INFO_1511(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1511
			)
		)


class LPSERVER_INFO_1511(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1511
			)
		)


class SERVER_INFO_1512(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1512_maxnonpagedmemoryusage',
			DWORD
			)
		)


class PSERVER_INFO_1512(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1512
			)
		)


class LPSERVER_INFO_1512(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1512
			)
		)


class SERVER_INFO_1513(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1513_maxpagedmemoryusage',
			DWORD
			)
		)


class PSERVER_INFO_1513(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1513
			)
		)


class LPSERVER_INFO_1513(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1513
			)
		)


class SERVER_INFO_1514(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1514_enablesoftcompat',
			INT
			)
		)


class PSERVER_INFO_1514(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1514
			)
		)


class LPSERVER_INFO_1514(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1514
			)
		)


class SERVER_INFO_1515(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1515_enableforcedlogoff',
			INT
			)
		)


class PSERVER_INFO_1515(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1515
			)
		)


class LPSERVER_INFO_1515(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1515
			)
		)


class SERVER_INFO_1516(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1516_timesource',
			INT
			)
		)


class PSERVER_INFO_1516(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1516
			)
		)


class LPSERVER_INFO_1516(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1516
			)
		)


class SERVER_INFO_1518(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1518_lmannounce',
			INT
			)
		)


class PSERVER_INFO_1518(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1518
			)
		)


class LPSERVER_INFO_1518(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1518
			)
		)


class SERVER_INFO_1523(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1523_maxkeepsearch',
			DWORD
			)
		)


class PSERVER_INFO_1523(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1523
			)
		)


class LPSERVER_INFO_1523(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1523
			)
		)


class SERVER_INFO_1528(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1528_scavtimeout',
			DWORD
			)
		)


class PSERVER_INFO_1528(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1528
			)
		)


class LPSERVER_INFO_1528(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1528
			)
		)


class SERVER_INFO_1529(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1529_minrcvqueue',
			DWORD
			)
		)


class PSERVER_INFO_1529(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1529
			)
		)


class LPSERVER_INFO_1529(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1529
			)
		)


class SERVER_INFO_1530(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1530_minfreeworkitems',
			DWORD
			)
		)


class PSERVER_INFO_1530(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1530
			)
		)


class LPSERVER_INFO_1530(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1530
			)
		)


class SERVER_INFO_1533(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1533_maxmpxct',
			DWORD
			)
		)


class PSERVER_INFO_1533(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1533
			)
		)


class LPSERVER_INFO_1533(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1533
			)
		)


class SERVER_INFO_1534(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1534_oplockbreakwait',
			DWORD
			)
		)


class PSERVER_INFO_1534(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1534
			)
		)


class LPSERVER_INFO_1534(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1534
			)
		)


class SERVER_INFO_1535(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1535_oplockbreakresponsewait',
			DWORD
			)
		)


class PSERVER_INFO_1535(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1535
			)
		)


class LPSERVER_INFO_1535(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1535
			)
		)


class SERVER_INFO_1536(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1536_enableoplocks',
			INT
			)
		)


class PSERVER_INFO_1536(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1536
			)
		)


class LPSERVER_INFO_1536(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1536
			)
		)


class SERVER_INFO_1538(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1538_enablefcbopens',
			INT
			)
		)


class PSERVER_INFO_1538(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1538
			)
		)


class LPSERVER_INFO_1538(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1538
			)
		)


class SERVER_INFO_1539(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1539_enableraw',
			INT
			)
		)


class PSERVER_INFO_1539(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1539
			)
		)


class LPSERVER_INFO_1539(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1539
			)
		)


class SERVER_INFO_1540(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1540_enablesharednetdrives',
			INT
			)
		)


class PSERVER_INFO_1540(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1540
			)
		)


class LPSERVER_INFO_1540(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1540
			)
		)


class SERVER_INFO_1541(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1541_minfreeconnections',
			INT
			)
		)


class PSERVER_INFO_1541(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1541
			)
		)


class LPSERVER_INFO_1541(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1541
			)
		)


class SERVER_INFO_1542(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1542_maxfreeconnections',
			INT
			)
		)


class PSERVER_INFO_1542(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1542
			)
		)


class LPSERVER_INFO_1542(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1542
			)
		)


class SERVER_INFO_1543(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1543_initsesstable',
			DWORD
			)
		)


class PSERVER_INFO_1543(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1543
			)
		)


class LPSERVER_INFO_1543(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1543
			)
		)


class SERVER_INFO_1544(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1544_initconntable',
			DWORD
			)
		)


class PSERVER_INFO_1544(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1544
			)
		)


class LPSERVER_INFO_1544(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1544
			)
		)


class SERVER_INFO_1545(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1545_initfiletable',
			DWORD
			)
		)


class PSERVER_INFO_1545(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1545
			)
		)


class LPSERVER_INFO_1545(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1545
			)
		)


class SERVER_INFO_1546(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1546_initsearchtable',
			DWORD
			)
		)


class PSERVER_INFO_1546(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1546
			)
		)


class LPSERVER_INFO_1546(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1546
			)
		)


class SERVER_INFO_1547(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1547_alertschedule',
			DWORD
			)
		)


class PSERVER_INFO_1547(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1547
			)
		)


class LPSERVER_INFO_1547(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1547
			)
		)


class SERVER_INFO_1548(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1548_errorthreshold',
			DWORD
			)
		)


class PSERVER_INFO_1548(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1548
			)
		)


class LPSERVER_INFO_1548(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1548
			)
		)


class SERVER_INFO_1549(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1549_networkerrorthreshold',
			DWORD
			)
		)


class PSERVER_INFO_1549(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1549
			)
		)


class LPSERVER_INFO_1549(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1549
			)
		)


class SERVER_INFO_1550(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1550_diskspacethreshold',
			DWORD
			)
		)


class PSERVER_INFO_1550(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1550
			)
		)


class LPSERVER_INFO_1550(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1550
			)
		)


class SERVER_INFO_1552(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1552_maxlinkdelay',
			DWORD
			)
		)


class PSERVER_INFO_1552(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1552
			)
		)


class LPSERVER_INFO_1552(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1552
			)
		)


class SERVER_INFO_1553(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1553_minlinkthroughput',
			DWORD
			)
		)


class PSERVER_INFO_1553(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1553
			)
		)


class LPSERVER_INFO_1553(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1553
			)
		)


class SERVER_INFO_1554(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1554_linkinfovalidtime',
			DWORD
			)
		)


class PSERVER_INFO_1554(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1554
			)
		)


class LPSERVER_INFO_1554(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1554
			)
		)


class SERVER_INFO_1555(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1555_scavqosinfoupdatetime',
			DWORD
			)
		)


class PSERVER_INFO_1555(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1555
			)
		)


class LPSERVER_INFO_1555(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1555
			)
		)


class SERVER_INFO_1556(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv1556_maxworkitemidletime',
			DWORD
			)
		)


class PSERVER_INFO_1556(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1556
			)
		)


class LPSERVER_INFO_1556(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_1556
			)
		)


class SERVER_INFO(NDRUNION):
	union = {100 : (
		'ServerInfo100',
		LPSERVER_INFO_100
		),101 : (
		'ServerInfo101',
		LPSERVER_INFO_101
		),102 : (
		'ServerInfo102',
		LPSERVER_INFO_102
		),103 : (
		'ServerInfo103',
		LPSERVER_INFO_103
		),502 : (
		'ServerInfo502',
		LPSERVER_INFO_502
		),503 : (
		'ServerInfo503',
		LPSERVER_INFO_503
		),599 : (
		'ServerInfo599',
		LPSERVER_INFO_599
		),1005 : (
		'ServerInfo1005',
		LPSERVER_INFO_1005
		),1107 : (
		'ServerInfo1107',
		LPSERVER_INFO_1107
		),1010 : (
		'ServerInfo1010',
		LPSERVER_INFO_1010
		),1016 : (
		'ServerInfo1016',
		LPSERVER_INFO_1016
		),1017 : (
		'ServerInfo1017',
		LPSERVER_INFO_1017
		),1018 : (
		'ServerInfo1018',
		LPSERVER_INFO_1018
		),1501 : (
		'ServerInfo1501',
		LPSERVER_INFO_1501
		),1502 : (
		'ServerInfo1502',
		LPSERVER_INFO_1502
		),1503 : (
		'ServerInfo1503',
		LPSERVER_INFO_1503
		),1506 : (
		'ServerInfo1506',
		LPSERVER_INFO_1506
		),1510 : (
		'ServerInfo1510',
		LPSERVER_INFO_1510
		),1511 : (
		'ServerInfo1511',
		LPSERVER_INFO_1511
		),1512 : (
		'ServerInfo1512',
		LPSERVER_INFO_1512
		),1513 : (
		'ServerInfo1513',
		LPSERVER_INFO_1513
		),1514 : (
		'ServerInfo1514',
		LPSERVER_INFO_1514
		),1515 : (
		'ServerInfo1515',
		LPSERVER_INFO_1515
		),1516 : (
		'ServerInfo1516',
		LPSERVER_INFO_1516
		),1518 : (
		'ServerInfo1518',
		LPSERVER_INFO_1518
		),1523 : (
		'ServerInfo1523',
		LPSERVER_INFO_1523
		),1528 : (
		'ServerInfo1528',
		LPSERVER_INFO_1528
		),1529 : (
		'ServerInfo1529',
		LPSERVER_INFO_1529
		),1530 : (
		'ServerInfo1530',
		LPSERVER_INFO_1530
		),1533 : (
		'ServerInfo1533',
		LPSERVER_INFO_1533
		),1534 : (
		'ServerInfo1534',
		LPSERVER_INFO_1534
		),1535 : (
		'ServerInfo1535',
		LPSERVER_INFO_1535
		),1536 : (
		'ServerInfo1536',
		LPSERVER_INFO_1536
		),1538 : (
		'ServerInfo1538',
		LPSERVER_INFO_1538
		),1539 : (
		'ServerInfo1539',
		LPSERVER_INFO_1539
		),1540 : (
		'ServerInfo1540',
		LPSERVER_INFO_1540
		),1541 : (
		'ServerInfo1541',
		LPSERVER_INFO_1541
		),1542 : (
		'ServerInfo1542',
		LPSERVER_INFO_1542
		),1543 : (
		'ServerInfo1543',
		LPSERVER_INFO_1543
		),1544 : (
		'ServerInfo1544',
		LPSERVER_INFO_1544
		),1545 : (
		'ServerInfo1545',
		LPSERVER_INFO_1545
		),1546 : (
		'ServerInfo1546',
		LPSERVER_INFO_1546
		),1547 : (
		'ServerInfo1547',
		LPSERVER_INFO_1547
		),1548 : (
		'ServerInfo1548',
		LPSERVER_INFO_1548
		),1549 : (
		'ServerInfo1549',
		LPSERVER_INFO_1549
		),1550 : (
		'ServerInfo1550',
		LPSERVER_INFO_1550
		),1552 : (
		'ServerInfo1552',
		LPSERVER_INFO_1552
		),1553 : (
		'ServerInfo1553',
		LPSERVER_INFO_1553
		),1554 : (
		'ServerInfo1554',
		LPSERVER_INFO_1554
		),1555 : (
		'ServerInfo1555',
		LPSERVER_INFO_1555
		),1556 : (
		'ServerInfo1556',
		LPSERVER_INFO_1556
		)}


class PSERVER_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO
			)
		)


class LPSERVER_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO
			)
		)


class DISK_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Disk',
			WCHAR
			)
		)


class PDISK_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DISK_INFO
			)
		)


class LPDISK_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DISK_INFO
			)
		)


class DISK_ENUM_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPDISK_INFO
			)
		)


class DATA_SERVER_TRANSPORT_INFO_0(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SERVER_TRANSPORT_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SERVER_TRANSPORT_INFO_0
			)
		)


class SERVER_TRANSPORT_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'svti0_numberofvcs',
			DWORD
			),
			(
			'svti0_transportname',
			WCHAR_T
			),
			(
			'svti0_transportaddress',
			PTR_SERVER_TRANSPORT_INFO_0
			),
			(
			'svti0_transportaddresslength',
			DWORD
			),
			(
			'svti0_networkaddress',
			WCHAR_T
			)
		)


class SERVER_XPORT_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_0
			)
		)


class PSERVER_XPORT_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_INFO_0_CONTAINER
			)
		)


class DATA_SERVER_TRANSPORT_INFO_1(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SERVER_TRANSPORT_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SERVER_TRANSPORT_INFO_1
			)
		)


class SERVER_TRANSPORT_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'svti1_numberofvcs',
			DWORD
			),
			(
			'svti1_transportname',
			WCHAR_T
			),
			(
			'svti1_transportaddress',
			PTR_SERVER_TRANSPORT_INFO_1
			),
			(
			'svti1_transportaddresslength',
			DWORD
			),
			(
			'svti1_networkaddress',
			WCHAR_T
			),
			(
			'svti1_domain',
			WCHAR_T
			)
		)


class SERVER_XPORT_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_1
			)
		)


class PSERVER_XPORT_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_INFO_1_CONTAINER
			)
		)


class DATA_SERVER_TRANSPORT_INFO_2(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SERVER_TRANSPORT_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SERVER_TRANSPORT_INFO_2
			)
		)


class SERVER_TRANSPORT_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'svti2_numberofvcs',
			DWORD
			),
			(
			'svti2_transportname',
			WCHAR_T
			),
			(
			'svti2_transportaddress',
			PTR_SERVER_TRANSPORT_INFO_2
			),
			(
			'svti2_transportaddresslength',
			DWORD
			),
			(
			'svti2_networkaddress',
			WCHAR_T
			),
			(
			'svti2_domain',
			WCHAR_T
			),
			(
			'svti2_flags',
			UNSIGNED_LONG
			)
		)


class SERVER_XPORT_INFO_2_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_2
			)
		)


class PSERVER_XPORT_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_INFO_2_CONTAINER
			)
		)


class DATA_SERVER_TRANSPORT_INFO_3(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_SERVER_TRANSPORT_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SERVER_TRANSPORT_INFO_3
			)
		)


class SERVER_TRANSPORT_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'svti3_numberofvcs',
			DWORD
			),
			(
			'svti3_transportname',
			WCHAR_T
			),
			(
			'svti3_transportaddress',
			PTR_SERVER_TRANSPORT_INFO_3
			),
			(
			'svti3_transportaddresslength',
			DWORD
			),
			(
			'svti3_networkaddress',
			WCHAR_T
			),
			(
			'svti3_domain',
			WCHAR_T
			),
			(
			'svti3_flags',
			UNSIGNED_LONG
			),
			(
			'svti3_passwordlength',
			DWORD
			),
			(
			'svti3_password',
			UNSIGNED_CHAR
			)
		)


class SERVER_XPORT_INFO_3_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_3
			)
		)


class PSERVER_XPORT_INFO_3_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_INFO_3_CONTAINER
			)
		)


class TRANSPORT_INFO(NDRUNION):
	union = {0 : (
		'Transport0',
		SERVER_TRANSPORT_INFO_0
		),1 : (
		'Transport1',
		SERVER_TRANSPORT_INFO_1
		),2 : (
		'Transport2',
		SERVER_TRANSPORT_INFO_2
		),3 : (
		'Transport3',
		SERVER_TRANSPORT_INFO_3
		)}


class PTRANSPORT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			TRANSPORT_INFO
			)
		)


class LPTRANSPORT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			TRANSPORT_INFO
			)
		)


class SERVER_XPORT_ENUM_UNION(NDRUNION):
	union = {0 : (
		'Level0',
		PSERVER_XPORT_INFO_0_CONTAINER
		),1 : (
		'Level1',
		PSERVER_XPORT_INFO_1_CONTAINER
		),2 : (
		'Level2',
		PSERVER_XPORT_INFO_2_CONTAINER
		),3 : (
		'Level3',
		PSERVER_XPORT_INFO_3_CONTAINER
		)}


class SERVER_XPORT_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'XportInfo',
			SERVER_XPORT_ENUM_UNION
			)
		)


class PSERVER_XPORT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_ENUM_STRUCT
			)
		)


class LPSERVER_XPORT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_XPORT_ENUM_STRUCT
			)
		)


SHARE_DEL_HANDLE = VOID
PSHARE_DEL_HANDLE = SHARE_DEL_HANDLE
class DATA_ADT_SECURITY_DESCRIPTOR(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_ADT_SECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_ADT_SECURITY_DESCRIPTOR
			)
		)


class ADT_SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			DWORD
			),
			(
			'Buffer',
			PTR_ADT_SECURITY_DESCRIPTOR
			)
		)


class STAT_SERVER_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sts0_start',
			DWORD
			),
			(
			'sts0_fopens',
			DWORD
			),
			(
			'sts0_devopens',
			DWORD
			),
			(
			'sts0_jobsqueued',
			DWORD
			),
			(
			'sts0_sopens',
			DWORD
			),
			(
			'sts0_stimedout',
			DWORD
			),
			(
			'sts0_serrorout',
			DWORD
			),
			(
			'sts0_pwerrors',
			DWORD
			),
			(
			'sts0_permerrors',
			DWORD
			),
			(
			'sts0_syserrors',
			DWORD
			),
			(
			'sts0_bytessent_low',
			DWORD
			),
			(
			'sts0_bytessent_high',
			DWORD
			),
			(
			'sts0_bytesrcvd_low',
			DWORD
			),
			(
			'sts0_bytesrcvd_high',
			DWORD
			),
			(
			'sts0_avresponse',
			DWORD
			),
			(
			'sts0_reqbufneed',
			DWORD
			),
			(
			'sts0_bigbufneed',
			DWORD
			)
		)


class PSTAT_SERVER_0(NDRPOINTER):
	referent = (
			(
			'Data',
			STAT_SERVER_0
			)
		)


class LPSTAT_SERVER_0(NDRPOINTER):
	referent = (
			(
			'Data',
			STAT_SERVER_0
			)
		)


class TIME_OF_DAY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tod_elapsedt',
			DWORD
			),
			(
			'tod_msecs',
			DWORD
			),
			(
			'tod_hours',
			DWORD
			),
			(
			'tod_mins',
			DWORD
			),
			(
			'tod_secs',
			DWORD
			),
			(
			'tod_hunds',
			DWORD
			),
			(
			'tod_timezone',
			LONG
			),
			(
			'tod_tinterval',
			DWORD
			),
			(
			'tod_day',
			DWORD
			),
			(
			'tod_month',
			DWORD
			),
			(
			'tod_year',
			DWORD
			),
			(
			'tod_weekday',
			DWORD
			)
		)


class PTIME_OF_DAY_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			TIME_OF_DAY_INFO
			)
		)


class LPTIME_OF_DAY_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			TIME_OF_DAY_INFO
			)
		)


class NET_DFS_ENTRY_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			)
		)


class LPNET_DFS_ENTRY_ID(NDRPOINTER):
	referent = (
			(
			'Data',
			NET_DFS_ENTRY_ID
			)
		)


class NET_DFS_ENTRY_ID_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Count',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPNET_DFS_ENTRY_ID
			)
		)


class LPNET_DFS_ENTRY_ID_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			NET_DFS_ENTRY_ID_CONTAINER
			)
		)


class DFS_SITENAME_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SiteFlags',
			UNSIGNED_LONG
			),
			(
			'SiteName',
			WCHAR
			)
		)


class PDFS_SITENAME_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DFS_SITENAME_INFO
			)
		)


class LPDFS_SITENAME_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DFS_SITENAME_INFO
			)
		)


class DFS_SITELIST_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cSites',
			UNSIGNED_LONG
			),
			(
			'Site',
			DFS_SITENAME_INFO
			)
		)


class PDFS_SITELIST_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DFS_SITELIST_INFO
			)
		)


class LPDFS_SITELIST_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DFS_SITELIST_INFO
			)
		)


class SERVER_ALIAS_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'srvai0_alias',
			LMSTR
			),
			(
			'srvai0_target',
			LMSTR
			),
			(
			'srvai0_default',
			BOOLEAN
			),
			(
			'srvai0_reserved',
			ULONG
			)
		)


class PSERVER_ALIAS_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_INFO_0
			)
		)


class LPSERVER_ALIAS_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_INFO_0
			)
		)


class SERVER_ALIAS_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_ALIAS_INFO_0
			)
		)


class SERVERALIASINFO(NDRUNION):
	union = {0 : (
		'Level0',
		SERVER_ALIAS_INFO_0_CONTAINER
		)}


class SERVER_ALIAS_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'ServerAliasInfo',
			SERVERALIASINFO
			)
		)


class PSERVER_ALIAS_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_ENUM_STRUCT
			)
		)


class LPSERVER_ALIAS_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_ENUM_STRUCT
			)
		)


class SERVER_ALIAS_INFO(NDRUNION):
	union = {0 : (
		'ServerAliasInfo0',
		LPSERVER_ALIAS_INFO_0
		)}


class PSERVER_ALIAS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_INFO
			)
		)


class LPSERVER_ALIAS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_ALIAS_INFO
			)
		)


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


class Opnum3NotUsedOnWire(NDRCALL):
	OPNUM = 3
	structure = (

		)


class Opnum3NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum4NotUsedOnWire(NDRCALL):
	OPNUM = 4
	structure = (

		)


class Opnum4NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum5NotUsedOnWire(NDRCALL):
	OPNUM = 5
	structure = (

		)


class Opnum5NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum6NotUsedOnWire(NDRCALL):
	OPNUM = 6
	structure = (

		)


class Opnum6NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum7NotUsedOnWire(NDRCALL):
	OPNUM = 7
	structure = (

		)


class Opnum7NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrConnectionEnum(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Qualifier',
			WCHAR
			),
			(
			'InfoStruct',
			LPCONNECT_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrConnectionEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Qualifier',
			WCHAR
			),
			(
			'InfoStruct',
			LPCONNECT_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrFileEnum(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'BasePath',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			),
			(
			'InfoStruct',
			PFILE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrFileEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'BasePath',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			),
			(
			'InfoStruct',
			PFILE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrFileGetInfo(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'FileId',
			DWORD
			),
			(
			'Level',
			DWORD
			)
		)


class NetrFileGetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'FileId',
			DWORD
			),
			(
			'Level',
			DWORD
			)
		)


class NetrFileClose(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'FileId',
			DWORD
			)
		)


class NetrFileCloseResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'FileId',
			DWORD
			)
		)


class NetrSessionEnum(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ClientName',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			),
			(
			'InfoStruct',
			PSESSION_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrSessionEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ClientName',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			),
			(
			'InfoStruct',
			PSESSION_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrSessionDel(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ClientName',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			)
		)


class NetrSessionDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ClientName',
			WCHAR
			),
			(
			'UserName',
			WCHAR
			)
		)


class NetrShareAdd(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSHARE_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrShareAddResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSHARE_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrShareEnum(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSHARE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrShareEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSHARE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrShareGetInfo(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Level',
			DWORD
			)
		)


class NetrShareGetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Level',
			DWORD
			)
		)


class NetrShareSetInfo(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Level',
			DWORD
			),
			(
			'ShareInfo',
			LPSHARE_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrShareSetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Level',
			DWORD
			),
			(
			'ShareInfo',
			LPSHARE_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrShareDel(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareDelSticky(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareDelStickyResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareCheck(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Device',
			WCHAR
			)
		)


class NetrShareCheckResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Device',
			WCHAR
			)
		)


class NetrServerGetInfo(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			)
		)


class NetrServerGetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			)
		)


class NetrServerSetInfo(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'ServerInfo',
			LPSERVER_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrServerSetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'ServerInfo',
			LPSERVER_INFO
			),
			(
			'ParmErr',
			DWORD
			)
		)


class NetrServerDiskEnum(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'DiskInfoStruct',
			DISK_ENUM_CONTAINER
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrServerDiskEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'DiskInfoStruct',
			DISK_ENUM_CONTAINER
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrServerStatisticsGet(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Service',
			WCHAR
			),
			(
			'Level',
			DWORD
			),
			(
			'Options',
			DWORD
			)
		)


class NetrServerStatisticsGetResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Service',
			WCHAR
			),
			(
			'Level',
			DWORD
			),
			(
			'Options',
			DWORD
			)
		)


class NetrServerTransportAdd(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_0
			)
		)


class NetrServerTransportAddResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_0
			)
		)


class NetrServerTransportEnum(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSERVER_XPORT_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrServerTransportEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSERVER_XPORT_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrServerTransportDel(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_0
			)
		)


class NetrServerTransportDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPSERVER_TRANSPORT_INFO_0
			)
		)


class NetrRemoteTOD(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			)
		)


class NetrRemoteTODResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			)
		)


class Opnum29NotUsedOnWire(NDRCALL):
	OPNUM = 29
	structure = (

		)


class Opnum29NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetprPathType(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName',
			WCHAR
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprPathTypeResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName',
			WCHAR
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprPathCanonicalize(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName',
			WCHAR
			),
			(
			'OutbufLen',
			DWORD
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'PathType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprPathCanonicalizeResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName',
			WCHAR
			),
			(
			'OutbufLen',
			DWORD
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'PathType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprPathCompare(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName1',
			WCHAR
			),
			(
			'PathName2',
			WCHAR
			),
			(
			'PathType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprPathCompareResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'PathName1',
			WCHAR
			),
			(
			'PathName2',
			WCHAR
			),
			(
			'PathType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameValidate(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name',
			WCHAR
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameValidateResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name',
			WCHAR
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameCanonicalize(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name',
			WCHAR
			),
			(
			'OutbufLen',
			DWORD
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameCanonicalizeResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name',
			WCHAR
			),
			(
			'OutbufLen',
			DWORD
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameCompare(NDRCALL):
	OPNUM = 35
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name1',
			WCHAR
			),
			(
			'Name2',
			WCHAR
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetprNameCompareResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Name1',
			WCHAR
			),
			(
			'Name2',
			WCHAR
			),
			(
			'NameType',
			DWORD
			),
			(
			'Flags',
			DWORD
			)
		)


class NetrShareEnumSticky(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSHARE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrShareEnumStickyResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSHARE_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			DWORD
			)
		)


class NetrShareDelStart(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareDelStartResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'NetName',
			WCHAR
			),
			(
			'Reserved',
			DWORD
			)
		)


class NetrShareDelCommit(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'ContextHandle',
			PSHARE_DEL_HANDLE
			)
		)


class NetrShareDelCommitResponse(NDRCALL):
	structure = (
			(
			'ContextHandle',
			PSHARE_DEL_HANDLE
			)
		)


class NetrpGetFileSecurity(NDRCALL):
	OPNUM = 39
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'lpFileName',
			WCHAR
			),
			(
			'RequestedInformation',
			SECURITY_INFORMATION
			)
		)


class NetrpGetFileSecurityResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'lpFileName',
			WCHAR
			),
			(
			'RequestedInformation',
			SECURITY_INFORMATION
			)
		)


class NetrpSetFileSecurity(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'lpFileName',
			WCHAR
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			),
			(
			'SecurityDescriptor',
			PADT_SECURITY_DESCRIPTOR
			)
		)


class NetrpSetFileSecurityResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'lpFileName',
			WCHAR
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			),
			(
			'SecurityDescriptor',
			PADT_SECURITY_DESCRIPTOR
			)
		)


class NetrServerTransportAddEx(NDRCALL):
	OPNUM = 41
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPTRANSPORT_INFO
			)
		)


class NetrServerTransportAddExResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPTRANSPORT_INFO
			)
		)


class Opnum42NotUsedOnWire(NDRCALL):
	OPNUM = 42
	structure = (

		)


class Opnum42NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrDfsGetVersion(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			)
		)


class NetrDfsGetVersionResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			)
		)


class NetrDfsCreateLocalPartition(NDRCALL):
	OPNUM = 44
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'EntryUid',
			GUID
			),
			(
			'EntryPrefix',
			WCHAR
			),
			(
			'ShortName',
			WCHAR
			),
			(
			'RelationInfo',
			LPNET_DFS_ENTRY_ID_CONTAINER
			),
			(
			'Force',
			INT
			)
		)


class NetrDfsCreateLocalPartitionResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ShareName',
			WCHAR
			),
			(
			'EntryUid',
			GUID
			),
			(
			'EntryPrefix',
			WCHAR
			),
			(
			'ShortName',
			WCHAR
			),
			(
			'RelationInfo',
			LPNET_DFS_ENTRY_ID_CONTAINER
			),
			(
			'Force',
			INT
			)
		)


class NetrDfsDeleteLocalPartition(NDRCALL):
	OPNUM = 45
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			)
		)


class NetrDfsDeleteLocalPartitionResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			)
		)


class NetrDfsSetLocalVolumeState(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'State',
			UNSIGNED_LONG
			)
		)


class NetrDfsSetLocalVolumeStateResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'State',
			UNSIGNED_LONG
			)
		)


class Opnum47NotUsedOnWire(NDRCALL):
	OPNUM = 47
	structure = (

		)


class Opnum47NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrDfsCreateExitPoint(NDRCALL):
	OPNUM = 48
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'Type',
			UNSIGNED_LONG
			),
			(
			'ShortPrefixLen',
			DWORD
			)
		)


class NetrDfsCreateExitPointResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'Type',
			UNSIGNED_LONG
			),
			(
			'ShortPrefixLen',
			DWORD
			)
		)


class NetrDfsDeleteExitPoint(NDRCALL):
	OPNUM = 49
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'Type',
			UNSIGNED_LONG
			)
		)


class NetrDfsDeleteExitPointResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			),
			(
			'Type',
			UNSIGNED_LONG
			)
		)


class NetrDfsModifyPrefix(NDRCALL):
	OPNUM = 50
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			)
		)


class NetrDfsModifyPrefixResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Uid',
			GUID
			),
			(
			'Prefix',
			WCHAR
			)
		)


class NetrDfsFixLocalVolume(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'VolumeName',
			WCHAR
			),
			(
			'EntryType',
			UNSIGNED_LONG
			),
			(
			'ServiceType',
			UNSIGNED_LONG
			),
			(
			'StgId',
			WCHAR
			),
			(
			'EntryUid',
			GUID
			),
			(
			'EntryPrefix',
			WCHAR
			),
			(
			'RelationInfo',
			LPNET_DFS_ENTRY_ID_CONTAINER
			),
			(
			'CreateDisposition',
			UNSIGNED_LONG
			)
		)


class NetrDfsFixLocalVolumeResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'VolumeName',
			WCHAR
			),
			(
			'EntryType',
			UNSIGNED_LONG
			),
			(
			'ServiceType',
			UNSIGNED_LONG
			),
			(
			'StgId',
			WCHAR
			),
			(
			'EntryUid',
			GUID
			),
			(
			'EntryPrefix',
			WCHAR
			),
			(
			'RelationInfo',
			LPNET_DFS_ENTRY_ID_CONTAINER
			),
			(
			'CreateDisposition',
			UNSIGNED_LONG
			)
		)


class NetrDfsManagerReportSiteInfo(NDRCALL):
	OPNUM = 52
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ppSiteInfo',
			LPDFS_SITELIST_INFO
			)
		)


class NetrDfsManagerReportSiteInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'ppSiteInfo',
			LPDFS_SITELIST_INFO
			)
		)


class NetrServerTransportDelEx(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPTRANSPORT_INFO
			)
		)


class NetrServerTransportDelExResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'Buffer',
			LPTRANSPORT_INFO
			)
		)


class NetrServerAliasAdd(NDRCALL):
	OPNUM = 54
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_INFO
			)
		)


class NetrServerAliasAddResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_INFO
			)
		)


class NetrServerAliasEnum(NDRCALL):
	OPNUM = 55
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			LPDWORD
			)
		)


class NetrServerAliasEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_ENUM_STRUCT
			),
			(
			'PreferedMaximumLength',
			DWORD
			),
			(
			'ResumeHandle',
			LPDWORD
			)
		)


class NetrServerAliasDel(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_INFO
			)
		)


class NetrServerAliasDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'InfoStruct',
			LPSERVER_ALIAS_INFO
			)
		)


class NetrShareDelEx(NDRCALL):
	OPNUM = 57
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'ShareInfo',
			LPSHARE_INFO
			)
		)


class NetrShareDelExResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			SRVSVC_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'ShareInfo',
			LPSHARE_INFO
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
	Opnum3NotUsedOnWire,
	Opnum3NotUsedOnWireResponse
	),4 : (
	Opnum4NotUsedOnWire,
	Opnum4NotUsedOnWireResponse
	),5 : (
	Opnum5NotUsedOnWire,
	Opnum5NotUsedOnWireResponse
	),6 : (
	Opnum6NotUsedOnWire,
	Opnum6NotUsedOnWireResponse
	),7 : (
	Opnum7NotUsedOnWire,
	Opnum7NotUsedOnWireResponse
	),8 : (
	NetrConnectionEnum,
	NetrConnectionEnumResponse
	),9 : (
	NetrFileEnum,
	NetrFileEnumResponse
	),10 : (
	NetrFileGetInfo,
	NetrFileGetInfoResponse
	),11 : (
	NetrFileClose,
	NetrFileCloseResponse
	),12 : (
	NetrSessionEnum,
	NetrSessionEnumResponse
	),13 : (
	NetrSessionDel,
	NetrSessionDelResponse
	),14 : (
	NetrShareAdd,
	NetrShareAddResponse
	),15 : (
	NetrShareEnum,
	NetrShareEnumResponse
	),16 : (
	NetrShareGetInfo,
	NetrShareGetInfoResponse
	),17 : (
	NetrShareSetInfo,
	NetrShareSetInfoResponse
	),18 : (
	NetrShareDel,
	NetrShareDelResponse
	),19 : (
	NetrShareDelSticky,
	NetrShareDelStickyResponse
	),20 : (
	NetrShareCheck,
	NetrShareCheckResponse
	),21 : (
	NetrServerGetInfo,
	NetrServerGetInfoResponse
	),22 : (
	NetrServerSetInfo,
	NetrServerSetInfoResponse
	),23 : (
	NetrServerDiskEnum,
	NetrServerDiskEnumResponse
	),24 : (
	NetrServerStatisticsGet,
	NetrServerStatisticsGetResponse
	),25 : (
	NetrServerTransportAdd,
	NetrServerTransportAddResponse
	),26 : (
	NetrServerTransportEnum,
	NetrServerTransportEnumResponse
	),27 : (
	NetrServerTransportDel,
	NetrServerTransportDelResponse
	),28 : (
	NetrRemoteTOD,
	NetrRemoteTODResponse
	),29 : (
	Opnum29NotUsedOnWire,
	Opnum29NotUsedOnWireResponse
	),30 : (
	NetprPathType,
	NetprPathTypeResponse
	),31 : (
	NetprPathCanonicalize,
	NetprPathCanonicalizeResponse
	),32 : (
	NetprPathCompare,
	NetprPathCompareResponse
	),33 : (
	NetprNameValidate,
	NetprNameValidateResponse
	),34 : (
	NetprNameCanonicalize,
	NetprNameCanonicalizeResponse
	),35 : (
	NetprNameCompare,
	NetprNameCompareResponse
	),36 : (
	NetrShareEnumSticky,
	NetrShareEnumStickyResponse
	),37 : (
	NetrShareDelStart,
	NetrShareDelStartResponse
	),38 : (
	NetrShareDelCommit,
	NetrShareDelCommitResponse
	),39 : (
	NetrpGetFileSecurity,
	NetrpGetFileSecurityResponse
	),40 : (
	NetrpSetFileSecurity,
	NetrpSetFileSecurityResponse
	),41 : (
	NetrServerTransportAddEx,
	NetrServerTransportAddExResponse
	),42 : (
	Opnum42NotUsedOnWire,
	Opnum42NotUsedOnWireResponse
	),43 : (
	NetrDfsGetVersion,
	NetrDfsGetVersionResponse
	),44 : (
	NetrDfsCreateLocalPartition,
	NetrDfsCreateLocalPartitionResponse
	),45 : (
	NetrDfsDeleteLocalPartition,
	NetrDfsDeleteLocalPartitionResponse
	),46 : (
	NetrDfsSetLocalVolumeState,
	NetrDfsSetLocalVolumeStateResponse
	),47 : (
	Opnum47NotUsedOnWire,
	Opnum47NotUsedOnWireResponse
	),48 : (
	NetrDfsCreateExitPoint,
	NetrDfsCreateExitPointResponse
	),49 : (
	NetrDfsDeleteExitPoint,
	NetrDfsDeleteExitPointResponse
	),50 : (
	NetrDfsModifyPrefix,
	NetrDfsModifyPrefixResponse
	),51 : (
	NetrDfsFixLocalVolume,
	NetrDfsFixLocalVolumeResponse
	),52 : (
	NetrDfsManagerReportSiteInfo,
	NetrDfsManagerReportSiteInfoResponse
	),53 : (
	NetrServerTransportDelEx,
	NetrServerTransportDelExResponse
	),54 : (
	NetrServerAliasAdd,
	NetrServerAliasAddResponse
	),55 : (
	NetrServerAliasEnum,
	NetrServerAliasEnumResponse
	),56 : (
	NetrServerAliasDel,
	NetrServerAliasDelResponse
	),57 : (
	NetrShareDelEx,
	NetrShareDelExResponse
	)}
