
from fuzzer.midl import *
from fuzzer.core import *
DWORD64 = NdrHyper
DWORD = NdrLong
__INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
INT = NdrLong
VOID = CONTEXT_HANDLE
LONG = NdrLong
__INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    

class COMVERSION(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "MajorVersion"),(UNSIGNED_SHORT, "MinorVersion"),]

    

class ORPC_EXTENT(NdrStructure):
    MEMBERS = [(GUID, "id"),(UNSIGNED_LONG, "size"),(BYTE, "data"),]

    

class ORPC_EXTENT_ARRAY(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "size"),(UNSIGNED_LONG, "reserved"),(PPORPC_EXTENT, "extent"),]

    

class ORPCTHIS(NdrStructure):
    MEMBERS = [(COMVERSION, "version"),(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "reserved1"),(CID, "cid"),(PORPC_EXTENT_ARRAY, "extensions"),]

    

class ORPCTHAT(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(PORPC_EXTENT_ARRAY, "extensions"),]

    

class DUALSTRINGARRAY(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "wNumEntries"),(UNSIGNED_SHORT, "wSecurityOffset"),(UNSIGNED_SHORT, "aStringArray"),]

    

class MINTERFACEPOINTER(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "ulCntData"),(BYTE, "abData"),]

    

class ERROROBJECTDATA(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwHelpContext"),(IID, "iid"),(PWCHAR_T, "pszSource"),(PWCHAR_T, "pszDescription"),(PWCHAR_T, "pszHelpFile"),]

    

class STDOBJREF(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "cPublicRefs"),(OXID, "oxid"),(OID, "oid"),(IPID, "ipid"),]

    

class REMQIRESULT(NdrStructure):
    MEMBERS = [(HRESULT, "hResult"),(STDOBJREF, "std"),]

    

class REMINTERFACEREF(NdrStructure):
    MEMBERS = [(IPID, "ipid"),(UNSIGNED_LONG, "cPublicRefs"),(UNSIGNED_LONG, "cPrivateRefs"),]

    

class COSERVERINFO(NdrStructure):
    MEMBERS = [(DWORD, "dwReserved1"),(PWCHAR_T, "pwszName"),(PDWORD, "pdwReserved"),(DWORD, "dwReserved2"),]

    

class CUSTOMREMOTE_REQUEST_SCM_INFO(NdrStructure):
    MEMBERS = [(DWORD, "ClientImpLevel"),(UNSIGNED_SHORT, "cRequestedProtseqs"),(PUNSIGNED_SHORT, "pRequestedProtseqs"),]

    

class CUSTOMREMOTE_REPLY_SCM_INFO(NdrStructure):
    MEMBERS = [(OXID, "Oxid"),(PDUALSTRINGARRAY, "pdsaOxidBindings"),(IPID, "ipidRemUnknown"),(DWORD, "authnHint"),(COMVERSION, "serverVersion"),]

    

class INSTANTIATIONINFODATA(NdrStructure):
    MEMBERS = [(CLSID, "classId"),(DWORD, "classCtx"),(DWORD, "actvflags"),(LONG, "fIsSurrogate"),(DWORD, "cIID"),(DWORD, "instFlag"),(PIID, "pIID"),(DWORD, "thisSize"),(COMVERSION, "clientCOMVersion"),]

    

class LOCATIONINFODATA(NdrStructure):
    MEMBERS = [(PWCHAR_T, "machineName"),(DWORD, "processId"),(DWORD, "apartmentId"),(DWORD, "contextId"),]

    

class ACTIVATIONCONTEXTINFODATA(NdrStructure):
    MEMBERS = [(LONG, "clientOK"),(LONG, "bReserved1"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(PMINTERFACEPOINTER, "pIFDClientCtx"),(PMINTERFACEPOINTER, "pIFDPrototypeCtx"),]

    

class CUSTOMHEADER(NdrStructure):
    MEMBERS = [(DWORD, "totalSize"),(DWORD, "headerSize"),(DWORD, "dwReserved"),(DWORD, "destCtx"),(DWORD, "cIfs"),(CLSID, "classInfoClsid"),(PCLSID, "pclsid"),(PDWORD, "pSizes"),(PDWORD, "pdwReserved"),]

    

class PROPSOUTINFO(NdrStructure):
    MEMBERS = [(DWORD, "cIfs"),(PIID, "piid"),(PHRESULT, "phresults"),(PPMINTERFACEPOINTER, "ppIntfData"),]

    

class SECURITYINFODATA(NdrStructure):
    MEMBERS = [(DWORD, "dwAuthnFlags"),(PCOSERVERINFO, "pServerInfo"),(PDWORD, "pdwReserved"),]

    

class SCMREQUESTINFODATA(NdrStructure):
    MEMBERS = [(PDWORD, "pdwReserved"),(PCUSTOMREMOTE_REQUEST_SCM_INFO, "remoteRequest"),]

    

class SCMREPLYINFODATA(NdrStructure):
    MEMBERS = [(PDWORD, "pdwReserved"),(PCUSTOMREMOTE_REPLY_SCM_INFO, "remoteReply"),]

    

class INSTANCEINFODATA(NdrStructure):
    MEMBERS = [(PWCHAR_T, "fileName"),(DWORD, "mode"),(PMINTERFACEPOINTER, "ifdROT"),(PMINTERFACEPOINTER, "ifdStg"),]

    

class SPECIALPROPERTIESDATA(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved1"),(UNSIGNED___INT64, "Reserved2"),(DWORD, "Reserved3"),]

    

class SPECIALPROPERTIESDATA_ALTERNATE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "dwSessionId"),(LONG, "fRemoteThisSessionId"),(LONG, "fClientImpersonating"),(LONG, "fPartitionIDPresent"),(DWORD, "dwDefaultAuthnLvl"),(GUID, "guidPartition"),(DWORD, "dwPRTFlags"),(DWORD, "dwOrigClsctx"),(DWORD, "dwFlags"),(DWORD, "Reserved3"),]

    
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
class PVARIANT(NdrStructure):
    MEMBERS = []

    

class FLAGGED_WORD_BLOB(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "cBytes"),(UNSIGNED_LONG, "clSize"),(UNSIGNED_SHORT, "asData"),]

    

class CURRENCY(NdrStructure):
    MEMBERS = [(__INT64, "int64"),]

    

class DECIMAL(NdrStructure):
    MEMBERS = [(WORD, "wReserved"),(BYTE, "scale"),(BYTE, "sign"),(ULONG, "Hi32"),(ULONGLONG, "Lo64"),]

    

class WIREBRECORDSTR(NdrStructure):
    MEMBERS = [(ULONG, "fFlags"),(ULONG, "clSize"),(PMINTERFACEPOINTER, "pRecInfo"),(PBYTE, "pRecord"),]

    

class PBRECORD(NdrStructure):
    MEMBERS = []

    

class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (LONGLONG, "llVal"),2 : (LONG, "lVal"),3 : (BYTE, "bVal"),4 : (SHORT, "iVal"),5 : (FLOAT, "fltVal"),6 : (DOUBLE, "dblVal"),7 : (VARIANT_BOOL, "boolVal"),8 : (HRESULT, "scode"),9 : (CURRENCY, "cyVal"),10 : (DATE, "date"),11 : (BSTR, "bstrVal"),12 : (PIUNKNOWN, "punkVal"),13 : (PIDISPATCH, "pdispVal"),14 : (PSAFEARRAY, "parray"),15 : (BRECORD, "brecVal"),16 : (PBYTE, "pbVal"),17 : (PSHORT, "piVal"),18 : (PLONG, "plVal"),19 : (PLONGLONG, "pllVal"),20 : (PFLOAT, "pfltVal"),21 : (PDOUBLE, "pdblVal"),22 : (PVARIANT_BOOL, "pboolVal"),23 : (PHRESULT, "pscode"),24 : (PCURRENCY, "pcyVal"),25 : (PDATE, "pdate"),26 : (PBSTR, "pbstrVal"),27 : (PPIUNKNOWN, "ppunkVal"),28 : (PPIDISPATCH, "ppdispVal"),29 : (PPSAFEARRAY, "pparray"),30 : (PVARIANT, "pvarVal"),31 : (CHAR, "cVal"),32 : (USHORT, "uiVal"),33 : (ULONG, "ulVal"),34 : (ULONGLONG, "ullVal"),35 : (INT, "intVal"),36 : (UINT, "uintVal"),37 : (DECIMAL, "decVal"),38 : (PCHAR, "pcVal"),39 : (PUSHORT, "puiVal"),40 : (PULONG, "pulVal"),41 : (PULONGLONG, "pullVal"),42 : (PINT, "pintVal"),43 : (PUINT, "puintVal"),44 : (PDECIMAL, "pdecVal"),}

    

class WIREVARIANTSTR(NdrStructure):
    MEMBERS = [(DWORD, "clSize"),(DWORD, "rpcReserved"),(USHORT, "vt"),(USHORT, "wReserved1"),(USHORT, "wReserved2"),(USHORT, "wReserved3"),(_VARUNION, "_varUnion"),]

    

class SAFEARRAYBOUND(NdrStructure):
    MEMBERS = [(ULONG, "cElements"),(LONG, "lLbound"),]

    

class SAFEARR_BSTR(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PBSTR, "aBstr"),]

    

class SAFEARR_UNKNOWN(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIUNKNOWN, "apUnknown"),]

    

class SAFEARR_DISPATCH(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIDISPATCH, "apDispatch"),]

    

class SAFEARR_VARIANT(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PVARIANT, "aVariant"),]

    

class SAFEARR_BRECORD(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PBRECORD, "aRecord"),]

    

class SAFEARR_HAVEIID(NdrStructure):
    MEMBERS = [(ULONG, "Size"),(PPIUNKNOWN, "apUnknown"),(IID, "iid"),]

    

class BYTE_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PBYTE, "pData"),]

    

class WORD_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PUNSIGNED_SHORT, "pData"),]

    

class DWORD_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PUNSIGNED_LONG, "pData"),]

    

class HYPER_SIZEDARR(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "clSize"),(PHYPER, "pData"),]

    

class U(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (SAFEARR_BSTR, "BstrStr"),2 : (SAFEARR_UNKNOWN, "UnknownStr"),3 : (SAFEARR_DISPATCH, "DispatchStr"),4 : (SAFEARR_VARIANT, "VariantStr"),5 : (SAFEARR_BRECORD, "RecordStr"),6 : (SAFEARR_HAVEIID, "HaveIidStr"),7 : (BYTE_SIZEDARR, "ByteStr"),8 : (WORD_SIZEDARR, "WordStr"),9 : (DWORD_SIZEDARR, "LongStr"),10 : (HYPER_SIZEDARR, "HyperStr"),}

    

class SAFEARRAYUNION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "sfType"),(U, "u"),]

    

class PSAFEARRAY(NdrStructure):
    MEMBERS = [(USHORT, "cDims"),(USHORT, "fFeatures"),(ULONG, "cbElements"),(ULONG, "cLocks"),(SAFEARRAYUNION, "uArrayStructs"),(SAFEARRAYBOUND, "rgsabound"),]

    

class RECORDINFO(NdrStructure):
    MEMBERS = [(GUID, "libraryGuid"),(DWORD, "verMajor"),(GUID, "recGuid"),(DWORD, "verMinor"),(DWORD, "Lcid"),]

    

class DISPPARAMS(NdrStructure):
    MEMBERS = [(PVARIANT, "rgvarg"),(PDISPID, "rgdispidNamedArgs"),(UINT, "cArgs"),(UINT, "cNamedArgs"),]

    

class EXCEPINFO(NdrStructure):
    MEMBERS = [(WORD, "wCode"),(WORD, "wReserved"),(BSTR, "bstrSource"),(BSTR, "bstrDescription"),(BSTR, "bstrHelpFile"),(DWORD, "dwHelpContext"),(ULONG_PTR, "pvReserved"),(ULONG_PTR, "pfnDeferredFillIn"),(HRESULT, "scode"),]

    

class PLPTDESC(NdrStructure):
    MEMBERS = []

    

class PLPADESC(NdrStructure):
    MEMBERS = []

    

class _TDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLPTDESC, "*lptdesc"),2 : (PLPADESC, "*lpadesc"),3 : (HREFTYPE, "hreftype"),}

    

class TYPEDESC(NdrStructure):
    MEMBERS = [(_TDUNION, "_tdUnion"),(USHORT, "vt"),]

    

class ARRAYDESC(NdrStructure):
    MEMBERS = [(TYPEDESC, "tdescElem"),(USHORT, "cDims"),(SAFEARRAYBOUND, "rgbounds"),]

    

class PARAMDESCEX(NdrStructure):
    MEMBERS = [(ULONG, "cBytes"),(VARIANT, "varDefaultValue"),]

    

class PARAMDESC(NdrStructure):
    MEMBERS = [(PPARAMDESCEX, "pparamdescex"),(USHORT, "wParamFlags"),]

    

class ELEMDESC(NdrStructure):
    MEMBERS = [(TYPEDESC, "tdesc"),(PARAMDESC, "paramdesc"),]

    

class FUNCDESC(NdrStructure):
    MEMBERS = [(MEMBERID, "memid"),(PSCODE, "lReserved1"),(PELEMDESC, "lprgelemdescParam"),(FUNCKIND, "funckind"),(INVOKEKIND, "invkind"),(CALLCONV, "callconv"),(SHORT, "cParams"),(SHORT, "cParamsOpt"),(SHORT, "oVft"),(SHORT, "cReserved2"),(ELEMDESC, "elemdescFunc"),(WORD, "wFuncFlags"),]

    

class _VDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (ULONG, "oInst"),2 : (PVARIANT, "lpvarValue"),}

    

class VARDESC(NdrStructure):
    MEMBERS = [(MEMBERID, "memid"),(LPOLESTR, "lpstrReserved"),(_VDUNION, "_vdUnion"),(ELEMDESC, "elemdescVar"),(WORD, "wVarFlags"),(VARKIND, "varkind"),]

    

class TYPEATTR(NdrStructure):
    MEMBERS = [(GUID, "guid"),(LCID, "lcid"),(DWORD, "dwReserved1"),(DWORD, "dwReserved2"),(DWORD, "dwReserved3"),(LPOLESTR, "lpstrReserved4"),(ULONG, "cbSizeInstance"),(TYPEKIND, "typekind"),(WORD, "cFuncs"),(WORD, "cVars"),(WORD, "cImplTypes"),(WORD, "cbSizeVft"),(WORD, "cbAlignment"),(WORD, "wTypeFlags"),(WORD, "wMajorVerNum"),(WORD, "wMinorVerNum"),(TYPEDESC, "tdescAlias"),(DWORD, "dwReserved5"),(WORD, "wReserved6"),]

    

class TLIBATTR(NdrStructure):
    MEMBERS = [(GUID, "guid"),(LCID, "lcid"),(SYSKIND, "syskind"),(UNSIGNED_SHORT, "wMajorVerNum"),(UNSIGNED_SHORT, "wMinorVerNum"),(UNSIGNED_SHORT, "wLibFlags"),]

    

class CUSTDATAITEM(NdrStructure):
    MEMBERS = [(GUID, "guid"),(VARIANT, "varValue"),]

    

class CUSTDATA(NdrStructure):
    MEMBERS = [(DWORD, "cCustData"),(PCUSTDATAITEM, "prgCustData"),]

    
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
class IN6_ADDR(NdrStructure):
    MEMBERS = [(U, "u"),]

    

class DIM_INFORMATION_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "dwBufferSize"),(LPBYTE, "pBuffer"),]

    

class MPRAPI_OBJECT_HEADER_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(UCHAR, "type"),(USHORT, "size"),]

    

class PPP_PROJECTION_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwIPv4Options"),(DWORD, "dwIPv4RemoteOptions"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwLcpError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwLcpTerminateReason"),(DWORD, "dwLcpRemoteTerminateReason"),(DWORD, "dwLcpOptions"),(DWORD, "dwLcpRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwRemoteEapTypeId"),(DWORD, "dwCcpError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwCcpOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwCcpRemoteOptions"),]

    

class PPP_PROJECTION_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwIPv4Options"),(DWORD, "dwIPv4RemoteOptions"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwLcpError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwLcpTerminateReason"),(DWORD, "dwLcpRemoteTerminateReason"),(DWORD, "dwLcpOptions"),(DWORD, "dwLcpRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwEmbeddedEAPTypeId"),(DWORD, "dwRemoteEapTypeId"),(DWORD, "dwCcpError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwCcpOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwCcpRemoteOptions"),]

    

class IKEV2_PROJECTION_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwOptions"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwEapTypeId"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwEncryptionMethod"),]

    

class IKEV2_PROJECTION_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIPv4NegotiationError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(ULONG64, "IPv4SubInterfaceIndex"),(DWORD, "dwIPv6NegotiationError"),(UCHAR, "bInterfaceIdentifier"),(UCHAR, "bRemoteInterfaceIdentifier"),(UCHAR, "bPrefix"),(DWORD, "dwPrefixLength"),(ULONG64, "IPv6SubInterfaceIndex"),(DWORD, "dwOptions"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwEapTypeId"),(DWORD, "dwEmbeddedEAPTypeId"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwEncryptionMethod"),]

    

class PROJECTION_INFO_IDL_1(NdrStructure):
    MEMBERS = [(UCHAR, "projectionInfoType"),(ANONYMOUS22, "ProjectionInfoObject"),]

    

class PPPROJECTION_INFO_IDL_1(NdrStructure):
    MEMBERS = []

    

class PROJECTION_INFO_IDL_2(NdrStructure):
    MEMBERS = [(UCHAR, "projectionInfoType"),(ANONYMOUS23, "ProjectionInfoObject"),]

    

class RAS_CONNECTION_EX_1_IDL(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),(GUID, "guid"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "probationTime"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),(DWORD, "dwNumSwitchOvers"),(WCHAR, "wszRemoteEndpointAddress"),(WCHAR, "wszLocalEndpointAddress"),(PROJECTION_INFO_IDL_1, "ProjectionInfo"),(ULONG, "hConnection"),(ULONG, "hInterface"),]

    

class RAS_CONNECTION_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS24, "ConnObject"),]

    

class PPRAS_CONNECTION_EX_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_CONNECTION_4_IDL(NdrStructure):
    MEMBERS = [(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),(GUID, "guid"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "probationTime"),(FILETIME, "connectionStartTime"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),(DWORD, "dwNumSwitchOvers"),(WCHAR, "wszRemoteEndpointAddress"),(WCHAR, "wszLocalEndpointAddress"),(PROJECTION_INFO_IDL_2, "ProjectionInfo"),(ULONG, "hConnection"),(ULONG, "hInterface"),(DWORD, "dwDeviceType"),]

    

class CERT_BLOB_1(NdrStructure):
    MEMBERS = [(DWORD, "cbData"),(PBYTE, "pbData"),]

    

class CERT_EKU_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(BOOL, "IsEKUOID"),(PWCHAR, "pwszEKU"),]

    

class IKEV2_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),]

    

class ROUTER_CUSTOM_IKEV2_POLICY_0(NdrStructure):
    MEMBERS = [(DWORD, "dwIntegrityMethod"),(DWORD, "dwEncryptionMethod"),(DWORD, "dwCipherTransformConstant"),(DWORD, "dwAuthTransformConstant"),(DWORD, "dwPfsGroup"),(DWORD, "dwDhGroup"),]

    

class ROUTER_IKEV2_IF_CUSTOM_CONFIG_0(NdrStructure):
    MEMBERS = [(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSize"),(CERT_BLOB_1, "certificateName"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),]

    

class ROUTER_IKEV2_IF_CUSTOM_CONFIG_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSize"),(CERT_BLOB_1, "certificateName"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),(CERT_BLOB_1, "certificateHash"),]

    

class MPR_IF_CUSTOMINFOEX_0(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwFlags"),(ROUTER_IKEV2_IF_CUSTOM_CONFIG_0, "customIkev2Config"),]

    

class MPR_IF_CUSTOMINFOEX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwFlags"),(ROUTER_IKEV2_IF_CUSTOM_CONFIG_1, "customIkev2Config"),]

    

class MPR_IF_CUSTOMINFOEX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS25, "IfCustomConfigObject"),]

    

class IKEV2_TUNNEL_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),(CERT_BLOB_1, "machineCertificateName"),(DWORD, "dwEncryptionType"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),]

    

class IKEV2_TUNNEL_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwNetworkBlackoutTime"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(DWORD, "dwConfigOptions"),(DWORD, "dwTotalCertificates"),(PCERT_BLOB_1, "certificateNames"),(CERT_BLOB_1, "machineCertificateName"),(DWORD, "dwEncryptionType"),(PROUTER_CUSTOM_IKEV2_POLICY_0, "customPolicy"),(DWORD, "dwTotalEkus"),(PCERT_EKU_1, "certificateEKUs"),(CERT_BLOB_1, "machineCertificateHash"),]

    

class L2TP_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwIdleTimeout"),(DWORD, "dwEncryptionType"),(DWORD, "dwSaLifeTime"),(DWORD, "dwSaDataSizeForRenegotiation"),(PROUTER_CUSTOM_L2TP_POLICY_0, "customPolicy"),]

    

class IKEV2_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_1, "TunnelConfigParams"),]

    

class IKEV2_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_2, "TunnelConfigParams"),]

    

class IKEV2_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(IKEV2_TUNNEL_CONFIG_PARAMS_3, "TunnelConfigParams"),]

    

class PPTP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),]

    

class L2TP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),]

    

class L2TP_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(DWORD, "dwTunnelConfigParamFlags"),(L2TP_TUNNEL_CONFIG_PARAMS_1, "TunnelConfigParams"),]

    

class SSTP_CERT_INFO_1(NdrStructure):
    MEMBERS = [(BOOL, "isDefault"),(CERT_BLOB_1, "certBlob"),]

    

class SSTP_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPorts"),(DWORD, "dwPortFlags"),(BOOL, "isUseHttps"),(DWORD, "certAlgorithm"),(SSTP_CERT_INFO_1, "sstpCertDetails"),]

    

class MPRAPI_TUNNEL_CONFIG_PARAMS_1(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_1, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_1, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    

class MPRAPI_TUNNEL_CONFIG_PARAMS_2(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_2, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_1, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    

class MPRAPI_TUNNEL_CONFIG_PARAMS_3(NdrStructure):
    MEMBERS = [(IKEV2_CONFIG_PARAMS_3, "IkeConfigParams"),(PPTP_CONFIG_PARAMS_1, "PptpConfigParams"),(L2TP_CONFIG_PARAMS_2, "L2tpConfigParams"),(SSTP_CONFIG_PARAMS_1, "SstpConfigParams"),]

    

class MPR_SERVER_EX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_1, "ConfigParams"),]

    

class MPR_SERVER_EX_2(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_2, "ConfigParams"),]

    

class MPR_SERVER_EX_3(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),(DWORD, "Reserved"),(MPRAPI_TUNNEL_CONFIG_PARAMS_3, "ConfigParams"),]

    

class MPR_SERVER_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS26, "ServerConfigObject"),]

    

class PPMPR_SERVER_EX_IDL(NdrStructure):
    MEMBERS = []

    

class MPR_SERVER_SET_CONFIG_EX_1(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_1, "ConfigParams"),]

    

class MPR_SERVER_SET_CONFIG_EX_2(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_2, "ConfigParams"),]

    

class MPR_SERVER_SET_CONFIG_EX_3(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "setConfigForProtocols"),(MPRAPI_TUNNEL_CONFIG_PARAMS_3, "ConfigParams"),]

    

class MPR_SERVER_SET_CONFIG_EX_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS27, "ServerSetConfigObject"),]

    

class PPMPR_SERVER_SET_CONFIG_EX_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_UPDATE_CONNECTION_1_IDL(NdrStructure):
    MEMBERS = [(MPRAPI_OBJECT_HEADER_IDL, "Header"),(DWORD, "dwIfIndex"),(WCHAR, "wszRemoteEndpointAddress"),]

    

class PPRAS_UPDATE_CONNECTION_1_IDL(NdrStructure):
    MEMBERS = []

    

class RAS_UPDATE_CONNECTION_IDL(NdrStructure):
    MEMBERS = [(UCHAR, "revision"),(ANONYMOUS28, "UpdateConnection"),]

    

class PPRAS_UPDATE_CONNECTION_IDL(NdrStructure):
    MEMBERS = []

    

class DIM_INTERFACE_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "fGetInterfaceInfo"),(DWORD, "dwInterfaceInfoSize"),(LPBYTE, "pInterfaceInfo"),(DWORD, "fGetGlobalInfo"),(DWORD, "dwGlobalInfoSize"),(LPBYTE, "pGlobalInfo"),]

    

class RTR_TOC_ENTRY(NdrStructure):
    MEMBERS = [(ULONG, "InfoType"),(ULONG, "InfoSize"),(ULONG, "Count"),(ULONG, "Offset"),]

    

class RTR_INFO_BLOCK_HEADER(NdrStructure):
    MEMBERS = [(ULONG, "Version"),(ULONG, "Size"),(ULONG, "TocEntriesCount"),(RTR_TOC_ENTRY, "TocEntry"),]

    

class FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwSrcAddr"),(DWORD, "dwSrcMask"),(DWORD, "dwDstAddr"),(DWORD, "dwDstMask"),(DWORD, "dwProtocol"),(DWORD, "fLateBound"),(WORD, "wSrcPort"),(WORD, "wDstPort"),]

    

class FILTER_DESCRIPTOR(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwNumFilters"),(FORWARD_ACTION, "faDefaultAction"),(FILTER_INFO, "fiFilter"),]

    

class FILTER_INFO_V6(NdrStructure):
    MEMBERS = [(BYTE, "ipv6SrcAddr"),(DWORD, "dwSrcPrefixLength"),(BYTE, "ipv6DstAddr"),(DWORD, "dwDstPrefixLength"),(DWORD, "dwProtocol"),(DWORD, "fLateBound"),(WORD, "wSrcPort"),(WORD, "wDstPort"),]

    

class FILTER_DESCRIPTOR_V6(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwNumFilters"),(FORWARD_ACTION, "faDefaultAction"),(FILTER_INFO_V6, "fiFilter"),]

    

class GLOBAL_INFO(NdrStructure):
    MEMBERS = [(BOOL, "bFilteringOn"),(DWORD, "dwLoggingLevel"),]

    

class INTERFACE_ROUTE_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwRtInfoIfIndex"),(DWORD, "dwRtInfoType"),(DWORD, "dwRtInfoProto"),(DWORD, "dwRtInfoPreference"),(DWORD, "dwRtInfoViewSet"),(BOOL, "bV4"),]

    

class PROTOCOL_METRIC(NdrStructure):
    MEMBERS = [(DWORD, "dwProtocolId"),(DWORD, "dwMetric"),]

    

class PRIORITY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwNumProtocols"),(PROTOCOL_METRIC, "ppmProtocolMetric"),]

    

class PROTOCOL_METRIC_EX(NdrStructure):
    MEMBERS = [(DWORD, "dwProtocolId"),(DWORD, "dwSubProtocolId"),(DWORD, "dwMetric"),]

    

class PRIORITY_INFO_EX(NdrStructure):
    MEMBERS = [(DWORD, "dwNumProtocols"),(PROTOCOL_METRIC_EX, "ppmProtocolMetric"),]

    

class RTR_DISC_INFO(NdrStructure):
    MEMBERS = [(WORD, "wMaxAdvtInterval"),(WORD, "wMinAdvtInterval"),(WORD, "wAdvtLifetime"),(BOOL, "bAdvertise"),(LONG, "lPrefLevel"),]

    

class MCAST_HBEAT_INFO(NdrStructure):
    MEMBERS = [(WCHAR, "pwszGroup"),(BOOL, "bActive"),(ULONG, "ulDeadInterval"),(BYTE, "byProtocol"),(WORD, "wPort"),]

    

class MIB_MCAST_LIMIT_ROW(NdrStructure):
    MEMBERS = [(DWORD, "dwTtl"),(DWORD, "dwRateLimit"),]

    

class IPINIP_CONFIG_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwRemoteAddress"),(DWORD, "dwLocalAddress"),(BYTE, "byTtl"),]

    

class INTERFACE_STATUS_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwAdminStatus"),]

    

class DIM_MIB_ENTRY_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "dwMibInEntrySize"),(LPBYTE, "pMibInEntry"),(DWORD, "dwMibOutEntrySize"),(LPBYTE, "pMibOutEntry"),]

    

class MIB_IPFORWARDROW(NdrStructure):
    MEMBERS = [(DWORD, "dwForwardDest"),(DWORD, "dwForwardMask"),(DWORD, "dwForwardPolicy"),(DWORD, "dwForwardNextHop"),(DWORD, "dwForwardIfIndex"),(U0, "u0"),(U1, "u1"),(DWORD, "dwForwardAge"),(DWORD, "dwForwardNextHopAS"),(DWORD, "dwForwardMetric1"),(DWORD, "dwForwardMetric2"),(DWORD, "dwForwardMetric3"),(DWORD, "dwForwardMetric4"),(DWORD, "dwForwardMetric5"),]

    

class MIB_IPDESTROW(NdrStructure):
    MEMBERS = [(MIB_IPFORWARDROW, "ForwardRow"),(DWORD, "dwForwardPreference"),(DWORD, "dwForwardViewSet"),]

    

class MIB_IPDESTTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPDESTROW, "table"),]

    

class MIB_ROUTESTATE(NdrStructure):
    MEMBERS = [(BOOL, "bRoutesSetToStack"),]

    

class MIB_BEST_IF(NdrStructure):
    MEMBERS = [(DWORD, "dwDestAddr"),(DWORD, "dwIfIndex"),]

    

class MIB_BOUNDARYROW(NdrStructure):
    MEMBERS = [(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),]

    

class MIBICMPSTATS(NdrStructure):
    MEMBERS = [(DWORD, "dwMsgs"),(DWORD, "dwErrors"),(DWORD, "dwDestUnreachs"),(DWORD, "dwTimeExcds"),(DWORD, "dwParmProbs"),(DWORD, "dwSrcQuenchs"),(DWORD, "dwRedirects"),(DWORD, "dwEchos"),(DWORD, "dwEchoReps"),(DWORD, "dwTimestamps"),(DWORD, "dwTimestampReps"),(DWORD, "dwAddrMasks"),(DWORD, "dwAddrMaskReps"),]

    

class MIBICMPINFO(NdrStructure):
    MEMBERS = [(MIBICMPSTATS, "icmpInStats"),(MIBICMPSTATS, "icmpOutStats"),]

    

class MIB_ICMP(NdrStructure):
    MEMBERS = [(MIBICMPINFO, "stats"),]

    

class MIB_IFNUMBER(NdrStructure):
    MEMBERS = [(DWORD, "dwValue"),]

    

class MIB_IFROW(NdrStructure):
    MEMBERS = [(WCHAR, "wszName"),(DWORD, "dwIndex"),(DWORD, "dwType"),(DWORD, "dwMtu"),(DWORD, "dwSpeed"),(DWORD, "dwPhysAddrLen"),(BYTE, "bPhysAddr"),(DWORD, "dwAdminStatus"),(DWORD, "dwOperStatus"),(DWORD, "dwLastChange"),(DWORD, "dwInOctets"),(DWORD, "dwInUcastPkts"),(DWORD, "dwInNUcastPkts"),(DWORD, "dwInDiscards"),(DWORD, "dwInErrors"),(DWORD, "dwInUnknownProtos"),(DWORD, "dwOutOctets"),(DWORD, "dwOutUcastPkts"),(DWORD, "dwOutNUcastPkts"),(DWORD, "dwOutDiscards"),(DWORD, "dwOutErrors"),(DWORD, "dwOutQLen"),(DWORD, "dwDescrLen"),(BYTE, "bDescr"),]

    

class MIB_IFSTATUS(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwAdminStatus"),(DWORD, "dwOperationalStatus"),(BOOL, "bMHbeatActive"),(BOOL, "bMHbeatAlive"),]

    

class MIB_IFTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IFROW, "table"),]

    

class MIB_IPADDRROW(NdrStructure):
    MEMBERS = [(DWORD, "dwAddr"),(DWORD, "dwIndex"),(DWORD, "dwMask"),(DWORD, "dwBCastAddr"),(DWORD, "dwReasmSize"),(UNSIGNED_SHORT, "unused1"),(UNSIGNED_SHORT, "wType"),]

    

class MIB_IPADDRTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPADDRROW, "table"),]

    

class MIB_IPFORWARDNUMBER(NdrStructure):
    MEMBERS = [(DWORD, "dwValue"),]

    

class MIB_IPFORWARDTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPFORWARDROW, "table"),(BYTE, "reserved"),]

    

class MIB_IPMCAST_BOUNDARY(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),(DWORD, "dwStatus"),]

    

class MIB_IPMCAST_BOUNDARY_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_BOUNDARY, "table"),]

    

class MIB_IPMCAST_GLOBAL(NdrStructure):
    MEMBERS = [(DWORD, "dwEnable"),]

    

class MIB_IPMCAST_IF_ENTRY(NdrStructure):
    MEMBERS = [(DWORD, "dwIfIndex"),(DWORD, "dwTtl"),(DWORD, "dwProtocol"),(DWORD, "dwRateLimit"),(ULONG, "ulInMcastOctets"),(ULONG, "ulOutMcastOctets"),]

    

class MIB_IPMCAST_IF_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_IF_ENTRY, "table"),]

    

class MIB_IPMCAST_OIF(NdrStructure):
    MEMBERS = [(DWORD, "dwOutIfIndex"),(DWORD, "dwNextHopAddr"),(PVOID, "pvReserved"),(DWORD, "dwReserved"),]

    

class MIB_IPMCAST_MFE(NdrStructure):
    MEMBERS = [(DWORD, "dwGroup"),(DWORD, "dwSource"),(DWORD, "dwSrcMask"),(DWORD, "dwUpStrmNgbr"),(DWORD, "dwInIfIndex"),(DWORD, "dwInIfProtocol"),(DWORD, "dwRouteProtocol"),(DWORD, "dwRouteNetwork"),(DWORD, "dwRouteMask"),(ULONG, "ulUpTime"),(ULONG, "ulExpiryTime"),(ULONG, "ulTimeOut"),(ULONG, "ulNumOutIf"),(DWORD, "fFlags"),(DWORD, "dwReserved"),(MIB_IPMCAST_OIF, "rgmioOutInfo"),]

    

class MIB_IPMCAST_OIF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "dwOutIfIndex"),(DWORD, "dwNextHopAddr"),(PVOID, "pvDialContext"),(ULONG, "ulTtlTooLow"),(ULONG, "ulFragNeeded"),(ULONG, "ulOutPackets"),(ULONG, "ulOutDiscards"),]

    

class MIB_IPMCAST_MFE_STATS(NdrStructure):
    MEMBERS = [(DWORD, "dwGroup"),(DWORD, "dwSource"),(DWORD, "dwSrcMask"),(DWORD, "dwUpStrmNgbr"),(DWORD, "dwInIfIndex"),(DWORD, "dwInIfProtocol"),(DWORD, "dwRouteProtocol"),(DWORD, "dwRouteNetwork"),(DWORD, "dwRouteMask"),(ULONG, "ulUpTime"),(ULONG, "ulExpiryTime"),(ULONG, "ulNumOutIf"),(ULONG, "ulInPkts"),(ULONG, "ulInOctets"),(ULONG, "ulPktsDifferentIf"),(ULONG, "ulQueueOverflow"),(MIB_IPMCAST_OIF_STATS, "rgmiosOutStats"),]

    

class MIB_IPMCAST_SCOPE(NdrStructure):
    MEMBERS = [(DWORD, "dwGroupAddress"),(DWORD, "dwGroupMask"),(WCHAR, "snNameBuffer"),(DWORD, "dwStatus"),(BYTE, "reserved"),]

    

class MIB_IPNETROW(NdrStructure):
    MEMBERS = [(DWORD, "dwIndex"),(DWORD, "dwPhysAddrLen"),(BYTE, "bPhysAddr"),(DWORD, "dwAddr"),(DWORD, "dwType"),]

    

class MIB_IPNETTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPNETROW, "table"),(BYTE, "reserved"),]

    

class MIB_IPSTATS(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwDefaultTTL"),(DWORD, "dwInReceives"),(DWORD, "dwInHdrErrors"),(DWORD, "dwInAddrErrors"),(DWORD, "dwForwDatagrams"),(DWORD, "dwInUnknownProtos"),(DWORD, "dwInDiscards"),(DWORD, "dwInDelivers"),(DWORD, "dwOutRequests"),(DWORD, "dwRoutingDiscards"),(DWORD, "dwOutDiscards"),(DWORD, "dwOutNoRoutes"),(DWORD, "dwReasmTimeout"),(DWORD, "dwReasmReqds"),(DWORD, "dwReasmOks"),(DWORD, "dwReasmFails"),(DWORD, "dwFragOks"),(DWORD, "dwFragFails"),(DWORD, "dwFragCreates"),(DWORD, "dwNumIf"),(DWORD, "dwNumAddr"),(DWORD, "dwNumRoutes"),]

    

class MIB_MFE_STATS_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_MFE_STATS, "table"),]

    

class MIB_MFE_TABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_IPMCAST_MFE, "table"),]

    

class MIB_OPAQUE_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwId"),(U0, "u0"),]

    

class MIB_OPAQUE_QUERY(NdrStructure):
    MEMBERS = [(DWORD, "dwVarId"),(DWORD, "rgdwVarIndex"),]

    

class MIB_PROXYARP(NdrStructure):
    MEMBERS = [(DWORD, "dwAddress"),(DWORD, "dwMask"),(DWORD, "dwIfIndex"),]

    

class MIB_TCPROW(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwLocalAddr"),(DWORD, "dwLocalPort"),(DWORD, "dwRemoteAddr"),(DWORD, "dwRemotePort"),]

    

class MIB_TCPSTATS(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "dwRtoMin"),(DWORD, "dwRtoMax"),(DWORD, "dwMaxConn"),(DWORD, "dwActiveOpens"),(DWORD, "dwPassiveOpens"),(DWORD, "dwAttemptFails"),(DWORD, "dwEstabResets"),(DWORD, "dwCurrEstab"),(DWORD, "dwInSegs"),(DWORD, "dwOutSegs"),(DWORD, "dwRetransSegs"),(DWORD, "dwInErrs"),(DWORD, "dwOutRsts"),(DWORD, "dwNumConns"),]

    

class MIB_TCPTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_TCPROW, "table"),(BYTE, "reserved"),]

    

class MIB_UDPROW(NdrStructure):
    MEMBERS = [(DWORD, "dwLocalAddr"),(DWORD, "dwLocalPort"),]

    

class MIB_UDPSTATS(NdrStructure):
    MEMBERS = [(DWORD, "dwInDatagrams"),(DWORD, "dwNoPorts"),(DWORD, "dwInErrors"),(DWORD, "dwOutDatagrams"),(DWORD, "dwNumAddrs"),]

    

class MIB_UDPTABLE(NdrStructure):
    MEMBERS = [(DWORD, "dwNumEntries"),(MIB_UDPROW, "table"),(BYTE, "reserved"),]

    

class MPR_SERVER_0(NdrStructure):
    MEMBERS = [(BOOL, "fLanOnlyMode"),(DWORD, "dwUpTime"),(DWORD, "dwTotalPorts"),(DWORD, "dwPortsInUse"),]

    

class MPR_SERVER_1(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPptpPorts"),(DWORD, "dwPptpPortFlags"),(DWORD, "dwNumL2tpPorts"),(DWORD, "dwL2tpPortFlags"),]

    

class MPR_SERVER_2(NdrStructure):
    MEMBERS = [(DWORD, "dwNumPptpPorts"),(DWORD, "dwPptpPortFlags"),(DWORD, "dwNumL2tpPorts"),(DWORD, "dwL2tpPortFlags"),(DWORD, "dwNumSstpPorts"),(DWORD, "dwSstpPortFlags"),]

    

class PPP_NBFCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszWksta"),]

    

class PPP_IPCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),]

    

class PPP_IPCP_INFO2(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),(WCHAR, "wszRemoteAddress"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptons"),]

    

class PPP_IPXCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),]

    

class PPP_IPV6_CP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "dwError"),(BYTE, "bInterfaceIdentifier"),(BYTE, "bRemoteInterfaceIdentifier"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptions"),(BYTE, "bPrefix"),(DWORD, "dwPrefixLength"),]

    

class PPP_ATCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(WCHAR, "wszAddress"),]

    

class PPP_CCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(DWORD, "dwCompressionAlgorithm"),(DWORD, "dwOptions"),(DWORD, "dwRemoteCompressionAlgorithm"),(DWORD, "dwRemoteOptions"),]

    

class PPP_LCP_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwError"),(DWORD, "dwAuthenticationProtocol"),(DWORD, "dwAuthenticationData"),(DWORD, "dwRemoteAuthenticationProtocol"),(DWORD, "dwRemoteAuthenticationData"),(DWORD, "dwTerminateReason"),(DWORD, "dwRemoteTerminateReason"),(DWORD, "dwOptions"),(DWORD, "dwRemoteOptions"),(DWORD, "dwEapTypeId"),(DWORD, "dwRemoteEapTypeId"),]

    

class PPP_INFO(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO, "ip"),(PPP_IPXCP_INFO, "ipx"),(PPP_ATCP_INFO, "at"),]

    

class PPP_INFO_2(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO2, "ip"),(PPP_IPXCP_INFO, "ipx"),(PPP_ATCP_INFO, "at"),(PPP_CCP_INFO, "ccp"),(PPP_LCP_INFO, "lcp"),]

    

class PPP_INFO_3(NdrStructure):
    MEMBERS = [(PPP_NBFCP_INFO, "nbf"),(PPP_IPCP_INFO2, "ip"),(PPP_IPV6_CP_INFO, "ipv6"),(PPP_CCP_INFO, "ccp"),(PPP_LCP_INFO, "lcp"),]

    

class RASI_PORT_0(NdrStructure):
    MEMBERS = [(DWORD, "dwPort"),(DWORD, "dwConnection"),(RAS_PORT_CONDITION, "dwPortCondition"),(DWORD, "dwTotalNumberOfCalls"),(DWORD, "dwConnectDuration"),(WCHAR, "wszPortName"),(WCHAR, "wszMediaName"),(WCHAR, "wszDeviceName"),(WCHAR, "wszDeviceType"),]

    

class RASI_PORT_1(NdrStructure):
    MEMBERS = [(DWORD, "dwPort"),(DWORD, "dwConnection"),(RAS_HARDWARE_CONDITION, "dwHardwareCondition"),(DWORD, "dwLineSpeed"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),]

    

class RASI_CONNECTION_0(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(DWORD, "dwInterface"),(DWORD, "dwConnectDuration"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(DWORD, "dwConnectionFlags"),(WCHAR, "wszInterfaceName"),(WCHAR, "wszUserName"),(WCHAR, "wszLogonDomain"),(WCHAR, "wszRemoteComputer"),]

    

class RASI_CONNECTION_1(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(DWORD, "dwInterface"),(PPP_INFO, "PppInfo"),(DWORD, "dwBytesXmited"),(DWORD, "dwBytesRcved"),(DWORD, "dwFramesXmited"),(DWORD, "dwFramesRcved"),(DWORD, "dwCrcErr"),(DWORD, "dwTimeoutErr"),(DWORD, "dwAlignmentErr"),(DWORD, "dwHardwareOverrunErr"),(DWORD, "dwFramingErr"),(DWORD, "dwBufferOverrunErr"),(DWORD, "dwCompressionRatioIn"),(DWORD, "dwCompressionRatioOut"),]

    

class RASI_CONNECTION_2(NdrStructure):
    MEMBERS = [(DWORD, "dwConnection"),(WCHAR, "wszUserName"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(GUID, "guid"),(PPP_INFO_2, "PppInfo2"),]

    

class RASI_CONNECTION_3(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "dwConnection"),(WCHAR, "wszUserName"),(ROUTER_INTERFACE_TYPE, "dwInterfaceType"),(GUID, "guid"),(PPP_INFO_3, "PppInfo3"),(RAS_QUARANTINE_STATE, "rasQuarState"),(FILETIME, "timer"),]

    

class MPRI_INTERFACE_0(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),]

    

class MPRI_INTERFACE_1(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(LPWSTR, "lpwsDialoutHoursRestriction"),]

    

class MPRI_INTERFACE_2(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(DWORD, "dwfOptions"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),(DWORD, "ipaddr"),(DWORD, "ipaddrDns"),(DWORD, "ipaddrDnsAlt"),(DWORD, "ipaddrWins"),(DWORD, "ipaddrWinsAlt"),(DWORD, "dwfNetProtocols"),(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szX25PadType"),(WCHAR, "szX25Address"),(WCHAR, "szX25Facilities"),(WCHAR, "szX25UserData"),(DWORD, "dwChannels"),(DWORD, "dwSubEntries"),(DWORD, "dwDialMode"),(DWORD, "dwDialExtraPercent"),(DWORD, "dwDialExtraSampleSeconds"),(DWORD, "dwHangUpExtraPercent"),(DWORD, "dwHangUpExtraSampleSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(DWORD, "dwType"),(DWORD, "dwEncryptionType"),(DWORD, "dwCustomAuthKey"),(DWORD, "dwCustomAuthDataSize"),(LPBYTE, "lpbCustomAuthData"),(GUID, "guidId"),(DWORD, "dwVpnStrategy"),]

    

class MPRI_INTERFACE_3(NdrStructure):
    MEMBERS = [(WCHAR, "wszInterfaceName"),(DWORD, "dwInterface"),(BOOL, "fEnabled"),(ROUTER_INTERFACE_TYPE, "dwIfType"),(ROUTER_CONNECTION_STATE, "dwConnectionState"),(DWORD, "fUnReachabilityReasons"),(DWORD, "dwLastError"),(DWORD, "dwfOptions"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),(DWORD, "ipaddr"),(DWORD, "ipaddrDns"),(DWORD, "ipaddrDnsAlt"),(DWORD, "ipaddrWins"),(DWORD, "ipaddrWinsAlt"),(DWORD, "dwfNetProtocols"),(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szX25PadType"),(WCHAR, "szX25Address"),(WCHAR, "szX25Facilities"),(WCHAR, "szX25UserData"),(DWORD, "dwChannels"),(DWORD, "dwSubEntries"),(DWORD, "dwDialMode"),(DWORD, "dwDialExtraPercent"),(DWORD, "dwDialExtraSampleSeconds"),(DWORD, "dwHangUpExtraPercent"),(DWORD, "dwHangUpExtraSampleSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(DWORD, "dwType"),(DWORD, "dwEncryptionType"),(DWORD, "dwCustomAuthKey"),(DWORD, "dwCustomAuthDataSize"),(LPBYTE, "lpbCustomAuthData"),(GUID, "guidId"),(DWORD, "dwVpnStrategy"),(ULONG, "AddressCount"),(IN6_ADDR, "ipv6addrDns"),(IN6_ADDR, "ipv6addrDnsAlt"),(PIN6_ADDR, "ipv6addr"),]

    

class MPR_DEVICE_0(NdrStructure):
    MEMBERS = [(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),]

    

class MPR_DEVICE_1(NdrStructure):
    MEMBERS = [(WCHAR, "szDeviceType"),(WCHAR, "szDeviceName"),(WCHAR, "szLocalPhoneNumber"),(PWCHAR, "szAlternates"),]

    

class MPR_CREDENTIALSEX_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(DWORD, "dwOffset"),(BYTE, "bData"),]

    

class IFFILTER_INFO(NdrStructure):
    MEMBERS = [(BOOL, "bEnableFragChk"),]

    

class MPR_FILTER_0(NdrStructure):
    MEMBERS = [(BOOL, "fEnable"),]

    

class IPX_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "RoutingTableHashSize"),(ULONG, "EventLogMask"),]

    

class IPX_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdministratorState"),(ULONG, "NetbiosAccept"),(ULONG, "NetbiosDeliver"),]

    

class IPXWAN_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Adminstate"),]

    

class IPX_STATIC_ROUTE_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(USHORT, "TickCount"),(USHORT, "HopCount"),(UCHAR, "NextHopMacAddress"),]

    

class IPX_SERVER_ENTRY(NdrStructure):
    MEMBERS = [(USHORT, "Type"),(UCHAR, "Name"),(UCHAR, "Network"),(UCHAR, "Node"),(UCHAR, "Socket"),(USHORT, "HopCount"),]

    

class IPX_STATIC_NETBIOS_NAME_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),]

    

class IPX_ADAPTER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "PacketType"),(WCHAR, "AdapterName"),]

    

class IPX_TRAFFIC_FILTER_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "FilterAction"),]

    

class IPX_TRAFFIC_FILTER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "FilterDefinition"),(UCHAR, "DestinationNetwork"),(UCHAR, "DestinationNetworkMask"),(UCHAR, "DestinationNode"),(UCHAR, "DestinationSocket"),(UCHAR, "SourceNetwork"),(UCHAR, "SourceNetworkMask"),(UCHAR, "SourceNode"),(UCHAR, "SourceSocket"),(UCHAR, "PacketType"),]

    

class IF_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),]

    

class ROUTING_TABLE_INDEX(NdrStructure):
    MEMBERS = [(UCHAR, "Network"),]

    

class STATIC_ROUTES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(UCHAR, "Network"),]

    

class SERVICES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(USHORT, "ServiceType"),(UCHAR, "ServiceName"),]

    

class STATIC_SERVICES_TABLE_INDEX(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(USHORT, "ServiceType"),(UCHAR, "ServiceName"),]

    

class IPX_MIB_INDEX(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (IF_TABLE_INDEX, "InterfaceTableIndex"),2 : (ROUTING_TABLE_INDEX, "RoutingTableIndex"),3 : (STATIC_ROUTES_TABLE_INDEX, "StaticRoutesTableIndex"),4 : (SERVICES_TABLE_INDEX, "ServicesTableIndex"),5 : (STATIC_SERVICES_TABLE_INDEX, "StaticServicesTableIndex"),}

    

class IPX_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(IPX_MIB_INDEX, "MibIndex"),]

    

class IPXMIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "OperState"),(UCHAR, "PrimaryNetNumber"),(UCHAR, "Node"),(UCHAR, "SysName"),(ULONG, "MaxPathSplits"),(ULONG, "IfCount"),(ULONG, "DestCount"),(ULONG, "ServCount"),]

    

class IPX_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "IfOperState"),(ULONG, "MaxPacketSize"),(ULONG, "InHdrErrors"),(ULONG, "InFiltered"),(ULONG, "InNoRoutes"),(ULONG, "InDiscards"),(ULONG, "InDelivers"),(ULONG, "OutFiltered"),(ULONG, "OutDiscards"),(ULONG, "OutDelivers"),(ULONG, "NetbiosReceived"),(ULONG, "NetbiosSent"),]

    

class IPX_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "AdministratorState"),(ULONG, "AdapterIndex"),(UCHAR, "InterfaceName"),(ULONG, "InterfaceType"),(ULONG, "MediaType"),(UCHAR, "NetNumber"),(UCHAR, "MacAddress"),(ULONG, "Delay"),(ULONG, "Throughput"),(ULONG, "NetbiosAccept"),(ULONG, "NetbiosDeliver"),(ULONG, "EnableIpxWanNegotiation"),(IPX_IF_STATS, "IfStats"),]

    

class IPX_ROUTE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "Protocol"),(UCHAR, "Network"),(USHORT, "TickCount"),(USHORT, "HopCount"),(UCHAR, "NextHopMacAddress"),(ULONG, "Flags"),]

    

class IPX_SERVICE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(ULONG, "Protocol"),(IPX_SERVER_ENTRY, "Server"),]

    

class IPX_MIB_ROW(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (IPX_INTERFACE, "Interface"),2 : (IPX_ROUTE, "Route"),3 : (IPX_SERVICE, "Service"),}

    

class IPX_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(IPX_MIB_ROW, "MibRow"),]

    

class SAP_SERVICE_FILTER_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(UCHAR, "ServiceName"),]

    

class SAP_IF_FILTERS(NdrStructure):
    MEMBERS = [(ULONG, "SupplyFilterAction"),(ULONG, "SupplyFilterCount"),(ULONG, "ListenFilterAction"),(ULONG, "ListenFilterCount"),(SAP_SERVICE_FILTER_INFO, "ServiceFilter"),]

    

class SAP_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdminState"),(ULONG, "UpdateMode"),(ULONG, "PacketType"),(ULONG, "Supply"),(ULONG, "Listen"),(ULONG, "GetNearestServerReply"),(ULONG, "PeriodicUpdateInterval"),(ULONG, "AgeIntervalMultiplier"),]

    

class SAP_IF_CONFIG(NdrStructure):
    MEMBERS = [(SAP_IF_INFO, "SapIfInfo"),(SAP_IF_FILTERS, "SapIfFilters"),]

    

class SAP_MIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "SapOperState"),]

    

class SAP_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "SapIfOperState"),(ULONG, "SapIfInputPackets"),(ULONG, "SapIfOutputPackets"),]

    

class SAP_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(SAP_IF_INFO, "SapIfInfo"),(SAP_IF_STATS, "SapIfStats"),]

    

class SAP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(ULONG, "InterfaceIndex"),]

    

class SAP_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(SAP_INTERFACE, "SapInterface"),]

    

class RIPMIB_BASE(NdrStructure):
    MEMBERS = [(ULONG, "RIPOperState"),]

    

class RIP_IF_STATS(NdrStructure):
    MEMBERS = [(ULONG, "RipIfOperState"),(ULONG, "RipIfInputPackets"),(ULONG, "RipIfOutputPackets"),]

    

class RIP_IF_INFO(NdrStructure):
    MEMBERS = [(ULONG, "AdminState"),(ULONG, "UpdateMode"),(ULONG, "PacketType"),(ULONG, "Supply"),(ULONG, "Listen"),(ULONG, "PeriodicUpdateInterval"),(ULONG, "AgeIntervalMultiplier"),]

    

class RIP_INTERFACE(NdrStructure):
    MEMBERS = [(ULONG, "InterfaceIndex"),(RIP_IF_INFO, "RipIfInfo"),(RIP_IF_STATS, "RipIfStats"),]

    

class RIP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(ULONG, "InterfaceIndex"),]

    

class RIP_MIB_SET_INPUT_DATA(NdrStructure):
    MEMBERS = [(ULONG, "TableId"),(RIP_INTERFACE, "RipInterface"),]

    

class EAPTLS_HASH(NdrStructure):
    MEMBERS = [(DWORD, "cbHash"),(BYTE, "pbHash"),]

    

class EAPTLS_USER_PROPERTIES(NdrStructure):
    MEMBERS = [(DWORD, "reserved"),(DWORD, "dwVersion"),(DWORD, "dwSize"),(DWORD, "fFlags"),(EAPTLS_HASH, "Hash"),(PWCHAR, "pwszDiffUser"),(DWORD, "dwPinOffset"),(PWCHAR, "pwszPin"),(USHORT, "usLength"),(USHORT, "usMaximumLength"),(UCHAR, "ucSeed"),(WCHAR, "awszString"),]

    

class IPBOOTP_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_ServerCount"),]

    

class IPBOOTP_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_RelayMode"),(DWORD, "IC_MaxHopCount"),(DWORD, "IC_MinSecondsSinceBoot"),]

    

class IPBOOTP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(DWORD, "IMGID_IfIndex"),]

    

class IPBOOTP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(DWORD, "IMGOD_IfIndex"),(BYTE, "IMGOD_Buffer"),]

    

class IPBOOTP_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_ArpUpdateFailures"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_RequestsDiscarded"),(DWORD, "IS_RepliesReceived"),(DWORD, "IS_RepliesDiscarded"),]

    

class IPBOOTP_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IB_State"),(DWORD, "IB_AddrCount"),]

    

class IPBOOTP_IP_ADDRESS(NdrStructure):
    MEMBERS = [(DWORD, "IA_Address"),(DWORD, "IA_Netmask"),]

    

class DHCPV6R_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(DWORD, "IMGOD_IfIndex"),(BYTE, "IMGOD_Buffer"),]

    

class DHCPV6R_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_RequestsDiscarded"),(DWORD, "IS_RepliesReceived"),(DWORD, "IS_RepliesDiscarded"),]

    

class DHCPV6R_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(DWORD, "IMGID_IfIndex"),]

    

class DHCPV6R_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_ServerCount"),]

    

class DHCPV6R_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_RelayMode"),(DWORD, "IC_MaxHopCount"),(DWORD, "IC_MinElapsedTime"),]

    

class IPRIP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGID_TypeID"),(U0, "u0"),]

    

class IPRIP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "IMGOD_TypeID"),(U0, "u0"),(BYTE, "IMGOD_Buffer"),]

    

class IPRIP_GLOBAL_STATS(NdrStructure):
    MEMBERS = [(DWORD, "GS_SystemRouteChanges"),(DWORD, "GS_TotalResponsesSent"),]

    

class IPRIP_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "GC_LoggingLevel"),(DWORD, "GC_MaxRecvQueueSize"),(DWORD, "GC_MaxSendQueueSize"),(DWORD, "GC_MinTriggeredUpdateInterval"),(DWORD, "GC_PeerFilterMode"),(DWORD, "GC_PeerFilterCount"),]

    

class IPRIP_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IS_State"),(DWORD, "IS_SendFailures"),(DWORD, "IS_ReceiveFailures"),(DWORD, "IS_RequestsSent"),(DWORD, "IS_RequestsReceived"),(DWORD, "IS_ResponsesSent"),(DWORD, "IS_ResponsesReceived"),(DWORD, "IS_BadResponsePacketsReceived"),(DWORD, "IS_BadResponseEntriesReceived"),(DWORD, "IS_TriggeredUpdatesSent"),]

    

class IPRIP_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "IC_State"),(DWORD, "IC_Metric"),(DWORD, "IC_UpdateMode"),(DWORD, "IC_AcceptMode"),(DWORD, "IC_AnnounceMode"),(DWORD, "IC_ProtocolFlags"),(DWORD, "IC_RouteExpirationInterval"),(DWORD, "IC_RouteRemovalInterval"),(DWORD, "IC_FullUpdateInterval"),(DWORD, "IC_AuthenticationType"),(BYTE, "IC_AuthenticationKey"),(WORD, "IC_RouteTag"),(DWORD, "IC_UnicastPeerMode"),(DWORD, "IC_AcceptFilterMode"),(DWORD, "IC_AnnounceFilterMode"),(DWORD, "IC_UnicastPeerCount"),(DWORD, "IC_AcceptFilterCount"),(DWORD, "IC_AnnounceFilterCount"),]

    

class IPRIP_ROUTE_FILTER(NdrStructure):
    MEMBERS = [(DWORD, "RF_LoAddress"),(DWORD, "RF_HiAddress"),]

    

class IPRIP_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IB_State"),(DWORD, "IB_AddrCount"),]

    

class IPRIP_IP_ADDRESS(NdrStructure):
    MEMBERS = [(DWORD, "IA_Address"),(DWORD, "IA_Netmask"),]

    

class IPRIP_PEER_STATS(NdrStructure):
    MEMBERS = [(DWORD, "PS_LastPeerRouteTag"),(DWORD, "PS_LastPeerUpdateTickCount"),(DWORD, "PS_LastPeerUpdateVersion"),(DWORD, "PS_BadResponsePacketsFromPeer"),(DWORD, "PS_BadResponseEntriesFromPeer"),]

    

class IGMP_MIB_GET_INPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "TypeId"),(USHORT, "Flags"),(USHORT, "Signature"),(DWORD, "IfIndex"),(DWORD, "RasClientAddr"),(DWORD, "GroupAddr"),(DWORD, "Count"),]

    

class IGMP_MIB_GET_OUTPUT_DATA(NdrStructure):
    MEMBERS = [(DWORD, "TypeId"),(DWORD, "Flags"),(DWORD, "Count"),(BYTE, "Buffer"),]

    

class IGMP_MIB_GLOBAL_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "LoggingLevel"),(DWORD, "RasClientStats"),]

    

class IGMP_MIB_GLOBAL_STATS(NdrStructure):
    MEMBERS = [(DWORD, "CurrentGroupMemberships"),(DWORD, "GroupMembershipsAdded"),]

    

class IGMP_MIB_IF_BINDING(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IfType"),(DWORD, "State"),(DWORD, "AddrCount"),]

    

class IGMP_MIB_IF_CONFIG(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(DWORD, "Flags"),(DWORD, "IgmpProtocolType"),(DWORD, "RobustnessVariable"),(DWORD, "StartupQueryInterval"),(DWORD, "StartupQueryCount"),(DWORD, "GenQueryInterval"),(DWORD, "GenQueryMaxResponseTime"),(DWORD, "LastMemQueryInterval"),(DWORD, "LastMemQueryCount"),(DWORD, "OtherQuerierPresentInterval"),(DWORD, "GroupMembershipTimeout"),(DWORD, "NumStaticGroups"),]

    

class IGMP_MIB_IF_GROUPS_LIST(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(DWORD, "NumGroups"),(BYTE, "Buffer"),]

    

class IGMP_MIB_GROUP_INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "IpAddr"),(DWORD, "GroupUpTime"),(DWORD, "GroupExpiryTime"),(DWORD, "LastReporter"),(DWORD, "V1HostPresentTimeLeft"),(DWORD, "Flags"),]

    

class IGMP_MIB_IF_STATS(NdrStructure):
    MEMBERS = [(DWORD, "IfIndex"),(DWORD, "IpAddr"),(DWORD, "IfType"),(BYTE, "State"),(BYTE, "QuerierState"),(DWORD, "IgmpProtocolType"),(DWORD, "QuerierIpAddr"),(DWORD, "ProxyIfIndex"),(DWORD, "QuerierPresentTimeLeft"),(DWORD, "LastQuerierChangeTime"),(DWORD, "V1QuerierPresentTimeLeft"),(DWORD, "Uptime"),(DWORD, "TotalIgmpPacketsReceived"),(DWORD, "TotalIgmpPacketsForRouter"),(DWORD, "GeneralQueriesReceived"),(DWORD, "WrongVersionQueries"),(DWORD, "JoinsReceived"),(DWORD, "LeavesReceived"),(DWORD, "CurrentGroupMemberships"),(DWORD, "GroupMembershipsAdded"),(DWORD, "WrongChecksumPackets"),(DWORD, "ShortPacketsReceived"),(DWORD, "LongPacketsReceived"),(DWORD, "PacketsWithoutRtrAlert"),]

    

class IGMP_MIB_GROUP_IFS_LIST(NdrStructure):
    MEMBERS = [(DWORD, "GroupAddr"),(DWORD, "NumInterfaces"),(BYTE, "Buffer"),]

    

class IGMP_MIB_GROUP_SOURCE_INFO_V3(NdrStructure):
    MEMBERS = [(DWORD, "Source"),(DWORD, "SourceExpiryTime"),(DWORD, "SourceUpTime"),(DWORD, "Flags"),]

    

class IGMP_MIB_GROUP_INFO_V3(NdrStructure):
    MEMBERS = [(U0, "u0"),(DWORD, "IpAddr"),(DWORD, "GroupUpTime"),(DWORD, "GroupExpiryTime"),(DWORD, "LastReporter"),(DWORD, "V1HostPresentTimeLeft"),(DWORD, "Flags"),(DWORD, "Version"),(DWORD, "Size"),(DWORD, "FilterType"),(DWORD, "V2HostPresentTimeLeft"),(DWORD, "NumSources"),]

    

class INTERFACE_ROUTE_ENTRY(NdrStructure):
    MEMBERS = [(DWORD, "dwIndex"),(INTERFACE_ROUTE_INFO, "routeInfo"),]

    

class IP_NAT_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),]

    

class IP_NAT_SESSION_MAPPING(NdrStructure):
    MEMBERS = [(UCHAR, "Protocol"),(ULONG, "PrivateAddress"),(USHORT, "PrivatePort"),(ULONG, "PublicAddress"),(USHORT, "PublicPort"),(ULONG, "RemoteAddress"),(USHORT, "RemotePort"),(IP_NAT_DIRECTION, "Direction"),(ULONG, "IdleTime"),]

    

class IP_NAT_ENUMERATE_SESSION_MAPPINGS(NdrStructure):
    MEMBERS = [(ULONG, "Index"),(ULONG, "EnumerateContext"),(ULONG, "EnumerateCount"),(ULONG, "EnumerateTotalHint"),(IP_NAT_SESSION_MAPPING, "EnumerateTable"),]

    

class IP_NAT_INTERFACE_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "TotalMappings"),(ULONG, "InboundMappings"),(ULONG64, "BytesForward"),(ULONG64, "BytesReverse"),(ULONG64, "PacketsForward"),(ULONG64, "PacketsReverse"),(ULONG64, "RejectsForward"),(ULONG64, "RejectsReverse"),]

    

class IP_DNS_PROXY_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),]

    

class IP_DNS_PROXY_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "MessagesIgnored"),(ULONG, "QueriesReceived"),(ULONG, "ResponsesReceived"),(ULONG, "QueriesSent"),(ULONG, "ResponsesSent"),]

    

class IP_AUTO_DHCP_MIB_QUERY(NdrStructure):
    MEMBERS = [(ULONG, "Oid"),(U0, "u0"),(ULONG, "Reserved"),]

    

class IP_AUTO_DHCP_STATISTICS(NdrStructure):
    MEMBERS = [(ULONG, "MessagesIgnored"),(ULONG, "BootpOffersSent"),(ULONG, "DiscoversReceived"),(ULONG, "InformsReceived"),(ULONG, "OffersSent"),(ULONG, "RequestsReceived"),(ULONG, "AcksSent"),(ULONG, "NaksSent"),(ULONG, "DeclinesReceived"),(ULONG, "ReleasesReceived"),]

    

class MIB_DA_MSG(NdrStructure):
    MEMBERS = [(UINT32, "op_code"),(UINT32, "ret_code"),(UINT32, "in_snmp_id"),(UINT32, "obj_id"),(UINT32, "attr_id"),(UINT32, "inst_id"),(UINT32, "next_snmp_id"),(UINT32, "creator"),(UINT32, "attr_type"),(UINT32, "inst_cnt"),(UINT32, "map_flag"),(ULONG_PTR, "data"),]

    

class IP_AUTO_DHCP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(ULONG, "LeaseTime"),(ULONG, "ScopeNetwork"),(ULONG, "ScopeMask"),(ULONG, "ExclusionCount"),(ULONG, "ExclusionArray"),]

    

class IP_AUTO_DHCP_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),]

    

class IP_DNS_PROXY_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(ULONG, "TimeoutSeconds"),]

    

class IP_DNS_PROXY_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Flags"),]

    

class IP_NAT_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),(RTR_INFO_BLOCK_HEADER, "Header"),]

    

class IP_NAT_TIMEOUT(NdrStructure):
    MEMBERS = [(ULONG, "TCPTimeoutSeconds"),(ULONG, "UDPTimeoutSeconds"),]

    

class IP_NAT_INTERFACE_INFO(NdrStructure):
    MEMBERS = [(ULONG, "Index"),(ULONG, "Flags"),(RTR_INFO_BLOCK_HEADER, "Header"),]

    

class IP_NAT_ADDRESS_RANGE(NdrStructure):
    MEMBERS = [(ULONG, "StartAddress"),(ULONG, "EndAddress"),(ULONG, "SubnetMask"),]

    

class IP_NAT_PORT_MAPPING(NdrStructure):
    MEMBERS = [(UCHAR, "Protocol"),(USHORT, "PublicPort"),(ULONG, "PublicAddress"),(USHORT, "PrivatePort"),(ULONG, "PrivateAddress"),]

    

class IP_NAT_ADDRESS_MAPPING(NdrStructure):
    MEMBERS = [(ULONG, "PrivateAddress"),(ULONG, "PublicAddress"),(BOOLEAN, "AllowInboundSessions"),]

    

class IP_ALG_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(ULONG, "LoggingLevel"),(ULONG, "Flags"),]

    

class RIP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(DWORD, "EventLogMask"),]

    

class RIP_ROUTE_FILTER_INFO(NdrStructure):
    MEMBERS = [(UCHAR, "Network"),(UCHAR, "Mask"),]

    

class RIP_IF_FILTERS(NdrStructure):
    MEMBERS = [(ULONG, "SupplyFilterAction"),(ULONG, "SupplyFilterCount"),(ULONG, "ListenFilterAction"),(ULONG, "ListenFilterCount"),(RIP_ROUTE_FILTER_INFO, "RouteFilter"),]

    

class RIP_IF_CONFIG(NdrStructure):
    MEMBERS = [(RIP_IF_INFO, "RipIfInfo"),(RIP_IF_FILTERS, "RipIfFilters"),]

    

class SAP_GLOBAL_INFO(NdrStructure):
    MEMBERS = [(DWORD, "EventLogMask"),]

    

class OSPF_ROUTE_FILTER(NdrStructure):
    MEMBERS = [(DWORD, "dwAddress"),(DWORD, "dwMask"),]

    

class OSPF_ROUTE_FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "type"),(OSPF_FILTER_ACTION, "ofaActionOnMatch"),(DWORD, "dwNumFilters"),(OSPF_ROUTE_FILTER, "pFilters"),]

    

class OSPF_PROTO_FILTER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "type"),(OSPF_FILTER_ACTION, "ofaActionOnMatch"),(DWORD, "dwNumProtoIds"),(DWORD, "pdwProtoId"),]

    

class OSPF_GLOBAL_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "routerId"),(DWORD, "ASBrdrRtr"),(DWORD, "logLevel"),]

    

class OSPF_AREA_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "areaId"),(DWORD, "authType"),(DWORD, "importASExtern"),(DWORD, "stubMetric"),(DWORD, "importSumAdv"),]

    

class OSPF_AREA_RANGE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "areaId"),(DWORD, "rangeNet"),(DWORD, "rangeMask"),]

    

class OSPF_VIRT_INTERFACE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "transitAreaId"),(DWORD, "virtNeighborRouterId"),(DWORD, "transitDelay"),(DWORD, "retransInterval"),(DWORD, "helloInterval"),(DWORD, "deadInterval"),(BYTE, "password"),]

    

class OSPF_INTERFACE_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "intfIpAddr"),(DWORD, "intfSubnetMask"),(DWORD, "areaId"),(DWORD, "intfType"),(DWORD, "routerPriority"),(DWORD, "transitDelay"),(DWORD, "retransInterval"),(DWORD, "helloInterval"),(DWORD, "deadInterval"),(DWORD, "pollInterval"),(DWORD, "metricCost"),(BYTE, "password"),(DWORD, "mtuSize"),]

    

class OSPF_NBMA_NEIGHBOR_PARAM(NdrStructure):
    MEMBERS = [(DWORD, "type"),(DWORD, "create"),(DWORD, "enable"),(DWORD, "neighborIpAddr"),(DWORD, "intfIpAddr"),(DWORD, "neighborPriority"),]

    

class REQUESTBUFFER(NdrStructure):
    MEMBERS = [(DWORD, "RB_PCBIndex"),(REQTYPES, "RB_Reqtype"),(DWORD, "RB_Dummy"),(DWORD, "RB_Done"),(LONGLONG, "Alignment"),(BYTE, "RB_Buffer"),]

    

class DEVICECONFIGINFO(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(DWORD, "dwVersion"),(DWORD, "cbBuffer"),(DWORD, "cEntries"),(BYTE, "abdata"),]

    

class RAS_DEVICE_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwVersion"),(BOOL, "fWrite"),(BOOL, "fRasEnabled"),(BOOL, "fRouterEnabled"),(BOOL, "fRouterOutboundEnabled"),(DWORD, "dwTapiLineId"),(DWORD, "dwError"),(DWORD, "dwNumEndPoints"),(DWORD, "dwMaxOutCalls"),(DWORD, "dwMaxInCalls"),(DWORD, "dwMinWanEndPoints"),(DWORD, "dwMaxWanEndPoints"),(RASDEVICETYPE, "eDeviceType"),(GUID, "guidDevice"),(CHAR, "szPortName"),(CHAR, "szDeviceName"),(WCHAR, "wszDeviceName"),]

    

class RAS_CALLEDID_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(BYTE, "bCalledId"),]

    

class GETSETCALLEDID(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(BOOL, "fWrite"),(DWORD, "dwSize"),(GUID, "guidDevice"),(RAS_DEVICE_INFO, "rdi"),(RAS_CALLEDID_INFO, "rciInfo"),]

    

class RAS_NDISWAN_DRIVER_INFO(NdrStructure):
    MEMBERS = [(ULONG, "DriverCaps"),(ULONG, "Reserved"),]

    

class GETNDISWANDRIVERCAPSSTRUCT(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(RAS_NDISWAN_DRIVER_INFO, "NdiswanDriverInfo"),]

    

class GETDEVCONFIGSTRUCT(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(CHAR, "devicetype"),(DWORD, "size"),(BYTE, "config"),]

    

class ENUM(NdrStructure):
    MEMBERS = [(DWORD, "retcode"),(DWORD, "size"),(DWORD, "entries"),(BYTE, "buffer"),]

    

class RASMAN_PORT_32(NdrStructure):
    MEMBERS = [(DWORD, "P_Port"),(CHAR, "P_PortName"),(RASMAN_STATUS, "P_Status"),(RASDEVICETYPE, "P_rdtDeviceType"),(RASMAN_USAGE, "P_ConfiguredUsage"),(RASMAN_USAGE, "P_CurrentUsage"),(CHAR, "P_MediaName"),(CHAR, "P_DeviceType"),(CHAR, "P_DeviceName"),(DWORD, "P_LineDeviceId"),(DWORD, "P_AddressId"),]

    

class RASMAN_INFO(NdrStructure):
    MEMBERS = [(RASMAN_STATUS, "RI_PortStatus"),(RASMAN_STATE, "RI_ConnState"),(DWORD, "RI_LinkSpeed"),(DWORD, "RI_LastError"),(RASMAN_USAGE, "RI_CurrentUsage"),(CHAR, "RI_DeviceTypeConnecting"),(CHAR, "RI_DeviceConnecting"),(CHAR, "RI_szDeviceType"),(CHAR, "RI_szDeviceName"),(CHAR, "RI_szPortName"),(RASMAN_DISCONNECT_TYPE, "RI_DisconnectType"),(DWORD, "RI_OwnershipFlag"),(DWORD, "RI_ConnectDuration"),(DWORD, "RI_BytesReceived"),(CHAR, "RI_Phonebook"),(CHAR, "RI_PhoneEntry"),(HANDLE, "RI_ConnectionHandle"),(DWORD, "RI_SubEntry"),(RASDEVICETYPE, "RI_rdtDeviceType"),(GUID, "RI_GuidEntry"),(DWORD, "RI_dwSessionId"),(DWORD, "RI_dwFlags"),(GUID, "RI_CorrelationGuid"),]

    

class INFO(NdrStructure):
    MEMBERS = [(U0, "u0"),(RASMAN_INFO, "info"),]

    

class RASRPC_CALLBACKLIST(NdrStructure):
    MEMBERS = [(WCHAR, "pszPortName"),(WCHAR, "pszDeviceName"),(WCHAR, "pszNumber"),(DWORD, "dwDeviceType"),(PPNEXT, "*pNext"),]

    

class RASRPC_STRINGLIST(NdrStructure):
    MEMBERS = [(WCHAR, "psz"),(PPNEXT, "*pNext"),]

    

class RASRPC_LOCATIONLIST(NdrStructure):
    MEMBERS = [(DWORD, "dwLocationId"),(DWORD, "iPrefix"),(DWORD, "iSuffix"),(PPNEXT, "*pNext"),]

    

class RASRPC_PBUSER(NdrStructure):
    MEMBERS = [(BOOL, "fOperatorDial"),(BOOL, "fPreviewPhoneNumber"),(BOOL, "fUseLocation"),(BOOL, "fShowLights"),(BOOL, "fShowConnectStatus"),(BOOL, "fCloseOnDial"),(BOOL, "fAllowLogonPhonebookEdits"),(BOOL, "fAllowLogonLocationEdits"),(BOOL, "fSkipConnectComplete"),(BOOL, "fNewEntryWizard"),(DWORD, "dwRedialAttempts"),(DWORD, "dwRedialSeconds"),(DWORD, "dwIdleDisconnectSeconds"),(BOOL, "fRedialOnLinkFailure"),(BOOL, "fPopupOnTopWhenRedialing"),(BOOL, "fExpandAutoDialQuery"),(DWORD, "dwCallbackMode"),(LPRASRPC_CALLBACKLIST, "pCallbacks"),(WCHAR, "pszLastCallbackByCaller"),(DWORD, "dwPhonebookMode"),(WCHAR, "pszPersonalFile"),(WCHAR, "pszAlternatePath"),(LPRASRPC_STRINGLIST, "pPhonebooks"),(LPRASRPC_STRINGLIST, "pAreaCodes"),(BOOL, "fUseAreaAndCountry"),(LPRASRPC_STRINGLIST, "pPrefixes"),(LPRASRPC_STRINGLIST, "pSuffixes"),(LPRASRPC_LOCATIONLIST, "pLocations"),(DWORD, "dwXPhonebook"),(DWORD, "dwYPhonebook"),(WCHAR, "pszDefaultEntry"),(BOOL, "fInitialized"),(BOOL, "fDirty"),]

    
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