
from fuzzer.midl import *
from fuzzer.core import *
DWORD64 = NdrHyper
DWORD = NdrLong
__INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
INT = NdrLong
VOID = CONTEXT_HANDLE
LONG = NdrLong
__INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    

class DNSSRV_STAT_HEADER(NdrStructure):
    MEMBERS = [(DWORD, "StatId"),(WORD, "wLength"),(BOOLEAN, "fClear"),(UCHAR, "fReserved"),]

    

class DNSSRV_STAT(NdrStructure):
    MEMBERS = [(DNSSRV_STAT_HEADER, "Header"),(BYTE, "Buffer"),]

    

class IP4_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "AddrCount"),(DWORD, "AddrArray"),]

    

class DNS_ADDR(NdrStructure):
    MEMBERS = [(CHAR, "MaxSa"),(DWORD, "DnsAddrUserDword"),]

    

class DNS_ADDR_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "MaxCount"),(DWORD, "AddrCount"),(DWORD, "Tag"),(WORD, "Family"),(WORD, "WordReserved"),(DWORD, "Flags"),(DWORD, "MatchFlag"),(DWORD, "Reserved1"),(DWORD, "Reserved2"),(DNS_ADDR, "AddrArray"),]

    

class DNS_RPC_BUFFER(NdrStructure):
    MEMBERS = [(DWORD, "dwLength"),(BYTE, "Buffer"),]

    

class DNS_RPC_SERVER_INFO_W2K(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(UCHAR, "fBootMethod"),(BOOLEAN, "fAdminConfigured"),(BOOLEAN, "fAllowUpdate"),(BOOLEAN, "fDsAvailable"),(PCHAR, "pszServerName"),(PWCHAR_T, "pszDsContainer"),(PIP4_ARRAY, "aipServerAddrs"),(PIP4_ARRAY, "aipListenAddrs"),(PIP4_ARRAY, "aipForwarders"),(PDWORD, "pExtension1"),(PDWORD, "pExtension2"),(PDWORD, "pExtension3"),(PDWORD, "pExtension4"),(PDWORD, "pExtension5"),(DWORD, "dwLogLevel"),(DWORD, "dwDebugLevel"),(DWORD, "dwForwardTimeout"),(DWORD, "dwRpcProtocol"),(DWORD, "dwNameCheckFlag"),(DWORD, "cAddressAnswerLimit"),(DWORD, "dwRecursionRetry"),(DWORD, "dwRecursionTimeout"),(DWORD, "dwMaxCacheTtl"),(DWORD, "dwDsPollingInterval"),(DWORD, "dwScavengingInterval"),(DWORD, "dwDefaultRefreshInterval"),(DWORD, "dwDefaultNoRefreshInterval"),(DWORD, "dwReserveArray"),(BOOLEAN, "fAutoReverseZones"),(BOOLEAN, "fAutoCacheUpdate"),(BOOLEAN, "fRecurseAfterForwarding"),(BOOLEAN, "fForwardDelegations"),(BOOLEAN, "fNoRecursion"),(BOOLEAN, "fSecureResponses"),(BOOLEAN, "fRoundRobin"),(BOOLEAN, "fLocalNetPriority"),(BOOLEAN, "fBindSecondaries"),(BOOLEAN, "fWriteAuthorityNs"),(BOOLEAN, "fStrictFileParsing"),(BOOLEAN, "fLooseWildcarding"),(BOOLEAN, "fDefaultAgingState"),(BOOLEAN, "fReserveArray"),]

    

class DNS_RPC_SERVER_INFO_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwVersion"),(UCHAR, "fBootMethod"),(BOOLEAN, "fAdminConfigured"),(BOOLEAN, "fAllowUpdate"),(BOOLEAN, "fDsAvailable"),(PCHAR, "pszServerName"),(PWCHAR_T, "pszDsContainer"),(PIP4_ARRAY, "aipServerAddrs"),(PIP4_ARRAY, "aipListenAddrs"),(PIP4_ARRAY, "aipForwarders"),(PIP4_ARRAY, "aipLogFilter"),(PWCHAR_T, "pwszLogFilePath"),(PCHAR, "pszDomainName"),(PCHAR, "pszForestName"),(PCHAR, "pszDomainDirectoryPartition"),(PCHAR, "pszForestDirectoryPartition"),(PCHAR, "pExtensions"),(DWORD, "dwLogLevel"),(DWORD, "dwDebugLevel"),(DWORD, "dwForwardTimeout"),(DWORD, "dwRpcProtocol"),(DWORD, "dwNameCheckFlag"),(DWORD, "cAddressAnswerLimit"),(DWORD, "dwRecursionRetry"),(DWORD, "dwRecursionTimeout"),(DWORD, "dwMaxCacheTtl"),(DWORD, "dwDsPollingInterval"),(DWORD, "dwLocalNetPriorityNetMask"),(DWORD, "dwScavengingInterval"),(DWORD, "dwDefaultRefreshInterval"),(DWORD, "dwDefaultNoRefreshInterval"),(DWORD, "dwLastScavengeTime"),(DWORD, "dwEventLogLevel"),(DWORD, "dwLogFileMaxSize"),(DWORD, "dwDsForestVersion"),(DWORD, "dwDsDomainVersion"),(DWORD, "dwDsDsaVersion"),(DWORD, "dwReserveArray"),(BOOLEAN, "fAutoReverseZones"),(BOOLEAN, "fAutoCacheUpdate"),(BOOLEAN, "fRecurseAfterForwarding"),(BOOLEAN, "fForwardDelegations"),(BOOLEAN, "fNoRecursion"),(BOOLEAN, "fSecureResponses"),(BOOLEAN, "fRoundRobin"),(BOOLEAN, "fLocalNetPriority"),(BOOLEAN, "fBindSecondaries"),(BOOLEAN, "fWriteAuthorityNs"),(BOOLEAN, "fStrictFileParsing"),(BOOLEAN, "fLooseWildcarding"),(BOOLEAN, "fDefaultAgingState"),(BOOLEAN, "fReserveArray"),]

    

class DNS_RPC_SERVER_INFO_LONGHORN(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwVersion"),(UCHAR, "fBootMethod"),(BOOLEAN, "fAdminConfigured"),(BOOLEAN, "fAllowUpdate"),(BOOLEAN, "fDsAvailable"),(PCHAR, "pszServerName"),(PWCHAR_T, "pszDsContainer"),(PDNS_ADDR_ARRAY, "aipServerAddrs"),(PDNS_ADDR_ARRAY, "aipListenAddrs"),(PDNS_ADDR_ARRAY, "aipForwarders"),(PDNS_ADDR_ARRAY, "aipLogFilter"),(PWCHAR_T, "pwszLogFilePath"),(PCHAR, "pszDomainName"),(PCHAR, "pszForestName"),(PCHAR, "pszDomainDirectoryPartition"),(PCHAR, "pszForestDirectoryPartition"),(PCHAR, "pExtensions"),(DWORD, "dwLogLevel"),(DWORD, "dwDebugLevel"),(DWORD, "dwForwardTimeout"),(DWORD, "dwRpcProtocol"),(DWORD, "dwNameCheckFlag"),(DWORD, "cAddressAnswerLimit"),(DWORD, "dwRecursionRetry"),(DWORD, "dwRecursionTimeout"),(DWORD, "dwMaxCacheTtl"),(DWORD, "dwDsPollingInterval"),(DWORD, "dwLocalNetPriorityNetMask"),(DWORD, "dwScavengingInterval"),(DWORD, "dwDefaultRefreshInterval"),(DWORD, "dwDefaultNoRefreshInterval"),(DWORD, "dwLastScavengeTime"),(DWORD, "dwEventLogLevel"),(DWORD, "dwLogFileMaxSize"),(DWORD, "dwDsForestVersion"),(DWORD, "dwDsDomainVersion"),(DWORD, "dwDsDsaVersion"),(BOOLEAN, "fReadOnlyDC"),(DWORD, "dwReserveArray"),(BOOLEAN, "fAutoReverseZones"),(BOOLEAN, "fAutoCacheUpdate"),(BOOLEAN, "fRecurseAfterForwarding"),(BOOLEAN, "fForwardDelegations"),(BOOLEAN, "fNoRecursion"),(BOOLEAN, "fSecureResponses"),(BOOLEAN, "fRoundRobin"),(BOOLEAN, "fLocalNetPriority"),(BOOLEAN, "fBindSecondaries"),(BOOLEAN, "fWriteAuthorityNs"),(BOOLEAN, "fStrictFileParsing"),(BOOLEAN, "fLooseWildcarding"),(BOOLEAN, "fDefaultAgingState"),(BOOLEAN, "fReserveArray"),]

    

class DNS_RPC_FORWARDERS_W2K(NdrStructure):
    MEMBERS = [(DWORD, "fRecurseAfterForwarding"),(DWORD, "dwForwardTimeout"),(PIP4_ARRAY, "aipForwarders"),]

    

class DNS_RPC_FORWARDERS_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fRecurseAfterForwarding"),(DWORD, "dwForwardTimeout"),(PIP4_ARRAY, "aipForwarders"),]

    

class DNS_RPC_FORWARDERS_LONGHORN(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fRecurseAfterForwarding"),(DWORD, "dwForwardTimeout"),(PDNS_ADDR_ARRAY, "aipForwarders"),]

    

class DNS_RPC_ZONE_W2K(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszZoneName"),(DNS_RPC_ZONE_FLAGS, "Flags"),(UCHAR, "ZoneType"),(UCHAR, "Version"),]

    

class DNS_RPC_ZONE_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PWCHAR_T, "pszZoneName"),(DNS_RPC_ZONE_FLAGS, "Flags"),(UCHAR, "ZoneType"),(UCHAR, "Version"),(DWORD, "dwDpFlags"),(PCHAR, "pszDpFqdn"),]

    

class DNS_RPC_ZONE_LIST_W2K(NdrStructure):
    MEMBERS = [(DWORD, "dwZoneCount"),(PDNS_RPC_ZONE_W2K, "ZoneArray"),]

    

class DNS_RPC_ZONE_LIST_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwZoneCount"),(PDNS_RPC_ZONE_DOTNET, "ZoneArray"),]

    

class DNS_RPC_TRUST_POINT(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszTrustPointName"),(TRUSTPOINT_STATE, "eTrustPointState"),(__INT64, "i64LastActiveRefreshTime"),(__INT64, "i64NextActiveRefreshTime"),(__INT64, "i64LastSuccessfulActiveRefreshTime"),(DWORD, "dwLastActiveRefreshResult"),(DWORD, "dwReserved"),]

    

class DNS_RPC_TRUST_POINT_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwTrustPointCount"),(PDNS_RPC_TRUST_POINT, "TrustPointArray"),]

    

class DNS_RPC_SKD(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(GUID, "Guid"),(PWCHAR_T, "pwszKeyStorageProvider"),(BOOL, "fStoreKeysInDirectory"),(BOOL, "fIsKSK"),(BYTE, "bSigningAlgorithm"),(DWORD, "dwKeyLength"),(DWORD, "dwInitialRolloverOffset"),(DWORD, "dwDNSKEYSignatureValidityPeriod"),(DWORD, "dwDSSignatureValidityPeriod"),(DWORD, "dwStandardSignatureValidityPeriod"),(DWORD, "dwRolloverType"),(DWORD, "dwRolloverPeriod"),(DWORD, "dwNextRolloverAction"),(DWORD, "dwReserved"),]

    

class DNS_RPC_SKD_STATE_EX(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(GUID, "Guid"),(DWORD, "dwCurrentRollState"),(DWORD, "fManualTrigger"),(DWORD, "dwPreRollEventFired"),(FILETIME, "ftNextKeyGenerationTime"),(DWORD, "dwRevokedOrSwappedDnskeysLength"),(PBYTE, "pRevokedOrSwappedDnskeysBuffer"),(DWORD, "dwFinalDnskeysLength"),(PBYTE, "pFinalDnskeys"),(KEYSIGNSCOPE, "eActiveKeyScope"),(KEYSIGNSCOPE, "eStandByKeyScope"),(KEYSIGNSCOPE, "eNextKeyScope"),]

    

class DNS_RPC_SKD_STATE(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(GUID, "Guid"),(FILETIME, "ftLastRolloverTime"),(FILETIME, "ftNextRolloverTime"),(DWORD, "dwState"),(DWORD, "dwCurrentRolloverStatus"),(PWCHAR_T, "pwszActiveKey"),(PWCHAR_T, "pwszStandbyKey"),(PWCHAR_T, "pwszNextKey"),(DWORD, "dwReserved"),]

    

class DNS_RPC_ZONE_SKD(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PDNS_RPC_SKD, "pSkd"),(PDNS_RPC_SKD_STATE, "pSkdState"),(PDNS_RPC_SKD_STATE_EX, "pSkdStateEx"),]

    

class DNS_RPC_ZONE_DNSSEC_SETTINGS(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fIsSigned"),(DWORD, "fSignWithNSEC3"),(DWORD, "fNSEC3OptOut"),(DWORD, "dwMaintainTrustAnchor"),(DWORD, "fParentHasSecureDelegation"),(DWORD, "dwDSRecordAlgorithms"),(DWORD, "fRFC5011KeyRollovers"),(BYTE, "bNSEC3HashAlgorithm"),(BYTE, "bNSEC3RandomSaltLength"),(WORD, "wNSEC3IterationCount"),(LPWSTR, "pwszNSEC3UserSalt"),(DWORD, "dwDNSKEYRecordSetTtl"),(DWORD, "dwDSRecordSetTtl"),(DWORD, "dwSignatureInceptionOffset"),(DWORD, "dwSecureDelegationPollingPeriod"),(DWORD, "dwPropagationTime"),(DWORD, "cbNSEC3CurrentSaltLength"),(PBYTE, "pbNSEC3CurrentSalt"),(GUID, "CurrentRollingSKDGuid"),(DWORD, "dwBufferLength"),(PBYTE, "pBuffer"),(DWORD, "dwCount"),(PDNS_RPC_ZONE_SKD, "pZoneSkdArray"),]

    

class DNS_RPC_TRUST_ANCHOR(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(WORD, "wTrustAnchorType"),(WORD, "wKeyTag"),(WORD, "wRRLength"),(TRUSTANCHOR_STATE, "eTrustAnchorState"),(__INT64, "i64EnteredStateTime"),(__INT64, "i64NextStateTime"),(DWORD, "dwReserved"),(BYTE, "RRData"),]

    

class DNS_RPC_TRUST_ANCHOR_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwTrustAnchorCount"),(PDNS_RPC_TRUST_ANCHOR, "TrustAnchorArray"),]

    

class DNS_RPC_DP_ENUM(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszDpFqdn"),(DWORD, "dwFlags"),(DWORD, "dwZoneCount"),]

    

class DNS_RPC_DP_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwDpCount"),(PDNS_RPC_DP_ENUM, "DpArray"),]

    

class DNS_RPC_DP_REPLICA(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszReplicaDn"),]

    

class DNS_RPC_DP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszDpFqdn"),(PWCHAR_T, "pszDpDn"),(PWCHAR_T, "pszCrDn"),(DWORD, "dwFlags"),(DWORD, "dwZoneCount"),(DWORD, "dwState"),(DWORD, "dwReserved"),(PWCHAR_T, "pwszReserved"),(DWORD, "dwReplicaCount"),(PDNS_RPC_DP_REPLICA, "ReplicaArray"),]

    

class DNS_RPC_ENLIST_DP(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszDpFqdn"),(DWORD, "dwOperation"),]

    

class DNS_RPC_ZONE_EXPORT_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszZoneExportFile"),]

    

class DNS_RPC_ZONE_SECONDARIES_W2K(NdrStructure):
    MEMBERS = [(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PIP4_ARRAY, "aipSecondaries"),(PIP4_ARRAY, "aipNotify"),]

    

class DNS_RPC_ZONE_SECONDARIES_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PIP4_ARRAY, "aipSecondaries"),(PIP4_ARRAY, "aipNotify"),]

    

class DNS_RPC_ZONE_SECONDARIES_LONGHORN(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PDNS_ADDR_ARRAY, "aipSecondaries"),(PDNS_ADDR_ARRAY, "aipNotify"),]

    

class DNS_RPC_ZONE_DATABASE_W2K(NdrStructure):
    MEMBERS = [(DWORD, "fDsIntegrated"),(PCHAR, "pszFileName"),]

    

class DNS_RPC_ZONE_DATABASE_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "fDsIntegrated"),(PCHAR, "pszFileName"),]

    

class DNS_RPC_ZONE_CHANGE_DP(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszDestPartition"),]

    

class DNS_RPC_ZONE_INFO_W2K(NdrStructure):
    MEMBERS = [(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fReverse"),(DWORD, "fAllowUpdate"),(DWORD, "fPaused"),(DWORD, "fShutdown"),(DWORD, "fAutoCreated"),(DWORD, "fUseDatabase"),(PCHAR, "pszDataFile"),(PIP4_ARRAY, "aipMasters"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PIP4_ARRAY, "aipSecondaries"),(PIP4_ARRAY, "aipNotify"),(DWORD, "fUseWins"),(DWORD, "fUseNbstat"),(DWORD, "fAging"),(DWORD, "dwNoRefreshInterval"),(DWORD, "dwRefreshInterval"),(DWORD, "dwAvailForScavengeTime"),(PIP4_ARRAY, "aipScavengeServers"),(DWORD, "pvReserved1"),(DWORD, "pvReserved2"),(DWORD, "pvReserved3"),(DWORD, "pvReserved4"),]

    

class DNS_RPC_ZONE_INFO_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fReverse"),(DWORD, "fAllowUpdate"),(DWORD, "fPaused"),(DWORD, "fShutdown"),(DWORD, "fAutoCreated"),(DWORD, "fUseDatabase"),(PCHAR, "pszDataFile"),(PIP4_ARRAY, "aipMasters"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PIP4_ARRAY, "aipSecondaries"),(PIP4_ARRAY, "aipNotify"),(DWORD, "fUseWins"),(DWORD, "fUseNbstat"),(DWORD, "fAging"),(DWORD, "dwNoRefreshInterval"),(DWORD, "dwRefreshInterval"),(DWORD, "dwAvailForScavengeTime"),(PIP4_ARRAY, "aipScavengeServers"),(DWORD, "dwForwarderTimeout"),(DWORD, "fForwarderSlave"),(PIP4_ARRAY, "aipLocalMasters"),(DWORD, "dwDpFlags"),(PCHAR, "pszDpFqdn"),(PWCHAR_T, "pwszZoneDn"),(DWORD, "dwLastSuccessfulSoaCheck"),(DWORD, "dwLastSuccessfulXfr"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(DWORD, "dwReserved3"),(DWORD, "dwReserved4"),(DWORD, "dwReserved5"),(PCHAR, "pReserved1"),(PCHAR, "pReserved2"),(PCHAR, "pReserved3"),(PCHAR, "pReserved4"),]

    

class DNS_RPC_ZONE_INFO_LONGHORN(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fReverse"),(DWORD, "fAllowUpdate"),(DWORD, "fPaused"),(DWORD, "fShutdown"),(DWORD, "fAutoCreated"),(DWORD, "fUseDatabase"),(PCHAR, "pszDataFile"),(PDNS_ADDR_ARRAY, "aipMasters"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PDNS_ADDR_ARRAY, "aipSecondaries"),(PDNS_ADDR_ARRAY, "aipNotify"),(DWORD, "fUseWins"),(DWORD, "fUseNbstat"),(DWORD, "fAging"),(DWORD, "dwNoRefreshInterval"),(DWORD, "dwRefreshInterval"),(DWORD, "dwAvailForScavengeTime"),(PDNS_ADDR_ARRAY, "aipScavengeServers"),(DWORD, "dwForwarderTimeout"),(DWORD, "fForwarderSlave"),(PDNS_ADDR_ARRAY, "aipLocalMasters"),(DWORD, "dwDpFlags"),(PCHAR, "pszDpFqdn"),(PWCHAR_T, "pwszZoneDn"),(DWORD, "dwLastSuccessfulSoaCheck"),(DWORD, "dwLastSuccessfulXfr"),(DWORD, "fQueuedForBackgroundLoad"),(DWORD, "fBackgroundLoadInProgress"),(BOOL, "fReadOnlyZone"),(DWORD, "dwLastXfrAttempt"),(DWORD, "dwLastXfrResult"),]

    

class DNS_RPC_ZONE_CREATE_INFO_W2K(NdrStructure):
    MEMBERS = [(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fAllowUpdate"),(DWORD, "fAging"),(DWORD, "dwFlags"),(PCHAR, "pszDataFile"),(DWORD, "fDsIntegrated"),(DWORD, "fLoadExisting"),(PCHAR, "pszAdmin"),(PIP4_ARRAY, "aipMasters"),(PIP4_ARRAY, "aipSecondaries"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(PCHAR, "pvReserved1"),(PCHAR, "pvReserved2"),(PCHAR, "pvReserved3"),(PCHAR, "pvReserved4"),(PCHAR, "pvReserved5"),(PCHAR, "pvReserved6"),(PCHAR, "pvReserved7"),(PCHAR, "pvReserved8"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(DWORD, "dwReserved3"),(DWORD, "dwReserved4"),(DWORD, "dwReserved5"),(DWORD, "dwReserved6"),(DWORD, "dwReserved7"),(DWORD, "dwReserved8"),]

    

class DNS_RPC_ZONE_CREATE_INFO_DOTNET(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fAllowUpdate"),(DWORD, "fAging"),(DWORD, "dwFlags"),(PCHAR, "pszDataFile"),(DWORD, "fDsIntegrated"),(DWORD, "fLoadExisting"),(PCHAR, "pszAdmin"),(PIP4_ARRAY, "aipMasters"),(PIP4_ARRAY, "aipSecondaries"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(DWORD, "dwTimeout"),(DWORD, "fRecurseAfterForwarding"),(DWORD, "dwDpFlags"),(PCHAR, "pszDpFqdn"),(DWORD, "dwReserved"),]

    

class DNS_RPC_ZONE_CREATE_INFO_LONGHORN(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(PCHAR, "pszZoneName"),(DWORD, "dwZoneType"),(DWORD, "fAllowUpdate"),(DWORD, "fAging"),(DWORD, "dwFlags"),(PCHAR, "pszDataFile"),(DWORD, "fDsIntegrated"),(DWORD, "fLoadExisting"),(PCHAR, "pszAdmin"),(PDNS_ADDR_ARRAY, "aipMasters"),(PDNS_ADDR_ARRAY, "aipSecondaries"),(DWORD, "fSecureSecondaries"),(DWORD, "fNotifyLevel"),(DWORD, "dwTimeout"),(DWORD, "fRecurseAfterForwarding"),(DWORD, "dwDpFlags"),(PCHAR, "pszDpFqdn"),(DWORD, "dwReserved"),]

    

class DNS_RPC_SKD_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwCount"),(PDNS_RPC_SKD, "SkdArray"),]

    

class DNS_RPC_SIGNING_VALIDATION_ERROR(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(GUID, "guidSKD"),(PWCHAR_T, "pwszSigningKeyPointerString"),(DWORD, "dwExtendedError"),(DWORD, "dwReserved"),]

    

class DNS_RPC_AUTOCONFIGURE(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwAutoConfigFlags"),(DWORD, "dwReserved1"),(PCHAR, "pszNewDomainName"),]

    

class DNS_RPC_ENUM_ZONES_FILTER(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwFilter"),(PCHAR, "pszPartitionFqdn"),(PCHAR, "pszQueryString"),(PCHAR, "pszReserved"),]

    

class DNS_RPC_RECORD(NdrStructure):
    MEMBERS = [(WORD, "wDataLength"),(WORD, "wType"),(DWORD, "dwFlags"),(DWORD, "dwSerial"),(DWORD, "dwTtlSeconds"),(DWORD, "dwTimeStamp"),(DWORD, "dwReserved"),(BYTE, "Buffer"),]

    

class DNS_RPC_NAME_AND_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "dwParam"),(PCHAR, "pszNodeName"),]

    

class DNS_RPC_IP_VALIDATE(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved0"),(DWORD, "dwContext"),(DWORD, "dwReserved1"),(PCHAR, "pszContextName"),(PDNS_ADDR_ARRAY, "aipValidateAddrs"),]

    

class DNS_RPC_UTF8_STRING_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwCount"),(PCHAR, "pszStrings"),]

    

class DNS_RPC_UNICODE_STRING_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwCount"),(PWCHAR_T, "pwszStrings"),]

    

class DNS_RPC_CLIENT_SUBNET_RECORD(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszClientSubnetName"),(PDNS_ADDR_ARRAY, "pIPAddr"),(PDNS_ADDR_ARRAY, "pIPv6Addr"),]

    

class DNS_RPC_POLICY_CONTENT(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszScopeName"),(DWORD, "dwWeight"),]

    

class DNS_RPC_POLICY_CONTENT_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwContentCount"),(PDNS_RPC_POLICY_CONTENT, "pContent"),]

    

class DNS_RPC_CRITERIA(NdrStructure):
    MEMBERS = [(DNS_RPC_CRITERIA_ENUM, "type"),(LPWSTR, "pCriteria"),]

    

class DNS_RPC_POLICY(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszPolicyName"),(DNS_RPC_POLICY_LEVEL, "level"),(DNS_RPC_POLICY_TYPE, "appliesOn"),(DNS_RPC_POLICY_ACTION_TYPE, "action"),(DNS_RPC_POLICY_CONDITION, "condition"),(BOOL, "isEnabled"),(DWORD, "dwProcessingOrder"),(LPSTR, "pszZoneName"),(PDNS_RPC_POLICY_CONTENT_LIST, "pContentList"),(DWORDLONG, "flags"),(DWORD, "dwCriteriaCount"),(PDNS_RPC_CRITERIA, "pCriteriaList"),]

    

class DNS_RPC_POLICY_NAME(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszPolicyName"),(DNS_RPC_POLICY_TYPE, "appliesOn"),(BOOL, "fEnabled"),(DWORD, "processingOrder"),]

    

class DNS_RPC_ENUMERATE_POLICY_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwPolicyCount"),(PDNS_RPC_POLICY_NAME, "pPolicyArray"),]

    

class DNS_RPC_RRL_PARAMS(NdrStructure):
    MEMBERS = [(DWORD, "dwResponsesPerSecond"),(DWORD, "dwErrorsPerSecond"),(DWORD, "dwLeakRate"),(DWORD, "dwTCRate"),(DWORD, "dwTotalResponsesInWindow"),(DWORD, "dwWindowSize"),(DWORD, "dwIPv4PrefixLength"),(DWORD, "dwIPv6PrefixLength"),(DNS_RRL_MODE_ENUM, "eMode"),(DWORD, "dwFlags"),(BOOL, "fSetDefault"),]

    

class DNS_RPC_VIRTUALIZATION_INSTANCE(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwReserved"),(DWORD, "dwFlags"),(LPWSTR, "pwszVirtualizationID"),(LPWSTR, "pwszFriendlyName"),(LPWSTR, "pwszDescription"),]

    

class DNS_RPC_VIRTUALIZATION_INSTANCE_INFO(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszVirtualizationID"),(LPWSTR, "pwszFriendlyName"),(LPWSTR, "pwszDescription"),]

    

class DNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwVirtualizationInstanceCount"),(PDNS_RPC_VIRTUALIZATION_INSTANCE_INFO, "VirtualizationInstanceArray"),]

    

class DNS_RPC_ENUM_ZONE_SCOPE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwZoneScopeCount"),(LPWSTR, "ZoneScopeArray"),]

    

class DNS_SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    

class DNSSRV_ZONE_TIME_STATS(NdrStructure):
    MEMBERS = [(DNS_SYSTEMTIME, "StatsCollectionStartTime"),]

    

class DNSSRV_ZONE_QUERY_STATS(NdrStructure):
    MEMBERS = [(DNS_ZONE_STATS_TYPE, "RecordType"),(ULONG64, "QueriesResponded"),(ULONG64, "QueriesReceived"),(ULONG64, "QueriesFailure"),(ULONG64, "QueriesNameError"),]

    

class DNSSRV_RRL_STATS(NdrStructure):
    MEMBERS = [(DNSSRV_STAT_HEADER, "Header"),(DWORD, "TotalResponsesSent"),(DWORD, "TotalResponsesDropped"),(DWORD, "TotalResponsesTruncated"),(DWORD, "TotalResponsesLeaked"),]

    

class DNSSRV_ZONE_TRANSFER_STATS(NdrStructure):
    MEMBERS = [(DNS_ZONE_STATS_TYPE, "TransferType"),(ULONG64, "RequestReceived"),(ULONG64, "RequestSent"),(ULONG64, "ResponseReceived"),(ULONG64, "SuccessReceived"),(ULONG64, "SuccessSent"),]

    

class DNSSRV_ZONE_UPDATE_STATS(NdrStructure):
    MEMBERS = [(DNS_ZONE_STATS_TYPE, "Type"),(ULONG64, "DynamicUpdateReceived"),(ULONG64, "DynamicUpdateRejected"),]

    

class DNSSRV_ZONE_RRL_STATS(NdrStructure):
    MEMBERS = [(DNS_ZONE_STATS_TYPE, "Type"),(DWORD, "TotalResponsesSent"),(DWORD, "TotalResponsesDropped"),(DWORD, "TotalResponsesTruncated"),(DWORD, "TotalResponsesLeaked"),]

    

class DNS_RPC_ZONE_STATS_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DNSSRV_ZONE_TIME_STATS, "ZoneTimeStats"),(DNSSRV_ZONE_QUERY_STATS, "ZoneQueryStats"),(DNSSRV_ZONE_TRANSFER_STATS, "ZoneTransferStats"),(DNSSRV_ZONE_UPDATE_STATS, "ZoneUpdateStats"),(DNSSRV_ZONE_RRL_STATS, "ZoneRRLStats"),]

    

class DNS_RPC_ZONE_SCOPE_CREATE_INFO_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwFlags"),(LPWSTR, "pwszScopeName"),]

    

class DNS_RPC_ZONE_SCOPE_INFO_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(LPWSTR, "pwszScopeName"),(LPWSTR, "pwszDataFile"),]

    

class DNS_RPC_ENUM_SCOPE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "dwRpcStructureVersion"),(DWORD, "dwScopeCount"),(LPWSTR, "ScopeArray"),]

    

class DNSSRV_RPC_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PBYTE, "Null"),2 : (DWORD, "Dword"),3 : (PCHAR, "String"),4 : (PWCHAR_T, "WideString"),5 : (PIP4_ARRAY, "IpArray"),6 : (PDNS_RPC_BUFFER, "Buffer"),7 : (PDNS_RPC_SERVER_INFO_W2K, "ServerInfoW2K"),8 : (PDNSSRV_STATS, "Stats"),9 : (PDNS_RPC_FORWARDERS_W2K, "ForwardersW2K"),10 : (PDNS_RPC_ZONE_W2K, "ZoneW2K"),11 : (PDNS_RPC_ZONE_INFO_W2K, "ZoneInfoW2K"),12 : (PDNS_RPC_ZONE_SECONDARIES_W2K, "SecondariesW2K"),13 : (PDNS_RPC_ZONE_DATABASE_W2K, "DatabaseW2K"),14 : (PDNS_RPC_ZONE_CREATE_INFO_W2K, "ZoneCreateW2K"),15 : (PDNS_RPC_NAME_AND_PARAM, "NameAndParam"),16 : (PDNS_RPC_ZONE_LIST_W2K, "ZoneListW2K"),17 : (PDNS_RPC_SERVER_INFO_DOTNET, "ServerInfoDotNet"),18 : (PDNS_RPC_FORWARDERS_DOTNET, "ForwardersDotNet"),19 : (PDNS_RPC_ZONE, "Zone"),20 : (PDNS_RPC_ZONE_INFO_DOTNET, "ZoneInfoDotNet"),21 : (PDNS_RPC_ZONE_SECONDARIES_DOTNET, "SecondariesDotNet"),22 : (PDNS_RPC_ZONE_DATABASE, "Database"),23 : (PDNS_RPC_ZONE_CREATE_INFO_DOTNET, "ZoneCreateDotNet"),24 : (PDNS_RPC_ZONE_LIST, "ZoneList"),25 : (PDNS_RPC_ZONE_EXPORT_INFO, "ZoneExport"),26 : (PDNS_RPC_DP_INFO, "DirectoryPartition"),27 : (PDNS_RPC_DP_ENUM, "DirectoryPartitionEnum"),28 : (PDNS_RPC_DP_LIST, "DirectoryPartitionList"),29 : (PDNS_RPC_ENLIST_DP, "EnlistDirectoryPartition"),30 : (PDNS_RPC_ZONE_CHANGE_DP, "ZoneChangeDirectoryPartition"),31 : (PDNS_RPC_ENUM_ZONES_FILTER, "EnumZonesFilter"),32 : (PDNS_ADDR_ARRAY, "AddrArray"),33 : (PDNS_RPC_SERVER_INFO, "ServerInfo"),34 : (PDNS_RPC_ZONE_CREATE_INFO, "ZoneCreate"),35 : (PDNS_RPC_FORWARDERS, "Forwarders"),36 : (PDNS_RPC_ZONE_SECONDARIES, "Secondaries"),37 : (PDNS_RPC_IP_VALIDATE, "IpValidate"),38 : (PDNS_RPC_ZONE_INFO, "ZoneInfo"),39 : (PDNS_RPC_AUTOCONFIGURE, "AutoConfigure"),40 : (PDNS_RPC_UTF8_STRING_LIST, "Utf8StringList"),41 : (PDNS_RPC_UNICODE_STRING_LIST, "UnicodeStringList"),42 : (PDNS_RPC_SKD, "Skd"),43 : (PDNS_RPC_SKD_LIST, "SkdList"),44 : (PDNS_RPC_SKD_STATE, "SkdState"),45 : (PDNS_RPC_SIGNING_VALIDATION_ERROR, "SigningValidationError"),46 : (PDNS_RPC_TRUST_POINT_LIST, "TrustPointList"),47 : (PDNS_RPC_TRUST_ANCHOR_LIST, "TrustAnchorList"),48 : (PDNS_RPC_ZONE_DNSSEC_SETTINGS, "ZoneDnsSecSettings"),49 : (PDNS_RPC_ENUM_ZONE_SCOPE_LIST, "ZoneScopeList"),50 : (PDNS_RPC_ZONE_STATS_V1, "ZoneStats"),51 : (PDNS_RPC_ZONE_SCOPE_CREATE_INFO_V1, "ScopeCreate"),52 : (PDNS_RPC_ZONE_SCOPE_INFO_V1, "ScopeInfo"),53 : (PDNS_RPC_ENUM_SCOPE_LIST, "ScopeList"),54 : (PDNS_RPC_CLIENT_SUBNET_RECORD, "SubnetList"),55 : (PDNS_RPC_POLICY, "pPolicy"),56 : (PDNS_RPC_POLICY_NAME, "pPolicyName"),57 : (PDNS_RPC_ENUMERATE_POLICY_LIST, "pPolicyList"),58 : (PDNS_RPC_RRL_PARAMS, "pRRLParams"),59 : (PDNS_RPC_VIRTUALIZATION_INSTANCE, "VirtualizationInstance"),60 : (PDNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST, "VirtualizationInstanceList"),}

    
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