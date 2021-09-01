
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
FRS_REPLICA_SET_ID = GUID
FRS_CONTENT_SET_ID = GUID
FRS_DATABASE_ID = GUID
FRS_MEMBER_ID = GUID
FRS_CONNECTION_ID = GUID
EPOQUE = SYSTEMTIME

class FRS_VERSION_VECTOR(NdrStructure):
    MEMBERS = [(GUID, "dbGuid"),(DWORDLONG, "low"),(DWORDLONG, "high"),]

    

class FRS_EPOQUE_VECTOR(NdrStructure):
    MEMBERS = [(GUID, "machine"),(EPOQUE, "epoque"),]

    

class FRS_ID_GVSN(NdrStructure):
    MEMBERS = [(GUID, "uidDbGuid"),(DWORDLONG, "uidVersion"),(GUID, "gvsnDbGuid"),(DWORDLONG, "gvsnVersion"),]

    

class FRS_UPDATE(NdrStructure):
    MEMBERS = [(LONG, "present"),(LONG, "nameConflict"),(UNSIGNED_LONG, "attributes"),(FILETIME, "fence"),(FILETIME, "clock"),(FILETIME, "createTime"),(FRS_CONTENT_SET_ID, "contentSetId"),(UNSIGNED_CHAR, "hash"),(UNSIGNED_CHAR, "rdcSimilarity"),(GUID, "uidDbGuid"),(DWORDLONG, "uidVersion"),(GUID, "gvsnDbGuid"),(DWORDLONG, "gvsnVersion"),(GUID, "parentDbGuid"),(DWORDLONG, "parentVersion"),(WCHAR, "name"),(LONG, "flags"),]

    

class FRS_UPDATE_CANCEL_DATA(NdrStructure):
    MEMBERS = [(FRS_UPDATE, "blockingUpdate"),(FRS_CONTENT_SET_ID, "contentSetId"),(FRS_DATABASE_ID, "gvsnDatabaseId"),(FRS_DATABASE_ID, "uidDatabaseId"),(FRS_DATABASE_ID, "parentDatabaseId"),(DWORDLONG, "gvsnVersion"),(DWORDLONG, "uidVersion"),(DWORDLONG, "parentVersion"),(UNSIGNED_LONG, "cancelType"),(LONG, "isUidValid"),(LONG, "isParentUidValid"),(LONG, "isBlockerValid"),]

    

class FRS_RDC_SOURCE_NEED(NdrStructure):
    MEMBERS = [(ULONGLONG, "needOffset"),(ULONGLONG, "needSize"),]

    

class TRANSPORTFLAGS(NdrEnum):
    MAP = ((1 , 'TRANSPORT_SUPPORTS_RDC_SIMILARITY'),)        

class RDC_FILE_COMPRESSION_TYPES(NdrEnum):
    MAP = ((0 , 'RDC_UNCOMPRESSED'),(1 , 'RDC_XPRESS'),)        

class RDC_CHUNKER_ALGORITHM(NdrEnum):
    MAP = ((0 , 'RDC_FILTERGENERIC'),(1 , 'RDC_FILTERMAX'),(2 , 'RDC_FILTERPOINT'),(3 , 'RDC_MAXALGORITHM'),)        

class UPDATE_REQUEST_TYPE(NdrEnum):
    MAP = ((0 , 'UPDATE_REQUEST_ALL'),(1 , 'UPDATE_REQUEST_TOMBSTONES'),(2 , 'UPDATE_REQUEST_LIVE'),)        

class UPDATE_STATUS(NdrEnum):
    MAP = ((2 , 'UPDATE_STATUS_DONE'),(3 , 'UPDATE_STATUS_MORE'),)        

class RECORDS_STATUS(NdrEnum):
    MAP = ((0 , 'RECORDS_STATUS_DONE'),(1 , 'RECORDS_STATUS_MORE'),)        

class VERSION_REQUEST_TYPE(NdrEnum):
    MAP = ((0 , 'REQUEST_NORMAL_SYNC'),(1 , 'REQUEST_SLOW_SYNC'),(2 , 'REQUEST_SUBORDINATE_SYNC'),)        

class VERSION_CHANGE_TYPE(NdrEnum):
    MAP = ((0 , 'CHANGE_NOTIFY'),(2 , 'CHANGE_ALL'),)        

class FRS_REQUESTED_STAGING_POLICY(NdrEnum):
    MAP = ((0 , 'SERVER_DEFAULT'),(1 , 'STAGING_REQUIRED'),(2 , 'RESTAGING_REQUIRED'),)        

class FRS_RDC_PARAMETERS_FILTERMAX(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "horizonSize"),(UNSIGNED_SHORT, "windowSize"),]

    

class FRS_RDC_PARAMETERS_FILTERPOINT(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "minChunkSize"),(UNSIGNED_SHORT, "maxChunkSize"),]

    

class FRS_RDC_PARAMETERS_GENERIC(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "chunkerType"),(BYTE, "chunkerParameters"),]

    

class FRS_RDC_PARAMETERS(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "rdcChunkerAlgorithm"),(U, "u"),]

    

class FRS_RDC_FILEINFO(NdrStructure):
    MEMBERS = [(DWORDLONG, "onDiskFileSize"),(DWORDLONG, "fileSizeEstimate"),(UNSIGNED_SHORT, "rdcVersion"),(UNSIGNED_SHORT, "rdcMinimumCompatibleVersion"),(BYTE, "rdcSignatureLevels"),(RDC_FILE_COMPRESSION_TYPES, "compressionAlgorithm"),(FRS_RDC_PARAMETERS, "rdcFilterParameters"),]

    

class FRS_ASYNC_VERSION_VECTOR_RESPONSE(NdrStructure):
    MEMBERS = [(ULONGLONG, "vvGeneration"),(UNSIGNED_LONG, "versionVectorCount"),(PFRS_VERSION_VECTOR, "versionVector"),(UNSIGNED_LONG, "epoqueVectorCount"),(PFRS_EPOQUE_VECTOR, "epoqueVector"),]

    

class FRS_ASYNC_RESPONSE_CONTEXT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "sequenceNumber"),(DWORD, "status"),(FRS_ASYNC_VERSION_VECTOR_RESPONSE, "result"),]

    
BYTE_PIPE = PIPE_BYTE
PFRS_SERVER_CONTEXT = VOID
Interface("897e2e5f-93f3-4376-9c9c-fd2277495c27", "1.0",[Method("CheckConnectivity",
In((FRS_REPLICA_SET_ID,'replicaSetId')),
In((FRS_CONNECTION_ID,'connectionId')),
),Method("EstablishConnection",
In((FRS_REPLICA_SET_ID,'replicaSetId')),
In((FRS_CONNECTION_ID,'connectionId')),
In((DWORD,'downstreamProtocolVersion')),
In((DWORD,'downstreamFlags')),
Out((PDWORD,'upstreamProtocolVersion')),
Out((PDWORD,'upstreamFlags')),
),Method("EstablishSession",
In((FRS_CONNECTION_ID,'connectionId')),
In((FRS_CONTENT_SET_ID,'contentSetId')),
),Method("RequestUpdates",
In((FRS_CONNECTION_ID,'connectionId')),
In((FRS_CONTENT_SET_ID,'contentSetId')),
In((DWORD,'creditsAvailable')),
In((LONG,'hashRequested')),
In((UPDATE_REQUEST_TYPE,'updateRequestType')),
In((UNSIGNED_LONG,'versionVectorDiffCount')),
In((PFRS_VERSION_VECTOR,'versionVectorDiff')),
Out((PFRS_UPDATE,'frsUpdate')),
Out((PDWORD,'updateCount')),
Out((PUPDATE_STATUS,'updateStatus')),
Out((PGUID,'gvsnDbGuid')),
Out((PDWORDLONG,'gvsnVersion')),
),Method("RequestVersionVector",
In((DWORD,'sequenceNumber')),
In((FRS_CONNECTION_ID,'connectionId')),
In((FRS_CONTENT_SET_ID,'contentSetId')),
In((VERSION_REQUEST_TYPE,'requestType')),
In((VERSION_CHANGE_TYPE,'changeType')),
In((ULONGLONG,'vvGeneration')),
),Method("AsyncPoll",
In((FRS_CONNECTION_ID,'connectionId')),
Out((PFRS_ASYNC_RESPONSE_CONTEXT,'response')),
),Method("RequestRecords",
In((FRS_CONNECTION_ID,'connectionId')),
In((FRS_CONTENT_SET_ID,'contentSetId')),
In((FRS_DATABASE_ID,'uidDbGuid')),
In((DWORDLONG,'uidVersion')),
InOut((PDWORD,'maxRecords')),
Out((PDWORD,'numRecords')),
Out((PDWORD,'numBytes')),
Out((PPBYTE,'compressedRecords')),
Out((PRECORDS_STATUS,'recordsStatus')),
),Method("UpdateCancel",
In((FRS_CONNECTION_ID,'connectionId')),
In((FRS_UPDATE_CANCEL_DATA,'cancelData')),
),Method("RawGetFileData",
InOut((PPFRS_SERVER_CONTEXT,'serverContext')),
Out((PBYTE,'dataBuffer')),
In((DWORD,'bufferSize')),
Out((PDWORD,'sizeRead')),
Out((PLONG,'isEndOfFile')),
),Method("RdcGetSignatures",
In((PFRS_SERVER_CONTEXT,'serverContext')),
In((BYTE,'level')),
In((DWORDLONG,'offset')),
Out((PBYTE,'buffer')),
In((DWORD,'length')),
Out((PDWORD,'sizeRead')),
),Method("RdcPushSourceNeeds",
In((PFRS_SERVER_CONTEXT,'serverContext')),
In((PFRS_RDC_SOURCE_NEED,'sourceNeeds')),
In((DWORD,'needCount')),
),Method("RdcGetFileData",
In((PFRS_SERVER_CONTEXT,'serverContext')),
Out((PBYTE,'dataBuffer')),
In((DWORD,'bufferSize')),
Out((PDWORD,'sizeReturned')),
),Method("RdcClose",
InOut((PPFRS_SERVER_CONTEXT,'serverContext')),
),Method("InitializeFileTransferAsync",
In((FRS_CONNECTION_ID,'connectionId')),
InOut((PFRS_UPDATE,'frsUpdate')),
In((LONG,'rdcDesired')),
InOut((PFRS_REQUESTED_STAGING_POLICY,'stagingPolicy')),
Out((PPFRS_SERVER_CONTEXT,'serverContext')),
Out((PPFRS_RDC_FILEINFO,'rdcFileInfo')),
Out((PBYTE,'dataBuffer')),
In((DWORD,'bufferSize')),
Out((PDWORD,'sizeRead')),
Out((PLONG,'isEndOfFile')),
),Method("Opnum14NotUsedOnWire",
),Method("RawGetFileDataAsync",
In((PFRS_SERVER_CONTEXT,'serverContext')),
Out((PBYTE_PIPE,'bytePipe')),
),Method("RdcGetFileDataAsync",
In((PFRS_SERVER_CONTEXT,'serverContext')),
Out((PBYTE_PIPE,'bytePipe')),
),Method("RdcFileDataTransferKeepAlive",
In((PFRS_SERVER_CONTEXT,'serverContext')),
),])