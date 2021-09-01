
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

class RPC_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PCHAR, "Buffer"),]

    
PRPC_STRING = RPC_STRING

class RPC_CLIENT_ID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "UniqueProcess"),(UNSIGNED_LONG, "UniqueThread"),]

    
PRPC_CLIENT_ID = RPC_CLIENT_ID
EVENTLOG_HANDLE_W = WCHAR_T
EVENTLOG_HANDLE_A = CHAR
IELF_HANDLE = VOID
PIELF_HANDLE = VOID
RULONG = UNSIGNED_LONG
Interface("82273FDC-E32A-18C3-3F78-827929DC23EA", "0.0",[Method("ElfrClearELFW",
In((IELF_HANDLE,'LogHandle')),
In((PRPC_UNICODE_STRING,'BackupFileName')),
),Method("ElfrBackupELFW",
In((IELF_HANDLE,'LogHandle')),
In((PRPC_UNICODE_STRING,'BackupFileName')),
),Method("ElfrCloseEL",
InOut((PIELF_HANDLE,'LogHandle')),
),Method("ElfrDeregisterEventSource",
InOut((PIELF_HANDLE,'LogHandle')),
),Method("ElfrNumberOfRecords",
In((IELF_HANDLE,'LogHandle')),
Out((PUNSIGNED_LONG,'NumberOfRecords')),
),Method("ElfrOldestRecord",
In((IELF_HANDLE,'LogHandle')),
Out((PUNSIGNED_LONG,'OldestRecordNumber')),
),Method("ElfrChangeNotify",
In((IELF_HANDLE,'LogHandle')),
In((RPC_CLIENT_ID,'ClientId')),
In((ULONG,'Event')),
),Method("ElfrOpenELW",
In((EVENTLOG_HANDLE_W,'UNCServerName')),
In((PRPC_UNICODE_STRING,'ModuleName')),
In((PRPC_UNICODE_STRING,'RegModuleName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrRegisterEventSourceW",
In((EVENTLOG_HANDLE_W,'UNCServerName')),
In((PRPC_UNICODE_STRING,'ModuleName')),
In((PRPC_UNICODE_STRING,'RegModuleName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrOpenBELW",
In((EVENTLOG_HANDLE_W,'UNCServerName')),
In((PRPC_UNICODE_STRING,'BackupFileName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrReadELW",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'ReadFlags')),
In((UNSIGNED_LONG,'RecordOffset')),
In((RULONG,'NumberOfBytesToRead')),
Out((PUNSIGNED_CHAR,'Buffer')),
Out((PUNSIGNED_LONG,'NumberOfBytesRead')),
Out((PUNSIGNED_LONG,'MinNumberOfBytesNeeded')),
),Method("ElfrReportEventW",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'Time')),
In((UNSIGNED_SHORT,'EventType')),
In((UNSIGNED_SHORT,'EventCategory')),
In((UNSIGNED_LONG,'EventID')),
In((UNSIGNED_SHORT,'NumStrings')),
In((UNSIGNED_LONG,'DataSize')),
In((PRPC_UNICODE_STRING,'ComputerName')),
In((PRPC_SID,'UserSID')),
In((PRPC_UNICODE_STRING,'Strings')),
In((PUNSIGNED_CHAR,'Data')),
In((UNSIGNED_SHORT,'Flags')),
InOut((PUNSIGNED_LONG,'RecordNumber')),
InOut((PUNSIGNED_LONG,'TimeWritten')),
),Method("ElfrClearELFA",
In((IELF_HANDLE,'LogHandle')),
In((PRPC_STRING,'BackupFileName')),
),Method("ElfrBackupELFA",
In((IELF_HANDLE,'LogHandle')),
In((PRPC_STRING,'BackupFileName')),
),Method("ElfrOpenELA",
In((EVENTLOG_HANDLE_A,'UNCServerName')),
In((PRPC_STRING,'ModuleName')),
In((PRPC_STRING,'RegModuleName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrRegisterEventSourceA",
In((EVENTLOG_HANDLE_A,'UNCServerName')),
In((PRPC_STRING,'ModuleName')),
In((PRPC_STRING,'RegModuleName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrOpenBELA",
In((EVENTLOG_HANDLE_A,'UNCServerName')),
In((PRPC_STRING,'BackupFileName')),
In((UNSIGNED_LONG,'MajorVersion')),
In((UNSIGNED_LONG,'MinorVersion')),
Out((PIELF_HANDLE,'LogHandle')),
),Method("ElfrReadELA",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'ReadFlags')),
In((UNSIGNED_LONG,'RecordOffset')),
In((RULONG,'NumberOfBytesToRead')),
Out((PUNSIGNED_CHAR,'Buffer')),
Out((PUNSIGNED_LONG,'NumberOfBytesRead')),
Out((PUNSIGNED_LONG,'MinNumberOfBytesNeeded')),
),Method("ElfrReportEventA",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'Time')),
In((UNSIGNED_SHORT,'EventType')),
In((UNSIGNED_SHORT,'EventCategory')),
In((UNSIGNED_LONG,'EventID')),
In((UNSIGNED_SHORT,'NumStrings')),
In((UNSIGNED_LONG,'DataSize')),
In((PRPC_STRING,'ComputerName')),
In((PRPC_SID,'UserSID')),
In((PRPC_STRING,'Strings')),
In((PUNSIGNED_CHAR,'Data')),
In((UNSIGNED_SHORT,'Flags')),
InOut((PUNSIGNED_LONG,'RecordNumber')),
InOut((PUNSIGNED_LONG,'TimeWritten')),
),Method("Opnum19NotUsedOnWire",
),Method("Opnum20NotUsedOnWire",
),Method("Opnum21NotUsedOnWire",
),Method("ElfrGetLogInformation",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'InfoLevel')),
Out((PUNSIGNED_CHAR,'lpBuffer')),
In((UNSIGNED_LONG,'cbBufSize')),
Out((PUNSIGNED_LONG,'pcbBytesNeeded')),
),Method("Opnum23NotUsedOnWire",
),Method("ElfrReportEventAndSourceW",
In((IELF_HANDLE,'LogHandle')),
In((UNSIGNED_LONG,'Time')),
In((UNSIGNED_SHORT,'EventType')),
In((UNSIGNED_SHORT,'EventCategory')),
In((UNSIGNED_LONG,'EventID')),
In((PRPC_UNICODE_STRING,'SourceName')),
In((UNSIGNED_SHORT,'NumStrings')),
In((UNSIGNED_LONG,'DataSize')),
In((PRPC_UNICODE_STRING,'ComputerName')),
In((PRPC_SID,'UserSID')),
In((PRPC_UNICODE_STRING,'Strings')),
In((PUNSIGNED_CHAR,'Data')),
In((UNSIGNED_SHORT,'Flags')),
InOut((PUNSIGNED_LONG,'RecordNumber')),
InOut((PUNSIGNED_LONG,'TimeWritten')),
),Method("ElfrReportEventExW",
In((IELF_HANDLE,'LogHandle')),
In((PFILETIME,'TimeGenerated')),
In((UNSIGNED_SHORT,'EventType')),
In((UNSIGNED_SHORT,'EventCategory')),
In((UNSIGNED_LONG,'EventID')),
In((UNSIGNED_SHORT,'NumStrings')),
In((UNSIGNED_LONG,'DataSize')),
In((PRPC_UNICODE_STRING,'ComputerName')),
In((PRPC_SID,'UserSID')),
In((PRPC_UNICODE_STRING,'Strings')),
In((PUNSIGNED_CHAR,'Data')),
In((UNSIGNED_SHORT,'Flags')),
InOut((PUNSIGNED_LONG,'RecordNumber')),
),Method("ElfrReportEventExA",
In((IELF_HANDLE,'LogHandle')),
In((PFILETIME,'TimeGenerated')),
In((UNSIGNED_SHORT,'EventType')),
In((UNSIGNED_SHORT,'EventCategory')),
In((UNSIGNED_LONG,'EventID')),
In((UNSIGNED_SHORT,'NumStrings')),
In((UNSIGNED_LONG,'DataSize')),
In((PRPC_STRING,'ComputerName')),
In((PRPC_SID,'UserSID')),
In((PRPC_STRING,'Strings')),
In((PUNSIGNED_CHAR,'Data')),
In((UNSIGNED_SHORT,'Flags')),
InOut((PUNSIGNED_LONG,'RecordNumber')),
),])