
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

    
Method("R_GetServerPort",
In(HANDLE_T),
),Method("Opnum1NotUsedOnWire",
In(),
),Method("R_OpenQueue",
In(HANDLE_T),
In(PQUEUE_FORMAT),
In(DWORD),
In(DWORD),
In(PGUID),
In(LONG),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(USHORT),
In(LONG),
Out(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
),Method("R_CloseQueue",
In(HANDLE_T),
InOut(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
),Method("R_CreateCursor",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
Out(PDWORD),
),Method("R_CloseCursor",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(DWORD),
),Method("R_PurgeQueue",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
),Method("R_StartReceive",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(ULONGLONG),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
Out(PDWORD),
Out(PULONGLONG),
Out(PDWORD),
Out(PPSECTIONBUFFER),
),Method("R_CancelReceive",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(DWORD),
),Method("R_EndReceive",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(DWORD),
In(DWORD),
),Method("R_MoveMessage",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(ULONGLONG),
In(ULONGLONG),
In(PXACTUOW),
),Method("R_OpenQueueForMove",
In(HANDLE_T),
In(PQUEUE_FORMAT),
In(DWORD),
In(DWORD),
In(PGUID),
In(LONG),
In(UNSIGNED_CHAR),
In(UNSIGNED_CHAR),
In(USHORT),
In(LONG),
Out(PULONGLONG),
Out(PQUEUE_CONTEXT_HANDLE_SERIALIZE),
),Method("R_QMEnlistRemoteTransaction",
In(HANDLE_T),
In(PXACTUOW),
In(DWORD),
In(PUNSIGNED_CHAR),
In(PQUEUE_FORMAT),
),Method("R_StartTransactionalReceive",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(ULONGLONG),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(DWORD),
In(PXACTUOW),
Out(PDWORD),
Out(PULONGLONG),
Out(PDWORD),
Out(PPSECTIONBUFFER),
),Method("R_SetUserAcknowledgementClass",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(ULONGLONG),
In(USHORT),
),Method("R_EndTransactionalReceive",
In(HANDLE_T),
In(QUEUE_CONTEXT_HANDLE_NOSERIALIZE),
In(DWORD),
In(DWORD),
),Method("Opnum0NotUsedOnWire",
In(),
),Method("R_QMGetRemoteQueueName",
In(HANDLE_T),
In(DWORD),
InOut(PPWCHAR),
),Method("R_QMOpenRemoteQueue",
In(HANDLE_T),
Out(PPCTX_OPENREMOTE_HANDLE_TYPE),
Out(PDWORD),
In(PQUEUE_FORMAT),
In(DWORD),
In(DWORD),
In(DWORD),
In(PGUID),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("R_QMCloseRemoteQueueContext",
InOut(PPCTX_OPENREMOTE_HANDLE_TYPE),
),Method("R_QMCreateRemoteCursor",
In(HANDLE_T),
In(PSTRUCT_CACTRANSFERBUFFERV1),
In(DWORD),
Out(PDWORD),
),Method("Opnum5NotUsedOnWire",
In(),
),Method("R_QMCreateObjectInternal",
In(HANDLE_T),
In(DWORD),
In(PWCHAR),
In(DWORD),
In(PUNSIGNED_CHAR),
In(DWORD),
In(DWORD),
In(PROPVARIANT),
),Method("R_QMSetObjectSecurityInternal",
In(HANDLE_T),
In(PSTRUCT_OBJECT_FORMAT),
In(DWORD),
In(DWORD),
In(PUNSIGNED_CHAR),
),Method("R_QMGetObjectSecurityInternal",
In(HANDLE_T),
In(PSTRUCT_OBJECT_FORMAT),
In(DWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("R_QMDeleteObject",
In(HANDLE_T),
In(PSTRUCT_OBJECT_FORMAT),
),Method("R_QMGetObjectProperties",
In(HANDLE_T),
In(PSTRUCT_OBJECT_FORMAT),
In(DWORD),
In(DWORD),
InOut(PROPVARIANT),
),Method("R_QMSetObjectProperties",
In(HANDLE_T),
In(PSTRUCT_OBJECT_FORMAT),
In(DWORD),
In(DWORD),
In(PROPVARIANT),
),Method("R_QMObjectPathToObjectFormat",
In(HANDLE_T),
In(PWCHAR),
InOut(PSTRUCT_OBJECT_FORMAT),
),Method("Opnum13NotUsedOnWire",
In(),
),Method("R_QMGetTmWhereabouts",
In(HANDLE_T),
In(DWORD),
Out(PUNSIGNED_CHAR),
Out(PDWORD),
),Method("R_QMEnlistTransaction",
In(HANDLE_T),
In(PXACTUOW),
In(DWORD),
In(PUNSIGNED_CHAR),
),Method("R_QMEnlistInternalTransaction",
In(HANDLE_T),
In(PXACTUOW),
Out(PRPC_INT_XACT_HANDLE),
),Method("R_QMCommitTransaction",
InOut(PRPC_INT_XACT_HANDLE),
),Method("R_QMAbortTransaction",
InOut(PRPC_INT_XACT_HANDLE),
),Method("rpc_QMOpenQueueInternal",
In(HANDLE_T),
In(PQUEUE_FORMAT),
In(DWORD),
In(DWORD),
In(DWORD),
InOut(PPWCHAR),
In(PDWORD),
In(PGUID),
In(PWCHAR),
Out(PDWORD),
Out(PRPC_QUEUE_HANDLE),
In(DWORD),
In(DWORD),
),Method("rpc_ACCloseHandle",
InOut(PRPC_QUEUE_HANDLE),
),Method("Opnum21NotUsedOnWire",
In(),
),Method("rpc_ACCloseCursor",
In(RPC_QUEUE_HANDLE),
In(DWORD),
),Method("rpc_ACSetCursorProperties",
In(RPC_QUEUE_HANDLE),
In(DWORD),
In(DWORD),
),Method("Opnum24NotUsedOnWire",
In(),
),Method("Opnum25NotUsedOnWire",
In(),
),Method("rpc_ACHandleToFormatName",
In(RPC_QUEUE_HANDLE),
In(DWORD),
InOut(PWCHAR),
InOut(PDWORD),
),Method("rpc_ACPurgeQueue",
In(RPC_QUEUE_HANDLE),
),Method("R_QMQueryQMRegistryInternal",
In(HANDLE_T),
In(DWORD),
Out(PPWCHAR),
),Method("Opnum29NotUsedOnWire",
In(),
),Method("Opnum30NotUsedOnWire",
In(),
),Method("R_QMGetRTQMServerPort",
In(HANDLE_T),
In(DWORD),
),Method("Opnum32NotUsedOnWire",
In(),
),Method("Opnum33NotUsedOnWire",
In(),
),Method("Opnum34NotUsedOnWire",
In(),
),