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
DWORD64 = LONGLONG
__INT64 = DWORD64
LPCWSTR = LPWSTR
LCID = DWORD
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

#################################################################################

#TYPEDEFS

#################################################################################

#################################################################################

#CONSTANTS

#################################################################################

MAX_PAYLOAD = 2 * 1024 * 1024
MAX_RPC_QUERY_LENGTH = MAX_PAYLOAD / 4
MAX_RPC_CHANNEL_NAME_LENGTH = 512
MAX_RPC_QUERY_CHANNEL_SIZE = 512
MAX_RPC_EVENT_ID_SIZE = 256
MAX_RPC_FILE_PATH_LENGTH = 32768
MAX_RPC_CHANNEL_PATH_LENGTH = 32768
MAX_RPC_BOOKMARK_LENGTH = MAX_PAYLOAD / 4
MAX_RPC_PUBLISHER_ID_LENGTH = 2048
MAX_RPC_PROPERTY_BUFFER_SIZE = MAX_PAYLOAD
MAX_RPC_FILTER_LENGTH = MAX_RPC_QUERY_LENGTH
MAX_RPC_RECORD_COUNT = 1024
MAX_RPC_EVENT_SIZE = MAX_PAYLOAD
MAX_RPC_BATCH_SIZE = MAX_PAYLOAD
MAX_RPC_RENDERED_STRING_SIZE = MAX_PAYLOAD
MAX_RPC_CHANNEL_COUNT = 8192
MAX_RPC_PUBLISHER_COUNT = 8192
MAX_RPC_EVENT_METADATA_COUNT = 256
MAX_RPC_VARIANT_LIST_COUNT = 256
MAX_RPC_BOOL_ARRAY_COUNT = MAX_PAYLOAD / 1
MAX_RPC_UINT32_ARRAY_COUNT = MAX_PAYLOAD / 2
MAX_RPC_UINT64_ARRAY_COUNT = MAX_PAYLOAD / 4
MAX_RPC_STRING_ARRAY_COUNT = MAX_PAYLOAD / 512
MAX_RPC_GUID_ARRAY_COUNT = MAX_PAYLOAD / 16
MAX_RPC_STRING_LENGTH = MAX_PAYLOAD / 4
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IEventService Definition

#################################################################################

MSRPC_UUID_IEVENTSERVICE = uuidtup_to_bin(('uuid(f6beaff7-1e19-4fbb-9f8f-b89e2018337c,)','0.0'))

PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION = VOID
PCONTEXT_HANDLE_LOG_QUERY = VOID
PCONTEXT_HANDLE_LOG_HANDLE = VOID
PCONTEXT_HANDLE_OPERATION_CONTROL = VOID
PCONTEXT_HANDLE_PUBLISHER_METADATA = VOID
PCONTEXT_HANDLE_EVENT_METADATA_ENUM = VOID

class RPCINFO(NDRSTRUCT):
    structure = (
        ('m_error', DWORD),('m_subErr', DWORD),('m_subErrParam', DWORD),
    )
        

class DATA_BOOLEANARRAY(NDRUniConformantArray):
    item = BOOLEAN

class PTR_BOOLEANARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_BOOLEANARRAY),
    )

class BOOLEANARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_BOOLEANARRAY),

    )
        

class DATA_UINT32ARRAY(NDRUniConformantArray):
    item = DWORD

class PTR_UINT32ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT32ARRAY),
    )

class UINT32ARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_UINT32ARRAY),

    )
        

class DATA_UINT64ARRAY(NDRUniConformantArray):
    item = DWORD64

class PTR_UINT64ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT64ARRAY),
    )

class UINT64ARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_UINT64ARRAY),

    )
        

class DATA_STRINGARRAY(NDRUniConformantArray):
    item = LPWSTR

class PTR_STRINGARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_STRINGARRAY),
    )

class STRINGARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_STRINGARRAY),

    )
        

class DATA_GUIDARRAY(NDRUniConformantArray):
    item = GUID

class PTR_GUIDARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_GUIDARRAY),
    )

class GUIDARRAY(NDRSTRUCT):
    structure = (
	('count', DWORD),	('ptr', PTR_GUIDARRAY),

    )
        

class EVTRPCVARIANTTYPE:
	EvtRpcVarTypeNull = 0,
	EvtRpcVarTypeBoolean = 1,
	EvtRpcVarTypeUInt32 = 2,
	EvtRpcVarTypeUInt64 = 3,
	EvtRpcVarTypeString = 4,
	EvtRpcVarTypeGuid = 5,
	EvtRpcVarTypeBooleanArray = 6,
	EvtRpcVarTypeUInt32Array = 7,
	EvtRpcVarTypeUInt64Array = 8,
	EvtRpcVarTypeStringArray = 9
        

class EVTRPCASSERTCONFIGFLAGS:
	EvtRpcChannelPath = 0
        

class U0(NDRUNION):
    union = {
        1: ('nullVal',INT),2: ('booleanVal',BOOLEAN),3: ('uint32Val',DWORD),4: ('uint64Val',DWORD64),5: ('stringVal',LPWSTR),6: ('guidVal',GUID),7: ('booleanArray',BOOLEANARRAY),8: ('uint32Array',UINT32ARRAY),9: ('uint64Array',UINT64ARRAY),10: ('stringArray',STRINGARRAY),11: ('guidArray',GUIDARRAY),
    }
        

class EVTRPCVARIANT(NDRSTRUCT):
    structure = (
        ('type', EVTRPCVARIANTTYPE),('flags', DWORD),('u0', U0),
    )
        

class DATA_EVTRPCVARIANTLIST(NDRUniConformantArray):
    item = EVTRPCVARIANT

class PTR_EVTRPCVARIANTLIST(NDRPOINTER):
    referent = (
        ('Data', DATA_EVTRPCVARIANTLIST),
    )

class EVTRPCVARIANTLIST(NDRSTRUCT):
    structure = (
	('count', DWORD),	('props', PTR_EVTRPCVARIANTLIST),

    )
        

class EVTRPCQUERYCHANNELINFO(NDRSTRUCT):
    structure = (
        ('name', LPWSTR),('status', DWORD),
    )
        

class EvtRpcRegisterRemoteSubscription(NDRCALL):
    opnum = 0
    structure = (
		('channelPath', LPCWSTR),
		('query', LPCWSTR),
		('bookmarkXml', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcRegisterRemoteSubscriptionResponse(NDRCALL):
    structure = (
		('handle', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('control', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('queryChannelInfoSize', DWORD),
		('queryChannelInfo', EVTRPCQUERYCHANNELINFO),
		('error', RPCINFO),
    )
        

class EvtRpcRemoteSubscriptionNextAsync(NDRCALL):
    opnum = 1
    structure = (
		('handle', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('numRequestedRecords', DWORD),
		('flags', DWORD),
    )

class EvtRpcRemoteSubscriptionNextAsyncResponse(NDRCALL):
    structure = (
		('numActualRecords', DWORD),
		('eventDataIndices', DWORD),
		('eventDataSizes', DWORD),
		('resultBufferSize', DWORD),
		('resultBuffer', BYTE),
    )
        

class EvtRpcRemoteSubscriptionNext(NDRCALL):
    opnum = 2
    structure = (
		('handle', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
		('numRequestedRecords', DWORD),
		('timeOut', DWORD),
		('flags', DWORD),
    )

class EvtRpcRemoteSubscriptionNextResponse(NDRCALL):
    structure = (
		('numActualRecords', DWORD),
		('eventDataIndices', DWORD),
		('eventDataSizes', DWORD),
		('resultBufferSize', DWORD),
		('resultBuffer', BYTE),
    )
        

class EvtRpcRemoteSubscriptionWaitAsync(NDRCALL):
    opnum = 3
    structure = (
		('handle', PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION),
    )

class EvtRpcRemoteSubscriptionWaitAsyncResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcRegisterControllableOperation(NDRCALL):
    opnum = 4
    structure = (

    )

class EvtRpcRegisterControllableOperationResponse(NDRCALL):
    structure = (
		('handle', PCONTEXT_HANDLE_OPERATION_CONTROL),
    )
        

class EvtRpcRegisterLogQuery(NDRCALL):
    opnum = 5
    structure = (
		('path', LPCWSTR),
		('query', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcRegisterLogQueryResponse(NDRCALL):
    structure = (
		('handle', PCONTEXT_HANDLE_LOG_QUERY),
		('opControl', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('queryChannelInfoSize', DWORD),
		('queryChannelInfo', EVTRPCQUERYCHANNELINFO),
		('error', RPCINFO),
    )
        

class EvtRpcClearLog(NDRCALL):
    opnum = 6
    structure = (
		('control', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('channelPath', LPCWSTR),
		('backupPath', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcClearLogResponse(NDRCALL):
    structure = (
		('error', RPCINFO),
    )
        

class EvtRpcExportLog(NDRCALL):
    opnum = 7
    structure = (
		('control', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('channelPath', LPCWSTR),
		('query', LPCWSTR),
		('backupPath', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcExportLogResponse(NDRCALL):
    structure = (
		('error', RPCINFO),
    )
        

class EvtRpcLocalizeExportLog(NDRCALL):
    opnum = 8
    structure = (
		('control', PCONTEXT_HANDLE_OPERATION_CONTROL),
		('logFilePath', LPCWSTR),
		('locale', LCID),
		('flags', DWORD),
    )

class EvtRpcLocalizeExportLogResponse(NDRCALL):
    structure = (
		('error', RPCINFO),
    )
        

class EvtRpcMessageRender(NDRCALL):
    opnum = 9
    structure = (
		('pubCfgObj', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('sizeEventId', DWORD),
		('eventId', BYTE),
		('messageId', DWORD),
		('values', EVTRPCVARIANTLIST),
		('flags', DWORD),
		('maxSizeString', DWORD),
    )

class EvtRpcMessageRenderResponse(NDRCALL):
    structure = (
		('actualSizeString', DWORD),
		('neededSizeString', DWORD),
		('string', BYTE),
		('error', RPCINFO),
    )
        

class EvtRpcMessageRenderDefault(NDRCALL):
    opnum = 10
    structure = (
		('sizeEventId', DWORD),
		('eventId', BYTE),
		('messageId', DWORD),
		('values', EVTRPCVARIANTLIST),
		('flags', DWORD),
		('maxSizeString', DWORD),
    )

class EvtRpcMessageRenderDefaultResponse(NDRCALL):
    structure = (
		('actualSizeString', DWORD),
		('neededSizeString', DWORD),
		('string', BYTE),
		('error', RPCINFO),
    )
        

class EvtRpcQueryNext(NDRCALL):
    opnum = 11
    structure = (
		('logQuery', PCONTEXT_HANDLE_LOG_QUERY),
		('numRequestedRecords', DWORD),
		('timeOutEnd', DWORD),
		('flags', DWORD),
    )

class EvtRpcQueryNextResponse(NDRCALL):
    structure = (
		('numActualRecords', DWORD),
		('eventDataIndices', DWORD),
		('eventDataSizes', DWORD),
		('resultBufferSize', DWORD),
		('resultBuffer', BYTE),
    )
        

class EvtRpcQuerySeek(NDRCALL):
    opnum = 12
    structure = (
		('logQuery', PCONTEXT_HANDLE_LOG_QUERY),
		('pos', __INT64),
		('bookmarkXml', LPCWSTR),
		('timeOut', DWORD),
		('flags', DWORD),
    )

class EvtRpcQuerySeekResponse(NDRCALL):
    structure = (
		('error', RPCINFO),
    )
        

class EvtRpcClose(NDRCALL):
    opnum = 13
    structure = (
		('handle', CONTEXT_HANDLE),
    )

class EvtRpcCloseResponse(NDRCALL):
    structure = (
		('handle', CONTEXT_HANDLE),
    )
        

class EvtRpcCancel(NDRCALL):
    opnum = 14
    structure = (
		('handle', PCONTEXT_HANDLE_OPERATION_CONTROL),
    )

class EvtRpcCancelResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcAssertConfig(NDRCALL):
    opnum = 15
    structure = (
		('path', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcAssertConfigResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcRetractConfig(NDRCALL):
    opnum = 16
    structure = (
		('path', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcRetractConfigResponse(NDRCALL):
    structure = (

    )
        

class EvtRpcOpenLogHandle(NDRCALL):
    opnum = 17
    structure = (
		('channel', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcOpenLogHandleResponse(NDRCALL):
    structure = (
		('handle', PCONTEXT_HANDLE_LOG_HANDLE),
		('error', RPCINFO),
    )
        

class EvtRpcGetLogFileInfo(NDRCALL):
    opnum = 18
    structure = (
		('logHandle', PCONTEXT_HANDLE_LOG_HANDLE),
		('propertyId', DWORD),
		('propertyValueBufferSize', DWORD),
    )

class EvtRpcGetLogFileInfoResponse(NDRCALL):
    structure = (
		('propertyValueBuffer', BYTE),
		('propertyValueBufferLength', DWORD),
    )
        

class EvtRpcGetChannelList(NDRCALL):
    opnum = 19
    structure = (
		('flags', DWORD),
    )

class EvtRpcGetChannelListResponse(NDRCALL):
    structure = (
		('numChannelPaths', DWORD),
		('channelPaths', LPWSTR),
    )
        

class EvtRpcGetChannelConfig(NDRCALL):
    opnum = 20
    structure = (
		('channelPath', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcGetChannelConfigResponse(NDRCALL):
    structure = (
		('props', EVTRPCVARIANTLIST),
    )
        

class EvtRpcPutChannelConfig(NDRCALL):
    opnum = 21
    structure = (
		('channelPath', LPCWSTR),
		('flags', DWORD),
		('props', EVTRPCVARIANTLIST),
    )

class EvtRpcPutChannelConfigResponse(NDRCALL):
    structure = (
		('error', RPCINFO),
    )
        

class EvtRpcGetPublisherList(NDRCALL):
    opnum = 22
    structure = (
		('flags', DWORD),
    )

class EvtRpcGetPublisherListResponse(NDRCALL):
    structure = (
		('numPublisherIds', DWORD),
		('publisherIds', LPWSTR),
    )
        

class EvtRpcGetPublisherListForChannel(NDRCALL):
    opnum = 23
    structure = (
		('channelName', LPCWSTR),
		('flags', DWORD),
    )

class EvtRpcGetPublisherListForChannelResponse(NDRCALL):
    structure = (
		('numPublisherIds', DWORD),
		('publisherIds', LPWSTR),
    )
        

class EvtRpcGetPublisherMetadata(NDRCALL):
    opnum = 24
    structure = (
		('publisherId', LPCWSTR),
		('logFilePath', LPCWSTR),
		('locale', LCID),
		('flags', DWORD),
    )

class EvtRpcGetPublisherMetadataResponse(NDRCALL):
    structure = (
		('pubMetadataProps', EVTRPCVARIANTLIST),
		('pubMetadata', PCONTEXT_HANDLE_PUBLISHER_METADATA),
    )
        

class EvtRpcGetPublisherResourceMetadata(NDRCALL):
    opnum = 25
    structure = (
		('handle', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('propertyId', DWORD),
		('flags', DWORD),
    )

class EvtRpcGetPublisherResourceMetadataResponse(NDRCALL):
    structure = (
		('pubMetadataProps', EVTRPCVARIANTLIST),
    )
        

class EvtRpcGetEventMetadataEnum(NDRCALL):
    opnum = 26
    structure = (
		('pubMetadata', PCONTEXT_HANDLE_PUBLISHER_METADATA),
		('flags', DWORD),
		('reservedForFilter', LPCWSTR),
    )

class EvtRpcGetEventMetadataEnumResponse(NDRCALL):
    structure = (
		('eventMetaDataEnum', PCONTEXT_HANDLE_EVENT_METADATA_ENUM),
    )
        

class EvtRpcGetNextEventMetadata(NDRCALL):
    opnum = 27
    structure = (
		('eventMetaDataEnum', PCONTEXT_HANDLE_EVENT_METADATA_ENUM),
		('flags', DWORD),
		('numRequested', DWORD),
    )

class EvtRpcGetNextEventMetadataResponse(NDRCALL):
    structure = (
		('numReturned', DWORD),
		('eventMetadataInstances', EVTRPCVARIANTLIST),
    )
        

class EvtRpcGetClassicLogDisplayName(NDRCALL):
    opnum = 28
    structure = (
		('logName', LPCWSTR),
		('locale', LCID),
		('flags', DWORD),
    )

class EvtRpcGetClassicLogDisplayNameResponse(NDRCALL):
    structure = (
		('displayName', LPWSTR),
    )
        
OPNUMS = {
0 : (EvtRpcRegisterRemoteSubscription,EvtRpcRegisterRemoteSubscriptionResponse),
1 : (EvtRpcRemoteSubscriptionNextAsync,EvtRpcRemoteSubscriptionNextAsyncResponse),
2 : (EvtRpcRemoteSubscriptionNext,EvtRpcRemoteSubscriptionNextResponse),
3 : (EvtRpcRemoteSubscriptionWaitAsync,EvtRpcRemoteSubscriptionWaitAsyncResponse),
4 : (EvtRpcRegisterControllableOperation,EvtRpcRegisterControllableOperationResponse),
5 : (EvtRpcRegisterLogQuery,EvtRpcRegisterLogQueryResponse),
6 : (EvtRpcClearLog,EvtRpcClearLogResponse),
7 : (EvtRpcExportLog,EvtRpcExportLogResponse),
8 : (EvtRpcLocalizeExportLog,EvtRpcLocalizeExportLogResponse),
9 : (EvtRpcMessageRender,EvtRpcMessageRenderResponse),
10 : (EvtRpcMessageRenderDefault,EvtRpcMessageRenderDefaultResponse),
11 : (EvtRpcQueryNext,EvtRpcQueryNextResponse),
12 : (EvtRpcQuerySeek,EvtRpcQuerySeekResponse),
13 : (EvtRpcClose,EvtRpcCloseResponse),
14 : (EvtRpcCancel,EvtRpcCancelResponse),
15 : (EvtRpcAssertConfig,EvtRpcAssertConfigResponse),
16 : (EvtRpcRetractConfig,EvtRpcRetractConfigResponse),
17 : (EvtRpcOpenLogHandle,EvtRpcOpenLogHandleResponse),
18 : (EvtRpcGetLogFileInfo,EvtRpcGetLogFileInfoResponse),
19 : (EvtRpcGetChannelList,EvtRpcGetChannelListResponse),
20 : (EvtRpcGetChannelConfig,EvtRpcGetChannelConfigResponse),
21 : (EvtRpcPutChannelConfig,EvtRpcPutChannelConfigResponse),
22 : (EvtRpcGetPublisherList,EvtRpcGetPublisherListResponse),
23 : (EvtRpcGetPublisherListForChannel,EvtRpcGetPublisherListForChannelResponse),
24 : (EvtRpcGetPublisherMetadata,EvtRpcGetPublisherMetadataResponse),
25 : (EvtRpcGetPublisherResourceMetadata,EvtRpcGetPublisherResourceMetadataResponse),
26 : (EvtRpcGetEventMetadataEnum,EvtRpcGetEventMetadataEnumResponse),
27 : (EvtRpcGetNextEventMetadata,EvtRpcGetNextEventMetadataResponse),
28 : (EvtRpcGetClassicLogDisplayName,EvtRpcGetClassicLogDisplayNameResponse),
}

