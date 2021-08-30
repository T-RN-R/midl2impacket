
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
class ('PVARIANT', None)(NdrStructure):
    MEMBERS = []

    

class ('FLAGGED_WORD_BLOB', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "cBytes"),(('UNSIGNED_LONG', None), "clSize"),(('UNSIGNED_SHORT', None), "asData"),]

    

class ('CURRENCY', None)(NdrStructure):
    MEMBERS = [(('__INT64', None), "int64"),]

    

class ('DECIMAL', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wReserved"),(('BYTE', None), "scale"),(('BYTE', None), "sign"),(('ULONG', None), "Hi32"),(('ULONGLONG', None), "Lo64"),]

    

class ('WIREBRECORDSTR', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "fFlags"),(('ULONG', None), "clSize"),(('PMINTERFACEPOINTER', None), "pRecInfo"),(('PBYTE', None), "pRecord"),]

    

class ('PBRECORD', None)(NdrStructure):
    MEMBERS = []

    

class ('_VARUNION', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('LONGLONG', None), llVal),2 : (('LONG', None), lVal),3 : (('BYTE', None), bVal),4 : (('SHORT', None), iVal),5 : (('FLOAT', None), fltVal),6 : (('DOUBLE', None), dblVal),7 : (('VARIANT_BOOL', None), boolVal),8 : (('HRESULT', None), scode),9 : (('CURRENCY', None), cyVal),10 : (('DATE', None), date),11 : (('BSTR', None), bstrVal),12 : (('PIUNKNOWN', None), punkVal),13 : (('PIDISPATCH', None), pdispVal),14 : (('PSAFEARRAY', None), parray),15 : (('BRECORD', None), brecVal),16 : (('PBYTE', None), pbVal),17 : (('PSHORT', None), piVal),18 : (('PLONG', None), plVal),19 : (('PLONGLONG', None), pllVal),20 : (('PFLOAT', None), pfltVal),21 : (('PDOUBLE', None), pdblVal),22 : (('PVARIANT_BOOL', None), pboolVal),23 : (('PHRESULT', None), pscode),24 : (('PCURRENCY', None), pcyVal),25 : (('PDATE', None), pdate),26 : (('PBSTR', None), pbstrVal),27 : (('PPIUNKNOWN', None), ppunkVal),28 : (('PPIDISPATCH', None), ppdispVal),29 : (('PPSAFEARRAY', None), pparray),30 : (('PVARIANT', None), pvarVal),31 : (('CHAR', None), cVal),32 : (('USHORT', None), uiVal),33 : (('ULONG', None), ulVal),34 : (('ULONGLONG', None), ullVal),35 : (('INT', None), intVal),36 : (('UINT', None), uintVal),37 : (('DECIMAL', None), decVal),38 : (('PCHAR', None), pcVal),39 : (('PUSHORT', None), puiVal),40 : (('PULONG', None), pulVal),41 : (('PULONGLONG', None), pullVal),42 : (('PINT', None), pintVal),43 : (('PUINT', None), puintVal),44 : (('PDECIMAL', None), pdecVal),}

    

class ('WIREVARIANTSTR', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "clSize"),(('DWORD', None), "rpcReserved"),(('USHORT', None), "vt"),(('USHORT', None), "wReserved1"),(('USHORT', None), "wReserved2"),(('USHORT', None), "wReserved3"),(('_VARUNION', None), "_varUnion"),]

    

class ('SAFEARRAYBOUND', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "cElements"),(('LONG', None), "lLbound"),]

    

class ('SAFEARR_BSTR', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PBSTR', None), "aBstr"),]

    

class ('SAFEARR_UNKNOWN', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PPIUNKNOWN', None), "apUnknown"),]

    

class ('SAFEARR_DISPATCH', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PPIDISPATCH', None), "apDispatch"),]

    

class ('SAFEARR_VARIANT', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PVARIANT', None), "aVariant"),]

    

class ('SAFEARR_BRECORD', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PBRECORD', None), "aRecord"),]

    

class ('SAFEARR_HAVEIID', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Size"),(('PPIUNKNOWN', None), "apUnknown"),(('IID', None), "iid"),]

    

class ('BYTE_SIZEDARR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "clSize"),(('PBYTE', None), "pData"),]

    

class ('WORD_SIZEDARR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "clSize"),(('PUNSIGNED_SHORT', None), "pData"),]

    

class ('DWORD_SIZEDARR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "clSize"),(('PUNSIGNED_LONG', None), "pData"),]

    

class ('HYPER_SIZEDARR', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "clSize"),(('PHYPER', None), "pData"),]

    

class ('U', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('SAFEARR_BSTR', None), BstrStr),2 : (('SAFEARR_UNKNOWN', None), UnknownStr),3 : (('SAFEARR_DISPATCH', None), DispatchStr),4 : (('SAFEARR_VARIANT', None), VariantStr),5 : (('SAFEARR_BRECORD', None), RecordStr),6 : (('SAFEARR_HAVEIID', None), HaveIidStr),7 : (('BYTE_SIZEDARR', None), ByteStr),8 : (('WORD_SIZEDARR', None), WordStr),9 : (('DWORD_SIZEDARR', None), LongStr),10 : (('HYPER_SIZEDARR', None), HyperStr),}

    

class ('SAFEARRAYUNION', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "sfType"),(('U', None), "u"),]

    

class ('PSAFEARRAY', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "cDims"),(('USHORT', None), "fFeatures"),(('ULONG', None), "cbElements"),(('ULONG', None), "cLocks"),(('SAFEARRAYUNION', None), "uArrayStructs"),(('SAFEARRAYBOUND', None), "rgsabound"),]

    

class ('RECORDINFO', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "libraryGuid"),(('DWORD', None), "verMajor"),(('GUID', None), "recGuid"),(('DWORD', None), "verMinor"),(('DWORD', None), "Lcid"),]

    

class ('DISPPARAMS', None)(NdrStructure):
    MEMBERS = [(('PVARIANT', None), "rgvarg"),(('PDISPID', None), "rgdispidNamedArgs"),(('UINT', None), "cArgs"),(('UINT', None), "cNamedArgs"),]

    

class ('EXCEPINFO', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wCode"),(('WORD', None), "wReserved"),(('BSTR', None), "bstrSource"),(('BSTR', None), "bstrDescription"),(('BSTR', None), "bstrHelpFile"),(('DWORD', None), "dwHelpContext"),(('ULONG_PTR', None), "pvReserved"),(('ULONG_PTR', None), "pfnDeferredFillIn"),(('HRESULT', None), "scode"),]

    

class ('PLPTDESC', None)(NdrStructure):
    MEMBERS = []

    

class ('PLPADESC', None)(NdrStructure):
    MEMBERS = []

    

class ('_TDUNION', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PLPTDESC', None), *lptdesc),2 : (('PLPADESC', None), *lpadesc),3 : (('HREFTYPE', None), hreftype),}

    

class ('TYPEDESC', None)(NdrStructure):
    MEMBERS = [(('_TDUNION', None), "_tdUnion"),(('USHORT', None), "vt"),]

    

class ('ARRAYDESC', None)(NdrStructure):
    MEMBERS = [(('TYPEDESC', None), "tdescElem"),(('USHORT', None), "cDims"),(('SAFEARRAYBOUND', None), "rgbounds"),]

    

class ('PARAMDESCEX', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "cBytes"),(('VARIANT', None), "varDefaultValue"),]

    

class ('PARAMDESC', None)(NdrStructure):
    MEMBERS = [(('PPARAMDESCEX', None), "pparamdescex"),(('USHORT', None), "wParamFlags"),]

    

class ('ELEMDESC', None)(NdrStructure):
    MEMBERS = [(('TYPEDESC', None), "tdesc"),(('PARAMDESC', None), "paramdesc"),]

    

class ('FUNCDESC', None)(NdrStructure):
    MEMBERS = [(('MEMBERID', None), "memid"),(('PSCODE', None), "lReserved1"),(('PELEMDESC', None), "lprgelemdescParam"),(('FUNCKIND', None), "funckind"),(('INVOKEKIND', None), "invkind"),(('CALLCONV', None), "callconv"),(('SHORT', None), "cParams"),(('SHORT', None), "cParamsOpt"),(('SHORT', None), "oVft"),(('SHORT', None), "cReserved2"),(('ELEMDESC', None), "elemdescFunc"),(('WORD', None), "wFuncFlags"),]

    

class ('_VDUNION', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('ULONG', None), oInst),2 : (('PVARIANT', None), lpvarValue),}

    

class ('VARDESC', None)(NdrStructure):
    MEMBERS = [(('MEMBERID', None), "memid"),(('LPOLESTR', None), "lpstrReserved"),(('_VDUNION', None), "_vdUnion"),(('ELEMDESC', None), "elemdescVar"),(('WORD', None), "wVarFlags"),(('VARKIND', None), "varkind"),]

    

class ('TYPEATTR', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "guid"),(('LCID', None), "lcid"),(('DWORD', None), "dwReserved1"),(('DWORD', None), "dwReserved2"),(('DWORD', None), "dwReserved3"),(('LPOLESTR', None), "lpstrReserved4"),(('ULONG', None), "cbSizeInstance"),(('TYPEKIND', None), "typekind"),(('WORD', None), "cFuncs"),(('WORD', None), "cVars"),(('WORD', None), "cImplTypes"),(('WORD', None), "cbSizeVft"),(('WORD', None), "cbAlignment"),(('WORD', None), "wTypeFlags"),(('WORD', None), "wMajorVerNum"),(('WORD', None), "wMinorVerNum"),(('TYPEDESC', None), "tdescAlias"),(('DWORD', None), "dwReserved5"),(('WORD', None), "wReserved6"),]

    

class ('TLIBATTR', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "guid"),(('LCID', None), "lcid"),(('SYSKIND', None), "syskind"),(('UNSIGNED_SHORT', None), "wMajorVerNum"),(('UNSIGNED_SHORT', None), "wMinorVerNum"),(('UNSIGNED_SHORT', None), "wLibFlags"),]

    

class ('CUSTDATAITEM', None)(NdrStructure):
    MEMBERS = [(('GUID', None), "guid"),(('VARIANT', None), "varValue"),]

    

class ('CUSTDATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "cCustData"),(('PCUSTDATAITEM', None), "prgCustData"),]

    
Method("GetTypeInfoCount",
Out(PUINT),
),Method("GetTypeInfo",
In(UINT),
In(LCID),
Out(PPITYPEINFO),
),Method("GetIDsOfNames",
In(REFIID),
In(PLPOLESTR),
In(UINT),
In(LCID),
Out(PDISPID),
),Method("Invoke",
In(DISPID),
In(REFIID),
In(LCID),
In(DWORD),
In(PDISPPARAMS),
Out(PVARIANT),
Out(PEXCEPINFO),
Out(PUINT),
In(UINT),
In(PUINT),
InOut(PVARIANT),
),Method("Item",
In(LONG),
Out(PBSTR),
),Method("Item",
In(LONG),
In(BSTR),
),Method("_NewEnum",
Out(PPIUNKNOWN),
),Method("Count",
Out(PLONG),
),Method("ReadOnly",
Out(PVARIANT_BOOL),
),Method("Add",
In(BSTR),
Out(PLONG),
),Method("Clear",
),Method("Copy",
Out(PPISTRINGCOLLECTION),
),Method("Insert",
In(LONG),
In(BSTR),
),Method("RemoveAt",
In(LONG),
),