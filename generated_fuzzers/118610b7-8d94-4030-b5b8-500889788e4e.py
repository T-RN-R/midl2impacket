
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

    

class ('COMVERSION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "MajorVersion"),(('UNSIGNED_SHORT', None), "MinorVersion"),]

    

class ('ORPC_EXTENT', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "id"),(('UNSIGNED_LONG', None), "size"),(('BYTE', None), "data"),]

    

class ('ORPC_EXTENT_ARRAY', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "size"),(('UNSIGNED_LONG', None), "reserved"),(('PPORPC_EXTENT', None), "extent"),]

    

class ('ORPCTHIS', None)(NdrStructure):
    MEMBERS = [(('COMVERSION', None), "version"),(('UNSIGNED_LONG', None), "flags"),(('UNSIGNED_LONG', None), "reserved1"),(('CID', None), "cid"),(('PORPC_EXTENT_ARRAY', None), "extensions"),]

    

class ('ORPCTHAT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "flags"),(('PORPC_EXTENT_ARRAY', None), "extensions"),]

    

class ('DUALSTRINGARRAY', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "wNumEntries"),(('UNSIGNED_SHORT', None), "wSecurityOffset"),(('UNSIGNED_SHORT', None), "aStringArray"),]

    

class ('MINTERFACEPOINTER', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulCntData"),(('BYTE', None), "abData"),]

    

class ('ERROROBJECTDATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('DWORD', None), "dwHelpContext"),(('IID', None), "iid"),(('PWCHAR_T', None), "pszSource"),(('PWCHAR_T', None), "pszDescription"),(('PWCHAR_T', None), "pszHelpFile"),]

    

class ('STDOBJREF', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "flags"),(('UNSIGNED_LONG', None), "cPublicRefs"),(('OXID', None), "oxid"),(('OID', None), "oid"),(('IPID', None), "ipid"),]

    

class ('REMQIRESULT', None)(NdrStructure):
    MEMBERS = [(('HRESULT', None), "hResult"),(('STDOBJREF', None), "std"),]

    

class ('REMINTERFACEREF', None)(NdrStructure):
    MEMBERS = [(('IPID', None), "ipid"),(('UNSIGNED_LONG', None), "cPublicRefs"),(('UNSIGNED_LONG', None), "cPrivateRefs"),]

    

class ('COSERVERINFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwReserved1"),(('PWCHAR_T', None), "pwszName"),(('PDWORD', None), "pdwReserved"),(('DWORD', None), "dwReserved2"),]

    

class ('CUSTOMREMOTE_REQUEST_SCM_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "ClientImpLevel"),(('UNSIGNED_SHORT', None), "cRequestedProtseqs"),(('PUNSIGNED_SHORT', None), "pRequestedProtseqs"),]

    

class ('CUSTOMREMOTE_REPLY_SCM_INFO', None)(NdrStructure):
    MEMBERS = [(('OXID', None), "Oxid"),(('PDUALSTRINGARRAY', None), "pdsaOxidBindings"),(('IPID', None), "ipidRemUnknown"),(('DWORD', None), "authnHint"),(('COMVERSION', None), "serverVersion"),]

    

class ('INSTANTIATIONINFODATA', None)(NdrStructure):
    MEMBERS = [(('CLSID', None), "classId"),(('DWORD', None), "classCtx"),(('DWORD', None), "actvflags"),(('LONG', None), "fIsSurrogate"),(('DWORD', None), "cIID"),(('DWORD', None), "instFlag"),(('PIID', None), "pIID"),(('DWORD', None), "thisSize"),(('COMVERSION', None), "clientCOMVersion"),]

    

class ('LOCATIONINFODATA', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "machineName"),(('DWORD', None), "processId"),(('DWORD', None), "apartmentId"),(('DWORD', None), "contextId"),]

    

class ('ACTIVATIONCONTEXTINFODATA', None)(NdrStructure):
    MEMBERS = [(('LONG', None), "clientOK"),(('LONG', None), "bReserved1"),(('DWORD', None), "dwReserved1"),(('DWORD', None), "dwReserved2"),(('PMINTERFACEPOINTER', None), "pIFDClientCtx"),(('PMINTERFACEPOINTER', None), "pIFDPrototypeCtx"),]

    

class ('CUSTOMHEADER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "totalSize"),(('DWORD', None), "headerSize"),(('DWORD', None), "dwReserved"),(('DWORD', None), "destCtx"),(('DWORD', None), "cIfs"),(('CLSID', None), "classInfoClsid"),(('PCLSID', None), "pclsid"),(('PDWORD', None), "pSizes"),(('PDWORD', None), "pdwReserved"),]

    

class ('PROPSOUTINFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "cIfs"),(('PIID', None), "piid"),(('PHRESULT', None), "phresults"),(('PPMINTERFACEPOINTER', None), "ppIntfData"),]

    

class ('SECURITYINFODATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAuthnFlags"),(('PCOSERVERINFO', None), "pServerInfo"),(('PDWORD', None), "pdwReserved"),]

    

class ('SCMREQUESTINFODATA', None)(NdrStructure):
    MEMBERS = [(('PDWORD', None), "pdwReserved"),(('PCUSTOMREMOTE_REQUEST_SCM_INFO', None), "remoteRequest"),]

    

class ('SCMREPLYINFODATA', None)(NdrStructure):
    MEMBERS = [(('PDWORD', None), "pdwReserved"),(('PCUSTOMREMOTE_REPLY_SCM_INFO', None), "remoteReply"),]

    

class ('INSTANCEINFODATA', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "fileName"),(('DWORD', None), "mode"),(('PMINTERFACEPOINTER', None), "ifdROT"),(('PMINTERFACEPOINTER', None), "ifdStg"),]

    

class ('SPECIALPROPERTIESDATA', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "dwSessionId"),(('LONG', None), "fRemoteThisSessionId"),(('LONG', None), "fClientImpersonating"),(('LONG', None), "fPartitionIDPresent"),(('DWORD', None), "dwDefaultAuthnLvl"),(('GUID', None), "guidPartition"),(('DWORD', None), "dwPRTFlags"),(('DWORD', None), "dwOrigClsctx"),(('DWORD', None), "dwFlags"),(('DWORD', None), "Reserved1"),(('UNSIGNED___INT64', None), "Reserved2"),(('DWORD', None), "Reserved3"),]

    

class ('SPECIALPROPERTIESDATA_ALTERNATE', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "dwSessionId"),(('LONG', None), "fRemoteThisSessionId"),(('LONG', None), "fClientImpersonating"),(('LONG', None), "fPartitionIDPresent"),(('DWORD', None), "dwDefaultAuthnLvl"),(('GUID', None), "guidPartition"),(('DWORD', None), "dwPRTFlags"),(('DWORD', None), "dwOrigClsctx"),(('DWORD', None), "dwFlags"),(('DWORD', None), "Reserved3"),]

    
Method("RemoteActivation",
In(HANDLE_T),
In(PORPCTHIS),
Out(PORPCTHAT),
In(PGUID),
In(PWCHAR_T),
In(PMINTERFACEPOINTER),
In(DWORD),
In(DWORD),
In(DWORD),
In(PIID),
In(UNSIGNED_SHORT),
In(UNSIGNED_SHORT),
Out(POXID),
Out(PPDUALSTRINGARRAY),
Out(PIPID),
Out(PDWORD),
Out(PCOMVERSION),
Out(PHRESULT),
Out(PPMINTERFACEPOINTER),
Out(PHRESULT),
),
class ('VDS_PACK_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "packId"),]

    

class ('VDS_DISK_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "diskId"),]

    

class ('VDS_VOLUME_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "volumeId"),(('VDS_OBJECT_ID', None), "plexId"),(('UNSIGNED_LONG', None), "ulPercentCompleted"),]

    

class ('VDS_PARTITION_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "diskId"),(('ULONGLONG', None), "ullOffset"),]

    

class ('VDS_DRIVE_LETTER_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('WCHAR', None), "wcLetter"),(('VDS_OBJECT_ID', None), "volumeId"),]

    

class ('VDS_FILE_SYSTEM_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "volumeId"),(('DWORD', None), "dwPercentCompleted"),]

    

class ('VDS_MOUNT_POINT_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulEvent"),(('VDS_OBJECT_ID', None), "volumeId"),]

    

class ('VDS_SERVICE_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "ulEvent"),(('VDS_RECOVER_ACTION', None), "action"),]

    

class ('VDS_NOTIFICATION', None)(NdrStructure):
    MEMBERS = [(('VDS_NOTIFICATION_TARGET_TYPE', None), "objectType"),(('U0', None), "u0"),]

    

class ('VDS_ASYNC_OUTPUT', None)(NdrStructure):
    MEMBERS = [(('VDS_ASYNC_OUTPUT_TYPE', None), "type"),(('U0', None), "u0"),]

    

class ('VDS_PARTITION_INFO_MBR', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "partitionType"),(('BOOLEAN', None), "bootIndicator"),(('BOOLEAN', None), "recognizedPartition"),(('DWORD', None), "hiddenSectors"),]

    

class ('VDS_PARTITION_INFO_GPT', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "partitionType"),(('GUID', None), "partitionId"),(('ULONGLONG', None), "attributes"),(('WCHAR', None), "name"),]

    

class ('VDS_STORAGE_IDENTIFIER', None)(NdrStructure):
    MEMBERS = [(('VDS_STORAGE_IDENTIFIER_CODE_SET', None), "m_CodeSet"),(('VDS_STORAGE_IDENTIFIER_TYPE', None), "m_Type"),(('UNSIGNED_LONG', None), "m_cbIdentifier"),(('PBYTE', None), "m_rgbIdentifier"),]

    

class ('VDS_STORAGE_DEVICE_ID_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "m_version"),(('UNSIGNED_LONG', None), "m_cIdentifiers"),(('PVDS_STORAGE_IDENTIFIER', None), "m_rgIdentifiers"),]

    

class ('VDS_INTERCONNECT', None)(NdrStructure):
    MEMBERS = [(('VDS_INTERCONNECT_ADDRESS_TYPE', None), "m_addressType"),(('UNSIGNED_LONG', None), "m_cbPort"),(('PBYTE', None), "m_pbPort"),(('UNSIGNED_LONG', None), "m_cbAddress"),(('PBYTE', None), "m_pbAddress"),]

    

class ('VDS_LUN_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "m_version"),(('BYTE', None), "m_DeviceType"),(('BYTE', None), "m_DeviceTypeModifier"),(('LONG', None), "m_bCommandQueuing"),(('VDS_STORAGE_BUS_TYPE', None), "m_BusType"),(('PCHAR', None), "m_szVendorId"),(('PCHAR', None), "m_szProductId"),(('PCHAR', None), "m_szProductRevision"),(('PCHAR', None), "m_szSerialNumber"),(('GUID', None), "m_diskSignature"),(('VDS_STORAGE_DEVICE_ID_DESCRIPTOR', None), "m_deviceIdDescriptor"),(('UNSIGNED_LONG', None), "m_cInterconnects"),(('PVDS_INTERCONNECT', None), "m_rgInterconnects"),]

    

class ('VDS_FILE_SYSTEM_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_FILE_SYSTEM_TYPE', None), "type"),(('VDS_OBJECT_ID', None), "volumeId"),(('UNSIGNED_LONG', None), "ulFlags"),(('ULONGLONG', None), "ullTotalAllocationUnits"),(('ULONGLONG', None), "ullAvailableAllocationUnits"),(('UNSIGNED_LONG', None), "ulAllocationUnitSize"),(('PWCHAR', None), "pwszLabel"),]

    

class ('VDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "ulFlags"),(('UNSIGNED_SHORT', None), "usRevision"),(('UNSIGNED_LONG', None), "ulDefaultUnitAllocationSize"),(('UNSIGNED_LONG', None), "rgulAllowedUnitAllocationSizes"),(('WCHAR', None), "wszName"),]

    

class ('VDS_DISK_EXTENT', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "diskId"),(('VDS_DISK_EXTENT_TYPE', None), "type"),(('ULONGLONG', None), "ullOffset"),(('ULONGLONG', None), "ullSize"),(('VDS_OBJECT_ID', None), "volumeId"),(('VDS_OBJECT_ID', None), "plexId"),(('UNSIGNED_LONG', None), "memberIdx"),]

    

class ('VDS_DISK_FREE_EXTENT', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "diskId"),(('ULONGLONG', None), "ullOffset"),(('ULONGLONG', None), "ullSize"),]

    

class ('VDS_PARTITION_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_PARTITION_STYLE', None), "PartitionStyle"),(('UNSIGNED_LONG', None), "ulFlags"),(('UNSIGNED_LONG', None), "ulPartitionNumber"),(('ULONGLONG', None), "ullOffset"),(('ULONGLONG', None), "ullSize"),(('U0', None), "u0"),]

    

class ('VDS_INPUT_DISK', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "diskId"),(('ULONGLONG', None), "ullSize"),(('VDS_OBJECT_ID', None), "plexId"),(('UNSIGNED_LONG', None), "memberIdx"),]

    

class ('CREATE_PARTITION_PARAMETERS', None)(NdrStructure):
    MEMBERS = [(('VDS_PARTITION_STYLE', None), "style"),(('U0', None), "u0"),]

    

class ('VIRTUAL_STORAGE_TYPE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "DeviceId"),(('GUID', None), "VendorId"),]

    

class ('VDS_REPARSE_POINT_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "SourceVolumeId"),(('PWCHAR', None), "pwszPath"),]

    

class ('VDS_DRIVE_LETTER_PROP', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wcLetter"),(('VDS_OBJECT_ID', None), "volumeId"),(('UNSIGNED_LONG', None), "ulFlags"),(('LONG', None), "bUsed"),]

    

class ('VDS_FILE_SYSTEM_TYPE_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_FILE_SYSTEM_TYPE', None), "type"),(('WCHAR', None), "wszName"),(('UNSIGNED_LONG', None), "ulFlags"),(('UNSIGNED_LONG', None), "ulCompressionFlags"),(('UNSIGNED_LONG', None), "ulMaxLabelLength"),(('PWCHAR', None), "pwszIllegalLabelCharSet"),]

    

class ('CHANGE_ATTRIBUTES_PARAMETERS', None)(NdrStructure):
    MEMBERS = [(('VDS_PARTITION_STYLE', None), "style"),(('U0', None), "u0"),]

    

class ('CHANGE_PARTITION_TYPE_PARAMETERS', None)(NdrStructure):
    MEMBERS = [(('VDS_PARTITION_STYLE', None), "style"),(('U0', None), "u0"),]

    

class ('VDS_WWN', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "rguchWwn"),]

    

class ('VDS_IPADDRESS', None)(NdrStructure):
    MEMBERS = [(('VDS_IPADDRESS_TYPE', None), "type"),(('UNSIGNED_LONG', None), "ipv4Address"),(('UNSIGNED_CHAR', None), "ipv6Address"),(('UNSIGNED_LONG', None), "ulIpv6FlowInfo"),(('UNSIGNED_LONG', None), "ulIpv6ScopeId"),(('WCHAR', None), "wszTextAddress"),(('UNSIGNED_LONG', None), "ulPort"),]

    

class ('VDS_ISCSI_SHARED_SECRET', None)(NdrStructure):
    MEMBERS = [(('PUNSIGNED_CHAR', None), "pSharedSecret"),(('UNSIGNED_LONG', None), "ulSharedSecretSize"),]

    

class ('VDS_SERVICE_PROP', None)(NdrStructure):
    MEMBERS = [(('PWCHAR', None), "pwszVersion"),(('UNSIGNED_LONG', None), "ulFlags"),]

    

class ('VDS_HBAPORT_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_WWN', None), "wwnNode"),(('VDS_WWN', None), "wwnPort"),(('VDS_HBAPORT_TYPE', None), "type"),(('VDS_HBAPORT_STATUS', None), "status"),(('UNSIGNED_LONG', None), "ulPortSpeed"),(('UNSIGNED_LONG', None), "ulSupportedPortSpeed"),]

    

class ('VDS_ISCSI_INITIATOR_ADAPTER_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('PWCHAR', None), "pwszName"),]

    

class ('VDS_ISCSI_INITIATOR_PORTAL_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_IPADDRESS', None), "address"),(('UNSIGNED_LONG', None), "ulPortIndex"),]

    

class ('VDS_PROVIDER_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('PWCHAR', None), "pwszName"),(('GUID', None), "guidVersionId"),(('PWCHAR', None), "pwszVersion"),(('VDS_PROVIDER_TYPE', None), "type"),(('UNSIGNED_LONG', None), "ulFlags"),(('UNSIGNED_LONG', None), "ulStripeSizeFlags"),(('SHORT', None), "sRebuildPriority"),]

    

class ('VDS_PACK_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('PWCHAR', None), "pwszName"),(('VDS_PACK_STATUS', None), "status"),(('UNSIGNED_LONG', None), "ulFlags"),]

    

class ('VDS_DISK_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_DISK_STATUS', None), "status"),(('VDS_LUN_RESERVE_MODE', None), "ReserveMode"),(('VDS_HEALTH', None), "health"),(('DWORD', None), "dwDeviceType"),(('DWORD', None), "dwMediaType"),(('ULONGLONG', None), "ullSize"),(('UNSIGNED_LONG', None), "ulBytesPerSector"),(('UNSIGNED_LONG', None), "ulSectorsPerTrack"),(('UNSIGNED_LONG', None), "ulTracksPerCylinder"),(('UNSIGNED_LONG', None), "ulFlags"),(('VDS_STORAGE_BUS_TYPE', None), "BusType"),(('VDS_PARTITION_STYLE', None), "PartitionStyle"),(('PWSZDEVICEPATH', None), "u0"),(('PWCHAR', None), "pwszDiskAddress"),(('PWCHAR', None), "pwszName"),(('PWCHAR', None), "pwszFriendlyName"),(('PWCHAR', None), "pwszAdaptorName"),(('PWCHAR', None), "pwszDevicePath"),]

    

class ('VDS_DISK_PROP2', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_DISK_STATUS', None), "status"),(('VDS_LUN_RESERVE_MODE', None), "ReserveMode"),(('VDS_HEALTH', None), "health"),(('DWORD', None), "dwDeviceType"),(('DWORD', None), "dwMediaType"),(('ULONGLONG', None), "ullSize"),(('UNSIGNED_LONG', None), "ulBytesPerSector"),(('UNSIGNED_LONG', None), "ulSectorsPerTrack"),(('UNSIGNED_LONG', None), "ulTracksPerCylinder"),(('UNSIGNED_LONG', None), "ulFlags"),(('VDS_STORAGE_BUS_TYPE', None), "BusType"),(('VDS_PARTITION_STYLE', None), "PartitionStyle"),(('PWSZLOCATIONPATH', None), "u0"),(('PWCHAR', None), "pwszDiskAddress"),(('PWCHAR', None), "pwszName"),(('PWCHAR', None), "pwszFriendlyName"),(('PWCHAR', None), "pwszAdaptorName"),(('PWCHAR', None), "pwszDevicePath"),(('PWCHAR', None), "pwszLocationPath"),]

    

class ('VDS_ADVANCEDDISK_PROP', None)(NdrStructure):
    MEMBERS = [(('LPWSTR', None), "pwszId"),(('LPWSTR', None), "pwszPathname"),(('LPWSTR', None), "pwszLocation"),(('LPWSTR', None), "pwszFriendlyName"),(('LPWSTR', None), "pswzIdentifier"),(('USHORT', None), "usIdentifierFormat"),(('ULONG', None), "ulNumber"),(('LPWSTR', None), "pwszSerialNumber"),(('LPWSTR', None), "pwszFirmwareVersion"),(('LPWSTR', None), "pwszManufacturer"),(('LPWSTR', None), "pwszModel"),(('ULONGLONG', None), "ullTotalSize"),(('ULONGLONG', None), "ullAllocatedSize"),(('ULONG', None), "ulLogicalSectorSize"),(('ULONG', None), "ulPhysicalSectorSize"),(('ULONG', None), "ulPartitionCount"),(('VDS_DISK_STATUS', None), "status"),(('VDS_HEALTH', None), "health"),(('VDS_STORAGE_BUS_TYPE', None), "BusType"),(('VDS_PARTITION_STYLE', None), "PartitionStyle"),(('DWDEVICETYPE', None), "u0"),(('ULONG', None), "ulFlags"),(('DWORD', None), "dwDeviceType"),]

    

class ('VDS_VOLUME_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_VOLUME_TYPE', None), "type"),(('VDS_VOLUME_STATUS', None), "status"),(('VDS_HEALTH', None), "health"),(('VDS_TRANSITION_STATE', None), "TransitionState"),(('ULONGLONG', None), "ullSize"),(('UNSIGNED_LONG', None), "ulFlags"),(('VDS_FILE_SYSTEM_TYPE', None), "RecommendedFileSystemType"),(('PWCHAR', None), "pwszName"),]

    

class ('VDS_VOLUME_PROP2', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_VOLUME_TYPE', None), "type"),(('VDS_VOLUME_STATUS', None), "status"),(('VDS_HEALTH', None), "health"),(('VDS_TRANSITION_STATE', None), "TransitionState"),(('ULONGLONG', None), "ullSize"),(('UNSIGNED_LONG', None), "ulFlags"),(('VDS_FILE_SYSTEM_TYPE', None), "RecommendedFileSystemType"),(('ULONG', None), "cbUniqueId"),(('PWCHAR', None), "pwszName"),(('PBYTE', None), "pUniqueId"),]

    

class ('VDS_VOLUME_PLEX_PROP', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "id"),(('VDS_VOLUME_PLEX_TYPE', None), "type"),(('VDS_VOLUME_PLEX_STATUS', None), "status"),(('VDS_HEALTH', None), "health"),(('VDS_TRANSITION_STATE', None), "TransitionState"),(('ULONGLONG', None), "ullSize"),(('UNSIGNED_LONG', None), "ulStripeSize"),(('UNSIGNED_LONG', None), "ulNumberOfMembers"),]

    

class ('VDS_CREATE_VDISK_PARAMETERS', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "UniqueId"),(('ULONGLONG', None), "MaximumSize"),(('ULONG', None), "BlockSizeInBytes"),(('ULONG', None), "SectorSizeInBytes"),(('LPWSTR', None), "pParentPath"),(('LPWSTR', None), "pSourcePath"),]

    

class ('VDS_VDISK_PROPERTIES', None)(NdrStructure):
    MEMBERS = [(('VDS_OBJECT_ID', None), "Id"),(('VDS_VDISK_STATE', None), "State"),(('VIRTUAL_STORAGE_TYPE', None), "VirtualDeviceType"),(('ULONGLONG', None), "VirtualSize"),(('ULONGLONG', None), "PhysicalSize"),(('LPWSTR', None), "pPath"),(('LPWSTR', None), "pDeviceName"),(('DEPENDENT_DISK_FLAG', None), "DiskFlag"),(('BOOL', None), "bIsChild"),(('LPWSTR', None), "pParentPath"),]

    

class ('PPVIRTUAL_STORAGE_TYPE', None)(NdrStructure):
    MEMBERS = []

    
Method("Next",
In(UNSIGNED_LONG),
Out(PPIUNKNOWN),
Out(PUNSIGNED_LONG),
),Method("Skip",
In(UNSIGNED_LONG),
),Method("Reset",
),Method("Clone",
Out(PPIENUMVDSOBJECT),
),