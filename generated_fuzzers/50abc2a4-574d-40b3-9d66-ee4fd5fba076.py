
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

    

class ('DNSSRV_STAT_HEADER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "StatId"),(('WORD', None), "wLength"),(('BOOLEAN', None), "fClear"),(('UCHAR', None), "fReserved"),]

    

class ('DNSSRV_STAT', None)(NdrStructure):
    MEMBERS = [(('DNSSRV_STAT_HEADER', None), "Header"),(('BYTE', None), "Buffer"),]

    

class ('IP4_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "AddrCount"),(('DWORD', None), "AddrArray"),]

    

class ('DNS_ADDR', None)(NdrStructure):
    MEMBERS = [(('CHAR', None), "MaxSa"),(('DWORD', None), "DnsAddrUserDword"),]

    

class ('DNS_ADDR_ARRAY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "MaxCount"),(('DWORD', None), "AddrCount"),(('DWORD', None), "Tag"),(('WORD', None), "Family"),(('WORD', None), "WordReserved"),(('DWORD', None), "Flags"),(('DWORD', None), "MatchFlag"),(('DWORD', None), "Reserved1"),(('DWORD', None), "Reserved2"),(('DNS_ADDR', None), "AddrArray"),]

    

class ('DNS_RPC_BUFFER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLength"),(('BYTE', None), "Buffer"),]

    

class ('DNS_RPC_SERVER_INFO_W2K', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('UCHAR', None), "fBootMethod"),(('BOOLEAN', None), "fAdminConfigured"),(('BOOLEAN', None), "fAllowUpdate"),(('BOOLEAN', None), "fDsAvailable"),(('PCHAR', None), "pszServerName"),(('PWCHAR_T', None), "pszDsContainer"),(('PIP4_ARRAY', None), "aipServerAddrs"),(('PIP4_ARRAY', None), "aipListenAddrs"),(('PIP4_ARRAY', None), "aipForwarders"),(('PDWORD', None), "pExtension1"),(('PDWORD', None), "pExtension2"),(('PDWORD', None), "pExtension3"),(('PDWORD', None), "pExtension4"),(('PDWORD', None), "pExtension5"),(('DWORD', None), "dwLogLevel"),(('DWORD', None), "dwDebugLevel"),(('DWORD', None), "dwForwardTimeout"),(('DWORD', None), "dwRpcProtocol"),(('DWORD', None), "dwNameCheckFlag"),(('DWORD', None), "cAddressAnswerLimit"),(('DWORD', None), "dwRecursionRetry"),(('DWORD', None), "dwRecursionTimeout"),(('DWORD', None), "dwMaxCacheTtl"),(('DWORD', None), "dwDsPollingInterval"),(('DWORD', None), "dwScavengingInterval"),(('DWORD', None), "dwDefaultRefreshInterval"),(('DWORD', None), "dwDefaultNoRefreshInterval"),(('DWORD', None), "dwReserveArray"),(('BOOLEAN', None), "fAutoReverseZones"),(('BOOLEAN', None), "fAutoCacheUpdate"),(('BOOLEAN', None), "fRecurseAfterForwarding"),(('BOOLEAN', None), "fForwardDelegations"),(('BOOLEAN', None), "fNoRecursion"),(('BOOLEAN', None), "fSecureResponses"),(('BOOLEAN', None), "fRoundRobin"),(('BOOLEAN', None), "fLocalNetPriority"),(('BOOLEAN', None), "fBindSecondaries"),(('BOOLEAN', None), "fWriteAuthorityNs"),(('BOOLEAN', None), "fStrictFileParsing"),(('BOOLEAN', None), "fLooseWildcarding"),(('BOOLEAN', None), "fDefaultAgingState"),(('BOOLEAN', None), "fReserveArray"),]

    

class ('DNS_RPC_SERVER_INFO_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwVersion"),(('UCHAR', None), "fBootMethod"),(('BOOLEAN', None), "fAdminConfigured"),(('BOOLEAN', None), "fAllowUpdate"),(('BOOLEAN', None), "fDsAvailable"),(('PCHAR', None), "pszServerName"),(('PWCHAR_T', None), "pszDsContainer"),(('PIP4_ARRAY', None), "aipServerAddrs"),(('PIP4_ARRAY', None), "aipListenAddrs"),(('PIP4_ARRAY', None), "aipForwarders"),(('PIP4_ARRAY', None), "aipLogFilter"),(('PWCHAR_T', None), "pwszLogFilePath"),(('PCHAR', None), "pszDomainName"),(('PCHAR', None), "pszForestName"),(('PCHAR', None), "pszDomainDirectoryPartition"),(('PCHAR', None), "pszForestDirectoryPartition"),(('PCHAR', None), "pExtensions"),(('DWORD', None), "dwLogLevel"),(('DWORD', None), "dwDebugLevel"),(('DWORD', None), "dwForwardTimeout"),(('DWORD', None), "dwRpcProtocol"),(('DWORD', None), "dwNameCheckFlag"),(('DWORD', None), "cAddressAnswerLimit"),(('DWORD', None), "dwRecursionRetry"),(('DWORD', None), "dwRecursionTimeout"),(('DWORD', None), "dwMaxCacheTtl"),(('DWORD', None), "dwDsPollingInterval"),(('DWORD', None), "dwLocalNetPriorityNetMask"),(('DWORD', None), "dwScavengingInterval"),(('DWORD', None), "dwDefaultRefreshInterval"),(('DWORD', None), "dwDefaultNoRefreshInterval"),(('DWORD', None), "dwLastScavengeTime"),(('DWORD', None), "dwEventLogLevel"),(('DWORD', None), "dwLogFileMaxSize"),(('DWORD', None), "dwDsForestVersion"),(('DWORD', None), "dwDsDomainVersion"),(('DWORD', None), "dwDsDsaVersion"),(('DWORD', None), "dwReserveArray"),(('BOOLEAN', None), "fAutoReverseZones"),(('BOOLEAN', None), "fAutoCacheUpdate"),(('BOOLEAN', None), "fRecurseAfterForwarding"),(('BOOLEAN', None), "fForwardDelegations"),(('BOOLEAN', None), "fNoRecursion"),(('BOOLEAN', None), "fSecureResponses"),(('BOOLEAN', None), "fRoundRobin"),(('BOOLEAN', None), "fLocalNetPriority"),(('BOOLEAN', None), "fBindSecondaries"),(('BOOLEAN', None), "fWriteAuthorityNs"),(('BOOLEAN', None), "fStrictFileParsing"),(('BOOLEAN', None), "fLooseWildcarding"),(('BOOLEAN', None), "fDefaultAgingState"),(('BOOLEAN', None), "fReserveArray"),]

    

class ('DNS_RPC_SERVER_INFO_LONGHORN', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwVersion"),(('UCHAR', None), "fBootMethod"),(('BOOLEAN', None), "fAdminConfigured"),(('BOOLEAN', None), "fAllowUpdate"),(('BOOLEAN', None), "fDsAvailable"),(('PCHAR', None), "pszServerName"),(('PWCHAR_T', None), "pszDsContainer"),(('PDNS_ADDR_ARRAY', None), "aipServerAddrs"),(('PDNS_ADDR_ARRAY', None), "aipListenAddrs"),(('PDNS_ADDR_ARRAY', None), "aipForwarders"),(('PDNS_ADDR_ARRAY', None), "aipLogFilter"),(('PWCHAR_T', None), "pwszLogFilePath"),(('PCHAR', None), "pszDomainName"),(('PCHAR', None), "pszForestName"),(('PCHAR', None), "pszDomainDirectoryPartition"),(('PCHAR', None), "pszForestDirectoryPartition"),(('PCHAR', None), "pExtensions"),(('DWORD', None), "dwLogLevel"),(('DWORD', None), "dwDebugLevel"),(('DWORD', None), "dwForwardTimeout"),(('DWORD', None), "dwRpcProtocol"),(('DWORD', None), "dwNameCheckFlag"),(('DWORD', None), "cAddressAnswerLimit"),(('DWORD', None), "dwRecursionRetry"),(('DWORD', None), "dwRecursionTimeout"),(('DWORD', None), "dwMaxCacheTtl"),(('DWORD', None), "dwDsPollingInterval"),(('DWORD', None), "dwLocalNetPriorityNetMask"),(('DWORD', None), "dwScavengingInterval"),(('DWORD', None), "dwDefaultRefreshInterval"),(('DWORD', None), "dwDefaultNoRefreshInterval"),(('DWORD', None), "dwLastScavengeTime"),(('DWORD', None), "dwEventLogLevel"),(('DWORD', None), "dwLogFileMaxSize"),(('DWORD', None), "dwDsForestVersion"),(('DWORD', None), "dwDsDomainVersion"),(('DWORD', None), "dwDsDsaVersion"),(('BOOLEAN', None), "fReadOnlyDC"),(('DWORD', None), "dwReserveArray"),(('BOOLEAN', None), "fAutoReverseZones"),(('BOOLEAN', None), "fAutoCacheUpdate"),(('BOOLEAN', None), "fRecurseAfterForwarding"),(('BOOLEAN', None), "fForwardDelegations"),(('BOOLEAN', None), "fNoRecursion"),(('BOOLEAN', None), "fSecureResponses"),(('BOOLEAN', None), "fRoundRobin"),(('BOOLEAN', None), "fLocalNetPriority"),(('BOOLEAN', None), "fBindSecondaries"),(('BOOLEAN', None), "fWriteAuthorityNs"),(('BOOLEAN', None), "fStrictFileParsing"),(('BOOLEAN', None), "fLooseWildcarding"),(('BOOLEAN', None), "fDefaultAgingState"),(('BOOLEAN', None), "fReserveArray"),]

    

class ('DNS_RPC_FORWARDERS_W2K', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "fRecurseAfterForwarding"),(('DWORD', None), "dwForwardTimeout"),(('PIP4_ARRAY', None), "aipForwarders"),]

    

class ('DNS_RPC_FORWARDERS_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fRecurseAfterForwarding"),(('DWORD', None), "dwForwardTimeout"),(('PIP4_ARRAY', None), "aipForwarders"),]

    

class ('DNS_RPC_FORWARDERS_LONGHORN', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fRecurseAfterForwarding"),(('DWORD', None), "dwForwardTimeout"),(('PDNS_ADDR_ARRAY', None), "aipForwarders"),]

    

class ('DNS_RPC_ZONE_W2K', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "pszZoneName"),(('DNS_RPC_ZONE_FLAGS', None), "Flags"),(('UCHAR', None), "ZoneType"),(('UCHAR', None), "Version"),]

    

class ('DNS_RPC_ZONE_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PWCHAR_T', None), "pszZoneName"),(('DNS_RPC_ZONE_FLAGS', None), "Flags"),(('UCHAR', None), "ZoneType"),(('UCHAR', None), "Version"),(('DWORD', None), "dwDpFlags"),(('PCHAR', None), "pszDpFqdn"),]

    

class ('DNS_RPC_ZONE_LIST_W2K', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwZoneCount"),(('PDNS_RPC_ZONE_W2K', None), "ZoneArray"),]

    

class ('DNS_RPC_ZONE_LIST_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwZoneCount"),(('PDNS_RPC_ZONE_DOTNET', None), "ZoneArray"),]

    

class ('DNS_RPC_TRUST_POINT', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszTrustPointName"),(('TRUSTPOINT_STATE', None), "eTrustPointState"),(('__INT64', None), "i64LastActiveRefreshTime"),(('__INT64', None), "i64NextActiveRefreshTime"),(('__INT64', None), "i64LastSuccessfulActiveRefreshTime"),(('DWORD', None), "dwLastActiveRefreshResult"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_TRUST_POINT_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwTrustPointCount"),(('PDNS_RPC_TRUST_POINT', None), "TrustPointArray"),]

    

class ('DNS_RPC_SKD', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('GUID', None), "Guid"),(('PWCHAR_T', None), "pwszKeyStorageProvider"),(('BOOL', None), "fStoreKeysInDirectory"),(('BOOL', None), "fIsKSK"),(('BYTE', None), "bSigningAlgorithm"),(('DWORD', None), "dwKeyLength"),(('DWORD', None), "dwInitialRolloverOffset"),(('DWORD', None), "dwDNSKEYSignatureValidityPeriod"),(('DWORD', None), "dwDSSignatureValidityPeriod"),(('DWORD', None), "dwStandardSignatureValidityPeriod"),(('DWORD', None), "dwRolloverType"),(('DWORD', None), "dwRolloverPeriod"),(('DWORD', None), "dwNextRolloverAction"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_SKD_STATE_EX', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('GUID', None), "Guid"),(('DWORD', None), "dwCurrentRollState"),(('DWORD', None), "fManualTrigger"),(('DWORD', None), "dwPreRollEventFired"),(('FILETIME', None), "ftNextKeyGenerationTime"),(('DWORD', None), "dwRevokedOrSwappedDnskeysLength"),(('PBYTE', None), "pRevokedOrSwappedDnskeysBuffer"),(('DWORD', None), "dwFinalDnskeysLength"),(('PBYTE', None), "pFinalDnskeys"),(('KEYSIGNSCOPE', None), "eActiveKeyScope"),(('KEYSIGNSCOPE', None), "eStandByKeyScope"),(('KEYSIGNSCOPE', None), "eNextKeyScope"),]

    

class ('DNS_RPC_SKD_STATE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('GUID', None), "Guid"),(('FILETIME', None), "ftLastRolloverTime"),(('FILETIME', None), "ftNextRolloverTime"),(('DWORD', None), "dwState"),(('DWORD', None), "dwCurrentRolloverStatus"),(('PWCHAR_T', None), "pwszActiveKey"),(('PWCHAR_T', None), "pwszStandbyKey"),(('PWCHAR_T', None), "pwszNextKey"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_ZONE_SKD', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PDNS_RPC_SKD', None), "pSkd"),(('PDNS_RPC_SKD_STATE', None), "pSkdState"),(('PDNS_RPC_SKD_STATE_EX', None), "pSkdStateEx"),]

    

class ('DNS_RPC_ZONE_DNSSEC_SETTINGS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fIsSigned"),(('DWORD', None), "fSignWithNSEC3"),(('DWORD', None), "fNSEC3OptOut"),(('DWORD', None), "dwMaintainTrustAnchor"),(('DWORD', None), "fParentHasSecureDelegation"),(('DWORD', None), "dwDSRecordAlgorithms"),(('DWORD', None), "fRFC5011KeyRollovers"),(('BYTE', None), "bNSEC3HashAlgorithm"),(('BYTE', None), "bNSEC3RandomSaltLength"),(('WORD', None), "wNSEC3IterationCount"),(('LPWSTR', None), "pwszNSEC3UserSalt"),(('DWORD', None), "dwDNSKEYRecordSetTtl"),(('DWORD', None), "dwDSRecordSetTtl"),(('DWORD', None), "dwSignatureInceptionOffset"),(('DWORD', None), "dwSecureDelegationPollingPeriod"),(('DWORD', None), "dwPropagationTime"),(('DWORD', None), "cbNSEC3CurrentSaltLength"),(('PBYTE', None), "pbNSEC3CurrentSalt"),(('GUID', None), "CurrentRollingSKDGuid"),(('DWORD', None), "dwBufferLength"),(('PBYTE', None), "pBuffer"),(('DWORD', None), "dwCount"),(('PDNS_RPC_ZONE_SKD', None), "pZoneSkdArray"),]

    

class ('DNS_RPC_TRUST_ANCHOR', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('WORD', None), "wTrustAnchorType"),(('WORD', None), "wKeyTag"),(('WORD', None), "wRRLength"),(('TRUSTANCHOR_STATE', None), "eTrustAnchorState"),(('__INT64', None), "i64EnteredStateTime"),(('__INT64', None), "i64NextStateTime"),(('DWORD', None), "dwReserved"),(('BYTE', None), "RRData"),]

    

class ('DNS_RPC_TRUST_ANCHOR_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwTrustAnchorCount"),(('PDNS_RPC_TRUST_ANCHOR', None), "TrustAnchorArray"),]

    

class ('DNS_RPC_DP_ENUM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszDpFqdn"),(('DWORD', None), "dwFlags"),(('DWORD', None), "dwZoneCount"),]

    

class ('DNS_RPC_DP_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwDpCount"),(('PDNS_RPC_DP_ENUM', None), "DpArray"),]

    

class ('DNS_RPC_DP_REPLICA', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "pszReplicaDn"),]

    

class ('DNS_RPC_DP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszDpFqdn"),(('PWCHAR_T', None), "pszDpDn"),(('PWCHAR_T', None), "pszCrDn"),(('DWORD', None), "dwFlags"),(('DWORD', None), "dwZoneCount"),(('DWORD', None), "dwState"),(('DWORD', None), "dwReserved"),(('PWCHAR_T', None), "pwszReserved"),(('DWORD', None), "dwReplicaCount"),(('PDNS_RPC_DP_REPLICA', None), "ReplicaArray"),]

    

class ('DNS_RPC_ENLIST_DP', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszDpFqdn"),(('DWORD', None), "dwOperation"),]

    

class ('DNS_RPC_ZONE_EXPORT_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszZoneExportFile"),]

    

class ('DNS_RPC_ZONE_SECONDARIES_W2K', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PIP4_ARRAY', None), "aipSecondaries"),(('PIP4_ARRAY', None), "aipNotify"),]

    

class ('DNS_RPC_ZONE_SECONDARIES_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PIP4_ARRAY', None), "aipSecondaries"),(('PIP4_ARRAY', None), "aipNotify"),]

    

class ('DNS_RPC_ZONE_SECONDARIES_LONGHORN', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PDNS_ADDR_ARRAY', None), "aipSecondaries"),(('PDNS_ADDR_ARRAY', None), "aipNotify"),]

    

class ('DNS_RPC_ZONE_DATABASE_W2K', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "fDsIntegrated"),(('PCHAR', None), "pszFileName"),]

    

class ('DNS_RPC_ZONE_DATABASE_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "fDsIntegrated"),(('PCHAR', None), "pszFileName"),]

    

class ('DNS_RPC_ZONE_CHANGE_DP', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszDestPartition"),]

    

class ('DNS_RPC_ZONE_INFO_W2K', None)(NdrStructure):
    MEMBERS = [(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fReverse"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fPaused"),(('DWORD', None), "fShutdown"),(('DWORD', None), "fAutoCreated"),(('DWORD', None), "fUseDatabase"),(('PCHAR', None), "pszDataFile"),(('PIP4_ARRAY', None), "aipMasters"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PIP4_ARRAY', None), "aipSecondaries"),(('PIP4_ARRAY', None), "aipNotify"),(('DWORD', None), "fUseWins"),(('DWORD', None), "fUseNbstat"),(('DWORD', None), "fAging"),(('DWORD', None), "dwNoRefreshInterval"),(('DWORD', None), "dwRefreshInterval"),(('DWORD', None), "dwAvailForScavengeTime"),(('PIP4_ARRAY', None), "aipScavengeServers"),(('DWORD', None), "pvReserved1"),(('DWORD', None), "pvReserved2"),(('DWORD', None), "pvReserved3"),(('DWORD', None), "pvReserved4"),]

    

class ('DNS_RPC_ZONE_INFO_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fReverse"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fPaused"),(('DWORD', None), "fShutdown"),(('DWORD', None), "fAutoCreated"),(('DWORD', None), "fUseDatabase"),(('PCHAR', None), "pszDataFile"),(('PIP4_ARRAY', None), "aipMasters"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PIP4_ARRAY', None), "aipSecondaries"),(('PIP4_ARRAY', None), "aipNotify"),(('DWORD', None), "fUseWins"),(('DWORD', None), "fUseNbstat"),(('DWORD', None), "fAging"),(('DWORD', None), "dwNoRefreshInterval"),(('DWORD', None), "dwRefreshInterval"),(('DWORD', None), "dwAvailForScavengeTime"),(('PIP4_ARRAY', None), "aipScavengeServers"),(('DWORD', None), "dwForwarderTimeout"),(('DWORD', None), "fForwarderSlave"),(('PIP4_ARRAY', None), "aipLocalMasters"),(('DWORD', None), "dwDpFlags"),(('PCHAR', None), "pszDpFqdn"),(('PWCHAR_T', None), "pwszZoneDn"),(('DWORD', None), "dwLastSuccessfulSoaCheck"),(('DWORD', None), "dwLastSuccessfulXfr"),(('DWORD', None), "dwReserved1"),(('DWORD', None), "dwReserved2"),(('DWORD', None), "dwReserved3"),(('DWORD', None), "dwReserved4"),(('DWORD', None), "dwReserved5"),(('PCHAR', None), "pReserved1"),(('PCHAR', None), "pReserved2"),(('PCHAR', None), "pReserved3"),(('PCHAR', None), "pReserved4"),]

    

class ('DNS_RPC_ZONE_INFO_LONGHORN', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fReverse"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fPaused"),(('DWORD', None), "fShutdown"),(('DWORD', None), "fAutoCreated"),(('DWORD', None), "fUseDatabase"),(('PCHAR', None), "pszDataFile"),(('PDNS_ADDR_ARRAY', None), "aipMasters"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PDNS_ADDR_ARRAY', None), "aipSecondaries"),(('PDNS_ADDR_ARRAY', None), "aipNotify"),(('DWORD', None), "fUseWins"),(('DWORD', None), "fUseNbstat"),(('DWORD', None), "fAging"),(('DWORD', None), "dwNoRefreshInterval"),(('DWORD', None), "dwRefreshInterval"),(('DWORD', None), "dwAvailForScavengeTime"),(('PDNS_ADDR_ARRAY', None), "aipScavengeServers"),(('DWORD', None), "dwForwarderTimeout"),(('DWORD', None), "fForwarderSlave"),(('PDNS_ADDR_ARRAY', None), "aipLocalMasters"),(('DWORD', None), "dwDpFlags"),(('PCHAR', None), "pszDpFqdn"),(('PWCHAR_T', None), "pwszZoneDn"),(('DWORD', None), "dwLastSuccessfulSoaCheck"),(('DWORD', None), "dwLastSuccessfulXfr"),(('DWORD', None), "fQueuedForBackgroundLoad"),(('DWORD', None), "fBackgroundLoadInProgress"),(('BOOL', None), "fReadOnlyZone"),(('DWORD', None), "dwLastXfrAttempt"),(('DWORD', None), "dwLastXfrResult"),]

    

class ('DNS_RPC_ZONE_CREATE_INFO_W2K', None)(NdrStructure):
    MEMBERS = [(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fAging"),(('DWORD', None), "dwFlags"),(('PCHAR', None), "pszDataFile"),(('DWORD', None), "fDsIntegrated"),(('DWORD', None), "fLoadExisting"),(('PCHAR', None), "pszAdmin"),(('PIP4_ARRAY', None), "aipMasters"),(('PIP4_ARRAY', None), "aipSecondaries"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('PCHAR', None), "pvReserved1"),(('PCHAR', None), "pvReserved2"),(('PCHAR', None), "pvReserved3"),(('PCHAR', None), "pvReserved4"),(('PCHAR', None), "pvReserved5"),(('PCHAR', None), "pvReserved6"),(('PCHAR', None), "pvReserved7"),(('PCHAR', None), "pvReserved8"),(('DWORD', None), "dwReserved1"),(('DWORD', None), "dwReserved2"),(('DWORD', None), "dwReserved3"),(('DWORD', None), "dwReserved4"),(('DWORD', None), "dwReserved5"),(('DWORD', None), "dwReserved6"),(('DWORD', None), "dwReserved7"),(('DWORD', None), "dwReserved8"),]

    

class ('DNS_RPC_ZONE_CREATE_INFO_DOTNET', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fAging"),(('DWORD', None), "dwFlags"),(('PCHAR', None), "pszDataFile"),(('DWORD', None), "fDsIntegrated"),(('DWORD', None), "fLoadExisting"),(('PCHAR', None), "pszAdmin"),(('PIP4_ARRAY', None), "aipMasters"),(('PIP4_ARRAY', None), "aipSecondaries"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('DWORD', None), "dwTimeout"),(('DWORD', None), "fRecurseAfterForwarding"),(('DWORD', None), "dwDpFlags"),(('PCHAR', None), "pszDpFqdn"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_ZONE_CREATE_INFO_LONGHORN', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('PCHAR', None), "pszZoneName"),(('DWORD', None), "dwZoneType"),(('DWORD', None), "fAllowUpdate"),(('DWORD', None), "fAging"),(('DWORD', None), "dwFlags"),(('PCHAR', None), "pszDataFile"),(('DWORD', None), "fDsIntegrated"),(('DWORD', None), "fLoadExisting"),(('PCHAR', None), "pszAdmin"),(('PDNS_ADDR_ARRAY', None), "aipMasters"),(('PDNS_ADDR_ARRAY', None), "aipSecondaries"),(('DWORD', None), "fSecureSecondaries"),(('DWORD', None), "fNotifyLevel"),(('DWORD', None), "dwTimeout"),(('DWORD', None), "fRecurseAfterForwarding"),(('DWORD', None), "dwDpFlags"),(('PCHAR', None), "pszDpFqdn"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_SKD_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwCount"),(('PDNS_RPC_SKD', None), "SkdArray"),]

    

class ('DNS_RPC_SIGNING_VALIDATION_ERROR', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('GUID', None), "guidSKD"),(('PWCHAR_T', None), "pwszSigningKeyPointerString"),(('DWORD', None), "dwExtendedError"),(('DWORD', None), "dwReserved"),]

    

class ('DNS_RPC_AUTOCONFIGURE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwAutoConfigFlags"),(('DWORD', None), "dwReserved1"),(('PCHAR', None), "pszNewDomainName"),]

    

class ('DNS_RPC_ENUM_ZONES_FILTER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwFilter"),(('PCHAR', None), "pszPartitionFqdn"),(('PCHAR', None), "pszQueryString"),(('PCHAR', None), "pszReserved"),]

    

class ('DNS_RPC_RECORD', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wDataLength"),(('WORD', None), "wType"),(('DWORD', None), "dwFlags"),(('DWORD', None), "dwSerial"),(('DWORD', None), "dwTtlSeconds"),(('DWORD', None), "dwTimeStamp"),(('DWORD', None), "dwReserved"),(('BYTE', None), "Buffer"),]

    

class ('DNS_RPC_NAME_AND_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwParam"),(('PCHAR', None), "pszNodeName"),]

    

class ('DNS_RPC_IP_VALIDATE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved0"),(('DWORD', None), "dwContext"),(('DWORD', None), "dwReserved1"),(('PCHAR', None), "pszContextName"),(('PDNS_ADDR_ARRAY', None), "aipValidateAddrs"),]

    

class ('DNS_RPC_UTF8_STRING_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwCount"),(('PCHAR', None), "pszStrings"),]

    

class ('DNS_RPC_UNICODE_STRING_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwCount"),(('PWCHAR_T', None), "pwszStrings"),]

    

class ('DNS_RPC_CLIENT_SUBNET_RECORD', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszClientSubnetName"),(('PDNS_ADDR_ARRAY', None), "pIPAddr"),(('PDNS_ADDR_ARRAY', None), "pIPv6Addr"),]

    

class ('DNS_RPC_POLICY_CONTENT', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszScopeName"),(('DWORD', None), "dwWeight"),]

    

class ('DNS_RPC_POLICY_CONTENT_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwContentCount"),(('PDNS_RPC_POLICY_CONTENT', None), "pContent"),]

    

class ('DNS_RPC_CRITERIA', None)(NdrStructure):
    MEMBERS = [(('DNS_RPC_CRITERIA_ENUM', None), "type"),(('LPWSTR', None), "pCriteria"),]

    

class ('DNS_RPC_POLICY', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszPolicyName"),(('DNS_RPC_POLICY_LEVEL', None), "level"),(('DNS_RPC_POLICY_TYPE', None), "appliesOn"),(('DNS_RPC_POLICY_ACTION_TYPE', None), "action"),(('DNS_RPC_POLICY_CONDITION', None), "condition"),(('BOOL', None), "isEnabled"),(('DWORD', None), "dwProcessingOrder"),(('LPSTR', None), "pszZoneName"),(('PDNS_RPC_POLICY_CONTENT_LIST', None), "pContentList"),(('DWORDLONG', None), "flags"),(('DWORD', None), "dwCriteriaCount"),(('PDNS_RPC_CRITERIA', None), "pCriteriaList"),]

    

class ('DNS_RPC_POLICY_NAME', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszPolicyName"),(('DNS_RPC_POLICY_TYPE', None), "appliesOn"),(('BOOL', None), "fEnabled"),(('DWORD', None), "processingOrder"),]

    

class ('DNS_RPC_ENUMERATE_POLICY_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwPolicyCount"),(('PDNS_RPC_POLICY_NAME', None), "pPolicyArray"),]

    

class ('DNS_RPC_RRL_PARAMS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwResponsesPerSecond"),(('DWORD', None), "dwErrorsPerSecond"),(('DWORD', None), "dwLeakRate"),(('DWORD', None), "dwTCRate"),(('DWORD', None), "dwTotalResponsesInWindow"),(('DWORD', None), "dwWindowSize"),(('DWORD', None), "dwIPv4PrefixLength"),(('DWORD', None), "dwIPv6PrefixLength"),(('DNS_RRL_MODE_ENUM', None), "eMode"),(('DWORD', None), "dwFlags"),(('BOOL', None), "fSetDefault"),]

    

class ('DNS_RPC_VIRTUALIZATION_INSTANCE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwReserved"),(('DWORD', None), "dwFlags"),(('LPWSTR', None), "pwszVirtualizationID"),(('LPWSTR', None), "pwszFriendlyName"),(('LPWSTR', None), "pwszDescription"),]

    

class ('DNS_RPC_VIRTUALIZATION_INSTANCE_INFO', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszVirtualizationID"),(('LPWSTR', None), "pwszFriendlyName"),(('LPWSTR', None), "pwszDescription"),]

    

class ('DNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwVirtualizationInstanceCount"),(('PDNS_RPC_VIRTUALIZATION_INSTANCE_INFO', None), "VirtualizationInstanceArray"),]

    

class ('DNS_RPC_ENUM_ZONE_SCOPE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwZoneScopeCount"),(('LPWSTR', None), "ZoneScopeArray"),]

    

class ('DNS_SYSTEMTIME', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wYear"),(('WORD', None), "wMonth"),(('WORD', None), "wDayOfWeek"),(('WORD', None), "wDay"),(('WORD', None), "wHour"),(('WORD', None), "wMinute"),(('WORD', None), "wSecond"),(('WORD', None), "wMilliseconds"),]

    

class ('DNSSRV_ZONE_TIME_STATS', None)(NdrStructure):
    MEMBERS = [(('DNS_SYSTEMTIME', None), "StatsCollectionStartTime"),]

    

class ('DNSSRV_ZONE_QUERY_STATS', None)(NdrStructure):
    MEMBERS = [(('DNS_ZONE_STATS_TYPE', None), "RecordType"),(('ULONG64', None), "QueriesResponded"),(('ULONG64', None), "QueriesReceived"),(('ULONG64', None), "QueriesFailure"),(('ULONG64', None), "QueriesNameError"),]

    

class ('DNSSRV_RRL_STATS', None)(NdrStructure):
    MEMBERS = [(('DNSSRV_STAT_HEADER', None), "Header"),(('DWORD', None), "TotalResponsesSent"),(('DWORD', None), "TotalResponsesDropped"),(('DWORD', None), "TotalResponsesTruncated"),(('DWORD', None), "TotalResponsesLeaked"),]

    

class ('DNSSRV_ZONE_TRANSFER_STATS', None)(NdrStructure):
    MEMBERS = [(('DNS_ZONE_STATS_TYPE', None), "TransferType"),(('ULONG64', None), "RequestReceived"),(('ULONG64', None), "RequestSent"),(('ULONG64', None), "ResponseReceived"),(('ULONG64', None), "SuccessReceived"),(('ULONG64', None), "SuccessSent"),]

    

class ('DNSSRV_ZONE_UPDATE_STATS', None)(NdrStructure):
    MEMBERS = [(('DNS_ZONE_STATS_TYPE', None), "Type"),(('ULONG64', None), "DynamicUpdateReceived"),(('ULONG64', None), "DynamicUpdateRejected"),]

    

class ('DNSSRV_ZONE_RRL_STATS', None)(NdrStructure):
    MEMBERS = [(('DNS_ZONE_STATS_TYPE', None), "Type"),(('DWORD', None), "TotalResponsesSent"),(('DWORD', None), "TotalResponsesDropped"),(('DWORD', None), "TotalResponsesTruncated"),(('DWORD', None), "TotalResponsesLeaked"),]

    

class ('DNS_RPC_ZONE_STATS_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DNSSRV_ZONE_TIME_STATS', None), "ZoneTimeStats"),(('DNSSRV_ZONE_QUERY_STATS', None), "ZoneQueryStats"),(('DNSSRV_ZONE_TRANSFER_STATS', None), "ZoneTransferStats"),(('DNSSRV_ZONE_UPDATE_STATS', None), "ZoneUpdateStats"),(('DNSSRV_ZONE_RRL_STATS', None), "ZoneRRLStats"),]

    

class ('DNS_RPC_ZONE_SCOPE_CREATE_INFO_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwFlags"),(('LPWSTR', None), "pwszScopeName"),]

    

class ('DNS_RPC_ZONE_SCOPE_INFO_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('LPWSTR', None), "pwszScopeName"),(('LPWSTR', None), "pwszDataFile"),]

    

class ('DNS_RPC_ENUM_SCOPE_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRpcStructureVersion"),(('DWORD', None), "dwScopeCount"),(('LPWSTR', None), "ScopeArray"),]

    

class ('DNSSRV_RPC_UNION', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PBYTE', None), Null),2 : (('DWORD', None), Dword),3 : (('PCHAR', None), String),4 : (('PWCHAR_T', None), WideString),5 : (('PIP4_ARRAY', None), IpArray),6 : (('PDNS_RPC_BUFFER', None), Buffer),7 : (('PDNS_RPC_SERVER_INFO_W2K', None), ServerInfoW2K),8 : (('PDNSSRV_STATS', None), Stats),9 : (('PDNS_RPC_FORWARDERS_W2K', None), ForwardersW2K),10 : (('PDNS_RPC_ZONE_W2K', None), ZoneW2K),11 : (('PDNS_RPC_ZONE_INFO_W2K', None), ZoneInfoW2K),12 : (('PDNS_RPC_ZONE_SECONDARIES_W2K', None), SecondariesW2K),13 : (('PDNS_RPC_ZONE_DATABASE_W2K', None), DatabaseW2K),14 : (('PDNS_RPC_ZONE_CREATE_INFO_W2K', None), ZoneCreateW2K),15 : (('PDNS_RPC_NAME_AND_PARAM', None), NameAndParam),16 : (('PDNS_RPC_ZONE_LIST_W2K', None), ZoneListW2K),17 : (('PDNS_RPC_SERVER_INFO_DOTNET', None), ServerInfoDotNet),18 : (('PDNS_RPC_FORWARDERS_DOTNET', None), ForwardersDotNet),19 : (('PDNS_RPC_ZONE', None), Zone),20 : (('PDNS_RPC_ZONE_INFO_DOTNET', None), ZoneInfoDotNet),21 : (('PDNS_RPC_ZONE_SECONDARIES_DOTNET', None), SecondariesDotNet),22 : (('PDNS_RPC_ZONE_DATABASE', None), Database),23 : (('PDNS_RPC_ZONE_CREATE_INFO_DOTNET', None), ZoneCreateDotNet),24 : (('PDNS_RPC_ZONE_LIST', None), ZoneList),25 : (('PDNS_RPC_ZONE_EXPORT_INFO', None), ZoneExport),26 : (('PDNS_RPC_DP_INFO', None), DirectoryPartition),27 : (('PDNS_RPC_DP_ENUM', None), DirectoryPartitionEnum),28 : (('PDNS_RPC_DP_LIST', None), DirectoryPartitionList),29 : (('PDNS_RPC_ENLIST_DP', None), EnlistDirectoryPartition),30 : (('PDNS_RPC_ZONE_CHANGE_DP', None), ZoneChangeDirectoryPartition),31 : (('PDNS_RPC_ENUM_ZONES_FILTER', None), EnumZonesFilter),32 : (('PDNS_ADDR_ARRAY', None), AddrArray),33 : (('PDNS_RPC_SERVER_INFO', None), ServerInfo),34 : (('PDNS_RPC_ZONE_CREATE_INFO', None), ZoneCreate),35 : (('PDNS_RPC_FORWARDERS', None), Forwarders),36 : (('PDNS_RPC_ZONE_SECONDARIES', None), Secondaries),37 : (('PDNS_RPC_IP_VALIDATE', None), IpValidate),38 : (('PDNS_RPC_ZONE_INFO', None), ZoneInfo),39 : (('PDNS_RPC_AUTOCONFIGURE', None), AutoConfigure),40 : (('PDNS_RPC_UTF8_STRING_LIST', None), Utf8StringList),41 : (('PDNS_RPC_UNICODE_STRING_LIST', None), UnicodeStringList),42 : (('PDNS_RPC_SKD', None), Skd),43 : (('PDNS_RPC_SKD_LIST', None), SkdList),44 : (('PDNS_RPC_SKD_STATE', None), SkdState),45 : (('PDNS_RPC_SIGNING_VALIDATION_ERROR', None), SigningValidationError),46 : (('PDNS_RPC_TRUST_POINT_LIST', None), TrustPointList),47 : (('PDNS_RPC_TRUST_ANCHOR_LIST', None), TrustAnchorList),48 : (('PDNS_RPC_ZONE_DNSSEC_SETTINGS', None), ZoneDnsSecSettings),49 : (('PDNS_RPC_ENUM_ZONE_SCOPE_LIST', None), ZoneScopeList),50 : (('PDNS_RPC_ZONE_STATS_V1', None), ZoneStats),51 : (('PDNS_RPC_ZONE_SCOPE_CREATE_INFO_V1', None), ScopeCreate),52 : (('PDNS_RPC_ZONE_SCOPE_INFO_V1', None), ScopeInfo),53 : (('PDNS_RPC_ENUM_SCOPE_LIST', None), ScopeList),54 : (('PDNS_RPC_CLIENT_SUBNET_RECORD', None), SubnetList),55 : (('PDNS_RPC_POLICY', None), pPolicy),56 : (('PDNS_RPC_POLICY_NAME', None), pPolicyName),57 : (('PDNS_RPC_ENUMERATE_POLICY_LIST', None), pPolicyList),58 : (('PDNS_RPC_RRL_PARAMS', None), pRRLParams),59 : (('PDNS_RPC_VIRTUALIZATION_INSTANCE', None), VirtualizationInstance),60 : (('PDNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST', None), VirtualizationInstanceList),}

    
Method("R_DnssrvOperation",
In(LPCWSTR),
In(LPCSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),Method("R_DnssrvQuery",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvComplexOperation",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvEnumRecords",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),Method("R_DnssrvUpdateRecord",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),Method("R_DnssrvOperation2",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),Method("R_DnssrvQuery2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvComplexOperation2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvEnumRecords2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),Method("R_DnssrvUpdateRecord2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),Method("R_DnssrvUpdateRecord3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),Method("R_DnssrvEnumRecords3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),Method("R_DnssrvOperation3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),Method("R_DnssrvQuery3",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvComplexOperation3",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvOperation4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),Method("R_DnssrvQuery4",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),Method("R_DnssrvUpdateRecord4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),Method("R_DnssrvEnumRecords4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),