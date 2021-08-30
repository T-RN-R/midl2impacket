
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

    
Method("NetrLogonUasLogon",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
Out(PPNETLOGON_VALIDATION_UAS_INFO),
),Method("NetrLogonUasLogoff",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
Out(PNETLOGON_LOGOFF_UAS_INFO),
),Method("NetrLogonSamLogon",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(NETLOGON_LOGON_INFO_CLASS),
In(PNETLOGON_LEVEL),
In(NETLOGON_VALIDATION_INFO_CLASS),
Out(PNETLOGON_VALIDATION),
Out(PUCHAR),
),Method("NetrLogonSamLogoff",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(NETLOGON_LOGON_INFO_CLASS),
In(PNETLOGON_LEVEL),
),Method("NetrServerReqChallenge",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_CREDENTIAL),
Out(PNETLOGON_CREDENTIAL),
),Method("NetrServerAuthenticate",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_CREDENTIAL),
Out(PNETLOGON_CREDENTIAL),
),Method("NetrServerPasswordSet",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
In(PENCRYPTED_NT_OWF_PASSWORD),
),Method("NetrDatabaseDeltas",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
InOut(PNLPR_MODIFIED_COUNT),
Out(PPNETLOGON_DELTA_ENUM_ARRAY),
In(DWORD),
),Method("NetrDatabaseSync",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
InOut(PULONG),
Out(PPNETLOGON_DELTA_ENUM_ARRAY),
In(DWORD),
),Method("NetrAccountDeltas",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(PUAS_INFO_0),
In(DWORD),
In(DWORD),
Out(PUCHAR),
In(DWORD),
Out(PULONG),
Out(PULONG),
Out(PUAS_INFO_0),
),Method("NetrAccountSync",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
In(DWORD),
Out(PUCHAR),
In(DWORD),
Out(PULONG),
Out(PULONG),
Out(PULONG),
Out(PUAS_INFO_0),
),Method("NetrGetDCName",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
Out(PPWCHAR_T),
),Method("NetrLogonControl",
In(LOGONSRV_HANDLE),
In(DWORD),
In(DWORD),
Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
),Method("NetrGetAnyDCName",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
Out(PPWCHAR_T),
),Method("NetrLogonControl2",
In(LOGONSRV_HANDLE),
In(DWORD),
In(DWORD),
In(PNETLOGON_CONTROL_DATA_INFORMATION),
Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
),Method("NetrServerAuthenticate2",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_CREDENTIAL),
Out(PNETLOGON_CREDENTIAL),
InOut(PULONG),
),Method("NetrDatabaseSync2",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
In(SYNC_STATE),
InOut(PULONG),
Out(PPNETLOGON_DELTA_ENUM_ARRAY),
In(DWORD),
),Method("NetrDatabaseRedo",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(PUCHAR),
In(DWORD),
Out(PPNETLOGON_DELTA_ENUM_ARRAY),
),Method("NetrLogonControl2Ex",
In(LOGONSRV_HANDLE),
In(DWORD),
In(DWORD),
In(PNETLOGON_CONTROL_DATA_INFORMATION),
Out(PNETLOGON_CONTROL_QUERY_INFORMATION),
),Method("NetrEnumerateTrustedDomains",
In(LOGONSRV_HANDLE),
Out(PDOMAIN_NAME_BUFFER),
),Method("DsrGetDcName",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PGUID),
In(PGUID),
In(ULONG),
Out(PPDOMAIN_CONTROLLER_INFOW),
),Method("NetrLogonGetCapabilities",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
Out(PNETLOGON_CAPABILITIES),
),Method("NetrLogonSetServiceBits",
In(LOGONSRV_HANDLE),
In(DWORD),
In(DWORD),
),Method("NetrLogonGetTrustRid",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
Out(PULONG),
),Method("NetrLogonComputeServerDigest",
In(LOGONSRV_HANDLE),
In(ULONG),
In(PUCHAR),
In(ULONG),
Out(CHAR),
Out(CHAR),
),Method("NetrLogonComputeClientDigest",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PUCHAR),
In(ULONG),
Out(CHAR),
Out(CHAR),
),Method("NetrServerAuthenticate3",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_CREDENTIAL),
Out(PNETLOGON_CREDENTIAL),
InOut(PULONG),
Out(PULONG),
),Method("DsrGetDcNameEx",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PGUID),
In(PWCHAR_T),
In(ULONG),
Out(PPDOMAIN_CONTROLLER_INFOW),
),Method("DsrGetSiteName",
In(LOGONSRV_HANDLE),
Out(PPWCHAR_T),
),Method("NetrLogonGetDomainInfo",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
In(PNETLOGON_WORKSTATION_INFORMATION),
Out(PNETLOGON_DOMAIN_INFORMATION),
),Method("NetrServerPasswordSet2",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
In(PNL_TRUST_PASSWORD),
),Method("NetrServerPasswordGet",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
Out(PENCRYPTED_NT_OWF_PASSWORD),
),Method("NetrLogonSendToSam",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
In(PUCHAR),
In(ULONG),
),Method("DsrAddressToSiteNamesW",
In(LOGONSRV_HANDLE),
In(DWORD),
In(PNL_SOCKET_ADDRESS),
Out(PPNL_SITE_NAME_ARRAY),
),Method("DsrGetDcNameEx2",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(ULONG),
In(PWCHAR_T),
In(PGUID),
In(PWCHAR_T),
In(ULONG),
Out(PPDOMAIN_CONTROLLER_INFOW),
),Method("NetrLogonGetTimeServiceParentDomain",
In(LOGONSRV_HANDLE),
Out(PPWCHAR_T),
Out(PINT),
),Method("NetrEnumerateTrustedDomainsEx",
In(LOGONSRV_HANDLE),
Out(PNETLOGON_TRUSTED_DOMAIN_ARRAY),
),Method("DsrAddressToSiteNamesExW",
In(LOGONSRV_HANDLE),
In(DWORD),
In(PNL_SOCKET_ADDRESS),
Out(PPNL_SITE_NAME_EX_ARRAY),
),Method("DsrGetDcSiteCoverageW",
In(LOGONSRV_HANDLE),
Out(PPNL_SITE_NAME_ARRAY),
),Method("NetrLogonSamLogonEx",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(NETLOGON_LOGON_INFO_CLASS),
In(PNETLOGON_LEVEL),
In(NETLOGON_VALIDATION_INFO_CLASS),
Out(PNETLOGON_VALIDATION),
Out(PUCHAR),
InOut(PULONG),
),Method("DsrEnumerateDomainTrusts",
In(LOGONSRV_HANDLE),
In(ULONG),
Out(PNETLOGON_TRUSTED_DOMAIN_ARRAY),
),Method("DsrDeregisterDnsHostRecords",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PGUID),
In(PGUID),
In(PWCHAR_T),
),Method("NetrServerTrustPasswordsGet",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
Out(PENCRYPTED_NT_OWF_PASSWORD),
Out(PENCRYPTED_NT_OWF_PASSWORD),
),Method("DsrGetForestTrustInformation",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(DWORD),
Out(PPLSA_FOREST_TRUST_INFORMATION),
),Method("NetrGetForestTrustInformation",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
In(DWORD),
Out(PPLSA_FOREST_TRUST_INFORMATION),
),Method("NetrLogonSamLogonWithFlags",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(NETLOGON_LOGON_INFO_CLASS),
In(PNETLOGON_LEVEL),
In(NETLOGON_VALIDATION_INFO_CLASS),
Out(PNETLOGON_VALIDATION),
Out(PUCHAR),
InOut(PULONG),
),Method("NetrServerGetTrustInfo",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(NETLOGON_SECURE_CHANNEL_TYPE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
Out(PENCRYPTED_NT_OWF_PASSWORD),
Out(PENCRYPTED_NT_OWF_PASSWORD),
Out(PPNL_GENERIC_RPC_DATA),
),Method("OpnumUnused47",
In(),
),Method("DsrUpdateReadOnlyServerDnsRecords",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
Out(PNETLOGON_AUTHENTICATOR),
In(PWCHAR_T),
In(ULONG),
InOut(PNL_DNS_NAME_INFO_ARRAY),
),Method("NetrChainSetClientAttributes",
In(LOGONSRV_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
In(PNETLOGON_AUTHENTICATOR),
InOut(PNETLOGON_AUTHENTICATOR),
In(DWORD),
In(PNL_IN_CHAIN_SET_CLIENT_ATTRIBUTES),
InOut(PDWORD),
InOut(PNL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES),
),