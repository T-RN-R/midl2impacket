
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

    

class ('XACTUOW', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "rgb"),]

    

class ('BLOB', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cbSize"),(('PUNSIGNED_CHAR', None), "pBlobData"),]

    

class ('CAUB', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PUNSIGNED_CHAR', None), "pElems"),]

    

class ('CAUI', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PUNSIGNED_SHORT', None), "pElems"),]

    

class ('CAL', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PLONG', None), "pElems"),]

    

class ('CAUL', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PUNSIGNED_LONG', None), "pElems"),]

    

class ('CAUH', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PULARGE_INTEGER', None), "pElems"),]

    

class ('CACLSID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PGUID', None), "pElems"),]

    

class ('CALPWSTR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PPWCHAR_T', None), "pElems"),]

    

class ('CAPROPVARIANT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cElems"),(('PPROPVARIANT', None), "pElems"),]

    

class ('_VARUNION', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (('CHAR', None), cVal),3 : (('UCHAR', None), bVal),4 : (('SHORT', None), iVal),5 : (('USHORT', None), uiVal),6 : (('LONG', None), lVal),7 : (('ULONG', None), ulVal),8 : (('LARGE_INTEGER', None), hVal),9 : (('ULARGE_INTEGER', None), uhVal),10 : (('VARIANT_BOOL', None), boolVal),11 : (('PGUID', None), puuid),12 : (('BLOB', None), blob),13 : (('PWCHAR_T', None), pwszVal),14 : (('CAUB', None), caub),15 : (('CAUI', None), caui),16 : (('CAL', None), cal),17 : (('CAUL', None), caul),18 : (('CAUH', None), cauh),19 : (('CACLSID', None), cauuid),20 : (('CALPWSTR', None), calpwstr),21 : (('CAPROPVARIANT', None), capropvar),}

    

class ('TAG_INNER_PROPVARIANT', None)(NdrStructure):
    MEMBERS = [(('VARTYPE', None), "vt"),(('UCHAR', None), "wReserved1"),(('UCHAR', None), "wReserved2"),(('ULONG', None), "wReserved3"),(('_VARUNION', None), "_varUnion"),]

    

class ('DL_ID', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "m_DlGuid"),(('PWCHAR_T', None), "m_pwzDomain"),]

    

class ('MULTICAST_ID', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "m_address"),(('ULONG', None), "m_port"),]

    

class ('OBJECTID', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "Lineage"),(('DWORD', None), "Uniquifier"),]

    

class ('U0', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {2 : (('GUID', None), m_gPublicID),3 : (('OBJECTID', None), m_oPrivateID),4 : (('PWCHAR_T', None), m_pDirectID),5 : (('GUID', None), m_gMachineID),6 : (('GUID', None), m_GConnectorID),7 : (('DL_ID', None), m_DlID),8 : (('MULTICAST_ID', None), m_MulticastID),9 : (('PWCHAR_T', None), m_pDirectSubqueueID),}

    

class ('QUEUE_FORMAT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "m_qft"),(('UNSIGNED_CHAR', None), "m_SuffixAndFlags"),(('UNSIGNED_SHORT', None), "m_reserved"),(('U0', None), "u0"),]

    

class ('MQPROPERTYRESTRICTION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "rel"),(('UNSIGNED_LONG', None), "prop"),(('PROPVARIANT', None), "prval"),]

    

class ('MQRESTRICTION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cRes"),(('PMQPROPERTYRESTRICTION', None), "paPropRes"),]

    

class ('MQCOLUMNSET', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cCol"),(('PPROPID', None), "aCol"),]

    

class ('MQSORTKEY', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "propColumn"),(('UNSIGNED_LONG', None), "dwOrder"),]

    

class ('MQSORTSET', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cCol"),(('PMQSORTKEY', None), "aCol"),]

    
Method("S_DSCreateObject",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PROPVARIANT),
InOut(PGUID),
),Method("S_DSDeleteObject",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
),Method("S_DSGetProps",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
InOut(PROPVARIANT),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSSetProps",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PROPVARIANT),
),Method("S_DSGetObjectSecurity",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
Out(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSSetObjectSecurity",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
),Method("S_DSLookupBegin",
In(HANDLE_T),
Out(PPCONTEXT_HANDLE_TYPE),
In(PWCHAR_T),
In(PMQRESTRICTION),
In(PMQCOLUMNSET),
In(PMQSORTSET),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
),Method("S_DSLookupNext",
In(HANDLE_T),
In(PCONTEXT_HANDLE_TYPE),
In(LPBOUNDED_PROPERTIES),
Out(PUNSIGNED_LONG),
Out(PROPVARIANT),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSLookupEnd",
In(HANDLE_T),
InOut(PPCONTEXT_HANDLE_TYPE),
),Method("Opnum9NotUsedOnWire",
In(),
),Method("S_DSDeleteObjectGuid",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
),Method("S_DSGetPropsGuid",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
InOut(PROPVARIANT),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSSetPropsGuid",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PROPVARIANT),
),Method("S_DSGetObjectSecurityGuid",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
In(UNSIGNED_LONG),
Out(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSSetObjectSecurityGuid",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
In(UNSIGNED_LONG),
In(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
),Method("Opnum15NotUsedOnWire",
In(),
),Method("Opnum16NotUsedOnWire",
In(),
),Method("Opnum17NotUsedOnWire",
In(),
),Method("Opnum18NotUsedOnWire",
In(),
),Method("S_DSQMSetMachineProperties",
In(HANDLE_T),
In(PWCHAR_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PROPVARIANT),
In(UNSIGNED_LONG),
),Method("S_DSCreateServersCache",
In(HANDLE_T),
InOut(PUNSIGNED_LONG),
InOut(PPWCHAR_T),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSQMSetMachinePropertiesSignProc",
In(PBYTE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
InOut(PBYTE),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("S_DSQMGetObjectSecurity",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(PGUID),
In(UNSIGNED_LONG),
Out(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
Out(PUNSIGNED_CHAR),
InOut(LPBOUNDED_SIGNATURE_SIZE),
),Method("S_DSQMGetObjectSecurityChallengeResponceProc",
In(PBYTE),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
InOut(PBYTE),
InOut(PUNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("S_InitSecCtx",
In(UNSIGNED_LONG),
In(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
Out(PUNSIGNED_CHAR),
Out(PUNSIGNED_LONG),
),Method("S_DSValidateServer",
In(HANDLE_T),
In(PGUID),
In(BOOL),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PUNSIGNED_CHAR),
In(UNSIGNED_LONG),
Out(PPCONTEXT_HANDLE_SERVER_AUTH_TYPE),
),Method("S_DSCloseServerHandle",
InOut(PPCONTEXT_HANDLE_SERVER_AUTH_TYPE),
),Method("Opnum24NotUsedOnWire",
In(),
),Method("Opnum25NotUsedOnWire",
In(),
),Method("Opnum26NotUsedOnWire",
In(),
),Method("S_DSGetServerPort",
In(HANDLE_T),
In(UNSIGNED_LONG),
),