
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