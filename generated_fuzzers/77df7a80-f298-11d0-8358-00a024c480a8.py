
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

class VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (CHAR, "cVal"),3 : (UCHAR, "bVal"),4 : (SHORT, "iVal"),5 : (USHORT, "uiVal"),6 : (LONG, "lVal"),7 : (ULONG, "ulVal"),8 : (LARGE_INTEGER, "hVal"),9 : (ULARGE_INTEGER, "uhVal"),10 : (VARIANT_BOOL, "boolVal"),11 : (PGUID, "puuid"),12 : (BLOB, "blob"),13 : (PWCHAR_T, "pwszVal"),14 : (CAUB, "caub"),15 : (CAUI, "caui"),16 : (CAL, "cal"),17 : (CAUL, "caul"),18 : (CAUH, "cauh"),19 : (CACLSID, "cauuid"),20 : (CALPWSTR, "calpwstr"),21 : (CAPROPVARIANT, "capropvar"),}

    

class TAG_INNER_PROPVARIANT(NdrStructure):
    MEMBERS = [(VARTYPE, "vt"),(UCHAR, "wReserved1"),(UCHAR, "wReserved2"),(ULONG, "wReserved3"),(VARUNION, "_varUnion"),]

    

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

    

class MQPROPERTYRESTRICTION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "rel"),(UNSIGNED_LONG, "prop"),(PROPVARIANT, "prval"),]

    

class MQRESTRICTION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cRes"),(PMQPROPERTYRESTRICTION, "paPropRes"),]

    

class MQCOLUMNSET(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cCol"),(PPROPID, "aCol"),]

    

class MQSORTKEY(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "propColumn"),(UNSIGNED_LONG, "dwOrder"),]

    

class MQSORTSET(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cCol"),(PMQSORTKEY, "aCol"),]

    
BOUNDED_SIGNATURE_SIZE = UNSIGNED_LONG
LPBOUNDED_SIGNATURE_SIZE = BOUNDED_SIGNATURE_SIZE
BOUNDED_PROPERTIES = DWORD
LPBOUNDED_PROPERTIES = BOUNDED_PROPERTIES
PCONTEXT_HANDLE_TYPE = VOID
PPCONTEXT_HANDLE_TYPE = PCONTEXT_HANDLE_TYPE
PCONTEXT_HANDLE_SERVER_AUTH_TYPE = VOID
PPCONTEXT_HANDLE_SERVER_AUTH_TYPE = PCONTEXT_HANDLE_SERVER_AUTH_TYPE
PCONTEXT_HANDLE_DELETE_TYPE = VOID
PPCONTEXT_HANDLE_DELETE_TYPE = PCONTEXT_HANDLE_DELETE_TYPE
Interface("77df7a80-f298-11d0-8358-00a024c480a8", "1.0",[Method("S_DSCreateObject",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'dwSDLength')),
In((PUNSIGNED_CHAR,'SecurityDescriptor')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
In((PROPVARIANT,'apVar')),
InOut((PGUID,'pObjGuid')),
),Method("S_DSDeleteObject",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
),Method("S_DSGetProps",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
InOut((PROPVARIANT,'apVar')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSSetProps",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
In((PROPVARIANT,'apVar')),
),Method("S_DSGetObjectSecurity",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'SecurityInformation')),
Out((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((UNSIGNED_LONG,'nLength')),
Out((PUNSIGNED_LONG,'lpnLengthNeeded')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSSetObjectSecurity",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'SecurityInformation')),
In((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((UNSIGNED_LONG,'nLength')),
),Method("S_DSLookupBegin",
In((HANDLE_T,'hBind')),
Out((PPCONTEXT_HANDLE_TYPE,'pHandle')),
In((PWCHAR_T,'pwcsContext')),
In((PMQRESTRICTION,'pRestriction')),
In((PMQCOLUMNSET,'pColumns')),
In((PMQSORTSET,'pSort')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
),Method("S_DSLookupNext",
In((HANDLE_T,'hBind')),
In((PCONTEXT_HANDLE_TYPE,'Handle')),
In((LPBOUNDED_PROPERTIES,'dwSize')),
Out((PUNSIGNED_LONG,'dwOutSize')),
Out((PROPVARIANT,'pbBuffer')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSLookupEnd",
In((HANDLE_T,'hBind')),
InOut((PPCONTEXT_HANDLE_TYPE,'phContext')),
),Method("Opnum9NotUsedOnWire",
),Method("S_DSDeleteObjectGuid",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
),Method("S_DSGetPropsGuid",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
InOut((PROPVARIANT,'apVar')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSSetPropsGuid",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
In((PROPVARIANT,'apVar')),
),Method("S_DSGetObjectSecurityGuid",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
In((UNSIGNED_LONG,'SecurityInformation')),
Out((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((UNSIGNED_LONG,'nLength')),
Out((PUNSIGNED_LONG,'lpnLengthNeeded')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSSetObjectSecurityGuid",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
In((UNSIGNED_LONG,'SecurityInformation')),
In((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((UNSIGNED_LONG,'nLength')),
),Method("Opnum15NotUsedOnWire",
),Method("Opnum16NotUsedOnWire",
),Method("Opnum17NotUsedOnWire",
),Method("Opnum18NotUsedOnWire",
),Method("S_DSQMSetMachineProperties",
In((HANDLE_T,'hBind')),
In((PWCHAR_T,'pwcsPathName')),
In((UNSIGNED_LONG,'cp')),
In((UNSIGNED_LONG,'aProp')),
In((PROPVARIANT,'apVar')),
In((UNSIGNED_LONG,'dwContext')),
),Method("S_DSCreateServersCache",
In((HANDLE_T,'hBind')),
InOut((PUNSIGNED_LONG,'pdwIndex')),
InOut((PPWCHAR_T,'lplpSiteServers')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSQMSetMachinePropertiesSignProc",
In((PBYTE,'abChallenge')),
In((UNSIGNED_LONG,'dwCallengeSize')),
In((UNSIGNED_LONG,'dwContext')),
InOut((PBYTE,'abSignature')),
InOut((PUNSIGNED_LONG,'pdwSignatureSize')),
In((UNSIGNED_LONG,'dwSignatureMaxSize')),
),Method("S_DSQMGetObjectSecurity",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'dwObjectType')),
In((PGUID,'pGuid')),
In((UNSIGNED_LONG,'SecurityInformation')),
Out((PUNSIGNED_CHAR,'pSecurityDescriptor')),
In((UNSIGNED_LONG,'nLength')),
Out((PUNSIGNED_LONG,'lpnLengthNeeded')),
In((UNSIGNED_LONG,'dwContext')),
In((PCONTEXT_HANDLE_SERVER_AUTH_TYPE,'phServerAuth')),
Out((PUNSIGNED_CHAR,'pbServerSignature')),
InOut((LPBOUNDED_SIGNATURE_SIZE,'pdwServerSignatureSize')),
),Method("S_DSQMGetObjectSecurityChallengeResponceProc",
In((PBYTE,'abChallenge')),
In((UNSIGNED_LONG,'dwCallengeSize')),
In((UNSIGNED_LONG,'dwContext')),
InOut((PBYTE,'abCallengeResponce')),
InOut((PUNSIGNED_LONG,'pdwCallengeResponceSize')),
In((UNSIGNED_LONG,'dwCallengeResponceMaxSize')),
),Method("S_InitSecCtx",
In((UNSIGNED_LONG,'dwContext')),
In((PUNSIGNED_CHAR,'pServerbuff')),
In((UNSIGNED_LONG,'dwServerBuffSize')),
In((UNSIGNED_LONG,'dwClientBuffMaxSize')),
Out((PUNSIGNED_CHAR,'pClientBuff')),
Out((PUNSIGNED_LONG,'pdwClientBuffSize')),
),Method("S_DSValidateServer",
In((HANDLE_T,'hBind')),
In((PGUID,'pguidEnterpriseId')),
In((BOOL,'fSetupMode')),
In((UNSIGNED_LONG,'dwContext')),
In((UNSIGNED_LONG,'dwClientBuffMaxSize')),
In((PUNSIGNED_CHAR,'pClientBuff')),
In((UNSIGNED_LONG,'dwClientBuffSize')),
Out((PPCONTEXT_HANDLE_SERVER_AUTH_TYPE,'pphServerAuth')),
),Method("S_DSCloseServerHandle",
InOut((PPCONTEXT_HANDLE_SERVER_AUTH_TYPE,'pphServerAuth')),
),Method("Opnum24NotUsedOnWire",
),Method("Opnum25NotUsedOnWire",
),Method("Opnum26NotUsedOnWire",
),Method("S_DSGetServerPort",
In((HANDLE_T,'hBind')),
In((UNSIGNED_LONG,'fIP')),
),])