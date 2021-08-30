
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
),Method("GetSeqAndTxViaExport",
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PBYTE),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PPBYTE),
),Method("GetSeqAndTxViaTransmitter",
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PPBYTE),
),Method("GetTxViaExport",
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
In(PBYTE),
Out(PUNSIGNED_LONG),
Out(PPBYTE),
),Method("GetTxViaTransmitter",
In(UNSIGNED_LONG),
Out(PUNSIGNED_LONG),
Out(PPBYTE),
),