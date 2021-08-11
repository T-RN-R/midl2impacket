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


class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
    item = WCHAR

class PTR_UNSIGNED_SHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_SHORT),
    )

class UNSIGNED_SHORT(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_UNSIGNED_SHORT),

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

DHCP_SRV_HANDLE = LPWSTR
DHCP_IP_ADDRESS = DWORD
PDHCP_IP_ADDRESS = DWORD
LPDHCP_IP_ADDRESS = DWORD
DHCP_IP_MASK = DWORD
DHCP_RESUME_HANDLE = DWORD
DHCP_OPTION_ID = DWORD

class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('DataLength', DWORD),	('Data', PTR_DWORD),

    )
        
DHCP_CLIENT_UID = DHCP_BINARY_DATA

DhcpSubnetEnabled = ,
DhcpSubnetDisabled = ,
DhcpSubnetEnabledSwitched = ,
DhcpSubnetDisabledSwitched = 
        

DhcpIpRanges = ,
DhcpSecondaryHosts = ,
DhcpReservedIps = ,
DhcpExcludedIpRanges = ,
DhcpIpUsedClusters = ,
DhcpIpRangesDhcpOnly = ,
DhcpIpRangesDhcpBootp = ,
DhcpIpRangesBootpOnly = 
        

DhcpFullForce = ,
DhcpNoForce = 
        

DhcpUnaryElementTypeOption = 
        

DhcpByteOption = ,
DhcpWordOption = ,
DhcpDWordOption = ,
DhcpDWordDWordOption = ,
DhcpIpAddressOption = ,
DhcpStringDataOption = ,
DhcpBinaryDataOption = ,
DhcpEncapsulatedDataOption = 
        

DhcpDefaultOptions = ,
DhcpGlobalOptions = ,
DhcpSubnetOptions = ,
DhcpReservedOptions = 
        

DhcpClientIpAddress = ,
DhcpClientHardwareAddress = 
        

DhcpRegistryFix = 
        

NOQUARANTINE = 0,
RESTRICTEDACCESS = 0,
DROPPACKET = 0,
PROBATION = 0,
EXEMPT = 0,
DEFAULTQUARSETTING = 0
        

class DHCP_HOST_INFO(NDRSTRUCT):
    structure = (
        ('IpAddress', DHCP_IP_ADDRESS),('NetBiosName', LPWSTR),('HostName', LPWSTR),
    )
class LPDHCP_HOST_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_HOST_INFO),
    )    


class DHCP_SUBNET_INFO(NDRSTRUCT):
    structure = (
        ('SubnetAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('SubnetName', LPWSTR),('SubnetComment', LPWSTR),('PrimaryHost', DHCP_HOST_INFO),('SubnetState', DHCP_SUBNET_STATE),
    )
class LPDHCP_SUBNET_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_INFO),
    )    


class DHCP_IP_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_IP_ADDRESS),
    )
class LPDHCP_IP_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_ARRAY),
    )    


class DHCP_IP_RANGE(NDRSTRUCT):
    structure = (
        ('StartAddress', DHCP_IP_ADDRESS),('EndAddress', DHCP_IP_ADDRESS),
    )
class LPDHCP_IP_RANGE(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RANGE),
    )    


class DHCP_IP_RESERVATION(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IP_ADDRESS),('ReservedForClient', DHCP_CLIENT_UID),
    )
class LPDHCP_IP_RESERVATION(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RESERVATION),
    )    


class DHCP_IP_CLUSTER(NDRSTRUCT):
    structure = (
        ('ClusterAddress', DHCP_IP_ADDRESS),('ClusterMask', DWORD),
    )
class LPDHCP_IP_CLUSTER(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_CLUSTER),
    )    


class DHCP_BOOTP_IP_RANGE(NDRSTRUCT):
    structure = (
        ('StartAddress', DHCP_IP_ADDRESS),('EndAddress', DHCP_IP_ADDRESS),('BootpAllocated', ULONG),('MaxBootpAllowed', ULONG),
    )
class LPDHCP_BOOT_IP_RANGE(NDRPOINTER):
    referent = (
        ('Data', DHCP_BOOTP_IP_RANGE),
    )    


class ELEMENT(NDRUNION):
    union = {
        DhcpIpRanges: ('IpRange',DHCP_IP_RANGE),DhcpSecondaryHosts: ('SecondaryHost',DHCP_HOST_INFO),DhcpReservedIps: ('ReservedIp',DHCP_IP_RESERVATION),DhcpExcludedIpRanges: ('ExcludeIpRange',DHCP_IP_RANGE),DhcpIpUsedClusters: ('IpUsedCluster',DHCP_IP_CLUSTER),
    }
        

class DHCP_SUBNET_ELEMENT_DATA(NDRSTRUCT):
    structure = (
        ('ElementType', DHCP_SUBNET_ELEMENT_TYPE),('Element', ELEMENT),
    )
class LPDHCP_SUBNET_ELEMENT_DATA(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_DATA),
    )    


class DHCP_SUBNET_ELEMENT_INFO_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_SUBNET_ELEMENT_DATA),
    )
class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_INFO_ARRAY),
    )    


class DWORD_DWORD(NDRSTRUCT):
    structure = (
        ('DWord1', DWORD),('DWord2', DWORD),
    )
class LPDWORD_DWORD(NDRPOINTER):
    referent = (
        ('Data', DWORD_DWORD),
    )    


class ELEMENT(NDRUNION):
    union = {
        DhcpByteOption: ('ByteOption',BYTE),DhcpWordOption: ('WordOption',WORD),DhcpDWordOption: ('DWordOption',DWORD),DhcpDWordDWordOption: ('DWordDWordOption',DWORD_DWORD),DhcpIpAddressOption: ('IpAddressOption',DHCP_IP_ADDRESS),DhcpStringDataOption: ('StringDataOption',LPWSTR),DhcpBinaryDataOption: ('BinaryDataOption',DHCP_BINARY_DATA),DhcpEncapsulatedDataOption: ('EncapsulatedDataOption',DHCP_BINARY_DATA),DhcpIpv6AddressOption: ('Ipv6AddressDataOption',LPWSTR),
    }
        

class DHCP_OPTION_DATA_ELEMENT(NDRSTRUCT):
    structure = (
        ('OptionType', DHCP_OPTION_DATA_TYPE),('Element', ELEMENT),
    )
class LPDHCP_OPTION_DATA_ELEMENT(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_DATA_ELEMENT),
    )    


class DHCP_OPTION_DATA(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_OPTION_DATA_ELEMENT),
    )
class LPDHCP_OPTION_DATA(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_DATA),
    )    


class DHCP_OPTION(NDRSTRUCT):
    structure = (
        ('OptionID', DHCP_OPTION_ID),('OptionName', LPWSTR),('OptionComment', LPWSTR),('DefaultValue', DHCP_OPTION_DATA),('OptionType', DHCP_OPTION_TYPE),
    )
class LPDHCP_OPTION(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION),
    )    


class DHCP_RESERVED_SCOPE(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IP_ADDRESS),('ReservedIpSubnetAddress', DHCP_IP_ADDRESS),
    )
class LPDHCP_RESERVED_SCOPE(NDRPOINTER):
    referent = (
        ('Data', DHCP_RESERVED_SCOPE),
    )    


class SCOPEINFO(NDRUNION):
    union = {
        DhcpSubnetOptions: ('SubnetScopeInfo',DHCP_IP_ADDRESS),DhcpReservedOptions: ('ReservedScopeInfo',DHCP_RESERVED_SCOPE),DhcpMScopeOptions: ('MScopeInfo',LPWSTR),
    }
        

class DHCP_OPTION_SCOPE_INFO(NDRSTRUCT):
    structure = (
        ('ScopeType', DHCP_OPTION_SCOPE_TYPE),('ScopeInfo', SCOPEINFO),
    )
class LPDHCP_OPTION_SCOPE_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_SCOPE_INFO),
    )    


class DHCP_OPTION_VALUE(NDRSTRUCT):
    structure = (
        ('OptionID', DHCP_OPTION_ID),('Value', DHCP_OPTION_DATA),
    )
class LPDHCP_OPTION_VALUE(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_VALUE),
    )    


class DHCP_OPTION_VALUE_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Values', LPDHCP_OPTION_VALUE),
    )
class LPDHCP_OPTION_VALUE_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_VALUE_ARRAY),
    )    


class DATE_TIME(NDRSTRUCT):
    structure = (
        ('dwLowDateTime', DWORD),('dwHighDateTime', DWORD),
    )
class LPDATE_TIME(NDRPOINTER):
    referent = (
        ('Data', DATE_TIME),
    )    


class DHCP_CLIENT_INFO(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),
    )
class LPDHCP_CLIENT_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO),
    )    


class SEARCHINFO(NDRUNION):
    union = {
        DhcpClientIpAddress: ('ClientIpAddress',DHCP_IP_ADDRESS),DhcpClientHardwareAddress: ('ClientHardwareAddress',DHCP_CLIENT_UID),DhcpClientName: ('ClientName',LPWSTR),
    }
        

class DHCP_SEARCH_INFO(NDRSTRUCT):
    structure = (
        ('SearchType', DHCP_SEARCH_INFO_TYPE),('SearchInfo', SEARCHINFO),
    )
class LPDHCP_SEARCH_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_SEARCH_INFO),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = DHCP_OPTION_VALUE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumOptions', DWORD),	('Options', PTR_DWORD),

    )
        

class SCOPE_MIB_INFO(NDRSTRUCT):
    structure = (
        ('Subnet', DHCP_IP_ADDRESS),('NumAddressesInuse', DWORD),('NumAddressesFree', DWORD),('NumPendingOffers', DWORD),
    )
class LPSCOPE_MIB_INFO(NDRPOINTER):
    referent = (
        ('Data', SCOPE_MIB_INFO),
    )    


class DHCP_MIB_INFO(NDRSTRUCT):
    structure = (
        ('Discovers', DWORD),('Offers', DWORD),('Requests', DWORD),('Acks', DWORD),('Naks', DWORD),('Declines', DWORD),('Releases', DWORD),('ServerStartTime', DATE_TIME),('Scopes', DWORD),('ScopeInfo', LPSCOPE_MIB_INFO),
    )
class LPDHCP_MIB_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_MIB_INFO),
    )    


class DHCP_OPTION_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Options', LPDHCP_OPTION),
    )
class LPDHCP_OPTION_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_ARRAY),
    )    


class DHCP_SERVER_CONFIG_INFO(NDRSTRUCT):
    structure = (
        ('APIProtocolSupport', DWORD),('DatabaseName', LPWSTR),('DatabasePath', LPWSTR),('BackupPath', LPWSTR),('BackupInterval', DWORD),('DatabaseLoggingFlag', DWORD),('RestoreFlag', DWORD),('DatabaseCleanupInterval', DWORD),('DebugFlag', DWORD),
    )
class LPDHCP_SERVER_CONFIG_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_SERVER_CONFIG_INFO),
    )    


class DHCP_SCAN_ITEM(NDRSTRUCT):
    structure = (
        ('IpAddress', DHCP_IP_ADDRESS),('ScanFlag', DHCP_SCAN_FLAG),
    )
class LPDHCP_SCAN_ITEM(NDRPOINTER):
    referent = (
        ('Data', DHCP_SCAN_ITEM),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = DHCP_SCAN_ITEM

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumScanItems', DWORD),	('ScanItems', PTR_DWORD),

    )
        

class DHCP_IP_RESERVATION_V4(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IP_ADDRESS),('ReservedForClient', DHCP_CLIENT_UID),('bAllowedClientTypes', BYTE),
    )
class LPDHCP_IP_RESERVATION_V4(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RESERVATION_V4),
    )    


class ELEMENT(NDRUNION):
    union = {
        DhcpIpRanges: ('IpRange',DHCP_IP_RANGE),DhcpSecondaryHosts: ('SecondaryHost',DHCP_HOST_INFO),DhcpReservedIps: ('ReservedIp',DHCP_IP_RESERVATION_V4),DhcpExcludedIpRanges: ('ExcludeIpRange',DHCP_IP_RANGE),DhcpIpUsedClusters: ('IpUsedCluster',DHCP_IP_CLUSTER),
    }
        

class DHCP_SUBNET_ELEMENT_DATA_V4(NDRSTRUCT):
    structure = (
        ('ElementType', DHCP_SUBNET_ELEMENT_TYPE),('Element', ELEMENT),
    )
class LPDHCP_SUBNET_ELEMENT_DATA_V4(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_DATA_V4),
    )    


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_SUBNET_ELEMENT_DATA_V4),
    )
class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4),
    )    


class DHCP_CLIENT_INFO_V4(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),
    )
class LPDHCP_CLIENT_INFO_V4(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_V4),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_V4

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_SUPER_SCOPE_TABLE_ENTRY(NDRSTRUCT):
    structure = (
        ('SubnetAddress', DHCP_IP_ADDRESS),('SuperScopeNumber', DWORD),('NextInSuperScope', DWORD),('SuperScopeName', LPWSTR),
    )
class LPDHCP_SUPER_SCOPE_TABLE_ENTRY(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUPER_SCOPE_TABLE_ENTRY),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = DHCP_SUPER_SCOPE_TABLE_ENTRY

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cEntries', DWORD),	('pEntries', PTR_DWORD),

    )
        

class DATA_BOOL(NDRUniConformantArray):
    item = WCHAR

class PTR_BOOL(NDRPOINTER):
    referent = (
        ('Data', DATA_BOOL),
    )

class BOOL(NDRSTRUCT):
    structure = (
	('APIProtocolSupport', DWORD),	('DatabaseName', LPWSTR),	('DatabasePath', LPWSTR),	('BackupPath', LPWSTR),	('BackupInterval', DWORD),	('DatabaseLoggingFlag', DWORD),	('RestoreFlag', DWORD),	('DatabaseCleanupInterval', DWORD),	('DebugFlag', DWORD),	('dwPingRetries', DWORD),	('cbBootTableString', DWORD),	('wszBootTableString', PTR_DWORD),
	('fAuditLog', BOOL),
    )
        

class DATA_BOOL(NDRUniConformantArray):
    item = WCHAR

class PTR_BOOL(NDRPOINTER):
    referent = (
        ('Data', DATA_BOOL),
    )

class BOOL(NDRSTRUCT):
    structure = (
	('APIProtocolSupport', DWORD),	('DatabaseName', LPWSTR),	('DatabasePath', LPWSTR),	('BackupPath', LPWSTR),	('BackupInterval', DWORD),	('DatabaseLoggingFlag', DWORD),	('RestoreFlag', DWORD),	('DatabaseCleanupInterval', DWORD),	('DebugFlag', DWORD),	('dwPingRetries', DWORD),	('cbBootTableString', DWORD),	('wszBootTableString', PTR_DWORD),
	('fAuditLog', BOOL),	('QuarantineOn', BOOL),	('QuarDefFail', DWORD),	('QuarRuntimeStatus', BOOL),
    )
        

class SCOPE_MIB_INFO_VQ(NDRSTRUCT):
    structure = (
        ('Subnet', DHCP_IP_ADDRESS),('NumAddressesInuse', DWORD),('NumAddressesFree', DWORD),('NumPendingOffers', DWORD),('QtnNumLeases', DWORD),('QtnPctQtnLeases', DWORD),('QtnProbationLeases', DWORD),('QtnNonQtnLeases', DWORD),('QtnExemptLeases', DWORD),('QtnCapableClients', DWORD),
    )
class LPSCOPE_MIB_INFO_VQ(NDRPOINTER):
    referent = (
        ('Data', SCOPE_MIB_INFO_VQ),
    )    


class DHCP_MIB_INFO_VQ(NDRSTRUCT):
    structure = (
        ('Discovers', DWORD),('Offers', DWORD),('Requests', DWORD),('Acks', DWORD),('Naks', DWORD),('Declines', DWORD),('Releases', DWORD),('ServerStartTime', DATE_TIME),('QtnNumLeases', DWORD),('QtnPctQtnLeases', DWORD),('QtnProbationLeases', DWORD),('QtnNonQtnLeases', DWORD),('QtnExemptLeases', DWORD),('QtnCapableClients', DWORD),('QtnIASErrors', DWORD),('Scopes', DWORD),('ScopeInfo', LPSCOPE_MIB_INFO_VQ),
    )
class LPDHCP_MIB_INFO_VQ(NDRPOINTER):
    referent = (
        ('Data', DHCP_MIB_INFO_VQ),
    )    


class DHCP_CLIENT_INFO_VQ(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),('Status', QUARANTINESTATUS),('ProbationEnds', DATE_TIME),('QuarantineCapable', BOOL),
    )
class LPDHCP_CLIENT_INFO_VQ(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_VQ),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_VQ

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_SUBNET_INFO_VQ(NDRSTRUCT):
    structure = (
        ('SubnetAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('SubnetName', LPWSTR),('SubnetComment', LPWSTR),('PrimaryHost', DHCP_HOST_INFO),('SubnetState', DHCP_SUBNET_STATE),('QuarantineOn', DWORD),('Reserved1', DWORD),('Reserved2', DWORD),('Reserved3', INT64),('Reserved4', INT64),
    )
class LPDHCP_SUBNET_INFO_VQ(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_INFO_VQ),
    )    

LPWSTR_RPC_STRING = LPWSTR
DHCP_ATTRIB_ID = ULONG
PDHCP_ATTRIB_ID = ULONG
LPDHCP_ATTRIB_ID = ULONG

DhcpDefaultOptions6 = ,
DhcpScopeOptions6 = ,
DhcpReservedOptions6 = 
        

Dhcpv6IpRanges = ,
Dhcpv6ReservedIps = 
        

Dhcpv6ClientIpAddress = ,
Dhcpv6ClientDUID = 
        

class DHCP_IPV6_ADDRESS(NDRSTRUCT):
    structure = (
        ('HighOrderBits', ULONGLONG),('LowOrderBits', ULONGLONG),
    )
class LPDHCP_IPV6_ADDRESS(NDRPOINTER):
    referent = (
        ('Data', DHCP_IPV6_ADDRESS),
    )    
class PDHCP_IPV6_ADDRESS(NDRPOINTER):
    referent = (
        ('Data', DHCP_IPV6_ADDRESS),
    )    


class DHCP_CLIENT_INFO_V5(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),
    )
class LPDHCP_CLIENT_INFO_V5(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_V5),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_V5

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_MSCOPE_INFO(NDRSTRUCT):
    structure = (
        ('MScopeName', LPWSTR),('MScopeComment', LPWSTR),('MScopeId', DWORD),('MScopeAddressPolicy', DWORD),('PrimaryHost', DHCP_HOST_INFO),('MScopeState', DHCP_SUBNET_STATE),('MScopeFlags', DWORD),('ExpiryTime', DATE_TIME),('LangTag', LPWSTR),('TTL', BYTE),
    )
class LPDHCP_MSCOPE_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_MSCOPE_INFO),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPWSTR

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('pMScopeNames', PTR_DWORD),

    )
        

class DHCP_MCLIENT_INFO(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('MScopeId', DWORD),('ClientId', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientLeaseStarts', DATE_TIME),('ClientLeaseEnds', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('AddressFlags', DWORD),('AddressState', BYTE),
    )
class LPDHCP_MCLIENT_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_MCLIENT_INFO),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_MCLIENT_INFO

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_RESERVED_SCOPE6(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IPV6_ADDRESS),('ReservedIpSubnetAddress', DHCP_IPV6_ADDRESS),
    )
class LPDHCP_RESERVED_SCOPE6(NDRPOINTER):
    referent = (
        ('Data', DHCP_RESERVED_SCOPE6),
    )    


class SCOPEINFO(NDRUNION):
    union = {
        DhcpScopeOptions6: ('SubnetScopeInfo',DHCP_IPV6_ADDRESS),DhcpReservedOptions6: ('ReservedScopeInfo',DHCP_RESERVED_SCOPE6),
    }
        

class DHCP_OPTION_SCOPE_INFO6(NDRSTRUCT):
    structure = (
        ('ScopeType', DHCP_OPTION_SCOPE_TYPE6),('ScopeInfo', SCOPEINFO),
    )
class LPDHCP_OPTION_SCOPE_INFO6(NDRPOINTER):
    referent = (
        ('Data', DHCP_OPTION_SCOPE_INFO6),
    )    


class DHCP_CLASS_INFO(NDRSTRUCT):
    structure = (
        ('ClassName', LPWSTR),('ClassComment', LPWSTR),('ClassDataLength', DWORD),('IsVendor', BOOL),('Flags', DWORD),('ClassData', LPBYTE),
    )
class LPDHCP_CLASS_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLASS_INFO),
    )    


class DHCP_CLASS_INFO_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Classes', LPDHCP_CLASS_INFO),
    )
class LPDHCP_CLASS_INFO_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLASS_INFO_ARRAY),
    )    


class VENDOROPTIONS(NDRSTRUCT):
    structure = (
        ('Option', DHCP_OPTION),('VendorName', LPWSTR),('ClassName', LPWSTR),
    )


class DHCP_ALL_OPTIONS(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('NonVendorOptions', LPDHCP_OPTION_ARRAY),('NumVendorOptions', DWORD),('VENDOROPTIONS', VENDOROPTIONS),
    )
class LPDHCP_ALL_OPTIONS(NDRPOINTER):
    referent = (
        ('Data', DHCP_ALL_OPTIONS),
    )    


class OPTIONS(NDRSTRUCT):
    structure = (
        ('ClassName', LPWSTR),('VendorName', LPWSTR),('IsVendor', BOOL),('OptionsArray', LPDHCP_OPTION_VALUE_ARRAY),
    )


class DHCP_ALL_OPTION_VALUES(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('NumElements', DWORD),('OPTIONS', OPTIONS),
    )
class LPDHCP_ALL_OPTION_VALUES(NDRPOINTER):
    referent = (
        ('Data', DHCP_ALL_OPTION_VALUES),
    )    


class MSCOPE_MIB_INFO(NDRSTRUCT):
    structure = (
        ('MScopeId', DWORD),('MScopeName', LPWSTR),('NumAddressesInuse', DWORD),('NumAddressesFree', DWORD),('NumPendingOffers', DWORD),
    )
class LPMSCOPE_MIB_INFO(NDRPOINTER):
    referent = (
        ('Data', MSCOPE_MIB_INFO),
    )    


class DHCP_MCAST_MIB_INFO(NDRSTRUCT):
    structure = (
        ('Discovers', DWORD),('Offers', DWORD),('Requests', DWORD),('Renews', DWORD),('Acks', DWORD),('Naks', DWORD),('Releases', DWORD),('Informs', DWORD),('ServerStartTime', DATE_TIME),('Scopes', DWORD),('ScopeInfo', LPMSCOPE_MIB_INFO),
    )
class LPDHCP_MCAST_MIB_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_MCAST_MIB_INFO),
    )    


class U0(NDRUNION):
    union = {
        DHCP_ATTRIB_TYPE_BOOL: ('DhcpAttribBool',BOOL),DHCP_ATTRIB_TYPE_ULONG: ('DhcpAttribUlong',ULONG),
    }
        

class DHCP_ATTRIB(NDRSTRUCT):
    structure = (
        ('DhcpAttribId', DHCP_ATTRIB_ID),('DhcpAttribType', ULONG),('u0', U0),
    )
class PDHCP_ATTRIB(NDRPOINTER):
    referent = (
        ('Data', DHCP_ATTRIB),
    )    
class LPDHCP_ATTRIB(NDRPOINTER):
    referent = (
        ('Data', DHCP_ATTRIB),
    )    


class DHCP_ATTRIB_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', ULONG),('DhcpAttribs', LPDHCP_ATTRIB),
    )
class PDHCP_ATTRIB_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_ATTRIB_ARRAY),
    )    
class LPDHCP_ATTRIB_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_ATTRIB_ARRAY),
    )    


class ELEMENT(NDRUNION):
    union = {
        DhcpIpRanges: ('IpRange',DHCP_BOOTP_IP_RANGE),DhcpSecondaryHosts: ('SecondaryHost',DHCP_HOST_INFO),DhcpReservedIps: ('ReservedIp',DHCP_IP_RESERVATION_V4),DhcpExcludedIpRanges: ('ExcludeIpRange',DHCP_IP_RANGE),DhcpIpUsedClusters: ('IpUsedCluster',DHCP_IP_CLUSTER),
    }
        

class DHCP_SUBNET_ELEMENT_DATA_V5(NDRSTRUCT):
    structure = (
        ('ElementType', DHCP_SUBNET_ELEMENT_TYPE),('Element', ELEMENT),
    )
class LPDHCP_SUBNET_ELEMENT_DATA_V5(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_DATA_V5),
    )    


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_SUBNET_ELEMENT_DATA_V5),
    )
class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5),
    )    


class DHCP_BIND_ELEMENT(NDRSTRUCT):
    structure = (
        ('Flags', ULONG),('fBoundToDHCPServer', BOOL),('AdapterPrimaryAddress', DHCP_IP_ADDRESS),('AdapterSubnetAddress', DHCP_IP_ADDRESS),('IfDescription', LPWSTR),('IfIdSize', ULONG),('IfId', LPBYTE),
    )
class LPDHCP_BIND_ELEMENT(NDRPOINTER):
    referent = (
        ('Data', DHCP_BIND_ELEMENT),
    )    


class DHCP_BIND_ELEMENT_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_BIND_ELEMENT),
    )
class LPDHCP_BIND_ELEMENT_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_BIND_ELEMENT_ARRAY),
    )    


class DHCP_SERVER_SPECIFIC_STRINGS(NDRSTRUCT):
    structure = (
        ('DefaultVendorClassName', LPWSTR),('DefaultUserClassName', LPWSTR),
    )
class LPDHCP_SERVER_SPECIFIC_STRINGS(NDRPOINTER):
    referent = (
        ('Data', DHCP_SERVER_SPECIFIC_STRINGS),
    )    


class SCOPE_MIB_INFO_V5(NDRSTRUCT):
    structure = (
        ('Subnet', DHCP_IP_ADDRESS),('NumAddressesInuse', DWORD),('NumAddressesFree', DWORD),('NumPendingOffers', DWORD),
    )
class LPSCOPE_MIB_INFO_V5(NDRPOINTER):
    referent = (
        ('Data', SCOPE_MIB_INFO_V5),
    )    


class DHCP_MIB_INFO_V5(NDRSTRUCT):
    structure = (
        ('Discovers', DWORD),('Offers', DWORD),('Requests', DWORD),('Acks', DWORD),('Naks', DWORD),('Declines', DWORD),('Releases', DWORD),('ServerStartTime', DATE_TIME),('QtnNumLeases', DWORD),('QtnPctQtnLeases', DWORD),('QtnProbationLeases', DWORD),('QtnNonQtnLeases', DWORD),('QtnExemptLeases', DWORD),('QtnCapableClients', DWORD),('QtnIASErrors', DWORD),('DelayedOffers', DWORD),('ScopesWithDelayedOffers', DWORD),('Scopes', DWORD),('ScopeInfo', LPSCOPE_MIB_INFO_V5),
    )
class LPDHCP_MIB_INFO_V5(NDRPOINTER):
    referent = (
        ('Data', DHCP_MIB_INFO_V5),
    )    


Deny = 
        

class DHCP_ADDR_PATTERN(NDRSTRUCT):
    structure = (
        ('MatchHWType', BOOL),('HWType', BYTE),('IsWildcard', BOOL),('Length', BYTE),('Pattern', BYTE),
    )
class LPDHCP_ADDR_PATTERN(NDRPOINTER):
    referent = (
        ('Data', DHCP_ADDR_PATTERN),
    )    


class DHCP_FILTER_ADD_INFO(NDRSTRUCT):
    structure = (
        ('AddrPatt', DHCP_ADDR_PATTERN),('Comment', LPWSTR),('ListType', DHCP_FILTER_LIST_TYPE),
    )
class LPDHCP_FILTER_ADD_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_FILTER_ADD_INFO),
    )    


class DHCP_FILTER_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('EnforceAllowList', BOOL),('EnforceDenyList', BOOL),
    )
class LPDHCP_FILTER_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_FILTER_GLOBAL_INFO),
    )    


class DHCP_FILTER_RECORD(NDRSTRUCT):
    structure = (
        ('AddrPatt', DHCP_ADDR_PATTERN),('Comment', LPWSTR),
    )
class LPDHCP_FILTER_RECORD(NDRPOINTER):
    referent = (
        ('Data', DHCP_FILTER_RECORD),
    )    


class DHCP_FILTER_ENUM_INFO(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('pEnumRecords', LPDHCP_FILTER_RECORD),
    )
class LPDHCP_FILTER_ENUM_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_FILTER_ENUM_INFO),
    )    


class DHCP_SUBNET_INFO_V6(NDRSTRUCT):
    structure = (
        ('SubnetAddress', DHCP_IPV6_ADDRESS),('Prefix', ULONG),('Preference', USHORT),('SubnetName', LPWSTR),('SubnetComment', LPWSTR),('State', DWORD),('ScopeId', DWORD),
    )
class PDHCP_SUBNET_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_INFO_V6),
    )    
class LPDHCP_SUBNET_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_INFO_V6),
    )    


class DHCPV6_IP_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_IPV6_ADDRESS),
    )
class LPDHCPV6_IP_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_IP_ARRAY),
    )    


class DHCP_IP_RANGE_V6(NDRSTRUCT):
    structure = (
        ('StartAddress', DHCP_IPV6_ADDRESS),('EndAddress', DHCP_IPV6_ADDRESS),
    )
class LPDHCP_IP_RANGE_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RANGE_V6),
    )    


class DHCP_IP_RESERVATION_V6(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IPV6_ADDRESS),('ReservedForClient', DHCP_CLIENT_UID),('InterfaceId', DWORD),
    )
class LPDHCP_IP_RESERVATION_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RESERVATION_V6),
    )    


class ELEMENT(NDRUNION):
    union = {
        Dhcpv6IpRanges: ('IpRange',DHCP_IP_RANGE_V6),Dhcpv6ReservedIps: ('ReservedIp',DHCP_IP_RESERVATION_V6),Dhcpv6ExcludedIpRanges: ('ExcludeIpRange',DHCP_IP_RANGE_V6),
    }
        

class DHCP_SUBNET_ELEMENT_DATA_V6(NDRSTRUCT):
    structure = (
        ('ElementType', DHCP_SUBNET_ELEMENT_TYPE_V6),('Element', ELEMENT),
    )
class LPDHCP_SUBNET_ELEMENT_DATA_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_DATA_V6),
    )    


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_SUBNET_ELEMENT_DATA_V6),
    )
class LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6),
    )    

DHCP_RESUME_IPV6_HANDLE = DHCP_IPV6_ADDRESS

class DHCP_HOST_INFO_V6(NDRSTRUCT):
    structure = (
        ('IpAddress', DHCP_IPV6_ADDRESS),('NetBiosName', LPWSTR),('HostName', LPWSTR),
    )
class LPDHCP_HOST_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_HOST_INFO_V6),
    )    


class DHCP_CLIENT_INFO_V6(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IPV6_ADDRESS),('ClientDUID', DHCP_CLIENT_UID),('AddressType', DWORD),('IAID', DWORD),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientValidLeaseExpires', DATE_TIME),('ClientPrefLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO_V6),
    )
class LPDHCP_CLIENT_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_V6),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_V6

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_SERVER_CONFIG_INFO_V6(NDRSTRUCT):
    structure = (
        ('UnicastFlag', BOOL),('RapidCommitFlag', BOOL),('PreferredLifetime', DWORD),('ValidLifetime', DWORD),('T1', DWORD),('T2', DWORD),('PreferredLifetimeIATA', DWORD),('ValidLifetimeIATA', DWORD),('fAuditLog', BOOL),
    )
class LPDHCP_SERVER_CONFIG_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SERVER_CONFIG_INFO_V6),
    )    


class SCOPE_MIB_INFO_V6(NDRSTRUCT):
    structure = (
        ('Subnet', DHCP_IPV6_ADDRESS),('NumAddressesInuse', ULONGLONG),('NumAddressesFree', ULONGLONG),('NumPendingAdvertises', ULONGLONG),
    )
class LPSCOPE_MIB_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', SCOPE_MIB_INFO_V6),
    )    


class DHCP_MIB_INFO_V6(NDRSTRUCT):
    structure = (
        ('Solicits', DWORD),('Advertises', DWORD),('Requests', DWORD),('Renews', DWORD),('Rebinds', DWORD),('Replies', DWORD),('Confirms', DWORD),('Declines', DWORD),('Releases', DWORD),('Informs', DWORD),('ServerStartTime', DATE_TIME),('Scopes', DWORD),('ScopeInfo', LPSCOPE_MIB_INFO_V6),
    )
class LPDHCP_MIB_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_MIB_INFO_V6),
    )    


class DHCPV6_BIND_ELEMENT(NDRSTRUCT):
    structure = (
        ('Flags', ULONG),('fBoundToDHCPServer', BOOL),('AdapterPrimaryAddress', DHCP_IPV6_ADDRESS),('AdapterSubnetAddress', DHCP_IPV6_ADDRESS),('IfDescription', LPWSTR),('IpV6IfIndex', DWORD),('IfIdSize', ULONG),('IfId', LPBYTE),
    )
class LPDHCPV6_BIND_ELEMENT(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_BIND_ELEMENT),
    )    


class DHCPV6_BIND_ELEMENT_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCPV6_BIND_ELEMENT),
    )
class LPDHCPV6_BIND_ELEMENT_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_BIND_ELEMENT_ARRAY),
    )    


class SEARCHINFO(NDRUNION):
    union = {
        Dhcpv6ClientIpAddress: ('ClientIpAddress',DHCP_IPV6_ADDRESS),Dhcpv6ClientDUID: ('ClientDUID',DHCP_CLIENT_UID),Dhcpv6ClientName: ('ClientName',LPWSTR),
    }
        

class DHCP_SEARCH_INFO_V6(NDRSTRUCT):
    structure = (
        ('SearchType', DHCP_SEARCH_INFO_TYPE_V6),('SearchInfo', SEARCHINFO),
    )
class LPDHCP_SEARCH_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_SEARCH_INFO_V6),
    )    


class DHCP_CLASS_INFO_V6(NDRSTRUCT):
    structure = (
        ('ClassName', LPWSTR),('ClassComment', LPWSTR),('ClassDataLength', DWORD),('IsVendor', BOOL),('EnterpriseNumber', DWORD),('Flags', DWORD),('ClassData', LPBYTE),
    )
class LPDHCP_CLASS_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLASS_INFO_V6),
    )    


class DHCP_CLASS_INFO_ARRAY_V6(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Classes', LPDHCP_CLASS_INFO_V6),
    )
class LPDHCP_CLASS_INFO_ARRAY_V6(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLASS_INFO_ARRAY_V6),
    )    


class DHCP_CLIENT_FILTER_STATUS_INFO(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),('Status', QUARANTINESTATUS),('ProbationEnds', DATE_TIME),('QuarantineCapable', BOOL),('FilterStatus', DWORD),
    )
class LPDHCP_CLIENT_FILTER_STATUS_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_FILTER_STATUS_INFO),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_FILTER_STATUS_INFO

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

LoadBalance = 0,
HotStandby = 1
        

PrimaryServer = 0,
SecondaryServer = 1
        

NO_STATE = 0,
INIT = 0,
STARTUP = 0,
NORMAL = 0,
COMMUNICATION_INT = 0,
PARTNER_DOWN = 0,
POTENTIAL_CONFLICT = 0,
CONFLICT_DONE = 0,
RESOLUTION_INT = 0,
RECOVER = 0,
RECOVER_WAIT = 0,
RECOVER_DONE = 0
        

class DHCP_FAILOVER_RELATIONSHIP(NDRSTRUCT):
    structure = (
        ('primaryServer', DHCP_IP_ADDRESS),('secondaryServer', DHCP_IP_ADDRESS),('mode', DHCP_FAILOVER_MODE),('serverType', DHCP_FAILOVER_SERVER),('state', FSM_STATE),('prevState', FSM_STATE),('mclt', DWORD),('safePeriod', DWORD),('relationshipName', LPWSTR),('primaryServerName', LPWSTR),('secondaryServerName', LPWSTR),('pScopes', LPDHCP_IP_ARRAY),('percentage', BYTE),('pSharedSecret', LPWSTR),
    )
class LPDHCP_FAILOVER_RELATIONSHIP(NDRPOINTER):
    referent = (
        ('Data', DHCP_FAILOVER_RELATIONSHIP),
    )    


class DHCP_FAILOVER_RELATIONSHIP_ARRAY(NDRSTRUCT):
    structure = (
        ('numElements', DWORD),('pRelationships', LPDHCP_FAILOVER_RELATIONSHIP),
    )
class LPDHCP_FAILOVER_RELATIONSHIP_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_FAILOVER_RELATIONSHIP_ARRAY),
    )    


class DHCP_FAILOVER_STATISTICS(NDRSTRUCT):
    structure = (
        ('numAddr', DWORD),('addrFree', DWORD),('addrInUse', DWORD),('partnerAddrFree', DWORD),('thisAddrFree', DWORD),('partnerAddrInUse', DWORD),('thisAddrInUse', DWORD),
    )
class LPDHCP_FAILOVER_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', DHCP_FAILOVER_STATISTICS),
    )    


class DHCPV4_FAILOVER_CLIENT_INFO(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),('Status', QUARANTINESTATUS),('ProbationEnds', DATE_TIME),('QuarantineCapable', BOOL),('SentPotExpTime', DWORD),('AckPotExpTime', DWORD),('RecvPotExpTime', DWORD),('StartTime', DWORD),('CltLastTransTime', DWORD),('LastBndUpdTime', DWORD),('bndMsgStatus', DWORD),('PolicyName', LPWSTR),('flags', BYTE),
    )
class LPDHCPV4_FAILOVER_CLIENT_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCPV4_FAILOVER_CLIENT_INFO),
    )    


class DHCP_IP_RESERVATION_INFO(NDRSTRUCT):
    structure = (
        ('ReservedIpAddress', DHCP_IP_ADDRESS),('ReservedForClient', DHCP_CLIENT_UID),('ReservedClientName', LPWSTR),('ReservedClientDesc', LPWSTR),('bAllowedClientTypes', BYTE),('fOptionsPresent', BYTE),
    )
class LPDHCP_IP_RESERVATION_INFO(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RESERVATION_INFO),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_IP_RESERVATION_INFO

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Elements', PTR_DWORD),

    )
        

class OPTIONS(NDRSTRUCT):
    structure = (
        ('PolicyName', LPWSTR),('VendorName', LPWSTR),('IsVendor', BOOL),('OptionsArray', LPDHCP_OPTION_VALUE_ARRAY),
    )


class DHCP_ALL_OPTION_VALUES_PB(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('NumElements', DWORD),('OPTIONS', OPTIONS),
    )
class LPDHCP_ALL_OPTION_VALUES_PB(NDRPOINTER):
    referent = (
        ('Data', DHCP_ALL_OPTION_VALUES_PB),
    )    


DhcpAttrHWAddr = ,
DhcpAttrOption = ,
DhcpAttrSubOption = ,
DhcpAttrFqdn = ,
DhcpAttrFqdnSingleLabel = 
        

DhcpCompEqual = ,
DhcpCompNotEqual = ,
DhcpCompBeginsWith = ,
DhcpCompNotBeginWith = ,
DhcpCompEndsWith = 
        

DhcpLogicalOr = ,
DhcpLogicalAnd = 
        

DhcpUpdatePolicyName = 1,
DhcpUpdatePolicyOrder = 2,
DhcpUpdatePolicyExpr = 4,
DhcpUpdatePolicyRanges = 8,
DhcpUpdatePolicyDescr = 16,
DhcpUpdatePolicyStatus = 32,
DhcpUpdatePolicyDnsSuffix = 64
        

class DHCP_POL_COND(NDRSTRUCT):
    structure = (
        ('ParentExpr', DWORD),('Type', DHCP_POL_ATTR_TYPE),('OptionID', DWORD),('SubOptionID', DWORD),('VendorName', LPWSTR),('Operator', DHCP_POL_COMPARATOR),('Value', LPBYTE),('ValueLength', DWORD),
    )
class PDHCP_POL_COND(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_COND),
    )    
class LPDHCP_POL_COND(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_COND),
    )    


class DHCP_POL_COND_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_POL_COND),
    )
class PDHCP_POL_COND_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_COND_ARRAY),
    )    
class LPDHCP_POL_COND_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_COND_ARRAY),
    )    


class DHCP_POL_EXPR(NDRSTRUCT):
    structure = (
        ('ParentExpr', DWORD),('Operator', DHCP_POL_LOGIC_OPER),
    )
class PDHCP_POL_EXPR(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_EXPR),
    )    
class LPDHCP_POL_EXPR(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_EXPR),
    )    


class DHCP_POL_EXPR_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_POL_EXPR),
    )
class PDHCP_POL_EXPR_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_EXPR_ARRAY),
    )    
class LPDHCP_POL_EXPR_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POL_EXPR_ARRAY),
    )    


class DHCP_IP_RANGE_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_IP_RANGE),
    )
class PDHCP_IP_RANGE_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RANGE_ARRAY),
    )    
class LPDHCP_IP_RANGE_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_IP_RANGE_ARRAY),
    )    


class DHCP_POLICY(NDRSTRUCT):
    structure = (
        ('PolicyName', LPWSTR),('IsGlobalPolicy', BOOL),('Subnet', DHCP_IP_ADDRESS),('ProcessingOrder', DWORD),('Conditions', LPDHCP_POL_COND_ARRAY),('Expressions', LPDHCP_POL_EXPR_ARRAY),('Ranges', LPDHCP_IP_RANGE_ARRAY),('Description', LPWSTR),('Enabled', BOOL),
    )
class PDHCP_POLICY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY),
    )    
class LPDHCP_POLICY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY),
    )    


class DHCP_POLICY_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_POLICY),
    )
class PDHCP_POLICY_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_ARRAY),
    )    
class LPDHCP_POLICY_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_ARRAY),
    )    


class DHCPV6_STATELESS_PARAMS(NDRSTRUCT):
    structure = (
        ('Status', BOOL),('PurgeInterval', DWORD),
    )
class PDHCPV6_STATELESS_PARAMS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_PARAMS),
    )    
class LPDHCPV6_STATELESS_PARAMS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_PARAMS),
    )    


class DHCPV6_STATELESS_SCOPE_STATS(NDRSTRUCT):
    structure = (
        ('SubnetAddress', DHCP_IPV6_ADDRESS),('NumStatelessClientsAdded', ULONGLONG),('NumStatelessClientsRemoved', ULONGLONG),
    )
class PDHCPV6_STATELESS_SCOPE_STATS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_SCOPE_STATS),
    )    
class LPDHCPV6_STATELESS_SCOPE_STATS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_SCOPE_STATS),
    )    


class DHCPV6_STATELESS_STATS(NDRSTRUCT):
    structure = (
        ('NumScopes', DWORD),('ScopeStats', LPDHCPV6_STATELESS_SCOPE_STATS),
    )
class PDHCPV6_STATELESS_STATS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_STATS),
    )    
class LPDHCPV6_STATELESS_STATS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6_STATELESS_STATS),
    )    


class DHCP_CLIENT_INFO_PB(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),('Status', QUARANTINESTATUS),('ProbationEnds', DATE_TIME),('QuarantineCapable', BOOL),('FilterStatus', DWORD),('PolicyName', LPWSTR),
    )
class LPDHCP_CLIENT_INFO_PB(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_PB),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_PB

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

DhcpPropTypeByte = ,
DhcpPropTypeWord = ,
DhcpPropTypeDword = ,
DhcpPropTypeString = ,
DhcpPropTypeBinary = 
        

DhcpPropIdPolicyDnsSuffix = ,
DhcpPropIdClientAddressStateEx = 
        

class VALUE(NDRUNION):
    union = {
        DhcpPropTypeByte: ('ByteValue',BYTE),DhcpPropTypeWord: ('WordValue',WORD),DhcpPropTypeDword: ('DWordValue',DWORD),DhcpPropTypeString: ('StringValue',LPWSTR),DhcpPropTypeBinary: ('BinaryValue',DHCP_BINARY_DATA),
    }
        

class DHCP_PROPERTY(NDRSTRUCT):
    structure = (
        ('ID', DHCP_PROPERTY_ID),('Type', DHCP_PROPERTY_TYPE),('Value', VALUE),
    )
class PDHCP_PROPERTY(NDRPOINTER):
    referent = (
        ('Data', DHCP_PROPERTY),
    )    
class LPDHCP_PROPERTY(NDRPOINTER):
    referent = (
        ('Data', DHCP_PROPERTY),
    )    


class DHCP_PROPERTY_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_PROPERTY),
    )
class PDHCP_PROPERTY_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_PROPERTY_ARRAY),
    )    
class LPDHCP_PROPERTY_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_PROPERTY_ARRAY),
    )    


class DHCP_CLIENT_INFO_EX(NDRSTRUCT):
    structure = (
        ('ClientIpAddress', DHCP_IP_ADDRESS),('SubnetMask', DHCP_IP_MASK),('ClientHardwareAddress', DHCP_CLIENT_UID),('ClientName', LPWSTR),('ClientComment', LPWSTR),('ClientLeaseExpires', DATE_TIME),('OwnerHost', DHCP_HOST_INFO),('bClientType', BYTE),('AddressState', BYTE),('Status', QUARANTINESTATUS),('ProbationEnds', DATE_TIME),('QuarantineCapable', BOOL),('FilterStatus', DWORD),('PolicyName', LPWSTR),('Properties', LPDHCP_PROPERTY_ARRAY),
    )
class LPDHCP_CLIENT_INFO_EX(NDRPOINTER):
    referent = (
        ('Data', DHCP_CLIENT_INFO_EX),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = LPDHCP_CLIENT_INFO_EX

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('NumElements', DWORD),	('Clients', PTR_DWORD),

    )
        

class DHCP_POLICY_EX(NDRSTRUCT):
    structure = (
        ('PolicyName', LPWSTR),('IsGlobalPolicy', BOOL),('Subnet', DHCP_IP_ADDRESS),('ProcessingOrder', DWORD),('Conditions', LPDHCP_POL_COND_ARRAY),('Expressions', LPDHCP_POL_EXPR_ARRAY),('Ranges', LPDHCP_IP_RANGE_ARRAY),('Description', LPWSTR),('Enabled', BOOL),('Properties', LPDHCP_PROPERTY_ARRAY),
    )
class PDHCP_POLICY_EX(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_EX),
    )    
class LPDHCP_POLICY_EX(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_EX),
    )    


class DHCP_POLICY_EX_ARRAY(NDRSTRUCT):
    structure = (
        ('NumElements', DWORD),('Elements', LPDHCP_POLICY_EX),
    )
class PDHCP_POLICY_EX_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_EX_ARRAY),
    )    
class LPDHCP_POLICY_EX_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DHCP_POLICY_EX_ARRAY),
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
    opnum = 0
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('SubnetInfo', LPDHCP_SUBNET_INFO),
    )

class R_DhcpCreateSubnetResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetSubnetInfo(NDRCALL):
    opnum = 1
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('SubnetInfo', LPDHCP_SUBNET_INFO),
    )

class R_DhcpSetSubnetInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetSubnetInfo(NDRCALL):
    opnum = 2
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpGetSubnetInfoResponse(NDRCALL):
    structure = (
		('SubnetInfo', LPDHCP_SUBNET_INFO),
    )
        

class R_DhcpEnumSubnets(NDRCALL):
    opnum = 3
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumInfo', LPDHCP_IP_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpAddSubnetElement(NDRCALL):
    opnum = 4
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('AddElementInfo', LPDHCP_SUBNET_ELEMENT_DATA),
    )

class R_DhcpAddSubnetElementResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetElements(NDRCALL):
    opnum = 5
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('EnumElementType', DHCP_SUBNET_ELEMENT_TYPE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetElementsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_SUBNET_ELEMENT_INFO_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpRemoveSubnetElement(NDRCALL):
    opnum = 6
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('RemoveElementInfo', LPDHCP_SUBNET_ELEMENT_DATA),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpRemoveSubnetElementResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteSubnet(NDRCALL):
    opnum = 7
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpDeleteSubnetResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpCreateOption(NDRCALL):
    opnum = 8
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpCreateOptionResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionInfo(NDRCALL):
    opnum = 9
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpSetOptionInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetOptionInfo(NDRCALL):
    opnum = 10
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
    )

class R_DhcpGetOptionInfoResponse(NDRCALL):
    structure = (
		('OptionInfo', LPDHCP_OPTION),
    )
        

class R_DhcpRemoveOption(NDRCALL):
    opnum = 11
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
    )

class R_DhcpRemoveOptionResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionValue(NDRCALL):
    opnum = 12
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValue', LPDHCP_OPTION_DATA),
    )

class R_DhcpSetOptionValueResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetOptionValue(NDRCALL):
    opnum = 13
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpGetOptionValueResponse(NDRCALL):
    structure = (
		('OptionValue', LPDHCP_OPTION_VALUE),
    )
        

class R_DhcpEnumOptionValues(NDRCALL):
    opnum = 14
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionValuesResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpRemoveOptionValue(NDRCALL):
    opnum = 15
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('OptionID', DHCP_OPTION_ID),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpRemoveOptionValueResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpCreateClientInfo(NDRCALL):
    opnum = 16
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO),
    )

class R_DhcpCreateClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetClientInfo(NDRCALL):
    opnum = 17
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO),
    )

class R_DhcpSetClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetClientInfo(NDRCALL):
    opnum = 18
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpGetClientInfoResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO),
    )
        

class R_DhcpDeleteClientInfo(NDRCALL):
    opnum = 19
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpDeleteClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetClients(NDRCALL):
    opnum = 20
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_ARRAY),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpGetClientOptions(NDRCALL):
    opnum = 21
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientIpAddress', DHCP_IP_ADDRESS),
		('ClientSubnetMask', DHCP_IP_MASK),
    )

class R_DhcpGetClientOptionsResponse(NDRCALL):
    structure = (
		('ClientOptions', LPDHCP_OPTION_LIST),
    )
        

class R_DhcpGetMibInfo(NDRCALL):
    opnum = 22
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetMibInfoResponse(NDRCALL):
    structure = (
		('MibInfo', LPDHCP_MIB_INFO),
    )
        

class R_DhcpEnumOptions(NDRCALL):
    opnum = 23
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('Options', LPDHCP_OPTION_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpSetOptionValues(NDRCALL):
    opnum = 24
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
    )

class R_DhcpSetOptionValuesResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpServerSetConfig(NDRCALL):
    opnum = 25
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FieldsToSet', DWORD),
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO),
    )

class R_DhcpServerSetConfigResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpServerGetConfig(NDRCALL):
    opnum = 26
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpServerGetConfigResponse(NDRCALL):
    structure = (
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO),
    )
        

class R_DhcpScanDatabase(NDRCALL):
    opnum = 27
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('FixFlag', DWORD),
    )

class R_DhcpScanDatabaseResponse(NDRCALL):
    structure = (
		('ScanList', LPDHCP_SCAN_LIST),
    )
        

class R_DhcpGetVersion(NDRCALL):
    opnum = 28
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetVersionResponse(NDRCALL):
    structure = (
		('MajorVersion', LPDWORD),
		('MinorVersion', LPDWORD),
    )
        

class R_DhcpAddSubnetElementV4(NDRCALL):
    opnum = 29
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('AddElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V4),
    )

class R_DhcpAddSubnetElementV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetElementsV4(NDRCALL):
    opnum = 30
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('EnumElementType', DHCP_SUBNET_ELEMENT_TYPE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetElementsV4Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpRemoveSubnetElementV4(NDRCALL):
    opnum = 31
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('RemoveElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V4),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpRemoveSubnetElementV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpCreateClientInfoV4(NDRCALL):
    opnum = 32
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_V4),
    )

class R_DhcpCreateClientInfoV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetClientInfoV4(NDRCALL):
    opnum = 33
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_V4),
    )

class R_DhcpSetClientInfoV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetClientInfoV4(NDRCALL):
    opnum = 34
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpGetClientInfoV4Response(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO_V4),
    )
        

class R_DhcpEnumSubnetClientsV4(NDRCALL):
    opnum = 35
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsV4Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_ARRAY_V4),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpSetSuperScopeV4(NDRCALL):
    opnum = 36
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('SuperScopeName', WCHAR),
		('ChangeExisting', BOOL),
    )

class R_DhcpSetSuperScopeV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetSuperScopeInfoV4(NDRCALL):
    opnum = 37
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetSuperScopeInfoV4Response(NDRCALL):
    structure = (
		('SuperScopeTable', LPDHCP_SUPER_SCOPE_TABLE),
    )
        

class R_DhcpDeleteSuperScopeV4(NDRCALL):
    opnum = 38
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SuperScopeName', WCHAR),
    )

class R_DhcpDeleteSuperScopeV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpServerSetConfigV4(NDRCALL):
    opnum = 39
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FieldsToSet', DWORD),
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_V4),
    )

class R_DhcpServerSetConfigV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpServerGetConfigV4(NDRCALL):
    opnum = 40
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpServerGetConfigV4Response(NDRCALL):
    structure = (
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_V4),
    )
        

class R_DhcpServerSetConfigVQ(NDRCALL):
    opnum = 41
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FieldsToSet', DWORD),
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_VQ),
    )

class R_DhcpServerSetConfigVQResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpServerGetConfigVQ(NDRCALL):
    opnum = 42
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpServerGetConfigVQResponse(NDRCALL):
    structure = (
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_VQ),
    )
        

class R_DhcpGetMibInfoVQ(NDRCALL):
    opnum = 43
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetMibInfoVQResponse(NDRCALL):
    structure = (
		('MibInfo', LPDHCP_MIB_INFO_VQ),
    )
        

class R_DhcpCreateClientInfoVQ(NDRCALL):
    opnum = 44
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_VQ),
    )

class R_DhcpCreateClientInfoVQResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetClientInfoVQ(NDRCALL):
    opnum = 45
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_VQ),
    )

class R_DhcpSetClientInfoVQResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetClientInfoVQ(NDRCALL):
    opnum = 46
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpGetClientInfoVQResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO_VQ),
    )
        

class R_DhcpEnumSubnetClientsVQ(NDRCALL):
    opnum = 47
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsVQResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_ARRAY_VQ),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpCreateSubnetVQ(NDRCALL):
    opnum = 48
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('SubnetInfoVQ', LPDHCP_SUBNET_INFO_VQ),
    )

class R_DhcpCreateSubnetVQResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetSubnetInfoVQ(NDRCALL):
    opnum = 49
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpGetSubnetInfoVQResponse(NDRCALL):
    structure = (
		('SubnetInfoVQ', LPDHCP_SUBNET_INFO_VQ),
    )
        

class R_DhcpSetSubnetInfoVQ(NDRCALL):
    opnum = 50
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('SubnetInfoVQ', LPDHCP_SUBNET_INFO_VQ),
    )

class R_DhcpSetSubnetInfoVQResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (R_DhcpCreateSubnet,R_DhcpCreateSubnetResponse),
1 : (R_DhcpSetSubnetInfo,R_DhcpSetSubnetInfoResponse),
2 : (R_DhcpGetSubnetInfo,R_DhcpGetSubnetInfoResponse),
3 : (R_DhcpEnumSubnets,R_DhcpEnumSubnetsResponse),
4 : (R_DhcpAddSubnetElement,R_DhcpAddSubnetElementResponse),
5 : (R_DhcpEnumSubnetElements,R_DhcpEnumSubnetElementsResponse),
6 : (R_DhcpRemoveSubnetElement,R_DhcpRemoveSubnetElementResponse),
7 : (R_DhcpDeleteSubnet,R_DhcpDeleteSubnetResponse),
8 : (R_DhcpCreateOption,R_DhcpCreateOptionResponse),
9 : (R_DhcpSetOptionInfo,R_DhcpSetOptionInfoResponse),
10 : (R_DhcpGetOptionInfo,R_DhcpGetOptionInfoResponse),
11 : (R_DhcpRemoveOption,R_DhcpRemoveOptionResponse),
12 : (R_DhcpSetOptionValue,R_DhcpSetOptionValueResponse),
13 : (R_DhcpGetOptionValue,R_DhcpGetOptionValueResponse),
14 : (R_DhcpEnumOptionValues,R_DhcpEnumOptionValuesResponse),
15 : (R_DhcpRemoveOptionValue,R_DhcpRemoveOptionValueResponse),
16 : (R_DhcpCreateClientInfo,R_DhcpCreateClientInfoResponse),
17 : (R_DhcpSetClientInfo,R_DhcpSetClientInfoResponse),
18 : (R_DhcpGetClientInfo,R_DhcpGetClientInfoResponse),
19 : (R_DhcpDeleteClientInfo,R_DhcpDeleteClientInfoResponse),
20 : (R_DhcpEnumSubnetClients,R_DhcpEnumSubnetClientsResponse),
21 : (R_DhcpGetClientOptions,R_DhcpGetClientOptionsResponse),
22 : (R_DhcpGetMibInfo,R_DhcpGetMibInfoResponse),
23 : (R_DhcpEnumOptions,R_DhcpEnumOptionsResponse),
24 : (R_DhcpSetOptionValues,R_DhcpSetOptionValuesResponse),
25 : (R_DhcpServerSetConfig,R_DhcpServerSetConfigResponse),
26 : (R_DhcpServerGetConfig,R_DhcpServerGetConfigResponse),
27 : (R_DhcpScanDatabase,R_DhcpScanDatabaseResponse),
28 : (R_DhcpGetVersion,R_DhcpGetVersionResponse),
29 : (R_DhcpAddSubnetElementV4,R_DhcpAddSubnetElementV4Response),
30 : (R_DhcpEnumSubnetElementsV4,R_DhcpEnumSubnetElementsV4Response),
31 : (R_DhcpRemoveSubnetElementV4,R_DhcpRemoveSubnetElementV4Response),
32 : (R_DhcpCreateClientInfoV4,R_DhcpCreateClientInfoV4Response),
33 : (R_DhcpSetClientInfoV4,R_DhcpSetClientInfoV4Response),
34 : (R_DhcpGetClientInfoV4,R_DhcpGetClientInfoV4Response),
35 : (R_DhcpEnumSubnetClientsV4,R_DhcpEnumSubnetClientsV4Response),
36 : (R_DhcpSetSuperScopeV4,R_DhcpSetSuperScopeV4Response),
37 : (R_DhcpGetSuperScopeInfoV4,R_DhcpGetSuperScopeInfoV4Response),
38 : (R_DhcpDeleteSuperScopeV4,R_DhcpDeleteSuperScopeV4Response),
39 : (R_DhcpServerSetConfigV4,R_DhcpServerSetConfigV4Response),
40 : (R_DhcpServerGetConfigV4,R_DhcpServerGetConfigV4Response),
41 : (R_DhcpServerSetConfigVQ,R_DhcpServerSetConfigVQResponse),
42 : (R_DhcpServerGetConfigVQ,R_DhcpServerGetConfigVQResponse),
43 : (R_DhcpGetMibInfoVQ,R_DhcpGetMibInfoVQResponse),
44 : (R_DhcpCreateClientInfoVQ,R_DhcpCreateClientInfoVQResponse),
45 : (R_DhcpSetClientInfoVQ,R_DhcpSetClientInfoVQResponse),
46 : (R_DhcpGetClientInfoVQ,R_DhcpGetClientInfoVQResponse),
47 : (R_DhcpEnumSubnetClientsVQ,R_DhcpEnumSubnetClientsVQResponse),
48 : (R_DhcpCreateSubnetVQ,R_DhcpCreateSubnetVQResponse),
49 : (R_DhcpGetSubnetInfoVQ,R_DhcpGetSubnetInfoVQResponse),
50 : (R_DhcpSetSubnetInfoVQ,R_DhcpSetSubnetInfoVQResponse),
}

#################################################################################

#dhcpsrv2 Definition

#################################################################################

MSRPC_UUID_DHCPSRV2 = uuidtup_to_bin(('5b821720-f63b-11d0-aad2-00c04fc324db','0.0'))


class R_DhcpEnumSubnetClientsV5(NDRCALL):
    opnum = 0
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsV5Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_ARRAY_V5),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpSetMScopeInfo(NDRCALL):
    opnum = 1
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('MScopeInfo', LPDHCP_MSCOPE_INFO),
		('NewScope', BOOL),
    )

class R_DhcpSetMScopeInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetMScopeInfo(NDRCALL):
    opnum = 2
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
    )

class R_DhcpGetMScopeInfoResponse(NDRCALL):
    structure = (
		('MScopeInfo', LPDHCP_MSCOPE_INFO),
    )
        

class R_DhcpEnumMScopes(NDRCALL):
    opnum = 3
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumMScopesResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('MScopeTable', LPDHCP_MSCOPE_TABLE),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpAddMScopeElement(NDRCALL):
    opnum = 4
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('AddElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V4),
    )

class R_DhcpAddMScopeElementResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumMScopeElements(NDRCALL):
    opnum = 5
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('EnumElementType', DHCP_SUBNET_ELEMENT_TYPE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumMScopeElementsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpRemoveMScopeElement(NDRCALL):
    opnum = 6
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('RemoveElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V4),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpRemoveMScopeElementResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteMScope(NDRCALL):
    opnum = 7
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpDeleteMScopeResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpScanMDatabase(NDRCALL):
    opnum = 8
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('FixFlag', DWORD),
    )

class R_DhcpScanMDatabaseResponse(NDRCALL):
    structure = (
		('ScanList', LPDHCP_SCAN_LIST),
    )
        

class R_DhcpCreateMClientInfo(NDRCALL):
    opnum = 9
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('ClientInfo', LPDHCP_MCLIENT_INFO),
    )

class R_DhcpCreateMClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpSetMClientInfo(NDRCALL):
    opnum = 10
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_MCLIENT_INFO),
    )

class R_DhcpSetMClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetMClientInfo(NDRCALL):
    opnum = 11
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpGetMClientInfoResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_MCLIENT_INFO),
    )
        

class R_DhcpDeleteMClientInfo(NDRCALL):
    opnum = 12
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpDeleteMClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumMScopeClients(NDRCALL):
    opnum = 13
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('MScopeName', LPWSTR),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumMScopeClientsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_MCLIENT_INFO_ARRAY),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpCreateOptionV5(NDRCALL):
    opnum = 14
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionId', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpCreateOptionV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionInfoV5(NDRCALL):
    opnum = 15
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpSetOptionInfoV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetOptionInfoV5(NDRCALL):
    opnum = 16
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
    )

class R_DhcpGetOptionInfoV5Response(NDRCALL):
    structure = (
		('OptionInfo', LPDHCP_OPTION),
    )
        

class R_DhcpEnumOptionsV5(NDRCALL):
    opnum = 17
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionsV5Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('Options', LPDHCP_OPTION_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpRemoveOptionV5(NDRCALL):
    opnum = 18
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
    )

class R_DhcpRemoveOptionV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionValueV5(NDRCALL):
    opnum = 19
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionId', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValue', LPDHCP_OPTION_DATA),
    )

class R_DhcpSetOptionValueV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionValuesV5(NDRCALL):
    opnum = 20
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
    )

class R_DhcpSetOptionValuesV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetOptionValueV5(NDRCALL):
    opnum = 21
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpGetOptionValueV5Response(NDRCALL):
    structure = (
		('OptionValue', LPDHCP_OPTION_VALUE),
    )
        

class R_DhcpEnumOptionValuesV5(NDRCALL):
    opnum = 22
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionValuesV5Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpRemoveOptionValueV5(NDRCALL):
    opnum = 23
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpRemoveOptionValueV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpCreateClass(NDRCALL):
    opnum = 24
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassInfo', LPDHCP_CLASS_INFO),
    )

class R_DhcpCreateClassResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpModifyClass(NDRCALL):
    opnum = 25
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassInfo', LPDHCP_CLASS_INFO),
    )

class R_DhcpModifyClassResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteClass(NDRCALL):
    opnum = 26
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassName', WCHAR),
    )

class R_DhcpDeleteClassResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetClassInfo(NDRCALL):
    opnum = 27
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('PartialClassInfo', LPDHCP_CLASS_INFO),
    )

class R_DhcpGetClassInfoResponse(NDRCALL):
    structure = (
		('FilledClassInfo', LPDHCP_CLASS_INFO),
    )
        

class R_DhcpEnumClasses(NDRCALL):
    opnum = 28
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumClassesResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClassInfoArray', LPDHCP_CLASS_INFO_ARRAY),
		('nRead', DWORD),
		('nTotal', DWORD),
    )
        

class R_DhcpGetAllOptions(NDRCALL):
    opnum = 29
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
    )

class R_DhcpGetAllOptionsResponse(NDRCALL):
    structure = (
		('OptionStruct', LPDHCP_ALL_OPTIONS),
    )
        

class R_DhcpGetAllOptionValues(NDRCALL):
    opnum = 30
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpGetAllOptionValuesResponse(NDRCALL):
    structure = (
		('Values', LPDHCP_ALL_OPTION_VALUES),
    )
        

class R_DhcpGetMCastMibInfo(NDRCALL):
    opnum = 31
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetMCastMibInfoResponse(NDRCALL):
    structure = (
		('MibInfo', LPDHCP_MCAST_MIB_INFO),
    )
        

class R_DhcpAuditLogSetParams(NDRCALL):
    opnum = 32
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('AuditLogDir', LPWSTR),
		('DiskCheckInterval', DWORD),
		('MaxLogFilesSize', DWORD),
		('MinSpaceOnDisk', DWORD),
    )

class R_DhcpAuditLogSetParamsResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpAuditLogGetParams(NDRCALL):
    opnum = 33
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
    )

class R_DhcpAuditLogGetParamsResponse(NDRCALL):
    structure = (
		('AuditLogDir', LPWSTR_RPC_STRING),
		('DiskCheckInterval', DWORD),
		('MaxLogFilesSize', DWORD),
		('MinSpaceOnDisk', DWORD),
    )
        

class R_DhcpServerQueryAttribute(NDRCALL):
    opnum = 34
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('dwReserved', ULONG),
		('DhcpAttribId', DHCP_ATTRIB_ID),
    )

class R_DhcpServerQueryAttributeResponse(NDRCALL):
    structure = (
		('pDhcpAttrib', LPDHCP_ATTRIB),
    )
        

class R_DhcpServerQueryAttributes(NDRCALL):
    opnum = 35
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('dwReserved', ULONG),
		('dwAttribCount', ULONG),
		('pDhcpAttribs', LPDHCP_ATTRIB_ID),
    )

class R_DhcpServerQueryAttributesResponse(NDRCALL):
    structure = (
		('pDhcpAttribArr', LPDHCP_ATTRIB_ARRAY),
    )
        

class R_DhcpServerRedoAuthorization(NDRCALL):
    opnum = 36
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('dwReserved', ULONG),
    )

class R_DhcpServerRedoAuthorizationResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpAddSubnetElementV5(NDRCALL):
    opnum = 37
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('AddElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V5),
    )

class R_DhcpAddSubnetElementV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetElementsV5(NDRCALL):
    opnum = 38
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('EnumElementType', DHCP_SUBNET_ELEMENT_TYPE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetElementsV5Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V5),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpRemoveSubnetElementV5(NDRCALL):
    opnum = 39
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('RemoveElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V5),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpRemoveSubnetElementV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetServerBindingInfo(NDRCALL):
    opnum = 40
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', ULONG),
    )

class R_DhcpGetServerBindingInfoResponse(NDRCALL):
    structure = (
		('BindElementsInfo', LPDHCP_BIND_ELEMENT_ARRAY),
    )
        

class R_DhcpSetServerBindingInfo(NDRCALL):
    opnum = 41
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', ULONG),
		('BindElementsInfo', LPDHCP_BIND_ELEMENT_ARRAY),
    )

class R_DhcpSetServerBindingInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpQueryDnsRegCredentials(NDRCALL):
    opnum = 42
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('UnameSize', ULONG),
		('DomainSize', ULONG),
    )

class R_DhcpQueryDnsRegCredentialsResponse(NDRCALL):
    structure = (
		('Uname', WCHAR_T),
		('Domain', WCHAR_T),
    )
        

class R_DhcpSetDnsRegCredentials(NDRCALL):
    opnum = 43
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Uname', LPWSTR),
		('Domain', LPWSTR),
		('Passwd', LPWSTR),
    )

class R_DhcpSetDnsRegCredentialsResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpBackupDatabase(NDRCALL):
    opnum = 44
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Path', LPWSTR),
    )

class R_DhcpBackupDatabaseResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpRestoreDatabase(NDRCALL):
    opnum = 45
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Path', LPWSTR),
    )

class R_DhcpRestoreDatabaseResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetServerSpecificStrings(NDRCALL):
    opnum = 46
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetServerSpecificStringsResponse(NDRCALL):
    structure = (
		('ServerSpecificStrings', LPDHCP_SERVER_SPECIFIC_STRINGS),
    )
        

class R_DhcpCreateOptionV6(NDRCALL):
    opnum = 47
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionId', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpCreateOptionV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionInfoV6(NDRCALL):
    opnum = 48
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('OptionInfo', LPDHCP_OPTION),
    )

class R_DhcpSetOptionInfoV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetOptionInfoV6(NDRCALL):
    opnum = 49
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
    )

class R_DhcpGetOptionInfoV6Response(NDRCALL):
    structure = (
		('OptionInfo', LPDHCP_OPTION),
    )
        

class R_DhcpEnumOptionsV6(NDRCALL):
    opnum = 50
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionsV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('Options', LPDHCP_OPTION_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpRemoveOptionV6(NDRCALL):
    opnum = 51
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
    )

class R_DhcpRemoveOptionV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetOptionValueV6(NDRCALL):
    opnum = 52
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionId', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
		('OptionValue', LPDHCP_OPTION_DATA),
    )

class R_DhcpSetOptionValueV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumOptionValuesV6(NDRCALL):
    opnum = 53
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumOptionValuesV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
		('OptionsRead', DWORD),
		('OptionsTotal', DWORD),
    )
        

class R_DhcpRemoveOptionValueV6(NDRCALL):
    opnum = 54
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
    )

class R_DhcpRemoveOptionValueV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetAllOptionsV6(NDRCALL):
    opnum = 55
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
    )

class R_DhcpGetAllOptionsV6Response(NDRCALL):
    structure = (
		('OptionStruct', LPDHCP_ALL_OPTIONS),
    )
        

class R_DhcpGetAllOptionValuesV6(NDRCALL):
    opnum = 56
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
    )

class R_DhcpGetAllOptionValuesV6Response(NDRCALL):
    structure = (
		('Values', LPDHCP_ALL_OPTION_VALUES),
    )
        

class R_DhcpCreateSubnetV6(NDRCALL):
    opnum = 57
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('SubnetInfo', LPDHCP_SUBNET_INFO_V6),
    )

class R_DhcpCreateSubnetV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetsV6(NDRCALL):
    opnum = 58
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetsV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumInfo', LPDHCPV6_IP_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpAddSubnetElementV6(NDRCALL):
    opnum = 59
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('AddElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V6),
    )

class R_DhcpAddSubnetElementV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetElementsV6(NDRCALL):
    opnum = 60
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('EnumElementType', DHCP_SUBNET_ELEMENT_TYPE_V6),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetElementsV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpRemoveSubnetElementV6(NDRCALL):
    opnum = 61
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('RemoveElementInfo', LPDHCP_SUBNET_ELEMENT_DATA_V6),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpRemoveSubnetElementV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteSubnetV6(NDRCALL):
    opnum = 62
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('ForceFlag', DHCP_FORCE_FLAG),
    )

class R_DhcpDeleteSubnetV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetSubnetInfoV6(NDRCALL):
    opnum = 63
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
    )

class R_DhcpGetSubnetInfoV6Response(NDRCALL):
    structure = (
		('SubnetInfo', LPDHCP_SUBNET_INFO_V6),
    )
        

class R_DhcpEnumSubnetClientsV6(NDRCALL):
    opnum = 64
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('ResumeHandle', DHCP_RESUME_IPV6_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_IPV6_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_ARRAY_V6),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpServerSetConfigV6(NDRCALL):
    opnum = 65
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
		('FieldsToSet', DWORD),
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_V6),
    )

class R_DhcpServerSetConfigV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpServerGetConfigV6(NDRCALL):
    opnum = 66
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
    )

class R_DhcpServerGetConfigV6Response(NDRCALL):
    structure = (
		('ConfigInfo', LPDHCP_SERVER_CONFIG_INFO_V6),
    )
        

class R_DhcpSetSubnetInfoV6(NDRCALL):
    opnum = 67
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('SubnetInfo', LPDHCP_SUBNET_INFO_V6),
    )

class R_DhcpSetSubnetInfoV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetMibInfoV6(NDRCALL):
    opnum = 68
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetMibInfoV6Response(NDRCALL):
    structure = (
		('MibInfo', LPDHCP_MIB_INFO_V6),
    )
        

class R_DhcpGetServerBindingInfoV6(NDRCALL):
    opnum = 69
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', ULONG),
    )

class R_DhcpGetServerBindingInfoV6Response(NDRCALL):
    structure = (
		('BindElementsInfo', LPDHCPV6_BIND_ELEMENT_ARRAY),
    )
        

class R_DhcpSetServerBindingInfoV6(NDRCALL):
    opnum = 70
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', ULONG),
		('BindElementsInfo', LPDHCPV6_BIND_ELEMENT_ARRAY),
    )

class R_DhcpSetServerBindingInfoV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetClientInfoV6(NDRCALL):
    opnum = 71
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_V6),
    )

class R_DhcpSetClientInfoV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetClientInfoV6(NDRCALL):
    opnum = 72
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO_V6),
    )

class R_DhcpGetClientInfoV6Response(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO_V6),
    )
        

class R_DhcpDeleteClientInfoV6(NDRCALL):
    opnum = 73
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_SEARCH_INFO_V6),
    )

class R_DhcpDeleteClientInfoV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpCreateClassV6(NDRCALL):
    opnum = 74
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassInfo', LPDHCP_CLASS_INFO_V6),
    )

class R_DhcpCreateClassV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpModifyClassV6(NDRCALL):
    opnum = 75
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassInfo', LPDHCP_CLASS_INFO_V6),
    )

class R_DhcpModifyClassV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteClassV6(NDRCALL):
    opnum = 76
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ClassName', WCHAR),
    )

class R_DhcpDeleteClassV6Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumClassesV6(NDRCALL):
    opnum = 77
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ReservedMustBeZero', DWORD),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumClassesV6Response(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClassInfoArray', LPDHCP_CLASS_INFO_ARRAY_V6),
		('nRead', DWORD),
		('nTotal', DWORD),
    )
        

class R_DhcpGetOptionValueV6(NDRCALL):
    opnum = 78
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('ClassName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO6),
    )

class R_DhcpGetOptionValueV6Response(NDRCALL):
    structure = (
		('OptionValue', LPDHCP_OPTION_VALUE),
    )
        

class R_DhcpSetSubnetDelayOffer(NDRCALL):
    opnum = 79
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('TimeDelayInMilliseconds', USHORT),
    )

class R_DhcpSetSubnetDelayOfferResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpGetSubnetDelayOffer(NDRCALL):
    opnum = 80
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpGetSubnetDelayOfferResponse(NDRCALL):
    structure = (
		('TimeDelayInMilliseconds', USHORT),
    )
        

class R_DhcpGetMibInfoV5(NDRCALL):
    opnum = 81
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetMibInfoV5Response(NDRCALL):
    structure = (
		('MibInfo', LPDHCP_MIB_INFO_V5),
    )
        

class R_DhcpAddFilterV4(NDRCALL):
    opnum = 82
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('AddFilterInfo', DHCP_FILTER_ADD_INFO),
		('ForceFlag', BOOL),
    )

class R_DhcpAddFilterV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpDeleteFilterV4(NDRCALL):
    opnum = 83
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('DeleteFilterInfo', DHCP_ADDR_PATTERN),
    )

class R_DhcpDeleteFilterV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpSetFilterV4(NDRCALL):
    opnum = 84
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('GlobalFilterInfo', DHCP_FILTER_GLOBAL_INFO),
    )

class R_DhcpSetFilterV4Response(NDRCALL):
    structure = (

    )
        

class R_DhcpGetFilterV4(NDRCALL):
    opnum = 85
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpGetFilterV4Response(NDRCALL):
    structure = (
		('GlobalFilterInfo', DHCP_FILTER_GLOBAL_INFO),
    )
        

class R_DhcpEnumFilterV4(NDRCALL):
    opnum = 86
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', LPDHCP_ADDR_PATTERN),
		('PreferredMaximum', DWORD),
		('ListType', DHCP_FILTER_LIST_TYPE),
    )

class R_DhcpEnumFilterV4Response(NDRCALL):
    structure = (
		('ResumeHandle', LPDHCP_ADDR_PATTERN),
		('EnumFilterInfo', LPDHCP_FILTER_ENUM_INFO),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpSetDnsRegCredentialsV5(NDRCALL):
    opnum = 87
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Uname', LPWSTR),
		('Domain', LPWSTR),
		('Passwd', LPWSTR),
    )

class R_DhcpSetDnsRegCredentialsV5Response(NDRCALL):
    structure = (

    )
        

class R_DhcpEnumSubnetClientsFilterStatusInfo(NDRCALL):
    opnum = 88
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpEnumSubnetClientsFilterStatusInfoResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY),
		('ClientRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpV4FailoverCreateRelationship(NDRCALL):
    opnum = 89
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )

class R_DhcpV4FailoverCreateRelationshipResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverSetRelationship(NDRCALL):
    opnum = 90
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )

class R_DhcpV4FailoverSetRelationshipResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverDeleteRelationship(NDRCALL):
    opnum = 91
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pRelationshipName', LPWSTR),
    )

class R_DhcpV4FailoverDeleteRelationshipResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverGetRelationship(NDRCALL):
    opnum = 92
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pRelationshipName', LPWSTR),
    )

class R_DhcpV4FailoverGetRelationshipResponse(NDRCALL):
    structure = (
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )
        

class R_DhcpV4FailoverEnumRelationship(NDRCALL):
    opnum = 93
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('preferredMaximum', DWORD),
    )

class R_DhcpV4FailoverEnumRelationshipResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP_ARRAY),
		('relationshipRead', LPDWORD),
		('relationshipTotal', LPDWORD),
    )
        

class R_DhcpV4FailoverAddScopeToRelationship(NDRCALL):
    opnum = 94
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )

class R_DhcpV4FailoverAddScopeToRelationshipResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverDeleteScopeFromRelationship(NDRCALL):
    opnum = 95
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )

class R_DhcpV4FailoverDeleteScopeFromRelationshipResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverGetScopeRelationship(NDRCALL):
    opnum = 96
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('scopeId', DHCP_IP_ADDRESS),
    )

class R_DhcpV4FailoverGetScopeRelationshipResponse(NDRCALL):
    structure = (
		('pRelationship', LPDHCP_FAILOVER_RELATIONSHIP),
    )
        

class R_DhcpV4FailoverGetScopeStatistics(NDRCALL):
    opnum = 97
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('scopeId', DHCP_IP_ADDRESS),
    )

class R_DhcpV4FailoverGetScopeStatisticsResponse(NDRCALL):
    structure = (
		('pStats', LPDHCP_FAILOVER_STATISTICS),
    )
        

class R_DhcpV4FailoverGetClientInfo(NDRCALL):
    opnum = 98
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpV4FailoverGetClientInfoResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCPV4_FAILOVER_CLIENT_INFO),
    )
        

class R_DhcpV4FailoverGetSystemTime(NDRCALL):
    opnum = 99
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpV4FailoverGetSystemTimeResponse(NDRCALL):
    structure = (
		('pTime', LPDWORD),
    )
        

class R_DhcpV4FailoverTriggerAddrAllocation(NDRCALL):
    opnum = 100
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FailRelName', LPWSTR),
    )

class R_DhcpV4FailoverTriggerAddrAllocationResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4SetOptionValue(NDRCALL):
    opnum = 101
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('PolicyName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValue', LPDHCP_OPTION_DATA),
    )

class R_DhcpV4SetOptionValueResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4SetOptionValues(NDRCALL):
    opnum = 102
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('PolicyName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
		('OptionValues', LPDHCP_OPTION_VALUE_ARRAY),
    )

class R_DhcpV4SetOptionValuesResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetOptionValue(NDRCALL):
    opnum = 103
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('PolicyName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpV4GetOptionValueResponse(NDRCALL):
    structure = (
		('OptionValue', LPDHCP_OPTION_VALUE),
    )
        

class R_DhcpV4RemoveOptionValue(NDRCALL):
    opnum = 104
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('OptionID', DHCP_OPTION_ID),
		('PolicyName', WCHAR),
		('VendorName', WCHAR),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpV4RemoveOptionValueResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetAllOptionValues(NDRCALL):
    opnum = 105
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('Flags', DWORD),
		('ScopeInfo', LPDHCP_OPTION_SCOPE_INFO),
    )

class R_DhcpV4GetAllOptionValuesResponse(NDRCALL):
    structure = (
		('Values', LPDHCP_ALL_OPTION_VALUES_PB),
    )
        

class R_DhcpV4QueryPolicyEnforcement(NDRCALL):
    opnum = 106
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpV4QueryPolicyEnforcementResponse(NDRCALL):
    structure = (
		('Enabled', BOOL),
    )
        

class R_DhcpV4SetPolicyEnforcement(NDRCALL):
    opnum = 107
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('Enable', BOOL),
    )

class R_DhcpV4SetPolicyEnforcementResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4CreatePolicy(NDRCALL):
    opnum = 108
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pPolicy', LPDHCP_POLICY),
    )

class R_DhcpV4CreatePolicyResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetPolicy(NDRCALL):
    opnum = 109
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
    )

class R_DhcpV4GetPolicyResponse(NDRCALL):
    structure = (
		('Policy', LPDHCP_POLICY),
    )
        

class R_DhcpV4SetPolicy(NDRCALL):
    opnum = 110
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FieldsModified', DWORD),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
		('Policy', LPDHCP_POLICY),
    )

class R_DhcpV4SetPolicyResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4DeletePolicy(NDRCALL):
    opnum = 111
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
    )

class R_DhcpV4DeletePolicyResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4EnumPolicies(NDRCALL):
    opnum = 112
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', LPDWORD),
		('PreferredMaximum', DWORD),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpV4EnumPoliciesResponse(NDRCALL):
    structure = (
		('ResumeHandle', LPDWORD),
		('EnumInfo', LPDHCP_POLICY_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpV4AddPolicyRange(NDRCALL):
    opnum = 113
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
		('Range', LPDHCP_IP_RANGE),
    )

class R_DhcpV4AddPolicyRangeResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4RemovePolicyRange(NDRCALL):
    opnum = 114
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
		('Range', LPDHCP_IP_RANGE),
    )

class R_DhcpV4RemovePolicyRangeResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4EnumSubnetClients(NDRCALL):
    opnum = 115
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpV4EnumSubnetClientsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_PB_ARRAY),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpV6SetStatelessStoreParams(NDRCALL):
    opnum = 116
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('fServerLevel', BOOL),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
		('FieldModified', DWORD),
		('Params', LPDHCPV6_STATELESS_PARAMS),
    )

class R_DhcpV6SetStatelessStoreParamsResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV6GetStatelessStoreParams(NDRCALL):
    opnum = 117
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('fServerLevel', BOOL),
		('SubnetAddress', DHCP_IPV6_ADDRESS),
    )

class R_DhcpV6GetStatelessStoreParamsResponse(NDRCALL):
    structure = (
		('Params', LPDHCPV6_STATELESS_PARAMS),
    )
        

class R_DhcpV6GetStatelessStatistics(NDRCALL):
    opnum = 118
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
    )

class R_DhcpV6GetStatelessStatisticsResponse(NDRCALL):
    structure = (
		('StatelessStats', LPDHCPV6_STATELESS_STATS),
    )
        

class R_DhcpV4EnumSubnetReservations(NDRCALL):
    opnum = 119
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpV4EnumSubnetReservationsResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('EnumElementInfo', LPDHCP_RESERVATION_INFO_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpV4GetFreeIPAddress(NDRCALL):
    opnum = 120
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeId', DHCP_IP_ADDRESS),
		('startIP', DHCP_IP_ADDRESS),
		('endIP', DHCP_IP_ADDRESS),
		('numFreeAddr', DWORD),
    )

class R_DhcpV4GetFreeIPAddressResponse(NDRCALL):
    structure = (
		('IPAddrList', LPDHCP_IP_ARRAY),
    )
        

class R_DhcpV6GetFreeIPAddress(NDRCALL):
    opnum = 121
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ScopeId', DHCP_IPV6_ADDRESS),
		('startIP', DHCP_IPV6_ADDRESS),
		('endIP', DHCP_IPV6_ADDRESS),
		('numFreeAddr', DWORD),
    )

class R_DhcpV6GetFreeIPAddressResponse(NDRCALL):
    structure = (
		('IPAddrList', LPDHCPV6_IP_ARRAY),
    )
        

class R_DhcpV4CreateClientInfo(NDRCALL):
    opnum = 122
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_PB),
    )

class R_DhcpV4CreateClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetClientInfo(NDRCALL):
    opnum = 123
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpV4GetClientInfoResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO_PB),
    )
        

class R_DhcpV6CreateClientInfo(NDRCALL):
    opnum = 124
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_V6),
    )

class R_DhcpV6CreateClientInfoResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4FailoverGetAddressStatus(NDRCALL):
    opnum = 125
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpV4FailoverGetAddressStatusResponse(NDRCALL):
    structure = (
		('pStatus', LPDWORD),
    )
        

class R_DhcpV4CreatePolicyEx(NDRCALL):
    opnum = 126
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('pPolicy', LPDHCP_POLICY_EX),
    )

class R_DhcpV4CreatePolicyExResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetPolicyEx(NDRCALL):
    opnum = 127
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
    )

class R_DhcpV4GetPolicyExResponse(NDRCALL):
    structure = (
		('Policy', LPDHCP_POLICY_EX),
    )
        

class R_DhcpV4SetPolicyEx(NDRCALL):
    opnum = 128
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('FieldsModified', DWORD),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('PolicyName', LPWSTR),
		('Policy', LPDHCP_POLICY_EX),
    )

class R_DhcpV4SetPolicyExResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4EnumPoliciesEx(NDRCALL):
    opnum = 129
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ResumeHandle', LPDWORD),
		('PreferredMaximum', DWORD),
		('ServerPolicy', BOOL),
		('SubnetAddress', DHCP_IP_ADDRESS),
    )

class R_DhcpV4EnumPoliciesExResponse(NDRCALL):
    structure = (
		('ResumeHandle', LPDWORD),
		('EnumInfo', LPDHCP_POLICY_EX_ARRAY),
		('ElementsRead', DWORD),
		('ElementsTotal', DWORD),
    )
        

class R_DhcpV4EnumSubnetClientsEx(NDRCALL):
    opnum = 130
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SubnetAddress', DHCP_IP_ADDRESS),
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('PreferredMaximum', DWORD),
    )

class R_DhcpV4EnumSubnetClientsExResponse(NDRCALL):
    structure = (
		('ResumeHandle', DHCP_RESUME_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_EX_ARRAY),
		('ClientsRead', DWORD),
		('ClientsTotal', DWORD),
    )
        

class R_DhcpV4CreateClientInfoEx(NDRCALL):
    opnum = 131
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('ClientInfo', LPDHCP_CLIENT_INFO_EX),
    )

class R_DhcpV4CreateClientInfoExResponse(NDRCALL):
    structure = (

    )
        

class R_DhcpV4GetClientInfoEx(NDRCALL):
    opnum = 132
    structure = (
		('ServerIpAddress', DHCP_SRV_HANDLE),
		('SearchInfo', LPDHCP_SEARCH_INFO),
    )

class R_DhcpV4GetClientInfoExResponse(NDRCALL):
    structure = (
		('ClientInfo', LPDHCP_CLIENT_INFO_EX),
    )
        
OPNUMS = {
0 : (R_DhcpEnumSubnetClientsV5,R_DhcpEnumSubnetClientsV5Response),
1 : (R_DhcpSetMScopeInfo,R_DhcpSetMScopeInfoResponse),
2 : (R_DhcpGetMScopeInfo,R_DhcpGetMScopeInfoResponse),
3 : (R_DhcpEnumMScopes,R_DhcpEnumMScopesResponse),
4 : (R_DhcpAddMScopeElement,R_DhcpAddMScopeElementResponse),
5 : (R_DhcpEnumMScopeElements,R_DhcpEnumMScopeElementsResponse),
6 : (R_DhcpRemoveMScopeElement,R_DhcpRemoveMScopeElementResponse),
7 : (R_DhcpDeleteMScope,R_DhcpDeleteMScopeResponse),
8 : (R_DhcpScanMDatabase,R_DhcpScanMDatabaseResponse),
9 : (R_DhcpCreateMClientInfo,R_DhcpCreateMClientInfoResponse),
10 : (R_DhcpSetMClientInfo,R_DhcpSetMClientInfoResponse),
11 : (R_DhcpGetMClientInfo,R_DhcpGetMClientInfoResponse),
12 : (R_DhcpDeleteMClientInfo,R_DhcpDeleteMClientInfoResponse),
13 : (R_DhcpEnumMScopeClients,R_DhcpEnumMScopeClientsResponse),
14 : (R_DhcpCreateOptionV5,R_DhcpCreateOptionV5Response),
15 : (R_DhcpSetOptionInfoV5,R_DhcpSetOptionInfoV5Response),
16 : (R_DhcpGetOptionInfoV5,R_DhcpGetOptionInfoV5Response),
17 : (R_DhcpEnumOptionsV5,R_DhcpEnumOptionsV5Response),
18 : (R_DhcpRemoveOptionV5,R_DhcpRemoveOptionV5Response),
19 : (R_DhcpSetOptionValueV5,R_DhcpSetOptionValueV5Response),
20 : (R_DhcpSetOptionValuesV5,R_DhcpSetOptionValuesV5Response),
21 : (R_DhcpGetOptionValueV5,R_DhcpGetOptionValueV5Response),
22 : (R_DhcpEnumOptionValuesV5,R_DhcpEnumOptionValuesV5Response),
23 : (R_DhcpRemoveOptionValueV5,R_DhcpRemoveOptionValueV5Response),
24 : (R_DhcpCreateClass,R_DhcpCreateClassResponse),
25 : (R_DhcpModifyClass,R_DhcpModifyClassResponse),
26 : (R_DhcpDeleteClass,R_DhcpDeleteClassResponse),
27 : (R_DhcpGetClassInfo,R_DhcpGetClassInfoResponse),
28 : (R_DhcpEnumClasses,R_DhcpEnumClassesResponse),
29 : (R_DhcpGetAllOptions,R_DhcpGetAllOptionsResponse),
30 : (R_DhcpGetAllOptionValues,R_DhcpGetAllOptionValuesResponse),
31 : (R_DhcpGetMCastMibInfo,R_DhcpGetMCastMibInfoResponse),
32 : (R_DhcpAuditLogSetParams,R_DhcpAuditLogSetParamsResponse),
33 : (R_DhcpAuditLogGetParams,R_DhcpAuditLogGetParamsResponse),
34 : (R_DhcpServerQueryAttribute,R_DhcpServerQueryAttributeResponse),
35 : (R_DhcpServerQueryAttributes,R_DhcpServerQueryAttributesResponse),
36 : (R_DhcpServerRedoAuthorization,R_DhcpServerRedoAuthorizationResponse),
37 : (R_DhcpAddSubnetElementV5,R_DhcpAddSubnetElementV5Response),
38 : (R_DhcpEnumSubnetElementsV5,R_DhcpEnumSubnetElementsV5Response),
39 : (R_DhcpRemoveSubnetElementV5,R_DhcpRemoveSubnetElementV5Response),
40 : (R_DhcpGetServerBindingInfo,R_DhcpGetServerBindingInfoResponse),
41 : (R_DhcpSetServerBindingInfo,R_DhcpSetServerBindingInfoResponse),
42 : (R_DhcpQueryDnsRegCredentials,R_DhcpQueryDnsRegCredentialsResponse),
43 : (R_DhcpSetDnsRegCredentials,R_DhcpSetDnsRegCredentialsResponse),
44 : (R_DhcpBackupDatabase,R_DhcpBackupDatabaseResponse),
45 : (R_DhcpRestoreDatabase,R_DhcpRestoreDatabaseResponse),
46 : (R_DhcpGetServerSpecificStrings,R_DhcpGetServerSpecificStringsResponse),
47 : (R_DhcpCreateOptionV6,R_DhcpCreateOptionV6Response),
48 : (R_DhcpSetOptionInfoV6,R_DhcpSetOptionInfoV6Response),
49 : (R_DhcpGetOptionInfoV6,R_DhcpGetOptionInfoV6Response),
50 : (R_DhcpEnumOptionsV6,R_DhcpEnumOptionsV6Response),
51 : (R_DhcpRemoveOptionV6,R_DhcpRemoveOptionV6Response),
52 : (R_DhcpSetOptionValueV6,R_DhcpSetOptionValueV6Response),
53 : (R_DhcpEnumOptionValuesV6,R_DhcpEnumOptionValuesV6Response),
54 : (R_DhcpRemoveOptionValueV6,R_DhcpRemoveOptionValueV6Response),
55 : (R_DhcpGetAllOptionsV6,R_DhcpGetAllOptionsV6Response),
56 : (R_DhcpGetAllOptionValuesV6,R_DhcpGetAllOptionValuesV6Response),
57 : (R_DhcpCreateSubnetV6,R_DhcpCreateSubnetV6Response),
58 : (R_DhcpEnumSubnetsV6,R_DhcpEnumSubnetsV6Response),
59 : (R_DhcpAddSubnetElementV6,R_DhcpAddSubnetElementV6Response),
60 : (R_DhcpEnumSubnetElementsV6,R_DhcpEnumSubnetElementsV6Response),
61 : (R_DhcpRemoveSubnetElementV6,R_DhcpRemoveSubnetElementV6Response),
62 : (R_DhcpDeleteSubnetV6,R_DhcpDeleteSubnetV6Response),
63 : (R_DhcpGetSubnetInfoV6,R_DhcpGetSubnetInfoV6Response),
64 : (R_DhcpEnumSubnetClientsV6,R_DhcpEnumSubnetClientsV6Response),
65 : (R_DhcpServerSetConfigV6,R_DhcpServerSetConfigV6Response),
66 : (R_DhcpServerGetConfigV6,R_DhcpServerGetConfigV6Response),
67 : (R_DhcpSetSubnetInfoV6,R_DhcpSetSubnetInfoV6Response),
68 : (R_DhcpGetMibInfoV6,R_DhcpGetMibInfoV6Response),
69 : (R_DhcpGetServerBindingInfoV6,R_DhcpGetServerBindingInfoV6Response),
70 : (R_DhcpSetServerBindingInfoV6,R_DhcpSetServerBindingInfoV6Response),
71 : (R_DhcpSetClientInfoV6,R_DhcpSetClientInfoV6Response),
72 : (R_DhcpGetClientInfoV6,R_DhcpGetClientInfoV6Response),
73 : (R_DhcpDeleteClientInfoV6,R_DhcpDeleteClientInfoV6Response),
74 : (R_DhcpCreateClassV6,R_DhcpCreateClassV6Response),
75 : (R_DhcpModifyClassV6,R_DhcpModifyClassV6Response),
76 : (R_DhcpDeleteClassV6,R_DhcpDeleteClassV6Response),
77 : (R_DhcpEnumClassesV6,R_DhcpEnumClassesV6Response),
78 : (R_DhcpGetOptionValueV6,R_DhcpGetOptionValueV6Response),
79 : (R_DhcpSetSubnetDelayOffer,R_DhcpSetSubnetDelayOfferResponse),
80 : (R_DhcpGetSubnetDelayOffer,R_DhcpGetSubnetDelayOfferResponse),
81 : (R_DhcpGetMibInfoV5,R_DhcpGetMibInfoV5Response),
82 : (R_DhcpAddFilterV4,R_DhcpAddFilterV4Response),
83 : (R_DhcpDeleteFilterV4,R_DhcpDeleteFilterV4Response),
84 : (R_DhcpSetFilterV4,R_DhcpSetFilterV4Response),
85 : (R_DhcpGetFilterV4,R_DhcpGetFilterV4Response),
86 : (R_DhcpEnumFilterV4,R_DhcpEnumFilterV4Response),
87 : (R_DhcpSetDnsRegCredentialsV5,R_DhcpSetDnsRegCredentialsV5Response),
88 : (R_DhcpEnumSubnetClientsFilterStatusInfo,R_DhcpEnumSubnetClientsFilterStatusInfoResponse),
89 : (R_DhcpV4FailoverCreateRelationship,R_DhcpV4FailoverCreateRelationshipResponse),
90 : (R_DhcpV4FailoverSetRelationship,R_DhcpV4FailoverSetRelationshipResponse),
91 : (R_DhcpV4FailoverDeleteRelationship,R_DhcpV4FailoverDeleteRelationshipResponse),
92 : (R_DhcpV4FailoverGetRelationship,R_DhcpV4FailoverGetRelationshipResponse),
93 : (R_DhcpV4FailoverEnumRelationship,R_DhcpV4FailoverEnumRelationshipResponse),
94 : (R_DhcpV4FailoverAddScopeToRelationship,R_DhcpV4FailoverAddScopeToRelationshipResponse),
95 : (R_DhcpV4FailoverDeleteScopeFromRelationship,R_DhcpV4FailoverDeleteScopeFromRelationshipResponse),
96 : (R_DhcpV4FailoverGetScopeRelationship,R_DhcpV4FailoverGetScopeRelationshipResponse),
97 : (R_DhcpV4FailoverGetScopeStatistics,R_DhcpV4FailoverGetScopeStatisticsResponse),
98 : (R_DhcpV4FailoverGetClientInfo,R_DhcpV4FailoverGetClientInfoResponse),
99 : (R_DhcpV4FailoverGetSystemTime,R_DhcpV4FailoverGetSystemTimeResponse),
100 : (R_DhcpV4FailoverTriggerAddrAllocation,R_DhcpV4FailoverTriggerAddrAllocationResponse),
101 : (R_DhcpV4SetOptionValue,R_DhcpV4SetOptionValueResponse),
102 : (R_DhcpV4SetOptionValues,R_DhcpV4SetOptionValuesResponse),
103 : (R_DhcpV4GetOptionValue,R_DhcpV4GetOptionValueResponse),
104 : (R_DhcpV4RemoveOptionValue,R_DhcpV4RemoveOptionValueResponse),
105 : (R_DhcpV4GetAllOptionValues,R_DhcpV4GetAllOptionValuesResponse),
106 : (R_DhcpV4QueryPolicyEnforcement,R_DhcpV4QueryPolicyEnforcementResponse),
107 : (R_DhcpV4SetPolicyEnforcement,R_DhcpV4SetPolicyEnforcementResponse),
108 : (R_DhcpV4CreatePolicy,R_DhcpV4CreatePolicyResponse),
109 : (R_DhcpV4GetPolicy,R_DhcpV4GetPolicyResponse),
110 : (R_DhcpV4SetPolicy,R_DhcpV4SetPolicyResponse),
111 : (R_DhcpV4DeletePolicy,R_DhcpV4DeletePolicyResponse),
112 : (R_DhcpV4EnumPolicies,R_DhcpV4EnumPoliciesResponse),
113 : (R_DhcpV4AddPolicyRange,R_DhcpV4AddPolicyRangeResponse),
114 : (R_DhcpV4RemovePolicyRange,R_DhcpV4RemovePolicyRangeResponse),
115 : (R_DhcpV4EnumSubnetClients,R_DhcpV4EnumSubnetClientsResponse),
116 : (R_DhcpV6SetStatelessStoreParams,R_DhcpV6SetStatelessStoreParamsResponse),
117 : (R_DhcpV6GetStatelessStoreParams,R_DhcpV6GetStatelessStoreParamsResponse),
118 : (R_DhcpV6GetStatelessStatistics,R_DhcpV6GetStatelessStatisticsResponse),
119 : (R_DhcpV4EnumSubnetReservations,R_DhcpV4EnumSubnetReservationsResponse),
120 : (R_DhcpV4GetFreeIPAddress,R_DhcpV4GetFreeIPAddressResponse),
121 : (R_DhcpV6GetFreeIPAddress,R_DhcpV6GetFreeIPAddressResponse),
122 : (R_DhcpV4CreateClientInfo,R_DhcpV4CreateClientInfoResponse),
123 : (R_DhcpV4GetClientInfo,R_DhcpV4GetClientInfoResponse),
124 : (R_DhcpV6CreateClientInfo,R_DhcpV6CreateClientInfoResponse),
125 : (R_DhcpV4FailoverGetAddressStatus,R_DhcpV4FailoverGetAddressStatusResponse),
126 : (R_DhcpV4CreatePolicyEx,R_DhcpV4CreatePolicyExResponse),
127 : (R_DhcpV4GetPolicyEx,R_DhcpV4GetPolicyExResponse),
128 : (R_DhcpV4SetPolicyEx,R_DhcpV4SetPolicyExResponse),
129 : (R_DhcpV4EnumPoliciesEx,R_DhcpV4EnumPoliciesExResponse),
130 : (R_DhcpV4EnumSubnetClientsEx,R_DhcpV4EnumSubnetClientsExResponse),
131 : (R_DhcpV4CreateClientInfoEx,R_DhcpV4CreateClientInfoExResponse),
132 : (R_DhcpV4GetClientInfoEx,R_DhcpV4GetClientInfoExResponse),
}

