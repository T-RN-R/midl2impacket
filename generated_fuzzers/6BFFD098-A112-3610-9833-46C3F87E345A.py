
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

    
Method("NetrWkstaGetInfo",
In(WKSSVC_IDENTIFY_HANDLE),
In(UNSIGNED_LONG),
Out(LPWKSTA_INFO),
),Method("NetrWkstaSetInfo",
In(WKSSVC_IDENTIFY_HANDLE),
In(UNSIGNED_LONG),
In(LPWKSTA_INFO),
InOut(PUNSIGNED_LONG),
),Method("NetrWkstaUserEnum",
In(WKSSVC_IDENTIFY_HANDLE),
InOut(LPWKSTA_USER_ENUM_STRUCT),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
InOut(PUNSIGNED_LONG),
),Method("Opnum3NotUsedOnWire",
In(),
),Method("Opnum4NotUsedOnWire",
In(),
),Method("NetrWkstaTransportEnum",
In(WKSSVC_IDENTIFY_HANDLE),
InOut(LPWKSTA_TRANSPORT_ENUM_STRUCT),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
InOut(PUNSIGNED_LONG),
),Method("NetrWkstaTransportAdd",
In(WKSSVC_IDENTIFY_HANDLE),
In(UNSIGNED_LONG),
In(LPWKSTA_TRANSPORT_INFO_0),
InOut(PUNSIGNED_LONG),
),Method("NetrWkstaTransportDel",
In(WKSSVC_IDENTIFY_HANDLE),
In(PWCHAR_T),
In(UNSIGNED_LONG),
),Method("NetrUseAdd",
In(WKSSVC_IMPERSONATE_HANDLE),
In(UNSIGNED_LONG),
In(LPUSE_INFO),
InOut(PUNSIGNED_LONG),
),Method("NetrUseGetInfo",
In(WKSSVC_IMPERSONATE_HANDLE),
In(PWCHAR_T),
In(UNSIGNED_LONG),
Out(LPUSE_INFO),
),Method("NetrUseDel",
In(WKSSVC_IMPERSONATE_HANDLE),
In(PWCHAR_T),
In(UNSIGNED_LONG),
),Method("NetrUseEnum",
In(WKSSVC_IDENTIFY_HANDLE),
InOut(LPUSE_ENUM_STRUCT),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
InOut(PUNSIGNED_LONG),
),Method("Opnum12NotUsedOnWire",
In(),
),Method("NetrWorkstationStatisticsGet",
In(WKSSVC_IDENTIFY_HANDLE),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PLPSTAT_WORKSTATION_0),
),Method("Opnum14NotUsedOnWire",
In(),
),Method("Opnum15NotUsedOnWire",
In(),
),Method("Opnum16NotUsedOnWire",
In(),
),Method("Opnum17NotUsedOnWire",
In(),
),Method("Opnum18NotUsedOnWire",
In(),
),Method("Opnum19NotUsedOnWire",
In(),
),Method("NetrGetJoinInformation",
In(WKSSVC_IMPERSONATE_HANDLE),
InOut(PPWCHAR_T),
Out(PNETSETUP_JOIN_STATUS),
),Method("Opnum21NotUsedOnWire",
In(),
),Method("NetrJoinDomain2",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrUnjoinDomain2",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrRenameMachineInDomain2",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrValidateName2",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(NETSETUP_NAME_TYPE),
),Method("NetrGetJoinableOUs2",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
InOut(PUNSIGNED_LONG),
Out(PPPWCHAR_T),
),Method("NetrAddAlternateComputerName",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrRemoveAlternateComputerName",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrSetPrimaryComputerName",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PJOINPR_ENCRYPTED_USER_PASSWORD),
In(UNSIGNED_LONG),
),Method("NetrEnumerateComputerNames",
In(WKSSVC_IMPERSONATE_HANDLE),
In(NET_COMPUTER_NAME_TYPE),
In(UNSIGNED_LONG),
Out(PPNET_COMPUTER_NAME_ARRAY),
),