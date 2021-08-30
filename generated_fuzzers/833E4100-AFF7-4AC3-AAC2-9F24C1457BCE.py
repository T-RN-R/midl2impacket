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


class COMVERSION(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "MajorVersion"),
        (UNSIGNED_SHORT, "MinorVersion"),
    ]


class ORPC_EXTENT(NdrStructure):
    MEMBERS = [
        (GUID, "id"),
        (UNSIGNED_LONG, "size"),
        (BYTE, "data"),
    ]


class ORPC_EXTENT_ARRAY(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "size"),
        (UNSIGNED_LONG, "reserved"),
        (PPORPC_EXTENT, "extent"),
    ]


class ORPCTHIS(NdrStructure):
    MEMBERS = [
        (COMVERSION, "version"),
        (UNSIGNED_LONG, "flags"),
        (UNSIGNED_LONG, "reserved1"),
        (CID, "cid"),
        (PORPC_EXTENT_ARRAY, "extensions"),
    ]


class ORPCTHAT(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "flags"),
        (PORPC_EXTENT_ARRAY, "extensions"),
    ]


class DUALSTRINGARRAY(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "wNumEntries"),
        (UNSIGNED_SHORT, "wSecurityOffset"),
        (UNSIGNED_SHORT, "aStringArray"),
    ]


class MINTERFACEPOINTER(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "ulCntData"),
        (BYTE, "abData"),
    ]


class ERROROBJECTDATA(NdrStructure):
    MEMBERS = [
        (DWORD, "dwVersion"),
        (DWORD, "dwHelpContext"),
        (IID, "iid"),
        (PWCHAR_T, "pszSource"),
        (PWCHAR_T, "pszDescription"),
        (PWCHAR_T, "pszHelpFile"),
    ]


class STDOBJREF(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "flags"),
        (UNSIGNED_LONG, "cPublicRefs"),
        (OXID, "oxid"),
        (OID, "oid"),
        (IPID, "ipid"),
    ]


class REMQIRESULT(NdrStructure):
    MEMBERS = [
        (HRESULT, "hResult"),
        (STDOBJREF, "std"),
    ]


class REMINTERFACEREF(NdrStructure):
    MEMBERS = [
        (IPID, "ipid"),
        (UNSIGNED_LONG, "cPublicRefs"),
        (UNSIGNED_LONG, "cPrivateRefs"),
    ]


class COSERVERINFO(NdrStructure):
    MEMBERS = [
        (DWORD, "dwReserved1"),
        (PWCHAR_T, "pwszName"),
        (PDWORD, "pdwReserved"),
        (DWORD, "dwReserved2"),
    ]


class CUSTOMREMOTE_REQUEST_SCM_INFO(NdrStructure):
    MEMBERS = [
        (DWORD, "ClientImpLevel"),
        (UNSIGNED_SHORT, "cRequestedProtseqs"),
        (PUNSIGNED_SHORT, "pRequestedProtseqs"),
    ]


class CUSTOMREMOTE_REPLY_SCM_INFO(NdrStructure):
    MEMBERS = [
        (OXID, "Oxid"),
        (PDUALSTRINGARRAY, "pdsaOxidBindings"),
        (IPID, "ipidRemUnknown"),
        (DWORD, "authnHint"),
        (COMVERSION, "serverVersion"),
    ]


class INSTANTIATIONINFODATA(NdrStructure):
    MEMBERS = [
        (CLSID, "classId"),
        (DWORD, "classCtx"),
        (DWORD, "actvflags"),
        (LONG, "fIsSurrogate"),
        (DWORD, "cIID"),
        (DWORD, "instFlag"),
        (PIID, "pIID"),
        (DWORD, "thisSize"),
        (COMVERSION, "clientCOMVersion"),
    ]


class LOCATIONINFODATA(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "machineName"),
        (DWORD, "processId"),
        (DWORD, "apartmentId"),
        (DWORD, "contextId"),
    ]


class ACTIVATIONCONTEXTINFODATA(NdrStructure):
    MEMBERS = [
        (LONG, "clientOK"),
        (LONG, "bReserved1"),
        (DWORD, "dwReserved1"),
        (DWORD, "dwReserved2"),
        (PMINTERFACEPOINTER, "pIFDClientCtx"),
        (PMINTERFACEPOINTER, "pIFDPrototypeCtx"),
    ]


class CUSTOMHEADER(NdrStructure):
    MEMBERS = [
        (DWORD, "totalSize"),
        (DWORD, "headerSize"),
        (DWORD, "dwReserved"),
        (DWORD, "destCtx"),
        (DWORD, "cIfs"),
        (CLSID, "classInfoClsid"),
        (PCLSID, "pclsid"),
        (PDWORD, "pSizes"),
        (PDWORD, "pdwReserved"),
    ]


class PROPSOUTINFO(NdrStructure):
    MEMBERS = [
        (DWORD, "cIfs"),
        (PIID, "piid"),
        (PHRESULT, "phresults"),
        (PPMINTERFACEPOINTER, "ppIntfData"),
    ]


class SECURITYINFODATA(NdrStructure):
    MEMBERS = [
        (DWORD, "dwAuthnFlags"),
        (PCOSERVERINFO, "pServerInfo"),
        (PDWORD, "pdwReserved"),
    ]


class SCMREQUESTINFODATA(NdrStructure):
    MEMBERS = [
        (PDWORD, "pdwReserved"),
        (PCUSTOMREMOTE_REQUEST_SCM_INFO, "remoteRequest"),
    ]


class SCMREPLYINFODATA(NdrStructure):
    MEMBERS = [
        (PDWORD, "pdwReserved"),
        (PCUSTOMREMOTE_REPLY_SCM_INFO, "remoteReply"),
    ]


class INSTANCEINFODATA(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "fileName"),
        (DWORD, "mode"),
        (PMINTERFACEPOINTER, "ifdROT"),
        (PMINTERFACEPOINTER, "ifdStg"),
    ]


class SPECIALPROPERTIESDATA(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "dwSessionId"),
        (LONG, "fRemoteThisSessionId"),
        (LONG, "fClientImpersonating"),
        (LONG, "fPartitionIDPresent"),
        (DWORD, "dwDefaultAuthnLvl"),
        (GUID, "guidPartition"),
        (DWORD, "dwPRTFlags"),
        (DWORD, "dwOrigClsctx"),
        (DWORD, "dwFlags"),
        (DWORD, "Reserved1"),
        (UNSIGNED___INT64, "Reserved2"),
        (DWORD, "Reserved3"),
    ]


class SPECIALPROPERTIESDATA_ALTERNATE(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "dwSessionId"),
        (LONG, "fRemoteThisSessionId"),
        (LONG, "fClientImpersonating"),
        (LONG, "fPartitionIDPresent"),
        (DWORD, "dwDefaultAuthnLvl"),
        (GUID, "guidPartition"),
        (DWORD, "dwPRTFlags"),
        (DWORD, "dwOrigClsctx"),
        (DWORD, "dwFlags"),
        (DWORD, "Reserved3"),
    ]


Method(
    "RemoteActivation",
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
    MEMBERS = [
        (UNSIGNED_LONG, "cBytes"),
        (UNSIGNED_LONG, "clSize"),
        (UNSIGNED_SHORT, "asData"),
    ]


class CURRENCY(NdrStructure):
    MEMBERS = [
        (__INT64, "int64"),
    ]


class DECIMAL(NdrStructure):
    MEMBERS = [
        (WORD, "wReserved"),
        (BYTE, "scale"),
        (BYTE, "sign"),
        (ULONG, "Hi32"),
        (ULONGLONG, "Lo64"),
    ]


class WIREBRECORDSTR(NdrStructure):
    MEMBERS = [
        (ULONG, "fFlags"),
        (ULONG, "clSize"),
        (PMINTERFACEPOINTER, "pRecInfo"),
        (PBYTE, "pRecord"),
    ]


class PBRECORD(NdrStructure):
    MEMBERS = []


class _VARUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (LONGLONG, "llVal"),
        2: (LONG, "lVal"),
        3: (BYTE, "bVal"),
        4: (SHORT, "iVal"),
        5: (FLOAT, "fltVal"),
        6: (DOUBLE, "dblVal"),
        7: (VARIANT_BOOL, "boolVal"),
        8: (HRESULT, "scode"),
        9: (CURRENCY, "cyVal"),
        10: (DATE, "date"),
        11: (BSTR, "bstrVal"),
        12: (PIUNKNOWN, "punkVal"),
        13: (PIDISPATCH, "pdispVal"),
        14: (PSAFEARRAY, "parray"),
        15: (BRECORD, "brecVal"),
        16: (PBYTE, "pbVal"),
        17: (PSHORT, "piVal"),
        18: (PLONG, "plVal"),
        19: (PLONGLONG, "pllVal"),
        20: (PFLOAT, "pfltVal"),
        21: (PDOUBLE, "pdblVal"),
        22: (PVARIANT_BOOL, "pboolVal"),
        23: (PHRESULT, "pscode"),
        24: (PCURRENCY, "pcyVal"),
        25: (PDATE, "pdate"),
        26: (PBSTR, "pbstrVal"),
        27: (PPIUNKNOWN, "ppunkVal"),
        28: (PPIDISPATCH, "ppdispVal"),
        29: (PPSAFEARRAY, "pparray"),
        30: (PVARIANT, "pvarVal"),
        31: (CHAR, "cVal"),
        32: (USHORT, "uiVal"),
        33: (ULONG, "ulVal"),
        34: (ULONGLONG, "ullVal"),
        35: (INT, "intVal"),
        36: (UINT, "uintVal"),
        37: (DECIMAL, "decVal"),
        38: (PCHAR, "pcVal"),
        39: (PUSHORT, "puiVal"),
        40: (PULONG, "pulVal"),
        41: (PULONGLONG, "pullVal"),
        42: (PINT, "pintVal"),
        43: (PUINT, "puintVal"),
        44: (PDECIMAL, "pdecVal"),
    }


class WIREVARIANTSTR(NdrStructure):
    MEMBERS = [
        (DWORD, "clSize"),
        (DWORD, "rpcReserved"),
        (USHORT, "vt"),
        (USHORT, "wReserved1"),
        (USHORT, "wReserved2"),
        (USHORT, "wReserved3"),
        (_VARUNION, "_varUnion"),
    ]


class SAFEARRAYBOUND(NdrStructure):
    MEMBERS = [
        (ULONG, "cElements"),
        (LONG, "lLbound"),
    ]


class SAFEARR_BSTR(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PBSTR, "aBstr"),
    ]


class SAFEARR_UNKNOWN(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PPIUNKNOWN, "apUnknown"),
    ]


class SAFEARR_DISPATCH(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PPIDISPATCH, "apDispatch"),
    ]


class SAFEARR_VARIANT(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PVARIANT, "aVariant"),
    ]


class SAFEARR_BRECORD(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PBRECORD, "aRecord"),
    ]


class SAFEARR_HAVEIID(NdrStructure):
    MEMBERS = [
        (ULONG, "Size"),
        (PPIUNKNOWN, "apUnknown"),
        (IID, "iid"),
    ]


class BYTE_SIZEDARR(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "clSize"),
        (PBYTE, "pData"),
    ]


class WORD_SIZEDARR(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "clSize"),
        (PUNSIGNED_SHORT, "pData"),
    ]


class DWORD_SIZEDARR(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "clSize"),
        (PUNSIGNED_LONG, "pData"),
    ]


class HYPER_SIZEDARR(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "clSize"),
        (PHYPER, "pData"),
    ]


class U(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (SAFEARR_BSTR, "BstrStr"),
        2: (SAFEARR_UNKNOWN, "UnknownStr"),
        3: (SAFEARR_DISPATCH, "DispatchStr"),
        4: (SAFEARR_VARIANT, "VariantStr"),
        5: (SAFEARR_BRECORD, "RecordStr"),
        6: (SAFEARR_HAVEIID, "HaveIidStr"),
        7: (BYTE_SIZEDARR, "ByteStr"),
        8: (WORD_SIZEDARR, "WordStr"),
        9: (DWORD_SIZEDARR, "LongStr"),
        10: (HYPER_SIZEDARR, "HyperStr"),
    }


class SAFEARRAYUNION(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "sfType"),
        (U, "u"),
    ]


class PSAFEARRAY(NdrStructure):
    MEMBERS = [
        (USHORT, "cDims"),
        (USHORT, "fFeatures"),
        (ULONG, "cbElements"),
        (ULONG, "cLocks"),
        (SAFEARRAYUNION, "uArrayStructs"),
        (SAFEARRAYBOUND, "rgsabound"),
    ]


class RECORDINFO(NdrStructure):
    MEMBERS = [
        (GUID, "libraryGuid"),
        (DWORD, "verMajor"),
        (GUID, "recGuid"),
        (DWORD, "verMinor"),
        (DWORD, "Lcid"),
    ]


class DISPPARAMS(NdrStructure):
    MEMBERS = [
        (PVARIANT, "rgvarg"),
        (PDISPID, "rgdispidNamedArgs"),
        (UINT, "cArgs"),
        (UINT, "cNamedArgs"),
    ]


class EXCEPINFO(NdrStructure):
    MEMBERS = [
        (WORD, "wCode"),
        (WORD, "wReserved"),
        (BSTR, "bstrSource"),
        (BSTR, "bstrDescription"),
        (BSTR, "bstrHelpFile"),
        (DWORD, "dwHelpContext"),
        (ULONG_PTR, "pvReserved"),
        (ULONG_PTR, "pfnDeferredFillIn"),
        (HRESULT, "scode"),
    ]


class PLPTDESC(NdrStructure):
    MEMBERS = []


class PLPADESC(NdrStructure):
    MEMBERS = []


class _TDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLPTDESC, "*lptdesc"),
        2: (PLPADESC, "*lpadesc"),
        3: (HREFTYPE, "hreftype"),
    }


class TYPEDESC(NdrStructure):
    MEMBERS = [
        (_TDUNION, "_tdUnion"),
        (USHORT, "vt"),
    ]


class ARRAYDESC(NdrStructure):
    MEMBERS = [
        (TYPEDESC, "tdescElem"),
        (USHORT, "cDims"),
        (SAFEARRAYBOUND, "rgbounds"),
    ]


class PARAMDESCEX(NdrStructure):
    MEMBERS = [
        (ULONG, "cBytes"),
        (VARIANT, "varDefaultValue"),
    ]


class PARAMDESC(NdrStructure):
    MEMBERS = [
        (PPARAMDESCEX, "pparamdescex"),
        (USHORT, "wParamFlags"),
    ]


class ELEMDESC(NdrStructure):
    MEMBERS = [
        (TYPEDESC, "tdesc"),
        (PARAMDESC, "paramdesc"),
    ]


class FUNCDESC(NdrStructure):
    MEMBERS = [
        (MEMBERID, "memid"),
        (PSCODE, "lReserved1"),
        (PELEMDESC, "lprgelemdescParam"),
        (FUNCKIND, "funckind"),
        (INVOKEKIND, "invkind"),
        (CALLCONV, "callconv"),
        (SHORT, "cParams"),
        (SHORT, "cParamsOpt"),
        (SHORT, "oVft"),
        (SHORT, "cReserved2"),
        (ELEMDESC, "elemdescFunc"),
        (WORD, "wFuncFlags"),
    ]


class _VDUNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (ULONG, "oInst"),
        2: (PVARIANT, "lpvarValue"),
    }


class VARDESC(NdrStructure):
    MEMBERS = [
        (MEMBERID, "memid"),
        (LPOLESTR, "lpstrReserved"),
        (_VDUNION, "_vdUnion"),
        (ELEMDESC, "elemdescVar"),
        (WORD, "wVarFlags"),
        (VARKIND, "varkind"),
    ]


class TYPEATTR(NdrStructure):
    MEMBERS = [
        (GUID, "guid"),
        (LCID, "lcid"),
        (DWORD, "dwReserved1"),
        (DWORD, "dwReserved2"),
        (DWORD, "dwReserved3"),
        (LPOLESTR, "lpstrReserved4"),
        (ULONG, "cbSizeInstance"),
        (TYPEKIND, "typekind"),
        (WORD, "cFuncs"),
        (WORD, "cVars"),
        (WORD, "cImplTypes"),
        (WORD, "cbSizeVft"),
        (WORD, "cbAlignment"),
        (WORD, "wTypeFlags"),
        (WORD, "wMajorVerNum"),
        (WORD, "wMinorVerNum"),
        (TYPEDESC, "tdescAlias"),
        (DWORD, "dwReserved5"),
        (WORD, "wReserved6"),
    ]


class TLIBATTR(NdrStructure):
    MEMBERS = [
        (GUID, "guid"),
        (LCID, "lcid"),
        (SYSKIND, "syskind"),
        (UNSIGNED_SHORT, "wMajorVerNum"),
        (UNSIGNED_SHORT, "wMinorVerNum"),
        (UNSIGNED_SHORT, "wLibFlags"),
    ]


class CUSTDATAITEM(NdrStructure):
    MEMBERS = [
        (GUID, "guid"),
        (VARIANT, "varValue"),
    ]


class CUSTDATA(NdrStructure):
    MEMBERS = [
        (DWORD, "cCustData"),
        (PCUSTDATAITEM, "prgCustData"),
    ]


Method("GetTypeInfoCount", Out(PUINT),), Method(
    "GetTypeInfo",
    In(UINT),
    In(LCID),
    Out(PPITYPEINFO),
), Method(
    "GetIDsOfNames",
    In(REFIID),
    In(PLPOLESTR),
    In(UINT),
    In(LCID),
    Out(PDISPID),
), Method(
    "Invoke",
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
), Method(
    "_NewEnum",
    Out(PPIUNKNOWN),
), Method(
    "Item",
    In(LONG),
    Out(PVARIANT),
), Method(
    "Count",
    Out(PLONG),
),
