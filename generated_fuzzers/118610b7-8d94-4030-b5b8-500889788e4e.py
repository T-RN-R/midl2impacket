
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
),])VDS_OBJECT_ID = GUID

class VDS_HEALTH(NdrEnum):
    MAP = ((0 , 'VDS_H_UNKNOWN'),(1 , 'VDS_H_HEALTHY'),(2 , 'VDS_H_REBUILDING'),(3 , 'VDS_H_STALE'),(4 , 'VDS_H_FAILING'),(5 , 'VDS_H_FAILING_REDUNDANCY'),(6 , 'VDS_H_FAILED_REDUNDANCY'),(7 , 'VDS_H_FAILED_REDUNDANCY_FAILING'),(8 , 'VDS_H_FAILED'),)        

class VDS_NOTIFICATION_TARGET_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_NTT_UNKNOWN'),(10 , 'VDS_NTT_PACK'),(11 , 'VDS_NTT_VOLUME'),(13 , 'VDS_NTT_DISK'),(60 , 'VDS_NTT_PARTITION'),(61 , 'VDS_NTT_DRIVE_LETTER'),(62 , 'VDS_NTT_FILE_SYSTEM'),(63 , 'VDS_NTT_MOUNT_POINT'),(200 , 'VDS_NTT_SERVICE'),)        

class VDS_ASYNC_OUTPUT_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_ASYNCOUT_UNKNOWN'),(1 , 'VDS_ASYNCOUT_CREATEVOLUME'),(2 , 'VDS_ASYNCOUT_EXTENDVOLUME'),(3 , 'VDS_ASYNCOUT_SHRINKVOLUME'),(4 , 'VDS_ASYNCOUT_ADDVOLUMEPLEX'),(5 , 'VDS_ASYNCOUT_BREAKVOLUMEPLEX'),(6 , 'VDS_ASYNCOUT_REMOVEVOLUMEPLEX'),(7 , 'VDS_ASYNCOUT_REPAIRVOLUMEPLEX'),(8 , 'VDS_ASYNCOUT_RECOVERPACK'),(9 , 'VDS_ASYNCOUT_REPLACEDISK'),(10 , 'VDS_ASYNCOUT_CREATEPARTITION'),(11 , 'VDS_ASYNCOUT_CLEAN'),(50 , 'VDS_ASYNCOUT_CREATELUN'),(101 , 'VDS_ASYNCOUT_FORMAT'),(200 , 'VDS_ASYNCOUT_CREATE_VDISK'),(201 , 'VDS_ASYNCOUT_SURFACE_VDISK'),(202 , 'VDS_ASYNCOUT_COMPACT_VDISK'),(203 , 'VDS_ASYNCOUT_MERGE_VDISK'),(204 , 'VDS_ASYNCOUT_EXPAND_VDISK'),)        

class VDS_STORAGE_BUS_TYPE(NdrEnum):
    MAP = ((0 , 'VDSBusTypeUnknown'),(1 , 'VDSBusTypeScsi'),(2 , 'VDSBusTypeAtapi'),(3 , 'VDSBusTypeAta'),(4 , 'VDSBusType1394'),(5 , 'VDSBusTypeSsa'),(6 , 'VDSBusTypeFibre'),(7 , 'VDSBusTypeUsb'),(8 , 'VDSBusTypeRAID'),(9 , 'VDSBusTypeiScsi'),(10 , 'VDSBusTypeSas'),(11 , 'VDSBusTypeSata'),(12 , 'VDSBusTypeSd'),(13 , 'VDSBusTypeMmc'),(14 , 'VDSBusTypeMax'),(14 , 'VDSBusTypeVirtual'),(15 , 'VDSBusTypeFileBackedVirtual'),(16 , 'VDSBusTypeSpaces'),(127 , 'VDSBusTypeMaxReserved'),)        

class VDS_STORAGE_IDENTIFIER_CODE_SET(NdrEnum):
    MAP = ((0 , 'VDSStorageIdCodeSetReserved'),(1 , 'VDSStorageIdCodeSetBinary'),(2 , 'VDSStorageIdCodeSetAscii'),(3 , 'VDSStorageIdCodeSetUtf8'),)        

class VDS_STORAGE_IDENTIFIER_TYPE(NdrEnum):
    MAP = ((0 , 'VDSStorageIdTypeVendorSpecific'),(1 , 'VDSStorageIdTypeVendorId'),(2 , 'VDSStorageIdTypeEUI64'),(3 , 'VDSStorageIdTypeFCPHName'),(4 , 'VDSStorageIdTypePortRelative'),(5 , 'VDSStorageIdTypeTargetPortGroup'),(6 , 'VDSStorageIdTypeLogicalUnitGroup'),(7 , 'VDSStorageIdTypeMD5LogicalUnitIdentifier'),(8 , 'VDSStorageIdTypeScsiNameString'),)        

class VDS_INTERCONNECT_ADDRESS_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_IA_UNKNOWN'),(1 , 'VDS_IA_FCFS'),(2 , 'VDS_IA_FCPH'),(3 , 'VDS_IA_FCPH3'),(4 , 'VDS_IA_MAC'),(5 , 'VDS_IA_SCSI'),)        

class VDS_FILE_SYSTEM_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_FST_UNKNOWN'),(1 , 'VDS_FST_RAW'),(2 , 'VDS_FST_FAT'),(3 , 'VDS_FST_FAT32'),(4 , 'VDS_FST_NTFS'),(5 , 'VDS_FST_CDFS'),(6 , 'VDS_FST_UDF'),(7 , 'VDS_FST_EXFAT'),(8 , 'VDS_FST_CSVFS'),(9 , 'VDS_FST_REFS'),)        

class VDS_FILE_SYSTEM_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_FSF_SUPPORT_FORMAT'),(2 , 'VDS_FSF_SUPPORT_QUICK_FORMAT'),(4 , 'VDS_FSF_SUPPORT_COMPRESS'),(8 , 'VDS_FSF_SUPPORT_SPECIFY_LABEL'),(16 , 'VDS_FSF_SUPPORT_MOUNT_POINT'),(32 , 'VDS_FSF_SUPPORT_REMOVABLE_MEDIA'),(64 , 'VDS_FSF_SUPPORT_EXTEND'),(65536 , 'VDS_FSF_ALLOCATION_UNIT_512'),(131072 , 'VDS_FSF_ALLOCATION_UNIT_1K'),(262144 , 'VDS_FSF_ALLOCATION_UNIT_2K'),(524288 , 'VDS_FSF_ALLOCATION_UNIT_4K'),(1048576 , 'VDS_FSF_ALLOCATION_UNIT_8K'),(2097152 , 'VDS_FSF_ALLOCATION_UNIT_16K'),(4194304 , 'VDS_FSF_ALLOCATION_UNIT_32K'),(8388608 , 'VDS_FSF_ALLOCATION_UNIT_64K'),(16777216 , 'VDS_FSF_ALLOCATION_UNIT_128K'),(33554432 , 'VDS_FSF_ALLOCATION_UNIT_256K'),)        

class VDS_FILE_SYSTEM_PROP_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_FPF_COMPRESSED'),)        

class VDS_FILE_SYSTEM_FORMAT_SUPPORT_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_FSS_DEFAULT'),(2 , 'VDS_FSS_PREVIOUS_REVISION'),(4 , 'VDS_FSS_RECOMMENDED'),)        

class VDS_DISK_EXTENT_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_DET_UNKNOWN'),(1 , 'VDS_DET_FREE'),(2 , 'VDS_DET_DATA'),(3 , 'VDS_DET_OEM'),(4 , 'VDS_DET_ESP'),(5 , 'VDS_DET_MSR'),(6 , 'VDS_DET_LDM'),(32767 , 'VDS_DET_UNUSABLE'),)        

class VDS_PARTITION_STYLE(NdrEnum):
    MAP = ((0 , 'VDS_PST_UNKNOWN'),(1 , 'VDS_PST_MBR'),(2 , 'VDS_PST_GPT'),)        

class VDS_PARTITION_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_PTF_SYSTEM'),)        

class VDS_VOLUME_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_VT_UNKNOWN'),(10 , 'VDS_VT_SIMPLE'),(11 , 'VDS_VT_SPAN'),(12 , 'VDS_VT_STRIPE'),(13 , 'VDS_VT_MIRROR'),(14 , 'VDS_VT_PARITY'),)        

class VDS_TRANSITION_STATE(NdrEnum):
    MAP = ((0 , 'VDS_TS_UNKNOWN'),(1 , 'VDS_TS_STABLE'),(2 , 'VDS_TS_EXTENDING'),(3 , 'VDS_TS_SHRINKING'),(4 , 'VDS_TS_RECONFIGING'),)        

class VDS_FORMAT_OPTION_FLAGS(NdrEnum):
    MAP = ((0 , 'VDS_FSOF_NONE'),(1 , 'VDS_FSOF_FORCE'),(2 , 'VDS_FSOF_QUICK'),(4 , 'VDS_FSOF_COMPRESSION'),(8 , 'VDS_FSOF_DUPLICATE_METADATA'),)        

class VDS_DISK_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_DF_AUDIO_CD'),(2 , 'VDS_DF_HOTSPARE'),(4 , 'VDS_DF_RESERVE_CAPABLE'),(8 , 'VDS_DF_MASKED'),(16 , 'VDS_DF_STYLE_CONVERTIBLE'),(32 , 'VDS_DF_CLUSTERED'),(64 , 'VDS_DF_READ_ONLY'),(128 , 'VDS_DF_SYSTEM_DISK'),(256 , 'VDS_DF_BOOT_DISK'),(512 , 'VDS_DF_PAGEFILE_DISK'),(1024 , 'VDS_DF_HIBERNATIONFILE_DISK'),(2048 , 'VDS_DF_CRASHDUMP_DISK'),(4096 , 'VDS_DF_HAS_ARC_PATH'),(8192 , 'VDS_DF_DYNAMIC'),(16384 , 'VDS_DF_BOOT_FROM_DISK'),(32768 , 'VDS_DF_CURRENT_READ_ONLY'),)        

class VDS_DISK_STATUS(NdrEnum):
    MAP = ((0 , 'VDS_DS_UNKNOWN'),(1 , 'VDS_DS_ONLINE'),(2 , 'VDS_DS_NOT_READY'),(3 , 'VDS_DS_NO_MEDIA'),(4 , 'VDS_DS_OFFLINE'),(5 , 'VDS_DS_FAILED'),(6 , 'VDS_DS_MISSING'),)        

class VDS_LUN_RESERVE_MODE(NdrEnum):
    MAP = ((0 , 'VDS_LRM_NONE'),(1 , 'VDS_LRM_EXCLUSIVE_RW'),(2 , 'VDS_LRM_EXCLUSIVE_RO'),(3 , 'VDS_LRM_SHARED_RO'),(4 , 'VDS_LRM_SHARED_RW'),)        

class VDS_VOLUME_STATUS(NdrEnum):
    MAP = ((0 , 'VDS_VS_UNKNOWN'),(1 , 'VDS_VS_ONLINE'),(3 , 'VDS_VS_NO_MEDIA'),(4 , 'VDS_VS_OFFLINE'),(5 , 'VDS_VS_FAILED'),)        

class VDS_VOLUME_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_VF_SYSTEM_VOLUME'),(2 , 'VDS_VF_BOOT_VOLUME'),(4 , 'VDS_VF_ACTIVE'),(8 , 'VDS_VF_READONLY'),(16 , 'VDS_VF_HIDDEN'),(32 , 'VDS_VF_CAN_EXTEND'),(64 , 'VDS_VF_CAN_SHRINK'),(128 , 'VDS_VF_PAGEFILE'),(256 , 'VDS_VF_HIBERNATION'),(512 , 'VDS_VF_CRASHDUMP'),(1024 , 'VDS_VF_INSTALLABLE'),(2048 , 'VDS_VF_LBN_REMAP_ENABLED'),(4096 , 'VDS_VF_FORMATTING'),(8192 , 'VDS_VF_NOT_FORMATTABLE'),(16384 , 'VDS_VF_NTFS_NOT_SUPPORTED'),(32768 , 'VDS_VF_FAT32_NOT_SUPPORTED'),(65536 , 'VDS_VF_FAT_NOT_SUPPORTED'),(131072 , 'VDS_VF_NO_DEFAULT_DRIVE_LETTER'),(262144 , 'VDS_VF_PERMANENTLY_DISMOUNTED'),(524288 , 'VDS_VF_PERMANENT_DISMOUNT_SUPPORTED'),(1048576 , 'VDS_VF_SHADOW_COPY'),(2097152 , 'VDS_VF_FVE_ENABLED'),(4194304 , 'VDS_VF_DIRTY'),(8388608 , 'VDS_VF_REFS_NOT_SUPPORTED'),)        

class VDS_PACK_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "packId"),]

    

class VDS_DISK_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "diskId"),]

    

class VDS_VOLUME_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "volumeId"),(VDS_OBJECT_ID, "plexId"),(UNSIGNED_LONG, "ulPercentCompleted"),]

    

class VDS_PARTITION_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "diskId"),(ULONGLONG, "ullOffset"),]

    

class VDS_DRIVE_LETTER_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(WCHAR, "wcLetter"),(VDS_OBJECT_ID, "volumeId"),]

    

class VDS_FILE_SYSTEM_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "volumeId"),(DWORD, "dwPercentCompleted"),]

    

class VDS_MOUNT_POINT_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulEvent"),(VDS_OBJECT_ID, "volumeId"),]

    

class VDS_RECOVER_ACTION(NdrEnum):
    MAP = ((0 , 'VDS_RA_UNKNOWN'),(1 , 'VDS_RA_REFRESH'),(2 , 'VDS_RA_RESTART'),)        

class VDS_SERVICE_NOTIFICATION(NdrStructure):
    MEMBERS = [(ULONG, "ulEvent"),(VDS_RECOVER_ACTION, "action"),]

    

class VDS_NOTIFICATION(NdrStructure):
    MEMBERS = [(VDS_NOTIFICATION_TARGET_TYPE, "objectType"),(U0, "u0"),]

    

class VDS_ASYNC_OUTPUT(NdrStructure):
    MEMBERS = [(VDS_ASYNC_OUTPUT_TYPE, "type"),(U0, "u0"),]

    

class VDS_PARTITION_INFO_MBR(NdrStructure):
    MEMBERS = [(BYTE, "partitionType"),(BOOLEAN, "bootIndicator"),(BOOLEAN, "recognizedPartition"),(DWORD, "hiddenSectors"),]

    

class VDS_PARTITION_INFO_GPT(NdrStructure):
    MEMBERS = [(GUID, "partitionType"),(GUID, "partitionId"),(ULONGLONG, "attributes"),(WCHAR, "name"),]

    

class VDS_STORAGE_IDENTIFIER(NdrStructure):
    MEMBERS = [(VDS_STORAGE_IDENTIFIER_CODE_SET, "m_CodeSet"),(VDS_STORAGE_IDENTIFIER_TYPE, "m_Type"),(UNSIGNED_LONG, "m_cbIdentifier"),(PBYTE, "m_rgbIdentifier"),]

    

class VDS_STORAGE_DEVICE_ID_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "m_version"),(UNSIGNED_LONG, "m_cIdentifiers"),(PVDS_STORAGE_IDENTIFIER, "m_rgIdentifiers"),]

    

class VDS_INTERCONNECT(NdrStructure):
    MEMBERS = [(VDS_INTERCONNECT_ADDRESS_TYPE, "m_addressType"),(UNSIGNED_LONG, "m_cbPort"),(PBYTE, "m_pbPort"),(UNSIGNED_LONG, "m_cbAddress"),(PBYTE, "m_pbAddress"),]

    

class VDS_LUN_INFORMATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "m_version"),(BYTE, "m_DeviceType"),(BYTE, "m_DeviceTypeModifier"),(LONG, "m_bCommandQueuing"),(VDS_STORAGE_BUS_TYPE, "m_BusType"),(PCHAR, "m_szVendorId"),(PCHAR, "m_szProductId"),(PCHAR, "m_szProductRevision"),(PCHAR, "m_szSerialNumber"),(GUID, "m_diskSignature"),(VDS_STORAGE_DEVICE_ID_DESCRIPTOR, "m_deviceIdDescriptor"),(UNSIGNED_LONG, "m_cInterconnects"),(PVDS_INTERCONNECT, "m_rgInterconnects"),]

    

class VDS_FILE_SYSTEM_PROP(NdrStructure):
    MEMBERS = [(VDS_FILE_SYSTEM_TYPE, "type"),(VDS_OBJECT_ID, "volumeId"),(UNSIGNED_LONG, "ulFlags"),(ULONGLONG, "ullTotalAllocationUnits"),(ULONGLONG, "ullAvailableAllocationUnits"),(UNSIGNED_LONG, "ulAllocationUnitSize"),(PWCHAR, "pwszLabel"),]

    
PVDS_FILE_SYSTEM_PROP = VDS_FILE_SYSTEM_PROP

class VDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulFlags"),(UNSIGNED_SHORT, "usRevision"),(UNSIGNED_LONG, "ulDefaultUnitAllocationSize"),(UNSIGNED_LONG, "rgulAllowedUnitAllocationSizes"),(WCHAR, "wszName"),]

    
PVDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP = VDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP

class VDS_DISK_EXTENT(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "diskId"),(VDS_DISK_EXTENT_TYPE, "type"),(ULONGLONG, "ullOffset"),(ULONGLONG, "ullSize"),(VDS_OBJECT_ID, "volumeId"),(VDS_OBJECT_ID, "plexId"),(UNSIGNED_LONG, "memberIdx"),]

    
PVDS_DISK_EXTENT = VDS_DISK_EXTENT

class VDS_DISK_FREE_EXTENT(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "diskId"),(ULONGLONG, "ullOffset"),(ULONGLONG, "ullSize"),]

    
PVDS_DISK_FREE_EXTENT = VDS_DISK_FREE_EXTENT

class VDS_PARTITION_PROP(NdrStructure):
    MEMBERS = [(VDS_PARTITION_STYLE, "PartitionStyle"),(UNSIGNED_LONG, "ulFlags"),(UNSIGNED_LONG, "ulPartitionNumber"),(ULONGLONG, "ullOffset"),(ULONGLONG, "ullSize"),(U0, "u0"),]

    

class VDS_INPUT_DISK(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "diskId"),(ULONGLONG, "ullSize"),(VDS_OBJECT_ID, "plexId"),(UNSIGNED_LONG, "memberIdx"),]

    

class CREATE_PARTITION_PARAMETERS(NdrStructure):
    MEMBERS = [(VDS_PARTITION_STYLE, "style"),(U0, "u0"),]

    

class VIRTUAL_STORAGE_TYPE(NdrStructure):
    MEMBERS = [(ULONG, "DeviceId"),(GUID, "VendorId"),]

    

class __VDS_PARTITION_STYLE(NdrEnum):
    MAP = ((0 , 'VDS_PARTITION_STYLE_MBR'),(1 , 'VDS_PARTITION_STYLE_GPT'),(2 , 'VDS_PARTITION_STYLE_RAW'),)        

class VDS_OBJECT_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_OT_UNKNOWN'),(1 , 'VDS_OT_PROVIDER'),(10 , 'VDS_OT_PACK'),(11 , 'VDS_OT_VOLUME'),(12 , 'VDS_OT_VOLUME_PLEX'),(13 , 'VDS_OT_DISK'),(90 , 'VDS_OT_HBAPORT'),(91 , 'VDS_OT_INIT_ADAPTER'),(92 , 'VDS_OT_INIT_PORTAL'),(100 , 'VDS_OT_ASYNC'),(101 , 'VDS_OT_ENUM'),(200 , 'VDS_OT_VDISK'),(201 , 'VDS_OT_OPEN_VDISK'),)        

class VDS_SERVICE_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_SVF_SUPPORT_DYNAMIC'),(2 , 'VDS_SVF_SUPPORT_FAULT_TOLERANT'),(4 , 'VDS_SVF_SUPPORT_GPT'),(8 , 'VDS_SVF_SUPPORT_DYNAMIC_1394'),(16 , 'VDS_SVF_CLUSTER_SERVICE_CONFIGURED'),(32 , 'VDS_SVF_AUTO_MOUNT_OFF'),(64 , 'VDS_SVF_OS_UNINSTALL_VALID'),(128 , 'VDS_SVF_EFI'),(256 , 'VDS_SVF_SUPPORT_MIRROR'),(512 , 'VDS_SVF_SUPPORT_RAIDS'),(1024 , 'VDS_SVF_SUPPORT_REFS'),)        

class VDS_PROVIDER_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_PT_UNKNOWN'),(1 , 'VDS_PT_SOFTWARE'),(2 , 'VDS_PT_HARDWARE'),(3 , 'VDS_PT_VIRTUALDISK'),(4 , 'VDS_PT_MAX'),)        

class VDS_PROVIDER_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_PF_DYNAMIC'),(2 , 'VDS_PF_INTERNAL_HARDWARE_PROVIDER'),(4 , 'VDS_PF_ONE_DISK_ONLY_PER_PACK'),(8 , 'VDS_PF_ONE_PACK_ONLINE_ONLY'),(16 , 'VDS_PF_VOLUME_SPACE_MUST_BE_CONTIGUOUS'),(32 , 'VDS_PF_SUPPORT_MIRROR'),(64 , 'VDS_PF_SUPPORT_RAID5'),(536870912 , 'VDS_PF_SUPPORT_DYNAMIC_1394'),(1073741824 , 'VDS_PF_SUPPORT_FAULT_TOLERANT'),(2147483648 , 'VDS_PF_SUPPORT_DYNAMIC'),)        

class VDS_QUERY_PROVIDER_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_QUERY_SOFTWARE_PROVIDERS'),(2 , 'VDS_QUERY_HARDWARE_PROVIDERS'),(4 , 'VDS_QUERY_VIRTUALDISK_PROVIDERS'),)        

class VDS_DRIVE_LETTER_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_DLF_NON_PERSISTENT'),)        

class VDS_PACK_STATUS(NdrEnum):
    MAP = ((0 , 'VDS_PS_UNKNOWN'),(1 , 'VDS_PS_ONLINE'),(4 , 'VDS_PS_OFFLINE'),)        

class VDS_PACK_FLAG(NdrEnum):
    MAP = ((1 , 'VDS_PKF_FOREIGN'),(2 , 'VDS_PKF_NOQUORUM'),(4 , 'VDS_PKF_POLICY'),(8 , 'VDS_PKF_CORRUPTED'),(16 , 'VDS_PKF_ONLINE_ERROR'),)        

class VDS_DISK_OFFLINE_REASON(NdrEnum):
    MAP = ((0 , 'VDSDiskOfflineReasonNone'),(1 , 'VDSDiskOfflineReasonPolicy'),(2 , 'VDSDiskOfflineReasonRedundantPath'),(3 , 'VDSDiskOfflineReasonSnapshot'),(4 , 'VDSDiskOfflineReasonCollision'),(5 , 'VDSDiskOfflineReasonResourceExhaustion'),(6 , 'VDSDiskOfflineReasonWriteFailure'),(7 , 'VDSDiskOfflineReasonDIScan'),)        

class VDS_VOLUME_PLEX_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_VPT_UNKNOWN'),(10 , 'VDS_VPT_SIMPLE'),(11 , 'VDS_VPT_SPAN'),(12 , 'VDS_VPT_STRIPE'),(14 , 'VDS_VPT_PARITY'),)        

class VDS_VOLUME_PLEX_STATUS(NdrEnum):
    MAP = ((0 , 'VDS_VPS_UNKNOWN'),(1 , 'VDS_VPS_ONLINE'),(3 , 'VDS_VPS_NO_MEDIA'),(5 , 'VDS_VPS_FAILED'),)        

class VDS_IPADDRESS_TYPE(NdrEnum):
    MAP = ((0 , 'VDS_IPT_TEXT'),(1 , 'VDS_IPT_IPV4'),(2 , 'VDS_IPT_IPV6'),(3 , 'VDS_IPT_EMPTY'),)        

class VDS_HBAPORT_TYPE(NdrEnum):
    MAP = ((1 , 'VDS_HPT_UNKNOWN'),(2 , 'VDS_HPT_OTHER'),(3 , 'VDS_HPT_NOTPRESENT'),(5 , 'VDS_HPT_NPORT'),(6 , 'VDS_HPT_NLPORT'),(7 , 'VDS_HPT_FLPORT'),(8 , 'VDS_HPT_FPORT'),(9 , 'VDS_HPT_EPORT'),(10 , 'VDS_HPT_GPORT'),(20 , 'VDS_HPT_LPORT'),(21 , 'VDS_HPT_PTP'),)        

class VDS_HBAPORT_STATUS(NdrEnum):
    MAP = ((1 , 'VDS_HPS_UNKNOWN'),(2 , 'VDS_HPS_ONLINE'),(3 , 'VDS_HPS_OFFLINE'),(4 , 'VDS_HPS_BYPASSED'),(5 , 'VDS_HPS_DIAGNOSTICS'),(6 , 'VDS_HPS_LINKDOWN'),(7 , 'VDS_HPS_ERROR'),(8 , 'VDS_HPS_LOOPBACK'),)        

class VDS_HBAPORT_SPEED_FLAG(NdrEnum):
    MAP = ((0 , 'VDS_HSF_UNKNOWN'),(1 , 'VDS_HSF_1GBIT'),(2 , 'VDS_HSF_2GBIT'),(4 , 'VDS_HSF_10GBIT'),(8 , 'VDS_HSF_4GBIT'),(32768 , 'VDS_HSF_NOT_NEGOTIATED'),)        

class VDS_PATH_STATUS(NdrEnum):
    MAP = ((0 , 'VDS_MPS_UNKNOWN'),(1 , 'VDS_MPS_ONLINE'),(5 , 'VDS_MPS_FAILED'),(7 , 'VDS_MPS_STANDBY'),)        

class VDS_REPARSE_POINT_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "SourceVolumeId"),(PWCHAR, "pwszPath"),]

    
PVDS_REPARSE_POINT_PROP = VDS_REPARSE_POINT_PROP

class VDS_DRIVE_LETTER_PROP(NdrStructure):
    MEMBERS = [(WCHAR, "wcLetter"),(VDS_OBJECT_ID, "volumeId"),(UNSIGNED_LONG, "ulFlags"),(LONG, "bUsed"),]

    
PVDS_DRIVE_LETTER_PROP = VDS_DRIVE_LETTER_PROP

class VDS_SAN_POLICY(NdrEnum):
    MAP = ((0 , 'VDS_SP_UNKNOWN'),(1 , 'VDS_SP_ONLINE'),(2 , 'VDS_SP_OFFLINE_SHARED'),(3 , 'VDS_SP_OFFLINE'),(4 , 'VDS_SP_OFFLINE_INTERNAL'),(5 , 'VDS_SP_MAX'),)        

class VDS_FILE_SYSTEM_TYPE_PROP(NdrStructure):
    MEMBERS = [(VDS_FILE_SYSTEM_TYPE, "type"),(WCHAR, "wszName"),(UNSIGNED_LONG, "ulFlags"),(UNSIGNED_LONG, "ulCompressionFlags"),(UNSIGNED_LONG, "ulMaxLabelLength"),(PWCHAR, "pwszIllegalLabelCharSet"),]

    
PVDS_FILE_SYSTEM_TYPE_PROP = VDS_FILE_SYSTEM_TYPE_PROP

class CHANGE_ATTRIBUTES_PARAMETERS(NdrStructure):
    MEMBERS = [(VDS_PARTITION_STYLE, "style"),(U0, "u0"),]

    

class CHANGE_PARTITION_TYPE_PARAMETERS(NdrStructure):
    MEMBERS = [(VDS_PARTITION_STYLE, "style"),(U0, "u0"),]

    

class VDS_WWN(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "rguchWwn"),]

    

class VDS_IPADDRESS(NdrStructure):
    MEMBERS = [(VDS_IPADDRESS_TYPE, "type"),(UNSIGNED_LONG, "ipv4Address"),(UNSIGNED_CHAR, "ipv6Address"),(UNSIGNED_LONG, "ulIpv6FlowInfo"),(UNSIGNED_LONG, "ulIpv6ScopeId"),(WCHAR, "wszTextAddress"),(UNSIGNED_LONG, "ulPort"),]

    

class VDS_ISCSI_SHARED_SECRET(NdrStructure):
    MEMBERS = [(PUNSIGNED_CHAR, "pSharedSecret"),(UNSIGNED_LONG, "ulSharedSecretSize"),]

    

class VDS_SERVICE_PROP(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszVersion"),(UNSIGNED_LONG, "ulFlags"),]

    

class VDS_HBAPORT_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_WWN, "wwnNode"),(VDS_WWN, "wwnPort"),(VDS_HBAPORT_TYPE, "type"),(VDS_HBAPORT_STATUS, "status"),(UNSIGNED_LONG, "ulPortSpeed"),(UNSIGNED_LONG, "ulSupportedPortSpeed"),]

    

class VDS_ISCSI_INITIATOR_ADAPTER_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(PWCHAR, "pwszName"),]

    

class VDS_ISCSI_INITIATOR_PORTAL_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_IPADDRESS, "address"),(UNSIGNED_LONG, "ulPortIndex"),]

    

class VDS_PROVIDER_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(PWCHAR, "pwszName"),(GUID, "guidVersionId"),(PWCHAR, "pwszVersion"),(VDS_PROVIDER_TYPE, "type"),(UNSIGNED_LONG, "ulFlags"),(UNSIGNED_LONG, "ulStripeSizeFlags"),(SHORT, "sRebuildPriority"),]

    

class VDS_PACK_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(PWCHAR, "pwszName"),(VDS_PACK_STATUS, "status"),(UNSIGNED_LONG, "ulFlags"),]

    
PVDS_PACK_PROP = VDS_PACK_PROP

class VDS_DISK_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_DISK_STATUS, "status"),(VDS_LUN_RESERVE_MODE, "ReserveMode"),(VDS_HEALTH, "health"),(DWORD, "dwDeviceType"),(DWORD, "dwMediaType"),(ULONGLONG, "ullSize"),(UNSIGNED_LONG, "ulBytesPerSector"),(UNSIGNED_LONG, "ulSectorsPerTrack"),(UNSIGNED_LONG, "ulTracksPerCylinder"),(UNSIGNED_LONG, "ulFlags"),(VDS_STORAGE_BUS_TYPE, "BusType"),(VDS_PARTITION_STYLE, "PartitionStyle"),(PWSZDEVICEPATH, "u0"),(PWCHAR, "pwszDiskAddress"),(PWCHAR, "pwszName"),(PWCHAR, "pwszFriendlyName"),(PWCHAR, "pwszAdaptorName"),(PWCHAR, "pwszDevicePath"),]

    
PVDS_DISK_PROP = VDS_DISK_PROP

class VDS_DISK_PROP2(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_DISK_STATUS, "status"),(VDS_LUN_RESERVE_MODE, "ReserveMode"),(VDS_HEALTH, "health"),(DWORD, "dwDeviceType"),(DWORD, "dwMediaType"),(ULONGLONG, "ullSize"),(UNSIGNED_LONG, "ulBytesPerSector"),(UNSIGNED_LONG, "ulSectorsPerTrack"),(UNSIGNED_LONG, "ulTracksPerCylinder"),(UNSIGNED_LONG, "ulFlags"),(VDS_STORAGE_BUS_TYPE, "BusType"),(VDS_PARTITION_STYLE, "PartitionStyle"),(PWSZLOCATIONPATH, "u0"),(PWCHAR, "pwszDiskAddress"),(PWCHAR, "pwszName"),(PWCHAR, "pwszFriendlyName"),(PWCHAR, "pwszAdaptorName"),(PWCHAR, "pwszDevicePath"),(PWCHAR, "pwszLocationPath"),]

    
PVDS_DISK_PROP2 = VDS_DISK_PROP2

class VDS_ADVANCEDDISK_PROP(NdrStructure):
    MEMBERS = [(LPWSTR, "pwszId"),(LPWSTR, "pwszPathname"),(LPWSTR, "pwszLocation"),(LPWSTR, "pwszFriendlyName"),(LPWSTR, "pswzIdentifier"),(USHORT, "usIdentifierFormat"),(ULONG, "ulNumber"),(LPWSTR, "pwszSerialNumber"),(LPWSTR, "pwszFirmwareVersion"),(LPWSTR, "pwszManufacturer"),(LPWSTR, "pwszModel"),(ULONGLONG, "ullTotalSize"),(ULONGLONG, "ullAllocatedSize"),(ULONG, "ulLogicalSectorSize"),(ULONG, "ulPhysicalSectorSize"),(ULONG, "ulPartitionCount"),(VDS_DISK_STATUS, "status"),(VDS_HEALTH, "health"),(VDS_STORAGE_BUS_TYPE, "BusType"),(VDS_PARTITION_STYLE, "PartitionStyle"),(DWDEVICETYPE, "u0"),(ULONG, "ulFlags"),(DWORD, "dwDeviceType"),]

    
PVDS_ADVANCEDDISK_PROP = VDS_ADVANCEDDISK_PROP

class VDS_VOLUME_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_VOLUME_TYPE, "type"),(VDS_VOLUME_STATUS, "status"),(VDS_HEALTH, "health"),(VDS_TRANSITION_STATE, "TransitionState"),(ULONGLONG, "ullSize"),(UNSIGNED_LONG, "ulFlags"),(VDS_FILE_SYSTEM_TYPE, "RecommendedFileSystemType"),(PWCHAR, "pwszName"),]

    
PVDS_VOLUME_PROP = VDS_VOLUME_PROP

class VDS_VOLUME_PROP2(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_VOLUME_TYPE, "type"),(VDS_VOLUME_STATUS, "status"),(VDS_HEALTH, "health"),(VDS_TRANSITION_STATE, "TransitionState"),(ULONGLONG, "ullSize"),(UNSIGNED_LONG, "ulFlags"),(VDS_FILE_SYSTEM_TYPE, "RecommendedFileSystemType"),(ULONG, "cbUniqueId"),(PWCHAR, "pwszName"),(PBYTE, "pUniqueId"),]

    
PVDS_VOLUME_PROP2 = VDS_VOLUME_PROP2

class VDS_VOLUME_PLEX_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "id"),(VDS_VOLUME_PLEX_TYPE, "type"),(VDS_VOLUME_PLEX_STATUS, "status"),(VDS_HEALTH, "health"),(VDS_TRANSITION_STATE, "TransitionState"),(ULONGLONG, "ullSize"),(UNSIGNED_LONG, "ulStripeSize"),(UNSIGNED_LONG, "ulNumberOfMembers"),]

    
PVDS_VOLUME_PLEX_PROP = VDS_VOLUME_PLEX_PROP

class CREATE_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'CREATE_VIRTUAL_DISK_FLAG_NONE'),(1 , 'CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION'),)        

class OPEN_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'OPEN_VIRTUAL_DISK_FLAG_NONE'),(1 , 'OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS'),(2 , 'OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE'),(4 , 'OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE'),)        

class VDS_CREATE_VDISK_PARAMETERS(NdrStructure):
    MEMBERS = [(GUID, "UniqueId"),(ULONGLONG, "MaximumSize"),(ULONG, "BlockSizeInBytes"),(ULONG, "SectorSizeInBytes"),(LPWSTR, "pParentPath"),(LPWSTR, "pSourcePath"),]

    
PVDS_CREATE_VDISK_PARAMETERS = VDS_CREATE_VDISK_PARAMETERS

class VDS_VDISK_STATE(NdrEnum):
    MAP = ((0 , 'VDS_VST_UNKNOWN'),(1 , 'VDS_VST_ADDED'),(2 , 'VDS_VST_OPEN'),(3 , 'VDS_VST_ATTACH_PENDING'),(4 , 'VDS_VST_ATTACHED_NOT_OPEN'),(5 , 'VDS_VST_ATTACHED'),(6 , 'VDS_VST_DETACH_PENDING'),(7 , 'VDS_VST_COMPACTING'),(8 , 'VDS_VST_MERGING'),(9 , 'VDS_VST_EXPANDING'),(10 , 'VDS_VST_DELETED'),(11 , 'VDS_VST_MAX'),)        

class ATTACH_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'ATTACH_VIRTUAL_DISK_FLAG_NONE'),(1 , 'ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY'),(2 , 'ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER'),(4 , 'ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME'),(8 , 'ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST'),)        

class DETACH_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'DETACH_VIRTUAL_DISK_FLAG_NONE'),)        

class COMPACT_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'COMPACT_VIRTUAL_DISK_FLAG_NONE'),)        

class MERGE_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'MERGE_VIRTUAL_DISK_FLAG_NONE'),)        

class EXPAND_VIRTUAL_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'EXPAND_VIRTUAL_DISK_FLAG_NONE'),)        

class DEPENDENT_DISK_FLAG(NdrEnum):
    MAP = ((0 , 'DEPENDENT_DISK_FLAG_NONE'),(1 , 'DEPENDENT_DISK_FLAG_MULT_BACKING_FILES'),(2 , 'DEPENDENT_DISK_FLAG_FULLY_ALLOCATED'),(4 , 'DEPENDENT_DISK_FLAG_READ_ONLY'),(8 , 'DEPENDENT_DISK_FLAG_REMOTE'),(16 , 'DEPENDENT_DISK_FLAG_SYSTEM_VOLUME'),(32 , 'DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT'),(64 , 'DEPENDENT_DISK_FLAG_REMOVABLE'),(128 , 'DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER'),(256 , 'DEPENDENT_DISK_FLAG_PARENT'),(512 , 'DEPENDENT_DISK_FLAG_NO_HOST_DISK'),(1024 , 'DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME'),)        

class VDS_VDISK_PROPERTIES(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "Id"),(VDS_VDISK_STATE, "State"),(VIRTUAL_STORAGE_TYPE, "VirtualDeviceType"),(ULONGLONG, "VirtualSize"),(ULONGLONG, "PhysicalSize"),(LPWSTR, "pPath"),(LPWSTR, "pDeviceName"),(DEPENDENT_DISK_FLAG, "DiskFlag"),(BOOL, "bIsChild"),(LPWSTR, "pParentPath"),]

    
PVDS_VDISK_PROPERTIES = VDS_VDISK_PROPERTIES

class VIRTUAL_DISK_ACCESS_MASK(NdrEnum):
    MAP = ((65536 , 'VIRTUAL_DISK_ACCESS_SURFACE_RO'),(131072 , 'VIRTUAL_DISK_ACCESS_SURFACE_RW'),(262144 , 'VIRTUAL_DISK_ACCESS_UNSURFACE'),(524288 , 'VIRTUAL_DISK_ACCESS_GET_INFO'),(1048576 , 'VIRTUAL_DISK_ACCESS_CREATE'),(2097152 , 'VIRTUAL_DISK_ACCESS_METAOPS'),(851968 , 'VIRTUAL_DISK_ACCESS_READ'),(4128768 , 'VIRTUAL_DISK_ACCESS_ALL'),(3276800 , 'VIRTUAL_DISK_ACCESS_WRITABLE'),)        

class _VIRTUAL_STORAGE_TYPE(NdrStructure):
    MEMBERS = []

    
PVIRTUAL_STORAGE_TYPE = _VIRTUAL_STORAGE_TYPE
Interface("118610b7-8d94-4030-b5b8-500889788e4e", "1.0",[Method("Next",
In((UNSIGNED_LONG,'celt')),
Out((PPIUNKNOWN,'ppObjectArray')),
Out((PUNSIGNED_LONG,'pcFetched')),
),Method("Skip",
In((UNSIGNED_LONG,'celt')),
),Method("Reset",
),Method("Clone",
Out((PPIENUMVDSOBJECT,'ppEnum')),
),])