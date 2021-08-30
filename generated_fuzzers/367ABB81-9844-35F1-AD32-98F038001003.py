
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

    
Method("RCloseServiceHandle",
InOut(LPSC_RPC_HANDLE),
),Method("RControlService",
In(SC_RPC_HANDLE),
In(DWORD),
Out(LPSERVICE_STATUS),
),Method("RDeleteService",
In(SC_RPC_HANDLE),
),Method("RLockServiceDatabase",
In(SC_RPC_HANDLE),
Out(LPSC_RPC_LOCK),
),Method("RQueryServiceObjectSecurity",
In(SC_RPC_HANDLE),
In(SECURITY_INFORMATION),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
),Method("RSetServiceObjectSecurity",
In(SC_RPC_HANDLE),
In(SECURITY_INFORMATION),
In(LPBYTE),
In(DWORD),
),Method("RQueryServiceStatus",
In(SC_RPC_HANDLE),
Out(LPSERVICE_STATUS),
),Method("RSetServiceStatus",
In(SC_RPC_HANDLE),
In(LPSERVICE_STATUS),
),Method("RUnlockServiceDatabase",
InOut(LPSC_RPC_LOCK),
),Method("RNotifyBootConfigStatus",
In(SVCCTL_HANDLEW),
In(DWORD),
),Method("Opnum10NotUsedOnWire",
In(),
),Method("RChangeServiceConfigW",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
In(PWCHAR_T),
In(PWCHAR_T),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(PWCHAR_T),
In(LPBYTE),
In(DWORD),
In(PWCHAR_T),
),Method("RCreateServiceW",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(PWCHAR_T),
In(PWCHAR_T),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(PWCHAR_T),
In(LPBYTE),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("REnumDependentServicesW",
In(SC_RPC_HANDLE),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
),Method("REnumServicesStatusW",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
InOut(LPBOUNDED_DWORD_256K),
),Method("ROpenSCManagerW",
In(SVCCTL_HANDLEW),
In(PWCHAR_T),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("ROpenServiceW",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("RQueryServiceConfigW",
In(SC_RPC_HANDLE),
Out(LPQUERY_SERVICE_CONFIGW),
In(DWORD),
Out(LPBOUNDED_DWORD_8K),
),Method("RQueryServiceLockStatusW",
In(SC_RPC_HANDLE),
Out(LPQUERY_SERVICE_LOCK_STATUSW),
In(DWORD),
Out(LPBOUNDED_DWORD_4K),
),Method("RStartServiceW",
In(SC_RPC_HANDLE),
In(DWORD),
In(LPSTRING_PTRSW),
),Method("RGetServiceDisplayNameW",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
Out(PWCHAR_T),
InOut(PDWORD),
),Method("RGetServiceKeyNameW",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
Out(PWCHAR_T),
InOut(PDWORD),
),Method("Opnum22NotUsedOnWire",
In(),
),Method("RChangeServiceConfigA",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
In(LPSTR),
In(LPSTR),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(LPSTR),
In(LPBYTE),
In(DWORD),
In(LPSTR),
),Method("RCreateServiceA",
In(SC_RPC_HANDLE),
In(LPSTR),
In(LPSTR),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(LPSTR),
In(LPSTR),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(LPSTR),
In(LPBYTE),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("REnumDependentServicesA",
In(SC_RPC_HANDLE),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
),Method("REnumServicesStatusA",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
InOut(LPBOUNDED_DWORD_256K),
),Method("ROpenSCManagerA",
In(SVCCTL_HANDLEA),
In(LPSTR),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("ROpenServiceA",
In(SC_RPC_HANDLE),
In(LPSTR),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("RQueryServiceConfigA",
In(SC_RPC_HANDLE),
Out(LPQUERY_SERVICE_CONFIGA),
In(DWORD),
Out(LPBOUNDED_DWORD_8K),
),Method("RQueryServiceLockStatusA",
In(SC_RPC_HANDLE),
Out(LPQUERY_SERVICE_LOCK_STATUSA),
In(DWORD),
Out(LPBOUNDED_DWORD_4K),
),Method("RStartServiceA",
In(SC_RPC_HANDLE),
In(DWORD),
In(LPSTRING_PTRSA),
),Method("RGetServiceDisplayNameA",
In(SC_RPC_HANDLE),
In(LPSTR),
Out(LPSTR),
InOut(LPBOUNDED_DWORD_4K),
),Method("RGetServiceKeyNameA",
In(SC_RPC_HANDLE),
In(LPSTR),
Out(LPSTR),
InOut(LPBOUNDED_DWORD_4K),
),Method("Opnum34NotUsedOnWire",
In(),
),Method("REnumServiceGroupW",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
InOut(LPBOUNDED_DWORD_256K),
In(LPCWSTR),
),Method("RChangeServiceConfig2A",
In(SC_RPC_HANDLE),
In(SC_RPC_CONFIG_INFOA),
),Method("RChangeServiceConfig2W",
In(SC_RPC_HANDLE),
In(SC_RPC_CONFIG_INFOW),
),Method("RQueryServiceConfig2A",
In(SC_RPC_HANDLE),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_8K),
),Method("RQueryServiceConfig2W",
In(SC_RPC_HANDLE),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_8K),
),Method("RQueryServiceStatusEx",
In(SC_RPC_HANDLE),
In(SC_STATUS_TYPE),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_8K),
),Method("REnumServicesStatusExA",
In(SC_RPC_HANDLE),
In(SC_ENUM_TYPE),
In(DWORD),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
InOut(LPBOUNDED_DWORD_256K),
In(LPCSTR),
),Method("REnumServicesStatusExW",
In(SC_RPC_HANDLE),
In(SC_ENUM_TYPE),
In(DWORD),
In(DWORD),
Out(LPBYTE),
In(DWORD),
Out(LPBOUNDED_DWORD_256K),
Out(LPBOUNDED_DWORD_256K),
InOut(LPBOUNDED_DWORD_256K),
In(LPCWSTR),
),Method("Opnum43NotUsedOnWire",
In(),
),Method("RCreateServiceWOW64A",
In(SC_RPC_HANDLE),
In(LPSTR),
In(LPSTR),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(LPSTR),
In(LPSTR),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(LPSTR),
In(LPBYTE),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("RCreateServiceWOW64W",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(PWCHAR_T),
In(PWCHAR_T),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(PWCHAR_T),
In(LPBYTE),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),Method("Opnum46NotUsedOnWire",
In(),
),Method("RNotifyServiceStatusChange",
In(SC_RPC_HANDLE),
In(SC_RPC_NOTIFY_PARAMS),
In(PGUID),
Out(PGUID),
Out(PBOOL),
Out(LPSC_NOTIFY_RPC_HANDLE),
),Method("RGetNotifyResults",
In(SC_NOTIFY_RPC_HANDLE),
Out(PPSC_RPC_NOTIFY_PARAMS_LIST),
),Method("RCloseNotifyHandle",
InOut(LPSC_NOTIFY_RPC_HANDLE),
Out(PBOOL),
),Method("RControlServiceExA",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
In(PSC_RPC_SERVICE_CONTROL_IN_PARAMSA),
Out(PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA),
),Method("RControlServiceExW",
In(SC_RPC_HANDLE),
In(DWORD),
In(DWORD),
In(PSC_RPC_SERVICE_CONTROL_IN_PARAMSW),
Out(PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW),
),Method("Opnum52NotUsedOnWire",
In(),
),Method("Opnum53NotUsedOnWire",
In(),
),Method("Opnum54NotUsedOnWire",
In(),
),Method("Opnum55NotUsedOnWire",
In(),
),Method("RQueryServiceConfigEx",
In(SC_RPC_HANDLE),
In(DWORD),
Out(PSC_RPC_CONFIG_INFOW),
),Method("Opnum57NotUsedOnWire",
In(),
),Method("Opnum58NotUsedOnWire",
In(),
),Method("Opnum59NotUsedOnWire",
In(),
),Method("RCreateWowService",
In(SC_RPC_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(PWCHAR_T),
In(PWCHAR_T),
InOut(LPDWORD),
In(LPBYTE),
In(DWORD),
In(PWCHAR_T),
In(LPBYTE),
In(DWORD),
In(USHORT),
Out(LPSC_RPC_HANDLE),
),Method("ROpenSCManager2",
In(HANDLE_T),
In(PWCHAR_T),
In(DWORD),
Out(LPSC_RPC_HANDLE),
),