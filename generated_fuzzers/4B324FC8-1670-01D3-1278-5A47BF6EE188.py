
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