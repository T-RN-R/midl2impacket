
from fuzzer.midl import *
from fuzzer.core import *
DWORD64 = NdrHyper
DWORD = NdrLong
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

    

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
Method("SamrConnect",
In(PSAMPR_SERVER_NAME),
Out(PSAMPR_HANDLE),
In(UNSIGNED_LONG),
),Method("SamrCloseHandle",
InOut(PSAMPR_HANDLE),
),Method("SamrSetSecurityObject",
In(SAMPR_HANDLE),
In(SECURITY_INFORMATION),
In(PSAMPR_SR_SECURITY_DESCRIPTOR),
),Method("SamrQuerySecurityObject",
In(SAMPR_HANDLE),
In(SECURITY_INFORMATION),
Out(PPSAMPR_SR_SECURITY_DESCRIPTOR),
),Method("Opnum4NotUsedOnWire",
In(),
),Method("SamrLookupDomainInSamServer",
In(SAMPR_HANDLE),
In(PRPC_UNICODE_STRING),
Out(PPRPC_SID),
),Method("SamrEnumerateDomainsInSamServer",
In(SAMPR_HANDLE),
InOut(PUNSIGNED_LONG),
Out(PPSAMPR_ENUMERATION_BUFFER),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),Method("SamrOpenDomain",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(PRPC_SID),
Out(PSAMPR_HANDLE),
),Method("SamrQueryInformationDomain",
In(SAMPR_HANDLE),
In(DOMAIN_INFORMATION_CLASS),
Out(PPSAMPR_DOMAIN_INFO_BUFFER),
),Method("SamrSetInformationDomain",
In(SAMPR_HANDLE),
In(DOMAIN_INFORMATION_CLASS),
In(PSAMPR_DOMAIN_INFO_BUFFER),
),Method("SamrCreateGroupInDomain",
In(SAMPR_HANDLE),
In(PRPC_UNICODE_STRING),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
Out(PUNSIGNED_LONG),
),Method("SamrEnumerateGroupsInDomain",
In(SAMPR_HANDLE),
InOut(PUNSIGNED_LONG),
Out(PPSAMPR_ENUMERATION_BUFFER),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),Method("SamrCreateUserInDomain",
In(SAMPR_HANDLE),
In(PRPC_UNICODE_STRING),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
Out(PUNSIGNED_LONG),
),Method("SamrEnumerateUsersInDomain",
In(SAMPR_HANDLE),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PPSAMPR_ENUMERATION_BUFFER),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),Method("SamrCreateAliasInDomain",
In(SAMPR_HANDLE),
In(PRPC_UNICODE_STRING),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
Out(PUNSIGNED_LONG),
),Method("SamrEnumerateAliasesInDomain",
In(SAMPR_HANDLE),
InOut(PUNSIGNED_LONG),
Out(PPSAMPR_ENUMERATION_BUFFER),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),Method("SamrGetAliasMembership",
In(SAMPR_HANDLE),
In(PSAMPR_PSID_ARRAY),
Out(PSAMPR_ULONG_ARRAY),
),Method("SamrLookupNamesInDomain",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(RPC_UNICODE_STRING),
Out(PSAMPR_ULONG_ARRAY),
Out(PSAMPR_ULONG_ARRAY),
),Method("SamrLookupIdsInDomain",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(PUNSIGNED_LONG),
Out(PSAMPR_RETURNED_USTRING_ARRAY),
Out(PSAMPR_ULONG_ARRAY),
),Method("SamrOpenGroup",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
),Method("SamrQueryInformationGroup",
In(SAMPR_HANDLE),
In(GROUP_INFORMATION_CLASS),
Out(PPSAMPR_GROUP_INFO_BUFFER),
),Method("SamrSetInformationGroup",
In(SAMPR_HANDLE),
In(GROUP_INFORMATION_CLASS),
In(PSAMPR_GROUP_INFO_BUFFER),
),Method("SamrAddMemberToGroup",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("SamrDeleteGroup",
InOut(PSAMPR_HANDLE),
),Method("SamrRemoveMemberFromGroup",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
),Method("SamrGetMembersInGroup",
In(SAMPR_HANDLE),
Out(PPSAMPR_GET_MEMBERS_BUFFER),
),Method("SamrSetMemberAttributesOfGroup",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("SamrOpenAlias",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
),Method("SamrQueryInformationAlias",
In(SAMPR_HANDLE),
In(ALIAS_INFORMATION_CLASS),
Out(PPSAMPR_ALIAS_INFO_BUFFER),
),Method("SamrSetInformationAlias",
In(SAMPR_HANDLE),
In(ALIAS_INFORMATION_CLASS),
In(PSAMPR_ALIAS_INFO_BUFFER),
),Method("SamrDeleteAlias",
InOut(PSAMPR_HANDLE),
),Method("SamrAddMemberToAlias",
In(SAMPR_HANDLE),
In(PRPC_SID),
),Method("SamrRemoveMemberFromAlias",
In(SAMPR_HANDLE),
In(PRPC_SID),
),Method("SamrGetMembersInAlias",
In(SAMPR_HANDLE),
Out(PSAMPR_PSID_ARRAY_OUT),
),Method("SamrOpenUser",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
),Method("SamrDeleteUser",
InOut(PSAMPR_HANDLE),
),Method("SamrQueryInformationUser",
In(SAMPR_HANDLE),
In(USER_INFORMATION_CLASS),
Out(PPSAMPR_USER_INFO_BUFFER),
),Method("SamrSetInformationUser",
In(SAMPR_HANDLE),
In(USER_INFORMATION_CLASS),
In(PSAMPR_USER_INFO_BUFFER),
),Method("SamrChangePasswordUser",
In(SAMPR_HANDLE),
In(UNSIGNED_CHAR),
In(PENCRYPTED_LM_OWF_PASSWORD),
In(PENCRYPTED_LM_OWF_PASSWORD),
In(UNSIGNED_CHAR),
In(PENCRYPTED_NT_OWF_PASSWORD),
In(PENCRYPTED_NT_OWF_PASSWORD),
In(UNSIGNED_CHAR),
In(PENCRYPTED_NT_OWF_PASSWORD),
In(UNSIGNED_CHAR),
In(PENCRYPTED_LM_OWF_PASSWORD),
),Method("SamrGetGroupsForUser",
In(SAMPR_HANDLE),
Out(PPSAMPR_GET_GROUPS_BUFFER),
),Method("SamrQueryDisplayInformation",
In(SAMPR_HANDLE),
In(DOMAIN_DISPLAY_INFORMATION),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PSAMPR_DISPLAY_INFO_BUFFER),
),Method("SamrGetDisplayEnumerationIndex",
In(SAMPR_HANDLE),
In(DOMAIN_DISPLAY_INFORMATION),
In(PRPC_UNICODE_STRING),
Out(PUNSIGNED_LONG),
),Method("Opnum42NotUsedOnWire",
In(),
),Method("Opnum43NotUsedOnWire",
In(),
),Method("SamrGetUserDomainPasswordInformation",
In(SAMPR_HANDLE),
Out(PUSER_DOMAIN_PASSWORD_INFORMATION),
),Method("SamrRemoveMemberFromForeignDomain",
In(SAMPR_HANDLE),
In(PRPC_SID),
),Method("SamrQueryInformationDomain2",
In(SAMPR_HANDLE),
In(DOMAIN_INFORMATION_CLASS),
Out(PPSAMPR_DOMAIN_INFO_BUFFER),
),Method("SamrQueryInformationUser2",
In(SAMPR_HANDLE),
In(USER_INFORMATION_CLASS),
Out(PPSAMPR_USER_INFO_BUFFER),
),Method("SamrQueryDisplayInformation2",
In(SAMPR_HANDLE),
In(DOMAIN_DISPLAY_INFORMATION),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PSAMPR_DISPLAY_INFO_BUFFER),
),Method("SamrGetDisplayEnumerationIndex2",
In(SAMPR_HANDLE),
In(DOMAIN_DISPLAY_INFORMATION),
In(PRPC_UNICODE_STRING),
Out(PUNSIGNED_LONG),
),Method("SamrCreateUser2InDomain",
In(SAMPR_HANDLE),
In(PRPC_UNICODE_STRING),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PSAMPR_HANDLE),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
),Method("SamrQueryDisplayInformation3",
In(SAMPR_HANDLE),
In(DOMAIN_DISPLAY_INFORMATION),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PSAMPR_DISPLAY_INFO_BUFFER),
),Method("SamrAddMultipleMembersToAlias",
In(SAMPR_HANDLE),
In(PSAMPR_PSID_ARRAY),
),Method("SamrRemoveMultipleMembersFromAlias",
In(SAMPR_HANDLE),
In(PSAMPR_PSID_ARRAY),
),Method("SamrOemChangePasswordUser2",
In(HANDLE_T),
In(PRPC_STRING),
In(PRPC_STRING),
In(PSAMPR_ENCRYPTED_USER_PASSWORD),
In(PENCRYPTED_LM_OWF_PASSWORD),
),Method("SamrUnicodeChangePasswordUser2",
In(HANDLE_T),
In(PRPC_UNICODE_STRING),
In(PRPC_UNICODE_STRING),
In(PSAMPR_ENCRYPTED_USER_PASSWORD),
In(PENCRYPTED_NT_OWF_PASSWORD),
In(UNSIGNED_CHAR),
In(PSAMPR_ENCRYPTED_USER_PASSWORD),
In(PENCRYPTED_LM_OWF_PASSWORD),
),Method("SamrGetDomainPasswordInformation",
In(HANDLE_T),
In(PRPC_UNICODE_STRING),
Out(PUSER_DOMAIN_PASSWORD_INFORMATION),
),Method("SamrConnect2",
In(PSAMPR_SERVER_NAME),
Out(PSAMPR_HANDLE),
In(UNSIGNED_LONG),
),Method("SamrSetInformationUser2",
In(SAMPR_HANDLE),
In(USER_INFORMATION_CLASS),
In(PSAMPR_USER_INFO_BUFFER),
),Method("Opnum59NotUsedOnWire",
In(),
),Method("Opnum60NotUsedOnWire",
In(),
),Method("Opnum61NotUsedOnWire",
In(),
),Method("SamrConnect4",
In(PSAMPR_SERVER_NAME),
Out(PSAMPR_HANDLE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("Opnum63NotUsedOnWire",
In(),
),Method("SamrConnect5",
In(PSAMPR_SERVER_NAME),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PSAMPR_REVISION_INFO),
Out(PUNSIGNED_LONG),
Out(PSAMPR_REVISION_INFO),
Out(PSAMPR_HANDLE),
),Method("SamrRidToSid",
In(SAMPR_HANDLE),
In(UNSIGNED_LONG),
Out(PPRPC_SID),
),Method("SamrSetDSRMPassword",
In(HANDLE_T),
In(PRPC_UNICODE_STRING),
In(UNSIGNED_LONG),
In(PENCRYPTED_NT_OWF_PASSWORD),
),Method("SamrValidatePassword",
In(HANDLE_T),
In(PASSWORD_POLICY_VALIDATION_TYPE),
In(PSAM_VALIDATE_INPUT_ARG),
Out(PPSAM_VALIDATE_OUTPUT_ARG),
),Method("Opnum68NotUsedOnWire",
In(),
),Method("Opnum69NotUsedOnWire",
In(),
),Method("Opnum70NotUsedOnWire",
In(),
),Method("Opnum71NotUsedOnWire",
In(),
),Method("Opnum72NotUsedOnWire",
In(),
),Method("SamrUnicodeChangePasswordUser4",
In(HANDLE_T),
In(PRPC_UNICODE_STRING),
In(PRPC_UNICODE_STRING),
In(PSAMPR_ENCRYPTED_PASSWORD_AES),
),