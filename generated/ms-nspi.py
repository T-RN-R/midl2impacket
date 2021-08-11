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


class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
    item = WCHAR

class PTR_UNSIGNED_SHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_SHORT),
    )

class UNSIGNED_SHORT(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_UNSIGNED_SHORT),

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

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#nspi Definition

#################################################################################

MSRPC_UUID_NSPI = uuidtup_to_bin(('F5CC5A18-4264-101-859-0800228426','0.0'))


class FLATUID_R(NDRSTRUCT):
    structure = (
        ('ab', BYTE),
    )


class PROPERTYTAGARRAY_R(NDRSTRUCT):
    structure = (
        ('cValues', DWORD),('aulPropTag', DWORD),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cb', DWORD),	('lpb', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = SHORT INT

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lpi', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = LONG

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lpl', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = CHAR

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lppszA', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = BINARY_R

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lpbin', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = FLATUID_R

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lpguid', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lppszW', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = FILETIME

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cValues', DWORD),	('lpft', PTR_DWORD),

    )
        

class PROPERTYVALUE_R(NDRSTRUCT):
    structure = (
        
    )


class DATA_DWORD(NDRUniConformantArray):
    item = PROPERTYVALUE_R

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('Reserved', DWORD),	('cValues', DWORD),	('lpProps', PTR_DWORD),

    )
        

class PROPERTYROWSET_R(NDRSTRUCT):
    structure = (
        ('cRows', DWORD),('aRow', PROPERTYROW_R),
    )


class RESTRICTION_R(NDRSTRUCT):
    structure = (
        
    )


class DATA_DWORD(NDRUniConformantArray):
    item = RESTRICTION_R

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cRes', DWORD),	('lpRes', PTR_DWORD),

    )
        

class NOTRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('lpRes', RESTRICTION_R),
    )


class CONTENTRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('ulFuzzyLevel', DWORD),('ulPropTag', DWORD),('lpProp', PROPERTYVALUE_R),
    )


class BITMASKRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('relBMR', DWORD),('ulPropTag', DWORD),('ulMask', DWORD),
    )


class PROPERTYRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('relop', DWORD),('ulPropTag', DWORD),('lpProp', PROPERTYVALUE_R),
    )


class COMPAREPROPSRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('relop', DWORD),('ulPropTag1', DWORD),('ulPropTag2', DWORD),
    )


class SUBRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('ulSubObject', DWORD),('lpRes', RESTRICTION_R),
    )


class SIZERESTRICTION_R(NDRSTRUCT):
    structure = (
        ('relop', DWORD),('ulPropTag', DWORD),('cb', DWORD),
    )


class EXISTRESTRICTION_R(NDRSTRUCT):
    structure = (
        ('ulReserved1', DWORD),('ulPropTag', DWORD),('ulReserved2', DWORD),
    )


class RESTRICTIONUNION_R(NDRUNION):
    union = {
        0x00000000: ('resAnd',ANDRESTRICTION_R),0x00000001: ('resOr',ORRESTRICTION_R),0x00000002: ('resNot',NOTRESTRICTION_R),0x00000003: ('resContent',CONTENTRESTRICTION_R),0x00000004: ('resProperty',PROPERTYRESTRICTION_R),0x00000005: ('resCompareProps',COMPAREPROPSRESTRICTION_R),0x00000006: ('resBitMask',BITMASKRESTRICTION_R),0x00000007: ('resSize',SIZERESTRICTION_R),0x00000008: ('resExist',EXISTRESTRICTION_R),0x00000009: ('resSubRestriction',SUBRESTRICTION_R),
    }
        

class Anonymous15(NDRSTRUCT):
    structure = (
        ('rt', DWORD),('res', RESTRICTIONUNION_R),
    )


class PROPERTYNAME_R(NDRSTRUCT):
    structure = (
        ('lpguid', FLATUID_R),('ulReserved', DWORD),('lID', LONG),
    )


class PROPERTYNAMESET_R(NDRSTRUCT):
    structure = (
        ('cNames', DWORD),('aNames', PROPERTYNAME_R),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = CHAR

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('Count', DWORD),	('Strings', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('Count', DWORD),	('Strings', PTR_DWORD),

    )
        

class STAT(NDRSTRUCT):
    structure = (
        ('SortType', DWORD),('ContainerID', DWORD),('CurrentRec', DWORD),('Delta', LONG),('NumPos', DWORD),('TotalRecs', DWORD),('CodePage', DWORD),('TemplateLocale', DWORD),('SortLocale', DWORD),
    )


class PROP_VAL_UNION(NDRUNION):
    union = {
        0x00000002: ('i',SHORT INT),0x00000003: ('l',LONG),0x0000000B: ('b',UNSIGNED SHORT INT),0x0000001E: ('lpszA',CHAR),0x00000102: ('bin',BINARY_R),0x0000001F: ('lpszW',WCHAR_T),0x00000048: ('lpguid',FLATUID_R),0x00000040: ('ft',FILETIME),0x0000000A: ('err',LONG),0x00001002: ('MVi',SHORTARRAY_R),0x00001003: ('MVl',LONGARRAY_R),0x0000101E: ('MVszA',STRINGARRAY_R),0x00001102: ('MVbin',BINARYARRAY_R),0x00001048: ('MVguid',FLATUIDARRAY_R),0x0000101F: ('MVszW',WSTRINGARRAY_R),0x00001040: ('MVft',DATETIMEARRAY_R),0x00000001: ('lReserved',LONG),
    }
        

class Anonymous16(NDRSTRUCT):
    structure = (
        ('ulPropTag', DWORD),('ulReserved', DWORD),('Value', PROP_VAL_UNION),
    )

NSPI_HANDLE = VOID

class NspiBind(NDRCALL):
    opnum = 0
    structure = (
		('hRpc', HANDLE_T),
		('dwFlags', DWORD),
		('pStat', STAT),
		('pServerGuid', FLATUID_R),
    )

class NspiBindResponse(NDRCALL):
    structure = (
		('pServerGuid', FLATUID_R),
		('contextHandle', NSPI_HANDLE),
    )
        

class NspiUnbind(NDRCALL):
    opnum = 1
    structure = (
		('contextHandle', NSPI_HANDLE),
		('Reserved', DWORD),
    )

class NspiUnbindResponse(NDRCALL):
    structure = (
		('contextHandle', NSPI_HANDLE),
    )
        

class NspiUpdateStat(NDRCALL):
    opnum = 2
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('plDelta', LONG),
    )

class NspiUpdateStatResponse(NDRCALL):
    structure = (
		('pStat', STAT),
		('plDelta', LONG),
    )
        

class NspiQueryRows(NDRCALL):
    opnum = 3
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('pStat', STAT),
		('dwETableCount', DWORD),
		('lpETable', DWORD),
		('Count', DWORD),
		('pPropTags', PROPERTYTAGARRAY_R),
    )

class NspiQueryRowsResponse(NDRCALL):
    structure = (
		('pStat', STAT),
		('ppRows', PROPERTYROWSET_R),
    )
        

class NspiSeekEntries(NDRCALL):
    opnum = 4
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('pTarget', PROPERTYVALUE_R),
		('lpETable', PROPERTYTAGARRAY_R),
		('pPropTags', PROPERTYTAGARRAY_R),
    )

class NspiSeekEntriesResponse(NDRCALL):
    structure = (
		('pStat', STAT),
		('ppRows', PROPERTYROWSET_R),
    )
        

class NspiGetMatches(NDRCALL):
    opnum = 5
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved1', DWORD),
		('pStat', STAT),
		('pReserved', PROPERTYTAGARRAY_R),
		('Reserved2', DWORD),
		('Filter', RESTRICTION_R),
		('lpPropName', PROPERTYNAME_R),
		('ulRequested', DWORD),
		('pPropTags', PROPERTYTAGARRAY_R),
    )

class NspiGetMatchesResponse(NDRCALL):
    structure = (
		('pStat', STAT),
		('ppOutMIds', PROPERTYTAGARRAY_R),
		('ppRows', PROPERTYROWSET_R),
    )
        

class NspiResortRestriction(NDRCALL):
    opnum = 6
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('pInMIds', PROPERTYTAGARRAY_R),
		('ppOutMIds', PROPERTYTAGARRAY_R),
    )

class NspiResortRestrictionResponse(NDRCALL):
    structure = (
		('pStat', STAT),
		('ppOutMIds', PROPERTYTAGARRAY_R),
    )
        

class NspiDNToMId(NDRCALL):
    opnum = 7
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pNames', STRINGSARRAY_R),
    )

class NspiDNToMIdResponse(NDRCALL):
    structure = (
		('ppOutMIds', PROPERTYTAGARRAY_R),
    )
        

class NspiGetPropList(NDRCALL):
    opnum = 8
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('dwMId', DWORD),
		('CodePage', DWORD),
    )

class NspiGetPropListResponse(NDRCALL):
    structure = (
		('ppPropTags', PROPERTYTAGARRAY_R),
    )
        

class NspiGetProps(NDRCALL):
    opnum = 9
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('pStat', STAT),
		('pPropTags', PROPERTYTAGARRAY_R),
    )

class NspiGetPropsResponse(NDRCALL):
    structure = (
		('ppRows', PROPERTYROW_R),
    )
        

class NspiCompareMIds(NDRCALL):
    opnum = 10
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('MId1', DWORD),
		('MId2', DWORD),
    )

class NspiCompareMIdsResponse(NDRCALL):
    structure = (
		('plResult', LONG),
    )
        

class NspiModProps(NDRCALL):
    opnum = 11
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('pPropTags', PROPERTYTAGARRAY_R),
		('pRow', PROPERTYROW_R),
    )

class NspiModPropsResponse(NDRCALL):
    structure = (

    )
        

class NspiGetSpecialTable(NDRCALL):
    opnum = 12
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('pStat', STAT),
		('lpVersion', DWORD),
    )

class NspiGetSpecialTableResponse(NDRCALL):
    structure = (
		('lpVersion', DWORD),
		('ppRows', PROPERTYROWSET_R),
    )
        

class NspiGetTemplateInfo(NDRCALL):
    opnum = 13
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('ulType', DWORD),
		('pDN', CHAR),
		('dwCodePage', DWORD),
		('dwLocaleID', DWORD),
    )

class NspiGetTemplateInfoResponse(NDRCALL):
    structure = (
		('ppData', PROPERTYROW_R),
    )
        

class NspiModLinkAtt(NDRCALL):
    opnum = 14
    structure = (
		('hRpc', NSPI_HANDLE),
		('dwFlags', DWORD),
		('ulPropTag', DWORD),
		('dwMId', DWORD),
		('lpEntryIds', BINARYARRAY_R),
    )

class NspiModLinkAttResponse(NDRCALL):
    structure = (

    )
        

class Opnum15NotUsedOnWire(NDRCALL):
    opnum = 15
    structure = (
		('Reserved1', NSPI_HANDLE),
		('Reserved2', DWORD),
		('Reserved3', DWORD),
		('Reserved4', BINARYARRAY_R),
    )

class Opnum15NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class NspiQueryColumns(NDRCALL):
    opnum = 16
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('dwFlags', DWORD),
    )

class NspiQueryColumnsResponse(NDRCALL):
    structure = (
		('ppColumns', PROPERTYTAGARRAY_R),
    )
        

class NspiGetNamesFromIDs(NDRCALL):
    opnum = 17
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('lpguid', FLATUID_R),
		('pPropTags', PROPERTYTAGARRAY_R),
    )

class NspiGetNamesFromIDsResponse(NDRCALL):
    structure = (
		('ppReturnedPropTags', PROPERTYTAGARRAY_R),
		('ppNames', PROPERTYNAMESET_R),
    )
        

class NspiGetIDsFromNames(NDRCALL):
    opnum = 18
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('dwFlags', DWORD),
		('cPropNames', DWORD),
		('pNames', PROPERTYNAME_R),
    )

class NspiGetIDsFromNamesResponse(NDRCALL):
    structure = (
		('ppPropTags', PROPERTYTAGARRAY_R),
    )
        

class NspiResolveNames(NDRCALL):
    opnum = 19
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('pPropTags', PROPERTYTAGARRAY_R),
		('paStr', STRINGSARRAY_R),
    )

class NspiResolveNamesResponse(NDRCALL):
    structure = (
		('ppMIds', PROPERTYTAGARRAY_R),
		('ppRows', PROPERTYROWSET_R),
    )
        

class NspiResolveNamesW(NDRCALL):
    opnum = 20
    structure = (
		('hRpc', NSPI_HANDLE),
		('Reserved', DWORD),
		('pStat', STAT),
		('pPropTags', PROPERTYTAGARRAY_R),
		('paWStr', WSTRINGSARRAY_R),
    )

class NspiResolveNamesWResponse(NDRCALL):
    structure = (
		('ppMIds', PROPERTYTAGARRAY_R),
		('ppRows', PROPERTYROWSET_R),
    )
        
OPNUMS = {
0 : (NspiBind,NspiBindResponse),
1 : (NspiUnbind,NspiUnbindResponse),
2 : (NspiUpdateStat,NspiUpdateStatResponse),
3 : (NspiQueryRows,NspiQueryRowsResponse),
4 : (NspiSeekEntries,NspiSeekEntriesResponse),
5 : (NspiGetMatches,NspiGetMatchesResponse),
6 : (NspiResortRestriction,NspiResortRestrictionResponse),
7 : (NspiDNToMId,NspiDNToMIdResponse),
8 : (NspiGetPropList,NspiGetPropListResponse),
9 : (NspiGetProps,NspiGetPropsResponse),
10 : (NspiCompareMIds,NspiCompareMIdsResponse),
11 : (NspiModProps,NspiModPropsResponse),
12 : (NspiGetSpecialTable,NspiGetSpecialTableResponse),
13 : (NspiGetTemplateInfo,NspiGetTemplateInfoResponse),
14 : (NspiModLinkAtt,NspiModLinkAttResponse),
15 : (Opnum15NotUsedOnWire,Opnum15NotUsedOnWireResponse),
16 : (NspiQueryColumns,NspiQueryColumnsResponse),
17 : (NspiGetNamesFromIDs,NspiGetNamesFromIDsResponse),
18 : (NspiGetIDsFromNames,NspiGetIDsFromNamesResponse),
19 : (NspiResolveNames,NspiResolveNamesResponse),
20 : (NspiResolveNamesW,NspiResolveNamesWResponse),
}

