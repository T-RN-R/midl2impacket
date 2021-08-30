
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

    

class ('FW_IPV4_SUBNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAddress"),(('DWORD', None), "dwSubNetMask"),]

    

class ('FW_IPV4_SUBNET_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_IPV4_SUBNET', None), "pSubNets"),]

    

class ('FW_IPV6_SUBNET', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "Address"),(('DWORD', None), "dwNumPrefixBits"),]

    

class ('FW_IPV6_SUBNET_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_IPV6_SUBNET', None), "pSubNets"),]

    

class ('FW_IPV4_ADDRESS_RANGE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwBegin"),(('DWORD', None), "dwEnd"),]

    

class ('FW_IPV6_ADDRESS_RANGE', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "Begin"),(('BYTE', None), "End"),]

    

class ('FW_IPV4_RANGE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_IPV4_ADDRESS_RANGE', None), "pRanges"),]

    

class ('FW_IPV6_RANGE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_IPV6_ADDRESS_RANGE', None), "pRanges"),]

    

class ('FW_PORT_RANGE', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wBegin"),(('WORD', None), "wEnd"),]

    

class ('FW_PORT_RANGE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_PORT_RANGE', None), "pPorts"),]

    

class ('FW_PORTS', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wPortKeywords"),(('FW_PORT_RANGE_LIST', None), "Ports"),]

    

class ('FW_ICMP_TYPE_CODE', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "bType"),(('WORD', None), "wCode"),]

    

class ('FW_ICMP_TYPE_CODE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_ICMP_TYPE_CODE', None), "pEntries"),]

    

class ('FW_INTERFACE_LUIDS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumLUIDs"),(('PGUID', None), "pLUIDs"),]

    

class ('FW_ADDRESSES', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwV4AddressKeywords"),(('DWORD', None), "dwV6AddressKeywords"),(('FW_IPV4_SUBNET_LIST', None), "V4SubNets"),(('FW_IPV4_RANGE_LIST', None), "V4Ranges"),(('FW_IPV6_SUBNET_LIST', None), "V6SubNets"),(('FW_IPV6_RANGE_LIST', None), "V6Ranges"),]

    

class ('FW_OBJECT_METADATA', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "qwFilterContextID"),(('DWORD', None), "dwNumEntries"),(('PFW_ENFORCEMENT_STATE', None), "pEnforcementStates"),]

    

class ('FW_OS_PLATFORM', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "bPlatform"),(('BYTE', None), "bMajorVersion"),(('BYTE', None), "bMinorVersion"),(('BYTE', None), "Reserved"),]

    

class ('FW_OS_PLATFORM_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_OS_PLATFORM', None), "pPlatforms"),]

    

class ('FW_NETWORK_NAMES', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PLPWSTR', None), "wszNames"),]

    

class ('FW_RULE2_0', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('PWCHAR', None), "wszRuleId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('PWCHAR', None), "wszLocalApplication"),(('PWCHAR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('PWCHAR', None), "wszRemoteMachineAuthorizationList"),(('PWCHAR', None), "wszRemoteUserAuthorizationList"),(('PWCHAR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('DWORD', None), "Reserved"),]

    

class ('FW_RULE2_10', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),]

    

class ('FW_RULE2_20', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('DWORD', None), "dwTrustTupleKeywords"),]

    

class ('FW_RULE2_24', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('DWORD', None), "dwTrustTupleKeywords"),(('FW_NETWORK_NAMES', None), "OnNetworkNames"),(('PWCHAR', None), "wszSecurityRealmId"),]

    

class ('FW_RULE2_25', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('DWORD', None), "dwTrustTupleKeywords"),(('FW_NETWORK_NAMES', None), "OnNetworkNames"),(('PWCHAR', None), "wszSecurityRealmId"),(('WORD', None), "wFlags2"),]

    

class ('FW_RULE2_26', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('DWORD', None), "dwTrustTupleKeywords"),(('FW_NETWORK_NAMES', None), "OnNetworkNames"),(('PWCHAR', None), "wszSecurityRealmId"),(('WORD', None), "wFlags2"),(('FW_NETWORK_NAMES', None), "RemoteOutServerNames"),]

    

class ('FW_RULE2_27', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('UNSIGNED_SHORT', None), "wSchemaVersion"),(('PWCHAR_T', None), "wszRuleId"),(('PWCHAR_T', None), "wszName"),(('PWCHAR_T', None), "wszDescription"),(('UNSIGNED_LONG', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('UNSIGNED_SHORT', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('UNSIGNED_LONG', None), "dwLocalInterfaceTypes"),(('PWCHAR_T', None), "wszLocalApplication"),(('PWCHAR_T', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('UNSIGNED_SHORT', None), "wFlags"),(('PWCHAR_T', None), "wszRemoteMachineAuthorizationList"),(('PWCHAR_T', None), "wszRemoteUserAuthorizationList"),(('PWCHAR_T', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR_T', None), "wszGPOName"),(('UNSIGNED_LONG', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('UNSIGNED_LONG', None), "dwTrustTupleKeywords"),(('FW_NETWORK_NAMES', None), "OnNetworkNames"),(('PWCHAR', None), "wszSecurityRealmId"),(('UNSIGNED_SHORT', None), "wFlags2"),(('FW_NETWORK_NAMES', None), "RemoteOutServerNames"),(('PWCHAR', None), "wszFqbn"),(('UNSIGNED_LONG', None), "compartmentId"),]

    

class ('FW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumIds"),(('PUINT32', None), "ids"),]

    

class ('FW_RULE', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('LPWSTR', None), "wszRuleId"),(('LPWSTR', None), "wszName"),(('LPWSTR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_DIRECTION', None), "Direction"),(('WORD', None), "wIpProtocol"),(('U0', None), "u0"),(('FW_ADDRESSES', None), "LocalAddresses"),(('FW_ADDRESSES', None), "RemoteAddresses"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('LPWSTR', None), "wszLocalApplication"),(('LPWSTR', None), "wszLocalService"),(('FW_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('LPWSTR', None), "wszRemoteMachineAuthorizationList"),(('LPWSTR', None), "wszRemoteUserAuthorizationList"),(('LPWSTR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_STATUS', None), "Status"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('LPWSTR', None), "wszGPOName"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszLocalUserAuthorizationList"),(('PWCHAR', None), "wszPackageId"),(('PWCHAR', None), "wszLocalUserOwner"),(('DWORD', None), "dwTrustTupleKeywords"),(('FW_NETWORK_NAMES', None), "OnNetworkNames"),(('PWCHAR', None), "wszSecurityRealmId"),(('WORD', None), "wFlags2"),(('FW_NETWORK_NAMES', None), "RemoteOutServerNames"),(('PWCHAR', None), "wszFqbn"),(('DWORD', None), "compartmentId"),(('GUID', None), "providerContextKey"),(('FW_DYNAMIC_KEYWORD_ADDRESS_ID_LIST', None), "RemoteDynamicKeywordAddresses"),]

    

class ('FW_NETWORK', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "pszName"),(('FW_PROFILE_TYPE', None), "ProfileType"),]

    

class ('FW_ADAPTER', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "pszFriendlyName"),(('GUID', None), "Guid"),]

    

class ('FW_DIAG_APP', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "pszAppPath"),]

    

class ('FW_PRODUCT', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwFlags"),(('DWORD', None), "dwNumRuleCategories"),(('PFW_RULE_CATEGORY', None), "pRuleCategories"),(('PWCHAR_T', None), "pszDisplayName"),(('PWCHAR_T', None), "pszPathToSignedProductExe"),]

    

class ('FW_CS_RULE2_0', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('PWCHAR', None), "wszRuleId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_ADDRESSES', None), "Endpoint1"),(('FW_ADDRESSES', None), "Endpoint2"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('DWORD', None), "dwLocalTunnelEndpointV4"),(('BYTE', None), "LocalTunnelEndpointV6"),(('DWORD', None), "dwRemoteTunnelEndpointV4"),(('BYTE', None), "RemoteTunnelEndpointV6"),(('FW_PORTS', None), "Endpoint1Ports"),(('FW_PORTS', None), "Endpoint2Ports"),(('WORD', None), "wIpProtocol"),(('PWCHAR', None), "wszPhase1AuthSet"),(('PWCHAR', None), "wszPhase2CryptoSet"),(('PWCHAR', None), "wszPhase2AuthSet"),(('FW_CS_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('PWCHAR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),]

    

class ('FW_CS_RULE2_10', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('PWCHAR', None), "wszRuleId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_ADDRESSES', None), "Endpoint1"),(('FW_ADDRESSES', None), "Endpoint2"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('DWORD', None), "dwLocalTunnelEndpointV4"),(('BYTE', None), "LocalTunnelEndpointV6"),(('DWORD', None), "dwRemoteTunnelEndpointV4"),(('BYTE', None), "RemoteTunnelEndpointV6"),(('FW_PORTS', None), "Endpoint1Ports"),(('FW_PORTS', None), "Endpoint2Ports"),(('WORD', None), "wIpProtocol"),(('PWCHAR', None), "wszPhase1AuthSet"),(('PWCHAR', None), "wszPhase2CryptoSet"),(('PWCHAR', None), "wszPhase2AuthSet"),(('FW_CS_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('PWCHAR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('PWCHAR', None), "wszMMParentRuleId"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),]

    

class ('FW_CS_RULE', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('PWCHAR', None), "wszRuleId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_ADDRESSES', None), "Endpoint1"),(('FW_ADDRESSES', None), "Endpoint2"),(('FW_INTERFACE_LUIDS', None), "LocalInterfaceIds"),(('DWORD', None), "dwLocalInterfaceTypes"),(('DWORD', None), "dwLocalTunnelEndpointV4"),(('BYTE', None), "LocalTunnelEndpointV6"),(('DWORD', None), "dwRemoteTunnelEndpointV4"),(('BYTE', None), "RemoteTunnelEndpointV6"),(('FW_PORTS', None), "Endpoint1Ports"),(('FW_PORTS', None), "Endpoint2Ports"),(('WORD', None), "wIpProtocol"),(('PWCHAR', None), "wszPhase1AuthSet"),(('PWCHAR', None), "wszPhase2CryptoSet"),(('PWCHAR', None), "wszPhase2AuthSet"),(('FW_CS_RULE_ACTION', None), "Action"),(('WORD', None), "wFlags"),(('PWCHAR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('PWCHAR', None), "wszMMParentRuleId"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),(('PWCHAR', None), "wszRemoteTunnelEndpointFqdn"),(('FW_ADDRESSES', None), "RemoteTunnelEndpoints"),(('DWORD', None), "dwKeyModules"),(('DWORD', None), "FwdPathSALifetime"),(('LPWSTR', None), "wszTransportMachineAuthzSDDL"),(('LPWSTR', None), "wszTransportUserAuthzSDDL"),]

    

class ('FW_AUTH_SUITE2_10', None)(NdrStructure):
    MEMBERS = [(('FW_AUTH_METHOD', None), "Method"),(('WORD', None), "wFlags"),(('U0', None), "u0"),]

    

class ('FW_CERT_CRITERIA', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wSchemaVersion"),(('WORD', None), "wFlags"),(('FW_CERT_CRITERIA_TYPE', None), "CertCriteriaType"),(('FW_CERT_CRITERIA_NAME_TYPE', None), "NameType"),(('LPWSTR', None), "wszName"),(('DWORD', None), "dwNumEku"),(('PLPSTR', None), "ppEku"),(('LPWSTR', None), "wszHash"),]

    

class ('FW_AUTH_SUITE', None)(NdrStructure):
    MEMBERS = [(('FW_AUTH_METHOD', None), "Method"),(('WORD', None), "wFlags"),(('U0', None), "u0"),]

    

class ('FW_AUTH_SET2_10', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('FW_IPSEC_PHASE', None), "IpSecPhase"),(('PWCHAR', None), "wszSetId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('PWCHAR', None), "wszEmbeddedContext"),(('DWORD', None), "dwNumSuites"),(('PFW_AUTH_SUITE2_10', None), "pSuites"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('DWORD', None), "dwAuthSetFlags"),]

    

class ('FW_AUTH_SET', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('FW_IPSEC_PHASE', None), "IpSecPhase"),(('PWCHAR', None), "wszSetId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('PWCHAR', None), "wszEmbeddedContext"),(('DWORD', None), "dwNumSuites"),(('PFW_AUTH_SUITE', None), "pSuites"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('DWORD', None), "dwAuthSetFlags"),]

    

class ('FW_PHASE1_CRYPTO_SUITE', None)(NdrStructure):
    MEMBERS = [(('FW_CRYPTO_KEY_EXCHANGE_TYPE', None), "KeyExchange"),(('FW_CRYPTO_ENCRYPTION_TYPE', None), "Encryption"),(('FW_CRYPTO_HASH_TYPE', None), "Hash"),(('DWORD', None), "dwP1CryptoSuiteFlags"),]

    

class ('FW_PHASE2_CRYPTO_SUITE', None)(NdrStructure):
    MEMBERS = [(('FW_CRYPTO_PROTOCOL_TYPE', None), "Protocol"),(('FW_CRYPTO_HASH_TYPE', None), "AhHash"),(('FW_CRYPTO_HASH_TYPE', None), "EspHash"),(('FW_CRYPTO_ENCRYPTION_TYPE', None), "Encryption"),(('DWORD', None), "dwTimeoutMinutes"),(('DWORD', None), "dwTimeoutKBytes"),(('DWORD', None), "dwP2CryptoSuiteFlags"),]

    

class ('FW_CRYPTO_SET', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('FW_IPSEC_PHASE', None), "IpSecPhase"),(('PWCHAR', None), "wszSetId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('PWCHAR', None), "wszEmbeddedContext"),(('U0', None), "u0"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('DWORD', None), "dwCryptoSetFlags"),]

    

class ('FW_BYTE_BLOB', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('PBYTE', None), "Blob"),]

    

class ('FW_COOKIE_PAIR', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "Initiator"),(('UINT64', None), "Responder"),]

    

class ('FW_CERT_INFO', None)(NdrStructure):
    MEMBERS = [(('FW_BYTE_BLOB', None), "SubjectName"),(('DWORD', None), "dwCertFlags"),]

    

class ('FW_AUTH_INFO', None)(NdrStructure):
    MEMBERS = [(('FW_AUTH_METHOD', None), "AuthMethod"),(('U0', None), "u0"),(('DWORD', None), "dwAuthInfoFlags"),]

    

class ('FW_ENDPOINTS', None)(NdrStructure):
    MEMBERS = [(('FW_IP_VERSION', None), "IpVersion"),(('DWORD', None), "dwSourceV4Address"),(('DWORD', None), "dwDestinationV4Address"),(('BYTE', None), "SourceV6Address"),(('BYTE', None), "DestinationV6Address"),]

    

class ('FW_PHASE1_SA_DETAILS', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "SaId"),(('FW_PHASE1_KEY_MODULE_TYPE', None), "KeyModuleType"),(('FW_ENDPOINTS', None), "Endpoints"),(('FW_PHASE1_CRYPTO_SUITE', None), "SelectedProposal"),(('DWORD', None), "dwProposalLifetimeKBytes"),(('DWORD', None), "dwProposalLifetimeMinutes"),(('DWORD', None), "dwProposalMaxNumPhase2"),(('FW_COOKIE_PAIR', None), "CookiePair"),(('PFW_AUTH_INFO', None), "pFirstAuth"),(('PFW_AUTH_INFO', None), "pSecondAuth"),(('DWORD', None), "dwP1SaFlags"),]

    

class ('FW_PHASE2_SA_DETAILS', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "SaId"),(('FW_DIRECTION', None), "Direction"),(('FW_ENDPOINTS', None), "Endpoints"),(('WORD', None), "wLocalPort"),(('WORD', None), "wRemotePort"),(('WORD', None), "wIpProtocol"),(('FW_PHASE2_CRYPTO_SUITE', None), "SelectedProposal"),(('FW_PHASE2_CRYPTO_PFS', None), "Pfs"),(('GUID', None), "TransportFilterId"),(('DWORD', None), "dwP2SaFlags"),]

    

class ('FW_PROFILE_CONFIG_VALUE', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PWCHAR', None), wszStr),2 : (('PFW_INTERFACE_LUIDS', None), pDisabledInterfaces),3 : (('PDWORD', None), pdwVal),}

    

class ('FW_MM_RULE', None)(NdrStructure):
    MEMBERS = [(('PPNEXT', None), "*pNext"),(('WORD', None), "wSchemaVersion"),(('PWCHAR', None), "wszRuleId"),(('PWCHAR', None), "wszName"),(('PWCHAR', None), "wszDescription"),(('DWORD', None), "dwProfiles"),(('FW_ADDRESSES', None), "Endpoint1"),(('FW_ADDRESSES', None), "Endpoint2"),(('PWCHAR', None), "wszPhase1AuthSet"),(('PWCHAR', None), "wszPhase1CryptoSet"),(('WORD', None), "wFlags"),(('PWCHAR', None), "wszEmbeddedContext"),(('FW_OS_PLATFORM_LIST', None), "PlatformValidityList"),(('FW_RULE_ORIGIN_TYPE', None), "Origin"),(('PWCHAR', None), "wszGPOName"),(('FW_RULE_STATUS', None), "Status"),(('DWORD', None), "Reserved"),(('PFW_OBJECT_METADATA', None), "pMetaData"),]

    

class ('FW_MATCH_VALUE', None)(NdrStructure):
    MEMBERS = [(('FW_DATA_TYPE', None), "type"),(('U0', None), "u0"),]

    

class ('FW_QUERY_CONDITION', None)(NdrStructure):
    MEMBERS = [(('FW_MATCH_KEY', None), "matchKey"),(('FW_MATCH_TYPE', None), "matchType"),(('FW_MATCH_VALUE', None), "matchValue"),]

    

class ('FW_QUERY_CONDITIONS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('PFW_QUERY_CONDITION', None), "AndedConditions"),]

    

class ('FW_QUERY', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wSchemaVersion"),(('UINT32', None), "dwNumEntries"),(('PFW_QUERY_CONDITIONS', None), "ORConditions"),(('FW_RULE_STATUS', None), "Status"),]

    
Method("RRPC_FWOpenPolicyStore",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_POLICY_ACCESS_RIGHT),
In(DWORD),
Out(PFW_POLICY_STORE_HANDLE),
),Method("RRPC_FWClosePolicyStore",
In(FW_CONN_HANDLE),
InOut(PFW_POLICY_STORE_HANDLE),
),Method("RRPC_FWRestoreDefaults",
In(FW_CONN_HANDLE),
),Method("RRPC_FWGetGlobalConfig",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
),Method("RRPC_FWSetGlobalConfig",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(PBYTE),
In(DWORD),
),Method("RRPC_FWAddFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_0),
),Method("RRPC_FWSetFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_0),
),Method("RRPC_FWDeleteFirewallRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_0),
),Method("RRPC_FWGetConfig",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
),Method("RRPC_FWSetConfig",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(FW_PROFILE_CONFIG_VALUE),
In(DWORD),
),Method("RRPC_FWAddConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_0),
),Method("RRPC_FWSetConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_0),
),Method("RRPC_FWDeleteConnectionSecurityRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPWSTR),
),Method("RRPC_FWDeleteAllConnectionSecurityRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumConnectionSecurityRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_0),
),Method("RRPC_FWAddAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
),Method("RRPC_FWSetAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
),Method("RRPC_FWDeleteAuthenticationSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
),Method("RRPC_FWEnumAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWAddCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
),Method("RRPC_FWSetCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
),Method("RRPC_FWDeleteCryptoSet",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(LPCWSTR),
),Method("RRPC_FWDeleteAllCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
),Method("RRPC_FWEnumCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWEnumPhase1SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
Out(PDWORD),
Out(PPFW_PHASE1_SA_DETAILS),
),Method("RRPC_FWEnumPhase2SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
Out(PDWORD),
Out(PPFW_PHASE2_SA_DETAILS),
),Method("RRPC_FWDeletePhase1SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
),Method("RRPC_FWDeletePhase2SAs",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_ENDPOINTS),
),Method("RRPC_FWEnumProducts",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_PRODUCT),
),Method("RRPC_FWAddMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_MM_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_MM_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWDeleteMainModeRule",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(LPWSTR),
),Method("RRPC_FWDeleteAllMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
),Method("RRPC_FWEnumMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_MM_RULE),
),Method("RRPC_FWQueryFirewallRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_10),
),Method("RRPC_FWQueryConnectionSecurityRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_10),
),Method("RRPC_FWQueryMainModeRules",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_MM_RULE),
),Method("RRPC_FWQueryAuthenticationSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWQueryCryptoSets",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWEnumNetworks",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_NETWORK),
),Method("RRPC_FWEnumAdapters",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
Out(PDWORD),
Out(PPFW_ADAPTER),
),Method("RRPC_FWGetGlobalConfig2_10",
In(FW_CONN_HANDLE),
In(WORD),
In(FW_STORE_TYPE),
In(FW_GLOBAL_CONFIG),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
Out(PFW_RULE_ORIGIN_TYPE),
),Method("RRPC_FWGetConfig2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_PROFILE_CONFIG),
In(FW_PROFILE_TYPE),
In(DWORD),
InOut(PBYTE),
In(DWORD),
InOut(LPDWORD),
Out(LPDWORD),
Out(PFW_RULE_ORIGIN_TYPE),
),Method("RRPC_FWAddFirewallRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_10),
),Method("RRPC_FWAddConnectionSecurityRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetConnectionSecurityRule2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumConnectionSecurityRules2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE2_10),
),Method("RRPC_FWAddAuthenticationSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetAuthenticationSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET2_10),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumAuthenticationSets2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET2_10),
),Method("RRPC_FWAddCryptoSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetCryptoSet2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CRYPTO_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumCryptoSets2_10",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CRYPTO_SET),
),Method("RRPC_FWAddConnectionSecurityRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetConnectionSecurityRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_CS_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumConnectionSecurityRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE),
),Method("RRPC_FWQueryConnectionSecurityRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_CS_RULE),
),Method("RRPC_FWAddAuthenticationSet2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetAuthenticationSet2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_AUTH_SET),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumAuthenticationSets2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET),
),Method("RRPC_FWQueryAuthenticationSets2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(FW_IPSEC_PHASE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_AUTH_SET),
),Method("RRPC_FWAddFirewallRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_20),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_20),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_20),
),Method("RRPC_FWQueryFirewallRules2_20",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_20),
),Method("RRPC_FWAddFirewallRule2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_24),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_24),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_24),
),Method("RRPC_FWQueryFirewallRules2_24",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_24),
),Method("RRPC_FWAddFirewallRule2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_25),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_25),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_25),
),Method("RRPC_FWQueryFirewallRules2_25",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_25),
),Method("RRPC_FWAddFirewallRule2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_26),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_26),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_26),
),Method("RRPC_FWQueryFirewallRules2_26",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_26),
),Method("RRPC_FWAddFirewallRule2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_27),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE2_27),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_27),
),Method("RRPC_FWQueryFirewallRules2_27",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE2_27),
),Method("RRPC_FWAddFirewallRule2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWSetFirewallRule2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_RULE),
Out(PFW_RULE_STATUS),
),Method("RRPC_FWEnumFirewallRules2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(DWORD),
In(DWORD),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE),
),Method("RRPC_FWQueryFirewallRules2_31",
In(FW_CONN_HANDLE),
In(FW_POLICY_STORE_HANDLE),
In(PFW_QUERY),
In(WORD),
Out(PDWORD),
Out(PPFW_RULE),
),