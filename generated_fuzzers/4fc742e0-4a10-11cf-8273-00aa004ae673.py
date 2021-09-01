
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
NET_API_STATUS = DWORD
NETDFS_SERVER_OR_DOMAIN_HANDLE = WCHAR

class DFS_TARGET_PRIORITY_CLASS(NdrEnum):
    MAP = ((1-1 , 'DfsInvalidPriorityClass'),(0 , 'DfsSiteCostNormalPriorityClass'),(1 , 'DfsGlobalHighPriorityClass'),(2 , 'DfsSiteCostHighPriorityClass'),(3 , 'DfsSiteCostLowPriorityClass'),(4 , 'DfsGlobalLowPriorityClass'),)        

class DFS_TARGET_PRIORITY(NdrStructure):
    MEMBERS = [(DFS_TARGET_PRIORITY_CLASS, "TargetPriorityClass"),(UNSIGNED_SHORT, "TargetPriorityRank"),(UNSIGNED_SHORT, "Reserved"),]

    

class DFS_STORAGE_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "State"),(PWCHAR, "ServerName"),(PWCHAR, "ShareName"),]

    

class DFS_STORAGE_INFO_1(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "State"),(PWCHAR, "ServerName"),(PWCHAR, "ShareName"),(DFS_TARGET_PRIORITY, "TargetPriority"),]

    
PDFS_STORAGE_INFO_1 = DFS_STORAGE_INFO_1
LPDFS_STORAGE_INFO_1 = DFS_STORAGE_INFO_1

class DFSM_ROOT_LIST_ENTRY(NdrStructure):
    MEMBERS = [(PWCHAR, "ServerShare"),]

    

class DFSM_ROOT_LIST(NdrStructure):
    MEMBERS = [(DWORD, "cEntries"),(DFSM_ROOT_LIST_ENTRY, "Entry"),]

    

class DFS_NAMESPACE_VERSION_ORIGIN(NdrEnum):
    MAP = ((0 , 'DFS_NAMESPACE_VERSION_ORIGIN_COMBINED'),(1 , 'DFS_NAMESPACE_VERSION_ORIGIN_SERVER'),(2 , 'DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN'),)        

class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "DomainDfsMajorVersion"),(UNSIGNED_LONG, "DomainDfsMinorVersion"),(ULONGLONG, "DomainDfsCapabilities"),(UNSIGNED_LONG, "StandaloneDfsMajorVersion"),(UNSIGNED_LONG, "StandaloneDfsMinorVersion"),(ULONGLONG, "StandaloneDfsCapabilities"),]

    
PDFS_SUPPORTED_NAMESPACE_VERSION_INFO = DFS_SUPPORTED_NAMESPACE_VERSION_INFO

class DFS_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),]

    

class DFS_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(DWORD, "NumberOfStorages"),]

    

class DFS_INFO_3(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(DWORD, "NumberOfStorages"),(PDFS_STORAGE_INFO, "Storage"),]

    

class DFS_INFO_4(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(GUID, "Guid"),(DWORD, "NumberOfStorages"),(PDFS_STORAGE_INFO, "Storage"),]

    

class DFS_INFO_5(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(GUID, "Guid"),(UNSIGNED_LONG, "PropertyFlags"),(UNSIGNED_LONG, "MetadataSize"),(DWORD, "NumberOfStorages"),]

    

class DFS_INFO_6(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(GUID, "Guid"),(UNSIGNED_LONG, "PropertyFlags"),(UNSIGNED_LONG, "MetadataSize"),(DWORD, "NumberOfStorages"),(PDFS_STORAGE_INFO_1, "Storage"),]

    

class DFS_INFO_7(NdrStructure):
    MEMBERS = [(GUID, "GenerationGuid"),]

    

class DFS_INFO_8(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(GUID, "Guid"),(UNSIGNED_LONG, "PropertyFlags"),(UNSIGNED_LONG, "MetadataSize"),(ULONG, "SecurityDescriptorLength"),(PUCHAR, "pSecurityDescriptor"),(DWORD, "NumberOfStorages"),]

    
LPDFS_INFO_8 = DFS_INFO_8

class DFS_INFO_9(NdrStructure):
    MEMBERS = [(PWCHAR, "EntryPath"),(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(GUID, "Guid"),(UNSIGNED_LONG, "PropertyFlags"),(UNSIGNED_LONG, "MetadataSize"),(ULONG, "SecurityDescriptorLength"),(PUCHAR, "pSecurityDescriptor"),(DWORD, "NumberOfStorages"),(LPDFS_STORAGE_INFO_1, "Storage"),]

    
LPDFS_INFO_9 = DFS_INFO_9

class DFS_INFO_50(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "NamespaceMajorVersion"),(UNSIGNED_LONG, "NamespaceMinorVersion"),(UNSIGNED___INT64, "NamespaceCapabilities"),]

    

class DFS_INFO_100(NdrStructure):
    MEMBERS = [(PWCHAR, "Comment"),]

    

class DFS_INFO_101(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "State"),]

    

class DFS_INFO_102(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Timeout"),]

    

class DFS_INFO_103(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "PropertyFlagMask"),(UNSIGNED_LONG, "PropertyFlags"),]

    

class DFS_INFO_104(NdrStructure):
    MEMBERS = [(DFS_TARGET_PRIORITY, "TargetPriority"),]

    

class DFS_INFO_105(NdrStructure):
    MEMBERS = [(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(UNSIGNED_LONG, "PropertyFlagMask"),(UNSIGNED_LONG, "PropertyFlags"),]

    

class DFS_INFO_106(NdrStructure):
    MEMBERS = [(DWORD, "State"),(DFS_TARGET_PRIORITY, "TargetPriority"),]

    

class DFS_INFO_107(NdrStructure):
    MEMBERS = [(PWCHAR, "Comment"),(DWORD, "State"),(UNSIGNED_LONG, "Timeout"),(UNSIGNED_LONG, "PropertyFlagMask"),(UNSIGNED_LONG, "PropertyFlags"),(ULONG, "SecurityDescriptorLength"),(PUCHAR, "pSecurityDescriptor"),]

    

class DFS_INFO_150(NdrStructure):
    MEMBERS = [(ULONG, "SecurityDescriptorLength"),(PUCHAR, "pSecurityDescriptor"),]

    

class DFS_INFO_200(NdrStructure):
    MEMBERS = [(PWCHAR, "FtDfsName"),]

    

class DFS_INFO_300(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(PWCHAR, "DfsName"),]

    

class DFS_INFO_STRUCT(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PDFS_INFO_1, "DfsInfo1"),2 : (PDFS_INFO_2, "DfsInfo2"),3 : (PDFS_INFO_3, "DfsInfo3"),4 : (PDFS_INFO_4, "DfsInfo4"),5 : (PDFS_INFO_5, "DfsInfo5"),6 : (PDFS_INFO_6, "DfsInfo6"),7 : (PDFS_INFO_7, "DfsInfo7"),8 : (PDFS_INFO_8, "DfsInfo8"),9 : (PDFS_INFO_9, "DfsInfo9"),10 : (PDFS_INFO_50, "DfsInfo50"),11 : (PDFS_INFO_100, "DfsInfo100"),12 : (PDFS_INFO_101, "DfsInfo101"),13 : (PDFS_INFO_102, "DfsInfo102"),14 : (PDFS_INFO_103, "DfsInfo103"),15 : (PDFS_INFO_104, "DfsInfo104"),16 : (PDFS_INFO_105, "DfsInfo105"),17 : (PDFS_INFO_106, "DfsInfo106"),18 : (PDFS_INFO_107, "DfsInfo107"),19 : (PDFS_INFO_150, "DfsInfo150"),}

    

class DFS_INFO_1_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_1, "Buffer"),]

    

class DFS_INFO_2_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_2, "Buffer"),]

    

class DFS_INFO_3_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_3, "Buffer"),]

    

class DFS_INFO_4_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_4, "Buffer"),]

    

class DFS_INFO_5_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_5, "Buffer"),]

    

class DFS_INFO_6_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_6, "Buffer"),]

    

class DFS_INFO_8_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPDFS_INFO_8, "Buffer"),]

    
LPDFS_INFO_8_CONTAINER = DFS_INFO_8_CONTAINER

class DFS_INFO_9_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPDFS_INFO_9, "Buffer"),]

    
LPDFS_INFO_9_CONTAINER = DFS_INFO_9_CONTAINER

class DFS_INFO_200_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_200, "Buffer"),]

    

class DFS_INFO_300_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(PDFS_INFO_300, "Buffer"),]

    

class DFS_INFO_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(DFSINFOCONTAINER, "DfsInfoContainer"),]

    
Interface("4fc742e0-4a10-11cf-8273-00aa004ae673", "3.0",[Method("NetrDfsManagerGetVersion",
),Method("NetrDfsAdd",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
In((PWCHAR,'Comment')),
In((DWORD,'Flags')),
),Method("NetrDfsRemove",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
),Method("NetrDfsSetInfo",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
In((DWORD,'Level')),
In((PDFS_INFO_STRUCT,'DfsInfo')),
),Method("NetrDfsGetInfo",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
In((DWORD,'Level')),
Out((PDFS_INFO_STRUCT,'DfsInfo')),
),Method("NetrDfsEnum",
In((DWORD,'Level')),
In((DWORD,'PrefMaxLen')),
InOut((PDFS_INFO_ENUM_STRUCT,'DfsEnum')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrDfsMove",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'NewDfsEntryPath')),
In((UNSIGNED_LONG,'Flags')),
),Method("Opnum7NotUsedOnWire",
),Method("Opnum8NotUsedOnWire",
),Method("Opnum9NotUsedOnWire",
),Method("NetrDfsAddFtRoot",
In((PWCHAR,'ServerName')),
In((PWCHAR,'DcName')),
In((PWCHAR,'RootShare')),
In((PWCHAR,'FtDfsName')),
In((PWCHAR,'Comment')),
In((PWCHAR,'ConfigDN')),
In((BOOLEAN,'NewFtDfs')),
In((DWORD,'ApiFlags')),
InOut((PPDFSM_ROOT_LIST,'ppRootList')),
),Method("NetrDfsRemoveFtRoot",
In((PWCHAR,'ServerName')),
In((PWCHAR,'DcName')),
In((PWCHAR,'RootShare')),
In((PWCHAR,'FtDfsName')),
In((DWORD,'ApiFlags')),
InOut((PPDFSM_ROOT_LIST,'ppRootList')),
),Method("NetrDfsAddStdRoot",
In((PWCHAR,'ServerName')),
In((PWCHAR,'RootShare')),
In((PWCHAR,'Comment')),
In((DWORD,'ApiFlags')),
),Method("NetrDfsRemoveStdRoot",
In((PWCHAR,'ServerName')),
In((PWCHAR,'RootShare')),
In((DWORD,'ApiFlags')),
),Method("NetrDfsManagerInitialize",
In((PWCHAR,'ServerName')),
In((DWORD,'Flags')),
),Method("NetrDfsAddStdRootForced",
In((PWCHAR,'ServerName')),
In((PWCHAR,'RootShare')),
In((PWCHAR,'Comment')),
In((PWCHAR,'Share')),
),Method("NetrDfsGetDcAddress",
In((PWCHAR,'ServerName')),
InOut((PPWCHAR,'DcName')),
InOut((PBOOLEAN,'IsRoot')),
InOut((PUNSIGNED_LONG,'Timeout')),
),Method("NetrDfsSetDcAddress",
In((PWCHAR,'ServerName')),
In((PWCHAR,'DcName')),
In((DWORD,'Timeout')),
In((DWORD,'Flags')),
),Method("NetrDfsFlushFtTable",
In((PWCHAR,'DcName')),
In((PWCHAR,'wszFtDfsName')),
),Method("NetrDfsAdd2",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'DcName')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
In((PWCHAR,'Comment')),
In((DWORD,'Flags')),
InOut((PPDFSM_ROOT_LIST,'ppRootList')),
),Method("NetrDfsRemove2",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'DcName')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
InOut((PPDFSM_ROOT_LIST,'ppRootList')),
),Method("NetrDfsEnumEx",
In((PWCHAR,'DfsEntryPath')),
In((DWORD,'Level')),
In((DWORD,'PrefMaxLen')),
InOut((PDFS_INFO_ENUM_STRUCT,'DfsEnum')),
InOut((PDWORD,'ResumeHandle')),
),Method("NetrDfsSetInfo2",
In((PWCHAR,'DfsEntryPath')),
In((PWCHAR,'DcName')),
In((PWCHAR,'ServerName')),
In((PWCHAR,'ShareName')),
In((DWORD,'Level')),
In((PDFS_INFO_STRUCT,'pDfsInfo')),
InOut((PPDFSM_ROOT_LIST,'ppRootList')),
),Method("NetrDfsAddRootTarget",
In((LPWSTR,'pDfsPath')),
In((LPWSTR,'pTargetPath')),
In((ULONG,'MajorVersion')),
In((LPWSTR,'pComment')),
In((BOOLEAN,'NewNamespace')),
In((ULONG,'Flags')),
),Method("NetrDfsRemoveRootTarget",
In((LPWSTR,'pDfsPath')),
In((LPWSTR,'pTargetPath')),
In((ULONG,'Flags')),
),Method("NetrDfsGetSupportedNamespaceVersion",
In((DFS_NAMESPACE_VERSION_ORIGIN,'Origin')),
In((NETDFS_SERVER_OR_DOMAIN_HANDLE,'pName')),
Out((PDFS_SUPPORTED_NAMESPACE_VERSION_INFO,'pVersionInfo')),
),])