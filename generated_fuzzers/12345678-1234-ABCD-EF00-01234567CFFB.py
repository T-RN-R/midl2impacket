
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

class STRING(NdrStructure):
    MEMBERS = [(USHORT, "Length"),(USHORT, "MaximumLength"),(PCHAR, "Buffer"),]

    
PSTRING = STRING

class OLD_LARGE_INTEGER(NdrStructure):
    MEMBERS = [(ULONG, "LowPart"),(LONG, "HighPart"),]

    
POLD_LARGE_INTEGER = OLD_LARGE_INTEGER

class CYPHER_BLOCK(NdrStructure):
    MEMBERS = [(CHAR, "data"),]

    
PCYPHER_BLOCK = CYPHER_BLOCK

class NT_OWF_PASSWORD(NdrStructure):
    MEMBERS = [(CYPHER_BLOCK, "data"),]

    
PNT_OWF_PASSWORD = NT_OWF_PASSWORD
ENCRYPTED_NT_OWF_PASSWORD = NT_OWF_PASSWORD
PENCRYPTED_NT_OWF_PASSWORD = NT_OWF_PASSWORD

class LM_OWF_PASSWORD(NdrStructure):
    MEMBERS = [(CYPHER_BLOCK, "data"),]

    
PLM_OWF_PASSWORD = LM_OWF_PASSWORD
ENCRYPTED_LM_OWF_PASSWORD = LM_OWF_PASSWORD
PENCRYPTED_LM_OWF_PASSWORD = LM_OWF_PASSWORD
LOGONSRV_HANDLE = WCHAR_T

class NLPR_SID_INFORMATION(NdrStructure):
    MEMBERS = [(PRPC_SID, "SidPointer"),]

    
PNLPR_SID_INFORMATION = NLPR_SID_INFORMATION

class NLPR_SID_ARRAY(NdrStructure):
    MEMBERS = [(ULONG, "Count"),(PNLPR_SID_INFORMATION, "Sids"),]

    
PNLPR_SID_ARRAY = NLPR_SID_ARRAY

class NLPR_CR_CIPHER_VALUE(NdrStructure):
    MEMBERS = [(ULONG, "Length"),(ULONG, "MaximumLength"),(PUCHAR, "Buffer"),]

    
PNLPR_CR_CIPHER_VALUE = NLPR_CR_CIPHER_VALUE

class NLPR_LOGON_HOURS(NdrStructure):
    MEMBERS = [(USHORT, "UnitsPerWeek"),(PUCHAR, "LogonHours"),]

    
PNLPR_LOGON_HOURS = NLPR_LOGON_HOURS

class NLPR_USER_PRIVATE_INFO(NdrStructure):
    MEMBERS = [(UCHAR, "SensitiveData"),(ULONG, "DataLength"),(PUCHAR, "Data"),]

    
PNLPR_USER_PRIVATE_INFO = NLPR_USER_PRIVATE_INFO

class NLPR_MODIFIED_COUNT(NdrStructure):
    MEMBERS = [(OLD_LARGE_INTEGER, "ModifiedCount"),]

    
PNLPR_MODIFIED_COUNT = NLPR_MODIFIED_COUNT

class NLPR_QUOTA_LIMITS(NdrStructure):
    MEMBERS = [(ULONG, "PagedPoolLimit"),(ULONG, "NonPagedPoolLimit"),(ULONG, "MinimumWorkingSetSize"),(ULONG, "MaximumWorkingSetSize"),(ULONG, "PagefileLimit"),(OLD_LARGE_INTEGER, "Reserved"),]

    
PNLPR_QUOTA_LIMITS = NLPR_QUOTA_LIMITS

class NETLOGON_DELTA_USER(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "UserName"),(RPC_UNICODE_STRING, "FullName"),(ULONG, "UserId"),(ULONG, "PrimaryGroupId"),(RPC_UNICODE_STRING, "HomeDirectory"),(RPC_UNICODE_STRING, "HomeDirectoryDrive"),(RPC_UNICODE_STRING, "ScriptPath"),(RPC_UNICODE_STRING, "AdminComment"),(RPC_UNICODE_STRING, "WorkStations"),(OLD_LARGE_INTEGER, "LastLogon"),(OLD_LARGE_INTEGER, "LastLogoff"),(NLPR_LOGON_HOURS, "LogonHours"),(USHORT, "BadPasswordCount"),(USHORT, "LogonCount"),(OLD_LARGE_INTEGER, "PasswordLastSet"),(OLD_LARGE_INTEGER, "AccountExpires"),(ULONG, "UserAccountControl"),(ENCRYPTED_NT_OWF_PASSWORD, "EncryptedNtOwfPassword"),(ENCRYPTED_LM_OWF_PASSWORD, "EncryptedLmOwfPassword"),(UCHAR, "NtPasswordPresent"),(UCHAR, "LmPasswordPresent"),(UCHAR, "PasswordExpired"),(RPC_UNICODE_STRING, "UserComment"),(RPC_UNICODE_STRING, "Parameters"),(USHORT, "CountryCode"),(USHORT, "CodePage"),(NLPR_USER_PRIVATE_INFO, "PrivateData"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "ProfilePath"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_USER = NETLOGON_DELTA_USER

class NETLOGON_DELTA_GROUP(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "Name"),(ULONG, "RelativeId"),(ULONG, "Attributes"),(RPC_UNICODE_STRING, "AdminComment"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_GROUP = NETLOGON_DELTA_GROUP

class NETLOGON_DELTA_GROUP_MEMBER(NdrStructure):
    MEMBERS = [(PULONG, "Members"),(PULONG, "Attributes"),(ULONG, "MemberCount"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_GROUP_MEMBER = NETLOGON_DELTA_GROUP_MEMBER

class NETLOGON_DELTA_ALIAS(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "Name"),(ULONG, "RelativeId"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "Comment"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_ALIAS = NETLOGON_DELTA_ALIAS

class NETLOGON_DELTA_ALIAS_MEMBER(NdrStructure):
    MEMBERS = [(NLPR_SID_ARRAY, "Members"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_ALIAS_MEMBER = NETLOGON_DELTA_ALIAS_MEMBER

class NETLOGON_DELTA_DOMAIN(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "DomainName"),(RPC_UNICODE_STRING, "OemInformation"),(OLD_LARGE_INTEGER, "ForceLogoff"),(USHORT, "MinPasswordLength"),(USHORT, "PasswordHistoryLength"),(OLD_LARGE_INTEGER, "MaxPasswordAge"),(OLD_LARGE_INTEGER, "MinPasswordAge"),(OLD_LARGE_INTEGER, "DomainModifiedCount"),(OLD_LARGE_INTEGER, "DomainCreationTime"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DomainLockoutInformation"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "PasswordProperties"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_DOMAIN = NETLOGON_DELTA_DOMAIN

class NETLOGON_RENAME_GROUP(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "OldName"),(RPC_UNICODE_STRING, "NewName"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_RENAME_GROUP = NETLOGON_RENAME_GROUP

class NETLOGON_RENAME_USER(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "OldName"),(RPC_UNICODE_STRING, "NewName"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_RENAME_USER = NETLOGON_RENAME_USER

class NETLOGON_RENAME_ALIAS(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "OldName"),(RPC_UNICODE_STRING, "NewName"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_RENAME_ALIAS = NETLOGON_RENAME_ALIAS

class NETLOGON_DELTA_POLICY(NdrStructure):
    MEMBERS = [(ULONG, "MaximumLogSize"),(OLD_LARGE_INTEGER, "AuditRetentionPeriod"),(UCHAR, "AuditingMode"),(ULONG, "MaximumAuditEventCount"),(PULONG, "EventAuditingOptions"),(RPC_UNICODE_STRING, "PrimaryDomainName"),(PRPC_SID, "PrimaryDomainSid"),(NLPR_QUOTA_LIMITS, "QuotaLimits"),(OLD_LARGE_INTEGER, "ModifiedId"),(OLD_LARGE_INTEGER, "DatabaseCreationTime"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_POLICY = NETLOGON_DELTA_POLICY

class NETLOGON_DELTA_TRUSTED_DOMAINS(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "DomainName"),(ULONG, "NumControllerEntries"),(PRPC_UNICODE_STRING, "ControllerNames"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "TrustedPosixOffset"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_TRUSTED_DOMAINS = NETLOGON_DELTA_TRUSTED_DOMAINS

class NETLOGON_DELTA_ACCOUNTS(NdrStructure):
    MEMBERS = [(ULONG, "PrivilegeEntries"),(ULONG, "PrivilegeControl"),(PULONG, "PrivilegeAttributes"),(PRPC_UNICODE_STRING, "PrivilegeNames"),(NLPR_QUOTA_LIMITS, "QuotaLimits"),(ULONG, "SystemAccessFlags"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_ACCOUNTS = NETLOGON_DELTA_ACCOUNTS

class NETLOGON_DELTA_SECRET(NdrStructure):
    MEMBERS = [(NLPR_CR_CIPHER_VALUE, "CurrentValue"),(OLD_LARGE_INTEGER, "CurrentValueSetTime"),(NLPR_CR_CIPHER_VALUE, "OldValue"),(OLD_LARGE_INTEGER, "OldValueSetTime"),(SECURITY_INFORMATION, "SecurityInformation"),(ULONG, "SecuritySize"),(PUCHAR, "SecurityDescriptor"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_SECRET = NETLOGON_DELTA_SECRET

class NETLOGON_DELTA_DELETE_GROUP(NdrStructure):
    MEMBERS = [(PWCHAR_T, "AccountName"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_DELETE_GROUP = NETLOGON_DELTA_DELETE_GROUP

class NETLOGON_DELTA_DELETE_USER(NdrStructure):
    MEMBERS = [(PWCHAR_T, "AccountName"),(RPC_UNICODE_STRING, "DummyString1"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DELTA_DELETE_USER = NETLOGON_DELTA_DELETE_USER

class NETLOGON_DELTA_TYPE(NdrEnum):
    MAP = ((1 , 'AddOrChangeDomain'),(2 , 'AddOrChangeGroup'),(3 , 'DeleteGroup'),(4 , 'RenameGroup'),(5 , 'AddOrChangeUser'),(6 , 'DeleteUser'),(7 , 'RenameUser'),(8 , 'ChangeGroupMembership'),(9 , 'AddOrChangeAlias'),(10 , 'DeleteAlias'),(11 , 'RenameAlias'),(12 , 'ChangeAliasMembership'),(13 , 'AddOrChangeLsaPolicy'),(14 , 'AddOrChangeLsaTDomain'),(15 , 'DeleteLsaTDomain'),(16 , 'AddOrChangeLsaAccount'),(17 , 'DeleteLsaAccount'),(18 , 'AddOrChangeLsaSecret'),(19 , 'DeleteLsaSecret'),(20 , 'DeleteGroupByName'),(21 , 'DeleteUserByName'),(22 , 'SerialNumberSkip'),)        

class NETLOGON_DELTA_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_DELTA_DOMAIN, "DeltaDomain"),2 : (PNETLOGON_DELTA_GROUP, "DeltaGroup"),3 : (PNETLOGON_DELTA_RENAME_GROUP, "DeltaRenameGroup"),4 : (PNETLOGON_DELTA_USER, "DeltaUser"),5 : (PNETLOGON_DELTA_RENAME_USER, "DeltaRenameUser"),6 : (PNETLOGON_DELTA_GROUP_MEMBER, "DeltaGroupMember"),7 : (PNETLOGON_DELTA_ALIAS, "DeltaAlias"),8 : (PNETLOGON_DELTA_RENAME_ALIAS, "DeltaRenameAlias"),9 : (PNETLOGON_DELTA_ALIAS_MEMBER, "DeltaAliasMember"),10 : (PNETLOGON_DELTA_POLICY, "DeltaPolicy"),11 : (PNETLOGON_DELTA_TRUSTED_DOMAINS, "DeltaTDomains"),12 : (PNETLOGON_DELTA_ACCOUNTS, "DeltaAccounts"),13 : (PNETLOGON_DELTA_SECRET, "DeltaSecret"),14 : (PNETLOGON_DELTA_DELETE_GROUP, "DeltaDeleteGroup"),15 : (PNETLOGON_DELTA_DELETE_USER, "DeltaDeleteUser"),16 : (PNLPR_MODIFIED_COUNT, "DeltaSerialNumberSkip"),}

    
PNETLOGON_DELTA_UNION = NETLOGON_DELTA_UNION

class NETLOGON_DELTA_ID_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ULONG, "Rid"),2 : (PRPC_SID, "Sid"),3 : (PWCHAR_T, "Name"),}

    
PNETLOGON_DELTA_ID_UNION = NETLOGON_DELTA_ID_UNION

class NETLOGON_DELTA_ENUM(NdrStructure):
    MEMBERS = [(NETLOGON_DELTA_TYPE, "DeltaType"),(NETLOGON_DELTA_ID_UNION, "DeltaID"),(NETLOGON_DELTA_UNION, "DeltaUnion"),]

    
PNETLOGON_DELTA_ENUM = NETLOGON_DELTA_ENUM

class NETLOGON_DELTA_ENUM_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "CountReturned"),(PNETLOGON_DELTA_ENUM, "Deltas"),]

    
PNETLOGON_DELTA_ENUM_ARRAY = NETLOGON_DELTA_ENUM_ARRAY

class NETLOGON_LOGON_IDENTITY_INFO(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "LogonDomainName"),(ULONG, "ParameterControl"),(OLD_LARGE_INTEGER, "Reserved"),(RPC_UNICODE_STRING, "UserName"),(RPC_UNICODE_STRING, "Workstation"),]

    
PNETLOGON_LOGON_IDENTITY_INFO = NETLOGON_LOGON_IDENTITY_INFO

class NETLOGON_INTERACTIVE_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_LOGON_IDENTITY_INFO, "Identity"),(LM_OWF_PASSWORD, "LmOwfPassword"),(NT_OWF_PASSWORD, "NtOwfPassword"),]

    
PNETLOGON_INTERACTIVE_INFO = NETLOGON_INTERACTIVE_INFO

class NETLOGON_LOGON_INFO_CLASS(NdrEnum):
    MAP = ((1 , 'NetlogonInteractiveInformation'),(2 , 'NetlogonNetworkInformation'),(3 , 'NetlogonServiceInformation'),(4 , 'NetlogonGenericInformation'),(5 , 'NetlogonInteractiveTransitiveInformation'),(6 , 'NetlogonNetworkTransitiveInformation'),(7 , 'NetlogonServiceTransitiveInformation'),)        

class NETLOGON_SERVICE_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_LOGON_IDENTITY_INFO, "Identity"),(LM_OWF_PASSWORD, "LmOwfPassword"),(NT_OWF_PASSWORD, "NtOwfPassword"),]

    
PNETLOGON_SERVICE_INFO = NETLOGON_SERVICE_INFO

class LM_CHALLENGE(NdrStructure):
    MEMBERS = [(CHAR, "data"),]

    

class NETLOGON_NETWORK_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_LOGON_IDENTITY_INFO, "Identity"),(LM_CHALLENGE, "LmChallenge"),(STRING, "NtChallengeResponse"),(STRING, "LmChallengeResponse"),]

    
PNETLOGON_NETWORK_INFO = NETLOGON_NETWORK_INFO

class NETLOGON_GENERIC_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_LOGON_IDENTITY_INFO, "Identity"),(RPC_UNICODE_STRING, "PackageName"),(ULONG, "DataLength"),(PUCHAR, "LogonData"),]

    
PNETLOGON_GENERIC_INFO = NETLOGON_GENERIC_INFO

class NETLOGON_LEVEL(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_INTERACTIVE_INFO, "LogonInteractive"),2 : (PNETLOGON_INTERACTIVE_INFO, "LogonInteractiveTransitive"),3 : (PNETLOGON_SERVICE_INFO, "LogonService"),4 : (PNETLOGON_SERVICE_INFO, "LogonServiceTransitive"),5 : (PNETLOGON_NETWORK_INFO, "LogonNetwork"),6 : (PNETLOGON_NETWORK_INFO, "LogonNetworkTransitive"),7 : (PNETLOGON_GENERIC_INFO, "LogonGeneric"),}

    
PNETLOGON_LEVEL = NETLOGON_LEVEL

class NETLOGON_VALIDATION_INFO_CLASS(NdrEnum):
    MAP = ((1 , 'NetlogonValidationUasInfo'),(2 , 'NetlogonValidationSamInfo'),(3 , 'NetlogonValidationSamInfo2'),(4 , 'NetlogonValidationGenericInfo'),(5 , 'NetlogonValidationGenericInfo2'),(6 , 'NetlogonValidationSamInfo4'),)        

class GROUP_MEMBERSHIP(NdrStructure):
    MEMBERS = [(ULONG, "RelativeId"),(ULONG, "Attributes"),]

    
PGROUP_MEMBERSHIP = GROUP_MEMBERSHIP

class USER_SESSION_KEY(NdrStructure):
    MEMBERS = [(CYPHER_BLOCK, "data"),]

    
PUSER_SESSION_KEY = USER_SESSION_KEY

class NETLOGON_SID_AND_ATTRIBUTES(NdrStructure):
    MEMBERS = [(PRPC_SID, "Sid"),(ULONG, "Attributes"),]

    
PNETLOGON_SID_AND_ATTRIBUTES = NETLOGON_SID_AND_ATTRIBUTES

class NETLOGON_VALIDATION_SAM_INFO(NdrStructure):
    MEMBERS = [(OLD_LARGE_INTEGER, "LogonTime"),(OLD_LARGE_INTEGER, "LogoffTime"),(OLD_LARGE_INTEGER, "KickOffTime"),(OLD_LARGE_INTEGER, "PasswordLastSet"),(OLD_LARGE_INTEGER, "PasswordCanChange"),(OLD_LARGE_INTEGER, "PasswordMustChange"),(RPC_UNICODE_STRING, "EffectiveName"),(RPC_UNICODE_STRING, "FullName"),(RPC_UNICODE_STRING, "LogonScript"),(RPC_UNICODE_STRING, "ProfilePath"),(RPC_UNICODE_STRING, "HomeDirectory"),(RPC_UNICODE_STRING, "HomeDirectoryDrive"),(USHORT, "LogonCount"),(USHORT, "BadPasswordCount"),(ULONG, "UserId"),(ULONG, "PrimaryGroupId"),(ULONG, "GroupCount"),(PGROUP_MEMBERSHIP, "GroupIds"),(ULONG, "UserFlags"),(USER_SESSION_KEY, "UserSessionKey"),(RPC_UNICODE_STRING, "LogonServer"),(RPC_UNICODE_STRING, "LogonDomainName"),(PRPC_SID, "LogonDomainId"),(ULONG, "ExpansionRoom"),]

    
PNETLOGON_VALIDATION_SAM_INFO = NETLOGON_VALIDATION_SAM_INFO

class NETLOGON_VALIDATION_SAM_INFO2(NdrStructure):
    MEMBERS = [(OLD_LARGE_INTEGER, "LogonTime"),(OLD_LARGE_INTEGER, "LogoffTime"),(OLD_LARGE_INTEGER, "KickOffTime"),(OLD_LARGE_INTEGER, "PasswordLastSet"),(OLD_LARGE_INTEGER, "PasswordCanChange"),(OLD_LARGE_INTEGER, "PasswordMustChange"),(RPC_UNICODE_STRING, "EffectiveName"),(RPC_UNICODE_STRING, "FullName"),(RPC_UNICODE_STRING, "LogonScript"),(RPC_UNICODE_STRING, "ProfilePath"),(RPC_UNICODE_STRING, "HomeDirectory"),(RPC_UNICODE_STRING, "HomeDirectoryDrive"),(USHORT, "LogonCount"),(USHORT, "BadPasswordCount"),(ULONG, "UserId"),(ULONG, "PrimaryGroupId"),(ULONG, "GroupCount"),(PGROUP_MEMBERSHIP, "GroupIds"),(ULONG, "UserFlags"),(USER_SESSION_KEY, "UserSessionKey"),(RPC_UNICODE_STRING, "LogonServer"),(RPC_UNICODE_STRING, "LogonDomainName"),(PRPC_SID, "LogonDomainId"),(ULONG, "ExpansionRoom"),(ULONG, "SidCount"),(PNETLOGON_SID_AND_ATTRIBUTES, "ExtraSids"),]

    
PNETLOGON_VALIDATION_SAM_INFO2 = NETLOGON_VALIDATION_SAM_INFO2

class NETLOGON_VALIDATION_GENERIC_INFO2(NdrStructure):
    MEMBERS = [(ULONG, "DataLength"),(PUCHAR, "ValidationData"),]

    
PNETLOGON_VALIDATION_GENERIC_INFO2 = NETLOGON_VALIDATION_GENERIC_INFO2

class NETLOGON_VALIDATION_SAM_INFO4(NdrStructure):
    MEMBERS = [(OLD_LARGE_INTEGER, "LogonTime"),(OLD_LARGE_INTEGER, "LogoffTime"),(OLD_LARGE_INTEGER, "KickOffTime"),(OLD_LARGE_INTEGER, "PasswordLastSet"),(OLD_LARGE_INTEGER, "PasswordCanChange"),(OLD_LARGE_INTEGER, "PasswordMustChange"),(RPC_UNICODE_STRING, "EffectiveName"),(RPC_UNICODE_STRING, "FullName"),(RPC_UNICODE_STRING, "LogonScript"),(RPC_UNICODE_STRING, "ProfilePath"),(RPC_UNICODE_STRING, "HomeDirectory"),(RPC_UNICODE_STRING, "HomeDirectoryDrive"),(UNSIGNED_SHORT, "LogonCount"),(UNSIGNED_SHORT, "BadPasswordCount"),(UNSIGNED_LONG, "UserId"),(UNSIGNED_LONG, "PrimaryGroupId"),(UNSIGNED_LONG, "GroupCount"),(PGROUP_MEMBERSHIP, "GroupIds"),(UNSIGNED_LONG, "UserFlags"),(USER_SESSION_KEY, "UserSessionKey"),(RPC_UNICODE_STRING, "LogonServer"),(RPC_UNICODE_STRING, "LogonDomainName"),(PRPC_SID, "LogonDomainId"),(UNSIGNED_CHAR, "LMKey"),(ULONG, "UserAccountControl"),(ULONG, "SubAuthStatus"),(OLD_LARGE_INTEGER, "LastSuccessfulILogon"),(OLD_LARGE_INTEGER, "LastFailedILogon"),(ULONG, "FailedILogonCount"),(ULONG, "Reserved4"),(UNSIGNED_LONG, "SidCount"),(PNETLOGON_SID_AND_ATTRIBUTES, "ExtraSids"),(RPC_UNICODE_STRING, "DnsLogonDomainName"),(RPC_UNICODE_STRING, "Upn"),(RPC_UNICODE_STRING, "ExpansionString1"),(RPC_UNICODE_STRING, "ExpansionString2"),(RPC_UNICODE_STRING, "ExpansionString3"),(RPC_UNICODE_STRING, "ExpansionString4"),(RPC_UNICODE_STRING, "ExpansionString5"),(RPC_UNICODE_STRING, "ExpansionString6"),(RPC_UNICODE_STRING, "ExpansionString7"),(RPC_UNICODE_STRING, "ExpansionString8"),(RPC_UNICODE_STRING, "ExpansionString9"),(RPC_UNICODE_STRING, "ExpansionString10"),]

    
PNETLOGON_VALIDATION_SAM_INFO4 = NETLOGON_VALIDATION_SAM_INFO4

class NETLOGON_VALIDATION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_VALIDATION_SAM_INFO, "ValidationSam"),2 : (PNETLOGON_VALIDATION_SAM_INFO2, "ValidationSam2"),3 : (PNETLOGON_VALIDATION_GENERIC_INFO2, "ValidationGeneric2"),4 : (PNETLOGON_VALIDATION_SAM_INFO4, "ValidationSam4"),}

    
PNETLOGON_VALIDATION = NETLOGON_VALIDATION

class NETLOGON_CONTROL_DATA_INFORMATION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PWCHAR_T, "TrustedDomainName"),2 : (DWORD, "DebugFlag"),3 : (PWCHAR_T, "UserName"),}

    
PNETLOGON_CONTROL_DATA_INFORMATION = NETLOGON_CONTROL_DATA_INFORMATION

class NETLOGON_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "netlog1_flags"),(NET_API_STATUS, "netlog1_pdc_connection_status"),]

    
PNETLOGON_INFO_1 = NETLOGON_INFO_1

class NETLOGON_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "netlog2_flags"),(NET_API_STATUS, "netlog2_pdc_connection_status"),(PWCHAR_T, "netlog2_trusted_dc_name"),(NET_API_STATUS, "netlog2_tc_connection_status"),]

    
PNETLOGON_INFO_2 = NETLOGON_INFO_2

class NETLOGON_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "netlog3_flags"),(DWORD, "netlog3_logon_attempts"),(DWORD, "netlog3_reserved1"),(DWORD, "netlog3_reserved2"),(DWORD, "netlog3_reserved3"),(DWORD, "netlog3_reserved4"),(DWORD, "netlog3_reserved5"),]

    
PNETLOGON_INFO_3 = NETLOGON_INFO_3

class NETLOGON_INFO_4(NdrStructure):
    MEMBERS = [(PWCHAR_T, "netlog4_trusted_dc_name"),(PWCHAR_T, "netlog4_trusted_domain_name"),]

    
PNETLOGON_INFO_4 = NETLOGON_INFO_4

class NETLOGON_CONTROL_QUERY_INFORMATION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_INFO_1, "NetlogonInfo1"),2 : (PNETLOGON_INFO_2, "NetlogonInfo2"),3 : (PNETLOGON_INFO_3, "NetlogonInfo3"),4 : (PNETLOGON_INFO_4, "NetlogonInfo4"),}

    
PNETLOGON_CONTROL_QUERY_INFORMATION = NETLOGON_CONTROL_QUERY_INFORMATION

class SYNC_STATE(NdrEnum):
    MAP = ((0 , 'NormalState'),(1 , 'DomainState'),(2 , 'GroupState'),(3 , 'UasBuiltInGroupState'),(4 , 'UserState'),(5 , 'GroupMemberState'),(6 , 'AliasState'),(7 , 'AliasMemberState'),(8 , 'SamDoneState'),)        

class DOMAIN_NAME_BUFFER(NdrStructure):
    MEMBERS = [(ULONG, "DomainNameByteCount"),(PUCHAR, "DomainNames"),]

    
PDOMAIN_NAME_BUFFER = DOMAIN_NAME_BUFFER

class NETLOGON_LSA_POLICY_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LsaPolicySize"),(PUCHAR, "LsaPolicy"),]

    
PNETLOGON_LSA_POLICY_INFO = NETLOGON_LSA_POLICY_INFO

class NETLOGON_ONE_DOMAIN_INFO(NdrStructure):
    MEMBERS = [(RPC_UNICODE_STRING, "DomainName"),(RPC_UNICODE_STRING, "DnsDomainName"),(RPC_UNICODE_STRING, "DnsForestName"),(GUID, "DomainGuid"),(PRPC_SID, "DomainSid"),(RPC_UNICODE_STRING, "TrustExtension"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "DummyLong1"),(ULONG, "DummyLong2"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_ONE_DOMAIN_INFO = NETLOGON_ONE_DOMAIN_INFO

class NETLOGON_DOMAIN_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_ONE_DOMAIN_INFO, "PrimaryDomain"),(ULONG, "TrustedDomainCount"),(PNETLOGON_ONE_DOMAIN_INFO, "TrustedDomains"),(NETLOGON_LSA_POLICY_INFO, "LsaPolicy"),(RPC_UNICODE_STRING, "DnsHostNameInDs"),(RPC_UNICODE_STRING, "DummyString2"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "WorkstationFlags"),(ULONG, "SupportedEncTypes"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_DOMAIN_INFO = NETLOGON_DOMAIN_INFO

class NETLOGON_DOMAIN_INFORMATION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_DOMAIN_INFO, "DomainInfo"),2 : (PNETLOGON_LSA_POLICY_INFO, "LsaPolicyInfo"),}

    
PNETLOGON_DOMAIN_INFORMATION = NETLOGON_DOMAIN_INFORMATION

class NETLOGON_WORKSTATION_INFO(NdrStructure):
    MEMBERS = [(NETLOGON_LSA_POLICY_INFO, "LsaPolicy"),(PWCHAR_T, "DnsHostName"),(PWCHAR_T, "SiteName"),(PWCHAR_T, "Dummy1"),(PWCHAR_T, "Dummy2"),(PWCHAR_T, "Dummy3"),(PWCHAR_T, "Dummy4"),(RPC_UNICODE_STRING, "OsVersion"),(RPC_UNICODE_STRING, "OsName"),(RPC_UNICODE_STRING, "DummyString3"),(RPC_UNICODE_STRING, "DummyString4"),(ULONG, "WorkstationFlags"),(ULONG, "KerberosSupportedEncryptionTypes"),(ULONG, "DummyLong3"),(ULONG, "DummyLong4"),]

    
PNETLOGON_WORKSTATION_INFO = NETLOGON_WORKSTATION_INFO

class NETLOGON_WORKSTATION_INFORMATION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PNETLOGON_WORKSTATION_INFO, "WorkstationInfo"),2 : (PNETLOGON_WORKSTATION_INFO, "LsaPolicyInfo"),}

    
PNETLOGON_WORKSTATION_INFORMATION = NETLOGON_WORKSTATION_INFORMATION

class NL_SOCKET_ADDRESS(NdrStructure):
    MEMBERS = [(PUCHAR, "lpSockaddr"),(ULONG, "iSockaddrLength"),]

    
PNL_SOCKET_ADDRESS = NL_SOCKET_ADDRESS

class NL_SITE_NAME_ARRAY(NdrStructure):
    MEMBERS = [(ULONG, "EntryCount"),(PRPC_UNICODE_STRING, "SiteNames"),]

    
PNL_SITE_NAME_ARRAY = NL_SITE_NAME_ARRAY

class DS_DOMAIN_TRUSTSW(NdrStructure):
    MEMBERS = [(PWCHAR_T, "NetbiosDomainName"),(PWCHAR_T, "DnsDomainName"),(ULONG, "Flags"),(ULONG, "ParentIndex"),(ULONG, "TrustType"),(ULONG, "TrustAttributes"),(PRPC_SID, "DomainSid"),(GUID, "DomainGuid"),]

    
PDS_DOMAIN_TRUSTSW = DS_DOMAIN_TRUSTSW

class NETLOGON_TRUSTED_DOMAIN_ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "DomainCount"),(PDS_DOMAIN_TRUSTSW, "Domains"),]

    
PNETLOGON_TRUSTED_DOMAIN_ARRAY = NETLOGON_TRUSTED_DOMAIN_ARRAY

class NL_SITE_NAME_EX_ARRAY(NdrStructure):
    MEMBERS = [(ULONG, "EntryCount"),(PRPC_UNICODE_STRING, "SiteNames"),(PRPC_UNICODE_STRING, "SubnetNames"),]

    
PNL_SITE_NAME_EX_ARRAY = NL_SITE_NAME_EX_ARRAY

class NL_GENERIC_RPC_DATA(NdrStructure):
    MEMBERS = [(ULONG, "UlongEntryCount"),(PULONG, "UlongData"),(ULONG, "UnicodeStringEntryCount"),(PRPC_UNICODE_STRING, "UnicodeStringData"),]

    
PNL_GENERIC_RPC_DATA = NL_GENERIC_RPC_DATA

class NETLOGON_VALIDATION_UAS_INFO(NdrStructure):
    MEMBERS = [(PWCHAR_T, "usrlog1_eff_name"),(DWORD, "usrlog1_priv"),(DWORD, "usrlog1_auth_flags"),(DWORD, "usrlog1_num_logons"),(DWORD, "usrlog1_bad_pw_count"),(DWORD, "usrlog1_last_logon"),(DWORD, "usrlog1_last_logoff"),(DWORD, "usrlog1_logoff_time"),(DWORD, "usrlog1_kickoff_time"),(DWORD, "usrlog1_password_age"),(DWORD, "usrlog1_pw_can_change"),(DWORD, "usrlog1_pw_must_change"),(PWCHAR_T, "usrlog1_computer"),(PWCHAR_T, "usrlog1_domain"),(PWCHAR_T, "usrlog1_script_path"),(DWORD, "usrlog1_reserved1"),]

    
PNETLOGON_VALIDATION_UAS_INFO = NETLOGON_VALIDATION_UAS_INFO

class NETLOGON_LOGOFF_UAS_INFO(NdrStructure):
    MEMBERS = [(DWORD, "Duration"),(USHORT, "LogonCount"),]

    
PNETLOGON_LOGOFF_UAS_INFO = NETLOGON_LOGOFF_UAS_INFO

class NETLOGON_CAPABILITIES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ULONG, "ServerCapabilities"),}

    
PNETLOGON_CAPABILITIES = NETLOGON_CAPABILITIES

class NETLOGON_CREDENTIAL(NdrStructure):
    MEMBERS = [(CHAR, "data"),]

    
PNETLOGON_CREDENTIAL = NETLOGON_CREDENTIAL

class NETLOGON_AUTHENTICATOR(NdrStructure):
    MEMBERS = [(NETLOGON_CREDENTIAL, "Credential"),(DWORD, "Timestamp"),]

    
PNETLOGON_AUTHENTICATOR = NETLOGON_AUTHENTICATOR

class NETLOGON_SECURE_CHANNEL_TYPE(NdrEnum):
    MAP = ((0 , 'NullSecureChannel'),(1 , 'MsvApSecureChannel'),(2 , 'WorkstationSecureChannel'),(3 , 'TrustedDnsDomainSecureChannel'),(4 , 'TrustedDomainSecureChannel'),(5 , 'UasServerSecureChannel'),(6 , 'ServerSecureChannel'),(7 , 'CdcServerSecureChannel'),)        

class UAS_INFO_0(NdrStructure):
    MEMBERS = [(CHAR, "ComputerName"),(ULONG, "TimeCreated"),(ULONG, "SerialNumber"),]

    
PUAS_INFO_0 = UAS_INFO_0

class DOMAIN_CONTROLLER_INFOW(NdrStructure):
    MEMBERS = [(PWCHAR_T, "DomainControllerName"),(PWCHAR_T, "DomainControllerAddress"),(ULONG, "DomainControllerAddressType"),(GUID, "DomainGuid"),(PWCHAR_T, "DomainName"),(PWCHAR_T, "DnsForestName"),(ULONG, "Flags"),(PWCHAR_T, "DcSiteName"),(PWCHAR_T, "ClientSiteName"),]

    
PDOMAIN_CONTROLLER_INFOW = DOMAIN_CONTROLLER_INFOW

class NL_TRUST_PASSWORD(NdrStructure):
    MEMBERS = [(WCHAR, "Buffer"),(ULONG, "Length"),]

    
PNL_TRUST_PASSWORD = NL_TRUST_PASSWORD

class NL_PASSWORD_VERSION(NdrStructure):
    MEMBERS = [(ULONG, "ReservedField"),(ULONG, "PasswordVersionNumber"),(ULONG, "PasswordVersionPresent"),]

    
PNL_PASSWORD_VERSION = NL_PASSWORD_VERSION

class LSA_FOREST_TRUST_RECORD_TYPE(NdrEnum):
    MAP = ((0 , 'ForestTrustTopLevelName'),(1 , 'ForestTrustTopLevelNameEx'),(2 , 'ForestTrustDomainInfo'),(ForestTrustDomainInfo , 'ForestTrustRecordTypeLast'),)        
LSA_RPC_UNICODE_STRING = RPC_UNICODE_STRING
PPLSA_RPC_UNICODE_STRING = RPC_UNICODE_STRING

class LSA_FOREST_TRUST_DOMAIN_INFO(NdrStructure):
    MEMBERS = [(PRPC_SID, "Sid"),(LSA_RPC_UNICODE_STRING, "DnsName"),(LSA_RPC_UNICODE_STRING, "NetbiosName"),]

    
PLSA_FOREST_TRUST_DOMAIN_INFO = LSA_FOREST_TRUST_DOMAIN_INFO

class LSA_FOREST_TRUST_BINARY_DATA(NdrStructure):
    MEMBERS = [(ULONG, "Length"),(PUCHAR, "Buffer"),]

    
PLSA_FOREST_TRUST_BINARY_DATA = LSA_FOREST_TRUST_BINARY_DATA

class LSA_FOREST_TRUST_RECORD(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),(LSA_FOREST_TRUST_RECORD_TYPE, "ForestTrustType"),(LARGE_INTEGER, "Time"),(FORESTTRUSTDATA, "ForestTrustData"),]

    
PLSA_FOREST_TRUST_RECORD = LSA_FOREST_TRUST_RECORD

class LSA_FOREST_TRUST_INFORMATION(NdrStructure):
    MEMBERS = [(ULONG, "RecordCount"),(PPLSA_FOREST_TRUST_RECORD, "Entries"),]

    
PLSA_FOREST_TRUST_INFORMATION = LSA_FOREST_TRUST_INFORMATION

class NL_DNS_NAME_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Type"),(PWCHAR_T, "DnsDomainInfo"),(ULONG, "DnsDomainInfoType"),(ULONG, "Priority"),(ULONG, "Weight"),(ULONG, "Port"),(UCHAR, "Register"),(ULONG, "Status"),]

    
PNL_DNS_NAME_INFO = NL_DNS_NAME_INFO

class NL_DNS_NAME_INFO_ARRAY(NdrStructure):
    MEMBERS = [(ULONG, "EntryCount"),(PNL_DNS_NAME_INFO, "DnsNamesInfo"),]

    
PNL_DNS_NAME_INFO_ARRAY = NL_DNS_NAME_INFO_ARRAY

class NL_OSVERSIONINFO_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwOSVersionInfoSize"),(DWORD, "dwMajorVersion"),(DWORD, "dwMinorVersion"),(DWORD, "dwBuildNumber"),(DWORD, "dwPlatformId"),(WCHAR_T, "szCSDVersion"),(USHORT, "wServicePackMajor"),(USHORT, "wServicePackMinor"),(USHORT, "wSuiteMask"),(UCHAR, "wProductType"),(UCHAR, "wReserved"),]

    

class NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES_V1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "ClientDnsHostName"),(PNL_OSVERSIONINFO_V1, "OsVersionInfo_V1"),(PWCHAR_T, "OsName"),]

    

class NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES_V1, "V1"),}

    

class NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES_V1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "HubName"),(PPWCHAR_T, "OldDnsHostName"),(PULONG, "SupportedEncTypes"),]

    

class NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES_V1, "V1"),}

    
Interface("12345678-1234-ABCD-EF00-01234567CFFB", "1.0",[Method("NetrLogonUasLogon",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'UserName')),
In((PWCHAR_T,'Workstation')),
Out((PPNETLOGON_VALIDATION_UAS_INFO,'ValidationInformation')),
),Method("NetrLogonUasLogoff",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'UserName')),
In((PWCHAR_T,'Workstation')),
Out((PNETLOGON_LOGOFF_UAS_INFO,'LogoffInformation')),
),Method("NetrLogonSamLogon",
In((LOGONSRV_HANDLE,'LogonServer')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((NETLOGON_LOGON_INFO_CLASS,'LogonLevel')),
In((PNETLOGON_LEVEL,'LogonInformation')),
In((NETLOGON_VALIDATION_INFO_CLASS,'ValidationLevel')),
Out((PNETLOGON_VALIDATION,'ValidationInformation')),
Out((PUCHAR,'Authoritative')),
),Method("NetrLogonSamLogoff",
In((LOGONSRV_HANDLE,'LogonServer')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((NETLOGON_LOGON_INFO_CLASS,'LogonLevel')),
In((PNETLOGON_LEVEL,'LogonInformation')),
),Method("NetrServerReqChallenge",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_CREDENTIAL,'ClientChallenge')),
Out((PNETLOGON_CREDENTIAL,'ServerChallenge')),
),Method("NetrServerAuthenticate",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_CREDENTIAL,'ClientCredential')),
Out((PNETLOGON_CREDENTIAL,'ServerCredential')),
),Method("NetrServerPasswordSet",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PENCRYPTED_NT_OWF_PASSWORD,'UasNewPassword')),
),Method("NetrDatabaseDeltas",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'DatabaseID')),
InOut((PNLPR_MODIFIED_COUNT,'DomainModifiedCount')),
Out((PPNETLOGON_DELTA_ENUM_ARRAY,'DeltaArray')),
In((DWORD,'PreferredMaximumLength')),
),Method("NetrDatabaseSync",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'DatabaseID')),
InOut((PULONG,'SyncContext')),
Out((PPNETLOGON_DELTA_ENUM_ARRAY,'DeltaArray')),
In((DWORD,'PreferredMaximumLength')),
),Method("NetrAccountDeltas",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PUAS_INFO_0,'RecordId')),
In((DWORD,'Count')),
In((DWORD,'Level')),
Out((PUCHAR,'Buffer')),
In((DWORD,'BufferSize')),
Out((PULONG,'CountReturned')),
Out((PULONG,'TotalEntries')),
Out((PUAS_INFO_0,'NextRecordId')),
),Method("NetrAccountSync",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'Reference')),
In((DWORD,'Level')),
Out((PUCHAR,'Buffer')),
In((DWORD,'BufferSize')),
Out((PULONG,'CountReturned')),
Out((PULONG,'TotalEntries')),
Out((PULONG,'NextReference')),
Out((PUAS_INFO_0,'LastRecordId')),
),Method("NetrGetDCName",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'DomainName')),
Out((PPWCHAR_T,'Buffer')),
),Method("NetrLogonControl",
In((LOGONSRV_HANDLE,'ServerName')),
In((DWORD,'FunctionCode')),
In((DWORD,'QueryLevel')),
Out((PNETLOGON_CONTROL_QUERY_INFORMATION,'Buffer')),
),Method("NetrGetAnyDCName",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'DomainName')),
Out((PPWCHAR_T,'Buffer')),
),Method("NetrLogonControl2",
In((LOGONSRV_HANDLE,'ServerName')),
In((DWORD,'FunctionCode')),
In((DWORD,'QueryLevel')),
In((PNETLOGON_CONTROL_DATA_INFORMATION,'Data')),
Out((PNETLOGON_CONTROL_QUERY_INFORMATION,'Buffer')),
),Method("NetrServerAuthenticate2",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_CREDENTIAL,'ClientCredential')),
Out((PNETLOGON_CREDENTIAL,'ServerCredential')),
InOut((PULONG,'NegotiateFlags')),
),Method("NetrDatabaseSync2",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'DatabaseID')),
In((SYNC_STATE,'RestartState')),
InOut((PULONG,'SyncContext')),
Out((PPNETLOGON_DELTA_ENUM_ARRAY,'DeltaArray')),
In((DWORD,'PreferredMaximumLength')),
),Method("NetrDatabaseRedo",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PUCHAR,'ChangeLogEntry')),
In((DWORD,'ChangeLogEntrySize')),
Out((PPNETLOGON_DELTA_ENUM_ARRAY,'DeltaArray')),
),Method("NetrLogonControl2Ex",
In((LOGONSRV_HANDLE,'ServerName')),
In((DWORD,'FunctionCode')),
In((DWORD,'QueryLevel')),
In((PNETLOGON_CONTROL_DATA_INFORMATION,'Data')),
Out((PNETLOGON_CONTROL_QUERY_INFORMATION,'Buffer')),
),Method("NetrEnumerateTrustedDomains",
In((LOGONSRV_HANDLE,'ServerName')),
Out((PDOMAIN_NAME_BUFFER,'DomainNameBuffer')),
),Method("DsrGetDcName",
In((LOGONSRV_HANDLE,'ComputerName')),
In((PWCHAR_T,'DomainName')),
In((PGUID,'DomainGuid')),
In((PGUID,'SiteGuid')),
In((ULONG,'Flags')),
Out((PPDOMAIN_CONTROLLER_INFOW,'DomainControllerInfo')),
),Method("NetrLogonGetCapabilities",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'QueryLevel')),
Out((PNETLOGON_CAPABILITIES,'ServerCapabilities')),
),Method("NetrLogonSetServiceBits",
In((LOGONSRV_HANDLE,'ServerName')),
In((DWORD,'ServiceBitsOfInterest')),
In((DWORD,'ServiceBits')),
),Method("NetrLogonGetTrustRid",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'DomainName')),
Out((PULONG,'Rid')),
),Method("NetrLogonComputeServerDigest",
In((LOGONSRV_HANDLE,'ServerName')),
In((ULONG,'Rid')),
In((PUCHAR,'Message')),
In((ULONG,'MessageSize')),
Out((CHAR,'NewMessageDigest')),
Out((CHAR,'OldMessageDigest')),
),Method("NetrLogonComputeClientDigest",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'DomainName')),
In((PUCHAR,'Message')),
In((ULONG,'MessageSize')),
Out((CHAR,'NewMessageDigest')),
Out((CHAR,'OldMessageDigest')),
),Method("NetrServerAuthenticate3",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_CREDENTIAL,'ClientCredential')),
Out((PNETLOGON_CREDENTIAL,'ServerCredential')),
InOut((PULONG,'NegotiateFlags')),
Out((PULONG,'AccountRid')),
),Method("DsrGetDcNameEx",
In((LOGONSRV_HANDLE,'ComputerName')),
In((PWCHAR_T,'DomainName')),
In((PGUID,'DomainGuid')),
In((PWCHAR_T,'SiteName')),
In((ULONG,'Flags')),
Out((PPDOMAIN_CONTROLLER_INFOW,'DomainControllerInfo')),
),Method("DsrGetSiteName",
In((LOGONSRV_HANDLE,'ComputerName')),
Out((PPWCHAR_T,'SiteName')),
),Method("NetrLogonGetDomainInfo",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'Level')),
In((PNETLOGON_WORKSTATION_INFORMATION,'WkstaBuffer')),
Out((PNETLOGON_DOMAIN_INFORMATION,'DomBuffer')),
),Method("NetrServerPasswordSet2",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PNL_TRUST_PASSWORD,'ClearNewPassword')),
),Method("NetrServerPasswordGet",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'AccountType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
Out((PENCRYPTED_NT_OWF_PASSWORD,'EncryptedNtOwfPassword')),
),Method("NetrLogonSendToSam",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PUCHAR,'OpaqueBuffer')),
In((ULONG,'OpaqueBufferSize')),
),Method("DsrAddressToSiteNamesW",
In((LOGONSRV_HANDLE,'ComputerName')),
In((DWORD,'EntryCount')),
In((PNL_SOCKET_ADDRESS,'SocketAddresses')),
Out((PPNL_SITE_NAME_ARRAY,'SiteNames')),
),Method("DsrGetDcNameEx2",
In((LOGONSRV_HANDLE,'ComputerName')),
In((PWCHAR_T,'AccountName')),
In((ULONG,'AllowableAccountControlBits')),
In((PWCHAR_T,'DomainName')),
In((PGUID,'DomainGuid')),
In((PWCHAR_T,'SiteName')),
In((ULONG,'Flags')),
Out((PPDOMAIN_CONTROLLER_INFOW,'DomainControllerInfo')),
),Method("NetrLogonGetTimeServiceParentDomain",
In((LOGONSRV_HANDLE,'ServerName')),
Out((PPWCHAR_T,'DomainName')),
Out((PINT,'PdcSameSite')),
),Method("NetrEnumerateTrustedDomainsEx",
In((LOGONSRV_HANDLE,'ServerName')),
Out((PNETLOGON_TRUSTED_DOMAIN_ARRAY,'Domains')),
),Method("DsrAddressToSiteNamesExW",
In((LOGONSRV_HANDLE,'ComputerName')),
In((DWORD,'EntryCount')),
In((PNL_SOCKET_ADDRESS,'SocketAddresses')),
Out((PPNL_SITE_NAME_EX_ARRAY,'SiteNames')),
),Method("DsrGetDcSiteCoverageW",
In((LOGONSRV_HANDLE,'ServerName')),
Out((PPNL_SITE_NAME_ARRAY,'SiteNames')),
),Method("NetrLogonSamLogonEx",
In((HANDLE_T,'ContextHandle')),
In((PWCHAR_T,'LogonServer')),
In((PWCHAR_T,'ComputerName')),
In((NETLOGON_LOGON_INFO_CLASS,'LogonLevel')),
In((PNETLOGON_LEVEL,'LogonInformation')),
In((NETLOGON_VALIDATION_INFO_CLASS,'ValidationLevel')),
Out((PNETLOGON_VALIDATION,'ValidationInformation')),
Out((PUCHAR,'Authoritative')),
InOut((PULONG,'ExtraFlags')),
),Method("DsrEnumerateDomainTrusts",
In((LOGONSRV_HANDLE,'ServerName')),
In((ULONG,'Flags')),
Out((PNETLOGON_TRUSTED_DOMAIN_ARRAY,'Domains')),
),Method("DsrDeregisterDnsHostRecords",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'DnsDomainName')),
In((PGUID,'DomainGuid')),
In((PGUID,'DsaGuid')),
In((PWCHAR_T,'DnsHostName')),
),Method("NetrServerTrustPasswordsGet",
In((LOGONSRV_HANDLE,'TrustedDcName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
Out((PENCRYPTED_NT_OWF_PASSWORD,'EncryptedNewOwfPassword')),
Out((PENCRYPTED_NT_OWF_PASSWORD,'EncryptedOldOwfPassword')),
),Method("DsrGetForestTrustInformation",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'TrustedDomainName')),
In((DWORD,'Flags')),
Out((PPLSA_FOREST_TRUST_INFORMATION,'ForestTrustInfo')),
),Method("NetrGetForestTrustInformation",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'Flags')),
Out((PPLSA_FOREST_TRUST_INFORMATION,'ForestTrustInfo')),
),Method("NetrLogonSamLogonWithFlags",
In((LOGONSRV_HANDLE,'LogonServer')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((NETLOGON_LOGON_INFO_CLASS,'LogonLevel')),
In((PNETLOGON_LEVEL,'LogonInformation')),
In((NETLOGON_VALIDATION_INFO_CLASS,'ValidationLevel')),
Out((PNETLOGON_VALIDATION,'ValidationInformation')),
Out((PUCHAR,'Authoritative')),
InOut((PULONG,'ExtraFlags')),
),Method("NetrServerGetTrustInfo",
In((LOGONSRV_HANDLE,'TrustedDcName')),
In((PWCHAR_T,'AccountName')),
In((NETLOGON_SECURE_CHANNEL_TYPE,'SecureChannelType')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
Out((PENCRYPTED_NT_OWF_PASSWORD,'EncryptedNewOwfPassword')),
Out((PENCRYPTED_NT_OWF_PASSWORD,'EncryptedOldOwfPassword')),
Out((PPNL_GENERIC_RPC_DATA,'TrustInfo')),
),Method("OpnumUnused47",
),Method("DsrUpdateReadOnlyServerDnsRecords",
In((LOGONSRV_HANDLE,'ServerName')),
In((PWCHAR_T,'ComputerName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
Out((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((PWCHAR_T,'SiteName')),
In((ULONG,'DnsTtl')),
InOut((PNL_DNS_NAME_INFO_ARRAY,'DnsNames')),
),Method("NetrChainSetClientAttributes",
In((LOGONSRV_HANDLE,'PrimaryName')),
In((PWCHAR_T,'ChainedFromServerName')),
In((PWCHAR_T,'ChainedForClientName')),
In((PNETLOGON_AUTHENTICATOR,'Authenticator')),
InOut((PNETLOGON_AUTHENTICATOR,'ReturnAuthenticator')),
In((DWORD,'dwInVersion')),
In((PNL_IN_CHAIN_SET_CLIENT_ATTRIBUTES,'pmsgIn')),
InOut((PDWORD,'pdwOutVersion')),
InOut((PNL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES,'pmsgOut')),
),])