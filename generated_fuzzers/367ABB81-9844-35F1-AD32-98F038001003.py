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


Method("RCloseServiceHandle", InOut(LPSC_RPC_HANDLE),), Method(
    "RControlService",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(LPSERVICE_STATUS),
), Method("RDeleteService", In(SC_RPC_HANDLE),), Method(
    "RLockServiceDatabase",
    In(SC_RPC_HANDLE),
    Out(LPSC_RPC_LOCK),
), Method(
    "RQueryServiceObjectSecurity",
    In(SC_RPC_HANDLE),
    In(SECURITY_INFORMATION),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
), Method(
    "RSetServiceObjectSecurity",
    In(SC_RPC_HANDLE),
    In(SECURITY_INFORMATION),
    In(LPBYTE),
    In(DWORD),
), Method(
    "RQueryServiceStatus",
    In(SC_RPC_HANDLE),
    Out(LPSERVICE_STATUS),
), Method(
    "RSetServiceStatus",
    In(SC_RPC_HANDLE),
    In(LPSERVICE_STATUS),
), Method(
    "RUnlockServiceDatabase",
    InOut(LPSC_RPC_LOCK),
), Method(
    "RNotifyBootConfigStatus",
    In(SVCCTL_HANDLEW),
    In(DWORD),
), Method(
    "Opnum10NotUsedOnWire",
    In(),
), Method(
    "RChangeServiceConfigW",
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
), Method(
    "RCreateServiceW",
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
), Method(
    "REnumDependentServicesW",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
    Out(LPBOUNDED_DWORD_256K),
), Method(
    "REnumServicesStatusW",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
    Out(LPBOUNDED_DWORD_256K),
    InOut(LPBOUNDED_DWORD_256K),
), Method(
    "ROpenSCManagerW",
    In(SVCCTL_HANDLEW),
    In(PWCHAR_T),
    In(DWORD),
    Out(LPSC_RPC_HANDLE),
), Method(
    "ROpenServiceW",
    In(SC_RPC_HANDLE),
    In(PWCHAR_T),
    In(DWORD),
    Out(LPSC_RPC_HANDLE),
), Method(
    "RQueryServiceConfigW",
    In(SC_RPC_HANDLE),
    Out(LPQUERY_SERVICE_CONFIGW),
    In(DWORD),
    Out(LPBOUNDED_DWORD_8K),
), Method(
    "RQueryServiceLockStatusW",
    In(SC_RPC_HANDLE),
    Out(LPQUERY_SERVICE_LOCK_STATUSW),
    In(DWORD),
    Out(LPBOUNDED_DWORD_4K),
), Method(
    "RStartServiceW",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(LPSTRING_PTRSW),
), Method(
    "RGetServiceDisplayNameW",
    In(SC_RPC_HANDLE),
    In(PWCHAR_T),
    Out(PWCHAR_T),
    InOut(PDWORD),
), Method(
    "RGetServiceKeyNameW",
    In(SC_RPC_HANDLE),
    In(PWCHAR_T),
    Out(PWCHAR_T),
    InOut(PDWORD),
), Method(
    "Opnum22NotUsedOnWire",
    In(),
), Method(
    "RChangeServiceConfigA",
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
), Method(
    "RCreateServiceA",
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
), Method(
    "REnumDependentServicesA",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
    Out(LPBOUNDED_DWORD_256K),
), Method(
    "REnumServicesStatusA",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
    Out(LPBOUNDED_DWORD_256K),
    InOut(LPBOUNDED_DWORD_256K),
), Method(
    "ROpenSCManagerA",
    In(SVCCTL_HANDLEA),
    In(LPSTR),
    In(DWORD),
    Out(LPSC_RPC_HANDLE),
), Method(
    "ROpenServiceA",
    In(SC_RPC_HANDLE),
    In(LPSTR),
    In(DWORD),
    Out(LPSC_RPC_HANDLE),
), Method(
    "RQueryServiceConfigA",
    In(SC_RPC_HANDLE),
    Out(LPQUERY_SERVICE_CONFIGA),
    In(DWORD),
    Out(LPBOUNDED_DWORD_8K),
), Method(
    "RQueryServiceLockStatusA",
    In(SC_RPC_HANDLE),
    Out(LPQUERY_SERVICE_LOCK_STATUSA),
    In(DWORD),
    Out(LPBOUNDED_DWORD_4K),
), Method(
    "RStartServiceA",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(LPSTRING_PTRSA),
), Method(
    "RGetServiceDisplayNameA",
    In(SC_RPC_HANDLE),
    In(LPSTR),
    Out(LPSTR),
    InOut(LPBOUNDED_DWORD_4K),
), Method(
    "RGetServiceKeyNameA",
    In(SC_RPC_HANDLE),
    In(LPSTR),
    Out(LPSTR),
    InOut(LPBOUNDED_DWORD_4K),
), Method(
    "Opnum34NotUsedOnWire",
    In(),
), Method(
    "REnumServiceGroupW",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_256K),
    Out(LPBOUNDED_DWORD_256K),
    InOut(LPBOUNDED_DWORD_256K),
    In(LPCWSTR),
), Method(
    "RChangeServiceConfig2A",
    In(SC_RPC_HANDLE),
    In(SC_RPC_CONFIG_INFOA),
), Method(
    "RChangeServiceConfig2W",
    In(SC_RPC_HANDLE),
    In(SC_RPC_CONFIG_INFOW),
), Method(
    "RQueryServiceConfig2A",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_8K),
), Method(
    "RQueryServiceConfig2W",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_8K),
), Method(
    "RQueryServiceStatusEx",
    In(SC_RPC_HANDLE),
    In(SC_STATUS_TYPE),
    Out(LPBYTE),
    In(DWORD),
    Out(LPBOUNDED_DWORD_8K),
), Method(
    "REnumServicesStatusExA",
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
), Method(
    "REnumServicesStatusExW",
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
), Method(
    "Opnum43NotUsedOnWire",
    In(),
), Method(
    "RCreateServiceWOW64A",
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
), Method(
    "RCreateServiceWOW64W",
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
), Method(
    "Opnum46NotUsedOnWire",
    In(),
), Method(
    "RNotifyServiceStatusChange",
    In(SC_RPC_HANDLE),
    In(SC_RPC_NOTIFY_PARAMS),
    In(PGUID),
    Out(PGUID),
    Out(PBOOL),
    Out(LPSC_NOTIFY_RPC_HANDLE),
), Method(
    "RGetNotifyResults",
    In(SC_NOTIFY_RPC_HANDLE),
    Out(PPSC_RPC_NOTIFY_PARAMS_LIST),
), Method(
    "RCloseNotifyHandle",
    InOut(LPSC_NOTIFY_RPC_HANDLE),
    Out(PBOOL),
), Method(
    "RControlServiceExA",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PSC_RPC_SERVICE_CONTROL_IN_PARAMSA),
    Out(PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA),
), Method(
    "RControlServiceExW",
    In(SC_RPC_HANDLE),
    In(DWORD),
    In(DWORD),
    In(PSC_RPC_SERVICE_CONTROL_IN_PARAMSW),
    Out(PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW),
), Method(
    "Opnum52NotUsedOnWire",
    In(),
), Method(
    "Opnum53NotUsedOnWire",
    In(),
), Method(
    "Opnum54NotUsedOnWire",
    In(),
), Method(
    "Opnum55NotUsedOnWire",
    In(),
), Method(
    "RQueryServiceConfigEx",
    In(SC_RPC_HANDLE),
    In(DWORD),
    Out(PSC_RPC_CONFIG_INFOW),
), Method(
    "Opnum57NotUsedOnWire",
    In(),
), Method(
    "Opnum58NotUsedOnWire",
    In(),
), Method(
    "Opnum59NotUsedOnWire",
    In(),
), Method(
    "RCreateWowService",
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
), Method(
    "ROpenSCManager2",
    In(HANDLE_T),
    In(PWCHAR_T),
    In(DWORD),
    Out(LPSC_RPC_HANDLE),
),
