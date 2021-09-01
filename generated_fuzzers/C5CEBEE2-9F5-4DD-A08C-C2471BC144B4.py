
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
CLSID = GUID
IID = GUID
ID = UNSIGNED_HYPER
OXID = UNSIGNED_HYPER
OID = UNSIGNED_HYPER
SETID = UNSIGNED_HYPER
IPID = GUID
CID = GUID
REFIPID = GUID

class COMVERSION(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "MajorVersion"),(UNSIGNED_SHORT, "MinorVersion"),]

    

class ORPC_EXTENT(NdrStructure):
    MEMBERS = [(GUID, "id"),(UNSIGNED_LONG, "size"),(BYTE, "data"),]

    

class ORPC_EXTENT_ARRAY(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "size"),(UNSIGNED_LONG, "reserved"),(PPORPC_EXTENT, "extent"),]

    

class ORPCTHIS(NdrStructure):
    MEMBERS = [(COMVERSION, "version"),(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "reserved1"),(CID, "cid"),(PORPC_EXTENT_ARRAY, "extensions"),]

    

class ORPCTHAT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(PORPC_EXTENT_ARRAY, "extensions"),]

    

class DUALSTRINGARRAY(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "wNumEntries"),(UNSIGNED_SHORT, "wSecurityOffset"),(UNSIGNED_SHORT, "aStringArray"),]

    

class (NdrEnum):
    MAP = ((1 , 'CPFLAG_PROPAGATE'),(2 , 'CPFLAG_EXPOSE'),(4 , 'CPFLAG_ENVOY'),)        

class MINTERFACEPOINTER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulCntData"),(BYTE, "abData"),]

    
PMINTERFACEPOINTER = MINTERFACEPOINTER

class ERROROBJECTDATA(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwHelpContext"),(IID, "iid"),(PWCHAR_T, "pszSource"),(PWCHAR_T, "pszDescription"),(PWCHAR_T, "pszHelpFile"),]

    

class STDOBJREF(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "cPublicRefs"),(OXID, "oxid"),(OID, "oid"),(IPID, "ipid"),]

    

class REMQIRESULT(NdrStructure):
    MEMBERS = [(HRESULT, "hResult"),(STDOBJREF, "std"),]

    

class REMINTERFACEREF(NdrStructure):
    MEMBERS = [(IPID, "ipid"),(UNSIGNED_LONG, "cPublicRefs"),(UNSIGNED_LONG, "cPrivateRefs"),]

    
PREMQIRESULT = REMQIRESULT
PMINTERFACEPOINTERINTERNAL = MINTERFACEPOINTER

class COSERVERINFO(NdrStructure):
    MEMBERS = [(DWORD, "dwReserved1"),(PWCHAR_T, "pwszName"),(PDWORD, "pdwReserved"),(DWORD, "dwReserved2"),]

    

class CUSTOMREMOTE_REQUEST_SCM_INFO(NdrStructure):
    MEMBERS = [(DWORD, "ClientImpLevel"),(UNSIGNED_SHORT, "cRequestedProtseqs"),(PUNSIGNED_SHORT, "pRequestedProtseqs"),]

    

class CUSTOMREMOTE_REPLY_SCM_INFO(NdrStructure):
    MEMBERS = [(OXID, "Oxid"),(PDUALSTRINGARRAY, "pdsaOxidBindings"),(IPID, "ipidRemUnknown"),(DWORD, "authnHint"),(COMVERSION, "serverVersion"),]

    

class INSTANTIATIONINFODATA(NdrStructure):
    MEMBERS = [(CLSID, "classId"),(DWORD, "classCtx"),(DWORD, "actvflags"),(LONG, "fIsSurrogate"),(DWORD, "cIID"),(DWORD, "instFlag"),(PIID, "pIID"),(DWORD, "thisSize"),(COMVERSION, "clientCOMVersion"),]

    

class LOCATIONINFODATA(NdrStructure):
    MEMBERS = [(PWCHAR_T, "machineName"),(DWORD, "processId"),(DWORD, "apartmentId"),(DWORD, "contextId"),]

    

class ACTIVATIONCONTEXTINFODATA(NdrStructure):
    MEMBERS = [(LONG, "clientOK"),(LONG, "bReserved1"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(PMINTERFACEPOINTER, "pIFDClientCtx"),(PMINTERFACEPOINTER, "pIFDPrototypeCtx"),]

    

class CUSTOMHEADER(NdrStructure):
    MEMBERS = [(DWORD, "totalSize"),(DWORD, "headerSize"),(DWORD, "dwReserved"),(DWORD, "destCtx"),(DWORD, "cIfs"),(CLSID, "classInfoClsid"),(PCLSID, "pclsid"),(PDWORD, "pSizes"),(PDWORD, "pdwReserved"),]

    

class PROPSOUTINFO(NdrStructure):
    MEMBERS = [(DWORD, "cIfs"),(PIID, "piid"),(PHRESULT, "phresults"),(PPMINTERFACEPOINTER, "ppIntfData"),]

    

class SECURITYINFODATA(NdrStructure):
    MEMBERS = [(DWORD, "dwAuthnFlags"),(PCOSERVERINFO, "pServerInfo"),(PDWORD, "pdwReserved"),]

    

class SCMREQUESTINFODATA(NdrStructure):
    MEMBERS = [(PDWORD, "pdwReserved"),(PCUSTOMREMOTE_REQUEST_SCM_INFO, "remoteRequest"),]

    

class SCMREPLYINFODATA(NdrStructure):
    MEMBERS = [(PDWORD, "pdwReserved"),(PCUSTOMREMOTE_REPLY_SCM_INFO, "remoteReply"),]

    

class INSTANCEINFODATA(NdrStructure):
    MEMBERS = [(PWCHAR_T, "fileName"),(DWORD, "mode"),(PMINTERFACEPOINTER, "ifdROT"),(PMINTERFACEPOINTER, "ifdStg"),]

    

class SPD_FLAGS(NdrEnum):
    MAP = ((1 , 'SPD_FLAG_USE_CONSOLE_SESSION'),(2 , 'SPD_FLAG_USE_DEFAULT_AUTHN_LVL'),)        

class SPECIALPROPERTIESDATA(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved1"),(UNSIGNED___INT64, "Reserved2"),(DWORD, "Reserved3"),]

    

class SPECIALPROPERTIESDATA_ALTERNATE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved3"),]

    
Interface("4d9f4ab8-7d1c-11cf-861e-0020af6e7c57", "1.0",[Method("RemoteActivation",
In((HANDLE_T,'hRpc')),
In((PORPCTHIS,'ORPCthis')),
Out((PORPCTHAT,'ORPCthat')),
In((PGUID,'Clsid')),
In((PWCHAR_T,'pwszObjectName')),
In((PMINTERFACEPOINTER,'pObjectStorage')),
In((DWORD,'ClientImpLevel')),
In((DWORD,'Mode')),
In((DWORD,'Interfaces')),
In((PIID,'pIIDs')),
In((UNSIGNED_SHORT,'cRequestedProtseqs')),
In((UNSIGNED_SHORT,'aRequestedProtseqs')),
Out((POXID,'pOxid')),
Out((PPDUALSTRINGARRAY,'ppdsaOxidBindings')),
Out((PIPID,'pipidRemUnknown')),
Out((PDWORD,'pAuthnHint')),
Out((PCOMVERSION,'pServerVersion')),
Out((PHRESULT,'phr')),
Out((PPMINTERFACEPOINTER,'ppInterfaceData')),
Out((PHRESULT,'pResults')),
),])BYTE = BYTE
SCODE = LONG
REFIID = IID
REFGUID = GUID
LPOLESTR = WCHAR_T
LPCOLESTR = WCHAR_T
ULONG_PTR = UNSIGNED___INT3264
PPULONG_PTR = UNSIGNED___INT3264
PVOID = VOID
PLPVOID = VOID
PSAFEARRAY = SAFEARRAY
PLPSAFEARRAY = SAFEARRAY

class PVARIANT(NdrStructure):
    MEMBERS = []

    

class VARENUM(NdrEnum):
    MAP = ((0 , 'VT_EMPTY'),(1 , 'VT_NULL'),(2 , 'VT_I2'),(3 , 'VT_I4'),(4 , 'VT_R4'),(5 , 'VT_R8'),(6 , 'VT_CY'),(7 , 'VT_DATE'),(8 , 'VT_BSTR'),(9 , 'VT_DISPATCH'),(10 , 'VT_ERROR'),(11 , 'VT_BOOL'),(12 , 'VT_VARIANT'),(13 , 'VT_UNKNOWN'),(14 , 'VT_DECIMAL'),(16 , 'VT_I1'),(17 , 'VT_UI1'),(18 , 'VT_UI2'),(19 , 'VT_UI4'),(20 , 'VT_I8'),(21 , 'VT_UI8'),(22 , 'VT_INT'),(23 , 'VT_UINT'),(24 , 'VT_VOID'),(25 , 'VT_HRESULT'),(26 , 'VT_PTR'),(27 , 'VT_SAFEARRAY'),(28 , 'VT_CARRAY'),(29 , 'VT_USERDEFINED'),(30 , 'VT_LPSTR'),(31 , 'VT_LPWSTR'),(36 , 'VT_RECORD'),(37 , 'VT_INT_PTR'),(38 , 'VT_UINT_PTR'),(8192 , 'VT_ARRAY'),(16384 , 'VT_BYREF'),)        

class ADVFEATUREFLAGS(NdrEnum):
    MAP = ((1 , 'FADF_AUTO'),(2 , 'FADF_STATIC'),(4 , 'FADF_EMBEDDED'),(16 , 'FADF_FIXEDSIZE'),(32 , 'FADF_RECORD'),(64 , 'FADF_HAVEIID'),(128 , 'FADF_HAVEVARTYPE'),(256 , 'FADF_BSTR'),(512 , 'FADF_UNKNOWN'),(1024 , 'FADF_DISPATCH'),(2048 , 'FADF_VARIANT'),)        

class SF_TYPE(NdrEnum):
    MAP = ((VT_ERROR , 'SF_ERROR'),(VT_I1 , 'SF_I1'),(VT_I2 , 'SF_I2'),(VT_I4 , 'SF_I4'),(VT_I8 , 'SF_I8'),(VT_BSTR , 'SF_BSTR'),(VT_UNKNOWN , 'SF_UNKNOWN'),(VT_DISPATCH , 'SF_DISPATCH'),(VT_VARIANT , 'SF_VARIANT'),(VT_RECORD , 'SF_RECORD'),(VT_UNKNOWN|32768 , 'SF_HAVEIID'),)        

class CALLCONV(NdrEnum):
    MAP = ((1 , 'CC_CDECL'),(2 , 'CC_PASCAL'),(4 , 'CC_STDCALL'),)        

class FUNCFLAGS(NdrEnum):
    MAP = ((1 , 'FUNCFLAG_FRESTRICTED'),(2 , 'FUNCFLAG_FSOURCE'),(4 , 'FUNCFLAG_FBINDABLE'),(8 , 'FUNCFLAG_FREQUESTEDIT'),(16 , 'FUNCFLAG_FDISPLAYBIND'),(32 , 'FUNCFLAG_FDEFAULTBIND'),(64 , 'FUNCFLAG_FHIDDEN'),(128 , 'FUNCFLAG_FUSESGETLASTERROR'),(256 , 'FUNCFLAG_FDEFAULTCOLLELEM'),(512 , 'FUNCFLAG_FUIDEFAULT'),(1024 , 'FUNCFLAG_FNONBROWSABLE'),(2048 , 'FUNCFLAG_FREPLACEABLE'),(4096 , 'FUNCFLAG_FIMMEDIATEBIND'),)        

class FUNCKIND(NdrEnum):
    MAP = ((1 , 'FUNC_PUREVIRTUAL'),(3 , 'FUNC_STATIC'),(4 , 'FUNC_DISPATCH'),)        

class IMPLTYPEFLAGS(NdrEnum):
    MAP = ((1 , 'IMPLTYPEFLAG_FDEFAULT'),(2 , 'IMPLTYPEFLAG_FSOURCE'),(4 , 'IMPLTYPEFLAG_FRESTRICTED'),(8 , 'IMPLTYPEFLAG_FDEFAULTVTABLE'),)        

class INVOKEKIND(NdrEnum):
    MAP = ((1 , 'INVOKE_FUNC'),(2 , 'INVOKE_PROPERTYGET'),(4 , 'INVOKE_PROPERTYPUT'),(8 , 'INVOKE_PROPERTYPUTREF'),)        

class PARAMFLAGS(NdrEnum):
    MAP = ((0 , 'PARAMFLAG_NONE'),(1 , 'PARAMFLAG_FIN'),(2 , 'PARAMFLAG_FOUT'),(4 , 'PARAMFLAG_FLCID'),(8 , 'PARAMFLAG_FRETVAL'),(16 , 'PARAMFLAG_FOPT'),(32 , 'PARAMFLAG_FHASDEFAULT'),(64 , 'PARAMFLAG_FHASCUSTDATA'),)        

class TYPEFLAGS(NdrEnum):
    MAP = ((1 , 'TYPEFLAG_FAPPOBJECT'),(2 , 'TYPEFLAG_FCANCREATE'),(4 , 'TYPEFLAG_FLICENSED'),(8 , 'TYPEFLAG_FPREDECLID'),(16 , 'TYPEFLAG_FHIDDEN'),(32 , 'TYPEFLAG_FCONTROL'),(64 , 'TYPEFLAG_FDUAL'),(128 , 'TYPEFLAG_FNONEXTENSIBLE'),(256 , 'TYPEFLAG_FOLEAUTOMATION'),(512 , 'TYPEFLAG_FRESTRICTED'),(1024 , 'TYPEFLAG_FAGGREGATABLE'),(2048 , 'TYPEFLAG_FREPLACEABLE'),(4096 , 'TYPEFLAG_FDISPATCHABLE'),(16384 , 'TYPEFLAG_FPROXY'),)        

class TYPEKIND(NdrEnum):
    MAP = ((0 , 'TKIND_ENUM'),(1 , 'TKIND_RECORD'),(2 , 'TKIND_MODULE'),(3 , 'TKIND_INTERFACE'),(4 , 'TKIND_DISPATCH'),(5 , 'TKIND_COCLASS'),(6 , 'TKIND_ALIAS'),(7 , 'TKIND_UNION'),)        

class VARFLAGS(NdrEnum):
    MAP = ((1 , 'VARFLAG_FREADONLY'),(2 , 'VARFLAG_FSOURCE'),(4 , 'VARFLAG_FBINDABLE'),(8 , 'VARFLAG_FREQUESTEDIT'),(16 , 'VARFLAG_FDISPLAYBIND'),(32 , 'VARFLAG_FDEFAULTBIND'),(64 , 'VARFLAG_FHIDDEN'),(128 , 'VARFLAG_FRESTRICTED'),(256 , 'VARFLAG_FDEFAULTCOLLELEM'),(512 , 'VARFLAG_FUIDEFAULT'),(1024 , 'VARFLAG_FNONBROWSABLE'),(2048 , 'VARFLAG_FREPLACEABLE'),(4096 , 'VARFLAG_FIMMEDIATEBIND'),)        

class VARKIND(NdrEnum):
    MAP = ((0 , 'VAR_PERINSTANCE'),((VAR_PERINSTANCE+1) , 'VAR_STATIC'),((VAR_STATIC+1) , 'VAR_CONST'),((VAR_CONST+1) , 'VAR_DISPATCH'),)        

class LIBFLAGS(NdrEnum):
    MAP = ((1 , 'LIBFLAG_FRESTRICTED'),(2 , 'LIBFLAG_FCONTROL'),(4 , 'LIBFLAG_FHIDDEN'),(8 , 'LIBFLAG_FHASDISKIMAGE'),)        

class SYSKIND(NdrEnum):
    MAP = ((1 , 'SYS_WIN32'),(3 , 'SYS_WIN64'),)        

class DESCKIND(NdrEnum):
    MAP = ((0 , 'DESCKIND_NONE'),(1 , 'DESCKIND_FUNCDESC'),(2 , 'DESCKIND_VARDESC'),(3 , 'DESCKIND_TYPECOMP'),(4 , 'DESCKIND_IMPLICITAPPOBJ'),)        

class FLAGGED_WORD_BLOB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cBytes"),(UNSIGNED_LONG, "clSize"),(UNSIGNED_SHORT, "asData"),]

    
BSTR = FLAGGED_WORD_BLOB

class CURRENCY(NdrStructure):
    MEMBERS = [(__INT64, "int64"),]

    
DATE = DOUBLE

class DECIMAL(NdrStructure):
    MEMBERS = [(WORD, "wReserved"),(BYTE, "scale"),(BYTE, "sign"),(ULONG, "Hi32"),(ULONGLONG, "Lo64"),]

    
VARIANT_BOOL = SHORT

class WIREBRECORDSTR(NdrStructure):
    MEMBERS = [(ULONG, "fFlags"),(ULONG, "clSize"),(PMINTERFACEPOINTER, "pRecInfo"),(PBYTE, "pRecord"),]

    

class PBRECORD(NdrStructure):
    MEMBERS = []

    

class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LONGLONG, "llVal"),2 : (LONG, "lVal"),3 : (BYTE, "bVal"),4 : (SHORT, "iVal"),5 : (FLOAT, "fltVal"),6 : (DOUBLE, "dblVal"),7 : (VARIANT_BOOL, "boolVal"),8 : (HRESULT, "scode"),9 : (CURRENCY, "cyVal"),10 : (DATE, "date"),11 : (BSTR, "bstrVal"),12 : (PIUNKNOWN, "punkVal"),13 : (PIDISPATCH, "pdispVal"),14 : (PSAFEARRAY, "parray"),15 : (BRECORD, "brecVal"),16 : (PBYTE, "pbVal"),17 : (PSHORT, "piVal"),18 : (PLONG, "plVal"),19 : (PLONGLONG, "pllVal"),20 : (PFLOAT, "pfltVal"),21 : (PDOUBLE, "pdblVal"),22 : (PVARIANT_BOOL, "pboolVal"),23 : (PHRESULT, "pscode"),24 : (PCURRENCY, "pcyVal"),25 : (PDATE, "pdate"),26 : (PBSTR, "pbstrVal"),27 : (PPIUNKNOWN, "ppunkVal"),28 : (PPIDISPATCH, "ppdispVal"),29 : (PPSAFEARRAY, "pparray"),30 : (PVARIANT, "pvarVal"),31 : (CHAR, "cVal"),32 : (USHORT, "uiVal"),33 : (ULONG, "ulVal"),34 : (ULONGLONG, "ullVal"),35 : (INT, "intVal"),36 : (UINT, "uintVal"),37 : (DECIMAL, "decVal"),38 : (PCHAR, "pcVal"),39 : (PUSHORT, "puiVal"),40 : (PULONG, "pulVal"),41 : (PULONGLONG, "pullVal"),42 : (PINT, "pintVal"),43 : (PUINT, "puintVal"),44 : (PDECIMAL, "pdecVal"),}

    

class WIREVARIANTSTR(NdrStructure):
    MEMBERS = [(DWORD, "clSize"),(DWORD, "rpcReserved"),(USHORT, "vt"),(USHORT, "wReserved1"),(USHORT, "wReserved2"),(USHORT, "wReserved3"),(_VARUNION, "_varUnion"),]

    

class SAFEARRAYBOUND(NdrStructure):
    MEMBERS = [(ULONG, "cElements"),(LONG, "lLbound"),]

    
LPSAFEARRAYBOUND = SAFEARRAYBOUND

class SAFEARR_BSTR(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PBSTR, "aBstr"),]

    

class SAFEARR_UNKNOWN(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIUNKNOWN, "apUnknown"),]

    

class SAFEARR_DISPATCH(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIDISPATCH, "apDispatch"),]

    

class SAFEARR_VARIANT(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PVARIANT, "aVariant"),]

    

class SAFEARR_BRECORD(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PBRECORD, "aRecord"),]

    

class SAFEARR_HAVEIID(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIUNKNOWN, "apUnknown"),(IID, "iid"),]

    

class BYTE_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PBYTE, "pData"),]

    

class WORD_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PUNSIGNED_SHORT, "pData"),]

    

class DWORD_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PUNSIGNED_LONG, "pData"),]

    

class HYPER_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PHYPER, "pData"),]

    

class U(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (SAFEARR_BSTR, "BstrStr"),2 : (SAFEARR_UNKNOWN, "UnknownStr"),3 : (SAFEARR_DISPATCH, "DispatchStr"),4 : (SAFEARR_VARIANT, "VariantStr"),5 : (SAFEARR_BRECORD, "RecordStr"),6 : (SAFEARR_HAVEIID, "HaveIidStr"),7 : (BYTE_SIZEDARR, "ByteStr"),8 : (WORD_SIZEDARR, "WordStr"),9 : (DWORD_SIZEDARR, "LongStr"),10 : (HYPER_SIZEDARR, "HyperStr"),}

    

class SAFEARRAYUNION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "sfType"),(U, "u"),]

    

class PSAFEARRAY(NdrStructure):
    MEMBERS = [(USHORT, "cDims"),(USHORT, "fFeatures"),(ULONG, "cbElements"),(ULONG, "cLocks"),(SAFEARRAYUNION, "uArrayStructs"),(SAFEARRAYBOUND, "rgsabound"),]

    

class RECORDINFO(NdrStructure):
    MEMBERS = [(GUID, "libraryGuid"),(DWORD, "verMajor"),(GUID, "recGuid"),(DWORD, "verMinor"),(DWORD, "Lcid"),]

    
DISPID = LONG

class DISPPARAMS(NdrStructure):
    MEMBERS = [(PVARIANT, "rgvarg"),(PDISPID, "rgdispidNamedArgs"),(UINT, "cArgs"),(UINT, "cNamedArgs"),]

    

class EXCEPINFO(NdrStructure):
    MEMBERS = [(WORD, "wCode"),(WORD, "wReserved"),(BSTR, "bstrSource"),(BSTR, "bstrDescription"),(BSTR, "bstrHelpFile"),(DWORD, "dwHelpContext"),(ULONG_PTR, "pvReserved"),(ULONG_PTR, "pfnDeferredFillIn"),(HRESULT, "scode"),]

    
MEMBERID = DISPID
HREFTYPE = DWORD

class _TDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PTAGTYPEDESC, "lptdesc"),2 : (PTAGARRAYDESC, "lpadesc"),3 : (HREFTYPE, "hreftype"),}

    

class TYPEDESC(NdrStructure):
    MEMBERS = [(_TDUNION, "_tdUnion"),(USHORT, "vt"),]

    

class ARRAYDESC(NdrStructure):
    MEMBERS = [(TYPEDESC, "tdescElem"),(USHORT, "cDims"),(SAFEARRAYBOUND, "rgbounds"),]

    

class PARAMDESCEX(NdrStructure):
    MEMBERS = [(ULONG, "cBytes"),(VARIANT, "varDefaultValue"),]

    

class PARAMDESC(NdrStructure):
    MEMBERS = [(PPARAMDESCEX, "pparamdescex"),(USHORT, "wParamFlags"),]

    

class ELEMDESC(NdrStructure):
    MEMBERS = [(TYPEDESC, "tdesc"),(PARAMDESC, "paramdesc"),]

    

class FUNCDESC(NdrStructure):
    MEMBERS = [(MEMBERID, "memid"),(PSCODE, "lReserved1"),(PELEMDESC, "lprgelemdescParam"),(FUNCKIND, "funckind"),(INVOKEKIND, "invkind"),(CALLCONV, "callconv"),(SHORT, "cParams"),(SHORT, "cParamsOpt"),(SHORT, "oVft"),(SHORT, "cReserved2"),(ELEMDESC, "elemdescFunc"),(WORD, "wFuncFlags"),]

    
LPFUNCDESC = FUNCDESC

class _VDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ULONG, "oInst"),2 : (PVARIANT, "lpvarValue"),}

    

class VARDESC(NdrStructure):
    MEMBERS = [(MEMBERID, "memid"),(LPOLESTR, "lpstrReserved"),(_VDUNION, "_vdUnion"),(ELEMDESC, "elemdescVar"),(WORD, "wVarFlags"),(VARKIND, "varkind"),]

    
LPVARDESC = VARDESC

class TYPEATTR(NdrStructure):
    MEMBERS = [(GUID, "guid"),(LCID, "lcid"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(DWORD, "dwReserved3"),(LPOLESTR, "lpstrReserved4"),(ULONG, "cbSizeInstance"),(TYPEKIND, "typekind"),(WORD, "cFuncs"),(WORD, "cVars"),(WORD, "cImplTypes"),(WORD, "cbSizeVft"),(WORD, "cbAlignment"),(WORD, "wTypeFlags"),(WORD, "wMajorVerNum"),(WORD, "wMinorVerNum"),(TYPEDESC, "tdescAlias"),(DWORD, "dwReserved5"),(WORD, "wReserved6"),]

    
LPTYPEATTR = TYPEATTR

class TLIBATTR(NdrStructure):
    MEMBERS = [(GUID, "guid"),(LCID, "lcid"),(SYSKIND, "syskind"),(UNSIGNED_SHORT, "wMajorVerNum"),(UNSIGNED_SHORT, "wMinorVerNum"),(UNSIGNED_SHORT, "wLibFlags"),]

    
LPTLIBATTR = TLIBATTR

class CUSTDATAITEM(NdrStructure):
    MEMBERS = [(GUID, "guid"),(VARIANT, "varValue"),]

    

class CUSTDATA(NdrStructure):
    MEMBERS = [(DWORD, "cCustData"),(PCUSTDATAITEM, "prgCustData"),]

    
LPDISPATCH = IDISPATCH
Interface("00020400-0000-0000-C000-000000000046", "1.0",[Method("GetTypeInfoCount",
Out((PUINT,'pctinfo')),
),Method("GetTypeInfo",
In((UINT,'iTInfo')),
In((LCID,'lcid')),
Out((PPITYPEINFO,'ppTInfo')),
),Method("GetIDsOfNames",
In((REFIID,'riid')),
In((PLPOLESTR,'rgszNames')),
In((UINT,'cNames')),
In((LCID,'lcid')),
Out((PDISPID,'rgDispId')),
),Method("Invoke",
In((DISPID,'dispIdMember')),
In((REFIID,'riid')),
In((LCID,'lcid')),
In((DWORD,'dwFlags')),
In((PDISPPARAMS,'pDispParams')),
Out((PVARIANT,'pVarResult')),
Out((PEXCEPINFO,'pExcepInfo')),
Out((PUINT,'pArgErr')),
In((UINT,'cVarRef')),
In((PUINT,'rgVarRefIdx')),
InOut((PVARIANT,'rgVarRef')),
),])
class CONFIGTYPE(NdrEnum):
    MAP = ((1 , 'CONFIGTYPE_ACCOUNTING'),(2 , 'CONFIGTYPE_NOTIFICATION'),(3 , 'CONFIGTYPE_CALENDARING'),)        

class RESTORE_MODE(NdrEnum):
    MAP = ((1 , 'RESTORE_LAST_GOOD_STATE'),(2 , 'RESTORE_EMPTY_FILES'),)        

class OBJECT_TYPE(NdrEnum):
    MAP = ((1 , 'OBJECT_SELECTION_CRITERIA'),(2 , 'OBJECT_POLICY'),(3 , 'OBJECT_SCHEDULE'),)        

class MANAGEMENT_TYPE(NdrEnum):
    MAP = ((1 , 'MANUAL_ACTIVE_POLICY'),(2 , 'CALENDAR_POLICY'),(3 , 'PROFILING'),)        

class EXCLUSIONLIST_TYPE(NdrEnum):
    MAP = ((1 , 'SYSTEM_EXCLUSION_LIST'),(2 , 'USER_EXCLUSION_LIST'),(4 , 'DEFAULT_USER_EXCLUSION_LIST'),)        

class IMPORT_TYPE(NdrEnum):
    MAP = ((1 , 'OVERWRITE_IMPORT'),(2 , 'IGNORE_EXISTING_IMPORT'),(3 , 'OVERRIDE_EXISTING_IMPORT'),(4 , 'SMART_MERGE_RENAME_EXISTING_IMPORT'),(5 , 'SMART_MERGE_RENAME_IMPORTED_IMPORT'),)        

class MACHINE_GROUP_MERGE_OPTIONS(NdrEnum):
    MAP = ((1 , 'OVERWRITE_MG_MERGE_OPTION'),(2 , 'OVERRIDE_MG_MERGE_OPTION'),(3 , 'APPEND_MG_MERGE_OPTION'),(4 , 'SMART_MG_MERGE_OPTION'),)        
Interface("C5CEBEE2-9F5-4DD-A08C-C2471BC144B4", "1.0",[Method("RetrieveEventList",
Out((PBSTR,'pbstrEventList')),
),Method("GetSystemAffinity",
Out((PDWORD64,'pdwSysAffinity')),
),Method("ImportXMLFiles",
In((BSTR,'bstrPMCXml')),
In((BSTR,'bstrPolicyXml')),
In((BSTR,'bstrCalendarXml')),
In((BSTR,'bstrConditionalXml')),
),Method("ExportXMLFiles",
Out((PBSTR,'pbstrPMCXml')),
Out((PBSTR,'pbstrPolicyXml')),
Out((PBSTR,'pbstrCalendarXml')),
Out((PBSTR,'pbstrConditionalXml')),
),Method("RestoreXMLFiles",
In((RESTORE_MODE,'enumRestore')),
),Method("GetDependencies",
In((BSTR,'bstrObjectName')),
In((OBJECT_TYPE,'enumObject')),
Out((PBSTR,'pbstrDependencyList')),
),Method("GetServiceList",
Out((PBSTR,'pbstrServiceList')),
),Method("GetIISAppPoolNames",
Out((PBSTR,'pbstrIISAppPoolList')),
Out((PBSTR,'pbstrSystemDirectory')),
),Method("GetServerName",
Out((PBSTR,'pbstrServerName')),
),Method("GetCurrentMemory",
Out((PDWORD64,'pdwCurrMemory')),
),])