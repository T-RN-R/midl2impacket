
from fuzzer.midl import *
from fuzzer.core import *
ULONGLONG = NdrHyper
BYTE = NdrByte
USHORT = NdrShort
SHORT = NdrShort
UCHAR = NdrByte
PCHAR = NdrByte
PUCHAR = NdrByte
PLONG64 = NdrHyper
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
PDWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
PUNSIGNED_LONG = NdrLong
PUNSIGNED_CHAR = NdrByte
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
PWCHAR = NdrCString
INT = NdrLong
PVOID = NdrContextHandle
VOID = NdrContextHandle
CONTEXT_HANDLE = NdrContextHandle
PPCONTEXT_HANDLE = NdrContextHandle
LONG = NdrLong
INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LARGE_INTEGER = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte
DOUBLE = NdrDouble
FLOAT = NdrFloat

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')]

class LUID(NdrStructure):
    MEMBERS = [(DWORD,'LowPart'),(LONG,'HighPart')]

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),]
WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PPBOOL = INT
PLPBOOL = INT
BYTE = UNSIGNED_CHAR
PPBYTE = UNSIGNED_CHAR
PLPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PPBOOLEAN = BYTE
WCHAR = WCHAR_T
PPWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PPCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PPDWORD = UNSIGNED_LONG
PLPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PPDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PPDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PPUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
PLPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = WCHAR_T
LMSTR = WCHAR
LONG = LONG
PPLONG = LONG
PLPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PPLONG64 = SIGNED___INT64
LPCSTR = CHAR
LPCVOID = VOID
LPCWSTR = WCHAR_T
PSTR = CHAR
PLPSTR = CHAR
LPWSTR = WCHAR_T
PPWSTR = WCHAR_T
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
PPULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PPVOID = VOID
PLPVOID = VOID
WORD = UNSIGNED_SHORT
PPWORD = UNSIGNED_SHORT
PLPWORD = UNSIGNED_SHORT

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
PFILETIME = FILETIME
LPFILETIME = FILETIME

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    
UUID = GUID
PGUID = GUID

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    
PLARGE_INTEGER = LARGE_INTEGER

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    
PEVENT_DESCRIPTOR = EVENT_DESCRIPTOR
PCEVENT_DESCRIPTOR = EVENT_DESCRIPTOR

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    
PEVENT_HEADER = EVENT_HEADER
LCID = DWORD

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    
PLUID = LUID

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    
PRPC_UNICODE_STRING = RPC_UNICODE_STRING

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    
PSERVER_INFO_100 = SERVER_INFO_100
LPSERVER_INFO_100 = SERVER_INFO_100

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    
PSERVER_INFO_101 = SERVER_INFO_101
LPSERVER_INFO_101 = SERVER_INFO_101

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    
PSYSTEMTIME = SYSTEMTIME

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    
PUINT128 = UINT128

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    
PULARGE_INTEGER = ULARGE_INTEGER

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    
ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    
POBJECT_TYPE_LIST = OBJECT_TYPE_LIST

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    
PACE_HEADER = ACE_HEADER

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    
PSYSTEM_MANDATORY_LABEL_ACE = SYSTEM_MANDATORY_LABEL_ACE

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    
PTOKEN_MANDATORY_POLICY = TOKEN_MANDATORY_POLICY

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    
PMANDATORY_INFORMATION = MANDATORY_INFORMATION

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    
PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE = CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    
PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 = CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
SECURITY_INFORMATION = DWORD
PPSECURITY_INFORMATION = DWORD

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    
PRPC_SID = RPC_SID
PSID = RPC_SID

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    
PACL = ACL

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
PSECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR
DHCP_SRV_HANDLE = WCHAR_T
DHCP_IP_ADDRESS = DWORD
PPDHCP_IP_ADDRESS = DWORD
PLPDHCP_IP_ADDRESS = DWORD
DHCP_IP_MASK = DWORD
DHCP_RESUME_HANDLE = DWORD
DHCP_OPTION_ID = DWORD

class DHCP_BINARY_DATA(NdrStructure):
    MEMBERS = [(DWORD, "DataLength"),(PBYTE, "Data"),]

    
LPDHCP_BINARY_DATA = DHCP_BINARY_DATA
DHCP_CLIENT_UID = DHCP_BINARY_DATA

class DHCP_SUBNET_STATE(NdrEnum):
    MAP = ((0 , 'DhcpSubnetEnabled'),(1 , 'DhcpSubnetDisabled'),(2 , 'DhcpSubnetEnabledSwitched'),(3 , 'DhcpSubnetDisabledSwitched'),(4 , 'DhcpSubnetInvalidState'),)        

class DHCP_SUBNET_ELEMENT_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpIpRanges'),(1 , 'DhcpSecondaryHosts'),(2 , 'DhcpReservedIps'),(3 , 'DhcpExcludedIpRanges'),(4 , 'DhcpIpUsedClusters'),(5 , 'DhcpIpRangesDhcpOnly'),(6 , 'DhcpIpRangesDhcpBootp'),(7 , 'DhcpIpRangesBootpOnly'),)        

class DHCP_FORCE_FLAG(NdrEnum):
    MAP = ((0 , 'DhcpFullForce'),(1 , 'DhcpNoForce'),(2 , 'DhcpFailoverForce'),)        

class DHCP_OPTION_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpUnaryElementTypeOption'),(1 , 'DhcpArrayTypeOption'),)        

class DHCP_OPTION_DATA_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpByteOption'),(1 , 'DhcpWordOption'),(2 , 'DhcpDWordOption'),(3 , 'DhcpDWordDWordOption'),(4 , 'DhcpIpAddressOption'),(5 , 'DhcpStringDataOption'),(6 , 'DhcpBinaryDataOption'),(7 , 'DhcpEncapsulatedDataOption'),(8 , 'DhcpIpv6AddressOption'),)        

class DHCP_OPTION_SCOPE_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpDefaultOptions'),(1 , 'DhcpGlobalOptions'),(2 , 'DhcpSubnetOptions'),(3 , 'DhcpReservedOptions'),(4 , 'DhcpMScopeOptions'),)        

class DHCP_SEARCH_INFO_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpClientIpAddress'),(1 , 'DhcpClientHardwareAddress'),(2 , 'DhcpClientName'),)        

class DHCP_SCAN_FLAG(NdrEnum):
    MAP = ((0 , 'DhcpRegistryFix'),(1 , 'DhcpDatabaseFix'),)        

class QUARANTINESTATUS(NdrEnum):
    MAP = ((0 , 'NOQUARANTINE'),(1 , 'RESTRICTEDACCESS'),(2 , 'DROPPACKET'),(3 , 'PROBATION'),(4 , 'EXEMPT'),(5 , 'DEFAULTQUARSETTING'),(6 , 'NOQUARINFO'),)        

class DHCP_HOST_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "IpAddress"),(PWCHAR_T, "NetBiosName"),(PWCHAR_T, "HostName"),]

    
LPDHCP_HOST_INFO = DHCP_HOST_INFO

class DHCP_SUBNET_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "SubnetAddress"),(DHCP_IP_MASK, "SubnetMask"),(PWCHAR_T, "SubnetName"),(PWCHAR_T, "SubnetComment"),(DHCP_HOST_INFO, "PrimaryHost"),(DHCP_SUBNET_STATE, "SubnetState"),]

    
LPDHCP_SUBNET_INFO = DHCP_SUBNET_INFO

class DHCP_IP_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_IP_ADDRESS, "Elements"),]

    
LPDHCP_IP_ARRAY = DHCP_IP_ARRAY

class DHCP_IP_RANGE(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "StartAddress"),(DHCP_IP_ADDRESS, "EndAddress"),]

    
LPDHCP_IP_RANGE = DHCP_IP_RANGE

class DHCP_IP_RESERVATION(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ReservedIpAddress"),(PDHCP_CLIENT_UID, "ReservedForClient"),]

    
LPDHCP_IP_RESERVATION = DHCP_IP_RESERVATION

class DHCP_IP_CLUSTER(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClusterAddress"),(DWORD, "ClusterMask"),]

    
LPDHCP_IP_CLUSTER = DHCP_IP_CLUSTER

class DHCP_BOOTP_IP_RANGE(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "StartAddress"),(DHCP_IP_ADDRESS, "EndAddress"),(ULONG, "BootpAllocated"),(ULONG, "MaxBootpAllowed"),]

    
LPDHCP_BOOT_IP_RANGE = DHCP_BOOTP_IP_RANGE

class DHCP_SUBNET_ELEMENT_DATA(NdrStructure):
    MEMBERS = [(DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),(ELEMENT, "Element"),]

    
LPDHCP_SUBNET_ELEMENT_DATA = DHCP_SUBNET_ELEMENT_DATA

class DHCP_SUBNET_ELEMENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_SUBNET_ELEMENT_DATA, "Elements"),]

    
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY = DHCP_SUBNET_ELEMENT_INFO_ARRAY

class DWORD_DWORD(NdrStructure):
    MEMBERS = [(DWORD, "DWord1"),(DWORD, "DWord2"),]

    
LPDWORD_DWORD = DWORD_DWORD

class DHCP_OPTION_DATA_ELEMENT(NdrStructure):
    MEMBERS = [(DHCP_OPTION_DATA_TYPE, "OptionType"),(ELEMENT, "Element"),]

    
LPDHCP_OPTION_DATA_ELEMENT = DHCP_OPTION_DATA_ELEMENT

class DHCP_OPTION_DATA(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_OPTION_DATA_ELEMENT, "Elements"),]

    
LPDHCP_OPTION_DATA = DHCP_OPTION_DATA

class DHCP_OPTION(NdrStructure):
    MEMBERS = [(DHCP_OPTION_ID, "OptionID"),(PWCHAR_T, "OptionName"),(PWCHAR_T, "OptionComment"),(DHCP_OPTION_DATA, "DefaultValue"),(DHCP_OPTION_TYPE, "OptionType"),]

    
LPDHCP_OPTION = DHCP_OPTION

class DHCP_RESERVED_SCOPE(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ReservedIpAddress"),(DHCP_IP_ADDRESS, "ReservedIpSubnetAddress"),]

    
LPDHCP_RESERVED_SCOPE = DHCP_RESERVED_SCOPE

class DHCP_OPTION_SCOPE_INFO(NdrStructure):
    MEMBERS = [(DHCP_OPTION_SCOPE_TYPE, "ScopeType"),(SCOPEINFO, "ScopeInfo"),]

    
LPDHCP_OPTION_SCOPE_INFO = DHCP_OPTION_SCOPE_INFO

class DHCP_OPTION_VALUE(NdrStructure):
    MEMBERS = [(DHCP_OPTION_ID, "OptionID"),(DHCP_OPTION_DATA, "Value"),]

    
LPDHCP_OPTION_VALUE = DHCP_OPTION_VALUE

class DHCP_OPTION_VALUE_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_OPTION_VALUE, "Values"),]

    
LPDHCP_OPTION_VALUE_ARRAY = DHCP_OPTION_VALUE_ARRAY

class DATE_TIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
LPDATE_TIME = DATE_TIME

class DHCP_CLIENT_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),]

    
LPDHCP_CLIENT_INFO = DHCP_CLIENT_INFO

class DHCP_SEARCH_INFO(NdrStructure):
    MEMBERS = [(DHCP_SEARCH_INFO_TYPE, "SearchType"),(SEARCHINFO, "SearchInfo"),]

    
LPDHCP_SEARCH_INFO = DHCP_SEARCH_INFO

class DHCP_CLIENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO, "Clients"),]

    
LPDHCP_CLIENT_INFO_ARRAY = DHCP_CLIENT_INFO_ARRAY

class DHCP_OPTION_LIST(NdrStructure):
    MEMBERS = [(DWORD, "NumOptions"),(PDHCP_OPTION_VALUE, "Options"),]

    
LPDHCP_OPTION_LIST = DHCP_OPTION_LIST

class SCOPE_MIB_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "Subnet"),(DWORD, "NumAddressesInuse"),(DWORD, "NumAddressesFree"),(DWORD, "NumPendingOffers"),]

    
LPSCOPE_MIB_INFO = SCOPE_MIB_INFO

class DHCP_MIB_INFO(NdrStructure):
    MEMBERS = [(DWORD, "Discovers"),(DWORD, "Offers"),(DWORD, "Requests"),(DWORD, "Acks"),(DWORD, "Naks"),(DWORD, "Declines"),(DWORD, "Releases"),(DATE_TIME, "ServerStartTime"),(DWORD, "Scopes"),(LPSCOPE_MIB_INFO, "ScopeInfo"),]

    
LPDHCP_MIB_INFO = DHCP_MIB_INFO

class DHCP_OPTION_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_OPTION, "Options"),]

    
LPDHCP_OPTION_ARRAY = DHCP_OPTION_ARRAY

class DHCP_SERVER_CONFIG_INFO(NdrStructure):
    MEMBERS = [(DWORD, "APIProtocolSupport"),(PWCHAR_T, "DatabaseName"),(PWCHAR_T, "DatabasePath"),(PWCHAR_T, "BackupPath"),(DWORD, "BackupInterval"),(DWORD, "DatabaseLoggingFlag"),(DWORD, "RestoreFlag"),(DWORD, "DatabaseCleanupInterval"),(DWORD, "DebugFlag"),]

    
LPDHCP_SERVER_CONFIG_INFO = DHCP_SERVER_CONFIG_INFO

class DHCP_SCAN_ITEM(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "IpAddress"),(DHCP_SCAN_FLAG, "ScanFlag"),]

    
LPDHCP_SCAN_ITEM = DHCP_SCAN_ITEM

class DHCP_SCAN_LIST(NdrStructure):
    MEMBERS = [(DWORD, "NumScanItems"),(PDHCP_SCAN_ITEM, "ScanItems"),]

    
LPDHCP_SCAN_LIST = DHCP_SCAN_LIST

class DHCP_IP_RESERVATION_V4(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ReservedIpAddress"),(PDHCP_CLIENT_UID, "ReservedForClient"),(BYTE, "bAllowedClientTypes"),]

    
LPDHCP_IP_RESERVATION_V4 = DHCP_IP_RESERVATION_V4

class DHCP_SUBNET_ELEMENT_DATA_V4(NdrStructure):
    MEMBERS = [(DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),(ELEMENT, "Element"),]

    
LPDHCP_SUBNET_ELEMENT_DATA_V4 = DHCP_SUBNET_ELEMENT_DATA_V4

class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_SUBNET_ELEMENT_DATA_V4, "Elements"),]

    
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4 = DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4

class DHCP_CLIENT_INFO_V4(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),]

    
LPDHCP_CLIENT_INFO_V4 = DHCP_CLIENT_INFO_V4

class DHCP_CLIENT_INFO_ARRAY_V4(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_V4, "Clients"),]

    
LPDHCP_CLIENT_INFO_ARRAY_V4 = DHCP_CLIENT_INFO_ARRAY_V4

class DHCP_SUPER_SCOPE_TABLE_ENTRY(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "SubnetAddress"),(DWORD, "SuperScopeNumber"),(DWORD, "NextInSuperScope"),(PWCHAR_T, "SuperScopeName"),]

    
LPDHCP_SUPER_SCOPE_TABLE_ENTRY = DHCP_SUPER_SCOPE_TABLE_ENTRY

class DHCP_SUPER_SCOPE_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "cEntries"),(PDHCP_SUPER_SCOPE_TABLE_ENTRY, "pEntries"),]

    
LPDHCP_SUPER_SCOPE_TABLE = DHCP_SUPER_SCOPE_TABLE

class DHCP_SERVER_CONFIG_INFO_V4(NdrStructure):
    MEMBERS = [(DWORD, "APIProtocolSupport"),(PWCHAR_T, "DatabaseName"),(PWCHAR_T, "DatabasePath"),(PWCHAR_T, "BackupPath"),(DWORD, "BackupInterval"),(DWORD, "DatabaseLoggingFlag"),(DWORD, "RestoreFlag"),(DWORD, "DatabaseCleanupInterval"),(DWORD, "DebugFlag"),(DWORD, "dwPingRetries"),(DWORD, "cbBootTableString"),(PWCHAR, "wszBootTableString"),(BOOL, "fAuditLog"),]

    
LPDHCP_SERVER_CONFIG_INFO_V4 = DHCP_SERVER_CONFIG_INFO_V4

class DHCP_SERVER_CONFIG_INFO_VQ(NdrStructure):
    MEMBERS = [(DWORD, "APIProtocolSupport"),(PWCHAR_T, "DatabaseName"),(PWCHAR_T, "DatabasePath"),(PWCHAR_T, "BackupPath"),(DWORD, "BackupInterval"),(DWORD, "DatabaseLoggingFlag"),(DWORD, "RestoreFlag"),(DWORD, "DatabaseCleanupInterval"),(DWORD, "DebugFlag"),(DWORD, "dwPingRetries"),(DWORD, "cbBootTableString"),(PWCHAR, "wszBootTableString"),(BOOL, "fAuditLog"),(BOOL, "QuarantineOn"),(DWORD, "QuarDefFail"),(BOOL, "QuarRuntimeStatus"),]

    
LPDHCP_SERVER_CONFIG_INFO_VQ = DHCP_SERVER_CONFIG_INFO_VQ

class SCOPE_MIB_INFO_VQ(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "Subnet"),(DWORD, "NumAddressesInuse"),(DWORD, "NumAddressesFree"),(DWORD, "NumPendingOffers"),(DWORD, "QtnNumLeases"),(DWORD, "QtnPctQtnLeases"),(DWORD, "QtnProbationLeases"),(DWORD, "QtnNonQtnLeases"),(DWORD, "QtnExemptLeases"),(DWORD, "QtnCapableClients"),]

    
LPSCOPE_MIB_INFO_VQ = SCOPE_MIB_INFO_VQ

class DHCP_MIB_INFO_VQ(NdrStructure):
    MEMBERS = [(DWORD, "Discovers"),(DWORD, "Offers"),(DWORD, "Requests"),(DWORD, "Acks"),(DWORD, "Naks"),(DWORD, "Declines"),(DWORD, "Releases"),(DATE_TIME, "ServerStartTime"),(DWORD, "QtnNumLeases"),(DWORD, "QtnPctQtnLeases"),(DWORD, "QtnProbationLeases"),(DWORD, "QtnNonQtnLeases"),(DWORD, "QtnExemptLeases"),(DWORD, "QtnCapableClients"),(DWORD, "QtnIASErrors"),(DWORD, "Scopes"),(LPSCOPE_MIB_INFO_VQ, "ScopeInfo"),]

    
LPDHCP_MIB_INFO_VQ = DHCP_MIB_INFO_VQ

class DHCP_CLIENT_INFO_VQ(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),(QUARANTINESTATUS, "Status"),(DATE_TIME, "ProbationEnds"),(BOOL, "QuarantineCapable"),]

    
LPDHCP_CLIENT_INFO_VQ = DHCP_CLIENT_INFO_VQ

class DHCP_CLIENT_INFO_ARRAY_VQ(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_VQ, "Clients"),]

    
LPDHCP_CLIENT_INFO_ARRAY_VQ = DHCP_CLIENT_INFO_ARRAY_VQ

class DHCP_SUBNET_INFO_VQ(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "SubnetAddress"),(DHCP_IP_MASK, "SubnetMask"),(PWCHAR_T, "SubnetName"),(PWCHAR_T, "SubnetComment"),(DHCP_HOST_INFO, "PrimaryHost"),(DHCP_SUBNET_STATE, "SubnetState"),(DWORD, "QuarantineOn"),(DWORD, "Reserved1"),(DWORD, "Reserved2"),(INT64, "Reserved3"),(INT64, "Reserved4"),]

    
LPDHCP_SUBNET_INFO_VQ = DHCP_SUBNET_INFO_VQ
LPWSTR_RPC_STRING = WCHAR_T
DHCP_ATTRIB_ID = ULONG
PPDHCP_ATTRIB_ID = ULONG
PLPDHCP_ATTRIB_ID = ULONG

class DHCP_OPTION_SCOPE_TYPE6(NdrEnum):
    MAP = ((0 , 'DhcpDefaultOptions6'),(1 , 'DhcpScopeOptions6'),(2 , 'DhcpReservedOptions6'),(3 , 'DhcpGlobalOptions6'),)        

class DHCP_SUBNET_ELEMENT_TYPE_V6(NdrEnum):
    MAP = ((0 , 'Dhcpv6IpRanges'),(1 , 'Dhcpv6ReservedIps'),(2 , 'Dhcpv6ExcludedIpRanges'),)        

class DHCP_SEARCH_INFO_TYPE_V6(NdrEnum):
    MAP = ((0 , 'Dhcpv6ClientIpAddress'),(1 , 'Dhcpv6ClientDUID'),(2 , 'Dhcpv6ClientName'),)        

class DHCP_IPV6_ADDRESS(NdrStructure):
    MEMBERS = [(ULONGLONG, "HighOrderBits"),(ULONGLONG, "LowOrderBits"),]

    
LPDHCP_IPV6_ADDRESS = DHCP_IPV6_ADDRESS
PDHCP_IPV6_ADDRESS = DHCP_IPV6_ADDRESS

class DHCP_CLIENT_INFO_V5(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),]

    
LPDHCP_CLIENT_INFO_V5 = DHCP_CLIENT_INFO_V5

class DHCP_CLIENT_INFO_ARRAY_V5(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_V5, "Clients"),]

    
LPDHCP_CLIENT_INFO_ARRAY_V5 = DHCP_CLIENT_INFO_ARRAY_V5

class DHCP_MSCOPE_INFO(NdrStructure):
    MEMBERS = [(PWCHAR_T, "MScopeName"),(PWCHAR_T, "MScopeComment"),(DWORD, "MScopeId"),(DWORD, "MScopeAddressPolicy"),(DHCP_HOST_INFO, "PrimaryHost"),(DHCP_SUBNET_STATE, "MScopeState"),(DWORD, "MScopeFlags"),(DATE_TIME, "ExpiryTime"),(PWCHAR_T, "LangTag"),(BYTE, "TTL"),]

    
LPDHCP_MSCOPE_INFO = DHCP_MSCOPE_INFO

class DHCP_MSCOPE_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PPWCHAR_T, "pMScopeNames"),]

    
LPDHCP_MSCOPE_TABLE = DHCP_MSCOPE_TABLE

class DHCP_MCLIENT_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DWORD, "MScopeId"),(DHCP_CLIENT_UID, "ClientId"),(PWCHAR_T, "ClientName"),(DATE_TIME, "ClientLeaseStarts"),(DATE_TIME, "ClientLeaseEnds"),(DHCP_HOST_INFO, "OwnerHost"),(DWORD, "AddressFlags"),(BYTE, "AddressState"),]

    
LPDHCP_MCLIENT_INFO = DHCP_MCLIENT_INFO

class DHCP_MCLIENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_MCLIENT_INFO, "Clients"),]

    
LPDHCP_MCLIENT_INFO_ARRAY = DHCP_MCLIENT_INFO_ARRAY

class DHCP_RESERVED_SCOPE6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "ReservedIpAddress"),(DHCP_IPV6_ADDRESS, "ReservedIpSubnetAddress"),]

    
LPDHCP_RESERVED_SCOPE6 = DHCP_RESERVED_SCOPE6

class DHCP_OPTION_SCOPE_INFO6(NdrStructure):
    MEMBERS = [(DHCP_OPTION_SCOPE_TYPE6, "ScopeType"),(SCOPEINFO, "ScopeInfo"),]

    
LPDHCP_OPTION_SCOPE_INFO6 = DHCP_OPTION_SCOPE_INFO6

class DHCP_CLASS_INFO(NdrStructure):
    MEMBERS = [(PWCHAR_T, "ClassName"),(PWCHAR_T, "ClassComment"),(DWORD, "ClassDataLength"),(BOOL, "IsVendor"),(DWORD, "Flags"),(LPBYTE, "ClassData"),]

    
LPDHCP_CLASS_INFO = DHCP_CLASS_INFO

class DHCP_CLASS_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_CLASS_INFO, "Classes"),]

    
LPDHCP_CLASS_INFO_ARRAY = DHCP_CLASS_INFO_ARRAY

class DHCP_ALL_OPTIONS(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(LPDHCP_OPTION_ARRAY, "NonVendorOptions"),(DWORD, "NumVendorOptions"),(PVENDOROPTIONS, "*VendorOptions"),]

    
LPDHCP_ALL_OPTIONS = DHCP_ALL_OPTIONS

class DHCP_ALL_OPTION_VALUES(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(DWORD, "NumElements"),(POPTIONS, "*Options"),]

    
LPDHCP_ALL_OPTION_VALUES = DHCP_ALL_OPTION_VALUES

class MSCOPE_MIB_INFO(NdrStructure):
    MEMBERS = [(DWORD, "MScopeId"),(PWCHAR_T, "MScopeName"),(DWORD, "NumAddressesInuse"),(DWORD, "NumAddressesFree"),(DWORD, "NumPendingOffers"),]

    
LPMSCOPE_MIB_INFO = MSCOPE_MIB_INFO

class DHCP_MCAST_MIB_INFO(NdrStructure):
    MEMBERS = [(DWORD, "Discovers"),(DWORD, "Offers"),(DWORD, "Requests"),(DWORD, "Renews"),(DWORD, "Acks"),(DWORD, "Naks"),(DWORD, "Releases"),(DWORD, "Informs"),(DATE_TIME, "ServerStartTime"),(DWORD, "Scopes"),(LPMSCOPE_MIB_INFO, "ScopeInfo"),]

    
LPDHCP_MCAST_MIB_INFO = DHCP_MCAST_MIB_INFO

class DHCP_ATTRIB(NdrStructure):
    MEMBERS = [(DHCP_ATTRIB_ID, "DhcpAttribId"),(ULONG, "DhcpAttribType"),(U0, "u0"),]

    
PDHCP_ATTRIB = DHCP_ATTRIB
LPDHCP_ATTRIB = DHCP_ATTRIB

class DHCP_ATTRIB_ARRAY(NdrStructure):
    MEMBERS = [(ULONG, "NumElements"),(LPDHCP_ATTRIB, "DhcpAttribs"),]

    
PDHCP_ATTRIB_ARRAY = DHCP_ATTRIB_ARRAY
LPDHCP_ATTRIB_ARRAY = DHCP_ATTRIB_ARRAY

class DHCP_SUBNET_ELEMENT_DATA_V5(NdrStructure):
    MEMBERS = [(DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),(ELEMENT, "Element"),]

    
LPDHCP_SUBNET_ELEMENT_DATA_V5 = DHCP_SUBNET_ELEMENT_DATA_V5

class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_SUBNET_ELEMENT_DATA_V5, "Elements"),]

    
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V5 = DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5

class DHCP_BIND_ELEMENT(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),(BOOL, "fBoundToDHCPServer"),(DHCP_IP_ADDRESS, "AdapterPrimaryAddress"),(DHCP_IP_ADDRESS, "AdapterSubnetAddress"),(PWCHAR_T, "IfDescription"),(ULONG, "IfIdSize"),(LPBYTE, "IfId"),]

    
LPDHCP_BIND_ELEMENT = DHCP_BIND_ELEMENT

class DHCP_BIND_ELEMENT_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_BIND_ELEMENT, "Elements"),]

    
LPDHCP_BIND_ELEMENT_ARRAY = DHCP_BIND_ELEMENT_ARRAY

class DHCP_SERVER_SPECIFIC_STRINGS(NdrStructure):
    MEMBERS = [(PWCHAR_T, "DefaultVendorClassName"),(PWCHAR_T, "DefaultUserClassName"),]

    
LPDHCP_SERVER_SPECIFIC_STRINGS = DHCP_SERVER_SPECIFIC_STRINGS

class SCOPE_MIB_INFO_V5(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "Subnet"),(DWORD, "NumAddressesInuse"),(DWORD, "NumAddressesFree"),(DWORD, "NumPendingOffers"),]

    
LPSCOPE_MIB_INFO_V5 = SCOPE_MIB_INFO_V5

class DHCP_MIB_INFO_V5(NdrStructure):
    MEMBERS = [(DWORD, "Discovers"),(DWORD, "Offers"),(DWORD, "Requests"),(DWORD, "Acks"),(DWORD, "Naks"),(DWORD, "Declines"),(DWORD, "Releases"),(DATE_TIME, "ServerStartTime"),(DWORD, "QtnNumLeases"),(DWORD, "QtnPctQtnLeases"),(DWORD, "QtnProbationLeases"),(DWORD, "QtnNonQtnLeases"),(DWORD, "QtnExemptLeases"),(DWORD, "QtnCapableClients"),(DWORD, "QtnIASErrors"),(DWORD, "DelayedOffers"),(DWORD, "ScopesWithDelayedOffers"),(DWORD, "Scopes"),(LPSCOPE_MIB_INFO_V5, "ScopeInfo"),]

    
LPDHCP_MIB_INFO_V5 = DHCP_MIB_INFO_V5

class DHCP_FILTER_LIST_TYPE(NdrEnum):
    MAP = ((0 , 'Deny'),(1 , 'Allow'),)        

class DHCP_ADDR_PATTERN(NdrStructure):
    MEMBERS = [(BOOL, "MatchHWType"),(BYTE, "HWType"),(BOOL, "IsWildcard"),(BYTE, "Length"),(BYTE, "Pattern"),]

    
LPDHCP_ADDR_PATTERN = DHCP_ADDR_PATTERN

class DHCP_FILTER_ADD_INFO(NdrStructure):
    MEMBERS = [(DHCP_ADDR_PATTERN, "AddrPatt"),(PWCHAR_T, "Comment"),(DHCP_FILTER_LIST_TYPE, "ListType"),]

    
LPDHCP_FILTER_ADD_INFO = DHCP_FILTER_ADD_INFO

class DHCP_FILTER_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(BOOL, "EnforceAllowList"),(BOOL, "EnforceDenyList"),]

    
LPDHCP_FILTER_GLOBAL_INFO = DHCP_FILTER_GLOBAL_INFO

class DHCP_FILTER_RECORD(NdrStructure):
    MEMBERS = [(DHCP_ADDR_PATTERN, "AddrPatt"),(PWCHAR_T, "Comment"),]

    
LPDHCP_FILTER_RECORD = DHCP_FILTER_RECORD

class DHCP_FILTER_ENUM_INFO(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_FILTER_RECORD, "pEnumRecords"),]

    
LPDHCP_FILTER_ENUM_INFO = DHCP_FILTER_ENUM_INFO

class DHCP_SUBNET_INFO_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "SubnetAddress"),(ULONG, "Prefix"),(USHORT, "Preference"),(PWCHAR_T, "SubnetName"),(PWCHAR_T, "SubnetComment"),(DWORD, "State"),(DWORD, "ScopeId"),]

    
PDHCP_SUBNET_INFO_V6 = DHCP_SUBNET_INFO_V6
LPDHCP_SUBNET_INFO_V6 = DHCP_SUBNET_INFO_V6

class DHCPV6_IP_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_IPV6_ADDRESS, "Elements"),]

    
LPDHCPV6_IP_ARRAY = DHCPV6_IP_ARRAY

class DHCP_IP_RANGE_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "StartAddress"),(DHCP_IPV6_ADDRESS, "EndAddress"),]

    
LPDHCP_IP_RANGE_V6 = DHCP_IP_RANGE_V6

class DHCP_IP_RESERVATION_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "ReservedIpAddress"),(PDHCP_CLIENT_UID, "ReservedForClient"),(DWORD, "InterfaceId"),]

    
LPDHCP_IP_RESERVATION_V6 = DHCP_IP_RESERVATION_V6

class DHCP_SUBNET_ELEMENT_DATA_V6(NdrStructure):
    MEMBERS = [(DHCP_SUBNET_ELEMENT_TYPE_V6, "ElementType"),(ELEMENT, "Element"),]

    
LPDHCP_SUBNET_ELEMENT_DATA_V6 = DHCP_SUBNET_ELEMENT_DATA_V6

class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_SUBNET_ELEMENT_DATA_V6, "Elements"),]

    
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6 = DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6
DHCP_RESUME_IPV6_HANDLE = DHCP_IPV6_ADDRESS

class DHCP_HOST_INFO_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "IpAddress"),(PWCHAR_T, "NetBiosName"),(PWCHAR_T, "HostName"),]

    
LPDHCP_HOST_INFO_V6 = DHCP_HOST_INFO_V6

class DHCP_CLIENT_INFO_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "ClientIpAddress"),(DHCP_CLIENT_UID, "ClientDUID"),(DWORD, "AddressType"),(DWORD, "IAID"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientValidLeaseExpires"),(DATE_TIME, "ClientPrefLeaseExpires"),(DHCP_HOST_INFO_V6, "OwnerHost"),]

    
LPDHCP_CLIENT_INFO_V6 = DHCP_CLIENT_INFO_V6

class DHCP_CLIENT_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_V6, "Clients"),]

    
LPDHCP_CLIENT_INFO_ARRAY_V6 = DHCP_CLIENT_INFO_ARRAY_V6

class DHCP_SERVER_CONFIG_INFO_V6(NdrStructure):
    MEMBERS = [(BOOL, "UnicastFlag"),(BOOL, "RapidCommitFlag"),(DWORD, "PreferredLifetime"),(DWORD, "ValidLifetime"),(DWORD, "T1"),(DWORD, "T2"),(DWORD, "PreferredLifetimeIATA"),(DWORD, "ValidLifetimeIATA"),(BOOL, "fAuditLog"),]

    
LPDHCP_SERVER_CONFIG_INFO_V6 = DHCP_SERVER_CONFIG_INFO_V6

class SCOPE_MIB_INFO_V6(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "Subnet"),(ULONGLONG, "NumAddressesInuse"),(ULONGLONG, "NumAddressesFree"),(ULONGLONG, "NumPendingAdvertises"),]

    
LPSCOPE_MIB_INFO_V6 = SCOPE_MIB_INFO_V6

class DHCP_MIB_INFO_V6(NdrStructure):
    MEMBERS = [(DWORD, "Solicits"),(DWORD, "Advertises"),(DWORD, "Requests"),(DWORD, "Renews"),(DWORD, "Rebinds"),(DWORD, "Replies"),(DWORD, "Confirms"),(DWORD, "Declines"),(DWORD, "Releases"),(DWORD, "Informs"),(DATE_TIME, "ServerStartTime"),(DWORD, "Scopes"),(LPSCOPE_MIB_INFO_V6, "ScopeInfo"),]

    
LPDHCP_MIB_INFO_V6 = DHCP_MIB_INFO_V6

class DHCPV6_BIND_ELEMENT(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),(BOOL, "fBoundToDHCPServer"),(DHCP_IPV6_ADDRESS, "AdapterPrimaryAddress"),(DHCP_IPV6_ADDRESS, "AdapterSubnetAddress"),(PWCHAR_T, "IfDescription"),(DWORD, "IpV6IfIndex"),(ULONG, "IfIdSize"),(LPBYTE, "IfId"),]

    
LPDHCPV6_BIND_ELEMENT = DHCPV6_BIND_ELEMENT

class DHCPV6_BIND_ELEMENT_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCPV6_BIND_ELEMENT, "Elements"),]

    
LPDHCPV6_BIND_ELEMENT_ARRAY = DHCPV6_BIND_ELEMENT_ARRAY

class DHCP_SEARCH_INFO_V6(NdrStructure):
    MEMBERS = [(DHCP_SEARCH_INFO_TYPE_V6, "SearchType"),(SEARCHINFO, "SearchInfo"),]

    
LPDHCP_SEARCH_INFO_V6 = DHCP_SEARCH_INFO_V6

class DHCP_CLASS_INFO_V6(NdrStructure):
    MEMBERS = [(PWCHAR_T, "ClassName"),(PWCHAR_T, "ClassComment"),(DWORD, "ClassDataLength"),(BOOL, "IsVendor"),(DWORD, "EnterpriseNumber"),(DWORD, "Flags"),(LPBYTE, "ClassData"),]

    
LPDHCP_CLASS_INFO_V6 = DHCP_CLASS_INFO_V6

class DHCP_CLASS_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_CLASS_INFO_V6, "Classes"),]

    
LPDHCP_CLASS_INFO_ARRAY_V6 = DHCP_CLASS_INFO_ARRAY_V6

class DHCP_CLIENT_FILTER_STATUS_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),(QUARANTINESTATUS, "Status"),(DATE_TIME, "ProbationEnds"),(BOOL, "QuarantineCapable"),(DWORD, "FilterStatus"),]

    
LPDHCP_CLIENT_FILTER_STATUS_INFO = DHCP_CLIENT_FILTER_STATUS_INFO

class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_FILTER_STATUS_INFO, "Clients"),]

    
LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY = DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY

class DHCP_FAILOVER_MODE(NdrEnum):
    MAP = ((0 , 'LoadBalance'),(1 , 'HotStandby'),)        

class DHCP_FAILOVER_SERVER(NdrEnum):
    MAP = ((0 , 'PrimaryServer'),(1 , 'SecondaryServer'),)        

class FSM_STATE(NdrEnum):
    MAP = ((0 , 'NO_STATE'),(1 , 'INIT'),(2 , 'STARTUP'),(3 , 'NORMAL'),(4 , 'COMMUNICATION_INT'),(5 , 'PARTNER_DOWN'),(6 , 'POTENTIAL_CONFLICT'),(7 , 'CONFLICT_DONE'),(8 , 'RESOLUTION_INT'),(9 , 'RECOVER'),(10 , 'RECOVER_WAIT'),(11 , 'RECOVER_DONE'),)        

class DHCP_FAILOVER_RELATIONSHIP(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "primaryServer"),(DHCP_IP_ADDRESS, "secondaryServer"),(DHCP_FAILOVER_MODE, "mode"),(DHCP_FAILOVER_SERVER, "serverType"),(FSM_STATE, "state"),(FSM_STATE, "prevState"),(DWORD, "mclt"),(DWORD, "safePeriod"),(PWCHAR_T, "relationshipName"),(PWCHAR_T, "primaryServerName"),(PWCHAR_T, "secondaryServerName"),(LPDHCP_IP_ARRAY, "pScopes"),(BYTE, "percentage"),(PWCHAR_T, "pSharedSecret"),]

    
LPDHCP_FAILOVER_RELATIONSHIP = DHCP_FAILOVER_RELATIONSHIP

class DHCP_FAILOVER_RELATIONSHIP_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "numElements"),(LPDHCP_FAILOVER_RELATIONSHIP, "pRelationships"),]

    
LPDHCP_FAILOVER_RELATIONSHIP_ARRAY = DHCP_FAILOVER_RELATIONSHIP_ARRAY

class DHCP_FAILOVER_STATISTICS(NdrStructure):
    MEMBERS = [(DWORD, "numAddr"),(DWORD, "addrFree"),(DWORD, "addrInUse"),(DWORD, "partnerAddrFree"),(DWORD, "thisAddrFree"),(DWORD, "partnerAddrInUse"),(DWORD, "thisAddrInUse"),]

    
LPDHCP_FAILOVER_STATISTICS = DHCP_FAILOVER_STATISTICS

class DHCPV4_FAILOVER_CLIENT_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),(QUARANTINESTATUS, "Status"),(DATE_TIME, "ProbationEnds"),(BOOL, "QuarantineCapable"),(DWORD, "SentPotExpTime"),(DWORD, "AckPotExpTime"),(DWORD, "RecvPotExpTime"),(DWORD, "StartTime"),(DWORD, "CltLastTransTime"),(DWORD, "LastBndUpdTime"),(DWORD, "bndMsgStatus"),(PWCHAR_T, "PolicyName"),(BYTE, "flags"),]

    
LPDHCPV4_FAILOVER_CLIENT_INFO = DHCPV4_FAILOVER_CLIENT_INFO

class DHCP_IP_RESERVATION_INFO(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ReservedIpAddress"),(DHCP_CLIENT_UID, "ReservedForClient"),(PWCHAR_T, "ReservedClientName"),(PWCHAR_T, "ReservedClientDesc"),(BYTE, "bAllowedClientTypes"),(BYTE, "fOptionsPresent"),]

    
LPDHCP_IP_RESERVATION_INFO = DHCP_IP_RESERVATION_INFO

class DHCP_RESERVATION_INFO_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_IP_RESERVATION_INFO, "Elements"),]

    
LPDHCP_RESERVATION_INFO_ARRAY = DHCP_RESERVATION_INFO_ARRAY

class DHCP_ALL_OPTION_VALUES_PB(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(DWORD, "NumElements"),(POPTIONS, "*Options"),]

    
LPDHCP_ALL_OPTION_VALUES_PB = DHCP_ALL_OPTION_VALUES_PB

class DHCP_POL_ATTR_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpAttrHWAddr'),(1 , 'DhcpAttrOption'),(2 , 'DhcpAttrSubOption'),(3 , 'DhcpAttrFqdn'),(4 , 'DhcpAttrFqdnSingleLabel'),)        

class DHCP_POL_COMPARATOR(NdrEnum):
    MAP = ((0 , 'DhcpCompEqual'),(1 , 'DhcpCompNotEqual'),(2 , 'DhcpCompBeginsWith'),(3 , 'DhcpCompNotBeginWith'),(4 , 'DhcpCompEndsWith'),(5 , 'DhcpCompNotEndWith'),)        

class DHCP_POL_LOGIC_OPER(NdrEnum):
    MAP = ((0 , 'DhcpLogicalOr'),(1 , 'DhcpLogicalAnd'),)        

class DHCP_POLICY_FIELDS_TO_UPDATE(NdrEnum):
    MAP = ((1 , 'DhcpUpdatePolicyName'),(2 , 'DhcpUpdatePolicyOrder'),(4 , 'DhcpUpdatePolicyExpr'),(8 , 'DhcpUpdatePolicyRanges'),(16 , 'DhcpUpdatePolicyDescr'),(32 , 'DhcpUpdatePolicyStatus'),(64 , 'DhcpUpdatePolicyDnsSuffix'),)        

class DHCP_POL_COND(NdrStructure):
    MEMBERS = [(DWORD, "ParentExpr"),(DHCP_POL_ATTR_TYPE, "Type"),(DWORD, "OptionID"),(DWORD, "SubOptionID"),(PWCHAR_T, "VendorName"),(DHCP_POL_COMPARATOR, "Operator"),(LPBYTE, "Value"),(DWORD, "ValueLength"),]

    
PDHCP_POL_COND = DHCP_POL_COND
LPDHCP_POL_COND = DHCP_POL_COND

class DHCP_POL_COND_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_POL_COND, "Elements"),]

    
PDHCP_POL_COND_ARRAY = DHCP_POL_COND_ARRAY
LPDHCP_POL_COND_ARRAY = DHCP_POL_COND_ARRAY

class DHCP_POL_EXPR(NdrStructure):
    MEMBERS = [(DWORD, "ParentExpr"),(DHCP_POL_LOGIC_OPER, "Operator"),]

    
PDHCP_POL_EXPR = DHCP_POL_EXPR
LPDHCP_POL_EXPR = DHCP_POL_EXPR

class DHCP_POL_EXPR_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_POL_EXPR, "Elements"),]

    
PDHCP_POL_EXPR_ARRAY = DHCP_POL_EXPR_ARRAY
LPDHCP_POL_EXPR_ARRAY = DHCP_POL_EXPR_ARRAY

class DHCP_IP_RANGE_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_IP_RANGE, "Elements"),]

    
PDHCP_IP_RANGE_ARRAY = DHCP_IP_RANGE_ARRAY
LPDHCP_IP_RANGE_ARRAY = DHCP_IP_RANGE_ARRAY

class DHCP_POLICY(NdrStructure):
    MEMBERS = [(PWCHAR_T, "PolicyName"),(BOOL, "IsGlobalPolicy"),(DHCP_IP_ADDRESS, "Subnet"),(DWORD, "ProcessingOrder"),(LPDHCP_POL_COND_ARRAY, "Conditions"),(LPDHCP_POL_EXPR_ARRAY, "Expressions"),(LPDHCP_IP_RANGE_ARRAY, "Ranges"),(PWCHAR_T, "Description"),(BOOL, "Enabled"),]

    
PDHCP_POLICY = DHCP_POLICY
LPDHCP_POLICY = DHCP_POLICY

class DHCP_POLICY_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_POLICY, "Elements"),]

    
PDHCP_POLICY_ARRAY = DHCP_POLICY_ARRAY
LPDHCP_POLICY_ARRAY = DHCP_POLICY_ARRAY

class DHCPV6_STATELESS_PARAMS(NdrStructure):
    MEMBERS = [(BOOL, "Status"),(DWORD, "PurgeInterval"),]

    
PDHCPV6_STATELESS_PARAMS = DHCPV6_STATELESS_PARAMS
LPDHCPV6_STATELESS_PARAMS = DHCPV6_STATELESS_PARAMS

class DHCPV6_STATELESS_SCOPE_STATS(NdrStructure):
    MEMBERS = [(DHCP_IPV6_ADDRESS, "SubnetAddress"),(ULONGLONG, "NumStatelessClientsAdded"),(ULONGLONG, "NumStatelessClientsRemoved"),]

    
PDHCPV6_STATELESS_SCOPE_STATS = DHCPV6_STATELESS_SCOPE_STATS
LPDHCPV6_STATELESS_SCOPE_STATS = DHCPV6_STATELESS_SCOPE_STATS

class DHCPV6_STATELESS_STATS(NdrStructure):
    MEMBERS = [(DWORD, "NumScopes"),(LPDHCPV6_STATELESS_SCOPE_STATS, "ScopeStats"),]

    
PDHCPV6_STATELESS_STATS = DHCPV6_STATELESS_STATS
LPDHCPV6_STATELESS_STATS = DHCPV6_STATELESS_STATS

class DHCP_CLIENT_INFO_PB(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),(QUARANTINESTATUS, "Status"),(DATE_TIME, "ProbationEnds"),(BOOL, "QuarantineCapable"),(DWORD, "FilterStatus"),(PWCHAR_T, "PolicyName"),]

    
LPDHCP_CLIENT_INFO_PB = DHCP_CLIENT_INFO_PB

class DHCP_CLIENT_INFO_PB_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_PB, "Clients"),]

    
LPDHCP_CLIENT_INFO_PB_ARRAY = DHCP_CLIENT_INFO_PB_ARRAY

class DHCP_PROPERTY_TYPE(NdrEnum):
    MAP = ((0 , 'DhcpPropTypeByte'),(1 , 'DhcpPropTypeWord'),(2 , 'DhcpPropTypeDword'),(3 , 'DhcpPropTypeString'),(4 , 'DhcpPropTypeBinary'),)        

class DHCP_PROPERTY_ID(NdrEnum):
    MAP = ((0 , 'DhcpPropIdPolicyDnsSuffix'),(1 , 'DhcpPropIdClientAddressStateEx'),)        

class DHCP_PROPERTY(NdrStructure):
    MEMBERS = [(DHCP_PROPERTY_ID, "ID"),(DHCP_PROPERTY_TYPE, "Type"),(VALUE, "Value"),]

    
PDHCP_PROPERTY = DHCP_PROPERTY
LPDHCP_PROPERTY = DHCP_PROPERTY

class DHCP_PROPERTY_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_PROPERTY, "Elements"),]

    
PDHCP_PROPERTY_ARRAY = DHCP_PROPERTY_ARRAY
LPDHCP_PROPERTY_ARRAY = DHCP_PROPERTY_ARRAY

class DHCP_CLIENT_INFO_EX(NdrStructure):
    MEMBERS = [(DHCP_IP_ADDRESS, "ClientIpAddress"),(DHCP_IP_MASK, "SubnetMask"),(DHCP_CLIENT_UID, "ClientHardwareAddress"),(PWCHAR_T, "ClientName"),(PWCHAR_T, "ClientComment"),(DATE_TIME, "ClientLeaseExpires"),(DHCP_HOST_INFO, "OwnerHost"),(BYTE, "bClientType"),(BYTE, "AddressState"),(QUARANTINESTATUS, "Status"),(DATE_TIME, "ProbationEnds"),(BOOL, "QuarantineCapable"),(DWORD, "FilterStatus"),(PWCHAR_T, "PolicyName"),(LPDHCP_PROPERTY_ARRAY, "Properties"),]

    
LPDHCP_CLIENT_INFO_EX = DHCP_CLIENT_INFO_EX

class DHCP_CLIENT_INFO_EX_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(PLPDHCP_CLIENT_INFO_EX, "Clients"),]

    
LPDHCP_CLIENT_INFO_EX_ARRAY = DHCP_CLIENT_INFO_EX_ARRAY

class DHCP_POLICY_EX(NdrStructure):
    MEMBERS = [(PWCHAR_T, "PolicyName"),(BOOL, "IsGlobalPolicy"),(DHCP_IP_ADDRESS, "Subnet"),(DWORD, "ProcessingOrder"),(LPDHCP_POL_COND_ARRAY, "Conditions"),(LPDHCP_POL_EXPR_ARRAY, "Expressions"),(LPDHCP_IP_RANGE_ARRAY, "Ranges"),(PWCHAR_T, "Description"),(BOOL, "Enabled"),(LPDHCP_PROPERTY_ARRAY, "Properties"),]

    
PDHCP_POLICY_EX = DHCP_POLICY_EX
LPDHCP_POLICY_EX = DHCP_POLICY_EX

class DHCP_POLICY_EX_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "NumElements"),(LPDHCP_POLICY_EX, "Elements"),]

    
PDHCP_POLICY_EX_ARRAY = DHCP_POLICY_EX_ARRAY
LPDHCP_POLICY_EX_ARRAY = DHCP_POLICY_EX_ARRAY
Interface("6BFFD098-A112-3610-9833-46C3F874532D", "1.0",[Method("R_DhcpCreateSubnet",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_INFO,'SubnetInfo')),
),Method("R_DhcpSetSubnetInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_INFO,'SubnetInfo')),
),Method("R_DhcpGetSubnetInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
Out((PLPDHCP_SUBNET_INFO,'SubnetInfo')),
),Method("R_DhcpEnumSubnets",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_IP_ARRAY,'EnumInfo')),
Out((PDWORD,'ElementsRead')),
Out((PDWORD,'ElementsTotal')),
),Method("R_DhcpAddSubnetElement",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_ELEMENT_DATA,'AddElementInfo')),
),Method("R_DhcpEnumSubnetElements",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((DHCP_SUBNET_ELEMENT_TYPE,'EnumElementType')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY,'EnumElementInfo')),
Out((PDWORD,'ElementsRead')),
Out((PDWORD,'ElementsTotal')),
),Method("R_DhcpRemoveSubnetElement",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_ELEMENT_DATA,'RemoveElementInfo')),
In((DHCP_FORCE_FLAG,'ForceFlag')),
),Method("R_DhcpDeleteSubnet",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((DHCP_FORCE_FLAG,'ForceFlag')),
),Method("R_DhcpCreateOption",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
In((LPDHCP_OPTION,'OptionInfo')),
),Method("R_DhcpSetOptionInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
In((LPDHCP_OPTION,'OptionInfo')),
),Method("R_DhcpGetOptionInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
Out((PLPDHCP_OPTION,'OptionInfo')),
),Method("R_DhcpRemoveOption",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
),Method("R_DhcpSetOptionValue",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
In((LPDHCP_OPTION_SCOPE_INFO,'ScopeInfo')),
In((LPDHCP_OPTION_DATA,'OptionValue')),
),Method("R_DhcpGetOptionValue",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
In((LPDHCP_OPTION_SCOPE_INFO,'ScopeInfo')),
Out((PLPDHCP_OPTION_VALUE,'OptionValue')),
),Method("R_DhcpEnumOptionValues",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_OPTION_SCOPE_INFO,'ScopeInfo')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_OPTION_VALUE_ARRAY,'OptionValues')),
Out((PDWORD,'OptionsRead')),
Out((PDWORD,'OptionsTotal')),
),Method("R_DhcpRemoveOptionValue",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_OPTION_ID,'OptionID')),
In((LPDHCP_OPTION_SCOPE_INFO,'ScopeInfo')),
),Method("R_DhcpCreateClientInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO,'ClientInfo')),
),Method("R_DhcpSetClientInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO,'ClientInfo')),
),Method("R_DhcpGetClientInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_SEARCH_INFO,'SearchInfo')),
Out((PLPDHCP_CLIENT_INFO,'ClientInfo')),
),Method("R_DhcpDeleteClientInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_SEARCH_INFO,'ClientInfo')),
),Method("R_DhcpEnumSubnetClients",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_CLIENT_INFO_ARRAY,'ClientInfo')),
Out((PDWORD,'ClientsRead')),
Out((PDWORD,'ClientsTotal')),
),Method("R_DhcpGetClientOptions",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'ClientIpAddress')),
In((DHCP_IP_MASK,'ClientSubnetMask')),
Out((PLPDHCP_OPTION_LIST,'ClientOptions')),
),Method("R_DhcpGetMibInfo",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_MIB_INFO,'MibInfo')),
),Method("R_DhcpEnumOptions",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_OPTION_ARRAY,'Options')),
Out((PDWORD,'OptionsRead')),
Out((PDWORD,'OptionsTotal')),
),Method("R_DhcpSetOptionValues",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_OPTION_SCOPE_INFO,'ScopeInfo')),
In((LPDHCP_OPTION_VALUE_ARRAY,'OptionValues')),
),Method("R_DhcpServerSetConfig",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DWORD,'FieldsToSet')),
In((LPDHCP_SERVER_CONFIG_INFO,'ConfigInfo')),
),Method("R_DhcpServerGetConfig",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_SERVER_CONFIG_INFO,'ConfigInfo')),
),Method("R_DhcpScanDatabase",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((DWORD,'FixFlag')),
Out((PLPDHCP_SCAN_LIST,'ScanList')),
),Method("R_DhcpGetVersion",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((LPDWORD,'MajorVersion')),
Out((LPDWORD,'MinorVersion')),
),Method("R_DhcpAddSubnetElementV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_ELEMENT_DATA_V4,'AddElementInfo')),
),Method("R_DhcpEnumSubnetElementsV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((DHCP_SUBNET_ELEMENT_TYPE,'EnumElementType')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4,'EnumElementInfo')),
Out((PDWORD,'ElementsRead')),
Out((PDWORD,'ElementsTotal')),
),Method("R_DhcpRemoveSubnetElementV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_ELEMENT_DATA_V4,'RemoveElementInfo')),
In((DHCP_FORCE_FLAG,'ForceFlag')),
),Method("R_DhcpCreateClientInfoV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO_V4,'ClientInfo')),
),Method("R_DhcpSetClientInfoV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO_V4,'ClientInfo')),
),Method("R_DhcpGetClientInfoV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_SEARCH_INFO,'SearchInfo')),
Out((PLPDHCP_CLIENT_INFO_V4,'ClientInfo')),
),Method("R_DhcpEnumSubnetClientsV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_CLIENT_INFO_ARRAY_V4,'ClientInfo')),
Out((PDWORD,'ClientsRead')),
Out((PDWORD,'ClientsTotal')),
),Method("R_DhcpSetSuperScopeV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((PWCHAR,'SuperScopeName')),
In((BOOL,'ChangeExisting')),
),Method("R_DhcpGetSuperScopeInfoV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_SUPER_SCOPE_TABLE,'SuperScopeTable')),
),Method("R_DhcpDeleteSuperScopeV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((PWCHAR,'SuperScopeName')),
),Method("R_DhcpServerSetConfigV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DWORD,'FieldsToSet')),
In((LPDHCP_SERVER_CONFIG_INFO_V4,'ConfigInfo')),
),Method("R_DhcpServerGetConfigV4",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_SERVER_CONFIG_INFO_V4,'ConfigInfo')),
),Method("R_DhcpServerSetConfigVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DWORD,'FieldsToSet')),
In((LPDHCP_SERVER_CONFIG_INFO_VQ,'ConfigInfo')),
),Method("R_DhcpServerGetConfigVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_SERVER_CONFIG_INFO_VQ,'ConfigInfo')),
),Method("R_DhcpGetMibInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
Out((PLPDHCP_MIB_INFO_VQ,'MibInfo')),
),Method("R_DhcpCreateClientInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO_VQ,'ClientInfo')),
),Method("R_DhcpSetClientInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_CLIENT_INFO_VQ,'ClientInfo')),
),Method("R_DhcpGetClientInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((LPDHCP_SEARCH_INFO,'SearchInfo')),
Out((PLPDHCP_CLIENT_INFO_VQ,'ClientInfo')),
),Method("R_DhcpEnumSubnetClientsVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
InOut((PDHCP_RESUME_HANDLE,'ResumeHandle')),
In((DWORD,'PreferredMaximum')),
Out((PLPDHCP_CLIENT_INFO_ARRAY_VQ,'ClientInfo')),
Out((PDWORD,'ClientsRead')),
Out((PDWORD,'ClientsTotal')),
),Method("R_DhcpCreateSubnetVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_INFO_VQ,'SubnetInfoVQ')),
),Method("R_DhcpGetSubnetInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
Out((PLPDHCP_SUBNET_INFO_VQ,'SubnetInfoVQ')),
),Method("R_DhcpSetSubnetInfoVQ",
In((DHCP_SRV_HANDLE,'ServerIpAddress')),
In((DHCP_IP_ADDRESS,'SubnetAddress')),
In((LPDHCP_SUBNET_INFO_VQ,'SubnetInfoVQ')),
),])