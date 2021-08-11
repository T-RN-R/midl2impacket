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
        

class ANONYMOUS2(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous2', ANONYMOUS2),
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

#################################################################################

#CONSTANTS

#################################################################################

IAPPHOSTMETHOD = 
IAPPHOSTMETHODINSTANCE = 
IAPPHOSTELEMENT = 
IAPPHOSTPROPERTY = 
IAPPHOSTCONFIGLOCATION = 
IAPPHOSTELEMENTSCHEMA = 
IAPPHOSTPROPERTYSCHEMA = 
IAPPHOSTCONSTANTVALUE = 
IAPPHOSTCONFIGMANAGER = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IAppHostMappingExtension Definition

#################################################################################

MSRPC_UUID_IAPPHOSTMAPPINGEXTENSION = uuidtup_to_bin(('31a83ea0-c0e4-4a2c-8a01-353cc2a4c60a','0.0'))


class GetSiteNameFromSiteId(NDRCALL):
    opnum = 0
    structure = (
		('dwSiteId', DWORD),
    )

class GetSiteNameFromSiteIdResponse(NDRCALL):
    structure = (
		('pbstrSiteName', BSTR),
    )
        

class GetSiteIdFromSiteName(NDRCALL):
    opnum = 1
    structure = (
		('bstrSiteName', BSTR),
    )

class GetSiteIdFromSiteNameResponse(NDRCALL):
    structure = (
		('pdwSiteId', DWORD),
    )
        

class GetSiteElementFromSiteId(NDRCALL):
    opnum = 2
    structure = (
		('dwSiteId', DWORD),
    )

class GetSiteElementFromSiteIdResponse(NDRCALL):
    structure = (
		('ppSiteElement', IAPPHOSTELEMENT),
    )
        

class MapPath(NDRCALL):
    opnum = 3
    structure = (
		('bstrSiteName', BSTR),
		('bstrVirtualPath', BSTR),
    )

class MapPathResponse(NDRCALL):
    structure = (
		('pbstrPhysicalPath', BSTR),
		('ppVirtualDirectoryElement', IAPPHOSTELEMENT),
		('ppApplicationElement', IAPPHOSTELEMENT),
    )
        
OPNUMS = {
0 : (GetSiteNameFromSiteId,GetSiteNameFromSiteIdResponse),
1 : (GetSiteIdFromSiteName,GetSiteIdFromSiteNameResponse),
2 : (GetSiteElementFromSiteId,GetSiteElementFromSiteIdResponse),
3 : (MapPath,MapPathResponse),
}

#################################################################################

#IAppHostChildElementCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCHILDELEMENTCOLLECTION = uuidtup_to_bin(('08a90f5f-0702-48d6-b45f-02a9885a9768','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppElement', IAPPHOSTELEMENT),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostPropertyCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPROPERTYCOLLECTION = uuidtup_to_bin(('0191775e-bcff-445a-b4f4-3bdda54e2816','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppProperty', IAPPHOSTPROPERTY),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostConfigLocationCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONFIGLOCATIONCOLLECTION = uuidtup_to_bin(('832a32f7-b3ea-4b8c-b260-9a2923001184','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('varIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppLocation', IAPPHOSTCONFIGLOCATION),
    )
        

class AddLocation(NDRCALL):
    opnum = 2
    structure = (
		('bstrLocationPath', BSTR),
    )

class AddLocationResponse(NDRCALL):
    structure = (
		('ppNewLocation', IAPPHOSTCONFIGLOCATION),
    )
        

class DeleteLocation(NDRCALL):
    opnum = 3
    structure = (
		('cIndex', VARIANT),
    )

class DeleteLocationResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (AddLocation,AddLocationResponse),
3 : (DeleteLocation,DeleteLocationResponse),
}

#################################################################################

#IAppHostMethodCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTMETHODCOLLECTION = uuidtup_to_bin(('d6c7cd8f-bb8d-496-b591-d3a5f1320269','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppMethod', IAPPHOSTMETHOD),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostElementSchemaCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTELEMENTSCHEMACOLLECTION = uuidtup_to_bin(('0344cdda-151e-4cbf-82da-66ae61e97754','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppElementSchema', IAPPHOSTELEMENTSCHEMA),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostPropertySchemaCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPROPERTYSCHEMACOLLECTION = uuidtup_to_bin(('8bed2c68-a5fb-4b28-8581-a0dc5267419f','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppPropertySchema', IAPPHOSTPROPERTYSCHEMA),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostConstantValueCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONSTANTVALUECOLLECTION = uuidtup_to_bin(('5b5a68e6-8b9f-45e1-8199-a95ffccdffff','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppConstantValue', IAPPHOSTCONSTANTVALUE),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
}

#################################################################################

#IAppHostConstantValue Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONSTANTVALUE = uuidtup_to_bin(('0716caf8-7d05-4a46-8099-77594be91394','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Value(NDRCALL):
    opnum = 1
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('pdwValue', DWORD),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Value,ValueResponse),
}

#################################################################################

#IAppHostPropertySchema Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPROPERTYSCHEMA = uuidtup_to_bin(('450386db-7409-4667-935e-384dbbee2a9e','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 1
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('pbstrType', BSTR),
    )
        

class DefaultValue(NDRCALL):
    opnum = 2
    structure = (

    )

class DefaultValueResponse(NDRCALL):
    structure = (
		('pDefaultValue', VARIANT),
    )
        

class IsRequired(NDRCALL):
    opnum = 3
    structure = (

    )

class IsRequiredResponse(NDRCALL):
    structure = (
		('pfIsRequired', VARIANT_BOOL),
    )
        

class IsUniqueKey(NDRCALL):
    opnum = 4
    structure = (

    )

class IsUniqueKeyResponse(NDRCALL):
    structure = (
		('pfIsUniqueKey', VARIANT_BOOL),
    )
        

class IsCombinedKey(NDRCALL):
    opnum = 5
    structure = (

    )

class IsCombinedKeyResponse(NDRCALL):
    structure = (
		('pfIsCombinedKey', VARIANT_BOOL),
    )
        

class IsExpanded(NDRCALL):
    opnum = 6
    structure = (

    )

class IsExpandedResponse(NDRCALL):
    structure = (
		('pfIsExpanded', VARIANT_BOOL),
    )
        

class ValidationType(NDRCALL):
    opnum = 7
    structure = (

    )

class ValidationTypeResponse(NDRCALL):
    structure = (
		('pbstrValidationType', BSTR),
    )
        

class ValidationParameter(NDRCALL):
    opnum = 8
    structure = (

    )

class ValidationParameterResponse(NDRCALL):
    structure = (
		('pbstrValidationParameter', BSTR),
    )
        

class GetMetadata(NDRCALL):
    opnum = 9
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class IsCaseSensitive(NDRCALL):
    opnum = 10
    structure = (

    )

class IsCaseSensitiveResponse(NDRCALL):
    structure = (
		('pfIsCaseSensitive', VARIANT_BOOL),
    )
        

class PossibleValues(NDRCALL):
    opnum = 11
    structure = (

    )

class PossibleValuesResponse(NDRCALL):
    structure = (
		('ppValues', IAPPHOSTCONSTANTVALUECOLLECTION),
    )
        

class DoesAllowInfinite(NDRCALL):
    opnum = 12
    structure = (

    )

class DoesAllowInfiniteResponse(NDRCALL):
    structure = (
		('pfAllowInfinite', VARIANT_BOOL),
    )
        

class IsEncrypted(NDRCALL):
    opnum = 13
    structure = (

    )

class IsEncryptedResponse(NDRCALL):
    structure = (
		('pfIsEncrypted', VARIANT_BOOL),
    )
        

class TimeSpanFormat(NDRCALL):
    opnum = 14
    structure = (

    )

class TimeSpanFormatResponse(NDRCALL):
    structure = (
		('pbstrTimeSpanFormat', BSTR),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Type,TypeResponse),
2 : (DefaultValue,DefaultValueResponse),
3 : (IsRequired,IsRequiredResponse),
4 : (IsUniqueKey,IsUniqueKeyResponse),
5 : (IsCombinedKey,IsCombinedKeyResponse),
6 : (IsExpanded,IsExpandedResponse),
7 : (ValidationType,ValidationTypeResponse),
8 : (ValidationParameter,ValidationParameterResponse),
9 : (GetMetadata,GetMetadataResponse),
10 : (IsCaseSensitive,IsCaseSensitiveResponse),
11 : (PossibleValues,PossibleValuesResponse),
12 : (DoesAllowInfinite,DoesAllowInfiniteResponse),
13 : (IsEncrypted,IsEncryptedResponse),
14 : (TimeSpanFormat,TimeSpanFormatResponse),
}

#################################################################################

#IAppHostCollectionSchema Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCOLLECTIONSCHEMA = uuidtup_to_bin(('de095db1-5368-411-816-efef619b7bcf','0.0'))


class AddElementNames(NDRCALL):
    opnum = 0
    structure = (

    )

class AddElementNamesResponse(NDRCALL):
    structure = (
		('pbstrElementName', BSTR),
    )
        

class GetAddElementSchema(NDRCALL):
    opnum = 1
    structure = (
		('bstrElementName', BSTR),
    )

class GetAddElementSchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class RemoveElementSchema(NDRCALL):
    opnum = 2
    structure = (

    )

class RemoveElementSchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class ClearElementSchema(NDRCALL):
    opnum = 3
    structure = (

    )

class ClearElementSchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class IsMergeAppend(NDRCALL):
    opnum = 4
    structure = (

    )

class IsMergeAppendResponse(NDRCALL):
    structure = (
		('pfIsMergeAppend', VARIANT_BOOL),
    )
        

class GetMetadata(NDRCALL):
    opnum = 5
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class DoesAllowDuplicates(NDRCALL):
    opnum = 6
    structure = (

    )

class DoesAllowDuplicatesResponse(NDRCALL):
    structure = (
		('pfAllowDuplicates', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (AddElementNames,AddElementNamesResponse),
1 : (GetAddElementSchema,GetAddElementSchemaResponse),
2 : (RemoveElementSchema,RemoveElementSchemaResponse),
3 : (ClearElementSchema,ClearElementSchemaResponse),
4 : (IsMergeAppend,IsMergeAppendResponse),
5 : (GetMetadata,GetMetadataResponse),
6 : (DoesAllowDuplicates,DoesAllowDuplicatesResponse),
}

#################################################################################

#IAppHostElementSchema Definition

#################################################################################

MSRPC_UUID_IAPPHOSTELEMENTSCHEMA = uuidtup_to_bin(('ef13d885-642-4709-99c-b89561c6bc69','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class DoesAllowUnschematizedProperties(NDRCALL):
    opnum = 1
    structure = (

    )

class DoesAllowUnschematizedPropertiesResponse(NDRCALL):
    structure = (
		('pfAllowUnschematized', VARIANT_BOOL),
    )
        

class GetMetadata(NDRCALL):
    opnum = 2
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class CollectionSchema(NDRCALL):
    opnum = 3
    structure = (

    )

class CollectionSchemaResponse(NDRCALL):
    structure = (
		('ppCollectionSchema', IAPPHOSTCOLLECTIONSCHEMA),
    )
        

class ChildElementSchemas(NDRCALL):
    opnum = 4
    structure = (

    )

class ChildElementSchemasResponse(NDRCALL):
    structure = (
		('ppChildSchemas', IAPPHOSTELEMENTSCHEMACOLLECTION),
    )
        

class PropertySchemas(NDRCALL):
    opnum = 5
    structure = (

    )

class PropertySchemasResponse(NDRCALL):
    structure = (
		('ppPropertySchemas', IAPPHOSTPROPERTYSCHEMACOLLECTION),
    )
        

class IsCollectionDefault(NDRCALL):
    opnum = 6
    structure = (

    )

class IsCollectionDefaultResponse(NDRCALL):
    structure = (
		('pfIsCollectionDefault', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (DoesAllowUnschematizedProperties,DoesAllowUnschematizedPropertiesResponse),
2 : (GetMetadata,GetMetadataResponse),
3 : (CollectionSchema,CollectionSchemaResponse),
4 : (ChildElementSchemas,ChildElementSchemasResponse),
5 : (PropertySchemas,PropertySchemasResponse),
6 : (IsCollectionDefault,IsCollectionDefaultResponse),
}

#################################################################################

#IAppHostMethodSchema Definition

#################################################################################

MSRPC_UUID_IAPPHOSTMETHODSCHEMA = uuidtup_to_bin(('2d9915fb-9d42-4328-b782-1b46819fab9e','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class InputSchema(NDRCALL):
    opnum = 1
    structure = (

    )

class InputSchemaResponse(NDRCALL):
    structure = (
		('ppInputSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class OutputSchema(NDRCALL):
    opnum = 2
    structure = (

    )

class OutputSchemaResponse(NDRCALL):
    structure = (
		('ppOutputSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class GetMetadata(NDRCALL):
    opnum = 3
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (InputSchema,InputSchemaResponse),
2 : (OutputSchema,OutputSchemaResponse),
3 : (GetMetadata,GetMetadataResponse),
}

#################################################################################

#IAppHostMethodInstance Definition

#################################################################################

MSRPC_UUID_IAPPHOSTMETHODINSTANCE = uuidtup_to_bin(('b80f3c42-600-4e0-9007-f52852d3dbed','0.0'))


class Input(NDRCALL):
    opnum = 0
    structure = (

    )

class InputResponse(NDRCALL):
    structure = (
		('ppInputElement', IAPPHOSTELEMENT),
    )
        

class Output(NDRCALL):
    opnum = 1
    structure = (

    )

class OutputResponse(NDRCALL):
    structure = (
		('ppOutputElement', IAPPHOSTELEMENT),
    )
        

class Execute(NDRCALL):
    opnum = 2
    structure = (

    )

class ExecuteResponse(NDRCALL):
    structure = (

    )
        

class GetMetadata(NDRCALL):
    opnum = 3
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class SetMetadata(NDRCALL):
    opnum = 4
    structure = (
		('bstrMetadataType', BSTR),
		('value', VARIANT),
    )

class SetMetadataResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Input,InputResponse),
1 : (Output,OutputResponse),
2 : (Execute,ExecuteResponse),
3 : (GetMetadata,GetMetadataResponse),
4 : (SetMetadata,SetMetadataResponse),
}

#################################################################################

#IAppHostMethod Definition

#################################################################################

MSRPC_UUID_IAPPHOSTMETHOD = uuidtup_to_bin(('7883ca1c-1112-4447-84c3-52fbeb38069d','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Schema(NDRCALL):
    opnum = 1
    structure = (

    )

class SchemaResponse(NDRCALL):
    structure = (
		('ppMethodSchema', IAPPHOSTMETHODSCHEMA),
    )
        

class CreateInstance(NDRCALL):
    opnum = 2
    structure = (

    )

class CreateInstanceResponse(NDRCALL):
    structure = (
		('ppMethodInstance', IAPPHOSTMETHODINSTANCE),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Schema,SchemaResponse),
2 : (CreateInstance,CreateInstanceResponse),
}

#################################################################################

#IAppHostConfigException Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONFIGEXCEPTION = uuidtup_to_bin(('4dfa1df3-8900-4bc7-bbb5-d1a458c52410','0.0'))


class LineNumber(NDRCALL):
    opnum = 0
    structure = (

    )

class LineNumberResponse(NDRCALL):
    structure = (
		('pcLineNumber', UNSIGNED_LONG),
    )
        

class FileName(NDRCALL):
    opnum = 1
    structure = (

    )

class FileNameResponse(NDRCALL):
    structure = (
		('pbstrFileName', BSTR),
    )
        

class ConfigPath(NDRCALL):
    opnum = 2
    structure = (

    )

class ConfigPathResponse(NDRCALL):
    structure = (
		('pbstrConfigPath', BSTR),
    )
        

class ErrorLine(NDRCALL):
    opnum = 3
    structure = (

    )

class ErrorLineResponse(NDRCALL):
    structure = (
		('pbstrErrorLine', BSTR),
    )
        

class PreErrorLine(NDRCALL):
    opnum = 4
    structure = (

    )

class PreErrorLineResponse(NDRCALL):
    structure = (
		('pbstrPreErrorLine', BSTR),
    )
        

class PostErrorLine(NDRCALL):
    opnum = 5
    structure = (

    )

class PostErrorLineResponse(NDRCALL):
    structure = (
		('pbstrPostErrorLine', BSTR),
    )
        

class ErrorString(NDRCALL):
    opnum = 6
    structure = (

    )

class ErrorStringResponse(NDRCALL):
    structure = (
		('pbstrErrorString', BSTR),
    )
        
OPNUMS = {
0 : (LineNumber,LineNumberResponse),
1 : (FileName,FileNameResponse),
2 : (ConfigPath,ConfigPathResponse),
3 : (ErrorLine,ErrorLineResponse),
4 : (PreErrorLine,PreErrorLineResponse),
5 : (PostErrorLine,PostErrorLineResponse),
6 : (ErrorString,ErrorStringResponse),
}

#################################################################################

#IAppHostPropertyException Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPROPERTYEXCEPTION = uuidtup_to_bin(('eafe4895-a929-41a-b14d-613236271','0.0'))


class InvalidValue(NDRCALL):
    opnum = 0
    structure = (

    )

class InvalidValueResponse(NDRCALL):
    structure = (
		('pbstrValue', BSTR),
    )
        

class ValidationFailureReason(NDRCALL):
    opnum = 1
    structure = (

    )

class ValidationFailureReasonResponse(NDRCALL):
    structure = (
		('pbstrValidationReason', BSTR),
    )
        

class ValidationFailureParameters(NDRCALL):
    opnum = 2
    structure = (

    )

class ValidationFailureParametersResponse(NDRCALL):
    structure = (
		('pParameterArray', SAFEARRAY ( VARIANT )),
    )
        
OPNUMS = {
0 : (InvalidValue,InvalidValueResponse),
1 : (ValidationFailureReason,ValidationFailureReasonResponse),
2 : (ValidationFailureParameters,ValidationFailureParametersResponse),
}

#################################################################################

#IAppHostElementCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTELEMENTCOLLECTION = uuidtup_to_bin(('c8550bff-5281-41-ac34-996a38464d','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcElementCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppElement', IAPPHOSTELEMENT),
    )
        

class AddElement(NDRCALL):
    opnum = 2
    structure = (
		('pElement', IAPPHOSTELEMENT),
		('cPosition', INT),
    )

class AddElementResponse(NDRCALL):
    structure = (

    )
        

class DeleteElement(NDRCALL):
    opnum = 3
    structure = (
		('cIndex', VARIANT),
    )

class DeleteElementResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 4
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class CreateNewElement(NDRCALL):
    opnum = 5
    structure = (
		('bstrElementName', BSTR),
    )

class CreateNewElementResponse(NDRCALL):
    structure = (
		('ppElement', IAPPHOSTELEMENT),
    )
        

class Schema(NDRCALL):
    opnum = 6
    structure = (

    )

class SchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTCOLLECTIONSCHEMA),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (AddElement,AddElementResponse),
3 : (DeleteElement,DeleteElementResponse),
4 : (Clear,ClearResponse),
5 : (CreateNewElement,CreateNewElementResponse),
6 : (Schema,SchemaResponse),
}

#################################################################################

#IAppHostElement Definition

#################################################################################

MSRPC_UUID_IAPPHOSTELEMENT = uuidtup_to_bin(('64ff8ccc-b287-4dae-b08a-a72cbf45f453','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Collection(NDRCALL):
    opnum = 1
    structure = (

    )

class CollectionResponse(NDRCALL):
    structure = (
		('ppCollection', IAPPHOSTELEMENTCOLLECTION),
    )
        

class Properties(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppProperties', IAPPHOSTPROPERTYCOLLECTION),
    )
        

class ChildElements(NDRCALL):
    opnum = 3
    structure = (

    )

class ChildElementsResponse(NDRCALL):
    structure = (
		('ppElements', IAPPHOSTCHILDELEMENTCOLLECTION),
    )
        

class GetMetadata(NDRCALL):
    opnum = 4
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class SetMetadata(NDRCALL):
    opnum = 5
    structure = (
		('bstrMetadataType', BSTR),
		('value', VARIANT),
    )

class SetMetadataResponse(NDRCALL):
    structure = (

    )
        

class Schema(NDRCALL):
    opnum = 6
    structure = (

    )

class SchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTELEMENTSCHEMA),
    )
        

class GetElementByName(NDRCALL):
    opnum = 7
    structure = (
		('bstrSubName', BSTR),
    )

class GetElementByNameResponse(NDRCALL):
    structure = (
		('ppElement', IAPPHOSTELEMENT),
    )
        

class GetPropertyByName(NDRCALL):
    opnum = 8
    structure = (
		('bstrSubName', BSTR),
    )

class GetPropertyByNameResponse(NDRCALL):
    structure = (
		('ppProperty', IAPPHOSTPROPERTY),
    )
        

class Clear(NDRCALL):
    opnum = 9
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class Methods(NDRCALL):
    opnum = 10
    structure = (

    )

class MethodsResponse(NDRCALL):
    structure = (
		('ppMethods', IAPPHOSTMETHODCOLLECTION),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Collection,CollectionResponse),
2 : (Properties,PropertiesResponse),
3 : (ChildElements,ChildElementsResponse),
4 : (GetMetadata,GetMetadataResponse),
5 : (SetMetadata,SetMetadataResponse),
6 : (Schema,SchemaResponse),
7 : (GetElementByName,GetElementByNameResponse),
8 : (GetPropertyByName,GetPropertyByNameResponse),
9 : (Clear,ClearResponse),
10 : (Methods,MethodsResponse),
}

#################################################################################

#IAppHostProperty Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPROPERTY = uuidtup_to_bin(('ed35f7a1-5024-47-a44d-07daf4b524d','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Value(NDRCALL):
    opnum = 1
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('pVariant', VARIANT),
    )
        

class Value(NDRCALL):
    opnum = 2
    structure = (
		('value', VARIANT),
    )

class ValueResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 3
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class StringValue(NDRCALL):
    opnum = 4
    structure = (

    )

class StringValueResponse(NDRCALL):
    structure = (
		('pbstrValue', BSTR),
    )
        

class Exception(NDRCALL):
    opnum = 5
    structure = (

    )

class ExceptionResponse(NDRCALL):
    structure = (
		('ppException', IAPPHOSTPROPERTYEXCEPTION),
    )
        

class GetMetadata(NDRCALL):
    opnum = 6
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class SetMetadata(NDRCALL):
    opnum = 7
    structure = (
		('bstrMetadataType', BSTR),
		('value', VARIANT),
    )

class SetMetadataResponse(NDRCALL):
    structure = (

    )
        

class Schema(NDRCALL):
    opnum = 8
    structure = (

    )

class SchemaResponse(NDRCALL):
    structure = (
		('ppSchema', IAPPHOSTPROPERTYSCHEMA),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Value,ValueResponse),
2 : (Clear,ClearResponse),
3 : (StringValue,StringValueResponse),
4 : (Exception,ExceptionResponse),
5 : (GetMetadata,GetMetadataResponse),
6 : (SetMetadata,SetMetadataResponse),
7 : (Schema,SchemaResponse),
}

#################################################################################

#IAppHostConfigLocation Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONFIGLOCATION = uuidtup_to_bin(('370af178-7758-4dad-8146-7391f6e18585','0.0'))


class Path(NDRCALL):
    opnum = 0
    structure = (

    )

class PathResponse(NDRCALL):
    structure = (
		('pbstrLocationPath', BSTR),
    )
        

class Count(NDRCALL):
    opnum = 1
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', DWORD),
    )
        

class Item(NDRCALL):
    opnum = 2
    structure = (
		('cIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppSection', IAPPHOSTELEMENT),
    )
        

class AddConfigSection(NDRCALL):
    opnum = 3
    structure = (
		('bstrSectionName', BSTR),
    )

class AddConfigSectionResponse(NDRCALL):
    structure = (
		('ppAdminElement', IAPPHOSTELEMENT),
    )
        

class DeleteConfigSection(NDRCALL):
    opnum = 4
    structure = (
		('cIndex', VARIANT),
    )

class DeleteConfigSectionResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Path,PathResponse),
1 : (Count,CountResponse),
2 : (Item,ItemResponse),
3 : (AddConfigSection,AddConfigSectionResponse),
4 : (DeleteConfigSection,DeleteConfigSectionResponse),
}

#################################################################################

#IAppHostSectionDefinition Definition

#################################################################################

MSRPC_UUID_IAPPHOSTSECTIONDEFINITION = uuidtup_to_bin(('c5c04795-321-4014-8d6-d44658799393','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 1
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('pbstrType', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 2
    structure = (
		('bstrType', BSTR),
    )

class TypeResponse(NDRCALL):
    structure = (

    )
        

class OverrideModeDefault(NDRCALL):
    opnum = 3
    structure = (

    )

class OverrideModeDefaultResponse(NDRCALL):
    structure = (
		('pbstrOverrideModeDefault', BSTR),
    )
        

class OverrideModeDefault(NDRCALL):
    opnum = 4
    structure = (
		('bstrOverrideModeDefault', BSTR),
    )

class OverrideModeDefaultResponse(NDRCALL):
    structure = (

    )
        

class AllowDefinition(NDRCALL):
    opnum = 5
    structure = (

    )

class AllowDefinitionResponse(NDRCALL):
    structure = (
		('pbstrAllowDefinition', BSTR),
    )
        

class AllowDefinition(NDRCALL):
    opnum = 6
    structure = (
		('bstrAllowDefinition', BSTR),
    )

class AllowDefinitionResponse(NDRCALL):
    structure = (

    )
        

class AllowLocation(NDRCALL):
    opnum = 7
    structure = (

    )

class AllowLocationResponse(NDRCALL):
    structure = (
		('pbstrAllowLocation', BSTR),
    )
        

class AllowLocation(NDRCALL):
    opnum = 8
    structure = (
		('bstrAllowLocation', BSTR),
    )

class AllowLocationResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Type,TypeResponse),
2 : (OverrideModeDefault,OverrideModeDefaultResponse),
3 : (AllowDefinition,AllowDefinitionResponse),
4 : (AllowLocation,AllowLocationResponse),
}

#################################################################################

#IAppHostSectionDefinitionCollection Definition

#################################################################################

MSRPC_UUID_IAPPHOSTSECTIONDEFINITIONCOLLECTION = uuidtup_to_bin(('b7d381ee-8860-471-8f4-13321325','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcCount', UNSIGNED_LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('varIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppConfigSection', IAPPHOSTSECTIONDEFINITION),
    )
        

class AddSection(NDRCALL):
    opnum = 2
    structure = (
		('bstrSectionName', BSTR),
    )

class AddSectionResponse(NDRCALL):
    structure = (
		('ppConfigSection', IAPPHOSTSECTIONDEFINITION),
    )
        

class DeleteSection(NDRCALL):
    opnum = 3
    structure = (
		('varIndex', VARIANT),
    )

class DeleteSectionResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (AddSection,AddSectionResponse),
3 : (DeleteSection,DeleteSectionResponse),
}

#################################################################################

#IAppHostSectionGroup Definition

#################################################################################

MSRPC_UUID_IAPPHOSTSECTIONGROUP = uuidtup_to_bin(('0dd8a158-ebe6-4008-a1d9-b7ecc8f1104b','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pcSectionGroup', UNSIGNED_LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('varIndex', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ppSectionGroup', IAPPHOSTSECTIONGROUP),
    )
        

class Sections(NDRCALL):
    opnum = 2
    structure = (

    )

class SectionsResponse(NDRCALL):
    structure = (
		('ppSections', IAPPHOSTSECTIONDEFINITIONCOLLECTION),
    )
        

class AddSectionGroup(NDRCALL):
    opnum = 3
    structure = (
		('bstrSectionGroupName', BSTR),
    )

class AddSectionGroupResponse(NDRCALL):
    structure = (
		('ppSectionGroup', IAPPHOSTSECTIONGROUP),
    )
        

class DeleteSectionGroup(NDRCALL):
    opnum = 4
    structure = (
		('varIndex', VARIANT),
    )

class DeleteSectionGroupResponse(NDRCALL):
    structure = (

    )
        

class Name(NDRCALL):
    opnum = 5
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('pbstrName', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 6
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('pbstrType', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 7
    structure = (
		('bstrType', BSTR),
    )

class TypeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (Sections,SectionsResponse),
3 : (AddSectionGroup,AddSectionGroupResponse),
4 : (DeleteSectionGroup,DeleteSectionGroupResponse),
5 : (Name,NameResponse),
6 : (Type,TypeResponse),
}

#################################################################################

#IAppHostConfigFile Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONFIGFILE = uuidtup_to_bin(('ada4e6fb-e025-401-a5d0-c3134a281f07','0.0'))


class ConfigPath(NDRCALL):
    opnum = 0
    structure = (

    )

class ConfigPathResponse(NDRCALL):
    structure = (
		('pbstrConfigPath', BSTR),
    )
        

class FilePath(NDRCALL):
    opnum = 1
    structure = (

    )

class FilePathResponse(NDRCALL):
    structure = (
		('pbstrFilePath', BSTR),
    )
        

class Locations(NDRCALL):
    opnum = 2
    structure = (

    )

class LocationsResponse(NDRCALL):
    structure = (
		('ppLocations', IAPPHOSTCONFIGLOCATIONCOLLECTION),
    )
        

class GetAdminSection(NDRCALL):
    opnum = 3
    structure = (
		('bstrSectionName', BSTR),
		('bstrPath', BSTR),
    )

class GetAdminSectionResponse(NDRCALL):
    structure = (
		('ppAdminSection', IAPPHOSTELEMENT),
    )
        

class GetMetadata(NDRCALL):
    opnum = 4
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class SetMetadata(NDRCALL):
    opnum = 5
    structure = (
		('bstrMetadataType', BSTR),
		('value', VARIANT),
    )

class SetMetadataResponse(NDRCALL):
    structure = (

    )
        

class ClearInvalidSections(NDRCALL):
    opnum = 6
    structure = (

    )

class ClearInvalidSectionsResponse(NDRCALL):
    structure = (

    )
        

class RootSectionGroup(NDRCALL):
    opnum = 7
    structure = (

    )

class RootSectionGroupResponse(NDRCALL):
    structure = (
		('ppSectionGroups', IAPPHOSTSECTIONGROUP),
    )
        
OPNUMS = {
0 : (ConfigPath,ConfigPathResponse),
1 : (FilePath,FilePathResponse),
2 : (Locations,LocationsResponse),
3 : (GetAdminSection,GetAdminSectionResponse),
4 : (GetMetadata,GetMetadataResponse),
5 : (SetMetadata,SetMetadataResponse),
6 : (ClearInvalidSections,ClearInvalidSectionsResponse),
7 : (RootSectionGroup,RootSectionGroupResponse),
}

#################################################################################

#IAppHostPathMapper Definition

#################################################################################

MSRPC_UUID_IAPPHOSTPATHMAPPER = uuidtup_to_bin(('e7927575-5c3-403-822-3286904ee','0.0'))


class MapPath(NDRCALL):
    opnum = 0
    structure = (
		('bstrConfigPath', BSTR),
		('bstrMappedPhysicalPath', BSTR),
    )

class MapPathResponse(NDRCALL):
    structure = (
		('pbstrNewPhysicalPath', BSTR),
    )
        
OPNUMS = {
0 : (MapPath,MapPathResponse),
}

#################################################################################

#IAppHostChangeHandler Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCHANGEHANDLER = uuidtup_to_bin(('09829352-87c2-418d-8d79-4133969a489d','0.0'))


class OnSectionChanges(NDRCALL):
    opnum = 0
    structure = (
		('bstrSectionName', BSTR),
		('bstrConfigPath', BSTR),
    )

class OnSectionChangesResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OnSectionChanges,OnSectionChangesResponse),
}

#################################################################################

#IAppHostAdminManager Definition

#################################################################################

MSRPC_UUID_IAPPHOSTADMINMANAGER = uuidtup_to_bin(('9be77978-73ed-4a9a-87fd-13f09fec1b13','0.0'))


class GetAdminSection(NDRCALL):
    opnum = 0
    structure = (
		('bstrSectionName', BSTR),
		('bstrPath', BSTR),
    )

class GetAdminSectionResponse(NDRCALL):
    structure = (
		('ppAdminSection', IAPPHOSTELEMENT),
    )
        

class GetMetadata(NDRCALL):
    opnum = 1
    structure = (
		('bstrMetadataType', BSTR),
    )

class GetMetadataResponse(NDRCALL):
    structure = (
		('pValue', VARIANT),
    )
        

class SetMetadata(NDRCALL):
    opnum = 2
    structure = (
		('bstrMetadataType', BSTR),
		('value', VARIANT),
    )

class SetMetadataResponse(NDRCALL):
    structure = (

    )
        

class ConfigManager(NDRCALL):
    opnum = 3
    structure = (

    )

class ConfigManagerResponse(NDRCALL):
    structure = (
		('ppConfigManager', IAPPHOSTCONFIGMANAGER),
    )
        
OPNUMS = {
0 : (GetAdminSection,GetAdminSectionResponse),
1 : (GetMetadata,GetMetadataResponse),
2 : (SetMetadata,SetMetadataResponse),
3 : (ConfigManager,ConfigManagerResponse),
}

#################################################################################

#IAppHostWritableAdminManager Definition

#################################################################################

MSRPC_UUID_IAPPHOSTWRITABLEADMINMANAGER = uuidtup_to_bin(('fa7660f6-73-4237-a8bf-ed0ad0dcbbd9','0.0'))


class CommitChanges(NDRCALL):
    opnum = 0
    structure = (

    )

class CommitChangesResponse(NDRCALL):
    structure = (

    )
        

class CommitPath(NDRCALL):
    opnum = 1
    structure = (

    )

class CommitPathResponse(NDRCALL):
    structure = (
		('pbstrCommitPath', BSTR),
    )
        

class CommitPath(NDRCALL):
    opnum = 2
    structure = (
		('bstrCommitPath', BSTR),
    )

class CommitPathResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CommitChanges,CommitChangesResponse),
1 : (CommitPath,CommitPathResponse),
}

#################################################################################

#IAppHostConfigManager Definition

#################################################################################

MSRPC_UUID_IAPPHOSTCONFIGMANAGER = uuidtup_to_bin(('8f6d760f-f0cb-4d69-b5f6-848b33e9bdc6','0.0'))


class GetConfigFile(NDRCALL):
    opnum = 0
    structure = (
		('bstrConfigPath', BSTR),
    )

class GetConfigFileResponse(NDRCALL):
    structure = (
		('ppConfigFile', IAPPHOSTCONFIGFILE),
    )
        

class GetUniqueConfigPath(NDRCALL):
    opnum = 1
    structure = (
		('bstrConfigPath', BSTR),
    )

class GetUniqueConfigPathResponse(NDRCALL):
    structure = (
		('pbstrUniquePath', BSTR),
    )
        
OPNUMS = {
0 : (GetConfigFile,GetConfigFileResponse),
1 : (GetUniqueConfigPath,GetUniqueConfigPathResponse),
}

