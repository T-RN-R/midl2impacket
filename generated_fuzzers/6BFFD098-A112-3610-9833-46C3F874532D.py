
from fuzzer.midl import *
from fuzzer.core import *

class ('FILETIME', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLowDateTime"),(('DWORD', None), "dwHighDateTime"),]

    

class ('GUID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "Data1"),(('UNSIGNED_SHORT', None), "Data2"),(('UNSIGNED_SHORT', None), "Data3"),(('BYTE', None), "Data4"),]

    

class ('LARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('SIGNED___INT64', None), "QuadPart"),]

    

class ('EVENT_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Id"),(('UCHAR', None), "Version"),(('UCHAR', None), "Channel"),(('UCHAR', None), "Level"),(('UCHAR', None), "Opcode"),(('USHORT', None), "Task"),(('ULONGLONG', None), "Keyword"),]

    

class ('S0', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "KernelTime"),(('ULONG', None), "UserTime"),]

    

class ('U0', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('S0', None), s0),2 : (('ULONG64', None), ProcessorTime),}

    

class ('EVENT_HEADER', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Size"),(('USHORT', None), "HeaderType"),(('USHORT', None), "Flags"),(('USHORT', None), "EventProperty"),(('ULONG', None), "ThreadId"),(('ULONG', None), "ProcessId"),(('LARGE_INTEGER', None), "TimeStamp"),(('GUID', None), "ProviderId"),(('EVENT_DESCRIPTOR', None), "EventDescriptor"),(('U0', None), "u0"),(('GUID', None), "ActivityId"),]

    

class ('LUID', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "LowPart"),(('LONG', None), "HighPart"),]

    

class ('MULTI_SZ', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "Value"),(('DWORD', None), "nChar"),]

    

class ('RPC_UNICODE_STRING', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "Length"),(('UNSIGNED_SHORT', None), "MaximumLength"),(('PWCHAR', None), "Buffer"),]

    

class ('SERVER_INFO_100', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv100_platform_id"),(('PWCHAR_T', None), "sv100_name"),]

    

class ('SERVER_INFO_101', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv101_platform_id"),(('PWCHAR_T', None), "sv101_name"),(('DWORD', None), "sv101_version_major"),(('DWORD', None), "sv101_version_minor"),(('DWORD', None), "sv101_version_type"),(('PWCHAR_T', None), "sv101_comment"),]

    

class ('SYSTEMTIME', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wYear"),(('WORD', None), "wMonth"),(('WORD', None), "wDayOfWeek"),(('WORD', None), "wDay"),(('WORD', None), "wHour"),(('WORD', None), "wMinute"),(('WORD', None), "wSecond"),(('WORD', None), "wMilliseconds"),]

    

class ('UINT128', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "lower"),(('UINT64', None), "upper"),]

    

class ('ULARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT64', None), "QuadPart"),]

    

class ('RPC_SID_IDENTIFIER_AUTHORITY', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "Value"),]

    

class ('OBJECT_TYPE_LIST', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "Level"),(('ACCESS_MASK', None), "Remaining"),(('PGUID', None), "ObjectType"),]

    

class ('ACE_HEADER', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "AceType"),(('UCHAR', None), "AceFlags"),(('USHORT', None), "AceSize"),]

    

class ('SYSTEM_MANDATORY_LABEL_ACE', None)(NdrStructure):
    MEMBERS = [(('ACE_HEADER', None), "Header"),(('ACCESS_MASK', None), "Mask"),(('DWORD', None), "SidStart"),]

    

class ('TOKEN_MANDATORY_POLICY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Policy"),]

    

class ('MANDATORY_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('ACCESS_MASK', None), "AllowedAccess"),(('BOOLEAN', None), "WriteAllowed"),(('BOOLEAN', None), "ReadAllowed"),(('BOOLEAN', None), "ExecuteAllowed"),(('TOKEN_MANDATORY_POLICY', None), "MandatoryPolicy"),]

    

class ('CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Length"),(('BYTE', None), "OctetString"),]

    

class ('VALUES', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PLONG64', None), pInt64),2 : (('PDWORD64', None), pUint64),3 : (('PWSTR', None), ppString),4 : (('PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None), pOctetString),}

    

class ('CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Name"),(('WORD', None), "ValueType"),(('WORD', None), "Reserved"),(('DWORD', None), "Flags"),(('DWORD', None), "ValueCount"),(('VALUES', None), "Values"),]

    

class ('RPC_SID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "Revision"),(('UNSIGNED_CHAR', None), "SubAuthorityCount"),(('RPC_SID_IDENTIFIER_AUTHORITY', None), "IdentifierAuthority"),(('UNSIGNED_LONG', None), "SubAuthority"),]

    

class ('ACL', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "AclRevision"),(('UNSIGNED_CHAR', None), "Sbz1"),(('UNSIGNED_SHORT', None), "AclSize"),(('UNSIGNED_SHORT', None), "AceCount"),(('UNSIGNED_SHORT', None), "Sbz2"),]

    

class ('SECURITY_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Revision"),(('UCHAR', None), "Sbz1"),(('USHORT', None), "Control"),(('PSID', None), "Owner"),(('PSID', None), "Group"),(('PACL', None), "Sacl"),(('PACL', None), "Dacl"),]

    

class ('DHCP_BINARY_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "DataLength"),(('PBYTE', None), "Data"),]

    

class ('DHCP_HOST_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "IpAddress"),(('PWCHAR_T', None), "NetBiosName"),(('PWCHAR_T', None), "HostName"),]

    

class ('DHCP_SUBNET_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "SubnetAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('PWCHAR_T', None), "SubnetName"),(('PWCHAR_T', None), "SubnetComment"),(('DHCP_HOST_INFO', None), "PrimaryHost"),(('DHCP_SUBNET_STATE', None), "SubnetState"),]

    

class ('DHCP_IP_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_IP_ADDRESS', None), "Elements"),]

    

class ('DHCP_IP_RANGE', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "StartAddress"),(('DHCP_IP_ADDRESS', None), "EndAddress"),]

    

class ('DHCP_IP_RESERVATION', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ReservedIpAddress"),(('PDHCP_CLIENT_UID', None), "ReservedForClient"),]

    

class ('DHCP_IP_CLUSTER', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClusterAddress"),(('DWORD', None), "ClusterMask"),]

    

class ('DHCP_BOOTP_IP_RANGE', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "StartAddress"),(('DHCP_IP_ADDRESS', None), "EndAddress"),(('ULONG', None), "BootpAllocated"),(('ULONG', None), "MaxBootpAllowed"),]

    

class ('DHCP_SUBNET_ELEMENT_DATA', None)(NdrStructure):
    MEMBERS = [(('DHCP_SUBNET_ELEMENT_TYPE', None), "ElementType"),(('ELEMENT', None), "Element"),]

    

class ('DHCP_SUBNET_ELEMENT_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_SUBNET_ELEMENT_DATA', None), "Elements"),]

    

class ('DWORD_DWORD', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "DWord1"),(('DWORD', None), "DWord2"),]

    

class ('DHCP_OPTION_DATA_ELEMENT', None)(NdrStructure):
    MEMBERS = [(('DHCP_OPTION_DATA_TYPE', None), "OptionType"),(('ELEMENT', None), "Element"),]

    

class ('DHCP_OPTION_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_OPTION_DATA_ELEMENT', None), "Elements"),]

    

class ('DHCP_OPTION', None)(NdrStructure):
    MEMBERS = [(('DHCP_OPTION_ID', None), "OptionID"),(('PWCHAR_T', None), "OptionName"),(('PWCHAR_T', None), "OptionComment"),(('DHCP_OPTION_DATA', None), "DefaultValue"),(('DHCP_OPTION_TYPE', None), "OptionType"),]

    

class ('DHCP_RESERVED_SCOPE', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ReservedIpAddress"),(('DHCP_IP_ADDRESS', None), "ReservedIpSubnetAddress"),]

    

class ('DHCP_OPTION_SCOPE_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_OPTION_SCOPE_TYPE', None), "ScopeType"),(('SCOPEINFO', None), "ScopeInfo"),]

    

class ('DHCP_OPTION_VALUE', None)(NdrStructure):
    MEMBERS = [(('DHCP_OPTION_ID', None), "OptionID"),(('DHCP_OPTION_DATA', None), "Value"),]

    

class ('DHCP_OPTION_VALUE_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_OPTION_VALUE', None), "Values"),]

    

class ('DATE_TIME', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLowDateTime"),(('DWORD', None), "dwHighDateTime"),]

    

class ('DHCP_CLIENT_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),]

    

class ('DHCP_SEARCH_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_SEARCH_INFO_TYPE', None), "SearchType"),(('SEARCHINFO', None), "SearchInfo"),]

    

class ('DHCP_CLIENT_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO', None), "Clients"),]

    

class ('DHCP_OPTION_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumOptions"),(('PDHCP_OPTION_VALUE', None), "Options"),]

    

class ('SCOPE_MIB_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "Subnet"),(('DWORD', None), "NumAddressesInuse"),(('DWORD', None), "NumAddressesFree"),(('DWORD', None), "NumPendingOffers"),]

    

class ('DHCP_MIB_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Discovers"),(('DWORD', None), "Offers"),(('DWORD', None), "Requests"),(('DWORD', None), "Acks"),(('DWORD', None), "Naks"),(('DWORD', None), "Declines"),(('DWORD', None), "Releases"),(('DATE_TIME', None), "ServerStartTime"),(('DWORD', None), "Scopes"),(('LPSCOPE_MIB_INFO', None), "ScopeInfo"),]

    

class ('DHCP_OPTION_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_OPTION', None), "Options"),]

    

class ('DHCP_SERVER_CONFIG_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "APIProtocolSupport"),(('PWCHAR_T', None), "DatabaseName"),(('PWCHAR_T', None), "DatabasePath"),(('PWCHAR_T', None), "BackupPath"),(('DWORD', None), "BackupInterval"),(('DWORD', None), "DatabaseLoggingFlag"),(('DWORD', None), "RestoreFlag"),(('DWORD', None), "DatabaseCleanupInterval"),(('DWORD', None), "DebugFlag"),]

    

class ('DHCP_SCAN_ITEM', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "IpAddress"),(('DHCP_SCAN_FLAG', None), "ScanFlag"),]

    

class ('DHCP_SCAN_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumScanItems"),(('PDHCP_SCAN_ITEM', None), "ScanItems"),]

    

class ('DHCP_IP_RESERVATION_V4', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ReservedIpAddress"),(('PDHCP_CLIENT_UID', None), "ReservedForClient"),(('BYTE', None), "bAllowedClientTypes"),]

    

class ('DHCP_SUBNET_ELEMENT_DATA_V4', None)(NdrStructure):
    MEMBERS = [(('DHCP_SUBNET_ELEMENT_TYPE', None), "ElementType"),(('ELEMENT', None), "Element"),]

    

class ('DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_SUBNET_ELEMENT_DATA_V4', None), "Elements"),]

    

class ('DHCP_CLIENT_INFO_V4', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),]

    

class ('DHCP_CLIENT_INFO_ARRAY_V4', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_V4', None), "Clients"),]

    

class ('DHCP_SUPER_SCOPE_TABLE_ENTRY', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "SubnetAddress"),(('DWORD', None), "SuperScopeNumber"),(('DWORD', None), "NextInSuperScope"),(('PWCHAR_T', None), "SuperScopeName"),]

    

class ('DHCP_SUPER_SCOPE_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "cEntries"),(('PDHCP_SUPER_SCOPE_TABLE_ENTRY', None), "pEntries"),]

    

class ('DHCP_SERVER_CONFIG_INFO_V4', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "APIProtocolSupport"),(('PWCHAR_T', None), "DatabaseName"),(('PWCHAR_T', None), "DatabasePath"),(('PWCHAR_T', None), "BackupPath"),(('DWORD', None), "BackupInterval"),(('DWORD', None), "DatabaseLoggingFlag"),(('DWORD', None), "RestoreFlag"),(('DWORD', None), "DatabaseCleanupInterval"),(('DWORD', None), "DebugFlag"),(('DWORD', None), "dwPingRetries"),(('DWORD', None), "cbBootTableString"),(('PWCHAR', None), "wszBootTableString"),(('BOOL', None), "fAuditLog"),]

    

class ('DHCP_SERVER_CONFIG_INFO_VQ', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "APIProtocolSupport"),(('PWCHAR_T', None), "DatabaseName"),(('PWCHAR_T', None), "DatabasePath"),(('PWCHAR_T', None), "BackupPath"),(('DWORD', None), "BackupInterval"),(('DWORD', None), "DatabaseLoggingFlag"),(('DWORD', None), "RestoreFlag"),(('DWORD', None), "DatabaseCleanupInterval"),(('DWORD', None), "DebugFlag"),(('DWORD', None), "dwPingRetries"),(('DWORD', None), "cbBootTableString"),(('PWCHAR', None), "wszBootTableString"),(('BOOL', None), "fAuditLog"),(('BOOL', None), "QuarantineOn"),(('DWORD', None), "QuarDefFail"),(('BOOL', None), "QuarRuntimeStatus"),]

    

class ('SCOPE_MIB_INFO_VQ', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "Subnet"),(('DWORD', None), "NumAddressesInuse"),(('DWORD', None), "NumAddressesFree"),(('DWORD', None), "NumPendingOffers"),(('DWORD', None), "QtnNumLeases"),(('DWORD', None), "QtnPctQtnLeases"),(('DWORD', None), "QtnProbationLeases"),(('DWORD', None), "QtnNonQtnLeases"),(('DWORD', None), "QtnExemptLeases"),(('DWORD', None), "QtnCapableClients"),]

    

class ('DHCP_MIB_INFO_VQ', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Discovers"),(('DWORD', None), "Offers"),(('DWORD', None), "Requests"),(('DWORD', None), "Acks"),(('DWORD', None), "Naks"),(('DWORD', None), "Declines"),(('DWORD', None), "Releases"),(('DATE_TIME', None), "ServerStartTime"),(('DWORD', None), "QtnNumLeases"),(('DWORD', None), "QtnPctQtnLeases"),(('DWORD', None), "QtnProbationLeases"),(('DWORD', None), "QtnNonQtnLeases"),(('DWORD', None), "QtnExemptLeases"),(('DWORD', None), "QtnCapableClients"),(('DWORD', None), "QtnIASErrors"),(('DWORD', None), "Scopes"),(('LPSCOPE_MIB_INFO_VQ', None), "ScopeInfo"),]

    

class ('DHCP_CLIENT_INFO_VQ', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),(('QUARANTINESTATUS', None), "Status"),(('DATE_TIME', None), "ProbationEnds"),(('BOOL', None), "QuarantineCapable"),]

    

class ('DHCP_CLIENT_INFO_ARRAY_VQ', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_VQ', None), "Clients"),]

    

class ('DHCP_SUBNET_INFO_VQ', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "SubnetAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('PWCHAR_T', None), "SubnetName"),(('PWCHAR_T', None), "SubnetComment"),(('DHCP_HOST_INFO', None), "PrimaryHost"),(('DHCP_SUBNET_STATE', None), "SubnetState"),(('DWORD', None), "QuarantineOn"),(('DWORD', None), "Reserved1"),(('DWORD', None), "Reserved2"),(('INT64', None), "Reserved3"),(('INT64', None), "Reserved4"),]

    

class ('DHCP_IPV6_ADDRESS', None)(NdrStructure):
    MEMBERS = [(('ULONGLONG', None), "HighOrderBits"),(('ULONGLONG', None), "LowOrderBits"),]

    

class ('DHCP_CLIENT_INFO_V5', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),]

    

class ('DHCP_CLIENT_INFO_ARRAY_V5', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_V5', None), "Clients"),]

    

class ('DHCP_MSCOPE_INFO', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "MScopeName"),(('PWCHAR_T', None), "MScopeComment"),(('DWORD', None), "MScopeId"),(('DWORD', None), "MScopeAddressPolicy"),(('DHCP_HOST_INFO', None), "PrimaryHost"),(('DHCP_SUBNET_STATE', None), "MScopeState"),(('DWORD', None), "MScopeFlags"),(('DATE_TIME', None), "ExpiryTime"),(('PWCHAR_T', None), "LangTag"),(('BYTE', None), "TTL"),]

    

class ('DHCP_MSCOPE_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PPWCHAR_T', None), "pMScopeNames"),]

    

class ('DHCP_MCLIENT_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DWORD', None), "MScopeId"),(('DHCP_CLIENT_UID', None), "ClientId"),(('PWCHAR_T', None), "ClientName"),(('DATE_TIME', None), "ClientLeaseStarts"),(('DATE_TIME', None), "ClientLeaseEnds"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('DWORD', None), "AddressFlags"),(('BYTE', None), "AddressState"),]

    

class ('DHCP_MCLIENT_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_MCLIENT_INFO', None), "Clients"),]

    

class ('DHCP_RESERVED_SCOPE6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "ReservedIpAddress"),(('DHCP_IPV6_ADDRESS', None), "ReservedIpSubnetAddress"),]

    

class ('DHCP_OPTION_SCOPE_INFO6', None)(NdrStructure):
    MEMBERS = [(('DHCP_OPTION_SCOPE_TYPE6', None), "ScopeType"),(('SCOPEINFO', None), "ScopeInfo"),]

    

class ('DHCP_CLASS_INFO', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "ClassName"),(('PWCHAR_T', None), "ClassComment"),(('DWORD', None), "ClassDataLength"),(('BOOL', None), "IsVendor"),(('DWORD', None), "Flags"),(('LPBYTE', None), "ClassData"),]

    

class ('DHCP_CLASS_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_CLASS_INFO', None), "Classes"),]

    

class ('DHCP_ALL_OPTIONS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Flags"),(('LPDHCP_OPTION_ARRAY', None), "NonVendorOptions"),(('DWORD', None), "NumVendorOptions"),(('PVENDOROPTIONS', None), "*VendorOptions"),]

    

class ('DHCP_ALL_OPTION_VALUES', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Flags"),(('DWORD', None), "NumElements"),(('POPTIONS', None), "*Options"),]

    

class ('MSCOPE_MIB_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "MScopeId"),(('PWCHAR_T', None), "MScopeName"),(('DWORD', None), "NumAddressesInuse"),(('DWORD', None), "NumAddressesFree"),(('DWORD', None), "NumPendingOffers"),]

    

class ('DHCP_MCAST_MIB_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Discovers"),(('DWORD', None), "Offers"),(('DWORD', None), "Requests"),(('DWORD', None), "Renews"),(('DWORD', None), "Acks"),(('DWORD', None), "Naks"),(('DWORD', None), "Releases"),(('DWORD', None), "Informs"),(('DATE_TIME', None), "ServerStartTime"),(('DWORD', None), "Scopes"),(('LPMSCOPE_MIB_INFO', None), "ScopeInfo"),]

    

class ('DHCP_ATTRIB', None)(NdrStructure):
    MEMBERS = [(('DHCP_ATTRIB_ID', None), "DhcpAttribId"),(('ULONG', None), "DhcpAttribType"),(('U0', None), "u0"),]

    

class ('DHCP_ATTRIB_ARRAY', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "NumElements"),(('LPDHCP_ATTRIB', None), "DhcpAttribs"),]

    

class ('DHCP_SUBNET_ELEMENT_DATA_V5', None)(NdrStructure):
    MEMBERS = [(('DHCP_SUBNET_ELEMENT_TYPE', None), "ElementType"),(('ELEMENT', None), "Element"),]

    

class ('DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_SUBNET_ELEMENT_DATA_V5', None), "Elements"),]

    

class ('DHCP_BIND_ELEMENT', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Flags"),(('BOOL', None), "fBoundToDHCPServer"),(('DHCP_IP_ADDRESS', None), "AdapterPrimaryAddress"),(('DHCP_IP_ADDRESS', None), "AdapterSubnetAddress"),(('PWCHAR_T', None), "IfDescription"),(('ULONG', None), "IfIdSize"),(('LPBYTE', None), "IfId"),]

    

class ('DHCP_BIND_ELEMENT_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_BIND_ELEMENT', None), "Elements"),]

    

class ('DHCP_SERVER_SPECIFIC_STRINGS', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "DefaultVendorClassName"),(('PWCHAR_T', None), "DefaultUserClassName"),]

    

class ('SCOPE_MIB_INFO_V5', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "Subnet"),(('DWORD', None), "NumAddressesInuse"),(('DWORD', None), "NumAddressesFree"),(('DWORD', None), "NumPendingOffers"),]

    

class ('DHCP_MIB_INFO_V5', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Discovers"),(('DWORD', None), "Offers"),(('DWORD', None), "Requests"),(('DWORD', None), "Acks"),(('DWORD', None), "Naks"),(('DWORD', None), "Declines"),(('DWORD', None), "Releases"),(('DATE_TIME', None), "ServerStartTime"),(('DWORD', None), "QtnNumLeases"),(('DWORD', None), "QtnPctQtnLeases"),(('DWORD', None), "QtnProbationLeases"),(('DWORD', None), "QtnNonQtnLeases"),(('DWORD', None), "QtnExemptLeases"),(('DWORD', None), "QtnCapableClients"),(('DWORD', None), "QtnIASErrors"),(('DWORD', None), "DelayedOffers"),(('DWORD', None), "ScopesWithDelayedOffers"),(('DWORD', None), "Scopes"),(('LPSCOPE_MIB_INFO_V5', None), "ScopeInfo"),]

    

class ('DHCP_ADDR_PATTERN', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "MatchHWType"),(('BYTE', None), "HWType"),(('BOOL', None), "IsWildcard"),(('BYTE', None), "Length"),(('BYTE', None), "Pattern"),]

    

class ('DHCP_FILTER_ADD_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_ADDR_PATTERN', None), "AddrPatt"),(('PWCHAR_T', None), "Comment"),(('DHCP_FILTER_LIST_TYPE', None), "ListType"),]

    

class ('DHCP_FILTER_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "EnforceAllowList"),(('BOOL', None), "EnforceDenyList"),]

    

class ('DHCP_FILTER_RECORD', None)(NdrStructure):
    MEMBERS = [(('DHCP_ADDR_PATTERN', None), "AddrPatt"),(('PWCHAR_T', None), "Comment"),]

    

class ('DHCP_FILTER_ENUM_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_FILTER_RECORD', None), "pEnumRecords"),]

    

class ('DHCP_SUBNET_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "SubnetAddress"),(('ULONG', None), "Prefix"),(('USHORT', None), "Preference"),(('PWCHAR_T', None), "SubnetName"),(('PWCHAR_T', None), "SubnetComment"),(('DWORD', None), "State"),(('DWORD', None), "ScopeId"),]

    

class ('DHCPV6_IP_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_IPV6_ADDRESS', None), "Elements"),]

    

class ('DHCP_IP_RANGE_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "StartAddress"),(('DHCP_IPV6_ADDRESS', None), "EndAddress"),]

    

class ('DHCP_IP_RESERVATION_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "ReservedIpAddress"),(('PDHCP_CLIENT_UID', None), "ReservedForClient"),(('DWORD', None), "InterfaceId"),]

    

class ('DHCP_SUBNET_ELEMENT_DATA_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_SUBNET_ELEMENT_TYPE_V6', None), "ElementType"),(('ELEMENT', None), "Element"),]

    

class ('DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_SUBNET_ELEMENT_DATA_V6', None), "Elements"),]

    

class ('DHCP_HOST_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "IpAddress"),(('PWCHAR_T', None), "NetBiosName"),(('PWCHAR_T', None), "HostName"),]

    

class ('DHCP_CLIENT_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "ClientIpAddress"),(('DHCP_CLIENT_UID', None), "ClientDUID"),(('DWORD', None), "AddressType"),(('DWORD', None), "IAID"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientValidLeaseExpires"),(('DATE_TIME', None), "ClientPrefLeaseExpires"),(('DHCP_HOST_INFO_V6', None), "OwnerHost"),]

    

class ('DHCP_CLIENT_INFO_ARRAY_V6', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_V6', None), "Clients"),]

    

class ('DHCP_SERVER_CONFIG_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "UnicastFlag"),(('BOOL', None), "RapidCommitFlag"),(('DWORD', None), "PreferredLifetime"),(('DWORD', None), "ValidLifetime"),(('DWORD', None), "T1"),(('DWORD', None), "T2"),(('DWORD', None), "PreferredLifetimeIATA"),(('DWORD', None), "ValidLifetimeIATA"),(('BOOL', None), "fAuditLog"),]

    

class ('SCOPE_MIB_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "Subnet"),(('ULONGLONG', None), "NumAddressesInuse"),(('ULONGLONG', None), "NumAddressesFree"),(('ULONGLONG', None), "NumPendingAdvertises"),]

    

class ('DHCP_MIB_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Solicits"),(('DWORD', None), "Advertises"),(('DWORD', None), "Requests"),(('DWORD', None), "Renews"),(('DWORD', None), "Rebinds"),(('DWORD', None), "Replies"),(('DWORD', None), "Confirms"),(('DWORD', None), "Declines"),(('DWORD', None), "Releases"),(('DWORD', None), "Informs"),(('DATE_TIME', None), "ServerStartTime"),(('DWORD', None), "Scopes"),(('LPSCOPE_MIB_INFO_V6', None), "ScopeInfo"),]

    

class ('DHCPV6_BIND_ELEMENT', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Flags"),(('BOOL', None), "fBoundToDHCPServer"),(('DHCP_IPV6_ADDRESS', None), "AdapterPrimaryAddress"),(('DHCP_IPV6_ADDRESS', None), "AdapterSubnetAddress"),(('PWCHAR_T', None), "IfDescription"),(('DWORD', None), "IpV6IfIndex"),(('ULONG', None), "IfIdSize"),(('LPBYTE', None), "IfId"),]

    

class ('DHCPV6_BIND_ELEMENT_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCPV6_BIND_ELEMENT', None), "Elements"),]

    

class ('DHCP_SEARCH_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('DHCP_SEARCH_INFO_TYPE_V6', None), "SearchType"),(('SEARCHINFO', None), "SearchInfo"),]

    

class ('DHCP_CLASS_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "ClassName"),(('PWCHAR_T', None), "ClassComment"),(('DWORD', None), "ClassDataLength"),(('BOOL', None), "IsVendor"),(('DWORD', None), "EnterpriseNumber"),(('DWORD', None), "Flags"),(('LPBYTE', None), "ClassData"),]

    

class ('DHCP_CLASS_INFO_ARRAY_V6', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_CLASS_INFO_V6', None), "Classes"),]

    

class ('DHCP_CLIENT_FILTER_STATUS_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),(('QUARANTINESTATUS', None), "Status"),(('DATE_TIME', None), "ProbationEnds"),(('BOOL', None), "QuarantineCapable"),(('DWORD', None), "FilterStatus"),]

    

class ('DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_FILTER_STATUS_INFO', None), "Clients"),]

    

class ('DHCP_FAILOVER_RELATIONSHIP', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "primaryServer"),(('DHCP_IP_ADDRESS', None), "secondaryServer"),(('DHCP_FAILOVER_MODE', None), "mode"),(('DHCP_FAILOVER_SERVER', None), "serverType"),(('FSM_STATE', None), "state"),(('FSM_STATE', None), "prevState"),(('DWORD', None), "mclt"),(('DWORD', None), "safePeriod"),(('PWCHAR_T', None), "relationshipName"),(('PWCHAR_T', None), "primaryServerName"),(('PWCHAR_T', None), "secondaryServerName"),(('LPDHCP_IP_ARRAY', None), "pScopes"),(('BYTE', None), "percentage"),(('PWCHAR_T', None), "pSharedSecret"),]

    

class ('DHCP_FAILOVER_RELATIONSHIP_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "numElements"),(('LPDHCP_FAILOVER_RELATIONSHIP', None), "pRelationships"),]

    

class ('DHCP_FAILOVER_STATISTICS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "numAddr"),(('DWORD', None), "addrFree"),(('DWORD', None), "addrInUse"),(('DWORD', None), "partnerAddrFree"),(('DWORD', None), "thisAddrFree"),(('DWORD', None), "partnerAddrInUse"),(('DWORD', None), "thisAddrInUse"),]

    

class ('DHCPV4_FAILOVER_CLIENT_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),(('QUARANTINESTATUS', None), "Status"),(('DATE_TIME', None), "ProbationEnds"),(('BOOL', None), "QuarantineCapable"),(('DWORD', None), "SentPotExpTime"),(('DWORD', None), "AckPotExpTime"),(('DWORD', None), "RecvPotExpTime"),(('DWORD', None), "StartTime"),(('DWORD', None), "CltLastTransTime"),(('DWORD', None), "LastBndUpdTime"),(('DWORD', None), "bndMsgStatus"),(('PWCHAR_T', None), "PolicyName"),(('BYTE', None), "flags"),]

    

class ('DHCP_IP_RESERVATION_INFO', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ReservedIpAddress"),(('DHCP_CLIENT_UID', None), "ReservedForClient"),(('PWCHAR_T', None), "ReservedClientName"),(('PWCHAR_T', None), "ReservedClientDesc"),(('BYTE', None), "bAllowedClientTypes"),(('BYTE', None), "fOptionsPresent"),]

    

class ('DHCP_RESERVATION_INFO_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_IP_RESERVATION_INFO', None), "Elements"),]

    

class ('DHCP_ALL_OPTION_VALUES_PB', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Flags"),(('DWORD', None), "NumElements"),(('POPTIONS', None), "*Options"),]

    

class ('DHCP_POL_COND', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "ParentExpr"),(('DHCP_POL_ATTR_TYPE', None), "Type"),(('DWORD', None), "OptionID"),(('DWORD', None), "SubOptionID"),(('PWCHAR_T', None), "VendorName"),(('DHCP_POL_COMPARATOR', None), "Operator"),(('LPBYTE', None), "Value"),(('DWORD', None), "ValueLength"),]

    

class ('DHCP_POL_COND_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_POL_COND', None), "Elements"),]

    

class ('DHCP_POL_EXPR', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "ParentExpr"),(('DHCP_POL_LOGIC_OPER', None), "Operator"),]

    

class ('DHCP_POL_EXPR_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_POL_EXPR', None), "Elements"),]

    

class ('DHCP_IP_RANGE_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_IP_RANGE', None), "Elements"),]

    

class ('DHCP_POLICY', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "PolicyName"),(('BOOL', None), "IsGlobalPolicy"),(('DHCP_IP_ADDRESS', None), "Subnet"),(('DWORD', None), "ProcessingOrder"),(('LPDHCP_POL_COND_ARRAY', None), "Conditions"),(('LPDHCP_POL_EXPR_ARRAY', None), "Expressions"),(('LPDHCP_IP_RANGE_ARRAY', None), "Ranges"),(('PWCHAR_T', None), "Description"),(('BOOL', None), "Enabled"),]

    

class ('DHCP_POLICY_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_POLICY', None), "Elements"),]

    

class ('DHCPV6_STATELESS_PARAMS', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "Status"),(('DWORD', None), "PurgeInterval"),]

    

class ('DHCPV6_STATELESS_SCOPE_STATS', None)(NdrStructure):
    MEMBERS = [(('DHCP_IPV6_ADDRESS', None), "SubnetAddress"),(('ULONGLONG', None), "NumStatelessClientsAdded"),(('ULONGLONG', None), "NumStatelessClientsRemoved"),]

    

class ('DHCPV6_STATELESS_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumScopes"),(('LPDHCPV6_STATELESS_SCOPE_STATS', None), "ScopeStats"),]

    

class ('DHCP_CLIENT_INFO_PB', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),(('QUARANTINESTATUS', None), "Status"),(('DATE_TIME', None), "ProbationEnds"),(('BOOL', None), "QuarantineCapable"),(('DWORD', None), "FilterStatus"),(('PWCHAR_T', None), "PolicyName"),]

    

class ('DHCP_CLIENT_INFO_PB_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_PB', None), "Clients"),]

    

class ('DHCP_PROPERTY', None)(NdrStructure):
    MEMBERS = [(('DHCP_PROPERTY_ID', None), "ID"),(('DHCP_PROPERTY_TYPE', None), "Type"),(('VALUE', None), "Value"),]

    

class ('DHCP_PROPERTY_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_PROPERTY', None), "Elements"),]

    

class ('DHCP_CLIENT_INFO_EX', None)(NdrStructure):
    MEMBERS = [(('DHCP_IP_ADDRESS', None), "ClientIpAddress"),(('DHCP_IP_MASK', None), "SubnetMask"),(('DHCP_CLIENT_UID', None), "ClientHardwareAddress"),(('PWCHAR_T', None), "ClientName"),(('PWCHAR_T', None), "ClientComment"),(('DATE_TIME', None), "ClientLeaseExpires"),(('DHCP_HOST_INFO', None), "OwnerHost"),(('BYTE', None), "bClientType"),(('BYTE', None), "AddressState"),(('QUARANTINESTATUS', None), "Status"),(('DATE_TIME', None), "ProbationEnds"),(('BOOL', None), "QuarantineCapable"),(('DWORD', None), "FilterStatus"),(('PWCHAR_T', None), "PolicyName"),(('LPDHCP_PROPERTY_ARRAY', None), "Properties"),]

    

class ('DHCP_CLIENT_INFO_EX_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('PLPDHCP_CLIENT_INFO_EX', None), "Clients"),]

    

class ('DHCP_POLICY_EX', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "PolicyName"),(('BOOL', None), "IsGlobalPolicy"),(('DHCP_IP_ADDRESS', None), "Subnet"),(('DWORD', None), "ProcessingOrder"),(('LPDHCP_POL_COND_ARRAY', None), "Conditions"),(('LPDHCP_POL_EXPR_ARRAY', None), "Expressions"),(('LPDHCP_IP_RANGE_ARRAY', None), "Ranges"),(('PWCHAR_T', None), "Description"),(('BOOL', None), "Enabled"),(('LPDHCP_PROPERTY_ARRAY', None), "Properties"),]

    

class ('DHCP_POLICY_EX_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "NumElements"),(('LPDHCP_POLICY_EX', None), "Elements"),]

    
Method("R_DhcpCreateSubnet",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_INFO),
),Method("R_DhcpSetSubnetInfo",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_INFO),
),Method("R_DhcpGetSubnetInfo",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
Out(PLPDHCP_SUBNET_INFO),
),Method("R_DhcpEnumSubnets",
In(DHCP_SRV_HANDLE),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_IP_ARRAY),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpAddSubnetElement",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_ELEMENT_DATA),
),Method("R_DhcpEnumSubnetElements",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(DHCP_SUBNET_ELEMENT_TYPE),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpRemoveSubnetElement",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_ELEMENT_DATA),
In(DHCP_FORCE_FLAG),
),Method("R_DhcpDeleteSubnet",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(DHCP_FORCE_FLAG),
),Method("R_DhcpCreateOption",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
In(LPDHCP_OPTION),
),Method("R_DhcpSetOptionInfo",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
In(LPDHCP_OPTION),
),Method("R_DhcpGetOptionInfo",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
Out(PLPDHCP_OPTION),
),Method("R_DhcpRemoveOption",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
),Method("R_DhcpSetOptionValue",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
In(LPDHCP_OPTION_SCOPE_INFO),
In(LPDHCP_OPTION_DATA),
),Method("R_DhcpGetOptionValue",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
In(LPDHCP_OPTION_SCOPE_INFO),
Out(PLPDHCP_OPTION_VALUE),
),Method("R_DhcpEnumOptionValues",
In(DHCP_SRV_HANDLE),
In(LPDHCP_OPTION_SCOPE_INFO),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_OPTION_VALUE_ARRAY),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpRemoveOptionValue",
In(DHCP_SRV_HANDLE),
In(DHCP_OPTION_ID),
In(LPDHCP_OPTION_SCOPE_INFO),
),Method("R_DhcpCreateClientInfo",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO),
),Method("R_DhcpSetClientInfo",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO),
),Method("R_DhcpGetClientInfo",
In(DHCP_SRV_HANDLE),
In(LPDHCP_SEARCH_INFO),
Out(PLPDHCP_CLIENT_INFO),
),Method("R_DhcpDeleteClientInfo",
In(DHCP_SRV_HANDLE),
In(LPDHCP_SEARCH_INFO),
),Method("R_DhcpEnumSubnetClients",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_CLIENT_INFO_ARRAY),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpGetClientOptions",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(DHCP_IP_MASK),
Out(PLPDHCP_OPTION_LIST),
),Method("R_DhcpGetMibInfo",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_MIB_INFO),
),Method("R_DhcpEnumOptions",
In(DHCP_SRV_HANDLE),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_OPTION_ARRAY),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpSetOptionValues",
In(DHCP_SRV_HANDLE),
In(LPDHCP_OPTION_SCOPE_INFO),
In(LPDHCP_OPTION_VALUE_ARRAY),
),Method("R_DhcpServerSetConfig",
In(DHCP_SRV_HANDLE),
In(DWORD),
In(LPDHCP_SERVER_CONFIG_INFO),
),Method("R_DhcpServerGetConfig",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_SERVER_CONFIG_INFO),
),Method("R_DhcpScanDatabase",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(DWORD),
Out(PLPDHCP_SCAN_LIST),
),Method("R_DhcpGetVersion",
In(DHCP_SRV_HANDLE),
Out(LPDWORD),
Out(LPDWORD),
),Method("R_DhcpAddSubnetElementV4",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_ELEMENT_DATA_V4),
),Method("R_DhcpEnumSubnetElementsV4",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(DHCP_SUBNET_ELEMENT_TYPE),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpRemoveSubnetElementV4",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_ELEMENT_DATA_V4),
In(DHCP_FORCE_FLAG),
),Method("R_DhcpCreateClientInfoV4",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO_V4),
),Method("R_DhcpSetClientInfoV4",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO_V4),
),Method("R_DhcpGetClientInfoV4",
In(DHCP_SRV_HANDLE),
In(LPDHCP_SEARCH_INFO),
Out(PLPDHCP_CLIENT_INFO_V4),
),Method("R_DhcpEnumSubnetClientsV4",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_CLIENT_INFO_ARRAY_V4),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpSetSuperScopeV4",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(PWCHAR),
In(BOOL),
),Method("R_DhcpGetSuperScopeInfoV4",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_SUPER_SCOPE_TABLE),
),Method("R_DhcpDeleteSuperScopeV4",
In(DHCP_SRV_HANDLE),
In(PWCHAR),
),Method("R_DhcpServerSetConfigV4",
In(DHCP_SRV_HANDLE),
In(DWORD),
In(LPDHCP_SERVER_CONFIG_INFO_V4),
),Method("R_DhcpServerGetConfigV4",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_SERVER_CONFIG_INFO_V4),
),Method("R_DhcpServerSetConfigVQ",
In(DHCP_SRV_HANDLE),
In(DWORD),
In(LPDHCP_SERVER_CONFIG_INFO_VQ),
),Method("R_DhcpServerGetConfigVQ",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_SERVER_CONFIG_INFO_VQ),
),Method("R_DhcpGetMibInfoVQ",
In(DHCP_SRV_HANDLE),
Out(PLPDHCP_MIB_INFO_VQ),
),Method("R_DhcpCreateClientInfoVQ",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO_VQ),
),Method("R_DhcpSetClientInfoVQ",
In(DHCP_SRV_HANDLE),
In(LPDHCP_CLIENT_INFO_VQ),
),Method("R_DhcpGetClientInfoVQ",
In(DHCP_SRV_HANDLE),
In(LPDHCP_SEARCH_INFO),
Out(PLPDHCP_CLIENT_INFO_VQ),
),Method("R_DhcpEnumSubnetClientsVQ",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
InOut(PDHCP_RESUME_HANDLE),
In(DWORD),
Out(PLPDHCP_CLIENT_INFO_ARRAY_VQ),
Out(PDWORD),
Out(PDWORD),
),Method("R_DhcpCreateSubnetVQ",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_INFO_VQ),
),Method("R_DhcpGetSubnetInfoVQ",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
Out(PLPDHCP_SUBNET_INFO_VQ),
),Method("R_DhcpSetSubnetInfoVQ",
In(DHCP_SRV_HANDLE),
In(DHCP_IP_ADDRESS),
In(LPDHCP_SUBNET_INFO_VQ),
),