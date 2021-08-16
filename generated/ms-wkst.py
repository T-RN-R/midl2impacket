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
#wkssvc Definition
#################################################################################
MSRPC_UUID_WKSSVC = uuidtup_to_bin(('6BFFD098-A112-3610-9833-46C3F87E345A','0.0'))
NETSETUP_JOIN_STATUS = DWORD__ENUM
NetSetupUnknownStatus = 0
NetSetupUnjoined = 0
NetSetupWorkgroupName = 0
NETSETUP_NAME_TYPE = DWORD__ENUM
NetSetupUnknown = 0
NetSetupMachine = 0
NetSetupWorkgroup = 0
NetSetupDomain = 0
NetSetupNonExistentDomain = 0
NET_COMPUTER_NAME_TYPE = DWORD__ENUM
NetPrimaryComputerName = 0
NetAlternateComputerNames = 0
NetAllComputerNames = 0
class STAT_WORKSTATION_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'StatisticsStartTime',
			LARGE_INTEGER
			),
			(
			'BytesReceived',
			LARGE_INTEGER
			),
			(
			'SmbsReceived',
			LARGE_INTEGER
			),
			(
			'PagingReadBytesRequested',
			LARGE_INTEGER
			),
			(
			'NonPagingReadBytesRequested',
			LARGE_INTEGER
			),
			(
			'CacheReadBytesRequested',
			LARGE_INTEGER
			),
			(
			'NetworkReadBytesRequested',
			LARGE_INTEGER
			),
			(
			'BytesTransmitted',
			LARGE_INTEGER
			),
			(
			'SmbsTransmitted',
			LARGE_INTEGER
			),
			(
			'PagingWriteBytesRequested',
			LARGE_INTEGER
			),
			(
			'NonPagingWriteBytesRequested',
			LARGE_INTEGER
			),
			(
			'CacheWriteBytesRequested',
			LARGE_INTEGER
			),
			(
			'NetworkWriteBytesRequested',
			LARGE_INTEGER
			),
			(
			'InitiallyFailedOperations',
			UNSIGNED_LONG
			),
			(
			'FailedCompletionOperations',
			UNSIGNED_LONG
			),
			(
			'ReadOperations',
			UNSIGNED_LONG
			),
			(
			'RandomReadOperations',
			UNSIGNED_LONG
			),
			(
			'ReadSmbs',
			UNSIGNED_LONG
			),
			(
			'LargeReadSmbs',
			UNSIGNED_LONG
			),
			(
			'SmallReadSmbs',
			UNSIGNED_LONG
			),
			(
			'WriteOperations',
			UNSIGNED_LONG
			),
			(
			'RandomWriteOperations',
			UNSIGNED_LONG
			),
			(
			'WriteSmbs',
			UNSIGNED_LONG
			),
			(
			'LargeWriteSmbs',
			UNSIGNED_LONG
			),
			(
			'SmallWriteSmbs',
			UNSIGNED_LONG
			),
			(
			'RawReadsDenied',
			UNSIGNED_LONG
			),
			(
			'RawWritesDenied',
			UNSIGNED_LONG
			),
			(
			'NetworkErrors',
			UNSIGNED_LONG
			),
			(
			'Sessions',
			UNSIGNED_LONG
			),
			(
			'FailedSessions',
			UNSIGNED_LONG
			),
			(
			'Reconnects',
			UNSIGNED_LONG
			),
			(
			'CoreConnects',
			UNSIGNED_LONG
			),
			(
			'Lanman20Connects',
			UNSIGNED_LONG
			),
			(
			'Lanman21Connects',
			UNSIGNED_LONG
			),
			(
			'LanmanNtConnects',
			UNSIGNED_LONG
			),
			(
			'ServerDisconnects',
			UNSIGNED_LONG
			),
			(
			'HungSessions',
			UNSIGNED_LONG
			),
			(
			'UseCount',
			UNSIGNED_LONG
			),
			(
			'FailedUseCount',
			UNSIGNED_LONG
			),
			(
			'CurrentCommands',
			UNSIGNED_LONG
			)
		)


class PSTAT_WORKSTATION_0(NDRPOINTER):
	referent = (
			(
			'Data',
			STAT_WORKSTATION_0
			)
		)


class LPSTAT_WORKSTATION_0(NDRPOINTER):
	referent = (
			(
			'Data',
			STAT_WORKSTATION_0
			)
		)


class WKSTA_INFO_100(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki100_platform_id',
			UNSIGNED_LONG
			),
			(
			'wki100_computername',
			WCHAR_T
			),
			(
			'wki100_langroup',
			WCHAR_T
			),
			(
			'wki100_ver_major',
			UNSIGNED_LONG
			),
			(
			'wki100_ver_minor',
			UNSIGNED_LONG
			)
		)


class PWKSTA_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_100
			)
		)


class LPWKSTA_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_100
			)
		)


class WKSTA_INFO_101(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki101_platform_id',
			UNSIGNED_LONG
			),
			(
			'wki101_computername',
			WCHAR_T
			),
			(
			'wki101_langroup',
			WCHAR_T
			),
			(
			'wki101_ver_major',
			UNSIGNED_LONG
			),
			(
			'wki101_ver_minor',
			UNSIGNED_LONG
			),
			(
			'wki101_lanroot',
			WCHAR_T
			)
		)


class PWKSTA_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_101
			)
		)


class LPWKSTA_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_101
			)
		)


class WKSTA_INFO_102(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki102_platform_id',
			UNSIGNED_LONG
			),
			(
			'wki102_computername',
			WCHAR_T
			),
			(
			'wki102_langroup',
			WCHAR_T
			),
			(
			'wki102_ver_major',
			UNSIGNED_LONG
			),
			(
			'wki102_ver_minor',
			UNSIGNED_LONG
			),
			(
			'wki102_lanroot',
			WCHAR_T
			),
			(
			'wki102_logged_on_users',
			UNSIGNED_LONG
			)
		)


class PWKSTA_INFO_102(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_102
			)
		)


class LPWKSTA_INFO_102(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_102
			)
		)


class WKSTA_INFO_502(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki502_char_wait',
			UNSIGNED_LONG
			),
			(
			'wki502_collection_time',
			UNSIGNED_LONG
			),
			(
			'wki502_maximum_collection_count',
			UNSIGNED_LONG
			),
			(
			'wki502_keep_conn',
			UNSIGNED_LONG
			),
			(
			'wki502_max_cmds',
			UNSIGNED_LONG
			),
			(
			'wki502_sess_timeout',
			UNSIGNED_LONG
			),
			(
			'wki502_siz_char_buf',
			UNSIGNED_LONG
			),
			(
			'wki502_max_threads',
			UNSIGNED_LONG
			),
			(
			'wki502_lock_quota',
			UNSIGNED_LONG
			),
			(
			'wki502_lock_increment',
			UNSIGNED_LONG
			),
			(
			'wki502_lock_maximum',
			UNSIGNED_LONG
			),
			(
			'wki502_pipe_increment',
			UNSIGNED_LONG
			),
			(
			'wki502_pipe_maximum',
			UNSIGNED_LONG
			),
			(
			'wki502_cache_file_timeout',
			UNSIGNED_LONG
			),
			(
			'wki502_dormant_file_limit',
			UNSIGNED_LONG
			),
			(
			'wki502_read_ahead_throughput',
			UNSIGNED_LONG
			),
			(
			'wki502_num_mailslot_buffers',
			UNSIGNED_LONG
			),
			(
			'wki502_num_srv_announce_buffers',
			UNSIGNED_LONG
			),
			(
			'wki502_max_illegal_datagram_events',
			UNSIGNED_LONG
			),
			(
			'wki502_illegal_datagram_event_reset_frequency',
			UNSIGNED_LONG
			),
			(
			'wki502_log_election_packets',
			INT
			),
			(
			'wki502_use_opportunistic_locking',
			INT
			),
			(
			'wki502_use_unlock_behind',
			INT
			),
			(
			'wki502_use_close_behind',
			INT
			),
			(
			'wki502_buf_named_pipes',
			INT
			),
			(
			'wki502_use_lock_read_unlock',
			INT
			),
			(
			'wki502_utilize_nt_caching',
			INT
			),
			(
			'wki502_use_raw_read',
			INT
			),
			(
			'wki502_use_raw_write',
			INT
			),
			(
			'wki502_use_write_raw_data',
			INT
			),
			(
			'wki502_use_encryption',
			INT
			),
			(
			'wki502_buf_files_deny_write',
			INT
			),
			(
			'wki502_buf_read_only_files',
			INT
			),
			(
			'wki502_force_core_create_mode',
			INT
			),
			(
			'wki502_use_512_byte_max_transfer',
			INT
			)
		)


class PWKSTA_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_502
			)
		)


class LPWKSTA_INFO_502(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_502
			)
		)


class WKSTA_INFO_1013(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki1013_keep_conn',
			UNSIGNED_LONG
			)
		)


class PWKSTA_INFO_1013(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1013
			)
		)


class LPWKSTA_INFO_1013(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1013
			)
		)


class WKSTA_INFO_1018(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki1018_sess_timeout',
			UNSIGNED_LONG
			)
		)


class PWKSTA_INFO_1018(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1018
			)
		)


class LPWKSTA_INFO_1018(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1018
			)
		)


class WKSTA_INFO_1046(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wki1046_dormant_file_limit',
			UNSIGNED_LONG
			)
		)


class PWKSTA_INFO_1046(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1046
			)
		)


class LPWKSTA_INFO_1046(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO_1046
			)
		)


class WKSTA_USER_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wkui0_username',
			WCHAR_T
			)
		)


class PWKSTA_USER_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_0
			)
		)


class LPWKSTA_USER_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_0
			)
		)


class WKSTA_USER_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wkui1_username',
			WCHAR_T
			),
			(
			'wkui1_logon_domain',
			WCHAR_T
			),
			(
			'wkui1_oth_domains',
			WCHAR_T
			),
			(
			'wkui1_logon_server',
			WCHAR_T
			)
		)


class PWKSTA_USER_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_1
			)
		)


class LPWKSTA_USER_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_1
			)
		)


class WKSTA_TRANSPORT_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wkti0_quality_of_service',
			UNSIGNED_LONG
			),
			(
			'wkti0_number_of_vcs',
			UNSIGNED_LONG
			),
			(
			'wkti0_transport_name',
			WCHAR_T
			),
			(
			'wkti0_transport_address',
			WCHAR_T
			),
			(
			'wkti0_wan_ish',
			UNSIGNED_LONG
			)
		)


class PWKSTA_TRANSPORT_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_INFO_0
			)
		)


class LPWKSTA_TRANSPORT_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_INFO_0
			)
		)


WKSSVC_IDENTIFY_HANDLE = WCHAR_T
WKSSVC_IMPERSONATE_HANDLE = WCHAR_T
class WKSTA_INFO(NDRUNION):
	union = {100 : (
		'WkstaInfo100',
		LPWKSTA_INFO_100
		),101 : (
		'WkstaInfo101',
		LPWKSTA_INFO_101
		),102 : (
		'WkstaInfo102',
		LPWKSTA_INFO_102
		),502 : (
		'WkstaInfo502',
		LPWKSTA_INFO_502
		),1013 : (
		'WkstaInfo1013',
		LPWKSTA_INFO_1013
		),1018 : (
		'WkstaInfo1018',
		LPWKSTA_INFO_1018
		),1046 : (
		'WkstaInfo1046',
		LPWKSTA_INFO_1046
		)}


class PWKSTA_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO
			)
		)


class LPWKSTA_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_INFO
			)
		)


class USE_INFO_0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ui0_local',
			WCHAR_T
			),
			(
			'ui0_remote',
			WCHAR_T
			)
		)


class PUSE_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_0
			)
		)


class LPUSE_INFO_0(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_0
			)
		)


class USE_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ui1_local',
			WCHAR_T
			),
			(
			'ui1_remote',
			WCHAR_T
			),
			(
			'ui1_password',
			WCHAR_T
			),
			(
			'ui1_status',
			UNSIGNED_LONG
			),
			(
			'ui1_asg_type',
			UNSIGNED_LONG
			),
			(
			'ui1_refcount',
			UNSIGNED_LONG
			),
			(
			'ui1_usecount',
			UNSIGNED_LONG
			)
		)


class PUSE_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_1
			)
		)


class LPUSE_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_1
			)
		)


class USE_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ui2_useinfo',
			USE_INFO_1
			),
			(
			'ui2_username',
			WCHAR_T
			),
			(
			'ui2_domainname',
			WCHAR_T
			)
		)


class PUSE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_2
			)
		)


class LPUSE_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_2
			)
		)


class USE_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ui3_ui2',
			USE_INFO_2
			),
			(
			'ui3_flags',
			ULONG
			)
		)


class PUSE_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_3
			)
		)


class LPUSE_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_3
			)
		)


class USE_INFO(NDRUNION):
	union = {0 : (
		'UseInfo0',
		LPUSE_INFO_0
		),1 : (
		'UseInfo1',
		LPUSE_INFO_1
		),2 : (
		'UseInfo2',
		LPUSE_INFO_2
		),3 : (
		'UseInfo3',
		LPUSE_INFO_3
		)}


class PUSE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO
			)
		)


class LPUSE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO
			)
		)


class USE_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPUSE_INFO_0
			)
		)


class PUSE_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_0_CONTAINER
			)
		)


class LPUSE_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_0_CONTAINER
			)
		)


class USE_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPUSE_INFO_1
			)
		)


class PUSE_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_1_CONTAINER
			)
		)


class LPUSE_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_1_CONTAINER
			)
		)


class USE_INFO_2_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPUSE_INFO_2
			)
		)


class PUSE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_2_CONTAINER
			)
		)


class LPUSE_INFO_2_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_INFO_2_CONTAINER
			)
		)


class USEINFO(NDRUNION):
	union = {0 : (
		'Level0',
		LPUSE_INFO_0_CONTAINER
		),1 : (
		'Level1',
		LPUSE_INFO_1_CONTAINER
		),2 : (
		'Level2',
		LPUSE_INFO_2_CONTAINER
		)}


class USE_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'UseInfo',
			USEINFO
			)
		)


class PUSE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_ENUM_STRUCT
			)
		)


class LPUSE_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			USE_ENUM_STRUCT
			)
		)


class WKSTA_USER_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPWKSTA_USER_INFO_0
			)
		)


class PWKSTA_USER_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_0_CONTAINER
			)
		)


class LPWKSTA_USER_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_0_CONTAINER
			)
		)


class WKSTA_USER_INFO_1_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPWKSTA_USER_INFO_1
			)
		)


class PWKSTA_USER_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_1_CONTAINER
			)
		)


class LPWKSTA_USER_INFO_1_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_INFO_1_CONTAINER
			)
		)


class WKSTAUSERINFO(NDRUNION):
	union = {0 : (
		'Level0',
		LPWKSTA_USER_INFO_0_CONTAINER
		),1 : (
		'Level1',
		LPWKSTA_USER_INFO_1_CONTAINER
		)}


class WKSTA_USER_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'WkstaUserInfo',
			WKSTAUSERINFO
			)
		)


class PWKSTA_USER_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_ENUM_STRUCT
			)
		)


class LPWKSTA_USER_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_USER_ENUM_STRUCT
			)
		)


class WKSTA_TRANSPORT_INFO_0_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			LPWKSTA_TRANSPORT_INFO_0
			)
		)


class PWKSTA_TRANSPORT_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_INFO_0_CONTAINER
			)
		)


class LPWKSTA_TRANSPORT_INFO_0_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_INFO_0_CONTAINER
			)
		)


class WKSTATRANSPORTINFO(NDRUNION):
	union = {0 : (
		'Level0',
		LPWKSTA_TRANSPORT_INFO_0_CONTAINER
		)}


class WKSTA_TRANSPORT_ENUM_STRUCT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'WkstaTransportInfo',
			WKSTATRANSPORTINFO
			)
		)


class PWKSTA_TRANSPORT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_ENUM_STRUCT
			)
		)


class LPWKSTA_TRANSPORT_ENUM_STRUCT(NDRPOINTER):
	referent = (
			(
			'Data',
			WKSTA_TRANSPORT_ENUM_STRUCT
			)
		)


class JOINPR_USER_PASSWORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Obfuscator',
			UNSIGNED_CHAR
			),
			(
			'Buffer',
			WCHAR_T
			),
			(
			'Length',
			UNSIGNED_LONG
			)
		)


class PJOINPR_USER_PASSWORD(NDRPOINTER):
	referent = (
			(
			'Data',
			JOINPR_USER_PASSWORD
			)
		)


class JOINPR_ENCRYPTED_USER_PASSWORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Buffer',
			UNSIGNED_CHAR
			)
		)


class PJOINPR_ENCRYPTED_USER_PASSWORD(NDRPOINTER):
	referent = (
			(
			'Data',
			JOINPR_ENCRYPTED_USER_PASSWORD
			)
		)


class DATA_UNICODE_STRING(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_UNICODE_STRING(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_UNICODE_STRING
			)
		)


class UNICODE_STRING(NDRSTRUCT):
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
			PTR_UNICODE_STRING
			)
		)


class NET_COMPUTER_NAME_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntryCount',
			UNSIGNED_LONG
			),
			(
			'ComputerNames',
			PUNICODE_STRING
			)
		)


class PNET_COMPUTER_NAME_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			NET_COMPUTER_NAME_ARRAY
			)
		)


class NetrWkstaGetInfo(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			)
		)


class NetrWkstaGetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			)
		)


class NetrWkstaSetInfo(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'WkstaInfo',
			LPWKSTA_INFO
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrWkstaSetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'WkstaInfo',
			LPWKSTA_INFO
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrWkstaUserEnum(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'UserInfo',
			LPWKSTA_USER_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
		)


class NetrWkstaUserEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'UserInfo',
			LPWKSTA_USER_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
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


class NetrWkstaTransportEnum(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'TransportInfo',
			LPWKSTA_TRANSPORT_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
		)


class NetrWkstaTransportEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'TransportInfo',
			LPWKSTA_TRANSPORT_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
		)


class NetrWkstaTransportAdd(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'TransportInfo',
			LPWKSTA_TRANSPORT_INFO_0
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrWkstaTransportAddResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'TransportInfo',
			LPWKSTA_TRANSPORT_INFO_0
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrWkstaTransportDel(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'TransportName',
			WCHAR_T
			),
			(
			'ForceLevel',
			UNSIGNED_LONG
			)
		)


class NetrWkstaTransportDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'TransportName',
			WCHAR_T
			),
			(
			'ForceLevel',
			UNSIGNED_LONG
			)
		)


class NetrUseAdd(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'InfoStruct',
			LPUSE_INFO
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrUseAddResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'InfoStruct',
			LPUSE_INFO
			),
			(
			'ErrorParameter',
			UNSIGNED_LONG
			)
		)


class NetrUseGetInfo(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'UseName',
			WCHAR_T
			),
			(
			'Level',
			UNSIGNED_LONG
			)
		)


class NetrUseGetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'UseName',
			WCHAR_T
			),
			(
			'Level',
			UNSIGNED_LONG
			)
		)


class NetrUseDel(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'UseName',
			WCHAR_T
			),
			(
			'ForceLevel',
			UNSIGNED_LONG
			)
		)


class NetrUseDelResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'UseName',
			WCHAR_T
			),
			(
			'ForceLevel',
			UNSIGNED_LONG
			)
		)


class NetrUseEnum(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'InfoStruct',
			LPUSE_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
		)


class NetrUseEnumResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'InfoStruct',
			LPUSE_ENUM_STRUCT
			),
			(
			'PreferredMaximumLength',
			UNSIGNED_LONG
			),
			(
			'ResumeHandle',
			UNSIGNED_LONG
			)
		)


class Opnum12NotUsedOnWire(NDRCALL):
	OPNUM = 12
	structure = (

		)


class Opnum12NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrWorkstationStatisticsGet(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'ServiceName',
			WCHAR_T
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrWorkstationStatisticsGetResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IDENTIFY_HANDLE
			),
			(
			'ServiceName',
			WCHAR_T
			),
			(
			'Level',
			UNSIGNED_LONG
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class Opnum14NotUsedOnWire(NDRCALL):
	OPNUM = 14
	structure = (

		)


class Opnum14NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum15NotUsedOnWire(NDRCALL):
	OPNUM = 15
	structure = (

		)


class Opnum15NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum16NotUsedOnWire(NDRCALL):
	OPNUM = 16
	structure = (

		)


class Opnum16NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum17NotUsedOnWire(NDRCALL):
	OPNUM = 17
	structure = (

		)


class Opnum17NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum18NotUsedOnWire(NDRCALL):
	OPNUM = 18
	structure = (

		)


class Opnum18NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum19NotUsedOnWire(NDRCALL):
	OPNUM = 19
	structure = (

		)


class Opnum19NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrGetJoinInformation(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'NameBuffer',
			WCHAR_T
			)
		)


class NetrGetJoinInformationResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'NameBuffer',
			WCHAR_T
			)
		)


class Opnum21NotUsedOnWire(NDRCALL):
	OPNUM = 21
	structure = (

		)


class Opnum21NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class NetrJoinDomain2(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'DomainNameParam',
			WCHAR_T
			),
			(
			'MachineAccountOU',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrJoinDomain2Response(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'DomainNameParam',
			WCHAR_T
			),
			(
			'MachineAccountOU',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrUnjoinDomain2(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrUnjoinDomain2Response(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrRenameMachineInDomain2(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'MachineName',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrRenameMachineInDomain2Response(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'MachineName',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Options',
			UNSIGNED_LONG
			)
		)


class NetrValidateName2(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'NameToValidate',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'NameType',
			NETSETUP_NAME_TYPE
			)
		)


class NetrValidateName2Response(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'NameToValidate',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'NameType',
			NETSETUP_NAME_TYPE
			)
		)


class NetrGetJoinableOUs2(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'DomainNameParam',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'OUCount',
			UNSIGNED_LONG
			)
		)


class NetrGetJoinableOUs2Response(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'DomainNameParam',
			WCHAR_T
			),
			(
			'AccountName',
			WCHAR_T
			),
			(
			'Password',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'OUCount',
			UNSIGNED_LONG
			)
		)


class NetrAddAlternateComputerName(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AlternateName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrAddAlternateComputerNameResponse(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AlternateName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrRemoveAlternateComputerName(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AlternateName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrRemoveAlternateComputerNameResponse(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'AlternateName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrSetPrimaryComputerName(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'PrimaryName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrSetPrimaryComputerNameResponse(NDRCALL):
	structure = (
			(
			'RpcBindingHandle',
			HANDLE_T
			),
			(
			'ServerName',
			WCHAR_T
			),
			(
			'PrimaryName',
			WCHAR_T
			),
			(
			'DomainAccount',
			WCHAR_T
			),
			(
			'EncryptedPassword',
			PJOINPR_ENCRYPTED_USER_PASSWORD
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrEnumerateComputerNames(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'NameType',
			NET_COMPUTER_NAME_TYPE
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


class NetrEnumerateComputerNamesResponse(NDRCALL):
	structure = (
			(
			'ServerName',
			WKSSVC_IMPERSONATE_HANDLE
			),
			(
			'NameType',
			NET_COMPUTER_NAME_TYPE
			),
			(
			'Reserved',
			UNSIGNED_LONG
			)
		)


OPNUMS = {0 : (
	NetrWkstaGetInfo,
	NetrWkstaGetInfoResponse
	),1 : (
	NetrWkstaSetInfo,
	NetrWkstaSetInfoResponse
	),2 : (
	NetrWkstaUserEnum,
	NetrWkstaUserEnumResponse
	),3 : (
	Opnum3NotUsedOnWire,
	Opnum3NotUsedOnWireResponse
	),4 : (
	Opnum4NotUsedOnWire,
	Opnum4NotUsedOnWireResponse
	),5 : (
	NetrWkstaTransportEnum,
	NetrWkstaTransportEnumResponse
	),6 : (
	NetrWkstaTransportAdd,
	NetrWkstaTransportAddResponse
	),7 : (
	NetrWkstaTransportDel,
	NetrWkstaTransportDelResponse
	),8 : (
	NetrUseAdd,
	NetrUseAddResponse
	),9 : (
	NetrUseGetInfo,
	NetrUseGetInfoResponse
	),10 : (
	NetrUseDel,
	NetrUseDelResponse
	),11 : (
	NetrUseEnum,
	NetrUseEnumResponse
	),12 : (
	Opnum12NotUsedOnWire,
	Opnum12NotUsedOnWireResponse
	),13 : (
	NetrWorkstationStatisticsGet,
	NetrWorkstationStatisticsGetResponse
	),14 : (
	Opnum14NotUsedOnWire,
	Opnum14NotUsedOnWireResponse
	),15 : (
	Opnum15NotUsedOnWire,
	Opnum15NotUsedOnWireResponse
	),16 : (
	Opnum16NotUsedOnWire,
	Opnum16NotUsedOnWireResponse
	),17 : (
	Opnum17NotUsedOnWire,
	Opnum17NotUsedOnWireResponse
	),18 : (
	Opnum18NotUsedOnWire,
	Opnum18NotUsedOnWireResponse
	),19 : (
	Opnum19NotUsedOnWire,
	Opnum19NotUsedOnWireResponse
	),20 : (
	NetrGetJoinInformation,
	NetrGetJoinInformationResponse
	),21 : (
	Opnum21NotUsedOnWire,
	Opnum21NotUsedOnWireResponse
	),22 : (
	NetrJoinDomain2,
	NetrJoinDomain2Response
	),23 : (
	NetrUnjoinDomain2,
	NetrUnjoinDomain2Response
	),24 : (
	NetrRenameMachineInDomain2,
	NetrRenameMachineInDomain2Response
	),25 : (
	NetrValidateName2,
	NetrValidateName2Response
	),26 : (
	NetrGetJoinableOUs2,
	NetrGetJoinableOUs2Response
	),27 : (
	NetrAddAlternateComputerName,
	NetrAddAlternateComputerNameResponse
	),28 : (
	NetrRemoveAlternateComputerName,
	NetrRemoveAlternateComputerNameResponse
	),29 : (
	NetrSetPrimaryComputerName,
	NetrSetPrimaryComputerNameResponse
	),30 : (
	NetrEnumerateComputerNames,
	NetrEnumerateComputerNamesResponse
	)}
