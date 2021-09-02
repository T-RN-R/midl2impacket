
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
PEXIMPORT_CONTEXT_HANDLE = VOID
EFS_EXIM_PIPE = PIPE_UNSIGNED_CHAR

class EFS_RPC_BLOB(NdrStructure):
    MEMBERS = [(DWORD, "cbData"),(PUNSIGNED_CHAR, "bData"),]

    
PEFS_RPC_BLOB = EFS_RPC_BLOB

class EFS_COMPATIBILITY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "EfsVersion"),]

    
ALG_ID = UNSIGNED_INT

class EFS_HASH_BLOB(NdrStructure):
    MEMBERS = [(DWORD, "cbData"),(PUNSIGNED_CHAR, "bData"),]

    

class ENCRYPTION_CERTIFICATE_HASH(NdrStructure):
    MEMBERS = [(DWORD, "cbTotalLength"),(PRPC_SID, "UserSid"),(PEFS_HASH_BLOB, "Hash"),(PWCHAR_T, "lpDisplayInformation"),]

    

class ENCRYPTION_CERTIFICATE_HASH_LIST(NdrStructure):
    MEMBERS = [(DWORD, "nCert_Hash"),(PPENCRYPTION_CERTIFICATE_HASH, "Users"),]

    

class EFS_CERTIFICATE_BLOB(NdrStructure):
    MEMBERS = [(DWORD, "dwCertEncodingType"),(DWORD, "cbData"),(PUNSIGNED_CHAR, "bData"),]

    

class ENCRYPTION_CERTIFICATE(NdrStructure):
    MEMBERS = [(DWORD, "cbTotalLength"),(PRPC_SID, "UserSid"),(PEFS_CERTIFICATE_BLOB, "CertBlob"),]

    

class ENCRYPTION_CERTIFICATE_LIST(NdrStructure):
    MEMBERS = [(DWORD, "nUsers"),(PPENCRYPTION_CERTIFICATE, "Users"),]

    

class ENCRYPTED_FILE_METADATA_SIGNATURE(NdrStructure):
    MEMBERS = [(DWORD, "dwEfsAccessType"),(PENCRYPTION_CERTIFICATE_HASH_LIST, "CertificatesAdded"),(PENCRYPTION_CERTIFICATE, "EncryptionCertificate"),(PEFS_RPC_BLOB, "EfsStreamSignature"),]

    

class EFS_KEY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(UNSIGNED_LONG, "Entropy"),(ALG_ID, "Algorithm"),(UNSIGNED_LONG, "KeyLength"),]

    

class EFS_DECRYPTION_STATUS_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwDecryptionError"),(DWORD, "dwHashOffset"),(DWORD, "cbHash"),]

    

class EFS_ENCRYPTION_STATUS_INFO(NdrStructure):
    MEMBERS = [(BOOL, "bHasCurrentKey"),(DWORD, "dwEncryptionError"),]

    

class ENCRYPTION_PROTECTOR(NdrStructure):
    MEMBERS = [(DWORD, "cbTotalLength"),(PRPC_SID, "UserSid"),(PWCHAR_T, "lpProtectorDescriptor"),]

    
PENCRYPTION_PROTECTOR = ENCRYPTION_PROTECTOR

class ENCRYPTION_PROTECTOR_LIST(NdrStructure):
    MEMBERS = [(DWORD, "nProtectors"),(PPENCRYPTION_PROTECTOR, "pProtectors"),]

    
PENCRYPTION_PROTECTOR_LIST = ENCRYPTION_PROTECTOR_LIST
Interface("c681d488-d850-110-852-0004d90f7e", "1.0",[Method("EfsRpcOpenFileRaw",
In((HANDLE_T,'binding_h')),
Out((PPEXIMPORT_CONTEXT_HANDLE,'hContext')),
In((PWCHAR_T,'FileName')),
In((LONG,'Flags')),
),Method("EfsRpcReadFileRaw",
In((PEXIMPORT_CONTEXT_HANDLE,'hContext')),
Out((PEFS_EXIM_PIPE,'EfsOutPipe')),
),Method("EfsRpcWriteFileRaw",
In((PEXIMPORT_CONTEXT_HANDLE,'hContext')),
In((PEFS_EXIM_PIPE,'EfsInPipe')),
),Method("EfsRpcCloseRaw",
InOut((PPEXIMPORT_CONTEXT_HANDLE,'hContext')),
),Method("EfsRpcEncryptFileSrv",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
),Method("EfsRpcDecryptFileSrv",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((UNSIGNED_LONG,'OpenFlag')),
),Method("EfsRpcQueryUsersOnFile",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
Out((PPENCRYPTION_CERTIFICATE_HASH_LIST,'Users')),
),Method("EfsRpcQueryRecoveryAgents",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
Out((PPENCRYPTION_CERTIFICATE_HASH_LIST,'RecoveryAgents')),
),Method("EfsRpcRemoveUsersFromFile",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((PENCRYPTION_CERTIFICATE_HASH_LIST,'Users')),
),Method("EfsRpcAddUsersToFile",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((PENCRYPTION_CERTIFICATE_LIST,'EncryptionCertificates')),
),Method("Opnum10NotUsedOnWire",
),Method("EfsRpcNotSupported",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'Reserved1')),
In((PWCHAR_T,'Reserved2')),
In((DWORD,'dwReserved1')),
In((DWORD,'dwReserved2')),
In((PEFS_RPC_BLOB,'Reserved')),
In((BOOL,'bReserved')),
),Method("EfsRpcFileKeyInfo",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((DWORD,'InfoClass')),
Out((PPEFS_RPC_BLOB,'KeyInfo')),
),Method("EfsRpcDuplicateEncryptionInfoFile",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'SrcFileName')),
In((PWCHAR_T,'DestFileName')),
In((DWORD,'dwCreationDisposition')),
In((DWORD,'dwAttributes')),
In((PEFS_RPC_BLOB,'RelativeSD')),
In((BOOL,'bInheritHandle')),
),Method("Opnum14NotUsedOnWire",
),Method("EfsRpcAddUsersToFileEx",
In((HANDLE_T,'binding_h')),
In((DWORD,'dwFlags')),
In((PEFS_RPC_BLOB,'Reserved')),
In((PWCHAR_T,'FileName')),
In((PENCRYPTION_CERTIFICATE_LIST,'EncryptionCertificates')),
),Method("EfsRpcFileKeyInfoEx",
In((HANDLE_T,'binding_h')),
In((DWORD,'dwFileKeyInfoFlags')),
In((PEFS_RPC_BLOB,'Reserved')),
In((PWCHAR_T,'FileName')),
In((DWORD,'InfoClass')),
Out((PPEFS_RPC_BLOB,'KeyInfo')),
),Method("Opnum17NotUsedOnWire",
),Method("EfsRpcGetEncryptedFileMetadata",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
Out((PPEFS_RPC_BLOB,'EfsStreamBlob')),
),Method("EfsRpcSetEncryptedFileMetadata",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((PEFS_RPC_BLOB,'OldEfsStreamBlob')),
In((PEFS_RPC_BLOB,'NewEfsStreamBlob')),
In((PENCRYPTED_FILE_METADATA_SIGNATURE,'NewEfsSignature')),
),Method("EfsRpcFlushEfsCache",
In((HANDLE_T,'binding_h')),
),Method("EfsRpcEncryptFileExSrv",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
In((PWCHAR_T,'ProtectorDescriptor')),
In((UNSIGNED_LONG,'Flags')),
),Method("EfsRpcQueryProtectors",
In((HANDLE_T,'binding_h')),
In((PWCHAR_T,'FileName')),
Out((PPPENCRYPTION_PROTECTOR_LIST,'ppProtectorList')),
),Method("Opnum23NotUsedOnWire",
),Method("Opnum24NotUsedOnWire",
),Method("Opnum25NotUsedOnWire",
),Method("Opnum26NotUsedOnWire",
),Method("Opnum27NotUsedOnWire",
),Method("Opnum28NotUsedOnWire",
),Method("Opnum29NotUsedOnWire",
),Method("Opnum30NotUsedOnWire",
),Method("Opnum31NotUsedOnWire",
),Method("Opnum32NotUsedOnWire",
),Method("Opnum33NotUsedOnWire",
),Method("Opnum34NotUsedOnWire",
),Method("Opnum35NotUsedOnWire",
),Method("Opnum36NotUsedOnWire",
),Method("Opnum37NotUsedOnWire",
),Method("Opnum38NotUsedOnWire",
),Method("Opnum39NotUsedOnWire",
),Method("Opnum40NotUsedOnWire",
),Method("Opnum41NotUsedOnWire",
),Method("Opnum42NotUsedOnWire",
),Method("Opnum43NotUsedOnWire",
),Method("Opnum44NotUsedOnWire",
),])