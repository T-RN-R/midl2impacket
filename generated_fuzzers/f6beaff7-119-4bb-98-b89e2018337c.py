
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
PWCHAR = NdrCString
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
LARGE_INTEGER = NdrHyper
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

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')]

class LUID(NdrStructure):
    MEMBERS = [(DWORD,'LowPart'),(LONG,'HighPart')]

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),]
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
PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION = VOID
PCONTEXT_HANDLE_LOG_QUERY = VOID
PCONTEXT_HANDLE_LOG_HANDLE = VOID
PCONTEXT_HANDLE_OPERATION_CONTROL = VOID
PCONTEXT_HANDLE_PUBLISHER_METADATA = VOID
PCONTEXT_HANDLE_EVENT_METADATA_ENUM = VOID

class RPCINFO(NdrStructure):
    MEMBERS = [(DWORD, "m_error"),(DWORD, "m_subErr"),(DWORD, "m_subErrParam"),]

    

class BOOLEANARRAY(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PBOOLEAN, "ptr"),]

    

class UINT32ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PDWORD, "ptr"),]

    

class UINT64ARRAY(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PDWORD64, "ptr"),]

    

class STRINGARRAY(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PLPWSTR, "ptr"),]

    

class GUIDARRAY(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PGUID, "ptr"),]

    

class EVTRPCVARIANTTYPE(NdrEnum):
    MAP = ((0 , 'EvtRpcVarTypeNull'),(1 , 'EvtRpcVarTypeBoolean'),(2 , 'EvtRpcVarTypeUInt32'),(3 , 'EvtRpcVarTypeUInt64'),(4 , 'EvtRpcVarTypeString'),(5 , 'EvtRpcVarTypeGuid'),(6 , 'EvtRpcVarTypeBooleanArray'),(7 , 'EvtRpcVarTypeUInt32Array'),(8 , 'EvtRpcVarTypeUInt64Array'),(9 , 'EvtRpcVarTypeStringArray'),(10 , 'EvtRpcVarTypeGuidArray'),)        

class EVTRPCASSERTCONFIGFLAGS(NdrEnum):
    MAP = ((0 , 'EvtRpcChannelPath'),(1 , 'EvtRpcPublisherName'),)        

class EVTRPCVARIANT(NdrStructure):
    MEMBERS = [(EVTRPCVARIANTTYPE, "type"),(DWORD, "flags"),(U0, "u0"),]

    

class EVTRPCVARIANTLIST(NdrStructure):
    MEMBERS = [(DWORD, "count"),(PEVTRPCVARIANT, "props"),]

    

class EVTRPCQUERYCHANNELINFO(NdrStructure):
    MEMBERS = [(LPWSTR, "name"),(DWORD, "status"),]

    
Interface("f6beaff7-119-4bb-98-b89e2018337c", "1.0",[Method("EvtRpcRegisterRemoteSubscription",
In((LPCWSTR,'channelPath')),
In((LPCWSTR,'query')),
In((LPCWSTR,'bookmarkXml')),
In((DWORD,'flags')),
Out((PPCONTEXT_HANDLE_REMOTE_SUBSCRIPTION,'handle')),
Out((PPCONTEXT_HANDLE_OPERATION_CONTROL,'control')),
Out((PDWORD,'queryChannelInfoSize')),
Out((PPEVTRPCQUERYCHANNELINFO,'queryChannelInfo')),
Out((PRPCINFO,'error')),
),Method("EvtRpcRemoteSubscriptionNextAsync",
In((PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION,'handle')),
In((DWORD,'numRequestedRecords')),
In((DWORD,'flags')),
Out((PDWORD,'numActualRecords')),
Out((PPDWORD,'eventDataIndices')),
Out((PPDWORD,'eventDataSizes')),
Out((PDWORD,'resultBufferSize')),
Out((PPBYTE,'resultBuffer')),
),Method("EvtRpcRemoteSubscriptionNext",
In((PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION,'handle')),
In((DWORD,'numRequestedRecords')),
In((DWORD,'timeOut')),
In((DWORD,'flags')),
Out((PDWORD,'numActualRecords')),
Out((PPDWORD,'eventDataIndices')),
Out((PPDWORD,'eventDataSizes')),
Out((PDWORD,'resultBufferSize')),
Out((PPBYTE,'resultBuffer')),
),Method("EvtRpcRemoteSubscriptionWaitAsync",
In((PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION,'handle')),
),Method("EvtRpcRegisterControllableOperation",
Out((PPCONTEXT_HANDLE_OPERATION_CONTROL,'handle')),
),Method("EvtRpcRegisterLogQuery",
In((LPCWSTR,'path')),
In((LPCWSTR,'query')),
In((DWORD,'flags')),
Out((PPCONTEXT_HANDLE_LOG_QUERY,'handle')),
Out((PPCONTEXT_HANDLE_OPERATION_CONTROL,'opControl')),
Out((PDWORD,'queryChannelInfoSize')),
Out((PPEVTRPCQUERYCHANNELINFO,'queryChannelInfo')),
Out((PRPCINFO,'error')),
),Method("EvtRpcClearLog",
In((PCONTEXT_HANDLE_OPERATION_CONTROL,'control')),
In((LPCWSTR,'channelPath')),
In((LPCWSTR,'backupPath')),
In((DWORD,'flags')),
Out((PRPCINFO,'error')),
),Method("EvtRpcExportLog",
In((PCONTEXT_HANDLE_OPERATION_CONTROL,'control')),
In((LPCWSTR,'channelPath')),
In((LPCWSTR,'query')),
In((LPCWSTR,'backupPath')),
In((DWORD,'flags')),
Out((PRPCINFO,'error')),
),Method("EvtRpcLocalizeExportLog",
In((PCONTEXT_HANDLE_OPERATION_CONTROL,'control')),
In((LPCWSTR,'logFilePath')),
In((LCID,'locale')),
In((DWORD,'flags')),
Out((PRPCINFO,'error')),
),Method("EvtRpcMessageRender",
In((PCONTEXT_HANDLE_PUBLISHER_METADATA,'pubCfgObj')),
In((DWORD,'sizeEventId')),
In((PBYTE,'eventId')),
In((DWORD,'messageId')),
In((PEVTRPCVARIANTLIST,'values')),
In((DWORD,'flags')),
In((DWORD,'maxSizeString')),
Out((PDWORD,'actualSizeString')),
Out((PDWORD,'neededSizeString')),
Out((PPBYTE,'string')),
Out((PRPCINFO,'error')),
),Method("EvtRpcMessageRenderDefault",
In((DWORD,'sizeEventId')),
In((PBYTE,'eventId')),
In((DWORD,'messageId')),
In((PEVTRPCVARIANTLIST,'values')),
In((DWORD,'flags')),
In((DWORD,'maxSizeString')),
Out((PDWORD,'actualSizeString')),
Out((PDWORD,'neededSizeString')),
Out((PPBYTE,'string')),
Out((PRPCINFO,'error')),
),Method("EvtRpcQueryNext",
In((PCONTEXT_HANDLE_LOG_QUERY,'logQuery')),
In((DWORD,'numRequestedRecords')),
In((DWORD,'timeOutEnd')),
In((DWORD,'flags')),
Out((PDWORD,'numActualRecords')),
Out((PPDWORD,'eventDataIndices')),
Out((PPDWORD,'eventDataSizes')),
Out((PDWORD,'resultBufferSize')),
Out((PPBYTE,'resultBuffer')),
),Method("EvtRpcQuerySeek",
In((PCONTEXT_HANDLE_LOG_QUERY,'logQuery')),
In((__INT64,'pos')),
In((LPCWSTR,'bookmarkXml')),
In((DWORD,'timeOut')),
In((DWORD,'flags')),
Out((PRPCINFO,'error')),
),Method("EvtRpcClose",
InOut((PPVOID,'handle')),
),Method("EvtRpcCancel",
In((PCONTEXT_HANDLE_OPERATION_CONTROL,'handle')),
),Method("EvtRpcAssertConfig",
In((LPCWSTR,'path')),
In((DWORD,'flags')),
),Method("EvtRpcRetractConfig",
In((LPCWSTR,'path')),
In((DWORD,'flags')),
),Method("EvtRpcOpenLogHandle",
In((LPCWSTR,'channel')),
In((DWORD,'flags')),
Out((PPCONTEXT_HANDLE_LOG_HANDLE,'handle')),
Out((PRPCINFO,'error')),
),Method("EvtRpcGetLogFileInfo",
In((PCONTEXT_HANDLE_LOG_HANDLE,'logHandle')),
In((DWORD,'propertyId')),
In((DWORD,'propertyValueBufferSize')),
Out((PBYTE,'propertyValueBuffer')),
Out((PDWORD,'propertyValueBufferLength')),
),Method("EvtRpcGetChannelList",
In((DWORD,'flags')),
Out((PDWORD,'numChannelPaths')),
Out((PPLPWSTR,'channelPaths')),
),Method("EvtRpcGetChannelConfig",
In((LPCWSTR,'channelPath')),
In((DWORD,'flags')),
Out((PEVTRPCVARIANTLIST,'props')),
),Method("EvtRpcPutChannelConfig",
In((LPCWSTR,'channelPath')),
In((DWORD,'flags')),
In((PEVTRPCVARIANTLIST,'props')),
Out((PRPCINFO,'error')),
),Method("EvtRpcGetPublisherList",
In((DWORD,'flags')),
Out((PDWORD,'numPublisherIds')),
Out((PPLPWSTR,'publisherIds')),
),Method("EvtRpcGetPublisherListForChannel",
In((LPCWSTR,'channelName')),
In((DWORD,'flags')),
Out((PDWORD,'numPublisherIds')),
Out((PPLPWSTR,'publisherIds')),
),Method("EvtRpcGetPublisherMetadata",
In((LPCWSTR,'publisherId')),
In((LPCWSTR,'logFilePath')),
In((LCID,'locale')),
In((DWORD,'flags')),
Out((PEVTRPCVARIANTLIST,'pubMetadataProps')),
Out((PPCONTEXT_HANDLE_PUBLISHER_METADATA,'pubMetadata')),
),Method("EvtRpcGetPublisherResourceMetadata",
In((PCONTEXT_HANDLE_PUBLISHER_METADATA,'handle')),
In((DWORD,'propertyId')),
In((DWORD,'flags')),
Out((PEVTRPCVARIANTLIST,'pubMetadataProps')),
),Method("EvtRpcGetEventMetadataEnum",
In((PCONTEXT_HANDLE_PUBLISHER_METADATA,'pubMetadata')),
In((DWORD,'flags')),
In((LPCWSTR,'reservedForFilter')),
Out((PPCONTEXT_HANDLE_EVENT_METADATA_ENUM,'eventMetaDataEnum')),
),Method("EvtRpcGetNextEventMetadata",
In((PCONTEXT_HANDLE_EVENT_METADATA_ENUM,'eventMetaDataEnum')),
In((DWORD,'flags')),
In((DWORD,'numRequested')),
Out((PDWORD,'numReturned')),
Out((PPEVTRPCVARIANTLIST,'eventMetadataInstances')),
),Method("EvtRpcGetClassicLogDisplayName",
In((LPCWSTR,'logName')),
In((LCID,'locale')),
In((DWORD,'flags')),
Out((PLPWSTR,'displayName')),
),])