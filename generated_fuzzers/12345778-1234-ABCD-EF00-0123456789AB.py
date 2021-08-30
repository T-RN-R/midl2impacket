from fuzzer.midl import *
from fuzzer.core import *


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


Method("LsarClose", InOut(PLSAPR_HANDLE),), Method(
    "Opnum1NotUsedOnWire",
    In(),
), Method("Lsar_LSA_DP_2", In(),), Method("Lsar_LSA_DP_3", In(),), Method(
    "Lsar_LSA_DP_4",
    In(),
), Method(
    "Opnum5NotUsedOnWire",
    In(),
), Method(
    "LsarOpenPolicy",
    In(PWCHAR_T),
    In(PLSAPR_OBJECT_ATTRIBUTES),
    In(ACCESS_MASK),
    Out(PLSAPR_HANDLE),
), Method(
    "Lsar_LSA_DP_7",
    In(),
), Method(
    "Lsar_LSA_DP_8",
    In(),
), Method(
    "Opnum9NotUsedOnWire",
    In(),
), Method(
    "Lsar_LSA_DP_10",
    In(),
), Method(
    "Lsar_LSA_DP_11",
    In(),
), Method(
    "Lsar_LSA_DP_12",
    In(),
), Method(
    "Lsar_LSA_DP_13",
    In(),
), Method(
    "LsarLookupNames",
    In(LSAPR_HANDLE),
    In(UNSIGNED_LONG),
    In(PRPC_UNICODE_STRING),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_SIDS),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
), Method(
    "LsarLookupSids",
    In(LSAPR_HANDLE),
    In(PLSAPR_SID_ENUM_BUFFER),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_NAMES),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
), Method(
    "Lsar_LSA_DP_16",
    In(),
), Method(
    "Lsar_LSA_DP_17",
    In(),
), Method(
    "Lsar_LSA_DP_18",
    In(),
), Method(
    "Lsar_LSA_DP_19",
    In(),
), Method(
    "Lsar_LSA_DP_20",
    In(),
), Method(
    "Opnum21NotUsedOnWire",
    In(),
), Method(
    "Opnum22NotUsedOnWire",
    In(),
), Method(
    "Lsar_LSA_DP_23",
    In(),
), Method(
    "Lsar_LSA_DP_24",
    In(),
), Method(
    "Lsar_LSA_DP_25",
    In(),
), Method(
    "Lsar_LSA_DP_26",
    In(),
), Method(
    "Lsar_LSA_DP_27",
    In(),
), Method(
    "Lsar_LSA_DP_28",
    In(),
), Method(
    "Lsar_LSA_DP_29",
    In(),
), Method(
    "Lsar_LSA_DP_30",
    In(),
), Method(
    "Lsar_LSA_DP_31",
    In(),
), Method(
    "Lsar_LSA_DP_32",
    In(),
), Method(
    "Lsar_LSA_DP_33",
    In(),
), Method(
    "Lsar_LSA_DP_34",
    In(),
), Method(
    "Lsar_LSA_DP_35",
    In(),
), Method(
    "Lsar_LSA_DP_36",
    In(),
), Method(
    "Lsar_LSA_DP_37",
    In(),
), Method(
    "Lsar_LSA_DP_38",
    In(),
), Method(
    "Lsar_LSA_DP_39",
    In(),
), Method(
    "Lsar_LSA_DP_40",
    In(),
), Method(
    "Lsar_LSA_DP_41",
    In(),
), Method(
    "Lsar_LSA_DP_42",
    In(),
), Method(
    "Lsar_LSA_DP_43",
    In(),
), Method(
    "LsarOpenPolicy2",
    In(PWCHAR_T),
    In(PLSAPR_OBJECT_ATTRIBUTES),
    In(ACCESS_MASK),
    Out(PLSAPR_HANDLE),
), Method(
    "LsarGetUserName",
    In(PWCHAR_T),
    InOut(PPRPC_UNICODE_STRING),
    InOut(PPRPC_UNICODE_STRING),
), Method(
    "Lsar_LSA_DP_46",
    In(),
), Method(
    "Lsar_LSA_DP_47",
    In(),
), Method(
    "Lsar_LSA_DP_48",
    In(),
), Method(
    "Lsar_LSA_DP_49",
    In(),
), Method(
    "Lsar_LSA_DP_50",
    In(),
), Method(
    "Lsar_LSA_DP_51",
    In(),
), Method(
    "Opnum52NotUsedOnWire",
    In(),
), Method(
    "Lsar_LSA_DP_53",
    In(),
), Method(
    "Lsar_LSA_DP_54",
    In(),
), Method(
    "Lsar_LSA_DP_55",
    In(),
), Method(
    "Opnum56NotUsedOnWire",
    In(),
), Method(
    "LsarLookupSids2",
    In(LSAPR_HANDLE),
    In(PLSAPR_SID_ENUM_BUFFER),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_NAMES_EX),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
    In(UNSIGNED_LONG),
    In(UNSIGNED_LONG),
), Method(
    "LsarLookupNames2",
    In(LSAPR_HANDLE),
    In(UNSIGNED_LONG),
    In(PRPC_UNICODE_STRING),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_SIDS_EX),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
    In(UNSIGNED_LONG),
    In(UNSIGNED_LONG),
), Method(
    "Lsar_LSA_DP_59",
    In(),
), Method(
    "Opnum60NotUsedOnWire",
    In(),
), Method(
    "Opnum61NotUsedOnWire",
    In(),
), Method(
    "Opnum62NotUsedOnWire",
    In(),
), Method(
    "Opnum63NotUsedOnWire",
    In(),
), Method(
    "Opnum64NotUsedOnWire",
    In(),
), Method(
    "Opnum65NotUsedOnWire",
    In(),
), Method(
    "Opnum66NotUsedOnWire",
    In(),
), Method(
    "Opnum67NotUsedOnWire",
    In(),
), Method(
    "LsarLookupNames3",
    In(LSAPR_HANDLE),
    In(UNSIGNED_LONG),
    In(PRPC_UNICODE_STRING),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_SIDS_EX2),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
    In(UNSIGNED_LONG),
    In(UNSIGNED_LONG),
), Method(
    "Opnum69NotUsedOnWire",
    In(),
), Method(
    "Opnum70NotUsedOnWire",
    In(),
), Method(
    "Opnum71NotUsedOnWire",
    In(),
), Method(
    "Opnum72NotUsedOnWire",
    In(),
), Method(
    "Lsar_LSA_DP_73",
    In(),
), Method(
    "Lsar_LSA_DP_74",
    In(),
), Method(
    "Opnum75NotUsedOnWire",
    In(),
), Method(
    "LsarLookupSids3",
    In(HANDLE_T),
    In(PLSAPR_SID_ENUM_BUFFER),
    Out(PPLSAPR_REFERENCED_DOMAIN_LIST),
    InOut(PLSAPR_TRANSLATED_NAMES_EX),
    In(LSAP_LOOKUP_LEVEL),
    InOut(PUNSIGNED_LONG),
    In(UNSIGNED_LONG),
    In(UNSIGNED_LONG),
), Method(
    "LsarLookupNames4",
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
