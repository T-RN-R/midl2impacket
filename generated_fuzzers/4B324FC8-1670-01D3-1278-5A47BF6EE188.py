
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
SRVSVC_HANDLE = WCHAR_T

class CONNECTION_INFO_0(NdrStructure):
    MEMBERS = [(DWORD, "coni0_id"),]

    
PCONNECTION_INFO_0 = CONNECTION_INFO_0
LPCONNECTION_INFO_0 = CONNECTION_INFO_0

class CONNECT_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPCONNECTION_INFO_0, "Buffer"),]

    
PCONNECT_INFO_0_CONTAINER = CONNECT_INFO_0_CONTAINER
LPCONNECT_INFO_0_CONTAINER = CONNECT_INFO_0_CONTAINER

class CONNECTION_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "coni1_id"),(DWORD, "coni1_type"),(DWORD, "coni1_num_opens"),(DWORD, "coni1_num_users"),(DWORD, "coni1_time"),(PWCHAR_T, "coni1_username"),(PWCHAR_T, "coni1_netname"),]

    
PCONNECTION_INFO_1 = CONNECTION_INFO_1
LPCONNECTION_INFO_1 = CONNECTION_INFO_1

class CONNECT_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPCONNECTION_INFO_1, "Buffer"),]

    
PCONNECT_INFO_1_CONTAINER = CONNECT_INFO_1_CONTAINER
LPCONNECT_INFO_1_CONTAINER = CONNECT_INFO_1_CONTAINER

class CONNECT_ENUM_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PCONNECT_INFO_0_CONTAINER, "Level0"),2 : (PCONNECT_INFO_1_CONTAINER, "Level1"),}

    

class CONNECT_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(CONNECT_ENUM_UNION, "ConnectInfo"),]

    
PCONNECT_ENUM_STRUCT = CONNECT_ENUM_STRUCT
LPCONNECT_ENUM_STRUCT = CONNECT_ENUM_STRUCT

class FILE_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "fi2_id"),]

    
PFILE_INFO_2 = FILE_INFO_2
LPFILE_INFO_2 = FILE_INFO_2

class FILE_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPFILE_INFO_2, "Buffer"),]

    
PFILE_INFO_2_CONTAINER = FILE_INFO_2_CONTAINER
LPFILE_INFO_2_CONTAINER = FILE_INFO_2_CONTAINER

class FILE_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "fi3_id"),(DWORD, "fi3_permissions"),(DWORD, "fi3_num_locks"),(PWCHAR_T, "fi3_pathname"),(PWCHAR_T, "fi3_username"),]

    
PFILE_INFO_3 = FILE_INFO_3
LPFILE_INFO_3 = FILE_INFO_3

class FILE_INFO_3_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPFILE_INFO_3, "Buffer"),]

    
PFILE_INFO_3_CONTAINER = FILE_INFO_3_CONTAINER
LPFILE_INFO_3_CONTAINER = FILE_INFO_3_CONTAINER

class FILE_ENUM_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PFILE_INFO_2_CONTAINER, "Level2"),2 : (PFILE_INFO_3_CONTAINER, "Level3"),}

    

class FILE_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(FILE_ENUM_UNION, "FileInfo"),]

    
PFILE_ENUM_STRUCT = FILE_ENUM_STRUCT
LPFILE_ENUM_STRUCT = FILE_ENUM_STRUCT

class FILE_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPFILE_INFO_2, "FileInfo2"),2 : (LPFILE_INFO_3, "FileInfo3"),}

    
PFILE_INFO = FILE_INFO
LPFILE_INFO = FILE_INFO

class SESSION_INFO_0(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sesi0_cname"),]

    
PSESSION_INFO_0 = SESSION_INFO_0
LPSESSION_INFO_0 = SESSION_INFO_0

class SESSION_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSESSION_INFO_0, "Buffer"),]

    
PSESSION_INFO_0_CONTAINER = SESSION_INFO_0_CONTAINER
LPSESSION_INFO_0_CONTAINER = SESSION_INFO_0_CONTAINER

class SESSION_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sesi1_cname"),(PWCHAR_T, "sesi1_username"),(DWORD, "sesi1_num_opens"),(DWORD, "sesi1_time"),(DWORD, "sesi1_idle_time"),(DWORD, "sesi1_user_flags"),]

    
PSESSION_INFO_1 = SESSION_INFO_1
LPSESSION_INFO_1 = SESSION_INFO_1

class SESSION_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSESSION_INFO_1, "Buffer"),]

    
PSESSION_INFO_1_CONTAINER = SESSION_INFO_1_CONTAINER
LPSESSION_INFO_1_CONTAINER = SESSION_INFO_1_CONTAINER

class SESSION_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sesi2_cname"),(PWCHAR_T, "sesi2_username"),(DWORD, "sesi2_num_opens"),(DWORD, "sesi2_time"),(DWORD, "sesi2_idle_time"),(DWORD, "sesi2_user_flags"),(PWCHAR_T, "sesi2_cltype_name"),]

    
PSESSION_INFO_2 = SESSION_INFO_2
LPSESSION_INFO_2 = SESSION_INFO_2

class SESSION_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSESSION_INFO_2, "Buffer"),]

    
PSESSION_INFO_2_CONTAINER = SESSION_INFO_2_CONTAINER
LPSESSION_INFO_2_CONTAINER = SESSION_INFO_2_CONTAINER

class SESSION_INFO_10(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sesi10_cname"),(PWCHAR_T, "sesi10_username"),(DWORD, "sesi10_time"),(DWORD, "sesi10_idle_time"),]

    
PSESSION_INFO_10 = SESSION_INFO_10
LPSESSION_INFO_10 = SESSION_INFO_10

class SESSION_INFO_10_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSESSION_INFO_10, "Buffer"),]

    
PSESSION_INFO_10_CONTAINER = SESSION_INFO_10_CONTAINER
LPSESSION_INFO_10_CONTAINER = SESSION_INFO_10_CONTAINER

class SESSION_INFO_502(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sesi502_cname"),(PWCHAR_T, "sesi502_username"),(DWORD, "sesi502_num_opens"),(DWORD, "sesi502_time"),(DWORD, "sesi502_idle_time"),(DWORD, "sesi502_user_flags"),(PWCHAR_T, "sesi502_cltype_name"),(PWCHAR_T, "sesi502_transport"),]

    
PSESSION_INFO_502 = SESSION_INFO_502
LPSESSION_INFO_502 = SESSION_INFO_502

class SESSION_INFO_502_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSESSION_INFO_502, "Buffer"),]

    
PSESSION_INFO_502_CONTAINER = SESSION_INFO_502_CONTAINER
LPSESSION_INFO_502_CONTAINER = SESSION_INFO_502_CONTAINER

class SESSION_ENUM_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSESSION_INFO_0_CONTAINER, "Level0"),2 : (PSESSION_INFO_1_CONTAINER, "Level1"),3 : (PSESSION_INFO_2_CONTAINER, "Level2"),4 : (PSESSION_INFO_10_CONTAINER, "Level10"),5 : (PSESSION_INFO_502_CONTAINER, "Level502"),}

    

class SESSION_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(SESSION_ENUM_UNION, "SessionInfo"),]

    
PSESSION_ENUM_STRUCT = SESSION_ENUM_STRUCT
LPSESSION_ENUM_STRUCT = SESSION_ENUM_STRUCT

class SHARE_INFO_502_I(NdrStructure):
    MEMBERS = [(PWCHAR, "shi502_netname"),(DWORD, "shi502_type"),(PWCHAR, "shi502_remark"),(DWORD, "shi502_permissions"),(DWORD, "shi502_max_uses"),(DWORD, "shi502_current_uses"),(PWCHAR, "shi502_path"),(PWCHAR, "shi502_passwd"),(DWORD, "shi502_reserved"),(PUNSIGNED_CHAR, "shi502_security_descriptor"),]

    
PSHARE_INFO_502_I = SHARE_INFO_502_I
LPSHARE_INFO_502_I = SHARE_INFO_502_I

class SHARE_INFO_503_I(NdrStructure):
    MEMBERS = [(PWCHAR, "shi503_netname"),(DWORD, "shi503_type"),(PWCHAR, "shi503_remark"),(DWORD, "shi503_permissions"),(DWORD, "shi503_max_uses"),(DWORD, "shi503_current_uses"),(PWCHAR, "shi503_path"),(PWCHAR, "shi503_passwd"),(PWCHAR, "shi503_servername"),(DWORD, "shi503_reserved"),(PUCHAR, "shi503_security_descriptor"),]

    
PSHARE_INFO_503_I = SHARE_INFO_503_I
LPSHARE_INFO_503_I = SHARE_INFO_503_I

class SHARE_INFO_503_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_503_I, "Buffer"),]

    
PSHARE_INFO_503_CONTAINER = SHARE_INFO_503_CONTAINER
LPSHARE_INFO_503_CONTAINER = SHARE_INFO_503_CONTAINER

class SHARE_INFO_1501_I(NdrStructure):
    MEMBERS = [(DWORD, "shi1501_reserved"),(PUNSIGNED_CHAR, "shi1501_security_descriptor"),]

    
PSHARE_INFO_1501_I = SHARE_INFO_1501_I
LPSHARE_INFO_1501_I = SHARE_INFO_1501_I

class SHARE_INFO_0(NdrStructure):
    MEMBERS = [(PWCHAR_T, "shi0_netname"),]

    
PSHARE_INFO_0 = SHARE_INFO_0
LPSHARE_INFO_0 = SHARE_INFO_0

class SHARE_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_0, "Buffer"),]

    

class SHARE_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "shi1_netname"),(DWORD, "shi1_type"),(PWCHAR_T, "shi1_remark"),]

    
PSHARE_INFO_1 = SHARE_INFO_1
LPSHARE_INFO_1 = SHARE_INFO_1

class SHARE_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_1, "Buffer"),]

    

class SHARE_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR_T, "shi2_netname"),(DWORD, "shi2_type"),(PWCHAR_T, "shi2_remark"),(DWORD, "shi2_permissions"),(DWORD, "shi2_max_uses"),(DWORD, "shi2_current_uses"),(PWCHAR_T, "shi2_path"),(PWCHAR_T, "shi2_passwd"),]

    
PSHARE_INFO_2 = SHARE_INFO_2
LPSHARE_INFO_2 = SHARE_INFO_2

class SHARE_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_2, "Buffer"),]

    
PSHARE_INFO_2_CONTAINER = SHARE_INFO_2_CONTAINER
LPSHARE_INFO_2_CONTAINER = SHARE_INFO_2_CONTAINER

class SHARE_INFO_501(NdrStructure):
    MEMBERS = [(PWCHAR_T, "shi501_netname"),(DWORD, "shi501_type"),(PWCHAR_T, "shi501_remark"),(DWORD, "shi501_flags"),]

    
PSHARE_INFO_501 = SHARE_INFO_501
LPSHARE_INFO_501 = SHARE_INFO_501

class SHARE_INFO_501_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_501, "Buffer"),]

    
PSHARE_INFO_501_CONTAINER = SHARE_INFO_501_CONTAINER
LPSHARE_INFO_501_CONTAINER = SHARE_INFO_501_CONTAINER

class SHARE_INFO_502_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSHARE_INFO_502_I, "Buffer"),]

    
PSHARE_INFO_502_CONTAINER = SHARE_INFO_502_CONTAINER
LPSHARE_INFO_502_CONTAINER = SHARE_INFO_502_CONTAINER

class SHARE_ENUM_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSHARE_INFO_0_CONTAINER, "Level0"),2 : (PSHARE_INFO_1_CONTAINER, "Level1"),3 : (PSHARE_INFO_2_CONTAINER, "Level2"),4 : (PSHARE_INFO_501_CONTAINER, "Level501"),5 : (PSHARE_INFO_502_CONTAINER, "Level502"),6 : (PSHARE_INFO_503_CONTAINER, "Level503"),}

    

class SHARE_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(SHARE_ENUM_UNION, "ShareInfo"),]

    
PSHARE_ENUM_STRUCT = SHARE_ENUM_STRUCT
LPSHARE_ENUM_STRUCT = SHARE_ENUM_STRUCT

class SHARE_INFO_1004(NdrStructure):
    MEMBERS = [(PWCHAR_T, "shi1004_remark"),]

    
PSHARE_INFO_1004 = SHARE_INFO_1004
LPSHARE_INFO_1004 = SHARE_INFO_1004

class SHARE_INFO_1006(NdrStructure):
    MEMBERS = [(DWORD, "shi1006_max_uses"),]

    
PSHARE_INFO_1006 = SHARE_INFO_1006
LPSHARE_INFO_1006 = SHARE_INFO_1006

class SHARE_INFO_1005(NdrStructure):
    MEMBERS = [(DWORD, "shi1005_flags"),]

    
PSHARE_INFO_1005 = SHARE_INFO_1005
LPSHARE_INFO_1005 = SHARE_INFO_1005

class SHARE_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPSHARE_INFO_0, "ShareInfo0"),2 : (LPSHARE_INFO_1, "ShareInfo1"),3 : (LPSHARE_INFO_2, "ShareInfo2"),4 : (LPSHARE_INFO_502_I, "ShareInfo502"),5 : (LPSHARE_INFO_1004, "ShareInfo1004"),6 : (LPSHARE_INFO_1006, "ShareInfo1006"),7 : (LPSHARE_INFO_1501_I, "ShareInfo1501"),9 : (LPSHARE_INFO_1005, "ShareInfo1005"),10 : (LPSHARE_INFO_501, "ShareInfo501"),11 : (LPSHARE_INFO_503_I, "ShareInfo503"),}

    
PSHARE_INFO = SHARE_INFO
LPSHARE_INFO = SHARE_INFO

class SERVER_INFO_102(NdrStructure):
    MEMBERS = [(DWORD, "sv102_platform_id"),(PWCHAR_T, "sv102_name"),(DWORD, "sv102_version_major"),(DWORD, "sv102_version_minor"),(DWORD, "sv102_type"),(PWCHAR_T, "sv102_comment"),(DWORD, "sv102_users"),(LONG, "sv102_disc"),(INT, "sv102_hidden"),(DWORD, "sv102_announce"),(DWORD, "sv102_anndelta"),(DWORD, "sv102_licenses"),(PWCHAR_T, "sv102_userpath"),]

    
PSERVER_INFO_102 = SERVER_INFO_102
LPSERVER_INFO_102 = SERVER_INFO_102

class SERVER_INFO_103(NdrStructure):
    MEMBERS = [(DWORD, "sv103_platform_id"),(PWCHAR_T, "sv103_name"),(DWORD, "sv103_version_major"),(DWORD, "sv103_version_minor"),(DWORD, "sv103_type"),(PWCHAR_T, "sv103_comment"),(DWORD, "sv103_users"),(LONG, "sv103_disc"),(BOOL, "sv103_hidden"),(DWORD, "sv103_announce"),(DWORD, "sv103_anndelta"),(DWORD, "sv103_licenses"),(PWCHAR_T, "sv103_userpath"),(DWORD, "sv103_capabilities"),]

    
PSERVER_INFO_103 = SERVER_INFO_103
LPSERVER_INFO_103 = SERVER_INFO_103

class SERVER_INFO_502(NdrStructure):
    MEMBERS = [(DWORD, "sv502_sessopens"),(DWORD, "sv502_sessvcs"),(DWORD, "sv502_opensearch"),(DWORD, "sv502_sizreqbuf"),(DWORD, "sv502_initworkitems"),(DWORD, "sv502_maxworkitems"),(DWORD, "sv502_rawworkitems"),(DWORD, "sv502_irpstacksize"),(DWORD, "sv502_maxrawbuflen"),(DWORD, "sv502_sessusers"),(DWORD, "sv502_sessconns"),(DWORD, "sv502_maxpagedmemoryusage"),(DWORD, "sv502_maxnonpagedmemoryusage"),(INT, "sv502_enablesoftcompat"),(INT, "sv502_enableforcedlogoff"),(INT, "sv502_timesource"),(INT, "sv502_acceptdownlevelapis"),(INT, "sv502_lmannounce"),]

    
PSERVER_INFO_502 = SERVER_INFO_502
LPSERVER_INFO_502 = SERVER_INFO_502

class SERVER_INFO_503(NdrStructure):
    MEMBERS = [(DWORD, "sv503_sessopens"),(DWORD, "sv503_sessvcs"),(DWORD, "sv503_opensearch"),(DWORD, "sv503_sizreqbuf"),(DWORD, "sv503_initworkitems"),(DWORD, "sv503_maxworkitems"),(DWORD, "sv503_rawworkitems"),(DWORD, "sv503_irpstacksize"),(DWORD, "sv503_maxrawbuflen"),(DWORD, "sv503_sessusers"),(DWORD, "sv503_sessconns"),(DWORD, "sv503_maxpagedmemoryusage"),(DWORD, "sv503_maxnonpagedmemoryusage"),(INT, "sv503_enablesoftcompat"),(INT, "sv503_enableforcedlogoff"),(INT, "sv503_timesource"),(INT, "sv503_acceptdownlevelapis"),(INT, "sv503_lmannounce"),(PWCHAR_T, "sv503_domain"),(DWORD, "sv503_maxcopyreadlen"),(DWORD, "sv503_maxcopywritelen"),(DWORD, "sv503_minkeepsearch"),(DWORD, "sv503_maxkeepsearch"),(DWORD, "sv503_minkeepcomplsearch"),(DWORD, "sv503_maxkeepcomplsearch"),(DWORD, "sv503_threadcountadd"),(DWORD, "sv503_numblockthreads"),(DWORD, "sv503_scavtimeout"),(DWORD, "sv503_minrcvqueue"),(DWORD, "sv503_minfreeworkitems"),(DWORD, "sv503_xactmemsize"),(DWORD, "sv503_threadpriority"),(DWORD, "sv503_maxmpxct"),(DWORD, "sv503_oplockbreakwait"),(DWORD, "sv503_oplockbreakresponsewait"),(INT, "sv503_enableoplocks"),(INT, "sv503_enableoplockforceclose"),(INT, "sv503_enablefcbopens"),(INT, "sv503_enableraw"),(INT, "sv503_enablesharednetdrives"),(DWORD, "sv503_minfreeconnections"),(DWORD, "sv503_maxfreeconnections"),]

    
PSERVER_INFO_503 = SERVER_INFO_503
LPSERVER_INFO_503 = SERVER_INFO_503

class SERVER_INFO_599(NdrStructure):
    MEMBERS = [(DWORD, "sv599_sessopens"),(DWORD, "sv599_sessvcs"),(DWORD, "sv599_opensearch"),(DWORD, "sv599_sizreqbuf"),(DWORD, "sv599_initworkitems"),(DWORD, "sv599_maxworkitems"),(DWORD, "sv599_rawworkitems"),(DWORD, "sv599_irpstacksize"),(DWORD, "sv599_maxrawbuflen"),(DWORD, "sv599_sessusers"),(DWORD, "sv599_sessconns"),(DWORD, "sv599_maxpagedmemoryusage"),(DWORD, "sv599_maxnonpagedmemoryusage"),(INT, "sv599_enablesoftcompat"),(INT, "sv599_enableforcedlogoff"),(INT, "sv599_timesource"),(INT, "sv599_acceptdownlevelapis"),(INT, "sv599_lmannounce"),(PWCHAR_T, "sv599_domain"),(DWORD, "sv599_maxcopyreadlen"),(DWORD, "sv599_maxcopywritelen"),(DWORD, "sv599_minkeepsearch"),(DWORD, "sv599_maxkeepsearch"),(DWORD, "sv599_minkeepcomplsearch"),(DWORD, "sv599_maxkeepcomplsearch"),(DWORD, "sv599_threadcountadd"),(DWORD, "sv599_numblockthreads"),(DWORD, "sv599_scavtimeout"),(DWORD, "sv599_minrcvqueue"),(DWORD, "sv599_minfreeworkitems"),(DWORD, "sv599_xactmemsize"),(DWORD, "sv599_threadpriority"),(DWORD, "sv599_maxmpxct"),(DWORD, "sv599_oplockbreakwait"),(DWORD, "sv599_oplockbreakresponsewait"),(INT, "sv599_enableoplocks"),(INT, "sv599_enableoplockforceclose"),(INT, "sv599_enablefcbopens"),(INT, "sv599_enableraw"),(INT, "sv599_enablesharednetdrives"),(DWORD, "sv599_minfreeconnections"),(DWORD, "sv599_maxfreeconnections"),(DWORD, "sv599_initsesstable"),(DWORD, "sv599_initconntable"),(DWORD, "sv599_initfiletable"),(DWORD, "sv599_initsearchtable"),(DWORD, "sv599_alertschedule"),(DWORD, "sv599_errorthreshold"),(DWORD, "sv599_networkerrorthreshold"),(DWORD, "sv599_diskspacethreshold"),(DWORD, "sv599_reserved"),(DWORD, "sv599_maxlinkdelay"),(DWORD, "sv599_minlinkthroughput"),(DWORD, "sv599_linkinfovalidtime"),(DWORD, "sv599_scavqosinfoupdatetime"),(DWORD, "sv599_maxworkitemidletime"),]

    
PSERVER_INFO_599 = SERVER_INFO_599
LPSERVER_INFO_599 = SERVER_INFO_599

class SERVER_INFO_1005(NdrStructure):
    MEMBERS = [(PWCHAR_T, "sv1005_comment"),]

    
PSERVER_INFO_1005 = SERVER_INFO_1005
LPSERVER_INFO_1005 = SERVER_INFO_1005

class SERVER_INFO_1107(NdrStructure):
    MEMBERS = [(DWORD, "sv1107_users"),]

    
PSERVER_INFO_1107 = SERVER_INFO_1107
LPSERVER_INFO_1107 = SERVER_INFO_1107

class SERVER_INFO_1010(NdrStructure):
    MEMBERS = [(LONG, "sv1010_disc"),]

    
PSERVER_INFO_1010 = SERVER_INFO_1010
LPSERVER_INFO_1010 = SERVER_INFO_1010

class SERVER_INFO_1016(NdrStructure):
    MEMBERS = [(INT, "sv1016_hidden"),]

    
PSERVER_INFO_1016 = SERVER_INFO_1016
LPSERVER_INFO_1016 = SERVER_INFO_1016

class SERVER_INFO_1017(NdrStructure):
    MEMBERS = [(DWORD, "sv1017_announce"),]

    
PSERVER_INFO_1017 = SERVER_INFO_1017
LPSERVER_INFO_1017 = SERVER_INFO_1017

class SERVER_INFO_1018(NdrStructure):
    MEMBERS = [(DWORD, "sv1018_anndelta"),]

    
PSERVER_INFO_1018 = SERVER_INFO_1018
LPSERVER_INFO_1018 = SERVER_INFO_1018

class SERVER_INFO_1501(NdrStructure):
    MEMBERS = [(DWORD, "sv1501_sessopens"),]

    
PSERVER_INFO_1501 = SERVER_INFO_1501
LPSERVER_INFO_1501 = SERVER_INFO_1501

class SERVER_INFO_1502(NdrStructure):
    MEMBERS = [(DWORD, "sv1502_sessvcs"),]

    
PSERVER_INFO_1502 = SERVER_INFO_1502
LPSERVER_INFO_1502 = SERVER_INFO_1502

class SERVER_INFO_1503(NdrStructure):
    MEMBERS = [(DWORD, "sv1503_opensearch"),]

    
PSERVER_INFO_1503 = SERVER_INFO_1503
LPSERVER_INFO_1503 = SERVER_INFO_1503

class SERVER_INFO_1506(NdrStructure):
    MEMBERS = [(DWORD, "sv1506_maxworkitems"),]

    
PSERVER_INFO_1506 = SERVER_INFO_1506
LPSERVER_INFO_1506 = SERVER_INFO_1506

class SERVER_INFO_1510(NdrStructure):
    MEMBERS = [(DWORD, "sv1510_sessusers"),]

    
PSERVER_INFO_1510 = SERVER_INFO_1510
LPSERVER_INFO_1510 = SERVER_INFO_1510

class SERVER_INFO_1511(NdrStructure):
    MEMBERS = [(DWORD, "sv1511_sessconns"),]

    
PSERVER_INFO_1511 = SERVER_INFO_1511
LPSERVER_INFO_1511 = SERVER_INFO_1511

class SERVER_INFO_1512(NdrStructure):
    MEMBERS = [(DWORD, "sv1512_maxnonpagedmemoryusage"),]

    
PSERVER_INFO_1512 = SERVER_INFO_1512
LPSERVER_INFO_1512 = SERVER_INFO_1512

class SERVER_INFO_1513(NdrStructure):
    MEMBERS = [(DWORD, "sv1513_maxpagedmemoryusage"),]

    
PSERVER_INFO_1513 = SERVER_INFO_1513
LPSERVER_INFO_1513 = SERVER_INFO_1513

class SERVER_INFO_1514(NdrStructure):
    MEMBERS = [(INT, "sv1514_enablesoftcompat"),]

    
PSERVER_INFO_1514 = SERVER_INFO_1514
LPSERVER_INFO_1514 = SERVER_INFO_1514

class SERVER_INFO_1515(NdrStructure):
    MEMBERS = [(INT, "sv1515_enableforcedlogoff"),]

    
PSERVER_INFO_1515 = SERVER_INFO_1515
LPSERVER_INFO_1515 = SERVER_INFO_1515

class SERVER_INFO_1516(NdrStructure):
    MEMBERS = [(INT, "sv1516_timesource"),]

    
PSERVER_INFO_1516 = SERVER_INFO_1516
LPSERVER_INFO_1516 = SERVER_INFO_1516

class SERVER_INFO_1518(NdrStructure):
    MEMBERS = [(INT, "sv1518_lmannounce"),]

    
PSERVER_INFO_1518 = SERVER_INFO_1518
LPSERVER_INFO_1518 = SERVER_INFO_1518

class SERVER_INFO_1523(NdrStructure):
    MEMBERS = [(DWORD, "sv1523_maxkeepsearch"),]

    
PSERVER_INFO_1523 = SERVER_INFO_1523
LPSERVER_INFO_1523 = SERVER_INFO_1523

class SERVER_INFO_1528(NdrStructure):
    MEMBERS = [(DWORD, "sv1528_scavtimeout"),]

    
PSERVER_INFO_1528 = SERVER_INFO_1528
LPSERVER_INFO_1528 = SERVER_INFO_1528

class SERVER_INFO_1529(NdrStructure):
    MEMBERS = [(DWORD, "sv1529_minrcvqueue"),]

    
PSERVER_INFO_1529 = SERVER_INFO_1529
LPSERVER_INFO_1529 = SERVER_INFO_1529

class SERVER_INFO_1530(NdrStructure):
    MEMBERS = [(DWORD, "sv1530_minfreeworkitems"),]

    
PSERVER_INFO_1530 = SERVER_INFO_1530
LPSERVER_INFO_1530 = SERVER_INFO_1530

class SERVER_INFO_1533(NdrStructure):
    MEMBERS = [(DWORD, "sv1533_maxmpxct"),]

    
PSERVER_INFO_1533 = SERVER_INFO_1533
LPSERVER_INFO_1533 = SERVER_INFO_1533

class SERVER_INFO_1534(NdrStructure):
    MEMBERS = [(DWORD, "sv1534_oplockbreakwait"),]

    
PSERVER_INFO_1534 = SERVER_INFO_1534
LPSERVER_INFO_1534 = SERVER_INFO_1534

class SERVER_INFO_1535(NdrStructure):
    MEMBERS = [(DWORD, "sv1535_oplockbreakresponsewait"),]

    
PSERVER_INFO_1535 = SERVER_INFO_1535
LPSERVER_INFO_1535 = SERVER_INFO_1535

class SERVER_INFO_1536(NdrStructure):
    MEMBERS = [(INT, "sv1536_enableoplocks"),]

    
PSERVER_INFO_1536 = SERVER_INFO_1536
LPSERVER_INFO_1536 = SERVER_INFO_1536

class SERVER_INFO_1538(NdrStructure):
    MEMBERS = [(INT, "sv1538_enablefcbopens"),]

    
PSERVER_INFO_1538 = SERVER_INFO_1538
LPSERVER_INFO_1538 = SERVER_INFO_1538

class SERVER_INFO_1539(NdrStructure):
    MEMBERS = [(INT, "sv1539_enableraw"),]

    
PSERVER_INFO_1539 = SERVER_INFO_1539
LPSERVER_INFO_1539 = SERVER_INFO_1539

class SERVER_INFO_1540(NdrStructure):
    MEMBERS = [(INT, "sv1540_enablesharednetdrives"),]

    
PSERVER_INFO_1540 = SERVER_INFO_1540
LPSERVER_INFO_1540 = SERVER_INFO_1540

class SERVER_INFO_1541(NdrStructure):
    MEMBERS = [(INT, "sv1541_minfreeconnections"),]

    
PSERVER_INFO_1541 = SERVER_INFO_1541
LPSERVER_INFO_1541 = SERVER_INFO_1541

class SERVER_INFO_1542(NdrStructure):
    MEMBERS = [(INT, "sv1542_maxfreeconnections"),]

    
PSERVER_INFO_1542 = SERVER_INFO_1542
LPSERVER_INFO_1542 = SERVER_INFO_1542

class SERVER_INFO_1543(NdrStructure):
    MEMBERS = [(DWORD, "sv1543_initsesstable"),]

    
PSERVER_INFO_1543 = SERVER_INFO_1543
LPSERVER_INFO_1543 = SERVER_INFO_1543

class SERVER_INFO_1544(NdrStructure):
    MEMBERS = [(DWORD, "sv1544_initconntable"),]

    
PSERVER_INFO_1544 = SERVER_INFO_1544
LPSERVER_INFO_1544 = SERVER_INFO_1544

class SERVER_INFO_1545(NdrStructure):
    MEMBERS = [(DWORD, "sv1545_initfiletable"),]

    
PSERVER_INFO_1545 = SERVER_INFO_1545
LPSERVER_INFO_1545 = SERVER_INFO_1545

class SERVER_INFO_1546(NdrStructure):
    MEMBERS = [(DWORD, "sv1546_initsearchtable"),]

    
PSERVER_INFO_1546 = SERVER_INFO_1546
LPSERVER_INFO_1546 = SERVER_INFO_1546

class SERVER_INFO_1547(NdrStructure):
    MEMBERS = [(DWORD, "sv1547_alertschedule"),]

    
PSERVER_INFO_1547 = SERVER_INFO_1547
LPSERVER_INFO_1547 = SERVER_INFO_1547

class SERVER_INFO_1548(NdrStructure):
    MEMBERS = [(DWORD, "sv1548_errorthreshold"),]

    
PSERVER_INFO_1548 = SERVER_INFO_1548
LPSERVER_INFO_1548 = SERVER_INFO_1548

class SERVER_INFO_1549(NdrStructure):
    MEMBERS = [(DWORD, "sv1549_networkerrorthreshold"),]

    
PSERVER_INFO_1549 = SERVER_INFO_1549
LPSERVER_INFO_1549 = SERVER_INFO_1549

class SERVER_INFO_1550(NdrStructure):
    MEMBERS = [(DWORD, "sv1550_diskspacethreshold"),]

    
PSERVER_INFO_1550 = SERVER_INFO_1550
LPSERVER_INFO_1550 = SERVER_INFO_1550

class SERVER_INFO_1552(NdrStructure):
    MEMBERS = [(DWORD, "sv1552_maxlinkdelay"),]

    
PSERVER_INFO_1552 = SERVER_INFO_1552
LPSERVER_INFO_1552 = SERVER_INFO_1552

class SERVER_INFO_1553(NdrStructure):
    MEMBERS = [(DWORD, "sv1553_minlinkthroughput"),]

    
PSERVER_INFO_1553 = SERVER_INFO_1553
LPSERVER_INFO_1553 = SERVER_INFO_1553

class SERVER_INFO_1554(NdrStructure):
    MEMBERS = [(DWORD, "sv1554_linkinfovalidtime"),]

    
PSERVER_INFO_1554 = SERVER_INFO_1554
LPSERVER_INFO_1554 = SERVER_INFO_1554

class SERVER_INFO_1555(NdrStructure):
    MEMBERS = [(DWORD, "sv1555_scavqosinfoupdatetime"),]

    
PSERVER_INFO_1555 = SERVER_INFO_1555
LPSERVER_INFO_1555 = SERVER_INFO_1555

class SERVER_INFO_1556(NdrStructure):
    MEMBERS = [(DWORD, "sv1556_maxworkitemidletime"),]

    
PSERVER_INFO_1556 = SERVER_INFO_1556
LPSERVER_INFO_1556 = SERVER_INFO_1556

class SERVER_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPSERVER_INFO_100, "ServerInfo100"),2 : (LPSERVER_INFO_101, "ServerInfo101"),3 : (LPSERVER_INFO_102, "ServerInfo102"),4 : (LPSERVER_INFO_103, "ServerInfo103"),5 : (LPSERVER_INFO_502, "ServerInfo502"),6 : (LPSERVER_INFO_503, "ServerInfo503"),7 : (LPSERVER_INFO_599, "ServerInfo599"),8 : (LPSERVER_INFO_1005, "ServerInfo1005"),9 : (LPSERVER_INFO_1107, "ServerInfo1107"),10 : (LPSERVER_INFO_1010, "ServerInfo1010"),11 : (LPSERVER_INFO_1016, "ServerInfo1016"),12 : (LPSERVER_INFO_1017, "ServerInfo1017"),13 : (LPSERVER_INFO_1018, "ServerInfo1018"),14 : (LPSERVER_INFO_1501, "ServerInfo1501"),15 : (LPSERVER_INFO_1502, "ServerInfo1502"),16 : (LPSERVER_INFO_1503, "ServerInfo1503"),17 : (LPSERVER_INFO_1506, "ServerInfo1506"),18 : (LPSERVER_INFO_1510, "ServerInfo1510"),19 : (LPSERVER_INFO_1511, "ServerInfo1511"),20 : (LPSERVER_INFO_1512, "ServerInfo1512"),21 : (LPSERVER_INFO_1513, "ServerInfo1513"),22 : (LPSERVER_INFO_1514, "ServerInfo1514"),23 : (LPSERVER_INFO_1515, "ServerInfo1515"),24 : (LPSERVER_INFO_1516, "ServerInfo1516"),25 : (LPSERVER_INFO_1518, "ServerInfo1518"),26 : (LPSERVER_INFO_1523, "ServerInfo1523"),27 : (LPSERVER_INFO_1528, "ServerInfo1528"),28 : (LPSERVER_INFO_1529, "ServerInfo1529"),29 : (LPSERVER_INFO_1530, "ServerInfo1530"),30 : (LPSERVER_INFO_1533, "ServerInfo1533"),31 : (LPSERVER_INFO_1534, "ServerInfo1534"),32 : (LPSERVER_INFO_1535, "ServerInfo1535"),33 : (LPSERVER_INFO_1536, "ServerInfo1536"),34 : (LPSERVER_INFO_1538, "ServerInfo1538"),35 : (LPSERVER_INFO_1539, "ServerInfo1539"),36 : (LPSERVER_INFO_1540, "ServerInfo1540"),37 : (LPSERVER_INFO_1541, "ServerInfo1541"),38 : (LPSERVER_INFO_1542, "ServerInfo1542"),39 : (LPSERVER_INFO_1543, "ServerInfo1543"),40 : (LPSERVER_INFO_1544, "ServerInfo1544"),41 : (LPSERVER_INFO_1545, "ServerInfo1545"),42 : (LPSERVER_INFO_1546, "ServerInfo1546"),43 : (LPSERVER_INFO_1547, "ServerInfo1547"),44 : (LPSERVER_INFO_1548, "ServerInfo1548"),45 : (LPSERVER_INFO_1549, "ServerInfo1549"),46 : (LPSERVER_INFO_1550, "ServerInfo1550"),47 : (LPSERVER_INFO_1552, "ServerInfo1552"),48 : (LPSERVER_INFO_1553, "ServerInfo1553"),49 : (LPSERVER_INFO_1554, "ServerInfo1554"),50 : (LPSERVER_INFO_1555, "ServerInfo1555"),51 : (LPSERVER_INFO_1556, "ServerInfo1556"),}

    
PSERVER_INFO = SERVER_INFO
LPSERVER_INFO = SERVER_INFO

class DISK_INFO(NdrStructure):
    MEMBERS = [(WCHAR, "Disk"),]

    
PDISK_INFO = DISK_INFO
LPDISK_INFO = DISK_INFO

class DISK_ENUM_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPDISK_INFO, "Buffer"),]

    

class SERVER_TRANSPORT_INFO_0(NdrStructure):
    MEMBERS = [(DWORD, "svti0_numberofvcs"),(PWCHAR_T, "svti0_transportname"),(PUNSIGNED_CHAR, "svti0_transportaddress"),(DWORD, "svti0_transportaddresslength"),(PWCHAR_T, "svti0_networkaddress"),]

    
PSERVER_TRANSPORT_INFO_0 = SERVER_TRANSPORT_INFO_0
LPSERVER_TRANSPORT_INFO_0 = SERVER_TRANSPORT_INFO_0

class SERVER_XPORT_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_TRANSPORT_INFO_0, "Buffer"),]

    
PSERVER_XPORT_INFO_0_CONTAINER = SERVER_XPORT_INFO_0_CONTAINER

class SERVER_TRANSPORT_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "svti1_numberofvcs"),(PWCHAR_T, "svti1_transportname"),(PUNSIGNED_CHAR, "svti1_transportaddress"),(DWORD, "svti1_transportaddresslength"),(PWCHAR_T, "svti1_networkaddress"),(PWCHAR_T, "svti1_domain"),]

    
PSERVER_TRANSPORT_INFO_1 = SERVER_TRANSPORT_INFO_1
LPSERVER_TRANSPORT_INFO_1 = SERVER_TRANSPORT_INFO_1

class SERVER_XPORT_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_TRANSPORT_INFO_1, "Buffer"),]

    
PSERVER_XPORT_INFO_1_CONTAINER = SERVER_XPORT_INFO_1_CONTAINER

class SERVER_TRANSPORT_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "svti2_numberofvcs"),(PWCHAR_T, "svti2_transportname"),(PUNSIGNED_CHAR, "svti2_transportaddress"),(DWORD, "svti2_transportaddresslength"),(PWCHAR_T, "svti2_networkaddress"),(PWCHAR_T, "svti2_domain"),(UNSIGNED_LONG, "svti2_flags"),]

    
PSERVER_TRANSPORT_INFO_2 = SERVER_TRANSPORT_INFO_2
LPSERVER_TRANSPORT_INFO_2 = SERVER_TRANSPORT_INFO_2

class SERVER_XPORT_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_TRANSPORT_INFO_2, "Buffer"),]

    
PSERVER_XPORT_INFO_2_CONTAINER = SERVER_XPORT_INFO_2_CONTAINER

class SERVER_TRANSPORT_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "svti3_numberofvcs"),(PWCHAR_T, "svti3_transportname"),(PUNSIGNED_CHAR, "svti3_transportaddress"),(DWORD, "svti3_transportaddresslength"),(PWCHAR_T, "svti3_networkaddress"),(PWCHAR_T, "svti3_domain"),(UNSIGNED_LONG, "svti3_flags"),(DWORD, "svti3_passwordlength"),(UNSIGNED_CHAR, "svti3_password"),]

    
PSERVER_TRANSPORT_INFO_3 = SERVER_TRANSPORT_INFO_3
LPSERVER_TRANSPORT_INFO_3 = SERVER_TRANSPORT_INFO_3

class SERVER_XPORT_INFO_3_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_TRANSPORT_INFO_3, "Buffer"),]

    
PSERVER_XPORT_INFO_3_CONTAINER = SERVER_XPORT_INFO_3_CONTAINER

class TRANSPORT_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (SERVER_TRANSPORT_INFO_0, "Transport0"),2 : (SERVER_TRANSPORT_INFO_1, "Transport1"),3 : (SERVER_TRANSPORT_INFO_2, "Transport2"),4 : (SERVER_TRANSPORT_INFO_3, "Transport3"),}

    
PTRANSPORT_INFO = TRANSPORT_INFO
LPTRANSPORT_INFO = TRANSPORT_INFO

class SERVER_XPORT_ENUM_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSERVER_XPORT_INFO_0_CONTAINER, "Level0"),2 : (PSERVER_XPORT_INFO_1_CONTAINER, "Level1"),3 : (PSERVER_XPORT_INFO_2_CONTAINER, "Level2"),4 : (PSERVER_XPORT_INFO_3_CONTAINER, "Level3"),}

    

class SERVER_XPORT_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(SERVER_XPORT_ENUM_UNION, "XportInfo"),]

    
PSERVER_XPORT_ENUM_STRUCT = SERVER_XPORT_ENUM_STRUCT
LPSERVER_XPORT_ENUM_STRUCT = SERVER_XPORT_ENUM_STRUCT
SHARE_DEL_HANDLE = VOID
PSHARE_DEL_HANDLE = SHARE_DEL_HANDLE

class ADT_SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(PUNSIGNED_CHAR, "Buffer"),]

    
PADT_SECURITY_DESCRIPTOR = ADT_SECURITY_DESCRIPTOR

class STAT_SERVER_0(NdrStructure):
    MEMBERS = [(DWORD, "sts0_start"),(DWORD, "sts0_fopens"),(DWORD, "sts0_devopens"),(DWORD, "sts0_jobsqueued"),(DWORD, "sts0_sopens"),(DWORD, "sts0_stimedout"),(DWORD, "sts0_serrorout"),(DWORD, "sts0_pwerrors"),(DWORD, "sts0_permerrors"),(DWORD, "sts0_syserrors"),(DWORD, "sts0_bytessent_low"),(DWORD, "sts0_bytessent_high"),(DWORD, "sts0_bytesrcvd_low"),(DWORD, "sts0_bytesrcvd_high"),(DWORD, "sts0_avresponse"),(DWORD, "sts0_reqbufneed"),(DWORD, "sts0_bigbufneed"),]

    
PSTAT_SERVER_0 = STAT_SERVER_0
LPSTAT_SERVER_0 = STAT_SERVER_0

class TIME_OF_DAY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "tod_elapsedt"),(DWORD, "tod_msecs"),(DWORD, "tod_hours"),(DWORD, "tod_mins"),(DWORD, "tod_secs"),(DWORD, "tod_hunds"),(LONG, "tod_timezone"),(DWORD, "tod_tinterval"),(DWORD, "tod_day"),(DWORD, "tod_month"),(DWORD, "tod_year"),(DWORD, "tod_weekday"),]

    
PTIME_OF_DAY_INFO = TIME_OF_DAY_INFO
LPTIME_OF_DAY_INFO = TIME_OF_DAY_INFO

class NET_DFS_ENTRY_ID(NdrStructure):
    MEMBERS = [(GUID, "Uid"),(PWCHAR, "Prefix"),]

    
LPNET_DFS_ENTRY_ID = NET_DFS_ENTRY_ID

class NET_DFS_ENTRY_ID_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Count"),(LPNET_DFS_ENTRY_ID, "Buffer"),]

    
LPNET_DFS_ENTRY_ID_CONTAINER = NET_DFS_ENTRY_ID_CONTAINER

class DFS_SITENAME_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "SiteFlags"),(PWCHAR, "SiteName"),]

    
PDFS_SITENAME_INFO = DFS_SITENAME_INFO
LPDFS_SITENAME_INFO = DFS_SITENAME_INFO

class DFS_SITELIST_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cSites"),(DFS_SITENAME_INFO, "Site"),]

    
PDFS_SITELIST_INFO = DFS_SITELIST_INFO
LPDFS_SITELIST_INFO = DFS_SITELIST_INFO

class SERVER_ALIAS_INFO_0(NdrStructure):
    MEMBERS = [(LMSTR, "srvai0_alias"),(LMSTR, "srvai0_target"),(BOOLEAN, "srvai0_default"),(ULONG, "srvai0_reserved"),]

    
PSERVER_ALIAS_INFO_0 = SERVER_ALIAS_INFO_0
LPSERVER_ALIAS_INFO_0 = SERVER_ALIAS_INFO_0

class SERVER_ALIAS_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_ALIAS_INFO_0, "Buffer"),]

    

class SERVER_ALIAS_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(SERVERALIASINFO, "ServerAliasInfo"),]

    
PSERVER_ALIAS_ENUM_STRUCT = SERVER_ALIAS_ENUM_STRUCT
LPSERVER_ALIAS_ENUM_STRUCT = SERVER_ALIAS_ENUM_STRUCT

class SERVER_ALIAS_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPSERVER_ALIAS_INFO_0, "ServerAliasInfo0"),}

    
PSERVER_ALIAS_INFO = SERVER_ALIAS_INFO
LPSERVER_ALIAS_INFO = SERVER_ALIAS_INFO
Interface("4B324FC8-1670-01D3-1278-5A47BF6EE188", "3.0",[Method("Opnum0NotUsedOnWire",
),Method("Opnum1NotUsedOnWire",
),Method("Opnum2NotUsedOnWire",
),Method("Opnum3NotUsedOnWire",
),Method("Opnum4NotUsedOnWire",
),Method("Opnum5NotUsedOnWire",
),Method("Opnum6NotUsedOnWire",
),Method("Opnum7NotUsedOnWire",
),Method("NetrConnectionEnum",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Qualifier')),
InOut((LPCONNECT_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrFileEnum",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'BasePath')),
In((PWCHAR,'UserName')),
InOut((PFILE_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrFileGetInfo",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'FileId')),
In((DWORD,'Level')),
Out((LPFILE_INFO,'InfoStruct')),
),Method("NetrFileClose",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'FileId')),
),Method("NetrSessionEnum",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'ClientName')),
In((PWCHAR,'UserName')),
InOut((PSESSION_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrSessionDel",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'ClientName')),
In((PWCHAR,'UserName')),
),Method("NetrShareAdd",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSHARE_INFO,'InfoStruct')),
InOut((PDWORD,'ParmErr')),
),Method("NetrShareEnum",
In((SRVSVC_HANDLE,'ServerName')),
InOut((LPSHARE_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrShareGetInfo",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'NetName')),
In((DWORD,'Level')),
Out((LPSHARE_INFO,'InfoStruct')),
),Method("NetrShareSetInfo",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'NetName')),
In((DWORD,'Level')),
In((LPSHARE_INFO,'ShareInfo')),
InOut((PDWORD,'ParmErr')),
),Method("NetrShareDel",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'NetName')),
In((DWORD,'Reserved')),
),Method("NetrShareDelSticky",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'NetName')),
In((DWORD,'Reserved')),
),Method("NetrShareCheck",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Device')),
Out((PDWORD,'Type')),
),Method("NetrServerGetInfo",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
Out((LPSERVER_INFO,'InfoStruct')),
),Method("NetrServerSetInfo",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSERVER_INFO,'ServerInfo')),
InOut((PDWORD,'ParmErr')),
),Method("NetrServerDiskEnum",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
InOut((PDISK_ENUM_CONTAINER,'DiskInfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrServerStatisticsGet",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Service')),
In((DWORD,'Level')),
In((DWORD,'Options')),
Out((PLPSTAT_SERVER_0,'InfoStruct')),
),Method("NetrServerTransportAdd",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSERVER_TRANSPORT_INFO_0,'Buffer')),
),Method("NetrServerTransportEnum",
In((SRVSVC_HANDLE,'ServerName')),
InOut((LPSERVER_XPORT_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrServerTransportDel",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSERVER_TRANSPORT_INFO_0,'Buffer')),
),Method("NetrRemoteTOD",
In((SRVSVC_HANDLE,'ServerName')),
Out((PLPTIME_OF_DAY_INFO,'BufferPtr')),
),Method("Opnum29NotUsedOnWire",
),Method("NetprPathType",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'PathName')),
Out((PDWORD,'PathType')),
In((DWORD,'Flags')),
),Method("NetprPathCanonicalize",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'PathName')),
Out((PUNSIGNED_CHAR,'Outbuf')),
In((DWORD,'OutbufLen')),
In((PWCHAR,'Prefix')),
InOut((PDWORD,'PathType')),
In((DWORD,'Flags')),
),Method("NetprPathCompare",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'PathName1')),
In((PWCHAR,'PathName2')),
In((DWORD,'PathType')),
In((DWORD,'Flags')),
),Method("NetprNameValidate",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Name')),
In((DWORD,'NameType')),
In((DWORD,'Flags')),
),Method("NetprNameCanonicalize",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Name')),
Out((PWCHAR,'Outbuf')),
In((DWORD,'OutbufLen')),
In((DWORD,'NameType')),
In((DWORD,'Flags')),
),Method("NetprNameCompare",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'Name1')),
In((PWCHAR,'Name2')),
In((DWORD,'NameType')),
In((DWORD,'Flags')),
),Method("NetrShareEnumSticky",
In((SRVSVC_HANDLE,'ServerName')),
InOut((LPSHARE_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((PDWORD,'TotalEntries')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrShareDelStart",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'NetName')),
In((DWORD,'Reserved')),
Out((PSHARE_DEL_HANDLE,'ContextHandle')),
),Method("NetrShareDelCommit",
InOut((PSHARE_DEL_HANDLE,'ContextHandle')),
),Method("NetrpGetFileSecurity",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'ShareName')),
In((PWCHAR,'lpFileName')),
In((SECURITY_INFORMATION,'RequestedInformation')),
Out((PPADT_SECURITY_DESCRIPTOR,'SecurityDescriptor')),
),Method("NetrpSetFileSecurity",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'ShareName')),
In((PWCHAR,'lpFileName')),
In((SECURITY_INFORMATION,'SecurityInformation')),
In((PADT_SECURITY_DESCRIPTOR,'SecurityDescriptor')),
),Method("NetrServerTransportAddEx",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPTRANSPORT_INFO,'Buffer')),
),Method("Opnum42NotUsedOnWire",
),Method("NetrDfsGetVersion",
In((SRVSVC_HANDLE,'ServerName')),
Out((PDWORD,'Version')),
),Method("NetrDfsCreateLocalPartition",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'ShareName')),
In((PGUID,'EntryUid')),
In((PWCHAR,'EntryPrefix')),
In((PWCHAR,'ShortName')),
In((LPNET_DFS_ENTRY_ID_CONTAINER,'RelationInfo')),
In((INT,'Force')),
),Method("NetrDfsDeleteLocalPartition",
In((SRVSVC_HANDLE,'ServerName')),
In((PGUID,'Uid')),
In((PWCHAR,'Prefix')),
),Method("NetrDfsSetLocalVolumeState",
In((SRVSVC_HANDLE,'ServerName')),
In((PGUID,'Uid')),
In((PWCHAR,'Prefix')),
In((UNSIGNED_LONG,'State')),
),Method("Opnum47NotUsedOnWire",
),Method("NetrDfsCreateExitPoint",
In((SRVSVC_HANDLE,'ServerName')),
In((PGUID,'Uid')),
In((PWCHAR,'Prefix')),
In((UNSIGNED_LONG,'Type')),
In((DWORD,'ShortPrefixLen')),
Out((PWCHAR,'ShortPrefix')),
),Method("NetrDfsDeleteExitPoint",
In((SRVSVC_HANDLE,'ServerName')),
In((PGUID,'Uid')),
In((PWCHAR,'Prefix')),
In((UNSIGNED_LONG,'Type')),
),Method("NetrDfsModifyPrefix",
In((SRVSVC_HANDLE,'ServerName')),
In((PGUID,'Uid')),
In((PWCHAR,'Prefix')),
),Method("NetrDfsFixLocalVolume",
In((SRVSVC_HANDLE,'ServerName')),
In((PWCHAR,'VolumeName')),
In((UNSIGNED_LONG,'EntryType')),
In((UNSIGNED_LONG,'ServiceType')),
In((PWCHAR,'StgId')),
In((PGUID,'EntryUid')),
In((PWCHAR,'EntryPrefix')),
In((LPNET_DFS_ENTRY_ID_CONTAINER,'RelationInfo')),
In((UNSIGNED_LONG,'CreateDisposition')),
),Method("NetrDfsManagerReportSiteInfo",
In((SRVSVC_HANDLE,'ServerName')),
InOut((PLPDFS_SITELIST_INFO,'ppSiteInfo')),
),Method("NetrServerTransportDelEx",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPTRANSPORT_INFO,'Buffer')),
),Method("NetrServerAliasAdd",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSERVER_ALIAS_INFO,'InfoStruct')),
),Method("NetrServerAliasEnum",
In((SRVSVC_HANDLE,'ServerName')),
InOut((LPSERVER_ALIAS_ENUM_STRUCT,'InfoStruct')),
In((DWORD,'PreferedMaximumLength')),
Out((LPDWORD,'TotalEntries')),
InOut((LPDWORD,'ResumeHandle')),
),Method("NetrServerAliasDel",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSERVER_ALIAS_INFO,'InfoStruct')),
),Method("NetrShareDelEx",
In((SRVSVC_HANDLE,'ServerName')),
In((DWORD,'Level')),
In((LPSHARE_INFO,'ShareInfo')),
),])