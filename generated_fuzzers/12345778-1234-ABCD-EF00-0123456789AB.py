
from fuzzer.midl import *
from fuzzer.core import *
import .server
BYTE = NdrByte
USHORT = NdrShort
UCHAR = NdrByte
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
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
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
INT = NdrLong
VOID = CONTEXT_HANDLE
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

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
PFILETIME = FILETIMELPFILETIME = FILETIME
class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    
UUID = GUIDPGUID = GUID
class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    
PLARGE_INTEGER = LARGE_INTEGER
class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    
PEVENT_DESCRIPTOR = EVENT_DESCRIPTORPCEVENT_DESCRIPTOR = EVENT_DESCRIPTOR
class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    
PEVENT_HEADER = EVENT_HEADER
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

    
PSERVER_INFO_100 = SERVER_INFO_100LPSERVER_INFO_100 = SERVER_INFO_100
class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    
PSERVER_INFO_101 = SERVER_INFO_101LPSERVER_INFO_101 = SERVER_INFO_101
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
class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    
PRPC_SID = RPC_SIDPSID = RPC_SID
class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    
PACL = ACL
class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
PSECURITY_DESCRIPTOR = SECURITY_DESCRIPTORMethod("LsarClose",
InOut(PLSAPR_HANDLE),
),Method("Opnum1NotUsedOnWire",
In(),
),Method("Lsar_LSA_DP_2",
In(),
),Method("Lsar_LSA_DP_3",
In(),
),Method("Lsar_LSA_DP_4",
In(),
),Method("Opnum5NotUsedOnWire",
In(),
),Method("LsarOpenPolicy",
In(PWCHAR_T),
In(PLSAPR_OBJECT_ATTRIBUTES),
In(ACCESS_MASK),
Out(PLSAPR_HANDLE),
),Method("Lsar_LSA_DP_7",
In(),
),Method("Lsar_LSA_DP_8",
In(),
),Method("Opnum9NotUsedOnWire",
In(),
),Method("Lsar_LSA_DP_10",
In(),
),Method("Lsar_LSA_DP_11",
In(),
),Method("Lsar_LSA_DP_12",
In(),
),Method("Lsar_LSA_DP_13",
In(),
),Method("LsarLookupNames",
In(LSAPR_HANDLE),
In(UNSIGNED_LONG),
In(PRPC_UNICODE_STRING),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_SIDS),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
),Method("LsarLookupSids",
In(LSAPR_HANDLE),
In(PLSAPR_SID_ENUM_BUFFER),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_NAMES),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
),Method("Lsar_LSA_DP_16",
In(),
),Method("Lsar_LSA_DP_17",
In(),
),Method("Lsar_LSA_DP_18",
In(),
),Method("Lsar_LSA_DP_19",
In(),
),Method("Lsar_LSA_DP_20",
In(),
),Method("Opnum21NotUsedOnWire",
In(),
),Method("Opnum22NotUsedOnWire",
In(),
),Method("Lsar_LSA_DP_23",
In(),
),Method("Lsar_LSA_DP_24",
In(),
),Method("Lsar_LSA_DP_25",
In(),
),Method("Lsar_LSA_DP_26",
In(),
),Method("Lsar_LSA_DP_27",
In(),
),Method("Lsar_LSA_DP_28",
In(),
),Method("Lsar_LSA_DP_29",
In(),
),Method("Lsar_LSA_DP_30",
In(),
),Method("Lsar_LSA_DP_31",
In(),
),Method("Lsar_LSA_DP_32",
In(),
),Method("Lsar_LSA_DP_33",
In(),
),Method("Lsar_LSA_DP_34",
In(),
),Method("Lsar_LSA_DP_35",
In(),
),Method("Lsar_LSA_DP_36",
In(),
),Method("Lsar_LSA_DP_37",
In(),
),Method("Lsar_LSA_DP_38",
In(),
),Method("Lsar_LSA_DP_39",
In(),
),Method("Lsar_LSA_DP_40",
In(),
),Method("Lsar_LSA_DP_41",
In(),
),Method("Lsar_LSA_DP_42",
In(),
),Method("Lsar_LSA_DP_43",
In(),
),Method("LsarOpenPolicy2",
In(PWCHAR_T),
In(PLSAPR_OBJECT_ATTRIBUTES),
In(ACCESS_MASK),
Out(PLSAPR_HANDLE),
),Method("LsarGetUserName",
In(PWCHAR_T),
InOut(PPRPC_UNICODE_STRING),
InOut(PPRPC_UNICODE_STRING),
),Method("Lsar_LSA_DP_46",
In(),
),Method("Lsar_LSA_DP_47",
In(),
),Method("Lsar_LSA_DP_48",
In(),
),Method("Lsar_LSA_DP_49",
In(),
),Method("Lsar_LSA_DP_50",
In(),
),Method("Lsar_LSA_DP_51",
In(),
),Method("Opnum52NotUsedOnWire",
In(),
),Method("Lsar_LSA_DP_53",
In(),
),Method("Lsar_LSA_DP_54",
In(),
),Method("Lsar_LSA_DP_55",
In(),
),Method("Opnum56NotUsedOnWire",
In(),
),Method("LsarLookupSids2",
In(LSAPR_HANDLE),
In(PLSAPR_SID_ENUM_BUFFER),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_NAMES_EX),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("LsarLookupNames2",
In(LSAPR_HANDLE),
In(UNSIGNED_LONG),
In(PRPC_UNICODE_STRING),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_SIDS_EX),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("Lsar_LSA_DP_59",
In(),
),Method("Opnum60NotUsedOnWire",
In(),
),Method("Opnum61NotUsedOnWire",
In(),
),Method("Opnum62NotUsedOnWire",
In(),
),Method("Opnum63NotUsedOnWire",
In(),
),Method("Opnum64NotUsedOnWire",
In(),
),Method("Opnum65NotUsedOnWire",
In(),
),Method("Opnum66NotUsedOnWire",
In(),
),Method("Opnum67NotUsedOnWire",
In(),
),Method("LsarLookupNames3",
In(LSAPR_HANDLE),
In(UNSIGNED_LONG),
In(PRPC_UNICODE_STRING),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_SIDS_EX2),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("Opnum69NotUsedOnWire",
In(),
),Method("Opnum70NotUsedOnWire",
In(),
),Method("Opnum71NotUsedOnWire",
In(),
),Method("Opnum72NotUsedOnWire",
In(),
),Method("Lsar_LSA_DP_73",
In(),
),Method("Lsar_LSA_DP_74",
In(),
),Method("Opnum75NotUsedOnWire",
In(),
),Method("LsarLookupSids3",
In(HANDLE_T),
In(PLSAPR_SID_ENUM_BUFFER),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_NAMES_EX),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("LsarLookupNames4",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PRPC_UNICODE_STRING),
Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
InOut(PLSAPR_TRANSLATED_SIDS_EX2),
In(LSAP_LOOKUP_LEVEL),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),