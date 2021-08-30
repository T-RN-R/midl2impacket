
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

    
Method("OpenClassesRoot",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("OpenCurrentUser",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("OpenLocalMachine",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("OpenPerformanceData",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("OpenUsers",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("BaseRegCloseKey",
InOut(PRPC_HKEY),
),Method("BaseRegCreateKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(PRRP_UNICODE_STRING),
In(DWORD),
In(REGSAM),
In(PRPC_SECURITY_ATTRIBUTES),
Out(PRPC_HKEY),
InOut(LPDWORD),
),Method("BaseRegDeleteKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
),Method("BaseRegDeleteValue",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
),Method("BaseRegEnumKey",
In(RPC_HKEY),
In(DWORD),
In(PRRP_UNICODE_STRING),
Out(PRRP_UNICODE_STRING),
In(PRRP_UNICODE_STRING),
Out(PPRPC_UNICODE_STRING),
InOut(PFILETIME),
),Method("BaseRegEnumValue",
In(RPC_HKEY),
In(DWORD),
In(PRRP_UNICODE_STRING),
Out(PRPC_UNICODE_STRING),
InOut(LPDWORD),
InOut(LPBYTE),
InOut(LPDWORD),
InOut(LPDWORD),
),Method("BaseRegFlushKey",
In(RPC_HKEY),
),Method("BaseRegGetKeySecurity",
In(RPC_HKEY),
In(SECURITY_INFORMATION),
In(PRPC_SECURITY_DESCRIPTOR),
Out(PRPC_SECURITY_DESCRIPTOR),
),Method("BaseRegLoadKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(PRRP_UNICODE_STRING),
),Method("Opnum14NotImplemented",
),Method("BaseRegOpenKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(DWORD),
In(REGSAM),
Out(PRPC_HKEY),
),Method("BaseRegQueryInfoKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
Out(PRPC_UNICODE_STRING),
Out(LPDWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(PFILETIME),
),Method("BaseRegQueryValue",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
InOut(LPDWORD),
InOut(LPBYTE),
InOut(LPDWORD),
InOut(LPDWORD),
),Method("BaseRegReplaceKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(PRRP_UNICODE_STRING),
In(PRRP_UNICODE_STRING),
),Method("BaseRegRestoreKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(DWORD),
),Method("BaseRegSaveKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(PRPC_SECURITY_ATTRIBUTES),
),Method("BaseRegSetKeySecurity",
In(RPC_HKEY),
In(SECURITY_INFORMATION),
In(PRPC_SECURITY_DESCRIPTOR),
),Method("BaseRegSetValue",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(DWORD),
In(LPBYTE),
In(DWORD),
),Method("BaseRegUnLoadKey",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
),Method("Opnum24NotImplemented",
),Method("Opnum25NotImplemented",
),Method("BaseRegGetVersion",
In(RPC_HKEY),
Out(LPDWORD),
),Method("OpenCurrentConfig",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("Opnum28NotImplemented",
),Method("BaseRegQueryMultipleValues",
In(RPC_HKEY),
In(PRVALENT),
Out(PRVALENT),
In(DWORD),
InOut(PCHAR),
InOut(LPDWORD),
),Method("Opnum30NotImplemented",
),Method("BaseRegSaveKeyEx",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(PRPC_SECURITY_ATTRIBUTES),
In(DWORD),
),Method("OpenPerformanceText",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("OpenPerformanceNlsText",
In(PREGISTRY_SERVER_NAME),
In(REGSAM),
Out(PRPC_HKEY),
),Method("BaseRegQueryMultipleValues2",
In(RPC_HKEY),
In(PRVALENT),
Out(PRVALENT),
In(DWORD),
InOut(PCHAR),
In(LPDWORD),
Out(LPDWORD),
),Method("BaseRegDeleteKeyEx",
In(RPC_HKEY),
In(PRRP_UNICODE_STRING),
In(REGSAM),
In(DWORD),
),