
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
    MAP = ((VT_ERROR , 'SF_ERROR'),(VT_I1 , 'SF_I1'),(VT_I2 , 'SF_I2'),(VT_I4 , 'SF_I4'),(VT_I8 , 'SF_I8'),(VT_BSTR , 'SF_BSTR'),(VT_UNKNOWN , 'SF_UNKNOWN'),(VT_DISPATCH , 'SF_DISPATCH'),(VT_VARIANT , 'SF_VARIANT'),(VT_RECORD , 'SF_RECORD'),(32768 , 'SF_HAVEIID'),)        

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
    MAP = ((0 , 'VAR_PERINSTANCE'),(1) , 'VAR_STATIC'),(1) , 'VAR_CONST'),(1) , 'VAR_DISPATCH'),)        

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
    MEMBERS = [(INT64, "int64"),]

    
DATE = DOUBLE

class DECIMAL(NdrStructure):
    MEMBERS = [(WORD, "wReserved"),(BYTE, "scale"),(BYTE, "sign"),(ULONG, "Hi32"),(ULONGLONG, "Lo64"),]

    
VARIANT_BOOL = SHORT

class WIREBRECORDSTR(NdrStructure):
    MEMBERS = [(ULONG, "fFlags"),(ULONG, "clSize"),(PMINTERFACEPOINTER, "pRecInfo"),(PBYTE, "pRecord"),]

    

class PBRECORD(NdrStructure):
    MEMBERS = []

    

class VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LONGLONG, "llVal"),2 : (LONG, "lVal"),3 : (BYTE, "bVal"),4 : (SHORT, "iVal"),5 : (FLOAT, "fltVal"),6 : (DOUBLE, "dblVal"),7 : (VARIANT_BOOL, "boolVal"),8 : (HRESULT, "scode"),9 : (CURRENCY, "cyVal"),10 : (DATE, "date"),11 : (BSTR, "bstrVal"),12 : (PIUNKNOWN, "punkVal"),13 : (PIDISPATCH, "pdispVal"),14 : (PSAFEARRAY, "parray"),15 : (BRECORD, "brecVal"),16 : (PBYTE, "pbVal"),17 : (PSHORT, "piVal"),18 : (PLONG, "plVal"),19 : (PLONGLONG, "pllVal"),20 : (PFLOAT, "pfltVal"),21 : (PDOUBLE, "pdblVal"),22 : (PVARIANT_BOOL, "pboolVal"),23 : (PHRESULT, "pscode"),24 : (PCURRENCY, "pcyVal"),25 : (PDATE, "pdate"),26 : (PBSTR, "pbstrVal"),27 : (PPIUNKNOWN, "ppunkVal"),28 : (PPIDISPATCH, "ppdispVal"),29 : (PPSAFEARRAY, "pparray"),30 : (PVARIANT, "pvarVal"),31 : (CHAR, "cVal"),32 : (USHORT, "uiVal"),33 : (ULONG, "ulVal"),34 : (ULONGLONG, "ullVal"),35 : (INT, "intVal"),36 : (UINT, "uintVal"),37 : (DECIMAL, "decVal"),38 : (PCHAR, "pcVal"),39 : (PUSHORT, "puiVal"),40 : (PULONG, "pulVal"),41 : (PULONGLONG, "pullVal"),42 : (PINT, "pintVal"),43 : (PUINT, "puintVal"),44 : (PDECIMAL, "pdecVal"),}

    

class WIREVARIANTSTR(NdrStructure):
    MEMBERS = [(DWORD, "clSize"),(DWORD, "rpcReserved"),(USHORT, "vt"),(USHORT, "wReserved1"),(USHORT, "wReserved2"),(USHORT, "wReserved3"),(VARUNION, "_varUnion"),]

    

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

class PLPTDESC(NdrStructure):
    MEMBERS = []

    

class PLPADESC(NdrStructure):
    MEMBERS = []

    

class TDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLPTDESC, "*lptdesc"),2 : (PLPADESC, "*lpadesc"),3 : (HREFTYPE, "hreftype"),}

    

class TYPEDESC(NdrStructure):
    MEMBERS = [(TDUNION, "_tdUnion"),(USHORT, "vt"),]

    

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

class VDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ULONG, "oInst"),2 : (PVARIANT, "lpvarValue"),}

    

class VARDESC(NdrStructure):
    MEMBERS = [(MEMBERID, "memid"),(LPOLESTR, "lpstrReserved"),(VDUNION, "_vdUnion"),(ELEMDESC, "elemdescVar"),(WORD, "wVarFlags"),(VARKIND, "varkind"),]

    
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
class BOID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "rgb"),]

    

class XACTTRANSINFO(NdrStructure):
    MEMBERS = [(BOID, "uow"),(LONG, "isoLevel"),(ULONG, "isoFlags"),(DWORD, "grfTCSupported"),(DWORD, "grfRMSupported"),(DWORD, "grfTCSupportedRetaining"),(DWORD, "grfRMSupportedRetaining"),]

    

class XACTTC(NdrEnum):
    MAP = ((0 , 'XACTTC_NONE'),(1 , 'XACTTC_SYNC_PHASEONE'),(2 , 'XACTTC_SYNC_PHASETWO'),(2 , 'XACTTC_SYNC'),(4 , 'XACTTC_ASYNC_PHASEONE'),(4 , 'XACTTC_ASYNC'),)        

class (NdrEnum):
    MAP = ((32769 , 'MQMSG_CALG_MD2'),(32770 , 'MQMSG_CALG_MD4'),(32771 , 'MQMSG_CALG_MD5'),(32772 , 'MQMSG_CALG_SHA'),(32772 , 'MQMSG_CALG_SHA1'),(32773 , 'MQMSG_CALG_MAC'),(9216 , 'MQMSG_CALG_RSA_SIGN'),(8704 , 'MQMSG_CALG_DSS_SIGN'),(41984 , 'MQMSG_CALG_RSA_KEYX'),(26113 , 'MQMSG_CALG_DES'),(26114 , 'MQMSG_CALG_RC2'),(26625 , 'MQMSG_CALG_RC4'),(26626 , 'MQMSG_CALG_SEAL'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_NO_TRANSACTION'),(1 , 'MQ_MTS_TRANSACTION'),(2 , 'MQ_XA_TRANSACTION'),(3 , 'MQ_SINGLE_MESSAGE'),)        

class (NdrEnum):
    MAP = ((0 , 'REL_NOP'),(1 , 'REL_EQ'),(2 , 'REL_NEQ'),(3 , 'REL_LT'),(4 , 'REL_GT'),(5 , 'REL_LE'),(6 , 'REL_GE'),)        

class (NdrEnum):
    MAP = ((1 , 'MQCERT_REGISTER_ALWAYS'),(2 , 'MQCERT_REGISTER_IF_NOT_EXIST'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_FIRST'),(1 , 'MQMSG_CURRENT'),(2 , 'MQMSG_NEXT'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_CLASS_NORMAL'),(1 , 'MQMSG_CLASS_REPORT'),(2 , 'MQMSG_CLASS_ACK_REACH_QUEUE'),(16384 , 'MQMSG_CLASS_ACK_RECEIVE'),(32768 , 'MQMSG_CLASS_NACK_BAD_DST_Q'),(32769 , 'MQMSG_CLASS_NACK_PURGED'),(32770 , 'MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT'),(32771 , 'MQMSG_CLASS_NACK_Q_EXCEED_QUOTA'),(32772 , 'MQMSG_CLASS_NACK_ACCESS_DENIED'),(32773 , 'MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED'),(32774 , 'MQMSG_CLASS_NACK_BAD_SIGNATURE'),(32775 , 'MQMSG_CLASS_NACK_BAD_ENCRYPTION'),(32776 , 'MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT'),(32777 , 'MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q'),(32778 , 'MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG'),(32779 , 'MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER'),(32780 , 'MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED'),(49152 , 'MQMSG_CLASS_NACK_Q_DELETED'),(49153 , 'MQMSG_CLASS_NACK_Q_PURGED'),(49154 , 'MQMSG_CLASS_NACK_RECEIVE_TIMEOUT'),(49155 , 'MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_DELIVERY_EXPRESS'),(1 , 'MQMSG_DELIVERY_RECOVERABLE'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_ACKNOWLEDGMENT_NONE'),(1 , 'MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL'),(2 , 'MQMSG_ACKNOWLEDGMENT_POS_RECEIVE'),(4 , 'MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL'),(8 , 'MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE'),(4 , 'MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE'),(5 , 'MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE'),(12 , 'MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE'),(14 , 'MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_JOURNAL_NONE'),(1 , 'MQMSG_DEADLETTER'),(2 , 'MQMSG_JOURNAL'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_TRACE_NONE'),(1 , 'MQMSG_SEND_ROUTE_TO_REPORT_QUEUE'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_SENDERID_TYPE_NONE'),(1 , 'MQMSG_SENDERID_TYPE_SID'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_PRIV_LEVEL_NONE'),(1 , 'MQMSG_PRIV_LEVEL_BODY_BASE'),(3 , 'MQMSG_PRIV_LEVEL_BODY_ENHANCED'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_AUTH_LEVEL_NONE'),(1 , 'MQMSG_AUTH_LEVEL_ALWAYS'),(2 , 'MQMSG_AUTH_LEVEL_MSMQ10'),(2 , 'MQMSG_AUTH_LEVEL_SIG10'),(4 , 'MQMSG_AUTH_LEVEL_MSMQ20'),(4 , 'MQMSG_AUTH_LEVEL_SIG20'),(8 , 'MQMSG_AUTH_LEVEL_SIG30'),)        

class (NdrEnum):
    MAP = ((20 , 'MQMSG_MSGID_SIZE'),(20 , 'MQMSG_CORRELATIONID_SIZE'),(20 , 'MQMSG_XACTID_SIZE'),)        

class (NdrEnum):
    MAP = ((249 , 'MQ_MAX_MSG_LABEL_LEN'),)        

class (NdrEnum):
    MAP = ((0 , 'MQMSG_AUTHENTICATION_NOT_REQUESTED'),(1 , 'MQMSG_AUTHENTICATION_REQUESTED'),(1 , 'MQMSG_AUTHENTICATED_SIG10'),(3 , 'MQMSG_AUTHENTICATION_REQUESTED_EX'),(3 , 'MQMSG_AUTHENTICATED_SIG20'),(5 , 'MQMSG_AUTHENTICATED_SIG30'),(9 , 'MQMSG_AUTHENTICATED_SIGXML'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_DENY_NONE'),(1 , 'MQ_DENY_RECEIVE_SHARE'),)        

class (NdrEnum):
    MAP = ((1 , 'MQ_RECEIVE_ACCESS'),(2 , 'MQ_SEND_ACCESS'),(32 , 'MQ_PEEK_ACCESS'),(128 , 'MQ_ADMIN_ACCESS'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_JOURNAL_NONE'),(1 , 'MQ_JOURNAL'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_TRANSACTIONAL_NONE'),(1 , 'MQ_TRANSACTIONAL'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_AUTHENTICATE_NONE'),(1 , 'MQ_AUTHENTICATE'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_PRIV_LEVEL_NONE'),(1 , 'MQ_PRIV_LEVEL_OPTIONAL'),(2 , 'MQ_PRIV_LEVEL_BODY'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_MIN_PRIORITY'),(7 , 'MQ_MAX_PRIORITY'),)        

class (NdrEnum):
    MAP = ((124 , 'MQ_MAX_Q_NAME_LEN'),(124 , 'MQ_MAX_Q_LABEL_LEN'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_TYPE_PUBLIC'),(1 , 'MQ_TYPE_PRIVATE'),(2 , 'MQ_TYPE_MACHINE'),(3 , 'MQ_TYPE_CONNECTOR'),(4 , 'MQ_TYPE_MULTICAST'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_STATUS_FOREIGN'),(1 , 'MQ_STATUS_NOT_FOREIGN'),(2 , 'MQ_STATUS_UNKNOWN'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_XACT_STATUS_XACT'),(1 , 'MQ_XACT_STATUS_NOT_XACT'),(2 , 'MQ_XACT_STATUS_UNKNOWN'),)        

class (NdrEnum):
    MAP = ((0 , 'MQ_QUEUE_STATE_LOCAL_CONNECTION'),(1 , 'MQ_QUEUE_STATE_DISCONNECTED'),(2 , 'MQ_QUEUE_STATE_WAITING'),(3 , 'MQ_QUEUE_STATE_NEEDVALIDATE'),(4 , 'MQ_QUEUE_STATE_ONHOLD'),(5 , 'MQ_QUEUE_STATE_NONACTIVE'),(6 , 'MQ_QUEUE_STATE_CONNECTED'),(7 , 'MQ_QUEUE_STATE_DISCONNECTING'),(8 , 'MQ_QUEUE_STATE_LOCKED'),)        

class (NdrEnum):
    MAP = ((3 , 'DEFAULT_M_PRIORITY'),(0 , 'DEFAULT_M_DELIVERY'),(0 , 'DEFAULT_M_ACKNOWLEDGE'),(0 , 'DEFAULT_M_JOURNAL'),(0 , 'DEFAULT_M_APPSPECIFIC'),(0 , 'DEFAULT_M_PRIV_LEVEL'),(0 , 'DEFAULT_M_AUTH_LEVEL'),(1 , 'DEFAULT_M_SENDERID_TYPE'),(0 , 'DEFAULT_Q_JOURNAL'),(0 , 'DEFAULT_Q_BASEPRIORITY'),(4294967295 , 'DEFAULT_Q_QUOTA'),(4294967295 , 'DEFAULT_Q_JOURNAL_QUOTA'),(0 , 'DEFAULT_Q_TRANSACTION'),(0 , 'DEFAULT_Q_AUTHENTICATE'),(1 , 'DEFAULT_Q_PRIV_LEVEL'),(0 , 'DEFAULT_M_LOOKUPID'),)        

class (NdrEnum):
    MAP = ((3222142977 , 'MQ_ERROR'),(3222142978 , 'MQ_ERROR_PROPERTY'),(3222142979 , 'MQ_ERROR_QUEUE_NOT_FOUND'),(3222142980 , 'MQ_ERROR_QUEUE_NOT_ACTIVE'),(3222142981 , 'MQ_ERROR_QUEUE_EXISTS'),(3222142982 , 'MQ_ERROR_INVALID_PARAMETER'),(3222142983 , 'MQ_ERROR_INVALID_HANDLE'),(3222142984 , 'MQ_ERROR_OPERATION_CANCELLED'),(3222142985 , 'MQ_ERROR_SHARING_VIOLATION'),(3222142987 , 'MQ_ERROR_SERVICE_NOT_AVAILABLE'),(3222142989 , 'MQ_ERROR_MACHINE_NOT_FOUND'),(3222142992 , 'MQ_ERROR_ILLEGAL_SORT'),(3222142993 , 'MQ_ERROR_ILLEGAL_USER'),(3222142995 , 'MQ_ERROR_NO_DS'),(3222142996 , 'MQ_ERROR_ILLEGAL_QUEUE_PATHNAME'),(3222143000 , 'MQ_ERROR_ILLEGAL_PROPERTY_VALUE'),(3222143001 , 'MQ_ERROR_ILLEGAL_PROPERTY_VT'),(3222143002 , 'MQ_ERROR_BUFFER_OVERFLOW'),(3222143003 , 'MQ_ERROR_IO_TIMEOUT'),(3222143004 , 'MQ_ERROR_ILLEGAL_CURSOR_ACTION'),(3222143005 , 'MQ_ERROR_MESSAGE_ALREADY_RECEIVED'),(3222143006 , 'MQ_ERROR_ILLEGAL_FORMATNAME'),(3222143007 , 'MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL'),(3222143008 , 'MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION'),(3222143009 , 'MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR'),(3222143010 , 'MQ_ERROR_SENDERID_BUFFER_TOO_SMALL'),(3222143011 , 'MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL'),(3222143012 , 'MQ_ERROR_CANNOT_IMPERSONATE_CLIENT'),(3222143013 , 'MQ_ERROR_ACCESS_DENIED'),(3222143014 , 'MQ_ERROR_PRIVILEGE_NOT_HELD'),(3222143015 , 'MQ_ERROR_INSUFFICIENT_RESOURCES'),(3222143016 , 'MQ_ERROR_USER_BUFFER_TOO_SMALL'),(3222143018 , 'MQ_ERROR_MESSAGE_STORAGE_FAILED'),(3222143019 , 'MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL'),(3222143020 , 'MQ_ERROR_INVALID_CERTIFICATE'),(3222143021 , 'MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE'),(3222143022 , 'MQ_ERROR_INTERNAL_USER_CERT_EXIST'),(3222143023 , 'MQ_ERROR_NO_INTERNAL_USER_CERT'),(3222143024 , 'MQ_ERROR_CORRUPTED_SECURITY_DATA'),(3222143025 , 'MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE'),(3222143027 , 'MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION'),(3222143029 , 'MQ_ERROR_BAD_SECURITY_CONTEXT'),(3222143030 , 'MQ_ERROR_COULD_NOT_GET_USER_SID'),(3222143031 , 'MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO'),(3222143032 , 'MQ_ERROR_ILLEGAL_MQCOLUMNS'),(3222143033 , 'MQ_ERROR_ILLEGAL_PROPID'),(3222143034 , 'MQ_ERROR_ILLEGAL_RELATION'),(3222143035 , 'MQ_ERROR_ILLEGAL_PROPERTY_SIZE'),(3222143036 , 'MQ_ERROR_ILLEGAL_RESTRICTION_PROPID'),(3222143037 , 'MQ_ERROR_ILLEGAL_MQQUEUEPROPS'),(3222143038 , 'MQ_ERROR_PROPERTY_NOTALLOWED'),(3222143039 , 'MQ_ERROR_INSUFFICIENT_PROPERTIES'),(3222143040 , 'MQ_ERROR_MACHINE_EXISTS'),(3222143041 , 'MQ_ERROR_ILLEGAL_MQQMPROPS'),(3222143042 , 'MQ_ERROR_DS_IS_FULL'),(3222143043 , 'MQ_ERROR_DS_ERROR'),(3222143044 , 'MQ_ERROR_INVALID_OWNER'),(3222143045 , 'MQ_ERROR_UNSUPPORTED_ACCESS_MODE'),(3222143046 , 'MQ_ERROR_RESULT_BUFFER_TOO_SMALL'),(3222143048 , 'MQ_ERROR_DELETE_CN_IN_USE'),(3222143049 , 'MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER'),(3222143050 , 'MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE'),(3222143051 , 'MQ_ERROR_QUEUE_NOT_AVAILABLE'),(3222143052 , 'MQ_ERROR_DTC_CONNECT'),(3222143054 , 'MQ_ERROR_TRANSACTION_IMPORT'),(3222143056 , 'MQ_ERROR_TRANSACTION_USAGE'),(3222143057 , 'MQ_ERROR_TRANSACTION_SEQUENCE'),(3222143061 , 'MQ_ERROR_MISSING_CONNECTOR_TYPE'),(3222143062 , 'MQ_ERROR_STALE_HANDLE'),(3222143064 , 'MQ_ERROR_TRANSACTION_ENLIST'),(3222143066 , 'MQ_ERROR_QUEUE_DELETED'),(3222143067 , 'MQ_ERROR_ILLEGAL_CONTEXT'),(3222143068 , 'MQ_ERROR_ILLEGAL_SORT_PROPID'),(3222143069 , 'MQ_ERROR_LABEL_TOO_LONG'),(3222143070 , 'MQ_ERROR_LABEL_BUFFER_TOO_SMALL'),(3222143071 , 'MQ_ERROR_MQIS_SERVER_EMPTY'),(3222143072 , 'MQ_ERROR_MQIS_READONLY_MODE'),(3222143073 , 'MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL'),(3222143074 , 'MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL'),(3222143075 , 'MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL'),(3222143076 , 'MQ_ERROR_ILLEGAL_OPERATION'),(3222143077 , 'MQ_ERROR_WRITE_NOT_ALLOWED'),(3222143078 , 'MQ_ERROR_WKS_CANT_SERVE_CLIENT'),(3222143079 , 'MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW'),(3222143080 , 'MQ_CORRUPTED_QUEUE_WAS_DELETED'),(3222143081 , 'MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE'),(3222143082 , 'MQ_ERROR_UNSUPPORTED_OPERATION'),(3222143083 , 'MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED'),(3222143084 , 'MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR'),(3222143085 , 'MQ_ERROR_CERTIFICATE_NOT_PROVIDED'),(3222143086 , 'MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED'),(3222143087 , 'MQ_ERROR_CANT_CREATE_CERT_STORE'),(3222143087 , 'MQ_ERROR_CANNOT_CREATE_CERT_STORE'),(3222143088 , 'MQ_ERROR_CANT_OPEN_CERT_STORE'),(3222143088 , 'MQ_ERROR_CANNOT_OPEN_CERT_STORE'),(3222143089 , 'MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION'),(3222143090 , 'MQ_ERROR_CANNOT_GRANT_ADD_GUID'),(3222143091 , 'MQ_ERROR_CANNOT_LOAD_MSMQOCM'),(3222143092 , 'MQ_ERROR_NO_ENTRY_POINT_MSMQOCM'),(3222143093 , 'MQ_ERROR_NO_MSMQ_SERVERS_ON_DC'),(3222143094 , 'MQ_ERROR_CANNOT_JOIN_DOMAIN'),(3222143095 , 'MQ_ERROR_CANNOT_CREATE_ON_GC'),(3222143096 , 'MQ_ERROR_GUID_NOT_MATCHING'),(3222143097 , 'MQ_ERROR_PUBLIC_KEY_NOT_FOUND'),(3222143098 , 'MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST'),(3222143099 , 'MQ_ERROR_ILLEGAL_MQPRIVATEPROPS'),(3222143100 , 'MQ_ERROR_NO_GC_IN_DOMAIN'),(3222143101 , 'MQ_ERROR_NO_MSMQ_SERVERS_ON_GC'),(3222143102 , 'MQ_ERROR_CANNOT_GET_DN'),(3222143103 , 'MQ_ERROR_CANNOT_HASH_DATA_EX'),(3222143104 , 'MQ_ERROR_CANNOT_SIGN_DATA_EX'),(3222143105 , 'MQ_ERROR_CANNOT_CREATE_HASH_EX'),(3222143106 , 'MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX'),(3222143107 , 'MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS'),(3222143108 , 'MQ_ERROR_NO_MQUSER_OU'),(3222143109 , 'MQ_ERROR_CANNOT_LOAD_MQAD'),(3222143110 , 'MQ_ERROR_CANNOT_LOAD_MQDSSRV'),(3222143111 , 'MQ_ERROR_PROPERTIES_CONFLICT'),(3222143112 , 'MQ_ERROR_MESSAGE_NOT_FOUND'),(3222143113 , 'MQ_ERROR_CANT_RESOLVE_SITES'),(3222143114 , 'MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS'),(3222143115 , 'MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER'),(3222143116 , 'MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS'),(3222143117 , 'MQ_ERROR_MULTI_SORT_KEYS'),(3222143118 , 'MQ_ERROR_GC_NEEDED'),(3222143119 , 'MQ_ERROR_DS_BIND_ROOT_FOREST'),(3222143120 , 'MQ_ERROR_DS_LOCAL_USER'),(3222143121 , 'MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED'),(3222143122 , 'MQ_ERROR_BAD_XML_FORMAT'),(3222143123 , 'MQ_ERROR_UNSUPPORTED_CLASS'),(3222143124 , 'MQ_ERROR_UNINITIALIZED_OBJECT'),(3222143125 , 'MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS'),(3222143126 , 'MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS'),)        

class (NdrEnum):
    MAP = ((1074659329 , 'MQ_INFORMATION_PROPERTY'),(1074659330 , 'MQ_INFORMATION_ILLEGAL_PROPERTY'),(1074659331 , 'MQ_INFORMATION_PROPERTY_IGNORED'),(1074659332 , 'MQ_INFORMATION_UNSUPPORTED_PROPERTY'),(1074659333 , 'MQ_INFORMATION_DUPLICATE_PROPERTY'),(1074659334 , 'MQ_INFORMATION_OPERATION_PENDING'),(1074659337 , 'MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL'),(1074659338 , 'MQ_INFORMATION_INTERNAL_USER_CERT_EXIST'),(1074659339 , 'MQ_INFORMATION_OWNER_IGNORED'),)        
Interface("0fb15084-af41-11ce-bd2b-204c4f4f5020", "1.0",[Method("Commit",
In((SHORT,'fRetaining')),
In((DWORD,'grfTC')),
In((DWORD,'grfRM')),
),Method("Abort",
In((PBOID,'pboidReason')),
In((SHORT,'fRetaining')),
In((SHORT,'fAsync')),
),Method("GetTransactionInfo",
Out((PXACTTRANSINFO,'pinfo')),
),])