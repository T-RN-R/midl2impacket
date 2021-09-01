
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
PROPVARIANT = TAG_INNER_PROPVARIANT
PROPID = UNSIGNED_LONG
VARIANT_BOOL = SHORT

class XACTUOW(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "rgb"),]

    

class BLOB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cbSize"),(PUNSIGNED_CHAR, "pBlobData"),]

    

class CAUB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_CHAR, "pElems"),]

    

class CAUI(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_SHORT, "pElems"),]

    

class CAL(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PLONG, "pElems"),]

    

class CAUL(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_LONG, "pElems"),]

    

class CAUH(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PULARGE_INTEGER, "pElems"),]

    

class CACLSID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PGUID, "pElems"),]

    

class CALPWSTR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PPWCHAR_T, "pElems"),]

    

class CAPROPVARIANT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PPROPVARIANT, "pElems"),]

    

class VARENUM(NdrEnum):
    MAP = ((0 , 'VT_EMPTY'),(1 , 'VT_NULL'),(2 , 'VT_I2'),(3 , 'VT_I4'),(11 , 'VT_BOOL'),(12 , 'VT_VARIANT'),(16 , 'VT_I1'),(17 , 'VT_UI1'),(18 , 'VT_UI2'),(19 , 'VT_UI4'),(20 , 'VT_I8'),(21 , 'VT_UI8'),(31 , 'VT_LPWSTR'),(65 , 'VT_BLOB'),(72 , 'VT_CLSID'),(4096 , 'VT_VECTOR'),)        
VARTYPE = UNSIGNED_SHORT

class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (CHAR, "cVal"),3 : (UCHAR, "bVal"),4 : (SHORT, "iVal"),5 : (USHORT, "uiVal"),6 : (LONG, "lVal"),7 : (ULONG, "ulVal"),8 : (LARGE_INTEGER, "hVal"),9 : (ULARGE_INTEGER, "uhVal"),10 : (VARIANT_BOOL, "boolVal"),11 : (PGUID, "puuid"),12 : (BLOB, "blob"),13 : (PWCHAR_T, "pwszVal"),14 : (CAUB, "caub"),15 : (CAUI, "caui"),16 : (CAL, "cal"),17 : (CAUL, "caul"),18 : (CAUH, "cauh"),19 : (CACLSID, "cauuid"),20 : (CALPWSTR, "calpwstr"),21 : (CAPROPVARIANT, "capropvar"),}

    

class TAG_INNER_PROPVARIANT(NdrStructure):
    MEMBERS = [(VARTYPE, "vt"),(UCHAR, "wReserved1"),(UCHAR, "wReserved2"),(ULONG, "wReserved3"),(_VARUNION, "_varUnion"),]

    

class DL_ID(NdrStructure):
    MEMBERS = [(GUID, "m_DlGuid"),(PWCHAR_T, "m_pwzDomain"),]

    

class MULTICAST_ID(NdrStructure):
    MEMBERS = [(ULONG, "m_address"),(ULONG, "m_port"),]

    

class OBJECTID(NdrStructure):
    MEMBERS = [(GUID, "Lineage"),(DWORD, "Uniquifier"),]

    

class QUEUE_FORMAT_TYPE(NdrEnum):
    MAP = ((0 , 'QUEUE_FORMAT_TYPE_UNKNOWN'),(1 , 'QUEUE_FORMAT_TYPE_PUBLIC'),(2 , 'QUEUE_FORMAT_TYPE_PRIVATE'),(3 , 'QUEUE_FORMAT_TYPE_DIRECT'),(4 , 'QUEUE_FORMAT_TYPE_MACHINE'),(5 , 'QUEUE_FORMAT_TYPE_CONNECTOR'),(6 , 'QUEUE_FORMAT_TYPE_DL'),(7 , 'QUEUE_FORMAT_TYPE_MULTICAST'),(8 , 'QUEUE_FORMAT_TYPE_SUBQUEUE'),)        

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (GUID, "m_gPublicID"),3 : (OBJECTID, "m_oPrivateID"),4 : (PWCHAR_T, "m_pDirectID"),5 : (GUID, "m_gMachineID"),6 : (GUID, "m_GConnectorID"),7 : (DL_ID, "m_DlID"),8 : (MULTICAST_ID, "m_MulticastID"),9 : (PWCHAR_T, "m_pDirectSubqueueID"),}

    

class QUEUE_FORMAT(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "m_qft"),(UNSIGNED_CHAR, "m_SuffixAndFlags"),(UNSIGNED_SHORT, "m_reserved"),(U0, "u0"),]

    
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
PROPVARIANT = TAG_INNER_PROPVARIANT
PROPID = UNSIGNED_LONG
VARIANT_BOOL = SHORT

class XACTUOW(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "rgb"),]

    

class BLOB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cbSize"),(PUNSIGNED_CHAR, "pBlobData"),]

    

class CAUB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_CHAR, "pElems"),]

    

class CAUI(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_SHORT, "pElems"),]

    

class CAL(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PLONG, "pElems"),]

    

class CAUL(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PUNSIGNED_LONG, "pElems"),]

    

class CAUH(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PULARGE_INTEGER, "pElems"),]

    

class CACLSID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PGUID, "pElems"),]

    

class CALPWSTR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PPWCHAR_T, "pElems"),]

    

class CAPROPVARIANT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cElems"),(PPROPVARIANT, "pElems"),]

    

class VARENUM(NdrEnum):
    MAP = ((0 , 'VT_EMPTY'),(1 , 'VT_NULL'),(2 , 'VT_I2'),(3 , 'VT_I4'),(11 , 'VT_BOOL'),(12 , 'VT_VARIANT'),(16 , 'VT_I1'),(17 , 'VT_UI1'),(18 , 'VT_UI2'),(19 , 'VT_UI4'),(20 , 'VT_I8'),(21 , 'VT_UI8'),(31 , 'VT_LPWSTR'),(65 , 'VT_BLOB'),(72 , 'VT_CLSID'),(4096 , 'VT_VECTOR'),)        
VARTYPE = UNSIGNED_SHORT

class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (CHAR, "cVal"),3 : (UCHAR, "bVal"),4 : (SHORT, "iVal"),5 : (USHORT, "uiVal"),6 : (LONG, "lVal"),7 : (ULONG, "ulVal"),8 : (LARGE_INTEGER, "hVal"),9 : (ULARGE_INTEGER, "uhVal"),10 : (VARIANT_BOOL, "boolVal"),11 : (PGUID, "puuid"),12 : (BLOB, "blob"),13 : (PWCHAR_T, "pwszVal"),14 : (CAUB, "caub"),15 : (CAUI, "caui"),16 : (CAL, "cal"),17 : (CAUL, "caul"),18 : (CAUH, "cauh"),19 : (CACLSID, "cauuid"),20 : (CALPWSTR, "calpwstr"),21 : (CAPROPVARIANT, "capropvar"),}

    

class TAG_INNER_PROPVARIANT(NdrStructure):
    MEMBERS = [(VARTYPE, "vt"),(UCHAR, "wReserved1"),(UCHAR, "wReserved2"),(ULONG, "wReserved3"),(_VARUNION, "_varUnion"),]

    

class DL_ID(NdrStructure):
    MEMBERS = [(GUID, "m_DlGuid"),(PWCHAR_T, "m_pwzDomain"),]

    

class MULTICAST_ID(NdrStructure):
    MEMBERS = [(ULONG, "m_address"),(ULONG, "m_port"),]

    

class OBJECTID(NdrStructure):
    MEMBERS = [(GUID, "Lineage"),(DWORD, "Uniquifier"),]

    

class QUEUE_FORMAT_TYPE(NdrEnum):
    MAP = ((0 , 'QUEUE_FORMAT_TYPE_UNKNOWN'),(1 , 'QUEUE_FORMAT_TYPE_PUBLIC'),(2 , 'QUEUE_FORMAT_TYPE_PRIVATE'),(3 , 'QUEUE_FORMAT_TYPE_DIRECT'),(4 , 'QUEUE_FORMAT_TYPE_MACHINE'),(5 , 'QUEUE_FORMAT_TYPE_CONNECTOR'),(6 , 'QUEUE_FORMAT_TYPE_DL'),(7 , 'QUEUE_FORMAT_TYPE_MULTICAST'),(8 , 'QUEUE_FORMAT_TYPE_SUBQUEUE'),)        

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (GUID, "m_gPublicID"),3 : (OBJECTID, "m_oPrivateID"),4 : (PWCHAR_T, "m_pDirectID"),5 : (GUID, "m_gMachineID"),6 : (GUID, "m_GConnectorID"),7 : (DL_ID, "m_DlID"),8 : (MULTICAST_ID, "m_MulticastID"),9 : (PWCHAR_T, "m_pDirectSubqueueID"),}

    

class QUEUE_FORMAT(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "m_qft"),(UNSIGNED_CHAR, "m_SuffixAndFlags"),(UNSIGNED_SHORT, "m_reserved"),(U0, "u0"),]

    
QUEUE_CONTEXT_HANDLE_NOSERIALIZE = VOID
QUEUE_CONTEXT_HANDLE_SERIALIZE = QUEUE_CONTEXT_HANDLE_NOSERIALIZE

class SECTIONTYPE(NdrEnum):
    MAP = ((0 , 'stFullPacket'),(1 , 'stBinaryFirstSection'),(2 , 'stBinarySecondSection'),(3 , 'stSrmpFirstSection'),(4 , 'stSrmpSecondSection'),)        

class SECTIONBUFFER(NdrStructure):
    MEMBERS = [(SECTIONTYPE, "SectionBufferType"),(DWORD, "SectionSizeAlloc"),(DWORD, "SectionSize"),(PBYTE, "pSectionBuffer"),]

    
Interface("1a9134dd-7b39-45ba-ad88-44d01ca47f28", "1.0",[Method("R_GetServerPort",
In((HANDLE_T,'hBind')),
),Method("Opnum1NotUsedOnWire",
),Method("R_OpenQueue",
In((HANDLE_T,'hBind')),
In((PQUEUE_FORMAT,'pQueueFormat')),
In((DWORD,'dwAccess')),
In((DWORD,'dwShareMode')),
In((PGUID,'pClientId')),
In((LONG,'fNonRoutingServer')),
In((UNSIGNED_CHAR,'Major')),
In((UNSIGNED_CHAR,'Minor')),
In((USHORT,'BuildNumber')),
In((LONG,'fWorkgroup')),
Out((PQUEUE_CONTEXT_HANDLE_SERIALIZE,'pphContext')),
),Method("R_CloseQueue",
In((HANDLE_T,'hBind')),
InOut((PQUEUE_CONTEXT_HANDLE_SERIALIZE,'pphContext')),
),Method("R_CreateCursor",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
Out((PDWORD,'phCursor')),
),Method("R_CloseCursor",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((DWORD,'hCursor')),
),Method("R_PurgeQueue",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
),Method("R_StartReceive",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((ULONGLONG,'LookupId')),
In((DWORD,'hCursor')),
In((DWORD,'ulAction')),
In((DWORD,'ulTimeout')),
In((DWORD,'dwRequestId')),
In((DWORD,'dwMaxBodySize')),
In((DWORD,'dwMaxCompoundMessageSize')),
Out((PDWORD,'pdwArriveTime')),
Out((PULONGLONG,'pSequenceId')),
Out((PDWORD,'pdwNumberOfSections')),
Out((PPSECTIONBUFFER,'ppPacketSections')),
),Method("R_CancelReceive",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((DWORD,'dwRequestId')),
),Method("R_EndReceive",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((DWORD,'dwAck')),
In((DWORD,'dwRequestId')),
),Method("R_MoveMessage",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContextFrom')),
In((ULONGLONG,'ullContextTo')),
In((ULONGLONG,'LookupId')),
In((PXACTUOW,'pTransactionId')),
),Method("R_OpenQueueForMove",
In((HANDLE_T,'hBind')),
In((PQUEUE_FORMAT,'pQueueFormat')),
In((DWORD,'dwAccess')),
In((DWORD,'dwShareMode')),
In((PGUID,'pClientId')),
In((LONG,'fNonRoutingServer')),
In((UNSIGNED_CHAR,'Major')),
In((UNSIGNED_CHAR,'Minor')),
In((USHORT,'BuildNumber')),
In((LONG,'fWorkgroup')),
Out((PULONGLONG,'pMoveContext')),
Out((PQUEUE_CONTEXT_HANDLE_SERIALIZE,'pphContext')),
),Method("R_QMEnlistRemoteTransaction",
In((HANDLE_T,'hBind')),
In((PXACTUOW,'pTransactionId')),
In((DWORD,'cbPropagationToken')),
In((PUNSIGNED_CHAR,'pbPropagationToken')),
In((PQUEUE_FORMAT,'pQueueFormat')),
),Method("R_StartTransactionalReceive",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((ULONGLONG,'LookupId')),
In((DWORD,'hCursor')),
In((DWORD,'ulAction')),
In((DWORD,'ulTimeout')),
In((DWORD,'dwRequestId')),
In((DWORD,'dwMaxBodySize')),
In((DWORD,'dwMaxCompoundMessageSize')),
In((PXACTUOW,'pTransactionId')),
Out((PDWORD,'pdwArriveTime')),
Out((PULONGLONG,'pSequenceId')),
Out((PDWORD,'pdwNumberOfSections')),
Out((PPSECTIONBUFFER,'ppPacketSections')),
),Method("R_SetUserAcknowledgementClass",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((ULONGLONG,'LookupId')),
In((USHORT,'usClass')),
),Method("R_EndTransactionalReceive",
In((HANDLE_T,'hBind')),
In((QUEUE_CONTEXT_HANDLE_NOSERIALIZE,'phContext')),
In((DWORD,'dwAck')),
In((DWORD,'dwRequestId')),
),])
class CACCREATEREMOTECURSOR(NdrStructure):
    MEMBERS = [(DWORD, "hCursor"),(DWORD, "srv_hACQueue"),(DWORD, "cli_pQMQueue"),]

    

class TRANSFER_TYPE(NdrEnum):
    MAP = ((0 , 'CACTB_SEND'),(1 , 'CACTB_RECEIVE'),(2 , 'CACTB_CREATECURSOR'),)        

class CACTRANSFERBUFFERV1(NdrStructure):
    MEMBERS = [(DWORD, "uTransferType"),(PULVERSION, "u0"),(PUNSIGNED_SHORT, "pClass"),(PPOBJECTID, "ppMessageID"),(PPUNSIGNED_CHAR, "ppCorrelationID"),(PDWORD, "pSentTime"),(PDWORD, "pArrivedTime"),(PUNSIGNED_CHAR, "pPriority"),(PUNSIGNED_CHAR, "pDelivery"),(PUNSIGNED_CHAR, "pAcknowledge"),(PUNSIGNED_CHAR, "pAuditing"),(PDWORD, "pApplicationTag"),(PPUNSIGNED_CHAR, "ppBody"),(DWORD, "ulBodyBufferSizeInBytes"),(DWORD, "ulAllocBodyBufferInBytes"),(PDWORD, "pBodySize"),(PPWCHAR, "ppTitle"),(DWORD, "ulTitleBufferSizeInWCHARs"),(PDWORD, "pulTitleBufferSizeInWCHARs"),(DWORD, "ulAbsoluteTimeToQueue"),(PDWORD, "pulRelativeTimeToQueue"),(DWORD, "ulRelativeTimeToLive"),(PDWORD, "pulRelativeTimeToLive"),(PUNSIGNED_CHAR, "pTrace"),(PDWORD, "pulSenderIDType"),(PPUNSIGNED_CHAR, "ppSenderID"),(PDWORD, "pulSenderIDLenProp"),(PDWORD, "pulPrivLevel"),(DWORD, "ulAuthLevel"),(PUNSIGNED_CHAR, "pAuthenticated"),(PDWORD, "pulHashAlg"),(PDWORD, "pulEncryptAlg"),(PPUNSIGNED_CHAR, "ppSenderCert"),(DWORD, "ulSenderCertLen"),(PDWORD, "pulSenderCertLenProp"),(PPWCHAR, "ppwcsProvName"),(DWORD, "ulProvNameLen"),(PDWORD, "pulAuthProvNameLenProp"),(PDWORD, "pulProvType"),(LONG, "fDefaultProvider"),(PPUNSIGNED_CHAR, "ppSymmKeys"),(DWORD, "ulSymmKeysSize"),(PDWORD, "pulSymmKeysSizeProp"),(UNSIGNED_CHAR, "bEncrypted"),(UNSIGNED_CHAR, "bAuthenticated"),(UNSIGNED_SHORT, "uSenderIDLen"),(PPUNSIGNED_CHAR, "ppSignature"),(DWORD, "ulSignatureSize"),(PDWORD, "pulSignatureSizeProp"),(PPGUID, "ppSrcQMID"),(PXACTUOW, "pUow"),(PPUNSIGNED_CHAR, "ppMsgExtension"),(DWORD, "ulMsgExtensionBufferInBytes"),(PDWORD, "pMsgExtensionSize"),(PPGUID, "ppConnectorType"),(PDWORD, "pulBodyType"),(PDWORD, "pulVersion"),]

    

class CACTRANSFERBUFFERV2(NdrStructure):
    MEMBERS = [(CACTRANSFERBUFFERV1, "old"),(PUNSIGNED_CHAR, "pbFirstInXact"),(PUNSIGNED_CHAR, "pbLastInXact"),(PPOBJECTID, "ppXactID"),]

    

class OBJECT_FORMAT(NdrStructure):
    MEMBERS = [(DWORD, "ObjType"),(U0, "u0"),]

    
PCTX_OPENREMOTE_HANDLE_TYPE = VOID
RPC_QUEUE_HANDLE = VOID
RPC_INT_XACT_HANDLE = VOID
Interface("fdb3a030-065-111-bb9b-00024a5525", "1.0",[Method("Opnum0NotUsedOnWire",
),Method("R_QMGetRemoteQueueName",
In((HANDLE_T,'hBind')),
In((DWORD,'pQueue')),
InOut((PPWCHAR,'lplpRemoteQueueName')),
),Method("R_QMOpenRemoteQueue",
In((HANDLE_T,'hBind')),
Out((PPCTX_OPENREMOTE_HANDLE_TYPE,'pphContext')),
Out((PDWORD,'pdwContext')),
In((PQUEUE_FORMAT,'pQueueFormat')),
In((DWORD,'dwCallingProcessID')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwShareMode')),
In((PGUID,'pLicGuid')),
In((DWORD,'dwMQS')),
Out((PDWORD,'dwpQueue')),
Out((PDWORD,'phQueue')),
),Method("R_QMCloseRemoteQueueContext",
InOut((PPCTX_OPENREMOTE_HANDLE_TYPE,'pphContext')),
),Method("R_QMCreateRemoteCursor",
In((HANDLE_T,'hBind')),
In((PSTRUCT_CACTRANSFERBUFFERV1,'ptb1')),
In((DWORD,'hQueue')),
Out((PDWORD,'phCursor')),
),Method("Opnum5NotUsedOnWire",
),Method("R_QMCreateObjectInternal",
In((HANDLE_T,'hBind')),
In((DWORD,'dwObjectType')),
In((PWCHAR,'lpwcsPathName')),
In((DWORD,'SDSize')),
In((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((DWORD,'cp')),
In((DWORD,'aProp')),
In((PROPVARIANT,'apVar')),
),Method("R_QMSetObjectSecurityInternal",
In((HANDLE_T,'hBind')),
In((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
In((DWORD,'SecurityInformation')),
In((DWORD,'SDSize')),
In((PUNSIGNED_CHAR,'pSecurityDescriptor')),
),Method("R_QMGetObjectSecurityInternal",
In((HANDLE_T,'hBind')),
In((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
In((DWORD,'RequestedInformation')),
Out((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((DWORD,'nLength')),
Out((PDWORD,'lpnLengthNeeded')),
),Method("R_QMDeleteObject",
In((HANDLE_T,'hBind')),
In((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
),Method("R_QMGetObjectProperties",
In((HANDLE_T,'hBind')),
In((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
In((DWORD,'cp')),
In((DWORD,'aProp')),
InOut((PROPVARIANT,'apVar')),
),Method("R_QMSetObjectProperties",
In((HANDLE_T,'hBind')),
In((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
In((DWORD,'cp')),
In((DWORD,'aProp')),
In((PROPVARIANT,'apVar')),
),Method("R_QMObjectPathToObjectFormat",
In((HANDLE_T,'hBind')),
In((PWCHAR,'lpwcsPathName')),
InOut((PSTRUCT_OBJECT_FORMAT,'pObjectFormat')),
),Method("Opnum13NotUsedOnWire",
),Method("R_QMGetTmWhereabouts",
In((HANDLE_T,'hBind')),
In((DWORD,'cbBufSize')),
Out((PUNSIGNED_CHAR,'pbWhereabouts')),
Out((PDWORD,'pcbWhereabouts')),
),Method("R_QMEnlistTransaction",
In((HANDLE_T,'hBind')),
In((PXACTUOW,'pUow')),
In((DWORD,'cbCookie')),
In((PUNSIGNED_CHAR,'pbCookie')),
),Method("R_QMEnlistInternalTransaction",
In((HANDLE_T,'hBind')),
In((PXACTUOW,'pUow')),
Out((PRPC_INT_XACT_HANDLE,'phIntXact')),
),Method("R_QMCommitTransaction",
InOut((PRPC_INT_XACT_HANDLE,'phIntXact')),
),Method("R_QMAbortTransaction",
InOut((PRPC_INT_XACT_HANDLE,'phIntXact')),
),Method("rpc_QMOpenQueueInternal",
In((HANDLE_T,'hBind')),
In((PQUEUE_FORMAT,'pQueueFormat')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwShareMode')),
In((DWORD,'hRemoteQueue')),
InOut((PPWCHAR,'lplpRemoteQueueName')),
In((PDWORD,'dwpQueue')),
In((PGUID,'pLicGuid')),
In((PWCHAR,'lpClientName')),
Out((PDWORD,'pdwQMContext')),
Out((PRPC_QUEUE_HANDLE,'phQueue')),
In((DWORD,'dwRemoteProtocol')),
In((DWORD,'dwpRemoteContext')),
),Method("rpc_ACCloseHandle",
InOut((PRPC_QUEUE_HANDLE,'phQueue')),
),Method("Opnum21NotUsedOnWire",
),Method("rpc_ACCloseCursor",
In((RPC_QUEUE_HANDLE,'hQueue')),
In((DWORD,'hCursor')),
),Method("rpc_ACSetCursorProperties",
In((RPC_QUEUE_HANDLE,'hProxy')),
In((DWORD,'hCursor')),
In((DWORD,'hRemoteCursor')),
),Method("Opnum24NotUsedOnWire",
),Method("Opnum25NotUsedOnWire",
),Method("rpc_ACHandleToFormatName",
In((RPC_QUEUE_HANDLE,'hQueue')),
In((DWORD,'dwFormatNameRPCBufferLen')),
InOut((PWCHAR,'lpwcsFormatName')),
InOut((PDWORD,'pdwLength')),
),Method("rpc_ACPurgeQueue",
In((RPC_QUEUE_HANDLE,'hQueue')),
),Method("R_QMQueryQMRegistryInternal",
In((HANDLE_T,'hBind')),
In((DWORD,'dwQueryType')),
Out((PPWCHAR,'lplpMQISServer')),
),Method("Opnum29NotUsedOnWire",
),Method("Opnum30NotUsedOnWire",
),Method("R_QMGetRTQMServerPort",
In((HANDLE_T,'hBind')),
In((DWORD,'fIP')),
),Method("Opnum32NotUsedOnWire",
),Method("Opnum33NotUsedOnWire",
),Method("Opnum34NotUsedOnWire",
),])