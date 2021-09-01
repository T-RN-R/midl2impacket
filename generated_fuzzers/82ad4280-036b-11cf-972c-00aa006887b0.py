
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
INET_INFO_IMPERSONATE_HANDLE = LPWSTR

class INET_INFO_CAP_FLAGS(NdrStructure):
    MEMBERS = [(DWORD, "Flag"),(DWORD, "Mask"),]

    
LPINET_INFO_CAP_FLAGS = INET_INFO_CAP_FLAGS

class INET_INFO_CAPABILITIES_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "CapVersion"),(DWORD, "ProductType"),(DWORD, "MajorVersion"),(DWORD, "MinorVersion"),(DWORD, "BuildNumber"),(DWORD, "NumCapFlags"),(LPINET_INFO_CAP_FLAGS, "CapFlags"),]

    
LPINET_INFO_CAPABILITIES_STRUCT = INET_INFO_CAPABILITIES_STRUCT

class INET_LOG_CONFIGURATION(NdrStructure):
    MEMBERS = [(DWORD, "inetLogType"),(DWORD, "ilPeriod"),(WCHAR, "rgchLogFileDirectory"),(DWORD, "cbSizeForTruncation"),(WCHAR, "rgchDataSource"),(WCHAR, "rgchTableName"),(WCHAR, "rgchUserName"),(WCHAR, "rgchPassword"),]

    
LPINET_LOG_CONFIGURATION = INET_LOG_CONFIGURATION

class INET_INFO_IP_SEC_ENTRY(NdrStructure):
    MEMBERS = [(DWORD, "dwMask"),(DWORD, "dwNetwork"),]

    
LPINET_INFO_IP_SEC_ENTRY = INET_INFO_IP_SEC_ENTRY

class INET_INFO_IP_SEC_LIST(NdrStructure):
    MEMBERS = [(DWORD, "cEntries"),(INET_INFO_IP_SEC_ENTRY, "aIPSecEntry"),]

    
LPINET_INFO_IP_SEC_LIST = INET_INFO_IP_SEC_LIST

class INET_INFO_VIRTUAL_ROOT_ENTRY(NdrStructure):
    MEMBERS = [(LPWSTR, "pszRoot"),(LPWSTR, "pszAddress"),(LPWSTR, "pszDirectory"),(DWORD, "dwMask"),(LPWSTR, "pszAccountName"),(WCHAR, "AccountPassword"),(DWORD, "dwError"),]

    
LPINET_INFO_VIRTUAL_ROOT_ENTRY = INET_INFO_VIRTUAL_ROOT_ENTRY

class INET_INFO_VIRTUAL_ROOT_LIST(NdrStructure):
    MEMBERS = [(DWORD, "cEntries"),(INET_INFO_VIRTUAL_ROOT_ENTRY, "aVirtRootEntry"),]

    
LPINET_INFO_VIRTUAL_ROOT_LIST = INET_INFO_VIRTUAL_ROOT_LIST

class INET_INFO_CONFIG_INFO(NdrStructure):
    MEMBERS = [(DWORD, "FieldControl"),(DWORD, "dwConnectionTimeout"),(DWORD, "dwMaxConnections"),(LPWSTR, "lpszAdminName"),(LPWSTR, "lpszAdminEmail"),(LPWSTR, "lpszServerComment"),(LPINET_LOG_CONFIGURATION, "lpLogConfig"),(WORD, "LangId"),(LCID, "LocalId"),(BYTE, "ProductId"),(BOOL, "fLogAnonymous"),(BOOL, "fLogNonAnonymous"),(LPWSTR, "lpszAnonUserName"),(WCHAR, "szAnonPassword"),(DWORD, "dwAuthentication"),(SHORT, "sPort"),(LPINET_INFO_IP_SEC_LIST, "DenyIPList"),(LPINET_INFO_IP_SEC_LIST, "GrantIPList"),(LPINET_INFO_VIRTUAL_ROOT_LIST, "VirtualRoots"),]

    
LPINET_INFO_CONFIG_INFO = INET_INFO_CONFIG_INFO

class INET_INFO_SITE_ENTRY(NdrStructure):
    MEMBERS = [(LPWSTR, "pszComment"),(DWORD, "dwInstance"),]

    
LPINET_INFO_SITE_ENTRY = INET_INFO_SITE_ENTRY

class INET_INFO_SITE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "cEntries"),(INET_INFO_SITE_ENTRY, "aSiteEntry"),]

    
LPINET_INFO_SITE_LIST = INET_INFO_SITE_LIST

class INET_INFO_GLOBAL_CONFIG_INFO(NdrStructure):
    MEMBERS = [(DWORD, "FieldControl"),(DWORD, "BandwidthLevel"),(DWORD, "cbMemoryCacheSize"),]

    
LPINET_INFO_GLOBAL_CONFIG_INFO = INET_INFO_GLOBAL_CONFIG_INFO

class INETA_CACHE_STATISTICS(NdrStructure):
    MEMBERS = [(DWORD, "FilesCached"),(DWORD, "TotalFilesCached"),(DWORD, "FileHits"),(DWORD, "FileMisses"),(DWORD, "FileFlushes"),(DWORDLONG, "CurrentFileCacheSize"),(DWORDLONG, "MaximumFileCacheSize"),(DWORD, "FlushedEntries"),(DWORD, "TotalFlushed"),(DWORD, "URICached"),(DWORD, "TotalURICached"),(DWORD, "URIHits"),(DWORD, "URIMisses"),(DWORD, "URIFlushes"),(DWORD, "TotalURIFlushed"),(DWORD, "BlobCached"),(DWORD, "TotalBlobCached"),(DWORD, "BlobHits"),(DWORD, "BlobMisses"),(DWORD, "BlobFlushes"),(DWORD, "TotalBlobFlushed"),]

    
LPINETA_CACHE_STATISTICS = INETA_CACHE_STATISTICS

class INETA_ATQ_STATISTICS(NdrStructure):
    MEMBERS = [(DWORD, "TotalBlockedRequests"),(DWORD, "TotalRejectedRequests"),(DWORD, "TotalAllowedRequests"),(DWORD, "CurrentBlockedRequests"),(DWORD, "MeasuredBandwidth"),]

    
LPINETA_ATQ_STATISTICS = INETA_ATQ_STATISTICS

class INET_INFO_STATISTICS_0(NdrStructure):
    MEMBERS = [(INETA_CACHE_STATISTICS, "CacheCtrs"),(INETA_ATQ_STATISTICS, "AtqCtrs"),(DWORD, "nAuxCounters"),(DWORD, "rgCounters"),]

    
LPINET_INFO_STATISTICS_0 = INET_INFO_STATISTICS_0

class INET_INFO_STATISTICS_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPINET_INFO_STATISTICS_0, "InetStats0"),}

    
LPINET_INFO_STATISTICS_INFO = INET_INFO_STATISTICS_INFO

class W3_STATISTICS_1(NdrStructure):
    MEMBERS = [(LARGE_INTEGER, "TotalBytesSent"),(LARGE_INTEGER, "TotalBytesReceived"),(DWORD, "TotalFilesSent"),(DWORD, "TotalFilesReceived"),(DWORD, "CurrentAnonymousUsers"),(DWORD, "CurrentNonAnonymousUsers"),(DWORD, "TotalAnonymousUsers"),(DWORD, "TotalNonAnonymousUsers"),(DWORD, "MaxAnonymousUsers"),(DWORD, "MaxNonAnonymousUsers"),(DWORD, "CurrentConnections"),(DWORD, "MaxConnections"),(DWORD, "ConnectionAttempts"),(DWORD, "LogonAttempts"),(DWORD, "TotalOptions"),(DWORD, "TotalGets"),(DWORD, "TotalPosts"),(DWORD, "TotalHeads"),(DWORD, "TotalPuts"),(DWORD, "TotalDeletes"),(DWORD, "TotalTraces"),(DWORD, "TotalMove"),(DWORD, "TotalCopy"),(DWORD, "TotalMkcol"),(DWORD, "TotalPropfind"),(DWORD, "TotalProppatch"),(DWORD, "TotalSearch"),(DWORD, "TotalLock"),(DWORD, "TotalUnlock"),(DWORD, "TotalOthers"),(DWORD, "TotalCGIRequests"),(DWORD, "TotalBGIRequests"),(DWORD, "TotalNotFoundErrors"),(DWORD, "TotalLockedErrors"),(DWORD, "CurrentCalAuth"),(DWORD, "MaxCalAuth"),(DWORD, "TotalFailedCalAuth"),(DWORD, "CurrentCalSsl"),(DWORD, "MaxCalSsl"),(DWORD, "TotalFailedCalSsl"),(DWORD, "CurrentCGIRequests"),(DWORD, "CurrentBGIRequests"),(DWORD, "MaxCGIRequests"),(DWORD, "MaxBGIRequests"),(DWORD, "CurrentBlockedRequests"),(DWORD, "TotalBlockedRequests"),(DWORD, "TotalAllowedRequests"),(DWORD, "TotalRejectedRequests"),(DWORD, "MeasuredBw"),(DWORD, "ServiceUptime"),(DWORD, "TimeOfLastClear"),(DWORD, "nAuxCounters"),(DWORD, "rgCounters"),]

    
LPW3_STATISTICS_1 = W3_STATISTICS_1

class W3_STATISTICS_STRUCT(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPW3_STATISTICS_1, "StatInfo1"),}

    
LPW3_STATISTICS_STRUCT = W3_STATISTICS_STRUCT

class FTP_STATISTICS_0(NdrStructure):
    MEMBERS = [(LARGE_INTEGER, "TotalBytesSent"),(LARGE_INTEGER, "TotalBytesReceived"),(DWORD, "TotalFilesSent"),(DWORD, "TotalFilesReceived"),(DWORD, "CurrentAnonymousUsers"),(DWORD, "CurrentNonAnonymousUsers"),(DWORD, "TotalAnonymousUsers"),(DWORD, "TotalNonAnonymousUsers"),(DWORD, "MaxAnonymousUsers"),(DWORD, "MaxNonAnonymousUsers"),(DWORD, "CurrentConnections"),(DWORD, "MaxConnections"),(DWORD, "ConnectionAttempts"),(DWORD, "LogonAttempts"),(DWORD, "ServiceUptime"),(DWORD, "TotalAllowedRequests"),(DWORD, "TotalRejectedRequests"),(DWORD, "TotalBlockedRequests"),(DWORD, "CurrentBlockedRequests"),(DWORD, "MeasuredBandwidth"),(DWORD, "TimeOfLastClear"),]

    
LPFTP_STATISTICS_0 = FTP_STATISTICS_0

class FTP_STATISTICS_STRUCT(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPFTP_STATISTICS_0, "StatInfo0"),}

    
LPFTP_STATISTICS_STRUCT = FTP_STATISTICS_STRUCT

class IIS_USER_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "idUser"),(LPWSTR, "pszUser"),(BOOL, "fAnonymous"),(DWORD, "inetHost"),(DWORD, "tConnect"),]

    
LPIIS_USER_INFO_1 = IIS_USER_INFO_1

class IIS_USER_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPIIS_USER_INFO_1, "Buffer"),]

    
LPIIS_USER_INFO_1_CONTAINER = IIS_USER_INFO_1_CONTAINER

class IIS_USER_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(CONFIGINFO, "ConfigInfo"),]

    
LPIIS_USER_ENUM_STRUCT = IIS_USER_ENUM_STRUCT
Interface("82ad4280-036b-11cf-972c-00aa006887b0", "2.0",[Method("R_InetInfoGetVersion",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwReserved')),
Out((PDWORD,'pdwVersion')),
),Method("R_InetInfoGetAdminInformation",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
Out((PLPINET_INFO_CONFIG_INFO,'ppConfig')),
),Method("R_InetInfoGetSites",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
Out((PLPINET_INFO_SITE_LIST,'ppSites')),
),Method("R_InetInfoSetAdminInformation",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
In((PINET_INFO_CONFIG_INFO,'pConfig')),
),Method("R_InetInfoGetGlobalAdminInformation",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
Out((PLPINET_INFO_GLOBAL_CONFIG_INFO,'ppConfig')),
),Method("R_InetInfoSetGlobalAdminInformation",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
In((PINET_INFO_GLOBAL_CONFIG_INFO,'pConfig')),
),Method("R_InetInfoQueryStatistics",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'Level')),
In((DWORD,'dwServerMask')),
Out((LPINET_INFO_STATISTICS_INFO,'StatsInfo')),
),Method("R_InetInfoClearStatistics",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
),Method("R_InetInfoFlushMemoryCache",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServerMask')),
),Method("R_InetInfoGetServerCapabilities",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwReserved')),
Out((PLPINET_INFO_CAPABILITIES_STRUCT,'ppCap')),
),Method("R_W3QueryStatistics2",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwLevel')),
In((DWORD,'dwInstance')),
In((DWORD,'dwReserved')),
Out((LPW3_STATISTICS_STRUCT,'InfoStruct')),
),Method("R_W3ClearStatistics2",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwInstance')),
),Method("R_FtpQueryStatistics2",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwLevel')),
In((DWORD,'dwInstance')),
In((DWORD,'dwReserved')),
Out((LPFTP_STATISTICS_STRUCT,'InfoStruct')),
),Method("R_FtpClearStatistics2",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwInstance')),
),Method("R_IISEnumerateUsers",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServiceId')),
In((DWORD,'dwInstance')),
InOut((LPIIS_USER_ENUM_STRUCT,'InfoStruct')),
),Method("R_IISDisconnectUser",
In((INET_INFO_IMPERSONATE_HANDLE,'pszServer')),
In((DWORD,'dwServiceId')),
In((DWORD,'dwInstance')),
In((DWORD,'dwIdUser')),
),Method("Opnum16NotUsedOnWire",
),Method("Opnum17NotUsedOnWire",
),])