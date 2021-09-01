
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
class ROUTER_INTERFACE_TYPE(NdrEnum):
    MAP = ((0 , 'ROUTER_IF_TYPE_CLIENT'),(1 , 'ROUTER_IF_TYPE_HOME_ROUTER'),(2 , 'ROUTER_IF_TYPE_FULL_ROUTER'),(3 , 'ROUTER_IF_TYPE_DEDICATED'),(4 , 'ROUTER_IF_TYPE_INTERNAL'),(5 , 'ROUTER_IF_TYPE_LOOPBACK'),(6 , 'ROUTER_IF_TYPE_TUNNEL1'),(7 , 'ROUTER_IF_TYPE_DIALOUT'),)        

class ROUTER_CONNECTION_STATE(NdrEnum):
    MAP = ((0 , 'ROUTER_IF_STATE_UNREACHABLE'),(1 , 'ROUTER_IF_STATE_DISCONNECTED'),(2 , 'ROUTER_IF_STATE_CONNECTING'),(3 , 'ROUTER_IF_STATE_CONNECTED'),)        

class RAS_QUARANTINE_STATE(NdrEnum):
    MAP = ((0 , 'RAS_QUAR_STATE_NORMAL'),(1 , 'RAS_QUAR_STATE_QUARANTINE'),(2 , 'RAS_QUAR_STATE_PROBATION'),(3 , 'RAS_QUAR_STATE_UNKNOWN'),)        

class RAS_PORT_CONDITION(NdrEnum):
    MAP = ((0 , 'RAS_PORT_NON_OPERATIONAL'),(1 , 'RAS_PORT_DISCONNECTED'),(2 , 'RAS_PORT_CALLING_BACK'),(3 , 'RAS_PORT_LISTENING'),(4 , 'RAS_PORT_AUTHENTICATING'),(5 , 'RAS_PORT_AUTHENTICATED'),(6 , 'RAS_PORT_INITIALIZING'),)        

class RAS_HARDWARE_CONDITION(NdrEnum):
    MAP = ((0 , 'RAS_HARDWARE_OPERATIONAL'),(1 , 'RAS_HARDWARE_FAILURE'),)        
DIM_HANDLE = HANDLE_T

class FORWARD_ACTION(NdrEnum):
    MAP = ((0 , 'FORWARD'),(1 , 'DROP'),)        

class MIB_IPFORWARD_TYPE(NdrEnum):
    MAP = ((1 , 'MIB_IPROUTE_TYPE_OTHER'),(2 , 'MIB_IPROUTE_TYPE_INVALID'),(3 , 'MIB_IPROUTE_TYPE_DIRECT'),(4 , 'MIB_IPROUTE_TYPE_INDIRECT'),)        

class MIB_IPFORWARD_PROTO(NdrEnum):
    MAP = ((1 , 'MIB_IPPROTO_OTHER'),(2 , 'MIB_IPPROTO_LOCAL'),(3 , 'MIB_IPPROTO_NETMGMT'),(4 , 'MIB_IPPROTO_ICMP'),(5 , 'MIB_IPPROTO_EGP'),(6 , 'MIB_IPPROTO_GGP'),(7 , 'MIB_IPPROTO_HELLO'),(8 , 'MIB_IPPROTO_RIP'),(9 , 'MIB_IPPROTO_IS_IS'),(10 , 'MIB_IPPROTO_ES_IS'),(11 , 'MIB_IPPROTO_CISCO'),(12 , 'MIB_IPPROTO_BBN'),(13 , 'MIB_IPPROTO_OSPF'),(14 , 'MIB_IPPROTO_BGP'),(10002 , 'MIB_IPPROTO_NT_AUTOSTATIC'),(10006 , 'MIB_IPPROTO_NT_STATIC'),(10007 , 'MIB_IPPROTO_NT_STATIC_NON_DOD'),)        

class MIB_IPSTATS_FORWARDING(NdrEnum):
    MAP = ((1 , 'MIB_IP_FORWARDING'),(2 , 'MIB_IP_NOT_FORWARDING'),)        

class MIB_TCP_STATE(NdrEnum):
    MAP = ((1 , 'MIB_TCP_STATE_CLOSED'),(2 , 'MIB_TCP_STATE_LISTEN'),(3 , 'MIB_TCP_STATE_SYN_SENT'),(4 , 'MIB_TCP_STATE_SYN_RCVD'),(5 , 'MIB_TCP_STATE_ESTAB'),(6 , 'MIB_TCP_STATE_FIN_WAIT1'),(7 , 'MIB_TCP_STATE_FIN_WAIT2'),(8 , 'MIB_TCP_STATE_CLOSE_WAIT'),(9 , 'MIB_TCP_STATE_CLOSING'),(10 , 'MIB_TCP_STATE_LAST_ACK'),(11 , 'MIB_TCP_STATE_TIME_WAIT'),(12 , 'MIB_TCP_STATE_DELETE_TCB'),)        

class TCP_RTO_ALGORITHM(NdrEnum):
    MAP = ((1 , 'MIB_TCP_RTO_OTHER'),(2 , 'MIB_TCP_RTO_CONSTANT'),(3 , 'MIB_TCP_RTO_RSRE'),(4 , 'MIB_TCP_RTO_VANJ'),)        

class IN6_ADDR(NdrStructure):
    MEMBERS = [(U, "u"),]

    
PIN6_ADDR = IN6_ADDR
LPIN6_ADDR = IN6_ADDR

class DIM_INFORMATION_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "dwBufferSize"),(LPBYTE, "pBuffer"),]

    
PDIM_INFORMATION_CONTAINER = DIM_INFORMATION_CONTAINER

class MPRAPI_OBJECT_HEADER_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(UCHAR, "type"),(USHORT, "size"),]

    
PMPRAPI_OBJECT_HEADER_IDL = MPRAPI_OBJECT_HEADER_IDL

class PPP_PROJECTION_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwIPv4Options"),(DWORD, "dwIPv4RemoteOptions"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwLcpError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwLcpTerminateReason"),(DWORD, "dwLcpRemoteTerminateReason"),(DWORD, "dwLcpOptions"),(DWORD, "dwLcpRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwRemoteEapTypeId"),(DWORD, "dwCcpError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwCcpOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwCcpRemoteOptions"),]

    
PPPP_PROJECTION_INFO_1 = PPP_PROJECTION_INFO_1

class PPP_PROJECTION_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwIPv4Options"),(DWORD, "dwIPv4RemoteOptions"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwLcpError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwLcpTerminateReason"),(DWORD, "dwLcpRemoteTerminateReason"),(DWORD, "dwLcpOptions"),(DWORD, "dwLcpRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwEmbeddedEAPTypeId"),(DWORD, "dwRemoteEapTypeId"),(DWORD, "dwCcpError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwCcpOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwCcpRemoteOptions"),]

    
PPPP_PROJECTION_INFO_2 = PPP_PROJECTION_INFO_2

class IKEV2_PROJECTION_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwOptions"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwEapTypeId"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwEncryptionMethod"),]

    
PIKEV2_PROJECTION_INFO_1 = IKEV2_PROJECTION_INFO_1

class IKEV2_PROJECTION_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwOptions"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwEapTypeId"),(DWORD, "dwEmbeddedEAPTypeId"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwEncryptionMethod"),]

    
PIKEV2_PROJECTION_INFO_2 = IKEV2_PROJECTION_INFO_2

class PROJECTION_INFO_IDL_1(NdrStructure):
    MEMBERS = [(UCHAR, "projectionInfoType"),(ANONYMOUS22, "ProjectionInfoObject"),]

    

class PPPROJECTION_INFO_IDL_1(NdrStructure):
    MEMBERS = []

    

class PROJECTION_INFO_IDL_2(NdrStructure):
    MEMBERS = [(UCHAR, "projectionInfoType"),(ANONYMOUS23, "ProjectionInfoObject"),]

    
PPROJECTION_INFO_IDL_2 = PROJECTION_INFO_IDL_2

class RAS_CONNECTION_EX_1_IDL(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),(GUID, "guid"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "probationTime"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),(DWORD, "dwNumSwitchOvers"),(WCHAR, "wszRemoteEndpointAddress"),(WCHAR, "wszLocalEndpointAddress"),(PROJECTION_INFO_IDL_1, "ProjectionInfo"),(ULONG, "hConnection"),(ULONG, "hInterface"),]

    
PRAS_CONNECTION_EX_1_IDL = RAS_CONNECTION_EX_1_IDL

class RAS_CONNECTION_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS24, "ConnObject"),]

    

class PPRAS_CONNECTION_EX_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_CONNECTION_4_IDL(NdrStructure):
    MEMBERS = [(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),(GUID, "guid"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "probationTime"),(FILETIME, "connectionStartTime"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),(DWORD, "dwNumSwitchOvers"),(WCHAR, "wszRemoteEndpointAddress"),(WCHAR, "wszLocalEndpointAddress"),(PROJECTION_INFO_IDL_2, "ProjectionInfo"),(ULONG, "hConnection"),(ULONG, "hInterface"),(DWORD, "dwDeviceType"),]

    
PRAS_CONNECTION_4_IDL = RAS_CONNECTION_4_IDL

class CERT_BLOB_1(NdrStructure):
    MEMBERS = [(DWORD, "cbData"),(PBYTE, "pbData"),]

    
PCERT_BLOB_1 = CERT_BLOB_1

class CERT_EKU_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(BOOL, "IsEKUOID"),(PWCHAR, "pwszEKU"),]

    
PCERT_EKU_1 = CERT_EKU_1

class IKEV2_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),]

    
PIKEV2_TUNNEL_CONFIG_PARAMS_1 = IKEV2_TUNNEL_CONFIG_PARAMS_1

class ROUTER_CUSTOM_IKEV2_POLICY_0(NdrStructure):
    MEMBERS = [(DWORD, "dwIntegrityMethod"),(DWORD, "dwEncryptionMethod"),(DWORD, "dwCipherTransformConstant"),(DWORD, "dwAuthTransformConstant"),(DWORD, "dwPfsGroup"),(DWORD, "dwDhGroup"),]

    
PROUTER_CUSTOM_IKEV2_POLICY_0 = ROUTER_CUSTOM_IKEV2_POLICY_0
ROUTER_CUSTOM_L2TP_POLICY_0 = ROUTER_CUSTOM_IKEV2_POLICY_0
PROUTER_CUSTOM_L2TP_POLICY_0 = ROUTER_CUSTOM_IKEV2_POLICY_0

class ROUTER_IKEV2_IF_CUSTOM_CONFIG_0(NdrStructure):
    MEMBERS = [(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSize"),(CERT_BLOB_1, "certificateName"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),]

    
PROUTER_IKEV2_IF_CUSTOM_CONFIG_0 = ROUTER_IKEV2_IF_CUSTOM_CONFIG_0

class ROUTER_IKEV2_IF_CUSTOM_CONFIG_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSize"),(CERT_BLOB_1, "certificateName"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),(CERT_BLOB_1, "certificateHash"),]

    
PROUTER_IKEV2_IF_CUSTOM_CONFIG_1 = ROUTER_IKEV2_IF_CUSTOM_CONFIG_1

class MPR_IF_CUSTOMINFOEX_0(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwFlags"),(ROUTER_IKEV2_IF_CUSTOM_CONFIG_0, "customIkev2Config"),]

    
PMPR_IF_CUSTOMINFOEX_0 = MPR_IF_CUSTOMINFOEX_0

class MPR_IF_CUSTOMINFOEX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwFlags"),(ROUTER_IKEV2_IF_CUSTOM_CONFIG_1, "customIkev2Config"),]

    
PMPR_IF_CUSTOMINFOEX_1 = MPR_IF_CUSTOMINFOEX_1

class MPR_IF_CUSTOMINFOEX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS25, "IfCustomConfigObject"),]

    
PMPR_IF_CUSTOMINFOEX_IDL = MPR_IF_CUSTOMINFOEX_IDL

class IKEV2_TUNNEL_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),(CERT_BLOB_1, "machineCertificateName"),(DWORD, "dwEncryptionType"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),]

    
PIKEV2_TUNNEL_CONFIG_PARAMS_2 = IKEV2_TUNNEL_CONFIG_PARAMS_2

class IKEV2_TUNNEL_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),(CERT_BLOB_1, "machineCertificateName"),(DWORD, "dwEncryptionType"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),(DWORD, "dwTotalEkus"),(PCERT_EKU_1, "certificateEKUs"),(CERT_BLOB_1, "machineCertificateHash"),]

    
PIKEV2_TUNNEL_CONFIG_PARAMS_3 = IKEV2_TUNNEL_CONFIG_PARAMS_3

class L2TP_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwEncryptionType"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(PROUTER_CUSTOM_L2TP_POLICY_0, "customPolicy"),]

    
PL2TP_TUNNEL_CONFIG_PARAMS_1 = L2TP_TUNNEL_CONFIG_PARAMS_1

class IKEV2_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_1, "TunnelConfigParams"),]

    
PIKEV2_CONFIG_PARAMS_1 = IKEV2_CONFIG_PARAMS_1

class IKEV2_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_2, "TunnelConfigParams"),]

    
PIKEV2_CONFIG_PARAMS_2 = IKEV2_CONFIG_PARAMS_2

class IKEV2_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_3, "TunnelConfigParams"),]

    
PIKEV2_CONFIG_PARAMS_3 = IKEV2_CONFIG_PARAMS_3

class PPTP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),]

    
PPPTP_CONFIG_PARAMS_1 = PPTP_CONFIG_PARAMS_1

class L2TP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),]

    
PL2TP_CONFIG_PARAMS_1 = L2TP_CONFIG_PARAMS_1

class L2TP_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(L2TP_TUNNEL_CONFIG_PARAMS_1, "TunnelConfigParams"),]

    
PL2TP_CONFIG_PARAMS_2 = L2TP_CONFIG_PARAMS_2

class SSTP_CERT_INFO_1(NdrStructure):
    MEMBERS = [(BOOL, "isDefault"),(CERT_BLOB_1, "certBlob"),]

    
PSSTP_CERT_INFO_1 = SSTP_CERT_INFO_1

class SSTP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(BOOL, "isUseHttps"),(DWORD, "certAlgorithm"),(SSTP_CERT_INFO_1, "sstpCertDetails"),]

    
PSSTP_CONFIG_PARAMS_1 = SSTP_CONFIG_PARAMS_1

class MPRAPI_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_1, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_1, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    
PMPRAPI_TUNNEL_CONFIG_PARAMS_1 = MPRAPI_TUNNEL_CONFIG_PARAMS_1

class MPRAPI_TUNNEL_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_2, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_1, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    
PMPRAPI_TUNNEL_CONFIG_PARAMS_2 = MPRAPI_TUNNEL_CONFIG_PARAMS_2

class MPRAPI_TUNNEL_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_3, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_2, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    
PMPRAPI_TUNNEL_CONFIG_PARAMS_3 = MPRAPI_TUNNEL_CONFIG_PARAMS_3

class MPR_SERVER_EX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_1, "ConfigParams"),]

    
PMPR_SERVER_EX_1 = MPR_SERVER_EX_1

class MPR_SERVER_EX_2(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_2, "ConfigParams"),]

    
PMPR_SERVER_EX_2 = MPR_SERVER_EX_2

class MPR_SERVER_EX_3(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_3, "ConfigParams"),]

    
PMPR_SERVER_EX_3 = MPR_SERVER_EX_3

class MPR_SERVER_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS26, "ServerConfigObject"),]

    

class PPMPR_SERVER_EX_IDL(NdrStructure):
    MEMBERS = []

    

class MPR_SERVER_SET_CONFIG_EX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_1, "ConfigParams"),]

    
PMPR_SERVER_SET_CONFIG_EX_1 = MPR_SERVER_SET_CONFIG_EX_1

class MPR_SERVER_SET_CONFIG_EX_2(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_2, "ConfigParams"),]

    
PMPR_SERVER_SET_CONFIG_EX_2 = MPR_SERVER_SET_CONFIG_EX_2

class MPR_SERVER_SET_CONFIG_EX_3(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_3, "ConfigParams"),]

    
PMPR_SERVER_SET_CONFIG_EX_3 = MPR_SERVER_SET_CONFIG_EX_3

class MPR_SERVER_SET_CONFIG_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS27, "ServerSetConfigObject"),]

    

class PPMPR_SERVER_SET_CONFIG_EX_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_UPDATE_CONNECTION_1_IDL(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwIfIndex"),(WCHAR, "wszRemoteEndpointAddress"),]

    

class PPRAS_UPDATE_CONNECTION_1_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_UPDATE_CONNECTION_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS28, "UpdateConnection"),]

    

class PPRAS_UPDATE_CONNECTION_IDL(NdrStructure):
    MEMBERS = []

    

class DIM_INTERFACE_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "fGetInterfaceInfo"),(DWORD, "dwInterfaceInfoSize"),(LPBYTE, "pInterfaceInfo"),(DWORD, "fGetGlobalInfo"),(DWORD, "dwGlobalInfoSize"),(LPBYTE, "pGlobalInfo"),]

    
PDIM_INTERFACE_CONTAINER = DIM_INTERFACE_CONTAINER

class RTR_TOC_ENTRY(NdrStructure):
    MEMBERS = [(ULONG, "InfoType"),(ULONG, "InfoSize"),(ULONG, "Count"),(ULONG, "Offset"),]

    
PRTR_TOC_ENTRY = RTR_TOC_ENTRY

class RTR_INFO_BLOCK_HEADER(NdrStructure):
    MEMBERS = [(ULONG, "Version"),(ULONG, "Size"),(ULONG, "TocEntriesCount"),(RTR_TOC_ENTRY, "TocEntry"),]

    
PRTR_INFO_BLOCK_HEADER = RTR_INFO_BLOCK_HEADER

class FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwSrcAddr"),(DWORD, "dwSrcMask"),(DWORD, "dwDstAddr"),(DWORD, "dwDstMask"),(DWORD, "dwProtocol"),(DWORD, "fLateBound"),(WORD, "wSrcPort"),(WORD, "wDstPort"),]

    
PFILTER_INFO = FILTER_INFO

class FILTER_DESCRIPTOR(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwNumFilters"),(FORWARD_ACTION, "faDefaultAction"),(FILTER_INFO, "fiFilter"),]

    
PFILTER_DESCRIPTOR = FILTER_DESCRIPTOR

class FILTER_INFO_V6(NdrStructure):
    MEMBERS = [(BYTE, "ipv6SrcAddr"),(DWORD, "dwSrcPrefixLength"),(BYTE, "ipv6DstAddr"),(DWORD, "dwDstPrefixLength"),(DWORD, "dwProtocol"),(DWORD, "fLateBound"),(WORD, "wSrcPort"),(WORD, "wDstPort"),]

    
PFILTER_INFO_V6 = FILTER_INFO_V6

class FILTER_DESCRIPTOR_V6(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwNumFilters"),(FORWARD_ACTION, "faDefaultAction"),(FILTER_INFO_V6, "fiFilter"),]

    
PFILTER_DESCRIPTOR_V6 = FILTER_DESCRIPTOR_V6

class GLOBAL_INFO(NdrStructure):
    MEMBERS = [(BOOL, "bFilteringOn"),(DWORD, "dwLoggingLevel"),]

    
PGLOBAL_INFO = GLOBAL_INFO

class INTERFACE_ROUTE_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwRtInfoIfIndex"),(DWORD, "dwRtInfoType"),(DWORD, "dwRtInfoProto"),(DWORD, "dwRtInfoPreference"),(DWORD, "dwRtInfoViewSet"),(BOOL, "bV4"),]

    
PINTERFACE_ROUTE_INFO = INTERFACE_ROUTE_INFO

class PROTOCOL_METRIC(NdrStructure):
    MEMBERS = [(DWORD, "dwProtocolId"),(DWORD, "dwMetric"),]

    
PPROTOCOL_METRIC = PROTOCOL_METRIC

class PRIORITY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwNumProtocols"),(PROTOCOL_METRIC, "ppmProtocolMetric"),]

    
PPRIORITY_INFO = PRIORITY_INFO

class PROTOCOL_METRIC_EX(NdrStructure):
    MEMBERS = [(DWORD, "dwProtocolId"),(DWORD, "dwSubProtocolId"),(DWORD, "dwMetric"),]

    
PPROTOCOL_METRIC_EX = PROTOCOL_METRIC_EX

class PRIORITY_INFO_EX(NdrStructure):
    MEMBERS = [(DWORD, "dwNumProtocols"),(PROTOCOL_METRIC_EX, "ppmProtocolMetric"),]

    
PPRIORITY_INFO_EX = PRIORITY_INFO_EX

class RTR_DISC_INFO(NdrStructure):
    MEMBERS = [(WORD, "wMaxAdvtInterval"),(WORD, "wMinAdvtInterval"),(WORD, "wAdvtLifetime"),(BOOL, "bAdvertise"),(LONG, "lPrefLevel"),]

    
PRTR_DISC_INFO = RTR_DISC_INFO

class MCAST_HBEAT_INFO(NdrStructure):
    MEMBERS = [(WCHAR, "pwszGroup"),(BOOL, "bActive"),(ULONG, "ulDeadInterval"),(BYTE, "byProtocol"),(WORD, "wPort"),]

    
PMCAST_HBEAT_INFO = MCAST_HBEAT_INFO

class MIB_MCAST_LIMIT_ROW(NdrStructure):
    MEMBERS = [(DWORD, "dwTtl"),(DWORD, "dwRateLimit"),]

    
PMIB_MCAST_LIMIT_ROW = MIB_MCAST_LIMIT_ROW

class IPINIP_CONFIG_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwRemoteAddress"),(DWORD, "dwLocalAddress"),(BYTE, "byTtl"),]

    
PIPINIP_CONFIG_INFO = IPINIP_CONFIG_INFO

class INTERFACE_STATUS_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwAdminStatus"),]

    
PINTERFACE_STATUS_INFO = INTERFACE_STATUS_INFO

class DIM_MIB_ENTRY_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "dwMibInEntrySize"),(LPBYTE, "pMibInEntry"),(DWORD, "dwMibOutEntrySize"),(LPBYTE, "pMibOutEntry"),]

    
PDIM_MIB_ENTRY_CONTAINER = DIM_MIB_ENTRY_CONTAINER

class MIB_IPFORWARDROW(NdrStructure):
    MEMBERS = [(DWORD, "dwForwardDest"),(DWORD, "dwForwardMask"),(DWORD, "dwForwardPolicy"),(DWORD, "dwForwardNextHop"),(DWORD, "dwForwardIfIndex"),(U0, "u0"),(U1, "u1"),(DWORD, "dwForwardAge"),(DWORD, "dwForwardNextHopAS"),(DWORD, "dwForwardMetric1"),(DWORD, "dwForwardMetric2"),(DWORD, "dwForwardMetric3"),(DWORD, "dwForwardMetric4"),(DWORD, "dwForwardMetric5"),]

    
PMIB_IPFORWARDROW = MIB_IPFORWARDROW

class MIB_IPDESTROW(NdrStructure):
    MEMBERS = [(MIB_IPFORWARDROW, "ForwardRow"),(DWORD, "dwForwardPreference"),(DWORD, "dwForwardViewSet"),]

    
PMIB_IPDESTROW = MIB_IPDESTROW

class MIB_IPDESTTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPDESTROW, "table"),]

    
PMIB_IPDESTTABLE = MIB_IPDESTTABLE

class MIB_ROUTESTATE(NdrStructure):
    MEMBERS = [(BOOL, "bRoutesSetToStack"),]

    
PMIB_ROUTESTATE = MIB_ROUTESTATE

class MIB_BEST_IF(NdrStructure):
    MEMBERS = [(DWORD, "dwDestAddr"),(DWORD, "dwIfIndex"),]

    
PMIB_BEST_IF = MIB_BEST_IF

class MIB_BOUNDARYROW(NdrStructure):
    MEMBERS = [(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),]

    
PMIB_BOUNDARYROW = MIB_BOUNDARYROW

class MIBICMPSTATS(NdrStructure):
    MEMBERS = [(DWORD, "dwMsgs"),(DWORD, "dwErrors"),(DWORD, "dwDestUnreachs"),(DWORD, "dwTimeExcds"),(DWORD, "dwParmProbs"),(DWORD, "dwSrcQuenchs"),(DWORD, "dwRedirects"),(DWORD, "dwEchos"),(DWORD, "dwEchoReps"),(DWORD, "dwTimestamps"),(DWORD, "dwTimestampReps"),(DWORD, "dwAddrMasks"),(DWORD, "dwAddrMaskReps"),]

    

class MIBICMPINFO(NdrStructure):
    MEMBERS = [(MIBICMPSTATS, "icmpInStats"),(MIBICMPSTATS, "icmpOutStats"),]

    

class MIB_ICMP(NdrStructure):
    MEMBERS = [(MIBICMPINFO, "stats"),]

    
PMIB_ICMP = MIB_ICMP

class MIB_IFNUMBER(NdrStructure):
    MEMBERS = [(DWORD, "dwValue"),]

    
PMIB_IFNUMBER = MIB_IFNUMBER

class MIB_IFROW(NdrStructure):
    MEMBERS = [(WCHAR, "wszName"),(DWORD, "dwIndex"),(DWORD, "dwType"),(DWORD, "dwMtu"),(DWORD, "dwSpeed"),(DWORD, "dwPhysAddrLen"),(BYTE, "bPhysAddr"),(DWORD, "dwAdminStatus"),(DWORD, "dwOperStatus"),(DWORD, "dwLastChange"),(DWORD, "dwInOctets"),(DWORD, "dwInUcastPkts"),(DWORD, "dwInNUcastPkts"),(DWORD, "dwInDiscards"),(DWORD, "dwInErrors"),(DWORD, "dwInUnknownProtos"),(DWORD, "dwOutOctets"),(DWORD, "dwOutUcastPkts"),(DWORD, "dwOutNUcastPkts"),(DWORD, "dwOutDiscards"),(DWORD, "dwOutErrors"),(DWORD, "dwOutQLen"),(DWORD, "dwDescrLen"),(BYTE, "bDescr"),]

    

class MIB_IFSTATUS(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwAdminStatus"),(DWORD, "dwOperationalStatus"),(BOOL, "bMHbeatActive"),(BOOL, "bMHbeatAlive"),]

    
PMIB_IFSTATUS = MIB_IFSTATUS

class MIB_IFTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IFROW, "table"),]

    
PMIB_IFTABLE = MIB_IFTABLE

class MIB_IPADDRROW(NdrStructure):
    MEMBERS = [(DWORD, "dwAddr"),(DWORD, "dwIndex"),(DWORD, "dwMask"),(DWORD, "dwBCastAddr"),(DWORD, "dwReasmSize"),(UNSIGNED_SHORT, "unused1"),(UNSIGNED_SHORT, "wType"),]

    
PMIB_IPADDRROW = MIB_IPADDRROW

class MIB_IPADDRTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPADDRROW, "table"),]

    
PMIB_IPADDRTABLE = MIB_IPADDRTABLE

class MIB_IPFORWARDNUMBER(NdrStructure):
    MEMBERS = [(DWORD, "dwValue"),]

    
PMIB_IPFORWARDNUMBER = MIB_IPFORWARDNUMBER

class MIB_IPFORWARDTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPFORWARDROW, "table"),(BYTE, "reserved"),]

    
PMIB_IPFORWARDTABLE = MIB_IPFORWARDTABLE

class MIB_IPMCAST_BOUNDARY(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),(DWORD, "dwStatus"),]

    
PMIB_IPMCAST_BOUNDARY = MIB_IPMCAST_BOUNDARY

class MIB_IPMCAST_BOUNDARY_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_BOUNDARY, "table"),]

    
PMIB_IPMCAST_BOUNDARY_TABLE = MIB_IPMCAST_BOUNDARY_TABLE

class MIB_IPMCAST_GLOBAL(NdrStructure):
    MEMBERS = [(DWORD, "dwEnable"),]

    
PMIB_IPMCAST_GLOBAL = MIB_IPMCAST_GLOBAL

class MIB_IPMCAST_IF_ENTRY(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwTtl"),(DWORD, "dwProtocol"),(DWORD, "dwRateLimit"),(ULONG, "ulInMcastOctets"),(ULONG, "ulOutMcastOctets"),]

    
PMIB_IPMCAST_IF_ENTRY = MIB_IPMCAST_IF_ENTRY

class MIB_IPMCAST_IF_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_IF_ENTRY, "table"),]

    
PMIB_IPMCAST_IF_TABLE = MIB_IPMCAST_IF_TABLE

class MIB_IPMCAST_OIF(NdrStructure):
    MEMBERS = [(DWORD, "dwOutIfIndex"),(DWORD, "dwNextHopAddr"),(PVOID, "pvReserved"),(DWORD, "dwReserved"),]

    
PMIB_IPMCAST_OIF = MIB_IPMCAST_OIF

class MIB_IPMCAST_MFE(NdrStructure):
    MEMBERS = [(DWORD, "dwGroup"),(DWORD, "dwSource"),(DWORD, "dwSrcMask"),(DWORD, "dwUpStrmNgbr"),(DWORD, "dwInIfIndex"),(DWORD, "dwInIfProtocol"),(DWORD, "dwRouteProtocol"),(DWORD, "dwRouteNetwork"),(DWORD, "dwRouteMask"),(ULONG, "ulUpTime"),(ULONG, "ulExpiryTime"),(ULONG, "ulTimeOut"),(ULONG, "ulNumOutIf"),(DWORD, "fFlags"),(DWORD, "dwReserved"),(MIB_IPMCAST_OIF, "rgmioOutInfo"),]

    
PMIB_IPMCAST_MFE = MIB_IPMCAST_MFE

class MIB_IPMCAST_OIF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "dwOutIfIndex"),(DWORD, "dwNextHopAddr"),(PVOID, "pvDialContext"),(ULONG, "ulTtlTooLow"),(ULONG, "ulFragNeeded"),(ULONG, "ulOutPackets"),(ULONG, "ulOutDiscards"),]

    
PMIB_IPMCAST_OIF_STATS = MIB_IPMCAST_OIF_STATS

class MIB_IPMCAST_MFE_STATS(NdrStructure):
    MEMBERS = [(DWORD, "dwGroup"),(DWORD, "dwSource"),(DWORD, "dwSrcMask"),(DWORD, "dwUpStrmNgbr"),(DWORD, "dwInIfIndex"),(DWORD, "dwInIfProtocol"),(DWORD, "dwRouteProtocol"),(DWORD, "dwRouteNetwork"),(DWORD, "dwRouteMask"),(ULONG, "ulUpTime"),(ULONG, "ulExpiryTime"),(ULONG, "ulNumOutIf"),(ULONG, "ulInPkts"),(ULONG, "ulInOctets"),(ULONG, "ulPktsDifferentIf"),(ULONG, "ulQueueOverflow"),(MIB_IPMCAST_OIF_STATS, "rgmiosOutStats"),]

    
PMIB_IPMCAST_MFE_STATS = MIB_IPMCAST_MFE_STATS

class MIB_IPMCAST_SCOPE(NdrStructure):
    MEMBERS = [(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),(WCHAR, "snNameBuffer"),(DWORD, "dwStatus"),(BYTE, "reserved"),]

    
PMIB_IPMCAST_SCOPE = MIB_IPMCAST_SCOPE

class MIB_IPNETROW(NdrStructure):
    MEMBERS = [(DWORD, "dwIndex"),(DWORD, "dwPhysAddrLen"),(BYTE, "bPhysAddr"),(DWORD, "dwAddr"),(DWORD, "dwType"),]

    
PMIB_IPNETROW = MIB_IPNETROW

class MIB_IPNETTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPNETROW, "table"),(BYTE, "reserved"),]

    
PMIB_IPNETTABLE = MIB_IPNETTABLE

class MIB_IPSTATS(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwDefaultTTL"),(DWORD, "dwInReceives"),(DWORD, "dwInHdrErrors"),(DWORD, "dwInAddrErrors"),(DWORD, "dwForwDatagrams"),(DWORD, "dwInUnknownProtos"),(DWORD, "dwInDiscards"),(DWORD, "dwInDelivers"),(DWORD, "dwOutRequests"),(DWORD, "dwRoutingDiscards"),(DWORD, "dwOutDiscards"),(DWORD, "dwOutNoRoutes"),(DWORD, "dwReasmTimeout"),(DWORD, "dwReasmReqds"),(DWORD, "dwReasmOks"),(DWORD, "dwReasmFails"),(DWORD, "dwFragOks"),(DWORD, "dwFragFails"),(DWORD, "dwFragCreates"),(DWORD, "dwNumIf"),(DWORD, "dwNumAddr"),(DWORD, "dwNumRoutes"),]

    
PMIB_IPSTATS = MIB_IPSTATS

class MIB_MFE_STATS_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_MFE_STATS, "table"),]

    
PMIB_MFE_STATS_TABLE = MIB_MFE_STATS_TABLE

class MIB_MFE_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_MFE, "table"),]

    
PMIB_MFE_TABLE = MIB_MFE_TABLE

class MIB_OPAQUE_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwId"),(U0, "u0"),]

    
PMIB_OPAQUE_INFO = MIB_OPAQUE_INFO

class MIB_OPAQUE_QUERY(NdrStructure):
    MEMBERS = [(DWORD, "dwVarId"),(DWORD, "rgdwVarIndex"),]

    
PMIB_OPAQUE_QUERY = MIB_OPAQUE_QUERY

class MIB_PROXYARP(NdrStructure):
    MEMBERS = [(DWORD, "dwAddress"),(DWORD, "dwMask"),(DWORD, "dwIfIndex"),]

    
PMIB_PROXYARP = MIB_PROXYARP

class MIB_TCPROW(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwLocalAddr"),(DWORD, "dwLocalPort"),(DWORD, "dwRemoteAddr"),(DWORD, "dwRemotePort"),]

    
PMIB_TCPROW = MIB_TCPROW

class MIB_TCPSTATS(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwRtoMin"),(DWORD, "dwRtoMax"),(DWORD, "dwMaxConn"),(DWORD, "dwActiveOpens"),(DWORD, "dwPassiveOpens"),(DWORD, "dwAttemptFails"),(DWORD, "dwEstabResets"),(DWORD, "dwCurrEstab"),(DWORD, "dwInSegs"),(DWORD, "dwOutSegs"),(DWORD, "dwRetransSegs"),(DWORD, "dwInErrs"),(DWORD, "dwOutRsts"),(DWORD, "dwNumConns"),]

    
PMIB_TCPSTATS = MIB_TCPSTATS

class MIB_TCPTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_TCPROW, "table"),(BYTE, "reserved"),]

    
PMIB_TCPTABLE = MIB_TCPTABLE

class MIB_UDPROW(NdrStructure):
    MEMBERS = [(DWORD, "dwLocalAddr"),(DWORD, "dwLocalPort"),]

    
PMIB_UDPROW = MIB_UDPROW

class MIB_UDPSTATS(NdrStructure):
    MEMBERS = [(DWORD, "dwInDatagrams"),(DWORD, "dwNoPorts"),(DWORD, "dwInErrors"),(DWORD, "dwOutDatagrams"),(DWORD, "dwNumAddrs"),]

    
PMIB_UDPSTATS = MIB_UDPSTATS

class MIB_UDPTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_UDPROW, "table"),(BYTE, "reserved"),]

    
PMIB_UDPTABLE = MIB_UDPTABLE

class MPR_SERVER_0(NdrStructure):
    MEMBERS = [(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),]

    
PMPR_SERVER_0 = MPR_SERVER_0

class MPR_SERVER_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPptpPorts"),(DWORD, "dwPptpPortFlags"),(DWORD, "dwNumL2tpPorts"),(DWORD, "dwL2tpPortFlags"),]

    
PMPR_SERVER_1 = MPR_SERVER_1

class MPR_SERVER_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPptpPorts"),(DWORD, "dwPptpPortFlags"),(DWORD, "dwNumL2tpPorts"),(DWORD, "dwL2tpPortFlags"),(DWORD, "dwNumSstpPorts"),(DWORD, "dwSstpPortFlags"),]

    
PMPR_SERVER_2 = MPR_SERVER_2

class PPP_NBFCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszWksta"),]

    

class PPP_IPCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),]

    

class PPP_IPCP_INFO2(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptons"),]

    

class PPP_IPXCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),]

    

class PPP_IPV6_CP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "dwError"),(BYTE, "bInterfaceIdentifier"),(BYTE, "bRemoteInterfaceIdentifier"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptions"),(BYTE, "bPrefix"),(DWORD, "dwPrefixLength"),]

    
PPPP_IPV6_CP_INFO = PPP_IPV6_CP_INFO

class PPP_ATCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),]

    

class PPP_CCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwRemoteOptions"),]

    

class PPP_LCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwTerminateReason"),(DWORD, "dwRemoteTerminateReason"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwRemoteEapTypeId"),]

    

class PPP_INFO(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO, "ip"),(PPP_IPXCP_INFO, "ipx"),(PPP_ATCP_INFO, "at"),]

    

class PPP_INFO_2(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO2, "ip"),(PPP_IPXCP_INFO, "ipx"),(PPP_ATCP_INFO, "at"),(PPP_CCP_INFO, "ccp"),(PPP_LCP_INFO, "lcp"),]

    

class PPP_INFO_3(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO2, "ip"),(PPP_IPV6_CP_INFO, "ipv6"),(PPP_CCP_INFO, "ccp"),(PPP_LCP_INFO, "lcp"),]

    

class RASI_PORT_0(NdrStructure):
    MEMBERS = [(DWORD, "dwPort"),(DWORD, "dwConnection"),(RAS_PORT_CONDITION, "dwPortCondition"),(DWORD, "dwTotalNumberOfCalls"),(DWORD, "dwConnectDuration"),(WCHAR, "wszPortName"),(WCHAR, "wszMediaName"),(WCHAR, "wszDeviceName"),(WCHAR, "wszDeviceType"),]

    
PRASI_PORT_0 = RASI_PORT_0

class RASI_PORT_1(NdrStructure):
    MEMBERS = [(DWORD, "dwPort"),(DWORD, "dwConnection"),(RAS_HARDWARE_CONDITION, "dwHardwareCondition"),(DWORD, "dwLineSpeed"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),]

    
PRASI_PORT_1 = RASI_PORT_1

class RASI_CONNECTION_0(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(DWORD, "dwInterface"),(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),]

    
PRASI_CONNECTION_0 = RASI_CONNECTION_0

class RASI_CONNECTION_1(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(DWORD, "dwInterface"),(PPP_INFO, "PppInfo"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),]

    
PRASI_CONNECTION_1 = RASI_CONNECTION_1

class RASI_CONNECTION_2(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(WCHAR, "wszUserName"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(GUID, "guid"),(PPP_INFO_2, "PppInfo2"),]

    
PRASI_CONNECTION_2 = RASI_CONNECTION_2

class RASI_CONNECTION_3(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "dwConnection"),(WCHAR, "wszUserName"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(GUID, "guid"),(PPP_INFO_3, "PppInfo3"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "timer"),]

    
PRASI_CONNECTION_3 = RASI_CONNECTION_3

class MPRI_INTERFACE_0(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),]

    
PMPRI_INTERFACE_0 = MPRI_INTERFACE_0

class MPRI_INTERFACE_1(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(LPWSTR, "lpwsDialoutHoursRestriction"),]

    
PMPRI_INTERFACE_1 = MPRI_INTERFACE_1

class MPRI_INTERFACE_2(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(DWORD, "dwfOptions"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),(DWORD, "ipaddr"),(DWORD, "ipaddrDns"),(DWORD, "ipaddrDnsAlt"),(DWORD, "ipaddrWins"),(DWORD, "ipaddrWinsAlt"),(DWORD, "dwfNetProtocols"),(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szX25PadType"),(WCHAR, "szX25Address"),(WCHAR, "szX25Facilities"),(WCHAR, "szX25UserData"),(DWORD, "dwChannels"),(DWORD, "dwSubEntries"),(DWORD, "dwDialMode"),(DWORD, "dwDialExtraPercent"),(DWORD, "dwDialExtraSampleSeconds"),(DWORD, "dwHangUpExtraPercent"),(DWORD, "dwHangUpExtraSampleSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(DWORD, "dwType"),(DWORD, "dwEncryptionType"),(DWORD, "dwCustomAuthKey"),(DWORD, "dwCustomAuthDataSize"),(LPBYTE, "lpbCustomAuthData"),(GUID, "guidId"),(DWORD, "dwVpnStrategy"),]

    
PMPRI_INTERFACE_2 = MPRI_INTERFACE_2

class MPRI_INTERFACE_3(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(DWORD, "dwfOptions"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),(DWORD, "ipaddr"),(DWORD, "ipaddrDns"),(DWORD, "ipaddrDnsAlt"),(DWORD, "ipaddrWins"),(DWORD, "ipaddrWinsAlt"),(DWORD, "dwfNetProtocols"),(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szX25PadType"),(WCHAR, "szX25Address"),(WCHAR, "szX25Facilities"),(WCHAR, "szX25UserData"),(DWORD, "dwChannels"),(DWORD, "dwSubEntries"),(DWORD, "dwDialMode"),(DWORD, "dwDialExtraPercent"),(DWORD, "dwDialExtraSampleSeconds"),(DWORD, "dwHangUpExtraPercent"),(DWORD, "dwHangUpExtraSampleSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(DWORD, "dwType"),(DWORD, "dwEncryptionType"),(DWORD, "dwCustomAuthKey"),(DWORD, "dwCustomAuthDataSize"),(LPBYTE, "lpbCustomAuthData"),(GUID, "guidId"),(DWORD, "dwVpnStrategy"),(ULONG, "AddressCount"),(IN6_ADDR, "ipv6addrDns"),(IN6_ADDR, "ipv6addrDnsAlt"),(PIN6_ADDR, "ipv6addr"),]

    
PMPRI_INTERFACE_3 = MPRI_INTERFACE_3

class MPR_DEVICE_0(NdrStructure):
    MEMBERS = [(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),]

    
PMPR_DEVICE_0 = MPR_DEVICE_0

class MPR_DEVICE_1(NdrStructure):
    MEMBERS = [(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),]

    
PMPR_DEVICE_1 = MPR_DEVICE_1

class MPR_CREDENTIALSEX_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(DWORD, "dwOffset"),(BYTE, "bData"),]

    
PMPR_CREDENTIALSEX_1 = MPR_CREDENTIALSEX_1

class IFFILTER_INFO(NdrStructure):
    MEMBERS = [(BOOL, "bEnableFragChk"),]

    
PIFFILTER_INFO = IFFILTER_INFO

class MPR_FILTER_0(NdrStructure):
    MEMBERS = [(BOOL, "fEnable"),]

    
PMPR_FILTER_0 = MPR_FILTER_0

class IPX_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "RoutingTableHashSize"),(ULONG, "EventLogMask"),]

    
PIPX_GLOBAL_INFO = IPX_GLOBAL_INFO

class IPX_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdministratorState"),(ULONG, "NetbiosAccept"),(ULONG, "NetbiosDeliver"),]

    
PIPX_IF_INFO = IPX_IF_INFO

class IPXWAN_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Adminstate"),]

    
PIPXWAN_IF_INFO = IPXWAN_IF_INFO

class IPX_STATIC_ROUTE_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(USHORT, "TickCount"),(USHORT, "HopCount"),(UCHAR, "NextHopMacAddress"),]

    
PIPX_STATIC_ROUTE_INFO = IPX_STATIC_ROUTE_INFO
IPX_STATIC_SERVICE_INFO = IPX_SERVER_ENTRY
PPIPX_STATIC_SERVICE_INFO = IPX_SERVER_ENTRY

class IPX_SERVER_ENTRY(NdrStructure):
    MEMBERS = [(USHORT, "Type"),(UCHAR, "Name"),(UCHAR, "Network"),(UCHAR, "Node"),(UCHAR, "Socket"),(USHORT, "HopCount"),]

    
PIPX_SERVER_ENTRY = IPX_SERVER_ENTRY

class IPX_STATIC_NETBIOS_NAME_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),]

    
PIPX_STATIC_NETBIOS_NAME_INFO = IPX_STATIC_NETBIOS_NAME_INFO

class IPX_ADAPTER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "PacketType"),(WCHAR, "AdapterName"),]

    
PIPX_ADAPTER_INFO = IPX_ADAPTER_INFO

class IPX_TRAFFIC_FILTER_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "FilterAction"),]

    
PIPX_TRAFFIC_FILTER_GLOBAL_INFO = IPX_TRAFFIC_FILTER_GLOBAL_INFO

class IPX_TRAFFIC_FILTER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "FilterDefinition"),(UCHAR, "DestinationNetwork"),(UCHAR, "DestinationNetworkMask"),(UCHAR, "DestinationNode"),(UCHAR, "DestinationSocket"),(UCHAR, "SourceNetwork"),(UCHAR, "SourceNetworkMask"),(UCHAR, "SourceNode"),(UCHAR, "SourceSocket"),(UCHAR, "PacketType"),]

    
PIPX_TRAFFIC_FILTER_INFO = IPX_TRAFFIC_FILTER_INFO

class IF_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),]

    
PIF_TABLE_INDEX = IF_TABLE_INDEX

class ROUTING_TABLE_INDEX(NdrStructure):
    MEMBERS = [(UCHAR, "Network"),]

    
PROUTING_TABLE_INDEX = ROUTING_TABLE_INDEX

class STATIC_ROUTES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(UCHAR, "Network"),]

    
PSTATIC_ROUTES_TABLE_INDEX = STATIC_ROUTES_TABLE_INDEX

class SERVICES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(USHORT, "ServiceType"),(UCHAR, "ServiceName"),]

    
PSERVICES_TABLE_INDEX = SERVICES_TABLE_INDEX

class STATIC_SERVICES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(USHORT, "ServiceType"),(UCHAR, "ServiceName"),]

    
PSTATIC_SERVICES_TABLE_INDEX = STATIC_SERVICES_TABLE_INDEX

class IPX_MIB_INDEX(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (IF_TABLE_INDEX, "InterfaceTableIndex"),2 : (ROUTING_TABLE_INDEX, "RoutingTableIndex"),3 : (STATIC_ROUTES_TABLE_INDEX, "StaticRoutesTableIndex"),4 : (SERVICES_TABLE_INDEX, "ServicesTableIndex"),5 : (STATIC_SERVICES_TABLE_INDEX, "StaticServicesTableIndex"),}

    
PIPX_MIB_INDEX = IPX_MIB_INDEX

class IPX_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(IPX_MIB_INDEX, "MibIndex"),]

    
PIPX_MIB_GET_INPUT_DATA = IPX_MIB_GET_INPUT_DATA

class IPXMIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "OperState"),(UCHAR, "PrimaryNetNumber"),(UCHAR, "Node"),(UCHAR, "SysName"),(ULONG, "MaxPathSplits"),(ULONG, "IfCount"),(ULONG, "DestCount"),(ULONG, "ServCount"),]

    
PIPXMIB_BASE = IPXMIB_BASE

class IPX_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "IfOperState"),(ULONG, "MaxPacketSize"),(ULONG, "InHdrErrors"),(ULONG, "InFiltered"),(ULONG, "InNoRoutes"),(ULONG, "InDiscards"),(ULONG, "InDelivers"),(ULONG, "OutFiltered"),(ULONG, "OutDiscards"),(ULONG, "OutDelivers"),(ULONG, "NetbiosReceived"),(ULONG, "NetbiosSent"),]

    
PIPX_IF_STATS = IPX_IF_STATS

class IPX_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "AdministratorState"),(ULONG, "AdapterIndex"),(UCHAR, "InterfaceName"),(ULONG, "InterfaceType"),(ULONG, "MediaType"),(UCHAR, "NetNumber"),(UCHAR, "MacAddress"),(ULONG, "Delay"),(ULONG, "Throughput"),(ULONG, "NetbiosAccept"),(ULONG, "NetbiosDeliver"),(ULONG, "EnableIpxWanNegotiation"),(IPX_IF_STATS, "IfStats"),]

    
PIPX_INTERFACE = IPX_INTERFACE

class IPX_ROUTE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "Protocol"),(UCHAR, "Network"),(USHORT, "TickCount"),(USHORT, "HopCount"),(UCHAR, "NextHopMacAddress"),(ULONG, "Flags"),]

    
PIPX_ROUTE = IPX_ROUTE

class IPX_SERVICE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "Protocol"),(IPX_SERVER_ENTRY, "Server"),]

    
PIPX_SERVICE = IPX_SERVICE

class IPX_MIB_ROW(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (IPX_INTERFACE, "Interface"),2 : (IPX_ROUTE, "Route"),3 : (IPX_SERVICE, "Service"),}

    
PIPX_MIB_ROW = IPX_MIB_ROW

class IPX_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(IPX_MIB_ROW, "MibRow"),]

    
PIPX_MIB_SET_INPUT_DATA = IPX_MIB_SET_INPUT_DATA

class SAP_SERVICE_FILTER_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(UCHAR, "ServiceName"),]

    
PSAP_SERVICE_FILTER_INFO = SAP_SERVICE_FILTER_INFO

class SAP_IF_FILTERS(NdrStructure):
    MEMBERS = [(ULONG, "SupplyFilterAction"),(ULONG, "SupplyFilterCount"),(ULONG, "ListenFilterAction"),(ULONG, "ListenFilterCount"),(SAP_SERVICE_FILTER_INFO, "ServiceFilter"),]

    
PSAP_IF_FILTERS = SAP_IF_FILTERS

class SAP_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdminState"),(ULONG, "UpdateMode"),(ULONG, "PacketType"),(ULONG, "Supply"),(ULONG, "Listen"),(ULONG, "GetNearestServerReply"),(ULONG, "PeriodicUpdateInterval"),(ULONG, "AgeIntervalMultiplier"),]

    
PSAP_IF_INFO = SAP_IF_INFO

class SAP_IF_CONFIG(NdrStructure):
    MEMBERS = [(SAP_IF_INFO, "SapIfInfo"),(SAP_IF_FILTERS, "SapIfFilters"),]

    
PSAP_IF_CONFIG = SAP_IF_CONFIG

class SAP_MIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "SapOperState"),]

    
PSAP_MIB_BASE = SAP_MIB_BASE

class SAP_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "SapIfOperState"),(ULONG, "SapIfInputPackets"),(ULONG, "SapIfOutputPackets"),]

    
PSAP_IF_STATS = SAP_IF_STATS

class SAP_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(SAP_IF_INFO, "SapIfInfo"),(SAP_IF_STATS, "SapIfStats"),]

    
PSAP_INTERFACE = SAP_INTERFACE

class SAP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(ULONG, "InterfaceIndex"),]

    
PSAP_MIB_GET_INPUT_DATA = SAP_MIB_GET_INPUT_DATA

class SAP_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(SAP_INTERFACE, "SapInterface"),]

    
PSAP_MIB_SET_INPUT_DATA = SAP_MIB_SET_INPUT_DATA

class RIPMIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "RIPOperState"),]

    
PRIPMIB_BASE = RIPMIB_BASE

class RIP_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "RipIfOperState"),(ULONG, "RipIfInputPackets"),(ULONG, "RipIfOutputPackets"),]

    
PRIP_IF_STATS = RIP_IF_STATS

class RIP_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdminState"),(ULONG, "UpdateMode"),(ULONG, "PacketType"),(ULONG, "Supply"),(ULONG, "Listen"),(ULONG, "PeriodicUpdateInterval"),(ULONG, "AgeIntervalMultiplier"),]

    
PRIP_IF_INFO = RIP_IF_INFO

class RIP_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(RIP_IF_INFO, "RipIfInfo"),(RIP_IF_STATS, "RipIfStats"),]

    
PRIP_INTERFACE = RIP_INTERFACE

class RIP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(ULONG, "InterfaceIndex"),]

    
PRIP_MIB_GET_INPUT_DATA = RIP_MIB_GET_INPUT_DATA

class RIP_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(RIP_INTERFACE, "RipInterface"),]

    
PRIP_MIB_SET_INPUT_DATA = RIP_MIB_SET_INPUT_DATA

class EAPTLS_HASH(NdrStructure):
    MEMBERS = [(DWORD, "cbHash"),(BYTE, "pbHash"),]

    

class EAPTLS_USER_PROPERTIES(NdrStructure):
    MEMBERS = [(DWORD, "reserved"),(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "fFlags"),(EAPTLS_HASH, "Hash"),(PWCHAR, "pwszDiffUser"),(DWORD, "dwPinOffset"),(PWCHAR, "pwszPin"),(USHORT, "usLength"),(USHORT, "usMaximumLength"),(UCHAR, "ucSeed"),(WCHAR, "awszString"),]

    

class IPBOOTP_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_ServerCount"),]

    
PIPBOOTP_GLOBAL_CONFIG = IPBOOTP_GLOBAL_CONFIG

class IPBOOTP_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_RelayMode"),(DWORD, "IC_MaxHopCount"),(DWORD, "IC_MinSecondsSinceBoot"),]

    
PIPBOOTP_IF_CONFIG = IPBOOTP_IF_CONFIG

class IPBOOTP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(DWORD, "IMGID_IfIndex"),]

    
PIPBOOTP_MIB_GET_INPUT_DATA = IPBOOTP_MIB_GET_INPUT_DATA

class IPBOOTP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(DWORD, "IMGOD_IfIndex"),(BYTE, "IMGOD_Buffer"),]

    
PIPBOOTP_MIB_GET_OUTPUT_DATA = IPBOOTP_MIB_GET_OUTPUT_DATA

class IPBOOTP_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_ArpUpdateFailures"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_RequestsDiscarded"),(DWORD, "IS_RepliesReceived"),(DWORD, "IS_RepliesDiscarded"),]

    
PIPBOOTP_IF_STATS = IPBOOTP_IF_STATS

class IPBOOTP_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IB_State"),(DWORD, "IB_AddrCount"),]

    
PIPBOOTP_IF_BINDING = IPBOOTP_IF_BINDING

class IPBOOTP_IP_ADDRESS(NdrStructure):
    MEMBERS = [(DWORD, "IA_Address"),(DWORD, "IA_Netmask"),]

    
PIPBOOTP_IP_ADDRESS = IPBOOTP_IP_ADDRESS

class DHCPV6R_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(DWORD, "IMGOD_IfIndex"),(BYTE, "IMGOD_Buffer"),]

    
PDHCPV6R_MIB_GET_OUTPUT_DATA = DHCPV6R_MIB_GET_OUTPUT_DATA

class DHCPV6R_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_RequestsDiscarded"),(DWORD, "IS_RepliesReceived"),(DWORD, "IS_RepliesDiscarded"),]

    
PDHCPV6R_IF_STATS = DHCPV6R_IF_STATS

class DHCPV6R_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(DWORD, "IMGID_IfIndex"),]

    
PDHCPV6R_MIB_GET_INPUT_DATA = DHCPV6R_MIB_GET_INPUT_DATA

class DHCPV6R_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_ServerCount"),]

    
PDHCPV6R_GLOBAL_CONFIG = DHCPV6R_GLOBAL_CONFIG

class DHCPV6R_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_RelayMode"),(DWORD, "IC_MaxHopCount"),(DWORD, "IC_MinElapsedTime"),]

    
PDHCPV6R_IF_CONFIG = DHCPV6R_IF_CONFIG

class IPRIP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(U0, "u0"),]

    
PIPRIP_MIB_GET_INPUT_DATA = IPRIP_MIB_GET_INPUT_DATA

class IPRIP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(U0, "u0"),(BYTE, "IMGOD_Buffer"),]

    
PIPRIP_MIB_GET_OUTPUT_DATA = IPRIP_MIB_GET_OUTPUT_DATA

class IPRIP_GLOBAL_STATS(NdrStructure):
    MEMBERS = [(DWORD, "GS_SystemRouteChanges"),(DWORD, "GS_TotalResponsesSent"),]

    
PIPRIP_GLOBAL_STATS = IPRIP_GLOBAL_STATS

class IPRIP_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_MaxSendQueueSize"),(DWORD, "GC_MinTriggeredUpdateInterval"),(DWORD, "GC_PeerFilterMode"),(DWORD, "GC_PeerFilterCount"),]

    
PIPRIP_GLOBAL_CONFIG = IPRIP_GLOBAL_CONFIG

class IPRIP_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_RequestsSent"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_ResponsesSent"),(DWORD, "IS_ResponsesReceived"),(DWORD, "IS_BadResponsePacketsReceived"),(DWORD, "IS_BadResponseEntriesReceived"),(DWORD, "IS_TriggeredUpdatesSent"),]

    
PIPRIP_IF_STATS = IPRIP_IF_STATS

class IPRIP_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_Metric"),(DWORD, "IC_UpdateMode"),(DWORD, "IC_AcceptMode"),(DWORD, "IC_AnnounceMode"),(DWORD, "IC_ProtocolFlags"),(DWORD, "IC_RouteExpirationInterval"),(DWORD, "IC_RouteRemovalInterval"),(DWORD, "IC_FullUpdateInterval"),(DWORD, "IC_AuthenticationType"),(BYTE, "IC_AuthenticationKey"),(WORD, "IC_RouteTag"),(DWORD, "IC_UnicastPeerMode"),(DWORD, "IC_AcceptFilterMode"),(DWORD, "IC_AnnounceFilterMode"),(DWORD, "IC_UnicastPeerCount"),(DWORD, "IC_AcceptFilterCount"),(DWORD, "IC_AnnounceFilterCount"),]

    
PIPRIP_IF_CONFIG = IPRIP_IF_CONFIG

class IPRIP_ROUTE_FILTER(NdrStructure):
    MEMBERS = [(DWORD, "RF_LoAddress"),(DWORD, "RF_HiAddress"),]

    
PIPRIP_ROUTE_FILTER = IPRIP_ROUTE_FILTER

class IPRIP_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IB_State"),(DWORD, "IB_AddrCount"),]

    
PIPRIP_IF_BINDING = IPRIP_IF_BINDING

class IPRIP_IP_ADDRESS(NdrStructure):
    MEMBERS = [(DWORD, "IA_Address"),(DWORD, "IA_Netmask"),]

    
PIPRIP_IP_ADDRESS = IPRIP_IP_ADDRESS

class IPRIP_PEER_STATS(NdrStructure):
    MEMBERS = [(DWORD, "PS_LastPeerRouteTag"),(DWORD, "PS_LastPeerUpdateTickCount"),(DWORD, "PS_LastPeerUpdateVersion"),(DWORD, "PS_BadResponsePacketsFromPeer"),(DWORD, "PS_BadResponseEntriesFromPeer"),]

    
PIPRIP_PEER_STATS = IPRIP_PEER_STATS

class IGMP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "TypeId"),(USHORT, "Flags"),(USHORT, "Signature"),(DWORD, "IfIndex"),(DWORD, "RasClientAddr"),(DWORD, "GroupAddr"),(DWORD, "Count"),]

    
PIGMP_MIB_GET_INPUT_DATA = IGMP_MIB_GET_INPUT_DATA

class IGMP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "TypeId"),(DWORD, "Flags"),(DWORD, "Count"),(BYTE, "Buffer"),]

    
PIGMP_MIB_GET_OUTPUT_DATA = IGMP_MIB_GET_OUTPUT_DATA

class IGMP_MIB_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "LoggingLevel"),(DWORD, "RasClientStats"),]

    
PIGMP_MIB_GLOBAL_CONFIG = IGMP_MIB_GLOBAL_CONFIG

class IGMP_MIB_GLOBAL_STATS(NdrStructure):
    MEMBERS = [(DWORD, "CurrentGroupMemberships"),(DWORD, "GroupMembershipsAdded"),]

    
PIGMP_MIB_GLOBAL_STATS = IGMP_MIB_GLOBAL_STATS

class IGMP_MIB_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IfType"),(DWORD, "State"),(DWORD, "AddrCount"),]

    
PIGMP_MIB_IF_BINDING = IGMP_MIB_IF_BINDING

class IGMP_MIB_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(DWORD, "Flags"),(DWORD, "IgmpProtocolType"),(DWORD, "RobustnessVariable"),(DWORD, "StartupQueryInterval"),(DWORD, "StartupQueryCount"),(DWORD, "GenQueryInterval"),(DWORD, "GenQueryMaxResponseTime"),(DWORD, "LastMemQueryInterval"),(DWORD, "LastMemQueryCount"),(DWORD, "OtherQuerierPresentInterval"),(DWORD, "GroupMembershipTimeout"),(DWORD, "NumStaticGroups"),]

    
PIGMP_MIB_IF_CONFIG = IGMP_MIB_IF_CONFIG

class IGMP_MIB_IF_GROUPS_LIST(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(DWORD, "NumGroups"),(BYTE, "Buffer"),]

    
PIGMP_MIB_IF_GROUPS_LIST = IGMP_MIB_IF_GROUPS_LIST

class IGMP_MIB_GROUP_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "IpAddr"),(DWORD, "GroupUpTime"),(DWORD, "GroupExpiryTime"),(DWORD, "LastReporter"),(DWORD, "V1HostPresentTimeLeft"),(DWORD, "Flags"),]

    
PIGMP_MIB_GROUP_INFO = IGMP_MIB_GROUP_INFO

class IGMP_MIB_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(BYTE, "State"),(BYTE, "QuerierState"),(DWORD, "IgmpProtocolType"),(DWORD, "QuerierIpAddr"),(DWORD, "ProxyIfIndex"),(DWORD, "QuerierPresentTimeLeft"),(DWORD, "LastQuerierChangeTime"),(DWORD, "V1QuerierPresentTimeLeft"),(DWORD, "Uptime"),(DWORD, "TotalIgmpPacketsReceived"),(DWORD, "TotalIgmpPacketsForRouter"),(DWORD, "GeneralQueriesReceived"),(DWORD, "WrongVersionQueries"),(DWORD, "JoinsReceived"),(DWORD, "LeavesReceived"),(DWORD, "CurrentGroupMemberships"),(DWORD, "GroupMembershipsAdded"),(DWORD, "WrongChecksumPackets"),(DWORD, "ShortPacketsReceived"),(DWORD, "LongPacketsReceived"),(DWORD, "PacketsWithoutRtrAlert"),]

    
PIGMP_MIB_IF_STATS = IGMP_MIB_IF_STATS

class IGMP_MIB_GROUP_IFS_LIST(NdrStructure):
    MEMBERS = [(DWORD, "GroupAddr"),(DWORD, "NumInterfaces"),(BYTE, "Buffer"),]

    
PIGMP_MIB_GROUP_IFS_LIST = IGMP_MIB_GROUP_IFS_LIST

class IGMP_MIB_GROUP_SOURCE_INFO_V3(NdrStructure):
    MEMBERS = [(DWORD, "Source"),(DWORD, "SourceExpiryTime"),(DWORD, "SourceUpTime"),(DWORD, "Flags"),]

    
PIGMP_MIB_GROUP_SOURCE_INFO_V3 = IGMP_MIB_GROUP_SOURCE_INFO_V3

class IGMP_MIB_GROUP_INFO_V3(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "IpAddr"),(DWORD, "GroupUpTime"),(DWORD, "GroupExpiryTime"),(DWORD, "LastReporter"),(DWORD, "V1HostPresentTimeLeft"),(DWORD, "Flags"),(DWORD, "Version"),(DWORD, "Size"),(DWORD, "FilterType"),(DWORD, "V2HostPresentTimeLeft"),(DWORD, "NumSources"),]

    
PIGMP_MIB_GROUP_INFO_V3 = IGMP_MIB_GROUP_INFO_V3

class INTERFACE_ROUTE_ENTRY(NdrStructure):
    MEMBERS = [(DWORD, "dwIndex"),(INTERFACE_ROUTE_INFO, "routeInfo"),]

    
PINTERFACE_ROUTE_ENTRY = INTERFACE_ROUTE_ENTRY

class IP_NAT_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),]

    
PIP_NAT_MIB_QUERY = IP_NAT_MIB_QUERY

class IP_NAT_DIRECTION(NdrEnum):
    MAP = ((0 , 'NatInboundDirection'),(1 , 'NatOutboundDirection'),)        

class IP_NAT_SESSION_MAPPING(NdrStructure):
    MEMBERS = [(UCHAR, "Protocol"),(ULONG, "PrivateAddress"),(USHORT, "PrivatePort"),(ULONG, "PublicAddress"),(USHORT, "PublicPort"),(ULONG, "RemoteAddress"),(USHORT, "RemotePort"),(IP_NAT_DIRECTION, "Direction"),(ULONG, "IdleTime"),]

    
PIP_NAT_SESSION_MAPPING = IP_NAT_SESSION_MAPPING

class IP_NAT_ENUMERATE_SESSION_MAPPINGS(NdrStructure):
    MEMBERS = [(ULONG, "Index"),(ULONG, "EnumerateContext"),(ULONG, "EnumerateCount"),(ULONG, "EnumerateTotalHint"),(IP_NAT_SESSION_MAPPING, "EnumerateTable"),]

    
PIP_NAT_ENUMERATE_SESSION_MAPPINGS = IP_NAT_ENUMERATE_SESSION_MAPPINGS

class IP_NAT_INTERFACE_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "TotalMappings"),(ULONG, "InboundMappings"),(ULONG64, "BytesForward"),(ULONG64, "BytesReverse"),(ULONG64, "PacketsForward"),(ULONG64, "PacketsReverse"),(ULONG64, "RejectsForward"),(ULONG64, "RejectsReverse"),]

    
PIP_NAT_INTERFACE_STATISTICS = IP_NAT_INTERFACE_STATISTICS

class IP_DNS_PROXY_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),]

    
PIP_DNS_PROXY_MIB_QUERY = IP_DNS_PROXY_MIB_QUERY

class IP_DNS_PROXY_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "MessagesIgnored"),(ULONG, "QueriesReceived"),(ULONG, "ResponsesReceived"),(ULONG, "QueriesSent"),(ULONG, "ResponsesSent"),]

    
PIP_DNS_PROXY_STATISTICS = IP_DNS_PROXY_STATISTICS

class IP_AUTO_DHCP_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),(ULONG, "Reserved"),]

    
PIP_AUTO_DHCP_MIB_QUERY = IP_AUTO_DHCP_MIB_QUERY

class IP_AUTO_DHCP_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "MessagesIgnored"),(ULONG, "BootpOffersSent"),(ULONG, "DiscoversReceived"),(ULONG, "InformsReceived"),(ULONG, "OffersSent"),(ULONG, "RequestsReceived"),(ULONG, "AcksSent"),(ULONG, "NaksSent"),(ULONG, "DeclinesReceived"),(ULONG, "ReleasesReceived"),]

    
PIP_AUTO_DHCP_STATISTICS = IP_AUTO_DHCP_STATISTICS

class MIB_DA_MSG(NdrStructure):
    MEMBERS = [(UINT32, "op_code"),(UINT32, "ret_code"),(UINT32, "in_snmp_id"),(UINT32, "obj_id"),(UINT32, "attr_id"),(UINT32, "inst_id"),(UINT32, "next_snmp_id"),(UINT32, "creator"),(UINT32, "attr_type"),(UINT32, "inst_cnt"),(UINT32, "map_flag"),(ULONG_PTR, "data"),]

    

class IP_AUTO_DHCP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(ULONG, "LeaseTime"),(ULONG, "ScopeNetwork"),(ULONG, "ScopeMask"),(ULONG, "ExclusionCount"),(ULONG, "ExclusionArray"),]

    
PIP_AUTO_DHCP_GLOBAL_INFO = IP_AUTO_DHCP_GLOBAL_INFO

class IP_AUTO_DHCP_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),]

    
PIP_AUTO_DHCP_INTERFACE_INFO = IP_AUTO_DHCP_INTERFACE_INFO

class IP_DNS_PROXY_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(ULONG, "TimeoutSeconds"),]

    
PIP_DNS_PROXY_GLOBAL_INFO = IP_DNS_PROXY_GLOBAL_INFO

class IP_DNS_PROXY_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),]

    
PIP_DNS_PROXY_INTERFACE_INFO = IP_DNS_PROXY_INTERFACE_INFO

class IP_NAT_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(RTR_INFO_BLOCK_HEADER, "Header"),]

    
PIP_NAT_GLOBAL_INFO = IP_NAT_GLOBAL_INFO

class IP_NAT_TIMEOUT(NdrStructure):
    MEMBERS = [(ULONG, "TCPTimeoutSeconds"),(ULONG, "UDPTimeoutSeconds"),]

    
PIP_NAT_TIMEOUT = IP_NAT_TIMEOUT

class IP_NAT_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Index"),(ULONG, "Flags"),(RTR_INFO_BLOCK_HEADER, "Header"),]

    
PIP_NAT_INTERFACE_INFO = IP_NAT_INTERFACE_INFO

class IP_NAT_ADDRESS_RANGE(NdrStructure):
    MEMBERS = [(ULONG, "StartAddress"),(ULONG, "EndAddress"),(ULONG, "SubnetMask"),]

    
PIP_NAT_ADDRESS_RANGE = IP_NAT_ADDRESS_RANGE

class IP_NAT_PORT_MAPPING(NdrStructure):
    MEMBERS = [(UCHAR, "Protocol"),(USHORT, "PublicPort"),(ULONG, "PublicAddress"),(USHORT, "PrivatePort"),(ULONG, "PrivateAddress"),]

    
PIP_NAT_PORT_MAPPING = IP_NAT_PORT_MAPPING

class IP_NAT_ADDRESS_MAPPING(NdrStructure):
    MEMBERS = [(ULONG, "PrivateAddress"),(ULONG, "PublicAddress"),(BOOLEAN, "AllowInboundSessions"),]

    
PIP_NAT_ADDRESS_MAPPING = IP_NAT_ADDRESS_MAPPING

class IP_ALG_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),]

    
PIP_ALG_GLOBAL_INFO = IP_ALG_GLOBAL_INFO

class RIP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(DWORD, "EventLogMask"),]

    
PRIP_GLOBAL_INFO = RIP_GLOBAL_INFO

class RIP_ROUTE_FILTER_INFO(NdrStructure):
    MEMBERS = [(UCHAR, "Network"),(UCHAR, "Mask"),]

    
PRIP_ROUTE_FILTER_INFO = RIP_ROUTE_FILTER_INFO

class RIP_IF_FILTERS(NdrStructure):
    MEMBERS = [(ULONG, "SupplyFilterAction"),(ULONG, "SupplyFilterCount"),(ULONG, "ListenFilterAction"),(ULONG, "ListenFilterCount"),(RIP_ROUTE_FILTER_INFO, "RouteFilter"),]

    
PRIP_IF_FILTERS = RIP_IF_FILTERS

class RIP_IF_CONFIG(NdrStructure):
    MEMBERS = [(RIP_IF_INFO, "RipIfInfo"),(RIP_IF_FILTERS, "RipIfFilters"),]

    
PRIP_IF_CONFIG = RIP_IF_CONFIG

class SAP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(DWORD, "EventLogMask"),]

    
PSAP_GLOBAL_INFO = SAP_GLOBAL_INFO

class OSPF_ROUTE_FILTER(NdrStructure):
    MEMBERS = [(DWORD, "dwAddress"),(DWORD, "dwMask"),]

    
POSPF_ROUTE_FILTER = OSPF_ROUTE_FILTER

class OSPF_FILTER_ACTION(NdrEnum):
    MAP = ((0 , 'ACTION_DROP'),(1 , 'ACTION_ACCEPT'),)        

class OSPF_ROUTE_FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "type"),(OSPF_FILTER_ACTION, "ofaActionOnMatch"),(DWORD, "dwNumFilters"),(OSPF_ROUTE_FILTER, "pFilters"),]

    
POSPF_ROUTE_FILTER_INFO = OSPF_ROUTE_FILTER_INFO

class OSPF_PROTO_FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "type"),(OSPF_FILTER_ACTION, "ofaActionOnMatch"),(DWORD, "dwNumProtoIds"),(DWORD, "pdwProtoId"),]

    
POSPF_PROTO_FILTER_INFO = OSPF_PROTO_FILTER_INFO

class OSPF_GLOBAL_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "routerId"),(DWORD, "ASBrdrRtr"),(DWORD, "logLevel"),]

    
POSPF_GLOBAL_PARAM = OSPF_GLOBAL_PARAM

class OSPF_AREA_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "areaId"),(DWORD, "authType"),(DWORD, "importASExtern"),(DWORD, "stubMetric"),(DWORD, "importSumAdv"),]

    
POSPF_AREA_PARAM = OSPF_AREA_PARAM

class OSPF_AREA_RANGE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "areaId"),(DWORD, "rangeNet"),(DWORD, "rangeMask"),]

    
POSPF_AREA_RANGE_PARAM = OSPF_AREA_RANGE_PARAM

class OSPF_VIRT_INTERFACE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "transitAreaId"),(DWORD, "virtNeighborRouterId"),(DWORD, "transitDelay"),(DWORD, "retransInterval"),(DWORD, "helloInterval"),(DWORD, "deadInterval"),(BYTE, "password"),]

    
POSPF_VIRT_INTERFACE_PARAM = OSPF_VIRT_INTERFACE_PARAM

class OSPF_INTERFACE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "intfIpAddr"),(DWORD, "intfSubnetMask"),(DWORD, "areaId"),(DWORD, "intfType"),(DWORD, "routerPriority"),(DWORD, "transitDelay"),(DWORD, "retransInterval"),(DWORD, "helloInterval"),(DWORD, "deadInterval"),(DWORD, "pollInterval"),(DWORD, "metricCost"),(BYTE, "password"),(DWORD, "mtuSize"),]

    
POSPF_INTERFACE_PARAM = OSPF_INTERFACE_PARAM

class OSPF_NBMA_NEIGHBOR_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "neighborIpAddr"),(DWORD, "intfIpAddr"),(DWORD, "neighborPriority"),]

    
POSPF_NBMA_NEIGHBOR_PARAM = OSPF_NBMA_NEIGHBOR_PARAM

class RASDEVICETYPE(NdrEnum):
    MAP = ((0 , 'RDT_Modem'),(1 , 'RDT_X25'),(2 , 'RDT_Isdn'),(3 , 'RDT_Serial'),(4 , 'RDT_FrameRelay'),(5 , 'RDT_Atm'),(6 , 'RDT_Sonet'),(7 , 'RDT_Sw56'),(8 , 'RDT_Tunnel_Pptp'),(9 , 'RDT_Tunnel_L2tp'),(10 , 'RDT_Irda'),(11 , 'RDT_Parallel'),(12 , 'RDT_Other'),(13 , 'RDT_PPPoE'),(14 , 'RDT_Tunnel_Sstp'),(15 , 'RDT_Tunnel_Ikev2'),(65536 , 'RDT_Tunnel'),(131072 , 'RDT_Direct'),(262144 , 'RDT_Null_Modem'),(524288 , 'RDT_Broadband'),)        

class RASMAN_STATUS(NdrEnum):
    MAP = ((0 , 'OPEN'),(1 , 'CLOSED'),(2 , 'UNAVAILABLE'),(3 , 'REMOVED'),)        

class REQTYPES(NdrEnum):
    MAP = ((21 , 'REQTYPE_PORTENUM'),(22 , 'REQTYPE_GETINFO'),(73 , 'REQTYPE_GETDEVCONFIG'),(94 , 'REQTYPE_SETDEVICECONFIGINFO'),(95 , 'REQTYPE_GETDEVICECONFIGINFO'),(105 , 'REQTYPE_GETCALLEDID'),(106 , 'REQTYPE_SETCALLEDID'),(111 , 'REQTYPE_GETNDISWANDRIVERCAPS'),)        

class RASMAN_STATE(NdrEnum):
    MAP = ((0 , 'CONNECTING'),(1 , 'LISTENING'),(2 , 'CONNECTED'),(3 , 'DISCONNECTING'),(4 , 'DISCONNECTED'),(5 , 'LISTENCOMPLETED'),)        

class RASMAN_DISCONNECT_TYPE(NdrEnum):
    MAP = ((0 , 'USER_REQUESTED'),(1 , 'REMOTE_DISCONNECTION'),(2 , 'HARDWARE_FAILURE'),(3 , 'NOT_DISCONNECTED'),)        

class RASMAN_USAGE(NdrEnum):
    MAP = ((0 , 'CALL_NONE'),(1 , 'CALL_IN'),(2 , 'CALL_OUT'),(4 , 'CALL_ROUTER'),(8 , 'CALL_LOGON'),(16 , 'CALL_OUT_ONLY'),(32 , 'CALL_IN_ONLY'),(64 , 'CALL_OUTBOUND_ROUTER'),)        

class REQUESTBUFFER(NdrStructure):
    MEMBERS = [(DWORD, "RB_PCBIndex"),(REQTYPES, "RB_Reqtype"),(DWORD, "RB_Dummy"),(DWORD, "RB_Done"),(LONGLONG, "Alignment"),(BYTE, "RB_Buffer"),]

    

class DEVICECONFIGINFO(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(DWORD, "dwVersion"),(DWORD, "cbBuffer"),(DWORD, "cEntries"),(BYTE, "abdata"),]

    

class RAS_DEVICE_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(BOOL, "fWrite"),(BOOL, "fRasEnabled"),(BOOL, "fRouterEnabled"),(BOOL, "fRouterOutboundEnabled"),(DWORD, "dwTapiLineId"),(DWORD, "dwError"),(DWORD, "dwNumEndPoints"),(DWORD, "dwMaxOutCalls"),(DWORD, "dwMaxInCalls"),(DWORD, "dwMinWanEndPoints"),(DWORD, "dwMaxWanEndPoints"),(RASDEVICETYPE, "eDeviceType"),(GUID, "guidDevice"),(CHAR, "szPortName"),(CHAR, "szDeviceName"),(WCHAR, "wszDeviceName"),]

    
PRAS_DEVICE_INFO = RAS_DEVICE_INFO

class RAS_CALLEDID_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(BYTE, "bCalledId"),]

    
PRAS_CALLEDID_INFO = RAS_CALLEDID_INFO

class GETSETCALLEDID(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(BOOL, "fWrite"),(DWORD, "dwSize"),(GUID, "guidDevice"),(RAS_DEVICE_INFO, "rdi"),(RAS_CALLEDID_INFO, "rciInfo"),]

    

class RAS_NDISWAN_DRIVER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "DriverCaps"),(ULONG, "Reserved"),]

    
P_NDISWAN_DRIVER_INFO = RAS_NDISWAN_DRIVER_INFO

class GETNDISWANDRIVERCAPSSTRUCT(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(RAS_NDISWAN_DRIVER_INFO, "NdiswanDriverInfo"),]

    

class GETDEVCONFIGSTRUCT(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(CHAR, "devicetype"),(DWORD, "size"),(BYTE, "config"),]

    

class ENUM(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(DWORD, "size"),(DWORD, "entries"),(BYTE, "buffer"),]

    

class RASMAN_PORT_32(NdrStructure):
    MEMBERS = [(DWORD, "P_Port"),(CHAR, "P_PortName"),(RASMAN_STATUS, "P_Status"),(RASDEVICETYPE, "P_rdtDeviceType"),(RASMAN_USAGE, "P_ConfiguredUsage"),(RASMAN_USAGE, "P_CurrentUsage"),(CHAR, "P_MediaName"),(CHAR, "P_DeviceType"),(CHAR, "P_DeviceName"),(DWORD, "P_LineDeviceId"),(DWORD, "P_AddressId"),]

    

class RASMAN_INFO(NdrStructure):
    MEMBERS = [(RASMAN_STATUS, "RI_PortStatus"),(RASMAN_STATE, "RI_ConnState"),(DWORD, "RI_LinkSpeed"),(DWORD, "RI_LastError"),(RASMAN_USAGE, "RI_CurrentUsage"),(CHAR, "RI_DeviceTypeConnecting"),(CHAR, "RI_DeviceConnecting"),(CHAR, "RI_szDeviceType"),(CHAR, "RI_szDeviceName"),(CHAR, "RI_szPortName"),(RASMAN_DISCONNECT_TYPE, "RI_DisconnectType"),(DWORD, "RI_OwnershipFlag"),(DWORD, "RI_ConnectDuration"),(DWORD, "RI_BytesReceived"),(CHAR, "RI_Phonebook"),(CHAR, "RI_PhoneEntry"),(HANDLE, "RI_ConnectionHandle"),(DWORD, "RI_SubEntry"),(RASDEVICETYPE, "RI_rdtDeviceType"),(GUID, "RI_GuidEntry"),(DWORD, "RI_dwSessionId"),(DWORD, "RI_dwFlags"),(GUID, "RI_CorrelationGuid"),]

    

class INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(RASMAN_INFO, "info"),]

    

class RASRPC_CALLBACKLIST(NdrStructure):
    MEMBERS = [(WCHAR, "pszPortName"),(WCHAR, "pszDeviceName"),(WCHAR, "pszNumber"),(DWORD, "dwDeviceType"),(PPNEXT, "*pNext"),]

    
LPRASRPC_CALLBACKLIST = RASRPC_CALLBACKLIST

class RASRPC_STRINGLIST(NdrStructure):
    MEMBERS = [(WCHAR, "psz"),(PPNEXT, "*pNext"),]

    
LPRASRPC_STRINGLIST = RASRPC_STRINGLIST

class RASRPC_LOCATIONLIST(NdrStructure):
    MEMBERS = [(DWORD, "dwLocationId"),(DWORD, "iPrefix"),(DWORD, "iSuffix"),(PPNEXT, "*pNext"),]

    
LPRASRPC_LOCATIONLIST = RASRPC_LOCATIONLIST

class RASRPC_PBUSER(NdrStructure):
    MEMBERS = [(BOOL, "fOperatorDial"),(BOOL, "fPreviewPhoneNumber"),(BOOL, "fUseLocation"),(BOOL, "fShowLights"),(BOOL, "fShowConnectStatus"),(BOOL, "fCloseOnDial"),(BOOL, "fAllowLogonPhonebookEdits"),(BOOL, "fAllowLogonLocationEdits"),(BOOL, "fSkipConnectComplete"),(BOOL, "fNewEntryWizard"),(DWORD, "dwRedialAttempts"),(DWORD, "dwRedialSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(BOOL, "fRedialOnLinkFailure"),(BOOL, "fPopupOnTopWhenRedialing"),(BOOL, "fExpandAutoDialQuery"),(DWORD, "dwCallbackMode"),(LPRASRPC_CALLBACKLIST, "pCallbacks"),(WCHAR, "pszLastCallbackByCaller"),(DWORD, "dwPhonebookMode"),(WCHAR, "pszPersonalFile"),(WCHAR, "pszAlternatePath"),(LPRASRPC_STRINGLIST, "pPhonebooks"),(LPRASRPC_STRINGLIST, "pAreaCodes"),(BOOL, "fUseAreaAndCountry"),(LPRASRPC_STRINGLIST, "pPrefixes"),(LPRASRPC_STRINGLIST, "pSuffixes"),(LPRASRPC_LOCATIONLIST, "pLocations"),(DWORD, "dwXPhonebook"),(DWORD, "dwYPhonebook"),(WCHAR, "pszDefaultEntry"),(BOOL, "fInitialized"),(BOOL, "fDirty"),]

    
LPRASRPC_PBUSER = RASRPC_PBUSER
Interface("8f09f000-b7ed-11ce-bbd2-00001a181cad", "0.0",[Method("RMprAdminServerGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
Out((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
),Method("RRasAdminConnectionEnum",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'dwPreferedMaximumLength')),
Out((LPDWORD,'lpdwEntriesRead')),
Out((LPDWORD,'lpdwTotalEntries')),
InOut((LPDWORD,'lpdwResumeHandle')),
),Method("RRasAdminConnectionGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((DWORD,'hDimConnection')),
Out((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
),Method("RRasAdminConnectionClearStats",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hDimConnection')),
),Method("RRasAdminPortEnum",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((DWORD,'hRasConnection')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'dwPreferedMaximumLength')),
Out((LPDWORD,'lpdwEntriesRead')),
Out((LPDWORD,'lpdwTotalEntries')),
InOut((LPDWORD,'lpdwResumeHandle')),
),Method("RRasAdminPortGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((DWORD,'hPort')),
Out((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
),Method("RRasAdminPortClearStats",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hPort')),
),Method("RRasAdminPortReset",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hPort')),
),Method("RRasAdminPortDisconnect",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hPort')),
),Method("RRouterInterfaceTransportSetGlobalInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwTransportId')),
In((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
),Method("RRouterInterfaceTransportGetGlobalInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwTransportId')),
InOut((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
),Method("RRouterInterfaceGetHandle",
In((DIM_HANDLE,'hDimServer')),
In((LPWSTR,'lpwsInterfaceName')),
InOut((LPDWORD,'phInterface')),
In((DWORD,'fIncludeClientInterfaces')),
),Method("RRouterInterfaceCreate",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
InOut((LPDWORD,'phInterface')),
),Method("RRouterInterfaceGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceSetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceDelete",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceTransportRemove",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
),Method("RRouterInterfaceTransportAdd",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
In((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
),Method("RRouterInterfaceTransportGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
InOut((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
),Method("RRouterInterfaceTransportSetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
In((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
),Method("RRouterInterfaceEnum",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'dwPreferedMaximumLength')),
Out((LPDWORD,'lpdwEntriesRead')),
Out((LPDWORD,'lpdwTotalEntries')),
InOut((LPDWORD,'lpdwResumeHandle')),
),Method("RRouterInterfaceConnect",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((ULONG_PTR,'hEvent')),
In((DWORD,'fBlocking')),
In((DWORD,'dwCallersProcessId')),
),Method("RRouterInterfaceDisconnect",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceUpdateRoutes",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
In((ULONG_PTR,'hEvent')),
In((DWORD,'dwClientProcessId')),
),Method("RRouterInterfaceQueryUpdateResult",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
In((DWORD,'dwTransportId')),
Out((LPDWORD,'pUpdateResult')),
),Method("RRouterInterfaceUpdatePhonebookInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
),Method("RMIBEntryCreate",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
In((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBEntryDelete",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
In((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBEntrySet",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
In((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBEntryGet",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
InOut((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBEntryGetFirst",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
InOut((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBEntryGetNext",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
InOut((PDIM_MIB_ENTRY_CONTAINER,'pInfoStuct')),
),Method("RMIBGetTrapInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
InOut((PDIM_MIB_ENTRY_CONTAINER,'pInfoStruct')),
),Method("RMIBSetTrapInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwPid')),
In((DWORD,'dwRoutingPid')),
In((ULONG_PTR,'hEvent')),
In((DWORD,'dwClientProcessId')),
InOut((PDIM_MIB_ENTRY_CONTAINER,'pInfoStruct')),
),Method("RRasAdminConnectionNotification",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'fRegister')),
In((DWORD,'dwClientProcessId')),
In((ULONG_PTR,'hEventNotification')),
),Method("RRasAdminSendUserMessage",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hDimConnection')),
In((LPWSTR,'lpwszMessage')),
),Method("RRouterDeviceEnum",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
InOut((LPDWORD,'lpdwTotalEntries')),
),Method("RRouterInterfaceTransportCreate",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwTransportId')),
In((LPWSTR,'lpwsTransportName')),
In((PDIM_INTERFACE_CONTAINER,'pInfoStruct')),
In((LPWSTR,'lpwsDLLPath')),
),Method("RRouterInterfaceDeviceGetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'dwIndex')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceDeviceSetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'dwIndex')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceSetCredentialsEx",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'hInterface')),
),Method("RRouterInterfaceGetCredentialsEx",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
InOut((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
In((DWORD,'hInterface')),
),Method("RRasAdminConnectionRemoveQuarantine",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hRasConnection')),
In((BOOL,'fIsIpAddress')),
),Method("RMprAdminServerSetInfo",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'dwLevel')),
In((PDIM_INFORMATION_CONTAINER,'pInfoStruct')),
),Method("RMprAdminServerGetInfoEx",
In((DIM_HANDLE,'hDimServer')),
InOut((PMPR_SERVER_EX_IDL,'pServerConfig')),
),Method("RRasAdminConnectionEnumEx",
In((DIM_HANDLE,'hDimServer')),
In((PMPRAPI_OBJECT_HEADER_IDL,'objectHeader')),
In((DWORD,'dwPreferedMaxLen')),
Out((LPDWORD,'lpdwEntriesRead')),
Out((LPDWORD,'lpdNumTotalElements')),
Out((PPRAS_CONNECTION_EX_IDL,'pRasConections')),
InOut((LPDWORD,'lpdwResumeHandle')),
),Method("RRasAdminConnectionGetInfoEx",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hDimConnection')),
In((PMPRAPI_OBJECT_HEADER_IDL,'objectHeader')),
Out((PRAS_CONNECTION_EX_IDL,'pRasConnection')),
),Method("RMprAdminServerSetInfoEx",
In((DIM_HANDLE,'hDimServer')),
In((PMPR_SERVER_SET_CONFIG_EX_IDL,'pServerConfig')),
),Method("RRasAdminUpdateConnection",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hDimConnection')),
In((PRAS_UPDATE_CONNECTION_IDL,'pServerConfig')),
),Method("RRouterInterfaceSetCredentialsLocal",
In((DIM_HANDLE,'hDimServer')),
In((LPWSTR,'lpwsInterfaceName')),
In((LPWSTR,'lpwsUserName')),
In((LPWSTR,'lpwsDomainName')),
In((LPWSTR,'lpwsPassword')),
),Method("RRouterInterfaceGetCredentialsLocal",
In((DIM_HANDLE,'hDimServer')),
In((LPWSTR,'lpwsInterfaceName')),
Out((PLPWSTR,'lpwsUserName')),
Out((PLPWSTR,'lpwsDomainName')),
Out((PLPWSTR,'lpwsPassword')),
),Method("RRouterInterfaceGetCustomInfoEx",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
InOut((PMPR_IF_CUSTOMINFOEX_IDL,'pIfCustomConfig')),
),Method("RRouterInterfaceSetCustomInfoEx",
In((DIM_HANDLE,'hDimServer')),
In((DWORD,'hInterface')),
InOut((PMPR_IF_CUSTOMINFOEX_IDL,'pIfCustomConfig')),
),])