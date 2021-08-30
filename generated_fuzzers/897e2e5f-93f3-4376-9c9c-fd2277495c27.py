from fuzzer.midl import *
from fuzzer.core import *


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


class FRS_VERSION_VECTOR(NdrStructure):
    MEMBERS = [
        (GUID, "dbGuid"),
        (DWORDLONG, "low"),
        (DWORDLONG, "high"),
    ]


class FRS_EPOQUE_VECTOR(NdrStructure):
    MEMBERS = [
        (GUID, "machine"),
        (EPOQUE, "epoque"),
    ]


class FRS_ID_GVSN(NdrStructure):
    MEMBERS = [
        (GUID, "uidDbGuid"),
        (DWORDLONG, "uidVersion"),
        (GUID, "gvsnDbGuid"),
        (DWORDLONG, "gvsnVersion"),
    ]


class FRS_UPDATE(NdrStructure):
    MEMBERS = [
        (LONG, "present"),
        (LONG, "nameConflict"),
        (UNSIGNED_LONG, "attributes"),
        (FILETIME, "fence"),
        (FILETIME, "clock"),
        (FILETIME, "createTime"),
        (FRS_CONTENT_SET_ID, "contentSetId"),
        (UNSIGNED_CHAR, "hash"),
        (UNSIGNED_CHAR, "rdcSimilarity"),
        (GUID, "uidDbGuid"),
        (DWORDLONG, "uidVersion"),
        (GUID, "gvsnDbGuid"),
        (DWORDLONG, "gvsnVersion"),
        (GUID, "parentDbGuid"),
        (DWORDLONG, "parentVersion"),
        (WCHAR, "name"),
        (LONG, "flags"),
    ]


class FRS_UPDATE_CANCEL_DATA(NdrStructure):
    MEMBERS = [
        (FRS_UPDATE, "blockingUpdate"),
        (FRS_CONTENT_SET_ID, "contentSetId"),
        (FRS_DATABASE_ID, "gvsnDatabaseId"),
        (FRS_DATABASE_ID, "uidDatabaseId"),
        (FRS_DATABASE_ID, "parentDatabaseId"),
        (DWORDLONG, "gvsnVersion"),
        (DWORDLONG, "uidVersion"),
        (DWORDLONG, "parentVersion"),
        (UNSIGNED_LONG, "cancelType"),
        (LONG, "isUidValid"),
        (LONG, "isParentUidValid"),
        (LONG, "isBlockerValid"),
    ]


class FRS_RDC_SOURCE_NEED(NdrStructure):
    MEMBERS = [
        (ULONGLONG, "needOffset"),
        (ULONGLONG, "needSize"),
    ]


class FRS_RDC_PARAMETERS_FILTERMAX(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "horizonSize"),
        (UNSIGNED_SHORT, "windowSize"),
    ]


class FRS_RDC_PARAMETERS_FILTERPOINT(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "minChunkSize"),
        (UNSIGNED_SHORT, "maxChunkSize"),
    ]


class FRS_RDC_PARAMETERS_GENERIC(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "chunkerType"),
        (BYTE, "chunkerParameters"),
    ]


class FRS_RDC_PARAMETERS(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "rdcChunkerAlgorithm"),
        (U, "u"),
    ]


class FRS_RDC_FILEINFO(NdrStructure):
    MEMBERS = [
        (DWORDLONG, "onDiskFileSize"),
        (DWORDLONG, "fileSizeEstimate"),
        (UNSIGNED_SHORT, "rdcVersion"),
        (UNSIGNED_SHORT, "rdcMinimumCompatibleVersion"),
        (BYTE, "rdcSignatureLevels"),
        (RDC_FILE_COMPRESSION_TYPES, "compressionAlgorithm"),
        (FRS_RDC_PARAMETERS, "rdcFilterParameters"),
    ]


class FRS_ASYNC_VERSION_VECTOR_RESPONSE(NdrStructure):
    MEMBERS = [
        (ULONGLONG, "vvGeneration"),
        (UNSIGNED_LONG, "versionVectorCount"),
        (PFRS_VERSION_VECTOR, "versionVector"),
        (UNSIGNED_LONG, "epoqueVectorCount"),
        (PFRS_EPOQUE_VECTOR, "epoqueVector"),
    ]


class FRS_ASYNC_RESPONSE_CONTEXT(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "sequenceNumber"),
        (DWORD, "status"),
        (FRS_ASYNC_VERSION_VECTOR_RESPONSE, "result"),
    ]


Method("CheckConnectivity", In(FRS_REPLICA_SET_ID), In(FRS_CONNECTION_ID),), Method(
    "EstablishConnection",
    In(FRS_REPLICA_SET_ID),
    In(FRS_CONNECTION_ID),
    In(DWORD),
    In(DWORD),
    Out(PDWORD),
    Out(PDWORD),
), Method("EstablishSession", In(FRS_CONNECTION_ID), In(FRS_CONTENT_SET_ID),), Method(
    "RequestUpdates",
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
), Method(
    "RequestVersionVector",
    In(DWORD),
    In(FRS_CONNECTION_ID),
    In(FRS_CONTENT_SET_ID),
    In(VERSION_REQUEST_TYPE),
    In(VERSION_CHANGE_TYPE),
    In(ULONGLONG),
), Method(
    "AsyncPoll",
    In(FRS_CONNECTION_ID),
    Out(PFRS_ASYNC_RESPONSE_CONTEXT),
), Method(
    "RequestRecords",
    In(FRS_CONNECTION_ID),
    In(FRS_CONTENT_SET_ID),
    In(FRS_DATABASE_ID),
    In(DWORDLONG),
    InOut(PDWORD),
    Out(PDWORD),
    Out(PDWORD),
    Out(PPBYTE),
    Out(PRECORDS_STATUS),
), Method(
    "UpdateCancel",
    In(FRS_CONNECTION_ID),
    In(FRS_UPDATE_CANCEL_DATA),
), Method(
    "RawGetFileData",
    InOut(PPFRS_SERVER_CONTEXT),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
    Out(PLONG),
), Method(
    "RdcGetSignatures",
    In(PFRS_SERVER_CONTEXT),
    In(BYTE),
    In(DWORDLONG),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RdcPushSourceNeeds",
    In(PFRS_SERVER_CONTEXT),
    In(PFRS_RDC_SOURCE_NEED),
    In(DWORD),
), Method(
    "RdcGetFileData",
    In(PFRS_SERVER_CONTEXT),
    Out(PBYTE),
    In(DWORD),
    Out(PDWORD),
), Method(
    "RdcClose",
    InOut(PPFRS_SERVER_CONTEXT),
), Method(
    "InitializeFileTransferAsync",
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
), Method(
    "Opnum14NotUsedOnWire",
    In(),
), Method(
    "RawGetFileDataAsync",
    In(PFRS_SERVER_CONTEXT),
    Out(PBYTE_PIPE),
), Method(
    "RdcGetFileDataAsync",
    In(PFRS_SERVER_CONTEXT),
    Out(PBYTE_PIPE),
), Method(
    "RdcFileDataTransferKeepAlive",
    In(PFRS_SERVER_CONTEXT),
),
