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

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#drsuapi Definition

#################################################################################

MSRPC_UUID_DRSUAPI = uuidtup_to_bin(('e3514235-406-111-ab04-0004c2dcd2','0.0'))

DSTIME = LONGLONG
DRS_HANDLE = VOID

class NT4SID(NDRSTRUCT):
    structure = (
        ('Data', CHAR),
    )


class DSNAME(NDRSTRUCT):
    structure = (
        ('structLen', UNSIGNED_LONG),('SidLen', UNSIGNED_LONG),('Guid', GUID),('Sid', NT4SID),('NameLen', UNSIGNED_LONG),('StringName', WCHAR),
    )

USN = LONGLONG

class USN_VECTOR(NDRSTRUCT):
    structure = (
        ('usnHighObjUpdate', USN),('usnReserved', USN),('usnHighPropUpdate', USN),
    )


class UPTODATE_CURSOR_V1(NDRSTRUCT):
    structure = (
        ('uuidDsa', UUID),('usnHighPropUpdate', USN),
    )


class UPTODATE_VECTOR_V1_EXT(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwReserved1', DWORD),('cNumCursors', DWORD),('dwReserved2', DWORD),('rgCursors', UPTODATE_CURSOR_V1),
    )


class DATA_OID_T(NDRUniConformantArray):
    item = BYTE

class PTR_OID_T(NDRPOINTER):
    referent = (
        ('Data', DATA_OID_T),
    )

class OID_T(NDRSTRUCT):
    structure = (
	('length', UNSIGNED_INT),	('elements', PTR_OID_T),

    )
        

class PREFIXTABLEENTRY(NDRSTRUCT):
    structure = (
        ('ndx', UNSIGNED_LONG),('prefix', OID_T),
    )


class DATA_SCHEMA_PREFIX_TABLE(NDRUniConformantArray):
    item = PREFIXTABLEENTRY

class PTR_SCHEMA_PREFIX_TABLE(NDRPOINTER):
    referent = (
        ('Data', DATA_SCHEMA_PREFIX_TABLE),
    )

class SCHEMA_PREFIX_TABLE(NDRSTRUCT):
    structure = (
	('PrefixCount', DWORD),	('pPrefixEntry', PTR_SCHEMA_PREFIX_TABLE),

    )
        
ATTRTYP = ULONG

class PARTIAL_ATTR_VECTOR_V1_EXT(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwReserved1', DWORD),('cAttrs', DWORD),('rgPartialAttr', ATTRTYP),
    )


class MTX_ADDR(NDRSTRUCT):
    structure = (
        ('mtx_namelen', UNSIGNED_LONG),('mtx_name', CHAR),
    )


class DATA_ATTRVAL(NDRUniConformantArray):
    item = UCHAR

class PTR_ATTRVAL(NDRPOINTER):
    referent = (
        ('Data', DATA_ATTRVAL),
    )

class ATTRVAL(NDRSTRUCT):
    structure = (
	('valLen', ULONG),	('pVal', PTR_ATTRVAL),

    )
        

class DATA_ATTRVALBLOCK(NDRUniConformantArray):
    item = ATTRVAL

class PTR_ATTRVALBLOCK(NDRPOINTER):
    referent = (
        ('Data', DATA_ATTRVALBLOCK),
    )

class ATTRVALBLOCK(NDRSTRUCT):
    structure = (
	('valCount', ULONG),	('pAVal', PTR_ATTRVALBLOCK),

    )
        

class ATTR(NDRSTRUCT):
    structure = (
        ('attrTyp', ATTRTYP),('AttrVal', ATTRVALBLOCK),
    )


class DATA_ATTRBLOCK(NDRUniConformantArray):
    item = ATTR

class PTR_ATTRBLOCK(NDRPOINTER):
    referent = (
        ('Data', DATA_ATTRBLOCK),
    )

class ATTRBLOCK(NDRSTRUCT):
    structure = (
	('attrCount', ULONG),	('pAttr', PTR_ATTRBLOCK),

    )
        

class ENTINF(NDRSTRUCT):
    structure = (
        ('pName', DSNAME),('ulFlags', UNSIGNED_LONG),('AttrBlock', ATTRBLOCK),
    )


class PROPERTY_META_DATA_EXT(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('timeChanged', DSTIME),('uuidDsaOriginating', UUID),('usnOriginating', USN),
    )


class PROPERTY_META_DATA_EXT_VECTOR(NDRSTRUCT):
    structure = (
        ('cNumProps', DWORD),('rgMetaData', PROPERTY_META_DATA_EXT),
    )


class PNEXTENTINF(NDRSTRUCT):
    structure = (
        
    )


class REPLENTINFLIST(NDRSTRUCT):
    structure = (
        ('PNEXTENTINF', PNEXTENTINF),('Entinf', ENTINF),('fIsNCPrefix', BOOL),('pParentGuid', UUID),('pMetaDataExt', PROPERTY_META_DATA_EXT_VECTOR),
    )


class UPTODATE_CURSOR_V2(NDRSTRUCT):
    structure = (
        ('uuidDsa', UUID),('usnHighPropUpdate', USN),('timeLastSyncSuccess', DSTIME),
    )


class UPTODATE_VECTOR_V2_EXT(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwReserved1', DWORD),('cNumCursors', DWORD),('dwReserved2', DWORD),('rgCursors', UPTODATE_CURSOR_V2),
    )


class VALUE_META_DATA_EXT_V1(NDRSTRUCT):
    structure = (
        ('timeCreated', DSTIME),('MetaData', PROPERTY_META_DATA_EXT),
    )


class VALUE_META_DATA_EXT_V3(NDRSTRUCT):
    structure = (
        ('timeCreated', DSTIME),('MetaData', PROPERTY_META_DATA_EXT),('unused1', DWORD),('unused2', DWORD),('unused3', DWORD),('timeExpired', DSTIME),
    )


class REPLVALINF_V1(NDRSTRUCT):
    structure = (
        ('pObject', DSNAME),('attrTyp', ATTRTYP),('Aval', ATTRVAL),('fIsPresent', BOOL),('MetaData', VALUE_META_DATA_EXT_V1),
    )


class REPLVALINF_V3(NDRSTRUCT):
    structure = (
        ('pObject', DSNAME),('attrTyp', ATTRTYP),('Aval', ATTRVAL),('fIsPresent', BOOL),('MetaData', VALUE_META_DATA_EXT_V3),
    )


class REPLTIMES(NDRSTRUCT):
    structure = (
        ('rgTimes', UCHAR),
    )


class DS_NAME_RESULT_ITEMW(NDRSTRUCT):
    structure = (
        ('status', DWORD),('pDomain', WCHAR),('pName', WCHAR),
    )
class PDS_NAME_RESULT_ITEMW(NDRPOINTER):
    referent = (
        ('Data', DS_NAME_RESULT_ITEMW),
    )    


class DS_NAME_RESULTW(NDRSTRUCT):
    structure = (
        ('cItems', DWORD),('rItems', PDS_NAME_RESULT_ITEMW),
    )
class PDS_NAME_RESULTW(NDRPOINTER):
    referent = (
        ('Data', DS_NAME_RESULTW),
    )    


class DS_DOMAIN_CONTROLLER_INFO_1W(NDRSTRUCT):
    structure = (
        ('NetbiosName', WCHAR),('DnsHostName', WCHAR),('SiteName', WCHAR),('ComputerObjectName', WCHAR),('ServerObjectName', WCHAR),('fIsPdc', BOOL),('fDsEnabled', BOOL),
    )


class DS_DOMAIN_CONTROLLER_INFO_2W(NDRSTRUCT):
    structure = (
        ('NetbiosName', WCHAR),('DnsHostName', WCHAR),('SiteName', WCHAR),('SiteObjectName', WCHAR),('ComputerObjectName', WCHAR),('ServerObjectName', WCHAR),('NtdsDsaObjectName', WCHAR),('fIsPdc', BOOL),('fDsEnabled', BOOL),('fIsGc', BOOL),('SiteObjectGuid', GUID),('ComputerObjectGuid', GUID),('ServerObjectGuid', GUID),('NtdsDsaObjectGuid', GUID),
    )


class DS_DOMAIN_CONTROLLER_INFO_3W(NDRSTRUCT):
    structure = (
        ('NetbiosName', WCHAR),('DnsHostName', WCHAR),('SiteName', WCHAR),('SiteObjectName', WCHAR),('ComputerObjectName', WCHAR),('ServerObjectName', WCHAR),('NtdsDsaObjectName', WCHAR),('fIsPdc', BOOL),('fDsEnabled', BOOL),('fIsGc', BOOL),('fIsRodc', BOOL),('SiteObjectGuid', GUID),('ComputerObjectGuid', GUID),('ServerObjectGuid', GUID),('NtdsDsaObjectGuid', GUID),
    )


class DS_DOMAIN_CONTROLLER_INFO_FFFFFFFFW(NDRSTRUCT):
    structure = (
        ('IPAddress', DWORD),('NotificationCount', DWORD),('secTimeConnected', DWORD),('Flags', DWORD),('TotalRequests', DWORD),('Reserved1', DWORD),('UserName', WCHAR),
    )


class PNEXTENTINF(NDRSTRUCT):
    structure = (
        
    )


class ENTINFLIST(NDRSTRUCT):
    structure = (
        ('PNEXTENTINF', PNEXTENTINF),('Entinf', ENTINF),
    )


class INTFORMPROB_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),('type', ATTRTYP),('valReturned', BOOL),('Val', ATTRVAL),
    )


class PNEXTPROBLEM(NDRSTRUCT):
    structure = (
        
    )


class PROBLEMLIST_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('PNEXTPROBLEM', PNEXTPROBLEM),('intprob', INTFORMPROB_DRS_WIRE_V1),
    )


class ATRERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('pObject', DSNAME),('count', ULONG),('FirstProblem', PROBLEMLIST_DRS_WIRE_V1),
    )


class NAMERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),('pMatched', DSNAME),
    )


class NAMERESOP_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('nameRes', UCHAR),('unusedPad', UCHAR),('nextRDN', USHORT),
    )


class PNEXTADDRESS(NDRSTRUCT):
    structure = (
        
    )


class DSA_ADDRESS_LIST_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('PNEXTADDRESS', PNEXTADDRESS),('pAddress', RPC_UNICODE_STRING),
    )


class PNEXTCONTREF(NDRSTRUCT):
    structure = (
        
    )


class CONTREF_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('pTarget', DSNAME),('OpState', NAMERESOP_DRS_WIRE_V1),('aliasRDN', USHORT),('RDNsInternal', USHORT),('refType', USHORT),('count', USHORT),('pDAL', DSA_ADDRESS_LIST_DRS_WIRE_V1),('PNEXTCONTREF', PNEXTCONTREF),('bNewChoice', BOOL),('choice', UCHAR),
    )


class REFERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('Refer', CONTREF_DRS_WIRE_V1),
    )


class SECERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),
    )


class SVCERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),
    )


class UPDERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),
    )


class SYSERR_DRS_WIRE_V1(NDRSTRUCT):
    structure = (
        ('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),
    )


class DIRERR_DRS_WIRE_V1(NDRUNION):
    union = {
        1: ('AtrErr',ATRERR_DRS_WIRE_V1),2: ('NamErr',NAMERR_DRS_WIRE_V1),3: ('RefErr',REFERR_DRS_WIRE_V1),4: ('SecErr',SECERR_DRS_WIRE_V1),5: ('SvcErr',SVCERR_DRS_WIRE_V1),6: ('UpdErr',UPDERR_DRS_WIRE_V1),7: ('SysErr',SYSERR_DRS_WIRE_V1),
    }
        

class DS_REPL_NEIGHBORW(NDRSTRUCT):
    structure = (
        ('pszNamingContext', LPWSTR),('pszSourceDsaDN', LPWSTR),('pszSourceDsaAddress', LPWSTR),('pszAsyncIntersiteTransportDN', LPWSTR),('dwReplicaFlags', DWORD),('dwReserved', DWORD),('uuidNamingContextObjGuid', UUID),('uuidSourceDsaObjGuid', UUID),('uuidSourceDsaInvocationID', UUID),('uuidAsyncIntersiteTransportObjGuid', UUID),('usnLastObjChangeSynced', USN),('usnAttributeFilter', USN),('ftimeLastSyncSuccess', FILETIME),('ftimeLastSyncAttempt', FILETIME),('dwLastSyncResult', DWORD),('cNumConsecutiveSyncFailures', DWORD),
    )


class DS_REPL_NEIGHBORSW(NDRSTRUCT):
    structure = (
        ('cNumNeighbors', DWORD),('dwReserved', DWORD),('rgNeighbor', DS_REPL_NEIGHBORW),
    )


class DS_REPL_CURSOR(NDRSTRUCT):
    structure = (
        ('uuidSourceDsaInvocationID', UUID),('usnAttributeFilter', USN),
    )


class DS_REPL_CURSORS(NDRSTRUCT):
    structure = (
        ('cNumCursors', DWORD),('dwReserved', DWORD),('rgCursor', DS_REPL_CURSOR),
    )


class DS_REPL_ATTR_META_DATA(NDRSTRUCT):
    structure = (
        ('pszAttributeName', LPWSTR),('dwVersion', DWORD),('ftimeLastOriginatingChange', FILETIME),('uuidLastOriginatingDsaInvocationID', UUID),('usnOriginatingChange', USN),('usnLocalChange', USN),
    )


class DS_REPL_KCC_DSA_FAILUREW(NDRSTRUCT):
    structure = (
        ('pszDsaDN', LPWSTR),('uuidDsaObjGuid', UUID),('ftimeFirstFailure', FILETIME),('cNumFailures', DWORD),('dwLastResult', DWORD),
    )


class DS_REPL_KCC_DSA_FAILURESW(NDRSTRUCT):
    structure = (
        ('cNumEntries', DWORD),('dwReserved', DWORD),('rgDsaFailure', DS_REPL_KCC_DSA_FAILUREW),
    )


class DS_REPL_OBJ_META_DATA(NDRSTRUCT):
    structure = (
        ('cNumEntries', DWORD),('dwReserved', DWORD),('rgMetaData', DS_REPL_ATTR_META_DATA),
    )


DS_REPL_OP_TYPE_SYNC = 0,
DS_REPL_OP_TYPE_ADD = 0,
DS_REPL_OP_TYPE_DELETE = 0,
DS_REPL_OP_TYPE_MODIFY = 0
        

class DS_REPL_OPW(NDRSTRUCT):
    structure = (
        ('ftimeEnqueued', FILETIME),('ulSerialNumber', ULONG),('ulPriority', ULONG),('OpType', DS_REPL_OP_TYPE),('ulOptions', ULONG),('pszNamingContext', LPWSTR),('pszDsaDN', LPWSTR),('pszDsaAddress', LPWSTR),('uuidNamingContextObjGuid', UUID),('uuidDsaObjGuid', UUID),
    )


class DS_REPL_PENDING_OPSW(NDRSTRUCT):
    structure = (
        ('ftimeCurrentOpStarted', FILETIME),('cNumPendingOps', DWORD),('rgPendingOp', DS_REPL_OPW),
    )


class DATA_DS_REPL_VALUE_META_DATA(NDRUniConformantArray):
    item = BYTE

class PTR_DS_REPL_VALUE_META_DATA(NDRPOINTER):
    referent = (
        ('Data', DATA_DS_REPL_VALUE_META_DATA),
    )

class DS_REPL_VALUE_META_DATA(NDRSTRUCT):
    structure = (
	('pszAttributeName', LPWSTR),	('pszObjectDn', LPWSTR),	('cbData', DWORD),	('pbData', PTR_DS_REPL_VALUE_META_DATA),
	('ftimeDeleted', FILETIME),	('ftimeCreated', FILETIME),	('dwVersion', DWORD),	('ftimeLastOriginatingChange', FILETIME),	('uuidLastOriginatingDsaInvocationID', UUID),	('usnOriginatingChange', USN),	('usnLocalChange', USN),
    )
        

class DS_REPL_ATTR_VALUE_META_DATA(NDRSTRUCT):
    structure = (
        ('cNumEntries', DWORD),('dwEnumerationContext', DWORD),('rgMetaData', DS_REPL_VALUE_META_DATA),
    )


class DS_REPL_CURSOR_2(NDRSTRUCT):
    structure = (
        ('uuidSourceDsaInvocationID', UUID),('usnAttributeFilter', USN),('ftimeLastSyncSuccess', FILETIME),
    )


class DS_REPL_CURSORS_2(NDRSTRUCT):
    structure = (
        ('cNumCursors', DWORD),('dwEnumerationContext', DWORD),('rgCursor', DS_REPL_CURSOR_2),
    )


class DS_REPL_CURSOR_3W(NDRSTRUCT):
    structure = (
        ('uuidSourceDsaInvocationID', UUID),('usnAttributeFilter', USN),('ftimeLastSyncSuccess', FILETIME),('pszSourceDsaDN', LPWSTR),
    )


class DS_REPL_CURSORS_3W(NDRSTRUCT):
    structure = (
        ('cNumCursors', DWORD),('dwEnumerationContext', DWORD),('rgCursor', DS_REPL_CURSOR_3W),
    )


class DS_REPL_ATTR_META_DATA_2(NDRSTRUCT):
    structure = (
        ('pszAttributeName', LPWSTR),('dwVersion', DWORD),('ftimeLastOriginatingChange', FILETIME),('uuidLastOriginatingDsaInvocationID', UUID),('usnOriginatingChange', USN),('usnLocalChange', USN),('pszLastOriginatingDsaDN', LPWSTR),
    )


class DS_REPL_OBJ_META_DATA_2(NDRSTRUCT):
    structure = (
        ('cNumEntries', DWORD),('dwReserved', DWORD),('rgMetaData', DS_REPL_ATTR_META_DATA_2),
    )


class DATA_DS_REPL_VALUE_META_DATA_2(NDRUniConformantArray):
    item = BYTE

class PTR_DS_REPL_VALUE_META_DATA_2(NDRPOINTER):
    referent = (
        ('Data', DATA_DS_REPL_VALUE_META_DATA_2),
    )

class DS_REPL_VALUE_META_DATA_2(NDRSTRUCT):
    structure = (
	('pszAttributeName', LPWSTR),	('pszObjectDn', LPWSTR),	('cbData', DWORD),	('pbData', PTR_DS_REPL_VALUE_META_DATA_2),
	('ftimeDeleted', FILETIME),	('ftimeCreated', FILETIME),	('dwVersion', DWORD),	('ftimeLastOriginatingChange', FILETIME),	('uuidLastOriginatingDsaInvocationID', UUID),	('usnOriginatingChange', USN),	('usnLocalChange', USN),	('pszLastOriginatingDsaDN', LPWSTR),
    )
        

class DS_REPL_ATTR_VALUE_META_DATA_2(NDRSTRUCT):
    structure = (
        ('cNumEntries', DWORD),('dwEnumerationContext', DWORD),('rgMetaData', DS_REPL_VALUE_META_DATA_2),
    )


class DRS_EXTENSIONS(NDRSTRUCT):
    structure = (
        ('cb', DWORD),('rgb', BYTE),
    )


class DRS_MSG_GETCHGREQ_V3(NDRSTRUCT):
    structure = (
        ('uuidDsaObjDest', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('pUpToDateVecDestV1', UPTODATE_VECTOR_V1_EXT),('pPartialAttrVecDestV1', PARTIAL_ATTR_VECTOR_V1_EXT),('PrefixTableDest', SCHEMA_PREFIX_TABLE),('ulFlags', ULONG),('cMaxObjects', ULONG),('cMaxBytes', ULONG),('ulExtendedOp', ULONG),
    )


class DRS_MSG_GETCHGREQ_V4(NDRSTRUCT):
    structure = (
        ('uuidTransportObj', UUID),('pmtxReturnAddress', MTX_ADDR),('V3', DRS_MSG_GETCHGREQ_V3),
    )


class DRS_MSG_GETCHGREQ_V7(NDRSTRUCT):
    structure = (
        ('uuidTransportObj', UUID),('pmtxReturnAddress', MTX_ADDR),('V3', DRS_MSG_GETCHGREQ_V3),('pPartialAttrSet', PARTIAL_ATTR_VECTOR_V1_EXT),('pPartialAttrSetEx', PARTIAL_ATTR_VECTOR_V1_EXT),('PrefixTableDest', SCHEMA_PREFIX_TABLE),
    )


class DRS_MSG_GETCHGREPLY_V1(NDRSTRUCT):
    structure = (
        ('uuidDsaObjSrc', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('usnvecTo', USN_VECTOR),('pUpToDateVecSrcV1', UPTODATE_VECTOR_V1_EXT),('PrefixTableSrc', SCHEMA_PREFIX_TABLE),('ulExtendedRet', ULONG),('cNumObjects', ULONG),('cNumBytes', ULONG),('pObjects', REPLENTINFLIST),('fMoreData', BOOL),
    )


class DATA_DRS_MSG_GETCHGREPLY_V6(NDRUniConformantArray):
    item = REPLVALINF_V1

class PTR_DRS_MSG_GETCHGREPLY_V6(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_GETCHGREPLY_V6),
    )

class DRS_MSG_GETCHGREPLY_V6(NDRSTRUCT):
    structure = (
	('uuidDsaObjSrc', UUID),	('uuidInvocIdSrc', UUID),	('pNC', DSNAME),	('usnvecFrom', USN_VECTOR),	('usnvecTo', USN_VECTOR),	('pUpToDateVecSrc', UPTODATE_VECTOR_V2_EXT),	('PrefixTableSrc', SCHEMA_PREFIX_TABLE),	('ulExtendedRet', ULONG),	('cNumObjects', ULONG),	('cNumBytes', ULONG),	('pObjects', REPLENTINFLIST),	('fMoreData', BOOL),	('cNumNcSizeObjects', ULONG),	('cNumNcSizeValues', ULONG),	('cNumValues', DWORD),	('rgValues', PTR_DRS_MSG_GETCHGREPLY_V6),
	('dwDRSError', DWORD),
    )
        

class DATA_DRS_MSG_GETCHGREPLY_V9(NDRUniConformantArray):
    item = REPLVALINF_V3

class PTR_DRS_MSG_GETCHGREPLY_V9(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_GETCHGREPLY_V9),
    )

class DRS_MSG_GETCHGREPLY_V9(NDRSTRUCT):
    structure = (
	('uuidDsaObjSrc', UUID),	('uuidInvocIdSrc', UUID),	('pNC', DSNAME),	('usnvecFrom', USN_VECTOR),	('usnvecTo', USN_VECTOR),	('pUpToDateVecSrc', UPTODATE_VECTOR_V2_EXT),	('PrefixTableSrc', SCHEMA_PREFIX_TABLE),	('ulExtendedRet', ULONG),	('cNumObjects', ULONG),	('cNumBytes', ULONG),	('pObjects', REPLENTINFLIST),	('fMoreData', BOOL),	('cNumNcSizeObjects', ULONG),	('cNumNcSizeValues', ULONG),	('cNumValues', DWORD),	('rgValues', PTR_DRS_MSG_GETCHGREPLY_V9),
	('dwDRSError', DWORD),
    )
        

class DATA_DRS_COMPRESSED_BLOB(NDRUniConformantArray):
    item = BYTE

class PTR_DRS_COMPRESSED_BLOB(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_COMPRESSED_BLOB),
    )

class DRS_COMPRESSED_BLOB(NDRSTRUCT):
    structure = (
	('cbUncompressedSize', DWORD),	('cbCompressedSize', DWORD),	('pbCompressedData', PTR_DRS_COMPRESSED_BLOB),

    )
        

class DRS_MSG_GETCHGREQ_V5(NDRSTRUCT):
    structure = (
        ('uuidDsaObjDest', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('pUpToDateVecDestV1', UPTODATE_VECTOR_V1_EXT),('ulFlags', ULONG),('cMaxObjects', ULONG),('cMaxBytes', ULONG),('ulExtendedOp', ULONG),('liFsmoInfo', ULARGE_INTEGER),
    )


class DRS_MSG_GETCHGREQ_V8(NDRSTRUCT):
    structure = (
        ('uuidDsaObjDest', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('pUpToDateVecDest', UPTODATE_VECTOR_V1_EXT),('ulFlags', ULONG),('cMaxObjects', ULONG),('cMaxBytes', ULONG),('ulExtendedOp', ULONG),('liFsmoInfo', ULARGE_INTEGER),('pPartialAttrSet', PARTIAL_ATTR_VECTOR_V1_EXT),('pPartialAttrSetEx', PARTIAL_ATTR_VECTOR_V1_EXT),('PrefixTableDest', SCHEMA_PREFIX_TABLE),
    )


class DRS_MSG_GETCHGREQ_V10(NDRSTRUCT):
    structure = (
        ('uuidDsaObjDest', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('pUpToDateVecDest', UPTODATE_VECTOR_V1_EXT),('ulFlags', ULONG),('cMaxObjects', ULONG),('cMaxBytes', ULONG),('ulExtendedOp', ULONG),('liFsmoInfo', ULARGE_INTEGER),('pPartialAttrSet', PARTIAL_ATTR_VECTOR_V1_EXT),('pPartialAttrSetEx', PARTIAL_ATTR_VECTOR_V1_EXT),('PrefixTableDest', SCHEMA_PREFIX_TABLE),('ulMoreFlags', ULONG),
    )


class VAR_SIZE_BUFFER_WITH_VERSION(NDRSTRUCT):
    structure = (
        ('ulVersion', ULONG),('cbByteBuffer', ULONG),('ullPadding', ULONGLONG),('rgbBuffer', BYTE),
    )


class DRS_MSG_GETCHGREQ_V11(NDRSTRUCT):
    structure = (
        ('uuidDsaObjDest', UUID),('uuidInvocIdSrc', UUID),('pNC', DSNAME),('usnvecFrom', USN_VECTOR),('pUpToDateVecDest', UPTODATE_VECTOR_V1_EXT),('ulFlags', ULONG),('cMaxObjects', ULONG),('cMaxBytes', ULONG),('ulExtendedOp', ULONG),('liFsmoInfo', ULARGE_INTEGER),('pPartialAttrSet', PARTIAL_ATTR_VECTOR_V1_EXT),('pPartialAttrSetEx', PARTIAL_ATTR_VECTOR_V1_EXT),('PrefixTableDest', SCHEMA_PREFIX_TABLE),('ulMoreFlags', ULONG),('correlationID', GUID),('pReservedBuffer', VAR_SIZE_BUFFER_WITH_VERSION),
    )


class DRS_MSG_GETCHGREQ(NDRUNION):
    union = {
        4: ('V4',DRS_MSG_GETCHGREQ_V4),5: ('V5',DRS_MSG_GETCHGREQ_V5),7: ('V7',DRS_MSG_GETCHGREQ_V7),8: ('V8',DRS_MSG_GETCHGREQ_V8),10: ('V10',DRS_MSG_GETCHGREQ_V10),11: ('V11',DRS_MSG_GETCHGREQ_V11),
    }
        

class DRS_MSG_GETCHGREPLY_V2(NDRSTRUCT):
    structure = (
        ('CompressedV1', DRS_COMPRESSED_BLOB),
    )


DRS_COMP_ALG_NONE = 0,
DRS_COMP_ALG_UNUSED = 1,
DRS_COMP_ALG_MSZIP = 2,
DRS_COMP_ALG_WIN2K3 = 3
        

class DRS_MSG_GETCHGREPLY_V7(NDRSTRUCT):
    structure = (
        ('dwCompressedVersion', DWORD),('CompressionAlg', DRS_COMP_ALG_TYPE),('CompressedAny', DRS_COMPRESSED_BLOB),
    )


class DRS_MSG_GETCHGREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_GETCHGREPLY_V1),2: ('V2',DRS_MSG_GETCHGREPLY_V2),6: ('V6',DRS_MSG_GETCHGREPLY_V6),7: ('V7',DRS_MSG_GETCHGREPLY_V7),9: ('V9',DRS_MSG_GETCHGREPLY_V9),
    }
        

class DRS_MSG_REPSYNC_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('uuidDsaSrc', UUID),('pszDsaSrc', CHAR),('ulOptions', ULONG),
    )


class DRS_MSG_REPSYNC_V2(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('uuidDsaSrc', UUID),('pszDsaSrc', CHAR),('ulOptions', ULONG),('correlationID', GUID),('pReservedBuffer', VAR_SIZE_BUFFER_WITH_VERSION),
    )


class DRS_MSG_REPSYNC(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPSYNC_V1),2: ('V2',DRS_MSG_REPSYNC_V2),
    }
        

class DRS_MSG_UPDREFS_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pszDsaDest', CHAR),('uuidDsaObjDest', UUID),('ulOptions', ULONG),
    )


class DRS_MSG_UPDREFS_V2(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pszDsaDest', CHAR),('uuidDsaObjDest', UUID),('ulOptions', ULONG),('correlationID', GUID),('pReservedBuffer', VAR_SIZE_BUFFER_WITH_VERSION),
    )


class DRS_MSG_UPDREFS(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_UPDREFS_V1),2: ('V2',DRS_MSG_UPDREFS_V2),
    }
        

class DRS_MSG_REPADD_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pszDsaSrc', CHAR),('rtSchedule', REPLTIMES),('ulOptions', ULONG),
    )


class DRS_MSG_REPADD_V2(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pSourceDsaDN', DSNAME),('pTransportDN', DSNAME),('pszSourceDsaAddress', CHAR),('rtSchedule', REPLTIMES),('ulOptions', ULONG),
    )


class DRS_MSG_REPADD_V3(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pSourceDsaDN', DSNAME),('pTransportDN', DSNAME),('pszSourceDsaAddress', CHAR),('rtSchedule', REPLTIMES),('ulOptions', ULONG),('correlationID', GUID),('pReservedBuffer', VAR_SIZE_BUFFER_WITH_VERSION),
    )


class DRS_MSG_REPADD(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPADD_V1),2: ('V2',DRS_MSG_REPADD_V2),3: ('V3',DRS_MSG_REPADD_V3),
    }
        

class DRS_MSG_REPDEL_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('pszDsaSrc', CHAR),('ulOptions', ULONG),
    )


class DRS_MSG_REPDEL(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPDEL_V1),
    }
        

class DRS_MSG_REPMOD_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('uuidSourceDRA', UUID),('pszSourceDRA', CHAR),('rtSchedule', REPLTIMES),('ulReplicaFlags', ULONG),('ulModifyFields', ULONG),('ulOptions', ULONG),
    )


class DRS_MSG_REPMOD(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPMOD_V1),
    }
        

class DATA_DRS_MSG_VERIFYREQ_V1(NDRUniConformantArray):
    item = DSNAME

class PTR_DRS_MSG_VERIFYREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_VERIFYREQ_V1),
    )

class DRS_MSG_VERIFYREQ_V1(NDRSTRUCT):
    structure = (
	('dwFlags', DWORD),	('cNames', DWORD),	('rpNames', PTR_DRS_MSG_VERIFYREQ_V1),
	('RequiredAttrs', ATTRBLOCK),	('PrefixTable', SCHEMA_PREFIX_TABLE),
    )
        

class DRS_MSG_VERIFYREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_VERIFYREQ_V1),
    }
        

class DATA_DRS_MSG_VERIFYREPLY_V1(NDRUniConformantArray):
    item = ENTINF

class PTR_DRS_MSG_VERIFYREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_VERIFYREPLY_V1),
    )

class DRS_MSG_VERIFYREPLY_V1(NDRSTRUCT):
    structure = (
	('error', DWORD),	('cNames', DWORD),	('rpEntInf', PTR_DRS_MSG_VERIFYREPLY_V1),
	('PrefixTable', SCHEMA_PREFIX_TABLE),
    )
        

class DRS_MSG_VERIFYREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_VERIFYREPLY_V1),
    }
        

RevMembGetGroupsForUser = 1,
RevMembGetAliasMembership = 1,
RevMembGetAccountGroups = 1,
RevMembGetResourceGroups = 1,
RevMembGetUniversalGroups = 1,
GroupMembersTransitive = 1
        

class DATA_DRS_MSG_REVMEMB_REQ_V1(NDRUniConformantArray):
    item = DSNAME

class PTR_DRS_MSG_REVMEMB_REQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_REVMEMB_REQ_V1),
    )

class DRS_MSG_REVMEMB_REQ_V1(NDRSTRUCT):
    structure = (
	('cDsNames', ULONG),	('ppDsNames', PTR_DRS_MSG_REVMEMB_REQ_V1),
	('dwFlags', DWORD),	('OperationType', REVERSE_MEMBERSHIP_OPERATION_TYPE),	('pLimitingDomain', DSNAME),
    )
        

class DRS_MSG_REVMEMB_REQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REVMEMB_REQ_V1),
    }
        

class DATA_DRS_MSG_REVMEMB_REPLY_V1(NDRUniConformantArray):
    item = NT4SID

class PTR_DRS_MSG_REVMEMB_REPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_REVMEMB_REPLY_V1),
    )

class DRS_MSG_REVMEMB_REPLY_V1(NDRSTRUCT):
    structure = (
	('errCode', ULONG),	('cDsNames', ULONG),	('cSidHistory', ULONG),	('ppDsNames', DSNAME),	('pAttributes', DWORD),	('ppSidHistory', PTR_DRS_MSG_REVMEMB_REPLY_V1),

    )
        

class DRS_MSG_REVMEMB_REPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REVMEMB_REPLY_V1),
    }
        

class DRS_MSG_MOVEREQ_V1(NDRSTRUCT):
    structure = (
        ('pSourceDSA', CHAR),('pObject', ENTINF),('pParentUUID', UUID),('PrefixTable', SCHEMA_PREFIX_TABLE),('ulFlags', ULONG),
    )


class DATA_DRS_SECBUFFER(NDRUniConformantArray):
    item = BYTE

class PTR_DRS_SECBUFFER(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_SECBUFFER),
    )

class DRS_SECBUFFER(NDRSTRUCT):
    structure = (
	('cbBuffer', UNSIGNED_LONG),	('BufferType', UNSIGNED_LONG),	('pvBuffer', PTR_DRS_SECBUFFER),

    )
        

class DATA_DRS_SECBUFFERDESC(NDRUniConformantArray):
    item = DRS_SECBUFFER

class PTR_DRS_SECBUFFERDESC(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_SECBUFFERDESC),
    )

class DRS_SECBUFFERDESC(NDRSTRUCT):
    structure = (
	('ulVersion', UNSIGNED_LONG),	('cBuffers', UNSIGNED_LONG),	('Buffers', PTR_DRS_SECBUFFERDESC),

    )
        

class DRS_MSG_MOVEREQ_V2(NDRSTRUCT):
    structure = (
        ('pSrcDSA', DSNAME),('pSrcObject', ENTINF),('pDstName', DSNAME),('pExpectedTargetNC', DSNAME),('pClientCreds', DRS_SECBUFFERDESC),('PrefixTable', SCHEMA_PREFIX_TABLE),('ulFlags', ULONG),
    )


class DRS_MSG_MOVEREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_MOVEREQ_V1),2: ('V2',DRS_MSG_MOVEREQ_V2),
    }
        

class DRS_MSG_MOVEREPLY_V1(NDRSTRUCT):
    structure = (
        ('ppResult', ENTINF),('PrefixTable', SCHEMA_PREFIX_TABLE),('pError', ULONG),
    )


class DRS_MSG_MOVEREPLY_V2(NDRSTRUCT):
    structure = (
        ('win32Error', ULONG),('pAddedName', DSNAME),
    )


class DRS_MSG_MOVEREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_MOVEREPLY_V1),2: ('V2',DRS_MSG_MOVEREPLY_V2),
    }
        

class DATA_DRS_MSG_CRACKREQ_V1(NDRUniConformantArray):
    item = WCHAR

class PTR_DRS_MSG_CRACKREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_CRACKREQ_V1),
    )

class DRS_MSG_CRACKREQ_V1(NDRSTRUCT):
    structure = (
	('CodePage', ULONG),	('LocaleId', ULONG),	('dwFlags', DWORD),	('formatOffered', DWORD),	('formatDesired', DWORD),	('cNames', DWORD),	('rpNames', PTR_DRS_MSG_CRACKREQ_V1),

    )
        

class DRS_MSG_CRACKREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_CRACKREQ_V1),
    }
        

class DRS_MSG_CRACKREPLY_V1(NDRSTRUCT):
    structure = (
        ('pResult', DS_NAME_RESULTW),
    )


class DRS_MSG_CRACKREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_CRACKREPLY_V1),
    }
        

class DATA_DRS_MSG_NT4_CHGLOG_REQ_V1(NDRUniConformantArray):
    item = BYTE

class PTR_DRS_MSG_NT4_CHGLOG_REQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_NT4_CHGLOG_REQ_V1),
    )

class DRS_MSG_NT4_CHGLOG_REQ_V1(NDRSTRUCT):
    structure = (
	('dwFlags', DWORD),	('PreferredMaximumLength', DWORD),	('cbRestart', DWORD),	('pRestart', PTR_DRS_MSG_NT4_CHGLOG_REQ_V1),

    )
        

class DRS_MSG_NT4_CHGLOG_REQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_NT4_CHGLOG_REQ_V1),
    }
        

class NT4_REPLICATION_STATE(NDRSTRUCT):
    structure = (
        ('SamSerialNumber', LARGE_INTEGER),('SamCreationTime', LARGE_INTEGER),('BuiltinSerialNumber', LARGE_INTEGER),('BuiltinCreationTime', LARGE_INTEGER),('LsaSerialNumber', LARGE_INTEGER),('LsaCreationTime', LARGE_INTEGER),
    )


class DATA_DRS_MSG_NT4_CHGLOG_REPLY_V1(NDRUniConformantArray):
    item = BYTE

class PTR_DRS_MSG_NT4_CHGLOG_REPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_NT4_CHGLOG_REPLY_V1),
    )

class DRS_MSG_NT4_CHGLOG_REPLY_V1(NDRSTRUCT):
    structure = (
	('cbRestart', DWORD),	('cbLog', DWORD),	('ReplicationState', NT4_REPLICATION_STATE),	('ActualNtStatus', DWORD),	('pRestart', BYTE),	('pLog', PTR_DRS_MSG_NT4_CHGLOG_REPLY_V1),

    )
        

class DRS_MSG_NT4_CHGLOG_REPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_NT4_CHGLOG_REPLY_V1),
    }
        

class DATA_DRS_MSG_SPNREQ_V1(NDRUniConformantArray):
    item =  WCHAR

class PTR_DRS_MSG_SPNREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_SPNREQ_V1),
    )

class DRS_MSG_SPNREQ_V1(NDRSTRUCT):
    structure = (
	('operation', DWORD),	('flags', DWORD),	('pwszAccount',  WCHAR),	('cSPN', DWORD),	('rpwszSPN', PTR_DRS_MSG_SPNREQ_V1),

    )
        

class DRS_MSG_SPNREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_SPNREQ_V1),
    }
        

class DRS_MSG_SPNREPLY_V1(NDRSTRUCT):
    structure = (
        ('retVal', DWORD),
    )


class DRS_MSG_SPNREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_SPNREPLY_V1),
    }
        

class DRS_MSG_RMSVRREQ_V1(NDRSTRUCT):
    structure = (
        ('ServerDN', LPWSTR),('DomainDN', LPWSTR),('fCommit', BOOL),
    )


class DRS_MSG_RMSVRREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_RMSVRREQ_V1),
    }
        

class DRS_MSG_RMSVRREPLY_V1(NDRSTRUCT):
    structure = (
        ('fLastDcInDomain', BOOL),
    )


class DRS_MSG_RMSVRREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_RMSVRREPLY_V1),
    }
        

class DRS_MSG_RMDMNREQ_V1(NDRSTRUCT):
    structure = (
        ('DomainDN', LPWSTR),
    )


class DRS_MSG_RMDMNREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_RMDMNREQ_V1),
    }
        

class DRS_MSG_RMDMNREPLY_V1(NDRSTRUCT):
    structure = (
        ('Reserved', DWORD),
    )


class DRS_MSG_RMDMNREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_RMDMNREPLY_V1),
    }
        

class DRS_MSG_DCINFOREQ_V1(NDRSTRUCT):
    structure = (
        ('Domain', WCHAR),('InfoLevel', DWORD),
    )


class DRS_MSG_DCINFOREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_DCINFOREQ_V1),
    }
        class PDRS_MSG_DCINFOREQ(NDRPOINTER):
    referent = (
        ('Data', DRS_MSG_DCINFOREQ),
    )    


class DATA_DRS_MSG_DCINFOREPLY_V1(NDRUniConformantArray):
    item = DS_DOMAIN_CONTROLLER_INFO_1W

class PTR_DRS_MSG_DCINFOREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_DCINFOREPLY_V1),
    )

class DRS_MSG_DCINFOREPLY_V1(NDRSTRUCT):
    structure = (
	('cItems', DWORD),	('rItems', PTR_DRS_MSG_DCINFOREPLY_V1),

    )
        

class DATA_DRS_MSG_DCINFOREPLY_V2(NDRUniConformantArray):
    item = DS_DOMAIN_CONTROLLER_INFO_2W

class PTR_DRS_MSG_DCINFOREPLY_V2(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_DCINFOREPLY_V2),
    )

class DRS_MSG_DCINFOREPLY_V2(NDRSTRUCT):
    structure = (
	('cItems', DWORD),	('rItems', PTR_DRS_MSG_DCINFOREPLY_V2),

    )
        

class DATA_DRS_MSG_DCINFOREPLY_V3(NDRUniConformantArray):
    item = DS_DOMAIN_CONTROLLER_INFO_3W

class PTR_DRS_MSG_DCINFOREPLY_V3(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_DCINFOREPLY_V3),
    )

class DRS_MSG_DCINFOREPLY_V3(NDRSTRUCT):
    structure = (
	('cItems', DWORD),	('rItems', PTR_DRS_MSG_DCINFOREPLY_V3),

    )
        

class DATA_DRS_MSG_DCINFOREPLY_VFFFFFFFF(NDRUniConformantArray):
    item = DS_DOMAIN_CONTROLLER_INFO_FFFFFFFFW

class PTR_DRS_MSG_DCINFOREPLY_VFFFFFFFF(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_DCINFOREPLY_VFFFFFFFF),
    )

class DRS_MSG_DCINFOREPLY_VFFFFFFFF(NDRSTRUCT):
    structure = (
	('cItems', DWORD),	('rItems', PTR_DRS_MSG_DCINFOREPLY_VFFFFFFFF),

    )
        

class DRS_MSG_DCINFOREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_DCINFOREPLY_V1),2: ('V2',DRS_MSG_DCINFOREPLY_V2),3: ('V3',DRS_MSG_DCINFOREPLY_V3),0xFFFFFFFF: ('VFFFFFFFF',DRS_MSG_DCINFOREPLY_VFFFFFFFF),
    }
        

class DRS_MSG_ADDENTRYREQ_V1(NDRSTRUCT):
    structure = (
        ('pObject', DSNAME),('AttrBlock', ATTRBLOCK),
    )


class DRS_MSG_ADDENTRYREQ_V2(NDRSTRUCT):
    structure = (
        ('EntInfList', ENTINFLIST),
    )


class DRS_MSG_ADDENTRYREQ_V3(NDRSTRUCT):
    structure = (
        ('EntInfList', ENTINFLIST),('pClientCreds', DRS_SECBUFFERDESC),
    )


class DRS_MSG_ADDENTRYREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDENTRYREQ_V1),2: ('V2',DRS_MSG_ADDENTRYREQ_V2),3: ('V3',DRS_MSG_ADDENTRYREQ_V3),
    }
        

class DRS_MSG_ADDENTRYREPLY_V1(NDRSTRUCT):
    structure = (
        ('Guid', GUID),('Sid', NT4SID),('errCode', DWORD),('dsid', DWORD),('extendedErr', DWORD),('extendedData', DWORD),('problem', USHORT),
    )


class ADDENTRY_REPLY_INFO(NDRSTRUCT):
    structure = (
        ('objGuid', GUID),('objSid', NT4SID),
    )


class DATA_DRS_MSG_ADDENTRYREPLY_V2(NDRUniConformantArray):
    item = ADDENTRY_REPLY_INFO

class PTR_DRS_MSG_ADDENTRYREPLY_V2(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_ADDENTRYREPLY_V2),
    )

class DRS_MSG_ADDENTRYREPLY_V2(NDRSTRUCT):
    structure = (
	('pErrorObject', DSNAME),	('errCode', DWORD),	('dsid', DWORD),	('extendedErr', DWORD),	('extendedData', DWORD),	('problem', USHORT),	('cObjectsAdded', ULONG),	('infoList', PTR_DRS_MSG_ADDENTRYREPLY_V2),

    )
        

class DRS_ERROR_DATA_V1(NDRSTRUCT):
    structure = (
        ('dwRepError', DWORD),('errCode', DWORD),('pErrInfo', DIRERR_DRS_WIRE_V1),
    )


class DRS_ERROR_DATA(NDRUNION):
    union = {
        1: ('V1',DRS_ERROR_DATA_V1),
    }
        

class DATA_DRS_MSG_ADDENTRYREPLY_V3(NDRUniConformantArray):
    item = ADDENTRY_REPLY_INFO

class PTR_DRS_MSG_ADDENTRYREPLY_V3(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_ADDENTRYREPLY_V3),
    )

class DRS_MSG_ADDENTRYREPLY_V3(NDRSTRUCT):
    structure = (
	('pdsErrObject', DSNAME),	('dwErrVer', DWORD),	('pErrData', DRS_ERROR_DATA),	('cObjectsAdded', ULONG),	('infoList', PTR_DRS_MSG_ADDENTRYREPLY_V3),

    )
        

class DRS_MSG_ADDENTRYREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDENTRYREPLY_V1),2: ('V2',DRS_MSG_ADDENTRYREPLY_V2),3: ('V3',DRS_MSG_ADDENTRYREPLY_V3),
    }
        

class DRS_MSG_KCC_EXECUTE_V1(NDRSTRUCT):
    structure = (
        ('dwTaskID', DWORD),('dwFlags', DWORD),
    )


class DRS_MSG_KCC_EXECUTE(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_KCC_EXECUTE_V1),
    }
        

class DS_REPL_CLIENT_CONTEXT(NDRSTRUCT):
    structure = (
        ('hCtx', ULONGLONG),('lReferenceCount', LONG),('fIsBound', BOOL),('uuidClient', UUID),('timeLastUsed', DSTIME),('IPAddr', ULONG),('pid', INT),
    )


class DS_REPL_CLIENT_CONTEXTS(NDRSTRUCT):
    structure = (
        ('cNumContexts', DWORD),('dwReserved', DWORD),('rgContext', DS_REPL_CLIENT_CONTEXT),
    )


class DS_REPL_SERVER_OUTGOING_CALL(NDRSTRUCT):
    structure = (
        ('pszServerName', LPWSTR),('fIsHandleBound', BOOL),('fIsHandleFromCache', BOOL),('fIsHandleInCache', BOOL),('dwThreadId', DWORD),('dwBindingTimeoutMins', DWORD),('dstimeCreated', DSTIME),('dwCallType', DWORD),
    )


class DS_REPL_SERVER_OUTGOING_CALLS(NDRSTRUCT):
    structure = (
        ('cNumCalls', DWORD),('dwReserved', DWORD),('rgCall', DS_REPL_SERVER_OUTGOING_CALL),
    )


class DRS_MSG_GETREPLINFO_REQ_V1(NDRSTRUCT):
    structure = (
        ('InfoType', DWORD),('pszObjectDN', LPWSTR),('uuidSourceDsaObjGuid', UUID),
    )


class DRS_MSG_GETREPLINFO_REQ_V2(NDRSTRUCT):
    structure = (
        ('InfoType', DWORD),('pszObjectDN', LPWSTR),('uuidSourceDsaObjGuid', UUID),('ulFlags', DWORD),('pszAttributeName', LPWSTR),('pszValueDN', LPWSTR),('dwEnumerationContext', DWORD),
    )


class DRS_MSG_GETREPLINFO_REQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_GETREPLINFO_REQ_V1),2: ('V2',DRS_MSG_GETREPLINFO_REQ_V2),
    }
        

class DRS_MSG_GETREPLINFO_REPLY(NDRUNION):
    union = {
        0: ('pNeighbors',DS_REPL_NEIGHBORSW),1: ('pCursors',DS_REPL_CURSORS),2: ('pObjMetaData',DS_REPL_OBJ_META_DATA),3: ('pConnectFailures',DS_REPL_KCC_DSA_FAILURESW),4: ('pLinkFailures',DS_REPL_KCC_DSA_FAILURESW),5: ('pPendingOps',DS_REPL_PENDING_OPSW),6: ('pAttrValueMetaData',DS_REPL_ATTR_VALUE_META_DATA),7: ('pCursors2',DS_REPL_CURSORS_2),8: ('pCursors3',DS_REPL_CURSORS_3W),9: ('pObjMetaData2',DS_REPL_OBJ_META_DATA_2),10: ('pAttrValueMetaData2',DS_REPL_ATTR_VALUE_META_DATA_2),0xFFFFFFFA: ('pServerOutgoingCalls',DS_REPL_SERVER_OUTGOING_CALLS),0xFFFFFFFB: ('pUpToDateVec',UPTODATE_VECTOR_V1_EXT),0xFFFFFFFC: ('pClientContexts',DS_REPL_CLIENT_CONTEXTS),0xFFFFFFFE: ('pRepsTo',DS_REPL_NEIGHBORSW),
    }
        

class DATA_DRS_MSG_ADDSIDREQ_V1(NDRUniConformantArray):
    item = WCHAR

class PTR_DRS_MSG_ADDSIDREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_ADDSIDREQ_V1),
    )

class DRS_MSG_ADDSIDREQ_V1(NDRSTRUCT):
    structure = (
	('Flags', DWORD),	('SrcDomain', WCHAR),	('SrcPrincipal', WCHAR),	('SrcDomainController', WCHAR),	('SrcCredsUserLength', DWORD),	('SrcCredsUser', WCHAR),	('SrcCredsDomainLength', DWORD),	('SrcCredsDomain', WCHAR),	('SrcCredsPasswordLength', DWORD),	('SrcCredsPassword', PTR_DRS_MSG_ADDSIDREQ_V1),
	('DstDomain', WCHAR),	('DstPrincipal', WCHAR),
    )
        

class DRS_MSG_ADDSIDREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDSIDREQ_V1),
    }
        

class DRS_MSG_ADDSIDREPLY_V1(NDRSTRUCT):
    structure = (
        ('dwWin32Error', DWORD),
    )


class DRS_MSG_ADDSIDREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDSIDREPLY_V1),
    }
        

class DATA_DRS_MSG_GETMEMBERSHIPS2_REQ_V1(NDRUniConformantArray):
    item = DRS_MSG_REVMEMB_REQ_V1

class PTR_DRS_MSG_GETMEMBERSHIPS2_REQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_GETMEMBERSHIPS2_REQ_V1),
    )

class DRS_MSG_GETMEMBERSHIPS2_REQ_V1(NDRSTRUCT):
    structure = (
	('Count', ULONG),	('Requests', PTR_DRS_MSG_GETMEMBERSHIPS2_REQ_V1),

    )
        

class DRS_MSG_GETMEMBERSHIPS2_REQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_GETMEMBERSHIPS2_REQ_V1),
    }
        

class DATA_DRS_MSG_GETMEMBERSHIPS2_REPLY_V1(NDRUniConformantArray):
    item = DRS_MSG_REVMEMB_REPLY_V1

class PTR_DRS_MSG_GETMEMBERSHIPS2_REPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_GETMEMBERSHIPS2_REPLY_V1),
    )

class DRS_MSG_GETMEMBERSHIPS2_REPLY_V1(NDRSTRUCT):
    structure = (
	('Count', ULONG),	('Replies', PTR_DRS_MSG_GETMEMBERSHIPS2_REPLY_V1),

    )
        

class DRS_MSG_GETMEMBERSHIPS2_REPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_GETMEMBERSHIPS2_REPLY_V1),
    }
        

class DRS_MSG_REPVERIFYOBJ_V1(NDRSTRUCT):
    structure = (
        ('pNC', DSNAME),('uuidDsaSrc', UUID),('ulOptions', ULONG),
    )


class DRS_MSG_REPVERIFYOBJ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPVERIFYOBJ_V1),
    }
        

class DRS_MSG_EXISTREQ_V1(NDRSTRUCT):
    structure = (
        ('guidStart', UUID),('cGuids', DWORD),('pNC', DSNAME),('pUpToDateVecCommonV1', UPTODATE_VECTOR_V1_EXT),('Md5Digest', UCHAR),
    )


class DRS_MSG_EXISTREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_EXISTREQ_V1),
    }
        

class DATA_DRS_MSG_EXISTREPLY_V1(NDRUniConformantArray):
    item = UUID

class PTR_DRS_MSG_EXISTREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_EXISTREPLY_V1),
    )

class DRS_MSG_EXISTREPLY_V1(NDRSTRUCT):
    structure = (
	('dwStatusFlags', DWORD),	('cNumGuids', DWORD),	('rgGuids', PTR_DRS_MSG_EXISTREPLY_V1),

    )
        

class DRS_MSG_EXISTREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_EXISTREPLY_V1),
    }
        

class DATA_DRS_MSG_QUERYSITESREQ_V1(NDRUniConformantArray):
    item = WCHAR

class PTR_DRS_MSG_QUERYSITESREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_QUERYSITESREQ_V1),
    )

class DRS_MSG_QUERYSITESREQ_V1(NDRSTRUCT):
    structure = (
	('pwszFromSite',  WCHAR),	('cToSites', DWORD),	('rgszToSites', PTR_DRS_MSG_QUERYSITESREQ_V1),
	('dwFlags', DWORD),
    )
        

class DRS_MSG_QUERYSITESREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_QUERYSITESREQ_V1),
    }
        

class DRS_MSG_QUERYSITESREPLYELEMENT_V1(NDRSTRUCT):
    structure = (
        ('dwErrorCode', DWORD),('dwCost', DWORD),
    )


class DATA_DRS_MSG_QUERYSITESREPLY_V1(NDRUniConformantArray):
    item = DRS_MSG_QUERYSITESREPLYELEMENT_V1

class PTR_DRS_MSG_QUERYSITESREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_QUERYSITESREPLY_V1),
    )

class DRS_MSG_QUERYSITESREPLY_V1(NDRSTRUCT):
    structure = (
	('cToSites', DWORD),	('rgCostInfo', PTR_DRS_MSG_QUERYSITESREPLY_V1),
	('dwFlags', DWORD),
    )
        

class DRS_MSG_QUERYSITESREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_QUERYSITESREPLY_V1),
    }
        

class DRS_MSG_INIT_DEMOTIONREQ_V1(NDRSTRUCT):
    structure = (
        ('dwReserved', DWORD),
    )


class DRS_MSG_INIT_DEMOTIONREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_INIT_DEMOTIONREQ_V1),
    }
        

class DRS_MSG_INIT_DEMOTIONREPLY_V1(NDRSTRUCT):
    structure = (
        ('dwOpError', DWORD),
    )


class DRS_MSG_INIT_DEMOTIONREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_INIT_DEMOTIONREPLY_V1),
    }
        

class DRS_MSG_REPLICA_DEMOTIONREQ_V1(NDRSTRUCT):
    structure = (
        ('dwFlags', DWORD),('uuidHelperDest', UUID),('pNC', DSNAME),
    )


class DRS_MSG_REPLICA_DEMOTIONREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPLICA_DEMOTIONREQ_V1),
    }
        

class DRS_MSG_REPLICA_DEMOTIONREPLY_V1(NDRSTRUCT):
    structure = (
        ('dwOpError', DWORD),
    )


class DRS_MSG_REPLICA_DEMOTIONREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_REPLICA_DEMOTIONREPLY_V1),
    }
        

class DRS_MSG_FINISH_DEMOTIONREQ_V1(NDRSTRUCT):
    structure = (
        ('dwOperations', DWORD),('uuidHelperDest', UUID),('szScriptBase', LPWSTR),
    )


class DRS_MSG_FINISH_DEMOTIONREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_FINISH_DEMOTIONREQ_V1),
    }
        

class DRS_MSG_FINISH_DEMOTIONREPLY_V1(NDRSTRUCT):
    structure = (
        ('dwOperationsDone', DWORD),('dwOpFailed', DWORD),('dwOpError', DWORD),
    )


class DRS_MSG_FINISH_DEMOTIONREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_FINISH_DEMOTIONREPLY_V1),
    }
        

class DRS_MSG_ADDCLONEDCREQ_V1(NDRSTRUCT):
    structure = (
        ('pwszCloneDCName',  WCHAR),('pwszSite',  WCHAR),
    )


class DRS_MSG_ADDCLONEDCREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDCLONEDCREQ_V1),
    }
        

class DATA_DRS_MSG_ADDCLONEDCREPLY_V1(NDRUniConformantArray):
    item = WCHAR

class PTR_DRS_MSG_ADDCLONEDCREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_ADDCLONEDCREPLY_V1),
    )

class DRS_MSG_ADDCLONEDCREPLY_V1(NDRSTRUCT):
    structure = (
	('pwszCloneDCName', WCHAR),	('pwszSite', WCHAR),	('cPasswordLength', DWORD),	('pwsNewDCAccountPassword', PTR_DRS_MSG_ADDCLONEDCREPLY_V1),

    )
        

class DRS_MSG_ADDCLONEDCREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_ADDCLONEDCREPLY_V1),
    }
        

class DATA_DRS_MSG_WRITENGCKEYREQ_V1(NDRUniConformantArray):
    item = UCHAR

class PTR_DRS_MSG_WRITENGCKEYREQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_WRITENGCKEYREQ_V1),
    )

class DRS_MSG_WRITENGCKEYREQ_V1(NDRSTRUCT):
    structure = (
	('pwszAccount',  WCHAR),	('cNgcKey', DWORD),	('pNgcKey', PTR_DRS_MSG_WRITENGCKEYREQ_V1),

    )
        

class DRS_MSG_WRITENGCKEYREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_WRITENGCKEYREQ_V1),
    }
        

class DRS_MSG_WRITENGCKEYREPLY_V1(NDRSTRUCT):
    structure = (
        ('retVal', DWORD),
    )


class DRS_MSG_WRITENGCKEYREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_WRITENGCKEYREPLY_V1),
    }
        

class DRS_MSG_READNGCKEYREQ_V1(NDRSTRUCT):
    structure = (
        ('pwszAccount',  WCHAR),
    )


class DRS_MSG_READNGCKEYREQ(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_READNGCKEYREQ_V1),
    }
        

class DATA_DRS_MSG_READNGCKEYREPLY_V1(NDRUniConformantArray):
    item = UCHAR

class PTR_DRS_MSG_READNGCKEYREPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DRS_MSG_READNGCKEYREPLY_V1),
    )

class DRS_MSG_READNGCKEYREPLY_V1(NDRSTRUCT):
    structure = (
	('retVal', DWORD),	('cNgcKey', DWORD),	('pNgcKey', PTR_DRS_MSG_READNGCKEYREPLY_V1),

    )
        

class DRS_MSG_READNGCKEYREPLY(NDRUNION):
    union = {
        1: ('V1',DRS_MSG_READNGCKEYREPLY_V1),
    }
        

class IDL_DRSBind(NDRCALL):
    opnum = 0
    structure = (
		('rpc_handle', HANDLE_T),
		('puuidClientDsa', UUID),
		('pextClient', DRS_EXTENSIONS),
    )

class IDL_DRSBindResponse(NDRCALL):
    structure = (
		('ppextServer', DRS_EXTENSIONS),
		('phDrs', DRS_HANDLE),
    )
        

class IDL_DRSUnbind(NDRCALL):
    opnum = 1
    structure = (
		('phDrs', DRS_HANDLE),
    )

class IDL_DRSUnbindResponse(NDRCALL):
    structure = (
		('phDrs', DRS_HANDLE),
    )
        

class IDL_DRSReplicaSync(NDRCALL):
    opnum = 2
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgSync', DRS_MSG_REPSYNC),
    )

class IDL_DRSReplicaSyncResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSGetNCChanges(NDRCALL):
    opnum = 3
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_GETCHGREQ),
    )

class IDL_DRSGetNCChangesResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_GETCHGREPLY),
    )
        

class IDL_DRSUpdateRefs(NDRCALL):
    opnum = 4
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgUpdRefs', DRS_MSG_UPDREFS),
    )

class IDL_DRSUpdateRefsResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSReplicaAdd(NDRCALL):
    opnum = 5
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgAdd', DRS_MSG_REPADD),
    )

class IDL_DRSReplicaAddResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSReplicaDel(NDRCALL):
    opnum = 6
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgDel', DRS_MSG_REPDEL),
    )

class IDL_DRSReplicaDelResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSReplicaModify(NDRCALL):
    opnum = 7
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgMod', DRS_MSG_REPMOD),
    )

class IDL_DRSReplicaModifyResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSVerifyNames(NDRCALL):
    opnum = 8
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_VERIFYREQ),
    )

class IDL_DRSVerifyNamesResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_VERIFYREPLY),
    )
        

class IDL_DRSGetMemberships(NDRCALL):
    opnum = 9
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_REVMEMB_REQ),
    )

class IDL_DRSGetMembershipsResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_REVMEMB_REPLY),
    )
        

class IDL_DRSInterDomainMove(NDRCALL):
    opnum = 10
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_MOVEREQ),
    )

class IDL_DRSInterDomainMoveResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_MOVEREPLY),
    )
        

class IDL_DRSGetNT4ChangeLog(NDRCALL):
    opnum = 11
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_NT4_CHGLOG_REQ),
    )

class IDL_DRSGetNT4ChangeLogResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_NT4_CHGLOG_REPLY),
    )
        

class IDL_DRSCrackNames(NDRCALL):
    opnum = 12
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_CRACKREQ),
    )

class IDL_DRSCrackNamesResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_CRACKREPLY),
    )
        

class IDL_DRSWriteSPN(NDRCALL):
    opnum = 13
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_SPNREQ),
    )

class IDL_DRSWriteSPNResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_SPNREPLY),
    )
        

class IDL_DRSRemoveDsServer(NDRCALL):
    opnum = 14
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_RMSVRREQ),
    )

class IDL_DRSRemoveDsServerResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_RMSVRREPLY),
    )
        

class IDL_DRSRemoveDsDomain(NDRCALL):
    opnum = 15
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_RMDMNREQ),
    )

class IDL_DRSRemoveDsDomainResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_RMDMNREPLY),
    )
        

class IDL_DRSDomainControllerInfo(NDRCALL):
    opnum = 16
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_DCINFOREQ),
    )

class IDL_DRSDomainControllerInfoResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_DCINFOREPLY),
    )
        

class IDL_DRSAddEntry(NDRCALL):
    opnum = 17
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_ADDENTRYREQ),
    )

class IDL_DRSAddEntryResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_ADDENTRYREPLY),
    )
        

class IDL_DRSExecuteKCC(NDRCALL):
    opnum = 18
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_KCC_EXECUTE),
    )

class IDL_DRSExecuteKCCResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSGetReplInfo(NDRCALL):
    opnum = 19
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_GETREPLINFO_REQ),
    )

class IDL_DRSGetReplInfoResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_GETREPLINFO_REPLY),
    )
        

class IDL_DRSAddSidHistory(NDRCALL):
    opnum = 20
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_ADDSIDREQ),
    )

class IDL_DRSAddSidHistoryResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_ADDSIDREPLY),
    )
        

class IDL_DRSGetMemberships2(NDRCALL):
    opnum = 21
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_GETMEMBERSHIPS2_REQ),
    )

class IDL_DRSGetMemberships2Response(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_GETMEMBERSHIPS2_REPLY),
    )
        

class IDL_DRSReplicaVerifyObjects(NDRCALL):
    opnum = 22
    structure = (
		('hDrs', DRS_HANDLE),
		('dwVersion', DWORD),
		('pmsgVerify', DRS_MSG_REPVERIFYOBJ),
    )

class IDL_DRSReplicaVerifyObjectsResponse(NDRCALL):
    structure = (

    )
        

class IDL_DRSGetObjectExistence(NDRCALL):
    opnum = 23
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_EXISTREQ),
    )

class IDL_DRSGetObjectExistenceResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_EXISTREPLY),
    )
        

class IDL_DRSQuerySitesByCost(NDRCALL):
    opnum = 24
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_QUERYSITESREQ),
    )

class IDL_DRSQuerySitesByCostResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_QUERYSITESREPLY),
    )
        

class IDL_DRSInitDemotion(NDRCALL):
    opnum = 25
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_INIT_DEMOTIONREQ),
    )

class IDL_DRSInitDemotionResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_INIT_DEMOTIONREPLY),
    )
        

class IDL_DRSReplicaDemotion(NDRCALL):
    opnum = 26
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_REPLICA_DEMOTIONREQ),
    )

class IDL_DRSReplicaDemotionResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_REPLICA_DEMOTIONREPLY),
    )
        

class IDL_DRSFinishDemotion(NDRCALL):
    opnum = 27
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_FINISH_DEMOTIONREQ),
    )

class IDL_DRSFinishDemotionResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_FINISH_DEMOTIONREPLY),
    )
        

class IDL_DRSAddCloneDC(NDRCALL):
    opnum = 28
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_ADDCLONEDCREQ),
    )

class IDL_DRSAddCloneDCResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_ADDCLONEDCREPLY),
    )
        

class IDL_DRSWriteNgcKey(NDRCALL):
    opnum = 29
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_WRITENGCKEYREQ),
    )

class IDL_DRSWriteNgcKeyResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_WRITENGCKEYREPLY),
    )
        

class IDL_DRSReadNgcKey(NDRCALL):
    opnum = 30
    structure = (
		('hDrs', DRS_HANDLE),
		('dwInVersion', DWORD),
		('pmsgIn', DRS_MSG_READNGCKEYREQ),
    )

class IDL_DRSReadNgcKeyResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DRS_MSG_READNGCKEYREPLY),
    )
        
OPNUMS = {
0 : (IDL_DRSBind,IDL_DRSBindResponse),
1 : (IDL_DRSUnbind,IDL_DRSUnbindResponse),
2 : (IDL_DRSReplicaSync,IDL_DRSReplicaSyncResponse),
3 : (IDL_DRSGetNCChanges,IDL_DRSGetNCChangesResponse),
4 : (IDL_DRSUpdateRefs,IDL_DRSUpdateRefsResponse),
5 : (IDL_DRSReplicaAdd,IDL_DRSReplicaAddResponse),
6 : (IDL_DRSReplicaDel,IDL_DRSReplicaDelResponse),
7 : (IDL_DRSReplicaModify,IDL_DRSReplicaModifyResponse),
8 : (IDL_DRSVerifyNames,IDL_DRSVerifyNamesResponse),
9 : (IDL_DRSGetMemberships,IDL_DRSGetMembershipsResponse),
10 : (IDL_DRSInterDomainMove,IDL_DRSInterDomainMoveResponse),
11 : (IDL_DRSGetNT4ChangeLog,IDL_DRSGetNT4ChangeLogResponse),
12 : (IDL_DRSCrackNames,IDL_DRSCrackNamesResponse),
13 : (IDL_DRSWriteSPN,IDL_DRSWriteSPNResponse),
14 : (IDL_DRSRemoveDsServer,IDL_DRSRemoveDsServerResponse),
15 : (IDL_DRSRemoveDsDomain,IDL_DRSRemoveDsDomainResponse),
16 : (IDL_DRSDomainControllerInfo,IDL_DRSDomainControllerInfoResponse),
17 : (IDL_DRSAddEntry,IDL_DRSAddEntryResponse),
18 : (IDL_DRSExecuteKCC,IDL_DRSExecuteKCCResponse),
19 : (IDL_DRSGetReplInfo,IDL_DRSGetReplInfoResponse),
20 : (IDL_DRSAddSidHistory,IDL_DRSAddSidHistoryResponse),
21 : (IDL_DRSGetMemberships2,IDL_DRSGetMemberships2Response),
22 : (IDL_DRSReplicaVerifyObjects,IDL_DRSReplicaVerifyObjectsResponse),
23 : (IDL_DRSGetObjectExistence,IDL_DRSGetObjectExistenceResponse),
24 : (IDL_DRSQuerySitesByCost,IDL_DRSQuerySitesByCostResponse),
25 : (IDL_DRSInitDemotion,IDL_DRSInitDemotionResponse),
26 : (IDL_DRSReplicaDemotion,IDL_DRSReplicaDemotionResponse),
27 : (IDL_DRSFinishDemotion,IDL_DRSFinishDemotionResponse),
28 : (IDL_DRSAddCloneDC,IDL_DRSAddCloneDCResponse),
29 : (IDL_DRSWriteNgcKey,IDL_DRSWriteNgcKeyResponse),
30 : (IDL_DRSReadNgcKey,IDL_DRSReadNgcKeyResponse),
}

#################################################################################

#dsaop Definition

#################################################################################

MSRPC_UUID_DSAOP = uuidtup_to_bin(('7c44d7d4-31d5-424c-bd5e-2b3e1f323d22','0.0'))


class DATA_DSA_MSG_EXECUTE_SCRIPT_REQ_V1(NDRUniConformantArray):
    item = BYTE

class PTR_DSA_MSG_EXECUTE_SCRIPT_REQ_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DSA_MSG_EXECUTE_SCRIPT_REQ_V1),
    )

class DSA_MSG_EXECUTE_SCRIPT_REQ_V1(NDRSTRUCT):
    structure = (
	('Flags', DWORD),	('cbPassword', DWORD),	('pbPassword', PTR_DSA_MSG_EXECUTE_SCRIPT_REQ_V1),

    )
        

class DSA_MSG_EXECUTE_SCRIPT_REQ(NDRUNION):
    union = {
        1: ('V1',DSA_MSG_EXECUTE_SCRIPT_REQ_V1),
    }
        

class DSA_MSG_EXECUTE_SCRIPT_REPLY_V1(NDRSTRUCT):
    structure = (
        ('dwOperationStatus', DWORD),('pwErrMessage', LPWSTR),
    )


class DSA_MSG_EXECUTE_SCRIPT_REPLY(NDRUNION):
    union = {
        1: ('V1',DSA_MSG_EXECUTE_SCRIPT_REPLY_V1),
    }
        

class DSA_MSG_PREPARE_SCRIPT_REQ_V1(NDRSTRUCT):
    structure = (
        ('Reserved', DWORD),
    )


class DSA_MSG_PREPARE_SCRIPT_REQ(NDRUNION):
    union = {
        1: ('V1',DSA_MSG_PREPARE_SCRIPT_REQ_V1),
    }
        

class DATA_DSA_MSG_PREPARE_SCRIPT_REPLY_V1(NDRUniConformantArray):
    item = BYTE

class PTR_DSA_MSG_PREPARE_SCRIPT_REPLY_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_DSA_MSG_PREPARE_SCRIPT_REPLY_V1),
    )

class DSA_MSG_PREPARE_SCRIPT_REPLY_V1(NDRSTRUCT):
    structure = (
	('dwOperationStatus', DWORD),	('pwErrMessage', LPWSTR),	('cbPassword', DWORD),	('pbPassword', BYTE),	('cbHashBody', DWORD),	('pbHashBody', BYTE),	('cbHashSignature', DWORD),	('pbHashSignature', PTR_DSA_MSG_PREPARE_SCRIPT_REPLY_V1),

    )
        

class DSA_MSG_PREPARE_SCRIPT_REPLY(NDRUNION):
    union = {
        1: ('V1',DSA_MSG_PREPARE_SCRIPT_REPLY_V1),
    }
        

class IDL_DSAPrepareScript(NDRCALL):
    opnum = 0
    structure = (
		('hRpc', HANDLE_T),
		('dwInVersion', DWORD),
		('pmsgIn', DSA_MSG_PREPARE_SCRIPT_REQ),
    )

class IDL_DSAPrepareScriptResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DSA_MSG_PREPARE_SCRIPT_REPLY),
    )
        

class IDL_DSAExecuteScript(NDRCALL):
    opnum = 1
    structure = (
		('hRpc', HANDLE_T),
		('dwInVersion', DWORD),
		('pmsgIn', DSA_MSG_EXECUTE_SCRIPT_REQ),
    )

class IDL_DSAExecuteScriptResponse(NDRCALL):
    structure = (
		('pdwOutVersion', DWORD),
		('pmsgOut', DSA_MSG_EXECUTE_SCRIPT_REPLY),
    )
        
OPNUMS = {
0 : (IDL_DSAPrepareScript,IDL_DSAPrepareScriptResponse),
1 : (IDL_DSAExecuteScript,IDL_DSAExecuteScriptResponse),
}

