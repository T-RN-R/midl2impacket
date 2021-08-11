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
		('HRPC', HANDLE_T),
		('ORPCTHIS', ORPCTHIS),
		('CLSID', GUID),
		('PWSZOBJECTNAME', WCHAR_T),
		('POBJECTSTORAGE', MINTERFACEPOINTER),
		('CLIENTIMPLEVEL', DWORD),
		('MODE', DWORD),
		('INTERFACES', DWORD),
		('PIIDS', IID),
		('CREQUESTEDPROTSEQS', UNSIGNED_SHORT),
		('AREQUESTEDPROTSEQS', UNSIGNED_SHORT),
    )

class RemoteActivationResponse(NDRCALL):
    structure = (
		('ORPCTHAT', ORPCTHAT),
		('POXID', OXID),
		('PPDSAOXIDBINDINGS', DUALSTRINGARRAY),
		('PIPIDREMUNKNOWN', IPID),
		('PAUTHNHINT', DWORD),
		('PSERVERVERSION', COMVERSION),
		('PHR', HRESULT),
		('PPINTERFACEDATA', MINTERFACEPOINTER),
		('PRESULTS', HRESULT),
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
		('RPC', HANDLE_T),
		('ORPCTHIS', ORPCTHIS),
		('PACTPROPERTIES', MINTERFACEPOINTER),
    )

class RemoteGetClassObjectResponse(NDRCALL):
    structure = (
		('ORPCTHAT', ORPCTHAT),
		('PPACTPROPERTIES', MINTERFACEPOINTER),
    )
        

class RemoteCreateInstance(NDRCALL):
    opnum = 4
    structure = (
		('RPC', HANDLE_T),
		('ORPCTHIS', ORPCTHIS),
		('PUNKOUTER', MINTERFACEPOINTER),
		('PACTPROPERTIES', MINTERFACEPOINTER),
    )

class RemoteCreateInstanceResponse(NDRCALL):
    structure = (
		('ORPCTHAT', ORPCTHAT),
		('PPACTPROPERTIES', MINTERFACEPOINTER),
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
		('HRPC', HANDLE_T),
		('POXID', OXID),
		('CREQUESTEDPROTSEQS', UNSIGNED_SHORT),
		('ARREQUESTEDPROTSEQS', UNSIGNED_SHORT),
    )

class ResolveOxidResponse(NDRCALL):
    structure = (
		('PPDSAOXIDBINDINGS', DUALSTRINGARRAY),
		('PIPIDREMUNKNOWN', IPID),
		('PAUTHNHINT', DWORD),
    )
        

class SimplePing(NDRCALL):
    opnum = 1
    structure = (
		('HRPC', HANDLE_T),
		('PSETID', SETID),
    )

class SimplePingResponse(NDRCALL):
    structure = (

    )
        

class ComplexPing(NDRCALL):
    opnum = 2
    structure = (
		('HRPC', HANDLE_T),
		('PSETID', SETID),
		('SEQUENCENUM', UNSIGNED_SHORT),
		('CADDTOSET', UNSIGNED_SHORT),
		('CDELFROMSET', UNSIGNED_SHORT),
		('ADDTOSET', OID),
		('DELFROMSET', OID),
    )

class ComplexPingResponse(NDRCALL):
    structure = (
		('PSETID', SETID),
		('PPINGBACKOFFFACTOR', UNSIGNED_SHORT),
    )
        

class ServerAlive(NDRCALL):
    opnum = 3
    structure = (
		('HRPC', HANDLE_T),
    )

class ServerAliveResponse(NDRCALL):
    structure = (

    )
        

class ResolveOxid2(NDRCALL):
    opnum = 4
    structure = (
		('HRPC', HANDLE_T),
		('POXID', OXID),
		('CREQUESTEDPROTSEQS', UNSIGNED_SHORT),
		('ARREQUESTEDPROTSEQS', UNSIGNED_SHORT),
    )

class ResolveOxid2Response(NDRCALL):
    structure = (
		('PPDSAOXIDBINDINGS', DUALSTRINGARRAY),
		('PIPIDREMUNKNOWN', IPID),
		('PAUTHNHINT', DWORD),
		('PCOMVERSION', COMVERSION),
    )
        

class ServerAlive2(NDRCALL):
    opnum = 5
    structure = (
		('HRPC', HANDLE_T),
    )

class ServerAlive2Response(NDRCALL):
    structure = (
		('PCOMVERSION', COMVERSION),
		('PPDSAORBINDINGS', DUALSTRINGARRAY),
		('PRESERVED', DWORD),
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
		('RIPID', REFIPID),
		('CREFS', UNSIGNED_LONG),
		('CIIDS', UNSIGNED_SHORT),
		('IIDS', IID),
    )

class RemQueryInterfaceResponse(NDRCALL):
    structure = (
		('PPQIRESULTS', PREMQIRESULT),
    )
        

class RemAddRef(NDRCALL):
    opnum = 1
    structure = (
		('CINTERFACEREFS', UNSIGNED_SHORT),
		('INTERFACEREFS', REMINTERFACEREF),
    )

class RemAddRefResponse(NDRCALL):
    structure = (
		('PRESULTS', HRESULT),
    )
        

class RemRelease(NDRCALL):
    opnum = 2
    structure = (
		('CINTERFACEREFS', UNSIGNED_SHORT),
		('INTERFACEREFS', REMINTERFACEREF),
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
		('RIPID', REFIPID),
		('CIIDS', UNSIGNED_SHORT),
		('IIDS', IID),
    )

class RemQueryInterface2Response(NDRCALL):
    structure = (
		('PHR', HRESULT),
		('PPMIF', PMINTERFACEPOINTERINTERNAL),
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
        

class ANONYMOUS4(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous4', ANONYMOUS4),
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
		('PCTINFO', UINT),
    )
        

class GetTypeInfo(NDRCALL):
    opnum = 1
    structure = (
		('ITINFO', UINT),
		('LCID', LCID),
    )

class GetTypeInfoResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
    )
        

class GetIDsOfNames(NDRCALL):
    opnum = 2
    structure = (
		('RIID', REFIID),
		('RGSZNAMES', LPOLESTR),
		('CNAMES', UINT),
		('LCID', LCID),
    )

class GetIDsOfNamesResponse(NDRCALL):
    structure = (
		('RGDISPID', DISPID),
    )
        

class Invoke(NDRCALL):
    opnum = 3
    structure = (
		('DISPIDMEMBER', DISPID),
		('RIID', REFIID),
		('LCID', LCID),
		('DWFLAGS', DWORD),
		('PDISPPARAMS', DISPPARAMS),
		('CVARREF', UINT),
		('RGVARREFIDX', UINT),
		('RGVARREF', VARIANT),
    )

class InvokeResponse(NDRCALL):
    structure = (
		('PVARRESULT', VARIANT),
		('PEXCEPINFO', EXCEPINFO),
		('PARGERR', UINT),
		('RGVARREF', VARIANT),
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
		('CELT', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('RGVAR', VARIANT),
		('PCELTFETCHED', ULONG),
    )
        

class Skip(NDRCALL):
    opnum = 1
    structure = (
		('CELT', ULONG),
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
		('PPENUM', IENUMVARIANT),
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
		('SZNAME', LPOLESTR),
		('LHASHVAL', ULONG),
		('WFLAGS', WORD),
    )

class BindResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
		('PDESCKIND', DESCKIND),
		('PPFUNCDESC', LPFUNCDESC),
		('PPVARDESC', LPVARDESC),
		('PPTYPECOMP', ITYPECOMP),
		('PRESERVED', DWORD),
    )
        

class BindType(NDRCALL):
    opnum = 1
    structure = (
		('SZNAME', LPOLESTR),
		('LHASHVAL', ULONG),
    )

class BindTypeResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
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
		('PPTYPEATTR', LPTYPEATTR),
		('PRESERVED', DWORD),
    )
        

class GetTypeComp(NDRCALL):
    opnum = 1
    structure = (

    )

class GetTypeCompResponse(NDRCALL):
    structure = (
		('PPTCOMP', ITYPECOMP),
    )
        

class GetFuncDesc(NDRCALL):
    opnum = 2
    structure = (
		('INDEX', UINT),
    )

class GetFuncDescResponse(NDRCALL):
    structure = (
		('PPFUNCDESC', LPFUNCDESC),
		('PRESERVED', DWORD),
    )
        

class GetVarDesc(NDRCALL):
    opnum = 3
    structure = (
		('INDEX', UINT),
    )

class GetVarDescResponse(NDRCALL):
    structure = (
		('PPVARDESC', LPVARDESC),
		('PRESERVED', DWORD),
    )
        

class GetNames(NDRCALL):
    opnum = 4
    structure = (
		('MEMID', MEMBERID),
		('CMAXNAMES', UINT),
    )

class GetNamesResponse(NDRCALL):
    structure = (
		('RGBSTRNAMES', BSTR),
		('PCNAMES', UINT),
    )
        

class GetRefTypeOfImplType(NDRCALL):
    opnum = 5
    structure = (
		('INDEX', UINT),
    )

class GetRefTypeOfImplTypeResponse(NDRCALL):
    structure = (
		('PREFTYPE', HREFTYPE),
    )
        

class GetImplTypeFlags(NDRCALL):
    opnum = 6
    structure = (
		('INDEX', UINT),
    )

class GetImplTypeFlagsResponse(NDRCALL):
    structure = (
		('PIMPLTYPEFLAGS', INT),
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
		('MEMID', MEMBERID),
		('REFPTRFLAGS', DWORD),
    )

class GetDocumentationResponse(NDRCALL):
    structure = (
		('PBSTRNAME', BSTR),
		('PBSTRDOCSTRING', BSTR),
		('PDWHELPCONTEXT', DWORD),
		('PBSTRHELPFILE', BSTR),
    )
        

class GetDllEntry(NDRCALL):
    opnum = 10
    structure = (
		('MEMID', MEMBERID),
		('INVKIND', INVOKEKIND),
		('REFPTRFLAGS', DWORD),
    )

class GetDllEntryResponse(NDRCALL):
    structure = (
		('PBSTRDLLNAME', BSTR),
		('PBSTRNAME', BSTR),
		('PWORDINAL', WORD),
    )
        

class GetRefTypeInfo(NDRCALL):
    opnum = 11
    structure = (
		('HREFTYPE', HREFTYPE),
    )

class GetRefTypeInfoResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
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
		('RIID', REFIID),
    )

class CreateInstanceResponse(NDRCALL):
    structure = (
		('PPVOBJ', IUNKNOWN),
    )
        

class GetMops(NDRCALL):
    opnum = 14
    structure = (
		('MEMID', MEMBERID),
    )

class GetMopsResponse(NDRCALL):
    structure = (
		('PBSTRMOPS', BSTR),
    )
        

class GetContainingTypeLib(NDRCALL):
    opnum = 15
    structure = (

    )

class GetContainingTypeLibResponse(NDRCALL):
    structure = (
		('PPTLIB', ITYPELIB),
		('PINDEX', UINT),
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
		('PTYPEKIND', TYPEKIND),
    )
        

class GetTypeFlags(NDRCALL):
    opnum = 1
    structure = (

    )

class GetTypeFlagsResponse(NDRCALL):
    structure = (
		('PTYPEFLAGS', ULONG),
    )
        

class GetFuncIndexOfMemId(NDRCALL):
    opnum = 2
    structure = (
		('MEMID', MEMBERID),
		('INVKIND', INVOKEKIND),
    )

class GetFuncIndexOfMemIdResponse(NDRCALL):
    structure = (
		('PFUNCINDEX', UINT),
    )
        

class GetVarIndexOfMemId(NDRCALL):
    opnum = 3
    structure = (
		('MEMID', MEMBERID),
    )

class GetVarIndexOfMemIdResponse(NDRCALL):
    structure = (
		('PVARINDEX', UINT),
    )
        

class GetCustData(NDRCALL):
    opnum = 4
    structure = (
		('GUID', REFGUID),
    )

class GetCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetFuncCustData(NDRCALL):
    opnum = 5
    structure = (
		('INDEX', UINT),
		('GUID', REFGUID),
    )

class GetFuncCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetParamCustData(NDRCALL):
    opnum = 6
    structure = (
		('INDEXFUNC', UINT),
		('INDEXPARAM', UINT),
		('GUID', REFGUID),
    )

class GetParamCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetVarCustData(NDRCALL):
    opnum = 7
    structure = (
		('INDEX', UINT),
		('GUID', REFGUID),
    )

class GetVarCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetImplTypeCustData(NDRCALL):
    opnum = 8
    structure = (
		('INDEX', UINT),
		('GUID', REFGUID),
    )

class GetImplTypeCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetDocumentation2(NDRCALL):
    opnum = 9
    structure = (
		('MEMID', MEMBERID),
		('LCID', LCID),
		('REFPTRFLAGS', DWORD),
    )

class GetDocumentation2Response(NDRCALL):
    structure = (
		('PBSTRHELPSTRING', BSTR),
		('PDWHELPSTRINGCONTEXT', DWORD),
		('PBSTRHELPSTRINGDLL', BSTR),
    )
        

class GetAllCustData(NDRCALL):
    opnum = 10
    structure = (

    )

class GetAllCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
    )
        

class GetAllFuncCustData(NDRCALL):
    opnum = 11
    structure = (
		('INDEX', UINT),
    )

class GetAllFuncCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
    )
        

class GetAllParamCustData(NDRCALL):
    opnum = 12
    structure = (
		('INDEXFUNC', UINT),
		('INDEXPARAM', UINT),
    )

class GetAllParamCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
    )
        

class GetAllVarCustData(NDRCALL):
    opnum = 13
    structure = (
		('INDEX', UINT),
    )

class GetAllVarCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
    )
        

class GetAllImplTypeCustData(NDRCALL):
    opnum = 14
    structure = (
		('INDEX', UINT),
    )

class GetAllImplTypeCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
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
		('PCTINFO', UINT),
    )
        

class GetTypeInfo(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', UINT),
    )

class GetTypeInfoResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
    )
        

class GetTypeInfoType(NDRCALL):
    opnum = 2
    structure = (
		('INDEX', UINT),
    )

class GetTypeInfoTypeResponse(NDRCALL):
    structure = (
		('PTKIND', TYPEKIND),
    )
        

class GetTypeInfoOfGuid(NDRCALL):
    opnum = 3
    structure = (
		('GUID', REFGUID),
    )

class GetTypeInfoOfGuidResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
    )
        

class GetLibAttr(NDRCALL):
    opnum = 4
    structure = (

    )

class GetLibAttrResponse(NDRCALL):
    structure = (
		('PPTLIBATTR', LPTLIBATTR),
		('PRESERVED', DWORD),
    )
        

class GetTypeComp(NDRCALL):
    opnum = 5
    structure = (

    )

class GetTypeCompResponse(NDRCALL):
    structure = (
		('PPTCOMP', ITYPECOMP),
    )
        

class GetDocumentation(NDRCALL):
    opnum = 6
    structure = (
		('INDEX', INT),
		('REFPTRFLAGS', DWORD),
    )

class GetDocumentationResponse(NDRCALL):
    structure = (
		('PBSTRNAME', BSTR),
		('PBSTRDOCSTRING', BSTR),
		('PDWHELPCONTEXT', DWORD),
		('PBSTRHELPFILE', BSTR),
    )
        

class IsName(NDRCALL):
    opnum = 7
    structure = (
		('SZNAMEBUF', LPOLESTR),
		('LHASHVAL', ULONG),
    )

class IsNameResponse(NDRCALL):
    structure = (
		('PFNAME', BOOL),
		('PBSTRNAMEINLIBRARY', BSTR),
    )
        

class FindName(NDRCALL):
    opnum = 8
    structure = (
		('SZNAMEBUF', LPOLESTR),
		('LHASHVAL', ULONG),
		('PCFOUND', USHORT),
    )

class FindNameResponse(NDRCALL):
    structure = (
		('PPTINFO', ITYPEINFO),
		('RGMEMID', MEMBERID),
		('PCFOUND', USHORT),
		('PBSTRNAMEINLIBRARY', BSTR),
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
		('GUID', REFGUID),
    )

class GetCustDataResponse(NDRCALL):
    structure = (
		('PVARVAL', VARIANT),
    )
        

class GetLibStatistics(NDRCALL):
    opnum = 1
    structure = (

    )

class GetLibStatisticsResponse(NDRCALL):
    structure = (
		('PCUNIQUENAMES', ULONG),
		('PCCHUNIQUENAMES', ULONG),
    )
        

class GetDocumentation2(NDRCALL):
    opnum = 2
    structure = (
		('INDEX', INT),
		('LCID', LCID),
		('REFPTRFLAGS', DWORD),
    )

class GetDocumentation2Response(NDRCALL):
    structure = (
		('PBSTRHELPSTRING', BSTR),
		('PDWHELPSTRINGCONTEXT', DWORD),
		('PBSTRHELPSTRINGDLL', BSTR),
    )
        

class GetAllCustData(NDRCALL):
    opnum = 3
    structure = (

    )

class GetAllCustDataResponse(NDRCALL):
    structure = (
		('PCUSTDATA', CUSTDATA),
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


class PROPERTYMETA(NDRSTRUCT):
    structure = (
        ('dataType', DWORD),('cbSize', ULONG),('flags', DWORD),
    )


eCT_UNKNOWN = 0,
eCT_32BIT = 1,
eCT_64BIT = 2,
eCT_NATIVE = 4096
        

class SRPLEVELINFO(NDRSTRUCT):
    structure = (
        ('dwSRPLevel', DWORD),('wszFriendlyName', WCHAR),
    )


css_lb = 1
        

css_serviceStopped = 0,
css_serviceStartPending = 1,
css_serviceStopPending = 2,
css_serviceRunning = 3,
css_serviceContinuePending = 4,
css_servicePausePending = 5,
css_servicePaused = 6,
css_serviceUnknownState = 7
        

class INSTANCECONTAINER(NDRSTRUCT):
    structure = (
        ('ConglomerationID', GUID),('PartitionID', GUID),('ContainerID', GUID),('dwProcessID', DWORD),('bPaused', BOOL),('bRecycled', BOOL),
    )

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#ICatalogSession Definition

#################################################################################

MSRPC_UUID_ICATALOGSESSION = uuidtup_to_bin(('182C40FA-32E4-11D0-818B-00A0C9231C29','0.0'))


class Opnum3NotUsedOnWire(NDRCALL):
    opnum = 0
    structure = (

    )

class Opnum3NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class InitializeSession(NDRCALL):
    opnum = 4
    structure = (
		('FLVERLOWER', FLOAT),
		('FLVERUPPER', FLOAT),
		('RESERVED', LONG),
    )

class InitializeSessionResponse(NDRCALL):
    structure = (
		('PFLVERSESSION', FLOAT),
    )
        

class GetServerInformation(NDRCALL):
    opnum = 5
    structure = (

    )

class GetServerInformationResponse(NDRCALL):
    structure = (
		('PLRESERVED1', LONG),
		('PLRESERVED2', LONG),
		('PLRESERVED3', LONG),
		('PLMULTIPLEPARTITIONSUPPORT', LONG),
		('PLRESERVED4', LONG),
		('PLRESERVED5', LONG),
    )
        
OPNUMS = {
0 : (Opnum3NotUsedOnWire,Opnum3NotUsedOnWireResponse),
1 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
3 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
4 : (InitializeSession,InitializeSessionResponse),
5 : (GetServerInformation,GetServerInformationResponse),
}

#################################################################################

#ICatalog64BitSupport Definition

#################################################################################

MSRPC_UUID_ICATALOG64BITSUPPORT = uuidtup_to_bin(('1D118904-94B3-4A64-9FA6-ED432666A7B9','0.0'))


class SupportsMultipleBitness(NDRCALL):
    opnum = 0
    structure = (

    )

class SupportsMultipleBitnessResponse(NDRCALL):
    structure = (
		('PBSUPPORTSMULTIPLEBITNESS', BOOL),
    )
        

class Initialize64BitQueryCellSupport(NDRCALL):
    opnum = 1
    structure = (
		('BCLIENTSUPPORTS64BITQUERYCELLS', BOOL),
    )

class Initialize64BitQueryCellSupportResponse(NDRCALL):
    structure = (
		('PBSERVERSUPPORTS64BITQUERYCELLS', BOOL),
    )
        
OPNUMS = {
0 : (SupportsMultipleBitness,SupportsMultipleBitnessResponse),
1 : (Initialize64BitQueryCellSupport,Initialize64BitQueryCellSupportResponse),
}

#################################################################################

#ICatalogTableInfo Definition

#################################################################################

MSRPC_UUID_ICATALOGTABLEINFO = uuidtup_to_bin(('A8927A41-D3CE-111-8472-00600805A','0.0'))


class GetClientTableInfo(NDRCALL):
    opnum = 0
    structure = (
		('PCATALOGIDENTIFIER', GUID),
		('PTABLEIDENTIFIER', GUID),
		('TABLEFLAGS', DWORD),
		('PQUERYCELLARRAY', CHAR),
		('CBQUERYCELLARRAY', ULONG),
		('PQUERYCOMPARISON', CHAR),
		('CBQUERYCOMPARISON', ULONG),
		('EQUERYFORMAT', DWORD),
    )

class GetClientTableInfoResponse(NDRCALL):
    structure = (
		('PREQUIREDFIXEDGUID', GUID),
		('PPRESERVED1', CHAR),
		('PCBRESERVED1', ULONG),
		('PPAUXILIARYGUID', GUID),
		('PCAUXILIARYGUID', ULONG),
		('PPPROPERTYMETA', PROPERTYMETA),
		('PCPROPERTIES', ULONG),
		('PIID', IID),
		('PITF', CONTEXT_HANDLE),
		('PPRESERVED2', CHAR),
		('PCBRESERVED2', ULONG),
    )
        
OPNUMS = {
0 : (GetClientTableInfo,GetClientTableInfoResponse),
}

#################################################################################

#ICatalogTableRead Definition

#################################################################################

MSRPC_UUID_ICATALOGTABLEREAD = uuidtup_to_bin(('0E3D6630-B46B-11D1-9D2D-006008B0E5CA','0.0'))


class ReadTable(NDRCALL):
    opnum = 0
    structure = (
		('PCATALOGIDENTIFIER', GUID),
		('PTABLEIDENTIFIER', GUID),
		('TABLEFLAGS', DWORD),
		('PQUERYCELLARRAY', CHAR),
		('CBQUERYCELLARRAY', ULONG),
		('PQUERYCOMPARISON', CHAR),
		('CBQUERYCOMPARISON', ULONG),
		('EQUERYFORMAT', DWORD),
    )

class ReadTableResponse(NDRCALL):
    structure = (
		('PPTABLEDATAFIXED', CHAR),
		('PCBTABLEDATAFIXED', ULONG),
		('PPTABLEDATAVARIABLE', CHAR),
		('PCBTABLEDATAVARIABLE', ULONG),
		('PPTABLEDETAILEDERRORS', CHAR),
		('PCBTABLEDETAILEDERRORS', ULONG),
		('PPRESERVED1', CHAR),
		('PCBRESERVED1', ULONG),
		('PPRESERVED2', CHAR),
		('PCBRESERVED2', ULONG),
    )
        
OPNUMS = {
0 : (ReadTable,ReadTableResponse),
}

#################################################################################

#ICatalogTableWrite Definition

#################################################################################

MSRPC_UUID_ICATALOGTABLEWRITE = uuidtup_to_bin(('0E3D6631-B46B-11D1-9D2D-006008B0E5CA','0.0'))


class WriteTable(NDRCALL):
    opnum = 0
    structure = (
		('PCATALOGIDENTIFIER', GUID),
		('PTABLEIDENTIFIER', GUID),
		('TABLEFLAGS', DWORD),
		('PQUERYCELLARRAY', CHAR),
		('CBQUERYCELLARRAY', ULONG),
		('PQUERYCOMPARISON', CHAR),
		('CBQUERYCOMPARISON', ULONG),
		('EQUERYFORMAT', DWORD),
		('PTABLEDATAFIXEDWRITE', CHAR),
		('CBTABLEDATAFIXEDWRITE', ULONG),
		('PTABLEDATAVARIABLE', CHAR),
		('CBTABLEDATAVARIABLE', ULONG),
		('PRESERVED1', CHAR),
		('CBRESERVED1', ULONG),
		('PRESERVED2', CHAR),
		('CBRESERVED2', ULONG),
		('PRESERVED3', CHAR),
		('CBRESERVED3', ULONG),
    )

class WriteTableResponse(NDRCALL):
    structure = (
		('PPTABLEDETAILEDERRORS', CHAR),
		('PCBTABLEDETAILEDERRORS', ULONG),
    )
        
OPNUMS = {
0 : (WriteTable,WriteTableResponse),
}

#################################################################################

#IRegister Definition

#################################################################################

MSRPC_UUID_IREGISTER = uuidtup_to_bin(('8DB2180E-BD29-11D1-8B7E-00C04FD7A924','0.0'))


class RegisterModule(NDRCALL):
    opnum = 0
    structure = (
		('CONGLOMERATIONIDENTIFIER', GUID),
		('PPMODULES', LPWSTR),
		('CMODULES', DWORD),
		('DWFLAGS', DWORD),
		('PREQUESTEDCLSIDS', GUID),
		('CREQUESTED', DWORD),
    )

class RegisterModuleResponse(NDRCALL):
    structure = (
		('PPMODULEFLAGS', DWORD),
		('PCRESULTS', DWORD),
		('PPRESULTCLSIDS', GUID),
		('PPRESULTNAMES', LPWSTR),
		('PPRESULTFLAGS', DWORD),
		('PPRESULTHRS', LONG),
    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RegisterModule,RegisterModuleResponse),
1 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
}

#################################################################################

#IRegister2 Definition

#################################################################################

MSRPC_UUID_IREGISTER2 = uuidtup_to_bin(('971668DC-C3FE-4EA1-9643-0C7230F494A1','0.0'))


class CreateFullConfiguration(NDRCALL):
    opnum = 0
    structure = (
		('PWSZCONGLOMERATIONIDORNAME', LPCWSTR),
		('PWSZCLSIDORPROGID', LPCWSTR),
		('CTCOMPONENTTYPE', ECOMPONENTTYPE),
    )

class CreateFullConfigurationResponse(NDRCALL):
    structure = (

    )
        

class CreateLegacyConfiguration(NDRCALL):
    opnum = 1
    structure = (
		('PWSZCONGLOMERATIONIDORNAME', LPCWSTR),
		('PWSZCLSIDORPROGID', LPCWSTR),
		('CTCOMPONENTTYPE', ECOMPONENTTYPE),
    )

class CreateLegacyConfigurationResponse(NDRCALL):
    structure = (

    )
        

class PromoteLegacyConfiguration(NDRCALL):
    opnum = 2
    structure = (
		('PWSZCONGLOMERATIONIDORNAME', LPCWSTR),
		('PWSZCLSIDORPROGID', LPCWSTR),
		('CTCOMPONENTTYPE', ECOMPONENTTYPE),
    )

class PromoteLegacyConfigurationResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum7NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum7NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RegisterModule2(NDRCALL):
    opnum = 5
    structure = (
		('CONGLOMERATIONIDENTIFIER', GUID),
		('PARTITIONIDENTIFIER', GUID),
		('PPMODULES', LPWSTR),
		('CMODULES', DWORD),
		('DWFLAGS', DWORD),
		('PREQUESTEDCLSIDS', GUID),
		('CREQUESTED', DWORD),
    )

class RegisterModule2Response(NDRCALL):
    structure = (
		('PPMODULEFLAGS', DWORD),
		('PCRESULTS', DWORD),
		('PPRESULTCLSIDS', GUID),
		('PPRESULTNAMES', LPWSTR),
		('PPRESULTFLAGS', DWORD),
		('PPRESULTHRS', LONG),
    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CreateFullConfiguration,CreateFullConfigurationResponse),
1 : (CreateLegacyConfiguration,CreateLegacyConfigurationResponse),
2 : (PromoteLegacyConfiguration,PromoteLegacyConfigurationResponse),
3 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
4 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
5 : (RegisterModule2,RegisterModule2Response),
6 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
}

#################################################################################

#IImport Definition

#################################################################################

MSRPC_UUID_IIMPORT = uuidtup_to_bin(('C2BE6970-DF9E-111-887-0004D7A924','0.0'))


class ImportFromFile(NDRCALL):
    opnum = 0
    structure = (
		('PWSZMODULEDESTINATION', WCHAR),
		('PWSZINSTALLERPACKAGE', WCHAR),
		('PWSZUSER', WCHAR),
		('PWSZPASSWORD', WCHAR),
		('PWSZREMOTESERVERNAME', WCHAR),
		('DWFLAGS', DWORD),
		('RESERVED1', GUID),
		('RESERVED2', DWORD),
    )

class ImportFromFileResponse(NDRCALL):
    structure = (
		('PCMODULES', DWORD),
		('PPMODULEFLAGS', DWORD),
		('PPMODULES', LPWSTR),
		('PCCOMPONENTS', DWORD),
		('PPRESULTCLSIDS', GUID),
		('PPRESULTNAMES', LPWSTR),
		('PPRESULTFLAGS', DWORD),
		('PPRESULTHRS', LONG),
    )
        

class QueryFile(NDRCALL):
    opnum = 1
    structure = (
		('PWSZINSTALLERPACKAGE', WCHAR),
    )

class QueryFileResponse(NDRCALL):
    structure = (
		('PDWCONGLOMERATIONS', DWORD),
		('PPNAMES', LPWSTR),
		('PPDESCRIPTIONS', LPWSTR),
		('PDWUSERS', DWORD),
		('PDWISPROXY', DWORD),
		('PCMODULES', DWORD),
		('PPMODULES', LPWSTR),
    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ImportFromFile,ImportFromFileResponse),
1 : (QueryFile,QueryFileResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
3 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
}

#################################################################################

#IImport2 Definition

#################################################################################

MSRPC_UUID_IIMPORT2 = uuidtup_to_bin(('1F7B1697-ECB2-4CBB-8A0E-75C427F4A6F0','0.0'))


class SetPartition(NDRCALL):
    opnum = 0
    structure = (
		('PPARTITIONIDENTIFIER', GUID),
    )

class SetPartitionResponse(NDRCALL):
    structure = (
		('PRESERVED', GUID),
    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SetPartition,SetPartitionResponse),
1 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
}

#################################################################################

#IExport Definition

#################################################################################

MSRPC_UUID_IEXPORT = uuidtup_to_bin(('CFADAC84-E12C-111-B34C-000499054','0.0'))


class ExportConglomeration(NDRCALL):
    opnum = 0
    structure = (
		('PCONGLOMERATIONIDENTIFIER', GUID),
		('PWSZINSTALLERPACKAGE', LPCWSTR),
		('PWSZRESERVED', LPCWSTR),
		('DWFLAGS', DWORD),
    )

class ExportConglomerationResponse(NDRCALL):
    structure = (

    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ExportConglomeration,ExportConglomerationResponse),
1 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
3 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
}

#################################################################################

#IExport2 Definition

#################################################################################

MSRPC_UUID_IEXPORT2 = uuidtup_to_bin(('F131EA3E-B7BE-480-A60D-51B2785779E','0.0'))


class ExportPartition(NDRCALL):
    opnum = 0
    structure = (
		('PPARTITIONIDENTIFIER', GUID),
		('PWSZINSTALLERPACKAGE', LPCWSTR),
		('PWSZRESERVED', LPCWSTR),
		('DWFLAGS', DWORD),
    )

class ExportPartitionResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ExportPartition,ExportPartitionResponse),
}

#################################################################################

#IAlternateLaunch Definition

#################################################################################

MSRPC_UUID_IALTERNATELAUNCH = uuidtup_to_bin(('7F43B400-1A0E-4D57-BBC9-6B0C65F7A889','0.0'))


class CreateConfiguration(NDRCALL):
    opnum = 0
    structure = (
		('CONGLOMERATIONIDENTIFIER', GUID),
		('BSTRCONFIGURATIONNAME', BSTR),
		('DWSTARTTYPE', DWORD),
		('DWERRORCONTROL', DWORD),
		('BSTRDEPENDENCIES', BSTR),
		('BSTRRUNAS', BSTR),
		('BSTRPASSWORD', BSTR),
		('BDESKTOPOK', VARIANT_BOOL),
    )

class CreateConfigurationResponse(NDRCALL):
    structure = (

    )
        

class DeleteConfiguration(NDRCALL):
    opnum = 1
    structure = (
		('CONGLOMERATIONIDENTIFIER', GUID),
    )

class DeleteConfigurationResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CreateConfiguration,CreateConfigurationResponse),
1 : (DeleteConfiguration,DeleteConfigurationResponse),
}

#################################################################################

#ICatalogUtils Definition

#################################################################################

MSRPC_UUID_ICATALOGUTILS = uuidtup_to_bin(('456129E2-1078-11D2-B0F9-00805FC73204','0.0'))


class ValidateUser(NDRCALL):
    opnum = 0
    structure = (
		('PWSZPRINCIPALNAME', LPWSTR),
		('PWSZPASSWORD', LPWSTR),
    )

class ValidateUserResponse(NDRCALL):
    structure = (

    )
        

class WaitForEndWrites(NDRCALL):
    opnum = 1
    structure = (

    )

class WaitForEndWritesResponse(NDRCALL):
    structure = (

    )
        

class GetEventClassesForIID(NDRCALL):
    opnum = 2
    structure = (
		('WSZIID', LPWSTR),
    )

class GetEventClassesForIIDResponse(NDRCALL):
    structure = (
		('PCCLASSES', DWORD),
		('PAWSZCLSIDS', LPWSTR),
		('PAWSZPROGIDS', LPWSTR),
		('PAWSZDESCRIPTIONS', LPWSTR),
    )
        
OPNUMS = {
0 : (ValidateUser,ValidateUserResponse),
1 : (WaitForEndWrites,WaitForEndWritesResponse),
2 : (GetEventClassesForIID,GetEventClassesForIIDResponse),
}

#################################################################################

#ICatalogUtils2 Definition

#################################################################################

MSRPC_UUID_ICATALOGUTILS2 = uuidtup_to_bin(('C726744E-5735-408-8286-C510EE638FB6','0.0'))


class CopyConglomerations(NDRCALL):
    opnum = 0
    structure = (
		('PWSZSOURCEPARTITION', LPCWSTR),
		('PWSZDESTPARTITION', LPCWSTR),
		('CCONGLOMERATIONS', DWORD),
		('PPWSZCONGLOMERATIONNAMESORIDS', LPCWSTR),
    )

class CopyConglomerationsResponse(NDRCALL):
    structure = (

    )
        

class CopyComponentConfiguration(NDRCALL):
    opnum = 1
    structure = (
		('PWSZSOURCECONGLOMERATION', LPCWSTR),
		('PWSZCOMPONENT', LPCWSTR),
		('PWSZDESTCONGLOMERATION', LPCWSTR),
    )

class CopyComponentConfigurationResponse(NDRCALL):
    structure = (

    )
        

class AliasComponent(NDRCALL):
    opnum = 2
    structure = (
		('PWSZSOURCECONGLOMERATION', LPCWSTR),
		('PWSZCOMPONENT', LPCWSTR),
		('PWSZDESTCONGLOMERATION', LPCWSTR),
		('PNEWCLSID', GUID),
		('PWSZNEWPROGID', LPCWSTR),
    )

class AliasComponentResponse(NDRCALL):
    structure = (

    )
        

class MoveComponentConfiguration(NDRCALL):
    opnum = 3
    structure = (
		('PWSZSOURCECONGLOMERATION', LPCWSTR),
		('PWSZCOMPONENT', LPCWSTR),
		('PWSZDESTINATIONCONGLOMERATION', LPCWSTR),
    )

class MoveComponentConfigurationResponse(NDRCALL):
    structure = (

    )
        

class GetEventClassesForIID2(NDRCALL):
    opnum = 4
    structure = (
		('WSZIID', LPWSTR),
		('PARTITIONID', GUID),
    )

class GetEventClassesForIID2Response(NDRCALL):
    structure = (
		('PCCLASSES', DWORD),
		('PAWSZCLSIDS', LPWSTR),
		('PAWSZPROGIDS', LPWSTR),
		('PAWSZDESCRIPTIONS', LPWSTR),
		('PAWSZCONGLOMERATIONIDS', LPWSTR),
		('PADWISPRIVATE', DWORD),
    )
        

class IsSafeToDelete(NDRCALL):
    opnum = 5
    structure = (
		('BSTRFILE', BSTR),
    )

class IsSafeToDeleteResponse(NDRCALL):
    structure = (
		('PINUSE', LONG),
    )
        

class FlushPartitionCache(NDRCALL):
    opnum = 6
    structure = (

    )

class FlushPartitionCacheResponse(NDRCALL):
    structure = (

    )
        

class EnumerateSRPLevels(NDRCALL):
    opnum = 7
    structure = (
		('LOCALE', LCID),
    )

class EnumerateSRPLevelsResponse(NDRCALL):
    structure = (
		('CLEVELS', INT),
		('ASRPLEVELS', SRPLEVELINFO),
    )
        

class GetComponentVersions(NDRCALL):
    opnum = 8
    structure = (
		('PWSZCLSIDORPROGID', LPCWSTR),
    )

class GetComponentVersionsResponse(NDRCALL):
    structure = (
		('PDWVERSIONS', DWORD),
		('PPPARTITIONIDS', GUID),
		('PPCONGLOMERATIONIDS', GUID),
		('PPISPRIVATE', BOOL),
		('PPBITNESS', LONG),
    )
        
OPNUMS = {
0 : (CopyConglomerations,CopyConglomerationsResponse),
1 : (CopyComponentConfiguration,CopyComponentConfigurationResponse),
2 : (AliasComponent,AliasComponentResponse),
3 : (MoveComponentConfiguration,MoveComponentConfigurationResponse),
4 : (GetEventClassesForIID2,GetEventClassesForIID2Response),
5 : (IsSafeToDelete,IsSafeToDeleteResponse),
6 : (FlushPartitionCache,FlushPartitionCacheResponse),
7 : (EnumerateSRPLevels,EnumerateSRPLevelsResponse),
8 : (GetComponentVersions,GetComponentVersionsResponse),
}

#################################################################################

#ICapabilitySupport Definition

#################################################################################

MSRPC_UUID_ICAPABILITYSUPPORT = uuidtup_to_bin(('47CDE9A1-0BF6-11D2-8016-00C04FB9988E','0.0'))


class Start(NDRCALL):
    opnum = 0
    structure = (
		('I_CSS', CATSRVSERVICES),
    )

class StartResponse(NDRCALL):
    structure = (

    )
        

class Stop(NDRCALL):
    opnum = 1
    structure = (
		('I_CSS', CATSRVSERVICES),
    )

class StopResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class IsInstalled(NDRCALL):
    opnum = 4
    structure = (
		('I_CSS', CATSRVSERVICES),
    )

class IsInstalledResponse(NDRCALL):
    structure = (
		('PULSTATUS', ULONG),
    )
        

class IsRunning(NDRCALL):
    opnum = 5
    structure = (
		('I_CSS', CATSRVSERVICES),
    )

class IsRunningResponse(NDRCALL):
    structure = (
		('PULSTATES', CATSRVSERVICESTATE),
    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Start,StartResponse),
1 : (Stop,StopResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
3 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
4 : (IsInstalled,IsInstalledResponse),
5 : (IsRunning,IsRunningResponse),
6 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
}

#################################################################################

#IContainerControl Definition

#################################################################################

MSRPC_UUID_ICONTAINERCONTROL = uuidtup_to_bin(('3F3B1B86-DBBE-11D1-9DA6-00805F85CFE3','0.0'))


class CreateContainer(NDRCALL):
    opnum = 0
    structure = (
		('PCONGLOMERATIONIDENTIFIER', GUID),
    )

class CreateContainerResponse(NDRCALL):
    structure = (

    )
        

class ShutdownContainers(NDRCALL):
    opnum = 1
    structure = (
		('PCONGLOMERATIONIDENTIFIER', GUID),
    )

class ShutdownContainersResponse(NDRCALL):
    structure = (

    )
        

class RefreshComponents(NDRCALL):
    opnum = 2
    structure = (

    )

class RefreshComponentsResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CreateContainer,CreateContainerResponse),
1 : (ShutdownContainers,ShutdownContainersResponse),
2 : (RefreshComponents,RefreshComponentsResponse),
}

#################################################################################

#IContainerControl2 Definition

#################################################################################

MSRPC_UUID_ICONTAINERCONTROL2 = uuidtup_to_bin(('6C935649-30A6-4211-8687-C4C83E5FE1C7','0.0'))


class ShutdownContainer(NDRCALL):
    opnum = 0
    structure = (
		('CONTAINERIDENTIFIER', GUID),
    )

class ShutdownContainerResponse(NDRCALL):
    structure = (

    )
        

class PauseContainer(NDRCALL):
    opnum = 1
    structure = (
		('CONTAINERIDENTIFIER', GUID),
    )

class PauseContainerResponse(NDRCALL):
    structure = (

    )
        

class ResumeContainer(NDRCALL):
    opnum = 2
    structure = (
		('CONTAINERIDENTIFIER', GUID),
    )

class ResumeContainerResponse(NDRCALL):
    structure = (

    )
        

class IsContainerPaused(NDRCALL):
    opnum = 3
    structure = (
		('CONTAINERIDENTIFIER', GUID),
    )

class IsContainerPausedResponse(NDRCALL):
    structure = (
		('BPAUSED', BOOL),
    )
        

class GetRunningContainers(NDRCALL):
    opnum = 4
    structure = (
		('PARTITIONID', GUID),
		('CONGLOMERATIONID', GUID),
    )

class GetRunningContainersResponse(NDRCALL):
    structure = (
		('PDWNUMCONTAINERS', DWORD),
		('PPCONTAINERS', INSTANCECONTAINER),
    )
        

class GetContainerIDFromProcessID(NDRCALL):
    opnum = 5
    structure = (
		('DWPID', DWORD),
    )

class GetContainerIDFromProcessIDResponse(NDRCALL):
    structure = (
		('PBSTRCONTAINERID', BSTR),
    )
        

class RecycleContainer(NDRCALL):
    opnum = 6
    structure = (
		('CONTAINERIDENTIFIER', GUID),
		('LREASONCODE', LONG),
    )

class RecycleContainerResponse(NDRCALL):
    structure = (

    )
        

class GetContainerIDFromConglomerationID(NDRCALL):
    opnum = 7
    structure = (
		('CONGLOMERATIONIDENTIFIER', GUID),
    )

class GetContainerIDFromConglomerationIDResponse(NDRCALL):
    structure = (
		('CONTAINERIDENTIFIER', GUID),
    )
        
OPNUMS = {
0 : (ShutdownContainer,ShutdownContainerResponse),
1 : (PauseContainer,PauseContainerResponse),
2 : (ResumeContainer,ResumeContainerResponse),
3 : (IsContainerPaused,IsContainerPausedResponse),
4 : (GetRunningContainers,GetRunningContainersResponse),
5 : (GetContainerIDFromProcessID,GetContainerIDFromProcessIDResponse),
6 : (RecycleContainer,RecycleContainerResponse),
7 : (GetContainerIDFromConglomerationID,GetContainerIDFromConglomerationIDResponse),
}

#################################################################################

#IReplicationUtil Definition

#################################################################################

MSRPC_UUID_IREPLICATIONUTIL = uuidtup_to_bin(('98315903-7BE5-11D2-ADC1-00A02463D6E7','0.0'))


class CreateShare(NDRCALL):
    opnum = 0
    structure = (
		('PWSZSHARENAME', LPCWSTR),
		('PWSZPATH', LPCWSTR),
    )

class CreateShareResponse(NDRCALL):
    structure = (

    )
        

class CreateEmptyDir(NDRCALL):
    opnum = 1
    structure = (
		('PWSZPATH', LPCWSTR),
    )

class CreateEmptyDirResponse(NDRCALL):
    structure = (

    )
        

class RemoveShare(NDRCALL):
    opnum = 2
    structure = (
		('PWSZSHARENAME', LPCWSTR),
    )

class RemoveShareResponse(NDRCALL):
    structure = (

    )
        

class BeginReplicationAsTarget(NDRCALL):
    opnum = 3
    structure = (
		('PWSZBASEREPLICATIONDIR', LPCWSTR),
    )

class BeginReplicationAsTargetResponse(NDRCALL):
    structure = (

    )
        

class QueryConglomerationPassword(NDRCALL):
    opnum = 4
    structure = (
		('CONGLOMERATIONID', REFGUID),
    )

class QueryConglomerationPasswordResponse(NDRCALL):
    structure = (
		('PPVPASSWORD', CHAR),
		('PCBPASSWORD', ULONG),
    )
        

class CreateReplicationDir(NDRCALL):
    opnum = 5
    structure = (

    )

class CreateReplicationDirResponse(NDRCALL):
    structure = (
		('PPWSZBASEREPLICATIONDIR', LPWSTR),
    )
        
OPNUMS = {
0 : (CreateShare,CreateShareResponse),
1 : (CreateEmptyDir,CreateEmptyDirResponse),
2 : (RemoveShare,RemoveShareResponse),
3 : (BeginReplicationAsTarget,BeginReplicationAsTargetResponse),
4 : (QueryConglomerationPassword,QueryConglomerationPasswordResponse),
5 : (CreateReplicationDir,CreateReplicationDirResponse),
}

