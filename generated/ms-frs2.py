"""
Generated from MIDL2Impacket.py
"""


from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG
CONST_UNSIGNED_LONG = NDRULONG
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER

#################################################################################

#"ms-dtyp.idl"

#################################################################################

#################################################################################

#TYPEDEFS

#################################################################################

WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PBOOL = INT
LPBOOL = INT
BYTE = UNSIGNED_CHAR
PBYTE = UNSIGNED_CHAR
LPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PBOOLEAN = BYTE
WCHAR = WCHAR_T
PWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PDWORD = UNSIGNED_LONG
LPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
LPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = CONST_WCHAR_T
LMSTR = WCHAR
LONG = LONG
PLONG = LONG
LPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = __INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PLONG64 = SIGNED___INT64
LPCSTR = CONST_CHAR
LPCVOID = CONST_VOID
LPCWSTR = CONST_WCHAR_T
PSTR = CHAR
LPSTR = CHAR
LPWSTR = WCHAR_T
PWSTR = WCHAR_T
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
PULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PVOID = VOID
LPVOID = VOID
WORD = UNSIGNED_SHORT
PWORD = UNSIGNED_SHORT
LPWORD = UNSIGNED_SHORT

class FILETIME(NDRSTRUCT):
    structure = (
        ('dwLowDateTime', DWORD),('dwHighDateTime', DWORD),
    )
class PFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    
class LPFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    


class GUID(NDRSTRUCT):
    structure = (
        ('Data1', UNSIGNED_LONG),('Data2', UNSIGNED_SHORT),('Data3', UNSIGNED_SHORT),('Data4', BYTE),
    )
UUID = GUID
class PGUID(NDRPOINTER):
    referent = (
        ('Data', GUID),
    )    


class LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', SIGNED___INT64),
    )
class PLARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', LARGE_INTEGER),
    )    


class EVENT_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Id', USHORT),('Version', UCHAR),('Channel', UCHAR),('Level', UCHAR),('Opcode', UCHAR),('Task', USHORT),('Keyword', ULONGLONG),
    )
class PEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    
class PCEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    


class S0(NDRSTRUCT):
    structure = (
        ('KernelTime', ULONG),('UserTime', ULONG),
    )


class U0(NDRUNION):
    union = {
        1: ('s0',S0),2: ('ProcessorTime',ULONG64),
    }
        

class EVENT_HEADER(NDRSTRUCT):
    structure = (
        ('Size', USHORT),('HeaderType', USHORT),('Flags', USHORT),('EventProperty', USHORT),('ThreadId', ULONG),('ProcessId', ULONG),('TimeStamp', LARGE_INTEGER),('ProviderId', GUID),('EventDescriptor', EVENT_DESCRIPTOR),('u0', U0),('ActivityId', GUID),
    )
class PEVENT_HEADER(NDRPOINTER):
    referent = (
        ('Data', EVENT_HEADER),
    )    

LCID = DWORD

class LUID(NDRSTRUCT):
    structure = (
        ('LowPart', DWORD),('HighPart', LONG),
    )
class PLUID(NDRPOINTER):
    referent = (
        ('Data', LUID),
    )    


class MULTI_SZ(NDRSTRUCT):
    structure = (
        ('Value', WCHAR_T),('nChar', DWORD),
    )


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
    item = WCHAR

class PTR_RPC_UNICODE_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_UNICODE_STRING),
    )

class RPC_UNICODE_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_UNICODE_STRING),

    )
        

class SERVER_INFO_100(NDRSTRUCT):
    structure = (
        ('sv100_platform_id', DWORD),('sv100_name', WCHAR_T),
    )
class PSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    
class LPSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    


class SERVER_INFO_101(NDRSTRUCT):
    structure = (
        ('sv101_platform_id', DWORD),('sv101_name', WCHAR_T),('sv101_version_major', DWORD),('sv101_version_minor', DWORD),('sv101_version_type', DWORD),('sv101_comment', WCHAR_T),
    )
class PSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    
class LPSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    


class SYSTEMTIME(NDRSTRUCT):
    structure = (
        ('wYear', WORD),('wMonth', WORD),('wDayOfWeek', WORD),('wDay', WORD),('wHour', WORD),('wMinute', WORD),('wSecond', WORD),('wMilliseconds', WORD),
    )
class PSYSTEMTIME(NDRPOINTER):
    referent = (
        ('Data', SYSTEMTIME),
    )    


class UINT128(NDRSTRUCT):
    structure = (
        ('lower', UINT64),('upper', UINT64),
    )
class PUINT128(NDRPOINTER):
    referent = (
        ('Data', UINT128),
    )    


class ULARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', UNSIGNED___INT64),
    )
class PULARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', ULARGE_INTEGER),
    )    


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
    structure = (
        ('Value', BYTE),
    )

ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NDRSTRUCT):
    structure = (
        ('Level', WORD),('Remaining', ACCESS_MASK),('ObjectType', GUID),
    )
class POBJECT_TYPE_LIST(NDRPOINTER):
    referent = (
        ('Data', OBJECT_TYPE_LIST),
    )    


class ACE_HEADER(NDRSTRUCT):
    structure = (
        ('AceType', UCHAR),('AceFlags', UCHAR),('AceSize', USHORT),
    )
class PACE_HEADER(NDRPOINTER):
    referent = (
        ('Data', ACE_HEADER),
    )    


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
    structure = (
        ('Header', ACE_HEADER),('Mask', ACCESS_MASK),('SidStart', DWORD),
    )
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
    referent = (
        ('Data', SYSTEM_MANDATORY_LABEL_ACE),
    )    


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
    structure = (
        ('Policy', DWORD),
    )
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
    referent = (
        ('Data', TOKEN_MANDATORY_POLICY),
    )    


class MANDATORY_INFORMATION(NDRSTRUCT):
    structure = (
        ('AllowedAccess', ACCESS_MASK),('WriteAllowed', BOOLEAN),('ReadAllowed', BOOLEAN),('ExecuteAllowed', BOOLEAN),('MandatoryPolicy', TOKEN_MANDATORY_POLICY),
    )
class PMANDATORY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', MANDATORY_INFORMATION),
    )    


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
    structure = (
        ('Length', DWORD),('OctetString', BYTE),
    )
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    )    


class VALUES(NDRUNION):
    union = {
        1: ('pInt64',PLONG64),2: ('pUint64',PDWORD64),3: ('ppString',PWSTR),4: ('pOctetString',PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    }
        

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
    structure = (
        ('Name', DWORD),('ValueType', WORD),('Reserved', WORD),('Flags', DWORD),('ValueCount', DWORD),('Values', VALUES),
    )
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1),
    )    

SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD

class RPC_SID(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('SubAuthorityCount', UNSIGNED_CHAR),('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),('SubAuthority', UNSIGNED_LONG),
    )
class PRPC_SID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    
class PSID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    


class ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('AceCount', UNSIGNED_SHORT),('Sbz2', UNSIGNED_SHORT),
    )
class PACL(NDRPOINTER):
    referent = (
        ('Data', ACL),
    )    


class SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UCHAR),('Sbz1', UCHAR),('Control', USHORT),('Owner', PSID),('Group', PSID),('Sacl', PACL),('Dacl', PACL),
    )
class PSECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', SECURITY_DESCRIPTOR),
    )    

#################################################################################

#TYPEDEFS

#################################################################################

FRS_REPLICA_SET_ID = GUID
FRS_CONTENT_SET_ID = GUID
FRS_DATABASE_ID = GUID
FRS_MEMBER_ID = GUID
FRS_CONNECTION_ID = GUID
EPOQUE = SYSTEMTIME

class FRS_VERSION_VECTOR(NDRSTRUCT):
    structure = (
        ('dbGuid', GUID),('low', DWORDLONG),('high', DWORDLONG),
    )


class FRS_EPOQUE_VECTOR(NDRSTRUCT):
    structure = (
        ('machine', GUID),('epoque', EPOQUE),
    )


class FRS_ID_GVSN(NDRSTRUCT):
    structure = (
        ('uidDbGuid', GUID),('uidVersion', DWORDLONG),('gvsnDbGuid', GUID),('gvsnVersion', DWORDLONG),
    )


class FRS_UPDATE(NDRSTRUCT):
    structure = (
        ('present', LONG),('nameConflict', LONG),('attributes', UNSIGNED_LONG),('fence', FILETIME),('clock', FILETIME),('createTime', FILETIME),('contentSetId', FRS_CONTENT_SET_ID),('hash', UNSIGNED_CHAR),('rdcSimilarity', UNSIGNED_CHAR),('uidDbGuid', GUID),('uidVersion', DWORDLONG),('gvsnDbGuid', GUID),('gvsnVersion', DWORDLONG),('parentDbGuid', GUID),('parentVersion', DWORDLONG),('name', WCHAR),('flags', LONG),
    )


class FRS_UPDATE_CANCEL_DATA(NDRSTRUCT):
    structure = (
        ('blockingUpdate', FRS_UPDATE),('contentSetId', FRS_CONTENT_SET_ID),('gvsnDatabaseId', FRS_DATABASE_ID),('uidDatabaseId', FRS_DATABASE_ID),('parentDatabaseId', FRS_DATABASE_ID),('gvsnVersion', DWORDLONG),('uidVersion', DWORDLONG),('parentVersion', DWORDLONG),('cancelType', UNSIGNED_LONG),('isUidValid', LONG),('isParentUidValid', LONG),('isBlockerValid', LONG),
    )


class FRS_RDC_SOURCE_NEED(NDRSTRUCT):
    structure = (
        ('needOffset', ULONGLONG),('needSize', ULONGLONG),
    )


TRANSPORT_SUPPORTS_RDC_SIMILARITY = 1
        

RDC_UNCOMPRESSED = 0,
RDC_XPRESS = 1
        

RDC_FILTERGENERIC = 0,
RDC_FILTERMAX = 1,
RDC_FILTERPOINT = 2,
RDC_MAXALGORITHM = 3
        

UPDATE_REQUEST_ALL = 0,
UPDATE_REQUEST_TOMBSTONES = 1,
UPDATE_REQUEST_LIVE = 2
        

UPDATE_STATUS_DONE = 2,
UPDATE_STATUS_MORE = 3
        

RECORDS_STATUS_DONE = 0,
RECORDS_STATUS_MORE = 1
        

REQUEST_NORMAL_SYNC = 0,
REQUEST_SLOW_SYNC = 1,
REQUEST_SUBORDINATE_SYNC = 2
        

CHANGE_NOTIFY = 0,
CHANGE_ALL = 2
        

SERVER_DEFAULT = 0,
STAGING_REQUIRED = 1,
RESTAGING_REQUIRED = 2
        

class FRS_RDC_PARAMETERS_FILTERMAX(NDRSTRUCT):
    structure = (
        ('horizonSize', UNSIGNED_SHORT),('windowSize', UNSIGNED_SHORT),
    )


class FRS_RDC_PARAMETERS_FILTERPOINT(NDRSTRUCT):
    structure = (
        ('minChunkSize', UNSIGNED_SHORT),('maxChunkSize', UNSIGNED_SHORT),
    )


class FRS_RDC_PARAMETERS_GENERIC(NDRSTRUCT):
    structure = (
        ('chunkerType', UNSIGNED_SHORT),('chunkerParameters', BYTE),
    )


class U(NDRUNION):
    union = {
        RDC_FILTERGENERIC: ('filterGeneric',FRS_RDC_PARAMETERS_GENERIC),RDC_FILTERMAX: ('filterMax',FRS_RDC_PARAMETERS_FILTERMAX),RDC_FILTERPOINT: ('filterPoint',FRS_RDC_PARAMETERS_FILTERPOINT),
    }
        

class FRS_RDC_PARAMETERS(NDRSTRUCT):
    structure = (
        ('rdcChunkerAlgorithm', UNSIGNED_SHORT),('u', U),
    )


class FRS_RDC_FILEINFO(NDRSTRUCT):
    structure = (
        ('onDiskFileSize', DWORDLONG),('fileSizeEstimate', DWORDLONG),('rdcVersion', UNSIGNED_SHORT),('rdcMinimumCompatibleVersion', UNSIGNED_SHORT),('rdcSignatureLevels', BYTE),('compressionAlgorithm', RDC_FILE_COMPRESSION_TYPES),('rdcFilterParameters', FRS_RDC_PARAMETERS),
    )


class DATA_FRS_ASYNC_VERSION_VECTOR_RESPONSE(NDRUniConformantArray):
    item = FRS_EPOQUE_VECTOR

class PTR_FRS_ASYNC_VERSION_VECTOR_RESPONSE(NDRPOINTER):
    referent = (
        ('Data', DATA_FRS_ASYNC_VERSION_VECTOR_RESPONSE),
    )

class FRS_ASYNC_VERSION_VECTOR_RESPONSE(NDRSTRUCT):
    structure = (
	('vvGeneration', ULONGLONG),	('versionVectorCount', UNSIGNED_LONG),	('versionVector', FRS_VERSION_VECTOR),	('epoqueVectorCount', UNSIGNED_LONG),	('epoqueVector', PTR_FRS_ASYNC_VERSION_VECTOR_RESPONSE),

    )
        

class FRS_ASYNC_RESPONSE_CONTEXT(NDRSTRUCT):
    structure = (
        ('sequenceNumber', UNSIGNED_LONG),('status', DWORD),('result', FRS_ASYNC_VERSION_VECTOR_RESPONSE),
    )

BYTE_PIPE = PIPE BYTE
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#FrsTransport Definition

#################################################################################

MSRPC_UUID_FRSTRANSPORT = uuidtup_to_bin(('897e2e5f-93f3-4376-9c9c-fd2277495c27','0.0'))

PFRS_SERVER_CONTEXT = VOID

class CheckConnectivity(NDRCALL):
    opnum = 0
    structure = (
		('REPLICASETID', FRS_REPLICA_SET_ID),
		('CONNECTIONID', FRS_CONNECTION_ID),
    )

class CheckConnectivityResponse(NDRCALL):
    structure = (

    )
        

class EstablishConnection(NDRCALL):
    opnum = 1
    structure = (
		('REPLICASETID', FRS_REPLICA_SET_ID),
		('CONNECTIONID', FRS_CONNECTION_ID),
		('DOWNSTREAMPROTOCOLVERSION', DWORD),
		('DOWNSTREAMFLAGS', DWORD),
    )

class EstablishConnectionResponse(NDRCALL):
    structure = (
		('UPSTREAMPROTOCOLVERSION', DWORD),
		('UPSTREAMFLAGS', DWORD),
    )
        

class EstablishSession(NDRCALL):
    opnum = 2
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
		('CONTENTSETID', FRS_CONTENT_SET_ID),
    )

class EstablishSessionResponse(NDRCALL):
    structure = (

    )
        

class RequestUpdates(NDRCALL):
    opnum = 3
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
		('CONTENTSETID', FRS_CONTENT_SET_ID),
		('CREDITSAVAILABLE', DWORD),
		('HASHREQUESTED', LONG),
		('UPDATEREQUESTTYPE', UPDATE_REQUEST_TYPE),
		('VERSIONVECTORDIFFCOUNT', UNSIGNED_LONG),
		('VERSIONVECTORDIFF', FRS_VERSION_VECTOR),
    )

class RequestUpdatesResponse(NDRCALL):
    structure = (
		('FRSUPDATE', FRS_UPDATE),
		('UPDATECOUNT', DWORD),
		('UPDATESTATUS', UPDATE_STATUS),
		('GVSNDBGUID', GUID),
		('GVSNVERSION', DWORDLONG),
    )
        

class RequestVersionVector(NDRCALL):
    opnum = 4
    structure = (
		('SEQUENCENUMBER', DWORD),
		('CONNECTIONID', FRS_CONNECTION_ID),
		('CONTENTSETID', FRS_CONTENT_SET_ID),
		('REQUESTTYPE', VERSION_REQUEST_TYPE),
		('CHANGETYPE', VERSION_CHANGE_TYPE),
		('VVGENERATION', ULONGLONG),
    )

class RequestVersionVectorResponse(NDRCALL):
    structure = (

    )
        

class AsyncPoll(NDRCALL):
    opnum = 5
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
    )

class AsyncPollResponse(NDRCALL):
    structure = (
		('RESPONSE', FRS_ASYNC_RESPONSE_CONTEXT),
    )
        

class RequestRecords(NDRCALL):
    opnum = 6
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
		('CONTENTSETID', FRS_CONTENT_SET_ID),
		('UIDDBGUID', FRS_DATABASE_ID),
		('UIDVERSION', DWORDLONG),
		('MAXRECORDS', DWORD),
    )

class RequestRecordsResponse(NDRCALL):
    structure = (
		('MAXRECORDS', DWORD),
		('NUMRECORDS', DWORD),
		('NUMBYTES', DWORD),
		('COMPRESSEDRECORDS', BYTE),
		('RECORDSSTATUS', RECORDS_STATUS),
    )
        

class UpdateCancel(NDRCALL):
    opnum = 7
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
		('CANCELDATA', FRS_UPDATE_CANCEL_DATA),
    )

class UpdateCancelResponse(NDRCALL):
    structure = (

    )
        

class RawGetFileData(NDRCALL):
    opnum = 8
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('BUFFERSIZE', DWORD),
    )

class RawGetFileDataResponse(NDRCALL):
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('DATABUFFER', BYTE),
		('SIZEREAD', DWORD),
		('ISENDOFFILE', LONG),
    )
        

class RdcGetSignatures(NDRCALL):
    opnum = 9
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('LEVEL', BYTE),
		('OFFSET', DWORDLONG),
		('LENGTH', DWORD),
    )

class RdcGetSignaturesResponse(NDRCALL):
    structure = (
		('BUFFER', BYTE),
		('SIZEREAD', DWORD),
    )
        

class RdcPushSourceNeeds(NDRCALL):
    opnum = 10
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('SOURCENEEDS', FRS_RDC_SOURCE_NEED),
		('NEEDCOUNT', DWORD),
    )

class RdcPushSourceNeedsResponse(NDRCALL):
    structure = (

    )
        

class RdcGetFileData(NDRCALL):
    opnum = 11
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('BUFFERSIZE', DWORD),
    )

class RdcGetFileDataResponse(NDRCALL):
    structure = (
		('DATABUFFER', BYTE),
		('SIZERETURNED', DWORD),
    )
        

class RdcClose(NDRCALL):
    opnum = 12
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
    )

class RdcCloseResponse(NDRCALL):
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
    )
        

class InitializeFileTransferAsync(NDRCALL):
    opnum = 13
    structure = (
		('CONNECTIONID', FRS_CONNECTION_ID),
		('FRSUPDATE', FRS_UPDATE),
		('RDCDESIRED', LONG),
		('STAGINGPOLICY', FRS_REQUESTED_STAGING_POLICY),
		('BUFFERSIZE', DWORD),
    )

class InitializeFileTransferAsyncResponse(NDRCALL):
    structure = (
		('FRSUPDATE', FRS_UPDATE),
		('STAGINGPOLICY', FRS_REQUESTED_STAGING_POLICY),
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
		('RDCFILEINFO', FRS_RDC_FILEINFO),
		('DATABUFFER', BYTE),
		('SIZEREAD', DWORD),
		('ISENDOFFILE', LONG),
    )
        

class Opnum14NotUsedOnWire(NDRCALL):
    opnum = 14
    structure = (

    )

class Opnum14NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RawGetFileDataAsync(NDRCALL):
    opnum = 15
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
    )

class RawGetFileDataAsyncResponse(NDRCALL):
    structure = (
		('BYTEPIPE', BYTE_PIPE),
    )
        

class RdcGetFileDataAsync(NDRCALL):
    opnum = 16
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
    )

class RdcGetFileDataAsyncResponse(NDRCALL):
    structure = (
		('BYTEPIPE', BYTE_PIPE),
    )
        

class RdcFileDataTransferKeepAlive(NDRCALL):
    opnum = 17
    structure = (
		('SERVERCONTEXT', PFRS_SERVER_CONTEXT),
    )

class RdcFileDataTransferKeepAliveResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CheckConnectivity,CheckConnectivityResponse),
1 : (EstablishConnection,EstablishConnectionResponse),
2 : (EstablishSession,EstablishSessionResponse),
3 : (RequestUpdates,RequestUpdatesResponse),
4 : (RequestVersionVector,RequestVersionVectorResponse),
5 : (AsyncPoll,AsyncPollResponse),
6 : (RequestRecords,RequestRecordsResponse),
7 : (UpdateCancel,UpdateCancelResponse),
8 : (RawGetFileData,RawGetFileDataResponse),
9 : (RdcGetSignatures,RdcGetSignaturesResponse),
10 : (RdcPushSourceNeeds,RdcPushSourceNeedsResponse),
11 : (RdcGetFileData,RdcGetFileDataResponse),
12 : (RdcClose,RdcCloseResponse),
13 : (InitializeFileTransferAsync,InitializeFileTransferAsyncResponse),
14 : (Opnum14NotUsedOnWire,Opnum14NotUsedOnWireResponse),
15 : (RawGetFileDataAsync,RawGetFileDataAsyncResponse),
16 : (RdcGetFileDataAsync,RdcGetFileDataAsyncResponse),
17 : (RdcFileDataTransferKeepAlive,RdcFileDataTransferKeepAliveResponse),
}

