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


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = ORPC_EXTENT

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('size', UNSIGNED_LONG),	('reserved', UNSIGNED_LONG),	('extent', PTR_UNSIGNED_LONG),

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


class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_UNSIGNED_SHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_SHORT),
    )

class UNSIGNED_SHORT(NDRSTRUCT):
    structure = (
	('ClientImpLevel', DWORD),	('cRequestedProtseqs', UNSIGNED_SHORT),	('pRequestedProtseqs', PTR_UNSIGNED_SHORT),

    )
        

class CUSTOMREMOTE_REPLY_SCM_INFO(NDRSTRUCT):
    structure = (
        ('Oxid', OXID),('pdsaOxidBindings', DUALSTRINGARRAY),('ipidRemUnknown', IPID),('authnHint', DWORD),('serverVersion', COMVERSION),
    )


class DATA_COMVERSION(NDRUniConformantArray):
    item = IID

class PTR_COMVERSION(NDRPOINTER):
    referent = (
        ('Data', DATA_COMVERSION),
    )

class COMVERSION(NDRSTRUCT):
    structure = (
	('classId', CLSID),	('classCtx', DWORD),	('actvflags', DWORD),	('fIsSurrogate', LONG),	('cIID', DWORD),	('instFlag', DWORD),	('pIID', PTR_DWORD),
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


class DATA_DWORD(NDRUniConformantArray):
    item = DWORD

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('totalSize', DWORD),	('headerSize', DWORD),	('dwReserved', DWORD),	('destCtx', DWORD),	('cIfs', DWORD),	('classInfoClsid', CLSID),	('pclsid', CLSID),	('pSizes', PTR_CLSID),
	('pdwReserved', DWORD),
    )
        

class DATA_HRESULT(NDRUniConformantArray):
    item = MINTERFACEPOINTER

class PTR_HRESULT(NDRPOINTER):
    referent = (
        ('Data', DATA_HRESULT),
    )

class HRESULT(NDRSTRUCT):
    structure = (
	('cIfs', DWORD),	('piid', IID),	('phresults', HRESULT),	('ppIntfData', PTR_HRESULT),

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

class DATA_MINTERFACEPOINTER(NDRUniConformantArray):
    item = BYTE

class PTR_MINTERFACEPOINTER(NDRPOINTER):
    referent = (
        ('Data', DATA_MINTERFACEPOINTER),
    )

class MINTERFACEPOINTER(NDRSTRUCT):
    structure = (
	('fFlags', ULONG),	('clSize', ULONG),	('pRecInfo', MINTERFACEPOINTER),	('pRecord', PTR_MINTERFACEPOINTER),

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


class DATA_ULONG(NDRUniConformantArray):
    item = BSTR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aBstr', PTR_ULONG),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = IUNKNOWN

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apUnknown', PTR_ULONG),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = IDISPATCH

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apDispatch', PTR_ULONG),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = VARIANT

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aVariant', PTR_ULONG),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = BRECORD

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('aRecord', PTR_ULONG),

    )
        

class DATA_IID(NDRUniConformantArray):
    item = IUNKNOWN

class PTR_IID(NDRPOINTER):
    referent = (
        ('Data', DATA_IID),
    )

class IID(NDRSTRUCT):
    structure = (
	('Size', ULONG),	('apUnknown', PTR_ULONG),
	('iid', IID),
    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = BYTE

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_UNSIGNED_LONG),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_UNSIGNED_LONG),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_UNSIGNED_LONG),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = HYPER

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('clSize', UNSIGNED_LONG),	('pData', PTR_UNSIGNED_LONG),

    )
        

class ANONYMOUS3(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous3', ANONYMOUS3),
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

class DATA_UINT(NDRUniConformantArray):
    item = DISPID

class PTR_UINT(NDRPOINTER):
    referent = (
        ('Data', DATA_UINT),
    )

class UINT(NDRSTRUCT):
    structure = (
	('rgvarg', VARIANT),	('rgdispidNamedArgs', PTR_VARIANT),
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


class DATA_WORD(NDRUniConformantArray):
    item = ELEMDESC

class PTR_WORD(NDRPOINTER):
    referent = (
        ('Data', DATA_WORD),
    )

class WORD(NDRSTRUCT):
    structure = (
	('memid', MEMBERID),	('lReserved1', SCODE),	('lprgelemdescParam', PTR_SCODE),
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


class DATA_DWORD(NDRUniConformantArray):
    item = CUSTDATAITEM

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cCustData', DWORD),	('prgCustData', PTR_DWORD),

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


class BOID(NDRSTRUCT):
    structure = (
        ('rgb', UNSIGNED_CHAR),
    )


class XACTTRANSINFO(NDRSTRUCT):
    structure = (
        ('uow', BOID),('isoLevel', LONG),('isoFlags', ULONG),('grfTCSupported', DWORD),('grfRMSupported', DWORD),('grfTCSupportedRetaining', DWORD),('grfRMSupportedRetaining', DWORD),
    )


XACTTC_NONE = 0,
XACTTC_SYNC_PHASEONE = 1,
XACTTC_SYNC_PHASETWO = 2,
XACTTC_SYNC = 2,
XACTTC_ASYNC_PHASEONE = 4,
XACTTC_ASYNC = 4
        

MQMSG_CALG_MD2 = 32769,
MQMSG_CALG_MD4 = 32770,
MQMSG_CALG_MD5 = 32771,
MQMSG_CALG_SHA = 32772,
MQMSG_CALG_SHA1 = 32772,
MQMSG_CALG_MAC = 32773,
MQMSG_CALG_RSA_SIGN = 9216,
MQMSG_CALG_DSS_SIGN = 8704,
MQMSG_CALG_RSA_KEYX = 41984,
MQMSG_CALG_DES = 26113,
MQMSG_CALG_RC2 = 26114,
MQMSG_CALG_RC4 = 26625,
MQMSG_CALG_SEAL = 26626
        

MQ_NO_TRANSACTION = 0,
MQ_MTS_TRANSACTION = 1,
MQ_XA_TRANSACTION = 2,
MQ_SINGLE_MESSAGE = 3
        

REL_NOP = 0,
REL_EQ = 0,
REL_NEQ = 0,
REL_LT = 0,
REL_GT = 0,
REL_LE = 0
        

MQCERT_REGISTER_ALWAYS = 1,
MQCERT_REGISTER_IF_NOT_EXIST = 2
        

MQMSG_FIRST = 0,
MQMSG_CURRENT = 1,
MQMSG_NEXT = 2
        

MQMSG_CLASS_NORMAL = 0,
MQMSG_CLASS_REPORT = 1,
MQMSG_CLASS_ACK_REACH_QUEUE = 2,
MQMSG_CLASS_ACK_RECEIVE = 16384,
MQMSG_CLASS_NACK_BAD_DST_Q = 32768,
MQMSG_CLASS_NACK_PURGED = 32769,
MQMSG_CLASS_NACK_REACH_QUEUE_TIMEOUT = 32770,
MQMSG_CLASS_NACK_Q_EXCEED_QUOTA = 32771,
MQMSG_CLASS_NACK_ACCESS_DENIED = 32772,
MQMSG_CLASS_NACK_HOP_COUNT_EXCEEDED = 32773,
MQMSG_CLASS_NACK_BAD_SIGNATURE = 32774,
MQMSG_CLASS_NACK_BAD_ENCRYPTION = 32775,
MQMSG_CLASS_NACK_COULD_NOT_ENCRYPT = 32776,
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_Q = 32777,
MQMSG_CLASS_NACK_NOT_TRANSACTIONAL_MSG = 32778,
MQMSG_CLASS_NACK_UNSUPPORTED_CRYPTO_PROVIDER = 32779,
MQMSG_CLASS_NACK_SOURCE_COMPUTER_GUID_CHANGED = 32780,
MQMSG_CLASS_NACK_Q_DELETED = 49152,
MQMSG_CLASS_NACK_Q_PURGED = 49153,
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT = 49154,
MQMSG_CLASS_NACK_RECEIVE_TIMEOUT_AT_SENDER = 49155
        

MQMSG_DELIVERY_EXPRESS = 0,
MQMSG_DELIVERY_RECOVERABLE = 1
        

MQMSG_ACKNOWLEDGMENT_NONE = 0,
MQMSG_ACKNOWLEDGMENT_POS_ARRIVAL = 1,
MQMSG_ACKNOWLEDGMENT_POS_RECEIVE = 2,
MQMSG_ACKNOWLEDGMENT_NEG_ARRIVAL = 4,
MQMSG_ACKNOWLEDGMENT_NEG_RECEIVE = 8,
MQMSG_ACKNOWLEDGMENT_NACK_REACH_QUEUE = 4,
MQMSG_ACKNOWLEDGMENT_FULL_REACH_QUEUE = 5,
MQMSG_ACKNOWLEDGMENT_NACK_RECEIVE = 12,
MQMSG_ACKNOWLEDGMENT_FULL_RECEIVE = 14
        

MQMSG_JOURNAL_NONE = 0,
MQMSG_DEADLETTER = 1,
MQMSG_JOURNAL = 2
        

MQMSG_TRACE_NONE = 0,
MQMSG_SEND_ROUTE_TO_REPORT_QUEUE = 1
        

MQMSG_SENDERID_TYPE_NONE = 0,
MQMSG_SENDERID_TYPE_SID = 1
        

MQMSG_PRIV_LEVEL_NONE = 0,
MQMSG_PRIV_LEVEL_BODY_BASE = 1,
MQMSG_PRIV_LEVEL_BODY_ENHANCED = 3
        

MQMSG_AUTH_LEVEL_NONE = 0,
MQMSG_AUTH_LEVEL_ALWAYS = 1,
MQMSG_AUTH_LEVEL_MSMQ10 = 2,
MQMSG_AUTH_LEVEL_SIG10 = 2,
MQMSG_AUTH_LEVEL_MSMQ20 = 4,
MQMSG_AUTH_LEVEL_SIG20 = 4,
MQMSG_AUTH_LEVEL_SIG30 = 8
        

MQMSG_MSGID_SIZE = 20,
MQMSG_CORRELATIONID_SIZE = 20,
MQMSG_XACTID_SIZE = 20
        

MQ_MAX_MSG_LABEL_LEN = 249
        

MQMSG_AUTHENTICATION_NOT_REQUESTED = 0,
MQMSG_AUTHENTICATION_REQUESTED = 1,
MQMSG_AUTHENTICATED_SIG10 = 1,
MQMSG_AUTHENTICATION_REQUESTED_EX = 3,
MQMSG_AUTHENTICATED_SIG20 = 3,
MQMSG_AUTHENTICATED_SIG30 = 5,
MQMSG_AUTHENTICATED_SIGXML = 9
        

MQ_DENY_NONE = 0,
MQ_DENY_RECEIVE_SHARE = 1
        

MQ_RECEIVE_ACCESS = 1,
MQ_SEND_ACCESS = 2,
MQ_PEEK_ACCESS = 32,
MQ_ADMIN_ACCESS = 128
        

MQ_JOURNAL_NONE = 0,
MQ_JOURNAL = 1
        

MQ_TRANSACTIONAL_NONE = 0,
MQ_TRANSACTIONAL = 1
        

MQ_AUTHENTICATE_NONE = 0,
MQ_AUTHENTICATE = 1
        

MQ_PRIV_LEVEL_NONE = 0,
MQ_PRIV_LEVEL_OPTIONAL = 1,
MQ_PRIV_LEVEL_BODY = 2
        

MQ_MIN_PRIORITY = 0,
MQ_MAX_PRIORITY = 7
        

MQ_MAX_Q_NAME_LEN = 124,
MQ_MAX_Q_LABEL_LEN = 124
        

MQ_TYPE_PUBLIC = ,
MQ_TYPE_PRIVATE = ,
MQ_TYPE_MACHINE = ,
MQ_TYPE_CONNECTOR = 
        

MQ_STATUS_FOREIGN = ,
MQ_STATUS_NOT_FOREIGN = 
        

MQ_XACT_STATUS_XACT = ,
MQ_XACT_STATUS_NOT_XACT = 
        

MQ_QUEUE_STATE_LOCAL_CONNECTION = ,
MQ_QUEUE_STATE_DISCONNECTED = ,
MQ_QUEUE_STATE_WAITING = ,
MQ_QUEUE_STATE_NEEDVALIDATE = ,
MQ_QUEUE_STATE_ONHOLD = ,
MQ_QUEUE_STATE_NONACTIVE = ,
MQ_QUEUE_STATE_CONNECTED = ,
MQ_QUEUE_STATE_DISCONNECTING = 
        

DEFAULT_M_PRIORITY = 3,
DEFAULT_M_DELIVERY = 0,
DEFAULT_M_ACKNOWLEDGE = 0,
DEFAULT_M_JOURNAL = 0,
DEFAULT_M_APPSPECIFIC = 0,
DEFAULT_M_PRIV_LEVEL = 0,
DEFAULT_M_AUTH_LEVEL = 0,
DEFAULT_M_SENDERID_TYPE = 1,
DEFAULT_Q_JOURNAL = 0,
DEFAULT_Q_BASEPRIORITY = 0,
DEFAULT_Q_QUOTA = 4294967295,
DEFAULT_Q_JOURNAL_QUOTA = 4294967295,
DEFAULT_Q_TRANSACTION = 0,
DEFAULT_Q_AUTHENTICATE = 0,
DEFAULT_Q_PRIV_LEVEL = 1,
DEFAULT_M_LOOKUPID = 0
        

MQ_ERROR = 3222142977,
MQ_ERROR_PROPERTY = 3222142978,
MQ_ERROR_QUEUE_NOT_FOUND = 3222142979,
MQ_ERROR_QUEUE_NOT_ACTIVE = 3222142980,
MQ_ERROR_QUEUE_EXISTS = 3222142981,
MQ_ERROR_INVALID_PARAMETER = 3222142982,
MQ_ERROR_INVALID_HANDLE = 3222142983,
MQ_ERROR_OPERATION_CANCELLED = 3222142984,
MQ_ERROR_SHARING_VIOLATION = 3222142985,
MQ_ERROR_SERVICE_NOT_AVAILABLE = 3222142987,
MQ_ERROR_MACHINE_NOT_FOUND = 3222142989,
MQ_ERROR_ILLEGAL_SORT = 3222142992,
MQ_ERROR_ILLEGAL_USER = 3222142993,
MQ_ERROR_NO_DS = 3222142995,
MQ_ERROR_ILLEGAL_QUEUE_PATHNAME = 3222142996,
MQ_ERROR_ILLEGAL_PROPERTY_VALUE = 3222143000,
MQ_ERROR_ILLEGAL_PROPERTY_VT = 3222143001,
MQ_ERROR_BUFFER_OVERFLOW = 3222143002,
MQ_ERROR_IO_TIMEOUT = 3222143003,
MQ_ERROR_ILLEGAL_CURSOR_ACTION = 3222143004,
MQ_ERROR_MESSAGE_ALREADY_RECEIVED = 3222143005,
MQ_ERROR_ILLEGAL_FORMATNAME = 3222143006,
MQ_ERROR_FORMATNAME_BUFFER_TOO_SMALL = 3222143007,
MQ_ERROR_UNSUPPORTED_FORMATNAME_OPERATION = 3222143008,
MQ_ERROR_ILLEGAL_SECURITY_DESCRIPTOR = 3222143009,
MQ_ERROR_SENDERID_BUFFER_TOO_SMALL = 3222143010,
MQ_ERROR_SECURITY_DESCRIPTOR_TOO_SMALL = 3222143011,
MQ_ERROR_CANNOT_IMPERSONATE_CLIENT = 3222143012,
MQ_ERROR_ACCESS_DENIED = 3222143013,
MQ_ERROR_PRIVILEGE_NOT_HELD = 3222143014,
MQ_ERROR_INSUFFICIENT_RESOURCES = 3222143015,
MQ_ERROR_USER_BUFFER_TOO_SMALL = 3222143016,
MQ_ERROR_MESSAGE_STORAGE_FAILED = 3222143018,
MQ_ERROR_SENDER_CERT_BUFFER_TOO_SMALL = 3222143019,
MQ_ERROR_INVALID_CERTIFICATE = 3222143020,
MQ_ERROR_CORRUPTED_INTERNAL_CERTIFICATE = 3222143021,
MQ_ERROR_INTERNAL_USER_CERT_EXIST = 3222143022,
MQ_ERROR_NO_INTERNAL_USER_CERT = 3222143023,
MQ_ERROR_CORRUPTED_SECURITY_DATA = 3222143024,
MQ_ERROR_CORRUPTED_PERSONAL_CERT_STORE = 3222143025,
MQ_ERROR_COMPUTER_DOES_NOT_SUPPORT_ENCRYPTION = 3222143027,
MQ_ERROR_BAD_SECURITY_CONTEXT = 3222143029,
MQ_ERROR_COULD_NOT_GET_USER_SID = 3222143030,
MQ_ERROR_COULD_NOT_GET_ACCOUNT_INFO = 3222143031,
MQ_ERROR_ILLEGAL_MQCOLUMNS = 3222143032,
MQ_ERROR_ILLEGAL_PROPID = 3222143033,
MQ_ERROR_ILLEGAL_RELATION = 3222143034,
MQ_ERROR_ILLEGAL_PROPERTY_SIZE = 3222143035,
MQ_ERROR_ILLEGAL_RESTRICTION_PROPID = 3222143036,
MQ_ERROR_ILLEGAL_MQQUEUEPROPS = 3222143037,
MQ_ERROR_PROPERTY_NOTALLOWED = 3222143038,
MQ_ERROR_INSUFFICIENT_PROPERTIES = 3222143039,
MQ_ERROR_MACHINE_EXISTS = 3222143040,
MQ_ERROR_ILLEGAL_MQQMPROPS = 3222143041,
MQ_ERROR_DS_IS_FULL = 3222143042,
MQ_ERROR_DS_ERROR = 3222143043,
MQ_ERROR_INVALID_OWNER = 3222143044,
MQ_ERROR_UNSUPPORTED_ACCESS_MODE = 3222143045,
MQ_ERROR_RESULT_BUFFER_TOO_SMALL = 3222143046,
MQ_ERROR_DELETE_CN_IN_USE = 3222143048,
MQ_ERROR_NO_RESPONSE_FROM_OBJECT_SERVER = 3222143049,
MQ_ERROR_OBJECT_SERVER_NOT_AVAILABLE = 3222143050,
MQ_ERROR_QUEUE_NOT_AVAILABLE = 3222143051,
MQ_ERROR_DTC_CONNECT = 3222143052,
MQ_ERROR_TRANSACTION_IMPORT = 3222143054,
MQ_ERROR_TRANSACTION_USAGE = 3222143056,
MQ_ERROR_TRANSACTION_SEQUENCE = 3222143057,
MQ_ERROR_MISSING_CONNECTOR_TYPE = 3222143061,
MQ_ERROR_STALE_HANDLE = 3222143062,
MQ_ERROR_TRANSACTION_ENLIST = 3222143064,
MQ_ERROR_QUEUE_DELETED = 3222143066,
MQ_ERROR_ILLEGAL_CONTEXT = 3222143067,
MQ_ERROR_ILLEGAL_SORT_PROPID = 3222143068,
MQ_ERROR_LABEL_TOO_LONG = 3222143069,
MQ_ERROR_LABEL_BUFFER_TOO_SMALL = 3222143070,
MQ_ERROR_MQIS_SERVER_EMPTY = 3222143071,
MQ_ERROR_MQIS_READONLY_MODE = 3222143072,
MQ_ERROR_SYMM_KEY_BUFFER_TOO_SMALL = 3222143073,
MQ_ERROR_SIGNATURE_BUFFER_TOO_SMALL = 3222143074,
MQ_ERROR_PROV_NAME_BUFFER_TOO_SMALL = 3222143075,
MQ_ERROR_ILLEGAL_OPERATION = 3222143076,
MQ_ERROR_WRITE_NOT_ALLOWED = 3222143077,
MQ_ERROR_WKS_CANT_SERVE_CLIENT = 3222143078,
MQ_ERROR_DEPEND_WKS_LICENSE_OVERFLOW = 3222143079,
MQ_CORRUPTED_QUEUE_WAS_DELETED = 3222143080,
MQ_ERROR_REMOTE_MACHINE_NOT_AVAILABLE = 3222143081,
MQ_ERROR_UNSUPPORTED_OPERATION = 3222143082,
MQ_ERROR_ENCRYPTION_PROVIDER_NOT_SUPPORTED = 3222143083,
MQ_ERROR_CANNOT_SET_CRYPTO_SEC_DESCR = 3222143084,
MQ_ERROR_CERTIFICATE_NOT_PROVIDED = 3222143085,
MQ_ERROR_Q_DNS_PROPERTY_NOT_SUPPORTED = 3222143086,
MQ_ERROR_CANT_CREATE_CERT_STORE = 3222143087,
MQ_ERROR_CANNOT_CREATE_CERT_STORE = 3222143087,
MQ_ERROR_CANT_OPEN_CERT_STORE = 3222143088,
MQ_ERROR_CANNOT_OPEN_CERT_STORE = 3222143088,
MQ_ERROR_ILLEGAL_ENTERPRISE_OPERATION = 3222143089,
MQ_ERROR_CANNOT_GRANT_ADD_GUID = 3222143090,
MQ_ERROR_CANNOT_LOAD_MSMQOCM = 3222143091,
MQ_ERROR_NO_ENTRY_POINT_MSMQOCM = 3222143092,
MQ_ERROR_NO_MSMQ_SERVERS_ON_DC = 3222143093,
MQ_ERROR_CANNOT_JOIN_DOMAIN = 3222143094,
MQ_ERROR_CANNOT_CREATE_ON_GC = 3222143095,
MQ_ERROR_GUID_NOT_MATCHING = 3222143096,
MQ_ERROR_PUBLIC_KEY_NOT_FOUND = 3222143097,
MQ_ERROR_PUBLIC_KEY_DOES_NOT_EXIST = 3222143098,
MQ_ERROR_ILLEGAL_MQPRIVATEPROPS = 3222143099,
MQ_ERROR_NO_GC_IN_DOMAIN = 3222143100,
MQ_ERROR_NO_MSMQ_SERVERS_ON_GC = 3222143101,
MQ_ERROR_CANNOT_GET_DN = 3222143102,
MQ_ERROR_CANNOT_HASH_DATA_EX = 3222143103,
MQ_ERROR_CANNOT_SIGN_DATA_EX = 3222143104,
MQ_ERROR_CANNOT_CREATE_HASH_EX = 3222143105,
MQ_ERROR_FAIL_VERIFY_SIGNATURE_EX = 3222143106,
MQ_ERROR_CANNOT_DELETE_PSC_OBJECTS = 3222143107,
MQ_ERROR_NO_MQUSER_OU = 3222143108,
MQ_ERROR_CANNOT_LOAD_MQAD = 3222143109,
MQ_ERROR_CANNOT_LOAD_MQDSSRV = 3222143110,
MQ_ERROR_PROPERTIES_CONFLICT = 3222143111,
MQ_ERROR_MESSAGE_NOT_FOUND = 3222143112,
MQ_ERROR_CANT_RESOLVE_SITES = 3222143113,
MQ_ERROR_NOT_SUPPORTED_BY_DEPENDENT_CLIENTS = 3222143114,
MQ_ERROR_OPERATION_NOT_SUPPORTED_BY_REMOTE_COMPUTER = 3222143115,
MQ_ERROR_NOT_A_CORRECT_OBJECT_CLASS = 3222143116,
MQ_ERROR_MULTI_SORT_KEYS = 3222143117,
MQ_ERROR_GC_NEEDED = 3222143118,
MQ_ERROR_DS_BIND_ROOT_FOREST = 3222143119,
MQ_ERROR_DS_LOCAL_USER = 3222143120,
MQ_ERROR_Q_ADS_PROPERTY_NOT_SUPPORTED = 3222143121,
MQ_ERROR_BAD_XML_FORMAT = 3222143122,
MQ_ERROR_UNSUPPORTED_CLASS = 3222143123,
MQ_ERROR_UNINITIALIZED_OBJECT = 3222143124,
MQ_ERROR_CANNOT_CREATE_PSC_OBJECTS = 3222143125,
MQ_ERROR_CANNOT_UPDATE_PSC_OBJECTS = 3222143126
        

MQ_INFORMATION_PROPERTY = 1074659329,
MQ_INFORMATION_ILLEGAL_PROPERTY = 1074659330,
MQ_INFORMATION_PROPERTY_IGNORED = 1074659331,
MQ_INFORMATION_UNSUPPORTED_PROPERTY = 1074659332,
MQ_INFORMATION_DUPLICATE_PROPERTY = 1074659333,
MQ_INFORMATION_OPERATION_PENDING = 1074659334,
MQ_INFORMATION_FORMATNAME_BUFFER_TOO_SMALL = 1074659337,
MQ_INFORMATION_INTERNAL_USER_CERT_EXIST = 1074659338,
MQ_INFORMATION_OWNER_IGNORED = 1074659339
        
#################################################################################

#CONSTANTS

#################################################################################

ICONNECTIONPOINTCONTAINER = 
IMSMQQUERY = 
IMSMQQUEUEINFO = 
IMSMQQUEUEINFO2 = 
IMSMQQUEUEINFO3 = 
IMSMQQUEUEINFO4 = 
IMSMQQUEUE = 
IMSMQQUEUE2 = 
IMSMQQUEUE3 = 
IMSMQQUEUE4 = 
IMSMQMESSAGE = 
IMSMQQUEUEINFOS = 
IMSMQQUEUEINFOS2 = 
IMSMQQUEUEINFOS3 = 
IMSMQQUEUEINFOS4 = 
IMSMQEVENT = 
IMSMQEVENT2 = 
IMSMQEVENT3 = 
IMSMQTRANSACTION = 
IMSMQCOORDINATEDTRANSACTIONDISPENSER = 
IMSMQTRANSACTIONDISPENSER = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#ITransaction Definition

#################################################################################

MSRPC_UUID_ITRANSACTION = uuidtup_to_bin(('0fb15084-af41-11ce-bd2b-204c4f4f5020','0.0'))


class Commit(NDRCALL):
    opnum = 0
    structure = (
		('fRetaining', SHORT),
		('grfTC', DWORD),
		('grfRM', DWORD),
    )

class CommitResponse(NDRCALL):
    structure = (

    )
        

class Abort(NDRCALL):
    opnum = 1
    structure = (
		('pboidReason', BOID),
		('fRetaining', SHORT),
		('fAsync', SHORT),
    )

class AbortResponse(NDRCALL):
    structure = (

    )
        

class GetTransactionInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class GetTransactionInfoResponse(NDRCALL):
    structure = (
		('pinfo', XACTTRANSINFO),
    )
        
OPNUMS = {
0 : (Commit,CommitResponse),
1 : (Abort,AbortResponse),
2 : (GetTransactionInfo,GetTransactionInfoResponse),
}

#################################################################################

#IEnumConnections Definition

#################################################################################

MSRPC_UUID_IENUMCONNECTIONS = uuidtup_to_bin(('B196B287-BAB4-101-B69C-00A00341D07','0.0'))

PENUMCONNECTIONS = IENUMCONNECTIONS
LPENUMCONNECTIONS = IENUMCONNECTIONS

class CONNECTDATA(NDRSTRUCT):
    structure = (
        ('pUnk', IUNKNOWN),('dwCookie', DWORD),
    )


class PCONNECTDATA(NDRSTRUCT):
    structure = (
        
    )


class LPCONNECTDATA(NDRSTRUCT):
    structure = (
        
    )


class Next(NDRCALL):
    opnum = 0
    structure = (
		('cConnections', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('rgcd', LPCONNECTDATA),
		('pcFetched', ULONG),
    )
        

class Skip(NDRCALL):
    opnum = 1
    structure = (
		('cConnections', ULONG),
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
		('ppEnum', IENUMCONNECTIONS),
    )
        
OPNUMS = {
0 : (Next,NextResponse),
1 : (Skip,SkipResponse),
2 : (Reset,ResetResponse),
3 : (Clone,CloneResponse),
}

#################################################################################

#IConnectionPoint Definition

#################################################################################

MSRPC_UUID_ICONNECTIONPOINT = uuidtup_to_bin(('B196B286-BAB4-101-B69C-00A00341D07','0.0'))

PCONNECTIONPOINT = ICONNECTIONPOINT
LPCONNECTIONPOINT = ICONNECTIONPOINT

class GetConnectionInterface(NDRCALL):
    opnum = 0
    structure = (

    )

class GetConnectionInterfaceResponse(NDRCALL):
    structure = (
		('pIID', IID),
    )
        

class GetConnectionPointContainer(NDRCALL):
    opnum = 1
    structure = (

    )

class GetConnectionPointContainerResponse(NDRCALL):
    structure = (
		('ppCPC', ICONNECTIONPOINTCONTAINER),
    )
        

class Advise(NDRCALL):
    opnum = 2
    structure = (
		('pUnkSink', IUNKNOWN),
    )

class AdviseResponse(NDRCALL):
    structure = (
		('pdwCookie', DWORD),
    )
        

class Unadvise(NDRCALL):
    opnum = 3
    structure = (
		('dwCookie', DWORD),
    )

class UnadviseResponse(NDRCALL):
    structure = (

    )
        

class EnumConnections(NDRCALL):
    opnum = 4
    structure = (

    )

class EnumConnectionsResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMCONNECTIONS),
    )
        
OPNUMS = {
0 : (GetConnectionInterface,GetConnectionInterfaceResponse),
1 : (GetConnectionPointContainer,GetConnectionPointContainerResponse),
2 : (Advise,AdviseResponse),
3 : (Unadvise,UnadviseResponse),
4 : (EnumConnections,EnumConnectionsResponse),
}

#################################################################################

#IEnumConnectionPoints Definition

#################################################################################

MSRPC_UUID_IENUMCONNECTIONPOINTS = uuidtup_to_bin(('B196B285-BAB4-101-B69C-00A00341D07','0.0'))

PENUMCONNECTIONPOINTS = IENUMCONNECTIONPOINTS
LPENUMCONNECTIONPOINTS = IENUMCONNECTIONPOINTS

class Next(NDRCALL):
    opnum = 0
    structure = (
		('cConnections', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('ppCP', LPCONNECTIONPOINT),
		('pcFetched', ULONG),
    )
        

class Skip(NDRCALL):
    opnum = 1
    structure = (
		('cConnections', ULONG),
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
		('ppEnum', IENUMCONNECTIONPOINTS),
    )
        
OPNUMS = {
0 : (Next,NextResponse),
1 : (Skip,SkipResponse),
2 : (Reset,ResetResponse),
3 : (Clone,CloneResponse),
}

#################################################################################

#IConnectionPointContainer Definition

#################################################################################

MSRPC_UUID_ICONNECTIONPOINTCONTAINER = uuidtup_to_bin(('B196B284-BAB4-101-B69C-00A00341D07','0.0'))

PCONNECTIONPOINTCONTAINER = ICONNECTIONPOINTCONTAINER
LPCONNECTIONPOINTCONTAINER = ICONNECTIONPOINTCONTAINER

class EnumConnectionPoints(NDRCALL):
    opnum = 0
    structure = (

    )

class EnumConnectionPointsResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMCONNECTIONPOINTS),
    )
        

class FindConnectionPoint(NDRCALL):
    opnum = 1
    structure = (
		('riid', REFIID),
    )

class FindConnectionPointResponse(NDRCALL):
    structure = (
		('ppCP', ICONNECTIONPOINT),
    )
        
OPNUMS = {
0 : (EnumConnectionPoints,EnumConnectionPointsResponse),
1 : (FindConnectionPoint,FindConnectionPointResponse),
}

#################################################################################

#IMSMQQuery Definition

#################################################################################

MSRPC_UUID_IMSMQQUERY = uuidtup_to_bin(('D7D6E072-DCCD-110-AA4B-0060970EBAE','0.0'))


class LookupQueue(NDRCALL):
    opnum = 0
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
    )

class LookupQueueResponse(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS),
    )
        
OPNUMS = {
0 : (LookupQueue,LookupQueueResponse),
}

#################################################################################

#IMSMQQuery2 Definition

#################################################################################

MSRPC_UUID_IMSMQQUERY2 = uuidtup_to_bin(('eba96b0e-2168-113-898-00020746','0.0'))


class LookupQueue(NDRCALL):
    opnum = 0
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
    )

class LookupQueueResponse(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS2),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (LookupQueue,LookupQueueResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQQuery3 Definition

#################################################################################

MSRPC_UUID_IMSMQQUERY3 = uuidtup_to_bin(('eba96b19-2168-113-898-00020746','0.0'))


class LookupQueue_v2(NDRCALL):
    opnum = 0
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
    )

class LookupQueue_v2Response(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS3),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class LookupQueue(NDRCALL):
    opnum = 2
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
		('MulticastAddress', VARIANT),
		('RelMulticastAddress', VARIANT),
    )

class LookupQueueResponse(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS3),
    )
        
OPNUMS = {
0 : (LookupQueue_v2,LookupQueue_v2Response),
1 : (Properties,PropertiesResponse),
2 : (LookupQueue,LookupQueueResponse),
}

#################################################################################

#IMSMQQuery4 Definition

#################################################################################

MSRPC_UUID_IMSMQQUERY4 = uuidtup_to_bin(('eba96b24-2168-113-898-00020746','0.0'))


class LookupQueue_v2(NDRCALL):
    opnum = 0
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
    )

class LookupQueue_v2Response(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS4),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class LookupQueue(NDRCALL):
    opnum = 2
    structure = (
		('QueueGuid', VARIANT),
		('ServiceTypeGuid', VARIANT),
		('Label', VARIANT),
		('CreateTime', VARIANT),
		('ModifyTime', VARIANT),
		('RelServiceType', VARIANT),
		('RelLabel', VARIANT),
		('RelCreateTime', VARIANT),
		('RelModifyTime', VARIANT),
		('MulticastAddress', VARIANT),
		('RelMulticastAddress', VARIANT),
    )

class LookupQueueResponse(NDRCALL):
    structure = (
		('ppqinfos', IMSMQQUEUEINFOS4),
    )
        
OPNUMS = {
0 : (LookupQueue_v2,LookupQueue_v2Response),
1 : (Properties,PropertiesResponse),
2 : (LookupQueue,LookupQueueResponse),
}

#################################################################################

#IMSMQMessage Definition

#################################################################################

MSRPC_UUID_IMSMQMESSAGE = uuidtup_to_bin(('D7D6E074-DCCD-110-AA4B-0060970EBAE','0.0'))


class Class(NDRCALL):
    opnum = 0
    structure = (

    )

class ClassResponse(NDRCALL):
    structure = (
		('plClass', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 1
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 2
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class AuthLevel(NDRCALL):
    opnum = 3
    structure = (

    )

class AuthLevelResponse(NDRCALL):
    structure = (
		('plAuthLevel', LONG),
    )
        

class AuthLevel(NDRCALL):
    opnum = 4
    structure = (
		('lAuthLevel', LONG),
    )

class AuthLevelResponse(NDRCALL):
    structure = (

    )
        

class IsAuthenticated(NDRCALL):
    opnum = 5
    structure = (

    )

class IsAuthenticatedResponse(NDRCALL):
    structure = (
		('pisAuthenticated', SHORT),
    )
        

class Delivery(NDRCALL):
    opnum = 6
    structure = (

    )

class DeliveryResponse(NDRCALL):
    structure = (
		('plDelivery', LONG),
    )
        

class Delivery(NDRCALL):
    opnum = 7
    structure = (
		('lDelivery', LONG),
    )

class DeliveryResponse(NDRCALL):
    structure = (

    )
        

class Trace(NDRCALL):
    opnum = 8
    structure = (

    )

class TraceResponse(NDRCALL):
    structure = (
		('plTrace', LONG),
    )
        

class Trace(NDRCALL):
    opnum = 9
    structure = (
		('lTrace', LONG),
    )

class TraceResponse(NDRCALL):
    structure = (

    )
        

class Priority(NDRCALL):
    opnum = 10
    structure = (

    )

class PriorityResponse(NDRCALL):
    structure = (
		('plPriority', LONG),
    )
        

class Priority(NDRCALL):
    opnum = 11
    structure = (
		('lPriority', LONG),
    )

class PriorityResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 14
    structure = (

    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 15
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO),
    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class AppSpecific(NDRCALL):
    opnum = 16
    structure = (

    )

class AppSpecificResponse(NDRCALL):
    structure = (
		('plAppSpecific', LONG),
    )
        

class AppSpecific(NDRCALL):
    opnum = 17
    structure = (
		('lAppSpecific', LONG),
    )

class AppSpecificResponse(NDRCALL):
    structure = (

    )
        

class SourceMachineGuid(NDRCALL):
    opnum = 18
    structure = (

    )

class SourceMachineGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidSrcMachine', BSTR),
    )
        

class BodyLength(NDRCALL):
    opnum = 19
    structure = (

    )

class BodyLengthResponse(NDRCALL):
    structure = (
		('pcbBody', LONG),
    )
        

class Body(NDRCALL):
    opnum = 20
    structure = (

    )

class BodyResponse(NDRCALL):
    structure = (
		('pvarBody', VARIANT),
    )
        

class Body(NDRCALL):
    opnum = 21
    structure = (
		('varBody', VARIANT),
    )

class BodyResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 22
    structure = (

    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO),
    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 23
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO),
    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class Id(NDRCALL):
    opnum = 24
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 25
    structure = (

    )

class CorrelationIdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 26
    structure = (
		('varMsgId', VARIANT),
    )

class CorrelationIdResponse(NDRCALL):
    structure = (

    )
        

class Ack(NDRCALL):
    opnum = 27
    structure = (

    )

class AckResponse(NDRCALL):
    structure = (
		('plAck', LONG),
    )
        

class Ack(NDRCALL):
    opnum = 28
    structure = (
		('lAck', LONG),
    )

class AckResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 29
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 30
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 31
    structure = (

    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (
		('plMaxTimeToReachQueue', LONG),
    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 32
    structure = (
		('lMaxTimeToReachQueue', LONG),
    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 33
    structure = (

    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (
		('plMaxTimeToReceive', LONG),
    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 34
    structure = (
		('lMaxTimeToReceive', LONG),
    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (

    )
        

class HashAlgorithm(NDRCALL):
    opnum = 35
    structure = (

    )

class HashAlgorithmResponse(NDRCALL):
    structure = (
		('plHashAlg', LONG),
    )
        

class HashAlgorithm(NDRCALL):
    opnum = 36
    structure = (
		('lHashAlg', LONG),
    )

class HashAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 37
    structure = (

    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (
		('plEncryptAlg', LONG),
    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 38
    structure = (
		('lEncryptAlg', LONG),
    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class SentTime(NDRCALL):
    opnum = 39
    structure = (

    )

class SentTimeResponse(NDRCALL):
    structure = (
		('pvarSentTime', VARIANT),
    )
        

class ArrivedTime(NDRCALL):
    opnum = 40
    structure = (

    )

class ArrivedTimeResponse(NDRCALL):
    structure = (
		('plArrivedTime', VARIANT),
    )
        

class DestinationQueueInfo(NDRCALL):
    opnum = 41
    structure = (

    )

class DestinationQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoDest', IMSMQQUEUEINFO),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 42
    structure = (

    )

class SenderCertificateResponse(NDRCALL):
    structure = (
		('pvarSenderCert', VARIANT),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 43
    structure = (
		('varSenderCert', VARIANT),
    )

class SenderCertificateResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 44
    structure = (

    )

class SenderIdResponse(NDRCALL):
    structure = (
		('pvarSenderId', VARIANT),
    )
        

class SenderIdType(NDRCALL):
    opnum = 45
    structure = (

    )

class SenderIdTypeResponse(NDRCALL):
    structure = (
		('plSenderIdType', LONG),
    )
        

class SenderIdType(NDRCALL):
    opnum = 46
    structure = (
		('lSenderIdType', LONG),
    )

class SenderIdTypeResponse(NDRCALL):
    structure = (

    )
        

class Send(NDRCALL):
    opnum = 47
    structure = (
		('DestinationQueue', IMSMQQUEUE),
		('Transaction', VARIANT),
    )

class SendResponse(NDRCALL):
    structure = (

    )
        

class AttachCurrentSecurityContext(NDRCALL):
    opnum = 48
    structure = (

    )

class AttachCurrentSecurityContextResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Class,ClassResponse),
1 : (PrivLevel,PrivLevelResponse),
2 : (AuthLevel,AuthLevelResponse),
3 : (IsAuthenticated,IsAuthenticatedResponse),
4 : (Delivery,DeliveryResponse),
5 : (Trace,TraceResponse),
6 : (Priority,PriorityResponse),
7 : (Journal,JournalResponse),
8 : (ResponseQueueInfo,ResponseQueueInfoResponse),
9 : (AppSpecific,AppSpecificResponse),
10 : (SourceMachineGuid,SourceMachineGuidResponse),
11 : (BodyLength,BodyLengthResponse),
12 : (Body,BodyResponse),
13 : (AdminQueueInfo,AdminQueueInfoResponse),
14 : (Id,IdResponse),
15 : (CorrelationId,CorrelationIdResponse),
16 : (Ack,AckResponse),
17 : (Label,LabelResponse),
18 : (MaxTimeToReachQueue,MaxTimeToReachQueueResponse),
19 : (MaxTimeToReceive,MaxTimeToReceiveResponse),
20 : (HashAlgorithm,HashAlgorithmResponse),
21 : (EncryptAlgorithm,EncryptAlgorithmResponse),
22 : (SentTime,SentTimeResponse),
23 : (ArrivedTime,ArrivedTimeResponse),
24 : (DestinationQueueInfo,DestinationQueueInfoResponse),
25 : (SenderCertificate,SenderCertificateResponse),
26 : (SenderId,SenderIdResponse),
27 : (SenderIdType,SenderIdTypeResponse),
28 : (Send,SendResponse),
29 : (AttachCurrentSecurityContext,AttachCurrentSecurityContextResponse),
}

#################################################################################

#IMSMQMessage2 Definition

#################################################################################

MSRPC_UUID_IMSMQMESSAGE2 = uuidtup_to_bin(('D9933BE0-A567-112-B0F3-00020746','0.0'))


class Class(NDRCALL):
    opnum = 0
    structure = (

    )

class ClassResponse(NDRCALL):
    structure = (
		('plClass', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 1
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 2
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class AuthLevel(NDRCALL):
    opnum = 3
    structure = (

    )

class AuthLevelResponse(NDRCALL):
    structure = (
		('plAuthLevel', LONG),
    )
        

class AuthLevel(NDRCALL):
    opnum = 4
    structure = (
		('lAuthLevel', LONG),
    )

class AuthLevelResponse(NDRCALL):
    structure = (

    )
        

class IsAuthenticated(NDRCALL):
    opnum = 5
    structure = (

    )

class IsAuthenticatedResponse(NDRCALL):
    structure = (
		('pisAuthenticated', SHORT),
    )
        

class Delivery(NDRCALL):
    opnum = 6
    structure = (

    )

class DeliveryResponse(NDRCALL):
    structure = (
		('plDelivery', LONG),
    )
        

class Delivery(NDRCALL):
    opnum = 7
    structure = (
		('lDelivery', LONG),
    )

class DeliveryResponse(NDRCALL):
    structure = (

    )
        

class Trace(NDRCALL):
    opnum = 8
    structure = (

    )

class TraceResponse(NDRCALL):
    structure = (
		('plTrace', LONG),
    )
        

class Trace(NDRCALL):
    opnum = 9
    structure = (
		('lTrace', LONG),
    )

class TraceResponse(NDRCALL):
    structure = (

    )
        

class Priority(NDRCALL):
    opnum = 10
    structure = (

    )

class PriorityResponse(NDRCALL):
    structure = (
		('plPriority', LONG),
    )
        

class Priority(NDRCALL):
    opnum = 11
    structure = (
		('lPriority', LONG),
    )

class PriorityResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 14
    structure = (

    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO),
    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 15
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO),
    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class AppSpecific(NDRCALL):
    opnum = 16
    structure = (

    )

class AppSpecificResponse(NDRCALL):
    structure = (
		('plAppSpecific', LONG),
    )
        

class AppSpecific(NDRCALL):
    opnum = 17
    structure = (
		('lAppSpecific', LONG),
    )

class AppSpecificResponse(NDRCALL):
    structure = (

    )
        

class SourceMachineGuid(NDRCALL):
    opnum = 18
    structure = (

    )

class SourceMachineGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidSrcMachine', BSTR),
    )
        

class BodyLength(NDRCALL):
    opnum = 19
    structure = (

    )

class BodyLengthResponse(NDRCALL):
    structure = (
		('pcbBody', LONG),
    )
        

class Body(NDRCALL):
    opnum = 20
    structure = (

    )

class BodyResponse(NDRCALL):
    structure = (
		('pvarBody', VARIANT),
    )
        

class Body(NDRCALL):
    opnum = 21
    structure = (
		('varBody', VARIANT),
    )

class BodyResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 22
    structure = (

    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO),
    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 23
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO),
    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class Id(NDRCALL):
    opnum = 24
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 25
    structure = (

    )

class CorrelationIdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 26
    structure = (
		('varMsgId', VARIANT),
    )

class CorrelationIdResponse(NDRCALL):
    structure = (

    )
        

class Ack(NDRCALL):
    opnum = 27
    structure = (

    )

class AckResponse(NDRCALL):
    structure = (
		('plAck', LONG),
    )
        

class Ack(NDRCALL):
    opnum = 28
    structure = (
		('lAck', LONG),
    )

class AckResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 29
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 30
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 31
    structure = (

    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (
		('plMaxTimeToReachQueue', LONG),
    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 32
    structure = (
		('lMaxTimeToReachQueue', LONG),
    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 33
    structure = (

    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (
		('plMaxTimeToReceive', LONG),
    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 34
    structure = (
		('lMaxTimeToReceive', LONG),
    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (

    )
        

class HashAlgorithm(NDRCALL):
    opnum = 35
    structure = (

    )

class HashAlgorithmResponse(NDRCALL):
    structure = (
		('plHashAlg', LONG),
    )
        

class HashAlgorithm(NDRCALL):
    opnum = 36
    structure = (
		('lHashAlg', LONG),
    )

class HashAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 37
    structure = (

    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (
		('plEncryptAlg', LONG),
    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 38
    structure = (
		('lEncryptAlg', LONG),
    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class SentTime(NDRCALL):
    opnum = 39
    structure = (

    )

class SentTimeResponse(NDRCALL):
    structure = (
		('pvarSentTime', VARIANT),
    )
        

class ArrivedTime(NDRCALL):
    opnum = 40
    structure = (

    )

class ArrivedTimeResponse(NDRCALL):
    structure = (
		('plArrivedTime', VARIANT),
    )
        

class DestinationQueueInfo(NDRCALL):
    opnum = 41
    structure = (

    )

class DestinationQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoDest', IMSMQQUEUEINFO2),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 42
    structure = (

    )

class SenderCertificateResponse(NDRCALL):
    structure = (
		('pvarSenderCert', VARIANT),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 43
    structure = (
		('varSenderCert', VARIANT),
    )

class SenderCertificateResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 44
    structure = (

    )

class SenderIdResponse(NDRCALL):
    structure = (
		('pvarSenderId', VARIANT),
    )
        

class SenderIdType(NDRCALL):
    opnum = 45
    structure = (

    )

class SenderIdTypeResponse(NDRCALL):
    structure = (
		('plSenderIdType', LONG),
    )
        

class SenderIdType(NDRCALL):
    opnum = 46
    structure = (
		('lSenderIdType', LONG),
    )

class SenderIdTypeResponse(NDRCALL):
    structure = (

    )
        

class Send(NDRCALL):
    opnum = 47
    structure = (
		('DestinationQueue', IMSMQQUEUE2),
		('Transaction', VARIANT),
    )

class SendResponse(NDRCALL):
    structure = (

    )
        

class AttachCurrentSecurityContext(NDRCALL):
    opnum = 48
    structure = (

    )

class AttachCurrentSecurityContextResponse(NDRCALL):
    structure = (

    )
        

class SenderVersion(NDRCALL):
    opnum = 49
    structure = (

    )

class SenderVersionResponse(NDRCALL):
    structure = (
		('plSenderVersion', LONG),
    )
        

class Extension(NDRCALL):
    opnum = 50
    structure = (

    )

class ExtensionResponse(NDRCALL):
    structure = (
		('pvarExtension', VARIANT),
    )
        

class Extension(NDRCALL):
    opnum = 51
    structure = (
		('varExtension', VARIANT),
    )

class ExtensionResponse(NDRCALL):
    structure = (

    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 52
    structure = (

    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidConnectorType', BSTR),
    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 53
    structure = (
		('bstrGuidConnectorType', BSTR),
    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class TransactionStatusQueueInfo(NDRCALL):
    opnum = 54
    structure = (

    )

class TransactionStatusQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoXactStatus', IMSMQQUEUEINFO2),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 55
    structure = (

    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (
		('pvarDestSymmKey', VARIANT),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 56
    structure = (
		('varDestSymmKey', VARIANT),
    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (

    )
        

class Signature(NDRCALL):
    opnum = 57
    structure = (

    )

class SignatureResponse(NDRCALL):
    structure = (
		('pvarSignature', VARIANT),
    )
        

class Signature(NDRCALL):
    opnum = 58
    structure = (
		('varSignature', VARIANT),
    )

class SignatureResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 59
    structure = (

    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (
		('plAuthProvType', LONG),
    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 60
    structure = (
		('lAuthProvType', LONG),
    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 61
    structure = (

    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (
		('pbstrAuthProvName', BSTR),
    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 62
    structure = (
		('bstrAuthProvName', BSTR),
    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 63
    structure = (
		('varSenderId', VARIANT),
    )

class SenderIdResponse(NDRCALL):
    structure = (

    )
        

class MsgClass(NDRCALL):
    opnum = 64
    structure = (

    )

class MsgClassResponse(NDRCALL):
    structure = (
		('plMsgClass', LONG),
    )
        

class MsgClass(NDRCALL):
    opnum = 65
    structure = (
		('lMsgClass', LONG),
    )

class MsgClassResponse(NDRCALL):
    structure = (

    )
        

class Properties(NDRCALL):
    opnum = 66
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class TransactionId(NDRCALL):
    opnum = 67
    structure = (

    )

class TransactionIdResponse(NDRCALL):
    structure = (
		('pvarXactId', VARIANT),
    )
        

class IsFirstInTransaction(NDRCALL):
    opnum = 68
    structure = (

    )

class IsFirstInTransactionResponse(NDRCALL):
    structure = (
		('pisFirstInXact', SHORT),
    )
        

class IsLastInTransaction(NDRCALL):
    opnum = 69
    structure = (

    )

class IsLastInTransactionResponse(NDRCALL):
    structure = (
		('pisLastInXact', SHORT),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 70
    structure = (

    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO2),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 71
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO2),
    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 72
    structure = (

    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO2),
    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 73
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO2),
    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class ReceivedAuthenticationLevel(NDRCALL):
    opnum = 74
    structure = (

    )

class ReceivedAuthenticationLevelResponse(NDRCALL):
    structure = (
		('psReceivedAuthenticationLevel', SHORT),
    )
        
OPNUMS = {
0 : (Class,ClassResponse),
1 : (PrivLevel,PrivLevelResponse),
2 : (AuthLevel,AuthLevelResponse),
3 : (IsAuthenticated,IsAuthenticatedResponse),
4 : (Delivery,DeliveryResponse),
5 : (Trace,TraceResponse),
6 : (Priority,PriorityResponse),
7 : (Journal,JournalResponse),
8 : (ResponseQueueInfo_v1,ResponseQueueInfo_v1Response),
9 : (AppSpecific,AppSpecificResponse),
10 : (SourceMachineGuid,SourceMachineGuidResponse),
11 : (BodyLength,BodyLengthResponse),
12 : (Body,BodyResponse),
13 : (AdminQueueInfo_v1,AdminQueueInfo_v1Response),
14 : (Id,IdResponse),
15 : (CorrelationId,CorrelationIdResponse),
16 : (Ack,AckResponse),
17 : (Label,LabelResponse),
18 : (MaxTimeToReachQueue,MaxTimeToReachQueueResponse),
19 : (MaxTimeToReceive,MaxTimeToReceiveResponse),
20 : (HashAlgorithm,HashAlgorithmResponse),
21 : (EncryptAlgorithm,EncryptAlgorithmResponse),
22 : (SentTime,SentTimeResponse),
23 : (ArrivedTime,ArrivedTimeResponse),
24 : (DestinationQueueInfo,DestinationQueueInfoResponse),
25 : (SenderCertificate,SenderCertificateResponse),
26 : (SenderId,SenderIdResponse),
27 : (SenderIdType,SenderIdTypeResponse),
28 : (Send,SendResponse),
29 : (AttachCurrentSecurityContext,AttachCurrentSecurityContextResponse),
30 : (SenderVersion,SenderVersionResponse),
31 : (Extension,ExtensionResponse),
32 : (ConnectorTypeGuid,ConnectorTypeGuidResponse),
33 : (TransactionStatusQueueInfo,TransactionStatusQueueInfoResponse),
34 : (DestinationSymmetricKey,DestinationSymmetricKeyResponse),
35 : (Signature,SignatureResponse),
36 : (AuthenticationProviderType,AuthenticationProviderTypeResponse),
37 : (AuthenticationProviderName,AuthenticationProviderNameResponse),
38 : (MsgClass,MsgClassResponse),
39 : (Properties,PropertiesResponse),
40 : (TransactionId,TransactionIdResponse),
41 : (IsFirstInTransaction,IsFirstInTransactionResponse),
42 : (IsLastInTransaction,IsLastInTransactionResponse),
43 : (ResponseQueueInfo,ResponseQueueInfoResponse),
44 : (AdminQueueInfo,AdminQueueInfoResponse),
45 : (ReceivedAuthenticationLevel,ReceivedAuthenticationLevelResponse),
}

#################################################################################

#IMSMQMessage3 Definition

#################################################################################

MSRPC_UUID_IMSMQMESSAGE3 = uuidtup_to_bin(('eba96b1a-2168-113-898-00020746','0.0'))


class Class(NDRCALL):
    opnum = 0
    structure = (

    )

class ClassResponse(NDRCALL):
    structure = (
		('plClass', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 1
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 2
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class AuthLevel(NDRCALL):
    opnum = 3
    structure = (

    )

class AuthLevelResponse(NDRCALL):
    structure = (
		('plAuthLevel', LONG),
    )
        

class AuthLevel(NDRCALL):
    opnum = 4
    structure = (
		('lAuthLevel', LONG),
    )

class AuthLevelResponse(NDRCALL):
    structure = (

    )
        

class IsAuthenticated(NDRCALL):
    opnum = 5
    structure = (

    )

class IsAuthenticatedResponse(NDRCALL):
    structure = (
		('pisAuthenticated', SHORT),
    )
        

class Delivery(NDRCALL):
    opnum = 6
    structure = (

    )

class DeliveryResponse(NDRCALL):
    structure = (
		('plDelivery', LONG),
    )
        

class Delivery(NDRCALL):
    opnum = 7
    structure = (
		('lDelivery', LONG),
    )

class DeliveryResponse(NDRCALL):
    structure = (

    )
        

class Trace(NDRCALL):
    opnum = 8
    structure = (

    )

class TraceResponse(NDRCALL):
    structure = (
		('plTrace', LONG),
    )
        

class Trace(NDRCALL):
    opnum = 9
    structure = (
		('lTrace', LONG),
    )

class TraceResponse(NDRCALL):
    structure = (

    )
        

class Priority(NDRCALL):
    opnum = 10
    structure = (

    )

class PriorityResponse(NDRCALL):
    structure = (
		('plPriority', LONG),
    )
        

class Priority(NDRCALL):
    opnum = 11
    structure = (
		('lPriority', LONG),
    )

class PriorityResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 14
    structure = (

    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO),
    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 15
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO),
    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class AppSpecific(NDRCALL):
    opnum = 16
    structure = (

    )

class AppSpecificResponse(NDRCALL):
    structure = (
		('plAppSpecific', LONG),
    )
        

class AppSpecific(NDRCALL):
    opnum = 17
    structure = (
		('lAppSpecific', LONG),
    )

class AppSpecificResponse(NDRCALL):
    structure = (

    )
        

class SourceMachineGuid(NDRCALL):
    opnum = 18
    structure = (

    )

class SourceMachineGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidSrcMachine', BSTR),
    )
        

class BodyLength(NDRCALL):
    opnum = 19
    structure = (

    )

class BodyLengthResponse(NDRCALL):
    structure = (
		('pcbBody', LONG),
    )
        

class Body(NDRCALL):
    opnum = 20
    structure = (

    )

class BodyResponse(NDRCALL):
    structure = (
		('pvarBody', VARIANT),
    )
        

class Body(NDRCALL):
    opnum = 21
    structure = (
		('varBody', VARIANT),
    )

class BodyResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 22
    structure = (

    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO),
    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 23
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO),
    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class Id(NDRCALL):
    opnum = 24
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 25
    structure = (

    )

class CorrelationIdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 26
    structure = (
		('varMsgId', VARIANT),
    )

class CorrelationIdResponse(NDRCALL):
    structure = (

    )
        

class Ack(NDRCALL):
    opnum = 27
    structure = (

    )

class AckResponse(NDRCALL):
    structure = (
		('plAck', LONG),
    )
        

class Ack(NDRCALL):
    opnum = 28
    structure = (
		('lAck', LONG),
    )

class AckResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 29
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 30
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 31
    structure = (

    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (
		('plMaxTimeToReachQueue', LONG),
    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 32
    structure = (
		('lMaxTimeToReachQueue', LONG),
    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 33
    structure = (

    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (
		('plMaxTimeToReceive', LONG),
    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 34
    structure = (
		('lMaxTimeToReceive', LONG),
    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (

    )
        

class HashAlgorithm(NDRCALL):
    opnum = 35
    structure = (

    )

class HashAlgorithmResponse(NDRCALL):
    structure = (
		('plHashAlg', LONG),
    )
        

class HashAlgorithm(NDRCALL):
    opnum = 36
    structure = (
		('lHashAlg', LONG),
    )

class HashAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 37
    structure = (

    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (
		('plEncryptAlg', LONG),
    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 38
    structure = (
		('lEncryptAlg', LONG),
    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class SentTime(NDRCALL):
    opnum = 39
    structure = (

    )

class SentTimeResponse(NDRCALL):
    structure = (
		('pvarSentTime', VARIANT),
    )
        

class ArrivedTime(NDRCALL):
    opnum = 40
    structure = (

    )

class ArrivedTimeResponse(NDRCALL):
    structure = (
		('plArrivedTime', VARIANT),
    )
        

class DestinationQueueInfo(NDRCALL):
    opnum = 41
    structure = (

    )

class DestinationQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoDest', IMSMQQUEUEINFO3),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 42
    structure = (

    )

class SenderCertificateResponse(NDRCALL):
    structure = (
		('pvarSenderCert', VARIANT),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 43
    structure = (
		('varSenderCert', VARIANT),
    )

class SenderCertificateResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 44
    structure = (

    )

class SenderIdResponse(NDRCALL):
    structure = (
		('pvarSenderId', VARIANT),
    )
        

class SenderIdType(NDRCALL):
    opnum = 45
    structure = (

    )

class SenderIdTypeResponse(NDRCALL):
    structure = (
		('plSenderIdType', LONG),
    )
        

class SenderIdType(NDRCALL):
    opnum = 46
    structure = (
		('lSenderIdType', LONG),
    )

class SenderIdTypeResponse(NDRCALL):
    structure = (

    )
        

class Send(NDRCALL):
    opnum = 47
    structure = (
		('DestinationQueue', IDISPATCH),
		('Transaction', VARIANT),
    )

class SendResponse(NDRCALL):
    structure = (

    )
        

class AttachCurrentSecurityContext(NDRCALL):
    opnum = 48
    structure = (

    )

class AttachCurrentSecurityContextResponse(NDRCALL):
    structure = (

    )
        

class SenderVersion(NDRCALL):
    opnum = 49
    structure = (

    )

class SenderVersionResponse(NDRCALL):
    structure = (
		('plSenderVersion', LONG),
    )
        

class Extension(NDRCALL):
    opnum = 50
    structure = (

    )

class ExtensionResponse(NDRCALL):
    structure = (
		('pvarExtension', VARIANT),
    )
        

class Extension(NDRCALL):
    opnum = 51
    structure = (
		('varExtension', VARIANT),
    )

class ExtensionResponse(NDRCALL):
    structure = (

    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 52
    structure = (

    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidConnectorType', BSTR),
    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 53
    structure = (
		('bstrGuidConnectorType', BSTR),
    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class TransactionStatusQueueInfo(NDRCALL):
    opnum = 54
    structure = (

    )

class TransactionStatusQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoXactStatus', IMSMQQUEUEINFO3),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 55
    structure = (

    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (
		('pvarDestSymmKey', VARIANT),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 56
    structure = (
		('varDestSymmKey', VARIANT),
    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (

    )
        

class Signature(NDRCALL):
    opnum = 57
    structure = (

    )

class SignatureResponse(NDRCALL):
    structure = (
		('pvarSignature', VARIANT),
    )
        

class Signature(NDRCALL):
    opnum = 58
    structure = (
		('varSignature', VARIANT),
    )

class SignatureResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 59
    structure = (

    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (
		('plAuthProvType', LONG),
    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 60
    structure = (
		('lAuthProvType', LONG),
    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 61
    structure = (

    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (
		('pbstrAuthProvName', BSTR),
    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 62
    structure = (
		('bstrAuthProvName', BSTR),
    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 63
    structure = (
		('varSenderId', VARIANT),
    )

class SenderIdResponse(NDRCALL):
    structure = (

    )
        

class MsgClass(NDRCALL):
    opnum = 64
    structure = (

    )

class MsgClassResponse(NDRCALL):
    structure = (
		('plMsgClass', LONG),
    )
        

class MsgClass(NDRCALL):
    opnum = 65
    structure = (
		('lMsgClass', LONG),
    )

class MsgClassResponse(NDRCALL):
    structure = (

    )
        

class Properties(NDRCALL):
    opnum = 66
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class TransactionId(NDRCALL):
    opnum = 67
    structure = (

    )

class TransactionIdResponse(NDRCALL):
    structure = (
		('pvarXactId', VARIANT),
    )
        

class IsFirstInTransaction(NDRCALL):
    opnum = 68
    structure = (

    )

class IsFirstInTransactionResponse(NDRCALL):
    structure = (
		('pisFirstInXact', SHORT),
    )
        

class IsLastInTransaction(NDRCALL):
    opnum = 69
    structure = (

    )

class IsLastInTransactionResponse(NDRCALL):
    structure = (
		('pisLastInXact', SHORT),
    )
        

class ResponseQueueInfo_v2(NDRCALL):
    opnum = 70
    structure = (

    )

class ResponseQueueInfo_v2Response(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO2),
    )
        

class ResponseQueueInfo_v2(NDRCALL):
    opnum = 71
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO2),
    )

class ResponseQueueInfo_v2Response(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo_v2(NDRCALL):
    opnum = 72
    structure = (

    )

class AdminQueueInfo_v2Response(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO2),
    )
        

class AdminQueueInfo_v2(NDRCALL):
    opnum = 73
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO2),
    )

class AdminQueueInfo_v2Response(NDRCALL):
    structure = (

    )
        

class ReceivedAuthenticationLevel(NDRCALL):
    opnum = 74
    structure = (

    )

class ReceivedAuthenticationLevelResponse(NDRCALL):
    structure = (
		('psReceivedAuthenticationLevel', SHORT),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 75
    structure = (

    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO3),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 76
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO3),
    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 77
    structure = (

    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO3),
    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 78
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO3),
    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class ResponseDestination(NDRCALL):
    opnum = 79
    structure = (

    )

class ResponseDestinationResponse(NDRCALL):
    structure = (
		('ppdestRespons', IDISPATCH),
    )
        

class ResponseDestination(NDRCALL):
    opnum = 80
    structure = (
		('pdestResponse', IDISPATCH),
    )

class ResponseDestinationResponse(NDRCALL):
    structure = (

    )
        

class Destination(NDRCALL):
    opnum = 81
    structure = (

    )

class DestinationResponse(NDRCALL):
    structure = (
		('ppdestDestination', IDISPATCH),
    )
        

class LookupId(NDRCALL):
    opnum = 82
    structure = (

    )

class LookupIdResponse(NDRCALL):
    structure = (
		('pvarLookupId', VARIANT),
    )
        

class IsAuthenticated2(NDRCALL):
    opnum = 83
    structure = (

    )

class IsAuthenticated2Response(NDRCALL):
    structure = (
		('pisAuthenticated', VARIANT_BOOL),
    )
        

class IsFirstInTransaction2(NDRCALL):
    opnum = 84
    structure = (

    )

class IsFirstInTransaction2Response(NDRCALL):
    structure = (
		('pisFirstInXact', VARIANT_BOOL),
    )
        

class IsLastInTransaction2(NDRCALL):
    opnum = 85
    structure = (

    )

class IsLastInTransaction2Response(NDRCALL):
    structure = (
		('pisLastInXact', VARIANT_BOOL),
    )
        

class AttachCurrentSecurityContext2(NDRCALL):
    opnum = 86
    structure = (

    )

class AttachCurrentSecurityContext2Response(NDRCALL):
    structure = (

    )
        

class SoapEnvelope(NDRCALL):
    opnum = 87
    structure = (

    )

class SoapEnvelopeResponse(NDRCALL):
    structure = (
		('pbstrSoapEnvelope', BSTR),
    )
        

class CompoundMessage(NDRCALL):
    opnum = 88
    structure = (

    )

class CompoundMessageResponse(NDRCALL):
    structure = (
		('pvarCompoundMessage', VARIANT),
    )
        

class SoapHeader(NDRCALL):
    opnum = 89
    structure = (
		('bstrSoapHeader', BSTR),
    )

class SoapHeaderResponse(NDRCALL):
    structure = (

    )
        

class SoapBody(NDRCALL):
    opnum = 90
    structure = (
		('bstrSoapBody', BSTR),
    )

class SoapBodyResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Class,ClassResponse),
1 : (PrivLevel,PrivLevelResponse),
2 : (AuthLevel,AuthLevelResponse),
3 : (IsAuthenticated,IsAuthenticatedResponse),
4 : (Delivery,DeliveryResponse),
5 : (Trace,TraceResponse),
6 : (Priority,PriorityResponse),
7 : (Journal,JournalResponse),
8 : (ResponseQueueInfo_v1,ResponseQueueInfo_v1Response),
9 : (AppSpecific,AppSpecificResponse),
10 : (SourceMachineGuid,SourceMachineGuidResponse),
11 : (BodyLength,BodyLengthResponse),
12 : (Body,BodyResponse),
13 : (AdminQueueInfo_v1,AdminQueueInfo_v1Response),
14 : (Id,IdResponse),
15 : (CorrelationId,CorrelationIdResponse),
16 : (Ack,AckResponse),
17 : (Label,LabelResponse),
18 : (MaxTimeToReachQueue,MaxTimeToReachQueueResponse),
19 : (MaxTimeToReceive,MaxTimeToReceiveResponse),
20 : (HashAlgorithm,HashAlgorithmResponse),
21 : (EncryptAlgorithm,EncryptAlgorithmResponse),
22 : (SentTime,SentTimeResponse),
23 : (ArrivedTime,ArrivedTimeResponse),
24 : (DestinationQueueInfo,DestinationQueueInfoResponse),
25 : (SenderCertificate,SenderCertificateResponse),
26 : (SenderId,SenderIdResponse),
27 : (SenderIdType,SenderIdTypeResponse),
28 : (Send,SendResponse),
29 : (AttachCurrentSecurityContext,AttachCurrentSecurityContextResponse),
30 : (SenderVersion,SenderVersionResponse),
31 : (Extension,ExtensionResponse),
32 : (ConnectorTypeGuid,ConnectorTypeGuidResponse),
33 : (TransactionStatusQueueInfo,TransactionStatusQueueInfoResponse),
34 : (DestinationSymmetricKey,DestinationSymmetricKeyResponse),
35 : (Signature,SignatureResponse),
36 : (AuthenticationProviderType,AuthenticationProviderTypeResponse),
37 : (AuthenticationProviderName,AuthenticationProviderNameResponse),
38 : (MsgClass,MsgClassResponse),
39 : (Properties,PropertiesResponse),
40 : (TransactionId,TransactionIdResponse),
41 : (IsFirstInTransaction,IsFirstInTransactionResponse),
42 : (IsLastInTransaction,IsLastInTransactionResponse),
43 : (ResponseQueueInfo_v2,ResponseQueueInfo_v2Response),
44 : (AdminQueueInfo_v2,AdminQueueInfo_v2Response),
45 : (ReceivedAuthenticationLevel,ReceivedAuthenticationLevelResponse),
46 : (ResponseQueueInfo,ResponseQueueInfoResponse),
47 : (AdminQueueInfo,AdminQueueInfoResponse),
48 : (ResponseDestination,ResponseDestinationResponse),
49 : (Destination,DestinationResponse),
50 : (LookupId,LookupIdResponse),
51 : (IsAuthenticated2,IsAuthenticated2Response),
52 : (IsFirstInTransaction2,IsFirstInTransaction2Response),
53 : (IsLastInTransaction2,IsLastInTransaction2Response),
54 : (AttachCurrentSecurityContext2,AttachCurrentSecurityContext2Response),
55 : (SoapEnvelope,SoapEnvelopeResponse),
56 : (CompoundMessage,CompoundMessageResponse),
57 : (SoapHeader,SoapHeaderResponse),
58 : (SoapBody,SoapBodyResponse),
}

#################################################################################

#IMSMQMessage4 Definition

#################################################################################

MSRPC_UUID_IMSMQMESSAGE4 = uuidtup_to_bin(('eba96b23-2168-113-898-00020746','0.0'))


class Class(NDRCALL):
    opnum = 0
    structure = (

    )

class ClassResponse(NDRCALL):
    structure = (
		('plClass', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 1
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 2
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class AuthLevel(NDRCALL):
    opnum = 3
    structure = (

    )

class AuthLevelResponse(NDRCALL):
    structure = (
		('plAuthLevel', LONG),
    )
        

class AuthLevel(NDRCALL):
    opnum = 4
    structure = (
		('lAuthLevel', LONG),
    )

class AuthLevelResponse(NDRCALL):
    structure = (

    )
        

class IsAuthenticated(NDRCALL):
    opnum = 5
    structure = (

    )

class IsAuthenticatedResponse(NDRCALL):
    structure = (
		('pisAuthenticated', SHORT),
    )
        

class Delivery(NDRCALL):
    opnum = 6
    structure = (

    )

class DeliveryResponse(NDRCALL):
    structure = (
		('plDelivery', LONG),
    )
        

class Delivery(NDRCALL):
    opnum = 7
    structure = (
		('lDelivery', LONG),
    )

class DeliveryResponse(NDRCALL):
    structure = (

    )
        

class Trace(NDRCALL):
    opnum = 8
    structure = (

    )

class TraceResponse(NDRCALL):
    structure = (
		('plTrace', LONG),
    )
        

class Trace(NDRCALL):
    opnum = 9
    structure = (
		('lTrace', LONG),
    )

class TraceResponse(NDRCALL):
    structure = (

    )
        

class Priority(NDRCALL):
    opnum = 10
    structure = (

    )

class PriorityResponse(NDRCALL):
    structure = (
		('plPriority', LONG),
    )
        

class Priority(NDRCALL):
    opnum = 11
    structure = (
		('lPriority', LONG),
    )

class PriorityResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 14
    structure = (

    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO),
    )
        

class ResponseQueueInfo_v1(NDRCALL):
    opnum = 15
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO),
    )

class ResponseQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class AppSpecific(NDRCALL):
    opnum = 16
    structure = (

    )

class AppSpecificResponse(NDRCALL):
    structure = (
		('plAppSpecific', LONG),
    )
        

class AppSpecific(NDRCALL):
    opnum = 17
    structure = (
		('lAppSpecific', LONG),
    )

class AppSpecificResponse(NDRCALL):
    structure = (

    )
        

class SourceMachineGuid(NDRCALL):
    opnum = 18
    structure = (

    )

class SourceMachineGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidSrcMachine', BSTR),
    )
        

class BodyLength(NDRCALL):
    opnum = 19
    structure = (

    )

class BodyLengthResponse(NDRCALL):
    structure = (
		('pcbBody', LONG),
    )
        

class Body(NDRCALL):
    opnum = 20
    structure = (

    )

class BodyResponse(NDRCALL):
    structure = (
		('pvarBody', VARIANT),
    )
        

class Body(NDRCALL):
    opnum = 21
    structure = (
		('varBody', VARIANT),
    )

class BodyResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 22
    structure = (

    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO),
    )
        

class AdminQueueInfo_v1(NDRCALL):
    opnum = 23
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO),
    )

class AdminQueueInfo_v1Response(NDRCALL):
    structure = (

    )
        

class Id(NDRCALL):
    opnum = 24
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 25
    structure = (

    )

class CorrelationIdResponse(NDRCALL):
    structure = (
		('pvarMsgId', VARIANT),
    )
        

class CorrelationId(NDRCALL):
    opnum = 26
    structure = (
		('varMsgId', VARIANT),
    )

class CorrelationIdResponse(NDRCALL):
    structure = (

    )
        

class Ack(NDRCALL):
    opnum = 27
    structure = (

    )

class AckResponse(NDRCALL):
    structure = (
		('plAck', LONG),
    )
        

class Ack(NDRCALL):
    opnum = 28
    structure = (
		('lAck', LONG),
    )

class AckResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 29
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 30
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 31
    structure = (

    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (
		('plMaxTimeToReachQueue', LONG),
    )
        

class MaxTimeToReachQueue(NDRCALL):
    opnum = 32
    structure = (
		('lMaxTimeToReachQueue', LONG),
    )

class MaxTimeToReachQueueResponse(NDRCALL):
    structure = (

    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 33
    structure = (

    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (
		('plMaxTimeToReceive', LONG),
    )
        

class MaxTimeToReceive(NDRCALL):
    opnum = 34
    structure = (
		('lMaxTimeToReceive', LONG),
    )

class MaxTimeToReceiveResponse(NDRCALL):
    structure = (

    )
        

class HashAlgorithm(NDRCALL):
    opnum = 35
    structure = (

    )

class HashAlgorithmResponse(NDRCALL):
    structure = (
		('plHashAlg', LONG),
    )
        

class HashAlgorithm(NDRCALL):
    opnum = 36
    structure = (
		('lHashAlg', LONG),
    )

class HashAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 37
    structure = (

    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (
		('plEncryptAlg', LONG),
    )
        

class EncryptAlgorithm(NDRCALL):
    opnum = 38
    structure = (
		('lEncryptAlg', LONG),
    )

class EncryptAlgorithmResponse(NDRCALL):
    structure = (

    )
        

class SentTime(NDRCALL):
    opnum = 39
    structure = (

    )

class SentTimeResponse(NDRCALL):
    structure = (
		('pvarSentTime', VARIANT),
    )
        

class ArrivedTime(NDRCALL):
    opnum = 40
    structure = (

    )

class ArrivedTimeResponse(NDRCALL):
    structure = (
		('plArrivedTime', VARIANT),
    )
        

class DestinationQueueInfo(NDRCALL):
    opnum = 41
    structure = (

    )

class DestinationQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoDest', IMSMQQUEUEINFO4),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 42
    structure = (

    )

class SenderCertificateResponse(NDRCALL):
    structure = (
		('pvarSenderCert', VARIANT),
    )
        

class SenderCertificate(NDRCALL):
    opnum = 43
    structure = (
		('varSenderCert', VARIANT),
    )

class SenderCertificateResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 44
    structure = (

    )

class SenderIdResponse(NDRCALL):
    structure = (
		('pvarSenderId', VARIANT),
    )
        

class SenderIdType(NDRCALL):
    opnum = 45
    structure = (

    )

class SenderIdTypeResponse(NDRCALL):
    structure = (
		('plSenderIdType', LONG),
    )
        

class SenderIdType(NDRCALL):
    opnum = 46
    structure = (
		('lSenderIdType', LONG),
    )

class SenderIdTypeResponse(NDRCALL):
    structure = (

    )
        

class Send(NDRCALL):
    opnum = 47
    structure = (
		('DestinationQueue', IDISPATCH),
		('Transaction', VARIANT),
    )

class SendResponse(NDRCALL):
    structure = (

    )
        

class AttachCurrentSecurityContext(NDRCALL):
    opnum = 48
    structure = (

    )

class AttachCurrentSecurityContextResponse(NDRCALL):
    structure = (

    )
        

class SenderVersion(NDRCALL):
    opnum = 49
    structure = (

    )

class SenderVersionResponse(NDRCALL):
    structure = (
		('plSenderVersion', LONG),
    )
        

class Extension(NDRCALL):
    opnum = 50
    structure = (

    )

class ExtensionResponse(NDRCALL):
    structure = (
		('pvarExtension', VARIANT),
    )
        

class Extension(NDRCALL):
    opnum = 51
    structure = (
		('varExtension', VARIANT),
    )

class ExtensionResponse(NDRCALL):
    structure = (

    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 52
    structure = (

    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidConnectorType', BSTR),
    )
        

class ConnectorTypeGuid(NDRCALL):
    opnum = 53
    structure = (
		('bstrGuidConnectorType', BSTR),
    )

class ConnectorTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class TransactionStatusQueueInfo(NDRCALL):
    opnum = 54
    structure = (

    )

class TransactionStatusQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoXactStatus', IMSMQQUEUEINFO4),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 55
    structure = (

    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (
		('pvarDestSymmKey', VARIANT),
    )
        

class DestinationSymmetricKey(NDRCALL):
    opnum = 56
    structure = (
		('varDestSymmKey', VARIANT),
    )

class DestinationSymmetricKeyResponse(NDRCALL):
    structure = (

    )
        

class Signature(NDRCALL):
    opnum = 57
    structure = (

    )

class SignatureResponse(NDRCALL):
    structure = (
		('pvarSignature', VARIANT),
    )
        

class Signature(NDRCALL):
    opnum = 58
    structure = (
		('varSignature', VARIANT),
    )

class SignatureResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 59
    structure = (

    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (
		('plAuthProvType', LONG),
    )
        

class AuthenticationProviderType(NDRCALL):
    opnum = 60
    structure = (
		('lAuthProvType', LONG),
    )

class AuthenticationProviderTypeResponse(NDRCALL):
    structure = (

    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 61
    structure = (

    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (
		('pbstrAuthProvName', BSTR),
    )
        

class AuthenticationProviderName(NDRCALL):
    opnum = 62
    structure = (
		('bstrAuthProvName', BSTR),
    )

class AuthenticationProviderNameResponse(NDRCALL):
    structure = (

    )
        

class SenderId(NDRCALL):
    opnum = 63
    structure = (
		('varSenderId', VARIANT),
    )

class SenderIdResponse(NDRCALL):
    structure = (

    )
        

class MsgClass(NDRCALL):
    opnum = 64
    structure = (

    )

class MsgClassResponse(NDRCALL):
    structure = (
		('plMsgClass', LONG),
    )
        

class MsgClass(NDRCALL):
    opnum = 65
    structure = (
		('lMsgClass', LONG),
    )

class MsgClassResponse(NDRCALL):
    structure = (

    )
        

class Properties(NDRCALL):
    opnum = 66
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class TransactionId(NDRCALL):
    opnum = 67
    structure = (

    )

class TransactionIdResponse(NDRCALL):
    structure = (
		('pvarXactId', VARIANT),
    )
        

class IsFirstInTransaction(NDRCALL):
    opnum = 68
    structure = (

    )

class IsFirstInTransactionResponse(NDRCALL):
    structure = (
		('pisFirstInXact', SHORT),
    )
        

class IsLastInTransaction(NDRCALL):
    opnum = 69
    structure = (

    )

class IsLastInTransactionResponse(NDRCALL):
    structure = (
		('pisLastInXact', SHORT),
    )
        

class ResponseQueueInfo_v2(NDRCALL):
    opnum = 70
    structure = (

    )

class ResponseQueueInfo_v2Response(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO2),
    )
        

class ResponseQueueInfo_v2(NDRCALL):
    opnum = 71
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO2),
    )

class ResponseQueueInfo_v2Response(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo_v2(NDRCALL):
    opnum = 72
    structure = (

    )

class AdminQueueInfo_v2Response(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO2),
    )
        

class AdminQueueInfo_v2(NDRCALL):
    opnum = 73
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO2),
    )

class AdminQueueInfo_v2Response(NDRCALL):
    structure = (

    )
        

class ReceivedAuthenticationLevel(NDRCALL):
    opnum = 74
    structure = (

    )

class ReceivedAuthenticationLevelResponse(NDRCALL):
    structure = (
		('psReceivedAuthenticationLevel', SHORT),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 75
    structure = (

    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoResponse', IMSMQQUEUEINFO4),
    )
        

class ResponseQueueInfo(NDRCALL):
    opnum = 76
    structure = (
		('pqinfoResponse', IMSMQQUEUEINFO4),
    )

class ResponseQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 77
    structure = (

    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfoAdmin', IMSMQQUEUEINFO4),
    )
        

class AdminQueueInfo(NDRCALL):
    opnum = 78
    structure = (
		('pqinfoAdmin', IMSMQQUEUEINFO4),
    )

class AdminQueueInfoResponse(NDRCALL):
    structure = (

    )
        

class ResponseDestination(NDRCALL):
    opnum = 79
    structure = (

    )

class ResponseDestinationResponse(NDRCALL):
    structure = (
		('ppdestResponse', IDISPATCH),
    )
        

class ResponseDestination(NDRCALL):
    opnum = 80
    structure = (
		('pdestResponse', IDISPATCH),
    )

class ResponseDestinationResponse(NDRCALL):
    structure = (

    )
        

class Destination(NDRCALL):
    opnum = 81
    structure = (

    )

class DestinationResponse(NDRCALL):
    structure = (
		('ppdestDestination', IDISPATCH),
    )
        

class LookupId(NDRCALL):
    opnum = 82
    structure = (

    )

class LookupIdResponse(NDRCALL):
    structure = (
		('pvarLookupId', VARIANT),
    )
        

class IsAuthenticated2(NDRCALL):
    opnum = 83
    structure = (

    )

class IsAuthenticated2Response(NDRCALL):
    structure = (
		('pisAuthenticated', VARIANT_BOOL),
    )
        

class IsFirstInTransaction2(NDRCALL):
    opnum = 84
    structure = (

    )

class IsFirstInTransaction2Response(NDRCALL):
    structure = (
		('pisFirstInXact', VARIANT_BOOL),
    )
        

class IsLastInTransaction2(NDRCALL):
    opnum = 85
    structure = (

    )

class IsLastInTransaction2Response(NDRCALL):
    structure = (
		('pisLastInXact', VARIANT_BOOL),
    )
        

class AttachCurrentSecurityContext2(NDRCALL):
    opnum = 86
    structure = (

    )

class AttachCurrentSecurityContext2Response(NDRCALL):
    structure = (

    )
        

class SoapEnvelope(NDRCALL):
    opnum = 87
    structure = (

    )

class SoapEnvelopeResponse(NDRCALL):
    structure = (
		('pbstrSoapEnvelope', BSTR),
    )
        

class CompoundMessage(NDRCALL):
    opnum = 88
    structure = (

    )

class CompoundMessageResponse(NDRCALL):
    structure = (
		('pvarCompoundMessage', VARIANT),
    )
        

class SoapHeader(NDRCALL):
    opnum = 89
    structure = (
		('bstrSoapHeader', BSTR),
    )

class SoapHeaderResponse(NDRCALL):
    structure = (

    )
        

class SoapBody(NDRCALL):
    opnum = 90
    structure = (
		('bstrSoapBody', BSTR),
    )

class SoapBodyResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Class,ClassResponse),
1 : (PrivLevel,PrivLevelResponse),
2 : (AuthLevel,AuthLevelResponse),
3 : (IsAuthenticated,IsAuthenticatedResponse),
4 : (Delivery,DeliveryResponse),
5 : (Trace,TraceResponse),
6 : (Priority,PriorityResponse),
7 : (Journal,JournalResponse),
8 : (ResponseQueueInfo_v1,ResponseQueueInfo_v1Response),
9 : (AppSpecific,AppSpecificResponse),
10 : (SourceMachineGuid,SourceMachineGuidResponse),
11 : (BodyLength,BodyLengthResponse),
12 : (Body,BodyResponse),
13 : (AdminQueueInfo_v1,AdminQueueInfo_v1Response),
14 : (Id,IdResponse),
15 : (CorrelationId,CorrelationIdResponse),
16 : (Ack,AckResponse),
17 : (Label,LabelResponse),
18 : (MaxTimeToReachQueue,MaxTimeToReachQueueResponse),
19 : (MaxTimeToReceive,MaxTimeToReceiveResponse),
20 : (HashAlgorithm,HashAlgorithmResponse),
21 : (EncryptAlgorithm,EncryptAlgorithmResponse),
22 : (SentTime,SentTimeResponse),
23 : (ArrivedTime,ArrivedTimeResponse),
24 : (DestinationQueueInfo,DestinationQueueInfoResponse),
25 : (SenderCertificate,SenderCertificateResponse),
26 : (SenderId,SenderIdResponse),
27 : (SenderIdType,SenderIdTypeResponse),
28 : (Send,SendResponse),
29 : (AttachCurrentSecurityContext,AttachCurrentSecurityContextResponse),
30 : (SenderVersion,SenderVersionResponse),
31 : (Extension,ExtensionResponse),
32 : (ConnectorTypeGuid,ConnectorTypeGuidResponse),
33 : (TransactionStatusQueueInfo,TransactionStatusQueueInfoResponse),
34 : (DestinationSymmetricKey,DestinationSymmetricKeyResponse),
35 : (Signature,SignatureResponse),
36 : (AuthenticationProviderType,AuthenticationProviderTypeResponse),
37 : (AuthenticationProviderName,AuthenticationProviderNameResponse),
38 : (MsgClass,MsgClassResponse),
39 : (Properties,PropertiesResponse),
40 : (TransactionId,TransactionIdResponse),
41 : (IsFirstInTransaction,IsFirstInTransactionResponse),
42 : (IsLastInTransaction,IsLastInTransactionResponse),
43 : (ResponseQueueInfo_v2,ResponseQueueInfo_v2Response),
44 : (AdminQueueInfo_v2,AdminQueueInfo_v2Response),
45 : (ReceivedAuthenticationLevel,ReceivedAuthenticationLevelResponse),
46 : (ResponseQueueInfo,ResponseQueueInfoResponse),
47 : (AdminQueueInfo,AdminQueueInfoResponse),
48 : (ResponseDestination,ResponseDestinationResponse),
49 : (Destination,DestinationResponse),
50 : (LookupId,LookupIdResponse),
51 : (IsAuthenticated2,IsAuthenticated2Response),
52 : (IsFirstInTransaction2,IsFirstInTransaction2Response),
53 : (IsLastInTransaction2,IsLastInTransaction2Response),
54 : (AttachCurrentSecurityContext2,AttachCurrentSecurityContext2Response),
55 : (SoapEnvelope,SoapEnvelopeResponse),
56 : (CompoundMessage,CompoundMessageResponse),
57 : (SoapHeader,SoapHeaderResponse),
58 : (SoapBody,SoapBodyResponse),
}

#################################################################################

#IMSMQQueue Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUE = uuidtup_to_bin(('D7D6E076-DCCD-110-AA4B-0060970EBAE','0.0'))


class Access(NDRCALL):
    opnum = 0
    structure = (

    )

class AccessResponse(NDRCALL):
    structure = (
		('plAccess', LONG),
    )
        

class ShareMode(NDRCALL):
    opnum = 1
    structure = (

    )

class ShareModeResponse(NDRCALL):
    structure = (
		('plShareMode', LONG),
    )
        

class QueueInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class QueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfo', IMSMQQUEUEINFO),
    )
        

class Handle(NDRCALL):
    opnum = 3
    structure = (

    )

class HandleResponse(NDRCALL):
    structure = (
		('plHandle', LONG),
    )
        

class IsOpen(NDRCALL):
    opnum = 4
    structure = (

    )

class IsOpenResponse(NDRCALL):
    structure = (
		('pisOpen', SHORT),
    )
        

class Close(NDRCALL):
    opnum = 5
    structure = (

    )

class CloseResponse(NDRCALL):
    structure = (

    )
        

class Receive(NDRCALL):
    opnum = 6
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class ReceiveResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Peek(NDRCALL):
    opnum = 7
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class EnableNotification(NDRCALL):
    opnum = 8
    structure = (
		('Event', IMSMQEVENT),
		('Cursor', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class EnableNotificationResponse(NDRCALL):
    structure = (

    )
        

class Reset(NDRCALL):
    opnum = 9
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class ReceiveCurrent(NDRCALL):
    opnum = 10
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class ReceiveCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekNext(NDRCALL):
    opnum = 11
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekNextResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekCurrent(NDRCALL):
    opnum = 12
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        
OPNUMS = {
0 : (Access,AccessResponse),
1 : (ShareMode,ShareModeResponse),
2 : (QueueInfo,QueueInfoResponse),
3 : (Handle,HandleResponse),
4 : (IsOpen,IsOpenResponse),
5 : (Close,CloseResponse),
6 : (Receive,ReceiveResponse),
7 : (Peek,PeekResponse),
8 : (EnableNotification,EnableNotificationResponse),
9 : (Reset,ResetResponse),
10 : (ReceiveCurrent,ReceiveCurrentResponse),
11 : (PeekNext,PeekNextResponse),
12 : (PeekCurrent,PeekCurrentResponse),
}

#################################################################################

#IMSMQQueue2 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUE2 = uuidtup_to_bin(('EF0574E0-068-113-B100-00020746','0.0'))


class Access(NDRCALL):
    opnum = 0
    structure = (

    )

class AccessResponse(NDRCALL):
    structure = (
		('plAccess', LONG),
    )
        

class ShareMode(NDRCALL):
    opnum = 1
    structure = (

    )

class ShareModeResponse(NDRCALL):
    structure = (
		('plShareMode', LONG),
    )
        

class QueueInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class QueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfo', IMSMQQUEUEINFO2),
    )
        

class Handle(NDRCALL):
    opnum = 3
    structure = (

    )

class HandleResponse(NDRCALL):
    structure = (
		('plHandle', LONG),
    )
        

class IsOpen(NDRCALL):
    opnum = 4
    structure = (

    )

class IsOpenResponse(NDRCALL):
    structure = (
		('pisOpen', SHORT),
    )
        

class Close(NDRCALL):
    opnum = 5
    structure = (

    )

class CloseResponse(NDRCALL):
    structure = (

    )
        

class Receive_v1(NDRCALL):
    opnum = 6
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Receive_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Peek_v1(NDRCALL):
    opnum = 7
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Peek_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class EnableNotification(NDRCALL):
    opnum = 8
    structure = (
		('Event', IMSMQEVENT2),
		('Cursor', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class EnableNotificationResponse(NDRCALL):
    structure = (

    )
        

class Reset(NDRCALL):
    opnum = 9
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class ReceiveCurrent_v1(NDRCALL):
    opnum = 10
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class ReceiveCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekNext_v1(NDRCALL):
    opnum = 11
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekNext_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekCurrent_v1(NDRCALL):
    opnum = 12
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Receive(NDRCALL):
    opnum = 13
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE2),
    )
        

class Peek(NDRCALL):
    opnum = 14
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE2),
    )
        

class ReceiveCurrent(NDRCALL):
    opnum = 15
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE2),
    )
        

class PeekNext(NDRCALL):
    opnum = 16
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekNextResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE2),
    )
        

class PeekCurrent(NDRCALL):
    opnum = 17
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE2),
    )
        

class Properties(NDRCALL):
    opnum = 18
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Access,AccessResponse),
1 : (ShareMode,ShareModeResponse),
2 : (QueueInfo,QueueInfoResponse),
3 : (Handle,HandleResponse),
4 : (IsOpen,IsOpenResponse),
5 : (Close,CloseResponse),
6 : (Receive_v1,Receive_v1Response),
7 : (Peek_v1,Peek_v1Response),
8 : (EnableNotification,EnableNotificationResponse),
9 : (Reset,ResetResponse),
10 : (ReceiveCurrent_v1,ReceiveCurrent_v1Response),
11 : (PeekNext_v1,PeekNext_v1Response),
12 : (PeekCurrent_v1,PeekCurrent_v1Response),
13 : (Receive,ReceiveResponse),
14 : (Peek,PeekResponse),
15 : (ReceiveCurrent,ReceiveCurrentResponse),
16 : (PeekNext,PeekNextResponse),
17 : (PeekCurrent,PeekCurrentResponse),
18 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQQueue3 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUE3 = uuidtup_to_bin(('eba96b1b-2168-113-898-00020746','0.0'))


class Access(NDRCALL):
    opnum = 0
    structure = (

    )

class AccessResponse(NDRCALL):
    structure = (
		('plAccess', LONG),
    )
        

class ShareMode(NDRCALL):
    opnum = 1
    structure = (

    )

class ShareModeResponse(NDRCALL):
    structure = (
		('plShareMode', LONG),
    )
        

class QueueInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class QueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfo', IMSMQQUEUEINFO3),
    )
        

class Handle(NDRCALL):
    opnum = 3
    structure = (

    )

class HandleResponse(NDRCALL):
    structure = (
		('plHandle', LONG),
    )
        

class IsOpen(NDRCALL):
    opnum = 4
    structure = (

    )

class IsOpenResponse(NDRCALL):
    structure = (
		('pisOpen', SHORT),
    )
        

class Close(NDRCALL):
    opnum = 5
    structure = (

    )

class CloseResponse(NDRCALL):
    structure = (

    )
        

class Receive_v1(NDRCALL):
    opnum = 6
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Receive_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Peek_v1(NDRCALL):
    opnum = 7
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Peek_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class EnableNotification(NDRCALL):
    opnum = 8
    structure = (
		('Event', IMSMQEVENT3),
		('Cursor', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class EnableNotificationResponse(NDRCALL):
    structure = (

    )
        

class Reset(NDRCALL):
    opnum = 9
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class ReceiveCurrent_v1(NDRCALL):
    opnum = 10
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class ReceiveCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekNext_v1(NDRCALL):
    opnum = 11
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekNext_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekCurrent_v1(NDRCALL):
    opnum = 12
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Receive(NDRCALL):
    opnum = 13
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class Peek(NDRCALL):
    opnum = 14
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class ReceiveCurrent(NDRCALL):
    opnum = 15
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekNext(NDRCALL):
    opnum = 16
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekNextResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekCurrent(NDRCALL):
    opnum = 17
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class Properties(NDRCALL):
    opnum = 18
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class Handle2(NDRCALL):
    opnum = 19
    structure = (

    )

class Handle2Response(NDRCALL):
    structure = (
		('pvarHandle', VARIANT),
    )
        

class ReceiveByLookupId(NDRCALL):
    opnum = 20
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class ReceiveNextByLookupId(NDRCALL):
    opnum = 21
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveNextByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class ReceivePreviousByLookupId(NDRCALL):
    opnum = 22
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceivePreviousByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class ReceiveFirstByLookupId(NDRCALL):
    opnum = 23
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveFirstByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class ReceiveLastByLookupId(NDRCALL):
    opnum = 24
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveLastByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekByLookupId(NDRCALL):
    opnum = 25
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekNextByLookupId(NDRCALL):
    opnum = 26
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekNextByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekPreviousByLookupId(NDRCALL):
    opnum = 27
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekPreviousByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekFirstByLookupId(NDRCALL):
    opnum = 28
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekFirstByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class PeekLastByLookupId(NDRCALL):
    opnum = 29
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekLastByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE3),
    )
        

class Purge(NDRCALL):
    opnum = 30
    structure = (

    )

class PurgeResponse(NDRCALL):
    structure = (

    )
        

class IsOpen2(NDRCALL):
    opnum = 31
    structure = (

    )

class IsOpen2Response(NDRCALL):
    structure = (
		('pisOpen', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (Access,AccessResponse),
1 : (ShareMode,ShareModeResponse),
2 : (QueueInfo,QueueInfoResponse),
3 : (Handle,HandleResponse),
4 : (IsOpen,IsOpenResponse),
5 : (Close,CloseResponse),
6 : (Receive_v1,Receive_v1Response),
7 : (Peek_v1,Peek_v1Response),
8 : (EnableNotification,EnableNotificationResponse),
9 : (Reset,ResetResponse),
10 : (ReceiveCurrent_v1,ReceiveCurrent_v1Response),
11 : (PeekNext_v1,PeekNext_v1Response),
12 : (PeekCurrent_v1,PeekCurrent_v1Response),
13 : (Receive,ReceiveResponse),
14 : (Peek,PeekResponse),
15 : (ReceiveCurrent,ReceiveCurrentResponse),
16 : (PeekNext,PeekNextResponse),
17 : (PeekCurrent,PeekCurrentResponse),
18 : (Properties,PropertiesResponse),
19 : (Handle2,Handle2Response),
20 : (ReceiveByLookupId,ReceiveByLookupIdResponse),
21 : (ReceiveNextByLookupId,ReceiveNextByLookupIdResponse),
22 : (ReceivePreviousByLookupId,ReceivePreviousByLookupIdResponse),
23 : (ReceiveFirstByLookupId,ReceiveFirstByLookupIdResponse),
24 : (ReceiveLastByLookupId,ReceiveLastByLookupIdResponse),
25 : (PeekByLookupId,PeekByLookupIdResponse),
26 : (PeekNextByLookupId,PeekNextByLookupIdResponse),
27 : (PeekPreviousByLookupId,PeekPreviousByLookupIdResponse),
28 : (PeekFirstByLookupId,PeekFirstByLookupIdResponse),
29 : (PeekLastByLookupId,PeekLastByLookupIdResponse),
30 : (Purge,PurgeResponse),
31 : (IsOpen2,IsOpen2Response),
}

#################################################################################

#IMSMQQueue4 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUE4 = uuidtup_to_bin(('eba96b20-2168-113-898-00020746','0.0'))


class Access(NDRCALL):
    opnum = 0
    structure = (

    )

class AccessResponse(NDRCALL):
    structure = (
		('plAccess', LONG),
    )
        

class ShareMode(NDRCALL):
    opnum = 1
    structure = (

    )

class ShareModeResponse(NDRCALL):
    structure = (
		('plShareMode', LONG),
    )
        

class QueueInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class QueueInfoResponse(NDRCALL):
    structure = (
		('ppqinfo', IMSMQQUEUEINFO4),
    )
        

class Handle(NDRCALL):
    opnum = 3
    structure = (

    )

class HandleResponse(NDRCALL):
    structure = (
		('plHandle', LONG),
    )
        

class IsOpen(NDRCALL):
    opnum = 4
    structure = (

    )

class IsOpenResponse(NDRCALL):
    structure = (
		('pisOpen', SHORT),
    )
        

class Close(NDRCALL):
    opnum = 5
    structure = (

    )

class CloseResponse(NDRCALL):
    structure = (

    )
        

class Receive_v1(NDRCALL):
    opnum = 6
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Receive_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Peek_v1(NDRCALL):
    opnum = 7
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class Peek_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class EnableNotification(NDRCALL):
    opnum = 8
    structure = (
		('Event', IMSMQEVENT3),
		('Cursor', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class EnableNotificationResponse(NDRCALL):
    structure = (

    )
        

class Reset(NDRCALL):
    opnum = 9
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class ReceiveCurrent_v1(NDRCALL):
    opnum = 10
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class ReceiveCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekNext_v1(NDRCALL):
    opnum = 11
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekNext_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class PeekCurrent_v1(NDRCALL):
    opnum = 12
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
    )

class PeekCurrent_v1Response(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE),
    )
        

class Receive(NDRCALL):
    opnum = 13
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class Peek(NDRCALL):
    opnum = 14
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class ReceiveCurrent(NDRCALL):
    opnum = 15
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekNext(NDRCALL):
    opnum = 16
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekNextResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekCurrent(NDRCALL):
    opnum = 17
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('ReceiveTimeout', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekCurrentResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class Properties(NDRCALL):
    opnum = 18
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class Handle2(NDRCALL):
    opnum = 19
    structure = (

    )

class Handle2Response(NDRCALL):
    structure = (
		('pvarHandle', VARIANT),
    )
        

class ReceiveByLookupId(NDRCALL):
    opnum = 20
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class ReceiveNextByLookupId(NDRCALL):
    opnum = 21
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveNextByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class ReceivePreviousByLookupId(NDRCALL):
    opnum = 22
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceivePreviousByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class ReceiveFirstByLookupId(NDRCALL):
    opnum = 23
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveFirstByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class ReceiveLastByLookupId(NDRCALL):
    opnum = 24
    structure = (
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveLastByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekByLookupId(NDRCALL):
    opnum = 25
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekNextByLookupId(NDRCALL):
    opnum = 26
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekNextByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekPreviousByLookupId(NDRCALL):
    opnum = 27
    structure = (
		('LookupId', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekPreviousByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekFirstByLookupId(NDRCALL):
    opnum = 28
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekFirstByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class PeekLastByLookupId(NDRCALL):
    opnum = 29
    structure = (
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class PeekLastByLookupIdResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        

class Purge(NDRCALL):
    opnum = 30
    structure = (

    )

class PurgeResponse(NDRCALL):
    structure = (

    )
        

class IsOpen2(NDRCALL):
    opnum = 31
    structure = (

    )

class IsOpen2Response(NDRCALL):
    structure = (
		('pisOpen', VARIANT_BOOL),
    )
        

class ReceiveByLookupIdAllowPeek(NDRCALL):
    opnum = 32
    structure = (
		('LookupId', VARIANT),
		('Transaction', VARIANT),
		('WantDestinationQueue', VARIANT),
		('WantBody', VARIANT),
		('WantConnectorType', VARIANT),
    )

class ReceiveByLookupIdAllowPeekResponse(NDRCALL):
    structure = (
		('ppmsg', IMSMQMESSAGE4),
    )
        
OPNUMS = {
0 : (Access,AccessResponse),
1 : (ShareMode,ShareModeResponse),
2 : (QueueInfo,QueueInfoResponse),
3 : (Handle,HandleResponse),
4 : (IsOpen,IsOpenResponse),
5 : (Close,CloseResponse),
6 : (Receive_v1,Receive_v1Response),
7 : (Peek_v1,Peek_v1Response),
8 : (EnableNotification,EnableNotificationResponse),
9 : (Reset,ResetResponse),
10 : (ReceiveCurrent_v1,ReceiveCurrent_v1Response),
11 : (PeekNext_v1,PeekNext_v1Response),
12 : (PeekCurrent_v1,PeekCurrent_v1Response),
13 : (Receive,ReceiveResponse),
14 : (Peek,PeekResponse),
15 : (ReceiveCurrent,ReceiveCurrentResponse),
16 : (PeekNext,PeekNextResponse),
17 : (PeekCurrent,PeekCurrentResponse),
18 : (Properties,PropertiesResponse),
19 : (Handle2,Handle2Response),
20 : (ReceiveByLookupId,ReceiveByLookupIdResponse),
21 : (ReceiveNextByLookupId,ReceiveNextByLookupIdResponse),
22 : (ReceivePreviousByLookupId,ReceivePreviousByLookupIdResponse),
23 : (ReceiveFirstByLookupId,ReceiveFirstByLookupIdResponse),
24 : (ReceiveLastByLookupId,ReceiveLastByLookupIdResponse),
25 : (PeekByLookupId,PeekByLookupIdResponse),
26 : (PeekNextByLookupId,PeekNextByLookupIdResponse),
27 : (PeekPreviousByLookupId,PeekPreviousByLookupIdResponse),
28 : (PeekFirstByLookupId,PeekFirstByLookupIdResponse),
29 : (PeekLastByLookupId,PeekLastByLookupIdResponse),
30 : (Purge,PurgeResponse),
31 : (IsOpen2,IsOpen2Response),
32 : (ReceiveByLookupIdAllowPeek,ReceiveByLookupIdAllowPeekResponse),
}

#################################################################################

#IMSMQPrivateEvent Definition

#################################################################################

MSRPC_UUID_IMSMQPRIVATEEVENT = uuidtup_to_bin(('D7AB3341-C9D3-111-BB47-00807520','0.0'))


class Hwnd(NDRCALL):
    opnum = 0
    structure = (

    )

class HwndResponse(NDRCALL):
    structure = (
		('phwnd', LONG),
    )
        

class FireArrivedEvent(NDRCALL):
    opnum = 1
    structure = (
		('pq', IMSMQQUEUE),
		('msgcursor', LONG),
    )

class FireArrivedEventResponse(NDRCALL):
    structure = (

    )
        

class FireArrivedErrorEvent(NDRCALL):
    opnum = 2
    structure = (
		('pq', IMSMQQUEUE),
		('hrStatus', HRESULT),
		('msgcursor', LONG),
    )

class FireArrivedErrorEventResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Hwnd,HwndResponse),
1 : (FireArrivedEvent,FireArrivedEventResponse),
2 : (FireArrivedErrorEvent,FireArrivedErrorEventResponse),
}

#################################################################################

#IMSMQEvent Definition

#################################################################################

MSRPC_UUID_IMSMQEVENT = uuidtup_to_bin(('D7D6E077-DCCD-110-AA4B-0060970EBAE','0.0'))

OPNUMS = {
}

#################################################################################

#IMSMQEvent2 Definition

#################################################################################

MSRPC_UUID_IMSMQEVENT2 = uuidtup_to_bin(('eba96b12-2168-113-898-00020746','0.0'))


class Properties(NDRCALL):
    opnum = 0
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQEvent3 Definition

#################################################################################

MSRPC_UUID_IMSMQEVENT3 = uuidtup_to_bin(('eba96b1c-2168-113-898-00020746','0.0'))

OPNUMS = {
}

#################################################################################

#IMSMQQueueInfo Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFO = uuidtup_to_bin(('D7D6E07B-DCCD-110-AA4B-0060970EBAE','0.0'))


class QueueGuid(NDRCALL):
    opnum = 0
    structure = (

    )

class QueueGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidQueue', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 1
    structure = (

    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidServiceType', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 2
    structure = (
		('bstrGuidServiceType', BSTR),
    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 3
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 4
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class PathName(NDRCALL):
    opnum = 5
    structure = (

    )

class PathNameResponse(NDRCALL):
    structure = (
		('pbstrPathName', BSTR),
    )
        

class PathName(NDRCALL):
    opnum = 6
    structure = (
		('bstrPathName', BSTR),
    )

class PathNameResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 7
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class FormatName(NDRCALL):
    opnum = 8
    structure = (
		('bstrFormatName', BSTR),
    )

class FormatNameResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional(NDRCALL):
    opnum = 9
    structure = (

    )

class IsTransactionalResponse(NDRCALL):
    structure = (
		('pisTransactional', SHORT),
    )
        

class PrivLevel(NDRCALL):
    opnum = 10
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 11
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class Quota(NDRCALL):
    opnum = 14
    structure = (

    )

class QuotaResponse(NDRCALL):
    structure = (
		('plQuota', LONG),
    )
        

class Quota(NDRCALL):
    opnum = 15
    structure = (
		('lQuota', LONG),
    )

class QuotaResponse(NDRCALL):
    structure = (

    )
        

class BasePriority(NDRCALL):
    opnum = 16
    structure = (

    )

class BasePriorityResponse(NDRCALL):
    structure = (
		('plBasePriority', LONG),
    )
        

class BasePriority(NDRCALL):
    opnum = 17
    structure = (
		('lBasePriority', LONG),
    )

class BasePriorityResponse(NDRCALL):
    structure = (

    )
        

class CreateTime(NDRCALL):
    opnum = 18
    structure = (

    )

class CreateTimeResponse(NDRCALL):
    structure = (
		('pvarCreateTime', VARIANT),
    )
        

class ModifyTime(NDRCALL):
    opnum = 19
    structure = (

    )

class ModifyTimeResponse(NDRCALL):
    structure = (
		('pvarModifyTime', VARIANT),
    )
        

class Authenticate(NDRCALL):
    opnum = 20
    structure = (

    )

class AuthenticateResponse(NDRCALL):
    structure = (
		('plAuthenticate', LONG),
    )
        

class Authenticate(NDRCALL):
    opnum = 21
    structure = (
		('lAuthenticate', LONG),
    )

class AuthenticateResponse(NDRCALL):
    structure = (

    )
        

class JournalQuota(NDRCALL):
    opnum = 22
    structure = (

    )

class JournalQuotaResponse(NDRCALL):
    structure = (
		('plJournalQuota', LONG),
    )
        

class JournalQuota(NDRCALL):
    opnum = 23
    structure = (
		('lJournalQuota', LONG),
    )

class JournalQuotaResponse(NDRCALL):
    structure = (

    )
        

class IsWorldReadable(NDRCALL):
    opnum = 24
    structure = (

    )

class IsWorldReadableResponse(NDRCALL):
    structure = (
		('pisWorldReadable', SHORT),
    )
        

class Create(NDRCALL):
    opnum = 25
    structure = (
		('IsTransactional', VARIANT),
		('IsWorldReadable', VARIANT),
    )

class CreateResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 26
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Open(NDRCALL):
    opnum = 27
    structure = (
		('Access', LONG),
		('ShareMode', LONG),
    )

class OpenResponse(NDRCALL):
    structure = (
		('ppq', IMSMQQUEUE),
    )
        

class Refresh(NDRCALL):
    opnum = 28
    structure = (

    )

class RefreshResponse(NDRCALL):
    structure = (

    )
        

class Update(NDRCALL):
    opnum = 29
    structure = (

    )

class UpdateResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (QueueGuid,QueueGuidResponse),
1 : (ServiceTypeGuid,ServiceTypeGuidResponse),
2 : (Label,LabelResponse),
3 : (PathName,PathNameResponse),
4 : (FormatName,FormatNameResponse),
5 : (IsTransactional,IsTransactionalResponse),
6 : (PrivLevel,PrivLevelResponse),
7 : (Journal,JournalResponse),
8 : (Quota,QuotaResponse),
9 : (BasePriority,BasePriorityResponse),
10 : (CreateTime,CreateTimeResponse),
11 : (ModifyTime,ModifyTimeResponse),
12 : (Authenticate,AuthenticateResponse),
13 : (JournalQuota,JournalQuotaResponse),
14 : (IsWorldReadable,IsWorldReadableResponse),
15 : (Create,CreateResponse),
16 : (Delete,DeleteResponse),
17 : (Open,OpenResponse),
18 : (Refresh,RefreshResponse),
19 : (Update,UpdateResponse),
}

#################################################################################

#IMSMQQueueInfo2 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFO2 = uuidtup_to_bin(('FD174A80-89F-112-B0F2-00020746','0.0'))


class QueueGuid(NDRCALL):
    opnum = 0
    structure = (

    )

class QueueGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidQueue', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 1
    structure = (

    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidServiceType', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 2
    structure = (
		('bstrGuidServiceType', BSTR),
    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 3
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 4
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class PathName(NDRCALL):
    opnum = 5
    structure = (

    )

class PathNameResponse(NDRCALL):
    structure = (
		('pbstrPathName', BSTR),
    )
        

class PathName(NDRCALL):
    opnum = 6
    structure = (
		('bstrPathName', BSTR),
    )

class PathNameResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 7
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class FormatName(NDRCALL):
    opnum = 8
    structure = (
		('bstrFormatName', BSTR),
    )

class FormatNameResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional(NDRCALL):
    opnum = 9
    structure = (

    )

class IsTransactionalResponse(NDRCALL):
    structure = (
		('pisTransactional', SHORT),
    )
        

class PrivLevel(NDRCALL):
    opnum = 10
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 11
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class Quota(NDRCALL):
    opnum = 14
    structure = (

    )

class QuotaResponse(NDRCALL):
    structure = (
		('plQuota', LONG),
    )
        

class Quota(NDRCALL):
    opnum = 15
    structure = (
		('lQuota', LONG),
    )

class QuotaResponse(NDRCALL):
    structure = (

    )
        

class BasePriority(NDRCALL):
    opnum = 16
    structure = (

    )

class BasePriorityResponse(NDRCALL):
    structure = (
		('plBasePriority', LONG),
    )
        

class BasePriority(NDRCALL):
    opnum = 17
    structure = (
		('lBasePriority', LONG),
    )

class BasePriorityResponse(NDRCALL):
    structure = (

    )
        

class CreateTime(NDRCALL):
    opnum = 18
    structure = (

    )

class CreateTimeResponse(NDRCALL):
    structure = (
		('pvarCreateTime', VARIANT),
    )
        

class ModifyTime(NDRCALL):
    opnum = 19
    structure = (

    )

class ModifyTimeResponse(NDRCALL):
    structure = (
		('pvarModifyTime', VARIANT),
    )
        

class Authenticate(NDRCALL):
    opnum = 20
    structure = (

    )

class AuthenticateResponse(NDRCALL):
    structure = (
		('plAuthenticate', LONG),
    )
        

class Authenticate(NDRCALL):
    opnum = 21
    structure = (
		('lAuthenticate', LONG),
    )

class AuthenticateResponse(NDRCALL):
    structure = (

    )
        

class JournalQuota(NDRCALL):
    opnum = 22
    structure = (

    )

class JournalQuotaResponse(NDRCALL):
    structure = (
		('plJournalQuota', LONG),
    )
        

class JournalQuota(NDRCALL):
    opnum = 23
    structure = (
		('lJournalQuota', LONG),
    )

class JournalQuotaResponse(NDRCALL):
    structure = (

    )
        

class IsWorldReadable(NDRCALL):
    opnum = 24
    structure = (

    )

class IsWorldReadableResponse(NDRCALL):
    structure = (
		('pisWorldReadable', SHORT),
    )
        

class Create(NDRCALL):
    opnum = 25
    structure = (
		('IsTransactional', VARIANT),
		('IsWorldReadable', VARIANT),
    )

class CreateResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 26
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Open(NDRCALL):
    opnum = 27
    structure = (
		('Access', LONG),
		('ShareMode', LONG),
    )

class OpenResponse(NDRCALL):
    structure = (
		('ppq', IMSMQQUEUE2),
    )
        

class Refresh(NDRCALL):
    opnum = 28
    structure = (

    )

class RefreshResponse(NDRCALL):
    structure = (

    )
        

class Update(NDRCALL):
    opnum = 29
    structure = (

    )

class UpdateResponse(NDRCALL):
    structure = (

    )
        

class PathNameDNS(NDRCALL):
    opnum = 30
    structure = (

    )

class PathNameDNSResponse(NDRCALL):
    structure = (
		('pbstrPathNameDNS', BSTR),
    )
        

class Properties(NDRCALL):
    opnum = 31
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class Security(NDRCALL):
    opnum = 32
    structure = (

    )

class SecurityResponse(NDRCALL):
    structure = (
		('pvarSecurity', VARIANT),
    )
        

class Security(NDRCALL):
    opnum = 33
    structure = (
		('varSecurity', VARIANT),
    )

class SecurityResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (QueueGuid,QueueGuidResponse),
1 : (ServiceTypeGuid,ServiceTypeGuidResponse),
2 : (Label,LabelResponse),
3 : (PathName,PathNameResponse),
4 : (FormatName,FormatNameResponse),
5 : (IsTransactional,IsTransactionalResponse),
6 : (PrivLevel,PrivLevelResponse),
7 : (Journal,JournalResponse),
8 : (Quota,QuotaResponse),
9 : (BasePriority,BasePriorityResponse),
10 : (CreateTime,CreateTimeResponse),
11 : (ModifyTime,ModifyTimeResponse),
12 : (Authenticate,AuthenticateResponse),
13 : (JournalQuota,JournalQuotaResponse),
14 : (IsWorldReadable,IsWorldReadableResponse),
15 : (Create,CreateResponse),
16 : (Delete,DeleteResponse),
17 : (Open,OpenResponse),
18 : (Refresh,RefreshResponse),
19 : (Update,UpdateResponse),
20 : (PathNameDNS,PathNameDNSResponse),
21 : (Properties,PropertiesResponse),
22 : (Security,SecurityResponse),
}

#################################################################################

#IMSMQQueueInfo3 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFO3 = uuidtup_to_bin(('eba96b1d-2168-113-898-00020746','0.0'))


class QueueGuid(NDRCALL):
    opnum = 0
    structure = (

    )

class QueueGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidQueue', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 1
    structure = (

    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidServiceType', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 2
    structure = (
		('bstrGuidServiceType', BSTR),
    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 3
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 4
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class PathName(NDRCALL):
    opnum = 5
    structure = (

    )

class PathNameResponse(NDRCALL):
    structure = (
		('pbstrPathName', BSTR),
    )
        

class PathName(NDRCALL):
    opnum = 6
    structure = (
		('bstrPathName', BSTR),
    )

class PathNameResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 7
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class FormatName(NDRCALL):
    opnum = 8
    structure = (
		('bstrFormatName', BSTR),
    )

class FormatNameResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional(NDRCALL):
    opnum = 9
    structure = (

    )

class IsTransactionalResponse(NDRCALL):
    structure = (
		('pisTransactional', SHORT),
    )
        

class PrivLevel(NDRCALL):
    opnum = 10
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 11
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class Quota(NDRCALL):
    opnum = 14
    structure = (

    )

class QuotaResponse(NDRCALL):
    structure = (
		('plQuota', LONG),
    )
        

class Quota(NDRCALL):
    opnum = 15
    structure = (
		('lQuota', LONG),
    )

class QuotaResponse(NDRCALL):
    structure = (

    )
        

class BasePriority(NDRCALL):
    opnum = 16
    structure = (

    )

class BasePriorityResponse(NDRCALL):
    structure = (
		('plBasePriority', LONG),
    )
        

class BasePriority(NDRCALL):
    opnum = 17
    structure = (
		('lBasePriority', LONG),
    )

class BasePriorityResponse(NDRCALL):
    structure = (

    )
        

class CreateTime(NDRCALL):
    opnum = 18
    structure = (

    )

class CreateTimeResponse(NDRCALL):
    structure = (
		('pvarCreateTime', VARIANT),
    )
        

class ModifyTime(NDRCALL):
    opnum = 19
    structure = (

    )

class ModifyTimeResponse(NDRCALL):
    structure = (
		('pvarModifyTime', VARIANT),
    )
        

class Authenticate(NDRCALL):
    opnum = 20
    structure = (

    )

class AuthenticateResponse(NDRCALL):
    structure = (
		('plAuthenticate', LONG),
    )
        

class Authenticate(NDRCALL):
    opnum = 21
    structure = (
		('lAuthenticate', LONG),
    )

class AuthenticateResponse(NDRCALL):
    structure = (

    )
        

class JournalQuota(NDRCALL):
    opnum = 22
    structure = (

    )

class JournalQuotaResponse(NDRCALL):
    structure = (
		('plJournalQuota', LONG),
    )
        

class JournalQuota(NDRCALL):
    opnum = 23
    structure = (
		('lJournalQuota', LONG),
    )

class JournalQuotaResponse(NDRCALL):
    structure = (

    )
        

class IsWorldReadable(NDRCALL):
    opnum = 24
    structure = (

    )

class IsWorldReadableResponse(NDRCALL):
    structure = (
		('pisWorldReadable', SHORT),
    )
        

class Create(NDRCALL):
    opnum = 25
    structure = (
		('IsTransactional', VARIANT),
		('IsWorldReadable', VARIANT),
    )

class CreateResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 26
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Open(NDRCALL):
    opnum = 27
    structure = (
		('Access', LONG),
		('ShareMode', LONG),
    )

class OpenResponse(NDRCALL):
    structure = (
		('ppq', IMSMQQUEUE3),
    )
        

class Refresh(NDRCALL):
    opnum = 28
    structure = (

    )

class RefreshResponse(NDRCALL):
    structure = (

    )
        

class Update(NDRCALL):
    opnum = 29
    structure = (

    )

class UpdateResponse(NDRCALL):
    structure = (

    )
        

class PathNameDNS(NDRCALL):
    opnum = 30
    structure = (

    )

class PathNameDNSResponse(NDRCALL):
    structure = (
		('pbstrPathNameDNS', BSTR),
    )
        

class Properties(NDRCALL):
    opnum = 31
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class Security(NDRCALL):
    opnum = 32
    structure = (

    )

class SecurityResponse(NDRCALL):
    structure = (
		('pvarSecurity', VARIANT),
    )
        

class Security(NDRCALL):
    opnum = 33
    structure = (
		('varSecurity', VARIANT),
    )

class SecurityResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional2(NDRCALL):
    opnum = 34
    structure = (

    )

class IsTransactional2Response(NDRCALL):
    structure = (
		('pisTransactional', VARIANT_BOOL),
    )
        

class IsWorldReadable2(NDRCALL):
    opnum = 35
    structure = (

    )

class IsWorldReadable2Response(NDRCALL):
    structure = (
		('pisWorldReadable', VARIANT_BOOL),
    )
        

class MulticastAddress(NDRCALL):
    opnum = 36
    structure = (

    )

class MulticastAddressResponse(NDRCALL):
    structure = (
		('pbstrMulticastAddress', BSTR),
    )
        

class MulticastAddress(NDRCALL):
    opnum = 37
    structure = (
		('bstrMulticastAddress', BSTR),
    )

class MulticastAddressResponse(NDRCALL):
    structure = (

    )
        

class ADsPath(NDRCALL):
    opnum = 38
    structure = (

    )

class ADsPathResponse(NDRCALL):
    structure = (
		('pbstrADsPath', BSTR),
    )
        
OPNUMS = {
0 : (QueueGuid,QueueGuidResponse),
1 : (ServiceTypeGuid,ServiceTypeGuidResponse),
2 : (Label,LabelResponse),
3 : (PathName,PathNameResponse),
4 : (FormatName,FormatNameResponse),
5 : (IsTransactional,IsTransactionalResponse),
6 : (PrivLevel,PrivLevelResponse),
7 : (Journal,JournalResponse),
8 : (Quota,QuotaResponse),
9 : (BasePriority,BasePriorityResponse),
10 : (CreateTime,CreateTimeResponse),
11 : (ModifyTime,ModifyTimeResponse),
12 : (Authenticate,AuthenticateResponse),
13 : (JournalQuota,JournalQuotaResponse),
14 : (IsWorldReadable,IsWorldReadableResponse),
15 : (Create,CreateResponse),
16 : (Delete,DeleteResponse),
17 : (Open,OpenResponse),
18 : (Refresh,RefreshResponse),
19 : (Update,UpdateResponse),
20 : (PathNameDNS,PathNameDNSResponse),
21 : (Properties,PropertiesResponse),
22 : (Security,SecurityResponse),
23 : (IsTransactional2,IsTransactional2Response),
24 : (IsWorldReadable2,IsWorldReadable2Response),
25 : (MulticastAddress,MulticastAddressResponse),
26 : (ADsPath,ADsPathResponse),
}

#################################################################################

#IMSMQQueueInfo4 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFO4 = uuidtup_to_bin(('eba96b21-2168-113-898-00020746','0.0'))


class QueueGuid(NDRCALL):
    opnum = 0
    structure = (

    )

class QueueGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidQueue', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 1
    structure = (

    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (
		('pbstrGuidServiceType', BSTR),
    )
        

class ServiceTypeGuid(NDRCALL):
    opnum = 2
    structure = (
		('bstrGuidServiceType', BSTR),
    )

class ServiceTypeGuidResponse(NDRCALL):
    structure = (

    )
        

class Label(NDRCALL):
    opnum = 3
    structure = (

    )

class LabelResponse(NDRCALL):
    structure = (
		('pbstrLabel', BSTR),
    )
        

class Label(NDRCALL):
    opnum = 4
    structure = (
		('bstrLabel', BSTR),
    )

class LabelResponse(NDRCALL):
    structure = (

    )
        

class PathName(NDRCALL):
    opnum = 5
    structure = (

    )

class PathNameResponse(NDRCALL):
    structure = (
		('pbstrPathName', BSTR),
    )
        

class PathName(NDRCALL):
    opnum = 6
    structure = (
		('bstrPathName', BSTR),
    )

class PathNameResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 7
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class FormatName(NDRCALL):
    opnum = 8
    structure = (
		('bstrFormatName', BSTR),
    )

class FormatNameResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional(NDRCALL):
    opnum = 9
    structure = (

    )

class IsTransactionalResponse(NDRCALL):
    structure = (
		('pisTransactional', SHORT),
    )
        

class PrivLevel(NDRCALL):
    opnum = 10
    structure = (

    )

class PrivLevelResponse(NDRCALL):
    structure = (
		('plPrivLevel', LONG),
    )
        

class PrivLevel(NDRCALL):
    opnum = 11
    structure = (
		('lPrivLevel', LONG),
    )

class PrivLevelResponse(NDRCALL):
    structure = (

    )
        

class Journal(NDRCALL):
    opnum = 12
    structure = (

    )

class JournalResponse(NDRCALL):
    structure = (
		('plJournal', LONG),
    )
        

class Journal(NDRCALL):
    opnum = 13
    structure = (
		('lJournal', LONG),
    )

class JournalResponse(NDRCALL):
    structure = (

    )
        

class Quota(NDRCALL):
    opnum = 14
    structure = (

    )

class QuotaResponse(NDRCALL):
    structure = (
		('plQuota', LONG),
    )
        

class Quota(NDRCALL):
    opnum = 15
    structure = (
		('lQuota', LONG),
    )

class QuotaResponse(NDRCALL):
    structure = (

    )
        

class BasePriority(NDRCALL):
    opnum = 16
    structure = (

    )

class BasePriorityResponse(NDRCALL):
    structure = (
		('plBasePriority', LONG),
    )
        

class BasePriority(NDRCALL):
    opnum = 17
    structure = (
		('lBasePriority', LONG),
    )

class BasePriorityResponse(NDRCALL):
    structure = (

    )
        

class CreateTime(NDRCALL):
    opnum = 18
    structure = (

    )

class CreateTimeResponse(NDRCALL):
    structure = (
		('pvarCreateTime', VARIANT),
    )
        

class ModifyTime(NDRCALL):
    opnum = 19
    structure = (

    )

class ModifyTimeResponse(NDRCALL):
    structure = (
		('pvarModifyTime', VARIANT),
    )
        

class Authenticate(NDRCALL):
    opnum = 20
    structure = (

    )

class AuthenticateResponse(NDRCALL):
    structure = (
		('plAuthenticate', LONG),
    )
        

class Authenticate(NDRCALL):
    opnum = 21
    structure = (
		('lAuthenticate', LONG),
    )

class AuthenticateResponse(NDRCALL):
    structure = (

    )
        

class JournalQuota(NDRCALL):
    opnum = 22
    structure = (

    )

class JournalQuotaResponse(NDRCALL):
    structure = (
		('plJournalQuota', LONG),
    )
        

class JournalQuota(NDRCALL):
    opnum = 23
    structure = (
		('lJournalQuota', LONG),
    )

class JournalQuotaResponse(NDRCALL):
    structure = (

    )
        

class IsWorldReadable(NDRCALL):
    opnum = 24
    structure = (

    )

class IsWorldReadableResponse(NDRCALL):
    structure = (
		('pisWorldReadable', SHORT),
    )
        

class Create(NDRCALL):
    opnum = 25
    structure = (
		('IsTransactional', VARIANT),
		('IsWorldReadable', VARIANT),
    )

class CreateResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 26
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Open(NDRCALL):
    opnum = 27
    structure = (
		('Access', LONG),
		('ShareMode', LONG),
    )

class OpenResponse(NDRCALL):
    structure = (
		('ppq', IMSMQQUEUE4),
    )
        

class Refresh(NDRCALL):
    opnum = 28
    structure = (

    )

class RefreshResponse(NDRCALL):
    structure = (

    )
        

class Update(NDRCALL):
    opnum = 29
    structure = (

    )

class UpdateResponse(NDRCALL):
    structure = (

    )
        

class PathNameDNS(NDRCALL):
    opnum = 30
    structure = (

    )

class PathNameDNSResponse(NDRCALL):
    structure = (
		('pbstrPathNameDNS', BSTR),
    )
        

class Properties(NDRCALL):
    opnum = 31
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        

class Security(NDRCALL):
    opnum = 32
    structure = (

    )

class SecurityResponse(NDRCALL):
    structure = (
		('pvarSecurity', VARIANT),
    )
        

class Security(NDRCALL):
    opnum = 33
    structure = (
		('varSecurity', VARIANT),
    )

class SecurityResponse(NDRCALL):
    structure = (

    )
        

class IsTransactional2(NDRCALL):
    opnum = 34
    structure = (

    )

class IsTransactional2Response(NDRCALL):
    structure = (
		('pisTransactional', VARIANT_BOOL),
    )
        

class IsWorldReadable2(NDRCALL):
    opnum = 35
    structure = (

    )

class IsWorldReadable2Response(NDRCALL):
    structure = (
		('pisWorldReadable', VARIANT_BOOL),
    )
        

class MulticastAddress(NDRCALL):
    opnum = 36
    structure = (

    )

class MulticastAddressResponse(NDRCALL):
    structure = (
		('pbstrMulticastAddress', BSTR),
    )
        

class MulticastAddress(NDRCALL):
    opnum = 37
    structure = (
		('bstrMulticastAddress', BSTR),
    )

class MulticastAddressResponse(NDRCALL):
    structure = (

    )
        

class ADsPath(NDRCALL):
    opnum = 38
    structure = (

    )

class ADsPathResponse(NDRCALL):
    structure = (
		('pbstrADsPath', BSTR),
    )
        
OPNUMS = {
0 : (QueueGuid,QueueGuidResponse),
1 : (ServiceTypeGuid,ServiceTypeGuidResponse),
2 : (Label,LabelResponse),
3 : (PathName,PathNameResponse),
4 : (FormatName,FormatNameResponse),
5 : (IsTransactional,IsTransactionalResponse),
6 : (PrivLevel,PrivLevelResponse),
7 : (Journal,JournalResponse),
8 : (Quota,QuotaResponse),
9 : (BasePriority,BasePriorityResponse),
10 : (CreateTime,CreateTimeResponse),
11 : (ModifyTime,ModifyTimeResponse),
12 : (Authenticate,AuthenticateResponse),
13 : (JournalQuota,JournalQuotaResponse),
14 : (IsWorldReadable,IsWorldReadableResponse),
15 : (Create,CreateResponse),
16 : (Delete,DeleteResponse),
17 : (Open,OpenResponse),
18 : (Refresh,RefreshResponse),
19 : (Update,UpdateResponse),
20 : (PathNameDNS,PathNameDNSResponse),
21 : (Properties,PropertiesResponse),
22 : (Security,SecurityResponse),
23 : (IsTransactional2,IsTransactional2Response),
24 : (IsWorldReadable2,IsWorldReadable2Response),
25 : (MulticastAddress,MulticastAddressResponse),
26 : (ADsPath,ADsPathResponse),
}

#################################################################################

#IMSMQQueueInfos Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFOS = uuidtup_to_bin(('D7D6E07D-DCCD-110-AA4B-0060970EBAE','0.0'))


class Reset(NDRCALL):
    opnum = 0
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class Next(NDRCALL):
    opnum = 1
    structure = (

    )

class NextResponse(NDRCALL):
    structure = (
		('ppqinfoNext', IMSMQQUEUEINFO),
    )
        
OPNUMS = {
0 : (Reset,ResetResponse),
1 : (Next,NextResponse),
}

#################################################################################

#IMSMQQueueInfos2 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFOS2 = uuidtup_to_bin(('eba96b0f-2168-113-898-00020746','0.0'))


class Reset(NDRCALL):
    opnum = 0
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class Next(NDRCALL):
    opnum = 1
    structure = (

    )

class NextResponse(NDRCALL):
    structure = (
		('ppqinfoNext', IMSMQQUEUEINFO2),
    )
        

class Properties(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Reset,ResetResponse),
1 : (Next,NextResponse),
2 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQQueueInfos3 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFOS3 = uuidtup_to_bin(('eba96b1e-2168-113-898-00020746','0.0'))


class Reset(NDRCALL):
    opnum = 0
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class Next(NDRCALL):
    opnum = 1
    structure = (

    )

class NextResponse(NDRCALL):
    structure = (
		('ppqinfoNext', IMSMQQUEUEINFO3),
    )
        

class Properties(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Reset,ResetResponse),
1 : (Next,NextResponse),
2 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQQueueInfos4 Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEINFOS4 = uuidtup_to_bin(('eba96b22-2168-113-898-00020746','0.0'))


class Reset(NDRCALL):
    opnum = 0
    structure = (

    )

class ResetResponse(NDRCALL):
    structure = (

    )
        

class Next(NDRCALL):
    opnum = 1
    structure = (

    )

class NextResponse(NDRCALL):
    structure = (
		('ppqinfoNext', IMSMQQUEUEINFO4),
    )
        

class Properties(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Reset,ResetResponse),
1 : (Next,NextResponse),
2 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQTransaction Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTION = uuidtup_to_bin(('D7D6E07F-DCCD-110-AA4B-0060970EBAE','0.0'))


class Transaction(NDRCALL):
    opnum = 0
    structure = (

    )

class TransactionResponse(NDRCALL):
    structure = (
		('plTransaction', LONG),
    )
        

class Commit(NDRCALL):
    opnum = 1
    structure = (
		('fRetaining', VARIANT),
		('grfTC', VARIANT),
		('grfRM', VARIANT),
    )

class CommitResponse(NDRCALL):
    structure = (

    )
        

class Abort(NDRCALL):
    opnum = 2
    structure = (
		('fRetaining', VARIANT),
		('fAsync', VARIANT),
    )

class AbortResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Transaction,TransactionResponse),
1 : (Commit,CommitResponse),
2 : (Abort,AbortResponse),
}

#################################################################################

#IMSMQTransaction2 Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTION2 = uuidtup_to_bin(('2CE0C5B0-6E67-11D2-B0E6-00E02C074F6B','0.0'))


class InitNew(NDRCALL):
    opnum = 0
    structure = (
		('varTransaction', VARIANT),
    )

class InitNewResponse(NDRCALL):
    structure = (

    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (InitNew,InitNewResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQTransaction3 Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTION3 = uuidtup_to_bin(('eba96b13-2168-113-898-00020746','0.0'))


class ITransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class ITransactionResponse(NDRCALL):
    structure = (
		('pvarITransaction', VARIANT),
    )
        
OPNUMS = {
0 : (ITransaction,ITransactionResponse),
}

#################################################################################

#IMSMQCoordinatedTransactionDispenser Definition

#################################################################################

MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER = uuidtup_to_bin(('D7D6E081-DCCD-110-AA4B-0060970EBAE','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
}

#################################################################################

#IMSMQCoordinatedTransactionDispenser2 Definition

#################################################################################

MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER2 = uuidtup_to_bin(('eba96b10-2168-113-898-00020746','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION2),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQCoordinatedTransactionDispenser3 Definition

#################################################################################

MSRPC_UUID_IMSMQCOORDINATEDTRANSACTIONDISPENSER3 = uuidtup_to_bin(('eba96b14-2168-113-898-00020746','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION3),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQTransactionDispenser Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTIONDISPENSER = uuidtup_to_bin(('D7D6E083-DCCD-110-AA4B-0060970EBAE','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
}

#################################################################################

#IMSMQTransactionDispenser2 Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTIONDISPENSER2 = uuidtup_to_bin(('eba96b11-2168-113-898-00020746','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION2),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQTransactionDispenser3 Definition

#################################################################################

MSRPC_UUID_IMSMQTRANSACTIONDISPENSER3 = uuidtup_to_bin(('eba96b15-2168-113-898-00020746','0.0'))


class BeginTransaction(NDRCALL):
    opnum = 0
    structure = (

    )

class BeginTransactionResponse(NDRCALL):
    structure = (
		('ptransaction', IMSMQTRANSACTION3),
    )
        

class Properties(NDRCALL):
    opnum = 1
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (BeginTransaction,BeginTransactionResponse),
1 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQApplication Definition

#################################################################################

MSRPC_UUID_IMSMQAPPLICATION = uuidtup_to_bin(('D7D6E085-DCCD-110-AA4B-0060970EBAE','0.0'))


class MachineIdOfMachineName(NDRCALL):
    opnum = 0
    structure = (
		('MachineName', BSTR),
    )

class MachineIdOfMachineNameResponse(NDRCALL):
    structure = (
		('pbstrGuid', BSTR),
    )
        
OPNUMS = {
0 : (MachineIdOfMachineName,MachineIdOfMachineNameResponse),
}

#################################################################################

#IMSMQApplication2 Definition

#################################################################################

MSRPC_UUID_IMSMQAPPLICATION2 = uuidtup_to_bin(('12A30900-7300-11D2-B0E6-00E02C074F6B','0.0'))


class RegisterCertificate(NDRCALL):
    opnum = 0
    structure = (
		('Flags', VARIANT),
		('ExternalCertificate', VARIANT),
    )

class RegisterCertificateResponse(NDRCALL):
    structure = (

    )
        

class MachineNameOfMachineId(NDRCALL):
    opnum = 1
    structure = (
		('bstrGuid', BSTR),
    )

class MachineNameOfMachineIdResponse(NDRCALL):
    structure = (
		('pbstrMachineName', BSTR),
    )
        

class MSMQVersionMajor(NDRCALL):
    opnum = 2
    structure = (

    )

class MSMQVersionMajorResponse(NDRCALL):
    structure = (
		('psMSMQVersionMajor', SHORT),
    )
        

class MSMQVersionMinor(NDRCALL):
    opnum = 3
    structure = (

    )

class MSMQVersionMinorResponse(NDRCALL):
    structure = (
		('psMSMQVersionMinor', SHORT),
    )
        

class MSMQVersionBuild(NDRCALL):
    opnum = 4
    structure = (

    )

class MSMQVersionBuildResponse(NDRCALL):
    structure = (
		('psMSMQVersionBuild', SHORT),
    )
        

class IsDsEnabled(NDRCALL):
    opnum = 5
    structure = (

    )

class IsDsEnabledResponse(NDRCALL):
    structure = (
		('pfIsDsEnabled', VARIANT_BOOL),
    )
        

class Properties(NDRCALL):
    opnum = 6
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (RegisterCertificate,RegisterCertificateResponse),
1 : (MachineNameOfMachineId,MachineNameOfMachineIdResponse),
2 : (MSMQVersionMajor,MSMQVersionMajorResponse),
3 : (MSMQVersionMinor,MSMQVersionMinorResponse),
4 : (MSMQVersionBuild,MSMQVersionBuildResponse),
5 : (IsDsEnabled,IsDsEnabledResponse),
6 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQApplication3 Definition

#################################################################################

MSRPC_UUID_IMSMQAPPLICATION3 = uuidtup_to_bin(('eba96b1f-2168-113-898-00020746','0.0'))


class ActiveQueues(NDRCALL):
    opnum = 0
    structure = (

    )

class ActiveQueuesResponse(NDRCALL):
    structure = (
		('pvActiveQueues', VARIANT),
    )
        

class PrivateQueues(NDRCALL):
    opnum = 1
    structure = (

    )

class PrivateQueuesResponse(NDRCALL):
    structure = (
		('pvPrivateQueues', VARIANT),
    )
        

class DirectoryServiceServer(NDRCALL):
    opnum = 2
    structure = (

    )

class DirectoryServiceServerResponse(NDRCALL):
    structure = (
		('pbstrDirectoryServiceServer', BSTR),
    )
        

class IsConnected(NDRCALL):
    opnum = 3
    structure = (

    )

class IsConnectedResponse(NDRCALL):
    structure = (
		('pfIsConnected', VARIANT_BOOL),
    )
        

class BytesInAllQueues(NDRCALL):
    opnum = 4
    structure = (

    )

class BytesInAllQueuesResponse(NDRCALL):
    structure = (
		('pvBytesInAllQueues', VARIANT),
    )
        

class Machine(NDRCALL):
    opnum = 5
    structure = (
		('bstrMachine', BSTR),
    )

class MachineResponse(NDRCALL):
    structure = (

    )
        

class Machine(NDRCALL):
    opnum = 6
    structure = (

    )

class MachineResponse(NDRCALL):
    structure = (
		('pbstrMachine', BSTR),
    )
        

class Connect(NDRCALL):
    opnum = 7
    structure = (

    )

class ConnectResponse(NDRCALL):
    structure = (

    )
        

class Disconnect(NDRCALL):
    opnum = 8
    structure = (

    )

class DisconnectResponse(NDRCALL):
    structure = (

    )
        

class Tidy(NDRCALL):
    opnum = 9
    structure = (

    )

class TidyResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ActiveQueues,ActiveQueuesResponse),
1 : (PrivateQueues,PrivateQueuesResponse),
2 : (DirectoryServiceServer,DirectoryServiceServerResponse),
3 : (IsConnected,IsConnectedResponse),
4 : (BytesInAllQueues,BytesInAllQueuesResponse),
5 : (Machine,MachineResponse),
6 : (Connect,ConnectResponse),
7 : (Disconnect,DisconnectResponse),
8 : (Tidy,TidyResponse),
}

#################################################################################

#IMSMQDestination Definition

#################################################################################

MSRPC_UUID_IMSMQDESTINATION = uuidtup_to_bin(('eba96b16-2168-113-898-00020746','0.0'))


class Open(NDRCALL):
    opnum = 0
    structure = (

    )

class OpenResponse(NDRCALL):
    structure = (

    )
        

class Close(NDRCALL):
    opnum = 1
    structure = (

    )

class CloseResponse(NDRCALL):
    structure = (

    )
        

class IsOpen(NDRCALL):
    opnum = 2
    structure = (

    )

class IsOpenResponse(NDRCALL):
    structure = (
		('pfIsOpen', VARIANT_BOOL),
    )
        

class IADs(NDRCALL):
    opnum = 3
    structure = (

    )

class IADsResponse(NDRCALL):
    structure = (
		('ppIADs', IDISPATCH),
    )
        

class IADs(NDRCALL):
    opnum = 4
    structure = (
		('pIADs', IDISPATCH),
    )

class IADsResponse(NDRCALL):
    structure = (

    )
        

class ADsPath(NDRCALL):
    opnum = 5
    structure = (

    )

class ADsPathResponse(NDRCALL):
    structure = (
		('pbstrADsPath', BSTR),
    )
        

class ADsPath(NDRCALL):
    opnum = 6
    structure = (
		('bstrADsPath', BSTR),
    )

class ADsPathResponse(NDRCALL):
    structure = (

    )
        

class PathName(NDRCALL):
    opnum = 7
    structure = (

    )

class PathNameResponse(NDRCALL):
    structure = (
		('pbstrPathName', BSTR),
    )
        

class PathName(NDRCALL):
    opnum = 8
    structure = (
		('bstrPathName', BSTR),
    )

class PathNameResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 9
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class FormatName(NDRCALL):
    opnum = 10
    structure = (
		('bstrFormatName', BSTR),
    )

class FormatNameResponse(NDRCALL):
    structure = (

    )
        

class Destinations(NDRCALL):
    opnum = 11
    structure = (

    )

class DestinationsResponse(NDRCALL):
    structure = (
		('ppDestinations', IDISPATCH),
    )
        

class Destinations(NDRCALL):
    opnum = 12
    structure = (
		('pDestinations', IDISPATCH),
    )

class DestinationsResponse(NDRCALL):
    structure = (

    )
        

class Properties(NDRCALL):
    opnum = 13
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('ppcolProperties', IDISPATCH),
    )
        
OPNUMS = {
0 : (Open,OpenResponse),
1 : (Close,CloseResponse),
2 : (IsOpen,IsOpenResponse),
3 : (IADs,IADsResponse),
4 : (ADsPath,ADsPathResponse),
5 : (PathName,PathNameResponse),
6 : (FormatName,FormatNameResponse),
7 : (Destinations,DestinationsResponse),
8 : (Properties,PropertiesResponse),
}

#################################################################################

#IMSMQPrivateDestination Definition

#################################################################################

MSRPC_UUID_IMSMQPRIVATEDESTINATION = uuidtup_to_bin(('eba96b17-2168-113-898-00020746','0.0'))


class Handle(NDRCALL):
    opnum = 0
    structure = (

    )

class HandleResponse(NDRCALL):
    structure = (
		('pvarHandle', VARIANT),
    )
        

class Handle(NDRCALL):
    opnum = 1
    structure = (
		('varHandle', VARIANT),
    )

class HandleResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Handle,HandleResponse),
}

#################################################################################

#IMSMQCollection Definition

#################################################################################

MSRPC_UUID_IMSMQCOLLECTION = uuidtup_to_bin(('0188AC2F-ECB3-4173-9779-635CA2039C72','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('Index', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('pvarRet', VARIANT),
    )
        

class Count(NDRCALL):
    opnum = 1
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('pCount', LONG),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('ppunk', IUNKNOWN),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (Count,CountResponse),
2 : (_NewEnum,_NewEnumResponse),
}

#################################################################################

#IMSMQManagement Definition

#################################################################################

MSRPC_UUID_IMSMQMANAGEMENT = uuidtup_to_bin(('BE5F0241-E489-4957-8C4-A452FCF3E23E','0.0'))


class Init(NDRCALL):
    opnum = 0
    structure = (
		('Machine', VARIANT),
		('Pathname', VARIANT),
		('FormatName', VARIANT),
    )

class InitResponse(NDRCALL):
    structure = (

    )
        

class FormatName(NDRCALL):
    opnum = 1
    structure = (

    )

class FormatNameResponse(NDRCALL):
    structure = (
		('pbstrFormatName', BSTR),
    )
        

class Machine(NDRCALL):
    opnum = 2
    structure = (

    )

class MachineResponse(NDRCALL):
    structure = (
		('pbstrMachine', BSTR),
    )
        

class MessageCount(NDRCALL):
    opnum = 3
    structure = (

    )

class MessageCountResponse(NDRCALL):
    structure = (
		('plMessageCount', LONG),
    )
        

class ForeignStatus(NDRCALL):
    opnum = 4
    structure = (

    )

class ForeignStatusResponse(NDRCALL):
    structure = (
		('plForeignStatus', LONG),
    )
        

class QueueType(NDRCALL):
    opnum = 5
    structure = (

    )

class QueueTypeResponse(NDRCALL):
    structure = (
		('plQueueType', LONG),
    )
        

class IsLocal(NDRCALL):
    opnum = 6
    structure = (

    )

class IsLocalResponse(NDRCALL):
    structure = (
		('pfIsLocal', VARIANT_BOOL),
    )
        

class TransactionalStatus(NDRCALL):
    opnum = 7
    structure = (

    )

class TransactionalStatusResponse(NDRCALL):
    structure = (
		('plTransactionalStatus', LONG),
    )
        

class BytesInQueue(NDRCALL):
    opnum = 8
    structure = (

    )

class BytesInQueueResponse(NDRCALL):
    structure = (
		('pvBytesInQueue', VARIANT),
    )
        
OPNUMS = {
0 : (Init,InitResponse),
1 : (FormatName,FormatNameResponse),
2 : (Machine,MachineResponse),
3 : (MessageCount,MessageCountResponse),
4 : (ForeignStatus,ForeignStatusResponse),
5 : (QueueType,QueueTypeResponse),
6 : (IsLocal,IsLocalResponse),
7 : (TransactionalStatus,TransactionalStatusResponse),
8 : (BytesInQueue,BytesInQueueResponse),
}

#################################################################################

#IMSMQOutgoingQueueManagement Definition

#################################################################################

MSRPC_UUID_IMSMQOUTGOINGQUEUEMANAGEMENT = uuidtup_to_bin(('64C478FB-F9B0-4695-8A7F-439AC94326D3','0.0'))


class State(NDRCALL):
    opnum = 0
    structure = (

    )

class StateResponse(NDRCALL):
    structure = (
		('plState', LONG),
    )
        

class NextHops(NDRCALL):
    opnum = 1
    structure = (

    )

class NextHopsResponse(NDRCALL):
    structure = (
		('pvNextHops', VARIANT),
    )
        

class EodGetSendInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class EodGetSendInfoResponse(NDRCALL):
    structure = (
		('ppCollection', IMSMQCOLLECTION),
    )
        

class Resume(NDRCALL):
    opnum = 3
    structure = (

    )

class ResumeResponse(NDRCALL):
    structure = (

    )
        

class Pause(NDRCALL):
    opnum = 4
    structure = (

    )

class PauseResponse(NDRCALL):
    structure = (

    )
        

class EodResend(NDRCALL):
    opnum = 5
    structure = (

    )

class EodResendResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (State,StateResponse),
1 : (NextHops,NextHopsResponse),
2 : (EodGetSendInfo,EodGetSendInfoResponse),
3 : (Resume,ResumeResponse),
4 : (Pause,PauseResponse),
5 : (EodResend,EodResendResponse),
}

#################################################################################

#IMSMQQueueManagement Definition

#################################################################################

MSRPC_UUID_IMSMQQUEUEMANAGEMENT = uuidtup_to_bin(('7FBE7759-5760-444d-B8A5-5E7AB9A84CCE','0.0'))


class JournalMessageCount(NDRCALL):
    opnum = 0
    structure = (

    )

class JournalMessageCountResponse(NDRCALL):
    structure = (
		('plJournalMessageCount', LONG),
    )
        

class BytesInJournal(NDRCALL):
    opnum = 1
    structure = (

    )

class BytesInJournalResponse(NDRCALL):
    structure = (
		('pvBytesInJournal', VARIANT),
    )
        

class EodGetReceiveInfo(NDRCALL):
    opnum = 2
    structure = (

    )

class EodGetReceiveInfoResponse(NDRCALL):
    structure = (
		('pvCollection', VARIANT),
    )
        
OPNUMS = {
0 : (JournalMessageCount,JournalMessageCountResponse),
1 : (BytesInJournal,BytesInJournalResponse),
2 : (EodGetReceiveInfo,EodGetReceiveInfoResponse),
}

