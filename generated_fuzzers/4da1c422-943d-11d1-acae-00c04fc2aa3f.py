
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

    

class COBJID(NdrStructure):
    MEMBERS = [(GUID, "_object"),]

    

class CVOLUMEID(NdrStructure):
    MEMBERS = [(GUID, "_volume"),]

    

class CMACHINEID(NdrStructure):
    MEMBERS = [(CHAR, "_szMachine"),]

    

class CDOMAINRELATIVEOBJID(NdrStructure):
    MEMBERS = [(CVOLUMEID, "_volume"),(COBJID, "_object"),]

    
Method("Opnum0NotUsedOnWire",
In(),
),Method("Opnum1NotUsedOnWire",
In(),
),Method("Opnum2NotUsedOnWire",
In(),
),Method("Opnum3NotUsedOnWire",
In(),
),Method("Opnum4NotUsedOnWire",
In(),
),Method("Opnum5NotUsedOnWire",
In(),
),Method("Opnum6NotUsedOnWire",
In(),
),Method("Opnum7NotUsedOnWire",
In(),
),Method("Opnum8NotUsedOnWire",
In(),
),Method("Opnum9NotUsedOnWire",
In(),
),Method("Opnum10NotUsedOnWire",
In(),
),Method("Opnum11NotUsedOnWire",
In(),
),Method("LnkSearchMachine",
In(UNSIGNED_LONG),
In(PCDOMAINRELATIVEOBJID),
In(PCDOMAINRELATIVEOBJID),
Out(PCDOMAINRELATIVEOBJID),
Out(PCDOMAINRELATIVEOBJID),
Out(PCMACHINEID),
Out(PWCHAR_T),
),
class CVOLUMESECRET(NdrStructure):
    MEMBERS = [(BYTE, "_abSecret"),]

    

class OLD_TRK_FILE_TRACKING_INFORMATION(NdrStructure):
    MEMBERS = [(WCHAR, "tszFilePath"),(CDOMAINRELATIVEOBJID, "droidBirth"),(CDOMAINRELATIVEOBJID, "droidLast"),(HRESULT, "hr"),]

    

class TRK_FILE_TRACKING_INFORMATION(NdrStructure):
    MEMBERS = [(CDOMAINRELATIVEOBJID, "droidBirth"),(CDOMAINRELATIVEOBJID, "droidLast"),(CMACHINEID, "mcidLast"),(HRESULT, "hr"),]

    

class OLD_TRKSVR_CALL_SEARCH(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cSearch"),(POLD_TRK_FILE_TRACKING_INFORMATION, "pSearches"),]

    

class TRKSVR_CALL_SEARCH(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cSearch"),(PTRK_FILE_TRACKING_INFORMATION, "pSearches"),]

    

class TRKSVR_CALL_MOVE_NOTIFICATION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cNotifications"),(UNSIGNED_LONG, "cProcessed"),(SEQUENCENUMBER, "seq"),(LONG, "fForceSeqNumber"),(PCVOLUMEID, "pvolid"),(PCOBJID, "rgobjidCurrent"),(PCDOMAINRELATIVEOBJID, "rgdroidBirth"),(PCDOMAINRELATIVEOBJID, "rgdroidNew"),]

    

class TRKSVR_CALL_REFRESH(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cSources"),(PCDOMAINRELATIVEOBJID, "adroidBirth"),(UNSIGNED_LONG, "cVolumes"),(PCVOLUMEID, "avolid"),]

    

class TRKSVR_CALL_DELETE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cdroidBirth"),(PCDOMAINRELATIVEOBJID, "adroidBirth"),(UNSIGNED_LONG, "cVolumes"),(PCVOLUMEID, "pVolumes"),]

    

class TRKSVR_SYNC_VOLUME(NdrStructure):
    MEMBERS = [(HRESULT, "hr"),(TRKSVR_SYNC_TYPE, "SyncType"),(CVOLUMEID, "volume"),(CVOLUMESECRET, "secret"),(CVOLUMESECRET, "secretOld"),(SEQUENCENUMBER, "seq"),(FILETIME, "ftLastRefresh"),(CMACHINEID, "machine"),]

    

class TRKSVR_CALL_SYNC_VOLUMES(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cVolumes"),(PTRKSVR_SYNC_VOLUME, "pVolumes"),]

    

class TRKSVR_STATISTICS(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cSyncVolumeRequests"),(UNSIGNED_LONG, "cSyncVolumeErrors"),(UNSIGNED_LONG, "cSyncVolumeThreads"),(UNSIGNED_LONG, "cCreateVolumeRequests"),(UNSIGNED_LONG, "cCreateVolumeErrors"),(UNSIGNED_LONG, "cClaimVolumeRequests"),(UNSIGNED_LONG, "cClaimVolumeErrors"),(UNSIGNED_LONG, "cQueryVolumeRequests"),(UNSIGNED_LONG, "cQueryVolumeErrors"),(UNSIGNED_LONG, "cFindVolumeRequests"),(UNSIGNED_LONG, "cFindVolumeErrors"),(UNSIGNED_LONG, "cTestVolumeRequests"),(UNSIGNED_LONG, "cTestVolumeErrors"),(UNSIGNED_LONG, "cSearchRequests"),(UNSIGNED_LONG, "cSearchErrors"),(UNSIGNED_LONG, "cSearchThreads"),(UNSIGNED_LONG, "cMoveNotifyRequests"),(UNSIGNED_LONG, "cMoveNotifyErrors"),(UNSIGNED_LONG, "cMoveNotifyThreads"),(UNSIGNED_LONG, "cRefreshRequests"),(UNSIGNED_LONG, "cRefreshErrors"),(UNSIGNED_LONG, "cRefreshThreads"),(UNSIGNED_LONG, "cDeleteNotifyRequests"),(UNSIGNED_LONG, "cDeleteNotifyErrors"),(UNSIGNED_LONG, "cDeleteNotifyThreads"),(UNSIGNED_LONG, "ulGCIterationPeriod"),(FILETIME, "ftLastSuccessfulRequest"),(HRESULT, "hrLastError"),(UNSIGNED_LONG, "dwMoveLimit"),(LONG, "lRefreshCounter"),(UNSIGNED_LONG, "dwCachedVolumeTableCount"),(UNSIGNED_LONG, "dwCachedMoveTableCount"),(FILETIME, "ftCachedLastUpdated"),(LONG, "fIsDesignatedDc"),(FILETIME, "ftNextGC"),(FILETIME, "ftServiceStart"),(UNSIGNED_LONG, "cMaxRPCThreads"),(UNSIGNED_LONG, "cAvailableRPCThreads"),(UNSIGNED_LONG, "cLowestAvailableRPCThreads"),(UNSIGNED_LONG, "cNumThreadPoolThreads"),(UNSIGNED_LONG, "cMostThreadPoolThreads"),(SHORT, "cEntriesToGC"),(SHORT, "cEntriesGCed"),(SHORT, "cMaxDsWriteEvents"),(SHORT, "cCurrentFailedWrites"),(VERSION, "Version"),]

    

class TRKWKS_CONFIG(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwParameter"),(UNSIGNED_LONG, "dwNewValue"),]

    

class TRKSVR_MESSAGE_UNION(NdrStructure):
    MEMBERS = [(TRKSVR_MESSAGE_TYPE, "MessageType"),(TRKSVR_MESSAGE_PRIORITY, "Priority"),(PTSZMACHINEID, "u0"),(PWCHAR, "ptszMachineID"),]

    
Method("LnkSvrMessage",
In(HANDLE_T),
InOut(PTRKSVR_MESSAGE_UNION),
),Method("LnkSvrMessageCallback",
InOut(PTRKSVR_MESSAGE_UNION),
),