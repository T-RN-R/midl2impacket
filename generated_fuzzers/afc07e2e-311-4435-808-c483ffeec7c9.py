
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

    
Method("LsarClose",
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
class ('LSAPR_WRAPPED_CAPID_SET', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Entries"),(('PLSAPR_SID_INFORMATION', None), "SidInfo"),]

    
Method("LsarGetAvailableCAPIDs",
In(HANDLE_T),
Out(PLSAPR_WRAPPED_CAPID_SET),
),