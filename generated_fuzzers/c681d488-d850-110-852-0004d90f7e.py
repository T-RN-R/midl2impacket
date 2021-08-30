
from fuzzer.midl import *
from fuzzer.core import *

class ('FILETIME', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLowDateTime"),(('DWORD', None), "dwHighDateTime"),]

    

class ('GUID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "Data1"),(('UNSIGNED_SHORT', None), "Data2"),(('UNSIGNED_SHORT', None), "Data3"),(('BYTE', None), "Data4"),]

    

class ('LARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('SIGNED___INT64', None), "QuadPart"),]

    

class ('EVENT_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Id"),(('UCHAR', None), "Version"),(('UCHAR', None), "Channel"),(('UCHAR', None), "Level"),(('UCHAR', None), "Opcode"),(('USHORT', None), "Task"),(('ULONGLONG', None), "Keyword"),]

    

class ('S0', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "KernelTime"),(('ULONG', None), "UserTime"),]

    

class ('U0', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('S0', None), s0),2 : (('ULONG64', None), ProcessorTime),}

    

class ('EVENT_HEADER', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Size"),(('USHORT', None), "HeaderType"),(('USHORT', None), "Flags"),(('USHORT', None), "EventProperty"),(('ULONG', None), "ThreadId"),(('ULONG', None), "ProcessId"),(('LARGE_INTEGER', None), "TimeStamp"),(('GUID', None), "ProviderId"),(('EVENT_DESCRIPTOR', None), "EventDescriptor"),(('U0', None), "u0"),(('GUID', None), "ActivityId"),]

    

class ('LUID', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "LowPart"),(('LONG', None), "HighPart"),]

    

class ('MULTI_SZ', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "Value"),(('DWORD', None), "nChar"),]

    

class ('RPC_UNICODE_STRING', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "Length"),(('UNSIGNED_SHORT', None), "MaximumLength"),(('PWCHAR', None), "Buffer"),]

    

class ('SERVER_INFO_100', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv100_platform_id"),(('PWCHAR_T', None), "sv100_name"),]

    

class ('SERVER_INFO_101', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv101_platform_id"),(('PWCHAR_T', None), "sv101_name"),(('DWORD', None), "sv101_version_major"),(('DWORD', None), "sv101_version_minor"),(('DWORD', None), "sv101_version_type"),(('PWCHAR_T', None), "sv101_comment"),]

    

class ('SYSTEMTIME', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wYear"),(('WORD', None), "wMonth"),(('WORD', None), "wDayOfWeek"),(('WORD', None), "wDay"),(('WORD', None), "wHour"),(('WORD', None), "wMinute"),(('WORD', None), "wSecond"),(('WORD', None), "wMilliseconds"),]

    

class ('UINT128', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "lower"),(('UINT64', None), "upper"),]

    

class ('ULARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT64', None), "QuadPart"),]

    

class ('RPC_SID_IDENTIFIER_AUTHORITY', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "Value"),]

    

class ('OBJECT_TYPE_LIST', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "Level"),(('ACCESS_MASK', None), "Remaining"),(('PGUID', None), "ObjectType"),]

    

class ('ACE_HEADER', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "AceType"),(('UCHAR', None), "AceFlags"),(('USHORT', None), "AceSize"),]

    

class ('SYSTEM_MANDATORY_LABEL_ACE', None)(NdrStructure):
    MEMBERS = [(('ACE_HEADER', None), "Header"),(('ACCESS_MASK', None), "Mask"),(('DWORD', None), "SidStart"),]

    

class ('TOKEN_MANDATORY_POLICY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Policy"),]

    

class ('MANDATORY_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('ACCESS_MASK', None), "AllowedAccess"),(('BOOLEAN', None), "WriteAllowed"),(('BOOLEAN', None), "ReadAllowed"),(('BOOLEAN', None), "ExecuteAllowed"),(('TOKEN_MANDATORY_POLICY', None), "MandatoryPolicy"),]

    

class ('CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Length"),(('BYTE', None), "OctetString"),]

    

class ('VALUES', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PLONG64', None), pInt64),2 : (('PDWORD64', None), pUint64),3 : (('PWSTR', None), ppString),4 : (('PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None), pOctetString),}

    

class ('CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Name"),(('WORD', None), "ValueType"),(('WORD', None), "Reserved"),(('DWORD', None), "Flags"),(('DWORD', None), "ValueCount"),(('VALUES', None), "Values"),]

    

class ('RPC_SID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "Revision"),(('UNSIGNED_CHAR', None), "SubAuthorityCount"),(('RPC_SID_IDENTIFIER_AUTHORITY', None), "IdentifierAuthority"),(('UNSIGNED_LONG', None), "SubAuthority"),]

    

class ('ACL', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "AclRevision"),(('UNSIGNED_CHAR', None), "Sbz1"),(('UNSIGNED_SHORT', None), "AclSize"),(('UNSIGNED_SHORT', None), "AceCount"),(('UNSIGNED_SHORT', None), "Sbz2"),]

    

class ('SECURITY_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Revision"),(('UCHAR', None), "Sbz1"),(('USHORT', None), "Control"),(('PSID', None), "Owner"),(('PSID', None), "Group"),(('PACL', None), "Sacl"),(('PACL', None), "Dacl"),]

    
Method("EfsRpcOpenFileRaw",
In(HANDLE_T),
Out(PPEXIMPORT_CONTEXT_HANDLE),
In(PWCHAR_T),
In(LONG),
),Method("EfsRpcReadFileRaw",
In(PEXIMPORT_CONTEXT_HANDLE),
Out(PEFS_EXIM_PIPE),
),Method("EfsRpcWriteFileRaw",
In(PEXIMPORT_CONTEXT_HANDLE),
In(PEFS_EXIM_PIPE),
),Method("EfsRpcCloseRaw",
InOut(PPEXIMPORT_CONTEXT_HANDLE),
),Method("EfsRpcEncryptFileSrv",
In(HANDLE_T),
In(PWCHAR_T),
),Method("EfsRpcDecryptFileSrv",
In(HANDLE_T),
In(PWCHAR_T),
In(UNSIGNED_LONG),
),Method("EfsRpcQueryUsersOnFile",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPENCRYPTION_CERTIFICATE_HASH_LIST),
),Method("EfsRpcQueryRecoveryAgents",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPENCRYPTION_CERTIFICATE_HASH_LIST),
),Method("EfsRpcRemoveUsersFromFile",
In(HANDLE_T),
In(PWCHAR_T),
In(PENCRYPTION_CERTIFICATE_HASH_LIST),
),Method("EfsRpcAddUsersToFile",
In(HANDLE_T),
In(PWCHAR_T),
In(PENCRYPTION_CERTIFICATE_LIST),
),Method("Opnum10NotUsedOnWire",
In(),
),Method("EfsRpcNotSupported",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
In(PEFS_RPC_BLOB),
In(BOOL),
),Method("EfsRpcFileKeyInfo",
In(HANDLE_T),
In(PWCHAR_T),
In(DWORD),
Out(PPEFS_RPC_BLOB),
),Method("EfsRpcDuplicateEncryptionInfoFile",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
In(PEFS_RPC_BLOB),
In(BOOL),
),Method("Opnum14NotUsedOnWire",
In(),
),Method("EfsRpcAddUsersToFileEx",
In(HANDLE_T),
In(DWORD),
In(PEFS_RPC_BLOB),
In(PWCHAR_T),
In(PENCRYPTION_CERTIFICATE_LIST),
),Method("EfsRpcFileKeyInfoEx",
In(HANDLE_T),
In(DWORD),
In(PEFS_RPC_BLOB),
In(PWCHAR_T),
In(DWORD),
Out(PPEFS_RPC_BLOB),
),Method("Opnum17NotUsedOnWire",
In(),
),Method("EfsRpcGetEncryptedFileMetadata",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPEFS_RPC_BLOB),
),Method("EfsRpcSetEncryptedFileMetadata",
In(HANDLE_T),
In(PWCHAR_T),
In(PEFS_RPC_BLOB),
In(PEFS_RPC_BLOB),
In(PENCRYPTED_FILE_METADATA_SIGNATURE),
),Method("EfsRpcFlushEfsCache",
In(HANDLE_T),
),Method("EfsRpcEncryptFileExSrv",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(UNSIGNED_LONG),
),Method("EfsRpcQueryProtectors",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPPENCRYPTION_PROTECTOR_LIST),
),Method("Opnum23NotUsedOnWire",
In(),
),Method("Opnum24NotUsedOnWire",
In(),
),Method("Opnum25NotUsedOnWire",
In(),
),Method("Opnum26NotUsedOnWire",
In(),
),Method("Opnum27NotUsedOnWire",
In(),
),Method("Opnum28NotUsedOnWire",
In(),
),Method("Opnum29NotUsedOnWire",
In(),
),Method("Opnum30NotUsedOnWire",
In(),
),Method("Opnum31NotUsedOnWire",
In(),
),Method("Opnum32NotUsedOnWire",
In(),
),Method("Opnum33NotUsedOnWire",
In(),
),Method("Opnum34NotUsedOnWire",
In(),
),Method("Opnum35NotUsedOnWire",
In(),
),Method("Opnum36NotUsedOnWire",
In(),
),Method("Opnum37NotUsedOnWire",
In(),
),Method("Opnum38NotUsedOnWire",
In(),
),Method("Opnum39NotUsedOnWire",
In(),
),Method("Opnum40NotUsedOnWire",
In(),
),Method("Opnum41NotUsedOnWire",
In(),
),Method("Opnum42NotUsedOnWire",
In(),
),Method("Opnum43NotUsedOnWire",
In(),
),Method("Opnum44NotUsedOnWire",
In(),
),