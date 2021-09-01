
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
__INT64 = NdrHyper
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
__INT3264 = NdrHyper
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
LONG_PTR = __INT3264
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
RRP_UNICODE_STRING = RPC_UNICODE_STRING
PPRRP_UNICODE_STRING = RPC_UNICODE_STRING
RPC_HKEY = HANDLE
PRPC_HKEY = RPC_HKEY
PREGISTRY_SERVER_NAME = PWCHAR
SECURITY_INFORMATION = DWORD
PPSECURITY_INFORMATION = DWORD

class RVALENT(NdrStructure):
    MEMBERS = [(PRPC_UNICODE_STRING, "ve_valuename"),(DWORD, "ve_valuelen"),(LPDWORD, "ve_valueptr"),(DWORD, "ve_type"),]

    
PRVALENT = RVALENT
REGSAM = ULONG

class RPC_SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(PBYTE, "lpSecurityDescriptor"),(DWORD, "cbInSecurityDescriptor"),(DWORD, "cbOutSecurityDescriptor"),]

    
PRPC_SECURITY_DESCRIPTOR = RPC_SECURITY_DESCRIPTOR

class RPC_SECURITY_ATTRIBUTES(NdrStructure):
    MEMBERS = [(DWORD, "nLength"),(RPC_SECURITY_DESCRIPTOR, "RpcSecurityDescriptor"),(BOOLEAN, "bInheritHandle"),]

    
PRPC_SECURITY_ATTRIBUTES = RPC_SECURITY_ATTRIBUTES
Interface("338CD001-2244-31F1-AAAA-900038001003", "1.0",[Method("OpenClassesRoot",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("OpenCurrentUser",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("OpenLocalMachine",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("OpenPerformanceData",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("OpenUsers",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("BaseRegCloseKey",
InOut((PRPC_HKEY,'hKey')),
),Method("BaseRegCreateKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
In((PRRP_UNICODE_STRING,'lpClass')),
In((DWORD,'dwOptions')),
In((REGSAM,'samDesired')),
In((PRPC_SECURITY_ATTRIBUTES,'lpSecurityAttributes')),
Out((PRPC_HKEY,'phkResult')),
InOut((LPDWORD,'lpdwDisposition')),
),Method("BaseRegDeleteKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
),Method("BaseRegDeleteValue",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpValueName')),
),Method("BaseRegEnumKey",
In((RPC_HKEY,'hKey')),
In((DWORD,'dwIndex')),
In((PRRP_UNICODE_STRING,'lpNameIn')),
Out((PRRP_UNICODE_STRING,'lpNameOut')),
In((PRRP_UNICODE_STRING,'lpClassIn')),
Out((PPRPC_UNICODE_STRING,'lplpClassOut')),
InOut((PFILETIME,'lpftLastWriteTime')),
),Method("BaseRegEnumValue",
In((RPC_HKEY,'hKey')),
In((DWORD,'dwIndex')),
In((PRRP_UNICODE_STRING,'lpValueNameIn')),
Out((PRPC_UNICODE_STRING,'lpValueNameOut')),
InOut((LPDWORD,'lpType')),
InOut((LPBYTE,'lpData')),
InOut((LPDWORD,'lpcbData')),
InOut((LPDWORD,'lpcbLen')),
),Method("BaseRegFlushKey",
In((RPC_HKEY,'hKey')),
),Method("BaseRegGetKeySecurity",
In((RPC_HKEY,'hKey')),
In((SECURITY_INFORMATION,'SecurityInformation')),
In((PRPC_SECURITY_DESCRIPTOR,'pRpcSecurityDescriptorIn')),
Out((PRPC_SECURITY_DESCRIPTOR,'pRpcSecurityDescriptorOut')),
),Method("BaseRegLoadKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
In((PRRP_UNICODE_STRING,'lpFile')),
),Method("Opnum14NotImplemented",
),Method("BaseRegOpenKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
In((DWORD,'dwOptions')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phkResult')),
),Method("BaseRegQueryInfoKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpClassIn')),
Out((PRPC_UNICODE_STRING,'lpClassOut')),
Out((LPDWORD,'lpcSubKeys')),
Out((LPDWORD,'lpcbMaxSubKeyLen')),
Out((LPDWORD,'lpcbMaxClassLen')),
Out((LPDWORD,'lpcValues')),
Out((LPDWORD,'lpcbMaxValueNameLen')),
Out((LPDWORD,'lpcbMaxValueLen')),
Out((LPDWORD,'lpcbSecurityDescriptor')),
Out((PFILETIME,'lpftLastWriteTime')),
),Method("BaseRegQueryValue",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpValueName')),
InOut((LPDWORD,'lpType')),
InOut((LPBYTE,'lpData')),
InOut((LPDWORD,'lpcbData')),
InOut((LPDWORD,'lpcbLen')),
),Method("BaseRegReplaceKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
In((PRRP_UNICODE_STRING,'lpNewFile')),
In((PRRP_UNICODE_STRING,'lpOldFile')),
),Method("BaseRegRestoreKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpFile')),
In((DWORD,'Flags')),
),Method("BaseRegSaveKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpFile')),
In((PRPC_SECURITY_ATTRIBUTES,'pSecurityAttributes')),
),Method("BaseRegSetKeySecurity",
In((RPC_HKEY,'hKey')),
In((SECURITY_INFORMATION,'SecurityInformation')),
In((PRPC_SECURITY_DESCRIPTOR,'pRpcSecurityDescriptor')),
),Method("BaseRegSetValue",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpValueName')),
In((DWORD,'dwType')),
In((LPBYTE,'lpData')),
In((DWORD,'cbData')),
),Method("BaseRegUnLoadKey",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
),Method("Opnum24NotImplemented",
),Method("Opnum25NotImplemented",
),Method("BaseRegGetVersion",
In((RPC_HKEY,'hKey')),
Out((LPDWORD,'lpdwVersion')),
),Method("OpenCurrentConfig",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("Opnum28NotImplemented",
),Method("BaseRegQueryMultipleValues",
In((RPC_HKEY,'hKey')),
In((PRVALENT,'val_listIn')),
Out((PRVALENT,'val_listOut')),
In((DWORD,'num_vals')),
InOut((PCHAR,'lpvalueBuf')),
InOut((LPDWORD,'ldwTotsize')),
),Method("Opnum30NotImplemented",
),Method("BaseRegSaveKeyEx",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpFile')),
In((PRPC_SECURITY_ATTRIBUTES,'pSecurityAttributes')),
In((DWORD,'Flags')),
),Method("OpenPerformanceText",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("OpenPerformanceNlsText",
In((PREGISTRY_SERVER_NAME,'ServerName')),
In((REGSAM,'samDesired')),
Out((PRPC_HKEY,'phKey')),
),Method("BaseRegQueryMultipleValues2",
In((RPC_HKEY,'hKey')),
In((PRVALENT,'val_listIn')),
Out((PRVALENT,'val_listOut')),
In((DWORD,'num_vals')),
InOut((PCHAR,'lpvalueBuf')),
In((LPDWORD,'ldwTotsize')),
Out((LPDWORD,'ldwRequiredSize')),
),Method("BaseRegDeleteKeyEx",
In((RPC_HKEY,'hKey')),
In((PRRP_UNICODE_STRING,'lpSubKey')),
In((REGSAM,'AccessMask')),
In((DWORD,'Reserved')),
),])