from fuzzer.midl import *
from fuzzer.core import *


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


class DHCP_BINARY_DATA(NdrStructure):
    MEMBERS = [
        (DWORD, "DataLength"),
        (PBYTE, "Data"),
    ]


class DHCP_HOST_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "IpAddress"),
        (PWCHAR_T, "NetBiosName"),
        (PWCHAR_T, "HostName"),
    ]


class DHCP_SUBNET_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "SubnetAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (PWCHAR_T, "SubnetName"),
        (PWCHAR_T, "SubnetComment"),
        (DHCP_HOST_INFO, "PrimaryHost"),
        (DHCP_SUBNET_STATE, "SubnetState"),
    ]


class DHCP_IP_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_IP_ADDRESS, "Elements"),
    ]


class DHCP_IP_RANGE(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "StartAddress"),
        (DHCP_IP_ADDRESS, "EndAddress"),
    ]


class DHCP_IP_RESERVATION(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ReservedIpAddress"),
        (PDHCP_CLIENT_UID, "ReservedForClient"),
    ]


class DHCP_IP_CLUSTER(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClusterAddress"),
        (DWORD, "ClusterMask"),
    ]


class DHCP_BOOTP_IP_RANGE(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "StartAddress"),
        (DHCP_IP_ADDRESS, "EndAddress"),
        (ULONG, "BootpAllocated"),
        (ULONG, "MaxBootpAllowed"),
    ]


class DHCP_SUBNET_ELEMENT_DATA(NdrStructure):
    MEMBERS = [
        (DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),
        (ELEMENT, "Element"),
    ]


class DHCP_SUBNET_ELEMENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_SUBNET_ELEMENT_DATA, "Elements"),
    ]


class DWORD_DWORD(NdrStructure):
    MEMBERS = [
        (DWORD, "DWord1"),
        (DWORD, "DWord2"),
    ]


class DHCP_OPTION_DATA_ELEMENT(NdrStructure):
    MEMBERS = [
        (DHCP_OPTION_DATA_TYPE, "OptionType"),
        (ELEMENT, "Element"),
    ]


class DHCP_OPTION_DATA(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_OPTION_DATA_ELEMENT, "Elements"),
    ]


class DHCP_OPTION(NdrStructure):
    MEMBERS = [
        (DHCP_OPTION_ID, "OptionID"),
        (PWCHAR_T, "OptionName"),
        (PWCHAR_T, "OptionComment"),
        (DHCP_OPTION_DATA, "DefaultValue"),
        (DHCP_OPTION_TYPE, "OptionType"),
    ]


class DHCP_RESERVED_SCOPE(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ReservedIpAddress"),
        (DHCP_IP_ADDRESS, "ReservedIpSubnetAddress"),
    ]


class DHCP_OPTION_SCOPE_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_OPTION_SCOPE_TYPE, "ScopeType"),
        (SCOPEINFO, "ScopeInfo"),
    ]


class DHCP_OPTION_VALUE(NdrStructure):
    MEMBERS = [
        (DHCP_OPTION_ID, "OptionID"),
        (DHCP_OPTION_DATA, "Value"),
    ]


class DHCP_OPTION_VALUE_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_OPTION_VALUE, "Values"),
    ]


class DATE_TIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class DHCP_CLIENT_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
    ]


class DHCP_SEARCH_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_SEARCH_INFO_TYPE, "SearchType"),
        (SEARCHINFO, "SearchInfo"),
    ]


class DHCP_CLIENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO, "Clients"),
    ]


class DHCP_OPTION_LIST(NdrStructure):
    MEMBERS = [
        (DWORD, "NumOptions"),
        (PDHCP_OPTION_VALUE, "Options"),
    ]


class SCOPE_MIB_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "Subnet"),
        (DWORD, "NumAddressesInuse"),
        (DWORD, "NumAddressesFree"),
        (DWORD, "NumPendingOffers"),
    ]


class DHCP_MIB_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "Discovers"),
        (DWORD, "Offers"),
        (DWORD, "Requests"),
        (DWORD, "Acks"),
        (DWORD, "Naks"),
        (DWORD, "Declines"),
        (DWORD, "Releases"),
        (DATE_TIME, "ServerStartTime"),
        (DWORD, "Scopes"),
        (LPSCOPE_MIB_INFO, "ScopeInfo"),
    ]


class DHCP_OPTION_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_OPTION, "Options"),
    ]


class DHCP_SERVER_CONFIG_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "APIProtocolSupport"),
        (PWCHAR_T, "DatabaseName"),
        (PWCHAR_T, "DatabasePath"),
        (PWCHAR_T, "BackupPath"),
        (DWORD, "BackupInterval"),
        (DWORD, "DatabaseLoggingFlag"),
        (DWORD, "RestoreFlag"),
        (DWORD, "DatabaseCleanupInterval"),
        (DWORD, "DebugFlag"),
    ]


class DHCP_SCAN_ITEM(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "IpAddress"),
        (DHCP_SCAN_FLAG, "ScanFlag"),
    ]


class DHCP_SCAN_LIST(NdrStructure):
    MEMBERS = [
        (DWORD, "NumScanItems"),
        (PDHCP_SCAN_ITEM, "ScanItems"),
    ]


class DHCP_IP_RESERVATION_V4(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ReservedIpAddress"),
        (PDHCP_CLIENT_UID, "ReservedForClient"),
        (BYTE, "bAllowedClientTypes"),
    ]


class DHCP_SUBNET_ELEMENT_DATA_V4(NdrStructure):
    MEMBERS = [
        (DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),
        (ELEMENT, "Element"),
    ]


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_SUBNET_ELEMENT_DATA_V4, "Elements"),
    ]


class DHCP_CLIENT_INFO_V4(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
    ]


class DHCP_CLIENT_INFO_ARRAY_V4(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_V4, "Clients"),
    ]


class DHCP_SUPER_SCOPE_TABLE_ENTRY(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "SubnetAddress"),
        (DWORD, "SuperScopeNumber"),
        (DWORD, "NextInSuperScope"),
        (PWCHAR_T, "SuperScopeName"),
    ]


class DHCP_SUPER_SCOPE_TABLE(NdrStructure):
    MEMBERS = [
        (DWORD, "cEntries"),
        (PDHCP_SUPER_SCOPE_TABLE_ENTRY, "pEntries"),
    ]


class DHCP_SERVER_CONFIG_INFO_V4(NdrStructure):
    MEMBERS = [
        (DWORD, "APIProtocolSupport"),
        (PWCHAR_T, "DatabaseName"),
        (PWCHAR_T, "DatabasePath"),
        (PWCHAR_T, "BackupPath"),
        (DWORD, "BackupInterval"),
        (DWORD, "DatabaseLoggingFlag"),
        (DWORD, "RestoreFlag"),
        (DWORD, "DatabaseCleanupInterval"),
        (DWORD, "DebugFlag"),
        (DWORD, "dwPingRetries"),
        (DWORD, "cbBootTableString"),
        (PWCHAR, "wszBootTableString"),
        (BOOL, "fAuditLog"),
    ]


class DHCP_SERVER_CONFIG_INFO_VQ(NdrStructure):
    MEMBERS = [
        (DWORD, "APIProtocolSupport"),
        (PWCHAR_T, "DatabaseName"),
        (PWCHAR_T, "DatabasePath"),
        (PWCHAR_T, "BackupPath"),
        (DWORD, "BackupInterval"),
        (DWORD, "DatabaseLoggingFlag"),
        (DWORD, "RestoreFlag"),
        (DWORD, "DatabaseCleanupInterval"),
        (DWORD, "DebugFlag"),
        (DWORD, "dwPingRetries"),
        (DWORD, "cbBootTableString"),
        (PWCHAR, "wszBootTableString"),
        (BOOL, "fAuditLog"),
        (BOOL, "QuarantineOn"),
        (DWORD, "QuarDefFail"),
        (BOOL, "QuarRuntimeStatus"),
    ]


class SCOPE_MIB_INFO_VQ(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "Subnet"),
        (DWORD, "NumAddressesInuse"),
        (DWORD, "NumAddressesFree"),
        (DWORD, "NumPendingOffers"),
        (DWORD, "QtnNumLeases"),
        (DWORD, "QtnPctQtnLeases"),
        (DWORD, "QtnProbationLeases"),
        (DWORD, "QtnNonQtnLeases"),
        (DWORD, "QtnExemptLeases"),
        (DWORD, "QtnCapableClients"),
    ]


class DHCP_MIB_INFO_VQ(NdrStructure):
    MEMBERS = [
        (DWORD, "Discovers"),
        (DWORD, "Offers"),
        (DWORD, "Requests"),
        (DWORD, "Acks"),
        (DWORD, "Naks"),
        (DWORD, "Declines"),
        (DWORD, "Releases"),
        (DATE_TIME, "ServerStartTime"),
        (DWORD, "QtnNumLeases"),
        (DWORD, "QtnPctQtnLeases"),
        (DWORD, "QtnProbationLeases"),
        (DWORD, "QtnNonQtnLeases"),
        (DWORD, "QtnExemptLeases"),
        (DWORD, "QtnCapableClients"),
        (DWORD, "QtnIASErrors"),
        (DWORD, "Scopes"),
        (LPSCOPE_MIB_INFO_VQ, "ScopeInfo"),
    ]


class DHCP_CLIENT_INFO_VQ(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
        (QUARANTINESTATUS, "Status"),
        (DATE_TIME, "ProbationEnds"),
        (BOOL, "QuarantineCapable"),
    ]


class DHCP_CLIENT_INFO_ARRAY_VQ(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_VQ, "Clients"),
    ]


class DHCP_SUBNET_INFO_VQ(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "SubnetAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (PWCHAR_T, "SubnetName"),
        (PWCHAR_T, "SubnetComment"),
        (DHCP_HOST_INFO, "PrimaryHost"),
        (DHCP_SUBNET_STATE, "SubnetState"),
        (DWORD, "QuarantineOn"),
        (DWORD, "Reserved1"),
        (DWORD, "Reserved2"),
        (INT64, "Reserved3"),
        (INT64, "Reserved4"),
    ]


class DHCP_IPV6_ADDRESS(NdrStructure):
    MEMBERS = [
        (ULONGLONG, "HighOrderBits"),
        (ULONGLONG, "LowOrderBits"),
    ]


class DHCP_CLIENT_INFO_V5(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
    ]


class DHCP_CLIENT_INFO_ARRAY_V5(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_V5, "Clients"),
    ]


class DHCP_MSCOPE_INFO(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "MScopeName"),
        (PWCHAR_T, "MScopeComment"),
        (DWORD, "MScopeId"),
        (DWORD, "MScopeAddressPolicy"),
        (DHCP_HOST_INFO, "PrimaryHost"),
        (DHCP_SUBNET_STATE, "MScopeState"),
        (DWORD, "MScopeFlags"),
        (DATE_TIME, "ExpiryTime"),
        (PWCHAR_T, "LangTag"),
        (BYTE, "TTL"),
    ]


class DHCP_MSCOPE_TABLE(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PPWCHAR_T, "pMScopeNames"),
    ]


class DHCP_MCLIENT_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DWORD, "MScopeId"),
        (DHCP_CLIENT_UID, "ClientId"),
        (PWCHAR_T, "ClientName"),
        (DATE_TIME, "ClientLeaseStarts"),
        (DATE_TIME, "ClientLeaseEnds"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (DWORD, "AddressFlags"),
        (BYTE, "AddressState"),
    ]


class DHCP_MCLIENT_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_MCLIENT_INFO, "Clients"),
    ]


class DHCP_RESERVED_SCOPE6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "ReservedIpAddress"),
        (DHCP_IPV6_ADDRESS, "ReservedIpSubnetAddress"),
    ]


class DHCP_OPTION_SCOPE_INFO6(NdrStructure):
    MEMBERS = [
        (DHCP_OPTION_SCOPE_TYPE6, "ScopeType"),
        (SCOPEINFO, "ScopeInfo"),
    ]


class DHCP_CLASS_INFO(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "ClassName"),
        (PWCHAR_T, "ClassComment"),
        (DWORD, "ClassDataLength"),
        (BOOL, "IsVendor"),
        (DWORD, "Flags"),
        (LPBYTE, "ClassData"),
    ]


class DHCP_CLASS_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_CLASS_INFO, "Classes"),
    ]


class DHCP_ALL_OPTIONS(NdrStructure):
    MEMBERS = [
        (DWORD, "Flags"),
        (LPDHCP_OPTION_ARRAY, "NonVendorOptions"),
        (DWORD, "NumVendorOptions"),
        (PVENDOROPTIONS, "*VendorOptions"),
    ]


class DHCP_ALL_OPTION_VALUES(NdrStructure):
    MEMBERS = [
        (DWORD, "Flags"),
        (DWORD, "NumElements"),
        (POPTIONS, "*Options"),
    ]


class MSCOPE_MIB_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "MScopeId"),
        (PWCHAR_T, "MScopeName"),
        (DWORD, "NumAddressesInuse"),
        (DWORD, "NumAddressesFree"),
        (DWORD, "NumPendingOffers"),
    ]


class DHCP_MCAST_MIB_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "Discovers"),
        (DWORD, "Offers"),
        (DWORD, "Requests"),
        (DWORD, "Renews"),
        (DWORD, "Acks"),
        (DWORD, "Naks"),
        (DWORD, "Releases"),
        (DWORD, "Informs"),
        (DATE_TIME, "ServerStartTime"),
        (DWORD, "Scopes"),
        (LPMSCOPE_MIB_INFO, "ScopeInfo"),
    ]


class DHCP_ATTRIB(NdrStructure):
    MEMBERS = [
        (DHCP_ATTRIB_ID, "DhcpAttribId"),
        (ULONG, "DhcpAttribType"),
        (U0, "u0"),
    ]


class DHCP_ATTRIB_ARRAY(NdrStructure):
    MEMBERS = [
        (ULONG, "NumElements"),
        (LPDHCP_ATTRIB, "DhcpAttribs"),
    ]


class DHCP_SUBNET_ELEMENT_DATA_V5(NdrStructure):
    MEMBERS = [
        (DHCP_SUBNET_ELEMENT_TYPE, "ElementType"),
        (ELEMENT, "Element"),
    ]


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V5(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_SUBNET_ELEMENT_DATA_V5, "Elements"),
    ]


class DHCP_BIND_ELEMENT(NdrStructure):
    MEMBERS = [
        (ULONG, "Flags"),
        (BOOL, "fBoundToDHCPServer"),
        (DHCP_IP_ADDRESS, "AdapterPrimaryAddress"),
        (DHCP_IP_ADDRESS, "AdapterSubnetAddress"),
        (PWCHAR_T, "IfDescription"),
        (ULONG, "IfIdSize"),
        (LPBYTE, "IfId"),
    ]


class DHCP_BIND_ELEMENT_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_BIND_ELEMENT, "Elements"),
    ]


class DHCP_SERVER_SPECIFIC_STRINGS(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "DefaultVendorClassName"),
        (PWCHAR_T, "DefaultUserClassName"),
    ]


class SCOPE_MIB_INFO_V5(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "Subnet"),
        (DWORD, "NumAddressesInuse"),
        (DWORD, "NumAddressesFree"),
        (DWORD, "NumPendingOffers"),
    ]


class DHCP_MIB_INFO_V5(NdrStructure):
    MEMBERS = [
        (DWORD, "Discovers"),
        (DWORD, "Offers"),
        (DWORD, "Requests"),
        (DWORD, "Acks"),
        (DWORD, "Naks"),
        (DWORD, "Declines"),
        (DWORD, "Releases"),
        (DATE_TIME, "ServerStartTime"),
        (DWORD, "QtnNumLeases"),
        (DWORD, "QtnPctQtnLeases"),
        (DWORD, "QtnProbationLeases"),
        (DWORD, "QtnNonQtnLeases"),
        (DWORD, "QtnExemptLeases"),
        (DWORD, "QtnCapableClients"),
        (DWORD, "QtnIASErrors"),
        (DWORD, "DelayedOffers"),
        (DWORD, "ScopesWithDelayedOffers"),
        (DWORD, "Scopes"),
        (LPSCOPE_MIB_INFO_V5, "ScopeInfo"),
    ]


class DHCP_ADDR_PATTERN(NdrStructure):
    MEMBERS = [
        (BOOL, "MatchHWType"),
        (BYTE, "HWType"),
        (BOOL, "IsWildcard"),
        (BYTE, "Length"),
        (BYTE, "Pattern"),
    ]


class DHCP_FILTER_ADD_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_ADDR_PATTERN, "AddrPatt"),
        (PWCHAR_T, "Comment"),
        (DHCP_FILTER_LIST_TYPE, "ListType"),
    ]


class DHCP_FILTER_GLOBAL_INFO(NdrStructure):
    MEMBERS = [
        (BOOL, "EnforceAllowList"),
        (BOOL, "EnforceDenyList"),
    ]


class DHCP_FILTER_RECORD(NdrStructure):
    MEMBERS = [
        (DHCP_ADDR_PATTERN, "AddrPatt"),
        (PWCHAR_T, "Comment"),
    ]


class DHCP_FILTER_ENUM_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_FILTER_RECORD, "pEnumRecords"),
    ]


class DHCP_SUBNET_INFO_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "SubnetAddress"),
        (ULONG, "Prefix"),
        (USHORT, "Preference"),
        (PWCHAR_T, "SubnetName"),
        (PWCHAR_T, "SubnetComment"),
        (DWORD, "State"),
        (DWORD, "ScopeId"),
    ]


class DHCPV6_IP_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_IPV6_ADDRESS, "Elements"),
    ]


class DHCP_IP_RANGE_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "StartAddress"),
        (DHCP_IPV6_ADDRESS, "EndAddress"),
    ]


class DHCP_IP_RESERVATION_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "ReservedIpAddress"),
        (PDHCP_CLIENT_UID, "ReservedForClient"),
        (DWORD, "InterfaceId"),
    ]


class DHCP_SUBNET_ELEMENT_DATA_V6(NdrStructure):
    MEMBERS = [
        (DHCP_SUBNET_ELEMENT_TYPE_V6, "ElementType"),
        (ELEMENT, "Element"),
    ]


class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_SUBNET_ELEMENT_DATA_V6, "Elements"),
    ]


class DHCP_HOST_INFO_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "IpAddress"),
        (PWCHAR_T, "NetBiosName"),
        (PWCHAR_T, "HostName"),
    ]


class DHCP_CLIENT_INFO_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "ClientIpAddress"),
        (DHCP_CLIENT_UID, "ClientDUID"),
        (DWORD, "AddressType"),
        (DWORD, "IAID"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientValidLeaseExpires"),
        (DATE_TIME, "ClientPrefLeaseExpires"),
        (DHCP_HOST_INFO_V6, "OwnerHost"),
    ]


class DHCP_CLIENT_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_V6, "Clients"),
    ]


class DHCP_SERVER_CONFIG_INFO_V6(NdrStructure):
    MEMBERS = [
        (BOOL, "UnicastFlag"),
        (BOOL, "RapidCommitFlag"),
        (DWORD, "PreferredLifetime"),
        (DWORD, "ValidLifetime"),
        (DWORD, "T1"),
        (DWORD, "T2"),
        (DWORD, "PreferredLifetimeIATA"),
        (DWORD, "ValidLifetimeIATA"),
        (BOOL, "fAuditLog"),
    ]


class SCOPE_MIB_INFO_V6(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "Subnet"),
        (ULONGLONG, "NumAddressesInuse"),
        (ULONGLONG, "NumAddressesFree"),
        (ULONGLONG, "NumPendingAdvertises"),
    ]


class DHCP_MIB_INFO_V6(NdrStructure):
    MEMBERS = [
        (DWORD, "Solicits"),
        (DWORD, "Advertises"),
        (DWORD, "Requests"),
        (DWORD, "Renews"),
        (DWORD, "Rebinds"),
        (DWORD, "Replies"),
        (DWORD, "Confirms"),
        (DWORD, "Declines"),
        (DWORD, "Releases"),
        (DWORD, "Informs"),
        (DATE_TIME, "ServerStartTime"),
        (DWORD, "Scopes"),
        (LPSCOPE_MIB_INFO_V6, "ScopeInfo"),
    ]


class DHCPV6_BIND_ELEMENT(NdrStructure):
    MEMBERS = [
        (ULONG, "Flags"),
        (BOOL, "fBoundToDHCPServer"),
        (DHCP_IPV6_ADDRESS, "AdapterPrimaryAddress"),
        (DHCP_IPV6_ADDRESS, "AdapterSubnetAddress"),
        (PWCHAR_T, "IfDescription"),
        (DWORD, "IpV6IfIndex"),
        (ULONG, "IfIdSize"),
        (LPBYTE, "IfId"),
    ]


class DHCPV6_BIND_ELEMENT_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCPV6_BIND_ELEMENT, "Elements"),
    ]


class DHCP_SEARCH_INFO_V6(NdrStructure):
    MEMBERS = [
        (DHCP_SEARCH_INFO_TYPE_V6, "SearchType"),
        (SEARCHINFO, "SearchInfo"),
    ]


class DHCP_CLASS_INFO_V6(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "ClassName"),
        (PWCHAR_T, "ClassComment"),
        (DWORD, "ClassDataLength"),
        (BOOL, "IsVendor"),
        (DWORD, "EnterpriseNumber"),
        (DWORD, "Flags"),
        (LPBYTE, "ClassData"),
    ]


class DHCP_CLASS_INFO_ARRAY_V6(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_CLASS_INFO_V6, "Classes"),
    ]


class DHCP_CLIENT_FILTER_STATUS_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
        (QUARANTINESTATUS, "Status"),
        (DATE_TIME, "ProbationEnds"),
        (BOOL, "QuarantineCapable"),
        (DWORD, "FilterStatus"),
    ]


class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_FILTER_STATUS_INFO, "Clients"),
    ]


class DHCP_FAILOVER_RELATIONSHIP(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "primaryServer"),
        (DHCP_IP_ADDRESS, "secondaryServer"),
        (DHCP_FAILOVER_MODE, "mode"),
        (DHCP_FAILOVER_SERVER, "serverType"),
        (FSM_STATE, "state"),
        (FSM_STATE, "prevState"),
        (DWORD, "mclt"),
        (DWORD, "safePeriod"),
        (PWCHAR_T, "relationshipName"),
        (PWCHAR_T, "primaryServerName"),
        (PWCHAR_T, "secondaryServerName"),
        (LPDHCP_IP_ARRAY, "pScopes"),
        (BYTE, "percentage"),
        (PWCHAR_T, "pSharedSecret"),
    ]


class DHCP_FAILOVER_RELATIONSHIP_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "numElements"),
        (LPDHCP_FAILOVER_RELATIONSHIP, "pRelationships"),
    ]


class DHCP_FAILOVER_STATISTICS(NdrStructure):
    MEMBERS = [
        (DWORD, "numAddr"),
        (DWORD, "addrFree"),
        (DWORD, "addrInUse"),
        (DWORD, "partnerAddrFree"),
        (DWORD, "thisAddrFree"),
        (DWORD, "partnerAddrInUse"),
        (DWORD, "thisAddrInUse"),
    ]


class DHCPV4_FAILOVER_CLIENT_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
        (QUARANTINESTATUS, "Status"),
        (DATE_TIME, "ProbationEnds"),
        (BOOL, "QuarantineCapable"),
        (DWORD, "SentPotExpTime"),
        (DWORD, "AckPotExpTime"),
        (DWORD, "RecvPotExpTime"),
        (DWORD, "StartTime"),
        (DWORD, "CltLastTransTime"),
        (DWORD, "LastBndUpdTime"),
        (DWORD, "bndMsgStatus"),
        (PWCHAR_T, "PolicyName"),
        (BYTE, "flags"),
    ]


class DHCP_IP_RESERVATION_INFO(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ReservedIpAddress"),
        (DHCP_CLIENT_UID, "ReservedForClient"),
        (PWCHAR_T, "ReservedClientName"),
        (PWCHAR_T, "ReservedClientDesc"),
        (BYTE, "bAllowedClientTypes"),
        (BYTE, "fOptionsPresent"),
    ]


class DHCP_RESERVATION_INFO_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_IP_RESERVATION_INFO, "Elements"),
    ]


class DHCP_ALL_OPTION_VALUES_PB(NdrStructure):
    MEMBERS = [
        (DWORD, "Flags"),
        (DWORD, "NumElements"),
        (POPTIONS, "*Options"),
    ]


class DHCP_POL_COND(NdrStructure):
    MEMBERS = [
        (DWORD, "ParentExpr"),
        (DHCP_POL_ATTR_TYPE, "Type"),
        (DWORD, "OptionID"),
        (DWORD, "SubOptionID"),
        (PWCHAR_T, "VendorName"),
        (DHCP_POL_COMPARATOR, "Operator"),
        (LPBYTE, "Value"),
        (DWORD, "ValueLength"),
    ]


class DHCP_POL_COND_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_POL_COND, "Elements"),
    ]


class DHCP_POL_EXPR(NdrStructure):
    MEMBERS = [
        (DWORD, "ParentExpr"),
        (DHCP_POL_LOGIC_OPER, "Operator"),
    ]


class DHCP_POL_EXPR_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_POL_EXPR, "Elements"),
    ]


class DHCP_IP_RANGE_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_IP_RANGE, "Elements"),
    ]


class DHCP_POLICY(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "PolicyName"),
        (BOOL, "IsGlobalPolicy"),
        (DHCP_IP_ADDRESS, "Subnet"),
        (DWORD, "ProcessingOrder"),
        (LPDHCP_POL_COND_ARRAY, "Conditions"),
        (LPDHCP_POL_EXPR_ARRAY, "Expressions"),
        (LPDHCP_IP_RANGE_ARRAY, "Ranges"),
        (PWCHAR_T, "Description"),
        (BOOL, "Enabled"),
    ]


class DHCP_POLICY_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_POLICY, "Elements"),
    ]


class DHCPV6_STATELESS_PARAMS(NdrStructure):
    MEMBERS = [
        (BOOL, "Status"),
        (DWORD, "PurgeInterval"),
    ]


class DHCPV6_STATELESS_SCOPE_STATS(NdrStructure):
    MEMBERS = [
        (DHCP_IPV6_ADDRESS, "SubnetAddress"),
        (ULONGLONG, "NumStatelessClientsAdded"),
        (ULONGLONG, "NumStatelessClientsRemoved"),
    ]


class DHCPV6_STATELESS_STATS(NdrStructure):
    MEMBERS = [
        (DWORD, "NumScopes"),
        (LPDHCPV6_STATELESS_SCOPE_STATS, "ScopeStats"),
    ]


class DHCP_CLIENT_INFO_PB(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
        (QUARANTINESTATUS, "Status"),
        (DATE_TIME, "ProbationEnds"),
        (BOOL, "QuarantineCapable"),
        (DWORD, "FilterStatus"),
        (PWCHAR_T, "PolicyName"),
    ]


class DHCP_CLIENT_INFO_PB_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_PB, "Clients"),
    ]


class DHCP_PROPERTY(NdrStructure):
    MEMBERS = [
        (DHCP_PROPERTY_ID, "ID"),
        (DHCP_PROPERTY_TYPE, "Type"),
        (VALUE, "Value"),
    ]


class DHCP_PROPERTY_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_PROPERTY, "Elements"),
    ]


class DHCP_CLIENT_INFO_EX(NdrStructure):
    MEMBERS = [
        (DHCP_IP_ADDRESS, "ClientIpAddress"),
        (DHCP_IP_MASK, "SubnetMask"),
        (DHCP_CLIENT_UID, "ClientHardwareAddress"),
        (PWCHAR_T, "ClientName"),
        (PWCHAR_T, "ClientComment"),
        (DATE_TIME, "ClientLeaseExpires"),
        (DHCP_HOST_INFO, "OwnerHost"),
        (BYTE, "bClientType"),
        (BYTE, "AddressState"),
        (QUARANTINESTATUS, "Status"),
        (DATE_TIME, "ProbationEnds"),
        (BOOL, "QuarantineCapable"),
        (DWORD, "FilterStatus"),
        (PWCHAR_T, "PolicyName"),
        (LPDHCP_PROPERTY_ARRAY, "Properties"),
    ]


class DHCP_CLIENT_INFO_EX_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (PLPDHCP_CLIENT_INFO_EX, "Clients"),
    ]


class DHCP_POLICY_EX(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "PolicyName"),
        (BOOL, "IsGlobalPolicy"),
        (DHCP_IP_ADDRESS, "Subnet"),
        (DWORD, "ProcessingOrder"),
        (LPDHCP_POL_COND_ARRAY, "Conditions"),
        (LPDHCP_POL_EXPR_ARRAY, "Expressions"),
        (LPDHCP_IP_RANGE_ARRAY, "Ranges"),
        (PWCHAR_T, "Description"),
        (BOOL, "Enabled"),
        (LPDHCP_PROPERTY_ARRAY, "Properties"),
    ]


class DHCP_POLICY_EX_ARRAY(NdrStructure):
    MEMBERS = [
        (DWORD, "NumElements"),
        (LPDHCP_POLICY_EX, "Elements"),
    ]


Method(
    "R_DhcpCreateSubnet",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_INFO),
), Method(
    "R_DhcpSetSubnetInfo",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_INFO),
), Method(
    "R_DhcpGetSubnetInfo",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    Out(PLPDHCP_SUBNET_INFO),
), Method(
    "R_DhcpEnumSubnets",
    In(DHCP_SRV_HANDLE),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_IP_ARRAY),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpAddSubnetElement",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_ELEMENT_DATA),
), Method(
    "R_DhcpEnumSubnetElements",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(DHCP_SUBNET_ELEMENT_TYPE),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpRemoveSubnetElement",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_ELEMENT_DATA),
    In(DHCP_FORCE_FLAG),
), Method(
    "R_DhcpDeleteSubnet",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(DHCP_FORCE_FLAG),
), Method(
    "R_DhcpCreateOption",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    In(LPDHCP_OPTION),
), Method(
    "R_DhcpSetOptionInfo",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    In(LPDHCP_OPTION),
), Method(
    "R_DhcpGetOptionInfo",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    Out(PLPDHCP_OPTION),
), Method(
    "R_DhcpRemoveOption",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
), Method(
    "R_DhcpSetOptionValue",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    In(LPDHCP_OPTION_SCOPE_INFO),
    In(LPDHCP_OPTION_DATA),
), Method(
    "R_DhcpGetOptionValue",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    In(LPDHCP_OPTION_SCOPE_INFO),
    Out(PLPDHCP_OPTION_VALUE),
), Method(
    "R_DhcpEnumOptionValues",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_OPTION_SCOPE_INFO),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_OPTION_VALUE_ARRAY),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpRemoveOptionValue",
    In(DHCP_SRV_HANDLE),
    In(DHCP_OPTION_ID),
    In(LPDHCP_OPTION_SCOPE_INFO),
), Method(
    "R_DhcpCreateClientInfo",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO),
), Method(
    "R_DhcpSetClientInfo",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO),
), Method(
    "R_DhcpGetClientInfo",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_SEARCH_INFO),
    Out(PLPDHCP_CLIENT_INFO),
), Method(
    "R_DhcpDeleteClientInfo",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_SEARCH_INFO),
), Method(
    "R_DhcpEnumSubnetClients",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_CLIENT_INFO_ARRAY),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpGetClientOptions",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(DHCP_IP_MASK),
    Out(PLPDHCP_OPTION_LIST),
), Method(
    "R_DhcpGetMibInfo",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_MIB_INFO),
), Method(
    "R_DhcpEnumOptions",
    In(DHCP_SRV_HANDLE),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_OPTION_ARRAY),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpSetOptionValues",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_OPTION_SCOPE_INFO),
    In(LPDHCP_OPTION_VALUE_ARRAY),
), Method(
    "R_DhcpServerSetConfig",
    In(DHCP_SRV_HANDLE),
    In(DWORD),
    In(LPDHCP_SERVER_CONFIG_INFO),
), Method(
    "R_DhcpServerGetConfig",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_SERVER_CONFIG_INFO),
), Method(
    "R_DhcpScanDatabase",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(DWORD),
    Out(PLPDHCP_SCAN_LIST),
), Method(
    "R_DhcpGetVersion",
    In(DHCP_SRV_HANDLE),
    Out(LPDWORD),
    Out(LPDWORD),
), Method(
    "R_DhcpAddSubnetElementV4",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_ELEMENT_DATA_V4),
), Method(
    "R_DhcpEnumSubnetElementsV4",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(DHCP_SUBNET_ELEMENT_TYPE),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpRemoveSubnetElementV4",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_ELEMENT_DATA_V4),
    In(DHCP_FORCE_FLAG),
), Method(
    "R_DhcpCreateClientInfoV4",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO_V4),
), Method(
    "R_DhcpSetClientInfoV4",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO_V4),
), Method(
    "R_DhcpGetClientInfoV4",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_SEARCH_INFO),
    Out(PLPDHCP_CLIENT_INFO_V4),
), Method(
    "R_DhcpEnumSubnetClientsV4",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_CLIENT_INFO_ARRAY_V4),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpSetSuperScopeV4",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(PWCHAR),
    In(BOOL),
), Method(
    "R_DhcpGetSuperScopeInfoV4",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_SUPER_SCOPE_TABLE),
), Method(
    "R_DhcpDeleteSuperScopeV4",
    In(DHCP_SRV_HANDLE),
    In(PWCHAR),
), Method(
    "R_DhcpServerSetConfigV4",
    In(DHCP_SRV_HANDLE),
    In(DWORD),
    In(LPDHCP_SERVER_CONFIG_INFO_V4),
), Method(
    "R_DhcpServerGetConfigV4",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_SERVER_CONFIG_INFO_V4),
), Method(
    "R_DhcpServerSetConfigVQ",
    In(DHCP_SRV_HANDLE),
    In(DWORD),
    In(LPDHCP_SERVER_CONFIG_INFO_VQ),
), Method(
    "R_DhcpServerGetConfigVQ",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_SERVER_CONFIG_INFO_VQ),
), Method(
    "R_DhcpGetMibInfoVQ",
    In(DHCP_SRV_HANDLE),
    Out(PLPDHCP_MIB_INFO_VQ),
), Method(
    "R_DhcpCreateClientInfoVQ",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO_VQ),
), Method(
    "R_DhcpSetClientInfoVQ",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_CLIENT_INFO_VQ),
), Method(
    "R_DhcpGetClientInfoVQ",
    In(DHCP_SRV_HANDLE),
    In(LPDHCP_SEARCH_INFO),
    Out(PLPDHCP_CLIENT_INFO_VQ),
), Method(
    "R_DhcpEnumSubnetClientsVQ",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    InOut(PDHCP_RESUME_HANDLE),
    In(DWORD),
    Out(PLPDHCP_CLIENT_INFO_ARRAY_VQ),
    Out(PDWORD),
    Out(PDWORD),
), Method(
    "R_DhcpCreateSubnetVQ",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_INFO_VQ),
), Method(
    "R_DhcpGetSubnetInfoVQ",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    Out(PLPDHCP_SUBNET_INFO_VQ),
), Method(
    "R_DhcpSetSubnetInfoVQ",
    In(DHCP_SRV_HANDLE),
    In(DHCP_IP_ADDRESS),
    In(LPDHCP_SUBNET_INFO_VQ),
),
