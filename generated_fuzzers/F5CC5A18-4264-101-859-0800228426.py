
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

    
Method("NspiBind",
In(HANDLE_T),
In(DWORD),
In(PSTAT),
InOut(PFLATUID_R),
Out(PNSPI_HANDLE),
),Method("NspiUnbind",
InOut(PNSPI_HANDLE),
In(DWORD),
),Method("NspiUpdateStat",
In(NSPI_HANDLE),
In(DWORD),
InOut(PSTAT),
InOut(PLONG),
),Method("NspiQueryRows",
In(NSPI_HANDLE),
In(DWORD),
InOut(PSTAT),
In(DWORD),
In(PDWORD),
In(DWORD),
In(PPROPERTYTAGARRAY_R),
Out(PPPROPERTYROWSET_R),
),Method("NspiSeekEntries",
In(NSPI_HANDLE),
In(DWORD),
InOut(PSTAT),
In(PPROPERTYVALUE_R),
In(PPROPERTYTAGARRAY_R),
In(PPROPERTYTAGARRAY_R),
Out(PPPROPERTYROWSET_R),
),Method("NspiGetMatches",
In(NSPI_HANDLE),
In(DWORD),
InOut(PSTAT),
In(PPROPERTYTAGARRAY_R),
In(DWORD),
In(PRESTRICTION_R),
In(PPROPERTYNAME_R),
In(DWORD),
Out(PPPROPERTYTAGARRAY_R),
In(PPROPERTYTAGARRAY_R),
Out(PPPROPERTYROWSET_R),
),Method("NspiResortRestriction",
In(NSPI_HANDLE),
In(DWORD),
InOut(PSTAT),
In(PPROPERTYTAGARRAY_R),
InOut(PPPROPERTYTAGARRAY_R),
),Method("NspiDNToMId",
In(NSPI_HANDLE),
In(DWORD),
In(PSTRINGSARRAY_R),
Out(PPPROPERTYTAGARRAY_R),
),Method("NspiGetPropList",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
Out(PPPROPERTYTAGARRAY_R),
),Method("NspiGetProps",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
In(PPROPERTYTAGARRAY_R),
Out(PPPROPERTYROW_R),
),Method("NspiCompareMIds",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
In(DWORD),
In(DWORD),
Out(PLONG),
),Method("NspiModProps",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
In(PPROPERTYTAGARRAY_R),
In(PPROPERTYROW_R),
),Method("NspiGetSpecialTable",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
InOut(PDWORD),
Out(PPPROPERTYROWSET_R),
),Method("NspiGetTemplateInfo",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
In(PCHAR),
In(DWORD),
In(DWORD),
Out(PPPROPERTYROW_R),
),Method("NspiModLinkAtt",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
In(PBINARYARRAY_R),
),Method("Opnum15NotUsedOnWire",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
In(PBINARYARRAY_R),
),Method("NspiQueryColumns",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
Out(PPPROPERTYTAGARRAY_R),
),Method("NspiGetNamesFromIDs",
In(NSPI_HANDLE),
In(DWORD),
In(PFLATUID_R),
In(PPROPERTYTAGARRAY_R),
Out(PPPROPERTYTAGARRAY_R),
Out(PPPROPERTYNAMESET_R),
),Method("NspiGetIDsFromNames",
In(NSPI_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
In(PPPROPERTYNAME_R),
Out(PPPROPERTYTAGARRAY_R),
),Method("NspiResolveNames",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
In(PPROPERTYTAGARRAY_R),
In(PSTRINGSARRAY_R),
Out(PPPROPERTYTAGARRAY_R),
Out(PPPROPERTYROWSET_R),
),Method("NspiResolveNamesW",
In(NSPI_HANDLE),
In(DWORD),
In(PSTAT),
In(PPROPERTYTAGARRAY_R),
In(PWSTRINGSARRAY_R),
Out(PPPROPERTYTAGARRAY_R),
Out(PPPROPERTYROWSET_R),
),