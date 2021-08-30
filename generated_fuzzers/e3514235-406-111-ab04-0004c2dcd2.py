
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
DSTIME = LONGLONG
DRS_HANDLE = VOID

class NT4SID(NdrStructure):
    MEMBERS = [(CHAR, "Data"),]

    

class DSNAME(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "structLen"),(UNSIGNED_LONG, "SidLen"),(GUID, "Guid"),(NT4SID, "Sid"),(UNSIGNED_LONG, "NameLen"),(WCHAR, "StringName"),]

    
USN = LONGLONG

class USN_VECTOR(NdrStructure):
    MEMBERS = [(USN, "usnHighObjUpdate"),(USN, "usnReserved"),(USN, "usnHighPropUpdate"),]

    

class UPTODATE_CURSOR_V1(NdrStructure):
    MEMBERS = [(UUID, "uuidDsa"),(USN, "usnHighPropUpdate"),]

    

class UPTODATE_VECTOR_V1_EXT(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwReserved1"),(DWORD, "cNumCursors"),(DWORD, "dwReserved2"),(UPTODATE_CURSOR_V1, "rgCursors"),]

    

class OID_T(NdrStructure):
    MEMBERS = [(UNSIGNED_INT, "length"),(PBYTE, "elements"),]

    

class PREFIXTABLEENTRY(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ndx"),(OID_T, "prefix"),]

    

class SCHEMA_PREFIX_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "PrefixCount"),(PPREFIXTABLEENTRY, "pPrefixEntry"),]

    
ATTRTYP = ULONG

class PARTIAL_ATTR_VECTOR_V1_EXT(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwReserved1"),(DWORD, "cAttrs"),(ATTRTYP, "rgPartialAttr"),]

    

class MTX_ADDR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "mtx_namelen"),(CHAR, "mtx_name"),]

    

class ATTRVAL(NdrStructure):
    MEMBERS = [(ULONG, "valLen"),(PUCHAR, "pVal"),]

    

class ATTRVALBLOCK(NdrStructure):
    MEMBERS = [(ULONG, "valCount"),(PATTRVAL, "pAVal"),]

    

class ATTR(NdrStructure):
    MEMBERS = [(ATTRTYP, "attrTyp"),(ATTRVALBLOCK, "AttrVal"),]

    

class ATTRBLOCK(NdrStructure):
    MEMBERS = [(ULONG, "attrCount"),(PATTR, "pAttr"),]

    

class ENTINF(NdrStructure):
    MEMBERS = [(PDSNAME, "pName"),(UNSIGNED_LONG, "ulFlags"),(ATTRBLOCK, "AttrBlock"),]

    

class PROPERTY_META_DATA_EXT(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DSTIME, "timeChanged"),(UUID, "uuidDsaOriginating"),(USN, "usnOriginating"),]

    

class PROPERTY_META_DATA_EXT_VECTOR(NdrStructure):
    MEMBERS = [(DWORD, "cNumProps"),(PROPERTY_META_DATA_EXT, "rgMetaData"),]

    

class REPLENTINFLIST(NdrStructure):
    MEMBERS = [(PPNEXTENTINF, "*pNextEntInf"),(ENTINF, "Entinf"),(BOOL, "fIsNCPrefix"),(PUUID, "pParentGuid"),(PPROPERTY_META_DATA_EXT_VECTOR, "pMetaDataExt"),]

    

class UPTODATE_CURSOR_V2(NdrStructure):
    MEMBERS = [(UUID, "uuidDsa"),(USN, "usnHighPropUpdate"),(DSTIME, "timeLastSyncSuccess"),]

    

class UPTODATE_VECTOR_V2_EXT(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwReserved1"),(DWORD, "cNumCursors"),(DWORD, "dwReserved2"),(UPTODATE_CURSOR_V2, "rgCursors"),]

    

class VALUE_META_DATA_EXT_V1(NdrStructure):
    MEMBERS = [(DSTIME, "timeCreated"),(PROPERTY_META_DATA_EXT, "MetaData"),]

    

class VALUE_META_DATA_EXT_V3(NdrStructure):
    MEMBERS = [(DSTIME, "timeCreated"),(PROPERTY_META_DATA_EXT, "MetaData"),(DWORD, "unused1"),(DWORD, "unused2"),(DWORD, "unused3"),(DSTIME, "timeExpired"),]

    

class REPLVALINF_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pObject"),(ATTRTYP, "attrTyp"),(ATTRVAL, "Aval"),(BOOL, "fIsPresent"),(VALUE_META_DATA_EXT_V1, "MetaData"),]

    

class REPLVALINF_V3(NdrStructure):
    MEMBERS = [(PDSNAME, "pObject"),(ATTRTYP, "attrTyp"),(ATTRVAL, "Aval"),(BOOL, "fIsPresent"),(VALUE_META_DATA_EXT_V3, "MetaData"),]

    

class REPLTIMES(NdrStructure):
    MEMBERS = [(UCHAR, "rgTimes"),]

    

class DS_NAME_RESULT_ITEMW(NdrStructure):
    MEMBERS = [(DWORD, "status"),(PWCHAR, "pDomain"),(PWCHAR, "pName"),]

    
PDS_NAME_RESULT_ITEMW = DS_NAME_RESULT_ITEMW

class DS_NAME_RESULTW(NdrStructure):
    MEMBERS = [(DWORD, "cItems"),(PDS_NAME_RESULT_ITEMW, "rItems"),]

    
PDS_NAME_RESULTW = DS_NAME_RESULTW

class DS_DOMAIN_CONTROLLER_INFO_1W(NdrStructure):
    MEMBERS = [(PWCHAR, "NetbiosName"),(PWCHAR, "DnsHostName"),(PWCHAR, "SiteName"),(PWCHAR, "ComputerObjectName"),(PWCHAR, "ServerObjectName"),(BOOL, "fIsPdc"),(BOOL, "fDsEnabled"),]

    

class DS_DOMAIN_CONTROLLER_INFO_2W(NdrStructure):
    MEMBERS = [(PWCHAR, "NetbiosName"),(PWCHAR, "DnsHostName"),(PWCHAR, "SiteName"),(PWCHAR, "SiteObjectName"),(PWCHAR, "ComputerObjectName"),(PWCHAR, "ServerObjectName"),(PWCHAR, "NtdsDsaObjectName"),(BOOL, "fIsPdc"),(BOOL, "fDsEnabled"),(BOOL, "fIsGc"),(GUID, "SiteObjectGuid"),(GUID, "ComputerObjectGuid"),(GUID, "ServerObjectGuid"),(GUID, "NtdsDsaObjectGuid"),]

    

class DS_DOMAIN_CONTROLLER_INFO_3W(NdrStructure):
    MEMBERS = [(PWCHAR, "NetbiosName"),(PWCHAR, "DnsHostName"),(PWCHAR, "SiteName"),(PWCHAR, "SiteObjectName"),(PWCHAR, "ComputerObjectName"),(PWCHAR, "ServerObjectName"),(PWCHAR, "NtdsDsaObjectName"),(BOOL, "fIsPdc"),(BOOL, "fDsEnabled"),(BOOL, "fIsGc"),(BOOL, "fIsRodc"),(GUID, "SiteObjectGuid"),(GUID, "ComputerObjectGuid"),(GUID, "ServerObjectGuid"),(GUID, "NtdsDsaObjectGuid"),]

    

class DS_DOMAIN_CONTROLLER_INFO_FFFFFFFFW(NdrStructure):
    MEMBERS = [(DWORD, "IPAddress"),(DWORD, "NotificationCount"),(DWORD, "secTimeConnected"),(DWORD, "Flags"),(DWORD, "TotalRequests"),(DWORD, "Reserved1"),(PWCHAR, "UserName"),]

    

class ENTINFLIST(NdrStructure):
    MEMBERS = [(PPNEXTENTINF, "*pNextEntInf"),(ENTINF, "Entinf"),]

    

class INTFORMPROB_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),(ATTRTYP, "type"),(BOOL, "valReturned"),(ATTRVAL, "Val"),]

    

class PROBLEMLIST_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(PPNEXTPROBLEM, "*pNextProblem"),(INTFORMPROB_DRS_WIRE_V1, "intprob"),]

    

class ATRERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pObject"),(ULONG, "count"),(PROBLEMLIST_DRS_WIRE_V1, "FirstProblem"),]

    

class NAMERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),(PDSNAME, "pMatched"),]

    

class NAMERESOP_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(UCHAR, "nameRes"),(UCHAR, "unusedPad"),(USHORT, "nextRDN"),]

    

class DSA_ADDRESS_LIST_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(PPNEXTADDRESS, "*pNextAddress"),(PRPC_UNICODE_STRING, "pAddress"),]

    

class CONTREF_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pTarget"),(NAMERESOP_DRS_WIRE_V1, "OpState"),(USHORT, "aliasRDN"),(USHORT, "RDNsInternal"),(USHORT, "refType"),(USHORT, "count"),(PDSA_ADDRESS_LIST_DRS_WIRE_V1, "pDAL"),(PPNEXTCONTREF, "*pNextContRef"),(BOOL, "bNewChoice"),(UCHAR, "choice"),]

    

class REFERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(CONTREF_DRS_WIRE_V1, "Refer"),]

    

class SECERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),]

    

class SVCERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),]

    

class UPDERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),]

    

class SYSERR_DRS_WIRE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),]

    

class DIRERR_DRS_WIRE_V1(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ATRERR_DRS_WIRE_V1, "AtrErr"),2 : (NAMERR_DRS_WIRE_V1, "NamErr"),3 : (REFERR_DRS_WIRE_V1, "RefErr"),4 : (SECERR_DRS_WIRE_V1, "SecErr"),5 : (SVCERR_DRS_WIRE_V1, "SvcErr"),6 : (UPDERR_DRS_WIRE_V1, "UpdErr"),7 : (SYSERR_DRS_WIRE_V1, "SysErr"),}

    

class DS_REPL_NEIGHBORW(NdrStructure):
    MEMBERS = [(LPWSTR, "pszNamingContext"),(LPWSTR, "pszSourceDsaDN"),(LPWSTR, "pszSourceDsaAddress"),(LPWSTR, "pszAsyncIntersiteTransportDN"),(DWORD, "dwReplicaFlags"),(DWORD, "dwReserved"),(UUID, "uuidNamingContextObjGuid"),(UUID, "uuidSourceDsaObjGuid"),(UUID, "uuidSourceDsaInvocationID"),(UUID, "uuidAsyncIntersiteTransportObjGuid"),(USN, "usnLastObjChangeSynced"),(USN, "usnAttributeFilter"),(FILETIME, "ftimeLastSyncSuccess"),(FILETIME, "ftimeLastSyncAttempt"),(DWORD, "dwLastSyncResult"),(DWORD, "cNumConsecutiveSyncFailures"),]

    

class DS_REPL_NEIGHBORSW(NdrStructure):
    MEMBERS = [(DWORD, "cNumNeighbors"),(DWORD, "dwReserved"),(DS_REPL_NEIGHBORW, "rgNeighbor"),]

    

class DS_REPL_CURSOR(NdrStructure):
    MEMBERS = [(UUID, "uuidSourceDsaInvocationID"),(USN, "usnAttributeFilter"),]

    

class DS_REPL_CURSORS(NdrStructure):
    MEMBERS = [(DWORD, "cNumCursors"),(DWORD, "dwReserved"),(DS_REPL_CURSOR, "rgCursor"),]

    

class DS_REPL_ATTR_META_DATA(NdrStructure):
    MEMBERS = [(LPWSTR, "pszAttributeName"),(DWORD, "dwVersion"),(FILETIME, "ftimeLastOriginatingChange"),(UUID, "uuidLastOriginatingDsaInvocationID"),(USN, "usnOriginatingChange"),(USN, "usnLocalChange"),]

    

class DS_REPL_KCC_DSA_FAILUREW(NdrStructure):
    MEMBERS = [(LPWSTR, "pszDsaDN"),(UUID, "uuidDsaObjGuid"),(FILETIME, "ftimeFirstFailure"),(DWORD, "cNumFailures"),(DWORD, "dwLastResult"),]

    

class DS_REPL_KCC_DSA_FAILURESW(NdrStructure):
    MEMBERS = [(DWORD, "cNumEntries"),(DWORD, "dwReserved"),(DS_REPL_KCC_DSA_FAILUREW, "rgDsaFailure"),]

    

class DS_REPL_OBJ_META_DATA(NdrStructure):
    MEMBERS = [(DWORD, "cNumEntries"),(DWORD, "dwReserved"),(DS_REPL_ATTR_META_DATA, "rgMetaData"),]

    

class DS_REPL_OPW(NdrStructure):
    MEMBERS = [(FILETIME, "ftimeEnqueued"),(ULONG, "ulSerialNumber"),(ULONG, "ulPriority"),(DS_REPL_OP_TYPE, "OpType"),(ULONG, "ulOptions"),(LPWSTR, "pszNamingContext"),(LPWSTR, "pszDsaDN"),(LPWSTR, "pszDsaAddress"),(UUID, "uuidNamingContextObjGuid"),(UUID, "uuidDsaObjGuid"),]

    

class DS_REPL_PENDING_OPSW(NdrStructure):
    MEMBERS = [(FILETIME, "ftimeCurrentOpStarted"),(DWORD, "cNumPendingOps"),(DS_REPL_OPW, "rgPendingOp"),]

    

class DS_REPL_VALUE_META_DATA(NdrStructure):
    MEMBERS = [(LPWSTR, "pszAttributeName"),(LPWSTR, "pszObjectDn"),(DWORD, "cbData"),(PBYTE, "pbData"),(FILETIME, "ftimeDeleted"),(FILETIME, "ftimeCreated"),(DWORD, "dwVersion"),(FILETIME, "ftimeLastOriginatingChange"),(UUID, "uuidLastOriginatingDsaInvocationID"),(USN, "usnOriginatingChange"),(USN, "usnLocalChange"),]

    

class DS_REPL_ATTR_VALUE_META_DATA(NdrStructure):
    MEMBERS = [(DWORD, "cNumEntries"),(DWORD, "dwEnumerationContext"),(DS_REPL_VALUE_META_DATA, "rgMetaData"),]

    

class DS_REPL_CURSOR_2(NdrStructure):
    MEMBERS = [(UUID, "uuidSourceDsaInvocationID"),(USN, "usnAttributeFilter"),(FILETIME, "ftimeLastSyncSuccess"),]

    

class DS_REPL_CURSORS_2(NdrStructure):
    MEMBERS = [(DWORD, "cNumCursors"),(DWORD, "dwEnumerationContext"),(DS_REPL_CURSOR_2, "rgCursor"),]

    

class DS_REPL_CURSOR_3W(NdrStructure):
    MEMBERS = [(UUID, "uuidSourceDsaInvocationID"),(USN, "usnAttributeFilter"),(FILETIME, "ftimeLastSyncSuccess"),(LPWSTR, "pszSourceDsaDN"),]

    

class DS_REPL_CURSORS_3W(NdrStructure):
    MEMBERS = [(DWORD, "cNumCursors"),(DWORD, "dwEnumerationContext"),(DS_REPL_CURSOR_3W, "rgCursor"),]

    

class DS_REPL_ATTR_META_DATA_2(NdrStructure):
    MEMBERS = [(LPWSTR, "pszAttributeName"),(DWORD, "dwVersion"),(FILETIME, "ftimeLastOriginatingChange"),(UUID, "uuidLastOriginatingDsaInvocationID"),(USN, "usnOriginatingChange"),(USN, "usnLocalChange"),(LPWSTR, "pszLastOriginatingDsaDN"),]

    

class DS_REPL_OBJ_META_DATA_2(NdrStructure):
    MEMBERS = [(DWORD, "cNumEntries"),(DWORD, "dwReserved"),(DS_REPL_ATTR_META_DATA_2, "rgMetaData"),]

    

class DS_REPL_VALUE_META_DATA_2(NdrStructure):
    MEMBERS = [(LPWSTR, "pszAttributeName"),(LPWSTR, "pszObjectDn"),(DWORD, "cbData"),(PBYTE, "pbData"),(FILETIME, "ftimeDeleted"),(FILETIME, "ftimeCreated"),(DWORD, "dwVersion"),(FILETIME, "ftimeLastOriginatingChange"),(UUID, "uuidLastOriginatingDsaInvocationID"),(USN, "usnOriginatingChange"),(USN, "usnLocalChange"),(LPWSTR, "pszLastOriginatingDsaDN"),]

    

class DS_REPL_ATTR_VALUE_META_DATA_2(NdrStructure):
    MEMBERS = [(DWORD, "cNumEntries"),(DWORD, "dwEnumerationContext"),(DS_REPL_VALUE_META_DATA_2, "rgMetaData"),]

    

class DRS_EXTENSIONS(NdrStructure):
    MEMBERS = [(DWORD, "cb"),(BYTE, "rgb"),]

    

class DRS_MSG_GETCHGREQ_V3(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjDest"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecDestV1"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrVecDestV1"),(SCHEMA_PREFIX_TABLE, "PrefixTableDest"),(ULONG, "ulFlags"),(ULONG, "cMaxObjects"),(ULONG, "cMaxBytes"),(ULONG, "ulExtendedOp"),]

    

class DRS_MSG_GETCHGREQ_V4(NdrStructure):
    MEMBERS = [(UUID, "uuidTransportObj"),(PMTX_ADDR, "pmtxReturnAddress"),(DRS_MSG_GETCHGREQ_V3, "V3"),]

    

class DRS_MSG_GETCHGREQ_V7(NdrStructure):
    MEMBERS = [(UUID, "uuidTransportObj"),(PMTX_ADDR, "pmtxReturnAddress"),(DRS_MSG_GETCHGREQ_V3, "V3"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSet"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSetEx"),(SCHEMA_PREFIX_TABLE, "PrefixTableDest"),]

    

class DRS_MSG_GETCHGREPLY_V1(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjSrc"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(USN_VECTOR, "usnvecTo"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecSrcV1"),(SCHEMA_PREFIX_TABLE, "PrefixTableSrc"),(ULONG, "ulExtendedRet"),(ULONG, "cNumObjects"),(ULONG, "cNumBytes"),(PREPLENTINFLIST, "pObjects"),(BOOL, "fMoreData"),]

    

class DRS_MSG_GETCHGREPLY_V6(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjSrc"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(USN_VECTOR, "usnvecTo"),(PUPTODATE_VECTOR_V2_EXT, "pUpToDateVecSrc"),(SCHEMA_PREFIX_TABLE, "PrefixTableSrc"),(ULONG, "ulExtendedRet"),(ULONG, "cNumObjects"),(ULONG, "cNumBytes"),(PREPLENTINFLIST, "pObjects"),(BOOL, "fMoreData"),(ULONG, "cNumNcSizeObjects"),(ULONG, "cNumNcSizeValues"),(DWORD, "cNumValues"),(PREPLVALINF_V1, "rgValues"),(DWORD, "dwDRSError"),]

    

class DRS_MSG_GETCHGREPLY_V9(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjSrc"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(USN_VECTOR, "usnvecTo"),(PUPTODATE_VECTOR_V2_EXT, "pUpToDateVecSrc"),(SCHEMA_PREFIX_TABLE, "PrefixTableSrc"),(ULONG, "ulExtendedRet"),(ULONG, "cNumObjects"),(ULONG, "cNumBytes"),(PREPLENTINFLIST, "pObjects"),(BOOL, "fMoreData"),(ULONG, "cNumNcSizeObjects"),(ULONG, "cNumNcSizeValues"),(DWORD, "cNumValues"),(PREPLVALINF_V3, "rgValues"),(DWORD, "dwDRSError"),]

    

class DRS_COMPRESSED_BLOB(NdrStructure):
    MEMBERS = [(DWORD, "cbUncompressedSize"),(DWORD, "cbCompressedSize"),(PBYTE, "pbCompressedData"),]

    

class DRS_MSG_GETCHGREQ_V5(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjDest"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecDestV1"),(ULONG, "ulFlags"),(ULONG, "cMaxObjects"),(ULONG, "cMaxBytes"),(ULONG, "ulExtendedOp"),(ULARGE_INTEGER, "liFsmoInfo"),]

    

class DRS_MSG_GETCHGREQ_V8(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjDest"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecDest"),(ULONG, "ulFlags"),(ULONG, "cMaxObjects"),(ULONG, "cMaxBytes"),(ULONG, "ulExtendedOp"),(ULARGE_INTEGER, "liFsmoInfo"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSet"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSetEx"),(SCHEMA_PREFIX_TABLE, "PrefixTableDest"),]

    

class DRS_MSG_GETCHGREQ_V10(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjDest"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecDest"),(ULONG, "ulFlags"),(ULONG, "cMaxObjects"),(ULONG, "cMaxBytes"),(ULONG, "ulExtendedOp"),(ULARGE_INTEGER, "liFsmoInfo"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSet"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSetEx"),(SCHEMA_PREFIX_TABLE, "PrefixTableDest"),(ULONG, "ulMoreFlags"),]

    

class VAR_SIZE_BUFFER_WITH_VERSION(NdrStructure):
    MEMBERS = [(ULONG, "ulVersion"),(ULONG, "cbByteBuffer"),(ULONGLONG, "ullPadding"),(BYTE, "rgbBuffer"),]

    

class DRS_MSG_GETCHGREQ_V11(NdrStructure):
    MEMBERS = [(UUID, "uuidDsaObjDest"),(UUID, "uuidInvocIdSrc"),(PDSNAME, "pNC"),(USN_VECTOR, "usnvecFrom"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecDest"),(ULONG, "ulFlags"),(ULONG, "cMaxObjects"),(ULONG, "cMaxBytes"),(ULONG, "ulExtendedOp"),(ULARGE_INTEGER, "liFsmoInfo"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSet"),(PPARTIAL_ATTR_VECTOR_V1_EXT, "pPartialAttrSetEx"),(SCHEMA_PREFIX_TABLE, "PrefixTableDest"),(ULONG, "ulMoreFlags"),(GUID, "correlationID"),(PVAR_SIZE_BUFFER_WITH_VERSION, "pReservedBuffer"),]

    

class DRS_MSG_GETCHGREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_GETCHGREQ_V4, "V4"),2 : (DRS_MSG_GETCHGREQ_V5, "V5"),3 : (DRS_MSG_GETCHGREQ_V7, "V7"),4 : (DRS_MSG_GETCHGREQ_V8, "V8"),5 : (DRS_MSG_GETCHGREQ_V10, "V10"),6 : (DRS_MSG_GETCHGREQ_V11, "V11"),}

    

class DRS_MSG_GETCHGREPLY_V2(NdrStructure):
    MEMBERS = [(DRS_COMPRESSED_BLOB, "CompressedV1"),]

    

class DRS_MSG_GETCHGREPLY_V7(NdrStructure):
    MEMBERS = [(DWORD, "dwCompressedVersion"),(DRS_COMP_ALG_TYPE, "CompressionAlg"),(DRS_COMPRESSED_BLOB, "CompressedAny"),]

    

class DRS_MSG_GETCHGREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_GETCHGREPLY_V1, "V1"),2 : (DRS_MSG_GETCHGREPLY_V2, "V2"),3 : (DRS_MSG_GETCHGREPLY_V6, "V6"),4 : (DRS_MSG_GETCHGREPLY_V7, "V7"),5 : (DRS_MSG_GETCHGREPLY_V9, "V9"),}

    

class DRS_MSG_REPSYNC_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(UUID, "uuidDsaSrc"),(PCHAR, "pszDsaSrc"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPSYNC_V2(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(UUID, "uuidDsaSrc"),(PCHAR, "pszDsaSrc"),(ULONG, "ulOptions"),(GUID, "correlationID"),(PVAR_SIZE_BUFFER_WITH_VERSION, "pReservedBuffer"),]

    

class DRS_MSG_REPSYNC(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPSYNC_V1, "V1"),2 : (DRS_MSG_REPSYNC_V2, "V2"),}

    

class DRS_MSG_UPDREFS_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PCHAR, "pszDsaDest"),(UUID, "uuidDsaObjDest"),(ULONG, "ulOptions"),]

    

class DRS_MSG_UPDREFS_V2(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PCHAR, "pszDsaDest"),(UUID, "uuidDsaObjDest"),(ULONG, "ulOptions"),(GUID, "correlationID"),(PVAR_SIZE_BUFFER_WITH_VERSION, "pReservedBuffer"),]

    

class DRS_MSG_UPDREFS(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_UPDREFS_V1, "V1"),2 : (DRS_MSG_UPDREFS_V2, "V2"),}

    

class DRS_MSG_REPADD_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PCHAR, "pszDsaSrc"),(REPLTIMES, "rtSchedule"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPADD_V2(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PDSNAME, "pSourceDsaDN"),(PDSNAME, "pTransportDN"),(PCHAR, "pszSourceDsaAddress"),(REPLTIMES, "rtSchedule"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPADD_V3(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PDSNAME, "pSourceDsaDN"),(PDSNAME, "pTransportDN"),(PCHAR, "pszSourceDsaAddress"),(REPLTIMES, "rtSchedule"),(ULONG, "ulOptions"),(GUID, "correlationID"),(PVAR_SIZE_BUFFER_WITH_VERSION, "pReservedBuffer"),]

    

class DRS_MSG_REPADD(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPADD_V1, "V1"),2 : (DRS_MSG_REPADD_V2, "V2"),3 : (DRS_MSG_REPADD_V3, "V3"),}

    

class DRS_MSG_REPDEL_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(PCHAR, "pszDsaSrc"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPDEL(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPDEL_V1, "V1"),}

    

class DRS_MSG_REPMOD_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(UUID, "uuidSourceDRA"),(PCHAR, "pszSourceDRA"),(REPLTIMES, "rtSchedule"),(ULONG, "ulReplicaFlags"),(ULONG, "ulModifyFields"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPMOD(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPMOD_V1, "V1"),}

    

class DRS_MSG_VERIFYREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwFlags"),(DWORD, "cNames"),(PPDSNAME, "rpNames"),(ATTRBLOCK, "RequiredAttrs"),(SCHEMA_PREFIX_TABLE, "PrefixTable"),]

    

class DRS_MSG_VERIFYREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_VERIFYREQ_V1, "V1"),}

    

class DRS_MSG_VERIFYREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "error"),(DWORD, "cNames"),(PENTINF, "rpEntInf"),(SCHEMA_PREFIX_TABLE, "PrefixTable"),]

    

class DRS_MSG_VERIFYREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_VERIFYREPLY_V1, "V1"),}

    

class DRS_MSG_REVMEMB_REQ_V1(NdrStructure):
    MEMBERS = [(ULONG, "cDsNames"),(PPDSNAME, "ppDsNames"),(DWORD, "dwFlags"),(REVERSE_MEMBERSHIP_OPERATION_TYPE, "OperationType"),(PDSNAME, "pLimitingDomain"),]

    

class DRS_MSG_REVMEMB_REQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REVMEMB_REQ_V1, "V1"),}

    

class DRS_MSG_REVMEMB_REPLY_V1(NdrStructure):
    MEMBERS = [(ULONG, "errCode"),(ULONG, "cDsNames"),(ULONG, "cSidHistory"),(PPDSNAME, "ppDsNames"),(PDWORD, "pAttributes"),(PPNT4SID, "ppSidHistory"),]

    

class DRS_MSG_REVMEMB_REPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REVMEMB_REPLY_V1, "V1"),}

    

class DRS_MSG_MOVEREQ_V1(NdrStructure):
    MEMBERS = [(PCHAR, "pSourceDSA"),(PENTINF, "pObject"),(PUUID, "pParentUUID"),(SCHEMA_PREFIX_TABLE, "PrefixTable"),(ULONG, "ulFlags"),]

    

class DRS_SECBUFFER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cbBuffer"),(UNSIGNED_LONG, "BufferType"),(PBYTE, "pvBuffer"),]

    

class DRS_SECBUFFERDESC(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulVersion"),(UNSIGNED_LONG, "cBuffers"),(PDRS_SECBUFFER, "Buffers"),]

    

class DRS_MSG_MOVEREQ_V2(NdrStructure):
    MEMBERS = [(PDSNAME, "pSrcDSA"),(PENTINF, "pSrcObject"),(PDSNAME, "pDstName"),(PDSNAME, "pExpectedTargetNC"),(PDRS_SECBUFFERDESC, "pClientCreds"),(SCHEMA_PREFIX_TABLE, "PrefixTable"),(ULONG, "ulFlags"),]

    

class DRS_MSG_MOVEREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_MOVEREQ_V1, "V1"),2 : (DRS_MSG_MOVEREQ_V2, "V2"),}

    

class DRS_MSG_MOVEREPLY_V1(NdrStructure):
    MEMBERS = [(PPENTINF, "ppResult"),(SCHEMA_PREFIX_TABLE, "PrefixTable"),(PULONG, "pError"),]

    

class DRS_MSG_MOVEREPLY_V2(NdrStructure):
    MEMBERS = [(ULONG, "win32Error"),(PDSNAME, "pAddedName"),]

    

class DRS_MSG_MOVEREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_MOVEREPLY_V1, "V1"),2 : (DRS_MSG_MOVEREPLY_V2, "V2"),}

    

class DRS_MSG_CRACKREQ_V1(NdrStructure):
    MEMBERS = [(ULONG, "CodePage"),(ULONG, "LocaleId"),(DWORD, "dwFlags"),(DWORD, "formatOffered"),(DWORD, "formatDesired"),(DWORD, "cNames"),(PPWCHAR, "rpNames"),]

    

class DRS_MSG_CRACKREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_CRACKREQ_V1, "V1"),}

    

class DRS_MSG_CRACKREPLY_V1(NdrStructure):
    MEMBERS = [(PDS_NAME_RESULTW, "pResult"),]

    

class DRS_MSG_CRACKREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_CRACKREPLY_V1, "V1"),}

    

class DRS_MSG_NT4_CHGLOG_REQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwFlags"),(DWORD, "PreferredMaximumLength"),(DWORD, "cbRestart"),(PBYTE, "pRestart"),]

    

class DRS_MSG_NT4_CHGLOG_REQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_NT4_CHGLOG_REQ_V1, "V1"),}

    

class NT4_REPLICATION_STATE(NdrStructure):
    MEMBERS = [(LARGE_INTEGER, "SamSerialNumber"),(LARGE_INTEGER, "SamCreationTime"),(LARGE_INTEGER, "BuiltinSerialNumber"),(LARGE_INTEGER, "BuiltinCreationTime"),(LARGE_INTEGER, "LsaSerialNumber"),(LARGE_INTEGER, "LsaCreationTime"),]

    

class DRS_MSG_NT4_CHGLOG_REPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "cbRestart"),(DWORD, "cbLog"),(NT4_REPLICATION_STATE, "ReplicationState"),(DWORD, "ActualNtStatus"),(PBYTE, "pRestart"),(PBYTE, "pLog"),]

    

class DRS_MSG_NT4_CHGLOG_REPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_NT4_CHGLOG_REPLY_V1, "V1"),}

    

class DRS_MSG_SPNREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "operation"),(DWORD, "flags"),(PWCHAR, "pwszAccount"),(DWORD, "cSPN"),(PPWCHAR, "rpwszSPN"),]

    

class DRS_MSG_SPNREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_SPNREQ_V1, "V1"),}

    

class DRS_MSG_SPNREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "retVal"),]

    

class DRS_MSG_SPNREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_SPNREPLY_V1, "V1"),}

    

class DRS_MSG_RMSVRREQ_V1(NdrStructure):
    MEMBERS = [(LPWSTR, "ServerDN"),(LPWSTR, "DomainDN"),(BOOL, "fCommit"),]

    

class DRS_MSG_RMSVRREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_RMSVRREQ_V1, "V1"),}

    

class DRS_MSG_RMSVRREPLY_V1(NdrStructure):
    MEMBERS = [(BOOL, "fLastDcInDomain"),]

    

class DRS_MSG_RMSVRREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_RMSVRREPLY_V1, "V1"),}

    

class DRS_MSG_RMDMNREQ_V1(NdrStructure):
    MEMBERS = [(LPWSTR, "DomainDN"),]

    

class DRS_MSG_RMDMNREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_RMDMNREQ_V1, "V1"),}

    

class DRS_MSG_RMDMNREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "Reserved"),]

    

class DRS_MSG_RMDMNREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_RMDMNREPLY_V1, "V1"),}

    

class DRS_MSG_DCINFOREQ_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "Domain"),(DWORD, "InfoLevel"),]

    

class DRS_MSG_DCINFOREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_DCINFOREQ_V1, "V1"),}

    
PDRS_MSG_DCINFOREQ = DRS_MSG_DCINFOREQ

class DRS_MSG_DCINFOREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "cItems"),(PDS_DOMAIN_CONTROLLER_INFO_1W, "rItems"),]

    

class DRS_MSG_DCINFOREPLY_V2(NdrStructure):
    MEMBERS = [(DWORD, "cItems"),(PDS_DOMAIN_CONTROLLER_INFO_2W, "rItems"),]

    

class DRS_MSG_DCINFOREPLY_V3(NdrStructure):
    MEMBERS = [(DWORD, "cItems"),(PDS_DOMAIN_CONTROLLER_INFO_3W, "rItems"),]

    

class DRS_MSG_DCINFOREPLY_VFFFFFFFF(NdrStructure):
    MEMBERS = [(DWORD, "cItems"),(PDS_DOMAIN_CONTROLLER_INFO_FFFFFFFFW, "rItems"),]

    

class DRS_MSG_DCINFOREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_DCINFOREPLY_V1, "V1"),2 : (DRS_MSG_DCINFOREPLY_V2, "V2"),3 : (DRS_MSG_DCINFOREPLY_V3, "V3"),4 : (DRS_MSG_DCINFOREPLY_VFFFFFFFF, "VFFFFFFFF"),}

    

class DRS_MSG_ADDENTRYREQ_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pObject"),(ATTRBLOCK, "AttrBlock"),]

    

class DRS_MSG_ADDENTRYREQ_V2(NdrStructure):
    MEMBERS = [(ENTINFLIST, "EntInfList"),]

    

class DRS_MSG_ADDENTRYREQ_V3(NdrStructure):
    MEMBERS = [(ENTINFLIST, "EntInfList"),(PDRS_SECBUFFERDESC, "pClientCreds"),]

    

class DRS_MSG_ADDENTRYREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDENTRYREQ_V1, "V1"),2 : (DRS_MSG_ADDENTRYREQ_V2, "V2"),3 : (DRS_MSG_ADDENTRYREQ_V3, "V3"),}

    

class DRS_MSG_ADDENTRYREPLY_V1(NdrStructure):
    MEMBERS = [(GUID, "Guid"),(NT4SID, "Sid"),(DWORD, "errCode"),(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),]

    

class ADDENTRY_REPLY_INFO(NdrStructure):
    MEMBERS = [(GUID, "objGuid"),(NT4SID, "objSid"),]

    

class DRS_MSG_ADDENTRYREPLY_V2(NdrStructure):
    MEMBERS = [(PDSNAME, "pErrorObject"),(DWORD, "errCode"),(DWORD, "dsid"),(DWORD, "extendedErr"),(DWORD, "extendedData"),(USHORT, "problem"),(ULONG, "cObjectsAdded"),(PADDENTRY_REPLY_INFO, "infoList"),]

    

class DRS_ERROR_DATA_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwRepError"),(DWORD, "errCode"),(PDIRERR_DRS_WIRE_V1, "pErrInfo"),]

    

class DRS_ERROR_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_ERROR_DATA_V1, "V1"),}

    

class DRS_MSG_ADDENTRYREPLY_V3(NdrStructure):
    MEMBERS = [(PDSNAME, "pdsErrObject"),(DWORD, "dwErrVer"),(PDRS_ERROR_DATA, "pErrData"),(ULONG, "cObjectsAdded"),(PADDENTRY_REPLY_INFO, "infoList"),]

    

class DRS_MSG_ADDENTRYREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDENTRYREPLY_V1, "V1"),2 : (DRS_MSG_ADDENTRYREPLY_V2, "V2"),3 : (DRS_MSG_ADDENTRYREPLY_V3, "V3"),}

    

class DRS_MSG_KCC_EXECUTE_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwTaskID"),(DWORD, "dwFlags"),]

    

class DRS_MSG_KCC_EXECUTE(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_KCC_EXECUTE_V1, "V1"),}

    

class DS_REPL_CLIENT_CONTEXT(NdrStructure):
    MEMBERS = [(ULONGLONG, "hCtx"),(LONG, "lReferenceCount"),(BOOL, "fIsBound"),(UUID, "uuidClient"),(DSTIME, "timeLastUsed"),(ULONG, "IPAddr"),(INT, "pid"),]

    

class DS_REPL_CLIENT_CONTEXTS(NdrStructure):
    MEMBERS = [(DWORD, "cNumContexts"),(DWORD, "dwReserved"),(DS_REPL_CLIENT_CONTEXT, "rgContext"),]

    

class DS_REPL_SERVER_OUTGOING_CALL(NdrStructure):
    MEMBERS = [(LPWSTR, "pszServerName"),(BOOL, "fIsHandleBound"),(BOOL, "fIsHandleFromCache"),(BOOL, "fIsHandleInCache"),(DWORD, "dwThreadId"),(DWORD, "dwBindingTimeoutMins"),(DSTIME, "dstimeCreated"),(DWORD, "dwCallType"),]

    

class DS_REPL_SERVER_OUTGOING_CALLS(NdrStructure):
    MEMBERS = [(DWORD, "cNumCalls"),(DWORD, "dwReserved"),(DS_REPL_SERVER_OUTGOING_CALL, "rgCall"),]

    

class DRS_MSG_GETREPLINFO_REQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "InfoType"),(LPWSTR, "pszObjectDN"),(UUID, "uuidSourceDsaObjGuid"),]

    

class DRS_MSG_GETREPLINFO_REQ_V2(NdrStructure):
    MEMBERS = [(DWORD, "InfoType"),(LPWSTR, "pszObjectDN"),(UUID, "uuidSourceDsaObjGuid"),(DWORD, "ulFlags"),(LPWSTR, "pszAttributeName"),(LPWSTR, "pszValueDN"),(DWORD, "dwEnumerationContext"),]

    

class DRS_MSG_GETREPLINFO_REQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_GETREPLINFO_REQ_V1, "V1"),2 : (DRS_MSG_GETREPLINFO_REQ_V2, "V2"),}

    

class DRS_MSG_GETREPLINFO_REPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PDS_REPL_NEIGHBORSW, "pNeighbors"),2 : (PDS_REPL_CURSORS, "pCursors"),3 : (PDS_REPL_OBJ_META_DATA, "pObjMetaData"),4 : (PDS_REPL_KCC_DSA_FAILURESW, "pConnectFailures"),5 : (PDS_REPL_KCC_DSA_FAILURESW, "pLinkFailures"),6 : (PDS_REPL_PENDING_OPSW, "pPendingOps"),7 : (PDS_REPL_ATTR_VALUE_META_DATA, "pAttrValueMetaData"),8 : (PDS_REPL_CURSORS_2, "pCursors2"),9 : (PDS_REPL_CURSORS_3W, "pCursors3"),10 : (PDS_REPL_OBJ_META_DATA_2, "pObjMetaData2"),11 : (PDS_REPL_ATTR_VALUE_META_DATA_2, "pAttrValueMetaData2"),12 : (PDS_REPL_SERVER_OUTGOING_CALLS, "pServerOutgoingCalls"),13 : (PUPTODATE_VECTOR_V1_EXT, "pUpToDateVec"),14 : (PDS_REPL_CLIENT_CONTEXTS, "pClientContexts"),15 : (PDS_REPL_NEIGHBORSW, "pRepsTo"),}

    

class DRS_MSG_ADDSIDREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(PWCHAR, "SrcDomain"),(PWCHAR, "SrcPrincipal"),(PWCHAR, "SrcDomainController"),(DWORD, "SrcCredsUserLength"),(PWCHAR, "SrcCredsUser"),(DWORD, "SrcCredsDomainLength"),(PWCHAR, "SrcCredsDomain"),(DWORD, "SrcCredsPasswordLength"),(PWCHAR, "SrcCredsPassword"),(PWCHAR, "DstDomain"),(PWCHAR, "DstPrincipal"),]

    

class DRS_MSG_ADDSIDREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDSIDREQ_V1, "V1"),}

    

class DRS_MSG_ADDSIDREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwWin32Error"),]

    

class DRS_MSG_ADDSIDREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDSIDREPLY_V1, "V1"),}

    

class DRS_MSG_GETMEMBERSHIPS2_REQ_V1(NdrStructure):
    MEMBERS = [(ULONG, "Count"),(PDRS_MSG_REVMEMB_REQ_V1, "Requests"),]

    

class DRS_MSG_GETMEMBERSHIPS2_REQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_GETMEMBERSHIPS2_REQ_V1, "V1"),}

    

class DRS_MSG_GETMEMBERSHIPS2_REPLY_V1(NdrStructure):
    MEMBERS = [(ULONG, "Count"),(PDRS_MSG_REVMEMB_REPLY_V1, "Replies"),]

    

class DRS_MSG_GETMEMBERSHIPS2_REPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_GETMEMBERSHIPS2_REPLY_V1, "V1"),}

    

class DRS_MSG_REPVERIFYOBJ_V1(NdrStructure):
    MEMBERS = [(PDSNAME, "pNC"),(UUID, "uuidDsaSrc"),(ULONG, "ulOptions"),]

    

class DRS_MSG_REPVERIFYOBJ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPVERIFYOBJ_V1, "V1"),}

    

class DRS_MSG_EXISTREQ_V1(NdrStructure):
    MEMBERS = [(UUID, "guidStart"),(DWORD, "cGuids"),(PDSNAME, "pNC"),(PUPTODATE_VECTOR_V1_EXT, "pUpToDateVecCommonV1"),(UCHAR, "Md5Digest"),]

    

class DRS_MSG_EXISTREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_EXISTREQ_V1, "V1"),}

    

class DRS_MSG_EXISTREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwStatusFlags"),(DWORD, "cNumGuids"),(PUUID, "rgGuids"),]

    

class DRS_MSG_EXISTREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_EXISTREPLY_V1, "V1"),}

    

class DRS_MSG_QUERYSITESREQ_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszFromSite"),(DWORD, "cToSites"),(PPWCHAR, "rgszToSites"),(DWORD, "dwFlags"),]

    

class DRS_MSG_QUERYSITESREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_QUERYSITESREQ_V1, "V1"),}

    

class DRS_MSG_QUERYSITESREPLYELEMENT_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwErrorCode"),(DWORD, "dwCost"),]

    

class DRS_MSG_QUERYSITESREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "cToSites"),(PDRS_MSG_QUERYSITESREPLYELEMENT_V1, "rgCostInfo"),(DWORD, "dwFlags"),]

    

class DRS_MSG_QUERYSITESREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_QUERYSITESREPLY_V1, "V1"),}

    

class DRS_MSG_INIT_DEMOTIONREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwReserved"),]

    

class DRS_MSG_INIT_DEMOTIONREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_INIT_DEMOTIONREQ_V1, "V1"),}

    

class DRS_MSG_INIT_DEMOTIONREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwOpError"),]

    

class DRS_MSG_INIT_DEMOTIONREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_INIT_DEMOTIONREPLY_V1, "V1"),}

    

class DRS_MSG_REPLICA_DEMOTIONREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwFlags"),(UUID, "uuidHelperDest"),(PDSNAME, "pNC"),]

    

class DRS_MSG_REPLICA_DEMOTIONREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPLICA_DEMOTIONREQ_V1, "V1"),}

    

class DRS_MSG_REPLICA_DEMOTIONREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwOpError"),]

    

class DRS_MSG_REPLICA_DEMOTIONREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_REPLICA_DEMOTIONREPLY_V1, "V1"),}

    

class DRS_MSG_FINISH_DEMOTIONREQ_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwOperations"),(UUID, "uuidHelperDest"),(LPWSTR, "szScriptBase"),]

    

class DRS_MSG_FINISH_DEMOTIONREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_FINISH_DEMOTIONREQ_V1, "V1"),}

    

class DRS_MSG_FINISH_DEMOTIONREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "dwOperationsDone"),(DWORD, "dwOpFailed"),(DWORD, "dwOpError"),]

    

class DRS_MSG_FINISH_DEMOTIONREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_FINISH_DEMOTIONREPLY_V1, "V1"),}

    

class DRS_MSG_ADDCLONEDCREQ_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszCloneDCName"),(PWCHAR, "pwszSite"),]

    

class DRS_MSG_ADDCLONEDCREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDCLONEDCREQ_V1, "V1"),}

    

class DRS_MSG_ADDCLONEDCREPLY_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszCloneDCName"),(PWCHAR, "pwszSite"),(DWORD, "cPasswordLength"),(PWCHAR, "pwsNewDCAccountPassword"),]

    

class DRS_MSG_ADDCLONEDCREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_ADDCLONEDCREPLY_V1, "V1"),}

    

class DRS_MSG_WRITENGCKEYREQ_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszAccount"),(DWORD, "cNgcKey"),(PUCHAR, "pNgcKey"),]

    

class DRS_MSG_WRITENGCKEYREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_WRITENGCKEYREQ_V1, "V1"),}

    

class DRS_MSG_WRITENGCKEYREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "retVal"),]

    

class DRS_MSG_WRITENGCKEYREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_WRITENGCKEYREPLY_V1, "V1"),}

    

class DRS_MSG_READNGCKEYREQ_V1(NdrStructure):
    MEMBERS = [(PWCHAR, "pwszAccount"),]

    

class DRS_MSG_READNGCKEYREQ(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_READNGCKEYREQ_V1, "V1"),}

    

class DRS_MSG_READNGCKEYREPLY_V1(NdrStructure):
    MEMBERS = [(DWORD, "retVal"),(DWORD, "cNgcKey"),(PUCHAR, "pNgcKey"),]

    

class DRS_MSG_READNGCKEYREPLY(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (DRS_MSG_READNGCKEYREPLY_V1, "V1"),}

    
Method("IDL_DRSBind",
In(HANDLE_T),
In(PUUID),
In(PDRS_EXTENSIONS),
Out(PPDRS_EXTENSIONS),
Out(PDRS_HANDLE),
),Method("IDL_DRSUnbind",
InOut(PDRS_HANDLE),
),Method("IDL_DRSReplicaSync",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPSYNC),
),Method("IDL_DRSGetNCChanges",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_GETCHGREQ),
Out(PDWORD),
Out(PDRS_MSG_GETCHGREPLY),
),Method("IDL_DRSUpdateRefs",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_UPDREFS),
),Method("IDL_DRSReplicaAdd",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPADD),
),Method("IDL_DRSReplicaDel",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPDEL),
),Method("IDL_DRSReplicaModify",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPMOD),
),Method("IDL_DRSVerifyNames",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_VERIFYREQ),
Out(PDWORD),
Out(PDRS_MSG_VERIFYREPLY),
),Method("IDL_DRSGetMemberships",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REVMEMB_REQ),
Out(PDWORD),
Out(PDRS_MSG_REVMEMB_REPLY),
),Method("IDL_DRSInterDomainMove",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_MOVEREQ),
Out(PDWORD),
Out(PDRS_MSG_MOVEREPLY),
),Method("IDL_DRSGetNT4ChangeLog",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_NT4_CHGLOG_REQ),
Out(PDWORD),
Out(PDRS_MSG_NT4_CHGLOG_REPLY),
),Method("IDL_DRSCrackNames",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_CRACKREQ),
Out(PDWORD),
Out(PDRS_MSG_CRACKREPLY),
),Method("IDL_DRSWriteSPN",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_SPNREQ),
Out(PDWORD),
Out(PDRS_MSG_SPNREPLY),
),Method("IDL_DRSRemoveDsServer",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_RMSVRREQ),
Out(PDWORD),
Out(PDRS_MSG_RMSVRREPLY),
),Method("IDL_DRSRemoveDsDomain",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_RMDMNREQ),
Out(PDWORD),
Out(PDRS_MSG_RMDMNREPLY),
),Method("IDL_DRSDomainControllerInfo",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_DCINFOREQ),
Out(PDWORD),
Out(PDRS_MSG_DCINFOREPLY),
),Method("IDL_DRSAddEntry",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_ADDENTRYREQ),
Out(PDWORD),
Out(PDRS_MSG_ADDENTRYREPLY),
),Method("IDL_DRSExecuteKCC",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_KCC_EXECUTE),
),Method("IDL_DRSGetReplInfo",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_GETREPLINFO_REQ),
Out(PDWORD),
Out(PDRS_MSG_GETREPLINFO_REPLY),
),Method("IDL_DRSAddSidHistory",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_ADDSIDREQ),
Out(PDWORD),
Out(PDRS_MSG_ADDSIDREPLY),
),Method("IDL_DRSGetMemberships2",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_GETMEMBERSHIPS2_REQ),
Out(PDWORD),
Out(PDRS_MSG_GETMEMBERSHIPS2_REPLY),
),Method("IDL_DRSReplicaVerifyObjects",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPVERIFYOBJ),
),Method("IDL_DRSGetObjectExistence",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_EXISTREQ),
Out(PDWORD),
Out(PDRS_MSG_EXISTREPLY),
),Method("IDL_DRSQuerySitesByCost",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_QUERYSITESREQ),
Out(PDWORD),
Out(PDRS_MSG_QUERYSITESREPLY),
),Method("IDL_DRSInitDemotion",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_INIT_DEMOTIONREQ),
Out(PDWORD),
Out(PDRS_MSG_INIT_DEMOTIONREPLY),
),Method("IDL_DRSReplicaDemotion",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_REPLICA_DEMOTIONREQ),
Out(PDWORD),
Out(PDRS_MSG_REPLICA_DEMOTIONREPLY),
),Method("IDL_DRSFinishDemotion",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_FINISH_DEMOTIONREQ),
Out(PDWORD),
Out(PDRS_MSG_FINISH_DEMOTIONREPLY),
),Method("IDL_DRSAddCloneDC",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_ADDCLONEDCREQ),
Out(PDWORD),
Out(PDRS_MSG_ADDCLONEDCREPLY),
),Method("IDL_DRSWriteNgcKey",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_WRITENGCKEYREQ),
Out(PDWORD),
Out(PDRS_MSG_WRITENGCKEYREPLY),
),Method("IDL_DRSReadNgcKey",
In(DRS_HANDLE),
In(DWORD),
In(PDRS_MSG_READNGCKEYREQ),
Out(PDWORD),
Out(PDRS_MSG_READNGCKEYREPLY),
),