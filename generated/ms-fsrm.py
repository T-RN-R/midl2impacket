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
        

class ANONYMOUS11(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous11', ANONYMOUS11),
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

FSRM_OBJECT_ID = GUID

FsrmQuotaFlags_Enforce = 256,
FsrmQuotaFlags_Disable = 512,
FsrmQuotaFlags_StatusIncomplete = 65536,
FsrmQuotaFlags_StatusRebuilding = 131072
        

FsrmFileScreenFlags_Enforce = 1
        

FsrmCollectionState_Fetching = 1,
FsrmCollectionState_Committing = 2,
FsrmCollectionState_Complete = 3,
FsrmCollectionState_Cancelled = 4
        

FsrmEnumOptions_None = 0,
FsrmEnumOptions_Asynchronous = 1,
FsrmEnumOptions_CheckRecycleBin = 2,
FsrmEnumOptions_IncludeClusterNodes = 4,
FsrmEnumOptions_IncludeDeprecatedObjects = 8
        

FsrmCommitOptions_None = 0,
FsrmCommitOptions_Asynchronous = 1
        

FsrmTemplateApplyOptions_ApplyToDerivedMatching = 1,
FsrmTemplateApplyOptions_ApplyToDerivedAll = 2
        

FsrmActionType_Unknown = 0,
FsrmActionType_EventLog = 1,
FsrmActionType_Email = 2,
FsrmActionType_Command = 3,
FsrmActionType_Report = 4
        

FsrmEventType_Unknown = 0,
FsrmEventType_Information = 1,
FsrmEventType_Warning = 2,
FsrmEventType_Error = 3
        

FsrmAccountType_Unknown = 0,
FsrmAccountType_NetworkService = 1,
FsrmAccountType_LocalService = 2,
FsrmAccountType_LocalSystem = 3,
FsrmAccountType_InProc = 4,
FsrmAccountType_External = 5,
FsrmAccountType_Automatic = 500
        

FsrmReportType_Unknown = 0,
FsrmReportType_LargeFiles = 1,
FsrmReportType_FilesByType = 2,
FsrmReportType_LeastRecentlyAccessed = 3,
FsrmReportType_MostRecentlyAccessed = 4,
FsrmReportType_QuotaUsage = 5,
FsrmReportType_FilesByOwner = 6,
FsrmReportType_ExportReport = 7,
FsrmReportType_DuplicateFiles = 8,
FsrmReportType_FileScreenAudit = 9,
FsrmReportType_FilesByProperty = 10,
FsrmReportType_AutomaticClassification = 11,
FsrmReportType_Expiration = 12,
FsrmReportType_FoldersByProperty = 13
        

FsrmReportFormat_Unknown = 0,
FsrmReportFormat_DHtml = 1,
FsrmReportFormat_Html = 2,
FsrmReportFormat_Txt = 3,
FsrmReportFormat_Csv = 4,
FsrmReportFormat_Xml = 5
        

FsrmReportRunningStatus_Unknown = 0,
FsrmReportRunningStatus_NotRunning = 1,
FsrmReportRunningStatus_Queued = 2,
FsrmReportRunningStatus_Running = 3
        

FsrmReportGenerationContext_Undefined = 1,
FsrmReportGenerationContext_ScheduledReport = 2,
FsrmReportGenerationContext_InteractiveReport = 3,
FsrmReportGenerationContext_IncidentReport = 4
        

FsrmReportFilter_MinSize = 1,
FsrmReportFilter_MinAgeDays = 2,
FsrmReportFilter_MaxAgeDays = 3,
FsrmReportFilter_MinQuotaUsage = 4,
FsrmReportFilter_FileGroups = 5,
FsrmReportFilter_Owners = 6,
FsrmReportFilter_NamePattern = 7,
FsrmReportFilter_Property = 8
        

FsrmReportLimit_MaxFiles = 1,
FsrmReportLimit_MaxFileGroups = 2,
FsrmReportLimit_MaxOwners = 3,
FsrmReportLimit_MaxFilesPerFileGroup = 4,
FsrmReportLimit_MaxFilesPerOwner = 5,
FsrmReportLimit_MaxFilesPerDuplGroup = 6,
FsrmReportLimit_MaxDuplicateGroups = 7,
FsrmReportLimit_MaxQuotas = 8,
FsrmReportLimit_MaxFileScreenEvents = 9,
FsrmReportLimit_MaxPropertyValues = 10,
FsrmReportLimit_MaxFilesPerPropertyValue = 11,
FsrmReportLimit_MaxFolders = 12
        

FsrmPropertyDefinitionType_Unknown = 0,
FsrmPropertyDefinitionType_OrderedList = 1,
FsrmPropertyDefinitionType_MultiChoiceList = 2,
FsrmPropertyDefinitionType_SingleChoiceList = 3,
FsrmPropertyDefinitionType_String = 4,
FsrmPropertyDefinitionType_MultiString = 5,
FsrmPropertyDefinitionType_Int = 6,
FsrmPropertyDefinitionType_Bool = 7,
FsrmPropertyDefinitionType_Date = 8
        

FsrmRuleType_Unknown = 0,
FsrmRuleType_Classification = 1,
FsrmRuleType_Generic = 2
        

FsrmRuleFlags_Disabled = 256,
FsrmRuleFlags_Invalid = 4096
        

FsrmClassificationLoggingFlags_None = 0,
FsrmClassificationLoggingFlags_ClassificationsInLogFile = 1,
FsrmClassificationLoggingFlags_ErrorsInLogFile = 2,
FsrmClassificationLoggingFlags_ClassificationsInSystemLog = 4,
FsrmClassificationLoggingFlags_ErrorsInSystemLog = 8
        

FsrmExecutionOption_Unknown = 0,
FsrmExecutionOption_EvaluateUnset = 1,
FsrmExecutionOption_ReEvaluate_ConsiderExistingValue = 2,
FsrmExecutionOption_ReEvaluate_IgnoreExistingValue = 3
        

FsrmStorageModuleCaps_Unknown = 0,
FsrmStorageModuleCaps_CanGet = 1,
FsrmStorageModuleCaps_CanSet = 2,
FsrmStorageModuleCaps_CanHandleDirectories = 4,
FsrmStorageModuleCaps_CanHandleFiles = 8
        

FsrmStorageModuleType_Unknown = 0,
FsrmStorageModuleType_Cache = 1,
FsrmStorageModuleType_InFile = 2,
FsrmStorageModuleType_Database = 3,
FsrmStorageModuleType_System = 100
        

FsrmPropertyFlags_Orphaned = 1,
FsrmPropertyFlags_RetrievedFromCache = 2,
FsrmPropertyFlags_RetrievedFromStorage = 4,
FsrmPropertyFlags_SetByClassifier = 8,
FsrmPropertyFlags_Deleted = 16,
FsrmPropertyFlags_Reclassified = 32,
FsrmPropertyFlags_AggregationFailed = 64,
FsrmPropertyFlags_Existing = 128,
FsrmPropertyFlags_FailedLoadingProperties = 256,
FsrmPropertyFlags_FailedClassifyingProperties = 512,
FsrmPropertyFlags_FailedSavingProperties = 1024,
FsrmPropertyFlags_Secure = 2048,
FsrmPropertyFlags_PolicyDerived = 4096,
FsrmPropertyFlags_Inherited = 8192,
FsrmPropertyFlags_Manual = 16384,
FsrmPropertyFlags_PropertySourceMask = 14
        

FsrmPipelineModuleType_Unknown = 0,
FsrmPipelineModuleType_Storage = 1,
FsrmPipelineModuleType_Classifier = 2
        

FsrmGetFilePropertyOptions_None = 0,
FsrmGetFilePropertyOptions_NoRuleEvaluation = 1,
FsrmGetFilePropertyOptions_Persistent = 2,
FsrmGetFilePropertyOptions_FailOnPersistErrors = 4,
FsrmGetFilePropertyOptions_SkipOrphaned = 8
        

FsrmFileManagementType_Unknown = 0,
FsrmFileManagementType_Expiration = 1,
FsrmFileManagementType_Custom = 2,
FsrmFileManagementType_Rms = 3
        

FsrmFileManagementLoggingFlags_None = 0,
FsrmFileManagementLoggingFlags_Error = 1,
FsrmFileManagementLoggingFlags_Information = 2,
FsrmFileManagementLoggingFlags_Audit = 4
        

FsrmPropertyConditionType_Unknown = 0,
FsrmPropertyConditionType_Equal = 1,
FsrmPropertyConditionType_NotEqual = 2,
FsrmPropertyConditionType_GreaterThan = 3,
FsrmPropertyConditionType_LessThan = 4,
FsrmPropertyConditionType_Contain = 5,
FsrmPropertyConditionType_Exist = 6,
FsrmPropertyConditionType_NotExist = 7,
FsrmPropertyConditionType_StartWith = 8,
FsrmPropertyConditionType_EndWith = 9,
FsrmPropertyConditionType_ContainedIn = 10,
FsrmPropertyConditionType_PrefixOf = 11,
FsrmPropertyConditionType_SuffixOf = 12
        
FSRM_QUOTA_THRESHOLD = LONG
#################################################################################

#CONSTANTS

#################################################################################

IFSRMOBJECT = 
IFSRMCOLLECTION = 
IFSRMMUTABLECOLLECTION = 
IFSRMCOMMITTABLECOLLECTION = 
IFSRMACTION = 
IFSRMACTIONEMAIL = 
IFSRMACTIONREPORT = 
IFSRMACTIONEVENTLOG = 
IFSRMACTIONCOMMAND = 
IFSRMSETTING = 
IFSRMPATHMAPPER = 
FSRM_DISPID_FEATURE_MASK = 0x0F000000
FSRM_DISPID_INTERFACE_A_MASK = 0x00F00000
FSRM_DISPID_INTERFACE_B_MASK = 0x000F0000
FSRM_DISPID_INTERFACE_C_MASK = 0x0000F000
FSRM_DISPID_INTERFACE_D_MASK = 0x00000F00
FSRM_DISPID_INTERFACE_MASK = FSRM_DISPID_INTERFACE_A_MASK | FSRM_DISPID_INTERFACE_B_MASK | FSRM_DISPID_INTERFACE_C_MASK | FSRM_DISPID_INTERFACE_D_MASK
FSRM_DISPID_IS_PROPERTY = 0x00000080
FSRM_DISPID_METHOD_NUM_MASK = 0x0000007F
FSRM_DISPID_METHOD_MASK = FSRM_DISPID_IS_PROPERTY | FSRM_DISPID_METHOD_NUM_MASK
FSRM_DISPID_FEATURE_GENERAL = 0x01000000
FSRM_DISPID_FEATURE_QUOTA = 0x02000000
FSRM_DISPID_FEATURE_FILESCREEN = 0x03000000
FSRM_DISPID_FEATURE_REPORTS = 0x04000000
FSRM_DISPID_FEATURE_CLASSIFICATION = 0x05000000
FSRM_DISPID_FEATURE_PIPELINE = 0x06000000
FSRM_DISPID_OBJECT = FSRM_DISPID_FEATURE_GENERAL | 0x100000
FSRM_DISPID_COLLECTION = FSRM_DISPID_FEATURE_GENERAL | 0x200000
FSRM_DISPID_COLLECTION_MUTABLE = FSRM_DISPID_COLLECTION | 0x010000
FSRM_DISPID_COLLECTION_COMMITTABLE = FSRM_DISPID_COLLECTION_MUTABLE | 0x001000
FSRM_DISPID_ACTION = FSRM_DISPID_FEATURE_GENERAL | 0x300000
FSRM_DISPID_ACTION_EMAIL = FSRM_DISPID_ACTION | 0x010000
FSRM_DISPID_ACTION_REPORT = FSRM_DISPID_ACTION | 0x020000
FSRM_DISPID_ACTION_EVENTLOG = FSRM_DISPID_ACTION | 0x030000
FSRM_DISPID_ACTION_COMMAND = FSRM_DISPID_ACTION | 0x040000
FSRM_DISPID_ACTION_EMAIL2 = FSRM_DISPID_ACTION | 0x050000
FSRM_DISPID_SETTING = FSRM_DISPID_FEATURE_GENERAL | 0x400000
FSRM_DISPID_PATHMAPPER = FSRM_DISPID_FEATURE_GENERAL | 0x500000
FSRM_DISPID_DERIVEDOBJECTSRESULT = FSRM_DISPID_FEATURE_GENERAL | 0x700000
IFSRMPROPERTYDEFINITION = 
IFSRMPROPERTYDEFINITION2 = 
IFSRMPROPERTYDEFINITIONVALUE = 
IFSRMPROPERTY = 
IFSRMRULE = 
IFSRMCLASSIFICATIONRULE = 
IFSRMPIPELINEMODULEDEFINITION = 
FSRM_DISPID_PROPERTY_DEFINITION = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x100000
FSRM_DISPID_PROPERTY_DEFINITION2 = FSRM_DISPID_PROPERTY_DEFINITION | 0x010000
FSRM_DISPID_PROPERTY = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x200000
FSRM_DISPID_RULE = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x300000
FSRM_DISPID_CLASSIFICATION_RULE = FSRM_DISPID_RULE | 0x010000
FSRM_DISPID_EXPIRATION_RULE = FSRM_DISPID_RULE | 0x020000
FSRM_DISPID_PIPELINE_MODULE_DEFINITION = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x400000
FSRM_DISPID_CLASSIFIER_MODULE_DEFINITION = FSRM_DISPID_PIPELINE_MODULE_DEFINITION | 0x010000
FSRM_DISPID_STORAGE_MODULE_DEFINITION = FSRM_DISPID_PIPELINE_MODULE_DEFINITION | 0x020000
FSRM_DISPID_CLASSIFICATION_MANAGER = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x500000
FSRM_DISPID_CLASSIFICATION_MANAGER2 = FSRM_DISPID_CLASSIFICATION_MANAGER | 0x010000
FSRM_DISPID_CLASSIFICATION_EVENTS = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x600000
FSRM_DISPID_PROPERTY_DEFINITION_VALUE = FSRM_DISPID_FEATURE_CLASSIFICATION | 0x700000
FSRM_DISPID_PROPERTY_BAG = FSRM_DISPID_FEATURE_PIPELINE | 0x600000
FSRM_DISPID_PIPELINE_MODULE_IMPLEMENTATION = FSRM_DISPID_FEATURE_PIPELINE | 0x700000
FSRM_DISPID_PIPELINE_MODULE_CONNECTOR = FSRM_DISPID_FEATURE_PIPELINE | 0x800000
FSRM_DISPID_PIPELINE_MODULE_HOST = FSRM_DISPID_FEATURE_PIPELINE | 0x900000
FSRMMAXNUMBERPROPERTYDEFINITIONS = 200
IFSRMQUOTABASE = 
IFSRMQUOTAOBJECT = 
IFSRMQUOTA = 
IFSRMAUTOAPPLYQUOTA = 
IFSRMQUOTAMANAGER = 
IFSRMQUOTATEMPLATE = 
IFSRMQUOTATEMPLATEIMPORTED = 
IFSRMQUOTATEMPLATEMANAGER = 
FSRM_DISPID_QUOTA_BASE = FSRM_DISPID_FEATURE_QUOTA | 0x100000
FSRM_DISPID_QUOTA_OBJECT = FSRM_DISPID_QUOTA_BASE | 0x010000
FSRM_DISPID_QUOTA = FSRM_DISPID_QUOTA_OBJECT | 0x001000
FSRM_DISPID_AUTOAPPLYQUOTA = FSRM_DISPID_QUOTA_OBJECT | 0x002000
FSRM_DISPID_QUOTA_TEMPLATE = FSRM_DISPID_QUOTA_BASE | 0x020000
FSRM_DISPID_QUOTA_TEMPLATE_IMPORTED = FSRM_DISPID_QUOTA_TEMPLATE | 0x001000
FSRM_DISPID_QUOTA_MANAGER = FSRM_DISPID_FEATURE_QUOTA | 0x200000
FSRM_DISPID_QUOTA_TEMPLATE_MANAGER = FSRM_DISPID_FEATURE_QUOTA | 0x300000
FSRM_DISPID_QUOTA_MANAGER_EX = FSRM_DISPID_FEATURE_QUOTA | 0x400000
FSRMMAXNUMBERTHRESHOLDS = 16
FSRMMINTHRESHOLDVALUE = 1
FSRMMAXTHRESHOLDVALUE = 250
FSRMMINQUOTALIMIT = 1024
FSRMMAXEXCLUDEFOLDERS = 32
IFSRMREPORTMANAGER = 
IFSRMREPORTJOB = 
IFSRMREPORT = 
IFSRMFILEMANAGEMENTJOBMANAGER = 
IFSRMFILEMANAGEMENTJOB = 
IFSRMPROPERTYCONDITION = 
FSRM_DISPID_REPORT_MANAGER = FSRM_DISPID_FEATURE_REPORTS | 0x100000
FSRM_DISPID_REPORT_JOB = FSRM_DISPID_FEATURE_REPORTS | 0x200000
FSRM_DISPID_REPORT = FSRM_DISPID_FEATURE_REPORTS | 0x300000
FSRM_DISPID_REPORT_SCHEDULER = FSRM_DISPID_FEATURE_REPORTS | 0x400000
FSRM_DISPID_FILE_MANAGEMENT_JOB_MANAGER = FSRM_DISPID_FEATURE_REPORTS | 0x500000
FSRM_DISPID_FILE_MANAGEMENT_JOB = FSRM_DISPID_FEATURE_REPORTS | 0x600000
FSRM_DISPID_FILE_MANAGEMENT_NOTIFICATION = FSRM_DISPID_FEATURE_REPORTS | 0x700000
FSRM_DISPID_PROPERTY_CONDITION = FSRM_DISPID_FEATURE_REPORTS | 0x800000
IFSRMFILEGROUP = 
IFSRMFILEGROUPIMPORTED = 
IFSRMFILEGROUPMANAGER = 
IFSRMFILESCREENBASE = 
IFSRMFILESCREEN = 
IFSRMFILESCREENEXCEPTION = 
IFSRMFILESCREENMANAGER = 
IFSRMFILESCREENTEMPLATE = 
IFSRMFILESCREENTEMPLATEIMPORTED = 
IFSRMFILESCREENTEMPLATEMANAGER = 
FSRM_DISPID_FILEGROUP = FSRM_DISPID_FEATURE_FILESCREEN | 0x100000
FSRM_DISPID_FILEGROUP_IMPORTED = FSRM_DISPID_FILEGROUP | 0x010000
FSRM_DISPID_FILEGROUP_MANAGER = FSRM_DISPID_FEATURE_FILESCREEN | 0x200000
FSRM_DISPID_FILESCREEN_BASE = FSRM_DISPID_FEATURE_FILESCREEN | 0x300000
FSRM_DISPID_FILESCREEN = FSRM_DISPID_FILESCREEN_BASE | 0x010000
FSRM_DISPID_FILESCREEN_TEMPLATE = FSRM_DISPID_FILESCREEN_BASE | 0x020000
FSRM_DISPID_FILESCREEN_TEMPLATE_IMPORTED = FSRM_DISPID_FILESCREEN_TEMPLATE | 0x001000
FSRM_DISPID_FILESCREEN_EXCEPTION = FSRM_DISPID_FEATURE_FILESCREEN | 0x400000
FSRM_DISPID_FILESCREEN_MANAGER = FSRM_DISPID_FEATURE_FILESCREEN | 0x500000
FSRM_DISPID_FILESCREEN_TEMPLATE_MANAGER = FSRM_DISPID_FEATURE_FILESCREEN | 0x600000
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IFsrmObject Definition

#################################################################################

MSRPC_UUID_IFSRMOBJECT = uuidtup_to_bin(('22bcef93-4a3f-4183-89f9-2f8b8a628aee','0.0'))


class Id(NDRCALL):
    opnum = 0
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('id', FSRM_OBJECT_ID),
    )
        

class Description(NDRCALL):
    opnum = 1
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('description', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 2
    structure = (
		('description', BSTR),
    )

class DescriptionResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 3
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Commit(NDRCALL):
    opnum = 4
    structure = (

    )

class CommitResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Id,IdResponse),
1 : (Description,DescriptionResponse),
2 : (Delete,DeleteResponse),
3 : (Commit,CommitResponse),
}

#################################################################################

#IFsrmCollection Definition

#################################################################################

MSRPC_UUID_IFSRMCOLLECTION = uuidtup_to_bin(('f76fbf3b-8dd-442-b05a-cb1c3ff1fee8','0.0'))


class _NewEnum(NDRCALL):
    opnum = 0
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('unknown', IUNKNOWN),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('item', VARIANT),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('count', LONG),
    )
        

class State(NDRCALL):
    opnum = 3
    structure = (

    )

class StateResponse(NDRCALL):
    structure = (
		('state', FSRMCOLLECTIONSTATE),
    )
        

class Cancel(NDRCALL):
    opnum = 4
    structure = (

    )

class CancelResponse(NDRCALL):
    structure = (

    )
        

class WaitForCompletion(NDRCALL):
    opnum = 5
    structure = (
		('waitSeconds', LONG),
    )

class WaitForCompletionResponse(NDRCALL):
    structure = (
		('completed', VARIANT_BOOL),
    )
        

class GetById(NDRCALL):
    opnum = 6
    structure = (
		('id', FSRM_OBJECT_ID),
    )

class GetByIdResponse(NDRCALL):
    structure = (
		('entry', VARIANT),
    )
        
OPNUMS = {
0 : (_NewEnum,_NewEnumResponse),
1 : (Item,ItemResponse),
2 : (Count,CountResponse),
3 : (State,StateResponse),
4 : (Cancel,CancelResponse),
5 : (WaitForCompletion,WaitForCompletionResponse),
6 : (GetById,GetByIdResponse),
}

#################################################################################

#IFsrmMutableCollection Definition

#################################################################################

MSRPC_UUID_IFSRMMUTABLECOLLECTION = uuidtup_to_bin(('1bb617b8-3886-49dc-af82-a6c90fa35dda','0.0'))


class Add(NDRCALL):
    opnum = 0
    structure = (
		('item', VARIANT),
    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 1
    structure = (
		('index', LONG),
    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class RemoveById(NDRCALL):
    opnum = 2
    structure = (
		('id', FSRM_OBJECT_ID),
    )

class RemoveByIdResponse(NDRCALL):
    structure = (

    )
        

class Clone(NDRCALL):
    opnum = 3
    structure = (

    )

class CloneResponse(NDRCALL):
    structure = (
		('collection', IFSRMMUTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (Add,AddResponse),
1 : (Remove,RemoveResponse),
2 : (RemoveById,RemoveByIdResponse),
3 : (Clone,CloneResponse),
}

#################################################################################

#IFsrmCommittableCollection Definition

#################################################################################

MSRPC_UUID_IFSRMCOMMITTABLECOLLECTION = uuidtup_to_bin(('96deb3b5-8b91-4a2a-9d93-80a35d8aa847','0.0'))


class Commit(NDRCALL):
    opnum = 0
    structure = (
		('options', FSRMCOMMITOPTIONS),
    )

class CommitResponse(NDRCALL):
    structure = (
		('results', IFSRMCOLLECTION),
    )
        
OPNUMS = {
0 : (Commit,CommitResponse),
}

#################################################################################

#IFsrmAction Definition

#################################################################################

MSRPC_UUID_IFSRMACTION = uuidtup_to_bin(('6cd6408a-ae60-463b-9ef1-e117534d69dc','0.0'))


class Id(NDRCALL):
    opnum = 0
    structure = (

    )

class IdResponse(NDRCALL):
    structure = (
		('id', FSRM_OBJECT_ID),
    )
        

class ActionType(NDRCALL):
    opnum = 1
    structure = (

    )

class ActionTypeResponse(NDRCALL):
    structure = (
		('actionType', FSRMACTIONTYPE),
    )
        

class RunLimitInterval(NDRCALL):
    opnum = 2
    structure = (

    )

class RunLimitIntervalResponse(NDRCALL):
    structure = (
		('minutes', LONG),
    )
        

class RunLimitInterval(NDRCALL):
    opnum = 3
    structure = (
		('minutes', LONG),
    )

class RunLimitIntervalResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 4
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Id,IdResponse),
1 : (ActionType,ActionTypeResponse),
2 : (RunLimitInterval,RunLimitIntervalResponse),
3 : (Delete,DeleteResponse),
}

#################################################################################

#IFsrmActionEmail Definition

#################################################################################

MSRPC_UUID_IFSRMACTIONEMAIL = uuidtup_to_bin(('d646567d-26e-4aa-984-40ad207fca','0.0'))


class MailFrom(NDRCALL):
    opnum = 0
    structure = (

    )

class MailFromResponse(NDRCALL):
    structure = (
		('mailFrom', BSTR),
    )
        

class MailFrom(NDRCALL):
    opnum = 1
    structure = (
		('mailFrom', BSTR),
    )

class MailFromResponse(NDRCALL):
    structure = (

    )
        

class MailReplyTo(NDRCALL):
    opnum = 2
    structure = (

    )

class MailReplyToResponse(NDRCALL):
    structure = (
		('mailReplyTo', BSTR),
    )
        

class MailReplyTo(NDRCALL):
    opnum = 3
    structure = (
		('mailReplyTo', BSTR),
    )

class MailReplyToResponse(NDRCALL):
    structure = (

    )
        

class MailTo(NDRCALL):
    opnum = 4
    structure = (

    )

class MailToResponse(NDRCALL):
    structure = (
		('mailTo', BSTR),
    )
        

class MailTo(NDRCALL):
    opnum = 5
    structure = (
		('mailTo', BSTR),
    )

class MailToResponse(NDRCALL):
    structure = (

    )
        

class MailCc(NDRCALL):
    opnum = 6
    structure = (

    )

class MailCcResponse(NDRCALL):
    structure = (
		('mailCc', BSTR),
    )
        

class MailCc(NDRCALL):
    opnum = 7
    structure = (
		('mailCc', BSTR),
    )

class MailCcResponse(NDRCALL):
    structure = (

    )
        

class MailBcc(NDRCALL):
    opnum = 8
    structure = (

    )

class MailBccResponse(NDRCALL):
    structure = (
		('mailBcc', BSTR),
    )
        

class MailBcc(NDRCALL):
    opnum = 9
    structure = (
		('mailBcc', BSTR),
    )

class MailBccResponse(NDRCALL):
    structure = (

    )
        

class MailSubject(NDRCALL):
    opnum = 10
    structure = (

    )

class MailSubjectResponse(NDRCALL):
    structure = (
		('mailSubject', BSTR),
    )
        

class MailSubject(NDRCALL):
    opnum = 11
    structure = (
		('mailSubject', BSTR),
    )

class MailSubjectResponse(NDRCALL):
    structure = (

    )
        

class MessageText(NDRCALL):
    opnum = 12
    structure = (

    )

class MessageTextResponse(NDRCALL):
    structure = (
		('messageText', BSTR),
    )
        

class MessageText(NDRCALL):
    opnum = 13
    structure = (
		('messageText', BSTR),
    )

class MessageTextResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (MailFrom,MailFromResponse),
1 : (MailReplyTo,MailReplyToResponse),
2 : (MailTo,MailToResponse),
3 : (MailCc,MailCcResponse),
4 : (MailBcc,MailBccResponse),
5 : (MailSubject,MailSubjectResponse),
6 : (MessageText,MessageTextResponse),
}

#################################################################################

#IFsrmActionEmail2 Definition

#################################################################################

MSRPC_UUID_IFSRMACTIONEMAIL2 = uuidtup_to_bin(('8276702f-2532-4839-89bf-4872609a2ea4','0.0'))


class AttachmentFileListSize(NDRCALL):
    opnum = 0
    structure = (

    )

class AttachmentFileListSizeResponse(NDRCALL):
    structure = (
		('attachmentFileListSize', LONG),
    )
        

class AttachmentFileListSize(NDRCALL):
    opnum = 1
    structure = (
		('attachmentFileListSize', LONG),
    )

class AttachmentFileListSizeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (AttachmentFileListSize,AttachmentFileListSizeResponse),
}

#################################################################################

#IFsrmActionReport Definition

#################################################################################

MSRPC_UUID_IFSRMACTIONREPORT = uuidtup_to_bin(('2dbe63c4-b340-48a0-a5b0-158e07fc567e','0.0'))


class ReportTypes(NDRCALL):
    opnum = 0
    structure = (

    )

class ReportTypesResponse(NDRCALL):
    structure = (
		('reportTypes', SAFEARRAY ( VARIANT )),
    )
        

class ReportTypes(NDRCALL):
    opnum = 1
    structure = (
		('reportTypes', SAFEARRAY ( VARIANT )),
    )

class ReportTypesResponse(NDRCALL):
    structure = (

    )
        

class MailTo(NDRCALL):
    opnum = 2
    structure = (

    )

class MailToResponse(NDRCALL):
    structure = (
		('mailTo', BSTR),
    )
        

class MailTo(NDRCALL):
    opnum = 3
    structure = (
		('mailTo', BSTR),
    )

class MailToResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ReportTypes,ReportTypesResponse),
1 : (MailTo,MailToResponse),
}

#################################################################################

#IFsrmActionEventLog Definition

#################################################################################

MSRPC_UUID_IFSRMACTIONEVENTLOG = uuidtup_to_bin(('4c8f96c3-5d94-4f37-a4f4-f56ab463546f','0.0'))


class EventType(NDRCALL):
    opnum = 0
    structure = (

    )

class EventTypeResponse(NDRCALL):
    structure = (
		('eventType', FSRMEVENTTYPE),
    )
        

class EventType(NDRCALL):
    opnum = 1
    structure = (
		('eventType', FSRMEVENTTYPE),
    )

class EventTypeResponse(NDRCALL):
    structure = (

    )
        

class MessageText(NDRCALL):
    opnum = 2
    structure = (

    )

class MessageTextResponse(NDRCALL):
    structure = (
		('messageText', BSTR),
    )
        

class MessageText(NDRCALL):
    opnum = 3
    structure = (
		('messageText', BSTR),
    )

class MessageTextResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (EventType,EventTypeResponse),
1 : (MessageText,MessageTextResponse),
}

#################################################################################

#IFsrmActionCommand Definition

#################################################################################

MSRPC_UUID_IFSRMACTIONCOMMAND = uuidtup_to_bin(('12937789-e247-4917-9c20-f3ee9c7ee783','0.0'))


class ExecutablePath(NDRCALL):
    opnum = 0
    structure = (

    )

class ExecutablePathResponse(NDRCALL):
    structure = (
		('executablePath', BSTR),
    )
        

class ExecutablePath(NDRCALL):
    opnum = 1
    structure = (
		('executablePath', BSTR),
    )

class ExecutablePathResponse(NDRCALL):
    structure = (

    )
        

class Arguments(NDRCALL):
    opnum = 2
    structure = (

    )

class ArgumentsResponse(NDRCALL):
    structure = (
		('arguments', BSTR),
    )
        

class Arguments(NDRCALL):
    opnum = 3
    structure = (
		('arguments', BSTR),
    )

class ArgumentsResponse(NDRCALL):
    structure = (

    )
        

class Account(NDRCALL):
    opnum = 4
    structure = (

    )

class AccountResponse(NDRCALL):
    structure = (
		('account', FSRMACCOUNTTYPE),
    )
        

class Account(NDRCALL):
    opnum = 5
    structure = (
		('account', FSRMACCOUNTTYPE),
    )

class AccountResponse(NDRCALL):
    structure = (

    )
        

class WorkingDirectory(NDRCALL):
    opnum = 6
    structure = (

    )

class WorkingDirectoryResponse(NDRCALL):
    structure = (
		('workingDirectory', BSTR),
    )
        

class WorkingDirectory(NDRCALL):
    opnum = 7
    structure = (
		('workingDirectory', BSTR),
    )

class WorkingDirectoryResponse(NDRCALL):
    structure = (

    )
        

class MonitorCommand(NDRCALL):
    opnum = 8
    structure = (

    )

class MonitorCommandResponse(NDRCALL):
    structure = (
		('monitorCommand', VARIANT_BOOL),
    )
        

class MonitorCommand(NDRCALL):
    opnum = 9
    structure = (
		('monitorCommand', VARIANT_BOOL),
    )

class MonitorCommandResponse(NDRCALL):
    structure = (

    )
        

class KillTimeOut(NDRCALL):
    opnum = 10
    structure = (

    )

class KillTimeOutResponse(NDRCALL):
    structure = (
		('minutes', LONG),
    )
        

class KillTimeOut(NDRCALL):
    opnum = 11
    structure = (
		('minutes', LONG),
    )

class KillTimeOutResponse(NDRCALL):
    structure = (

    )
        

class LogResult(NDRCALL):
    opnum = 12
    structure = (

    )

class LogResultResponse(NDRCALL):
    structure = (
		('logResults', VARIANT_BOOL),
    )
        

class LogResult(NDRCALL):
    opnum = 13
    structure = (
		('logResults', VARIANT_BOOL),
    )

class LogResultResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ExecutablePath,ExecutablePathResponse),
1 : (Arguments,ArgumentsResponse),
2 : (Account,AccountResponse),
3 : (WorkingDirectory,WorkingDirectoryResponse),
4 : (MonitorCommand,MonitorCommandResponse),
5 : (KillTimeOut,KillTimeOutResponse),
6 : (LogResult,LogResultResponse),
}

#################################################################################

#IFsrmSetting Definition

#################################################################################

MSRPC_UUID_IFSRMSETTING = uuidtup_to_bin(('f411d4fd-14e-4260-840-03795608','0.0'))


class SmtpServer(NDRCALL):
    opnum = 0
    structure = (

    )

class SmtpServerResponse(NDRCALL):
    structure = (
		('smtpServer', BSTR),
    )
        

class SmtpServer(NDRCALL):
    opnum = 1
    structure = (
		('smtpServer', BSTR),
    )

class SmtpServerResponse(NDRCALL):
    structure = (

    )
        

class MailFrom(NDRCALL):
    opnum = 2
    structure = (

    )

class MailFromResponse(NDRCALL):
    structure = (
		('mailFrom', BSTR),
    )
        

class MailFrom(NDRCALL):
    opnum = 3
    structure = (
		('mailFrom', BSTR),
    )

class MailFromResponse(NDRCALL):
    structure = (

    )
        

class AdminEmail(NDRCALL):
    opnum = 4
    structure = (

    )

class AdminEmailResponse(NDRCALL):
    structure = (
		('adminEmail', BSTR),
    )
        

class AdminEmail(NDRCALL):
    opnum = 5
    structure = (
		('adminEmail', BSTR),
    )

class AdminEmailResponse(NDRCALL):
    structure = (

    )
        

class DisableCommandLine(NDRCALL):
    opnum = 6
    structure = (

    )

class DisableCommandLineResponse(NDRCALL):
    structure = (
		('disableCommandLine', VARIANT_BOOL),
    )
        

class DisableCommandLine(NDRCALL):
    opnum = 7
    structure = (
		('disableCommandLine', VARIANT_BOOL),
    )

class DisableCommandLineResponse(NDRCALL):
    structure = (

    )
        

class EnableScreeningAudit(NDRCALL):
    opnum = 8
    structure = (

    )

class EnableScreeningAuditResponse(NDRCALL):
    structure = (
		('enableScreeningAudit', VARIANT_BOOL),
    )
        

class EnableScreeningAudit(NDRCALL):
    opnum = 9
    structure = (
		('enableScreeningAudit', VARIANT_BOOL),
    )

class EnableScreeningAuditResponse(NDRCALL):
    structure = (

    )
        

class EmailTest(NDRCALL):
    opnum = 10
    structure = (
		('mailTo', BSTR),
    )

class EmailTestResponse(NDRCALL):
    structure = (

    )
        

class SetActionRunLimitInterval(NDRCALL):
    opnum = 11
    structure = (
		('actionType', FSRMACTIONTYPE),
		('delayTimeMinutes', LONG),
    )

class SetActionRunLimitIntervalResponse(NDRCALL):
    structure = (

    )
        

class GetActionRunLimitInterval(NDRCALL):
    opnum = 12
    structure = (
		('actionType', FSRMACTIONTYPE),
    )

class GetActionRunLimitIntervalResponse(NDRCALL):
    structure = (
		('delayTimeMinutes', LONG),
    )
        
OPNUMS = {
0 : (SmtpServer,SmtpServerResponse),
1 : (MailFrom,MailFromResponse),
2 : (AdminEmail,AdminEmailResponse),
3 : (DisableCommandLine,DisableCommandLineResponse),
4 : (EnableScreeningAudit,EnableScreeningAuditResponse),
5 : (EmailTest,EmailTestResponse),
6 : (SetActionRunLimitInterval,SetActionRunLimitIntervalResponse),
7 : (GetActionRunLimitInterval,GetActionRunLimitIntervalResponse),
}

#################################################################################

#IFsrmPathMapper Definition

#################################################################################

MSRPC_UUID_IFSRMPATHMAPPER = uuidtup_to_bin(('6f4dbfff-6920-4821-a6c3-b7e94c1fd60c','0.0'))


class GetSharePathsForLocalPath(NDRCALL):
    opnum = 0
    structure = (
		('localPath', BSTR),
    )

class GetSharePathsForLocalPathResponse(NDRCALL):
    structure = (
		('sharePaths', SAFEARRAY ( VARIANT )),
    )
        
OPNUMS = {
0 : (GetSharePathsForLocalPath,GetSharePathsForLocalPathResponse),
}

#################################################################################

#IFsrmDerivedObjectsResult Definition

#################################################################################

MSRPC_UUID_IFSRMDERIVEDOBJECTSRESULT = uuidtup_to_bin(('39322a2d-38ee-4d0d-8095-421a80849a82','0.0'))


class DerivedObjects(NDRCALL):
    opnum = 0
    structure = (

    )

class DerivedObjectsResponse(NDRCALL):
    structure = (
		('derivedObjects', IFSRMCOLLECTION),
    )
        

class Results(NDRCALL):
    opnum = 1
    structure = (

    )

class ResultsResponse(NDRCALL):
    structure = (
		('results', IFSRMCOLLECTION),
    )
        
OPNUMS = {
0 : (DerivedObjects,DerivedObjectsResponse),
1 : (Results,ResultsResponse),
}

#################################################################################

#IFsrmPropertyDefinition Definition

#################################################################################

MSRPC_UUID_IFSRMPROPERTYDEFINITION = uuidtup_to_bin(('ede0150f-e9a3-419-877-01e5d24c5d3','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class Type(NDRCALL):
    opnum = 2
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('type', FSRMPROPERTYDEFINITIONTYPE),
    )
        

class Type(NDRCALL):
    opnum = 3
    structure = (
		('type', FSRMPROPERTYDEFINITIONTYPE),
    )

class TypeResponse(NDRCALL):
    structure = (

    )
        

class PossibleValues(NDRCALL):
    opnum = 4
    structure = (

    )

class PossibleValuesResponse(NDRCALL):
    structure = (
		('possibleValues', SAFEARRAY ( VARIANT )),
    )
        

class PossibleValues(NDRCALL):
    opnum = 5
    structure = (
		('possibleValues', SAFEARRAY ( VARIANT )),
    )

class PossibleValuesResponse(NDRCALL):
    structure = (

    )
        

class ValueDescriptions(NDRCALL):
    opnum = 6
    structure = (

    )

class ValueDescriptionsResponse(NDRCALL):
    structure = (
		('valueDescriptions', SAFEARRAY ( VARIANT )),
    )
        

class ValueDescriptions(NDRCALL):
    opnum = 7
    structure = (
		('valueDescriptions', SAFEARRAY ( VARIANT )),
    )

class ValueDescriptionsResponse(NDRCALL):
    structure = (

    )
        

class Parameters(NDRCALL):
    opnum = 8
    structure = (

    )

class ParametersResponse(NDRCALL):
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )
        

class Parameters(NDRCALL):
    opnum = 9
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )

class ParametersResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Type,TypeResponse),
2 : (PossibleValues,PossibleValuesResponse),
3 : (ValueDescriptions,ValueDescriptionsResponse),
4 : (Parameters,ParametersResponse),
}

#################################################################################

#IFsrmPropertyDefinition2 Definition

#################################################################################

MSRPC_UUID_IFSRMPROPERTYDEFINITION2 = uuidtup_to_bin(('47782152-d16c-4229-b4e1-0ddfe308b9f6','0.0'))


class PropertyDefinitionFlags(NDRCALL):
    opnum = 0
    structure = (

    )

class PropertyDefinitionFlagsResponse(NDRCALL):
    structure = (
		('propertyDefinitionFlags', LONG),
    )
        

class DisplayName(NDRCALL):
    opnum = 1
    structure = (

    )

class DisplayNameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class DisplayName(NDRCALL):
    opnum = 2
    structure = (
		('name', BSTR),
    )

class DisplayNameResponse(NDRCALL):
    structure = (

    )
        

class AppliesTo(NDRCALL):
    opnum = 3
    structure = (

    )

class AppliesToResponse(NDRCALL):
    structure = (
		('appliesTo', LONG),
    )
        

class ValueDefinitions(NDRCALL):
    opnum = 4
    structure = (

    )

class ValueDefinitionsResponse(NDRCALL):
    structure = (
		('valueDefinitions', IFSRMCOLLECTION),
    )
        
OPNUMS = {
0 : (PropertyDefinitionFlags,PropertyDefinitionFlagsResponse),
1 : (DisplayName,DisplayNameResponse),
2 : (AppliesTo,AppliesToResponse),
3 : (ValueDefinitions,ValueDefinitionsResponse),
}

#################################################################################

#IFsrmPropertyDefinitionValue Definition

#################################################################################

MSRPC_UUID_IFSRMPROPERTYDEFINITIONVALUE = uuidtup_to_bin(('E946D148-BD67-4178-822-144925D710','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class DisplayName(NDRCALL):
    opnum = 1
    structure = (

    )

class DisplayNameResponse(NDRCALL):
    structure = (
		('displayName', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 2
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('description', BSTR),
    )
        

class UniqueID(NDRCALL):
    opnum = 3
    structure = (

    )

class UniqueIDResponse(NDRCALL):
    structure = (
		('uniqueID', BSTR),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (DisplayName,DisplayNameResponse),
2 : (Description,DescriptionResponse),
3 : (UniqueID,UniqueIDResponse),
}

#################################################################################

#IFsrmProperty Definition

#################################################################################

MSRPC_UUID_IFSRMPROPERTY = uuidtup_to_bin(('4a73fee4-4102-4fcc-9ffb-38614f9ee768','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Value(NDRCALL):
    opnum = 1
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('value', BSTR),
    )
        

class Sources(NDRCALL):
    opnum = 2
    structure = (

    )

class SourcesResponse(NDRCALL):
    structure = (
		('sources', SAFEARRAY ( VARIANT )),
    )
        

class PropertyFlags(NDRCALL):
    opnum = 3
    structure = (

    )

class PropertyFlagsResponse(NDRCALL):
    structure = (
		('flags', LONG),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Value,ValueResponse),
2 : (Sources,SourcesResponse),
3 : (PropertyFlags,PropertyFlagsResponse),
}

#################################################################################

#IFsrmRule Definition

#################################################################################

MSRPC_UUID_IFSRMRULE = uuidtup_to_bin(('cb0df960-165-4495-9079-39360831f','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class RuleType(NDRCALL):
    opnum = 2
    structure = (

    )

class RuleTypeResponse(NDRCALL):
    structure = (
		('ruleType', FSRMRULETYPE),
    )
        

class ModuleDefinitionName(NDRCALL):
    opnum = 3
    structure = (

    )

class ModuleDefinitionNameResponse(NDRCALL):
    structure = (
		('moduleDefinitionName', BSTR),
    )
        

class ModuleDefinitionName(NDRCALL):
    opnum = 4
    structure = (
		('moduleDefinitionName', BSTR),
    )

class ModuleDefinitionNameResponse(NDRCALL):
    structure = (

    )
        

class NamespaceRoots(NDRCALL):
    opnum = 5
    structure = (

    )

class NamespaceRootsResponse(NDRCALL):
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )
        

class NamespaceRoots(NDRCALL):
    opnum = 6
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )

class NamespaceRootsResponse(NDRCALL):
    structure = (

    )
        

class RuleFlags(NDRCALL):
    opnum = 7
    structure = (

    )

class RuleFlagsResponse(NDRCALL):
    structure = (
		('ruleFlags', LONG),
    )
        

class RuleFlags(NDRCALL):
    opnum = 8
    structure = (
		('ruleFlags', LONG),
    )

class RuleFlagsResponse(NDRCALL):
    structure = (

    )
        

class Parameters(NDRCALL):
    opnum = 9
    structure = (

    )

class ParametersResponse(NDRCALL):
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )
        

class Parameters(NDRCALL):
    opnum = 10
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )

class ParametersResponse(NDRCALL):
    structure = (

    )
        

class LastModified(NDRCALL):
    opnum = 11
    structure = (

    )

class LastModifiedResponse(NDRCALL):
    structure = (
		('lastModified', DATE),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (RuleType,RuleTypeResponse),
2 : (ModuleDefinitionName,ModuleDefinitionNameResponse),
3 : (NamespaceRoots,NamespaceRootsResponse),
4 : (RuleFlags,RuleFlagsResponse),
5 : (Parameters,ParametersResponse),
6 : (LastModified,LastModifiedResponse),
}

#################################################################################

#IFsrmClassificationRule Definition

#################################################################################

MSRPC_UUID_IFSRMCLASSIFICATIONRULE = uuidtup_to_bin(('afc052c2-5315-45b-841-c6db0e120148','0.0'))


class ExecutionOption(NDRCALL):
    opnum = 0
    structure = (

    )

class ExecutionOptionResponse(NDRCALL):
    structure = (
		('executionOption', FSRMEXECUTIONOPTION),
    )
        

class ExecutionOption(NDRCALL):
    opnum = 1
    structure = (
		('executionOption', FSRMEXECUTIONOPTION),
    )

class ExecutionOptionResponse(NDRCALL):
    structure = (

    )
        

class PropertyAffected(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertyAffectedResponse(NDRCALL):
    structure = (
		('property', BSTR),
    )
        

class PropertyAffected(NDRCALL):
    opnum = 3
    structure = (
		('property', BSTR),
    )

class PropertyAffectedResponse(NDRCALL):
    structure = (

    )
        

class Value(NDRCALL):
    opnum = 4
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('value', BSTR),
    )
        

class Value(NDRCALL):
    opnum = 5
    structure = (
		('value', BSTR),
    )

class ValueResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ExecutionOption,ExecutionOptionResponse),
1 : (PropertyAffected,PropertyAffectedResponse),
2 : (Value,ValueResponse),
}

#################################################################################

#IFsrmPipelineModuleDefinition Definition

#################################################################################

MSRPC_UUID_IFSRMPIPELINEMODULEDEFINITION = uuidtup_to_bin(('515c1277-2c81-440e-8fcf-367921ed4f59','0.0'))


class ModuleClsid(NDRCALL):
    opnum = 0
    structure = (

    )

class ModuleClsidResponse(NDRCALL):
    structure = (
		('moduleClsid', BSTR),
    )
        

class ModuleClsid(NDRCALL):
    opnum = 1
    structure = (
		('moduleClsid', BSTR),
    )

class ModuleClsidResponse(NDRCALL):
    structure = (

    )
        

class Name(NDRCALL):
    opnum = 2
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 3
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class Company(NDRCALL):
    opnum = 4
    structure = (

    )

class CompanyResponse(NDRCALL):
    structure = (
		('company', BSTR),
    )
        

class Company(NDRCALL):
    opnum = 5
    structure = (
		('company', BSTR),
    )

class CompanyResponse(NDRCALL):
    structure = (

    )
        

class Version(NDRCALL):
    opnum = 6
    structure = (

    )

class VersionResponse(NDRCALL):
    structure = (
		('version', BSTR),
    )
        

class Version(NDRCALL):
    opnum = 7
    structure = (
		('version', BSTR),
    )

class VersionResponse(NDRCALL):
    structure = (

    )
        

class ModuleType(NDRCALL):
    opnum = 8
    structure = (

    )

class ModuleTypeResponse(NDRCALL):
    structure = (
		('moduleType', FSRMPIPELINEMODULETYPE),
    )
        

class Enabled(NDRCALL):
    opnum = 9
    structure = (

    )

class EnabledResponse(NDRCALL):
    structure = (
		('enabled', VARIANT_BOOL),
    )
        

class Enabled(NDRCALL):
    opnum = 10
    structure = (
		('enabled', VARIANT_BOOL),
    )

class EnabledResponse(NDRCALL):
    structure = (

    )
        

class NeedsFileContent(NDRCALL):
    opnum = 11
    structure = (

    )

class NeedsFileContentResponse(NDRCALL):
    structure = (
		('needsFileContent', VARIANT_BOOL),
    )
        

class NeedsFileContent(NDRCALL):
    opnum = 12
    structure = (
		('needsFileContent', VARIANT_BOOL),
    )

class NeedsFileContentResponse(NDRCALL):
    structure = (

    )
        

class Account(NDRCALL):
    opnum = 13
    structure = (

    )

class AccountResponse(NDRCALL):
    structure = (
		('retrievalAccount', FSRMACCOUNTTYPE),
    )
        

class Account(NDRCALL):
    opnum = 14
    structure = (
		('retrievalAccount', FSRMACCOUNTTYPE),
    )

class AccountResponse(NDRCALL):
    structure = (

    )
        

class SupportedExtensions(NDRCALL):
    opnum = 15
    structure = (

    )

class SupportedExtensionsResponse(NDRCALL):
    structure = (
		('supportedExtensions', SAFEARRAY ( VARIANT )),
    )
        

class SupportedExtensions(NDRCALL):
    opnum = 16
    structure = (
		('supportedExtensions', SAFEARRAY ( VARIANT )),
    )

class SupportedExtensionsResponse(NDRCALL):
    structure = (

    )
        

class Parameters(NDRCALL):
    opnum = 17
    structure = (

    )

class ParametersResponse(NDRCALL):
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )
        

class Parameters(NDRCALL):
    opnum = 18
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )

class ParametersResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ModuleClsid,ModuleClsidResponse),
1 : (Name,NameResponse),
2 : (Company,CompanyResponse),
3 : (Version,VersionResponse),
4 : (ModuleType,ModuleTypeResponse),
5 : (Enabled,EnabledResponse),
6 : (NeedsFileContent,NeedsFileContentResponse),
7 : (Account,AccountResponse),
8 : (SupportedExtensions,SupportedExtensionsResponse),
9 : (Parameters,ParametersResponse),
}

#################################################################################

#IFsrmClassifierModuleDefinition Definition

#################################################################################

MSRPC_UUID_IFSRMCLASSIFIERMODULEDEFINITION = uuidtup_to_bin(('bb36ea26-6318-48-8592-f72dd602e7a5','0.0'))


class PropertiesAffected(NDRCALL):
    opnum = 0
    structure = (

    )

class PropertiesAffectedResponse(NDRCALL):
    structure = (
		('propertiesAffected', SAFEARRAY ( VARIANT )),
    )
        

class PropertiesAffected(NDRCALL):
    opnum = 1
    structure = (
		('propertiesAffected', SAFEARRAY ( VARIANT )),
    )

class PropertiesAffectedResponse(NDRCALL):
    structure = (

    )
        

class PropertiesUsed(NDRCALL):
    opnum = 2
    structure = (

    )

class PropertiesUsedResponse(NDRCALL):
    structure = (
		('propertiesUsed', SAFEARRAY ( VARIANT )),
    )
        

class PropertiesUsed(NDRCALL):
    opnum = 3
    structure = (
		('propertiesUsed', SAFEARRAY ( VARIANT )),
    )

class PropertiesUsedResponse(NDRCALL):
    structure = (

    )
        

class NeedsExplicitValue(NDRCALL):
    opnum = 4
    structure = (

    )

class NeedsExplicitValueResponse(NDRCALL):
    structure = (
		('needsExplicitValue', VARIANT_BOOL),
    )
        

class NeedsExplicitValue(NDRCALL):
    opnum = 5
    structure = (
		('needsExplicitValue', VARIANT_BOOL),
    )

class NeedsExplicitValueResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (PropertiesAffected,PropertiesAffectedResponse),
1 : (PropertiesUsed,PropertiesUsedResponse),
2 : (NeedsExplicitValue,NeedsExplicitValueResponse),
}

#################################################################################

#IFsrmClassificationManager Definition

#################################################################################

MSRPC_UUID_IFSRMCLASSIFICATIONMANAGER = uuidtup_to_bin(('d2dc89da-ee91-480-858-cc72a56f7d04','0.0'))


class ClassificationReportFormats(NDRCALL):
    opnum = 0
    structure = (

    )

class ClassificationReportFormatsResponse(NDRCALL):
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )
        

class ClassificationReportFormats(NDRCALL):
    opnum = 1
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )

class ClassificationReportFormatsResponse(NDRCALL):
    structure = (

    )
        

class Logging(NDRCALL):
    opnum = 2
    structure = (

    )

class LoggingResponse(NDRCALL):
    structure = (
		('logging', LONG),
    )
        

class Logging(NDRCALL):
    opnum = 3
    structure = (
		('logging', LONG),
    )

class LoggingResponse(NDRCALL):
    structure = (

    )
        

class ClassificationReportMailTo(NDRCALL):
    opnum = 4
    structure = (

    )

class ClassificationReportMailToResponse(NDRCALL):
    structure = (
		('mailTo', BSTR),
    )
        

class ClassificationReportMailTo(NDRCALL):
    opnum = 5
    structure = (
		('mailTo', BSTR),
    )

class ClassificationReportMailToResponse(NDRCALL):
    structure = (

    )
        

class ClassificationReportEnabled(NDRCALL):
    opnum = 6
    structure = (

    )

class ClassificationReportEnabledResponse(NDRCALL):
    structure = (
		('reportEnabled', VARIANT_BOOL),
    )
        

class ClassificationReportEnabled(NDRCALL):
    opnum = 7
    structure = (
		('reportEnabled', VARIANT_BOOL),
    )

class ClassificationReportEnabledResponse(NDRCALL):
    structure = (

    )
        

class ClassificationLastReportPathWithoutExtension(NDRCALL):
    opnum = 8
    structure = (

    )

class ClassificationLastReportPathWithoutExtensionResponse(NDRCALL):
    structure = (
		('lastReportPath', BSTR),
    )
        

class ClassificationLastError(NDRCALL):
    opnum = 9
    structure = (

    )

class ClassificationLastErrorResponse(NDRCALL):
    structure = (
		('lastError', BSTR),
    )
        

class ClassificationRunningStatus(NDRCALL):
    opnum = 10
    structure = (

    )

class ClassificationRunningStatusResponse(NDRCALL):
    structure = (
		('runningStatus', FSRMREPORTRUNNINGSTATUS),
    )
        

class EnumPropertyDefinitions(NDRCALL):
    opnum = 11
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumPropertyDefinitionsResponse(NDRCALL):
    structure = (
		('propertyDefinitions', IFSRMCOLLECTION),
    )
        

class CreatePropertyDefinition(NDRCALL):
    opnum = 12
    structure = (

    )

class CreatePropertyDefinitionResponse(NDRCALL):
    structure = (
		('propertyDefinition', IFSRMPROPERTYDEFINITION),
    )
        

class GetPropertyDefinition(NDRCALL):
    opnum = 13
    structure = (
		('propertyName', BSTR),
    )

class GetPropertyDefinitionResponse(NDRCALL):
    structure = (
		('propertyDefinition', IFSRMPROPERTYDEFINITION),
    )
        

class EnumRules(NDRCALL):
    opnum = 14
    structure = (
		('ruleType', FSRMRULETYPE),
		('options', FSRMENUMOPTIONS),
    )

class EnumRulesResponse(NDRCALL):
    structure = (
		('Rules', IFSRMCOLLECTION),
    )
        

class CreateRule(NDRCALL):
    opnum = 15
    structure = (
		('ruleType', FSRMRULETYPE),
    )

class CreateRuleResponse(NDRCALL):
    structure = (
		('Rule', IFSRMRULE),
    )
        

class GetRule(NDRCALL):
    opnum = 16
    structure = (
		('ruleName', BSTR),
		('ruleType', FSRMRULETYPE),
    )

class GetRuleResponse(NDRCALL):
    structure = (
		('Rule', IFSRMRULE),
    )
        

class EnumModuleDefinitions(NDRCALL):
    opnum = 17
    structure = (
		('moduleType', FSRMPIPELINEMODULETYPE),
		('options', FSRMENUMOPTIONS),
    )

class EnumModuleDefinitionsResponse(NDRCALL):
    structure = (
		('moduleDefinitions', IFSRMCOLLECTION),
    )
        

class CreateModuleDefinition(NDRCALL):
    opnum = 18
    structure = (
		('moduleType', FSRMPIPELINEMODULETYPE),
    )

class CreateModuleDefinitionResponse(NDRCALL):
    structure = (
		('moduleDefinition', IFSRMPIPELINEMODULEDEFINITION),
    )
        

class GetModuleDefinition(NDRCALL):
    opnum = 19
    structure = (
		('moduleName', BSTR),
		('moduleType', FSRMPIPELINEMODULETYPE),
    )

class GetModuleDefinitionResponse(NDRCALL):
    structure = (
		('moduleDefinition', IFSRMPIPELINEMODULEDEFINITION),
    )
        

class RunClassification(NDRCALL):
    opnum = 20
    structure = (
		('context', FSRMREPORTGENERATIONCONTEXT),
		('reserved', BSTR),
    )

class RunClassificationResponse(NDRCALL):
    structure = (

    )
        

class WaitForClassificationCompletion(NDRCALL):
    opnum = 21
    structure = (
		('waitSeconds', LONG),
    )

class WaitForClassificationCompletionResponse(NDRCALL):
    structure = (
		('completed', VARIANT_BOOL),
    )
        

class CancelClassification(NDRCALL):
    opnum = 22
    structure = (

    )

class CancelClassificationResponse(NDRCALL):
    structure = (

    )
        

class EnumFileProperties(NDRCALL):
    opnum = 23
    structure = (
		('filePath', BSTR),
		('options', FSRMGETFILEPROPERTYOPTIONS),
    )

class EnumFilePropertiesResponse(NDRCALL):
    structure = (
		('fileProperties', IFSRMCOLLECTION),
    )
        

class GetFileProperty(NDRCALL):
    opnum = 24
    structure = (
		('filePath', BSTR),
		('propertyName', BSTR),
		('options', FSRMGETFILEPROPERTYOPTIONS),
    )

class GetFilePropertyResponse(NDRCALL):
    structure = (
		('property', IFSRMPROPERTY),
    )
        

class SetFileProperty(NDRCALL):
    opnum = 25
    structure = (
		('filePath', BSTR),
		('propertyName', BSTR),
		('propertyValue', BSTR),
    )

class SetFilePropertyResponse(NDRCALL):
    structure = (

    )
        

class ClearFileProperty(NDRCALL):
    opnum = 26
    structure = (
		('filePath', BSTR),
		('property', BSTR),
    )

class ClearFilePropertyResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ClassificationReportFormats,ClassificationReportFormatsResponse),
1 : (Logging,LoggingResponse),
2 : (ClassificationReportMailTo,ClassificationReportMailToResponse),
3 : (ClassificationReportEnabled,ClassificationReportEnabledResponse),
4 : (ClassificationLastReportPathWithoutExtension,ClassificationLastReportPathWithoutExtensionResponse),
5 : (ClassificationLastError,ClassificationLastErrorResponse),
6 : (ClassificationRunningStatus,ClassificationRunningStatusResponse),
7 : (EnumPropertyDefinitions,EnumPropertyDefinitionsResponse),
8 : (CreatePropertyDefinition,CreatePropertyDefinitionResponse),
9 : (GetPropertyDefinition,GetPropertyDefinitionResponse),
10 : (EnumRules,EnumRulesResponse),
11 : (CreateRule,CreateRuleResponse),
12 : (GetRule,GetRuleResponse),
13 : (EnumModuleDefinitions,EnumModuleDefinitionsResponse),
14 : (CreateModuleDefinition,CreateModuleDefinitionResponse),
15 : (GetModuleDefinition,GetModuleDefinitionResponse),
16 : (RunClassification,RunClassificationResponse),
17 : (WaitForClassificationCompletion,WaitForClassificationCompletionResponse),
18 : (CancelClassification,CancelClassificationResponse),
19 : (EnumFileProperties,EnumFilePropertiesResponse),
20 : (GetFileProperty,GetFilePropertyResponse),
21 : (SetFileProperty,SetFilePropertyResponse),
22 : (ClearFileProperty,ClearFilePropertyResponse),
}

#################################################################################

#IFsrmStorageModuleDefinition Definition

#################################################################################

MSRPC_UUID_IFSRMSTORAGEMODULEDEFINITION = uuidtup_to_bin(('15a81350-497d-4aba-80e9-d4dbcc5521fe','0.0'))


class Capabilities(NDRCALL):
    opnum = 0
    structure = (

    )

class CapabilitiesResponse(NDRCALL):
    structure = (
		('capabilities', FSRMSTORAGEMODULECAPS),
    )
        

class Capabilities(NDRCALL):
    opnum = 1
    structure = (
		('capabilities', FSRMSTORAGEMODULECAPS),
    )

class CapabilitiesResponse(NDRCALL):
    structure = (

    )
        

class StorageType(NDRCALL):
    opnum = 2
    structure = (

    )

class StorageTypeResponse(NDRCALL):
    structure = (
		('storageType', FSRMSTORAGEMODULETYPE),
    )
        

class StorageType(NDRCALL):
    opnum = 3
    structure = (
		('storageType', FSRMSTORAGEMODULETYPE),
    )

class StorageTypeResponse(NDRCALL):
    structure = (

    )
        

class UpdatesFileContent(NDRCALL):
    opnum = 4
    structure = (

    )

class UpdatesFileContentResponse(NDRCALL):
    structure = (
		('updatesFileContent', VARIANT_BOOL),
    )
        

class UpdatesFileContent(NDRCALL):
    opnum = 5
    structure = (
		('updatesFileContent', VARIANT_BOOL),
    )

class UpdatesFileContentResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Capabilities,CapabilitiesResponse),
1 : (StorageType,StorageTypeResponse),
2 : (UpdatesFileContent,UpdatesFileContentResponse),
}

#################################################################################

#IFsrmQuotaBase Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTABASE = uuidtup_to_bin(('1568a795-3924-4118-b74b-68d8f0fa5daf','0.0'))


class QuotaLimit(NDRCALL):
    opnum = 0
    structure = (

    )

class QuotaLimitResponse(NDRCALL):
    structure = (
		('quotaLimit', VARIANT),
    )
        

class QuotaLimit(NDRCALL):
    opnum = 1
    structure = (
		('quotaLimit', VARIANT),
    )

class QuotaLimitResponse(NDRCALL):
    structure = (

    )
        

class QuotaFlags(NDRCALL):
    opnum = 2
    structure = (

    )

class QuotaFlagsResponse(NDRCALL):
    structure = (
		('quotaFlags', LONG),
    )
        

class QuotaFlags(NDRCALL):
    opnum = 3
    structure = (
		('quotaFlags', LONG),
    )

class QuotaFlagsResponse(NDRCALL):
    structure = (

    )
        

class Thresholds(NDRCALL):
    opnum = 4
    structure = (

    )

class ThresholdsResponse(NDRCALL):
    structure = (
		('thresholds', SAFEARRAY ( VARIANT )),
    )
        

class AddThreshold(NDRCALL):
    opnum = 5
    structure = (
		('threshold', FSRM_QUOTA_THRESHOLD),
    )

class AddThresholdResponse(NDRCALL):
    structure = (

    )
        

class DeleteThreshold(NDRCALL):
    opnum = 6
    structure = (
		('threshold', FSRM_QUOTA_THRESHOLD),
    )

class DeleteThresholdResponse(NDRCALL):
    structure = (

    )
        

class ModifyThreshold(NDRCALL):
    opnum = 7
    structure = (
		('threshold', FSRM_QUOTA_THRESHOLD),
		('newThreshold', FSRM_QUOTA_THRESHOLD),
    )

class ModifyThresholdResponse(NDRCALL):
    structure = (

    )
        

class CreateThresholdAction(NDRCALL):
    opnum = 8
    structure = (
		('threshold', FSRM_QUOTA_THRESHOLD),
		('actionType', FSRMACTIONTYPE),
    )

class CreateThresholdActionResponse(NDRCALL):
    structure = (
		('action', IFSRMACTION),
    )
        

class EnumThresholdActions(NDRCALL):
    opnum = 9
    structure = (
		('threshold', FSRM_QUOTA_THRESHOLD),
    )

class EnumThresholdActionsResponse(NDRCALL):
    structure = (
		('actions', IFSRMCOLLECTION),
    )
        
OPNUMS = {
0 : (QuotaLimit,QuotaLimitResponse),
1 : (QuotaFlags,QuotaFlagsResponse),
2 : (Thresholds,ThresholdsResponse),
3 : (AddThreshold,AddThresholdResponse),
4 : (DeleteThreshold,DeleteThresholdResponse),
5 : (ModifyThreshold,ModifyThresholdResponse),
6 : (CreateThresholdAction,CreateThresholdActionResponse),
7 : (EnumThresholdActions,EnumThresholdActionsResponse),
}

#################################################################################

#IFsrmQuotaObject Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTAOBJECT = uuidtup_to_bin(('42dc3511-61d5-48ae-b6dc-59fc00c0a8d6','0.0'))


class Path(NDRCALL):
    opnum = 0
    structure = (

    )

class PathResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class UserSid(NDRCALL):
    opnum = 1
    structure = (

    )

class UserSidResponse(NDRCALL):
    structure = (
		('userSid', BSTR),
    )
        

class UserAccount(NDRCALL):
    opnum = 2
    structure = (

    )

class UserAccountResponse(NDRCALL):
    structure = (
		('userAccount', BSTR),
    )
        

class SourceTemplateName(NDRCALL):
    opnum = 3
    structure = (

    )

class SourceTemplateNameResponse(NDRCALL):
    structure = (
		('quotaTemplateName', BSTR),
    )
        

class MatchesSourceTemplate(NDRCALL):
    opnum = 4
    structure = (

    )

class MatchesSourceTemplateResponse(NDRCALL):
    structure = (
		('matches', VARIANT_BOOL),
    )
        

class ApplyTemplate(NDRCALL):
    opnum = 5
    structure = (
		('quotaTemplateName', BSTR),
    )

class ApplyTemplateResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Path,PathResponse),
1 : (UserSid,UserSidResponse),
2 : (UserAccount,UserAccountResponse),
3 : (SourceTemplateName,SourceTemplateNameResponse),
4 : (MatchesSourceTemplate,MatchesSourceTemplateResponse),
5 : (ApplyTemplate,ApplyTemplateResponse),
}

#################################################################################

#IFsrmQuota Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTA = uuidtup_to_bin(('377f739d-9647-4b8e-97d2-5ffce6d759cd','0.0'))


class QuotaUsed(NDRCALL):
    opnum = 0
    structure = (

    )

class QuotaUsedResponse(NDRCALL):
    structure = (
		('used', VARIANT),
    )
        

class QuotaPeakUsage(NDRCALL):
    opnum = 1
    structure = (

    )

class QuotaPeakUsageResponse(NDRCALL):
    structure = (
		('peakUsage', VARIANT),
    )
        

class QuotaPeakUsageTime(NDRCALL):
    opnum = 2
    structure = (

    )

class QuotaPeakUsageTimeResponse(NDRCALL):
    structure = (
		('peakUsageDateTime', DATE),
    )
        

class ResetPeakUsage(NDRCALL):
    opnum = 3
    structure = (

    )

class ResetPeakUsageResponse(NDRCALL):
    structure = (

    )
        

class RefreshUsageProperties(NDRCALL):
    opnum = 4
    structure = (

    )

class RefreshUsagePropertiesResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (QuotaUsed,QuotaUsedResponse),
1 : (QuotaPeakUsage,QuotaPeakUsageResponse),
2 : (QuotaPeakUsageTime,QuotaPeakUsageTimeResponse),
3 : (ResetPeakUsage,ResetPeakUsageResponse),
4 : (RefreshUsageProperties,RefreshUsagePropertiesResponse),
}

#################################################################################

#IFsrmAutoApplyQuota Definition

#################################################################################

MSRPC_UUID_IFSRMAUTOAPPLYQUOTA = uuidtup_to_bin(('f82e5729-6ba-4740-bfc7-c7f58f75fb7b','0.0'))


class ExcludeFolders(NDRCALL):
    opnum = 0
    structure = (

    )

class ExcludeFoldersResponse(NDRCALL):
    structure = (
		('folders', SAFEARRAY ( VARIANT )),
    )
        

class ExcludeFolders(NDRCALL):
    opnum = 1
    structure = (
		('folders', SAFEARRAY ( VARIANT )),
    )

class ExcludeFoldersResponse(NDRCALL):
    structure = (

    )
        

class CommitAndUpdateDerived(NDRCALL):
    opnum = 2
    structure = (
		('commitOptions', FSRMCOMMITOPTIONS),
		('applyOptions', FSRMTEMPLATEAPPLYOPTIONS),
    )

class CommitAndUpdateDerivedResponse(NDRCALL):
    structure = (
		('derivedObjectsResult', IFSRMDERIVEDOBJECTSRESULT),
    )
        
OPNUMS = {
0 : (ExcludeFolders,ExcludeFoldersResponse),
1 : (CommitAndUpdateDerived,CommitAndUpdateDerivedResponse),
}

#################################################################################

#IFsrmQuotaManager Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTAMANAGER = uuidtup_to_bin(('8bb68c7d-19d8-4ffb-809e-be4fc1734014','0.0'))


class ActionVariables(NDRCALL):
    opnum = 0
    structure = (

    )

class ActionVariablesResponse(NDRCALL):
    structure = (
		('variables', SAFEARRAY ( VARIANT )),
    )
        

class ActionVariableDescriptions(NDRCALL):
    opnum = 1
    structure = (

    )

class ActionVariableDescriptionsResponse(NDRCALL):
    structure = (
		('descriptions', SAFEARRAY ( VARIANT )),
    )
        

class CreateQuota(NDRCALL):
    opnum = 2
    structure = (
		('path', BSTR),
    )

class CreateQuotaResponse(NDRCALL):
    structure = (
		('quota', IFSRMQUOTA),
    )
        

class CreateAutoApplyQuota(NDRCALL):
    opnum = 3
    structure = (
		('quotaTemplateName', BSTR),
		('path', BSTR),
    )

class CreateAutoApplyQuotaResponse(NDRCALL):
    structure = (
		('quota', IFSRMAUTOAPPLYQUOTA),
    )
        

class GetQuota(NDRCALL):
    opnum = 4
    structure = (
		('path', BSTR),
    )

class GetQuotaResponse(NDRCALL):
    structure = (
		('quota', IFSRMQUOTA),
    )
        

class GetAutoApplyQuota(NDRCALL):
    opnum = 5
    structure = (
		('path', BSTR),
    )

class GetAutoApplyQuotaResponse(NDRCALL):
    structure = (
		('quota', IFSRMAUTOAPPLYQUOTA),
    )
        

class GetRestrictiveQuota(NDRCALL):
    opnum = 6
    structure = (
		('path', BSTR),
    )

class GetRestrictiveQuotaResponse(NDRCALL):
    structure = (
		('quota', IFSRMQUOTA),
    )
        

class EnumQuotas(NDRCALL):
    opnum = 7
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class EnumQuotasResponse(NDRCALL):
    structure = (
		('quotas', IFSRMCOMMITTABLECOLLECTION),
    )
        

class EnumAutoApplyQuotas(NDRCALL):
    opnum = 8
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class EnumAutoApplyQuotasResponse(NDRCALL):
    structure = (
		('quotas', IFSRMCOMMITTABLECOLLECTION),
    )
        

class EnumEffectiveQuotas(NDRCALL):
    opnum = 9
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class EnumEffectiveQuotasResponse(NDRCALL):
    structure = (
		('quotas', IFSRMCOMMITTABLECOLLECTION),
    )
        

class Scan(NDRCALL):
    opnum = 10
    structure = (
		('strPath', BSTR),
    )

class ScanResponse(NDRCALL):
    structure = (

    )
        

class CreateQuotaCollection(NDRCALL):
    opnum = 11
    structure = (

    )

class CreateQuotaCollectionResponse(NDRCALL):
    structure = (
		('collection', IFSRMCOMMITTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (ActionVariables,ActionVariablesResponse),
1 : (ActionVariableDescriptions,ActionVariableDescriptionsResponse),
2 : (CreateQuota,CreateQuotaResponse),
3 : (CreateAutoApplyQuota,CreateAutoApplyQuotaResponse),
4 : (GetQuota,GetQuotaResponse),
5 : (GetAutoApplyQuota,GetAutoApplyQuotaResponse),
6 : (GetRestrictiveQuota,GetRestrictiveQuotaResponse),
7 : (EnumQuotas,EnumQuotasResponse),
8 : (EnumAutoApplyQuotas,EnumAutoApplyQuotasResponse),
9 : (EnumEffectiveQuotas,EnumEffectiveQuotasResponse),
10 : (Scan,ScanResponse),
11 : (CreateQuotaCollection,CreateQuotaCollectionResponse),
}

#################################################################################

#IFsrmQuotaManagerEx Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTAMANAGEREX = uuidtup_to_bin(('4846cb01-d430-494f-abb4-b1054999fb09','0.0'))


class IsAffectedByQuota(NDRCALL):
    opnum = 0
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class IsAffectedByQuotaResponse(NDRCALL):
    structure = (
		('affected', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (IsAffectedByQuota,IsAffectedByQuotaResponse),
}

#################################################################################

#IFsrmQuotaTemplate Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTATEMPLATE = uuidtup_to_bin(('a2efab31-295-46b-b976-e86d58b52e8b','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class CopyTemplate(NDRCALL):
    opnum = 2
    structure = (
		('quotaTemplateName', BSTR),
    )

class CopyTemplateResponse(NDRCALL):
    structure = (

    )
        

class CommitAndUpdateDerived(NDRCALL):
    opnum = 3
    structure = (
		('commitOptions', FSRMCOMMITOPTIONS),
		('applyOptions', FSRMTEMPLATEAPPLYOPTIONS),
    )

class CommitAndUpdateDerivedResponse(NDRCALL):
    structure = (
		('derivedObjectsResult', IFSRMDERIVEDOBJECTSRESULT),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (CopyTemplate,CopyTemplateResponse),
2 : (CommitAndUpdateDerived,CommitAndUpdateDerivedResponse),
}

#################################################################################

#IFsrmQuotaTemplateImported Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTATEMPLATEIMPORTED = uuidtup_to_bin(('9a2bf113-a329-44cc-809a-5c00fce8da40','0.0'))


class OverwriteOnCommit(NDRCALL):
    opnum = 0
    structure = (

    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (
		('overwrite', VARIANT_BOOL),
    )
        

class OverwriteOnCommit(NDRCALL):
    opnum = 1
    structure = (
		('overwrite', VARIANT_BOOL),
    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OverwriteOnCommit,OverwriteOnCommitResponse),
}

#################################################################################

#IFsrmQuotaTemplateManager Definition

#################################################################################

MSRPC_UUID_IFSRMQUOTATEMPLATEMANAGER = uuidtup_to_bin(('4173ac41-172d-4d52-963c-fdc7e415f717','0.0'))


class CreateTemplate(NDRCALL):
    opnum = 0
    structure = (

    )

class CreateTemplateResponse(NDRCALL):
    structure = (
		('quotaTemplate', IFSRMQUOTATEMPLATE),
    )
        

class GetTemplate(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class GetTemplateResponse(NDRCALL):
    structure = (
		('quotaTemplate', IFSRMQUOTATEMPLATE),
    )
        

class EnumTemplates(NDRCALL):
    opnum = 2
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumTemplatesResponse(NDRCALL):
    structure = (
		('quotaTemplates', IFSRMCOMMITTABLECOLLECTION),
    )
        

class ExportTemplates(NDRCALL):
    opnum = 3
    structure = (
		('quotaTemplateNamesArray', VARIANT),
    )

class ExportTemplatesResponse(NDRCALL):
    structure = (
		('serializedQuotaTemplates', BSTR),
    )
        

class ImportTemplates(NDRCALL):
    opnum = 4
    structure = (
		('serializedQuotaTemplates', BSTR),
		('quotaTemplateNamesArray', VARIANT),
    )

class ImportTemplatesResponse(NDRCALL):
    structure = (
		('quotaTemplates', IFSRMCOMMITTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (CreateTemplate,CreateTemplateResponse),
1 : (GetTemplate,GetTemplateResponse),
2 : (EnumTemplates,EnumTemplatesResponse),
3 : (ExportTemplates,ExportTemplatesResponse),
4 : (ImportTemplates,ImportTemplatesResponse),
}

#################################################################################

#IFsrmReportManager Definition

#################################################################################

MSRPC_UUID_IFSRMREPORTMANAGER = uuidtup_to_bin(('27b899fe-6ffa-4481-a184-d3daade8a02b','0.0'))


class EnumReportJobs(NDRCALL):
    opnum = 0
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumReportJobsResponse(NDRCALL):
    structure = (
		('reportJobs', IFSRMCOLLECTION),
    )
        

class CreateReportJob(NDRCALL):
    opnum = 1
    structure = (

    )

class CreateReportJobResponse(NDRCALL):
    structure = (
		('reportJob', IFSRMREPORTJOB),
    )
        

class GetReportJob(NDRCALL):
    opnum = 2
    structure = (
		('taskName', BSTR),
    )

class GetReportJobResponse(NDRCALL):
    structure = (
		('reportJob', IFSRMREPORTJOB),
    )
        

class GetOutputDirectory(NDRCALL):
    opnum = 3
    structure = (
		('context', FSRMREPORTGENERATIONCONTEXT),
    )

class GetOutputDirectoryResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class SetOutputDirectory(NDRCALL):
    opnum = 4
    structure = (
		('context', FSRMREPORTGENERATIONCONTEXT),
		('path', BSTR),
    )

class SetOutputDirectoryResponse(NDRCALL):
    structure = (

    )
        

class IsFilterValidForReportType(NDRCALL):
    opnum = 5
    structure = (
		('reportType', FSRMREPORTTYPE),
		('filter', FSRMREPORTFILTER),
    )

class IsFilterValidForReportTypeResponse(NDRCALL):
    structure = (
		('valid', VARIANT_BOOL),
    )
        

class GetDefaultFilter(NDRCALL):
    opnum = 6
    structure = (
		('reportType', FSRMREPORTTYPE),
		('filter', FSRMREPORTFILTER),
    )

class GetDefaultFilterResponse(NDRCALL):
    structure = (
		('filterValue', VARIANT),
    )
        

class SetDefaultFilter(NDRCALL):
    opnum = 7
    structure = (
		('reportType', FSRMREPORTTYPE),
		('filter', FSRMREPORTFILTER),
		('filterValue', VARIANT),
    )

class SetDefaultFilterResponse(NDRCALL):
    structure = (

    )
        

class GetReportSizeLimit(NDRCALL):
    opnum = 8
    structure = (
		('limit', FSRMREPORTLIMIT),
    )

class GetReportSizeLimitResponse(NDRCALL):
    structure = (
		('limitValue', VARIANT),
    )
        

class SetReportSizeLimit(NDRCALL):
    opnum = 9
    structure = (
		('limit', FSRMREPORTLIMIT),
		('limitValue', VARIANT),
    )

class SetReportSizeLimitResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (EnumReportJobs,EnumReportJobsResponse),
1 : (CreateReportJob,CreateReportJobResponse),
2 : (GetReportJob,GetReportJobResponse),
3 : (GetOutputDirectory,GetOutputDirectoryResponse),
4 : (SetOutputDirectory,SetOutputDirectoryResponse),
5 : (IsFilterValidForReportType,IsFilterValidForReportTypeResponse),
6 : (GetDefaultFilter,GetDefaultFilterResponse),
7 : (SetDefaultFilter,SetDefaultFilterResponse),
8 : (GetReportSizeLimit,GetReportSizeLimitResponse),
9 : (SetReportSizeLimit,SetReportSizeLimitResponse),
}

#################################################################################

#IFsrmReportJob Definition

#################################################################################

MSRPC_UUID_IFSRMREPORTJOB = uuidtup_to_bin(('38e87280-715c-4c7d-a280-ea1651a19fef','0.0'))


class Task(NDRCALL):
    opnum = 0
    structure = (

    )

class TaskResponse(NDRCALL):
    structure = (
		('taskName', BSTR),
    )
        

class Task(NDRCALL):
    opnum = 1
    structure = (
		('taskName', BSTR),
    )

class TaskResponse(NDRCALL):
    structure = (

    )
        

class NamespaceRoots(NDRCALL):
    opnum = 2
    structure = (

    )

class NamespaceRootsResponse(NDRCALL):
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )
        

class NamespaceRoots(NDRCALL):
    opnum = 3
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )

class NamespaceRootsResponse(NDRCALL):
    structure = (

    )
        

class Formats(NDRCALL):
    opnum = 4
    structure = (

    )

class FormatsResponse(NDRCALL):
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )
        

class Formats(NDRCALL):
    opnum = 5
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )

class FormatsResponse(NDRCALL):
    structure = (

    )
        

class MailTo(NDRCALL):
    opnum = 6
    structure = (

    )

class MailToResponse(NDRCALL):
    structure = (
		('mailTo', BSTR),
    )
        

class MailTo(NDRCALL):
    opnum = 7
    structure = (
		('mailTo', BSTR),
    )

class MailToResponse(NDRCALL):
    structure = (

    )
        

class RunningStatus(NDRCALL):
    opnum = 8
    structure = (

    )

class RunningStatusResponse(NDRCALL):
    structure = (
		('runningStatus', FSRMREPORTRUNNINGSTATUS),
    )
        

class LastRun(NDRCALL):
    opnum = 9
    structure = (

    )

class LastRunResponse(NDRCALL):
    structure = (
		('lastRun', DATE),
    )
        

class LastError(NDRCALL):
    opnum = 10
    structure = (

    )

class LastErrorResponse(NDRCALL):
    structure = (
		('lastError', BSTR),
    )
        

class LastGeneratedInDirectory(NDRCALL):
    opnum = 11
    structure = (

    )

class LastGeneratedInDirectoryResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class EnumReports(NDRCALL):
    opnum = 12
    structure = (

    )

class EnumReportsResponse(NDRCALL):
    structure = (
		('reports', IFSRMCOLLECTION),
    )
        

class CreateReport(NDRCALL):
    opnum = 13
    structure = (
		('reportType', FSRMREPORTTYPE),
    )

class CreateReportResponse(NDRCALL):
    structure = (
		('report', IFSRMREPORT),
    )
        

class Run(NDRCALL):
    opnum = 14
    structure = (
		('context', FSRMREPORTGENERATIONCONTEXT),
    )

class RunResponse(NDRCALL):
    structure = (

    )
        

class WaitForCompletion(NDRCALL):
    opnum = 15
    structure = (
		('waitSeconds', LONG),
    )

class WaitForCompletionResponse(NDRCALL):
    structure = (
		('completed', VARIANT_BOOL),
    )
        

class Cancel(NDRCALL):
    opnum = 16
    structure = (

    )

class CancelResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Task,TaskResponse),
1 : (NamespaceRoots,NamespaceRootsResponse),
2 : (Formats,FormatsResponse),
3 : (MailTo,MailToResponse),
4 : (RunningStatus,RunningStatusResponse),
5 : (LastRun,LastRunResponse),
6 : (LastError,LastErrorResponse),
7 : (LastGeneratedInDirectory,LastGeneratedInDirectoryResponse),
8 : (EnumReports,EnumReportsResponse),
9 : (CreateReport,CreateReportResponse),
10 : (Run,RunResponse),
11 : (WaitForCompletion,WaitForCompletionResponse),
12 : (Cancel,CancelResponse),
}

#################################################################################

#IFsrmReport Definition

#################################################################################

MSRPC_UUID_IFSRMREPORT = uuidtup_to_bin(('d8cc81d9-468-4a4-bfa5-4a9dec9b638','0.0'))


class Type(NDRCALL):
    opnum = 0
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('reportType', FSRMREPORTTYPE),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 2
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class Description(NDRCALL):
    opnum = 3
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('description', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 4
    structure = (
		('description', BSTR),
    )

class DescriptionResponse(NDRCALL):
    structure = (

    )
        

class LastGeneratedFileNamePrefix(NDRCALL):
    opnum = 5
    structure = (

    )

class LastGeneratedFileNamePrefixResponse(NDRCALL):
    structure = (
		('prefix', BSTR),
    )
        

class GetFilter(NDRCALL):
    opnum = 6
    structure = (
		('filter', FSRMREPORTFILTER),
    )

class GetFilterResponse(NDRCALL):
    structure = (
		('filterValue', VARIANT),
    )
        

class SetFilter(NDRCALL):
    opnum = 7
    structure = (
		('filter', FSRMREPORTFILTER),
		('filterValue', VARIANT),
    )

class SetFilterResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 8
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Type,TypeResponse),
1 : (Name,NameResponse),
2 : (Description,DescriptionResponse),
3 : (LastGeneratedFileNamePrefix,LastGeneratedFileNamePrefixResponse),
4 : (GetFilter,GetFilterResponse),
5 : (SetFilter,SetFilterResponse),
6 : (Delete,DeleteResponse),
}

#################################################################################

#IFsrmReportScheduler Definition

#################################################################################

MSRPC_UUID_IFSRMREPORTSCHEDULER = uuidtup_to_bin(('6879caf9-6617-4484-8719-71c3d8645f94','0.0'))


class VerifyNamespaces(NDRCALL):
    opnum = 0
    structure = (
		('namespacesSafeArray', VARIANT),
    )

class VerifyNamespacesResponse(NDRCALL):
    structure = (

    )
        

class CreateScheduleTask(NDRCALL):
    opnum = 1
    structure = (
		('taskName', BSTR),
		('namespacesSafeArray', VARIANT),
		('serializedTask', BSTR),
    )

class CreateScheduleTaskResponse(NDRCALL):
    structure = (

    )
        

class ModifyScheduleTask(NDRCALL):
    opnum = 2
    structure = (
		('taskName', BSTR),
		('namespacesSafeArray', VARIANT),
		('serializedTask', BSTR),
    )

class ModifyScheduleTaskResponse(NDRCALL):
    structure = (

    )
        

class DeleteScheduleTask(NDRCALL):
    opnum = 3
    structure = (
		('taskName', BSTR),
    )

class DeleteScheduleTaskResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (VerifyNamespaces,VerifyNamespacesResponse),
1 : (CreateScheduleTask,CreateScheduleTaskResponse),
2 : (ModifyScheduleTask,ModifyScheduleTaskResponse),
3 : (DeleteScheduleTask,DeleteScheduleTaskResponse),
}

#################################################################################

#IFsrmFileManagementJobManager Definition

#################################################################################

MSRPC_UUID_IFSRMFILEMANAGEMENTJOBMANAGER = uuidtup_to_bin(('ee321ecb-d95e-489-907-c7685a013235','0.0'))


class ActionVariables(NDRCALL):
    opnum = 0
    structure = (

    )

class ActionVariablesResponse(NDRCALL):
    structure = (
		('variables', SAFEARRAY ( VARIANT )),
    )
        

class ActionVariableDescriptions(NDRCALL):
    opnum = 1
    structure = (

    )

class ActionVariableDescriptionsResponse(NDRCALL):
    structure = (
		('descriptions', SAFEARRAY ( VARIANT )),
    )
        

class EnumFileManagementJobs(NDRCALL):
    opnum = 2
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumFileManagementJobsResponse(NDRCALL):
    structure = (
		('fileManagementJobs', IFSRMCOLLECTION),
    )
        

class CreateFileManagementJob(NDRCALL):
    opnum = 3
    structure = (

    )

class CreateFileManagementJobResponse(NDRCALL):
    structure = (
		('fileManagementJob', IFSRMFILEMANAGEMENTJOB),
    )
        

class GetFileManagementJob(NDRCALL):
    opnum = 4
    structure = (
		('name', BSTR),
    )

class GetFileManagementJobResponse(NDRCALL):
    structure = (
		('fileManagementJob', IFSRMFILEMANAGEMENTJOB),
    )
        
OPNUMS = {
0 : (ActionVariables,ActionVariablesResponse),
1 : (ActionVariableDescriptions,ActionVariableDescriptionsResponse),
2 : (EnumFileManagementJobs,EnumFileManagementJobsResponse),
3 : (CreateFileManagementJob,CreateFileManagementJobResponse),
4 : (GetFileManagementJob,GetFileManagementJobResponse),
}

#################################################################################

#IFsrmFileManagementJob Definition

#################################################################################

MSRPC_UUID_IFSRMFILEMANAGEMENTJOB = uuidtup_to_bin(('0770687e-9f36-4d6f-8778-599d188461c9','0.0'))

FsrmDaysNotSpecified =  LONG
FsrmDateNotSpecified =  DATE

class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class NamespaceRoots(NDRCALL):
    opnum = 2
    structure = (

    )

class NamespaceRootsResponse(NDRCALL):
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )
        

class NamespaceRoots(NDRCALL):
    opnum = 3
    structure = (
		('namespaceRoots', SAFEARRAY ( VARIANT )),
    )

class NamespaceRootsResponse(NDRCALL):
    structure = (

    )
        

class Enabled(NDRCALL):
    opnum = 4
    structure = (

    )

class EnabledResponse(NDRCALL):
    structure = (
		('enabled', VARIANT_BOOL),
    )
        

class Enabled(NDRCALL):
    opnum = 5
    structure = (
		('enabled', VARIANT_BOOL),
    )

class EnabledResponse(NDRCALL):
    structure = (

    )
        

class OperationType(NDRCALL):
    opnum = 6
    structure = (

    )

class OperationTypeResponse(NDRCALL):
    structure = (
		('operationType', FSRMFILEMANAGEMENTTYPE),
    )
        

class OperationType(NDRCALL):
    opnum = 7
    structure = (
		('operationType', FSRMFILEMANAGEMENTTYPE),
    )

class OperationTypeResponse(NDRCALL):
    structure = (

    )
        

class ExpirationDirectory(NDRCALL):
    opnum = 8
    structure = (

    )

class ExpirationDirectoryResponse(NDRCALL):
    structure = (
		('expirationDirectory', BSTR),
    )
        

class ExpirationDirectory(NDRCALL):
    opnum = 9
    structure = (
		('expirationDirectory', BSTR),
    )

class ExpirationDirectoryResponse(NDRCALL):
    structure = (

    )
        

class CustomAction(NDRCALL):
    opnum = 10
    structure = (

    )

class CustomActionResponse(NDRCALL):
    structure = (
		('action', IFSRMACTIONCOMMAND),
    )
        

class Notifications(NDRCALL):
    opnum = 11
    structure = (

    )

class NotificationsResponse(NDRCALL):
    structure = (
		('notifications', SAFEARRAY ( VARIANT )),
    )
        

class Logging(NDRCALL):
    opnum = 12
    structure = (

    )

class LoggingResponse(NDRCALL):
    structure = (
		('loggingFlags', LONG),
    )
        

class Logging(NDRCALL):
    opnum = 13
    structure = (
		('loggingFlags', LONG),
    )

class LoggingResponse(NDRCALL):
    structure = (

    )
        

class ReportEnabled(NDRCALL):
    opnum = 14
    structure = (

    )

class ReportEnabledResponse(NDRCALL):
    structure = (
		('reportEnabled', VARIANT_BOOL),
    )
        

class ReportEnabled(NDRCALL):
    opnum = 15
    structure = (
		('reportEnabled', VARIANT_BOOL),
    )

class ReportEnabledResponse(NDRCALL):
    structure = (

    )
        

class Formats(NDRCALL):
    opnum = 16
    structure = (

    )

class FormatsResponse(NDRCALL):
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )
        

class Formats(NDRCALL):
    opnum = 17
    structure = (
		('formats', SAFEARRAY ( VARIANT )),
    )

class FormatsResponse(NDRCALL):
    structure = (

    )
        

class MailTo(NDRCALL):
    opnum = 18
    structure = (

    )

class MailToResponse(NDRCALL):
    structure = (
		('mailTo', BSTR),
    )
        

class MailTo(NDRCALL):
    opnum = 19
    structure = (
		('mailTo', BSTR),
    )

class MailToResponse(NDRCALL):
    structure = (

    )
        

class DaysSinceFileCreated(NDRCALL):
    opnum = 20
    structure = (

    )

class DaysSinceFileCreatedResponse(NDRCALL):
    structure = (
		('daysSinceCreation', LONG),
    )
        

class DaysSinceFileCreated(NDRCALL):
    opnum = 21
    structure = (
		('daysSinceCreation', LONG),
    )

class DaysSinceFileCreatedResponse(NDRCALL):
    structure = (

    )
        

class DaysSinceFileLastAccessed(NDRCALL):
    opnum = 22
    structure = (

    )

class DaysSinceFileLastAccessedResponse(NDRCALL):
    structure = (
		('daysSinceAccess', LONG),
    )
        

class DaysSinceFileLastAccessed(NDRCALL):
    opnum = 23
    structure = (
		('daysSinceAccess', LONG),
    )

class DaysSinceFileLastAccessedResponse(NDRCALL):
    structure = (

    )
        

class DaysSinceFileLastModified(NDRCALL):
    opnum = 24
    structure = (

    )

class DaysSinceFileLastModifiedResponse(NDRCALL):
    structure = (
		('daysSinceModify', LONG),
    )
        

class DaysSinceFileLastModified(NDRCALL):
    opnum = 25
    structure = (
		('daysSinceModify', LONG),
    )

class DaysSinceFileLastModifiedResponse(NDRCALL):
    structure = (

    )
        

class PropertyConditions(NDRCALL):
    opnum = 26
    structure = (

    )

class PropertyConditionsResponse(NDRCALL):
    structure = (
		('propertyConditions', IFSRMCOLLECTION),
    )
        

class FromDate(NDRCALL):
    opnum = 27
    structure = (

    )

class FromDateResponse(NDRCALL):
    structure = (
		('fromDate', DATE),
    )
        

class FromDate(NDRCALL):
    opnum = 28
    structure = (
		('fromDate', DATE),
    )

class FromDateResponse(NDRCALL):
    structure = (

    )
        

class Task(NDRCALL):
    opnum = 29
    structure = (

    )

class TaskResponse(NDRCALL):
    structure = (
		('taskName', BSTR),
    )
        

class Task(NDRCALL):
    opnum = 30
    structure = (
		('taskName', BSTR),
    )

class TaskResponse(NDRCALL):
    structure = (

    )
        

class Parameters(NDRCALL):
    opnum = 31
    structure = (

    )

class ParametersResponse(NDRCALL):
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )
        

class Parameters(NDRCALL):
    opnum = 32
    structure = (
		('parameters', SAFEARRAY ( VARIANT )),
    )

class ParametersResponse(NDRCALL):
    structure = (

    )
        

class RunningStatus(NDRCALL):
    opnum = 33
    structure = (

    )

class RunningStatusResponse(NDRCALL):
    structure = (
		('runningStatus', FSRMREPORTRUNNINGSTATUS),
    )
        

class LastError(NDRCALL):
    opnum = 34
    structure = (

    )

class LastErrorResponse(NDRCALL):
    structure = (
		('lastError', BSTR),
    )
        

class LastReportPathWithoutExtension(NDRCALL):
    opnum = 35
    structure = (

    )

class LastReportPathWithoutExtensionResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class LastRun(NDRCALL):
    opnum = 36
    structure = (

    )

class LastRunResponse(NDRCALL):
    structure = (
		('lastRun', DATE),
    )
        

class FileNamePattern(NDRCALL):
    opnum = 37
    structure = (

    )

class FileNamePatternResponse(NDRCALL):
    structure = (
		('fileNamePattern', BSTR),
    )
        

class FileNamePattern(NDRCALL):
    opnum = 38
    structure = (
		('fileNamePattern', BSTR),
    )

class FileNamePatternResponse(NDRCALL):
    structure = (

    )
        

class Run(NDRCALL):
    opnum = 39
    structure = (
		('context', FSRMREPORTGENERATIONCONTEXT),
    )

class RunResponse(NDRCALL):
    structure = (

    )
        

class WaitForCompletion(NDRCALL):
    opnum = 40
    structure = (
		('waitSeconds', LONG),
    )

class WaitForCompletionResponse(NDRCALL):
    structure = (
		('completed', VARIANT_BOOL),
    )
        

class Cancel(NDRCALL):
    opnum = 41
    structure = (

    )

class CancelResponse(NDRCALL):
    structure = (

    )
        

class AddNotification(NDRCALL):
    opnum = 42
    structure = (
		('days', LONG),
    )

class AddNotificationResponse(NDRCALL):
    structure = (

    )
        

class DeleteNotification(NDRCALL):
    opnum = 43
    structure = (
		('days', LONG),
    )

class DeleteNotificationResponse(NDRCALL):
    structure = (

    )
        

class ModifyNotification(NDRCALL):
    opnum = 44
    structure = (
		('days', LONG),
		('newDays', LONG),
    )

class ModifyNotificationResponse(NDRCALL):
    structure = (

    )
        

class CreateNotificationAction(NDRCALL):
    opnum = 45
    structure = (
		('days', LONG),
		('actionType', FSRMACTIONTYPE),
    )

class CreateNotificationActionResponse(NDRCALL):
    structure = (
		('action', IFSRMACTION),
    )
        

class EnumNotificationActions(NDRCALL):
    opnum = 46
    structure = (
		('days', LONG),
    )

class EnumNotificationActionsResponse(NDRCALL):
    structure = (
		('actions', IFSRMCOLLECTION),
    )
        

class CreatePropertyCondition(NDRCALL):
    opnum = 47
    structure = (
		('name', BSTR),
    )

class CreatePropertyConditionResponse(NDRCALL):
    structure = (
		('propertyCondition', IFSRMPROPERTYCONDITION),
    )
        

class CreateCustomAction(NDRCALL):
    opnum = 48
    structure = (

    )

class CreateCustomActionResponse(NDRCALL):
    structure = (
		('customAction', IFSRMACTIONCOMMAND),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (NamespaceRoots,NamespaceRootsResponse),
2 : (Enabled,EnabledResponse),
3 : (OperationType,OperationTypeResponse),
4 : (ExpirationDirectory,ExpirationDirectoryResponse),
5 : (CustomAction,CustomActionResponse),
6 : (Notifications,NotificationsResponse),
7 : (Logging,LoggingResponse),
8 : (ReportEnabled,ReportEnabledResponse),
9 : (Formats,FormatsResponse),
10 : (MailTo,MailToResponse),
11 : (DaysSinceFileCreated,DaysSinceFileCreatedResponse),
12 : (DaysSinceFileLastAccessed,DaysSinceFileLastAccessedResponse),
13 : (DaysSinceFileLastModified,DaysSinceFileLastModifiedResponse),
14 : (PropertyConditions,PropertyConditionsResponse),
15 : (FromDate,FromDateResponse),
16 : (Task,TaskResponse),
17 : (Parameters,ParametersResponse),
18 : (RunningStatus,RunningStatusResponse),
19 : (LastError,LastErrorResponse),
20 : (LastReportPathWithoutExtension,LastReportPathWithoutExtensionResponse),
21 : (LastRun,LastRunResponse),
22 : (FileNamePattern,FileNamePatternResponse),
23 : (Run,RunResponse),
24 : (WaitForCompletion,WaitForCompletionResponse),
25 : (Cancel,CancelResponse),
26 : (AddNotification,AddNotificationResponse),
27 : (DeleteNotification,DeleteNotificationResponse),
28 : (ModifyNotification,ModifyNotificationResponse),
29 : (CreateNotificationAction,CreateNotificationActionResponse),
30 : (EnumNotificationActions,EnumNotificationActionsResponse),
31 : (CreatePropertyCondition,CreatePropertyConditionResponse),
32 : (CreateCustomAction,CreateCustomActionResponse),
}

#################################################################################

#IFsrmPropertyCondition Definition

#################################################################################

MSRPC_UUID_IFSRMPROPERTYCONDITION = uuidtup_to_bin(('326af66f-2ac0-4f68-bf8c-4759f054fa29','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class Type(NDRCALL):
    opnum = 2
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('type', FSRMPROPERTYCONDITIONTYPE),
    )
        

class Type(NDRCALL):
    opnum = 3
    structure = (
		('type', FSRMPROPERTYCONDITIONTYPE),
    )

class TypeResponse(NDRCALL):
    structure = (

    )
        

class Value(NDRCALL):
    opnum = 4
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('value', BSTR),
    )
        

class Value(NDRCALL):
    opnum = 5
    structure = (
		('value', BSTR),
    )

class ValueResponse(NDRCALL):
    structure = (

    )
        

class Delete(NDRCALL):
    opnum = 6
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Type,TypeResponse),
2 : (Value,ValueResponse),
3 : (Delete,DeleteResponse),
}

#################################################################################

#IFsrmFileGroup Definition

#################################################################################

MSRPC_UUID_IFSRMFILEGROUP = uuidtup_to_bin(('8dd04909-0e34-4d55-afaa-89e1f1a1bbb9','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class Members(NDRCALL):
    opnum = 2
    structure = (

    )

class MembersResponse(NDRCALL):
    structure = (
		('members', IFSRMMUTABLECOLLECTION),
    )
        

class Members(NDRCALL):
    opnum = 3
    structure = (
		('members', IFSRMMUTABLECOLLECTION),
    )

class MembersResponse(NDRCALL):
    structure = (

    )
        

class NonMembers(NDRCALL):
    opnum = 4
    structure = (

    )

class NonMembersResponse(NDRCALL):
    structure = (
		('nonMembers', IFSRMMUTABLECOLLECTION),
    )
        

class NonMembers(NDRCALL):
    opnum = 5
    structure = (
		('nonMembers', IFSRMMUTABLECOLLECTION),
    )

class NonMembersResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (Members,MembersResponse),
2 : (NonMembers,NonMembersResponse),
}

#################################################################################

#IFsrmFileGroupImported Definition

#################################################################################

MSRPC_UUID_IFSRMFILEGROUPIMPORTED = uuidtup_to_bin(('ad55f10b-511-4e7-94f-d9ee2e470ded','0.0'))


class OverwriteOnCommit(NDRCALL):
    opnum = 0
    structure = (

    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (
		('overwrite', VARIANT_BOOL),
    )
        

class OverwriteOnCommit(NDRCALL):
    opnum = 1
    structure = (
		('overwrite', VARIANT_BOOL),
    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OverwriteOnCommit,OverwriteOnCommitResponse),
}

#################################################################################

#IFsrmFileGroupManager Definition

#################################################################################

MSRPC_UUID_IFSRMFILEGROUPMANAGER = uuidtup_to_bin(('426677d5-018c-485c-8a51-20b86d00bdc4','0.0'))


class CreateFileGroup(NDRCALL):
    opnum = 0
    structure = (

    )

class CreateFileGroupResponse(NDRCALL):
    structure = (
		('fileGroup', IFSRMFILEGROUP),
    )
        

class GetFileGroup(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class GetFileGroupResponse(NDRCALL):
    structure = (
		('fileGroup', IFSRMFILEGROUP),
    )
        

class EnumFileGroups(NDRCALL):
    opnum = 2
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumFileGroupsResponse(NDRCALL):
    structure = (
		('fileGroups', IFSRMCOMMITTABLECOLLECTION),
    )
        

class ExportFileGroups(NDRCALL):
    opnum = 3
    structure = (
		('fileGroupNamesArray', VARIANT),
    )

class ExportFileGroupsResponse(NDRCALL):
    structure = (
		('serializedFileGroups', BSTR),
    )
        

class ImportFileGroups(NDRCALL):
    opnum = 4
    structure = (
		('serializedFileGroups', BSTR),
		('fileGroupNamesArray', VARIANT),
    )

class ImportFileGroupsResponse(NDRCALL):
    structure = (
		('fileGroups', IFSRMCOMMITTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (CreateFileGroup,CreateFileGroupResponse),
1 : (GetFileGroup,GetFileGroupResponse),
2 : (EnumFileGroups,EnumFileGroupsResponse),
3 : (ExportFileGroups,ExportFileGroupsResponse),
4 : (ImportFileGroups,ImportFileGroupsResponse),
}

#################################################################################

#IFsrmFileScreenBase Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENBASE = uuidtup_to_bin(('f3637e80-522-42-a637-bbb642b41cfc','0.0'))


class BlockedFileGroups(NDRCALL):
    opnum = 0
    structure = (

    )

class BlockedFileGroupsResponse(NDRCALL):
    structure = (
		('blockList', IFSRMMUTABLECOLLECTION),
    )
        

class BlockedFileGroups(NDRCALL):
    opnum = 1
    structure = (
		('blockList', IFSRMMUTABLECOLLECTION),
    )

class BlockedFileGroupsResponse(NDRCALL):
    structure = (

    )
        

class FileScreenFlags(NDRCALL):
    opnum = 2
    structure = (

    )

class FileScreenFlagsResponse(NDRCALL):
    structure = (
		('fileScreenFlags', LONG),
    )
        

class FileScreenFlags(NDRCALL):
    opnum = 3
    structure = (
		('fileScreenFlags', LONG),
    )

class FileScreenFlagsResponse(NDRCALL):
    structure = (

    )
        

class CreateAction(NDRCALL):
    opnum = 4
    structure = (
		('actionType', FSRMACTIONTYPE),
    )

class CreateActionResponse(NDRCALL):
    structure = (
		('action', IFSRMACTION),
    )
        

class EnumActions(NDRCALL):
    opnum = 5
    structure = (

    )

class EnumActionsResponse(NDRCALL):
    structure = (
		('actions', IFSRMCOLLECTION),
    )
        
OPNUMS = {
0 : (BlockedFileGroups,BlockedFileGroupsResponse),
1 : (FileScreenFlags,FileScreenFlagsResponse),
2 : (CreateAction,CreateActionResponse),
3 : (EnumActions,EnumActionsResponse),
}

#################################################################################

#IFsrmFileScreen Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREEN = uuidtup_to_bin(('5f6325d3-ce88-4733-84c1-2d6aefc5ea07','0.0'))


class Path(NDRCALL):
    opnum = 0
    structure = (

    )

class PathResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class SourceTemplateName(NDRCALL):
    opnum = 1
    structure = (

    )

class SourceTemplateNameResponse(NDRCALL):
    structure = (
		('fileScreenTemplateName', BSTR),
    )
        

class MatchesSourceTemplate(NDRCALL):
    opnum = 2
    structure = (

    )

class MatchesSourceTemplateResponse(NDRCALL):
    structure = (
		('matches', VARIANT_BOOL),
    )
        

class UserSid(NDRCALL):
    opnum = 3
    structure = (

    )

class UserSidResponse(NDRCALL):
    structure = (
		('userSid', BSTR),
    )
        

class UserAccount(NDRCALL):
    opnum = 4
    structure = (

    )

class UserAccountResponse(NDRCALL):
    structure = (
		('userAccount', BSTR),
    )
        

class ApplyTemplate(NDRCALL):
    opnum = 5
    structure = (
		('fileScreenTemplateName', BSTR),
    )

class ApplyTemplateResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Path,PathResponse),
1 : (SourceTemplateName,SourceTemplateNameResponse),
2 : (MatchesSourceTemplate,MatchesSourceTemplateResponse),
3 : (UserSid,UserSidResponse),
4 : (UserAccount,UserAccountResponse),
5 : (ApplyTemplate,ApplyTemplateResponse),
}

#################################################################################

#IFsrmFileScreenException Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENEXCEPTION = uuidtup_to_bin(('bee7ce02-df77-4515-9389-78015fc1a','0.0'))


class Path(NDRCALL):
    opnum = 0
    structure = (

    )

class PathResponse(NDRCALL):
    structure = (
		('path', BSTR),
    )
        

class AllowedFileGroups(NDRCALL):
    opnum = 1
    structure = (

    )

class AllowedFileGroupsResponse(NDRCALL):
    structure = (
		('allowList', IFSRMMUTABLECOLLECTION),
    )
        

class AllowedFileGroups(NDRCALL):
    opnum = 2
    structure = (
		('allowList', IFSRMMUTABLECOLLECTION),
    )

class AllowedFileGroupsResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Path,PathResponse),
1 : (AllowedFileGroups,AllowedFileGroupsResponse),
}

#################################################################################

#IFsrmFileScreenManager Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENMANAGER = uuidtup_to_bin(('ff4fa04e-594-4da-a3a0-d5b4d3c52eba','0.0'))


class ActionVariables(NDRCALL):
    opnum = 0
    structure = (

    )

class ActionVariablesResponse(NDRCALL):
    structure = (
		('variables', SAFEARRAY ( VARIANT )),
    )
        

class ActionVariableDescriptions(NDRCALL):
    opnum = 1
    structure = (

    )

class ActionVariableDescriptionsResponse(NDRCALL):
    structure = (
		('descriptions', SAFEARRAY ( VARIANT )),
    )
        

class CreateFileScreen(NDRCALL):
    opnum = 2
    structure = (
		('path', BSTR),
    )

class CreateFileScreenResponse(NDRCALL):
    structure = (
		('fileScreen', IFSRMFILESCREEN),
    )
        

class GetFileScreen(NDRCALL):
    opnum = 3
    structure = (
		('path', BSTR),
    )

class GetFileScreenResponse(NDRCALL):
    structure = (
		('fileScreen', IFSRMFILESCREEN),
    )
        

class EnumFileScreens(NDRCALL):
    opnum = 4
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class EnumFileScreensResponse(NDRCALL):
    structure = (
		('fileScreens', IFSRMCOMMITTABLECOLLECTION),
    )
        

class CreateFileScreenException(NDRCALL):
    opnum = 5
    structure = (
		('path', BSTR),
    )

class CreateFileScreenExceptionResponse(NDRCALL):
    structure = (
		('fileScreenException', IFSRMFILESCREENEXCEPTION),
    )
        

class GetFileScreenException(NDRCALL):
    opnum = 6
    structure = (
		('path', BSTR),
    )

class GetFileScreenExceptionResponse(NDRCALL):
    structure = (
		('fileScreenException', IFSRMFILESCREENEXCEPTION),
    )
        

class EnumFileScreenExceptions(NDRCALL):
    opnum = 7
    structure = (
		('path', BSTR),
		('options', FSRMENUMOPTIONS),
    )

class EnumFileScreenExceptionsResponse(NDRCALL):
    structure = (
		('fileScreenExceptions', IFSRMCOMMITTABLECOLLECTION),
    )
        

class CreateFileScreenCollection(NDRCALL):
    opnum = 8
    structure = (

    )

class CreateFileScreenCollectionResponse(NDRCALL):
    structure = (
		('collection', IFSRMCOMMITTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (ActionVariables,ActionVariablesResponse),
1 : (ActionVariableDescriptions,ActionVariableDescriptionsResponse),
2 : (CreateFileScreen,CreateFileScreenResponse),
3 : (GetFileScreen,GetFileScreenResponse),
4 : (EnumFileScreens,EnumFileScreensResponse),
5 : (CreateFileScreenException,CreateFileScreenExceptionResponse),
6 : (GetFileScreenException,GetFileScreenExceptionResponse),
7 : (EnumFileScreenExceptions,EnumFileScreenExceptionsResponse),
8 : (CreateFileScreenCollection,CreateFileScreenCollectionResponse),
}

#################################################################################

#IFsrmFileScreenTemplate Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENTEMPLATE = uuidtup_to_bin(('205bebf8-dd93-452a-95a6-32b566b35828','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('name', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class CopyTemplate(NDRCALL):
    opnum = 2
    structure = (
		('fileScreenTemplateName', BSTR),
    )

class CopyTemplateResponse(NDRCALL):
    structure = (

    )
        

class CommitAndUpdateDerived(NDRCALL):
    opnum = 3
    structure = (
		('commitOptions', FSRMCOMMITOPTIONS),
		('applyOptions', FSRMTEMPLATEAPPLYOPTIONS),
    )

class CommitAndUpdateDerivedResponse(NDRCALL):
    structure = (
		('derivedObjectsResult', IFSRMDERIVEDOBJECTSRESULT),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (CopyTemplate,CopyTemplateResponse),
2 : (CommitAndUpdateDerived,CommitAndUpdateDerivedResponse),
}

#################################################################################

#IFsrmFileScreenTemplateImported Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENTEMPLATEIMPORTED = uuidtup_to_bin(('e1010359-35-4cd-9e4-ef48622fdf30','0.0'))


class OverwriteOnCommit(NDRCALL):
    opnum = 0
    structure = (

    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (
		('overwrite', VARIANT_BOOL),
    )
        

class OverwriteOnCommit(NDRCALL):
    opnum = 1
    structure = (
		('overwrite', VARIANT_BOOL),
    )

class OverwriteOnCommitResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OverwriteOnCommit,OverwriteOnCommitResponse),
}

#################################################################################

#IFsrmFileScreenTemplateManager Definition

#################################################################################

MSRPC_UUID_IFSRMFILESCREENTEMPLATEMANAGER = uuidtup_to_bin(('cfe36cba-1949-474-a14f-f1d580ceaf13','0.0'))


class CreateTemplate(NDRCALL):
    opnum = 0
    structure = (

    )

class CreateTemplateResponse(NDRCALL):
    structure = (
		('fileScreenTemplate', IFSRMFILESCREENTEMPLATE),
    )
        

class GetTemplate(NDRCALL):
    opnum = 1
    structure = (
		('name', BSTR),
    )

class GetTemplateResponse(NDRCALL):
    structure = (
		('fileScreenTemplate', IFSRMFILESCREENTEMPLATE),
    )
        

class EnumTemplates(NDRCALL):
    opnum = 2
    structure = (
		('options', FSRMENUMOPTIONS),
    )

class EnumTemplatesResponse(NDRCALL):
    structure = (
		('fileScreenTemplates', IFSRMCOMMITTABLECOLLECTION),
    )
        

class ExportTemplates(NDRCALL):
    opnum = 3
    structure = (
		('fileScreenTemplateNamesArray', VARIANT),
    )

class ExportTemplatesResponse(NDRCALL):
    structure = (
		('serializedFileScreenTemplates', BSTR),
    )
        

class ImportTemplates(NDRCALL):
    opnum = 4
    structure = (
		('serializedFileScreenTemplates', BSTR),
		('fileScreenTemplateNamesArray', VARIANT),
    )

class ImportTemplatesResponse(NDRCALL):
    structure = (
		('fileScreenTemplates', IFSRMCOMMITTABLECOLLECTION),
    )
        
OPNUMS = {
0 : (CreateTemplate,CreateTemplateResponse),
1 : (GetTemplate,GetTemplateResponse),
2 : (EnumTemplates,EnumTemplatesResponse),
3 : (ExportTemplates,ExportTemplatesResponse),
4 : (ImportTemplates,ImportTemplatesResponse),
}

