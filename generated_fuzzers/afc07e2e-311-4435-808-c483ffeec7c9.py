
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
LSAPR_HANDLE = VOID
SECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
PPSECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
SECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT
PPSECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT

class STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PCHAR, "Buffer"),]

    
PSTRING = STRING

class LSAPR_ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_CHAR, "Dummy1"),]

    
PLSAPR_ACL = LSAPR_ACL

class LSAPR_SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "Sbz1"),(SECURITY_DESCRIPTOR_CONTROL, "Control"),(PRPC_SID, "Owner"),(PRPC_SID, "Group"),(PLSAPR_ACL, "Sacl"),(PLSAPR_ACL, "Dacl"),]

    
PLSAPR_SECURITY_DESCRIPTOR = LSAPR_SECURITY_DESCRIPTOR

class SECURITY_IMPERSONATION_LEVEL(NdrEnum):
    MAP = ((0 , 'SecurityAnonymous'),(1 , 'SecurityIdentification'),(2 , 'SecurityImpersonation'),(3 , 'SecurityDelegation'),)        

class SECURITY_QUALITY_OF_SERVICE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Length"),(SECURITY_IMPERSONATION_LEVEL, "ImpersonationLevel"),(SECURITY_CONTEXT_TRACKING_MODE, "ContextTrackingMode"),(UNSIGNED_CHAR, "EffectiveOnly"),]

    
PSECURITY_QUALITY_OF_SERVICE = SECURITY_QUALITY_OF_SERVICE

class LSAPR_OBJECT_ATTRIBUTES(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Length"),(PUNSIGNED_CHAR, "RootDirectory"),(PSTRING, "ObjectName"),(UNSIGNED_LONG, "Attributes"),(PLSAPR_SECURITY_DESCRIPTOR, "SecurityDescriptor"),(PSECURITY_QUALITY_OF_SERVICE, "SecurityQualityOfService"),]

    
PLSAPR_OBJECT_ATTRIBUTES = LSAPR_OBJECT_ATTRIBUTES

class LSAPR_TRUST_INFORMATION(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "Name"),(PRPC_SID, "Sid"),]

    
PLSAPR_TRUST_INFORMATION = LSAPR_TRUST_INFORMATION

class LSAPR_REFERENCED_DOMAIN_LIST(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_TRUST_INFORMATION, "Domains"),(UNSIGNED_LONG, "MaxEntries"),]

    
PLSAPR_REFERENCED_DOMAIN_LIST = LSAPR_REFERENCED_DOMAIN_LIST

class SID_NAME_USE(NdrEnum):
    MAP = ((1 , 'SidTypeUser'),(2 , 'SidTypeGroup'),(3 , 'SidTypeDomain'),(4 , 'SidTypeAlias'),(5 , 'SidTypeWellKnownGroup'),(6 , 'SidTypeDeletedAccount'),(7 , 'SidTypeInvalid'),(8 , 'SidTypeUnknown'),(9 , 'SidTypeComputer'),(10 , 'SidTypeLabel'),)        

class LSA_TRANSLATED_SID(NdrStructure):
    MEMBERS = [(SID_NAME_USE, "Use"),(UNSIGNED_LONG, "RelativeId"),(LONG, "DomainIndex"),]

    
PLSA_TRANSLATED_SID = LSA_TRANSLATED_SID

class LSAPR_TRANSLATED_SIDS(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSA_TRANSLATED_SID, "Sids"),]

    
PLSAPR_TRANSLATED_SIDS = LSAPR_TRANSLATED_SIDS

class LSAP_LOOKUP_LEVEL(NdrEnum):
    MAP = ((1 , 'LsapLookupWksta'),(2 , 'LsapLookupPDC'),(3 , 'LsapLookupTDL'),(4 , 'LsapLookupGC'),(5 , 'LsapLookupXForestReferral'),(6 , 'LsapLookupXForestResolve'),(7 , 'LsapLookupRODCReferralToFullDC'),)        

class LSAPR_SID_INFORMATION(NdrStructure):
    MEMBERS = [(PRPC_SID, "Sid"),]

    
PLSAPR_SID_INFORMATION = LSAPR_SID_INFORMATION

class LSAPR_SID_ENUM_BUFFER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_SID_INFORMATION, "SidInfo"),]

    
PLSAPR_SID_ENUM_BUFFER = LSAPR_SID_ENUM_BUFFER

class LSAPR_TRANSLATED_NAME(NdrStructure):
    MEMBERS = [(SID_NAME_USE, "Use"),(RPC_UNICODE_STRING, "Name"),(LONG, "DomainIndex"),]

    
PLSAPR_TRANSLATED_NAME = LSAPR_TRANSLATED_NAME

class LSAPR_TRANSLATED_NAMES(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_TRANSLATED_NAME, "Names"),]

    
PLSAPR_TRANSLATED_NAMES = LSAPR_TRANSLATED_NAMES

class LSAPR_TRANSLATED_NAME_EX(NdrStructure):
    MEMBERS = [(SID_NAME_USE, "Use"),(RPC_UNICODE_STRING, "Name"),(LONG, "DomainIndex"),(UNSIGNED_LONG, "Flags"),]

    
PLSAPR_TRANSLATED_NAME_EX = LSAPR_TRANSLATED_NAME_EX

class LSAPR_TRANSLATED_NAMES_EX(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_TRANSLATED_NAME_EX, "Names"),]

    
PLSAPR_TRANSLATED_NAMES_EX = LSAPR_TRANSLATED_NAMES_EX

class LSAPR_TRANSLATED_SID_EX(NdrStructure):
    MEMBERS = [(SID_NAME_USE, "Use"),(UNSIGNED_LONG, "RelativeId"),(LONG, "DomainIndex"),(UNSIGNED_LONG, "Flags"),]

    
PLSAPR_TRANSLATED_SID_EX = LSAPR_TRANSLATED_SID_EX

class LSAPR_TRANSLATED_SIDS_EX(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_TRANSLATED_SID_EX, "Sids"),]

    
PLSAPR_TRANSLATED_SIDS_EX = LSAPR_TRANSLATED_SIDS_EX

class LSAPR_TRANSLATED_SID_EX2(NdrStructure):
    MEMBERS = [(SID_NAME_USE, "Use"),(PRPC_SID, "Sid"),(LONG, "DomainIndex"),(UNSIGNED_LONG, "Flags"),]

    
PLSAPR_TRANSLATED_SID_EX2 = LSAPR_TRANSLATED_SID_EX2

class LSAPR_TRANSLATED_SIDS_EX2(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Entries"),(PLSAPR_TRANSLATED_SID_EX2, "Sids"),]

    
PLSAPR_TRANSLATED_SIDS_EX2 = LSAPR_TRANSLATED_SIDS_EX2
Interface("12345778-1234-ABCD-EF00-0123456789AB", "0.0",[Method("LsarClose",
InOut((PLSAPR_HANDLE,'ObjectHandle')),
),Method("Opnum1NotUsedOnWire",
),Method("Lsar_LSA_DP_2",
),Method("Lsar_LSA_DP_3",
),Method("Lsar_LSA_DP_4",
),Method("Opnum5NotUsedOnWire",
),Method("LsarOpenPolicy",
In((PWCHAR_T,'SystemName')),
In((PLSAPR_OBJECT_ATTRIBUTES,'ObjectAttributes')),
In((ACCESS_MASK,'DesiredAccess')),
Out((PLSAPR_HANDLE,'PolicyHandle')),
),Method("Lsar_LSA_DP_7",
),Method("Lsar_LSA_DP_8",
),Method("Opnum9NotUsedOnWire",
),Method("Lsar_LSA_DP_10",
),Method("Lsar_LSA_DP_11",
),Method("Lsar_LSA_DP_12",
),Method("Lsar_LSA_DP_13",
),Method("LsarLookupNames",
In((LSAPR_HANDLE,'PolicyHandle')),
In((UNSIGNED_LONG,'Count')),
In((PRPC_UNICODE_STRING,'Names')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_SIDS,'TranslatedSids')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
),Method("LsarLookupSids",
In((LSAPR_HANDLE,'PolicyHandle')),
In((PLSAPR_SID_ENUM_BUFFER,'SidEnumBuffer')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_NAMES,'TranslatedNames')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
),Method("Lsar_LSA_DP_16",
),Method("Lsar_LSA_DP_17",
),Method("Lsar_LSA_DP_18",
),Method("Lsar_LSA_DP_19",
),Method("Lsar_LSA_DP_20",
),Method("Opnum21NotUsedOnWire",
),Method("Opnum22NotUsedOnWire",
),Method("Lsar_LSA_DP_23",
),Method("Lsar_LSA_DP_24",
),Method("Lsar_LSA_DP_25",
),Method("Lsar_LSA_DP_26",
),Method("Lsar_LSA_DP_27",
),Method("Lsar_LSA_DP_28",
),Method("Lsar_LSA_DP_29",
),Method("Lsar_LSA_DP_30",
),Method("Lsar_LSA_DP_31",
),Method("Lsar_LSA_DP_32",
),Method("Lsar_LSA_DP_33",
),Method("Lsar_LSA_DP_34",
),Method("Lsar_LSA_DP_35",
),Method("Lsar_LSA_DP_36",
),Method("Lsar_LSA_DP_37",
),Method("Lsar_LSA_DP_38",
),Method("Lsar_LSA_DP_39",
),Method("Lsar_LSA_DP_40",
),Method("Lsar_LSA_DP_41",
),Method("Lsar_LSA_DP_42",
),Method("Lsar_LSA_DP_43",
),Method("LsarOpenPolicy2",
In((PWCHAR_T,'SystemName')),
In((PLSAPR_OBJECT_ATTRIBUTES,'ObjectAttributes')),
In((ACCESS_MASK,'DesiredAccess')),
Out((PLSAPR_HANDLE,'PolicyHandle')),
),Method("LsarGetUserName",
In((PWCHAR_T,'SystemName')),
InOut((PPRPC_UNICODE_STRING,'UserName')),
InOut((PPRPC_UNICODE_STRING,'DomainName')),
),Method("Lsar_LSA_DP_46",
),Method("Lsar_LSA_DP_47",
),Method("Lsar_LSA_DP_48",
),Method("Lsar_LSA_DP_49",
),Method("Lsar_LSA_DP_50",
),Method("Lsar_LSA_DP_51",
),Method("Opnum52NotUsedOnWire",
),Method("Lsar_LSA_DP_53",
),Method("Lsar_LSA_DP_54",
),Method("Lsar_LSA_DP_55",
),Method("Opnum56NotUsedOnWire",
),Method("LsarLookupSids2",
In((LSAPR_HANDLE,'PolicyHandle')),
In((PLSAPR_SID_ENUM_BUFFER,'SidEnumBuffer')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_NAMES_EX,'TranslatedNames')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
In((UNSIGNED_LONG,'LookupOptions')),
In((UNSIGNED_LONG,'ClientRevision')),
),Method("LsarLookupNames2",
In((LSAPR_HANDLE,'PolicyHandle')),
In((UNSIGNED_LONG,'Count')),
In((PRPC_UNICODE_STRING,'Names')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_SIDS_EX,'TranslatedSids')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
In((UNSIGNED_LONG,'LookupOptions')),
In((UNSIGNED_LONG,'ClientRevision')),
),Method("Lsar_LSA_DP_59",
),Method("Opnum60NotUsedOnWire",
),Method("Opnum61NotUsedOnWire",
),Method("Opnum62NotUsedOnWire",
),Method("Opnum63NotUsedOnWire",
),Method("Opnum64NotUsedOnWire",
),Method("Opnum65NotUsedOnWire",
),Method("Opnum66NotUsedOnWire",
),Method("Opnum67NotUsedOnWire",
),Method("LsarLookupNames3",
In((LSAPR_HANDLE,'PolicyHandle')),
In((UNSIGNED_LONG,'Count')),
In((PRPC_UNICODE_STRING,'Names')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_SIDS_EX2,'TranslatedSids')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
In((UNSIGNED_LONG,'LookupOptions')),
In((UNSIGNED_LONG,'ClientRevision')),
),Method("Opnum69NotUsedOnWire",
),Method("Opnum70NotUsedOnWire",
),Method("Opnum71NotUsedOnWire",
),Method("Opnum72NotUsedOnWire",
),Method("Lsar_LSA_DP_73",
),Method("Lsar_LSA_DP_74",
),Method("Opnum75NotUsedOnWire",
),Method("LsarLookupSids3",
In((HANDLE_T,'RpcHandle')),
In((PLSAPR_SID_ENUM_BUFFER,'SidEnumBuffer')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_NAMES_EX,'TranslatedNames')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
In((UNSIGNED_LONG,'LookupOptions')),
In((UNSIGNED_LONG,'ClientRevision')),
),Method("LsarLookupNames4",
In((HANDLE_T,'RpcHandle')),
In((UNSIGNED_LONG,'Count')),
In((PRPC_UNICODE_STRING,'Names')),
Out((PPLSAPR_REFERENCED_DOMAIN_LIST,'ReferencedDomains')),
InOut((PLSAPR_TRANSLATED_SIDS_EX2,'TranslatedSids')),
In((LSAP_LOOKUP_LEVEL,'LookupLevel')),
InOut((PUNSIGNED_LONG,'MappedCount')),
In((UNSIGNED_LONG,'LookupOptions')),
In((UNSIGNED_LONG,'ClientRevision')),
),])
class LSAPR_WRAPPED_CAPID_SET(NdrStructure):
    MEMBERS = [(ULONG, "Entries"),(PLSAPR_SID_INFORMATION, "SidInfo"),]

    
Interface("afc07e2e-311-4435-808-c483ffeec7c9", "1.0",[Method("LsarGetAvailableCAPIDs",
In((HANDLE_T,'BindingHandle')),
Out((PLSAPR_WRAPPED_CAPID_SET,'WrappedCAPIDs')),
),])