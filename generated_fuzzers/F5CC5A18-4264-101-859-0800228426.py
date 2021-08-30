
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
PWCHAR = NdrByte
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

class FLATUID_R(NdrStructure):
    MEMBERS = [(BYTE, "ab"),]

    

class PROPERTYTAGARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(DWORD, "aulPropTag"),]

    

class BINARY_R(NdrStructure):
    MEMBERS = [(DWORD, "cb"),(PBYTE, "lpb"),]

    

class SHORTARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PSHORT_INT, "lpi"),]

    

class LONGARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PLONG, "lpl"),]

    

class STRINGARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PPCHAR, "lppszA"),]

    

class BINARYARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PBINARY_R, "lpbin"),]

    

class FLATUIDARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PPFLATUID_R, "lpguid"),]

    

class WSTRINGARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PPWCHAR_T, "lppszW"),]

    

class DATETIMEARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "cValues"),(PFILETIME, "lpft"),]

    

class PROPERTYVALUE_R(NdrStructure):
    MEMBERS = []

    

class PROPERTYROW_R(NdrStructure):
    MEMBERS = [(DWORD, "Reserved"),(DWORD, "cValues"),(PPROPERTYVALUE_R, "lpProps"),]

    

class PROPERTYROWSET_R(NdrStructure):
    MEMBERS = [(DWORD, "cRows"),(PROPERTYROW_R, "aRow"),]

    

class RESTRICTION_R(NdrStructure):
    MEMBERS = []

    

class ANDRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "cRes"),(PRESTRICTION_R, "lpRes"),]

    
ORRESTRICTION_R = ANDRESTRICTION_R

class NOTRESTRICTION_R(NdrStructure):
    MEMBERS = [(PRESTRICTION_R, "lpRes"),]

    

class CONTENTRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "ulFuzzyLevel"),(DWORD, "ulPropTag"),(PPROPERTYVALUE_R, "lpProp"),]

    

class BITMASKRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "relBMR"),(DWORD, "ulPropTag"),(DWORD, "ulMask"),]

    

class PROPERTYRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "relop"),(DWORD, "ulPropTag"),(PPROPERTYVALUE_R, "lpProp"),]

    

class COMPAREPROPSRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "relop"),(DWORD, "ulPropTag1"),(DWORD, "ulPropTag2"),]

    

class SUBRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "ulSubObject"),(PRESTRICTION_R, "lpRes"),]

    

class SIZERESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "relop"),(DWORD, "ulPropTag"),(DWORD, "cb"),]

    

class EXISTRESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "ulReserved1"),(DWORD, "ulPropTag"),(DWORD, "ulReserved2"),]

    

class RESTRICTIONUNION_R(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ANDRESTRICTION_R, "resAnd"),2 : (ORRESTRICTION_R, "resOr"),3 : (NOTRESTRICTION_R, "resNot"),4 : (CONTENTRESTRICTION_R, "resContent"),5 : (PROPERTYRESTRICTION_R, "resProperty"),6 : (COMPAREPROPSRESTRICTION_R, "resCompareProps"),7 : (BITMASKRESTRICTION_R, "resBitMask"),8 : (SIZERESTRICTION_R, "resSize"),9 : (EXISTRESTRICTION_R, "resExist"),10 : (SUBRESTRICTION_R, "resSubRestriction"),}

    

class _RESTRICTION_R(NdrStructure):
    MEMBERS = [(DWORD, "rt"),(RESTRICTIONUNION_R, "res"),]

    

class PROPERTYNAME_R(NdrStructure):
    MEMBERS = [(PFLATUID_R, "lpguid"),(DWORD, "ulReserved"),(LONG, "lID"),]

    

class PROPERTYNAMESET_R(NdrStructure):
    MEMBERS = [(DWORD, "cNames"),(PROPERTYNAME_R, "aNames"),]

    

class STRINGSARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "Count"),(PCHAR, "Strings"),]

    

class WSTRINGSARRAY_R(NdrStructure):
    MEMBERS = [(DWORD, "Count"),(PWCHAR_T, "Strings"),]

    

class STAT(NdrStructure):
    MEMBERS = [(DWORD, "SortType"),(DWORD, "ContainerID"),(DWORD, "CurrentRec"),(LONG, "Delta"),(DWORD, "NumPos"),(DWORD, "TotalRecs"),(DWORD, "CodePage"),(DWORD, "TemplateLocale"),(DWORD, "SortLocale"),]

    

class PROP_VAL_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (SHORT_INT, "i"),2 : (LONG, "l"),3 : (UNSIGNED_SHORT_INT, "b"),4 : (PCHAR, "lpszA"),5 : (BINARY_R, "bin"),6 : (PWCHAR_T, "lpszW"),7 : (PFLATUID_R, "lpguid"),8 : (FILETIME, "ft"),9 : (LONG, "err"),10 : (SHORTARRAY_R, "MVi"),11 : (LONGARRAY_R, "MVl"),12 : (STRINGARRAY_R, "MVszA"),13 : (BINARYARRAY_R, "MVbin"),14 : (FLATUIDARRAY_R, "MVguid"),15 : (WSTRINGARRAY_R, "MVszW"),16 : (DATETIMEARRAY_R, "MVft"),17 : (LONG, "lReserved"),}

    

class _PROPERTYVALUE_R(NdrStructure):
    MEMBERS = [(DWORD, "ulPropTag"),(DWORD, "ulReserved"),(PROP_VAL_UNION, "Value"),]

    
NSPI_HANDLE = VOID
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