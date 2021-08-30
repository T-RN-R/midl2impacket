
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
PWCHAR = NdrByte
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

    

class SPECIALPROPERTIESDATA(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved1"),(UNSIGNED___INT64, "Reserved2"),(DWORD, "Reserved3"),]

    

class SPECIALPROPERTIESDATA_ALTERNATE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved3"),]

    
Method("RemoteActivation",
In(HANDLE_T),
In(PORPCTHIS),
Out(PORPCTHAT),
In(PGUID),
In(PWCHAR_T),
In(PMINTERFACEPOINTER),
In(DWORD),
In(DWORD),
In(DWORD),
In(PIID),
In(UNSIGNED_SHORT),
In(UNSIGNED_SHORT),
Out(POXID),
Out(PPDUALSTRINGARRAY),
Out(PIPID),
Out(PDWORD),
Out(PCOMVERSION),
Out(PHRESULT),
Out(PPMINTERFACEPOINTER),
Out(PHRESULT),
),VDS_OBJECT_ID = GUID

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

    

class VDS_REPARSE_POINT_PROP(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "SourceVolumeId"),(PWCHAR, "pwszPath"),]

    
PVDS_REPARSE_POINT_PROP = VDS_REPARSE_POINT_PROP

class VDS_DRIVE_LETTER_PROP(NdrStructure):
    MEMBERS = [(WCHAR, "wcLetter"),(VDS_OBJECT_ID, "volumeId"),(UNSIGNED_LONG, "ulFlags"),(LONG, "bUsed"),]

    
PVDS_DRIVE_LETTER_PROP = VDS_DRIVE_LETTER_PROP

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

class VDS_CREATE_VDISK_PARAMETERS(NdrStructure):
    MEMBERS = [(GUID, "UniqueId"),(ULONGLONG, "MaximumSize"),(ULONG, "BlockSizeInBytes"),(ULONG, "SectorSizeInBytes"),(LPWSTR, "pParentPath"),(LPWSTR, "pSourcePath"),]

    
PVDS_CREATE_VDISK_PARAMETERS = VDS_CREATE_VDISK_PARAMETERS

class VDS_VDISK_PROPERTIES(NdrStructure):
    MEMBERS = [(VDS_OBJECT_ID, "Id"),(VDS_VDISK_STATE, "State"),(VIRTUAL_STORAGE_TYPE, "VirtualDeviceType"),(ULONGLONG, "VirtualSize"),(ULONGLONG, "PhysicalSize"),(LPWSTR, "pPath"),(LPWSTR, "pDeviceName"),(DEPENDENT_DISK_FLAG, "DiskFlag"),(BOOL, "bIsChild"),(LPWSTR, "pParentPath"),]

    
PVDS_VDISK_PROPERTIES = VDS_VDISK_PROPERTIES

class PPVIRTUAL_STORAGE_TYPE(NdrStructure):
    MEMBERS = []

    
Method("Next",
In(UNSIGNED_LONG),
Out(PPIUNKNOWN),
Out(PUNSIGNED_LONG),
),Method("Skip",
In(UNSIGNED_LONG),
),Method("Reset",
),Method("Clone",
Out(PPIENUMVDSOBJECT),
),