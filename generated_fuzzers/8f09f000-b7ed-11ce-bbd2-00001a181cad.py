
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
),
class ('IN6_ADDR', None)(NdrStructure):
    MEMBERS = [(('U', None), "u"),]

    

class ('DIM_INFORMATION_CONTAINER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwBufferSize"),(('LPBYTE', None), "pBuffer"),]

    

class ('MPRAPI_OBJECT_HEADER_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('UCHAR', None), "type"),(('USHORT', None), "size"),]

    

class ('PPP_PROJECTION_INFO_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIPv4NegotiationError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),(('DWORD', None), "dwIPv4Options"),(('DWORD', None), "dwIPv4RemoteOptions"),(('ULONG64', None), "IPv4SubInterfaceIndex"),(('DWORD', None), "dwIPv6NegotiationError"),(('UCHAR', None), "bInterfaceIdentifier"),(('UCHAR', None), "bRemoteInterfaceIdentifier"),(('UCHAR', None), "bPrefix"),(('DWORD', None), "dwPrefixLength"),(('ULONG64', None), "IPv6SubInterfaceIndex"),(('DWORD', None), "dwLcpError"),(('DWORD', None), "dwAuthenticationProtocol"),(('DWORD', None), "dwAuthenticationData"),(('DWORD', None), "dwRemoteAuthenticationProtocol"),(('DWORD', None), "dwRemoteAuthenticationData"),(('DWORD', None), "dwLcpTerminateReason"),(('DWORD', None), "dwLcpRemoteTerminateReason"),(('DWORD', None), "dwLcpOptions"),(('DWORD', None), "dwLcpRemoteOptions"),(('DWORD', None), "dwEapTypeId"),(('DWORD', None), "dwRemoteEapTypeId"),(('DWORD', None), "dwCcpError"),(('DWORD', None), "dwCompressionAlgorithm"),(('DWORD', None), "dwCcpOptions"),(('DWORD', None), "dwRemoteCompressionAlgorithm"),(('DWORD', None), "dwCcpRemoteOptions"),]

    

class ('PPP_PROJECTION_INFO_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIPv4NegotiationError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),(('DWORD', None), "dwIPv4Options"),(('DWORD', None), "dwIPv4RemoteOptions"),(('ULONG64', None), "IPv4SubInterfaceIndex"),(('DWORD', None), "dwIPv6NegotiationError"),(('UCHAR', None), "bInterfaceIdentifier"),(('UCHAR', None), "bRemoteInterfaceIdentifier"),(('UCHAR', None), "bPrefix"),(('DWORD', None), "dwPrefixLength"),(('ULONG64', None), "IPv6SubInterfaceIndex"),(('DWORD', None), "dwLcpError"),(('DWORD', None), "dwAuthenticationProtocol"),(('DWORD', None), "dwAuthenticationData"),(('DWORD', None), "dwRemoteAuthenticationProtocol"),(('DWORD', None), "dwRemoteAuthenticationData"),(('DWORD', None), "dwLcpTerminateReason"),(('DWORD', None), "dwLcpRemoteTerminateReason"),(('DWORD', None), "dwLcpOptions"),(('DWORD', None), "dwLcpRemoteOptions"),(('DWORD', None), "dwEapTypeId"),(('DWORD', None), "dwEmbeddedEAPTypeId"),(('DWORD', None), "dwRemoteEapTypeId"),(('DWORD', None), "dwCcpError"),(('DWORD', None), "dwCompressionAlgorithm"),(('DWORD', None), "dwCcpOptions"),(('DWORD', None), "dwRemoteCompressionAlgorithm"),(('DWORD', None), "dwCcpRemoteOptions"),]

    

class ('IKEV2_PROJECTION_INFO_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIPv4NegotiationError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),(('ULONG64', None), "IPv4SubInterfaceIndex"),(('DWORD', None), "dwIPv6NegotiationError"),(('UCHAR', None), "bInterfaceIdentifier"),(('UCHAR', None), "bRemoteInterfaceIdentifier"),(('UCHAR', None), "bPrefix"),(('DWORD', None), "dwPrefixLength"),(('ULONG64', None), "IPv6SubInterfaceIndex"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwAuthenticationProtocol"),(('DWORD', None), "dwEapTypeId"),(('DWORD', None), "dwCompressionAlgorithm"),(('DWORD', None), "dwEncryptionMethod"),]

    

class ('IKEV2_PROJECTION_INFO_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIPv4NegotiationError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),(('ULONG64', None), "IPv4SubInterfaceIndex"),(('DWORD', None), "dwIPv6NegotiationError"),(('UCHAR', None), "bInterfaceIdentifier"),(('UCHAR', None), "bRemoteInterfaceIdentifier"),(('UCHAR', None), "bPrefix"),(('DWORD', None), "dwPrefixLength"),(('ULONG64', None), "IPv6SubInterfaceIndex"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwAuthenticationProtocol"),(('DWORD', None), "dwEapTypeId"),(('DWORD', None), "dwEmbeddedEAPTypeId"),(('DWORD', None), "dwCompressionAlgorithm"),(('DWORD', None), "dwEncryptionMethod"),]

    

class ('PROJECTION_INFO_IDL_1', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "projectionInfoType"),(('ANONYMOUS22', None), "ProjectionInfoObject"),]

    

class ('PPPROJECTION_INFO_IDL_1', None)(NdrStructure):
    MEMBERS = []

    

class ('PROJECTION_INFO_IDL_2', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "projectionInfoType"),(('ANONYMOUS23', None), "ProjectionInfoObject"),]

    

class ('RAS_CONNECTION_EX_1_IDL', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "dwConnectDuration"),(('ROUTER_INTERFACE_TYPE', None), "dwInterfaceType"),(('DWORD', None), "dwConnectionFlags"),(('WCHAR', None), "wszInterfaceName"),(('WCHAR', None), "wszUserName"),(('WCHAR', None), "wszLogonDomain"),(('WCHAR', None), "wszRemoteComputer"),(('GUID', None), "guid"),(('RAS_QUARANTINE_STATE', None), "rasQuarState"),(('FILETIME', None), "probationTime"),(('DWORD', None), "dwBytesXmited"),(('DWORD', None), "dwBytesRcved"),(('DWORD', None), "dwFramesXmited"),(('DWORD', None), "dwFramesRcved"),(('DWORD', None), "dwCrcErr"),(('DWORD', None), "dwTimeoutErr"),(('DWORD', None), "dwAlignmentErr"),(('DWORD', None), "dwHardwareOverrunErr"),(('DWORD', None), "dwFramingErr"),(('DWORD', None), "dwBufferOverrunErr"),(('DWORD', None), "dwCompressionRatioIn"),(('DWORD', None), "dwCompressionRatioOut"),(('DWORD', None), "dwNumSwitchOvers"),(('WCHAR', None), "wszRemoteEndpointAddress"),(('WCHAR', None), "wszLocalEndpointAddress"),(('PROJECTION_INFO_IDL_1', None), "ProjectionInfo"),(('ULONG', None), "hConnection"),(('ULONG', None), "hInterface"),]

    

class ('RAS_CONNECTION_EX_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('ANONYMOUS24', None), "ConnObject"),]

    

class ('PPRAS_CONNECTION_EX_IDL', None)(NdrStructure):
    MEMBERS = []

    

class ('RAS_CONNECTION_4_IDL', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwConnectDuration"),(('ROUTER_INTERFACE_TYPE', None), "dwInterfaceType"),(('DWORD', None), "dwConnectionFlags"),(('WCHAR', None), "wszInterfaceName"),(('WCHAR', None), "wszUserName"),(('WCHAR', None), "wszLogonDomain"),(('WCHAR', None), "wszRemoteComputer"),(('GUID', None), "guid"),(('RAS_QUARANTINE_STATE', None), "rasQuarState"),(('FILETIME', None), "probationTime"),(('FILETIME', None), "connectionStartTime"),(('DWORD', None), "dwBytesXmited"),(('DWORD', None), "dwBytesRcved"),(('DWORD', None), "dwFramesXmited"),(('DWORD', None), "dwFramesRcved"),(('DWORD', None), "dwCrcErr"),(('DWORD', None), "dwTimeoutErr"),(('DWORD', None), "dwAlignmentErr"),(('DWORD', None), "dwHardwareOverrunErr"),(('DWORD', None), "dwFramingErr"),(('DWORD', None), "dwBufferOverrunErr"),(('DWORD', None), "dwCompressionRatioIn"),(('DWORD', None), "dwCompressionRatioOut"),(('DWORD', None), "dwNumSwitchOvers"),(('WCHAR', None), "wszRemoteEndpointAddress"),(('WCHAR', None), "wszLocalEndpointAddress"),(('PROJECTION_INFO_IDL_2', None), "ProjectionInfo"),(('ULONG', None), "hConnection"),(('ULONG', None), "hInterface"),(('DWORD', None), "dwDeviceType"),]

    

class ('CERT_BLOB_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "cbData"),(('PBYTE', None), "pbData"),]

    

class ('CERT_EKU_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('BOOL', None), "IsEKUOID"),(('PWCHAR', None), "pwszEKU"),]

    

class ('IKEV2_TUNNEL_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIdleTimeout"),(('DWORD', None), "dwNetworkBlackoutTime"),(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSizeForRenegotiation"),(('DWORD', None), "dwConfigOptions"),(('DWORD', None), "dwTotalCertificates"),(('PCERT_BLOB_1', None), "certificateNames"),]

    

class ('ROUTER_CUSTOM_IKEV2_POLICY_0', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIntegrityMethod"),(('DWORD', None), "dwEncryptionMethod"),(('DWORD', None), "dwCipherTransformConstant"),(('DWORD', None), "dwAuthTransformConstant"),(('DWORD', None), "dwPfsGroup"),(('DWORD', None), "dwDhGroup"),]

    

class ('ROUTER_IKEV2_IF_CUSTOM_CONFIG_0', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSize"),(('CERT_BLOB_1', None), "certificateName"),(('PROUTER_CUSTOM_IKEV2_POLICY_0', None), "customPolicy"),]

    

class ('ROUTER_IKEV2_IF_CUSTOM_CONFIG_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSize"),(('CERT_BLOB_1', None), "certificateName"),(('PROUTER_CUSTOM_IKEV2_POLICY_0', None), "customPolicy"),(('CERT_BLOB_1', None), "certificateHash"),]

    

class ('MPR_IF_CUSTOMINFOEX_0', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "dwFlags"),(('ROUTER_IKEV2_IF_CUSTOM_CONFIG_0', None), "customIkev2Config"),]

    

class ('MPR_IF_CUSTOMINFOEX_1', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "dwFlags"),(('ROUTER_IKEV2_IF_CUSTOM_CONFIG_1', None), "customIkev2Config"),]

    

class ('MPR_IF_CUSTOMINFOEX_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('ANONYMOUS25', None), "IfCustomConfigObject"),]

    

class ('IKEV2_TUNNEL_CONFIG_PARAMS_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIdleTimeout"),(('DWORD', None), "dwNetworkBlackoutTime"),(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSizeForRenegotiation"),(('DWORD', None), "dwConfigOptions"),(('DWORD', None), "dwTotalCertificates"),(('PCERT_BLOB_1', None), "certificateNames"),(('CERT_BLOB_1', None), "machineCertificateName"),(('DWORD', None), "dwEncryptionType"),(('PROUTER_CUSTOM_IKEV2_POLICY_0', None), "customPolicy"),]

    

class ('IKEV2_TUNNEL_CONFIG_PARAMS_3', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIdleTimeout"),(('DWORD', None), "dwNetworkBlackoutTime"),(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSizeForRenegotiation"),(('DWORD', None), "dwConfigOptions"),(('DWORD', None), "dwTotalCertificates"),(('PCERT_BLOB_1', None), "certificateNames"),(('CERT_BLOB_1', None), "machineCertificateName"),(('DWORD', None), "dwEncryptionType"),(('PROUTER_CUSTOM_IKEV2_POLICY_0', None), "customPolicy"),(('DWORD', None), "dwTotalEkus"),(('PCERT_EKU_1', None), "certificateEKUs"),(('CERT_BLOB_1', None), "machineCertificateHash"),]

    

class ('L2TP_TUNNEL_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIdleTimeout"),(('DWORD', None), "dwEncryptionType"),(('DWORD', None), "dwSaLifeTime"),(('DWORD', None), "dwSaDataSizeForRenegotiation"),(('PROUTER_CUSTOM_L2TP_POLICY_0', None), "customPolicy"),]

    

class ('IKEV2_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),(('DWORD', None), "dwTunnelConfigParamFlags"),(('IKEV2_TUNNEL_CONFIG_PARAMS_1', None), "TunnelConfigParams"),]

    

class ('IKEV2_CONFIG_PARAMS_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),(('DWORD', None), "dwTunnelConfigParamFlags"),(('IKEV2_TUNNEL_CONFIG_PARAMS_2', None), "TunnelConfigParams"),]

    

class ('IKEV2_CONFIG_PARAMS_3', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),(('DWORD', None), "dwTunnelConfigParamFlags"),(('IKEV2_TUNNEL_CONFIG_PARAMS_3', None), "TunnelConfigParams"),]

    

class ('PPTP_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),]

    

class ('L2TP_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),]

    

class ('L2TP_CONFIG_PARAMS_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),(('DWORD', None), "dwTunnelConfigParamFlags"),(('L2TP_TUNNEL_CONFIG_PARAMS_1', None), "TunnelConfigParams"),]

    

class ('SSTP_CERT_INFO_1', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "isDefault"),(('CERT_BLOB_1', None), "certBlob"),]

    

class ('SSTP_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPorts"),(('DWORD', None), "dwPortFlags"),(('BOOL', None), "isUseHttps"),(('DWORD', None), "certAlgorithm"),(('SSTP_CERT_INFO_1', None), "sstpCertDetails"),]

    

class ('MPRAPI_TUNNEL_CONFIG_PARAMS_1', None)(NdrStructure):
    MEMBERS = [(('IKEV2_CONFIG_PARAMS_1', None), "IkeConfigParams"),(('PPTP_CONFIG_PARAMS_1', None), "PptpConfigParams"),(('L2TP_CONFIG_PARAMS_1', None), "L2tpConfigParams"),(('SSTP_CONFIG_PARAMS_1', None), "SstpConfigParams"),]

    

class ('MPRAPI_TUNNEL_CONFIG_PARAMS_2', None)(NdrStructure):
    MEMBERS = [(('IKEV2_CONFIG_PARAMS_2', None), "IkeConfigParams"),(('PPTP_CONFIG_PARAMS_1', None), "PptpConfigParams"),(('L2TP_CONFIG_PARAMS_1', None), "L2tpConfigParams"),(('SSTP_CONFIG_PARAMS_1', None), "SstpConfigParams"),]

    

class ('MPRAPI_TUNNEL_CONFIG_PARAMS_3', None)(NdrStructure):
    MEMBERS = [(('IKEV2_CONFIG_PARAMS_3', None), "IkeConfigParams"),(('PPTP_CONFIG_PARAMS_1', None), "PptpConfigParams"),(('L2TP_CONFIG_PARAMS_2', None), "L2tpConfigParams"),(('SSTP_CONFIG_PARAMS_1', None), "SstpConfigParams"),]

    

class ('MPR_SERVER_EX_1', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('BOOL', None), "fLanOnlyMode"),(('DWORD', None), "dwUpTime"),(('DWORD', None), "dwTotalPorts"),(('DWORD', None), "dwPortsInUse"),(('DWORD', None), "Reserved"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_1', None), "ConfigParams"),]

    

class ('MPR_SERVER_EX_2', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('BOOL', None), "fLanOnlyMode"),(('DWORD', None), "dwUpTime"),(('DWORD', None), "dwTotalPorts"),(('DWORD', None), "dwPortsInUse"),(('DWORD', None), "Reserved"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_2', None), "ConfigParams"),]

    

class ('MPR_SERVER_EX_3', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('BOOL', None), "fLanOnlyMode"),(('DWORD', None), "dwUpTime"),(('DWORD', None), "dwTotalPorts"),(('DWORD', None), "dwPortsInUse"),(('DWORD', None), "Reserved"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_3', None), "ConfigParams"),]

    

class ('MPR_SERVER_EX_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('ANONYMOUS26', None), "ServerConfigObject"),]

    

class ('PPMPR_SERVER_EX_IDL', None)(NdrStructure):
    MEMBERS = []

    

class ('MPR_SERVER_SET_CONFIG_EX_1', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "setConfigForProtocols"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_1', None), "ConfigParams"),]

    

class ('MPR_SERVER_SET_CONFIG_EX_2', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "setConfigForProtocols"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_2', None), "ConfigParams"),]

    

class ('MPR_SERVER_SET_CONFIG_EX_3', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "setConfigForProtocols"),(('MPRAPI_TUNNEL_CONFIG_PARAMS_3', None), "ConfigParams"),]

    

class ('MPR_SERVER_SET_CONFIG_EX_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('ANONYMOUS27', None), "ServerSetConfigObject"),]

    

class ('PPMPR_SERVER_SET_CONFIG_EX_IDL', None)(NdrStructure):
    MEMBERS = []

    

class ('RAS_UPDATE_CONNECTION_1_IDL', None)(NdrStructure):
    MEMBERS = [(('MPRAPI_OBJECT_HEADER_IDL', None), "Header"),(('DWORD', None), "dwIfIndex"),(('WCHAR', None), "wszRemoteEndpointAddress"),]

    

class ('PPRAS_UPDATE_CONNECTION_1_IDL', None)(NdrStructure):
    MEMBERS = []

    

class ('RAS_UPDATE_CONNECTION_IDL', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "revision"),(('ANONYMOUS28', None), "UpdateConnection"),]

    

class ('PPRAS_UPDATE_CONNECTION_IDL', None)(NdrStructure):
    MEMBERS = []

    

class ('DIM_INTERFACE_CONTAINER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "fGetInterfaceInfo"),(('DWORD', None), "dwInterfaceInfoSize"),(('LPBYTE', None), "pInterfaceInfo"),(('DWORD', None), "fGetGlobalInfo"),(('DWORD', None), "dwGlobalInfoSize"),(('LPBYTE', None), "pGlobalInfo"),]

    

class ('RTR_TOC_ENTRY', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InfoType"),(('ULONG', None), "InfoSize"),(('ULONG', None), "Count"),(('ULONG', None), "Offset"),]

    

class ('RTR_INFO_BLOCK_HEADER', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Version"),(('ULONG', None), "Size"),(('ULONG', None), "TocEntriesCount"),(('RTR_TOC_ENTRY', None), "TocEntry"),]

    

class ('FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSrcAddr"),(('DWORD', None), "dwSrcMask"),(('DWORD', None), "dwDstAddr"),(('DWORD', None), "dwDstMask"),(('DWORD', None), "dwProtocol"),(('DWORD', None), "fLateBound"),(('WORD', None), "wSrcPort"),(('WORD', None), "wDstPort"),]

    

class ('FILTER_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('DWORD', None), "dwNumFilters"),(('FORWARD_ACTION', None), "faDefaultAction"),(('FILTER_INFO', None), "fiFilter"),]

    

class ('FILTER_INFO_V6', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "ipv6SrcAddr"),(('DWORD', None), "dwSrcPrefixLength"),(('BYTE', None), "ipv6DstAddr"),(('DWORD', None), "dwDstPrefixLength"),(('DWORD', None), "dwProtocol"),(('DWORD', None), "fLateBound"),(('WORD', None), "wSrcPort"),(('WORD', None), "wDstPort"),]

    

class ('FILTER_DESCRIPTOR_V6', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('DWORD', None), "dwNumFilters"),(('FORWARD_ACTION', None), "faDefaultAction"),(('FILTER_INFO_V6', None), "fiFilter"),]

    

class ('GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "bFilteringOn"),(('DWORD', None), "dwLoggingLevel"),]

    

class ('INTERFACE_ROUTE_INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "dwRtInfoIfIndex"),(('DWORD', None), "dwRtInfoType"),(('DWORD', None), "dwRtInfoProto"),(('DWORD', None), "dwRtInfoPreference"),(('DWORD', None), "dwRtInfoViewSet"),(('BOOL', None), "bV4"),]

    

class ('PROTOCOL_METRIC', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwProtocolId"),(('DWORD', None), "dwMetric"),]

    

class ('PRIORITY_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumProtocols"),(('PROTOCOL_METRIC', None), "ppmProtocolMetric"),]

    

class ('PROTOCOL_METRIC_EX', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwProtocolId"),(('DWORD', None), "dwSubProtocolId"),(('DWORD', None), "dwMetric"),]

    

class ('PRIORITY_INFO_EX', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumProtocols"),(('PROTOCOL_METRIC_EX', None), "ppmProtocolMetric"),]

    

class ('RTR_DISC_INFO', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wMaxAdvtInterval"),(('WORD', None), "wMinAdvtInterval"),(('WORD', None), "wAdvtLifetime"),(('BOOL', None), "bAdvertise"),(('LONG', None), "lPrefLevel"),]

    

class ('MCAST_HBEAT_INFO', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "pwszGroup"),(('BOOL', None), "bActive"),(('ULONG', None), "ulDeadInterval"),(('BYTE', None), "byProtocol"),(('WORD', None), "wPort"),]

    

class ('MIB_MCAST_LIMIT_ROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwTtl"),(('DWORD', None), "dwRateLimit"),]

    

class ('IPINIP_CONFIG_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwRemoteAddress"),(('DWORD', None), "dwLocalAddress"),(('BYTE', None), "byTtl"),]

    

class ('INTERFACE_STATUS_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAdminStatus"),]

    

class ('DIM_MIB_ENTRY_CONTAINER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwMibInEntrySize"),(('LPBYTE', None), "pMibInEntry"),(('DWORD', None), "dwMibOutEntrySize"),(('LPBYTE', None), "pMibOutEntry"),]

    

class ('MIB_IPFORWARDROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwForwardDest"),(('DWORD', None), "dwForwardMask"),(('DWORD', None), "dwForwardPolicy"),(('DWORD', None), "dwForwardNextHop"),(('DWORD', None), "dwForwardIfIndex"),(('U0', None), "u0"),(('U1', None), "u1"),(('DWORD', None), "dwForwardAge"),(('DWORD', None), "dwForwardNextHopAS"),(('DWORD', None), "dwForwardMetric1"),(('DWORD', None), "dwForwardMetric2"),(('DWORD', None), "dwForwardMetric3"),(('DWORD', None), "dwForwardMetric4"),(('DWORD', None), "dwForwardMetric5"),]

    

class ('MIB_IPDESTROW', None)(NdrStructure):
    MEMBERS = [(('MIB_IPFORWARDROW', None), "ForwardRow"),(('DWORD', None), "dwForwardPreference"),(('DWORD', None), "dwForwardViewSet"),]

    

class ('MIB_IPDESTTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPDESTROW', None), "table"),]

    

class ('MIB_ROUTESTATE', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "bRoutesSetToStack"),]

    

class ('MIB_BEST_IF', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwDestAddr"),(('DWORD', None), "dwIfIndex"),]

    

class ('MIB_BOUNDARYROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwGroupAddress"),(('DWORD', None), "dwGroupMask"),]

    

class ('MIBICMPSTATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwMsgs"),(('DWORD', None), "dwErrors"),(('DWORD', None), "dwDestUnreachs"),(('DWORD', None), "dwTimeExcds"),(('DWORD', None), "dwParmProbs"),(('DWORD', None), "dwSrcQuenchs"),(('DWORD', None), "dwRedirects"),(('DWORD', None), "dwEchos"),(('DWORD', None), "dwEchoReps"),(('DWORD', None), "dwTimestamps"),(('DWORD', None), "dwTimestampReps"),(('DWORD', None), "dwAddrMasks"),(('DWORD', None), "dwAddrMaskReps"),]

    

class ('MIBICMPINFO', None)(NdrStructure):
    MEMBERS = [(('MIBICMPSTATS', None), "icmpInStats"),(('MIBICMPSTATS', None), "icmpOutStats"),]

    

class ('MIB_ICMP', None)(NdrStructure):
    MEMBERS = [(('MIBICMPINFO', None), "stats"),]

    

class ('MIB_IFNUMBER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwValue"),]

    

class ('MIB_IFROW', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wszName"),(('DWORD', None), "dwIndex"),(('DWORD', None), "dwType"),(('DWORD', None), "dwMtu"),(('DWORD', None), "dwSpeed"),(('DWORD', None), "dwPhysAddrLen"),(('BYTE', None), "bPhysAddr"),(('DWORD', None), "dwAdminStatus"),(('DWORD', None), "dwOperStatus"),(('DWORD', None), "dwLastChange"),(('DWORD', None), "dwInOctets"),(('DWORD', None), "dwInUcastPkts"),(('DWORD', None), "dwInNUcastPkts"),(('DWORD', None), "dwInDiscards"),(('DWORD', None), "dwInErrors"),(('DWORD', None), "dwInUnknownProtos"),(('DWORD', None), "dwOutOctets"),(('DWORD', None), "dwOutUcastPkts"),(('DWORD', None), "dwOutNUcastPkts"),(('DWORD', None), "dwOutDiscards"),(('DWORD', None), "dwOutErrors"),(('DWORD', None), "dwOutQLen"),(('DWORD', None), "dwDescrLen"),(('BYTE', None), "bDescr"),]

    

class ('MIB_IFSTATUS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIfIndex"),(('DWORD', None), "dwAdminStatus"),(('DWORD', None), "dwOperationalStatus"),(('BOOL', None), "bMHbeatActive"),(('BOOL', None), "bMHbeatAlive"),]

    

class ('MIB_IFTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IFROW', None), "table"),]

    

class ('MIB_IPADDRROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAddr"),(('DWORD', None), "dwIndex"),(('DWORD', None), "dwMask"),(('DWORD', None), "dwBCastAddr"),(('DWORD', None), "dwReasmSize"),(('UNSIGNED_SHORT', None), "unused1"),(('UNSIGNED_SHORT', None), "wType"),]

    

class ('MIB_IPADDRTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPADDRROW', None), "table"),]

    

class ('MIB_IPFORWARDNUMBER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwValue"),]

    

class ('MIB_IPFORWARDTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPFORWARDROW', None), "table"),(('BYTE', None), "reserved"),]

    

class ('MIB_IPMCAST_BOUNDARY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIfIndex"),(('DWORD', None), "dwGroupAddress"),(('DWORD', None), "dwGroupMask"),(('DWORD', None), "dwStatus"),]

    

class ('MIB_IPMCAST_BOUNDARY_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPMCAST_BOUNDARY', None), "table"),]

    

class ('MIB_IPMCAST_GLOBAL', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwEnable"),]

    

class ('MIB_IPMCAST_IF_ENTRY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIfIndex"),(('DWORD', None), "dwTtl"),(('DWORD', None), "dwProtocol"),(('DWORD', None), "dwRateLimit"),(('ULONG', None), "ulInMcastOctets"),(('ULONG', None), "ulOutMcastOctets"),]

    

class ('MIB_IPMCAST_IF_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPMCAST_IF_ENTRY', None), "table"),]

    

class ('MIB_IPMCAST_OIF', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwOutIfIndex"),(('DWORD', None), "dwNextHopAddr"),(('PVOID', None), "pvReserved"),(('DWORD', None), "dwReserved"),]

    

class ('MIB_IPMCAST_MFE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwGroup"),(('DWORD', None), "dwSource"),(('DWORD', None), "dwSrcMask"),(('DWORD', None), "dwUpStrmNgbr"),(('DWORD', None), "dwInIfIndex"),(('DWORD', None), "dwInIfProtocol"),(('DWORD', None), "dwRouteProtocol"),(('DWORD', None), "dwRouteNetwork"),(('DWORD', None), "dwRouteMask"),(('ULONG', None), "ulUpTime"),(('ULONG', None), "ulExpiryTime"),(('ULONG', None), "ulTimeOut"),(('ULONG', None), "ulNumOutIf"),(('DWORD', None), "fFlags"),(('DWORD', None), "dwReserved"),(('MIB_IPMCAST_OIF', None), "rgmioOutInfo"),]

    

class ('MIB_IPMCAST_OIF_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwOutIfIndex"),(('DWORD', None), "dwNextHopAddr"),(('PVOID', None), "pvDialContext"),(('ULONG', None), "ulTtlTooLow"),(('ULONG', None), "ulFragNeeded"),(('ULONG', None), "ulOutPackets"),(('ULONG', None), "ulOutDiscards"),]

    

class ('MIB_IPMCAST_MFE_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwGroup"),(('DWORD', None), "dwSource"),(('DWORD', None), "dwSrcMask"),(('DWORD', None), "dwUpStrmNgbr"),(('DWORD', None), "dwInIfIndex"),(('DWORD', None), "dwInIfProtocol"),(('DWORD', None), "dwRouteProtocol"),(('DWORD', None), "dwRouteNetwork"),(('DWORD', None), "dwRouteMask"),(('ULONG', None), "ulUpTime"),(('ULONG', None), "ulExpiryTime"),(('ULONG', None), "ulNumOutIf"),(('ULONG', None), "ulInPkts"),(('ULONG', None), "ulInOctets"),(('ULONG', None), "ulPktsDifferentIf"),(('ULONG', None), "ulQueueOverflow"),(('MIB_IPMCAST_OIF_STATS', None), "rgmiosOutStats"),]

    

class ('MIB_IPMCAST_SCOPE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwGroupAddress"),(('DWORD', None), "dwGroupMask"),(('WCHAR', None), "snNameBuffer"),(('DWORD', None), "dwStatus"),(('BYTE', None), "reserved"),]

    

class ('MIB_IPNETROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIndex"),(('DWORD', None), "dwPhysAddrLen"),(('BYTE', None), "bPhysAddr"),(('DWORD', None), "dwAddr"),(('DWORD', None), "dwType"),]

    

class ('MIB_IPNETTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPNETROW', None), "table"),(('BYTE', None), "reserved"),]

    

class ('MIB_IPSTATS', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "dwDefaultTTL"),(('DWORD', None), "dwInReceives"),(('DWORD', None), "dwInHdrErrors"),(('DWORD', None), "dwInAddrErrors"),(('DWORD', None), "dwForwDatagrams"),(('DWORD', None), "dwInUnknownProtos"),(('DWORD', None), "dwInDiscards"),(('DWORD', None), "dwInDelivers"),(('DWORD', None), "dwOutRequests"),(('DWORD', None), "dwRoutingDiscards"),(('DWORD', None), "dwOutDiscards"),(('DWORD', None), "dwOutNoRoutes"),(('DWORD', None), "dwReasmTimeout"),(('DWORD', None), "dwReasmReqds"),(('DWORD', None), "dwReasmOks"),(('DWORD', None), "dwReasmFails"),(('DWORD', None), "dwFragOks"),(('DWORD', None), "dwFragFails"),(('DWORD', None), "dwFragCreates"),(('DWORD', None), "dwNumIf"),(('DWORD', None), "dwNumAddr"),(('DWORD', None), "dwNumRoutes"),]

    

class ('MIB_MFE_STATS_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPMCAST_MFE_STATS', None), "table"),]

    

class ('MIB_MFE_TABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_IPMCAST_MFE', None), "table"),]

    

class ('MIB_OPAQUE_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwId"),(('U0', None), "u0"),]

    

class ('MIB_OPAQUE_QUERY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVarId"),(('DWORD', None), "rgdwVarIndex"),]

    

class ('MIB_PROXYARP', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAddress"),(('DWORD', None), "dwMask"),(('DWORD', None), "dwIfIndex"),]

    

class ('MIB_TCPROW', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "dwLocalAddr"),(('DWORD', None), "dwLocalPort"),(('DWORD', None), "dwRemoteAddr"),(('DWORD', None), "dwRemotePort"),]

    

class ('MIB_TCPSTATS', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "dwRtoMin"),(('DWORD', None), "dwRtoMax"),(('DWORD', None), "dwMaxConn"),(('DWORD', None), "dwActiveOpens"),(('DWORD', None), "dwPassiveOpens"),(('DWORD', None), "dwAttemptFails"),(('DWORD', None), "dwEstabResets"),(('DWORD', None), "dwCurrEstab"),(('DWORD', None), "dwInSegs"),(('DWORD', None), "dwOutSegs"),(('DWORD', None), "dwRetransSegs"),(('DWORD', None), "dwInErrs"),(('DWORD', None), "dwOutRsts"),(('DWORD', None), "dwNumConns"),]

    

class ('MIB_TCPTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_TCPROW', None), "table"),(('BYTE', None), "reserved"),]

    

class ('MIB_UDPROW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLocalAddr"),(('DWORD', None), "dwLocalPort"),]

    

class ('MIB_UDPSTATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwInDatagrams"),(('DWORD', None), "dwNoPorts"),(('DWORD', None), "dwInErrors"),(('DWORD', None), "dwOutDatagrams"),(('DWORD', None), "dwNumAddrs"),]

    

class ('MIB_UDPTABLE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumEntries"),(('MIB_UDPROW', None), "table"),(('BYTE', None), "reserved"),]

    

class ('MPR_SERVER_0', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "fLanOnlyMode"),(('DWORD', None), "dwUpTime"),(('DWORD', None), "dwTotalPorts"),(('DWORD', None), "dwPortsInUse"),]

    

class ('MPR_SERVER_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPptpPorts"),(('DWORD', None), "dwPptpPortFlags"),(('DWORD', None), "dwNumL2tpPorts"),(('DWORD', None), "dwL2tpPortFlags"),]

    

class ('MPR_SERVER_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwNumPptpPorts"),(('DWORD', None), "dwPptpPortFlags"),(('DWORD', None), "dwNumL2tpPorts"),(('DWORD', None), "dwL2tpPortFlags"),(('DWORD', None), "dwNumSstpPorts"),(('DWORD', None), "dwSstpPortFlags"),]

    

class ('PPP_NBFCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('WCHAR', None), "wszWksta"),]

    

class ('PPP_IPCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),]

    

class ('PPP_IPCP_INFO2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('WCHAR', None), "wszAddress"),(('WCHAR', None), "wszRemoteAddress"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwRemoteOptons"),]

    

class ('PPP_IPXCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('WCHAR', None), "wszAddress"),]

    

class ('PPP_IPV6_CP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('DWORD', None), "dwSize"),(('DWORD', None), "dwError"),(('BYTE', None), "bInterfaceIdentifier"),(('BYTE', None), "bRemoteInterfaceIdentifier"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwRemoteOptions"),(('BYTE', None), "bPrefix"),(('DWORD', None), "dwPrefixLength"),]

    

class ('PPP_ATCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('WCHAR', None), "wszAddress"),]

    

class ('PPP_CCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('DWORD', None), "dwCompressionAlgorithm"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwRemoteCompressionAlgorithm"),(('DWORD', None), "dwRemoteOptions"),]

    

class ('PPP_LCP_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwError"),(('DWORD', None), "dwAuthenticationProtocol"),(('DWORD', None), "dwAuthenticationData"),(('DWORD', None), "dwRemoteAuthenticationProtocol"),(('DWORD', None), "dwRemoteAuthenticationData"),(('DWORD', None), "dwTerminateReason"),(('DWORD', None), "dwRemoteTerminateReason"),(('DWORD', None), "dwOptions"),(('DWORD', None), "dwRemoteOptions"),(('DWORD', None), "dwEapTypeId"),(('DWORD', None), "dwRemoteEapTypeId"),]

    

class ('PPP_INFO', None)(NdrStructure):
    MEMBERS = [(('PPP_NBFCP_INFO', None), "nbf"),(('PPP_IPCP_INFO', None), "ip"),(('PPP_IPXCP_INFO', None), "ipx"),(('PPP_ATCP_INFO', None), "at"),]

    

class ('PPP_INFO_2', None)(NdrStructure):
    MEMBERS = [(('PPP_NBFCP_INFO', None), "nbf"),(('PPP_IPCP_INFO2', None), "ip"),(('PPP_IPXCP_INFO', None), "ipx"),(('PPP_ATCP_INFO', None), "at"),(('PPP_CCP_INFO', None), "ccp"),(('PPP_LCP_INFO', None), "lcp"),]

    

class ('PPP_INFO_3', None)(NdrStructure):
    MEMBERS = [(('PPP_NBFCP_INFO', None), "nbf"),(('PPP_IPCP_INFO2', None), "ip"),(('PPP_IPV6_CP_INFO', None), "ipv6"),(('PPP_CCP_INFO', None), "ccp"),(('PPP_LCP_INFO', None), "lcp"),]

    

class ('RASI_PORT_0', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwPort"),(('DWORD', None), "dwConnection"),(('RAS_PORT_CONDITION', None), "dwPortCondition"),(('DWORD', None), "dwTotalNumberOfCalls"),(('DWORD', None), "dwConnectDuration"),(('WCHAR', None), "wszPortName"),(('WCHAR', None), "wszMediaName"),(('WCHAR', None), "wszDeviceName"),(('WCHAR', None), "wszDeviceType"),]

    

class ('RASI_PORT_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwPort"),(('DWORD', None), "dwConnection"),(('RAS_HARDWARE_CONDITION', None), "dwHardwareCondition"),(('DWORD', None), "dwLineSpeed"),(('DWORD', None), "dwBytesXmited"),(('DWORD', None), "dwBytesRcved"),(('DWORD', None), "dwFramesXmited"),(('DWORD', None), "dwFramesRcved"),(('DWORD', None), "dwCrcErr"),(('DWORD', None), "dwTimeoutErr"),(('DWORD', None), "dwAlignmentErr"),(('DWORD', None), "dwHardwareOverrunErr"),(('DWORD', None), "dwFramingErr"),(('DWORD', None), "dwBufferOverrunErr"),(('DWORD', None), "dwCompressionRatioIn"),(('DWORD', None), "dwCompressionRatioOut"),]

    

class ('RASI_CONNECTION_0', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwConnection"),(('DWORD', None), "dwInterface"),(('DWORD', None), "dwConnectDuration"),(('ROUTER_INTERFACE_TYPE', None), "dwInterfaceType"),(('DWORD', None), "dwConnectionFlags"),(('WCHAR', None), "wszInterfaceName"),(('WCHAR', None), "wszUserName"),(('WCHAR', None), "wszLogonDomain"),(('WCHAR', None), "wszRemoteComputer"),]

    

class ('RASI_CONNECTION_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwConnection"),(('DWORD', None), "dwInterface"),(('PPP_INFO', None), "PppInfo"),(('DWORD', None), "dwBytesXmited"),(('DWORD', None), "dwBytesRcved"),(('DWORD', None), "dwFramesXmited"),(('DWORD', None), "dwFramesRcved"),(('DWORD', None), "dwCrcErr"),(('DWORD', None), "dwTimeoutErr"),(('DWORD', None), "dwAlignmentErr"),(('DWORD', None), "dwHardwareOverrunErr"),(('DWORD', None), "dwFramingErr"),(('DWORD', None), "dwBufferOverrunErr"),(('DWORD', None), "dwCompressionRatioIn"),(('DWORD', None), "dwCompressionRatioOut"),]

    

class ('RASI_CONNECTION_2', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwConnection"),(('WCHAR', None), "wszUserName"),(('ROUTER_INTERFACE_TYPE', None), "dwInterfaceType"),(('GUID', None), "guid"),(('PPP_INFO_2', None), "PppInfo2"),]

    

class ('RASI_CONNECTION_3', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('DWORD', None), "dwSize"),(('DWORD', None), "dwConnection"),(('WCHAR', None), "wszUserName"),(('ROUTER_INTERFACE_TYPE', None), "dwInterfaceType"),(('GUID', None), "guid"),(('PPP_INFO_3', None), "PppInfo3"),(('RAS_QUARANTINE_STATE', None), "rasQuarState"),(('FILETIME', None), "timer"),]

    

class ('MPRI_INTERFACE_0', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wszInterfaceName"),(('DWORD', None), "dwInterface"),(('BOOL', None), "fEnabled"),(('ROUTER_INTERFACE_TYPE', None), "dwIfType"),(('ROUTER_CONNECTION_STATE', None), "dwConnectionState"),(('DWORD', None), "fUnReachabilityReasons"),(('DWORD', None), "dwLastError"),]

    

class ('MPRI_INTERFACE_1', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wszInterfaceName"),(('DWORD', None), "dwInterface"),(('BOOL', None), "fEnabled"),(('ROUTER_INTERFACE_TYPE', None), "dwIfType"),(('ROUTER_CONNECTION_STATE', None), "dwConnectionState"),(('DWORD', None), "fUnReachabilityReasons"),(('DWORD', None), "dwLastError"),(('LPWSTR', None), "lpwsDialoutHoursRestriction"),]

    

class ('MPRI_INTERFACE_2', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wszInterfaceName"),(('DWORD', None), "dwInterface"),(('BOOL', None), "fEnabled"),(('ROUTER_INTERFACE_TYPE', None), "dwIfType"),(('ROUTER_CONNECTION_STATE', None), "dwConnectionState"),(('DWORD', None), "fUnReachabilityReasons"),(('DWORD', None), "dwLastError"),(('DWORD', None), "dwfOptions"),(('WCHAR', None), "szLocalPhoneNumber"),(('PWCHAR', None), "szAlternates"),(('DWORD', None), "ipaddr"),(('DWORD', None), "ipaddrDns"),(('DWORD', None), "ipaddrDnsAlt"),(('DWORD', None), "ipaddrWins"),(('DWORD', None), "ipaddrWinsAlt"),(('DWORD', None), "dwfNetProtocols"),(('WCHAR', None), "szDeviceType"),(('WCHAR', None), "szDeviceName"),(('WCHAR', None), "szX25PadType"),(('WCHAR', None), "szX25Address"),(('WCHAR', None), "szX25Facilities"),(('WCHAR', None), "szX25UserData"),(('DWORD', None), "dwChannels"),(('DWORD', None), "dwSubEntries"),(('DWORD', None), "dwDialMode"),(('DWORD', None), "dwDialExtraPercent"),(('DWORD', None), "dwDialExtraSampleSeconds"),(('DWORD', None), "dwHangUpExtraPercent"),(('DWORD', None), "dwHangUpExtraSampleSeconds"),(('DWORD', None), "dwIdleDisconnectSeconds"),(('DWORD', None), "dwType"),(('DWORD', None), "dwEncryptionType"),(('DWORD', None), "dwCustomAuthKey"),(('DWORD', None), "dwCustomAuthDataSize"),(('LPBYTE', None), "lpbCustomAuthData"),(('GUID', None), "guidId"),(('DWORD', None), "dwVpnStrategy"),]

    

class ('MPRI_INTERFACE_3', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "wszInterfaceName"),(('DWORD', None), "dwInterface"),(('BOOL', None), "fEnabled"),(('ROUTER_INTERFACE_TYPE', None), "dwIfType"),(('ROUTER_CONNECTION_STATE', None), "dwConnectionState"),(('DWORD', None), "fUnReachabilityReasons"),(('DWORD', None), "dwLastError"),(('DWORD', None), "dwfOptions"),(('WCHAR', None), "szLocalPhoneNumber"),(('PWCHAR', None), "szAlternates"),(('DWORD', None), "ipaddr"),(('DWORD', None), "ipaddrDns"),(('DWORD', None), "ipaddrDnsAlt"),(('DWORD', None), "ipaddrWins"),(('DWORD', None), "ipaddrWinsAlt"),(('DWORD', None), "dwfNetProtocols"),(('WCHAR', None), "szDeviceType"),(('WCHAR', None), "szDeviceName"),(('WCHAR', None), "szX25PadType"),(('WCHAR', None), "szX25Address"),(('WCHAR', None), "szX25Facilities"),(('WCHAR', None), "szX25UserData"),(('DWORD', None), "dwChannels"),(('DWORD', None), "dwSubEntries"),(('DWORD', None), "dwDialMode"),(('DWORD', None), "dwDialExtraPercent"),(('DWORD', None), "dwDialExtraSampleSeconds"),(('DWORD', None), "dwHangUpExtraPercent"),(('DWORD', None), "dwHangUpExtraSampleSeconds"),(('DWORD', None), "dwIdleDisconnectSeconds"),(('DWORD', None), "dwType"),(('DWORD', None), "dwEncryptionType"),(('DWORD', None), "dwCustomAuthKey"),(('DWORD', None), "dwCustomAuthDataSize"),(('LPBYTE', None), "lpbCustomAuthData"),(('GUID', None), "guidId"),(('DWORD', None), "dwVpnStrategy"),(('ULONG', None), "AddressCount"),(('IN6_ADDR', None), "ipv6addrDns"),(('IN6_ADDR', None), "ipv6addrDnsAlt"),(('PIN6_ADDR', None), "ipv6addr"),]

    

class ('MPR_DEVICE_0', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "szDeviceType"),(('WCHAR', None), "szDeviceName"),]

    

class ('MPR_DEVICE_1', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "szDeviceType"),(('WCHAR', None), "szDeviceName"),(('WCHAR', None), "szLocalPhoneNumber"),(('PWCHAR', None), "szAlternates"),]

    

class ('MPR_CREDENTIALSEX_1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('DWORD', None), "dwOffset"),(('BYTE', None), "bData"),]

    

class ('IFFILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "bEnableFragChk"),]

    

class ('MPR_FILTER_0', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "fEnable"),]

    

class ('IPX_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "RoutingTableHashSize"),(('ULONG', None), "EventLogMask"),]

    

class ('IPX_IF_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "AdministratorState"),(('ULONG', None), "NetbiosAccept"),(('ULONG', None), "NetbiosDeliver"),]

    

class ('IPXWAN_IF_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Adminstate"),]

    

class ('IPX_STATIC_ROUTE_INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('USHORT', None), "TickCount"),(('USHORT', None), "HopCount"),(('UCHAR', None), "NextHopMacAddress"),]

    

class ('IPX_SERVER_ENTRY', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Type"),(('UCHAR', None), "Name"),(('UCHAR', None), "Network"),(('UCHAR', None), "Node"),(('UCHAR', None), "Socket"),(('USHORT', None), "HopCount"),]

    

class ('IPX_STATIC_NETBIOS_NAME_INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),]

    

class ('IPX_ADAPTER_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "PacketType"),(('WCHAR', None), "AdapterName"),]

    

class ('IPX_TRAFFIC_FILTER_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "FilterAction"),]

    

class ('IPX_TRAFFIC_FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "FilterDefinition"),(('UCHAR', None), "DestinationNetwork"),(('UCHAR', None), "DestinationNetworkMask"),(('UCHAR', None), "DestinationNode"),(('UCHAR', None), "DestinationSocket"),(('UCHAR', None), "SourceNetwork"),(('UCHAR', None), "SourceNetworkMask"),(('UCHAR', None), "SourceNode"),(('UCHAR', None), "SourceSocket"),(('UCHAR', None), "PacketType"),]

    

class ('IF_TABLE_INDEX', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),]

    

class ('ROUTING_TABLE_INDEX', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Network"),]

    

class ('STATIC_ROUTES_TABLE_INDEX', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('UCHAR', None), "Network"),]

    

class ('SERVICES_TABLE_INDEX', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "ServiceType"),(('UCHAR', None), "ServiceName"),]

    

class ('STATIC_SERVICES_TABLE_INDEX', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('USHORT', None), "ServiceType"),(('UCHAR', None), "ServiceName"),]

    

class ('IPX_MIB_INDEX', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('IF_TABLE_INDEX', None), InterfaceTableIndex),2 : (('ROUTING_TABLE_INDEX', None), RoutingTableIndex),3 : (('STATIC_ROUTES_TABLE_INDEX', None), StaticRoutesTableIndex),4 : (('SERVICES_TABLE_INDEX', None), ServicesTableIndex),5 : (('STATIC_SERVICES_TABLE_INDEX', None), StaticServicesTableIndex),}

    

class ('IPX_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('IPX_MIB_INDEX', None), "MibIndex"),]

    

class ('IPXMIB_BASE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "OperState"),(('UCHAR', None), "PrimaryNetNumber"),(('UCHAR', None), "Node"),(('UCHAR', None), "SysName"),(('ULONG', None), "MaxPathSplits"),(('ULONG', None), "IfCount"),(('ULONG', None), "DestCount"),(('ULONG', None), "ServCount"),]

    

class ('IPX_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "IfOperState"),(('ULONG', None), "MaxPacketSize"),(('ULONG', None), "InHdrErrors"),(('ULONG', None), "InFiltered"),(('ULONG', None), "InNoRoutes"),(('ULONG', None), "InDiscards"),(('ULONG', None), "InDelivers"),(('ULONG', None), "OutFiltered"),(('ULONG', None), "OutDiscards"),(('ULONG', None), "OutDelivers"),(('ULONG', None), "NetbiosReceived"),(('ULONG', None), "NetbiosSent"),]

    

class ('IPX_INTERFACE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('ULONG', None), "AdministratorState"),(('ULONG', None), "AdapterIndex"),(('UCHAR', None), "InterfaceName"),(('ULONG', None), "InterfaceType"),(('ULONG', None), "MediaType"),(('UCHAR', None), "NetNumber"),(('UCHAR', None), "MacAddress"),(('ULONG', None), "Delay"),(('ULONG', None), "Throughput"),(('ULONG', None), "NetbiosAccept"),(('ULONG', None), "NetbiosDeliver"),(('ULONG', None), "EnableIpxWanNegotiation"),(('IPX_IF_STATS', None), "IfStats"),]

    

class ('IPX_ROUTE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('ULONG', None), "Protocol"),(('UCHAR', None), "Network"),(('USHORT', None), "TickCount"),(('USHORT', None), "HopCount"),(('UCHAR', None), "NextHopMacAddress"),(('ULONG', None), "Flags"),]

    

class ('IPX_SERVICE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('ULONG', None), "Protocol"),(('IPX_SERVER_ENTRY', None), "Server"),]

    

class ('IPX_MIB_ROW', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('IPX_INTERFACE', None), Interface),2 : (('IPX_ROUTE', None), Route),3 : (('IPX_SERVICE', None), Service),}

    

class ('IPX_MIB_SET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('IPX_MIB_ROW', None), "MibRow"),]

    

class ('SAP_SERVICE_FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('UCHAR', None), "ServiceName"),]

    

class ('SAP_IF_FILTERS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "SupplyFilterAction"),(('ULONG', None), "SupplyFilterCount"),(('ULONG', None), "ListenFilterAction"),(('ULONG', None), "ListenFilterCount"),(('SAP_SERVICE_FILTER_INFO', None), "ServiceFilter"),]

    

class ('SAP_IF_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "AdminState"),(('ULONG', None), "UpdateMode"),(('ULONG', None), "PacketType"),(('ULONG', None), "Supply"),(('ULONG', None), "Listen"),(('ULONG', None), "GetNearestServerReply"),(('ULONG', None), "PeriodicUpdateInterval"),(('ULONG', None), "AgeIntervalMultiplier"),]

    

class ('SAP_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('SAP_IF_INFO', None), "SapIfInfo"),(('SAP_IF_FILTERS', None), "SapIfFilters"),]

    

class ('SAP_MIB_BASE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "SapOperState"),]

    

class ('SAP_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "SapIfOperState"),(('ULONG', None), "SapIfInputPackets"),(('ULONG', None), "SapIfOutputPackets"),]

    

class ('SAP_INTERFACE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('SAP_IF_INFO', None), "SapIfInfo"),(('SAP_IF_STATS', None), "SapIfStats"),]

    

class ('SAP_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('ULONG', None), "InterfaceIndex"),]

    

class ('SAP_MIB_SET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('SAP_INTERFACE', None), "SapInterface"),]

    

class ('RIPMIB_BASE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "RIPOperState"),]

    

class ('RIP_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "RipIfOperState"),(('ULONG', None), "RipIfInputPackets"),(('ULONG', None), "RipIfOutputPackets"),]

    

class ('RIP_IF_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "AdminState"),(('ULONG', None), "UpdateMode"),(('ULONG', None), "PacketType"),(('ULONG', None), "Supply"),(('ULONG', None), "Listen"),(('ULONG', None), "PeriodicUpdateInterval"),(('ULONG', None), "AgeIntervalMultiplier"),]

    

class ('RIP_INTERFACE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "InterfaceIndex"),(('RIP_IF_INFO', None), "RipIfInfo"),(('RIP_IF_STATS', None), "RipIfStats"),]

    

class ('RIP_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('ULONG', None), "InterfaceIndex"),]

    

class ('RIP_MIB_SET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TableId"),(('RIP_INTERFACE', None), "RipInterface"),]

    

class ('EAPTLS_HASH', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "cbHash"),(('BYTE', None), "pbHash"),]

    

class ('EAPTLS_USER_PROPERTIES', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "reserved"),(('DWORD', None), "dwVersion"),(('DWORD', None), "dwSize"),(('DWORD', None), "fFlags"),(('EAPTLS_HASH', None), "Hash"),(('PWCHAR', None), "pwszDiffUser"),(('DWORD', None), "dwPinOffset"),(('PWCHAR', None), "pwszPin"),(('USHORT', None), "usLength"),(('USHORT', None), "usMaximumLength"),(('UCHAR', None), "ucSeed"),(('WCHAR', None), "awszString"),]

    

class ('IPBOOTP_GLOBAL_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "GC_LoggingLevel"),(('DWORD', None), "GC_MaxRecvQueueSize"),(('DWORD', None), "GC_ServerCount"),]

    

class ('IPBOOTP_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IC_State"),(('DWORD', None), "IC_RelayMode"),(('DWORD', None), "IC_MaxHopCount"),(('DWORD', None), "IC_MinSecondsSinceBoot"),]

    

class ('IPBOOTP_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGID_TypeID"),(('DWORD', None), "IMGID_IfIndex"),]

    

class ('IPBOOTP_MIB_GET_OUTPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGOD_TypeID"),(('DWORD', None), "IMGOD_IfIndex"),(('BYTE', None), "IMGOD_Buffer"),]

    

class ('IPBOOTP_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IS_State"),(('DWORD', None), "IS_SendFailures"),(('DWORD', None), "IS_ReceiveFailures"),(('DWORD', None), "IS_ArpUpdateFailures"),(('DWORD', None), "IS_RequestsReceived"),(('DWORD', None), "IS_RequestsDiscarded"),(('DWORD', None), "IS_RepliesReceived"),(('DWORD', None), "IS_RepliesDiscarded"),]

    

class ('IPBOOTP_IF_BINDING', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IB_State"),(('DWORD', None), "IB_AddrCount"),]

    

class ('IPBOOTP_IP_ADDRESS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IA_Address"),(('DWORD', None), "IA_Netmask"),]

    

class ('DHCPV6R_MIB_GET_OUTPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGOD_TypeID"),(('DWORD', None), "IMGOD_IfIndex"),(('BYTE', None), "IMGOD_Buffer"),]

    

class ('DHCPV6R_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IS_State"),(('DWORD', None), "IS_SendFailures"),(('DWORD', None), "IS_ReceiveFailures"),(('DWORD', None), "IS_RequestsReceived"),(('DWORD', None), "IS_RequestsDiscarded"),(('DWORD', None), "IS_RepliesReceived"),(('DWORD', None), "IS_RepliesDiscarded"),]

    

class ('DHCPV6R_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGID_TypeID"),(('DWORD', None), "IMGID_IfIndex"),]

    

class ('DHCPV6R_GLOBAL_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "GC_LoggingLevel"),(('DWORD', None), "GC_MaxRecvQueueSize"),(('DWORD', None), "GC_ServerCount"),]

    

class ('DHCPV6R_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IC_State"),(('DWORD', None), "IC_RelayMode"),(('DWORD', None), "IC_MaxHopCount"),(('DWORD', None), "IC_MinElapsedTime"),]

    

class ('IPRIP_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGID_TypeID"),(('U0', None), "u0"),]

    

class ('IPRIP_MIB_GET_OUTPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IMGOD_TypeID"),(('U0', None), "u0"),(('BYTE', None), "IMGOD_Buffer"),]

    

class ('IPRIP_GLOBAL_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "GS_SystemRouteChanges"),(('DWORD', None), "GS_TotalResponsesSent"),]

    

class ('IPRIP_GLOBAL_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "GC_LoggingLevel"),(('DWORD', None), "GC_MaxRecvQueueSize"),(('DWORD', None), "GC_MaxSendQueueSize"),(('DWORD', None), "GC_MinTriggeredUpdateInterval"),(('DWORD', None), "GC_PeerFilterMode"),(('DWORD', None), "GC_PeerFilterCount"),]

    

class ('IPRIP_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IS_State"),(('DWORD', None), "IS_SendFailures"),(('DWORD', None), "IS_ReceiveFailures"),(('DWORD', None), "IS_RequestsSent"),(('DWORD', None), "IS_RequestsReceived"),(('DWORD', None), "IS_ResponsesSent"),(('DWORD', None), "IS_ResponsesReceived"),(('DWORD', None), "IS_BadResponsePacketsReceived"),(('DWORD', None), "IS_BadResponseEntriesReceived"),(('DWORD', None), "IS_TriggeredUpdatesSent"),]

    

class ('IPRIP_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IC_State"),(('DWORD', None), "IC_Metric"),(('DWORD', None), "IC_UpdateMode"),(('DWORD', None), "IC_AcceptMode"),(('DWORD', None), "IC_AnnounceMode"),(('DWORD', None), "IC_ProtocolFlags"),(('DWORD', None), "IC_RouteExpirationInterval"),(('DWORD', None), "IC_RouteRemovalInterval"),(('DWORD', None), "IC_FullUpdateInterval"),(('DWORD', None), "IC_AuthenticationType"),(('BYTE', None), "IC_AuthenticationKey"),(('WORD', None), "IC_RouteTag"),(('DWORD', None), "IC_UnicastPeerMode"),(('DWORD', None), "IC_AcceptFilterMode"),(('DWORD', None), "IC_AnnounceFilterMode"),(('DWORD', None), "IC_UnicastPeerCount"),(('DWORD', None), "IC_AcceptFilterCount"),(('DWORD', None), "IC_AnnounceFilterCount"),]

    

class ('IPRIP_ROUTE_FILTER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "RF_LoAddress"),(('DWORD', None), "RF_HiAddress"),]

    

class ('IPRIP_IF_BINDING', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IB_State"),(('DWORD', None), "IB_AddrCount"),]

    

class ('IPRIP_IP_ADDRESS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IA_Address"),(('DWORD', None), "IA_Netmask"),]

    

class ('IPRIP_PEER_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "PS_LastPeerRouteTag"),(('DWORD', None), "PS_LastPeerUpdateTickCount"),(('DWORD', None), "PS_LastPeerUpdateVersion"),(('DWORD', None), "PS_BadResponsePacketsFromPeer"),(('DWORD', None), "PS_BadResponseEntriesFromPeer"),]

    

class ('IGMP_MIB_GET_INPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "TypeId"),(('USHORT', None), "Flags"),(('USHORT', None), "Signature"),(('DWORD', None), "IfIndex"),(('DWORD', None), "RasClientAddr"),(('DWORD', None), "GroupAddr"),(('DWORD', None), "Count"),]

    

class ('IGMP_MIB_GET_OUTPUT_DATA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "TypeId"),(('DWORD', None), "Flags"),(('DWORD', None), "Count"),(('BYTE', None), "Buffer"),]

    

class ('IGMP_MIB_GLOBAL_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Version"),(('DWORD', None), "LoggingLevel"),(('DWORD', None), "RasClientStats"),]

    

class ('IGMP_MIB_GLOBAL_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "CurrentGroupMemberships"),(('DWORD', None), "GroupMembershipsAdded"),]

    

class ('IGMP_MIB_IF_BINDING', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IfIndex"),(('DWORD', None), "IfType"),(('DWORD', None), "State"),(('DWORD', None), "AddrCount"),]

    

class ('IGMP_MIB_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Version"),(('DWORD', None), "IfIndex"),(('DWORD', None), "IpAddr"),(('DWORD', None), "IfType"),(('DWORD', None), "Flags"),(('DWORD', None), "IgmpProtocolType"),(('DWORD', None), "RobustnessVariable"),(('DWORD', None), "StartupQueryInterval"),(('DWORD', None), "StartupQueryCount"),(('DWORD', None), "GenQueryInterval"),(('DWORD', None), "GenQueryMaxResponseTime"),(('DWORD', None), "LastMemQueryInterval"),(('DWORD', None), "LastMemQueryCount"),(('DWORD', None), "OtherQuerierPresentInterval"),(('DWORD', None), "GroupMembershipTimeout"),(('DWORD', None), "NumStaticGroups"),]

    

class ('IGMP_MIB_IF_GROUPS_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IfIndex"),(('DWORD', None), "IpAddr"),(('DWORD', None), "IfType"),(('DWORD', None), "NumGroups"),(('BYTE', None), "Buffer"),]

    

class ('IGMP_MIB_GROUP_INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "IpAddr"),(('DWORD', None), "GroupUpTime"),(('DWORD', None), "GroupExpiryTime"),(('DWORD', None), "LastReporter"),(('DWORD', None), "V1HostPresentTimeLeft"),(('DWORD', None), "Flags"),]

    

class ('IGMP_MIB_IF_STATS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "IfIndex"),(('DWORD', None), "IpAddr"),(('DWORD', None), "IfType"),(('BYTE', None), "State"),(('BYTE', None), "QuerierState"),(('DWORD', None), "IgmpProtocolType"),(('DWORD', None), "QuerierIpAddr"),(('DWORD', None), "ProxyIfIndex"),(('DWORD', None), "QuerierPresentTimeLeft"),(('DWORD', None), "LastQuerierChangeTime"),(('DWORD', None), "V1QuerierPresentTimeLeft"),(('DWORD', None), "Uptime"),(('DWORD', None), "TotalIgmpPacketsReceived"),(('DWORD', None), "TotalIgmpPacketsForRouter"),(('DWORD', None), "GeneralQueriesReceived"),(('DWORD', None), "WrongVersionQueries"),(('DWORD', None), "JoinsReceived"),(('DWORD', None), "LeavesReceived"),(('DWORD', None), "CurrentGroupMemberships"),(('DWORD', None), "GroupMembershipsAdded"),(('DWORD', None), "WrongChecksumPackets"),(('DWORD', None), "ShortPacketsReceived"),(('DWORD', None), "LongPacketsReceived"),(('DWORD', None), "PacketsWithoutRtrAlert"),]

    

class ('IGMP_MIB_GROUP_IFS_LIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "GroupAddr"),(('DWORD', None), "NumInterfaces"),(('BYTE', None), "Buffer"),]

    

class ('IGMP_MIB_GROUP_SOURCE_INFO_V3', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Source"),(('DWORD', None), "SourceExpiryTime"),(('DWORD', None), "SourceUpTime"),(('DWORD', None), "Flags"),]

    

class ('IGMP_MIB_GROUP_INFO_V3', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('DWORD', None), "IpAddr"),(('DWORD', None), "GroupUpTime"),(('DWORD', None), "GroupExpiryTime"),(('DWORD', None), "LastReporter"),(('DWORD', None), "V1HostPresentTimeLeft"),(('DWORD', None), "Flags"),(('DWORD', None), "Version"),(('DWORD', None), "Size"),(('DWORD', None), "FilterType"),(('DWORD', None), "V2HostPresentTimeLeft"),(('DWORD', None), "NumSources"),]

    

class ('INTERFACE_ROUTE_ENTRY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwIndex"),(('INTERFACE_ROUTE_INFO', None), "routeInfo"),]

    

class ('IP_NAT_MIB_QUERY', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Oid"),(('U0', None), "u0"),]

    

class ('IP_NAT_SESSION_MAPPING', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Protocol"),(('ULONG', None), "PrivateAddress"),(('USHORT', None), "PrivatePort"),(('ULONG', None), "PublicAddress"),(('USHORT', None), "PublicPort"),(('ULONG', None), "RemoteAddress"),(('USHORT', None), "RemotePort"),(('IP_NAT_DIRECTION', None), "Direction"),(('ULONG', None), "IdleTime"),]

    

class ('IP_NAT_ENUMERATE_SESSION_MAPPINGS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Index"),(('ULONG', None), "EnumerateContext"),(('ULONG', None), "EnumerateCount"),(('ULONG', None), "EnumerateTotalHint"),(('IP_NAT_SESSION_MAPPING', None), "EnumerateTable"),]

    

class ('IP_NAT_INTERFACE_STATISTICS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TotalMappings"),(('ULONG', None), "InboundMappings"),(('ULONG64', None), "BytesForward"),(('ULONG64', None), "BytesReverse"),(('ULONG64', None), "PacketsForward"),(('ULONG64', None), "PacketsReverse"),(('ULONG64', None), "RejectsForward"),(('ULONG64', None), "RejectsReverse"),]

    

class ('IP_DNS_PROXY_MIB_QUERY', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Oid"),(('U0', None), "u0"),]

    

class ('IP_DNS_PROXY_STATISTICS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "MessagesIgnored"),(('ULONG', None), "QueriesReceived"),(('ULONG', None), "ResponsesReceived"),(('ULONG', None), "QueriesSent"),(('ULONG', None), "ResponsesSent"),]

    

class ('IP_AUTO_DHCP_MIB_QUERY', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Oid"),(('U0', None), "u0"),(('ULONG', None), "Reserved"),]

    

class ('IP_AUTO_DHCP_STATISTICS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "MessagesIgnored"),(('ULONG', None), "BootpOffersSent"),(('ULONG', None), "DiscoversReceived"),(('ULONG', None), "InformsReceived"),(('ULONG', None), "OffersSent"),(('ULONG', None), "RequestsReceived"),(('ULONG', None), "AcksSent"),(('ULONG', None), "NaksSent"),(('ULONG', None), "DeclinesReceived"),(('ULONG', None), "ReleasesReceived"),]

    

class ('MIB_DA_MSG', None)(NdrStructure):
    MEMBERS = [(('UINT32', None), "op_code"),(('UINT32', None), "ret_code"),(('UINT32', None), "in_snmp_id"),(('UINT32', None), "obj_id"),(('UINT32', None), "attr_id"),(('UINT32', None), "inst_id"),(('UINT32', None), "next_snmp_id"),(('UINT32', None), "creator"),(('UINT32', None), "attr_type"),(('UINT32', None), "inst_cnt"),(('UINT32', None), "map_flag"),(('ULONG_PTR', None), "data"),]

    

class ('IP_AUTO_DHCP_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "LoggingLevel"),(('ULONG', None), "Flags"),(('ULONG', None), "LeaseTime"),(('ULONG', None), "ScopeNetwork"),(('ULONG', None), "ScopeMask"),(('ULONG', None), "ExclusionCount"),(('ULONG', None), "ExclusionArray"),]

    

class ('IP_AUTO_DHCP_INTERFACE_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Flags"),]

    

class ('IP_DNS_PROXY_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "LoggingLevel"),(('ULONG', None), "Flags"),(('ULONG', None), "TimeoutSeconds"),]

    

class ('IP_DNS_PROXY_INTERFACE_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Flags"),]

    

class ('IP_NAT_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "LoggingLevel"),(('ULONG', None), "Flags"),(('RTR_INFO_BLOCK_HEADER', None), "Header"),]

    

class ('IP_NAT_TIMEOUT', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "TCPTimeoutSeconds"),(('ULONG', None), "UDPTimeoutSeconds"),]

    

class ('IP_NAT_INTERFACE_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "Index"),(('ULONG', None), "Flags"),(('RTR_INFO_BLOCK_HEADER', None), "Header"),]

    

class ('IP_NAT_ADDRESS_RANGE', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "StartAddress"),(('ULONG', None), "EndAddress"),(('ULONG', None), "SubnetMask"),]

    

class ('IP_NAT_PORT_MAPPING', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Protocol"),(('USHORT', None), "PublicPort"),(('ULONG', None), "PublicAddress"),(('USHORT', None), "PrivatePort"),(('ULONG', None), "PrivateAddress"),]

    

class ('IP_NAT_ADDRESS_MAPPING', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "PrivateAddress"),(('ULONG', None), "PublicAddress"),(('BOOLEAN', None), "AllowInboundSessions"),]

    

class ('IP_ALG_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "LoggingLevel"),(('ULONG', None), "Flags"),]

    

class ('RIP_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "EventLogMask"),]

    

class ('RIP_ROUTE_FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Network"),(('UCHAR', None), "Mask"),]

    

class ('RIP_IF_FILTERS', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "SupplyFilterAction"),(('ULONG', None), "SupplyFilterCount"),(('ULONG', None), "ListenFilterAction"),(('ULONG', None), "ListenFilterCount"),(('RIP_ROUTE_FILTER_INFO', None), "RouteFilter"),]

    

class ('RIP_IF_CONFIG', None)(NdrStructure):
    MEMBERS = [(('RIP_IF_INFO', None), "RipIfInfo"),(('RIP_IF_FILTERS', None), "RipIfFilters"),]

    

class ('SAP_GLOBAL_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "EventLogMask"),]

    

class ('OSPF_ROUTE_FILTER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwAddress"),(('DWORD', None), "dwMask"),]

    

class ('OSPF_ROUTE_FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('OSPF_FILTER_ACTION', None), "ofaActionOnMatch"),(('DWORD', None), "dwNumFilters"),(('OSPF_ROUTE_FILTER', None), "pFilters"),]

    

class ('OSPF_PROTO_FILTER_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('OSPF_FILTER_ACTION', None), "ofaActionOnMatch"),(('DWORD', None), "dwNumProtoIds"),(('DWORD', None), "pdwProtoId"),]

    

class ('OSPF_GLOBAL_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "routerId"),(('DWORD', None), "ASBrdrRtr"),(('DWORD', None), "logLevel"),]

    

class ('OSPF_AREA_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "areaId"),(('DWORD', None), "authType"),(('DWORD', None), "importASExtern"),(('DWORD', None), "stubMetric"),(('DWORD', None), "importSumAdv"),]

    

class ('OSPF_AREA_RANGE_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "areaId"),(('DWORD', None), "rangeNet"),(('DWORD', None), "rangeMask"),]

    

class ('OSPF_VIRT_INTERFACE_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "transitAreaId"),(('DWORD', None), "virtNeighborRouterId"),(('DWORD', None), "transitDelay"),(('DWORD', None), "retransInterval"),(('DWORD', None), "helloInterval"),(('DWORD', None), "deadInterval"),(('BYTE', None), "password"),]

    

class ('OSPF_INTERFACE_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "intfIpAddr"),(('DWORD', None), "intfSubnetMask"),(('DWORD', None), "areaId"),(('DWORD', None), "intfType"),(('DWORD', None), "routerPriority"),(('DWORD', None), "transitDelay"),(('DWORD', None), "retransInterval"),(('DWORD', None), "helloInterval"),(('DWORD', None), "deadInterval"),(('DWORD', None), "pollInterval"),(('DWORD', None), "metricCost"),(('BYTE', None), "password"),(('DWORD', None), "mtuSize"),]

    

class ('OSPF_NBMA_NEIGHBOR_PARAM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "type"),(('DWORD', None), "create"),(('DWORD', None), "enable"),(('DWORD', None), "neighborIpAddr"),(('DWORD', None), "intfIpAddr"),(('DWORD', None), "neighborPriority"),]

    

class ('REQUESTBUFFER', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "RB_PCBIndex"),(('REQTYPES', None), "RB_Reqtype"),(('DWORD', None), "RB_Dummy"),(('DWORD', None), "RB_Done"),(('LONGLONG', None), "Alignment"),(('BYTE', None), "RB_Buffer"),]

    

class ('DEVICECONFIGINFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "retcode"),(('DWORD', None), "dwVersion"),(('DWORD', None), "cbBuffer"),(('DWORD', None), "cEntries"),(('BYTE', None), "abdata"),]

    

class ('RAS_DEVICE_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwVersion"),(('BOOL', None), "fWrite"),(('BOOL', None), "fRasEnabled"),(('BOOL', None), "fRouterEnabled"),(('BOOL', None), "fRouterOutboundEnabled"),(('DWORD', None), "dwTapiLineId"),(('DWORD', None), "dwError"),(('DWORD', None), "dwNumEndPoints"),(('DWORD', None), "dwMaxOutCalls"),(('DWORD', None), "dwMaxInCalls"),(('DWORD', None), "dwMinWanEndPoints"),(('DWORD', None), "dwMaxWanEndPoints"),(('RASDEVICETYPE', None), "eDeviceType"),(('GUID', None), "guidDevice"),(('CHAR', None), "szPortName"),(('CHAR', None), "szDeviceName"),(('WCHAR', None), "wszDeviceName"),]

    

class ('RAS_CALLEDID_INFO', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('BYTE', None), "bCalledId"),]

    

class ('GETSETCALLEDID', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "retcode"),(('BOOL', None), "fWrite"),(('DWORD', None), "dwSize"),(('GUID', None), "guidDevice"),(('RAS_DEVICE_INFO', None), "rdi"),(('RAS_CALLEDID_INFO', None), "rciInfo"),]

    

class ('RAS_NDISWAN_DRIVER_INFO', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "DriverCaps"),(('ULONG', None), "Reserved"),]

    

class ('GETNDISWANDRIVERCAPSSTRUCT', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "retcode"),(('RAS_NDISWAN_DRIVER_INFO', None), "NdiswanDriverInfo"),]

    

class ('GETDEVCONFIGSTRUCT', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "retcode"),(('CHAR', None), "devicetype"),(('DWORD', None), "size"),(('BYTE', None), "config"),]

    

class ('ENUM', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "retcode"),(('DWORD', None), "size"),(('DWORD', None), "entries"),(('BYTE', None), "buffer"),]

    

class ('RASMAN_PORT_32', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "P_Port"),(('CHAR', None), "P_PortName"),(('RASMAN_STATUS', None), "P_Status"),(('RASDEVICETYPE', None), "P_rdtDeviceType"),(('RASMAN_USAGE', None), "P_ConfiguredUsage"),(('RASMAN_USAGE', None), "P_CurrentUsage"),(('CHAR', None), "P_MediaName"),(('CHAR', None), "P_DeviceType"),(('CHAR', None), "P_DeviceName"),(('DWORD', None), "P_LineDeviceId"),(('DWORD', None), "P_AddressId"),]

    

class ('RASMAN_INFO', None)(NdrStructure):
    MEMBERS = [(('RASMAN_STATUS', None), "RI_PortStatus"),(('RASMAN_STATE', None), "RI_ConnState"),(('DWORD', None), "RI_LinkSpeed"),(('DWORD', None), "RI_LastError"),(('RASMAN_USAGE', None), "RI_CurrentUsage"),(('CHAR', None), "RI_DeviceTypeConnecting"),(('CHAR', None), "RI_DeviceConnecting"),(('CHAR', None), "RI_szDeviceType"),(('CHAR', None), "RI_szDeviceName"),(('CHAR', None), "RI_szPortName"),(('RASMAN_DISCONNECT_TYPE', None), "RI_DisconnectType"),(('DWORD', None), "RI_OwnershipFlag"),(('DWORD', None), "RI_ConnectDuration"),(('DWORD', None), "RI_BytesReceived"),(('CHAR', None), "RI_Phonebook"),(('CHAR', None), "RI_PhoneEntry"),(('HANDLE', None), "RI_ConnectionHandle"),(('DWORD', None), "RI_SubEntry"),(('RASDEVICETYPE', None), "RI_rdtDeviceType"),(('GUID', None), "RI_GuidEntry"),(('DWORD', None), "RI_dwSessionId"),(('DWORD', None), "RI_dwFlags"),(('GUID', None), "RI_CorrelationGuid"),]

    

class ('INFO', None)(NdrStructure):
    MEMBERS = [(('U0', None), "u0"),(('RASMAN_INFO', None), "info"),]

    

class ('RASRPC_CALLBACKLIST', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "pszPortName"),(('WCHAR', None), "pszDeviceName"),(('WCHAR', None), "pszNumber"),(('DWORD', None), "dwDeviceType"),(('PPNEXT', None), "*pNext"),]

    

class ('RASRPC_STRINGLIST', None)(NdrStructure):
    MEMBERS = [(('WCHAR', None), "psz"),(('PPNEXT', None), "*pNext"),]

    

class ('RASRPC_LOCATIONLIST', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLocationId"),(('DWORD', None), "iPrefix"),(('DWORD', None), "iSuffix"),(('PPNEXT', None), "*pNext"),]

    

class ('RASRPC_PBUSER', None)(NdrStructure):
    MEMBERS = [(('BOOL', None), "fOperatorDial"),(('BOOL', None), "fPreviewPhoneNumber"),(('BOOL', None), "fUseLocation"),(('BOOL', None), "fShowLights"),(('BOOL', None), "fShowConnectStatus"),(('BOOL', None), "fCloseOnDial"),(('BOOL', None), "fAllowLogonPhonebookEdits"),(('BOOL', None), "fAllowLogonLocationEdits"),(('BOOL', None), "fSkipConnectComplete"),(('BOOL', None), "fNewEntryWizard"),(('DWORD', None), "dwRedialAttempts"),(('DWORD', None), "dwRedialSeconds"),(('DWORD', None), "dwIdleDisconnectSeconds"),(('BOOL', None), "fRedialOnLinkFailure"),(('BOOL', None), "fPopupOnTopWhenRedialing"),(('BOOL', None), "fExpandAutoDialQuery"),(('DWORD', None), "dwCallbackMode"),(('LPRASRPC_CALLBACKLIST', None), "pCallbacks"),(('WCHAR', None), "pszLastCallbackByCaller"),(('DWORD', None), "dwPhonebookMode"),(('WCHAR', None), "pszPersonalFile"),(('WCHAR', None), "pszAlternatePath"),(('LPRASRPC_STRINGLIST', None), "pPhonebooks"),(('LPRASRPC_STRINGLIST', None), "pAreaCodes"),(('BOOL', None), "fUseAreaAndCountry"),(('LPRASRPC_STRINGLIST', None), "pPrefixes"),(('LPRASRPC_STRINGLIST', None), "pSuffixes"),(('LPRASRPC_LOCATIONLIST', None), "pLocations"),(('DWORD', None), "dwXPhonebook"),(('DWORD', None), "dwYPhonebook"),(('WCHAR', None), "pszDefaultEntry"),(('BOOL', None), "fInitialized"),(('BOOL', None), "fDirty"),]

    
Method("RMprAdminServerGetInfo",
In(DIM_HANDLE),
In(DWORD),
Out(PDIM_INFORMATION_CONTAINER),
),Method("RRasAdminConnectionEnum",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
Out(LPDWORD),
Out(LPDWORD),
InOut(LPDWORD),
),Method("RRasAdminConnectionGetInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
Out(PDIM_INFORMATION_CONTAINER),
),Method("RRasAdminConnectionClearStats",
In(DIM_HANDLE),
In(DWORD),
),Method("RRasAdminPortEnum",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
Out(LPDWORD),
Out(LPDWORD),
InOut(LPDWORD),
),Method("RRasAdminPortGetInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
Out(PDIM_INFORMATION_CONTAINER),
),Method("RRasAdminPortClearStats",
In(DIM_HANDLE),
In(DWORD),
),Method("RRasAdminPortReset",
In(DIM_HANDLE),
In(DWORD),
),Method("RRasAdminPortDisconnect",
In(DIM_HANDLE),
In(DWORD),
),Method("RRouterInterfaceTransportSetGlobalInfo",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INTERFACE_CONTAINER),
),Method("RRouterInterfaceTransportGetGlobalInfo",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INTERFACE_CONTAINER),
),Method("RRouterInterfaceGetHandle",
In(DIM_HANDLE),
In(LPWSTR),
InOut(LPDWORD),
In(DWORD),
),Method("RRouterInterfaceCreate",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INFORMATION_CONTAINER),
InOut(LPDWORD),
),Method("RRouterInterfaceGetInfo",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
),Method("RRouterInterfaceSetInfo",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INFORMATION_CONTAINER),
In(DWORD),
),Method("RRouterInterfaceDelete",
In(DIM_HANDLE),
In(DWORD),
),Method("RRouterInterfaceTransportRemove",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
),Method("RRouterInterfaceTransportAdd",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(PDIM_INTERFACE_CONTAINER),
),Method("RRouterInterfaceTransportGetInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_INTERFACE_CONTAINER),
),Method("RRouterInterfaceTransportSetInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(PDIM_INTERFACE_CONTAINER),
),Method("RRouterInterfaceEnum",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
Out(LPDWORD),
Out(LPDWORD),
InOut(LPDWORD),
),Method("RRouterInterfaceConnect",
In(DIM_HANDLE),
In(DWORD),
In(ULONG_PTR),
In(DWORD),
In(DWORD),
),Method("RRouterInterfaceDisconnect",
In(DIM_HANDLE),
In(DWORD),
),Method("RRouterInterfaceUpdateRoutes",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(ULONG_PTR),
In(DWORD),
),Method("RRouterInterfaceQueryUpdateResult",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
Out(LPDWORD),
),Method("RRouterInterfaceUpdatePhonebookInfo",
In(DIM_HANDLE),
In(DWORD),
),Method("RMIBEntryCreate",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBEntryDelete",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBEntrySet",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBEntryGet",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBEntryGetFirst",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBEntryGetNext",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBGetTrapInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
InOut(PDIM_MIB_ENTRY_CONTAINER),
),Method("RMIBSetTrapInfo",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(ULONG_PTR),
In(DWORD),
InOut(PDIM_MIB_ENTRY_CONTAINER),
),Method("RRasAdminConnectionNotification",
In(DIM_HANDLE),
In(DWORD),
In(DWORD),
In(ULONG_PTR),
),Method("RRasAdminSendUserMessage",
In(DIM_HANDLE),
In(DWORD),
In(LPWSTR),
),Method("RRouterDeviceEnum",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
InOut(LPDWORD),
),Method("RRouterInterfaceTransportCreate",
In(DIM_HANDLE),
In(DWORD),
In(LPWSTR),
In(PDIM_INTERFACE_CONTAINER),
In(LPWSTR),
),Method("RRouterInterfaceDeviceGetInfo",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
In(DWORD),
),Method("RRouterInterfaceDeviceSetInfo",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INFORMATION_CONTAINER),
In(DWORD),
In(DWORD),
),Method("RRouterInterfaceSetCredentialsEx",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INFORMATION_CONTAINER),
In(DWORD),
),Method("RRouterInterfaceGetCredentialsEx",
In(DIM_HANDLE),
In(DWORD),
InOut(PDIM_INFORMATION_CONTAINER),
In(DWORD),
),Method("RRasAdminConnectionRemoveQuarantine",
In(DIM_HANDLE),
In(DWORD),
In(BOOL),
),Method("RMprAdminServerSetInfo",
In(DIM_HANDLE),
In(DWORD),
In(PDIM_INFORMATION_CONTAINER),
),Method("RMprAdminServerGetInfoEx",
In(DIM_HANDLE),
InOut(PMPR_SERVER_EX_IDL),
),Method("RRasAdminConnectionEnumEx",
In(DIM_HANDLE),
In(PMPRAPI_OBJECT_HEADER_IDL),
In(DWORD),
Out(LPDWORD),
Out(LPDWORD),
Out(PPRAS_CONNECTION_EX_IDL),
InOut(LPDWORD),
),Method("RRasAdminConnectionGetInfoEx",
In(DIM_HANDLE),
In(DWORD),
In(PMPRAPI_OBJECT_HEADER_IDL),
Out(PRAS_CONNECTION_EX_IDL),
),Method("RMprAdminServerSetInfoEx",
In(DIM_HANDLE),
In(PMPR_SERVER_SET_CONFIG_EX_IDL),
),Method("RRasAdminUpdateConnection",
In(DIM_HANDLE),
In(DWORD),
In(PRAS_UPDATE_CONNECTION_IDL),
),Method("RRouterInterfaceSetCredentialsLocal",
In(DIM_HANDLE),
In(LPWSTR),
In(LPWSTR),
In(LPWSTR),
In(LPWSTR),
),Method("RRouterInterfaceGetCredentialsLocal",
In(DIM_HANDLE),
In(LPWSTR),
Out(PLPWSTR),
Out(PLPWSTR),
Out(PLPWSTR),
),Method("RRouterInterfaceGetCustomInfoEx",
In(DIM_HANDLE),
In(DWORD),
InOut(PMPR_IF_CUSTOMINFOEX_IDL),
),Method("RRouterInterfaceSetCustomInfoEx",
In(DIM_HANDLE),
In(DWORD),
InOut(PMPR_IF_CUSTOMINFOEX_IDL),
),