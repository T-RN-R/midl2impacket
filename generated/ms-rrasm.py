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

#"ms-oaut.idl"

#################################################################################

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

#"ms-dcom.idl"

#################################################################################

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

CLSID = GUID
IID = GUID
ID = UNSIGNED_HYPER
OXID = UNSIGNED_HYPER
OID = UNSIGNED_HYPER
SETID = UNSIGNED_HYPER
IPID = GUID
CID = GUID
REFIPID = REFGUID

class COMVERSION(NDRSTRUCT):
    structure = (
        ('MajorVersion', UNSIGNED_SHORT),('MinorVersion', UNSIGNED_SHORT),
    )


class ORPC_EXTENT(NDRSTRUCT):
    structure = (
        ('id', GUID),('size', UNSIGNED_LONG),('data', BYTE),
    )


class DATA_ORPC_EXTENT_ARRAY(NDRUniConformantArray):
    item = ORPC_EXTENT

class PTR_ORPC_EXTENT_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_ORPC_EXTENT_ARRAY),
    )

class ORPC_EXTENT_ARRAY(NDRSTRUCT):
    structure = (
	('size', UNSIGNED_LONG),	('reserved', UNSIGNED_LONG),	('extent', PTR_ORPC_EXTENT_ARRAY),

    )
        

class ORPCTHIS(NDRSTRUCT):
    structure = (
        ('version', COMVERSION),('flags', UNSIGNED_LONG),('reserved1', UNSIGNED_LONG),('cid', CID),('extensions', ORPC_EXTENT_ARRAY),
    )


class ORPCTHAT(NDRSTRUCT):
    structure = (
        ('flags', UNSIGNED_LONG),('extensions', ORPC_EXTENT_ARRAY),
    )


class DUALSTRINGARRAY(NDRSTRUCT):
    structure = (
        ('wNumEntries', UNSIGNED_SHORT),('wSecurityOffset', UNSIGNED_SHORT),('aStringArray', UNSIGNED_SHORT),
    )


CPFLAG_PROPAGATE = 1,
CPFLAG_EXPOSE = 2,
CPFLAG_ENVOY = 4
        

class MINTERFACEPOINTER(NDRSTRUCT):
    structure = (
        ('ulCntData', UNSIGNED_LONG),('abData', BYTE),
    )

PMINTERFACEPOINTER = MINTERFACEPOINTER

class ERROROBJECTDATA(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwHelpContext', DWORD),('iid', IID),('pszSource', WCHAR_T),('pszDescription', WCHAR_T),('pszHelpFile', WCHAR_T),
    )


class STDOBJREF(NDRSTRUCT):
    structure = (
        ('flags', UNSIGNED_LONG),('cPublicRefs', UNSIGNED_LONG),('oxid', OXID),('oid', OID),('ipid', IPID),
    )


class REMQIRESULT(NDRSTRUCT):
    structure = (
        ('hResult', HRESULT),('std', STDOBJREF),
    )


class REMINTERFACEREF(NDRSTRUCT):
    structure = (
        ('ipid', IPID),('cPublicRefs', UNSIGNED_LONG),('cPrivateRefs', UNSIGNED_LONG),
    )

PREMQIRESULT = REMQIRESULT
PMINTERFACEPOINTERINTERNAL = MINTERFACEPOINTER

class COSERVERINFO(NDRSTRUCT):
    structure = (
        ('dwReserved1', DWORD),('pwszName', WCHAR_T),('pdwReserved', DWORD),('dwReserved2', DWORD),
    )


class DATA_CUSTOMREMOTE_REQUEST_SCM_INFO(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_CUSTOMREMOTE_REQUEST_SCM_INFO(NDRPOINTER):
    referent = (
        ('Data', DATA_CUSTOMREMOTE_REQUEST_SCM_INFO),
    )

class CUSTOMREMOTE_REQUEST_SCM_INFO(NDRSTRUCT):
    structure = (
	('ClientImpLevel', DWORD),	('cRequestedProtseqs', UNSIGNED_SHORT),	('pRequestedProtseqs', PTR_CUSTOMREMOTE_REQUEST_SCM_INFO),

    )
        

class CUSTOMREMOTE_REPLY_SCM_INFO(NDRSTRUCT):
    structure = (
        ('Oxid', OXID),('pdsaOxidBindings', DUALSTRINGARRAY),('ipidRemUnknown', IPID),('authnHint', DWORD),('serverVersion', COMVERSION),
    )


class DATA_INSTANTIATIONINFODATA(NDRUniConformantArray):
    item = IID

class PTR_INSTANTIATIONINFODATA(NDRPOINTER):
    referent = (
        ('Data', DATA_INSTANTIATIONINFODATA),
    )

class INSTANTIATIONINFODATA(NDRSTRUCT):
    structure = (
	('classId', CLSID),	('classCtx', DWORD),	('actvflags', DWORD),	('fIsSurrogate', LONG),	('cIID', DWORD),	('instFlag', DWORD),	('pIID', PTR_INSTANTIATIONINFODATA),
	('thisSize', DWORD),	('clientCOMVersion', COMVERSION),
    )
        

class LOCATIONINFODATA(NDRSTRUCT):
    structure = (
        ('machineName', WCHAR_T),('processId', DWORD),('apartmentId', DWORD),('contextId', DWORD),
    )


class ACTIVATIONCONTEXTINFODATA(NDRSTRUCT):
    structure = (
        ('clientOK', LONG),('bReserved1', LONG),('dwReserved1', DWORD),('dwReserved2', DWORD),('pIFDClientCtx', MINTERFACEPOINTER),('pIFDPrototypeCtx', MINTERFACEPOINTER),
    )


class DATA_CUSTOMHEADER(NDRUniConformantArray):
    item = DWORD

class PTR_CUSTOMHEADER(NDRPOINTER):
    referent = (
        ('Data', DATA_CUSTOMHEADER),
    )

class CUSTOMHEADER(NDRSTRUCT):
    structure = (
	('totalSize', DWORD),	('headerSize', DWORD),	('dwReserved', DWORD),	('destCtx', DWORD),	('cIfs', DWORD),	('classInfoClsid', CLSID),	('pclsid', CLSID),	('pSizes', PTR_CUSTOMHEADER),
	('pdwReserved', DWORD),
    )
        

class DATA_PROPSOUTINFO(NDRUniConformantArray):
    item = MINTERFACEPOINTER

class PTR_PROPSOUTINFO(NDRPOINTER):
    referent = (
        ('Data', DATA_PROPSOUTINFO),
    )

class PROPSOUTINFO(NDRSTRUCT):
    structure = (
	('cIfs', DWORD),	('piid', IID),	('phresults', HRESULT),	('ppIntfData', PTR_PROPSOUTINFO),

    )
        

class SECURITYINFODATA(NDRSTRUCT):
    structure = (
        ('dwAuthnFlags', DWORD),('pServerInfo', COSERVERINFO),('pdwReserved', DWORD),
    )


class SCMREQUESTINFODATA(NDRSTRUCT):
    structure = (
        ('pdwReserved', DWORD),('remoteRequest', CUSTOMREMOTE_REQUEST_SCM_INFO),
    )


class SCMREPLYINFODATA(NDRSTRUCT):
    structure = (
        ('pdwReserved', DWORD),('remoteReply', CUSTOMREMOTE_REPLY_SCM_INFO),
    )


class INSTANCEINFODATA(NDRSTRUCT):
    structure = (
        ('fileName', WCHAR_T),('mode', DWORD),('ifdROT', MINTERFACEPOINTER),('ifdStg', MINTERFACEPOINTER),
    )


SPD_FLAG_USE_CONSOLE_SESSION = 1,
SPD_FLAG_USE_DEFAULT_AUTHN_LVL = 2
        

class SPECIALPROPERTIESDATA(NDRSTRUCT):
    structure = (
        ('dwSessionId', UNSIGNED_LONG),('fRemoteThisSessionId', LONG),('fClientImpersonating', LONG),('fPartitionIDPresent', LONG),('dwDefaultAuthnLvl', DWORD),('guidPartition', GUID),('dwPRTFlags', DWORD),('dwOrigClsctx', DWORD),('dwFlags', DWORD),('Reserved1', DWORD),('Reserved2', UNSIGNED___INT64),('Reserved3', DWORD),
    )


class SPECIALPROPERTIESDATA_ALTERNATE(NDRSTRUCT):
    structure = (
        ('dwSessionId', UNSIGNED_LONG),('fRemoteThisSessionId', LONG),('fClientImpersonating', LONG),('fPartitionIDPresent', LONG),('dwDefaultAuthnLvl', DWORD),('guidPartition', GUID),('dwPRTFlags', DWORD),('dwOrigClsctx', DWORD),('dwFlags', DWORD),('Reserved3', DWORD),
    )

#################################################################################

#CONSTANTS

#################################################################################

MIN_ACTPROP_LIMIT = 1
MAX_ACTPROP_LIMIT = 10
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IActivation Definition

#################################################################################

MSRPC_UUID_IACTIVATION = uuidtup_to_bin(('4d9f4ab8-7d1c-11cf-861e-0020af6e7c57','0.0'))

MAX_REQUESTED_INTERFACES = CONST_UNSIGNED_LONG
MAX_REQUESTED_PROTSEQS = CONST_UNSIGNED_LONG

class RemoteActivation(NDRCALL):
    opnum = 0
    structure = (
		('hRpc', HANDLE_T),
		('ORPCthis', ORPCTHIS),
		('Clsid', GUID),
		('pwszObjectName', WCHAR_T),
		('pObjectStorage', MINTERFACEPOINTER),
		('ClientImpLevel', DWORD),
		('Mode', DWORD),
		('Interfaces', DWORD),
		('pIIDs', IID),
		('cRequestedProtseqs', UNSIGNED_SHORT),
		('aRequestedProtseqs', UNSIGNED_SHORT),
    )

class RemoteActivationResponse(NDRCALL):
    structure = (
		('ORPCthat', ORPCTHAT),
		('pOxid', OXID),
		('ppdsaOxidBindings', DUALSTRINGARRAY),
		('pipidRemUnknown', IPID),
		('pAuthnHint', DWORD),
		('pServerVersion', COMVERSION),
		('phr', HRESULT),
		('ppInterfaceData', MINTERFACEPOINTER),
		('pResults', HRESULT),
    )
        
OPNUMS = {
0 : (RemoteActivation,RemoteActivationResponse),
}

#################################################################################

#IRemoteSCMActivator Definition

#################################################################################

MSRPC_UUID_IREMOTESCMACTIVATOR = uuidtup_to_bin(('000001A0-0000-0000-C000-000000000046','0.0'))


class Opnum0NotUsedOnWire(NDRCALL):
    opnum = 0
    structure = (

    )

class Opnum0NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum2NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum2NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RemoteGetClassObject(NDRCALL):
    opnum = 3
    structure = (
		('rpc', HANDLE_T),
		('orpcthis', ORPCTHIS),
		('pActProperties', MINTERFACEPOINTER),
    )

class RemoteGetClassObjectResponse(NDRCALL):
    structure = (
		('orpcthat', ORPCTHAT),
		('ppActProperties', MINTERFACEPOINTER),
    )
        

class RemoteCreateInstance(NDRCALL):
    opnum = 4
    structure = (
		('rpc', HANDLE_T),
		('orpcthis', ORPCTHIS),
		('pUnkOuter', MINTERFACEPOINTER),
		('pActProperties', MINTERFACEPOINTER),
    )

class RemoteCreateInstanceResponse(NDRCALL):
    structure = (
		('orpcthat', ORPCTHAT),
		('ppActProperties', MINTERFACEPOINTER),
    )
        
OPNUMS = {
0 : (Opnum0NotUsedOnWire,Opnum0NotUsedOnWireResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (Opnum2NotUsedOnWire,Opnum2NotUsedOnWireResponse),
3 : (RemoteGetClassObject,RemoteGetClassObjectResponse),
4 : (RemoteCreateInstance,RemoteCreateInstanceResponse),
}

#################################################################################

#IObjectExporter Definition

#################################################################################

MSRPC_UUID_IOBJECTEXPORTER = uuidtup_to_bin(('99fcfec4-5260-101b-bbcb-00aa0021347a','0.0'))


class ResolveOxid(NDRCALL):
    opnum = 0
    structure = (
		('hRpc', HANDLE_T),
		('pOxid', OXID),
		('cRequestedProtseqs', UNSIGNED_SHORT),
		('arRequestedProtseqs', UNSIGNED_SHORT),
    )

class ResolveOxidResponse(NDRCALL):
    structure = (
		('ppdsaOxidBindings', DUALSTRINGARRAY),
		('pipidRemUnknown', IPID),
		('pAuthnHint', DWORD),
    )
        

class SimplePing(NDRCALL):
    opnum = 1
    structure = (
		('hRpc', HANDLE_T),
		('pSetId', SETID),
    )

class SimplePingResponse(NDRCALL):
    structure = (

    )
        

class ComplexPing(NDRCALL):
    opnum = 2
    structure = (
		('hRpc', HANDLE_T),
		('pSetId', SETID),
		('SequenceNum', UNSIGNED_SHORT),
		('cAddToSet', UNSIGNED_SHORT),
		('cDelFromSet', UNSIGNED_SHORT),
		('AddToSet', OID),
		('DelFromSet', OID),
    )

class ComplexPingResponse(NDRCALL):
    structure = (
		('pSetId', SETID),
		('pPingBackoffFactor', UNSIGNED_SHORT),
    )
        

class ServerAlive(NDRCALL):
    opnum = 3
    structure = (
		('hRpc', HANDLE_T),
    )

class ServerAliveResponse(NDRCALL):
    structure = (

    )
        

class ResolveOxid2(NDRCALL):
    opnum = 4
    structure = (
		('hRpc', HANDLE_T),
		('pOxid', OXID),
		('cRequestedProtseqs', UNSIGNED_SHORT),
		('arRequestedProtseqs', UNSIGNED_SHORT),
    )

class ResolveOxid2Response(NDRCALL):
    structure = (
		('ppdsaOxidBindings', DUALSTRINGARRAY),
		('pipidRemUnknown', IPID),
		('pAuthnHint', DWORD),
		('pComVersion', COMVERSION),
    )
        

class ServerAlive2(NDRCALL):
    opnum = 5
    structure = (
		('hRpc', HANDLE_T),
    )

class ServerAlive2Response(NDRCALL):
    structure = (
		('pComVersion', COMVERSION),
		('ppdsaOrBindings', DUALSTRINGARRAY),
		('pReserved', DWORD),
    )
        
OPNUMS = {
0 : (ResolveOxid,ResolveOxidResponse),
1 : (SimplePing,SimplePingResponse),
2 : (ComplexPing,ComplexPingResponse),
3 : (ServerAlive,ServerAliveResponse),
4 : (ResolveOxid2,ResolveOxid2Response),
5 : (ServerAlive2,ServerAlive2Response),
}

#################################################################################

#IUnknown Definition

#################################################################################

MSRPC_UUID_IUNKNOWN = uuidtup_to_bin(('00000000-0000-0000-C000-000000000046','0.0'))


class Opnum0NotUsedOnWire(NDRCALL):
    opnum = 0
    structure = (

    )

class Opnum0NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum2NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum2NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Opnum0NotUsedOnWire,Opnum0NotUsedOnWireResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (Opnum2NotUsedOnWire,Opnum2NotUsedOnWireResponse),
}

#################################################################################

#IRemUnknown Definition

#################################################################################

MSRPC_UUID_IREMUNKNOWN = uuidtup_to_bin(('00000131-0000-0000-C000-000000000046','0.0'))


class RemQueryInterface(NDRCALL):
    opnum = 0
    structure = (
		('ripid', REFIPID),
		('cRefs', UNSIGNED_LONG),
		('cIids', UNSIGNED_SHORT),
		('iids', IID),
    )

class RemQueryInterfaceResponse(NDRCALL):
    structure = (
		('ppQIResults', PREMQIRESULT),
    )
        

class RemAddRef(NDRCALL):
    opnum = 1
    structure = (
		('cInterfaceRefs', UNSIGNED_SHORT),
		('InterfaceRefs', REMINTERFACEREF),
    )

class RemAddRefResponse(NDRCALL):
    structure = (
		('pResults', HRESULT),
    )
        

class RemRelease(NDRCALL):
    opnum = 2
    structure = (
		('cInterfaceRefs', UNSIGNED_SHORT),
		('InterfaceRefs', REMINTERFACEREF),
    )

class RemReleaseResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RemQueryInterface,RemQueryInterfaceResponse),
1 : (RemAddRef,RemAddRefResponse),
2 : (RemRelease,RemReleaseResponse),
}

#################################################################################

#IRemUnknown2 Definition

#################################################################################

MSRPC_UUID_IREMUNKNOWN2 = uuidtup_to_bin(('00000143-0000-0000-C000-000000000046','0.0'))


class RemQueryInterface2(NDRCALL):
    opnum = 0
    structure = (
		('ripid', REFIPID),
		('cIids', UNSIGNED_SHORT),
		('iids', IID),
    )

class RemQueryInterface2Response(NDRCALL):
    structure = (
		('phr', HRESULT),
		('ppMIF', PMINTERFACEPOINTERINTERNAL),
    )
        
OPNUMS = {
0 : (RemQueryInterface2,RemQueryInterface2Response),
}

#################################################################################

#TYPEDEFS

#################################################################################

BYTE = BYTE
SCODE = LONG
REFIID = IID
REFGUID = GUID
LPOLESTR = WCHAR_T
LPCOLESTR = CONST_WCHAR_T
ULONG_PTR = UNSIGNED___INT3264
PULONG_PTR = UNSIGNED___INT3264
PVOID = VOID
LPVOID = VOID
PSAFEARRAY = SAFEARRAY
LPSAFEARRAY = SAFEARRAY

class VARIANT(NDRSTRUCT):
    structure = (
        
    )


VT_EMPTY = 0,
VT_NULL = 1,
VT_I2 = 2,
VT_I4 = 3,
VT_R4 = 4,
VT_R8 = 5,
VT_CY = 6,
VT_DATE = 7,
VT_BSTR = 8,
VT_DISPATCH = 9,
VT_ERROR = 10,
VT_BOOL = 11,
VT_VARIANT = 12,
VT_UNKNOWN = 13,
VT_DECIMAL = 14,
VT_I1 = 16,
VT_UI1 = 17,
VT_UI2 = 18,
VT_UI4 = 19,
VT_I8 = 20,
VT_UI8 = 21,
VT_INT = 22,
VT_UINT = 23,
VT_VOID = 24,
VT_HRESULT = 25,
VT_PTR = 26,
VT_SAFEARRAY = 27,
VT_CARRAY = 28,
VT_USERDEFINED = 29,
VT_LPSTR = 30,
VT_LPWSTR = 31,
VT_RECORD = 36,
VT_INT_PTR = 37,
VT_UINT_PTR = 38,
VT_ARRAY = 8192,
VT_BYREF = 16384
        

FADF_AUTO = 1,
FADF_STATIC = 2,
FADF_EMBEDDED = 4,
FADF_FIXEDSIZE = 16,
FADF_RECORD = 32,
FADF_HAVEIID = 64,
FADF_HAVEVARTYPE = 128,
FADF_BSTR = 256,
FADF_UNKNOWN = 512,
FADF_DISPATCH = 1024,
FADF_VARIANT = 2048
        

SF_ERROR = VT_ERROR,
SF_I1 = VT_I1,
SF_I2 = VT_I2,
SF_I4 = VT_I4,
SF_I8 = VT_I8,
SF_BSTR = VT_BSTR,
SF_UNKNOWN = VT_UNKNOWN,
SF_DISPATCH = VT_DISPATCH,
SF_VARIANT = VT_VARIANT,
SF_RECORD = VT_RECORD,
SF_HAVEIID = 32768
        

CC_CDECL = 1,
CC_PASCAL = 2,
CC_STDCALL = 4
        

FUNCFLAG_FRESTRICTED = 1,
FUNCFLAG_FSOURCE = 2,
FUNCFLAG_FBINDABLE = 4,
FUNCFLAG_FREQUESTEDIT = 8,
FUNCFLAG_FDISPLAYBIND = 16,
FUNCFLAG_FDEFAULTBIND = 32,
FUNCFLAG_FHIDDEN = 64,
FUNCFLAG_FUSESGETLASTERROR = 128,
FUNCFLAG_FDEFAULTCOLLELEM = 256,
FUNCFLAG_FUIDEFAULT = 512,
FUNCFLAG_FNONBROWSABLE = 1024,
FUNCFLAG_FREPLACEABLE = 2048,
FUNCFLAG_FIMMEDIATEBIND = 4096
        

FUNC_PUREVIRTUAL = 1,
FUNC_STATIC = 3,
FUNC_DISPATCH = 4
        

IMPLTYPEFLAG_FDEFAULT = 1,
IMPLTYPEFLAG_FSOURCE = 2,
IMPLTYPEFLAG_FRESTRICTED = 4,
IMPLTYPEFLAG_FDEFAULTVTABLE = 8
        

INVOKE_FUNC = 1,
INVOKE_PROPERTYGET = 2,
INVOKE_PROPERTYPUT = 4,
INVOKE_PROPERTYPUTREF = 8
        

PARAMFLAG_NONE = 0,
PARAMFLAG_FIN = 1,
PARAMFLAG_FOUT = 2,
PARAMFLAG_FLCID = 4,
PARAMFLAG_FRETVAL = 8,
PARAMFLAG_FOPT = 16,
PARAMFLAG_FHASDEFAULT = 32,
PARAMFLAG_FHASCUSTDATA = 64
        

TYPEFLAG_FAPPOBJECT = 1,
TYPEFLAG_FCANCREATE = 2,
TYPEFLAG_FLICENSED = 4,
TYPEFLAG_FPREDECLID = 8,
TYPEFLAG_FHIDDEN = 16,
TYPEFLAG_FCONTROL = 32,
TYPEFLAG_FDUAL = 64,
TYPEFLAG_FNONEXTENSIBLE = 128,
TYPEFLAG_FOLEAUTOMATION = 256,
TYPEFLAG_FRESTRICTED = 512,
TYPEFLAG_FAGGREGATABLE = 1024,
TYPEFLAG_FREPLACEABLE = 2048,
TYPEFLAG_FDISPATCHABLE = 4096,
TYPEFLAG_FPROXY = 16384
        

TKIND_ENUM = 0,
TKIND_RECORD = 1,
TKIND_MODULE = 2,
TKIND_INTERFACE = 3,
TKIND_DISPATCH = 4,
TKIND_COCLASS = 5,
TKIND_ALIAS = 6,
TKIND_UNION = 7
        

VARFLAG_FREADONLY = 1,
VARFLAG_FSOURCE = 2,
VARFLAG_FBINDABLE = 4,
VARFLAG_FREQUESTEDIT = 8,
VARFLAG_FDISPLAYBIND = 16,
VARFLAG_FDEFAULTBIND = 32,
VARFLAG_FHIDDEN = 64,
VARFLAG_FRESTRICTED = 128,
VARFLAG_FDEFAULTCOLLELEM = 256,
VARFLAG_FUIDEFAULT = 512,
VARFLAG_FNONBROWSABLE = 1024,
VARFLAG_FREPLACEABLE = 2048,
VARFLAG_FIMMEDIATEBIND = 4096
        

VAR_PERINSTANCE = 0,
VAR_STATIC = 1),
VAR_CONST = 1),
VAR_DISPATCH = 1)
        

LIBFLAG_FRESTRICTED = 1,
LIBFLAG_FCONTROL = 2,
LIBFLAG_FHIDDEN = 4,
LIBFLAG_FHASDISKIMAGE = 8
        

SYS_WIN32 = 1,
SYS_WIN64 = 3
        

DESCKIND_NONE = 0,
DESCKIND_FUNCDESC = 1,
DESCKIND_VARDESC = 2,
DESCKIND_TYPECOMP = 3,
DESCKIND_IMPLICITAPPOBJ = 4
        

class FLAGGED_WORD_BLOB(NDRSTRUCT):
    structure = (
        ('cBytes', UNSIGNED_LONG),('clSize', UNSIGNED_LONG),('asData', UNSIGNED_SHORT),
    )

BSTR = FLAGGED_WORD_BLOB

class CURRENCY(NDRSTRUCT):
    structure = (
        ('int64', __INT64),
    )

DATE = DOUBLE

class DECIMAL(NDRSTRUCT):
    structure = (
        ('wReserved', WORD),('scale', BYTE),('sign', BYTE),('Hi32', ULONG),('Lo64', ULONGLONG),
    )

VARIANT_BOOL = SHORT

class DATA_WIREBRECORDSTR(NDRUniConformantArray):
    item = BYTE

class PTR_WIREBRECORDSTR(NDRPOINTER):
    referent = (
        ('Data', DATA_WIREBRECORDSTR),
    )

class WIREBRECORDSTR(NDRSTRUCT):
    structure = (
	('fFlags', ULONG),	('clSize', ULONG),	('pRecInfo', MINTERFACEPOINTER),	('pRecord', PTR_WIREBRECORDSTR),

    )
        

class BRECORD(NDRSTRUCT):
    structure = (
        
    )


class _VARUNION(NDRUNION):
    union = {
        VT_I8: ('llVal',LONGLONG),VT_I4: ('lVal',LONG),VT_UI1: ('bVal',BYTE),VT_I2: ('iVal',SHORT),VT_R4: ('fltVal',FLOAT),VT_R8: ('dblVal',DOUBLE),VT_BOOL: ('boolVal',VARIANT_BOOL),VT_ERROR: ('scode',HRESULT),VT_CY: ('cyVal',CURRENCY),VT_DATE: ('date',DATE),VT_BSTR: ('bstrVal',BSTR),VT_UNKNOWN: ('punkVal',IUNKNOWN),VT_DISPATCH: ('pdispVal',IDISPATCH),VT_ARRAY: ('parray',PSAFEARRAY),VT_RECORD: ('brecVal',BRECORD),VT_UI1|VT_BYREF: ('pbVal',BYTE),VT_I2|VT_BYREF: ('piVal',SHORT),VT_I4|VT_BYREF: ('plVal',LONG),VT_I8|VT_BYREF: ('pllVal',LONGLONG),VT_R4|VT_BYREF: ('pfltVal',FLOAT),VT_R8|VT_BYREF: ('pdblVal',DOUBLE),VT_BOOL|VT_BYREF: ('pboolVal',VARIANT_BOOL),VT_ERROR|VT_BYREF: ('pscode',HRESULT),VT_CY|VT_BYREF: ('pcyVal',CURRENCY),VT_DATE|VT_BYREF: ('pdate',DATE),VT_BSTR|VT_BYREF: ('pbstrVal',BSTR),VT_UNKNOWN|VT_BYREF: ('ppunkVal',IUNKNOWN),VT_DISPATCH|VT_BYREF: ('ppdispVal',IDISPATCH),VT_ARRAY|VT_BYREF: ('pparray',PSAFEARRAY),VT_VARIANT|VT_BYREF: ('pvarVal',VARIANT),VT_I1: ('cVal',CHAR),VT_UI2: ('uiVal',USHORT),VT_UI4: ('ulVal',ULONG),VT_UI8: ('ullVal',ULONGLONG),VT_INT: ('intVal',INT),VT_UINT: ('uintVal',UINT),VT_DECIMAL: ('decVal',DECIMAL),VT_I1|VT_BYREF: ('pcVal',CHAR),VT_UI2|VT_BYREF: ('puiVal',USHORT),VT_UI4|VT_BYREF: ('pulVal',ULONG),VT_UI8|VT_BYREF: ('pullVal',ULONGLONG),VT_INT|VT_BYREF: ('pintVal',INT),VT_UINT|VT_BYREF: ('puintVal',UINT),VT_DECIMAL|VT_BYREF: ('pdecVal',DECIMAL),
    }
        

class WIREVARIANTSTR(NDRSTRUCT):
    structure = (
        ('clSize', DWORD),('rpcReserved', DWORD),('vt', USHORT),('wReserved1', USHORT),('wReserved2', USHORT),('wReserved3', USHORT),('_varUnion', _VARUNION),
    )


class SAFEARRAYBOUND(NDRSTRUCT):
    structure = (
        ('cElements', ULONG),('lLbound', LONG),
    )
class LPSAFEARRAYBOUND(NDRPOINTER):
    referent = (
        ('Data', SAFEARRAYBOUND),
    )    


class DATA_SAFEARR_BSTR(NDRUniConformantArray):
    item = BSTR

class PTR_SAFEARR_BSTR(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_BSTR),
    )

class SAFEARR_BSTR(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aBstr', PTR_SAFEARR_BSTR),

    )
        

class DATA_SAFEARR_UNKNOWN(NDRUniConformantArray):
    item = IUNKNOWN

class PTR_SAFEARR_UNKNOWN(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_UNKNOWN),
    )

class SAFEARR_UNKNOWN(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apUnknown', PTR_SAFEARR_UNKNOWN),

    )
        

class DATA_SAFEARR_DISPATCH(NDRUniConformantArray):
    item = IDISPATCH

class PTR_SAFEARR_DISPATCH(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_DISPATCH),
    )

class SAFEARR_DISPATCH(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apDispatch', PTR_SAFEARR_DISPATCH),

    )
        

class DATA_SAFEARR_VARIANT(NDRUniConformantArray):
    item = VARIANT

class PTR_SAFEARR_VARIANT(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_VARIANT),
    )

class SAFEARR_VARIANT(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aVariant', PTR_SAFEARR_VARIANT),

    )
        

class DATA_SAFEARR_BRECORD(NDRUniConformantArray):
    item = BRECORD

class PTR_SAFEARR_BRECORD(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_BRECORD),
    )

class SAFEARR_BRECORD(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aRecord', PTR_SAFEARR_BRECORD),

    )
        

class DATA_SAFEARR_HAVEIID(NDRUniConformantArray):
    item = IUNKNOWN

class PTR_SAFEARR_HAVEIID(NDRPOINTER):
    referent = (
        ('Data', DATA_SAFEARR_HAVEIID),
    )

class SAFEARR_HAVEIID(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apUnknown', PTR_SAFEARR_HAVEIID),
	('iid', IID),
    )
        

class DATA_BYTE_SIZEDARR(NDRUniConformantArray):
    item = BYTE

class PTR_BYTE_SIZEDARR(NDRPOINTER):
    referent = (
        ('Data', DATA_BYTE_SIZEDARR),
    )

class BYTE_SIZEDARR(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_BYTE_SIZEDARR),

    )
        

class DATA_WORD_SIZEDARR(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_WORD_SIZEDARR(NDRPOINTER):
    referent = (
        ('Data', DATA_WORD_SIZEDARR),
    )

class WORD_SIZEDARR(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_WORD_SIZEDARR),

    )
        

class DATA_DWORD_SIZEDARR(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_DWORD_SIZEDARR(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD_SIZEDARR),
    )

class DWORD_SIZEDARR(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_DWORD_SIZEDARR),

    )
        

class DATA_HYPER_SIZEDARR(NDRUniConformantArray):
    item = HYPER

class PTR_HYPER_SIZEDARR(NDRPOINTER):
    referent = (
        ('Data', DATA_HYPER_SIZEDARR),
    )

class HYPER_SIZEDARR(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_HYPER_SIZEDARR),

    )
        

class ANONYMOUS21(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous21', ANONYMOUS21),
    )


class SAFEARRAY(NDRSTRUCT):
    structure = (
        ('cDims', USHORT),('fFeatures', USHORT),('cbElements', ULONG),('cLocks', ULONG),('uArrayStructs', SAFEARRAYUNION),('rgsabound', SAFEARRAYBOUND),
    )


class RECORDINFO(NDRSTRUCT):
    structure = (
        ('libraryGuid', GUID),('verMajor', DWORD),('recGuid', GUID),('verMinor', DWORD),('Lcid', DWORD),
    )

DISPID = LONG

class DATA_DISPPARAMS(NDRUniConformantArray):
    item = DISPID

class PTR_DISPPARAMS(NDRPOINTER):
    referent = (
        ('Data', DATA_DISPPARAMS),
    )

class DISPPARAMS(NDRSTRUCT):
    structure = (
	('rgvarg', VARIANT),	('rgdispidNamedArgs', PTR_DISPPARAMS),
	('cArgs', UINT),	('cNamedArgs', UINT),
    )
        

class EXCEPINFO(NDRSTRUCT):
    structure = (
        ('wCode', WORD),('wReserved', WORD),('bstrSource', BSTR),('bstrDescription', BSTR),('bstrHelpFile', BSTR),('dwHelpContext', DWORD),('pvReserved', ULONG_PTR),('pfnDeferredFillIn', ULONG_PTR),('scode', HRESULT),
    )

MEMBERID = DISPID
HREFTYPE = DWORD

class LPTDESC(NDRSTRUCT):
    structure = (
        
    )


class LPADESC(NDRSTRUCT):
    structure = (
        
    )


class _TDUNION(NDRUNION):
    union = {
        VT_USERDEFINED: ('*lptdesc',LPTDESC),VT_USERDEFINED: ('*lpadesc',LPADESC),VT_USERDEFINED: ('hreftype',HREFTYPE),
    }
        

class TYPEDESC(NDRSTRUCT):
    structure = (
        ('_tdUnion', _TDUNION),('vt', USHORT),
    )


class ARRAYDESC(NDRSTRUCT):
    structure = (
        ('tdescElem', TYPEDESC),('cDims', USHORT),('rgbounds', SAFEARRAYBOUND),
    )


class PARAMDESCEX(NDRSTRUCT):
    structure = (
        ('cBytes', ULONG),('varDefaultValue', VARIANT),
    )


class PARAMDESC(NDRSTRUCT):
    structure = (
        ('pparamdescex', PARAMDESCEX),('wParamFlags', USHORT),
    )


class ELEMDESC(NDRSTRUCT):
    structure = (
        ('tdesc', TYPEDESC),('paramdesc', PARAMDESC),
    )


class DATA_FUNCDESC(NDRUniConformantArray):
    item = ELEMDESC

class PTR_FUNCDESC(NDRPOINTER):
    referent = (
        ('Data', DATA_FUNCDESC),
    )

class FUNCDESC(NDRSTRUCT):
    structure = (
	('memid', MEMBERID),	('lReserved1', SCODE),	('lprgelemdescParam', PTR_FUNCDESC),
	('funckind', FUNCKIND),	('invkind', INVOKEKIND),	('callconv', CALLCONV),	('cParams', SHORT),	('cParamsOpt', SHORT),	('oVft', SHORT),	('cReserved2', SHORT),	('elemdescFunc', ELEMDESC),	('wFuncFlags', WORD),
    )
        

class _VDUNION(NDRUNION):
    union = {
        VAR_PERINSTANCE: ('oInst',ULONG),VAR_CONST: ('lpvarValue',VARIANT),
    }
        

class VARDESC(NDRSTRUCT):
    structure = (
        ('memid', MEMBERID),('lpstrReserved', LPOLESTR),('_vdUnion', _VDUNION),('elemdescVar', ELEMDESC),('wVarFlags', WORD),('varkind', VARKIND),
    )
class LPVARDESC(NDRPOINTER):
    referent = (
        ('Data', VARDESC),
    )    


class TYPEATTR(NDRSTRUCT):
    structure = (
        ('guid', GUID),('lcid', LCID),('dwReserved1', DWORD),('dwReserved2', DWORD),('dwReserved3', DWORD),('lpstrReserved4', LPOLESTR),('cbSizeInstance', ULONG),('typekind', TYPEKIND),('cFuncs', WORD),('cVars', WORD),('cImplTypes', WORD),('cbSizeVft', WORD),('cbAlignment', WORD),('wTypeFlags', WORD),('wMajorVerNum', WORD),('wMinorVerNum', WORD),('tdescAlias', TYPEDESC),('dwReserved5', DWORD),('wReserved6', WORD),
    )
class LPTYPEATTR(NDRPOINTER):
    referent = (
        ('Data', TYPEATTR),
    )    


class TLIBATTR(NDRSTRUCT):
    structure = (
        ('guid', GUID),('lcid', LCID),('syskind', SYSKIND),('wMajorVerNum', UNSIGNED_SHORT),('wMinorVerNum', UNSIGNED_SHORT),('wLibFlags', UNSIGNED_SHORT),
    )
class LPTLIBATTR(NDRPOINTER):
    referent = (
        ('Data', TLIBATTR),
    )    


class CUSTDATAITEM(NDRSTRUCT):
    structure = (
        ('guid', GUID),('varValue', VARIANT),
    )


class DATA_CUSTDATA(NDRUniConformantArray):
    item = CUSTDATAITEM

class PTR_CUSTDATA(NDRPOINTER):
    referent = (
        ('Data', DATA_CUSTDATA),
    )

class CUSTDATA(NDRSTRUCT):
    structure = (
	('cCustData', DWORD),	('prgCustData', PTR_CUSTDATA),

    )
        
#################################################################################

#CONSTANTS

#################################################################################

IDISPATCH = 
ITYPELIB = 
ITYPEINFO = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IDispatch Definition

#################################################################################

MSRPC_UUID_IDISPATCH = uuidtup_to_bin(('00020400-0000-0000-C000-000000000046','0.0'))

DISPATCH_METHOD =  DWORD
DISPATCH_PROPERTYGET =  DWORD
DISPATCH_PROPERTYPUT =  DWORD
DISPATCH_PROPERTYPUTREF =  DWORD
DISPATCH_zeroVarResult =  DWORD
DISPATCH_zeroExcepInfo =  DWORD
DISPATCH_zeroArgErr =  DWORD
DISPID_VALUE =  DISPID
DISPID_UNKNOWN =  DISPID
DISPID_PROPERTYPUT =  DISPID
DISPID_NEWENUM =  DISPID
LPDISPATCH = IDISPATCH

class GetTypeInfoCount(NDRCALL):
    opnum = 0
    structure = (

    )

class GetTypeInfoCountResponse(NDRCALL):
    structure = (
		('pctinfo', UINT),
    )
        

class GetTypeInfo(NDRCALL):
    opnum = 1
    structure = (
		('iTInfo', UINT),
		('lcid', LCID),
    )

class GetTypeInfoResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
    )
        

class GetIDsOfNames(NDRCALL):
    opnum = 2
    structure = (
		('riid', REFIID),
		('rgszNames', LPOLESTR),
		('cNames', UINT),
		('lcid', LCID),
    )

class GetIDsOfNamesResponse(NDRCALL):
    structure = (
		('rgDispId', DISPID),
    )
        

class Invoke(NDRCALL):
    opnum = 3
    structure = (
		('dispIdMember', DISPID),
		('riid', REFIID),
		('lcid', LCID),
		('dwFlags', DWORD),
		('pDispParams', DISPPARAMS),
		('cVarRef', UINT),
		('rgVarRefIdx', UINT),
		('rgVarRef', VARIANT),
    )

class InvokeResponse(NDRCALL):
    structure = (
		('pVarResult', VARIANT),
		('pExcepInfo', EXCEPINFO),
		('pArgErr', UINT),
		('rgVarRef', VARIANT),
    )
        
OPNUMS = {
0 : (GetTypeInfoCount,GetTypeInfoCountResponse),
1 : (GetTypeInfo,GetTypeInfoResponse),
2 : (GetIDsOfNames,GetIDsOfNamesResponse),
3 : (Invoke,InvokeResponse),
}

#################################################################################

#IEnumVARIANT Definition

#################################################################################

MSRPC_UUID_IENUMVARIANT = uuidtup_to_bin(('00020404-0000-0000-C000-000000000046','0.0'))


class Next(NDRCALL):
    opnum = 0
    structure = (
		('celt', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('rgVar', VARIANT),
		('pCeltFetched', ULONG),
    )
        

class Skip(NDRCALL):
    opnum = 1
    structure = (
		('celt', ULONG),
    )

class SkipResponse(NDRCALL):
    structure = (

    )
        

class Reset(NDRCALL):
    opnum = 2
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class Clone(NDRCALL):
    opnum = 3
    structure = (

    )

class CloneResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMVARIANT),
    )
        
OPNUMS = {
0 : (Next,NextResponse),
1 : (Skip,SkipResponse),
2 : (Reset,ResetResponse),
3 : (Clone,CloneResponse),
}

#################################################################################

#ITypeComp Definition

#################################################################################

MSRPC_UUID_ITYPECOMP = uuidtup_to_bin(('00020403-0000-0000-C000-000000000046','0.0'))


class Bind(NDRCALL):
    opnum = 0
    structure = (
		('szName', LPOLESTR),
		('lHashVal', ULONG),
		('wFlags', WORD),
    )

class BindResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
		('pDescKind', DESCKIND),
		('ppFuncDesc', LPFUNCDESC),
		('ppVarDesc', LPVARDESC),
		('ppTypeComp', ITYPECOMP),
		('pReserved', DWORD),
    )
        

class BindType(NDRCALL):
    opnum = 1
    structure = (
		('szName', LPOLESTR),
		('lHashVal', ULONG),
    )

class BindTypeResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
    )
        
OPNUMS = {
0 : (Bind,BindResponse),
1 : (BindType,BindTypeResponse),
}

#################################################################################

#ITypeInfo Definition

#################################################################################

MSRPC_UUID_ITYPEINFO = uuidtup_to_bin(('00020401-0000-0000-C000-000000000046','0.0'))


class GetTypeAttr(NDRCALL):
    opnum = 0
    structure = (

    )

class GetTypeAttrResponse(NDRCALL):
    structure = (
		('ppTypeAttr', LPTYPEATTR),
		('pReserved', DWORD),
    )
        

class GetTypeComp(NDRCALL):
    opnum = 1
    structure = (

    )

class GetTypeCompResponse(NDRCALL):
    structure = (
		('ppTComp', ITYPECOMP),
    )
        

class GetFuncDesc(NDRCALL):
    opnum = 2
    structure = (
		('index', UINT),
    )

class GetFuncDescResponse(NDRCALL):
    structure = (
		('ppFuncDesc', LPFUNCDESC),
		('pReserved', DWORD),
    )
        

class GetVarDesc(NDRCALL):
    opnum = 3
    structure = (
		('index', UINT),
    )

class GetVarDescResponse(NDRCALL):
    structure = (
		('ppVarDesc', LPVARDESC),
		('pReserved', DWORD),
    )
        

class GetNames(NDRCALL):
    opnum = 4
    structure = (
		('memid', MEMBERID),
		('cMaxNames', UINT),
    )

class GetNamesResponse(NDRCALL):
    structure = (
		('rgBstrNames', BSTR),
		('pcNames', UINT),
    )
        

class GetRefTypeOfImplType(NDRCALL):
    opnum = 5
    structure = (
		('index', UINT),
    )

class GetRefTypeOfImplTypeResponse(NDRCALL):
    structure = (
		('pRefType', HREFTYPE),
    )
        

class GetImplTypeFlags(NDRCALL):
    opnum = 6
    structure = (
		('index', UINT),
    )

class GetImplTypeFlagsResponse(NDRCALL):
    structure = (
		('pImplTypeFlags', INT),
    )
        

class Opnum10NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum10NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum11NotUsedOnWire(NDRCALL):
    opnum = 8
    structure = (

    )

class Opnum11NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class GetDocumentation(NDRCALL):
    opnum = 9
    structure = (
		('memid', MEMBERID),
		('refPtrFlags', DWORD),
    )

class GetDocumentationResponse(NDRCALL):
    structure = (
		('pBstrName', BSTR),
		('pBstrDocString', BSTR),
		('pdwHelpContext', DWORD),
		('pBstrHelpFile', BSTR),
    )
        

class GetDllEntry(NDRCALL):
    opnum = 10
    structure = (
		('memid', MEMBERID),
		('invKind', INVOKEKIND),
		('refPtrFlags', DWORD),
    )

class GetDllEntryResponse(NDRCALL):
    structure = (
		('pBstrDllName', BSTR),
		('pBstrName', BSTR),
		('pwOrdinal', WORD),
    )
        

class GetRefTypeInfo(NDRCALL):
    opnum = 11
    structure = (
		('hRefType', HREFTYPE),
    )

class GetRefTypeInfoResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
    )
        

class Opnum15NotUsedOnWire(NDRCALL):
    opnum = 12
    structure = (

    )

class Opnum15NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class CreateInstance(NDRCALL):
    opnum = 13
    structure = (
		('riid', REFIID),
    )

class CreateInstanceResponse(NDRCALL):
    structure = (
		('ppvObj', IUNKNOWN),
    )
        

class GetMops(NDRCALL):
    opnum = 14
    structure = (
		('memid', MEMBERID),
    )

class GetMopsResponse(NDRCALL):
    structure = (
		('pBstrMops', BSTR),
    )
        

class GetContainingTypeLib(NDRCALL):
    opnum = 15
    structure = (

    )

class GetContainingTypeLibResponse(NDRCALL):
    structure = (
		('ppTLib', ITYPELIB),
		('pIndex', UINT),
    )
        

class Opnum19NotUsedOnWire(NDRCALL):
    opnum = 16
    structure = (

    )

class Opnum19NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum20NotUsedOnWire(NDRCALL):
    opnum = 17
    structure = (

    )

class Opnum20NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum21NotUsedOnWire(NDRCALL):
    opnum = 18
    structure = (

    )

class Opnum21NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (GetTypeAttr,GetTypeAttrResponse),
1 : (GetTypeComp,GetTypeCompResponse),
2 : (GetFuncDesc,GetFuncDescResponse),
3 : (GetVarDesc,GetVarDescResponse),
4 : (GetNames,GetNamesResponse),
5 : (GetRefTypeOfImplType,GetRefTypeOfImplTypeResponse),
6 : (GetImplTypeFlags,GetImplTypeFlagsResponse),
7 : (Opnum10NotUsedOnWire,Opnum10NotUsedOnWireResponse),
8 : (Opnum11NotUsedOnWire,Opnum11NotUsedOnWireResponse),
9 : (GetDocumentation,GetDocumentationResponse),
10 : (GetDllEntry,GetDllEntryResponse),
11 : (GetRefTypeInfo,GetRefTypeInfoResponse),
12 : (Opnum15NotUsedOnWire,Opnum15NotUsedOnWireResponse),
13 : (CreateInstance,CreateInstanceResponse),
14 : (GetMops,GetMopsResponse),
15 : (GetContainingTypeLib,GetContainingTypeLibResponse),
16 : (Opnum19NotUsedOnWire,Opnum19NotUsedOnWireResponse),
17 : (Opnum20NotUsedOnWire,Opnum20NotUsedOnWireResponse),
18 : (Opnum21NotUsedOnWire,Opnum21NotUsedOnWireResponse),
}

#################################################################################

#ITypeInfo2 Definition

#################################################################################

MSRPC_UUID_ITYPEINFO2 = uuidtup_to_bin(('00020412-0000-0000-C000-000000000046','0.0'))


class GetTypeKind(NDRCALL):
    opnum = 0
    structure = (

    )

class GetTypeKindResponse(NDRCALL):
    structure = (
		('pTypeKind', TYPEKIND),
    )
        

class GetTypeFlags(NDRCALL):
    opnum = 1
    structure = (

    )

class GetTypeFlagsResponse(NDRCALL):
    structure = (
		('pTypeFlags', ULONG),
    )
        

class GetFuncIndexOfMemId(NDRCALL):
    opnum = 2
    structure = (
		('memid', MEMBERID),
		('invKind', INVOKEKIND),
    )

class GetFuncIndexOfMemIdResponse(NDRCALL):
    structure = (
		('pFuncIndex', UINT),
    )
        

class GetVarIndexOfMemId(NDRCALL):
    opnum = 3
    structure = (
		('memid', MEMBERID),
    )

class GetVarIndexOfMemIdResponse(NDRCALL):
    structure = (
		('pVarIndex', UINT),
    )
        

class GetCustData(NDRCALL):
    opnum = 4
    structure = (
		('guid', REFGUID),
    )

class GetCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetFuncCustData(NDRCALL):
    opnum = 5
    structure = (
		('index', UINT),
		('guid', REFGUID),
    )

class GetFuncCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetParamCustData(NDRCALL):
    opnum = 6
    structure = (
		('indexFunc', UINT),
		('indexParam', UINT),
		('guid', REFGUID),
    )

class GetParamCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetVarCustData(NDRCALL):
    opnum = 7
    structure = (
		('index', UINT),
		('guid', REFGUID),
    )

class GetVarCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetImplTypeCustData(NDRCALL):
    opnum = 8
    structure = (
		('index', UINT),
		('guid', REFGUID),
    )

class GetImplTypeCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetDocumentation2(NDRCALL):
    opnum = 9
    structure = (
		('memid', MEMBERID),
		('lcid', LCID),
		('refPtrFlags', DWORD),
    )

class GetDocumentation2Response(NDRCALL):
    structure = (
		('pbstrHelpString', BSTR),
		('pdwHelpStringContext', DWORD),
		('pbstrHelpStringDll', BSTR),
    )
        

class GetAllCustData(NDRCALL):
    opnum = 10
    structure = (

    )

class GetAllCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        

class GetAllFuncCustData(NDRCALL):
    opnum = 11
    structure = (
		('index', UINT),
    )

class GetAllFuncCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        

class GetAllParamCustData(NDRCALL):
    opnum = 12
    structure = (
		('indexFunc', UINT),
		('indexParam', UINT),
    )

class GetAllParamCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        

class GetAllVarCustData(NDRCALL):
    opnum = 13
    structure = (
		('index', UINT),
    )

class GetAllVarCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        

class GetAllImplTypeCustData(NDRCALL):
    opnum = 14
    structure = (
		('index', UINT),
    )

class GetAllImplTypeCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        
OPNUMS = {
0 : (GetTypeKind,GetTypeKindResponse),
1 : (GetTypeFlags,GetTypeFlagsResponse),
2 : (GetFuncIndexOfMemId,GetFuncIndexOfMemIdResponse),
3 : (GetVarIndexOfMemId,GetVarIndexOfMemIdResponse),
4 : (GetCustData,GetCustDataResponse),
5 : (GetFuncCustData,GetFuncCustDataResponse),
6 : (GetParamCustData,GetParamCustDataResponse),
7 : (GetVarCustData,GetVarCustDataResponse),
8 : (GetImplTypeCustData,GetImplTypeCustDataResponse),
9 : (GetDocumentation2,GetDocumentation2Response),
10 : (GetAllCustData,GetAllCustDataResponse),
11 : (GetAllFuncCustData,GetAllFuncCustDataResponse),
12 : (GetAllParamCustData,GetAllParamCustDataResponse),
13 : (GetAllVarCustData,GetAllVarCustDataResponse),
14 : (GetAllImplTypeCustData,GetAllImplTypeCustDataResponse),
}

#################################################################################

#ITypeLib Definition

#################################################################################

MSRPC_UUID_ITYPELIB = uuidtup_to_bin(('00020402-0000-0000-C000-000000000046','0.0'))


class GetTypeInfoCount(NDRCALL):
    opnum = 0
    structure = (

    )

class GetTypeInfoCountResponse(NDRCALL):
    structure = (
		('pcTInfo', UINT),
    )
        

class GetTypeInfo(NDRCALL):
    opnum = 1
    structure = (
		('index', UINT),
    )

class GetTypeInfoResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
    )
        

class GetTypeInfoType(NDRCALL):
    opnum = 2
    structure = (
		('index', UINT),
    )

class GetTypeInfoTypeResponse(NDRCALL):
    structure = (
		('pTKind', TYPEKIND),
    )
        

class GetTypeInfoOfGuid(NDRCALL):
    opnum = 3
    structure = (
		('guid', REFGUID),
    )

class GetTypeInfoOfGuidResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
    )
        

class GetLibAttr(NDRCALL):
    opnum = 4
    structure = (

    )

class GetLibAttrResponse(NDRCALL):
    structure = (
		('ppTLibAttr', LPTLIBATTR),
		('pReserved', DWORD),
    )
        

class GetTypeComp(NDRCALL):
    opnum = 5
    structure = (

    )

class GetTypeCompResponse(NDRCALL):
    structure = (
		('ppTComp', ITYPECOMP),
    )
        

class GetDocumentation(NDRCALL):
    opnum = 6
    structure = (
		('index', INT),
		('refPtrFlags', DWORD),
    )

class GetDocumentationResponse(NDRCALL):
    structure = (
		('pBstrName', BSTR),
		('pBstrDocString', BSTR),
		('pdwHelpContext', DWORD),
		('pBstrHelpFile', BSTR),
    )
        

class IsName(NDRCALL):
    opnum = 7
    structure = (
		('szNameBuf', LPOLESTR),
		('lHashVal', ULONG),
    )

class IsNameResponse(NDRCALL):
    structure = (
		('pfName', BOOL),
		('pBstrNameInLibrary', BSTR),
    )
        

class FindName(NDRCALL):
    opnum = 8
    structure = (
		('szNameBuf', LPOLESTR),
		('lHashVal', ULONG),
		('pcFound', USHORT),
    )

class FindNameResponse(NDRCALL):
    structure = (
		('ppTInfo', ITYPEINFO),
		('rgMemId', MEMBERID),
		('pcFound', USHORT),
		('pBstrNameInLibrary', BSTR),
    )
        

class Opnum12NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum12NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (GetTypeInfoCount,GetTypeInfoCountResponse),
1 : (GetTypeInfo,GetTypeInfoResponse),
2 : (GetTypeInfoType,GetTypeInfoTypeResponse),
3 : (GetTypeInfoOfGuid,GetTypeInfoOfGuidResponse),
4 : (GetLibAttr,GetLibAttrResponse),
5 : (GetTypeComp,GetTypeCompResponse),
6 : (GetDocumentation,GetDocumentationResponse),
7 : (IsName,IsNameResponse),
8 : (FindName,FindNameResponse),
9 : (Opnum12NotUsedOnWire,Opnum12NotUsedOnWireResponse),
}

#################################################################################

#ITypeLib2 Definition

#################################################################################

MSRPC_UUID_ITYPELIB2 = uuidtup_to_bin(('00020411-0000-0000-C000-000000000046','0.0'))


class GetCustData(NDRCALL):
    opnum = 0
    structure = (
		('guid', REFGUID),
    )

class GetCustDataResponse(NDRCALL):
    structure = (
		('pVarVal', VARIANT),
    )
        

class GetLibStatistics(NDRCALL):
    opnum = 1
    structure = (

    )

class GetLibStatisticsResponse(NDRCALL):
    structure = (
		('pcUniqueNames', ULONG),
		('pcchUniqueNames', ULONG),
    )
        

class GetDocumentation2(NDRCALL):
    opnum = 2
    structure = (
		('index', INT),
		('lcid', LCID),
		('refPtrFlags', DWORD),
    )

class GetDocumentation2Response(NDRCALL):
    structure = (
		('pbstrHelpString', BSTR),
		('pdwHelpStringContext', DWORD),
		('pbstrHelpStringDll', BSTR),
    )
        

class GetAllCustData(NDRCALL):
    opnum = 3
    structure = (

    )

class GetAllCustDataResponse(NDRCALL):
    structure = (
		('pCustData', CUSTDATA),
    )
        
OPNUMS = {
0 : (GetCustData,GetCustDataResponse),
1 : (GetLibStatistics,GetLibStatisticsResponse),
2 : (GetDocumentation2,GetDocumentation2Response),
3 : (GetAllCustData,GetAllCustDataResponse),
}

#################################################################################

#TYPEDEFS

#################################################################################


ROUTER_IF_TYPE_CLIENT = ,
ROUTER_IF_TYPE_HOME_ROUTER = ,
ROUTER_IF_TYPE_FULL_ROUTER = ,
ROUTER_IF_TYPE_DEDICATED = ,
ROUTER_IF_TYPE_INTERNAL = ,
ROUTER_IF_TYPE_LOOPBACK = ,
ROUTER_IF_TYPE_TUNNEL1 = 
        

ROUTER_IF_STATE_UNREACHABLE = ,
ROUTER_IF_STATE_DISCONNECTED = ,
ROUTER_IF_STATE_CONNECTING = 
        

RAS_QUAR_STATE_NORMAL = ,
RAS_QUAR_STATE_QUARANTINE = ,
RAS_QUAR_STATE_PROBATION = 
        

RAS_PORT_NON_OPERATIONAL = ,
RAS_PORT_DISCONNECTED = ,
RAS_PORT_CALLING_BACK = ,
RAS_PORT_LISTENING = ,
RAS_PORT_AUTHENTICATING = ,
RAS_PORT_AUTHENTICATED = 
        

RAS_HARDWARE_OPERATIONAL = 
        
DIM_HANDLE = HANDLE_T

FORWARD = 0,
DROP = 1
        

MIB_IPROUTE_TYPE_OTHER = 1,
MIB_IPROUTE_TYPE_INVALID = 2,
MIB_IPROUTE_TYPE_DIRECT = 3,
MIB_IPROUTE_TYPE_INDIRECT = 4
        

MIB_IPPROTO_OTHER = 1,
MIB_IPPROTO_LOCAL = 2,
MIB_IPPROTO_NETMGMT = 3,
MIB_IPPROTO_ICMP = 4,
MIB_IPPROTO_EGP = 5,
MIB_IPPROTO_GGP = 6,
MIB_IPPROTO_HELLO = 7,
MIB_IPPROTO_RIP = 8,
MIB_IPPROTO_IS_IS = 9,
MIB_IPPROTO_ES_IS = 10,
MIB_IPPROTO_CISCO = 11,
MIB_IPPROTO_BBN = 12,
MIB_IPPROTO_OSPF = 13,
MIB_IPPROTO_BGP = 14,
MIB_IPPROTO_NT_AUTOSTATIC = 10002,
MIB_IPPROTO_NT_STATIC = 10006,
MIB_IPPROTO_NT_STATIC_NON_DOD = 10007
        

MIB_IP_FORWARDING = 1,
MIB_IP_NOT_FORWARDING = 2
        

MIB_TCP_STATE_CLOSED = 1,
MIB_TCP_STATE_LISTEN = 2,
MIB_TCP_STATE_SYN_SENT = 3,
MIB_TCP_STATE_SYN_RCVD = 4,
MIB_TCP_STATE_ESTAB = 5,
MIB_TCP_STATE_FIN_WAIT1 = 6,
MIB_TCP_STATE_FIN_WAIT2 = 7,
MIB_TCP_STATE_CLOSE_WAIT = 8,
MIB_TCP_STATE_CLOSING = 9,
MIB_TCP_STATE_LAST_ACK = 10,
MIB_TCP_STATE_TIME_WAIT = 11,
MIB_TCP_STATE_DELETE_TCB = 12
        

MIB_TCP_RTO_OTHER = 1,
MIB_TCP_RTO_CONSTANT = 2,
MIB_TCP_RTO_RSRE = 3,
MIB_TCP_RTO_VANJ = 4
        

class U(NDRUNION):
    union = {
        1: ('Byte',UCHAR),2: ('Word',USHORT),
    }
        

class IN6_ADDR(NDRSTRUCT):
    structure = (
        ('u', U),
    )
class PIN6_ADDR(NDRPOINTER):
    referent = (
        ('Data', IN6_ADDR),
    )    
class LPIN6_ADDR(NDRPOINTER):
    referent = (
        ('Data', IN6_ADDR),
    )    


class DIM_INFORMATION_CONTAINER(NDRSTRUCT):
    structure = (
        ('dwBufferSize', DWORD),('pBuffer', LPBYTE),
    )
class PDIM_INFORMATION_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DIM_INFORMATION_CONTAINER),
    )    


class MPRAPI_OBJECT_HEADER_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('type', UCHAR),('size', USHORT),
    )
class PMPRAPI_OBJECT_HEADER_IDL(NDRPOINTER):
    referent = (
        ('Data', MPRAPI_OBJECT_HEADER_IDL),
    )    


class PPP_PROJECTION_INFO_1(NDRSTRUCT):
    structure = (
        ('dwIPv4NegotiationError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),('dwIPv4Options', DWORD),('dwIPv4RemoteOptions', DWORD),('IPv4SubInterfaceIndex', ULONG64),('dwIPv6NegotiationError', DWORD),('bInterfaceIdentifier', UCHAR),('bRemoteInterfaceIdentifier', UCHAR),('bPrefix', UCHAR),('dwPrefixLength', DWORD),('IPv6SubInterfaceIndex', ULONG64),('dwLcpError', DWORD),('dwAuthenticationProtocol', DWORD),('dwAuthenticationData', DWORD),('dwRemoteAuthenticationProtocol', DWORD),('dwRemoteAuthenticationData', DWORD),('dwLcpTerminateReason', DWORD),('dwLcpRemoteTerminateReason', DWORD),('dwLcpOptions', DWORD),('dwLcpRemoteOptions', DWORD),('dwEapTypeId', DWORD),('dwRemoteEapTypeId', DWORD),('dwCcpError', DWORD),('dwCompressionAlgorithm', DWORD),('dwCcpOptions', DWORD),('dwRemoteCompressionAlgorithm', DWORD),('dwCcpRemoteOptions', DWORD),
    )
class PPPP_PROJECTION_INFO_1(NDRPOINTER):
    referent = (
        ('Data', PPP_PROJECTION_INFO_1),
    )    


class PPP_PROJECTION_INFO_2(NDRSTRUCT):
    structure = (
        ('dwIPv4NegotiationError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),('dwIPv4Options', DWORD),('dwIPv4RemoteOptions', DWORD),('IPv4SubInterfaceIndex', ULONG64),('dwIPv6NegotiationError', DWORD),('bInterfaceIdentifier', UCHAR),('bRemoteInterfaceIdentifier', UCHAR),('bPrefix', UCHAR),('dwPrefixLength', DWORD),('IPv6SubInterfaceIndex', ULONG64),('dwLcpError', DWORD),('dwAuthenticationProtocol', DWORD),('dwAuthenticationData', DWORD),('dwRemoteAuthenticationProtocol', DWORD),('dwRemoteAuthenticationData', DWORD),('dwLcpTerminateReason', DWORD),('dwLcpRemoteTerminateReason', DWORD),('dwLcpOptions', DWORD),('dwLcpRemoteOptions', DWORD),('dwEapTypeId', DWORD),('dwEmbeddedEAPTypeId', DWORD),('dwRemoteEapTypeId', DWORD),('dwCcpError', DWORD),('dwCompressionAlgorithm', DWORD),('dwCcpOptions', DWORD),('dwRemoteCompressionAlgorithm', DWORD),('dwCcpRemoteOptions', DWORD),
    )
class PPPP_PROJECTION_INFO_2(NDRPOINTER):
    referent = (
        ('Data', PPP_PROJECTION_INFO_2),
    )    


class IKEV2_PROJECTION_INFO_1(NDRSTRUCT):
    structure = (
        ('dwIPv4NegotiationError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),('IPv4SubInterfaceIndex', ULONG64),('dwIPv6NegotiationError', DWORD),('bInterfaceIdentifier', UCHAR),('bRemoteInterfaceIdentifier', UCHAR),('bPrefix', UCHAR),('dwPrefixLength', DWORD),('IPv6SubInterfaceIndex', ULONG64),('dwOptions', DWORD),('dwAuthenticationProtocol', DWORD),('dwEapTypeId', DWORD),('dwCompressionAlgorithm', DWORD),('dwEncryptionMethod', DWORD),
    )
class PIKEV2_PROJECTION_INFO_1(NDRPOINTER):
    referent = (
        ('Data', IKEV2_PROJECTION_INFO_1),
    )    


class IKEV2_PROJECTION_INFO_2(NDRSTRUCT):
    structure = (
        ('dwIPv4NegotiationError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),('IPv4SubInterfaceIndex', ULONG64),('dwIPv6NegotiationError', DWORD),('bInterfaceIdentifier', UCHAR),('bRemoteInterfaceIdentifier', UCHAR),('bPrefix', UCHAR),('dwPrefixLength', DWORD),('IPv6SubInterfaceIndex', ULONG64),('dwOptions', DWORD),('dwAuthenticationProtocol', DWORD),('dwEapTypeId', DWORD),('dwEmbeddedEAPTypeId', DWORD),('dwCompressionAlgorithm', DWORD),('dwEncryptionMethod', DWORD),
    )
class PIKEV2_PROJECTION_INFO_2(NDRPOINTER):
    referent = (
        ('Data', IKEV2_PROJECTION_INFO_2),
    )    


class ANONYMOUS22(NDRUNION):
    union = {
        1: ('PppProjectionInfo',PPP_PROJECTION_INFO_1),2: ('Ikev2ProjectionInfo',IKEV2_PROJECTION_INFO_1),
    }
        

class PROJECTION_INFO_IDL_1(NDRSTRUCT):
    structure = (
        ('projectionInfoType', UCHAR),('Anonymous22', ANONYMOUS22),
    )


class PPROJECTION_INFO_IDL_1(NDRSTRUCT):
    structure = (
        
    )


class ANONYMOUS23(NDRUNION):
    union = {
        1: ('PppProjectionInfo',PPP_PROJECTION_INFO_2),2: ('Ikev2ProjectionInfo',IKEV2_PROJECTION_INFO_2),
    }
        

class PROJECTION_INFO_IDL_2(NDRSTRUCT):
    structure = (
        ('projectionInfoType', UCHAR),('Anonymous23', ANONYMOUS23),
    )
class PPROJECTION_INFO_IDL_2(NDRPOINTER):
    referent = (
        ('Data', PROJECTION_INFO_IDL_2),
    )    


class RAS_CONNECTION_EX_1_IDL(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('dwConnectDuration', DWORD),('dwInterfaceType', ROUTER_INTERFACE_TYPE),('dwConnectionFlags', DWORD),('wszInterfaceName', WCHAR),('wszUserName', WCHAR),('wszLogonDomain', WCHAR),('wszRemoteComputer', WCHAR),('guid', GUID),('rasQuarState', RAS_QUARANTINE_STATE),('probationTime', FILETIME),('dwBytesXmited', DWORD),('dwBytesRcved', DWORD),('dwFramesXmited', DWORD),('dwFramesRcved', DWORD),('dwCrcErr', DWORD),('dwTimeoutErr', DWORD),('dwAlignmentErr', DWORD),('dwHardwareOverrunErr', DWORD),('dwFramingErr', DWORD),('dwBufferOverrunErr', DWORD),('dwCompressionRatioIn', DWORD),('dwCompressionRatioOut', DWORD),('dwNumSwitchOvers', DWORD),('wszRemoteEndpointAddress', WCHAR),('wszLocalEndpointAddress', WCHAR),('ProjectionInfo', PROJECTION_INFO_IDL_1),('hConnection', ULONG),('hInterface', ULONG),
    )
class PRAS_CONNECTION_EX_1_IDL(NDRPOINTER):
    referent = (
        ('Data', RAS_CONNECTION_EX_1_IDL),
    )    


class ANONYMOUS24(NDRUNION):
    union = {
        1: ('RasConnection1',RAS_CONNECTION_EX_1_IDL),
    }
        

class RAS_CONNECTION_EX_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('Anonymous24', ANONYMOUS24),
    )


class PRAS_CONNECTION_EX_IDL(NDRSTRUCT):
    structure = (
        
    )


class RAS_CONNECTION_4_IDL(NDRSTRUCT):
    structure = (
        ('dwConnectDuration', DWORD),('dwInterfaceType', ROUTER_INTERFACE_TYPE),('dwConnectionFlags', DWORD),('wszInterfaceName', WCHAR),('wszUserName', WCHAR),('wszLogonDomain', WCHAR),('wszRemoteComputer', WCHAR),('guid', GUID),('rasQuarState', RAS_QUARANTINE_STATE),('probationTime', FILETIME),('connectionStartTime', FILETIME),('dwBytesXmited', DWORD),('dwBytesRcved', DWORD),('dwFramesXmited', DWORD),('dwFramesRcved', DWORD),('dwCrcErr', DWORD),('dwTimeoutErr', DWORD),('dwAlignmentErr', DWORD),('dwHardwareOverrunErr', DWORD),('dwFramingErr', DWORD),('dwBufferOverrunErr', DWORD),('dwCompressionRatioIn', DWORD),('dwCompressionRatioOut', DWORD),('dwNumSwitchOvers', DWORD),('wszRemoteEndpointAddress', WCHAR),('wszLocalEndpointAddress', WCHAR),('ProjectionInfo', PROJECTION_INFO_IDL_2),('hConnection', ULONG),('hInterface', ULONG),('dwDeviceType', DWORD),
    )
class PRAS_CONNECTION_4_IDL(NDRPOINTER):
    referent = (
        ('Data', RAS_CONNECTION_4_IDL),
    )    


class DATA_CERT_BLOB_1(NDRUniConformantArray):
    item = BYTE

class PTR_CERT_BLOB_1(NDRPOINTER):
    referent = (
        ('Data', DATA_CERT_BLOB_1),
    )

class CERT_BLOB_1(NDRSTRUCT):
    structure = (
	('cbData', DWORD),	('pbData', PTR_CERT_BLOB_1),

    )
        

class DATA_CERT_EKU_1(NDRUniConformantArray):
    item = WCHAR

class PTR_CERT_EKU_1(NDRPOINTER):
    referent = (
        ('Data', DATA_CERT_EKU_1),
    )

class CERT_EKU_1(NDRSTRUCT):
    structure = (
	('dwSize', DWORD),	('IsEKUOID', BOOL),	('pwszEKU', PTR_CERT_EKU_1),

    )
        

class DATA_IKEV2_TUNNEL_CONFIG_PARAMS_1(NDRUniConformantArray):
    item = CERT_BLOB_1

class PTR_IKEV2_TUNNEL_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', DATA_IKEV2_TUNNEL_CONFIG_PARAMS_1),
    )

class IKEV2_TUNNEL_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
	('dwIdleTimeout', DWORD),	('dwNetworkBlackoutTime', DWORD),	('dwSaLifeTime', DWORD),	('dwSaDataSizeForRenegotiation', DWORD),	('dwConfigOptions', DWORD),	('dwTotalCertificates', DWORD),	('certificateNames', PTR_IKEV2_TUNNEL_CONFIG_PARAMS_1),

    )
        

class ROUTER_CUSTOM_IKEV2_POLICY_0(NDRSTRUCT):
    structure = (
        ('dwIntegrityMethod', DWORD),('dwEncryptionMethod', DWORD),('dwCipherTransformConstant', DWORD),('dwAuthTransformConstant', DWORD),('dwPfsGroup', DWORD),('dwDhGroup', DWORD),
    )
class PROUTER_CUSTOM_IKEV2_POLICY_0(NDRPOINTER):
    referent = (
        ('Data', ROUTER_CUSTOM_IKEV2_POLICY_0),
    )    
ROUTER_CUSTOM_L2TP_POLICY_0 = ROUTER_CUSTOM_IKEV2_POLICY_0
class PROUTER_CUSTOM_L2TP_POLICY_0(NDRPOINTER):
    referent = (
        ('Data', ROUTER_CUSTOM_IKEV2_POLICY_0),
    )    


class ROUTER_IKEV2_IF_CUSTOM_CONFIG_0(NDRSTRUCT):
    structure = (
        ('dwSaLifeTime', DWORD),('dwSaDataSize', DWORD),('certificateName', CERT_BLOB_1),('customPolicy', PROUTER_CUSTOM_IKEV2_POLICY_0),
    )
class PROUTER_IKEV2_IF_CUSTOM_CONFIG_0(NDRPOINTER):
    referent = (
        ('Data', ROUTER_IKEV2_IF_CUSTOM_CONFIG_0),
    )    


class ROUTER_IKEV2_IF_CUSTOM_CONFIG_1(NDRSTRUCT):
    structure = (
        ('dwSaLifeTime', DWORD),('dwSaDataSize', DWORD),('certificateName', CERT_BLOB_1),('customPolicy', PROUTER_CUSTOM_IKEV2_POLICY_0),('certificateHash', CERT_BLOB_1),
    )
class PROUTER_IKEV2_IF_CUSTOM_CONFIG_1(NDRPOINTER):
    referent = (
        ('Data', ROUTER_IKEV2_IF_CUSTOM_CONFIG_1),
    )    


class MPR_IF_CUSTOMINFOEX_0(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('dwFlags', DWORD),('customIkev2Config', ROUTER_IKEV2_IF_CUSTOM_CONFIG_0),
    )
class PMPR_IF_CUSTOMINFOEX_0(NDRPOINTER):
    referent = (
        ('Data', MPR_IF_CUSTOMINFOEX_0),
    )    


class MPR_IF_CUSTOMINFOEX_1(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('dwFlags', DWORD),('customIkev2Config', ROUTER_IKEV2_IF_CUSTOM_CONFIG_1),
    )
class PMPR_IF_CUSTOMINFOEX_1(NDRPOINTER):
    referent = (
        ('Data', MPR_IF_CUSTOMINFOEX_1),
    )    


class ANONYMOUS25(NDRUNION):
    union = {
        1: ('IfConfigObj1',MPR_IF_CUSTOMINFOEX_0),2: ('IfConfigObj2',MPR_IF_CUSTOMINFOEX_1),
    }
        

class MPR_IF_CUSTOMINFOEX_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('Anonymous25', ANONYMOUS25),
    )
class PMPR_IF_CUSTOMINFOEX_IDL(NDRPOINTER):
    referent = (
        ('Data', MPR_IF_CUSTOMINFOEX_IDL),
    )    


class DATA_IKEV2_TUNNEL_CONFIG_PARAMS_2(NDRUniConformantArray):
    item = CERT_BLOB_1

class PTR_IKEV2_TUNNEL_CONFIG_PARAMS_2(NDRPOINTER):
    referent = (
        ('Data', DATA_IKEV2_TUNNEL_CONFIG_PARAMS_2),
    )

class IKEV2_TUNNEL_CONFIG_PARAMS_2(NDRSTRUCT):
    structure = (
	('dwIdleTimeout', DWORD),	('dwNetworkBlackoutTime', DWORD),	('dwSaLifeTime', DWORD),	('dwSaDataSizeForRenegotiation', DWORD),	('dwConfigOptions', DWORD),	('dwTotalCertificates', DWORD),	('certificateNames', PTR_IKEV2_TUNNEL_CONFIG_PARAMS_2),
	('machineCertificateName', CERT_BLOB_1),	('dwEncryptionType', DWORD),	('customPolicy', ROUTER_CUSTOM_IKEV2_POLICY_0),
    )
        

class DATA_IKEV2_TUNNEL_CONFIG_PARAMS_3(NDRUniConformantArray):
    item = CERT_EKU_1

class PTR_IKEV2_TUNNEL_CONFIG_PARAMS_3(NDRPOINTER):
    referent = (
        ('Data', DATA_IKEV2_TUNNEL_CONFIG_PARAMS_3),
    )

class IKEV2_TUNNEL_CONFIG_PARAMS_3(NDRSTRUCT):
    structure = (
	('dwIdleTimeout', DWORD),	('dwNetworkBlackoutTime', DWORD),	('dwSaLifeTime', DWORD),	('dwSaDataSizeForRenegotiation', DWORD),	('dwConfigOptions', DWORD),	('dwTotalCertificates', DWORD),	('certificateNames', CERT_BLOB_1),	('machineCertificateName', CERT_BLOB_1),	('dwEncryptionType', DWORD),	('customPolicy', ROUTER_CUSTOM_IKEV2_POLICY_0),	('dwTotalEkus', DWORD),	('certificateEKUs', PTR_IKEV2_TUNNEL_CONFIG_PARAMS_3),
	('machineCertificateHash', CERT_BLOB_1),
    )
        

class L2TP_TUNNEL_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('dwIdleTimeout', DWORD),('dwEncryptionType', DWORD),('dwSaLifeTime', DWORD),('dwSaDataSizeForRenegotiation', DWORD),('customPolicy', PROUTER_CUSTOM_L2TP_POLICY_0),
    )
class PL2TP_TUNNEL_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', L2TP_TUNNEL_CONFIG_PARAMS_1),
    )    


class IKEV2_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),('dwTunnelConfigParamFlags', DWORD),('TunnelConfigParams', IKEV2_TUNNEL_CONFIG_PARAMS_1),
    )
class PIKEV2_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', IKEV2_CONFIG_PARAMS_1),
    )    


class IKEV2_CONFIG_PARAMS_2(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),('dwTunnelConfigParamFlags', DWORD),('TunnelConfigParams', IKEV2_TUNNEL_CONFIG_PARAMS_2),
    )
class PIKEV2_CONFIG_PARAMS_2(NDRPOINTER):
    referent = (
        ('Data', IKEV2_CONFIG_PARAMS_2),
    )    


class IKEV2_CONFIG_PARAMS_3(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),('dwTunnelConfigParamFlags', DWORD),('TunnelConfigParams', IKEV2_TUNNEL_CONFIG_PARAMS_3),
    )
class PIKEV2_CONFIG_PARAMS_3(NDRPOINTER):
    referent = (
        ('Data', IKEV2_CONFIG_PARAMS_3),
    )    


class PPTP_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),
    )
class PPPTP_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', PPTP_CONFIG_PARAMS_1),
    )    


class L2TP_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),
    )
class PL2TP_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', L2TP_CONFIG_PARAMS_1),
    )    


class L2TP_CONFIG_PARAMS_2(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),('dwTunnelConfigParamFlags', DWORD),('TunnelConfigParams', L2TP_TUNNEL_CONFIG_PARAMS_1),
    )
class PL2TP_CONFIG_PARAMS_2(NDRPOINTER):
    referent = (
        ('Data', L2TP_CONFIG_PARAMS_2),
    )    


class SSTP_CERT_INFO_1(NDRSTRUCT):
    structure = (
        ('isDefault', BOOL),('certBlob', CERT_BLOB_1),
    )
class PSSTP_CERT_INFO_1(NDRPOINTER):
    referent = (
        ('Data', SSTP_CERT_INFO_1),
    )    


class SSTP_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('dwNumPorts', DWORD),('dwPortFlags', DWORD),('isUseHttps', BOOL),('certAlgorithm', DWORD),('sstpCertDetails', SSTP_CERT_INFO_1),
    )
class PSSTP_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', SSTP_CONFIG_PARAMS_1),
    )    


class MPRAPI_TUNNEL_CONFIG_PARAMS_1(NDRSTRUCT):
    structure = (
        ('IkeConfigParams', IKEV2_CONFIG_PARAMS_1),('PptpConfigParams', PPTP_CONFIG_PARAMS_1),('L2tpConfigParams', L2TP_CONFIG_PARAMS_1),('SstpConfigParams', SSTP_CONFIG_PARAMS_1),
    )
class PMPRAPI_TUNNEL_CONFIG_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', MPRAPI_TUNNEL_CONFIG_PARAMS_1),
    )    


class MPRAPI_TUNNEL_CONFIG_PARAMS_2(NDRSTRUCT):
    structure = (
        ('IkeConfigParams', IKEV2_CONFIG_PARAMS_2),('PptpConfigParams', PPTP_CONFIG_PARAMS_1),('L2tpConfigParams', L2TP_CONFIG_PARAMS_1),('SstpConfigParams', SSTP_CONFIG_PARAMS_1),
    )
class PMPRAPI_TUNNEL_CONFIG_PARAMS_2(NDRPOINTER):
    referent = (
        ('Data', MPRAPI_TUNNEL_CONFIG_PARAMS_2),
    )    


class MPRAPI_TUNNEL_CONFIG_PARAMS_3(NDRSTRUCT):
    structure = (
        ('IkeConfigParams', IKEV2_CONFIG_PARAMS_3),('PptpConfigParams', PPTP_CONFIG_PARAMS_1),('L2tpConfigParams', L2TP_CONFIG_PARAMS_2),('SstpConfigParams', SSTP_CONFIG_PARAMS_1),
    )
class PMPRAPI_TUNNEL_CONFIG_PARAMS_3(NDRPOINTER):
    referent = (
        ('Data', MPRAPI_TUNNEL_CONFIG_PARAMS_3),
    )    


class MPR_SERVER_EX_1(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('fLanOnlyMode', BOOL),('dwUpTime', DWORD),('dwTotalPorts', DWORD),('dwPortsInUse', DWORD),('Reserved', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_1),
    )
class PMPR_SERVER_EX_1(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_EX_1),
    )    


class MPR_SERVER_EX_2(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('fLanOnlyMode', BOOL),('dwUpTime', DWORD),('dwTotalPorts', DWORD),('dwPortsInUse', DWORD),('Reserved', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_2),
    )
class PMPR_SERVER_EX_2(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_EX_2),
    )    


class MPR_SERVER_EX_3(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('fLanOnlyMode', BOOL),('dwUpTime', DWORD),('dwTotalPorts', DWORD),('dwPortsInUse', DWORD),('Reserved', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_3),
    )
class PMPR_SERVER_EX_3(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_EX_3),
    )    


class ANONYMOUS26(NDRUNION):
    union = {
        1: ('ServerConfig1',MPR_SERVER_EX_1),2: ('ServerConfig2',MPR_SERVER_EX_2),3: ('ServerConfig3',MPR_SERVER_EX_3),
    }
        

class MPR_SERVER_EX_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('Anonymous26', ANONYMOUS26),
    )


class PMPR_SERVER_EX_IDL(NDRSTRUCT):
    structure = (
        
    )


class MPR_SERVER_SET_CONFIG_EX_1(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('setConfigForProtocols', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_1),
    )
class PMPR_SERVER_SET_CONFIG_EX_1(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_SET_CONFIG_EX_1),
    )    


class MPR_SERVER_SET_CONFIG_EX_2(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('setConfigForProtocols', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_2),
    )
class PMPR_SERVER_SET_CONFIG_EX_2(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_SET_CONFIG_EX_2),
    )    


class MPR_SERVER_SET_CONFIG_EX_3(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('setConfigForProtocols', DWORD),('ConfigParams', MPRAPI_TUNNEL_CONFIG_PARAMS_3),
    )
class PMPR_SERVER_SET_CONFIG_EX_3(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_SET_CONFIG_EX_3),
    )    


class ANONYMOUS27(NDRUNION):
    union = {
        1: ('ServerSetConfig1',MPR_SERVER_SET_CONFIG_EX_1),2: ('ServerSetConfig2',MPR_SERVER_SET_CONFIG_EX_2),3: ('ServerSetConfig3',MPR_SERVER_SET_CONFIG_EX_3),
    }
        

class MPR_SERVER_SET_CONFIG_EX_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('Anonymous27', ANONYMOUS27),
    )


class PMPR_SERVER_SET_CONFIG_EX_IDL(NDRSTRUCT):
    structure = (
        
    )


class RAS_UPDATE_CONNECTION_1_IDL(NDRSTRUCT):
    structure = (
        ('Header', MPRAPI_OBJECT_HEADER_IDL),('dwIfIndex', DWORD),('wszRemoteEndpointAddress', WCHAR),
    )


class PRAS_UPDATE_CONNECTION_1_IDL(NDRSTRUCT):
    structure = (
        
    )


class ANONYMOUS28(NDRUNION):
    union = {
        1: ('UpdateConnection1',RAS_UPDATE_CONNECTION_1_IDL),
    }
        

class RAS_UPDATE_CONNECTION_IDL(NDRSTRUCT):
    structure = (
        ('revision', UCHAR),('Anonymous28', ANONYMOUS28),
    )


class PRAS_UPDATE_CONNECTION_IDL(NDRSTRUCT):
    structure = (
        
    )


class DIM_INTERFACE_CONTAINER(NDRSTRUCT):
    structure = (
        ('fGetInterfaceInfo', DWORD),('dwInterfaceInfoSize', DWORD),('pInterfaceInfo', LPBYTE),('fGetGlobalInfo', DWORD),('dwGlobalInfoSize', DWORD),('pGlobalInfo', LPBYTE),
    )
class PDIM_INTERFACE_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DIM_INTERFACE_CONTAINER),
    )    


class RTR_TOC_ENTRY(NDRSTRUCT):
    structure = (
        ('InfoType', ULONG),('InfoSize', ULONG),('Count', ULONG),('Offset', ULONG),
    )
class PRTR_TOC_ENTRY(NDRPOINTER):
    referent = (
        ('Data', RTR_TOC_ENTRY),
    )    


class RTR_INFO_BLOCK_HEADER(NDRSTRUCT):
    structure = (
        ('Version', ULONG),('Size', ULONG),('TocEntriesCount', ULONG),('TocEntry', RTR_TOC_ENTRY),
    )
class PRTR_INFO_BLOCK_HEADER(NDRPOINTER):
    referent = (
        ('Data', RTR_INFO_BLOCK_HEADER),
    )    


class FILTER_INFO(NDRSTRUCT):
    structure = (
        ('dwSrcAddr', DWORD),('dwSrcMask', DWORD),('dwDstAddr', DWORD),('dwDstMask', DWORD),('dwProtocol', DWORD),('fLateBound', DWORD),('wSrcPort', WORD),('wDstPort', WORD),
    )
class PFILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', FILTER_INFO),
    )    


class FILTER_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwNumFilters', DWORD),('faDefaultAction', FORWARD_ACTION),('fiFilter', FILTER_INFO),
    )
class PFILTER_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', FILTER_DESCRIPTOR),
    )    


class FILTER_INFO_V6(NDRSTRUCT):
    structure = (
        ('ipv6SrcAddr', BYTE),('dwSrcPrefixLength', DWORD),('ipv6DstAddr', BYTE),('dwDstPrefixLength', DWORD),('dwProtocol', DWORD),('fLateBound', DWORD),('wSrcPort', WORD),('wDstPort', WORD),
    )
class PFILTER_INFO_V6(NDRPOINTER):
    referent = (
        ('Data', FILTER_INFO_V6),
    )    


class FILTER_DESCRIPTOR_V6(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwNumFilters', DWORD),('faDefaultAction', FORWARD_ACTION),('fiFilter', FILTER_INFO_V6),
    )
class PFILTER_DESCRIPTOR_V6(NDRPOINTER):
    referent = (
        ('Data', FILTER_DESCRIPTOR_V6),
    )    


class GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('bFilteringOn', IN OUT BOOL),('dwLoggingLevel', IN OUT DWORD),
    )
class PGLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', GLOBAL_INFO),
    )    


class S0(NDRSTRUCT):
    structure = (
        ('dwRtInfoDest', DWORD),('dwRtInfoMask', DWORD),('dwRtInfoPolicy', DWORD),('dwRtInfoNextHop', DWORD),('dwRtInfoAge', DWORD),('dwRtInfoNextHopAS', DWORD),('dwRtInfoMetric1', DWORD),('dwRtInfoMetric2', DWORD),('dwRtInfoMetric3', DWORD),
    )


class S1(NDRSTRUCT):
    structure = (
        ('DestinationPrefix', IN6_ADDR),('DestPrefixLength', DWORD),('NextHopAddress', IN6_ADDR),('ValidLifeTime', ULONG),('Flags', DWORD),('Metric', ULONG),
    )


class U0(NDRUNION):
    union = {
        1: ('s0',S0),2: ('s1',S1),
    }
        

class INTERFACE_ROUTE_INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),('dwRtInfoIfIndex', DWORD),('dwRtInfoType', DWORD),('dwRtInfoProto', DWORD),('dwRtInfoPreference', DWORD),('dwRtInfoViewSet', DWORD),('bV4', BOOL),
    )
class PINTERFACE_ROUTE_INFO(NDRPOINTER):
    referent = (
        ('Data', INTERFACE_ROUTE_INFO),
    )    


class PROTOCOL_METRIC(NDRSTRUCT):
    structure = (
        ('dwProtocolId', IN OUT DWORD),('dwMetric', IN OUT DWORD),
    )
class PPROTOCOL_METRIC(NDRPOINTER):
    referent = (
        ('Data', PROTOCOL_METRIC),
    )    


class PRIORITY_INFO(NDRSTRUCT):
    structure = (
        ('dwNumProtocols', IN OUT DWORD),('ppmProtocolMetric', IN OUT PROTOCOL_METRIC),
    )
class PPRIORITY_INFO(NDRPOINTER):
    referent = (
        ('Data', PRIORITY_INFO),
    )    


class PROTOCOL_METRIC_EX(NDRSTRUCT):
    structure = (
        ('dwProtocolId', IN OUT DWORD),('dwSubProtocolId', IN OUT DWORD),('dwMetric', IN OUT DWORD),
    )
class PPROTOCOL_METRIC_EX(NDRPOINTER):
    referent = (
        ('Data', PROTOCOL_METRIC_EX),
    )    


class PRIORITY_INFO_EX(NDRSTRUCT):
    structure = (
        ('dwNumProtocols', IN OUT DWORD),('ppmProtocolMetric', IN OUT PROTOCOL_METRIC_EX),
    )
class PPRIORITY_INFO_EX(NDRPOINTER):
    referent = (
        ('Data', PRIORITY_INFO_EX),
    )    


class RTR_DISC_INFO(NDRSTRUCT):
    structure = (
        ('wMaxAdvtInterval', IN OUT WORD),('wMinAdvtInterval', IN OUT WORD),('wAdvtLifetime', IN OUT WORD),('bAdvertise', IN OUT BOOL),('lPrefLevel', IN OUT LONG),
    )
class PRTR_DISC_INFO(NDRPOINTER):
    referent = (
        ('Data', RTR_DISC_INFO),
    )    


class MCAST_HBEAT_INFO(NDRSTRUCT):
    structure = (
        ('pwszGroup', WCHAR),('bActive', BOOL),('ulDeadInterval', ULONG),('byProtocol', BYTE),('wPort', WORD),
    )
class PMCAST_HBEAT_INFO(NDRPOINTER):
    referent = (
        ('Data', MCAST_HBEAT_INFO),
    )    


class MIB_MCAST_LIMIT_ROW(NDRSTRUCT):
    structure = (
        ('dwTtl', DWORD),('dwRateLimit', DWORD),
    )
class PMIB_MCAST_LIMIT_ROW(NDRPOINTER):
    referent = (
        ('Data', MIB_MCAST_LIMIT_ROW),
    )    


class IPINIP_CONFIG_INFO(NDRSTRUCT):
    structure = (
        ('dwRemoteAddress', DWORD),('dwLocalAddress', DWORD),('byTtl', BYTE),
    )
class PIPINIP_CONFIG_INFO(NDRPOINTER):
    referent = (
        ('Data', IPINIP_CONFIG_INFO),
    )    


class INTERFACE_STATUS_INFO(NDRSTRUCT):
    structure = (
        ('dwAdminStatus', IN OUT DWORD),
    )
class PINTERFACE_STATUS_INFO(NDRPOINTER):
    referent = (
        ('Data', INTERFACE_STATUS_INFO),
    )    


class DIM_MIB_ENTRY_CONTAINER(NDRSTRUCT):
    structure = (
        ('dwMibInEntrySize', DWORD),('pMibInEntry', LPBYTE),('dwMibOutEntrySize', DWORD),('pMibOutEntry', LPBYTE),
    )
class PDIM_MIB_ENTRY_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DIM_MIB_ENTRY_CONTAINER),
    )    


class U0(NDRUNION):
    union = {
        1: ('dwForwardType',DWORD),2: ('ForwardType',MIB_IPFORWARD_TYPE),
    }
        

class U1(NDRUNION):
    union = {
        1: ('dwForwardProto',DWORD),2: ('ForwardProto',MIB_IPFORWARD_PROTO),
    }
        

class MIB_IPFORWARDROW(NDRSTRUCT):
    structure = (
        ('dwForwardDest', DWORD),('dwForwardMask', DWORD),('dwForwardPolicy', DWORD),('dwForwardNextHop', DWORD),('dwForwardIfIndex', DWORD),('u0', U0),('u1', U1),('dwForwardAge', DWORD),('dwForwardNextHopAS', DWORD),('dwForwardMetric1', DWORD),('dwForwardMetric2', DWORD),('dwForwardMetric3', DWORD),('dwForwardMetric4', DWORD),('dwForwardMetric5', DWORD),
    )
class PMIB_IPFORWARDROW(NDRPOINTER):
    referent = (
        ('Data', MIB_IPFORWARDROW),
    )    


class MIB_IPDESTROW(NDRSTRUCT):
    structure = (
        ('ForwardRow', MIB_IPFORWARDROW),('dwForwardPreference', DWORD),('dwForwardViewSet', DWORD),
    )
class PMIB_IPDESTROW(NDRPOINTER):
    referent = (
        ('Data', MIB_IPDESTROW),
    )    


class MIB_IPDESTTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPDESTROW),
    )
class PMIB_IPDESTTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPDESTTABLE),
    )    


class MIB_ROUTESTATE(NDRSTRUCT):
    structure = (
        ('bRoutesSetToStack', BOOL),
    )
class PMIB_ROUTESTATE(NDRPOINTER):
    referent = (
        ('Data', MIB_ROUTESTATE),
    )    


class MIB_BEST_IF(NDRSTRUCT):
    structure = (
        ('dwDestAddr', DWORD),('dwIfIndex', DWORD),
    )
class PMIB_BEST_IF(NDRPOINTER):
    referent = (
        ('Data', MIB_BEST_IF),
    )    


class MIB_BOUNDARYROW(NDRSTRUCT):
    structure = (
        ('dwGroupAddress', DWORD),('dwGroupMask', DWORD),
    )
class PMIB_BOUNDARYROW(NDRPOINTER):
    referent = (
        ('Data', MIB_BOUNDARYROW),
    )    


class MIBICMPSTATS(NDRSTRUCT):
    structure = (
        ('dwMsgs', DWORD),('dwErrors', DWORD),('dwDestUnreachs', DWORD),('dwTimeExcds', DWORD),('dwParmProbs', DWORD),('dwSrcQuenchs', DWORD),('dwRedirects', DWORD),('dwEchos', DWORD),('dwEchoReps', DWORD),('dwTimestamps', DWORD),('dwTimestampReps', DWORD),('dwAddrMasks', DWORD),('dwAddrMaskReps', DWORD),
    )


class MIBICMPINFO(NDRSTRUCT):
    structure = (
        ('icmpInStats', MIBICMPSTATS),('icmpOutStats', MIBICMPSTATS),
    )


class MIB_ICMP(NDRSTRUCT):
    structure = (
        ('stats', MIBICMPINFO),
    )
class PMIB_ICMP(NDRPOINTER):
    referent = (
        ('Data', MIB_ICMP),
    )    


class MIB_IFNUMBER(NDRSTRUCT):
    structure = (
        ('dwValue', DWORD),
    )
class PMIB_IFNUMBER(NDRPOINTER):
    referent = (
        ('Data', MIB_IFNUMBER),
    )    


class MIB_IFROW(NDRSTRUCT):
    structure = (
        ('wszName', WCHAR),('dwIndex', DWORD),('dwType', DWORD),('dwMtu', DWORD),('dwSpeed', DWORD),('dwPhysAddrLen', DWORD),('bPhysAddr', BYTE),('dwAdminStatus', DWORD),('dwOperStatus', DWORD),('dwLastChange', DWORD),('dwInOctets', DWORD),('dwInUcastPkts', DWORD),('dwInNUcastPkts', DWORD),('dwInDiscards', DWORD),('dwInErrors', DWORD),('dwInUnknownProtos', DWORD),('dwOutOctets', DWORD),('dwOutUcastPkts', DWORD),('dwOutNUcastPkts', DWORD),('dwOutDiscards', DWORD),('dwOutErrors', DWORD),('dwOutQLen', DWORD),('dwDescrLen', DWORD),('bDescr', BYTE),
    )


class MIB_IFSTATUS(NDRSTRUCT):
    structure = (
        ('dwIfIndex', DWORD),('dwAdminStatus', DWORD),('dwOperationalStatus', DWORD),('bMHbeatActive', BOOL),('bMHbeatAlive', BOOL),
    )
class PMIB_IFSTATUS(NDRPOINTER):
    referent = (
        ('Data', MIB_IFSTATUS),
    )    


class MIB_IFTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IFROW),
    )
class PMIB_IFTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IFTABLE),
    )    


class MIB_IPADDRROW(NDRSTRUCT):
    structure = (
        ('dwAddr', DWORD),('dwIndex', DWORD),('dwMask', DWORD),('dwBCastAddr', DWORD),('dwReasmSize', DWORD),('unused1', UNSIGNED_SHORT),('wType', UNSIGNED_SHORT),
    )
class PMIB_IPADDRROW(NDRPOINTER):
    referent = (
        ('Data', MIB_IPADDRROW),
    )    


class MIB_IPADDRTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPADDRROW),
    )
class PMIB_IPADDRTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPADDRTABLE),
    )    


class MIB_IPFORWARDNUMBER(NDRSTRUCT):
    structure = (
        ('dwValue', DWORD),
    )
class PMIB_IPFORWARDNUMBER(NDRPOINTER):
    referent = (
        ('Data', MIB_IPFORWARDNUMBER),
    )    


class MIB_IPFORWARDTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPFORWARDROW),('reserved', BYTE),
    )
class PMIB_IPFORWARDTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPFORWARDTABLE),
    )    


class MIB_IPMCAST_BOUNDARY(NDRSTRUCT):
    structure = (
        ('dwIfIndex', DWORD),('dwGroupAddress', DWORD),('dwGroupMask', DWORD),('dwStatus', DWORD),
    )
class PMIB_IPMCAST_BOUNDARY(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_BOUNDARY),
    )    


class MIB_IPMCAST_BOUNDARY_TABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPMCAST_BOUNDARY),
    )
class PMIB_IPMCAST_BOUNDARY_TABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_BOUNDARY_TABLE),
    )    


class MIB_IPMCAST_GLOBAL(NDRSTRUCT):
    structure = (
        ('dwEnable', DWORD),
    )
class PMIB_IPMCAST_GLOBAL(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_GLOBAL),
    )    


class MIB_IPMCAST_IF_ENTRY(NDRSTRUCT):
    structure = (
        ('dwIfIndex', DWORD),('dwTtl', DWORD),('dwProtocol', DWORD),('dwRateLimit', DWORD),('ulInMcastOctets', ULONG),('ulOutMcastOctets', ULONG),
    )
class PMIB_IPMCAST_IF_ENTRY(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_IF_ENTRY),
    )    


class MIB_IPMCAST_IF_TABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPMCAST_IF_ENTRY),
    )
class PMIB_IPMCAST_IF_TABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_IF_TABLE),
    )    


class MIB_IPMCAST_OIF(NDRSTRUCT):
    structure = (
        ('dwOutIfIndex', DWORD),('dwNextHopAddr', DWORD),('pvReserved', PVOID),('dwReserved', DWORD),
    )
class PMIB_IPMCAST_OIF(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_OIF),
    )    


class MIB_IPMCAST_MFE(NDRSTRUCT):
    structure = (
        ('dwGroup', DWORD),('dwSource', DWORD),('dwSrcMask', DWORD),('dwUpStrmNgbr', DWORD),('dwInIfIndex', DWORD),('dwInIfProtocol', DWORD),('dwRouteProtocol', DWORD),('dwRouteNetwork', DWORD),('dwRouteMask', DWORD),('ulUpTime', ULONG),('ulExpiryTime', ULONG),('ulTimeOut', ULONG),('ulNumOutIf', ULONG),('fFlags', DWORD),('dwReserved', DWORD),('rgmioOutInfo', MIB_IPMCAST_OIF),
    )
class PMIB_IPMCAST_MFE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_MFE),
    )    


class MIB_IPMCAST_OIF_STATS(NDRSTRUCT):
    structure = (
        ('dwOutIfIndex', DWORD),('dwNextHopAddr', DWORD),('pvDialContext', PVOID),('ulTtlTooLow', ULONG),('ulFragNeeded', ULONG),('ulOutPackets', ULONG),('ulOutDiscards', ULONG),
    )
class PMIB_IPMCAST_OIF_STATS(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_OIF_STATS),
    )    


class MIB_IPMCAST_MFE_STATS(NDRSTRUCT):
    structure = (
        ('dwGroup', DWORD),('dwSource', DWORD),('dwSrcMask', DWORD),('dwUpStrmNgbr', DWORD),('dwInIfIndex', DWORD),('dwInIfProtocol', DWORD),('dwRouteProtocol', DWORD),('dwRouteNetwork', DWORD),('dwRouteMask', DWORD),('ulUpTime', ULONG),('ulExpiryTime', ULONG),('ulNumOutIf', ULONG),('ulInPkts', ULONG),('ulInOctets', ULONG),('ulPktsDifferentIf', ULONG),('ulQueueOverflow', ULONG),('rgmiosOutStats', MIB_IPMCAST_OIF_STATS),
    )
class PMIB_IPMCAST_MFE_STATS(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_MFE_STATS),
    )    


class MIB_IPMCAST_SCOPE(NDRSTRUCT):
    structure = (
        ('dwGroupAddress', DWORD),('dwGroupMask', DWORD),('snNameBuffer', WCHAR),('dwStatus', DWORD),('reserved', BYTE),
    )
class PMIB_IPMCAST_SCOPE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPMCAST_SCOPE),
    )    


class MIB_IPNETROW(NDRSTRUCT):
    structure = (
        ('dwIndex', DWORD),('dwPhysAddrLen', DWORD),('bPhysAddr', BYTE),('dwAddr', DWORD),('dwType', DWORD),
    )
class PMIB_IPNETROW(NDRPOINTER):
    referent = (
        ('Data', MIB_IPNETROW),
    )    


class MIB_IPNETTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPNETROW),('reserved', BYTE),
    )
class PMIB_IPNETTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_IPNETTABLE),
    )    


class U0(NDRUNION):
    union = {
        1: ('dwForwarding',DWORD),2: ('Forwarding',MIB_IPSTATS_FORWARDING),
    }
        

class MIB_IPSTATS(NDRSTRUCT):
    structure = (
        ('u0', U0),('dwDefaultTTL', DWORD),('dwInReceives', DWORD),('dwInHdrErrors', DWORD),('dwInAddrErrors', DWORD),('dwForwDatagrams', DWORD),('dwInUnknownProtos', DWORD),('dwInDiscards', DWORD),('dwInDelivers', DWORD),('dwOutRequests', DWORD),('dwRoutingDiscards', DWORD),('dwOutDiscards', DWORD),('dwOutNoRoutes', DWORD),('dwReasmTimeout', DWORD),('dwReasmReqds', DWORD),('dwReasmOks', DWORD),('dwReasmFails', DWORD),('dwFragOks', DWORD),('dwFragFails', DWORD),('dwFragCreates', DWORD),('dwNumIf', DWORD),('dwNumAddr', DWORD),('dwNumRoutes', DWORD),
    )
class PMIB_IPSTATS(NDRPOINTER):
    referent = (
        ('Data', MIB_IPSTATS),
    )    


class MIB_MFE_STATS_TABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPMCAST_MFE_STATS),
    )
class PMIB_MFE_STATS_TABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_MFE_STATS_TABLE),
    )    


class MIB_MFE_TABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_IPMCAST_MFE),
    )
class PMIB_MFE_TABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_MFE_TABLE),
    )    


class U0(NDRUNION):
    union = {
        1: ('ullAlign',ULONGLONG),2: ('rgbyData',BYTE),
    }
        

class MIB_OPAQUE_INFO(NDRSTRUCT):
    structure = (
        ('dwId', DWORD),('u0', U0),
    )
class PMIB_OPAQUE_INFO(NDRPOINTER):
    referent = (
        ('Data', MIB_OPAQUE_INFO),
    )    


class MIB_OPAQUE_QUERY(NDRSTRUCT):
    structure = (
        ('dwVarId', DWORD),('rgdwVarIndex', DWORD),
    )
class PMIB_OPAQUE_QUERY(NDRPOINTER):
    referent = (
        ('Data', MIB_OPAQUE_QUERY),
    )    


class MIB_PROXYARP(NDRSTRUCT):
    structure = (
        ('dwAddress', DWORD),('dwMask', DWORD),('dwIfIndex', DWORD),
    )
class PMIB_PROXYARP(NDRPOINTER):
    referent = (
        ('Data', MIB_PROXYARP),
    )    


class U0(NDRUNION):
    union = {
        1: ('dwState',DWORD),2: ('State',MIB_TCP_STATE),
    }
        

class MIB_TCPROW(NDRSTRUCT):
    structure = (
        ('u0', U0),('dwLocalAddr', DWORD),('dwLocalPort', DWORD),('dwRemoteAddr', DWORD),('dwRemotePort', DWORD),
    )
class PMIB_TCPROW(NDRPOINTER):
    referent = (
        ('Data', MIB_TCPROW),
    )    


class U0(NDRUNION):
    union = {
        1: ('dwRtoAlgorithm',DWORD),2: ('RtoAlgorithm',TCP_RTO_ALGORITHM),
    }
        

class MIB_TCPSTATS(NDRSTRUCT):
    structure = (
        ('u0', U0),('dwRtoMin', DWORD),('dwRtoMax', DWORD),('dwMaxConn', DWORD),('dwActiveOpens', DWORD),('dwPassiveOpens', DWORD),('dwAttemptFails', DWORD),('dwEstabResets', DWORD),('dwCurrEstab', DWORD),('dwInSegs', DWORD),('dwOutSegs', DWORD),('dwRetransSegs', DWORD),('dwInErrs', DWORD),('dwOutRsts', DWORD),('dwNumConns', DWORD),
    )
class PMIB_TCPSTATS(NDRPOINTER):
    referent = (
        ('Data', MIB_TCPSTATS),
    )    


class MIB_TCPTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_TCPROW),('reserved', BYTE),
    )
class PMIB_TCPTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_TCPTABLE),
    )    


class MIB_UDPROW(NDRSTRUCT):
    structure = (
        ('dwLocalAddr', DWORD),('dwLocalPort', DWORD),
    )
class PMIB_UDPROW(NDRPOINTER):
    referent = (
        ('Data', MIB_UDPROW),
    )    


class MIB_UDPSTATS(NDRSTRUCT):
    structure = (
        ('dwInDatagrams', DWORD),('dwNoPorts', DWORD),('dwInErrors', DWORD),('dwOutDatagrams', DWORD),('dwNumAddrs', DWORD),
    )
class PMIB_UDPSTATS(NDRPOINTER):
    referent = (
        ('Data', MIB_UDPSTATS),
    )    


class MIB_UDPTABLE(NDRSTRUCT):
    structure = (
        ('dwNumEntries', DWORD),('table', MIB_UDPROW),('reserved', BYTE),
    )
class PMIB_UDPTABLE(NDRPOINTER):
    referent = (
        ('Data', MIB_UDPTABLE),
    )    


class MPR_SERVER_0(NDRSTRUCT):
    structure = (
        ('fLanOnlyMode', BOOL),('dwUpTime', DWORD),('dwTotalPorts', DWORD),('dwPortsInUse', DWORD),
    )
class PMPR_SERVER_0(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_0),
    )    


class MPR_SERVER_1(NDRSTRUCT):
    structure = (
        ('dwNumPptpPorts', DWORD),('dwPptpPortFlags', DWORD),('dwNumL2tpPorts', DWORD),('dwL2tpPortFlags', DWORD),
    )
class PMPR_SERVER_1(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_1),
    )    


class MPR_SERVER_2(NDRSTRUCT):
    structure = (
        ('dwNumPptpPorts', DWORD),('dwPptpPortFlags', DWORD),('dwNumL2tpPorts', DWORD),('dwL2tpPortFlags', DWORD),('dwNumSstpPorts', DWORD),('dwSstpPortFlags', DWORD),
    )
class PMPR_SERVER_2(NDRPOINTER):
    referent = (
        ('Data', MPR_SERVER_2),
    )    


class PPP_NBFCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('wszWksta', WCHAR),
    )


class PPP_IPCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),
    )


class PPP_IPCP_INFO2(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('wszAddress', WCHAR),('wszRemoteAddress', WCHAR),('dwOptions', DWORD),('dwRemoteOptons', DWORD),
    )


class PPP_IPXCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('wszAddress', WCHAR),
    )


class PPP_IPV6_CP_INFO(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwSize', DWORD),('dwError', DWORD),('bInterfaceIdentifier', BYTE),('bRemoteInterfaceIdentifier', BYTE),('dwOptions', DWORD),('dwRemoteOptions', DWORD),('bPrefix', BYTE),('dwPrefixLength', DWORD),
    )
class PPPP_IPV6_CP_INFO(NDRPOINTER):
    referent = (
        ('Data', PPP_IPV6_CP_INFO),
    )    


class PPP_ATCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('wszAddress', WCHAR),
    )


class PPP_CCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('dwCompressionAlgorithm', DWORD),('dwOptions', DWORD),('dwRemoteCompressionAlgorithm', DWORD),('dwRemoteOptions', DWORD),
    )


class PPP_LCP_INFO(NDRSTRUCT):
    structure = (
        ('dwError', DWORD),('dwAuthenticationProtocol', DWORD),('dwAuthenticationData', DWORD),('dwRemoteAuthenticationProtocol', DWORD),('dwRemoteAuthenticationData', DWORD),('dwTerminateReason', DWORD),('dwRemoteTerminateReason', DWORD),('dwOptions', DWORD),('dwRemoteOptions', DWORD),('dwEapTypeId', DWORD),('dwRemoteEapTypeId', DWORD),
    )


class PPP_INFO(NDRSTRUCT):
    structure = (
        ('nbf', PPP_NBFCP_INFO),('ip', PPP_IPCP_INFO),('ipx', PPP_IPXCP_INFO),('at', PPP_ATCP_INFO),
    )


class PPP_INFO_2(NDRSTRUCT):
    structure = (
        ('nbf', PPP_NBFCP_INFO),('ip', PPP_IPCP_INFO2),('ipx', PPP_IPXCP_INFO),('at', PPP_ATCP_INFO),('ccp', PPP_CCP_INFO),('lcp', PPP_LCP_INFO),
    )


class PPP_INFO_3(NDRSTRUCT):
    structure = (
        ('nbf', PPP_NBFCP_INFO),('ip', PPP_IPCP_INFO2),('ipv6', PPP_IPV6_CP_INFO),('ccp', PPP_CCP_INFO),('lcp', PPP_LCP_INFO),
    )


class RASI_PORT_0(NDRSTRUCT):
    structure = (
        ('dwPort', DWORD),('dwConnection', DWORD),('dwPortCondition', RAS_PORT_CONDITION),('dwTotalNumberOfCalls', DWORD),('dwConnectDuration', DWORD),('wszPortName', WCHAR),('wszMediaName', WCHAR),('wszDeviceName', WCHAR),('wszDeviceType', WCHAR),
    )
class PRASI_PORT_0(NDRPOINTER):
    referent = (
        ('Data', RASI_PORT_0),
    )    


class RASI_PORT_1(NDRSTRUCT):
    structure = (
        ('dwPort', DWORD),('dwConnection', DWORD),('dwHardwareCondition', RAS_HARDWARE_CONDITION),('dwLineSpeed', DWORD),('dwBytesXmited', DWORD),('dwBytesRcved', DWORD),('dwFramesXmited', DWORD),('dwFramesRcved', DWORD),('dwCrcErr', DWORD),('dwTimeoutErr', DWORD),('dwAlignmentErr', DWORD),('dwHardwareOverrunErr', DWORD),('dwFramingErr', DWORD),('dwBufferOverrunErr', DWORD),('dwCompressionRatioIn', DWORD),('dwCompressionRatioOut', DWORD),
    )
class PRASI_PORT_1(NDRPOINTER):
    referent = (
        ('Data', RASI_PORT_1),
    )    


class RASI_CONNECTION_0(NDRSTRUCT):
    structure = (
        ('dwConnection', DWORD),('dwInterface', DWORD),('dwConnectDuration', DWORD),('dwInterfaceType', ROUTER_INTERFACE_TYPE),('dwConnectionFlags', DWORD),('wszInterfaceName', WCHAR),('wszUserName', WCHAR),('wszLogonDomain', WCHAR),('wszRemoteComputer', WCHAR),
    )
class PRASI_CONNECTION_0(NDRPOINTER):
    referent = (
        ('Data', RASI_CONNECTION_0),
    )    


class RASI_CONNECTION_1(NDRSTRUCT):
    structure = (
        ('dwConnection', DWORD),('dwInterface', DWORD),('PppInfo', PPP_INFO),('dwBytesXmited', DWORD),('dwBytesRcved', DWORD),('dwFramesXmited', DWORD),('dwFramesRcved', DWORD),('dwCrcErr', DWORD),('dwTimeoutErr', DWORD),('dwAlignmentErr', DWORD),('dwHardwareOverrunErr', DWORD),('dwFramingErr', DWORD),('dwBufferOverrunErr', DWORD),('dwCompressionRatioIn', DWORD),('dwCompressionRatioOut', DWORD),
    )
class PRASI_CONNECTION_1(NDRPOINTER):
    referent = (
        ('Data', RASI_CONNECTION_1),
    )    


class RASI_CONNECTION_2(NDRSTRUCT):
    structure = (
        ('dwConnection', DWORD),('wszUserName', WCHAR),('dwInterfaceType', ROUTER_INTERFACE_TYPE),('guid', GUID),('PppInfo2', PPP_INFO_2),
    )
class PRASI_CONNECTION_2(NDRPOINTER):
    referent = (
        ('Data', RASI_CONNECTION_2),
    )    


class RASI_CONNECTION_3(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('dwSize', DWORD),('dwConnection', DWORD),('wszUserName', WCHAR),('dwInterfaceType', ROUTER_INTERFACE_TYPE),('guid', GUID),('PppInfo3', PPP_INFO_3),('rasQuarState', RAS_QUARANTINE_STATE),('timer', FILETIME),
    )
class PRASI_CONNECTION_3(NDRPOINTER):
    referent = (
        ('Data', RASI_CONNECTION_3),
    )    


class MPRI_INTERFACE_0(NDRSTRUCT):
    structure = (
        ('wszInterfaceName', WCHAR),('dwInterface', DWORD),('fEnabled', BOOL),('dwIfType', ROUTER_INTERFACE_TYPE),('dwConnectionState', ROUTER_CONNECTION_STATE),('fUnReachabilityReasons', DWORD),('dwLastError', DWORD),
    )
class PMPRI_INTERFACE_0(NDRPOINTER):
    referent = (
        ('Data', MPRI_INTERFACE_0),
    )    


class MPRI_INTERFACE_1(NDRSTRUCT):
    structure = (
        ('wszInterfaceName', WCHAR),('dwInterface', DWORD),('fEnabled', BOOL),('dwIfType', ROUTER_INTERFACE_TYPE),('dwConnectionState', ROUTER_CONNECTION_STATE),('fUnReachabilityReasons', DWORD),('dwLastError', DWORD),('lpwsDialoutHoursRestriction', LPWSTR),
    )
class PMPRI_INTERFACE_1(NDRPOINTER):
    referent = (
        ('Data', MPRI_INTERFACE_1),
    )    


class MPRI_INTERFACE_2(NDRSTRUCT):
    structure = (
        ('wszInterfaceName', WCHAR),('dwInterface', DWORD),('fEnabled', BOOL),('dwIfType', ROUTER_INTERFACE_TYPE),('dwConnectionState', ROUTER_CONNECTION_STATE),('fUnReachabilityReasons', DWORD),('dwLastError', DWORD),('dwfOptions', DWORD),('szLocalPhoneNumber', WCHAR),('szAlternates', PWCHAR),('ipaddr', DWORD),('ipaddrDns', DWORD),('ipaddrDnsAlt', DWORD),('ipaddrWins', DWORD),('ipaddrWinsAlt', DWORD),('dwfNetProtocols', DWORD),('szDeviceType', WCHAR),('szDeviceName', WCHAR),('szX25PadType', WCHAR),('szX25Address', WCHAR),('szX25Facilities', WCHAR),('szX25UserData', WCHAR),('dwChannels', DWORD),('dwSubEntries', DWORD),('dwDialMode', DWORD),('dwDialExtraPercent', DWORD),('dwDialExtraSampleSeconds', DWORD),('dwHangUpExtraPercent', DWORD),('dwHangUpExtraSampleSeconds', DWORD),('dwIdleDisconnectSeconds', DWORD),('dwType', DWORD),('dwEncryptionType', DWORD),('dwCustomAuthKey', DWORD),('dwCustomAuthDataSize', DWORD),('lpbCustomAuthData', LPBYTE),('guidId', GUID),('dwVpnStrategy', DWORD),
    )
class PMPRI_INTERFACE_2(NDRPOINTER):
    referent = (
        ('Data', MPRI_INTERFACE_2),
    )    


class MPRI_INTERFACE_3(NDRSTRUCT):
    structure = (
        ('wszInterfaceName', WCHAR),('dwInterface', DWORD),('fEnabled', BOOL),('dwIfType', ROUTER_INTERFACE_TYPE),('dwConnectionState', ROUTER_CONNECTION_STATE),('fUnReachabilityReasons', DWORD),('dwLastError', DWORD),('dwfOptions', DWORD),('szLocalPhoneNumber', WCHAR),('szAlternates', PWCHAR),('ipaddr', DWORD),('ipaddrDns', DWORD),('ipaddrDnsAlt', DWORD),('ipaddrWins', DWORD),('ipaddrWinsAlt', DWORD),('dwfNetProtocols', DWORD),('szDeviceType', WCHAR),('szDeviceName', WCHAR),('szX25PadType', WCHAR),('szX25Address', WCHAR),('szX25Facilities', WCHAR),('szX25UserData', WCHAR),('dwChannels', DWORD),('dwSubEntries', DWORD),('dwDialMode', DWORD),('dwDialExtraPercent', DWORD),('dwDialExtraSampleSeconds', DWORD),('dwHangUpExtraPercent', DWORD),('dwHangUpExtraSampleSeconds', DWORD),('dwIdleDisconnectSeconds', DWORD),('dwType', DWORD),('dwEncryptionType', DWORD),('dwCustomAuthKey', DWORD),('dwCustomAuthDataSize', DWORD),('lpbCustomAuthData', LPBYTE),('guidId', GUID),('dwVpnStrategy', DWORD),('AddressCount', ULONG),('ipv6addrDns', IN6_ADDR),('ipv6addrDnsAlt', IN6_ADDR),('ipv6addr', IN6_ADDR),
    )
class PMPRI_INTERFACE_3(NDRPOINTER):
    referent = (
        ('Data', MPRI_INTERFACE_3),
    )    


class MPR_DEVICE_0(NDRSTRUCT):
    structure = (
        ('szDeviceType', WCHAR),('szDeviceName', WCHAR),
    )
class PMPR_DEVICE_0(NDRPOINTER):
    referent = (
        ('Data', MPR_DEVICE_0),
    )    


class MPR_DEVICE_1(NDRSTRUCT):
    structure = (
        ('szDeviceType', WCHAR),('szDeviceName', WCHAR),('szLocalPhoneNumber', WCHAR),('szAlternates', PWCHAR),
    )
class PMPR_DEVICE_1(NDRPOINTER):
    referent = (
        ('Data', MPR_DEVICE_1),
    )    


class MPR_CREDENTIALSEX_1(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('dwOffset', DWORD),('bData', BYTE),
    )
class PMPR_CREDENTIALSEX_1(NDRPOINTER):
    referent = (
        ('Data', MPR_CREDENTIALSEX_1),
    )    


class IFFILTER_INFO(NDRSTRUCT):
    structure = (
        ('bEnableFragChk', BOOL),
    )
class PIFFILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', IFFILTER_INFO),
    )    


class MPR_FILTER_0(NDRSTRUCT):
    structure = (
        ('fEnable', IN BOOL),
    )
class PMPR_FILTER_0(NDRPOINTER):
    referent = (
        ('Data', MPR_FILTER_0),
    )    


class IPX_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('RoutingTableHashSize', ULONG),('EventLogMask', ULONG),
    )
class PIPX_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_GLOBAL_INFO),
    )    


class IPX_IF_INFO(NDRSTRUCT):
    structure = (
        ('AdministratorState', ULONG),('NetbiosAccept', ULONG),('NetbiosDeliver', ULONG),
    )
class PIPX_IF_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_IF_INFO),
    )    


class IPXWAN_IF_INFO(NDRSTRUCT):
    structure = (
        ('Adminstate', ULONG),
    )
class PIPXWAN_IF_INFO(NDRPOINTER):
    referent = (
        ('Data', IPXWAN_IF_INFO),
    )    


class U0(NDRUNION):
    union = {
        1: ('DwordAlign',ULONG),2: ('Network',UCHAR),
    }
        

class IPX_STATIC_ROUTE_INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),('TickCount', USHORT),('HopCount', USHORT),('NextHopMacAddress', UCHAR),
    )
class PIPX_STATIC_ROUTE_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_STATIC_ROUTE_INFO),
    )    

IPX_STATIC_SERVICE_INFO = IPX_SERVER_ENTRY
PIPX_STATIC_SERVICE_INFO = IPX_SERVER_ENTRY

class IPX_SERVER_ENTRY(NDRSTRUCT):
    structure = (
        ('Type', USHORT),('Name', UCHAR),('Network', UCHAR),('Node', UCHAR),('Socket', UCHAR),('HopCount', USHORT),
    )
class PIPX_SERVER_ENTRY(NDRPOINTER):
    referent = (
        ('Data', IPX_SERVER_ENTRY),
    )    


class U0(NDRUNION):
    union = {
        1: ('DwordAlign',ULONG),2: ('Name',UCHAR),
    }
        

class IPX_STATIC_NETBIOS_NAME_INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),
    )
class PIPX_STATIC_NETBIOS_NAME_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_STATIC_NETBIOS_NAME_INFO),
    )    


class IPX_ADAPTER_INFO(NDRSTRUCT):
    structure = (
        ('PacketType', ULONG),('AdapterName', WCHAR),
    )
class PIPX_ADAPTER_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_ADAPTER_INFO),
    )    


class IPX_TRAFFIC_FILTER_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('FilterAction', ULONG),
    )
class PIPX_TRAFFIC_FILTER_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_TRAFFIC_FILTER_GLOBAL_INFO),
    )    


class IPX_TRAFFIC_FILTER_INFO(NDRSTRUCT):
    structure = (
        ('FilterDefinition', ULONG),('DestinationNetwork', UCHAR),('DestinationNetworkMask', UCHAR),('DestinationNode', UCHAR),('DestinationSocket', UCHAR),('SourceNetwork', UCHAR),('SourceNetworkMask', UCHAR),('SourceNode', UCHAR),('SourceSocket', UCHAR),('PacketType', UCHAR),
    )
class PIPX_TRAFFIC_FILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', IPX_TRAFFIC_FILTER_INFO),
    )    


class IF_TABLE_INDEX(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),
    )
class PIF_TABLE_INDEX(NDRPOINTER):
    referent = (
        ('Data', IF_TABLE_INDEX),
    )    


class ROUTING_TABLE_INDEX(NDRSTRUCT):
    structure = (
        ('Network', UCHAR),
    )
class PROUTING_TABLE_INDEX(NDRPOINTER):
    referent = (
        ('Data', ROUTING_TABLE_INDEX),
    )    


class STATIC_ROUTES_TABLE_INDEX(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('Network', UCHAR),
    )
class PSTATIC_ROUTES_TABLE_INDEX(NDRPOINTER):
    referent = (
        ('Data', STATIC_ROUTES_TABLE_INDEX),
    )    


class SERVICES_TABLE_INDEX(NDRSTRUCT):
    structure = (
        ('ServiceType', USHORT),('ServiceName', UCHAR),
    )
class PSERVICES_TABLE_INDEX(NDRPOINTER):
    referent = (
        ('Data', SERVICES_TABLE_INDEX),
    )    


class STATIC_SERVICES_TABLE_INDEX(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('ServiceType', USHORT),('ServiceName', UCHAR),
    )
class PSTATIC_SERVICES_TABLE_INDEX(NDRPOINTER):
    referent = (
        ('Data', STATIC_SERVICES_TABLE_INDEX),
    )    


class IPX_MIB_INDEX(NDRUNION):
    union = {
        1: ('InterfaceTableIndex',IF_TABLE_INDEX),2: ('RoutingTableIndex',ROUTING_TABLE_INDEX),3: ('StaticRoutesTableIndex',STATIC_ROUTES_TABLE_INDEX),4: ('ServicesTableIndex',SERVICES_TABLE_INDEX),5: ('StaticServicesTableIndex',STATIC_SERVICES_TABLE_INDEX),
    }
        class PIPX_MIB_INDEX(NDRPOINTER):
    referent = (
        ('Data', IPX_MIB_INDEX),
    )    


class IPX_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('MibIndex', IPX_MIB_INDEX),
    )
class PIPX_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPX_MIB_GET_INPUT_DATA),
    )    


class IPXMIB_BASE(NDRSTRUCT):
    structure = (
        ('OperState', ULONG),('PrimaryNetNumber', UCHAR),('Node', UCHAR),('SysName', UCHAR),('MaxPathSplits', ULONG),('IfCount', ULONG),('DestCount', ULONG),('ServCount', ULONG),
    )
class PIPXMIB_BASE(NDRPOINTER):
    referent = (
        ('Data', IPXMIB_BASE),
    )    


class IPX_IF_STATS(NDRSTRUCT):
    structure = (
        ('IfOperState', ULONG),('MaxPacketSize', ULONG),('InHdrErrors', ULONG),('InFiltered', ULONG),('InNoRoutes', ULONG),('InDiscards', ULONG),('InDelivers', ULONG),('OutFiltered', ULONG),('OutDiscards', ULONG),('OutDelivers', ULONG),('NetbiosReceived', ULONG),('NetbiosSent', ULONG),
    )
class PIPX_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', IPX_IF_STATS),
    )    


class IPX_INTERFACE(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('AdministratorState', ULONG),('AdapterIndex', ULONG),('InterfaceName', UCHAR),('InterfaceType', ULONG),('MediaType', ULONG),('NetNumber', UCHAR),('MacAddress', UCHAR),('Delay', ULONG),('Throughput', ULONG),('NetbiosAccept', ULONG),('NetbiosDeliver', ULONG),('EnableIpxWanNegotiation', ULONG),('IfStats', IPX_IF_STATS),
    )
class PIPX_INTERFACE(NDRPOINTER):
    referent = (
        ('Data', IPX_INTERFACE),
    )    


class IPX_ROUTE(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('Protocol', ULONG),('Network', UCHAR),('TickCount', USHORT),('HopCount', USHORT),('NextHopMacAddress', UCHAR),('Flags', ULONG),
    )
class PIPX_ROUTE(NDRPOINTER):
    referent = (
        ('Data', IPX_ROUTE),
    )    


class IPX_SERVICE(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('Protocol', ULONG),('Server', IPX_SERVER_ENTRY),
    )
class PIPX_SERVICE(NDRPOINTER):
    referent = (
        ('Data', IPX_SERVICE),
    )    


class IPX_MIB_ROW(NDRUNION):
    union = {
        1: ('Interface',IPX_INTERFACE),2: ('Route',IPX_ROUTE),3: ('Service',IPX_SERVICE),
    }
        class PIPX_MIB_ROW(NDRPOINTER):
    referent = (
        ('Data', IPX_MIB_ROW),
    )    


class IPX_MIB_SET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('MibRow', IPX_MIB_ROW),
    )
class PIPX_MIB_SET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPX_MIB_SET_INPUT_DATA),
    )    


class U0(NDRUNION):
    union = {
        1: ('ServiceType',USHORT),2: ('ServiceType_align',ULONG),
    }
        

class SAP_SERVICE_FILTER_INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),('ServiceName', UCHAR),
    )
class PSAP_SERVICE_FILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', SAP_SERVICE_FILTER_INFO),
    )    


class SAP_IF_FILTERS(NDRSTRUCT):
    structure = (
        ('SupplyFilterAction', ULONG),('SupplyFilterCount', ULONG),('ListenFilterAction', ULONG),('ListenFilterCount', ULONG),('ServiceFilter', SAP_SERVICE_FILTER_INFO),
    )
class PSAP_IF_FILTERS(NDRPOINTER):
    referent = (
        ('Data', SAP_IF_FILTERS),
    )    


class SAP_IF_INFO(NDRSTRUCT):
    structure = (
        ('AdminState', ULONG),('UpdateMode', ULONG),('PacketType', ULONG),('Supply', ULONG),('Listen', ULONG),('GetNearestServerReply', ULONG),('PeriodicUpdateInterval', ULONG),('AgeIntervalMultiplier', ULONG),
    )
class PSAP_IF_INFO(NDRPOINTER):
    referent = (
        ('Data', SAP_IF_INFO),
    )    


class SAP_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('SapIfInfo', SAP_IF_INFO),('SapIfFilters', SAP_IF_FILTERS),
    )
class PSAP_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', SAP_IF_CONFIG),
    )    


class SAP_MIB_BASE(NDRSTRUCT):
    structure = (
        ('SapOperState', ULONG),
    )
class PSAP_MIB_BASE(NDRPOINTER):
    referent = (
        ('Data', SAP_MIB_BASE),
    )    


class SAP_IF_STATS(NDRSTRUCT):
    structure = (
        ('SapIfOperState', ULONG),('SapIfInputPackets', ULONG),('SapIfOutputPackets', ULONG),
    )
class PSAP_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', SAP_IF_STATS),
    )    


class SAP_INTERFACE(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('SapIfInfo', SAP_IF_INFO),('SapIfStats', SAP_IF_STATS),
    )
class PSAP_INTERFACE(NDRPOINTER):
    referent = (
        ('Data', SAP_INTERFACE),
    )    


class SAP_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('InterfaceIndex', ULONG),
    )
class PSAP_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', SAP_MIB_GET_INPUT_DATA),
    )    


class SAP_MIB_SET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('SapInterface', SAP_INTERFACE),
    )
class PSAP_MIB_SET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', SAP_MIB_SET_INPUT_DATA),
    )    


class RIPMIB_BASE(NDRSTRUCT):
    structure = (
        ('RIPOperState', ULONG),
    )
class PRIPMIB_BASE(NDRPOINTER):
    referent = (
        ('Data', RIPMIB_BASE),
    )    


class RIP_IF_STATS(NDRSTRUCT):
    structure = (
        ('RipIfOperState', ULONG),('RipIfInputPackets', ULONG),('RipIfOutputPackets', ULONG),
    )
class PRIP_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', RIP_IF_STATS),
    )    


class RIP_IF_INFO(NDRSTRUCT):
    structure = (
        ('AdminState', ULONG),('UpdateMode', ULONG),('PacketType', ULONG),('Supply', ULONG),('Listen', ULONG),('PeriodicUpdateInterval', ULONG),('AgeIntervalMultiplier', ULONG),
    )
class PRIP_IF_INFO(NDRPOINTER):
    referent = (
        ('Data', RIP_IF_INFO),
    )    


class RIP_INTERFACE(NDRSTRUCT):
    structure = (
        ('InterfaceIndex', ULONG),('RipIfInfo', RIP_IF_INFO),('RipIfStats', RIP_IF_STATS),
    )
class PRIP_INTERFACE(NDRPOINTER):
    referent = (
        ('Data', RIP_INTERFACE),
    )    


class RIP_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('InterfaceIndex', ULONG),
    )
class PRIP_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', RIP_MIB_GET_INPUT_DATA),
    )    


class RIP_MIB_SET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TableId', ULONG),('RipInterface', RIP_INTERFACE),
    )
class PRIP_MIB_SET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', RIP_MIB_SET_INPUT_DATA),
    )    


class EAPTLS_HASH(NDRSTRUCT):
    structure = (
        ('cbHash', DWORD),('pbHash', BYTE),
    )


class EAPTLS_USER_PROPERTIES(NDRSTRUCT):
    structure = (
        ('reserved', DWORD),('dwVersion', DWORD),('dwSize', DWORD),('fFlags', DWORD),('Hash', EAPTLS_HASH),('pwszDiffUser', WCHAR),('dwPinOffset', DWORD),('pwszPin', WCHAR),('usLength', USHORT),('usMaximumLength', USHORT),('ucSeed', UCHAR),('awszString', WCHAR),
    )


class IPBOOTP_GLOBAL_CONFIG(NDRSTRUCT):
    structure = (
        ('GC_LoggingLevel', DWORD),('GC_MaxRecvQueueSize', DWORD),('GC_ServerCount', DWORD),
    )
class PIPBOOTP_GLOBAL_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_GLOBAL_CONFIG),
    )    


class IPBOOTP_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('IC_State', DWORD),('IC_RelayMode', DWORD),('IC_MaxHopCount', DWORD),('IC_MinSecondsSinceBoot', DWORD),
    )
class PIPBOOTP_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_IF_CONFIG),
    )    


class IPBOOTP_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGID_TypeID', DWORD),('IMGID_IfIndex', DWORD),
    )
class PIPBOOTP_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_MIB_GET_INPUT_DATA),
    )    


class IPBOOTP_MIB_GET_OUTPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGOD_TypeID', DWORD),('IMGOD_IfIndex', DWORD),('IMGOD_Buffer', BYTE),
    )
class PIPBOOTP_MIB_GET_OUTPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_MIB_GET_OUTPUT_DATA),
    )    


class IPBOOTP_IF_STATS(NDRSTRUCT):
    structure = (
        ('IS_State', DWORD),('IS_SendFailures', DWORD),('IS_ReceiveFailures', DWORD),('IS_ArpUpdateFailures', DWORD),('IS_RequestsReceived', DWORD),('IS_RequestsDiscarded', DWORD),('IS_RepliesReceived', DWORD),('IS_RepliesDiscarded', DWORD),
    )
class PIPBOOTP_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_IF_STATS),
    )    


class IPBOOTP_IF_BINDING(NDRSTRUCT):
    structure = (
        ('IB_State', DWORD),('IB_AddrCount', DWORD),
    )
class PIPBOOTP_IF_BINDING(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_IF_BINDING),
    )    


class IPBOOTP_IP_ADDRESS(NDRSTRUCT):
    structure = (
        ('IA_Address', DWORD),('IA_Netmask', DWORD),
    )
class PIPBOOTP_IP_ADDRESS(NDRPOINTER):
    referent = (
        ('Data', IPBOOTP_IP_ADDRESS),
    )    


class DHCPV6R_MIB_GET_OUTPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGOD_TypeID', DWORD),('IMGOD_IfIndex', DWORD),('IMGOD_Buffer', BYTE),
    )
class PDHCPV6R_MIB_GET_OUTPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', DHCPV6R_MIB_GET_OUTPUT_DATA),
    )    


class DHCPV6R_IF_STATS(NDRSTRUCT):
    structure = (
        ('IS_State', DWORD),('IS_SendFailures', DWORD),('IS_ReceiveFailures', DWORD),('IS_RequestsReceived', DWORD),('IS_RequestsDiscarded', DWORD),('IS_RepliesReceived', DWORD),('IS_RepliesDiscarded', DWORD),
    )
class PDHCPV6R_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', DHCPV6R_IF_STATS),
    )    


class DHCPV6R_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGID_TypeID', DWORD),('IMGID_IfIndex', DWORD),
    )
class PDHCPV6R_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', DHCPV6R_MIB_GET_INPUT_DATA),
    )    


class DHCPV6R_GLOBAL_CONFIG(NDRSTRUCT):
    structure = (
        ('GC_LoggingLevel', DWORD),('GC_MaxRecvQueueSize', DWORD),('GC_ServerCount', DWORD),
    )
class PDHCPV6R_GLOBAL_CONFIG(NDRPOINTER):
    referent = (
        ('Data', DHCPV6R_GLOBAL_CONFIG),
    )    


class DHCPV6R_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('IC_State', DWORD),('IC_RelayMode', DWORD),('IC_MaxHopCount', DWORD),('IC_MinElapsedTime', DWORD),
    )
class PDHCPV6R_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', DHCPV6R_IF_CONFIG),
    )    


class U0(NDRUNION):
    union = {
        1: ('IMGID_IfIndex',DWORD),2: ('IMGID_PeerAddress',DWORD),
    }
        

class IPRIP_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGID_TypeID', DWORD),('u0', U0),
    )
class PIPRIP_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPRIP_MIB_GET_INPUT_DATA),
    )    


class U0(NDRUNION):
    union = {
        1: ('IMGOD_IfIndex',DWORD),2: ('IMGOD_PeerAddress',DWORD),
    }
        

class IPRIP_MIB_GET_OUTPUT_DATA(NDRSTRUCT):
    structure = (
        ('IMGOD_TypeID', DWORD),('u0', U0),('IMGOD_Buffer', BYTE),
    )
class PIPRIP_MIB_GET_OUTPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IPRIP_MIB_GET_OUTPUT_DATA),
    )    


class IPRIP_GLOBAL_STATS(NDRSTRUCT):
    structure = (
        ('GS_SystemRouteChanges', DWORD),('GS_TotalResponsesSent', DWORD),
    )
class PIPRIP_GLOBAL_STATS(NDRPOINTER):
    referent = (
        ('Data', IPRIP_GLOBAL_STATS),
    )    


class IPRIP_GLOBAL_CONFIG(NDRSTRUCT):
    structure = (
        ('GC_LoggingLevel', DWORD),('GC_MaxRecvQueueSize', DWORD),('GC_MaxSendQueueSize', DWORD),('GC_MinTriggeredUpdateInterval', DWORD),('GC_PeerFilterMode', DWORD),('GC_PeerFilterCount', DWORD),
    )
class PIPRIP_GLOBAL_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IPRIP_GLOBAL_CONFIG),
    )    


class IPRIP_IF_STATS(NDRSTRUCT):
    structure = (
        ('IS_State', DWORD),('IS_SendFailures', DWORD),('IS_ReceiveFailures', DWORD),('IS_RequestsSent', DWORD),('IS_RequestsReceived', DWORD),('IS_ResponsesSent', DWORD),('IS_ResponsesReceived', DWORD),('IS_BadResponsePacketsReceived', DWORD),('IS_BadResponseEntriesReceived', DWORD),('IS_TriggeredUpdatesSent', DWORD),
    )
class PIPRIP_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', IPRIP_IF_STATS),
    )    


class IPRIP_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('IC_State', DWORD),('IC_Metric', DWORD),('IC_UpdateMode', DWORD),('IC_AcceptMode', DWORD),('IC_AnnounceMode', DWORD),('IC_ProtocolFlags', DWORD),('IC_RouteExpirationInterval', DWORD),('IC_RouteRemovalInterval', DWORD),('IC_FullUpdateInterval', DWORD),('IC_AuthenticationType', DWORD),('IC_AuthenticationKey', BYTE),('IC_RouteTag', WORD),('IC_UnicastPeerMode', DWORD),('IC_AcceptFilterMode', DWORD),('IC_AnnounceFilterMode', DWORD),('IC_UnicastPeerCount', DWORD),('IC_AcceptFilterCount', DWORD),('IC_AnnounceFilterCount', DWORD),
    )
class PIPRIP_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IPRIP_IF_CONFIG),
    )    


class IPRIP_ROUTE_FILTER(NDRSTRUCT):
    structure = (
        ('RF_LoAddress', DWORD),('RF_HiAddress', DWORD),
    )
class PIPRIP_ROUTE_FILTER(NDRPOINTER):
    referent = (
        ('Data', IPRIP_ROUTE_FILTER),
    )    


class IPRIP_IF_BINDING(NDRSTRUCT):
    structure = (
        ('IB_State', DWORD),('IB_AddrCount', DWORD),
    )
class PIPRIP_IF_BINDING(NDRPOINTER):
    referent = (
        ('Data', IPRIP_IF_BINDING),
    )    


class IPRIP_IP_ADDRESS(NDRSTRUCT):
    structure = (
        ('IA_Address', DWORD),('IA_Netmask', DWORD),
    )
class PIPRIP_IP_ADDRESS(NDRPOINTER):
    referent = (
        ('Data', IPRIP_IP_ADDRESS),
    )    


class IPRIP_PEER_STATS(NDRSTRUCT):
    structure = (
        ('PS_LastPeerRouteTag', DWORD),('PS_LastPeerUpdateTickCount', DWORD),('PS_LastPeerUpdateVersion', DWORD),('PS_BadResponsePacketsFromPeer', DWORD),('PS_BadResponseEntriesFromPeer', DWORD),
    )
class PIPRIP_PEER_STATS(NDRPOINTER):
    referent = (
        ('Data', IPRIP_PEER_STATS),
    )    


class IGMP_MIB_GET_INPUT_DATA(NDRSTRUCT):
    structure = (
        ('TypeId', DWORD),('Flags', USHORT),('Signature', USHORT),('IfIndex', DWORD),('RasClientAddr', DWORD),('GroupAddr', DWORD),('Count', DWORD),
    )
class PIGMP_MIB_GET_INPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GET_INPUT_DATA),
    )    


class IGMP_MIB_GET_OUTPUT_DATA(NDRSTRUCT):
    structure = (
        ('TypeId', DWORD),('Flags', DWORD),('Count', DWORD),('Buffer', BYTE),
    )
class PIGMP_MIB_GET_OUTPUT_DATA(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GET_OUTPUT_DATA),
    )    


class IGMP_MIB_GLOBAL_CONFIG(NDRSTRUCT):
    structure = (
        ('Version', DWORD),('LoggingLevel', DWORD),('RasClientStats', DWORD),
    )
class PIGMP_MIB_GLOBAL_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GLOBAL_CONFIG),
    )    


class IGMP_MIB_GLOBAL_STATS(NDRSTRUCT):
    structure = (
        ('CurrentGroupMemberships', DWORD),('GroupMembershipsAdded', DWORD),
    )
class PIGMP_MIB_GLOBAL_STATS(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GLOBAL_STATS),
    )    


class IGMP_MIB_IF_BINDING(NDRSTRUCT):
    structure = (
        ('IfIndex', DWORD),('IfType', DWORD),('State', DWORD),('AddrCount', DWORD),
    )
class PIGMP_MIB_IF_BINDING(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_IF_BINDING),
    )    


class IGMP_MIB_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('Version', DWORD),('IfIndex', DWORD),('IpAddr', DWORD),('IfType', DWORD),('Flags', DWORD),('IgmpProtocolType', DWORD),('RobustnessVariable', DWORD),('StartupQueryInterval', DWORD),('StartupQueryCount', DWORD),('GenQueryInterval', DWORD),('GenQueryMaxResponseTime', DWORD),('LastMemQueryInterval', DWORD),('LastMemQueryCount', DWORD),('OtherQuerierPresentInterval', DWORD),('GroupMembershipTimeout', DWORD),('NumStaticGroups', DWORD),
    )
class PIGMP_MIB_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_IF_CONFIG),
    )    


class IGMP_MIB_IF_GROUPS_LIST(NDRSTRUCT):
    structure = (
        ('IfIndex', DWORD),('IpAddr', DWORD),('IfType', DWORD),('NumGroups', DWORD),('Buffer', BYTE),
    )
class PIGMP_MIB_IF_GROUPS_LIST(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_IF_GROUPS_LIST),
    )    


class U0(NDRUNION):
    union = {
        1: ('IfIndex',DWORD),2: ('GroupAddr',DWORD),
    }
        

class IGMP_MIB_GROUP_INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),('IpAddr', DWORD),('GroupUpTime', DWORD),('GroupExpiryTime', DWORD),('LastReporter', DWORD),('V1HostPresentTimeLeft', DWORD),('Flags', DWORD),
    )
class PIGMP_MIB_GROUP_INFO(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GROUP_INFO),
    )    


class IGMP_MIB_IF_STATS(NDRSTRUCT):
    structure = (
        ('IfIndex', DWORD),('IpAddr', DWORD),('IfType', DWORD),('State', BYTE),('QuerierState', BYTE),('IgmpProtocolType', DWORD),('QuerierIpAddr', DWORD),('ProxyIfIndex', DWORD),('QuerierPresentTimeLeft', DWORD),('LastQuerierChangeTime', DWORD),('V1QuerierPresentTimeLeft', DWORD),('Uptime', DWORD),('TotalIgmpPacketsReceived', DWORD),('TotalIgmpPacketsForRouter', DWORD),('GeneralQueriesReceived', DWORD),('WrongVersionQueries', DWORD),('JoinsReceived', DWORD),('LeavesReceived', DWORD),('CurrentGroupMemberships', DWORD),('GroupMembershipsAdded', DWORD),('WrongChecksumPackets', DWORD),('ShortPacketsReceived', DWORD),('LongPacketsReceived', DWORD),('PacketsWithoutRtrAlert', DWORD),
    )
class PIGMP_MIB_IF_STATS(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_IF_STATS),
    )    


class IGMP_MIB_GROUP_IFS_LIST(NDRSTRUCT):
    structure = (
        ('GroupAddr', DWORD),('NumInterfaces', DWORD),('Buffer', BYTE),
    )
class PIGMP_MIB_GROUP_IFS_LIST(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GROUP_IFS_LIST),
    )    


class IGMP_MIB_GROUP_SOURCE_INFO_V3(NDRSTRUCT):
    structure = (
        ('Source', DWORD),('SourceExpiryTime', DWORD),('SourceUpTime', DWORD),('Flags', DWORD),
    )
class PIGMP_MIB_GROUP_SOURCE_INFO_V3(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GROUP_SOURCE_INFO_V3),
    )    


class U0(NDRUNION):
    union = {
        1: ('IfIndex',DWORD),2: ('GroupAddr',DWORD),
    }
        

class IGMP_MIB_GROUP_INFO_V3(NDRSTRUCT):
    structure = (
        ('u0', U0),('IpAddr', DWORD),('GroupUpTime', DWORD),('GroupExpiryTime', DWORD),('LastReporter', DWORD),('V1HostPresentTimeLeft', DWORD),('Flags', DWORD),('Version', DWORD),('Size', DWORD),('FilterType', DWORD),('V2HostPresentTimeLeft', DWORD),('NumSources', DWORD),
    )
class PIGMP_MIB_GROUP_INFO_V3(NDRPOINTER):
    referent = (
        ('Data', IGMP_MIB_GROUP_INFO_V3),
    )    


class INTERFACE_ROUTE_ENTRY(NDRSTRUCT):
    structure = (
        ('dwIndex', DWORD),('routeInfo', INTERFACE_ROUTE_INFO),
    )
class PINTERFACE_ROUTE_ENTRY(NDRPOINTER):
    referent = (
        ('Data', INTERFACE_ROUTE_ENTRY),
    )    


class U0(NDRUNION):
    union = {
        1: ('Index',ULONG),2: ('Data',UCHAR),
    }
        

class IP_NAT_MIB_QUERY(NDRSTRUCT):
    structure = (
        ('Oid', ULONG),('u0', U0),
    )
class PIP_NAT_MIB_QUERY(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_MIB_QUERY),
    )    


NatInboundDirection = 0
        

class IP_NAT_SESSION_MAPPING(NDRSTRUCT):
    structure = (
        ('Protocol', UCHAR),('PrivateAddress', ULONG),('PrivatePort', USHORT),('PublicAddress', ULONG),('PublicPort', USHORT),('RemoteAddress', ULONG),('RemotePort', USHORT),('Direction', IP_NAT_DIRECTION),('IdleTime', ULONG),
    )
class PIP_NAT_SESSION_MAPPING(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_SESSION_MAPPING),
    )    


class IP_NAT_ENUMERATE_SESSION_MAPPINGS(NDRSTRUCT):
    structure = (
        ('Index', IN ULONG),('EnumerateContext', IN OUT ULONG),('EnumerateCount', OUT ULONG),('EnumerateTotalHint', OUT ULONG),('EnumerateTable', OUT IP_NAT_SESSION_MAPPING),
    )
class PIP_NAT_ENUMERATE_SESSION_MAPPINGS(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_ENUMERATE_SESSION_MAPPINGS),
    )    


class IP_NAT_INTERFACE_STATISTICS(NDRSTRUCT):
    structure = (
        ('TotalMappings', OUT ULONG),('InboundMappings', OUT ULONG),('BytesForward', OUT ULONG64),('BytesReverse', OUT ULONG64),('PacketsForward', OUT ULONG64),('PacketsReverse', OUT ULONG64),('RejectsForward', OUT ULONG64),('RejectsReverse', OUT ULONG64),
    )
class PIP_NAT_INTERFACE_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_INTERFACE_STATISTICS),
    )    


class U0(NDRUNION):
    union = {
        1: ('Index',ULONG),2: ('Data',UCHAR),
    }
        

class IP_DNS_PROXY_MIB_QUERY(NDRSTRUCT):
    structure = (
        ('Oid', ULONG),('u0', U0),
    )
class PIP_DNS_PROXY_MIB_QUERY(NDRPOINTER):
    referent = (
        ('Data', IP_DNS_PROXY_MIB_QUERY),
    )    


class IP_DNS_PROXY_STATISTICS(NDRSTRUCT):
    structure = (
        ('MessagesIgnored', ULONG),('QueriesReceived', ULONG),('ResponsesReceived', ULONG),('QueriesSent', ULONG),('ResponsesSent', ULONG),
    )
class PIP_DNS_PROXY_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', IP_DNS_PROXY_STATISTICS),
    )    


class U0(NDRUNION):
    union = {
        1: ('Index',ULONG),2: ('Data',UCHAR),
    }
        

class IP_AUTO_DHCP_MIB_QUERY(NDRSTRUCT):
    structure = (
        ('Oid', ULONG),('u0', U0),('Reserved', ULONG),
    )
class PIP_AUTO_DHCP_MIB_QUERY(NDRPOINTER):
    referent = (
        ('Data', IP_AUTO_DHCP_MIB_QUERY),
    )    


class IP_AUTO_DHCP_STATISTICS(NDRSTRUCT):
    structure = (
        ('MessagesIgnored', ULONG),('BootpOffersSent', ULONG),('DiscoversReceived', ULONG),('InformsReceived', ULONG),('OffersSent', ULONG),('RequestsReceived', ULONG),('AcksSent', ULONG),('NaksSent', ULONG),('DeclinesReceived', ULONG),('ReleasesReceived', ULONG),
    )
class PIP_AUTO_DHCP_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', IP_AUTO_DHCP_STATISTICS),
    )    


class MIB_DA_MSG(NDRSTRUCT):
    structure = (
        ('op_code', UINT32),('ret_code', UINT32),('in_snmp_id', UINT32),('obj_id', UINT32),('attr_id', UINT32),('inst_id', UINT32),('next_snmp_id', UINT32),('creator', UINT32),('attr_type', UINT32),('inst_cnt', UINT32),('map_flag', UINT32),('data', ULONG_PTR),
    )


class IP_AUTO_DHCP_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('LoggingLevel', ULONG),('Flags', ULONG),('LeaseTime', ULONG),('ScopeNetwork', ULONG),('ScopeMask', ULONG),('ExclusionCount', ULONG),('ExclusionArray', ULONG),
    )
class PIP_AUTO_DHCP_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_AUTO_DHCP_GLOBAL_INFO),
    )    


class IP_AUTO_DHCP_INTERFACE_INFO(NDRSTRUCT):
    structure = (
        ('Flags', ULONG),
    )
class PIP_AUTO_DHCP_INTERFACE_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_AUTO_DHCP_INTERFACE_INFO),
    )    


class IP_DNS_PROXY_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('LoggingLevel', ULONG),('Flags', ULONG),('TimeoutSeconds', ULONG),
    )
class PIP_DNS_PROXY_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_DNS_PROXY_GLOBAL_INFO),
    )    


class IP_DNS_PROXY_INTERFACE_INFO(NDRSTRUCT):
    structure = (
        ('Flags', ULONG),
    )
class PIP_DNS_PROXY_INTERFACE_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_DNS_PROXY_INTERFACE_INFO),
    )    


class IP_NAT_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('LoggingLevel', ULONG),('Flags', ULONG),('Header', RTR_INFO_BLOCK_HEADER),
    )
class PIP_NAT_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_GLOBAL_INFO),
    )    


class IP_NAT_TIMEOUT(NDRSTRUCT):
    structure = (
        ('TCPTimeoutSeconds', ULONG),('UDPTimeoutSeconds', ULONG),
    )
class PIP_NAT_TIMEOUT(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_TIMEOUT),
    )    


class IP_NAT_INTERFACE_INFO(NDRSTRUCT):
    structure = (
        ('Index', ULONG),('Flags', ULONG),('Header', RTR_INFO_BLOCK_HEADER),
    )
class PIP_NAT_INTERFACE_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_INTERFACE_INFO),
    )    


class IP_NAT_ADDRESS_RANGE(NDRSTRUCT):
    structure = (
        ('StartAddress', ULONG),('EndAddress', ULONG),('SubnetMask', ULONG),
    )
class PIP_NAT_ADDRESS_RANGE(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_ADDRESS_RANGE),
    )    


class IP_NAT_PORT_MAPPING(NDRSTRUCT):
    structure = (
        ('Protocol', UCHAR),('PublicPort', USHORT),('PublicAddress', ULONG),('PrivatePort', USHORT),('PrivateAddress', ULONG),
    )
class PIP_NAT_PORT_MAPPING(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_PORT_MAPPING),
    )    


class IP_NAT_ADDRESS_MAPPING(NDRSTRUCT):
    structure = (
        ('PrivateAddress', ULONG),('PublicAddress', ULONG),('AllowInboundSessions', BOOLEAN),
    )
class PIP_NAT_ADDRESS_MAPPING(NDRPOINTER):
    referent = (
        ('Data', IP_NAT_ADDRESS_MAPPING),
    )    


class IP_ALG_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('LoggingLevel', ULONG),('Flags', ULONG),
    )
class PIP_ALG_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', IP_ALG_GLOBAL_INFO),
    )    


class RIP_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('EventLogMask', DWORD),
    )
class PRIP_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', RIP_GLOBAL_INFO),
    )    


class RIP_ROUTE_FILTER_INFO(NDRSTRUCT):
    structure = (
        ('Network', UCHAR),('Mask', UCHAR),
    )
class PRIP_ROUTE_FILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', RIP_ROUTE_FILTER_INFO),
    )    


class RIP_IF_FILTERS(NDRSTRUCT):
    structure = (
        ('SupplyFilterAction', ULONG),('SupplyFilterCount', ULONG),('ListenFilterAction', ULONG),('ListenFilterCount', ULONG),('RouteFilter', RIP_ROUTE_FILTER_INFO),
    )
class PRIP_IF_FILTERS(NDRPOINTER):
    referent = (
        ('Data', RIP_IF_FILTERS),
    )    


class RIP_IF_CONFIG(NDRSTRUCT):
    structure = (
        ('RipIfInfo', RIP_IF_INFO),('RipIfFilters', RIP_IF_FILTERS),
    )
class PRIP_IF_CONFIG(NDRPOINTER):
    referent = (
        ('Data', RIP_IF_CONFIG),
    )    


class SAP_GLOBAL_INFO(NDRSTRUCT):
    structure = (
        ('EventLogMask', DWORD),
    )
class PSAP_GLOBAL_INFO(NDRPOINTER):
    referent = (
        ('Data', SAP_GLOBAL_INFO),
    )    


class OSPF_ROUTE_FILTER(NDRSTRUCT):
    structure = (
        ('dwAddress', DWORD),('dwMask', DWORD),
    )
class POSPF_ROUTE_FILTER(NDRPOINTER):
    referent = (
        ('Data', OSPF_ROUTE_FILTER),
    )    


ACTION_DROP = 0,
ACTION_ACCEPT = 1
        

class OSPF_ROUTE_FILTER_INFO(NDRSTRUCT):
    structure = (
        ('type', DWORD),('ofaActionOnMatch', OSPF_FILTER_ACTION),('dwNumFilters', DWORD),('pFilters', OSPF_ROUTE_FILTER),
    )
class POSPF_ROUTE_FILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', OSPF_ROUTE_FILTER_INFO),
    )    


class OSPF_PROTO_FILTER_INFO(NDRSTRUCT):
    structure = (
        ('type', DWORD),('ofaActionOnMatch', OSPF_FILTER_ACTION),('dwNumProtoIds', DWORD),('pdwProtoId', DWORD),
    )
class POSPF_PROTO_FILTER_INFO(NDRPOINTER):
    referent = (
        ('Data', OSPF_PROTO_FILTER_INFO),
    )    


class OSPF_GLOBAL_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('routerId', DWORD),('ASBrdrRtr', DWORD),('logLevel', DWORD),
    )
class POSPF_GLOBAL_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_GLOBAL_PARAM),
    )    


class OSPF_AREA_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('areaId', DWORD),('authType', DWORD),('importASExtern', DWORD),('stubMetric', DWORD),('importSumAdv', DWORD),
    )
class POSPF_AREA_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_AREA_PARAM),
    )    


class OSPF_AREA_RANGE_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('areaId', DWORD),('rangeNet', DWORD),('rangeMask', DWORD),
    )
class POSPF_AREA_RANGE_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_AREA_RANGE_PARAM),
    )    


class OSPF_VIRT_INTERFACE_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('transitAreaId', DWORD),('virtNeighborRouterId', DWORD),('transitDelay', DWORD),('retransInterval', DWORD),('helloInterval', DWORD),('deadInterval', DWORD),('password', BYTE),
    )
class POSPF_VIRT_INTERFACE_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_VIRT_INTERFACE_PARAM),
    )    


class OSPF_INTERFACE_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('intfIpAddr', DWORD),('intfSubnetMask', DWORD),('areaId', DWORD),('intfType', DWORD),('routerPriority', DWORD),('transitDelay', DWORD),('retransInterval', DWORD),('helloInterval', DWORD),('deadInterval', DWORD),('pollInterval', DWORD),('metricCost', DWORD),('password', BYTE),('mtuSize', DWORD),
    )
class POSPF_INTERFACE_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_INTERFACE_PARAM),
    )    


class OSPF_NBMA_NEIGHBOR_PARAM(NDRSTRUCT):
    structure = (
        ('type', DWORD),('create', DWORD),('enable', DWORD),('neighborIpAddr', DWORD),('intfIpAddr', DWORD),('neighborPriority', DWORD),
    )
class POSPF_NBMA_NEIGHBOR_PARAM(NDRPOINTER):
    referent = (
        ('Data', OSPF_NBMA_NEIGHBOR_PARAM),
    )    


RDT_Modem = 0,
RDT_X25 = 0,
RDT_Isdn = 0,
RDT_Serial = 0,
RDT_FrameRelay = 0,
RDT_Atm = 0,
RDT_Sonet = 0,
RDT_Sw56 = 0,
RDT_Tunnel_Pptp = 0,
RDT_Tunnel_L2tp = 0,
RDT_Irda = 0,
RDT_Parallel = 0,
RDT_Other = 0,
RDT_PPPoE = 0,
RDT_Tunnel_Sstp = 0,
RDT_Tunnel_Ikev2 = 0,
RDT_Tunnel = 65536,
RDT_Direct = 131072,
RDT_Null_Modem = 262144,
RDT_Broadband = 524288
        

OPEN = 0,
CLOSED = 1,
UNAVAILABLE = 2,
REMOVED = 3
        

REQTYPE_PORTENUM = 21,
REQTYPE_GETINFO = 22,
REQTYPE_GETDEVCONFIG = 73,
REQTYPE_SETDEVICECONFIGINFO = 94,
REQTYPE_GETDEVICECONFIGINFO = 95,
REQTYPE_GETCALLEDID = 105,
REQTYPE_SETCALLEDID = 106,
REQTYPE_GETNDISWANDRIVERCAPS = 111
        

CONNECTING = 0,
LISTENING = 1,
CONNECTED = 2,
DISCONNECTING = 3,
DISCONNECTED = 4,
LISTENCOMPLETED = 5
        

USER_REQUESTED = 0,
REMOTE_DISCONNECTION = 1,
HARDWARE_FAILURE = 2,
NOT_DISCONNECTED = 3
        

CALL_NONE = 0,
CALL_IN = 1,
CALL_OUT = 2,
CALL_ROUTER = 4,
CALL_LOGON = 8,
CALL_OUT_ONLY = 16,
CALL_IN_ONLY = 32,
CALL_OUTBOUND_ROUTER = 64
        

class REQUESTBUFFER(NDRSTRUCT):
    structure = (
        ('RB_PCBIndex', DWORD),('RB_Reqtype', REQTYPES),('RB_Dummy', DWORD),('RB_Done', DWORD),('Alignment', LONGLONG),('RB_Buffer', BYTE),
    )


class DEVICECONFIGINFO(NDRSTRUCT):
    structure = (
        ('retcode', DWORD),('dwVersion', DWORD),('cbBuffer', DWORD),('cEntries', DWORD),('abdata', BYTE),
    )


class RAS_DEVICE_INFO(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('fWrite', BOOL),('fRasEnabled', BOOL),('fRouterEnabled', BOOL),('fRouterOutboundEnabled', BOOL),('dwTapiLineId', DWORD),('dwError', DWORD),('dwNumEndPoints', DWORD),('dwMaxOutCalls', DWORD),('dwMaxInCalls', DWORD),('dwMinWanEndPoints', DWORD),('dwMaxWanEndPoints', DWORD),('eDeviceType', RASDEVICETYPE),('guidDevice', GUID),('szPortName', CHAR),('szDeviceName', CHAR),('wszDeviceName', WCHAR),
    )
class PRAS_DEVICE_INFO(NDRPOINTER):
    referent = (
        ('Data', RAS_DEVICE_INFO),
    )    


class RAS_CALLEDID_INFO(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('bCalledId', BYTE),
    )
class PRAS_CALLEDID_INFO(NDRPOINTER):
    referent = (
        ('Data', RAS_CALLEDID_INFO),
    )    


class GETSETCALLEDID(NDRSTRUCT):
    structure = (
        ('retcode', DWORD),('fWrite', BOOL),('dwSize', DWORD),('guidDevice', GUID),('rdi', RAS_DEVICE_INFO),('rciInfo', RAS_CALLEDID_INFO),
    )


class RAS_NDISWAN_DRIVER_INFO(NDRSTRUCT):
    structure = (
        ('DriverCaps', ULONG),('Reserved', ULONG),
    )
class P_NDISWAN_DRIVER_INFO(NDRPOINTER):
    referent = (
        ('Data', RAS_NDISWAN_DRIVER_INFO),
    )    


class GETNDISWANDRIVERCAPSSTRUCT(NDRSTRUCT):
    structure = (
        ('retcode', DWORD),('NdiswanDriverInfo', RAS_NDISWAN_DRIVER_INFO),
    )


class GETDEVCONFIGSTRUCT(NDRSTRUCT):
    structure = (
        ('retcode', DWORD),('devicetype', CHAR),('size', DWORD),('config', BYTE),
    )


class ENUM(NDRSTRUCT):
    structure = (
        ('retcode', DWORD),('size', DWORD),('entries', DWORD),('buffer', BYTE),
    )


class RASMAN_PORT_32(NDRSTRUCT):
    structure = (
        ('P_Port', DWORD),('P_PortName', CHAR),('P_Status', RASMAN_STATUS),('P_rdtDeviceType', RASDEVICETYPE),('P_ConfiguredUsage', RASMAN_USAGE),('P_CurrentUsage', RASMAN_USAGE),('P_MediaName', CHAR),('P_DeviceType', CHAR),('P_DeviceName', CHAR),('P_LineDeviceId', DWORD),('P_AddressId', DWORD),
    )


class RASMAN_INFO(NDRSTRUCT):
    structure = (
        ('RI_PortStatus', RASMAN_STATUS),('RI_ConnState', RASMAN_STATE),('RI_LinkSpeed', DWORD),('RI_LastError', DWORD),('RI_CurrentUsage', RASMAN_USAGE),('RI_DeviceTypeConnecting', CHAR),('RI_DeviceConnecting', CHAR),('RI_szDeviceType', CHAR),('RI_szDeviceName', CHAR),('RI_szPortName', CHAR),('RI_DisconnectType', RASMAN_DISCONNECT_TYPE),('RI_OwnershipFlag', DWORD),('RI_ConnectDuration', DWORD),('RI_BytesReceived', DWORD),('RI_Phonebook', CHAR),('RI_PhoneEntry', CHAR),('RI_ConnectionHandle', HANDLE),('RI_SubEntry', DWORD),('RI_rdtDeviceType', RASDEVICETYPE),('RI_GuidEntry', GUID),('RI_dwSessionId', DWORD),('RI_dwFlags', DWORD),('RI_CorrelationGuid', GUID),
    )


class U0(NDRUNION):
    union = {
        1: ('retcode',DWORD),2: ('paddingField',HANDLE),
    }
        

class INFO(NDRSTRUCT):
    structure = (
        ('u0', U0),('info', RASMAN_INFO),
    )


class PNEXT(NDRSTRUCT):
    structure = (
        
    )


class RASRPC_CALLBACKLIST(NDRSTRUCT):
    structure = (
        ('pszPortName', WCHAR),('pszDeviceName', WCHAR),('pszNumber', WCHAR),('dwDeviceType', DWORD),('PNEXT', PNEXT),
    )
class LPRASRPC_CALLBACKLIST(NDRPOINTER):
    referent = (
        ('Data', RASRPC_CALLBACKLIST),
    )    


class PNEXT(NDRSTRUCT):
    structure = (
        
    )


class RASRPC_STRINGLIST(NDRSTRUCT):
    structure = (
        ('psz', WCHAR),('PNEXT', PNEXT),
    )
class LPRASRPC_STRINGLIST(NDRPOINTER):
    referent = (
        ('Data', RASRPC_STRINGLIST),
    )    


class PNEXT(NDRSTRUCT):
    structure = (
        
    )


class RASRPC_LOCATIONLIST(NDRSTRUCT):
    structure = (
        ('dwLocationId', DWORD),('iPrefix', DWORD),('iSuffix', DWORD),('PNEXT', PNEXT),
    )
class LPRASRPC_LOCATIONLIST(NDRPOINTER):
    referent = (
        ('Data', RASRPC_LOCATIONLIST),
    )    


class RASRPC_PBUSER(NDRSTRUCT):
    structure = (
        ('fOperatorDial', BOOL),('fPreviewPhoneNumber', BOOL),('fUseLocation', BOOL),('fShowLights', BOOL),('fShowConnectStatus', BOOL),('fCloseOnDial', BOOL),('fAllowLogonPhonebookEdits', BOOL),('fAllowLogonLocationEdits', BOOL),('fSkipConnectComplete', BOOL),('fNewEntryWizard', BOOL),('dwRedialAttempts', DWORD),('dwRedialSeconds', DWORD),('dwIdleDisconnectSeconds', DWORD),('fRedialOnLinkFailure', BOOL),('fPopupOnTopWhenRedialing', BOOL),('fExpandAutoDialQuery', BOOL),('dwCallbackMode', DWORD),('pCallbacks', LPRASRPC_CALLBACKLIST),('pszLastCallbackByCaller', WCHAR),('dwPhonebookMode', DWORD),('pszPersonalFile', WCHAR),('pszAlternatePath', WCHAR),('pPhonebooks', LPRASRPC_STRINGLIST),('pAreaCodes', LPRASRPC_STRINGLIST),('fUseAreaAndCountry', BOOL),('pPrefixes', LPRASRPC_STRINGLIST),('pSuffixes', LPRASRPC_STRINGLIST),('pLocations', LPRASRPC_LOCATIONLIST),('dwXPhonebook', DWORD),('dwYPhonebook', DWORD),('pszDefaultEntry', WCHAR),('fInitialized', BOOL),('fDirty', BOOL),
    )
class LPRASRPC_PBUSER(NDRPOINTER):
    referent = (
        ('Data', RASRPC_PBUSER),
    )    

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#dimsvc Definition

#################################################################################

MSRPC_UUID_DIMSVC = uuidtup_to_bin(('8f09f000-b7ed-11ce-bbd2-00001a181cad','0.0'))


class RMprAdminServerGetInfo(NDRCALL):
    opnum = 0
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
    )

class RMprAdminServerGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRasAdminConnectionEnum(NDRCALL):
    opnum = 1
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('dwPreferedMaximumLength', DWORD),
		('lpdwResumeHandle', LPDWORD),
    )

class RRasAdminConnectionEnumResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('lpdwEntriesRead', LPDWORD),
		('lpdwTotalEntries', LPDWORD),
		('lpdwResumeHandle', LPDWORD),
    )
        

class RRasAdminConnectionGetInfo(NDRCALL):
    opnum = 2
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('hDimConnection', DWORD),
    )

class RRasAdminConnectionGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRasAdminConnectionClearStats(NDRCALL):
    opnum = 3
    structure = (
		('hDimServer', DIM_HANDLE),
		('hDimConnection', DWORD),
    )

class RRasAdminConnectionClearStatsResponse(NDRCALL):
    structure = (

    )
        

class RRasAdminPortEnum(NDRCALL):
    opnum = 4
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('hRasConnection', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('dwPreferedMaximumLength', DWORD),
		('lpdwResumeHandle', LPDWORD),
    )

class RRasAdminPortEnumResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('lpdwEntriesRead', LPDWORD),
		('lpdwTotalEntries', LPDWORD),
		('lpdwResumeHandle', LPDWORD),
    )
        

class RRasAdminPortGetInfo(NDRCALL):
    opnum = 5
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('hPort', DWORD),
    )

class RRasAdminPortGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRasAdminPortClearStats(NDRCALL):
    opnum = 6
    structure = (
		('hDimServer', DIM_HANDLE),
		('hPort', DWORD),
    )

class RRasAdminPortClearStatsResponse(NDRCALL):
    structure = (

    )
        

class RRasAdminPortReset(NDRCALL):
    opnum = 7
    structure = (
		('hDimServer', DIM_HANDLE),
		('hPort', DWORD),
    )

class RRasAdminPortResetResponse(NDRCALL):
    structure = (

    )
        

class RRasAdminPortDisconnect(NDRCALL):
    opnum = 8
    structure = (
		('hDimServer', DIM_HANDLE),
		('hPort', DWORD),
    )

class RRasAdminPortDisconnectResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceTransportSetGlobalInfo(NDRCALL):
    opnum = 9
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwTransportId', DWORD),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )

class RRouterInterfaceTransportSetGlobalInfoResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceTransportGetGlobalInfo(NDRCALL):
    opnum = 10
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwTransportId', DWORD),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )

class RRouterInterfaceTransportGetGlobalInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )
        

class RRouterInterfaceGetHandle(NDRCALL):
    opnum = 11
    structure = (
		('hDimServer', DIM_HANDLE),
		('lpwsInterfaceName', LPWSTR),
		('phInterface', LPDWORD),
		('fIncludeClientInterfaces', DWORD),
    )

class RRouterInterfaceGetHandleResponse(NDRCALL):
    structure = (
		('phInterface', LPDWORD),
    )
        

class RRouterInterfaceCreate(NDRCALL):
    opnum = 12
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('phInterface', LPDWORD),
    )

class RRouterInterfaceCreateResponse(NDRCALL):
    structure = (
		('phInterface', LPDWORD),
    )
        

class RRouterInterfaceGetInfo(NDRCALL):
    opnum = 13
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('hInterface', DWORD),
    )

class RRouterInterfaceGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRouterInterfaceSetInfo(NDRCALL):
    opnum = 14
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('hInterface', DWORD),
    )

class RRouterInterfaceSetInfoResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceDelete(NDRCALL):
    opnum = 15
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
    )

class RRouterInterfaceDeleteResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceTransportRemove(NDRCALL):
    opnum = 16
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
    )

class RRouterInterfaceTransportRemoveResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceTransportAdd(NDRCALL):
    opnum = 17
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )

class RRouterInterfaceTransportAddResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceTransportGetInfo(NDRCALL):
    opnum = 18
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )

class RRouterInterfaceTransportGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )
        

class RRouterInterfaceTransportSetInfo(NDRCALL):
    opnum = 19
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
    )

class RRouterInterfaceTransportSetInfoResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceEnum(NDRCALL):
    opnum = 20
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('dwPreferedMaximumLength', DWORD),
		('lpdwResumeHandle', LPDWORD),
    )

class RRouterInterfaceEnumResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('lpdwEntriesRead', LPDWORD),
		('lpdwTotalEntries', LPDWORD),
		('lpdwResumeHandle', LPDWORD),
    )
        

class RRouterInterfaceConnect(NDRCALL):
    opnum = 21
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('hEvent', ULONG_PTR),
		('fBlocking', DWORD),
		('dwCallersProcessId', DWORD),
    )

class RRouterInterfaceConnectResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceDisconnect(NDRCALL):
    opnum = 22
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
    )

class RRouterInterfaceDisconnectResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceUpdateRoutes(NDRCALL):
    opnum = 23
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
		('hEvent', ULONG_PTR),
		('dwClientProcessId', DWORD),
    )

class RRouterInterfaceUpdateRoutesResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceQueryUpdateResult(NDRCALL):
    opnum = 24
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('dwTransportId', DWORD),
    )

class RRouterInterfaceQueryUpdateResultResponse(NDRCALL):
    structure = (
		('pUpdateResult', LPDWORD),
    )
        

class RRouterInterfaceUpdatePhonebookInfo(NDRCALL):
    opnum = 25
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
    )

class RRouterInterfaceUpdatePhonebookInfoResponse(NDRCALL):
    structure = (

    )
        

class RMIBEntryCreate(NDRCALL):
    opnum = 26
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntryCreateResponse(NDRCALL):
    structure = (

    )
        

class RMIBEntryDelete(NDRCALL):
    opnum = 27
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntryDeleteResponse(NDRCALL):
    structure = (

    )
        

class RMIBEntrySet(NDRCALL):
    opnum = 28
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntrySetResponse(NDRCALL):
    structure = (

    )
        

class RMIBEntryGet(NDRCALL):
    opnum = 29
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntryGetResponse(NDRCALL):
    structure = (
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )
        

class RMIBEntryGetFirst(NDRCALL):
    opnum = 30
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntryGetFirstResponse(NDRCALL):
    structure = (
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )
        

class RMIBEntryGetNext(NDRCALL):
    opnum = 31
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBEntryGetNextResponse(NDRCALL):
    structure = (
		('pInfoStuct', PDIM_MIB_ENTRY_CONTAINER),
    )
        

class RMIBGetTrapInfo(NDRCALL):
    opnum = 32
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('pInfoStruct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBGetTrapInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_MIB_ENTRY_CONTAINER),
    )
        

class RMIBSetTrapInfo(NDRCALL):
    opnum = 33
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwPid', DWORD),
		('dwRoutingPid', DWORD),
		('hEvent', ULONG_PTR),
		('dwClientProcessId', DWORD),
		('pInfoStruct', PDIM_MIB_ENTRY_CONTAINER),
    )

class RMIBSetTrapInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_MIB_ENTRY_CONTAINER),
    )
        

class RRasAdminConnectionNotification(NDRCALL):
    opnum = 34
    structure = (
		('hDimServer', DIM_HANDLE),
		('fRegister', DWORD),
		('dwClientProcessId', DWORD),
		('hEventNotification', ULONG_PTR),
    )

class RRasAdminConnectionNotificationResponse(NDRCALL):
    structure = (

    )
        

class RRasAdminSendUserMessage(NDRCALL):
    opnum = 35
    structure = (
		('hDimServer', DIM_HANDLE),
		('hDimConnection', DWORD),
		('lpwszMessage', LPWSTR),
    )

class RRasAdminSendUserMessageResponse(NDRCALL):
    structure = (

    )
        

class RRouterDeviceEnum(NDRCALL):
    opnum = 36
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('lpdwTotalEntries', LPDWORD),
    )

class RRouterDeviceEnumResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('lpdwTotalEntries', LPDWORD),
    )
        

class RRouterInterfaceTransportCreate(NDRCALL):
    opnum = 37
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwTransportId', DWORD),
		('lpwsTransportName', LPWSTR),
		('pInfoStruct', PDIM_INTERFACE_CONTAINER),
		('lpwsDLLPath', LPWSTR),
    )

class RRouterInterfaceTransportCreateResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceDeviceGetInfo(NDRCALL):
    opnum = 38
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('dwIndex', DWORD),
		('hInterface', DWORD),
    )

class RRouterInterfaceDeviceGetInfoResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRouterInterfaceDeviceSetInfo(NDRCALL):
    opnum = 39
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('dwIndex', DWORD),
		('hInterface', DWORD),
    )

class RRouterInterfaceDeviceSetInfoResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceSetCredentialsEx(NDRCALL):
    opnum = 40
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('hInterface', DWORD),
    )

class RRouterInterfaceSetCredentialsExResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceGetCredentialsEx(NDRCALL):
    opnum = 41
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
		('hInterface', DWORD),
    )

class RRouterInterfaceGetCredentialsExResponse(NDRCALL):
    structure = (
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )
        

class RRasAdminConnectionRemoveQuarantine(NDRCALL):
    opnum = 42
    structure = (
		('hDimServer', DIM_HANDLE),
		('hRasConnection', DWORD),
		('fIsIpAddress', BOOL),
    )

class RRasAdminConnectionRemoveQuarantineResponse(NDRCALL):
    structure = (

    )
        

class RMprAdminServerSetInfo(NDRCALL):
    opnum = 43
    structure = (
		('hDimServer', DIM_HANDLE),
		('dwLevel', DWORD),
		('pInfoStruct', PDIM_INFORMATION_CONTAINER),
    )

class RMprAdminServerSetInfoResponse(NDRCALL):
    structure = (

    )
        

class RMprAdminServerGetInfoEx(NDRCALL):
    opnum = 44
    structure = (
		('hDimServer', DIM_HANDLE),
		('pServerConfig', PMPR_SERVER_EX_IDL),
    )

class RMprAdminServerGetInfoExResponse(NDRCALL):
    structure = (
		('pServerConfig', PMPR_SERVER_EX_IDL),
    )
        

class RRasAdminConnectionEnumEx(NDRCALL):
    opnum = 45
    structure = (
		('hDimServer', DIM_HANDLE),
		('objectHeader', PMPRAPI_OBJECT_HEADER_IDL),
		('dwPreferedMaxLen', DWORD),
		('lpdwResumeHandle', LPDWORD),
    )

class RRasAdminConnectionEnumExResponse(NDRCALL):
    structure = (
		('lpdwEntriesRead', LPDWORD),
		('lpdNumTotalElements', LPDWORD),
		('pRasConections', PRAS_CONNECTION_EX_IDL),
		('lpdwResumeHandle', LPDWORD),
    )
        

class RRasAdminConnectionGetInfoEx(NDRCALL):
    opnum = 46
    structure = (
		('hDimServer', DIM_HANDLE),
		('hDimConnection', DWORD),
		('objectHeader', PMPRAPI_OBJECT_HEADER_IDL),
    )

class RRasAdminConnectionGetInfoExResponse(NDRCALL):
    structure = (
		('pRasConnection', PRAS_CONNECTION_EX_IDL),
    )
        

class RMprAdminServerSetInfoEx(NDRCALL):
    opnum = 47
    structure = (
		('hDimServer', DIM_HANDLE),
		('pServerConfig', PMPR_SERVER_SET_CONFIG_EX_IDL),
    )

class RMprAdminServerSetInfoExResponse(NDRCALL):
    structure = (

    )
        

class RRasAdminUpdateConnection(NDRCALL):
    opnum = 48
    structure = (
		('hDimServer', DIM_HANDLE),
		('hDimConnection', DWORD),
		('pServerConfig', PRAS_UPDATE_CONNECTION_IDL),
    )

class RRasAdminUpdateConnectionResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceSetCredentialsLocal(NDRCALL):
    opnum = 49
    structure = (
		('hDimServer', DIM_HANDLE),
		('lpwsInterfaceName', LPWSTR),
		('lpwsUserName', LPWSTR),
		('lpwsDomainName', LPWSTR),
		('lpwsPassword', LPWSTR),
    )

class RRouterInterfaceSetCredentialsLocalResponse(NDRCALL):
    structure = (

    )
        

class RRouterInterfaceGetCredentialsLocal(NDRCALL):
    opnum = 50
    structure = (
		('hDimServer', DIM_HANDLE),
		('lpwsInterfaceName', LPWSTR),
    )

class RRouterInterfaceGetCredentialsLocalResponse(NDRCALL):
    structure = (
		('lpwsUserName', LPWSTR),
		('lpwsDomainName', LPWSTR),
		('lpwsPassword', LPWSTR),
    )
        

class RRouterInterfaceGetCustomInfoEx(NDRCALL):
    opnum = 51
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('pIfCustomConfig', PMPR_IF_CUSTOMINFOEX_IDL),
    )

class RRouterInterfaceGetCustomInfoExResponse(NDRCALL):
    structure = (
		('pIfCustomConfig', PMPR_IF_CUSTOMINFOEX_IDL),
    )
        

class RRouterInterfaceSetCustomInfoEx(NDRCALL):
    opnum = 52
    structure = (
		('hDimServer', DIM_HANDLE),
		('hInterface', DWORD),
		('pIfCustomConfig', PMPR_IF_CUSTOMINFOEX_IDL),
    )

class RRouterInterfaceSetCustomInfoExResponse(NDRCALL):
    structure = (
		('pIfCustomConfig', PMPR_IF_CUSTOMINFOEX_IDL),
    )
        
OPNUMS = {
0 : (RMprAdminServerGetInfo,RMprAdminServerGetInfoResponse),
1 : (RRasAdminConnectionEnum,RRasAdminConnectionEnumResponse),
2 : (RRasAdminConnectionGetInfo,RRasAdminConnectionGetInfoResponse),
3 : (RRasAdminConnectionClearStats,RRasAdminConnectionClearStatsResponse),
4 : (RRasAdminPortEnum,RRasAdminPortEnumResponse),
5 : (RRasAdminPortGetInfo,RRasAdminPortGetInfoResponse),
6 : (RRasAdminPortClearStats,RRasAdminPortClearStatsResponse),
7 : (RRasAdminPortReset,RRasAdminPortResetResponse),
8 : (RRasAdminPortDisconnect,RRasAdminPortDisconnectResponse),
9 : (RRouterInterfaceTransportSetGlobalInfo,RRouterInterfaceTransportSetGlobalInfoResponse),
10 : (RRouterInterfaceTransportGetGlobalInfo,RRouterInterfaceTransportGetGlobalInfoResponse),
11 : (RRouterInterfaceGetHandle,RRouterInterfaceGetHandleResponse),
12 : (RRouterInterfaceCreate,RRouterInterfaceCreateResponse),
13 : (RRouterInterfaceGetInfo,RRouterInterfaceGetInfoResponse),
14 : (RRouterInterfaceSetInfo,RRouterInterfaceSetInfoResponse),
15 : (RRouterInterfaceDelete,RRouterInterfaceDeleteResponse),
16 : (RRouterInterfaceTransportRemove,RRouterInterfaceTransportRemoveResponse),
17 : (RRouterInterfaceTransportAdd,RRouterInterfaceTransportAddResponse),
18 : (RRouterInterfaceTransportGetInfo,RRouterInterfaceTransportGetInfoResponse),
19 : (RRouterInterfaceTransportSetInfo,RRouterInterfaceTransportSetInfoResponse),
20 : (RRouterInterfaceEnum,RRouterInterfaceEnumResponse),
21 : (RRouterInterfaceConnect,RRouterInterfaceConnectResponse),
22 : (RRouterInterfaceDisconnect,RRouterInterfaceDisconnectResponse),
23 : (RRouterInterfaceUpdateRoutes,RRouterInterfaceUpdateRoutesResponse),
24 : (RRouterInterfaceQueryUpdateResult,RRouterInterfaceQueryUpdateResultResponse),
25 : (RRouterInterfaceUpdatePhonebookInfo,RRouterInterfaceUpdatePhonebookInfoResponse),
26 : (RMIBEntryCreate,RMIBEntryCreateResponse),
27 : (RMIBEntryDelete,RMIBEntryDeleteResponse),
28 : (RMIBEntrySet,RMIBEntrySetResponse),
29 : (RMIBEntryGet,RMIBEntryGetResponse),
30 : (RMIBEntryGetFirst,RMIBEntryGetFirstResponse),
31 : (RMIBEntryGetNext,RMIBEntryGetNextResponse),
32 : (RMIBGetTrapInfo,RMIBGetTrapInfoResponse),
33 : (RMIBSetTrapInfo,RMIBSetTrapInfoResponse),
34 : (RRasAdminConnectionNotification,RRasAdminConnectionNotificationResponse),
35 : (RRasAdminSendUserMessage,RRasAdminSendUserMessageResponse),
36 : (RRouterDeviceEnum,RRouterDeviceEnumResponse),
37 : (RRouterInterfaceTransportCreate,RRouterInterfaceTransportCreateResponse),
38 : (RRouterInterfaceDeviceGetInfo,RRouterInterfaceDeviceGetInfoResponse),
39 : (RRouterInterfaceDeviceSetInfo,RRouterInterfaceDeviceSetInfoResponse),
40 : (RRouterInterfaceSetCredentialsEx,RRouterInterfaceSetCredentialsExResponse),
41 : (RRouterInterfaceGetCredentialsEx,RRouterInterfaceGetCredentialsExResponse),
42 : (RRasAdminConnectionRemoveQuarantine,RRasAdminConnectionRemoveQuarantineResponse),
43 : (RMprAdminServerSetInfo,RMprAdminServerSetInfoResponse),
44 : (RMprAdminServerGetInfoEx,RMprAdminServerGetInfoExResponse),
45 : (RRasAdminConnectionEnumEx,RRasAdminConnectionEnumExResponse),
46 : (RRasAdminConnectionGetInfoEx,RRasAdminConnectionGetInfoExResponse),
47 : (RMprAdminServerSetInfoEx,RMprAdminServerSetInfoExResponse),
48 : (RRasAdminUpdateConnection,RRasAdminUpdateConnectionResponse),
49 : (RRouterInterfaceSetCredentialsLocal,RRouterInterfaceSetCredentialsLocalResponse),
50 : (RRouterInterfaceGetCredentialsLocal,RRouterInterfaceGetCredentialsLocalResponse),
51 : (RRouterInterfaceGetCustomInfoEx,RRouterInterfaceGetCustomInfoExResponse),
52 : (RRouterInterfaceSetCustomInfoEx,RRouterInterfaceSetCustomInfoExResponse),
}

#################################################################################

#rasrpc Definition

#################################################################################

MSRPC_UUID_RASRPC = uuidtup_to_bin(('20610036-fa22-11cf-9823-00a0c911e5df','0.0'))


class Opnum0NotUsedOnWire(NDRCALL):
    opnum = 0
    structure = (

    )

class Opnum0NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum2NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum2NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum3NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum3NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RasRpcDeleteEntry(NDRCALL):
    opnum = 5
    structure = (
		('h', HANDLE_T),
		('lpszPhonebook', LPWSTR),
		('lpszEntry', LPWSTR),
    )

class RasRpcDeleteEntryResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum7NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum7NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum8NotUsedOnWire(NDRCALL):
    opnum = 8
    structure = (

    )

class Opnum8NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RasRpcGetUserPreferences(NDRCALL):
    opnum = 9
    structure = (
		('h', HANDLE_T),
		('pUser', LPRASRPC_PBUSER),
		('dwMode', DWORD),
    )

class RasRpcGetUserPreferencesResponse(NDRCALL):
    structure = (
		('pUser', LPRASRPC_PBUSER),
    )
        

class RasRpcSetUserPreferences(NDRCALL):
    opnum = 10
    structure = (
		('h', HANDLE_T),
		('pUser', LPRASRPC_PBUSER),
		('dwMode', DWORD),
    )

class RasRpcSetUserPreferencesResponse(NDRCALL):
    structure = (

    )
        

class RasRpcGetSystemDirectory(NDRCALL):
    opnum = 11
    structure = (
		('h', HANDLE_T),
		('lpBuffer', LPWSTR),
		('uSize', UINT),
    )

class RasRpcGetSystemDirectoryResponse(NDRCALL):
    structure = (
		('lpBuffer', LPWSTR),
    )
        

class RasRpcSubmitRequest(NDRCALL):
    opnum = 12
    structure = (
		('h', HANDLE_T),
		('pReqBuffer', PBYTE),
		('dwcbBufSize', DWORD),
    )

class RasRpcSubmitRequestResponse(NDRCALL):
    structure = (
		('pReqBuffer', PBYTE),
    )
        

class Opnum13NotUsedOnWire(NDRCALL):
    opnum = 13
    structure = (

    )

class Opnum13NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RasRpcGetInstalledProtocolsEx(NDRCALL):
    opnum = 14
    structure = (
		('h', HANDLE_T),
		('fRouter', BOOL),
		('fRasCli', BOOL),
		('fRasSrv', BOOL),
    )

class RasRpcGetInstalledProtocolsExResponse(NDRCALL):
    structure = (

    )
        

class RasRpcGetVersion(NDRCALL):
    opnum = 15
    structure = (
		('h', HANDLE_T),
		('pdwVersion', LPDWORD),
    )

class RasRpcGetVersionResponse(NDRCALL):
    structure = (
		('pdwVersion', LPDWORD),
    )
        

class Opnum16NotUsedOnWire(NDRCALL):
    opnum = 16
    structure = (

    )

class Opnum16NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Opnum0NotUsedOnWire,Opnum0NotUsedOnWireResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (Opnum2NotUsedOnWire,Opnum2NotUsedOnWireResponse),
3 : (Opnum3NotUsedOnWire,Opnum3NotUsedOnWireResponse),
4 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
5 : (RasRpcDeleteEntry,RasRpcDeleteEntryResponse),
6 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
7 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
8 : (Opnum8NotUsedOnWire,Opnum8NotUsedOnWireResponse),
9 : (RasRpcGetUserPreferences,RasRpcGetUserPreferencesResponse),
10 : (RasRpcSetUserPreferences,RasRpcSetUserPreferencesResponse),
11 : (RasRpcGetSystemDirectory,RasRpcGetSystemDirectoryResponse),
12 : (RasRpcSubmitRequest,RasRpcSubmitRequestResponse),
13 : (Opnum13NotUsedOnWire,Opnum13NotUsedOnWireResponse),
14 : (RasRpcGetInstalledProtocolsEx,RasRpcGetInstalledProtocolsExResponse),
15 : (RasRpcGetVersion,RasRpcGetVersionResponse),
16 : (Opnum16NotUsedOnWire,Opnum16NotUsedOnWireResponse),
}

#################################################################################

#IRemoteNetworkConfig Definition

#################################################################################

MSRPC_UUID_IREMOTENETWORKCONFIG = uuidtup_to_bin(('66a2db1b-d706-11d0-a37b-00c04fc9da04','0.0'))


class UpgradeRouterConfig(NDRCALL):
    opnum = 0
    structure = (

    )

class UpgradeRouterConfigResponse(NDRCALL):
    structure = (

    )
        

class SetUserConfig(NDRCALL):
    opnum = 1
    structure = (
		('pszService', LPCOLESTR),
		('pszNewGroup', LPCOLESTR),
    )

class SetUserConfigResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (UpgradeRouterConfig,UpgradeRouterConfigResponse),
1 : (SetUserConfig,SetUserConfigResponse),
}

#################################################################################

#IRemoteRouterRestart Definition

#################################################################################

MSRPC_UUID_IREMOTEROUTERRESTART = uuidtup_to_bin(('66a2db20-d706-11d0-a37b-00c04fc9da04','0.0'))


class RestartRouter(NDRCALL):
    opnum = 0
    structure = (
		('dwFlags', DWORD),
    )

class RestartRouterResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RestartRouter,RestartRouterResponse),
}

#################################################################################

#IRemoteSetDnsConfig Definition

#################################################################################

MSRPC_UUID_IREMOTESETDNSCONFIG = uuidtup_to_bin(('66a2db21-d706-11d0-a37b-00c04fc9da04','0.0'))


class SetDnsConfig(NDRCALL):
    opnum = 0
    structure = (
		('dwConfigId', DWORD),
		('dwNewValue', DWORD),
    )

class SetDnsConfigResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SetDnsConfig,SetDnsConfigResponse),
}

#################################################################################

#IRemoteICFICSConfig Definition

#################################################################################

MSRPC_UUID_IREMOTEICFICSCONFIG = uuidtup_to_bin(('66a2db22-d706-11d0-a37b-00c04fc9da04','0.0'))


class GetIcfEnabled(NDRCALL):
    opnum = 0
    structure = (

    )

class GetIcfEnabledResponse(NDRCALL):
    structure = (
		('status', BOOL),
    )
        

class GetIcsEnabled(NDRCALL):
    opnum = 1
    structure = (

    )

class GetIcsEnabledResponse(NDRCALL):
    structure = (
		('status', BOOL),
    )
        
OPNUMS = {
0 : (GetIcfEnabled,GetIcfEnabledResponse),
1 : (GetIcsEnabled,GetIcsEnabledResponse),
}

#################################################################################

#IRemoteStringIdConfig Definition

#################################################################################

MSRPC_UUID_IREMOTESTRINGIDCONFIG = uuidtup_to_bin(('67e08fc2-2984-4b62-b92e-fc1aae64bbbb','0.0'))


class GetStringFromId(NDRCALL):
    opnum = 0
    structure = (
		('stringId', UINT),
    )

class GetStringFromIdResponse(NDRCALL):
    structure = (
		('pBstrName', BSTR),
    )
        
OPNUMS = {
0 : (GetStringFromId,GetStringFromIdResponse),
}

#################################################################################

#IRemoteIPV6Config Definition

#################################################################################

MSRPC_UUID_IREMOTEIPV6CONFIG = uuidtup_to_bin(('6139d8a4-e508-4ebb-bac7-d7f275145897','0.0'))


class IPV6ADDRESS(NDRSTRUCT):
    structure = (
        ('bytes', UNSIGNED_CHAR),
    )


class GetAddressList(NDRCALL):
    opnum = 0
    structure = (
		('pszInterfaceName', WCHAR_T),
		('dwIfIndex', DWORD),
    )

class GetAddressListResponse(NDRCALL):
    structure = (
		('pdwNumAddresses', DWORD),
		('ppIPV6AddressList', IPV6ADDRESS),
    )
        
OPNUMS = {
0 : (GetAddressList,GetAddressListResponse),
}

#################################################################################

#IRemoteSstpCertCheck Definition

#################################################################################

MSRPC_UUID_IREMOTESSTPCERTCHECK = uuidtup_to_bin(('5ff9bdf6-bd91-4d8b-a614-d6317acc8dd8','0.0'))


class CheckIfCertificateAllowedRR(NDRCALL):
    opnum = 0
    structure = (
		('adminCertName', PCWSTR),
		('certSha1', PSSTP_CERT_INFO_1),
		('certSha256', PSSTP_CERT_INFO_1),
    )

class CheckIfCertificateAllowedRRResponse(NDRCALL):
    structure = (
		('certSha1', PSSTP_CERT_INFO_1),
		('certSha256', PSSTP_CERT_INFO_1),
    )
        
OPNUMS = {
0 : (CheckIfCertificateAllowedRR,CheckIfCertificateAllowedRRResponse),
}

