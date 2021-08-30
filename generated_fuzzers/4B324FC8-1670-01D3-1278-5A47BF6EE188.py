
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

    
Method("Opnum0NotUsedOnWire",
In(),
),Method("Opnum1NotUsedOnWire",
In(),
),Method("Opnum2NotUsedOnWire",
In(),
),Method("Opnum3NotUsedOnWire",
In(),
),Method("Opnum4NotUsedOnWire",
In(),
),Method("Opnum5NotUsedOnWire",
In(),
),Method("Opnum6NotUsedOnWire",
In(),
),Method("Opnum7NotUsedOnWire",
In(),
),Method("NetrConnectionEnum",
In(SRVSVC_HANDLE),
In(PWCHAR),
InOut(LPCONNECT_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrFileEnum",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
InOut(PFILE_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrFileGetInfo",
In(SRVSVC_HANDLE),
In(DWORD),
In(DWORD),
Out(LPFILE_INFO),
),Method("NetrFileClose",
In(SRVSVC_HANDLE),
In(DWORD),
),Method("NetrSessionEnum",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
InOut(PSESSION_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrSessionDel",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
),Method("NetrShareAdd",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSHARE_INFO),
InOut(PDWORD),
),Method("NetrShareEnum",
In(SRVSVC_HANDLE),
InOut(LPSHARE_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrShareGetInfo",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
Out(LPSHARE_INFO),
),Method("NetrShareSetInfo",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
In(LPSHARE_INFO),
InOut(PDWORD),
),Method("NetrShareDel",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
),Method("NetrShareDelSticky",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
),Method("NetrShareCheck",
In(SRVSVC_HANDLE),
In(PWCHAR),
Out(PDWORD),
),Method("NetrServerGetInfo",
In(SRVSVC_HANDLE),
In(DWORD),
Out(LPSERVER_INFO),
),Method("NetrServerSetInfo",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSERVER_INFO),
InOut(PDWORD),
),Method("NetrServerDiskEnum",
In(SRVSVC_HANDLE),
In(DWORD),
InOut(PDISK_ENUM_CONTAINER),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrServerStatisticsGet",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
In(DWORD),
Out(PLPSTAT_SERVER_0),
),Method("NetrServerTransportAdd",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSERVER_TRANSPORT_INFO_0),
),Method("NetrServerTransportEnum",
In(SRVSVC_HANDLE),
InOut(LPSERVER_XPORT_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrServerTransportDel",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSERVER_TRANSPORT_INFO_0),
),Method("NetrRemoteTOD",
In(SRVSVC_HANDLE),
Out(PLPTIME_OF_DAY_INFO),
),Method("Opnum29NotUsedOnWire",
In(),
),Method("NetprPathType",
In(SRVSVC_HANDLE),
In(PWCHAR),
Out(PDWORD),
In(DWORD),
),Method("NetprPathCanonicalize",
In(SRVSVC_HANDLE),
In(PWCHAR),
Out(PUNSIGNED_CHAR),
In(DWORD),
In(PWCHAR),
InOut(PDWORD),
In(DWORD),
),Method("NetprPathCompare",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
In(DWORD),
In(DWORD),
),Method("NetprNameValidate",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
In(DWORD),
),Method("NetprNameCanonicalize",
In(SRVSVC_HANDLE),
In(PWCHAR),
Out(PWCHAR),
In(DWORD),
In(DWORD),
In(DWORD),
),Method("NetprNameCompare",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
In(DWORD),
In(DWORD),
),Method("NetrShareEnumSticky",
In(SRVSVC_HANDLE),
InOut(LPSHARE_ENUM_STRUCT),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("NetrShareDelStart",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(DWORD),
Out(PSHARE_DEL_HANDLE),
),Method("NetrShareDelCommit",
InOut(PSHARE_DEL_HANDLE),
),Method("NetrpGetFileSecurity",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
In(SECURITY_INFORMATION),
Out(PPADT_SECURITY_DESCRIPTOR),
),Method("NetrpSetFileSecurity",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PWCHAR),
In(SECURITY_INFORMATION),
In(PADT_SECURITY_DESCRIPTOR),
),Method("NetrServerTransportAddEx",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPTRANSPORT_INFO),
),Method("Opnum42NotUsedOnWire",
In(),
),Method("NetrDfsGetVersion",
In(SRVSVC_HANDLE),
Out(PDWORD),
),Method("NetrDfsCreateLocalPartition",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(PGUID),
In(PWCHAR),
In(PWCHAR),
In(LPNET_DFS_ENTRY_ID_CONTAINER),
In(INT),
),Method("NetrDfsDeleteLocalPartition",
In(SRVSVC_HANDLE),
In(PGUID),
In(PWCHAR),
),Method("NetrDfsSetLocalVolumeState",
In(SRVSVC_HANDLE),
In(PGUID),
In(PWCHAR),
In(UNSIGNED_LONG),
),Method("Opnum47NotUsedOnWire",
In(),
),Method("NetrDfsCreateExitPoint",
In(SRVSVC_HANDLE),
In(PGUID),
In(PWCHAR),
In(UNSIGNED_LONG),
In(DWORD),
Out(PWCHAR),
),Method("NetrDfsDeleteExitPoint",
In(SRVSVC_HANDLE),
In(PGUID),
In(PWCHAR),
In(UNSIGNED_LONG),
),Method("NetrDfsModifyPrefix",
In(SRVSVC_HANDLE),
In(PGUID),
In(PWCHAR),
),Method("NetrDfsFixLocalVolume",
In(SRVSVC_HANDLE),
In(PWCHAR),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PWCHAR),
In(PGUID),
In(PWCHAR),
In(LPNET_DFS_ENTRY_ID_CONTAINER),
In(UNSIGNED_LONG),
),Method("NetrDfsManagerReportSiteInfo",
In(SRVSVC_HANDLE),
InOut(PLPDFS_SITELIST_INFO),
),Method("NetrServerTransportDelEx",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPTRANSPORT_INFO),
),Method("NetrServerAliasAdd",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSERVER_ALIAS_INFO),
),Method("NetrServerAliasEnum",
In(SRVSVC_HANDLE),
InOut(LPSERVER_ALIAS_ENUM_STRUCT),
In(DWORD),
Out(LPDWORD),
InOut(LPDWORD),
),Method("NetrServerAliasDel",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSERVER_ALIAS_INFO),
),Method("NetrShareDelEx",
In(SRVSVC_HANDLE),
In(DWORD),
In(LPSHARE_INFO),
),