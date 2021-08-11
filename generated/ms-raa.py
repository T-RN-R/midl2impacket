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

#authzr Definition

#################################################################################

MSRPC_UUID_AUTHZR = uuidtup_to_bin(('0b1c2170-5732-4e0e-8cd3-d9b16f3b84d7','0.0'))

AUTHZR_HANDLE = PVOID

class DATA_AUTHZR_ACCESS_REQUEST(NDRUniConformantArray):
    item = OBJECT_TYPE_LIST

class PTR_AUTHZR_ACCESS_REQUEST(NDRPOINTER):
    referent = (
        ('Data', DATA_AUTHZR_ACCESS_REQUEST),
    )

class AUTHZR_ACCESS_REQUEST(NDRSTRUCT):
    structure = (
	('DesiredAccess', ACCESS_MASK),	('PrincipalSelfSid', RPC_SID),	('ObjectTypeListLength', DWORD),	('ObjectTypeList', PTR_AUTHZR_ACCESS_REQUEST),

    )
        

class DATA_SR_SD(NDRUniConformantArray):
    item = BYTE

class PTR_SR_SD(NDRPOINTER):
    referent = (
        ('Data', DATA_SR_SD),
    )

class SR_SD(NDRSTRUCT):
    structure = (
	('dwLength', DWORD),	('pSrSd', PTR_SR_SD),

    )
        

class DATA_AUTHZR_ACCESS_REPLY(NDRUniConformantArray):
    item = DWORD

class PTR_AUTHZR_ACCESS_REPLY(NDRPOINTER):
    referent = (
        ('Data', DATA_AUTHZR_ACCESS_REPLY),
    )

class AUTHZR_ACCESS_REPLY(NDRSTRUCT):
    structure = (
	('ResultListLength', DWORD),	('GrantedAccessMask', ACCESS_MASK),	('Error', PTR_AUTHZR_ACCESS_REPLY),

    )
        

AuthzContextInfoUserSid = 1,
AuthzContextInfoGroupsSids = 2,
AuthzContextInfoRestrictedSids = 3,
ReservedEnumValue4 = 4,
ReservedEnumValue5 = 5,
ReservedEnumValue6 = 6,
ReservedEnumValue7 = 7,
ReservedEnumValue8 = 8,
ReservedEnumValue9 = 9,
ReservedEnumValue10 = 10,
ReservedEnumValue11 = 11,
AuthzContextInfoDeviceSids = 12,
AuthzContextInfoUserClaims = 13,
AuthzContextInfoDeviceClaims = 14,
ReservedEnumValue15 = 15,
ReservedEnumValue16 = 16
        

class AUTHZR_SID_AND_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('Sid', RPC_SID),('Attributes', DWORD),
    )


class AUTHZR_TOKEN_USER(NDRSTRUCT):
    structure = (
        ('User', AUTHZR_SID_AND_ATTRIBUTES),
    )


class AUTHZR_TOKEN_GROUPS(NDRSTRUCT):
    structure = (
        ('GroupCount', DWORD),('Groups', AUTHZR_SID_AND_ATTRIBUTES),
    )


class DATA_AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE(NDRUniConformantArray):
    item = WCHAR

class PTR_AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE(NDRPOINTER):
    referent = (
        ('Data', DATA_AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE),
    )

class AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE(NDRSTRUCT):
    structure = (
	('Length', ULONG),	('Value', PTR_AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE),

    )
        

class ATTRIBUTEUNION(NDRUNION):
    union = {
        1: ('Int64',LONG64),2: ('Uint64',ULONG64),3: ('String',AUTHZR_SECURITY_ATTRIBUTE_STRING_VALUE),
    }
        

class AUTHZR_SECURITY_ATTRIBUTE_V1_VALUE(NDRSTRUCT):
    structure = (
        ('ValueType', USHORT),('AttributeUnion', ATTRIBUTEUNION),
    )


class DATA_AUTHZR_SECURITY_ATTRIBUTE_V1(NDRUniConformantArray):
    item = AUTHZR_SECURITY_ATTRIBUTE_V1_VALUE

class PTR_AUTHZR_SECURITY_ATTRIBUTE_V1(NDRPOINTER):
    referent = (
        ('Data', DATA_AUTHZR_SECURITY_ATTRIBUTE_V1),
    )

class AUTHZR_SECURITY_ATTRIBUTE_V1(NDRSTRUCT):
    structure = (
	('Length', ULONG),	('Value', WCHAR),	('ValueType', USHORT),	('Reserved', USHORT),	('Flags', ULONG),	('ValueCount', ULONG),	('Values', PTR_AUTHZR_SECURITY_ATTRIBUTE_V1),

    )
        

class DATA_AUTHZR_SECURITY_ATTRIBUTES_INFORMATION(NDRUniConformantArray):
    item = AUTHZR_SECURITY_ATTRIBUTE_V1

class PTR_AUTHZR_SECURITY_ATTRIBUTES_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DATA_AUTHZR_SECURITY_ATTRIBUTES_INFORMATION),
    )

class AUTHZR_SECURITY_ATTRIBUTES_INFORMATION(NDRSTRUCT):
    structure = (
	('Version', USHORT),	('Reserved', USHORT),	('AttributeCount', ULONG),	('Attributes', PTR_AUTHZR_SECURITY_ATTRIBUTES_INFORMATION),

    )
        

class CONTEXTINFOUNION(NDRUNION):
    union = {
        1: ('pTokenUser',AUTHZR_TOKEN_USER),2: ('pTokenGroups',AUTHZR_TOKEN_GROUPS),3: ('pTokenClaims',AUTHZR_SECURITY_ATTRIBUTES_INFORMATION),
    }
        

class AUTHZR_CONTEXT_INFORMATION(NDRSTRUCT):
    structure = (
        ('ValueType', USHORT),('ContextInfoUnion', CONTEXTINFOUNION),
    )


AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE = 0,
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL = 1,
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD = 2,
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE = 3,
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE = 4
        

AUTHZ_SID_OPERATION_NONE = 0,
AUTHZ_SID_OPERATION_REPLACE_ALL = 1,
AUTHZ_SID_OPERATION_ADD = 2,
AUTHZ_SID_OPERATION_DELETE = 3,
AUTHZ_SID_OPERATION_REPLACE = 4
        

class AuthzrFreeContext(NDRCALL):
    opnum = 0
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
    )

class AuthzrFreeContextResponse(NDRCALL):
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
    )
        

class AuthzrInitializeContextFromSid(NDRCALL):
    opnum = 1
    structure = (
		('BINDING', HANDLE_T),
		('FLAGS', DWORD),
		('SID', RPC_SID),
		('PEXPIRATIONTIME', LARGE_INTEGER),
		('IDENTIFIER', LUID),
    )

class AuthzrInitializeContextFromSidResponse(NDRCALL):
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
    )
        

class AuthzrInitializeCompoundContext(NDRCALL):
    opnum = 2
    structure = (
		('USERCONTEXTHANDLE', AUTHZR_HANDLE),
		('DEVICECONTEXTHANDLE', AUTHZR_HANDLE),
    )

class AuthzrInitializeCompoundContextResponse(NDRCALL):
    structure = (
		('COMPOUNDCONTEXTHANDLE', AUTHZR_HANDLE),
    )
        

class AuthzrAccessCheck(NDRCALL):
    opnum = 3
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
		('FLAGS', DWORD),
		('PREQUEST', AUTHZR_ACCESS_REQUEST),
		('SECURITYDESCRIPTORCOUNT', DWORD),
		('PSECURITYDESCRIPTORS', SR_SD),
		('PREPLY', AUTHZR_ACCESS_REPLY),
    )

class AuthzrAccessCheckResponse(NDRCALL):
    structure = (
		('PREPLY', AUTHZR_ACCESS_REPLY),
    )
        

class AuthzGetInformationFromContext(NDRCALL):
    opnum = 4
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
		('INFOCLASS', AUTHZ_CONTEXT_INFORMATION_CLASS),
    )

class AuthzGetInformationFromContextResponse(NDRCALL):
    structure = (
		('PPCONTEXTINFORMATION', AUTHZR_CONTEXT_INFORMATION),
    )
        

class AuthzrModifyClaims(NDRCALL):
    opnum = 5
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
		('CLAIMCLASS', AUTHZ_CONTEXT_INFORMATION_CLASS),
		('OPERATIONCOUNT', DWORD),
		('PCLAIMOPERATIONS', AUTHZ_SECURITY_ATTRIBUTE_OPERATION),
		('PCLAIMS', AUTHZR_SECURITY_ATTRIBUTES_INFORMATION),
    )

class AuthzrModifyClaimsResponse(NDRCALL):
    structure = (

    )
        

class AuthzrModifySids(NDRCALL):
    opnum = 6
    structure = (
		('CONTEXTHANDLE', AUTHZR_HANDLE),
		('SIDCLASS', AUTHZ_CONTEXT_INFORMATION_CLASS),
		('OPERATIONCOUNT', DWORD),
		('PSIDOPERATIONS', AUTHZ_SID_OPERATION),
		('PSIDS', AUTHZR_TOKEN_GROUPS),
    )

class AuthzrModifySidsResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (AuthzrFreeContext,AuthzrFreeContextResponse),
1 : (AuthzrInitializeContextFromSid,AuthzrInitializeContextFromSidResponse),
2 : (AuthzrInitializeCompoundContext,AuthzrInitializeCompoundContextResponse),
3 : (AuthzrAccessCheck,AuthzrAccessCheckResponse),
4 : (AuthzGetInformationFromContext,AuthzGetInformationFromContextResponse),
5 : (AuthzrModifyClaims,AuthzrModifyClaimsResponse),
6 : (AuthzrModifySids,AuthzrModifySidsResponse),
}

