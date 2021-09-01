
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

class NETSETUP_JOIN_STATUS(NdrEnum):
    MAP = ((0 , 'NetSetupUnknownStatus'),(1 , 'NetSetupUnjoined'),(2 , 'NetSetupWorkgroupName'),(3 , 'NetSetupDomainName'),)        

class NETSETUP_NAME_TYPE(NdrEnum):
    MAP = ((0 , 'NetSetupUnknown'),(1 , 'NetSetupMachine'),(2 , 'NetSetupWorkgroup'),(3 , 'NetSetupDomain'),(4 , 'NetSetupNonExistentDomain'),(5 , 'NetSetupDnsMachine'),)        

class NET_COMPUTER_NAME_TYPE(NdrEnum):
    MAP = ((0 , 'NetPrimaryComputerName'),(1 , 'NetAlternateComputerNames'),(2 , 'NetAllComputerNames'),(3 , 'NetComputerNameTypeMax'),)        

class STAT_WORKSTATION_0(NdrStructure):
    MEMBERS = [(LARGE_INTEGER, "StatisticsStartTime"),(LARGE_INTEGER, "BytesReceived"),(LARGE_INTEGER, "SmbsReceived"),(LARGE_INTEGER, "PagingReadBytesRequested"),(LARGE_INTEGER, "NonPagingReadBytesRequested"),(LARGE_INTEGER, "CacheReadBytesRequested"),(LARGE_INTEGER, "NetworkReadBytesRequested"),(LARGE_INTEGER, "BytesTransmitted"),(LARGE_INTEGER, "SmbsTransmitted"),(LARGE_INTEGER, "PagingWriteBytesRequested"),(LARGE_INTEGER, "NonPagingWriteBytesRequested"),(LARGE_INTEGER, "CacheWriteBytesRequested"),(LARGE_INTEGER, "NetworkWriteBytesRequested"),(UNSIGNED_LONG, "InitiallyFailedOperations"),(UNSIGNED_LONG, "FailedCompletionOperations"),(UNSIGNED_LONG, "ReadOperations"),(UNSIGNED_LONG, "RandomReadOperations"),(UNSIGNED_LONG, "ReadSmbs"),(UNSIGNED_LONG, "LargeReadSmbs"),(UNSIGNED_LONG, "SmallReadSmbs"),(UNSIGNED_LONG, "WriteOperations"),(UNSIGNED_LONG, "RandomWriteOperations"),(UNSIGNED_LONG, "WriteSmbs"),(UNSIGNED_LONG, "LargeWriteSmbs"),(UNSIGNED_LONG, "SmallWriteSmbs"),(UNSIGNED_LONG, "RawReadsDenied"),(UNSIGNED_LONG, "RawWritesDenied"),(UNSIGNED_LONG, "NetworkErrors"),(UNSIGNED_LONG, "Sessions"),(UNSIGNED_LONG, "FailedSessions"),(UNSIGNED_LONG, "Reconnects"),(UNSIGNED_LONG, "CoreConnects"),(UNSIGNED_LONG, "Lanman20Connects"),(UNSIGNED_LONG, "Lanman21Connects"),(UNSIGNED_LONG, "LanmanNtConnects"),(UNSIGNED_LONG, "ServerDisconnects"),(UNSIGNED_LONG, "HungSessions"),(UNSIGNED_LONG, "UseCount"),(UNSIGNED_LONG, "FailedUseCount"),(UNSIGNED_LONG, "CurrentCommands"),]

    
PSTAT_WORKSTATION_0 = STAT_WORKSTATION_0
LPSTAT_WORKSTATION_0 = STAT_WORKSTATION_0

class WKSTA_INFO_100(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki100_platform_id"),(PWCHAR_T, "wki100_computername"),(PWCHAR_T, "wki100_langroup"),(UNSIGNED_LONG, "wki100_ver_major"),(UNSIGNED_LONG, "wki100_ver_minor"),]

    
PWKSTA_INFO_100 = WKSTA_INFO_100
LPWKSTA_INFO_100 = WKSTA_INFO_100

class WKSTA_INFO_101(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki101_platform_id"),(PWCHAR_T, "wki101_computername"),(PWCHAR_T, "wki101_langroup"),(UNSIGNED_LONG, "wki101_ver_major"),(UNSIGNED_LONG, "wki101_ver_minor"),(PWCHAR_T, "wki101_lanroot"),]

    
PWKSTA_INFO_101 = WKSTA_INFO_101
LPWKSTA_INFO_101 = WKSTA_INFO_101

class WKSTA_INFO_102(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki102_platform_id"),(PWCHAR_T, "wki102_computername"),(PWCHAR_T, "wki102_langroup"),(UNSIGNED_LONG, "wki102_ver_major"),(UNSIGNED_LONG, "wki102_ver_minor"),(PWCHAR_T, "wki102_lanroot"),(UNSIGNED_LONG, "wki102_logged_on_users"),]

    
PWKSTA_INFO_102 = WKSTA_INFO_102
LPWKSTA_INFO_102 = WKSTA_INFO_102

class WKSTA_INFO_502(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki502_char_wait"),(UNSIGNED_LONG, "wki502_collection_time"),(UNSIGNED_LONG, "wki502_maximum_collection_count"),(UNSIGNED_LONG, "wki502_keep_conn"),(UNSIGNED_LONG, "wki502_max_cmds"),(UNSIGNED_LONG, "wki502_sess_timeout"),(UNSIGNED_LONG, "wki502_siz_char_buf"),(UNSIGNED_LONG, "wki502_max_threads"),(UNSIGNED_LONG, "wki502_lock_quota"),(UNSIGNED_LONG, "wki502_lock_increment"),(UNSIGNED_LONG, "wki502_lock_maximum"),(UNSIGNED_LONG, "wki502_pipe_increment"),(UNSIGNED_LONG, "wki502_pipe_maximum"),(UNSIGNED_LONG, "wki502_cache_file_timeout"),(UNSIGNED_LONG, "wki502_dormant_file_limit"),(UNSIGNED_LONG, "wki502_read_ahead_throughput"),(UNSIGNED_LONG, "wki502_num_mailslot_buffers"),(UNSIGNED_LONG, "wki502_num_srv_announce_buffers"),(UNSIGNED_LONG, "wki502_max_illegal_datagram_events"),(UNSIGNED_LONG, "wki502_illegal_datagram_event_reset_frequency"),(INT, "wki502_log_election_packets"),(INT, "wki502_use_opportunistic_locking"),(INT, "wki502_use_unlock_behind"),(INT, "wki502_use_close_behind"),(INT, "wki502_buf_named_pipes"),(INT, "wki502_use_lock_read_unlock"),(INT, "wki502_utilize_nt_caching"),(INT, "wki502_use_raw_read"),(INT, "wki502_use_raw_write"),(INT, "wki502_use_write_raw_data"),(INT, "wki502_use_encryption"),(INT, "wki502_buf_files_deny_write"),(INT, "wki502_buf_read_only_files"),(INT, "wki502_force_core_create_mode"),(INT, "wki502_use_512_byte_max_transfer"),]

    
PWKSTA_INFO_502 = WKSTA_INFO_502
LPWKSTA_INFO_502 = WKSTA_INFO_502

class WKSTA_INFO_1013(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki1013_keep_conn"),]

    
PWKSTA_INFO_1013 = WKSTA_INFO_1013
LPWKSTA_INFO_1013 = WKSTA_INFO_1013

class WKSTA_INFO_1018(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki1018_sess_timeout"),]

    
PWKSTA_INFO_1018 = WKSTA_INFO_1018
LPWKSTA_INFO_1018 = WKSTA_INFO_1018

class WKSTA_INFO_1046(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wki1046_dormant_file_limit"),]

    
PWKSTA_INFO_1046 = WKSTA_INFO_1046
LPWKSTA_INFO_1046 = WKSTA_INFO_1046

class WKSTA_USER_INFO_0(NdrStructure):
    MEMBERS = [(PWCHAR_T, "wkui0_username"),]

    
PWKSTA_USER_INFO_0 = WKSTA_USER_INFO_0
LPWKSTA_USER_INFO_0 = WKSTA_USER_INFO_0

class WKSTA_USER_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "wkui1_username"),(PWCHAR_T, "wkui1_logon_domain"),(PWCHAR_T, "wkui1_oth_domains"),(PWCHAR_T, "wkui1_logon_server"),]

    
PWKSTA_USER_INFO_1 = WKSTA_USER_INFO_1
LPWKSTA_USER_INFO_1 = WKSTA_USER_INFO_1

class WKSTA_TRANSPORT_INFO_0(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "wkti0_quality_of_service"),(UNSIGNED_LONG, "wkti0_number_of_vcs"),(PWCHAR_T, "wkti0_transport_name"),(PWCHAR_T, "wkti0_transport_address"),(UNSIGNED_LONG, "wkti0_wan_ish"),]

    
PWKSTA_TRANSPORT_INFO_0 = WKSTA_TRANSPORT_INFO_0
LPWKSTA_TRANSPORT_INFO_0 = WKSTA_TRANSPORT_INFO_0
WKSSVC_IDENTIFY_HANDLE = WCHAR_T
WKSSVC_IMPERSONATE_HANDLE = WCHAR_T

class WKSTA_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPWKSTA_INFO_100, "WkstaInfo100"),2 : (LPWKSTA_INFO_101, "WkstaInfo101"),3 : (LPWKSTA_INFO_102, "WkstaInfo102"),4 : (LPWKSTA_INFO_502, "WkstaInfo502"),5 : (LPWKSTA_INFO_1013, "WkstaInfo1013"),6 : (LPWKSTA_INFO_1018, "WkstaInfo1018"),7 : (LPWKSTA_INFO_1046, "WkstaInfo1046"),}

    
PWKSTA_INFO = WKSTA_INFO
LPWKSTA_INFO = WKSTA_INFO

class USE_INFO_0(NdrStructure):
    MEMBERS = [(PWCHAR_T, "ui0_local"),(PWCHAR_T, "ui0_remote"),]

    
PUSE_INFO_0 = USE_INFO_0
LPUSE_INFO_0 = USE_INFO_0

class USE_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "ui1_local"),(PWCHAR_T, "ui1_remote"),(PWCHAR_T, "ui1_password"),(UNSIGNED_LONG, "ui1_status"),(UNSIGNED_LONG, "ui1_asg_type"),(UNSIGNED_LONG, "ui1_refcount"),(UNSIGNED_LONG, "ui1_usecount"),]

    
PUSE_INFO_1 = USE_INFO_1
LPUSE_INFO_1 = USE_INFO_1

class USE_INFO_2(NdrStructure):
    MEMBERS = [(USE_INFO_1, "ui2_useinfo"),(PWCHAR_T, "ui2_username"),(PWCHAR_T, "ui2_domainname"),]

    
PUSE_INFO_2 = USE_INFO_2
LPUSE_INFO_2 = USE_INFO_2

class USE_INFO_3(NdrStructure):
    MEMBERS = [(USE_INFO_2, "ui3_ui2"),(ULONG, "ui3_flags"),]

    
PUSE_INFO_3 = USE_INFO_3
LPUSE_INFO_3 = USE_INFO_3

class USE_INFO(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LPUSE_INFO_0, "UseInfo0"),2 : (LPUSE_INFO_1, "UseInfo1"),3 : (LPUSE_INFO_2, "UseInfo2"),4 : (LPUSE_INFO_3, "UseInfo3"),}

    
PUSE_INFO = USE_INFO
LPUSE_INFO = USE_INFO

class USE_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPUSE_INFO_0, "Buffer"),]

    
PUSE_INFO_0_CONTAINER = USE_INFO_0_CONTAINER
LPUSE_INFO_0_CONTAINER = USE_INFO_0_CONTAINER

class USE_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPUSE_INFO_1, "Buffer"),]

    
PUSE_INFO_1_CONTAINER = USE_INFO_1_CONTAINER
LPUSE_INFO_1_CONTAINER = USE_INFO_1_CONTAINER

class USE_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPUSE_INFO_2, "Buffer"),]

    
PUSE_INFO_2_CONTAINER = USE_INFO_2_CONTAINER
LPUSE_INFO_2_CONTAINER = USE_INFO_2_CONTAINER

class USE_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(USEINFO, "UseInfo"),]

    
PUSE_ENUM_STRUCT = USE_ENUM_STRUCT
LPUSE_ENUM_STRUCT = USE_ENUM_STRUCT

class WKSTA_USER_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPWKSTA_USER_INFO_0, "Buffer"),]

    
PWKSTA_USER_INFO_0_CONTAINER = WKSTA_USER_INFO_0_CONTAINER
LPWKSTA_USER_INFO_0_CONTAINER = WKSTA_USER_INFO_0_CONTAINER

class WKSTA_USER_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPWKSTA_USER_INFO_1, "Buffer"),]

    
PWKSTA_USER_INFO_1_CONTAINER = WKSTA_USER_INFO_1_CONTAINER
LPWKSTA_USER_INFO_1_CONTAINER = WKSTA_USER_INFO_1_CONTAINER

class WKSTA_USER_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Level"),(WKSTAUSERINFO, "WkstaUserInfo"),]

    
PWKSTA_USER_ENUM_STRUCT = WKSTA_USER_ENUM_STRUCT
LPWKSTA_USER_ENUM_STRUCT = WKSTA_USER_ENUM_STRUCT

class WKSTA_TRANSPORT_INFO_0_CONTAINER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntriesRead"),(LPWKSTA_TRANSPORT_INFO_0, "Buffer"),]

    
PWKSTA_TRANSPORT_INFO_0_CONTAINER = WKSTA_TRANSPORT_INFO_0_CONTAINER
LPWKSTA_TRANSPORT_INFO_0_CONTAINER = WKSTA_TRANSPORT_INFO_0_CONTAINER

class WKSTA_TRANSPORT_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Level"),(WKSTATRANSPORTINFO, "WkstaTransportInfo"),]

    
PWKSTA_TRANSPORT_ENUM_STRUCT = WKSTA_TRANSPORT_ENUM_STRUCT
LPWKSTA_TRANSPORT_ENUM_STRUCT = WKSTA_TRANSPORT_ENUM_STRUCT

class JOINPR_USER_PASSWORD(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Obfuscator"),(WCHAR_T, "Buffer"),(UNSIGNED_LONG, "Length"),]

    
PJOINPR_USER_PASSWORD = JOINPR_USER_PASSWORD

class JOINPR_ENCRYPTED_USER_PASSWORD(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Buffer"),]

    
PJOINPR_ENCRYPTED_USER_PASSWORD = JOINPR_ENCRYPTED_USER_PASSWORD

class UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PUNSIGNED_SHORT, "Buffer"),]

    
PUNICODE_STRING = UNICODE_STRING

class NET_COMPUTER_NAME_ARRAY(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "EntryCount"),(PUNICODE_STRING, "ComputerNames"),]

    
PNET_COMPUTER_NAME_ARRAY = NET_COMPUTER_NAME_ARRAY
Interface("6BFFD098-A112-3610-9833-46C3F87E345A", "1.0",[Method("NetrWkstaGetInfo",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
In((UNSIGNED_LONG,'Level')),
Out((LPWKSTA_INFO,'WkstaInfo')),
),Method("NetrWkstaSetInfo",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
In((UNSIGNED_LONG,'Level')),
In((LPWKSTA_INFO,'WkstaInfo')),
InOut((PUNSIGNED_LONG,'ErrorParameter')),
),Method("NetrWkstaUserEnum",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
InOut((LPWKSTA_USER_ENUM_STRUCT,'UserInfo')),
In((UNSIGNED_LONG,'PreferredMaximumLength')),
Out((PUNSIGNED_LONG,'TotalEntries')),
InOut((PUNSIGNED_LONG,'ResumeHandle')),
),Method("Opnum3NotUsedOnWire",
),Method("Opnum4NotUsedOnWire",
),Method("NetrWkstaTransportEnum",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
InOut((LPWKSTA_TRANSPORT_ENUM_STRUCT,'TransportInfo')),
In((UNSIGNED_LONG,'PreferredMaximumLength')),
Out((PUNSIGNED_LONG,'TotalEntries')),
InOut((PUNSIGNED_LONG,'ResumeHandle')),
),Method("NetrWkstaTransportAdd",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
In((UNSIGNED_LONG,'Level')),
In((LPWKSTA_TRANSPORT_INFO_0,'TransportInfo')),
InOut((PUNSIGNED_LONG,'ErrorParameter')),
),Method("NetrWkstaTransportDel",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
In((PWCHAR_T,'TransportName')),
In((UNSIGNED_LONG,'ForceLevel')),
),Method("NetrUseAdd",
In((WKSSVC_IMPERSONATE_HANDLE,'ServerName')),
In((UNSIGNED_LONG,'Level')),
In((LPUSE_INFO,'InfoStruct')),
InOut((PUNSIGNED_LONG,'ErrorParameter')),
),Method("NetrUseGetInfo",
In((WKSSVC_IMPERSONATE_HANDLE,'ServerName')),
In((PWCHAR_T,'UseName')),
In((UNSIGNED_LONG,'Level')),
Out((LPUSE_INFO,'InfoStruct')),
),Method("NetrUseDel",
In((WKSSVC_IMPERSONATE_HANDLE,'ServerName')),
In((PWCHAR_T,'UseName')),
In((UNSIGNED_LONG,'ForceLevel')),
),Method("NetrUseEnum",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
InOut((LPUSE_ENUM_STRUCT,'InfoStruct')),
In((UNSIGNED_LONG,'PreferredMaximumLength')),
Out((PUNSIGNED_LONG,'TotalEntries')),
InOut((PUNSIGNED_LONG,'ResumeHandle')),
),Method("Opnum12NotUsedOnWire",
),Method("NetrWorkstationStatisticsGet",
In((WKSSVC_IDENTIFY_HANDLE,'ServerName')),
In((PWCHAR_T,'ServiceName')),
In((UNSIGNED_LONG,'Level')),
In((UNSIGNED_LONG,'Options')),
Out((PLPSTAT_WORKSTATION_0,'Buffer')),
),Method("Opnum14NotUsedOnWire",
),Method("Opnum15NotUsedOnWire",
),Method("Opnum16NotUsedOnWire",
),Method("Opnum17NotUsedOnWire",
),Method("Opnum18NotUsedOnWire",
),Method("Opnum19NotUsedOnWire",
),Method("NetrGetJoinInformation",
In((WKSSVC_IMPERSONATE_HANDLE,'ServerName')),
InOut((PPWCHAR_T,'NameBuffer')),
Out((PNETSETUP_JOIN_STATUS,'BufferType')),
),Method("Opnum21NotUsedOnWire",
),Method("NetrJoinDomain2",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'DomainNameParam')),
In((PWCHAR_T,'MachineAccountOU')),
In((PWCHAR_T,'AccountName')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'Password')),
In((UNSIGNED_LONG,'Options')),
),Method("NetrUnjoinDomain2",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'AccountName')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'Password')),
In((UNSIGNED_LONG,'Options')),
),Method("NetrRenameMachineInDomain2",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'MachineName')),
In((PWCHAR_T,'AccountName')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'Password')),
In((UNSIGNED_LONG,'Options')),
),Method("NetrValidateName2",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'NameToValidate')),
In((PWCHAR_T,'AccountName')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'Password')),
In((NETSETUP_NAME_TYPE,'NameType')),
),Method("NetrGetJoinableOUs2",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'DomainNameParam')),
In((PWCHAR_T,'AccountName')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'Password')),
InOut((PUNSIGNED_LONG,'OUCount')),
Out((PPPWCHAR_T,'OUs')),
),Method("NetrAddAlternateComputerName",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'AlternateName')),
In((PWCHAR_T,'DomainAccount')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'EncryptedPassword')),
In((UNSIGNED_LONG,'Reserved')),
),Method("NetrRemoveAlternateComputerName",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'AlternateName')),
In((PWCHAR_T,'DomainAccount')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'EncryptedPassword')),
In((UNSIGNED_LONG,'Reserved')),
),Method("NetrSetPrimaryComputerName",
In((HANDLE_T,'RpcBindingHandle')),
In((PWCHAR_T,'ServerName')),
In((PWCHAR_T,'PrimaryName')),
In((PWCHAR_T,'DomainAccount')),
In((PJOINPR_ENCRYPTED_USER_PASSWORD,'EncryptedPassword')),
In((UNSIGNED_LONG,'Reserved')),
),Method("NetrEnumerateComputerNames",
In((WKSSVC_IMPERSONATE_HANDLE,'ServerName')),
In((NET_COMPUTER_NAME_TYPE,'NameType')),
In((UNSIGNED_LONG,'Reserved')),
Out((PPNET_COMPUTER_NAME_ARRAY,'ComputerNames')),
),])