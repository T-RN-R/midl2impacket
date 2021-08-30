
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

    

class ('FRS_VERSION_VECTOR', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "dbGuid"),(('DWORDLONG', None), "low"),(('DWORDLONG', None), "high"),]

    

class ('FRS_EPOQUE_VECTOR', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "machine"),(('EPOQUE', None), "epoque"),]

    

class ('FRS_ID_GVSN', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "uidDbGuid"),(('DWORDLONG', None), "uidVersion"),(('GUID', None), "gvsnDbGuid"),(('DWORDLONG', None), "gvsnVersion"),]

    

class ('FRS_UPDATE', None)(NdrStructure):
    MEMBERS = [(('LONG', None), "present"),(('LONG', None), "nameConflict"),(('UNSIGNED_LONG', None), "attributes"),(('FILETIME', None), "fence"),(('FILETIME', None), "clock"),(('FILETIME', None), "createTime"),(('FRS_CONTENT_SET_ID', None), "contentSetId"),(('UNSIGNED_CHAR', None), "hash"),(('UNSIGNED_CHAR', None), "rdcSimilarity"),(('GUID', None), "uidDbGuid"),(('DWORDLONG', None), "uidVersion"),(('GUID', None), "gvsnDbGuid"),(('DWORDLONG', None), "gvsnVersion"),(('GUID', None), "parentDbGuid"),(('DWORDLONG', None), "parentVersion"),(('WCHAR', None), "name"),(('LONG', None), "flags"),]

    

class ('FRS_UPDATE_CANCEL_DATA', None)(NdrStructure):
    MEMBERS = [(('FRS_UPDATE', None), "blockingUpdate"),(('FRS_CONTENT_SET_ID', None), "contentSetId"),(('FRS_DATABASE_ID', None), "gvsnDatabaseId"),(('FRS_DATABASE_ID', None), "uidDatabaseId"),(('FRS_DATABASE_ID', None), "parentDatabaseId"),(('DWORDLONG', None), "gvsnVersion"),(('DWORDLONG', None), "uidVersion"),(('DWORDLONG', None), "parentVersion"),(('UNSIGNED_LONG', None), "cancelType"),(('LONG', None), "isUidValid"),(('LONG', None), "isParentUidValid"),(('LONG', None), "isBlockerValid"),]

    

class ('FRS_RDC_SOURCE_NEED', None)(NdrStructure):
    MEMBERS = [(('ULONGLONG', None), "needOffset"),(('ULONGLONG', None), "needSize"),]

    

class ('FRS_RDC_PARAMETERS_FILTERMAX', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "horizonSize"),(('UNSIGNED_SHORT', None), "windowSize"),]

    

class ('FRS_RDC_PARAMETERS_FILTERPOINT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "minChunkSize"),(('UNSIGNED_SHORT', None), "maxChunkSize"),]

    

class ('FRS_RDC_PARAMETERS_GENERIC', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "chunkerType"),(('BYTE', None), "chunkerParameters"),]

    

class ('FRS_RDC_PARAMETERS', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "rdcChunkerAlgorithm"),(('U', None), "u"),]

    

class ('FRS_RDC_FILEINFO', None)(NdrStructure):
    MEMBERS = [(('DWORDLONG', None), "onDiskFileSize"),(('DWORDLONG', None), "fileSizeEstimate"),(('UNSIGNED_SHORT', None), "rdcVersion"),(('UNSIGNED_SHORT', None), "rdcMinimumCompatibleVersion"),(('BYTE', None), "rdcSignatureLevels"),(('RDC_FILE_COMPRESSION_TYPES', None), "compressionAlgorithm"),(('FRS_RDC_PARAMETERS', None), "rdcFilterParameters"),]

    

class ('FRS_ASYNC_VERSION_VECTOR_RESPONSE', None)(NdrStructure):
    MEMBERS = [(('ULONGLONG', None), "vvGeneration"),(('UNSIGNED_LONG', None), "versionVectorCount"),(('PFRS_VERSION_VECTOR', None), "versionVector"),(('UNSIGNED_LONG', None), "epoqueVectorCount"),(('PFRS_EPOQUE_VECTOR', None), "epoqueVector"),]

    

class ('FRS_ASYNC_RESPONSE_CONTEXT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "sequenceNumber"),(('DWORD', None), "status"),(('FRS_ASYNC_VERSION_VECTOR_RESPONSE', None), "result"),]

    
Method("CheckConnectivity",
In(FRS_REPLICA_SET_ID),
In(FRS_CONNECTION_ID),
),Method("EstablishConnection",
In(FRS_REPLICA_SET_ID),
In(FRS_CONNECTION_ID),
In(DWORD),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("EstablishSession",
In(FRS_CONNECTION_ID),
In(FRS_CONTENT_SET_ID),
),Method("RequestUpdates",
In(FRS_CONNECTION_ID),
In(FRS_CONTENT_SET_ID),
In(DWORD),
In(LONG),
In(UPDATE_REQUEST_TYPE),
In(UNSIGNED_LONG),
In(PFRS_VERSION_VECTOR),
Out(PFRS_UPDATE),
Out(PDWORD),
Out(PUPDATE_STATUS),
Out(PGUID),
Out(PDWORDLONG),
),Method("RequestVersionVector",
In(DWORD),
In(FRS_CONNECTION_ID),
In(FRS_CONTENT_SET_ID),
In(VERSION_REQUEST_TYPE),
In(VERSION_CHANGE_TYPE),
In(ULONGLONG),
),Method("AsyncPoll",
In(FRS_CONNECTION_ID),
Out(PFRS_ASYNC_RESPONSE_CONTEXT),
),Method("RequestRecords",
In(FRS_CONNECTION_ID),
In(FRS_CONTENT_SET_ID),
In(FRS_DATABASE_ID),
In(DWORDLONG),
InOut(PDWORD),
Out(PDWORD),
Out(PDWORD),
Out(PPBYTE),
Out(PRECORDS_STATUS),
),Method("UpdateCancel",
In(FRS_CONNECTION_ID),
In(FRS_UPDATE_CANCEL_DATA),
),Method("RawGetFileData",
InOut(PPFRS_SERVER_CONTEXT),
Out(PBYTE),
In(DWORD),
Out(PDWORD),
Out(PLONG),
),Method("RdcGetSignatures",
In(PFRS_SERVER_CONTEXT),
In(BYTE),
In(DWORDLONG),
Out(PBYTE),
In(DWORD),
Out(PDWORD),
),Method("RdcPushSourceNeeds",
In(PFRS_SERVER_CONTEXT),
In(PFRS_RDC_SOURCE_NEED),
In(DWORD),
),Method("RdcGetFileData",
In(PFRS_SERVER_CONTEXT),
Out(PBYTE),
In(DWORD),
Out(PDWORD),
),Method("RdcClose",
InOut(PPFRS_SERVER_CONTEXT),
),Method("InitializeFileTransferAsync",
In(FRS_CONNECTION_ID),
InOut(PFRS_UPDATE),
In(LONG),
InOut(PFRS_REQUESTED_STAGING_POLICY),
Out(PPFRS_SERVER_CONTEXT),
Out(PPFRS_RDC_FILEINFO),
Out(PBYTE),
In(DWORD),
Out(PDWORD),
Out(PLONG),
),Method("Opnum14NotUsedOnWire",
In(),
),Method("RawGetFileDataAsync",
In(PFRS_SERVER_CONTEXT),
Out(PBYTE_PIPE),
),Method("RdcGetFileDataAsync",
In(PFRS_SERVER_CONTEXT),
Out(PBYTE_PIPE),
),Method("RdcFileDataTransferKeepAlive",
In(PFRS_SERVER_CONTEXT),
),