
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