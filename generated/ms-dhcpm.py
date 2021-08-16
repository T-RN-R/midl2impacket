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
DHCP_SRV_HANDLE = WCHAR_T
DHCP_IP_ADDRESS = DWORD
PDHCP_IP_ADDRESS = DWORD
LPDHCP_IP_ADDRESS = DWORD
DHCP_IP_MASK = DWORD
DHCP_RESUME_HANDLE = DWORD
DHCP_OPTION_ID = DWORD
class DATA_DHCP_BINARY_DATA(NDRUniConformantArray):
	item = BYTE


class PTR_DHCP_BINARY_DATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_BINARY_DATA
			)
		)


class DHCP_BINARY_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'DataLength',
			DWORD
			),
			(
			'Data',
			PTR_DHCP_BINARY_DATA
			)
		)


DHCP_CLIENT_UID = DHCP_BINARY_DATA
DHCP_SUBNET_STATE = DWORD__ENUM
DhcpSubnetEnabled = 0
DhcpSubnetDisabled = 1
DhcpSubnetEnabledSwitched = 2
DhcpSubnetDisabledSwitched = 3
DHCP_SUBNET_ELEMENT_TYPE = DWORD__ENUM
DhcpIpRanges = 0
DhcpSecondaryHosts = 1
DhcpReservedIps = 2
DhcpExcludedIpRanges = 3
DhcpIpUsedClusters = 4
DhcpIpRangesDhcpOnly = 5
DhcpIpRangesDhcpBootp = 6
DhcpIpRangesBootpOnly = 7
DHCP_FORCE_FLAG = DWORD__ENUM
DhcpFullForce = 0
DhcpNoForce = 1
DHCP_OPTION_TYPE = DWORD__ENUM
DhcpUnaryElementTypeOption = 0
DHCP_OPTION_DATA_TYPE = DWORD__ENUM
DhcpByteOption = 0
DhcpWordOption = 1
DhcpDWordOption = 2
DhcpDWordDWordOption = 3
DhcpIpAddressOption = 4
DhcpStringDataOption = 5
DhcpBinaryDataOption = 6
DhcpEncapsulatedDataOption = 7
DHCP_OPTION_SCOPE_TYPE = DWORD__ENUM
DhcpDefaultOptions = 0
DhcpGlobalOptions = 1
DhcpSubnetOptions = 2
DhcpReservedOptions = 3
DHCP_SEARCH_INFO_TYPE = DWORD__ENUM
DhcpClientIpAddress = 0
DhcpClientHardwareAddress = 1
DHCP_SCAN_FLAG = DWORD__ENUM
DhcpRegistryFix = 0
QuarantineStatus = DWORD__ENUM
NOQUARANTINE = 0
RESTRICTEDACCESS = 0
DROPPACKET = 0
PROBATION = 0
EXEMPT = 0
DEFAULTQUARSETTING = 0
class DHCP_HOST_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'IpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'NetBiosName',
			WCHAR_T
			),
			(
			'HostName',
			WCHAR_T
			)
		)


class LPDHCP_HOST_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_HOST_INFO
			)
		)


class DHCP_SUBNET_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'SubnetName',
			WCHAR_T
			),
			(
			'SubnetComment',
			WCHAR_T
			),
			(
			'PrimaryHost',
			DHCP_HOST_INFO
			),
			(
			'SubnetState',
			DHCP_SUBNET_STATE
			)
		)


class LPDHCP_SUBNET_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_INFO
			)
		)


class DHCP_IP_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_IP_ADDRESS
			)
		)


class LPDHCP_IP_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_ARRAY
			)
		)


class DHCP_IP_RANGE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'StartAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EndAddress',
			DHCP_IP_ADDRESS
			)
		)


class LPDHCP_IP_RANGE(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RANGE
			)
		)


class DHCP_IP_RESERVATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ReservedForClient',
			DHCP_CLIENT_UID
			)
		)


class LPDHCP_IP_RESERVATION(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RESERVATION
			)
		)


class DHCP_IP_CLUSTER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClusterAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ClusterMask',
			DWORD
			)
		)


class LPDHCP_IP_CLUSTER(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_CLUSTER
			)
		)


class DHCP_BOOTP_IP_RANGE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'StartAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EndAddress',
			DHCP_IP_ADDRESS
			),
			(
			'BootpAllocated',
			ULONG
			),
			(
			'MaxBootpAllowed',
			ULONG
			)
		)


class LPDHCP_BOOT_IP_RANGE(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_BOOTP_IP_RANGE
			)
		)


class ELEMENT(NDRUNION):
	union = {DhcpIpRanges : (
		'IpRange',
		DHCP_IP_RANGE
		),DhcpSecondaryHosts : (
		'SecondaryHost',
		DHCP_HOST_INFO
		),DhcpReservedIps : (
		'ReservedIp',
		DHCP_IP_RESERVATION
		),DhcpExcludedIpRanges : (
		'ExcludeIpRange',
		DHCP_IP_RANGE
		),DhcpIpUsedClusters : (
		'IpUsedCluster',
		DHCP_IP_CLUSTER
		)}


class DHCP_SUBNET_ELEMENT_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'Element',
			ELEMENT
			)
		)


class LPDHCP_SUBNET_ELEMENT_DATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_DATA
			)
		)


class DHCP_SUBNET_ELEMENT_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_SUBNET_ELEMENT_DATA
			)
		)


class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_INFO_ARRAY
			)
		)


class DWORD_DWORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'DWord1',
			DWORD
			),
			(
			'DWord2',
			DWORD
			)
		)


class LPDWORD_DWORD(NDRPOINTER):
	referent = (
			(
			'Data',
			DWORD_DWORD
			)
		)


class ELEMENT(NDRUNION):
	union = {DhcpByteOption : (
		'ByteOption',
		BYTE
		),DhcpWordOption : (
		'WordOption',
		WORD
		),DhcpDWordOption : (
		'DWordOption',
		DWORD
		),DhcpDWordDWordOption : (
		'DWordDWordOption',
		DWORD_DWORD
		),DhcpIpAddressOption : (
		'IpAddressOption',
		DHCP_IP_ADDRESS
		),DhcpStringDataOption : (
		'StringDataOption',
		WCHAR_T
		),DhcpBinaryDataOption : (
		'BinaryDataOption',
		DHCP_BINARY_DATA
		),DhcpEncapsulatedDataOption : (
		'EncapsulatedDataOption',
		DHCP_BINARY_DATA
		),DhcpIpv6AddressOption : (
		'Ipv6AddressDataOption',
		WCHAR_T
		)}


class DHCP_OPTION_DATA_ELEMENT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'OptionType',
			DHCP_OPTION_DATA_TYPE
			),
			(
			'Element',
			ELEMENT
			)
		)


class LPDHCP_OPTION_DATA_ELEMENT(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_DATA_ELEMENT
			)
		)


class DHCP_OPTION_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_OPTION_DATA_ELEMENT
			)
		)


class LPDHCP_OPTION_DATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_DATA
			)
		)


class DHCP_OPTION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'OptionName',
			WCHAR_T
			),
			(
			'OptionComment',
			WCHAR_T
			),
			(
			'DefaultValue',
			DHCP_OPTION_DATA
			),
			(
			'OptionType',
			DHCP_OPTION_TYPE
			)
		)


class LPDHCP_OPTION(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION
			)
		)


class DHCP_RESERVED_SCOPE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ReservedIpSubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class LPDHCP_RESERVED_SCOPE(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_RESERVED_SCOPE
			)
		)


class SCOPEINFO(NDRUNION):
	union = {DhcpSubnetOptions : (
		'SubnetScopeInfo',
		DHCP_IP_ADDRESS
		),DhcpReservedOptions : (
		'ReservedScopeInfo',
		DHCP_RESERVED_SCOPE
		),DhcpMScopeOptions : (
		'MScopeInfo',
		WCHAR_T
		)}


class DHCP_OPTION_SCOPE_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ScopeType',
			DHCP_OPTION_SCOPE_TYPE
			),
			(
			'ScopeInfo',
			SCOPEINFO
			)
		)


class LPDHCP_OPTION_SCOPE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_SCOPE_INFO
			)
		)


class DHCP_OPTION_VALUE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'Value',
			DHCP_OPTION_DATA
			)
		)


class LPDHCP_OPTION_VALUE(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_VALUE
			)
		)


class DHCP_OPTION_VALUE_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Values',
			LPDHCP_OPTION_VALUE
			)
		)


class LPDHCP_OPTION_VALUE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_VALUE_ARRAY
			)
		)


class DATE_TIME(NDRSTRUCT):
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


class LPDATE_TIME(NDRPOINTER):
	referent = (
			(
			'Data',
			DATE_TIME
			)
		)


class DHCP_CLIENT_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			)
		)


class LPDHCP_CLIENT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO
			)
		)


class SEARCHINFO(NDRUNION):
	union = {DhcpClientIpAddress : (
		'ClientIpAddress',
		DHCP_IP_ADDRESS
		),DhcpClientHardwareAddress : (
		'ClientHardwareAddress',
		DHCP_CLIENT_UID
		),DhcpClientName : (
		'ClientName',
		WCHAR_T
		)}


class DHCP_SEARCH_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SearchType',
			DHCP_SEARCH_INFO_TYPE
			),
			(
			'SearchInfo',
			SEARCHINFO
			)
		)


class LPDHCP_SEARCH_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SEARCH_INFO
			)
		)


class DATA_DHCP_CLIENT_INFO_ARRAY(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO


class PTR_DHCP_CLIENT_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_ARRAY
			)
		)


class DHCP_CLIENT_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_ARRAY
			)
		)


class DATA_DHCP_OPTION_LIST(NDRUniConformantArray):
	item = DHCP_OPTION_VALUE


class PTR_DHCP_OPTION_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_OPTION_LIST
			)
		)


class DHCP_OPTION_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumOptions',
			DWORD
			),
			(
			'Options',
			PTR_DHCP_OPTION_LIST
			)
		)


class SCOPE_MIB_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Subnet',
			DHCP_IP_ADDRESS
			),
			(
			'NumAddressesInuse',
			DWORD
			),
			(
			'NumAddressesFree',
			DWORD
			),
			(
			'NumPendingOffers',
			DWORD
			)
		)


class LPSCOPE_MIB_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			SCOPE_MIB_INFO
			)
		)


class DHCP_MIB_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Discovers',
			DWORD
			),
			(
			'Offers',
			DWORD
			),
			(
			'Requests',
			DWORD
			),
			(
			'Acks',
			DWORD
			),
			(
			'Naks',
			DWORD
			),
			(
			'Declines',
			DWORD
			),
			(
			'Releases',
			DWORD
			),
			(
			'ServerStartTime',
			DATE_TIME
			),
			(
			'Scopes',
			DWORD
			),
			(
			'ScopeInfo',
			LPSCOPE_MIB_INFO
			)
		)


class LPDHCP_MIB_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MIB_INFO
			)
		)


class DHCP_OPTION_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Options',
			LPDHCP_OPTION
			)
		)


class LPDHCP_OPTION_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_ARRAY
			)
		)


class DHCP_SERVER_CONFIG_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'APIProtocolSupport',
			DWORD
			),
			(
			'DatabaseName',
			WCHAR_T
			),
			(
			'DatabasePath',
			WCHAR_T
			),
			(
			'BackupPath',
			WCHAR_T
			),
			(
			'BackupInterval',
			DWORD
			),
			(
			'DatabaseLoggingFlag',
			DWORD
			),
			(
			'RestoreFlag',
			DWORD
			),
			(
			'DatabaseCleanupInterval',
			DWORD
			),
			(
			'DebugFlag',
			DWORD
			)
		)


class LPDHCP_SERVER_CONFIG_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SERVER_CONFIG_INFO
			)
		)


class DHCP_SCAN_ITEM(NDRSTRUCT):
	align = 1
	structure = (
			(
			'IpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ScanFlag',
			DHCP_SCAN_FLAG
			)
		)


class LPDHCP_SCAN_ITEM(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SCAN_ITEM
			)
		)


class DATA_DHCP_SCAN_LIST(NDRUniConformantArray):
	item = DHCP_SCAN_ITEM


class PTR_DHCP_SCAN_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_SCAN_LIST
			)
		)


class DHCP_SCAN_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumScanItems',
			DWORD
			),
			(
			'ScanItems',
			PTR_DHCP_SCAN_LIST
			)
		)


class DHCP_IP_RESERVATION_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ReservedForClient',
			DHCP_CLIENT_UID
			),
			(
			'bAllowedClientTypes',
			BYTE
			)
		)


class LPDHCP_IP_RESERVATION_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RESERVATION_V4
			)
		)


class ELEMENT(NDRUNION):
	union = {DhcpIpRanges : (
		'IpRange',
		DHCP_IP_RANGE
		),DhcpSecondaryHosts : (
		'SecondaryHost',
		DHCP_HOST_INFO
		),DhcpReservedIps : (
		'ReservedIp',
		DHCP_IP_RESERVATION_V4
		),DhcpExcludedIpRanges : (
		'ExcludeIpRange',
		DHCP_IP_RANGE
		),DhcpIpUsedClusters : (
		'IpUsedCluster',
		DHCP_IP_CLUSTER
		)}


class DHCP_SUBNET_ELEMENT_DATA_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'Element',
			ELEMENT
			)
		)


class LPDHCP_SUBNET_ELEMENT_DATA_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4
			)
		)


class DHCP_CLIENT_INFO_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			)
		)


class LPDHCP_CLIENT_INFO_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_V4
			)
		)


class DATA_DHCP_CLIENT_INFO_ARRAY_V4(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_V4


class PTR_DHCP_CLIENT_INFO_ARRAY_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_ARRAY_V4
			)
		)


class DHCP_CLIENT_INFO_ARRAY_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_ARRAY_V4
			)
		)


class DHCP_SUPER_SCOPE_TABLE_ENTRY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SuperScopeNumber',
			DWORD
			),
			(
			'NextInSuperScope',
			DWORD
			),
			(
			'SuperScopeName',
			WCHAR_T
			)
		)


class LPDHCP_SUPER_SCOPE_TABLE_ENTRY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUPER_SCOPE_TABLE_ENTRY
			)
		)


class DATA_DHCP_SUPER_SCOPE_TABLE(NDRUniConformantArray):
	item = DHCP_SUPER_SCOPE_TABLE_ENTRY


class PTR_DHCP_SUPER_SCOPE_TABLE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_SUPER_SCOPE_TABLE
			)
		)


class DHCP_SUPER_SCOPE_TABLE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cEntries',
			DWORD
			),
			(
			'pEntries',
			PTR_DHCP_SUPER_SCOPE_TABLE
			)
		)


class DATA_DHCP_SERVER_CONFIG_INFO_V4(NDRUniConformantArray):
	item = WCHAR


class PTR_DHCP_SERVER_CONFIG_INFO_V4(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_SERVER_CONFIG_INFO_V4
			)
		)


class DHCP_SERVER_CONFIG_INFO_V4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'APIProtocolSupport',
			DWORD
			),
			(
			'DatabaseName',
			WCHAR_T
			),
			(
			'DatabasePath',
			WCHAR_T
			),
			(
			'BackupPath',
			WCHAR_T
			),
			(
			'BackupInterval',
			DWORD
			),
			(
			'DatabaseLoggingFlag',
			DWORD
			),
			(
			'RestoreFlag',
			DWORD
			),
			(
			'DatabaseCleanupInterval',
			DWORD
			),
			(
			'DebugFlag',
			DWORD
			),
			(
			'dwPingRetries',
			DWORD
			),
			(
			'cbBootTableString',
			DWORD
			),
			(
			'wszBootTableString',
			PTR_DHCP_SERVER_CONFIG_INFO_V4
			),
			(
			'fAuditLog',
			BOOL
			)
		)


class DATA_DHCP_SERVER_CONFIG_INFO_VQ(NDRUniConformantArray):
	item = WCHAR


class PTR_DHCP_SERVER_CONFIG_INFO_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_SERVER_CONFIG_INFO_VQ
			)
		)


class DHCP_SERVER_CONFIG_INFO_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'APIProtocolSupport',
			DWORD
			),
			(
			'DatabaseName',
			WCHAR_T
			),
			(
			'DatabasePath',
			WCHAR_T
			),
			(
			'BackupPath',
			WCHAR_T
			),
			(
			'BackupInterval',
			DWORD
			),
			(
			'DatabaseLoggingFlag',
			DWORD
			),
			(
			'RestoreFlag',
			DWORD
			),
			(
			'DatabaseCleanupInterval',
			DWORD
			),
			(
			'DebugFlag',
			DWORD
			),
			(
			'dwPingRetries',
			DWORD
			),
			(
			'cbBootTableString',
			DWORD
			),
			(
			'wszBootTableString',
			PTR_DHCP_SERVER_CONFIG_INFO_VQ
			),
			(
			'fAuditLog',
			BOOL
			),
			(
			'QuarantineOn',
			BOOL
			),
			(
			'QuarDefFail',
			DWORD
			),
			(
			'QuarRuntimeStatus',
			BOOL
			)
		)


class SCOPE_MIB_INFO_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Subnet',
			DHCP_IP_ADDRESS
			),
			(
			'NumAddressesInuse',
			DWORD
			),
			(
			'NumAddressesFree',
			DWORD
			),
			(
			'NumPendingOffers',
			DWORD
			),
			(
			'QtnNumLeases',
			DWORD
			),
			(
			'QtnPctQtnLeases',
			DWORD
			),
			(
			'QtnProbationLeases',
			DWORD
			),
			(
			'QtnNonQtnLeases',
			DWORD
			),
			(
			'QtnExemptLeases',
			DWORD
			),
			(
			'QtnCapableClients',
			DWORD
			)
		)


class LPSCOPE_MIB_INFO_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			SCOPE_MIB_INFO_VQ
			)
		)


class DHCP_MIB_INFO_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Discovers',
			DWORD
			),
			(
			'Offers',
			DWORD
			),
			(
			'Requests',
			DWORD
			),
			(
			'Acks',
			DWORD
			),
			(
			'Naks',
			DWORD
			),
			(
			'Declines',
			DWORD
			),
			(
			'Releases',
			DWORD
			),
			(
			'ServerStartTime',
			DATE_TIME
			),
			(
			'QtnNumLeases',
			DWORD
			),
			(
			'QtnPctQtnLeases',
			DWORD
			),
			(
			'QtnProbationLeases',
			DWORD
			),
			(
			'QtnNonQtnLeases',
			DWORD
			),
			(
			'QtnExemptLeases',
			DWORD
			),
			(
			'QtnCapableClients',
			DWORD
			),
			(
			'QtnIASErrors',
			DWORD
			),
			(
			'Scopes',
			DWORD
			),
			(
			'ScopeInfo',
			LPSCOPE_MIB_INFO_VQ
			)
		)


class LPDHCP_MIB_INFO_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MIB_INFO_VQ
			)
		)


class DHCP_CLIENT_INFO_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			),
			(
			'Status',
			QUARANTINESTATUS
			),
			(
			'ProbationEnds',
			DATE_TIME
			),
			(
			'QuarantineCapable',
			BOOL
			)
		)


class LPDHCP_CLIENT_INFO_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_VQ
			)
		)


class DATA_DHCP_CLIENT_INFO_ARRAY_VQ(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_VQ


class PTR_DHCP_CLIENT_INFO_ARRAY_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_ARRAY_VQ
			)
		)


class DHCP_CLIENT_INFO_ARRAY_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_ARRAY_VQ
			)
		)


class DHCP_SUBNET_INFO_VQ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'SubnetName',
			WCHAR_T
			),
			(
			'SubnetComment',
			WCHAR_T
			),
			(
			'PrimaryHost',
			DHCP_HOST_INFO
			),
			(
			'SubnetState',
			DHCP_SUBNET_STATE
			),
			(
			'QuarantineOn',
			DWORD
			),
			(
			'Reserved1',
			DWORD
			),
			(
			'Reserved2',
			DWORD
			),
			(
			'Reserved3',
			INT64
			),
			(
			'Reserved4',
			INT64
			)
		)


class LPDHCP_SUBNET_INFO_VQ(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_INFO_VQ
			)
		)


LPWSTR_RPC_STRING = WCHAR_T
DHCP_ATTRIB_ID = ULONG
PDHCP_ATTRIB_ID = ULONG
LPDHCP_ATTRIB_ID = ULONG
DHCP_OPTION_SCOPE_TYPE6 = DWORD__ENUM
DhcpDefaultOptions6 = 0
DhcpScopeOptions6 = 1
DhcpReservedOptions6 = 2
DHCP_SUBNET_ELEMENT_TYPE_V6 = DWORD__ENUM
Dhcpv6IpRanges = 0
Dhcpv6ReservedIps = 1
DHCP_SEARCH_INFO_TYPE_V6 = DWORD__ENUM
Dhcpv6ClientIpAddress = 0
Dhcpv6ClientDUID = 1
class DHCP_IPV6_ADDRESS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'HighOrderBits',
			ULONGLONG
			),
			(
			'LowOrderBits',
			ULONGLONG
			)
		)


class LPDHCP_IPV6_ADDRESS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IPV6_ADDRESS
			)
		)


class PDHCP_IPV6_ADDRESS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IPV6_ADDRESS
			)
		)


class DHCP_CLIENT_INFO_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			)
		)


class LPDHCP_CLIENT_INFO_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_V5
			)
		)


class DATA_DHCP_CLIENT_INFO_ARRAY_V5(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_V5


class PTR_DHCP_CLIENT_INFO_ARRAY_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_ARRAY_V5
			)
		)


class DHCP_CLIENT_INFO_ARRAY_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_ARRAY_V5
			)
		)


class DHCP_MSCOPE_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'MScopeComment',
			WCHAR_T
			),
			(
			'MScopeId',
			DWORD
			),
			(
			'MScopeAddressPolicy',
			DWORD
			),
			(
			'PrimaryHost',
			DHCP_HOST_INFO
			),
			(
			'MScopeState',
			DHCP_SUBNET_STATE
			),
			(
			'MScopeFlags',
			DWORD
			),
			(
			'ExpiryTime',
			DATE_TIME
			),
			(
			'LangTag',
			WCHAR_T
			),
			(
			'TTL',
			BYTE
			)
		)


class LPDHCP_MSCOPE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MSCOPE_INFO
			)
		)


class DATA_DHCP_MSCOPE_TABLE(NDRUniConformantArray):
	item = WCHAR_T


class PTR_DHCP_MSCOPE_TABLE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_MSCOPE_TABLE
			)
		)


class DHCP_MSCOPE_TABLE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'pMScopeNames',
			PTR_DHCP_MSCOPE_TABLE
			)
		)


class DHCP_MCLIENT_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'MScopeId',
			DWORD
			),
			(
			'ClientId',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientLeaseStarts',
			DATE_TIME
			),
			(
			'ClientLeaseEnds',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'AddressFlags',
			DWORD
			),
			(
			'AddressState',
			BYTE
			)
		)


class LPDHCP_MCLIENT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MCLIENT_INFO
			)
		)


class DATA_DHCP_MCLIENT_INFO_ARRAY(NDRUniConformantArray):
	item = LPDHCP_MCLIENT_INFO


class PTR_DHCP_MCLIENT_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_MCLIENT_INFO_ARRAY
			)
		)


class DHCP_MCLIENT_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_MCLIENT_INFO_ARRAY
			)
		)


class DHCP_RESERVED_SCOPE6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ReservedIpSubnetAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class LPDHCP_RESERVED_SCOPE6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_RESERVED_SCOPE6
			)
		)


class SCOPEINFO(NDRUNION):
	union = {DhcpScopeOptions6 : (
		'SubnetScopeInfo',
		DHCP_IPV6_ADDRESS
		),DhcpReservedOptions6 : (
		'ReservedScopeInfo',
		DHCP_RESERVED_SCOPE6
		)}


class DHCP_OPTION_SCOPE_INFO6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ScopeType',
			DHCP_OPTION_SCOPE_TYPE6
			),
			(
			'ScopeInfo',
			SCOPEINFO
			)
		)


class LPDHCP_OPTION_SCOPE_INFO6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_OPTION_SCOPE_INFO6
			)
		)


class DHCP_CLASS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClassName',
			WCHAR_T
			),
			(
			'ClassComment',
			WCHAR_T
			),
			(
			'ClassDataLength',
			DWORD
			),
			(
			'IsVendor',
			BOOL
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassData',
			LPBYTE
			)
		)


class LPDHCP_CLASS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLASS_INFO
			)
		)


class DHCP_CLASS_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Classes',
			LPDHCP_CLASS_INFO
			)
		)


class LPDHCP_CLASS_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLASS_INFO_ARRAY
			)
		)


class VENDOROPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Option',
			DHCP_OPTION
			),
			(
			'VendorName',
			WCHAR_T
			),
			(
			'ClassName',
			WCHAR_T
			)
		)


class DHCP_ALL_OPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'NonVendorOptions',
			LPDHCP_OPTION_ARRAY
			),
			(
			'NumVendorOptions',
			DWORD
			),
			(
			'VENDOROPTIONS',
			VENDOROPTIONS
			)
		)


class LPDHCP_ALL_OPTIONS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ALL_OPTIONS
			)
		)


class OPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClassName',
			WCHAR_T
			),
			(
			'VendorName',
			WCHAR_T
			),
			(
			'IsVendor',
			BOOL
			),
			(
			'OptionsArray',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class DHCP_ALL_OPTION_VALUES(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'NumElements',
			DWORD
			),
			(
			'OPTIONS',
			OPTIONS
			)
		)


class LPDHCP_ALL_OPTION_VALUES(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ALL_OPTION_VALUES
			)
		)


class MSCOPE_MIB_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'MScopeId',
			DWORD
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'NumAddressesInuse',
			DWORD
			),
			(
			'NumAddressesFree',
			DWORD
			),
			(
			'NumPendingOffers',
			DWORD
			)
		)


class LPMSCOPE_MIB_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			MSCOPE_MIB_INFO
			)
		)


class DHCP_MCAST_MIB_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Discovers',
			DWORD
			),
			(
			'Offers',
			DWORD
			),
			(
			'Requests',
			DWORD
			),
			(
			'Renews',
			DWORD
			),
			(
			'Acks',
			DWORD
			),
			(
			'Naks',
			DWORD
			),
			(
			'Releases',
			DWORD
			),
			(
			'Informs',
			DWORD
			),
			(
			'ServerStartTime',
			DATE_TIME
			),
			(
			'Scopes',
			DWORD
			),
			(
			'ScopeInfo',
			LPMSCOPE_MIB_INFO
			)
		)


class LPDHCP_MCAST_MIB_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MCAST_MIB_INFO
			)
		)


class U0(NDRUNION):
	union = {DHCP_ATTRIB_TYPE_BOOL : (
		'DhcpAttribBool',
		BOOL
		),DHCP_ATTRIB_TYPE_ULONG : (
		'DhcpAttribUlong',
		ULONG
		)}


class DHCP_ATTRIB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'DhcpAttribId',
			DHCP_ATTRIB_ID
			),
			(
			'DhcpAttribType',
			ULONG
			),
			(
			'u0',
			U0
			)
		)


class PDHCP_ATTRIB(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ATTRIB
			)
		)


class LPDHCP_ATTRIB(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ATTRIB
			)
		)


class DHCP_ATTRIB_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			ULONG
			),
			(
			'DhcpAttribs',
			LPDHCP_ATTRIB
			)
		)


class PDHCP_ATTRIB_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ATTRIB_ARRAY
			)
		)


class LPDHCP_ATTRIB_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ATTRIB_ARRAY
			)
		)


class ELEMENT(NDRUNION):
	union = {DhcpIpRanges : (
		'IpRange',
		DHCP_BOOTP_IP_RANGE
		),DhcpSecondaryHosts : (
		'SecondaryHost',
		DHCP_HOST_INFO
		),DhcpReservedIps : (
		'ReservedIp',
		DHCP_IP_RESERVATION_V4
		),DhcpExcludedIpRanges : (
		'ExcludeIpRange',
		DHCP_IP_RANGE
		),DhcpIpUsedClusters : (
		'IpUsedCluster',
		DHCP_IP_CLUSTER
		)}


class DHCP_SUBNET_ELEMENT_DATA_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'Element',
			ELEMENT
			)
		)


class LPDHCP_SUBNET_ELEMENT_DATA_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_DATA_V5
			)
		)


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_SUBNET_ELEMENT_DATA_V5
			)
		)


class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5
			)
		)


class DHCP_BIND_ELEMENT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			ULONG
			),
			(
			'fBoundToDHCPServer',
			BOOL
			),
			(
			'AdapterPrimaryAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AdapterSubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'IfDescription',
			WCHAR_T
			),
			(
			'IfIdSize',
			ULONG
			),
			(
			'IfId',
			LPBYTE
			)
		)


class LPDHCP_BIND_ELEMENT(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_BIND_ELEMENT
			)
		)


class DHCP_BIND_ELEMENT_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_BIND_ELEMENT
			)
		)


class LPDHCP_BIND_ELEMENT_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_BIND_ELEMENT_ARRAY
			)
		)


class DHCP_SERVER_SPECIFIC_STRINGS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'DefaultVendorClassName',
			WCHAR_T
			),
			(
			'DefaultUserClassName',
			WCHAR_T
			)
		)


class LPDHCP_SERVER_SPECIFIC_STRINGS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SERVER_SPECIFIC_STRINGS
			)
		)


class SCOPE_MIB_INFO_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Subnet',
			DHCP_IP_ADDRESS
			),
			(
			'NumAddressesInuse',
			DWORD
			),
			(
			'NumAddressesFree',
			DWORD
			),
			(
			'NumPendingOffers',
			DWORD
			)
		)


class LPSCOPE_MIB_INFO_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			SCOPE_MIB_INFO_V5
			)
		)


class DHCP_MIB_INFO_V5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Discovers',
			DWORD
			),
			(
			'Offers',
			DWORD
			),
			(
			'Requests',
			DWORD
			),
			(
			'Acks',
			DWORD
			),
			(
			'Naks',
			DWORD
			),
			(
			'Declines',
			DWORD
			),
			(
			'Releases',
			DWORD
			),
			(
			'ServerStartTime',
			DATE_TIME
			),
			(
			'QtnNumLeases',
			DWORD
			),
			(
			'QtnPctQtnLeases',
			DWORD
			),
			(
			'QtnProbationLeases',
			DWORD
			),
			(
			'QtnNonQtnLeases',
			DWORD
			),
			(
			'QtnExemptLeases',
			DWORD
			),
			(
			'QtnCapableClients',
			DWORD
			),
			(
			'QtnIASErrors',
			DWORD
			),
			(
			'DelayedOffers',
			DWORD
			),
			(
			'ScopesWithDelayedOffers',
			DWORD
			),
			(
			'Scopes',
			DWORD
			),
			(
			'ScopeInfo',
			LPSCOPE_MIB_INFO_V5
			)
		)


class LPDHCP_MIB_INFO_V5(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MIB_INFO_V5
			)
		)


DHCP_FILTER_LIST_TYPE = DWORD__ENUM
Deny = 0
class DHCP_ADDR_PATTERN(NDRSTRUCT):
	align = 1
	structure = (
			(
			'MatchHWType',
			BOOL
			),
			(
			'HWType',
			BYTE
			),
			(
			'IsWildcard',
			BOOL
			),
			(
			'Length',
			BYTE
			),
			(
			'Pattern',
			BYTE
			)
		)


class LPDHCP_ADDR_PATTERN(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ADDR_PATTERN
			)
		)


class DHCP_FILTER_ADD_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AddrPatt',
			DHCP_ADDR_PATTERN
			),
			(
			'Comment',
			WCHAR_T
			),
			(
			'ListType',
			DHCP_FILTER_LIST_TYPE
			)
		)


class LPDHCP_FILTER_ADD_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FILTER_ADD_INFO
			)
		)


class DHCP_FILTER_GLOBAL_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EnforceAllowList',
			BOOL
			),
			(
			'EnforceDenyList',
			BOOL
			)
		)


class LPDHCP_FILTER_GLOBAL_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FILTER_GLOBAL_INFO
			)
		)


class DHCP_FILTER_RECORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AddrPatt',
			DHCP_ADDR_PATTERN
			),
			(
			'Comment',
			WCHAR_T
			)
		)


class LPDHCP_FILTER_RECORD(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FILTER_RECORD
			)
		)


class DHCP_FILTER_ENUM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'pEnumRecords',
			LPDHCP_FILTER_RECORD
			)
		)


class LPDHCP_FILTER_ENUM_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FILTER_ENUM_INFO
			)
		)


class DHCP_SUBNET_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'Prefix',
			ULONG
			),
			(
			'Preference',
			USHORT
			),
			(
			'SubnetName',
			WCHAR_T
			),
			(
			'SubnetComment',
			WCHAR_T
			),
			(
			'State',
			DWORD
			),
			(
			'ScopeId',
			DWORD
			)
		)


class PDHCP_SUBNET_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_INFO_V6
			)
		)


class LPDHCP_SUBNET_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_INFO_V6
			)
		)


class DHCPV6_IP_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_IPV6_ADDRESS
			)
		)


class LPDHCPV6_IP_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_IP_ARRAY
			)
		)


class DHCP_IP_RANGE_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'StartAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'EndAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class LPDHCP_IP_RANGE_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RANGE_V6
			)
		)


class DHCP_IP_RESERVATION_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ReservedForClient',
			DHCP_CLIENT_UID
			),
			(
			'InterfaceId',
			DWORD
			)
		)


class LPDHCP_IP_RESERVATION_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RESERVATION_V6
			)
		)


class ELEMENT(NDRUNION):
	union = {Dhcpv6IpRanges : (
		'IpRange',
		DHCP_IP_RANGE_V6
		),Dhcpv6ReservedIps : (
		'ReservedIp',
		DHCP_IP_RESERVATION_V6
		),Dhcpv6ExcludedIpRanges : (
		'ExcludeIpRange',
		DHCP_IP_RANGE_V6
		)}


class DHCP_SUBNET_ELEMENT_DATA_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ElementType',
			DHCP_SUBNET_ELEMENT_TYPE_V6
			),
			(
			'Element',
			ELEMENT
			)
		)


class LPDHCP_SUBNET_ELEMENT_DATA_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_DATA_V6
			)
		)


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_SUBNET_ELEMENT_DATA_V6
			)
		)


class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6
			)
		)


DHCP_RESUME_IPV6_HANDLE = DHCP_IPV6_ADDRESS
class DHCP_HOST_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'IpAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'NetBiosName',
			WCHAR_T
			),
			(
			'HostName',
			WCHAR_T
			)
		)


class LPDHCP_HOST_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_HOST_INFO_V6
			)
		)


class DHCP_CLIENT_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ClientDUID',
			DHCP_CLIENT_UID
			),
			(
			'AddressType',
			DWORD
			),
			(
			'IAID',
			DWORD
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientValidLeaseExpires',
			DATE_TIME
			),
			(
			'ClientPrefLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO_V6
			)
		)


class LPDHCP_CLIENT_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_V6
			)
		)


class DATA_DHCP_CLIENT_INFO_ARRAY_V6(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_V6


class PTR_DHCP_CLIENT_INFO_ARRAY_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_ARRAY_V6
			)
		)


class DHCP_CLIENT_INFO_ARRAY_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_ARRAY_V6
			)
		)


class DHCP_SERVER_CONFIG_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'UnicastFlag',
			BOOL
			),
			(
			'RapidCommitFlag',
			BOOL
			),
			(
			'PreferredLifetime',
			DWORD
			),
			(
			'ValidLifetime',
			DWORD
			),
			(
			'T1',
			DWORD
			),
			(
			'T2',
			DWORD
			),
			(
			'PreferredLifetimeIATA',
			DWORD
			),
			(
			'ValidLifetimeIATA',
			DWORD
			),
			(
			'fAuditLog',
			BOOL
			)
		)


class LPDHCP_SERVER_CONFIG_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SERVER_CONFIG_INFO_V6
			)
		)


class SCOPE_MIB_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Subnet',
			DHCP_IPV6_ADDRESS
			),
			(
			'NumAddressesInuse',
			ULONGLONG
			),
			(
			'NumAddressesFree',
			ULONGLONG
			),
			(
			'NumPendingAdvertises',
			ULONGLONG
			)
		)


class LPSCOPE_MIB_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			SCOPE_MIB_INFO_V6
			)
		)


class DHCP_MIB_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Solicits',
			DWORD
			),
			(
			'Advertises',
			DWORD
			),
			(
			'Requests',
			DWORD
			),
			(
			'Renews',
			DWORD
			),
			(
			'Rebinds',
			DWORD
			),
			(
			'Replies',
			DWORD
			),
			(
			'Confirms',
			DWORD
			),
			(
			'Declines',
			DWORD
			),
			(
			'Releases',
			DWORD
			),
			(
			'Informs',
			DWORD
			),
			(
			'ServerStartTime',
			DATE_TIME
			),
			(
			'Scopes',
			DWORD
			),
			(
			'ScopeInfo',
			LPSCOPE_MIB_INFO_V6
			)
		)


class LPDHCP_MIB_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_MIB_INFO_V6
			)
		)


class DHCPV6_BIND_ELEMENT(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			ULONG
			),
			(
			'fBoundToDHCPServer',
			BOOL
			),
			(
			'AdapterPrimaryAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'AdapterSubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'IfDescription',
			WCHAR_T
			),
			(
			'IpV6IfIndex',
			DWORD
			),
			(
			'IfIdSize',
			ULONG
			),
			(
			'IfId',
			LPBYTE
			)
		)


class LPDHCPV6_BIND_ELEMENT(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_BIND_ELEMENT
			)
		)


class DHCPV6_BIND_ELEMENT_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCPV6_BIND_ELEMENT
			)
		)


class LPDHCPV6_BIND_ELEMENT_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_BIND_ELEMENT_ARRAY
			)
		)


class SEARCHINFO(NDRUNION):
	union = {Dhcpv6ClientIpAddress : (
		'ClientIpAddress',
		DHCP_IPV6_ADDRESS
		),Dhcpv6ClientDUID : (
		'ClientDUID',
		DHCP_CLIENT_UID
		),Dhcpv6ClientName : (
		'ClientName',
		WCHAR_T
		)}


class DHCP_SEARCH_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SearchType',
			DHCP_SEARCH_INFO_TYPE_V6
			),
			(
			'SearchInfo',
			SEARCHINFO
			)
		)


class LPDHCP_SEARCH_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_SEARCH_INFO_V6
			)
		)


class DHCP_CLASS_INFO_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClassName',
			WCHAR_T
			),
			(
			'ClassComment',
			WCHAR_T
			),
			(
			'ClassDataLength',
			DWORD
			),
			(
			'IsVendor',
			BOOL
			),
			(
			'EnterpriseNumber',
			DWORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassData',
			LPBYTE
			)
		)


class LPDHCP_CLASS_INFO_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLASS_INFO_V6
			)
		)


class DHCP_CLASS_INFO_ARRAY_V6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Classes',
			LPDHCP_CLASS_INFO_V6
			)
		)


class LPDHCP_CLASS_INFO_ARRAY_V6(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLASS_INFO_ARRAY_V6
			)
		)


class DHCP_CLIENT_FILTER_STATUS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			),
			(
			'Status',
			QUARANTINESTATUS
			),
			(
			'ProbationEnds',
			DATE_TIME
			),
			(
			'QuarantineCapable',
			BOOL
			),
			(
			'FilterStatus',
			DWORD
			)
		)


class LPDHCP_CLIENT_FILTER_STATUS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_FILTER_STATUS_INFO
			)
		)


class DATA_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(NDRUniConformantArray):
	item = LPDHCP_CLIENT_FILTER_STATUS_INFO


class PTR_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY
			)
		)


class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY
			)
		)


DHCP_FAILOVER_MODE = DWORD__ENUM
LoadBalance = 0
HotStandby = 1
DHCP_FAILOVER_SERVER = DWORD__ENUM
PrimaryServer = 0
SecondaryServer = 1
FSM_STATE = DWORD__ENUM
NO_STATE = 0
INIT = 0
STARTUP = 0
NORMAL = 0
COMMUNICATION_INT = 0
PARTNER_DOWN = 0
POTENTIAL_CONFLICT = 0
CONFLICT_DONE = 0
RESOLUTION_INT = 0
RECOVER = 0
RECOVER_WAIT = 0
RECOVER_DONE = 0
class DHCP_FAILOVER_RELATIONSHIP(NDRSTRUCT):
	align = 1
	structure = (
			(
			'primaryServer',
			DHCP_IP_ADDRESS
			),
			(
			'secondaryServer',
			DHCP_IP_ADDRESS
			),
			(
			'mode',
			DHCP_FAILOVER_MODE
			),
			(
			'serverType',
			DHCP_FAILOVER_SERVER
			),
			(
			'state',
			FSM_STATE
			),
			(
			'prevState',
			FSM_STATE
			),
			(
			'mclt',
			DWORD
			),
			(
			'safePeriod',
			DWORD
			),
			(
			'relationshipName',
			WCHAR_T
			),
			(
			'primaryServerName',
			WCHAR_T
			),
			(
			'secondaryServerName',
			WCHAR_T
			),
			(
			'pScopes',
			LPDHCP_IP_ARRAY
			),
			(
			'percentage',
			BYTE
			),
			(
			'pSharedSecret',
			WCHAR_T
			)
		)


class LPDHCP_FAILOVER_RELATIONSHIP(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FAILOVER_RELATIONSHIP
			)
		)


class DHCP_FAILOVER_RELATIONSHIP_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'numElements',
			DWORD
			),
			(
			'pRelationships',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class LPDHCP_FAILOVER_RELATIONSHIP_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FAILOVER_RELATIONSHIP_ARRAY
			)
		)


class DHCP_FAILOVER_STATISTICS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'numAddr',
			DWORD
			),
			(
			'addrFree',
			DWORD
			),
			(
			'addrInUse',
			DWORD
			),
			(
			'partnerAddrFree',
			DWORD
			),
			(
			'thisAddrFree',
			DWORD
			),
			(
			'partnerAddrInUse',
			DWORD
			),
			(
			'thisAddrInUse',
			DWORD
			)
		)


class LPDHCP_FAILOVER_STATISTICS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_FAILOVER_STATISTICS
			)
		)


class DHCPV4_FAILOVER_CLIENT_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			),
			(
			'Status',
			QUARANTINESTATUS
			),
			(
			'ProbationEnds',
			DATE_TIME
			),
			(
			'QuarantineCapable',
			BOOL
			),
			(
			'SentPotExpTime',
			DWORD
			),
			(
			'AckPotExpTime',
			DWORD
			),
			(
			'RecvPotExpTime',
			DWORD
			),
			(
			'StartTime',
			DWORD
			),
			(
			'CltLastTransTime',
			DWORD
			),
			(
			'LastBndUpdTime',
			DWORD
			),
			(
			'bndMsgStatus',
			DWORD
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'flags',
			BYTE
			)
		)


class LPDHCPV4_FAILOVER_CLIENT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV4_FAILOVER_CLIENT_INFO
			)
		)


class DHCP_IP_RESERVATION_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReservedIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ReservedForClient',
			DHCP_CLIENT_UID
			),
			(
			'ReservedClientName',
			WCHAR_T
			),
			(
			'ReservedClientDesc',
			WCHAR_T
			),
			(
			'bAllowedClientTypes',
			BYTE
			),
			(
			'fOptionsPresent',
			BYTE
			)
		)


class LPDHCP_IP_RESERVATION_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RESERVATION_INFO
			)
		)


class DATA_DHCP_RESERVATION_INFO_ARRAY(NDRUniConformantArray):
	item = LPDHCP_IP_RESERVATION_INFO


class PTR_DHCP_RESERVATION_INFO_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_RESERVATION_INFO_ARRAY
			)
		)


class DHCP_RESERVATION_INFO_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			PTR_DHCP_RESERVATION_INFO_ARRAY
			)
		)


class OPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'VendorName',
			WCHAR_T
			),
			(
			'IsVendor',
			BOOL
			),
			(
			'OptionsArray',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class DHCP_ALL_OPTION_VALUES_PB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'NumElements',
			DWORD
			),
			(
			'OPTIONS',
			OPTIONS
			)
		)


class LPDHCP_ALL_OPTION_VALUES_PB(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_ALL_OPTION_VALUES_PB
			)
		)


DHCP_POL_ATTR_TYPE = DWORD__ENUM
DhcpAttrHWAddr = 0
DhcpAttrOption = 1
DhcpAttrSubOption = 2
DhcpAttrFqdn = 3
DhcpAttrFqdnSingleLabel = 4
DHCP_POL_COMPARATOR = DWORD__ENUM
DhcpCompEqual = 0
DhcpCompNotEqual = 1
DhcpCompBeginsWith = 2
DhcpCompNotBeginWith = 3
DhcpCompEndsWith = 4
DHCP_POL_LOGIC_OPER = DWORD__ENUM
DhcpLogicalOr = 0
DhcpLogicalAnd = 1
DHCP_POLICY_FIELDS_TO_UPDATE = DWORD__ENUM
DhcpUpdatePolicyName = 1
DhcpUpdatePolicyOrder = 2
DhcpUpdatePolicyExpr = 4
DhcpUpdatePolicyRanges = 8
DhcpUpdatePolicyDescr = 16
DhcpUpdatePolicyStatus = 32
DhcpUpdatePolicyDnsSuffix = 64
class DHCP_POL_COND(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ParentExpr',
			DWORD
			),
			(
			'Type',
			DHCP_POL_ATTR_TYPE
			),
			(
			'OptionID',
			DWORD
			),
			(
			'SubOptionID',
			DWORD
			),
			(
			'VendorName',
			WCHAR_T
			),
			(
			'Operator',
			DHCP_POL_COMPARATOR
			),
			(
			'Value',
			LPBYTE
			),
			(
			'ValueLength',
			DWORD
			)
		)


class PDHCP_POL_COND(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_COND
			)
		)


class LPDHCP_POL_COND(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_COND
			)
		)


class DHCP_POL_COND_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_POL_COND
			)
		)


class PDHCP_POL_COND_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_COND_ARRAY
			)
		)


class LPDHCP_POL_COND_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_COND_ARRAY
			)
		)


class DHCP_POL_EXPR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ParentExpr',
			DWORD
			),
			(
			'Operator',
			DHCP_POL_LOGIC_OPER
			)
		)


class PDHCP_POL_EXPR(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_EXPR
			)
		)


class LPDHCP_POL_EXPR(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_EXPR
			)
		)


class DHCP_POL_EXPR_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_POL_EXPR
			)
		)


class PDHCP_POL_EXPR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_EXPR_ARRAY
			)
		)


class LPDHCP_POL_EXPR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POL_EXPR_ARRAY
			)
		)


class DHCP_IP_RANGE_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_IP_RANGE
			)
		)


class PDHCP_IP_RANGE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RANGE_ARRAY
			)
		)


class LPDHCP_IP_RANGE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_IP_RANGE_ARRAY
			)
		)


class DHCP_POLICY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'IsGlobalPolicy',
			BOOL
			),
			(
			'Subnet',
			DHCP_IP_ADDRESS
			),
			(
			'ProcessingOrder',
			DWORD
			),
			(
			'Conditions',
			LPDHCP_POL_COND_ARRAY
			),
			(
			'Expressions',
			LPDHCP_POL_EXPR_ARRAY
			),
			(
			'Ranges',
			LPDHCP_IP_RANGE_ARRAY
			),
			(
			'Description',
			WCHAR_T
			),
			(
			'Enabled',
			BOOL
			)
		)


class PDHCP_POLICY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY
			)
		)


class LPDHCP_POLICY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY
			)
		)


class DHCP_POLICY_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_POLICY
			)
		)


class PDHCP_POLICY_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_ARRAY
			)
		)


class LPDHCP_POLICY_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_ARRAY
			)
		)


class DHCPV6_STATELESS_PARAMS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Status',
			BOOL
			),
			(
			'PurgeInterval',
			DWORD
			)
		)


class PDHCPV6_STATELESS_PARAMS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_PARAMS
			)
		)


class LPDHCPV6_STATELESS_PARAMS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_PARAMS
			)
		)


class DHCPV6_STATELESS_SCOPE_STATS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'NumStatelessClientsAdded',
			ULONGLONG
			),
			(
			'NumStatelessClientsRemoved',
			ULONGLONG
			)
		)


class PDHCPV6_STATELESS_SCOPE_STATS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_SCOPE_STATS
			)
		)


class LPDHCPV6_STATELESS_SCOPE_STATS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_SCOPE_STATS
			)
		)


class DHCPV6_STATELESS_STATS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumScopes',
			DWORD
			),
			(
			'ScopeStats',
			LPDHCPV6_STATELESS_SCOPE_STATS
			)
		)


class PDHCPV6_STATELESS_STATS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_STATS
			)
		)


class LPDHCPV6_STATELESS_STATS(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCPV6_STATELESS_STATS
			)
		)


class DHCP_CLIENT_INFO_PB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			),
			(
			'Status',
			QUARANTINESTATUS
			),
			(
			'ProbationEnds',
			DATE_TIME
			),
			(
			'QuarantineCapable',
			BOOL
			),
			(
			'FilterStatus',
			DWORD
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class LPDHCP_CLIENT_INFO_PB(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_PB
			)
		)


class DATA_DHCP_CLIENT_INFO_PB_ARRAY(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_PB


class PTR_DHCP_CLIENT_INFO_PB_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_PB_ARRAY
			)
		)


class DHCP_CLIENT_INFO_PB_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_PB_ARRAY
			)
		)


DHCP_PROPERTY_TYPE = DWORD__ENUM
DhcpPropTypeByte = 0
DhcpPropTypeWord = 1
DhcpPropTypeDword = 2
DhcpPropTypeString = 3
DhcpPropTypeBinary = 4
DHCP_PROPERTY_ID = DWORD__ENUM
DhcpPropIdPolicyDnsSuffix = 0
DhcpPropIdClientAddressStateEx = 1
class VALUE(NDRUNION):
	union = {DhcpPropTypeByte : (
		'ByteValue',
		BYTE
		),DhcpPropTypeWord : (
		'WordValue',
		WORD
		),DhcpPropTypeDword : (
		'DWordValue',
		DWORD
		),DhcpPropTypeString : (
		'StringValue',
		WCHAR_T
		),DhcpPropTypeBinary : (
		'BinaryValue',
		DHCP_BINARY_DATA
		)}


class DHCP_PROPERTY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ID',
			DHCP_PROPERTY_ID
			),
			(
			'Type',
			DHCP_PROPERTY_TYPE
			),
			(
			'Value',
			VALUE
			)
		)


class PDHCP_PROPERTY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_PROPERTY
			)
		)


class LPDHCP_PROPERTY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_PROPERTY
			)
		)


class DHCP_PROPERTY_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_PROPERTY
			)
		)


class PDHCP_PROPERTY_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_PROPERTY_ARRAY
			)
		)


class LPDHCP_PROPERTY_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_PROPERTY_ARRAY
			)
		)


class DHCP_CLIENT_INFO_EX(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetMask',
			DHCP_IP_MASK
			),
			(
			'ClientHardwareAddress',
			DHCP_CLIENT_UID
			),
			(
			'ClientName',
			WCHAR_T
			),
			(
			'ClientComment',
			WCHAR_T
			),
			(
			'ClientLeaseExpires',
			DATE_TIME
			),
			(
			'OwnerHost',
			DHCP_HOST_INFO
			),
			(
			'bClientType',
			BYTE
			),
			(
			'AddressState',
			BYTE
			),
			(
			'Status',
			QUARANTINESTATUS
			),
			(
			'ProbationEnds',
			DATE_TIME
			),
			(
			'QuarantineCapable',
			BOOL
			),
			(
			'FilterStatus',
			DWORD
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Properties',
			LPDHCP_PROPERTY_ARRAY
			)
		)


class LPDHCP_CLIENT_INFO_EX(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_CLIENT_INFO_EX
			)
		)


class DATA_DHCP_CLIENT_INFO_EX_ARRAY(NDRUniConformantArray):
	item = LPDHCP_CLIENT_INFO_EX


class PTR_DHCP_CLIENT_INFO_EX_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DHCP_CLIENT_INFO_EX_ARRAY
			)
		)


class DHCP_CLIENT_INFO_EX_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Clients',
			PTR_DHCP_CLIENT_INFO_EX_ARRAY
			)
		)


class DHCP_POLICY_EX(NDRSTRUCT):
	align = 1
	structure = (
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'IsGlobalPolicy',
			BOOL
			),
			(
			'Subnet',
			DHCP_IP_ADDRESS
			),
			(
			'ProcessingOrder',
			DWORD
			),
			(
			'Conditions',
			LPDHCP_POL_COND_ARRAY
			),
			(
			'Expressions',
			LPDHCP_POL_EXPR_ARRAY
			),
			(
			'Ranges',
			LPDHCP_IP_RANGE_ARRAY
			),
			(
			'Description',
			WCHAR_T
			),
			(
			'Enabled',
			BOOL
			),
			(
			'Properties',
			LPDHCP_PROPERTY_ARRAY
			)
		)


class PDHCP_POLICY_EX(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_EX
			)
		)


class LPDHCP_POLICY_EX(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_EX
			)
		)


class DHCP_POLICY_EX_ARRAY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'NumElements',
			DWORD
			),
			(
			'Elements',
			LPDHCP_POLICY_EX
			)
		)


class PDHCP_POLICY_EX_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_EX_ARRAY
			)
		)


class LPDHCP_POLICY_EX_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DHCP_POLICY_EX_ARRAY
			)
		)


#################################################################################
#CONSTANTS
#################################################################################
DEBUG_ADDRESS = 0x00000001
DEBUG_CLIENT = 0x00000002
DEBUG_PARAMETERS = 0x00000004
DEBUG_OPTIONS = 0x00000008
DEBUG_ERRORS = 0x00000010
DEBUG_STOC = 0x00000020
DEBUG_INIT = 0x00000040
DEBUG_SCAVENGER = 0x00000080
DEBUG_TIMESTAMP = 0x00000100
DEBUG_APIS = 0x00000200
DEBUG_REGISTRY = 0x00000400
DEBUG_JET = 0x00000800
DEBUG_THREADPOOL = 0x00001000
DEBUG_AUDITLOG = 0x00002000
DEBUG_QUARANTINE = 0x00004000
DEBUG_MISC = 0x00008000
DEBUG_MESSAGE = 0x00010000
DEBUG_API_VERBOSE = 0x00020000
DEBUG_DNS = 0x00040000
DEBUG_MSTOC = 0x00080000
DEBUG_TRACK = 0x00100000
DEBUG_ROGUE = 0x00200000
DEBUG_PNP = 0x00400000
DEBUG_PERF = 0x01000000
DEBUG_ALLOC = 0x02000000
DEBUG_PING = 0x04000000
DEBUG_THREAD = 0x08000000
DEBUG_TRACE = 0x10000000
DEBUG_TRACE_CALLS = 0x20000000
DEBUG_STARTUP_BRK = 0x40000000
DEBUG_LOG_IN_FILE = 0x80000000
DHCP_SERVER_USE_RPC_OVER_TCPIP = 0x1
DHCP_SERVER_USE_RPC_OVER_NP = 0x2
DHCP_SERVER_USE_RPC_OVER_LPC = 0x4
DHCP_SERVER_USE_RPC_OVER_ALL = ( DHCP_SERVER_USE_RPC_OVER_TCPIP | DHCP_SERVER_USE_RPC_OVER_NP | DHCP_SERVER_USE_RPC_OVER_LPC )
SET_APIPROTOCOLSUPPORT = 0x00000001
SET_DATABASENAME = 0x00000002
SET_DATABASEPATH = 0x00000004
SET_BACKUPPATH = 0x00000008
SET_BACKUPINTERVAL = 0x00000010
SET_DATABASELOGGINGFLAG = 0x00000020
SET_RESTOREFLAG = 0x00000040
SET_DATABASECLEANUPINTERVAL = 0x00000080
SET_DEBUGFLAG = 0x00000100
SET_PINGRETRIES = 0x00000200
SET_BOOTFILETABLE = 0x00000400
SET_AUDITLOGSTATE = 0x00000800
SET_QUARANTINEON = 0x00001000
SET_QUARANTINEDEFFAIL = 0x00002000
CLIENT_TYPE_UNSPECIFIED = 0x0
CLIENT_TYPE_DHCP = 0x1
CLIENT_TYPE_BOOTP = 0x2
CLIENT_TYPE_BOTH = ( CLIENT_TYPE_DHCP | CLIENT_TYPE_BOOTP )
CLIENT_TYPE_RESERVATION_FLAG = 0x4
CLIENT_TYPE_NONE = 0x64
ADDRESS_STATE_OFFERED = 0
ADDRESS_STATE_ACTIVE = 1
ADDRESS_STATE_DECLINED = 2
ADDRESS_STATE_DOOM = 3
DHCP_ATTRIB_TYPE_BOOL = 0x01
DHCP_ATTRIB_TYPE_ULONG = 0x02
DHCP_ENDPOINT_FLAG_CANT_MODIFY = 0x01
MAX_PATTERN_LENGTH = 255
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#dhcpsrv Definition
#################################################################################
MSRPC_UUID_DHCPSRV = uuidtup_to_bin(('6BFFD098-A112-3610-9833-46C3F874532D','0.0'))
class R_DhcpCreateSubnet(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO
			)
		)


class R_DhcpCreateSubnetResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO
			)
		)


class R_DhcpSetSubnetInfo(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO
			)
		)


class R_DhcpSetSubnetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO
			)
		)


class R_DhcpGetSubnetInfo(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpGetSubnetInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpEnumSubnets(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpAddSubnetElement(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA
			)
		)


class R_DhcpAddSubnetElementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA
			)
		)


class R_DhcpEnumSubnetElements(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetElementsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveSubnetElement(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpRemoveSubnetElementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteSubnet(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteSubnetResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpCreateOption(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpCreateOptionResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfo(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpGetOptionInfo(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			)
		)


class R_DhcpGetOptionInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			)
		)


class R_DhcpRemoveOption(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			)
		)


class R_DhcpRemoveOptionResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			)
		)


class R_DhcpSetOptionValue(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpSetOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpGetOptionValue(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpGetOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpEnumOptionValues(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionValuesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveOptionValue(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpRemoveOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpCreateClientInfo(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO
			)
		)


class R_DhcpCreateClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO
			)
		)


class R_DhcpSetClientInfo(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO
			)
		)


class R_DhcpSetClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO
			)
		)


class R_DhcpGetClientInfo(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpGetClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpDeleteClientInfo(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpDeleteClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpEnumSubnetClients(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpGetClientOptions(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ClientSubnetMask',
			DHCP_IP_MASK
			)
		)


class R_DhcpGetClientOptionsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientIpAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ClientSubnetMask',
			DHCP_IP_MASK
			)
		)


class R_DhcpGetMibInfo(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMibInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpEnumOptions(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpSetOptionValues(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpSetOptionValuesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpServerSetConfig(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO
			)
		)


class R_DhcpServerSetConfigResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO
			)
		)


class R_DhcpServerGetConfig(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpServerGetConfigResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpScanDatabase(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'FixFlag',
			DWORD
			)
		)


class R_DhcpScanDatabaseResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'FixFlag',
			DWORD
			)
		)


class R_DhcpGetVersion(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetVersionResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpAddSubnetElementV4(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class R_DhcpAddSubnetElementV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class R_DhcpEnumSubnetElementsV4(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetElementsV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveSubnetElementV4(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpRemoveSubnetElementV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpCreateClientInfoV4(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V4
			)
		)


class R_DhcpCreateClientInfoV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V4
			)
		)


class R_DhcpSetClientInfoV4(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V4
			)
		)


class R_DhcpSetClientInfoV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V4
			)
		)


class R_DhcpGetClientInfoV4(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpGetClientInfoV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpEnumSubnetClientsV4(NDRCALL):
	OPNUM = 35
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpSetSuperScopeV4(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SuperScopeName',
			WCHAR
			),
			(
			'ChangeExisting',
			BOOL
			)
		)


class R_DhcpSetSuperScopeV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SuperScopeName',
			WCHAR
			),
			(
			'ChangeExisting',
			BOOL
			)
		)


class R_DhcpGetSuperScopeInfoV4(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetSuperScopeInfoV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpDeleteSuperScopeV4(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SuperScopeName',
			WCHAR
			)
		)


class R_DhcpDeleteSuperScopeV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SuperScopeName',
			WCHAR
			)
		)


class R_DhcpServerSetConfigV4(NDRCALL):
	OPNUM = 39
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_V4
			)
		)


class R_DhcpServerSetConfigV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_V4
			)
		)


class R_DhcpServerGetConfigV4(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpServerGetConfigV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpServerSetConfigVQ(NDRCALL):
	OPNUM = 41
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_VQ
			)
		)


class R_DhcpServerSetConfigVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_VQ
			)
		)


class R_DhcpServerGetConfigVQ(NDRCALL):
	OPNUM = 42
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpServerGetConfigVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMibInfoVQ(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMibInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpCreateClientInfoVQ(NDRCALL):
	OPNUM = 44
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_VQ
			)
		)


class R_DhcpCreateClientInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_VQ
			)
		)


class R_DhcpSetClientInfoVQ(NDRCALL):
	OPNUM = 45
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_VQ
			)
		)


class R_DhcpSetClientInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_VQ
			)
		)


class R_DhcpGetClientInfoVQ(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpGetClientInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpEnumSubnetClientsVQ(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpCreateSubnetVQ(NDRCALL):
	OPNUM = 48
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfoVQ',
			LPDHCP_SUBNET_INFO_VQ
			)
		)


class R_DhcpCreateSubnetVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfoVQ',
			LPDHCP_SUBNET_INFO_VQ
			)
		)


class R_DhcpGetSubnetInfoVQ(NDRCALL):
	OPNUM = 49
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpGetSubnetInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpSetSubnetInfoVQ(NDRCALL):
	OPNUM = 50
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfoVQ',
			LPDHCP_SUBNET_INFO_VQ
			)
		)


class R_DhcpSetSubnetInfoVQResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'SubnetInfoVQ',
			LPDHCP_SUBNET_INFO_VQ
			)
		)


OPNUMS = {0 : (
	R_DhcpCreateSubnet,
	R_DhcpCreateSubnetResponse
	),1 : (
	R_DhcpSetSubnetInfo,
	R_DhcpSetSubnetInfoResponse
	),2 : (
	R_DhcpGetSubnetInfo,
	R_DhcpGetSubnetInfoResponse
	),3 : (
	R_DhcpEnumSubnets,
	R_DhcpEnumSubnetsResponse
	),4 : (
	R_DhcpAddSubnetElement,
	R_DhcpAddSubnetElementResponse
	),5 : (
	R_DhcpEnumSubnetElements,
	R_DhcpEnumSubnetElementsResponse
	),6 : (
	R_DhcpRemoveSubnetElement,
	R_DhcpRemoveSubnetElementResponse
	),7 : (
	R_DhcpDeleteSubnet,
	R_DhcpDeleteSubnetResponse
	),8 : (
	R_DhcpCreateOption,
	R_DhcpCreateOptionResponse
	),9 : (
	R_DhcpSetOptionInfo,
	R_DhcpSetOptionInfoResponse
	),10 : (
	R_DhcpGetOptionInfo,
	R_DhcpGetOptionInfoResponse
	),11 : (
	R_DhcpRemoveOption,
	R_DhcpRemoveOptionResponse
	),12 : (
	R_DhcpSetOptionValue,
	R_DhcpSetOptionValueResponse
	),13 : (
	R_DhcpGetOptionValue,
	R_DhcpGetOptionValueResponse
	),14 : (
	R_DhcpEnumOptionValues,
	R_DhcpEnumOptionValuesResponse
	),15 : (
	R_DhcpRemoveOptionValue,
	R_DhcpRemoveOptionValueResponse
	),16 : (
	R_DhcpCreateClientInfo,
	R_DhcpCreateClientInfoResponse
	),17 : (
	R_DhcpSetClientInfo,
	R_DhcpSetClientInfoResponse
	),18 : (
	R_DhcpGetClientInfo,
	R_DhcpGetClientInfoResponse
	),19 : (
	R_DhcpDeleteClientInfo,
	R_DhcpDeleteClientInfoResponse
	),20 : (
	R_DhcpEnumSubnetClients,
	R_DhcpEnumSubnetClientsResponse
	),21 : (
	R_DhcpGetClientOptions,
	R_DhcpGetClientOptionsResponse
	),22 : (
	R_DhcpGetMibInfo,
	R_DhcpGetMibInfoResponse
	),23 : (
	R_DhcpEnumOptions,
	R_DhcpEnumOptionsResponse
	),24 : (
	R_DhcpSetOptionValues,
	R_DhcpSetOptionValuesResponse
	),25 : (
	R_DhcpServerSetConfig,
	R_DhcpServerSetConfigResponse
	),26 : (
	R_DhcpServerGetConfig,
	R_DhcpServerGetConfigResponse
	),27 : (
	R_DhcpScanDatabase,
	R_DhcpScanDatabaseResponse
	),28 : (
	R_DhcpGetVersion,
	R_DhcpGetVersionResponse
	),29 : (
	R_DhcpAddSubnetElementV4,
	R_DhcpAddSubnetElementV4Response
	),30 : (
	R_DhcpEnumSubnetElementsV4,
	R_DhcpEnumSubnetElementsV4Response
	),31 : (
	R_DhcpRemoveSubnetElementV4,
	R_DhcpRemoveSubnetElementV4Response
	),32 : (
	R_DhcpCreateClientInfoV4,
	R_DhcpCreateClientInfoV4Response
	),33 : (
	R_DhcpSetClientInfoV4,
	R_DhcpSetClientInfoV4Response
	),34 : (
	R_DhcpGetClientInfoV4,
	R_DhcpGetClientInfoV4Response
	),35 : (
	R_DhcpEnumSubnetClientsV4,
	R_DhcpEnumSubnetClientsV4Response
	),36 : (
	R_DhcpSetSuperScopeV4,
	R_DhcpSetSuperScopeV4Response
	),37 : (
	R_DhcpGetSuperScopeInfoV4,
	R_DhcpGetSuperScopeInfoV4Response
	),38 : (
	R_DhcpDeleteSuperScopeV4,
	R_DhcpDeleteSuperScopeV4Response
	),39 : (
	R_DhcpServerSetConfigV4,
	R_DhcpServerSetConfigV4Response
	),40 : (
	R_DhcpServerGetConfigV4,
	R_DhcpServerGetConfigV4Response
	),41 : (
	R_DhcpServerSetConfigVQ,
	R_DhcpServerSetConfigVQResponse
	),42 : (
	R_DhcpServerGetConfigVQ,
	R_DhcpServerGetConfigVQResponse
	),43 : (
	R_DhcpGetMibInfoVQ,
	R_DhcpGetMibInfoVQResponse
	),44 : (
	R_DhcpCreateClientInfoVQ,
	R_DhcpCreateClientInfoVQResponse
	),45 : (
	R_DhcpSetClientInfoVQ,
	R_DhcpSetClientInfoVQResponse
	),46 : (
	R_DhcpGetClientInfoVQ,
	R_DhcpGetClientInfoVQResponse
	),47 : (
	R_DhcpEnumSubnetClientsVQ,
	R_DhcpEnumSubnetClientsVQResponse
	),48 : (
	R_DhcpCreateSubnetVQ,
	R_DhcpCreateSubnetVQResponse
	),49 : (
	R_DhcpGetSubnetInfoVQ,
	R_DhcpGetSubnetInfoVQResponse
	),50 : (
	R_DhcpSetSubnetInfoVQ,
	R_DhcpSetSubnetInfoVQResponse
	)}
#################################################################################
#dhcpsrv2 Definition
#################################################################################
MSRPC_UUID_DHCPSRV2 = uuidtup_to_bin(('5b821720-f63b-11d0-aad2-00c04fc324db','0.0'))
class R_DhcpEnumSubnetClientsV5(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpSetMScopeInfo(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'MScopeInfo',
			LPDHCP_MSCOPE_INFO
			),
			(
			'NewScope',
			BOOL
			)
		)


class R_DhcpSetMScopeInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'MScopeInfo',
			LPDHCP_MSCOPE_INFO
			),
			(
			'NewScope',
			BOOL
			)
		)


class R_DhcpGetMScopeInfo(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			)
		)


class R_DhcpGetMScopeInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			)
		)


class R_DhcpEnumMScopes(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumMScopesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpAddMScopeElement(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class R_DhcpAddMScopeElementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			)
		)


class R_DhcpEnumMScopeElements(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumMScopeElementsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveMScopeElement(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpRemoveMScopeElementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V4
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteMScope(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteMScopeResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpScanMDatabase(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'FixFlag',
			DWORD
			)
		)


class R_DhcpScanMDatabaseResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'FixFlag',
			DWORD
			)
		)


class R_DhcpCreateMClientInfo(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ClientInfo',
			LPDHCP_MCLIENT_INFO
			)
		)


class R_DhcpCreateMClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ClientInfo',
			LPDHCP_MCLIENT_INFO
			)
		)


class R_DhcpSetMClientInfo(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_MCLIENT_INFO
			)
		)


class R_DhcpSetMClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_MCLIENT_INFO
			)
		)


class R_DhcpGetMClientInfo(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpGetMClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpDeleteMClientInfo(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpDeleteMClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpEnumMScopeClients(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumMScopeClientsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'MScopeName',
			WCHAR_T
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpCreateOptionV5(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpCreateOptionV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfoV5(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfoV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpGetOptionInfoV5(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpGetOptionInfoV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpEnumOptionsV5(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionsV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveOptionV5(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpRemoveOptionV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpSetOptionValueV5(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpSetOptionValueV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpSetOptionValuesV5(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpSetOptionValuesV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpGetOptionValueV5(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpGetOptionValueV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpEnumOptionValuesV5(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionValuesV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveOptionValueV5(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpRemoveOptionValueV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpCreateClass(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpCreateClassResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpModifyClass(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpModifyClassResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpDeleteClass(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			)
		)


class R_DhcpDeleteClassResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			)
		)


class R_DhcpGetClassInfo(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'PartialClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpGetClassInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'PartialClassInfo',
			LPDHCP_CLASS_INFO
			)
		)


class R_DhcpEnumClasses(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumClassesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpGetAllOptions(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpGetAllOptionsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpGetAllOptionValues(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpGetAllOptionValuesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpGetMCastMibInfo(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMCastMibInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpAuditLogSetParams(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'AuditLogDir',
			WCHAR_T
			),
			(
			'DiskCheckInterval',
			DWORD
			),
			(
			'MaxLogFilesSize',
			DWORD
			),
			(
			'MinSpaceOnDisk',
			DWORD
			)
		)


class R_DhcpAuditLogSetParamsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'AuditLogDir',
			WCHAR_T
			),
			(
			'DiskCheckInterval',
			DWORD
			),
			(
			'MaxLogFilesSize',
			DWORD
			),
			(
			'MinSpaceOnDisk',
			DWORD
			)
		)


class R_DhcpAuditLogGetParams(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpAuditLogGetParamsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpServerQueryAttribute(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			),
			(
			'DhcpAttribId',
			DHCP_ATTRIB_ID
			)
		)


class R_DhcpServerQueryAttributeResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			),
			(
			'DhcpAttribId',
			DHCP_ATTRIB_ID
			)
		)


class R_DhcpServerQueryAttributes(NDRCALL):
	OPNUM = 35
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			),
			(
			'dwAttribCount',
			ULONG
			),
			(
			'pDhcpAttribs',
			LPDHCP_ATTRIB_ID
			)
		)


class R_DhcpServerQueryAttributesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			),
			(
			'dwAttribCount',
			ULONG
			),
			(
			'pDhcpAttribs',
			LPDHCP_ATTRIB_ID
			)
		)


class R_DhcpServerRedoAuthorization(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			)
		)


class R_DhcpServerRedoAuthorizationResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'dwReserved',
			ULONG
			)
		)


class R_DhcpAddSubnetElementV5(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V5
			)
		)


class R_DhcpAddSubnetElementV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V5
			)
		)


class R_DhcpEnumSubnetElementsV5(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetElementsV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveSubnetElementV5(NDRCALL):
	OPNUM = 39
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V5
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpRemoveSubnetElementV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V5
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpGetServerBindingInfo(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			)
		)


class R_DhcpGetServerBindingInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			)
		)


class R_DhcpSetServerBindingInfo(NDRCALL):
	OPNUM = 41
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			),
			(
			'BindElementsInfo',
			LPDHCP_BIND_ELEMENT_ARRAY
			)
		)


class R_DhcpSetServerBindingInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			),
			(
			'BindElementsInfo',
			LPDHCP_BIND_ELEMENT_ARRAY
			)
		)


class R_DhcpQueryDnsRegCredentials(NDRCALL):
	OPNUM = 42
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'UnameSize',
			ULONG
			),
			(
			'DomainSize',
			ULONG
			)
		)


class R_DhcpQueryDnsRegCredentialsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'UnameSize',
			ULONG
			),
			(
			'DomainSize',
			ULONG
			)
		)


class R_DhcpSetDnsRegCredentials(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Uname',
			WCHAR_T
			),
			(
			'Domain',
			WCHAR_T
			),
			(
			'Passwd',
			WCHAR_T
			)
		)


class R_DhcpSetDnsRegCredentialsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Uname',
			WCHAR_T
			),
			(
			'Domain',
			WCHAR_T
			),
			(
			'Passwd',
			WCHAR_T
			)
		)


class R_DhcpBackupDatabase(NDRCALL):
	OPNUM = 44
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Path',
			WCHAR_T
			)
		)


class R_DhcpBackupDatabaseResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Path',
			WCHAR_T
			)
		)


class R_DhcpRestoreDatabase(NDRCALL):
	OPNUM = 45
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Path',
			WCHAR_T
			)
		)


class R_DhcpRestoreDatabaseResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Path',
			WCHAR_T
			)
		)


class R_DhcpGetServerSpecificStrings(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetServerSpecificStringsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpCreateOptionV6(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpCreateOptionV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfoV6(NDRCALL):
	OPNUM = 48
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpSetOptionInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'OptionInfo',
			LPDHCP_OPTION
			)
		)


class R_DhcpGetOptionInfoV6(NDRCALL):
	OPNUM = 49
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpGetOptionInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpEnumOptionsV6(NDRCALL):
	OPNUM = 50
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionsV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveOptionV6(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpRemoveOptionV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			)
		)


class R_DhcpSetOptionValueV6(NDRCALL):
	OPNUM = 52
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpSetOptionValueV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionId',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpEnumOptionValuesV6(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumOptionValuesV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveOptionValueV6(NDRCALL):
	OPNUM = 54
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpRemoveOptionValueV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpGetAllOptionsV6(NDRCALL):
	OPNUM = 55
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpGetAllOptionsV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class R_DhcpGetAllOptionValuesV6(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpGetAllOptionValuesV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpCreateSubnetV6(NDRCALL):
	OPNUM = 57
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO_V6
			)
		)


class R_DhcpCreateSubnetV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO_V6
			)
		)


class R_DhcpEnumSubnetsV6(NDRCALL):
	OPNUM = 58
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetsV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpAddSubnetElementV6(NDRCALL):
	OPNUM = 59
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V6
			)
		)


class R_DhcpAddSubnetElementV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'AddElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V6
			)
		)


class R_DhcpEnumSubnetElementsV6(NDRCALL):
	OPNUM = 60
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE_V6
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetElementsV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'EnumElementType',
			DHCP_SUBNET_ELEMENT_TYPE_V6
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpRemoveSubnetElementV6(NDRCALL):
	OPNUM = 61
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V6
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpRemoveSubnetElementV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'RemoveElementInfo',
			LPDHCP_SUBNET_ELEMENT_DATA_V6
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteSubnetV6(NDRCALL):
	OPNUM = 62
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpDeleteSubnetV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ForceFlag',
			DHCP_FORCE_FLAG
			)
		)


class R_DhcpGetSubnetInfoV6(NDRCALL):
	OPNUM = 63
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class R_DhcpGetSubnetInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class R_DhcpEnumSubnetClientsV6(NDRCALL):
	OPNUM = 64
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_IPV6_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_IPV6_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpServerSetConfigV6(NDRCALL):
	OPNUM = 65
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_V6
			)
		)


class R_DhcpServerSetConfigV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			),
			(
			'FieldsToSet',
			DWORD
			),
			(
			'ConfigInfo',
			LPDHCP_SERVER_CONFIG_INFO_V6
			)
		)


class R_DhcpServerGetConfigV6(NDRCALL):
	OPNUM = 66
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpServerGetConfigV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpSetSubnetInfoV6(NDRCALL):
	OPNUM = 67
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO_V6
			)
		)


class R_DhcpSetSubnetInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'SubnetInfo',
			LPDHCP_SUBNET_INFO_V6
			)
		)


class R_DhcpGetMibInfoV6(NDRCALL):
	OPNUM = 68
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMibInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetServerBindingInfoV6(NDRCALL):
	OPNUM = 69
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			)
		)


class R_DhcpGetServerBindingInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			)
		)


class R_DhcpSetServerBindingInfoV6(NDRCALL):
	OPNUM = 70
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			),
			(
			'BindElementsInfo',
			LPDHCPV6_BIND_ELEMENT_ARRAY
			)
		)


class R_DhcpSetServerBindingInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			ULONG
			),
			(
			'BindElementsInfo',
			LPDHCPV6_BIND_ELEMENT_ARRAY
			)
		)


class R_DhcpSetClientInfoV6(NDRCALL):
	OPNUM = 71
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V6
			)
		)


class R_DhcpSetClientInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V6
			)
		)


class R_DhcpGetClientInfoV6(NDRCALL):
	OPNUM = 72
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO_V6
			)
		)


class R_DhcpGetClientInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO_V6
			)
		)


class R_DhcpDeleteClientInfoV6(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO_V6
			)
		)


class R_DhcpDeleteClientInfoV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_SEARCH_INFO_V6
			)
		)


class R_DhcpCreateClassV6(NDRCALL):
	OPNUM = 74
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO_V6
			)
		)


class R_DhcpCreateClassV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO_V6
			)
		)


class R_DhcpModifyClassV6(NDRCALL):
	OPNUM = 75
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO_V6
			)
		)


class R_DhcpModifyClassV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassInfo',
			LPDHCP_CLASS_INFO_V6
			)
		)


class R_DhcpDeleteClassV6(NDRCALL):
	OPNUM = 76
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			)
		)


class R_DhcpDeleteClassV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ClassName',
			WCHAR
			)
		)


class R_DhcpEnumClassesV6(NDRCALL):
	OPNUM = 77
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumClassesV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ReservedMustBeZero',
			DWORD
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpGetOptionValueV6(NDRCALL):
	OPNUM = 78
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpGetOptionValueV6Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'ClassName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO6
			)
		)


class R_DhcpSetSubnetDelayOffer(NDRCALL):
	OPNUM = 79
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'TimeDelayInMilliseconds',
			USHORT
			)
		)


class R_DhcpSetSubnetDelayOfferResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'TimeDelayInMilliseconds',
			USHORT
			)
		)


class R_DhcpGetSubnetDelayOffer(NDRCALL):
	OPNUM = 80
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpGetSubnetDelayOfferResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpGetMibInfoV5(NDRCALL):
	OPNUM = 81
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetMibInfoV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpAddFilterV4(NDRCALL):
	OPNUM = 82
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'AddFilterInfo',
			DHCP_FILTER_ADD_INFO
			),
			(
			'ForceFlag',
			BOOL
			)
		)


class R_DhcpAddFilterV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'AddFilterInfo',
			DHCP_FILTER_ADD_INFO
			),
			(
			'ForceFlag',
			BOOL
			)
		)


class R_DhcpDeleteFilterV4(NDRCALL):
	OPNUM = 83
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'DeleteFilterInfo',
			DHCP_ADDR_PATTERN
			)
		)


class R_DhcpDeleteFilterV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'DeleteFilterInfo',
			DHCP_ADDR_PATTERN
			)
		)


class R_DhcpSetFilterV4(NDRCALL):
	OPNUM = 84
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'GlobalFilterInfo',
			DHCP_FILTER_GLOBAL_INFO
			)
		)


class R_DhcpSetFilterV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'GlobalFilterInfo',
			DHCP_FILTER_GLOBAL_INFO
			)
		)


class R_DhcpGetFilterV4(NDRCALL):
	OPNUM = 85
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpGetFilterV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpEnumFilterV4(NDRCALL):
	OPNUM = 86
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDHCP_ADDR_PATTERN
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ListType',
			DHCP_FILTER_LIST_TYPE
			)
		)


class R_DhcpEnumFilterV4Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDHCP_ADDR_PATTERN
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ListType',
			DHCP_FILTER_LIST_TYPE
			)
		)


class R_DhcpSetDnsRegCredentialsV5(NDRCALL):
	OPNUM = 87
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Uname',
			WCHAR_T
			),
			(
			'Domain',
			WCHAR_T
			),
			(
			'Passwd',
			WCHAR_T
			)
		)


class R_DhcpSetDnsRegCredentialsV5Response(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Uname',
			WCHAR_T
			),
			(
			'Domain',
			WCHAR_T
			),
			(
			'Passwd',
			WCHAR_T
			)
		)


class R_DhcpEnumSubnetClientsFilterStatusInfo(NDRCALL):
	OPNUM = 88
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpEnumSubnetClientsFilterStatusInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4FailoverCreateRelationship(NDRCALL):
	OPNUM = 89
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverCreateRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverSetRelationship(NDRCALL):
	OPNUM = 90
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverSetRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverDeleteRelationship(NDRCALL):
	OPNUM = 91
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationshipName',
			WCHAR_T
			)
		)


class R_DhcpV4FailoverDeleteRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationshipName',
			WCHAR_T
			)
		)


class R_DhcpV4FailoverGetRelationship(NDRCALL):
	OPNUM = 92
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationshipName',
			WCHAR_T
			)
		)


class R_DhcpV4FailoverGetRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationshipName',
			WCHAR_T
			)
		)


class R_DhcpV4FailoverEnumRelationship(NDRCALL):
	OPNUM = 93
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'preferredMaximum',
			DWORD
			)
		)


class R_DhcpV4FailoverEnumRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'preferredMaximum',
			DWORD
			)
		)


class R_DhcpV4FailoverAddScopeToRelationship(NDRCALL):
	OPNUM = 94
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverAddScopeToRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverDeleteScopeFromRelationship(NDRCALL):
	OPNUM = 95
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverDeleteScopeFromRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pRelationship',
			LPDHCP_FAILOVER_RELATIONSHIP
			)
		)


class R_DhcpV4FailoverGetScopeRelationship(NDRCALL):
	OPNUM = 96
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'scopeId',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4FailoverGetScopeRelationshipResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'scopeId',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4FailoverGetScopeStatistics(NDRCALL):
	OPNUM = 97
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'scopeId',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4FailoverGetScopeStatisticsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'scopeId',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4FailoverGetClientInfo(NDRCALL):
	OPNUM = 98
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpV4FailoverGetClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpV4FailoverGetSystemTime(NDRCALL):
	OPNUM = 99
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpV4FailoverGetSystemTimeResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpV4FailoverTriggerAddrAllocation(NDRCALL):
	OPNUM = 100
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FailRelName',
			WCHAR_T
			)
		)


class R_DhcpV4FailoverTriggerAddrAllocationResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FailRelName',
			WCHAR_T
			)
		)


class R_DhcpV4SetOptionValue(NDRCALL):
	OPNUM = 101
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpV4SetOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValue',
			LPDHCP_OPTION_DATA
			)
		)


class R_DhcpV4SetOptionValues(NDRCALL):
	OPNUM = 102
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpV4SetOptionValuesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			),
			(
			'OptionValues',
			LPDHCP_OPTION_VALUE_ARRAY
			)
		)


class R_DhcpV4GetOptionValue(NDRCALL):
	OPNUM = 103
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4GetOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4RemoveOptionValue(NDRCALL):
	OPNUM = 104
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4RemoveOptionValueResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'OptionID',
			DHCP_OPTION_ID
			),
			(
			'PolicyName',
			WCHAR
			),
			(
			'VendorName',
			WCHAR
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4GetAllOptionValues(NDRCALL):
	OPNUM = 105
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4GetAllOptionValuesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'Flags',
			DWORD
			),
			(
			'ScopeInfo',
			LPDHCP_OPTION_SCOPE_INFO
			)
		)


class R_DhcpV4QueryPolicyEnforcement(NDRCALL):
	OPNUM = 106
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4QueryPolicyEnforcementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4SetPolicyEnforcement(NDRCALL):
	OPNUM = 107
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'Enable',
			BOOL
			)
		)


class R_DhcpV4SetPolicyEnforcementResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'Enable',
			BOOL
			)
		)


class R_DhcpV4CreatePolicy(NDRCALL):
	OPNUM = 108
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pPolicy',
			LPDHCP_POLICY
			)
		)


class R_DhcpV4CreatePolicyResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pPolicy',
			LPDHCP_POLICY
			)
		)


class R_DhcpV4GetPolicy(NDRCALL):
	OPNUM = 109
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4GetPolicyResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4SetPolicy(NDRCALL):
	OPNUM = 110
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsModified',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Policy',
			LPDHCP_POLICY
			)
		)


class R_DhcpV4SetPolicyResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsModified',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Policy',
			LPDHCP_POLICY
			)
		)


class R_DhcpV4DeletePolicy(NDRCALL):
	OPNUM = 111
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4DeletePolicyResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4EnumPolicies(NDRCALL):
	OPNUM = 112
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDWORD
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4EnumPoliciesResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDWORD
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4AddPolicyRange(NDRCALL):
	OPNUM = 113
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Range',
			LPDHCP_IP_RANGE
			)
		)


class R_DhcpV4AddPolicyRangeResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Range',
			LPDHCP_IP_RANGE
			)
		)


class R_DhcpV4RemovePolicyRange(NDRCALL):
	OPNUM = 114
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Range',
			LPDHCP_IP_RANGE
			)
		)


class R_DhcpV4RemovePolicyRangeResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Range',
			LPDHCP_IP_RANGE
			)
		)


class R_DhcpV4EnumSubnetClients(NDRCALL):
	OPNUM = 115
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4EnumSubnetClientsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV6SetStatelessStoreParams(NDRCALL):
	OPNUM = 116
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'fServerLevel',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'FieldModified',
			DWORD
			),
			(
			'Params',
			LPDHCPV6_STATELESS_PARAMS
			)
		)


class R_DhcpV6SetStatelessStoreParamsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'fServerLevel',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			),
			(
			'FieldModified',
			DWORD
			),
			(
			'Params',
			LPDHCPV6_STATELESS_PARAMS
			)
		)


class R_DhcpV6GetStatelessStoreParams(NDRCALL):
	OPNUM = 117
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'fServerLevel',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class R_DhcpV6GetStatelessStoreParamsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'fServerLevel',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IPV6_ADDRESS
			)
		)


class R_DhcpV6GetStatelessStatistics(NDRCALL):
	OPNUM = 118
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpV6GetStatelessStatisticsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			)
		)


class R_DhcpV4EnumSubnetReservations(NDRCALL):
	OPNUM = 119
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4EnumSubnetReservationsResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4GetFreeIPAddress(NDRCALL):
	OPNUM = 120
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeId',
			DHCP_IP_ADDRESS
			),
			(
			'startIP',
			DHCP_IP_ADDRESS
			),
			(
			'endIP',
			DHCP_IP_ADDRESS
			),
			(
			'numFreeAddr',
			DWORD
			)
		)


class R_DhcpV4GetFreeIPAddressResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeId',
			DHCP_IP_ADDRESS
			),
			(
			'startIP',
			DHCP_IP_ADDRESS
			),
			(
			'endIP',
			DHCP_IP_ADDRESS
			),
			(
			'numFreeAddr',
			DWORD
			)
		)


class R_DhcpV6GetFreeIPAddress(NDRCALL):
	OPNUM = 121
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeId',
			DHCP_IPV6_ADDRESS
			),
			(
			'startIP',
			DHCP_IPV6_ADDRESS
			),
			(
			'endIP',
			DHCP_IPV6_ADDRESS
			),
			(
			'numFreeAddr',
			DWORD
			)
		)


class R_DhcpV6GetFreeIPAddressResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ScopeId',
			DHCP_IPV6_ADDRESS
			),
			(
			'startIP',
			DHCP_IPV6_ADDRESS
			),
			(
			'endIP',
			DHCP_IPV6_ADDRESS
			),
			(
			'numFreeAddr',
			DWORD
			)
		)


class R_DhcpV4CreateClientInfo(NDRCALL):
	OPNUM = 122
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_PB
			)
		)


class R_DhcpV4CreateClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_PB
			)
		)


class R_DhcpV4GetClientInfo(NDRCALL):
	OPNUM = 123
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpV4GetClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpV6CreateClientInfo(NDRCALL):
	OPNUM = 124
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V6
			)
		)


class R_DhcpV6CreateClientInfoResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_V6
			)
		)


class R_DhcpV4FailoverGetAddressStatus(NDRCALL):
	OPNUM = 125
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4FailoverGetAddressStatusResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4CreatePolicyEx(NDRCALL):
	OPNUM = 126
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pPolicy',
			LPDHCP_POLICY_EX
			)
		)


class R_DhcpV4CreatePolicyExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'pPolicy',
			LPDHCP_POLICY_EX
			)
		)


class R_DhcpV4GetPolicyEx(NDRCALL):
	OPNUM = 127
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4GetPolicyExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			)
		)


class R_DhcpV4SetPolicyEx(NDRCALL):
	OPNUM = 128
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsModified',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Policy',
			LPDHCP_POLICY_EX
			)
		)


class R_DhcpV4SetPolicyExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'FieldsModified',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'PolicyName',
			WCHAR_T
			),
			(
			'Policy',
			LPDHCP_POLICY_EX
			)
		)


class R_DhcpV4EnumPoliciesEx(NDRCALL):
	OPNUM = 129
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDWORD
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4EnumPoliciesExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ResumeHandle',
			LPDWORD
			),
			(
			'PreferredMaximum',
			DWORD
			),
			(
			'ServerPolicy',
			BOOL
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			)
		)


class R_DhcpV4EnumSubnetClientsEx(NDRCALL):
	OPNUM = 130
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4EnumSubnetClientsExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SubnetAddress',
			DHCP_IP_ADDRESS
			),
			(
			'ResumeHandle',
			DHCP_RESUME_HANDLE
			),
			(
			'PreferredMaximum',
			DWORD
			)
		)


class R_DhcpV4CreateClientInfoEx(NDRCALL):
	OPNUM = 131
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_EX
			)
		)


class R_DhcpV4CreateClientInfoExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'ClientInfo',
			LPDHCP_CLIENT_INFO_EX
			)
		)


class R_DhcpV4GetClientInfoEx(NDRCALL):
	OPNUM = 132
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


class R_DhcpV4GetClientInfoExResponse(NDRCALL):
	structure = (
			(
			'ServerIpAddress',
			DHCP_SRV_HANDLE
			),
			(
			'SearchInfo',
			LPDHCP_SEARCH_INFO
			)
		)


OPNUMS = {0 : (
	R_DhcpEnumSubnetClientsV5,
	R_DhcpEnumSubnetClientsV5Response
	),1 : (
	R_DhcpSetMScopeInfo,
	R_DhcpSetMScopeInfoResponse
	),2 : (
	R_DhcpGetMScopeInfo,
	R_DhcpGetMScopeInfoResponse
	),3 : (
	R_DhcpEnumMScopes,
	R_DhcpEnumMScopesResponse
	),4 : (
	R_DhcpAddMScopeElement,
	R_DhcpAddMScopeElementResponse
	),5 : (
	R_DhcpEnumMScopeElements,
	R_DhcpEnumMScopeElementsResponse
	),6 : (
	R_DhcpRemoveMScopeElement,
	R_DhcpRemoveMScopeElementResponse
	),7 : (
	R_DhcpDeleteMScope,
	R_DhcpDeleteMScopeResponse
	),8 : (
	R_DhcpScanMDatabase,
	R_DhcpScanMDatabaseResponse
	),9 : (
	R_DhcpCreateMClientInfo,
	R_DhcpCreateMClientInfoResponse
	),10 : (
	R_DhcpSetMClientInfo,
	R_DhcpSetMClientInfoResponse
	),11 : (
	R_DhcpGetMClientInfo,
	R_DhcpGetMClientInfoResponse
	),12 : (
	R_DhcpDeleteMClientInfo,
	R_DhcpDeleteMClientInfoResponse
	),13 : (
	R_DhcpEnumMScopeClients,
	R_DhcpEnumMScopeClientsResponse
	),14 : (
	R_DhcpCreateOptionV5,
	R_DhcpCreateOptionV5Response
	),15 : (
	R_DhcpSetOptionInfoV5,
	R_DhcpSetOptionInfoV5Response
	),16 : (
	R_DhcpGetOptionInfoV5,
	R_DhcpGetOptionInfoV5Response
	),17 : (
	R_DhcpEnumOptionsV5,
	R_DhcpEnumOptionsV5Response
	),18 : (
	R_DhcpRemoveOptionV5,
	R_DhcpRemoveOptionV5Response
	),19 : (
	R_DhcpSetOptionValueV5,
	R_DhcpSetOptionValueV5Response
	),20 : (
	R_DhcpSetOptionValuesV5,
	R_DhcpSetOptionValuesV5Response
	),21 : (
	R_DhcpGetOptionValueV5,
	R_DhcpGetOptionValueV5Response
	),22 : (
	R_DhcpEnumOptionValuesV5,
	R_DhcpEnumOptionValuesV5Response
	),23 : (
	R_DhcpRemoveOptionValueV5,
	R_DhcpRemoveOptionValueV5Response
	),24 : (
	R_DhcpCreateClass,
	R_DhcpCreateClassResponse
	),25 : (
	R_DhcpModifyClass,
	R_DhcpModifyClassResponse
	),26 : (
	R_DhcpDeleteClass,
	R_DhcpDeleteClassResponse
	),27 : (
	R_DhcpGetClassInfo,
	R_DhcpGetClassInfoResponse
	),28 : (
	R_DhcpEnumClasses,
	R_DhcpEnumClassesResponse
	),29 : (
	R_DhcpGetAllOptions,
	R_DhcpGetAllOptionsResponse
	),30 : (
	R_DhcpGetAllOptionValues,
	R_DhcpGetAllOptionValuesResponse
	),31 : (
	R_DhcpGetMCastMibInfo,
	R_DhcpGetMCastMibInfoResponse
	),32 : (
	R_DhcpAuditLogSetParams,
	R_DhcpAuditLogSetParamsResponse
	),33 : (
	R_DhcpAuditLogGetParams,
	R_DhcpAuditLogGetParamsResponse
	),34 : (
	R_DhcpServerQueryAttribute,
	R_DhcpServerQueryAttributeResponse
	),35 : (
	R_DhcpServerQueryAttributes,
	R_DhcpServerQueryAttributesResponse
	),36 : (
	R_DhcpServerRedoAuthorization,
	R_DhcpServerRedoAuthorizationResponse
	),37 : (
	R_DhcpAddSubnetElementV5,
	R_DhcpAddSubnetElementV5Response
	),38 : (
	R_DhcpEnumSubnetElementsV5,
	R_DhcpEnumSubnetElementsV5Response
	),39 : (
	R_DhcpRemoveSubnetElementV5,
	R_DhcpRemoveSubnetElementV5Response
	),40 : (
	R_DhcpGetServerBindingInfo,
	R_DhcpGetServerBindingInfoResponse
	),41 : (
	R_DhcpSetServerBindingInfo,
	R_DhcpSetServerBindingInfoResponse
	),42 : (
	R_DhcpQueryDnsRegCredentials,
	R_DhcpQueryDnsRegCredentialsResponse
	),43 : (
	R_DhcpSetDnsRegCredentials,
	R_DhcpSetDnsRegCredentialsResponse
	),44 : (
	R_DhcpBackupDatabase,
	R_DhcpBackupDatabaseResponse
	),45 : (
	R_DhcpRestoreDatabase,
	R_DhcpRestoreDatabaseResponse
	),46 : (
	R_DhcpGetServerSpecificStrings,
	R_DhcpGetServerSpecificStringsResponse
	),47 : (
	R_DhcpCreateOptionV6,
	R_DhcpCreateOptionV6Response
	),48 : (
	R_DhcpSetOptionInfoV6,
	R_DhcpSetOptionInfoV6Response
	),49 : (
	R_DhcpGetOptionInfoV6,
	R_DhcpGetOptionInfoV6Response
	),50 : (
	R_DhcpEnumOptionsV6,
	R_DhcpEnumOptionsV6Response
	),51 : (
	R_DhcpRemoveOptionV6,
	R_DhcpRemoveOptionV6Response
	),52 : (
	R_DhcpSetOptionValueV6,
	R_DhcpSetOptionValueV6Response
	),53 : (
	R_DhcpEnumOptionValuesV6,
	R_DhcpEnumOptionValuesV6Response
	),54 : (
	R_DhcpRemoveOptionValueV6,
	R_DhcpRemoveOptionValueV6Response
	),55 : (
	R_DhcpGetAllOptionsV6,
	R_DhcpGetAllOptionsV6Response
	),56 : (
	R_DhcpGetAllOptionValuesV6,
	R_DhcpGetAllOptionValuesV6Response
	),57 : (
	R_DhcpCreateSubnetV6,
	R_DhcpCreateSubnetV6Response
	),58 : (
	R_DhcpEnumSubnetsV6,
	R_DhcpEnumSubnetsV6Response
	),59 : (
	R_DhcpAddSubnetElementV6,
	R_DhcpAddSubnetElementV6Response
	),60 : (
	R_DhcpEnumSubnetElementsV6,
	R_DhcpEnumSubnetElementsV6Response
	),61 : (
	R_DhcpRemoveSubnetElementV6,
	R_DhcpRemoveSubnetElementV6Response
	),62 : (
	R_DhcpDeleteSubnetV6,
	R_DhcpDeleteSubnetV6Response
	),63 : (
	R_DhcpGetSubnetInfoV6,
	R_DhcpGetSubnetInfoV6Response
	),64 : (
	R_DhcpEnumSubnetClientsV6,
	R_DhcpEnumSubnetClientsV6Response
	),65 : (
	R_DhcpServerSetConfigV6,
	R_DhcpServerSetConfigV6Response
	),66 : (
	R_DhcpServerGetConfigV6,
	R_DhcpServerGetConfigV6Response
	),67 : (
	R_DhcpSetSubnetInfoV6,
	R_DhcpSetSubnetInfoV6Response
	),68 : (
	R_DhcpGetMibInfoV6,
	R_DhcpGetMibInfoV6Response
	),69 : (
	R_DhcpGetServerBindingInfoV6,
	R_DhcpGetServerBindingInfoV6Response
	),70 : (
	R_DhcpSetServerBindingInfoV6,
	R_DhcpSetServerBindingInfoV6Response
	),71 : (
	R_DhcpSetClientInfoV6,
	R_DhcpSetClientInfoV6Response
	),72 : (
	R_DhcpGetClientInfoV6,
	R_DhcpGetClientInfoV6Response
	),73 : (
	R_DhcpDeleteClientInfoV6,
	R_DhcpDeleteClientInfoV6Response
	),74 : (
	R_DhcpCreateClassV6,
	R_DhcpCreateClassV6Response
	),75 : (
	R_DhcpModifyClassV6,
	R_DhcpModifyClassV6Response
	),76 : (
	R_DhcpDeleteClassV6,
	R_DhcpDeleteClassV6Response
	),77 : (
	R_DhcpEnumClassesV6,
	R_DhcpEnumClassesV6Response
	),78 : (
	R_DhcpGetOptionValueV6,
	R_DhcpGetOptionValueV6Response
	),79 : (
	R_DhcpSetSubnetDelayOffer,
	R_DhcpSetSubnetDelayOfferResponse
	),80 : (
	R_DhcpGetSubnetDelayOffer,
	R_DhcpGetSubnetDelayOfferResponse
	),81 : (
	R_DhcpGetMibInfoV5,
	R_DhcpGetMibInfoV5Response
	),82 : (
	R_DhcpAddFilterV4,
	R_DhcpAddFilterV4Response
	),83 : (
	R_DhcpDeleteFilterV4,
	R_DhcpDeleteFilterV4Response
	),84 : (
	R_DhcpSetFilterV4,
	R_DhcpSetFilterV4Response
	),85 : (
	R_DhcpGetFilterV4,
	R_DhcpGetFilterV4Response
	),86 : (
	R_DhcpEnumFilterV4,
	R_DhcpEnumFilterV4Response
	),87 : (
	R_DhcpSetDnsRegCredentialsV5,
	R_DhcpSetDnsRegCredentialsV5Response
	),88 : (
	R_DhcpEnumSubnetClientsFilterStatusInfo,
	R_DhcpEnumSubnetClientsFilterStatusInfoResponse
	),89 : (
	R_DhcpV4FailoverCreateRelationship,
	R_DhcpV4FailoverCreateRelationshipResponse
	),90 : (
	R_DhcpV4FailoverSetRelationship,
	R_DhcpV4FailoverSetRelationshipResponse
	),91 : (
	R_DhcpV4FailoverDeleteRelationship,
	R_DhcpV4FailoverDeleteRelationshipResponse
	),92 : (
	R_DhcpV4FailoverGetRelationship,
	R_DhcpV4FailoverGetRelationshipResponse
	),93 : (
	R_DhcpV4FailoverEnumRelationship,
	R_DhcpV4FailoverEnumRelationshipResponse
	),94 : (
	R_DhcpV4FailoverAddScopeToRelationship,
	R_DhcpV4FailoverAddScopeToRelationshipResponse
	),95 : (
	R_DhcpV4FailoverDeleteScopeFromRelationship,
	R_DhcpV4FailoverDeleteScopeFromRelationshipResponse
	),96 : (
	R_DhcpV4FailoverGetScopeRelationship,
	R_DhcpV4FailoverGetScopeRelationshipResponse
	),97 : (
	R_DhcpV4FailoverGetScopeStatistics,
	R_DhcpV4FailoverGetScopeStatisticsResponse
	),98 : (
	R_DhcpV4FailoverGetClientInfo,
	R_DhcpV4FailoverGetClientInfoResponse
	),99 : (
	R_DhcpV4FailoverGetSystemTime,
	R_DhcpV4FailoverGetSystemTimeResponse
	),100 : (
	R_DhcpV4FailoverTriggerAddrAllocation,
	R_DhcpV4FailoverTriggerAddrAllocationResponse
	),101 : (
	R_DhcpV4SetOptionValue,
	R_DhcpV4SetOptionValueResponse
	),102 : (
	R_DhcpV4SetOptionValues,
	R_DhcpV4SetOptionValuesResponse
	),103 : (
	R_DhcpV4GetOptionValue,
	R_DhcpV4GetOptionValueResponse
	),104 : (
	R_DhcpV4RemoveOptionValue,
	R_DhcpV4RemoveOptionValueResponse
	),105 : (
	R_DhcpV4GetAllOptionValues,
	R_DhcpV4GetAllOptionValuesResponse
	),106 : (
	R_DhcpV4QueryPolicyEnforcement,
	R_DhcpV4QueryPolicyEnforcementResponse
	),107 : (
	R_DhcpV4SetPolicyEnforcement,
	R_DhcpV4SetPolicyEnforcementResponse
	),108 : (
	R_DhcpV4CreatePolicy,
	R_DhcpV4CreatePolicyResponse
	),109 : (
	R_DhcpV4GetPolicy,
	R_DhcpV4GetPolicyResponse
	),110 : (
	R_DhcpV4SetPolicy,
	R_DhcpV4SetPolicyResponse
	),111 : (
	R_DhcpV4DeletePolicy,
	R_DhcpV4DeletePolicyResponse
	),112 : (
	R_DhcpV4EnumPolicies,
	R_DhcpV4EnumPoliciesResponse
	),113 : (
	R_DhcpV4AddPolicyRange,
	R_DhcpV4AddPolicyRangeResponse
	),114 : (
	R_DhcpV4RemovePolicyRange,
	R_DhcpV4RemovePolicyRangeResponse
	),115 : (
	R_DhcpV4EnumSubnetClients,
	R_DhcpV4EnumSubnetClientsResponse
	),116 : (
	R_DhcpV6SetStatelessStoreParams,
	R_DhcpV6SetStatelessStoreParamsResponse
	),117 : (
	R_DhcpV6GetStatelessStoreParams,
	R_DhcpV6GetStatelessStoreParamsResponse
	),118 : (
	R_DhcpV6GetStatelessStatistics,
	R_DhcpV6GetStatelessStatisticsResponse
	),119 : (
	R_DhcpV4EnumSubnetReservations,
	R_DhcpV4EnumSubnetReservationsResponse
	),120 : (
	R_DhcpV4GetFreeIPAddress,
	R_DhcpV4GetFreeIPAddressResponse
	),121 : (
	R_DhcpV6GetFreeIPAddress,
	R_DhcpV6GetFreeIPAddressResponse
	),122 : (
	R_DhcpV4CreateClientInfo,
	R_DhcpV4CreateClientInfoResponse
	),123 : (
	R_DhcpV4GetClientInfo,
	R_DhcpV4GetClientInfoResponse
	),124 : (
	R_DhcpV6CreateClientInfo,
	R_DhcpV6CreateClientInfoResponse
	),125 : (
	R_DhcpV4FailoverGetAddressStatus,
	R_DhcpV4FailoverGetAddressStatusResponse
	),126 : (
	R_DhcpV4CreatePolicyEx,
	R_DhcpV4CreatePolicyExResponse
	),127 : (
	R_DhcpV4GetPolicyEx,
	R_DhcpV4GetPolicyExResponse
	),128 : (
	R_DhcpV4SetPolicyEx,
	R_DhcpV4SetPolicyExResponse
	),129 : (
	R_DhcpV4EnumPoliciesEx,
	R_DhcpV4EnumPoliciesExResponse
	),130 : (
	R_DhcpV4EnumSubnetClientsEx,
	R_DhcpV4EnumSubnetClientsExResponse
	),131 : (
	R_DhcpV4CreateClientInfoEx,
	R_DhcpV4CreateClientInfoExResponse
	),132 : (
	R_DhcpV4GetClientInfoEx,
	R_DhcpV4GetClientInfoExResponse
	)}
