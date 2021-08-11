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
        

class ANONYMOUS17(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous17', ANONYMOUS17),
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

BYTE = BYTE

plaPerformanceCounter = 0,
plaTrace = 1,
plaConfiguration = 2,
plaAlert = 3,
plaApiTrace = 4
        

plaCommaSeparated = 0,
plaTabSeparated = 1,
plaSql = 2,
plaBinary = 3
        

plaNone = 0,
plaPattern = 1,
plaComputer = 2,
plaMonthDayHour = 256,
plaSerialNumber = 512,
plaYearDayOfYear = 1024,
plaYearMonth = 2048,
plaYearMonthDay = 4096,
plaYearMonthDayHour = 8192,
plaMonthDayHourMinute = 16384
        

plaStopped = 0,
plaRunning = 1,
plaCompiling = 2,
plaPending = 3,
plaUndefined = 4
        

plaTimeStamp = 0,
plaPerformance = 1,
plaSystem = 2,
plaCycle = 3
        

plaFile = 1,
plaRealTime = 2,
plaBoth = 3,
plaBuffering = 4
        

plaCreateNew = 1,
plaModify = 2,
plaCreateOrModify = 3,
plaUpdateRunningInstance = 16,
plaFlushTrace = 32,
plaValidateOnly = 4096
        

plaIndex = 1,
plaFlag = 2,
plaFlagArray = 3,
plaValidation = 4
        

plaRunOnce = 0,
plaSunday = 1,
plaMonday = 2,
plaTuesday = 4,
plaWednesday = 8,
plaThursday = 16,
plaFriday = 32,
plaSaturday = 64,
plaEveryday = 127
        

plaDeleteLargest = 0,
plaDeleteOldest = 1
        

plaCreateReport = 1,
plaRunRules = 2,
plaCreateHtml = 4,
plaFolderActions = 8,
plaResourceFreeing = 16
        

plaCreateCab = 1,
plaDeleteData = 2,
plaSendCab = 4,
plaDeleteCab = 8,
plaDeleteReport = 16
        
#################################################################################

#CONSTANTS

#################################################################################

IDATACOLLECTORSET = 
IDATAMANAGER = 
IFOLDERACTION = 
IFOLDERACTIONCOLLECTION = 
IDATACOLLECTOR = 
IPERFORMANCECOUNTERDATACOLLECTOR = 
ITRACEDATACOLLECTOR = 
ICONFIGURATIONDATACOLLECTOR = 
IALERTDATACOLLECTOR = 
IAPITRACINGDATACOLLECTOR = 
IDATACOLLECTORCOLLECTION = 
IDATACOLLECTORSETCOLLECTION = 
ITRACEDATAPROVIDER = 
ITRACEDATAPROVIDERCOLLECTION = 
ISCHEDULE = 
ISCHEDULECOLLECTION = 
IVALUEMAPITEM = 
IVALUEMAP = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IDataCollectorSet Definition

#################################################################################

MSRPC_UUID_IDATACOLLECTORSET = uuidtup_to_bin(('03837520-098b-11d8-9414-505054503030','0.0'))


class DataCollectors(NDRCALL):
    opnum = 0
    structure = (

    )

class DataCollectorsResponse(NDRCALL):
    structure = (
		('COLLECTORS', IDATACOLLECTORCOLLECTION),
    )
        

class Duration(NDRCALL):
    opnum = 1
    structure = (

    )

class DurationResponse(NDRCALL):
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )
        

class Duration(NDRCALL):
    opnum = 2
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )

class DurationResponse(NDRCALL):
    structure = (

    )
        

class Description(NDRCALL):
    opnum = 3
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('DESCRIPTION', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 4
    structure = (
		('DESCRIPTION', BSTR),
    )

class DescriptionResponse(NDRCALL):
    structure = (

    )
        

class DescriptionUnresolved(NDRCALL):
    opnum = 5
    structure = (

    )

class DescriptionUnresolvedResponse(NDRCALL):
    structure = (
		('DESCR', BSTR),
    )
        

class DisplayName(NDRCALL):
    opnum = 6
    structure = (

    )

class DisplayNameResponse(NDRCALL):
    structure = (
		('DISPLAYNAME', BSTR),
    )
        

class DisplayName(NDRCALL):
    opnum = 7
    structure = (
		('DISPLAYNAME', BSTR),
    )

class DisplayNameResponse(NDRCALL):
    structure = (

    )
        

class DisplayNameUnresolved(NDRCALL):
    opnum = 8
    structure = (

    )

class DisplayNameUnresolvedResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class Keywords(NDRCALL):
    opnum = 9
    structure = (

    )

class KeywordsResponse(NDRCALL):
    structure = (
		('KEYWORDS', SAFEARRAY ( BSTR )),
    )
        

class Keywords(NDRCALL):
    opnum = 10
    structure = (
		('KEYWORDS', SAFEARRAY ( BSTR )),
    )

class KeywordsResponse(NDRCALL):
    structure = (

    )
        

class LatestOutputLocation(NDRCALL):
    opnum = 11
    structure = (

    )

class LatestOutputLocationResponse(NDRCALL):
    structure = (
		('PATH', BSTR),
    )
        

class LatestOutputLocation(NDRCALL):
    opnum = 12
    structure = (
		('PATH', BSTR),
    )

class LatestOutputLocationResponse(NDRCALL):
    structure = (

    )
        

class Name(NDRCALL):
    opnum = 13
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class OutputLocation(NDRCALL):
    opnum = 14
    structure = (

    )

class OutputLocationResponse(NDRCALL):
    structure = (
		('PATH', BSTR),
    )
        

class RootPath(NDRCALL):
    opnum = 15
    structure = (

    )

class RootPathResponse(NDRCALL):
    structure = (
		('FOLDER', BSTR),
    )
        

class RootPath(NDRCALL):
    opnum = 16
    structure = (
		('FOLDER', BSTR),
    )

class RootPathResponse(NDRCALL):
    structure = (

    )
        

class Segment(NDRCALL):
    opnum = 17
    structure = (

    )

class SegmentResponse(NDRCALL):
    structure = (
		('SEGMENT', VARIANT_BOOL),
    )
        

class Segment(NDRCALL):
    opnum = 18
    structure = (
		('SEGMENT', VARIANT_BOOL),
    )

class SegmentResponse(NDRCALL):
    structure = (

    )
        

class SegmentMaxDuration(NDRCALL):
    opnum = 19
    structure = (

    )

class SegmentMaxDurationResponse(NDRCALL):
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )
        

class SegmentMaxDuration(NDRCALL):
    opnum = 20
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )

class SegmentMaxDurationResponse(NDRCALL):
    structure = (

    )
        

class SegmentMaxSize(NDRCALL):
    opnum = 21
    structure = (

    )

class SegmentMaxSizeResponse(NDRCALL):
    structure = (
		('SIZE', UNSIGNED_LONG),
    )
        

class SegmentMaxSize(NDRCALL):
    opnum = 22
    structure = (
		('SIZE', UNSIGNED_LONG),
    )

class SegmentMaxSizeResponse(NDRCALL):
    structure = (

    )
        

class SerialNumber(NDRCALL):
    opnum = 23
    structure = (

    )

class SerialNumberResponse(NDRCALL):
    structure = (
		('INDEX', UNSIGNED_LONG),
    )
        

class SerialNumber(NDRCALL):
    opnum = 24
    structure = (
		('INDEX', UNSIGNED_LONG),
    )

class SerialNumberResponse(NDRCALL):
    structure = (

    )
        

class Server(NDRCALL):
    opnum = 25
    structure = (

    )

class ServerResponse(NDRCALL):
    structure = (
		('SERVER', BSTR),
    )
        

class Status(NDRCALL):
    opnum = 26
    structure = (

    )

class StatusResponse(NDRCALL):
    structure = (
		('STATUS', DATACOLLECTORSETSTATUS),
    )
        

class Subdirectory(NDRCALL):
    opnum = 27
    structure = (

    )

class SubdirectoryResponse(NDRCALL):
    structure = (
		('FOLDER', BSTR),
    )
        

class Subdirectory(NDRCALL):
    opnum = 28
    structure = (
		('FOLDER', BSTR),
    )

class SubdirectoryResponse(NDRCALL):
    structure = (

    )
        

class SubdirectoryFormat(NDRCALL):
    opnum = 29
    structure = (

    )

class SubdirectoryFormatResponse(NDRCALL):
    structure = (
		('FORMAT', AUTOPATHFORMAT),
    )
        

class SubdirectoryFormat(NDRCALL):
    opnum = 30
    structure = (
		('FORMAT', AUTOPATHFORMAT),
    )

class SubdirectoryFormatResponse(NDRCALL):
    structure = (

    )
        

class SubdirectoryFormatPattern(NDRCALL):
    opnum = 31
    structure = (

    )

class SubdirectoryFormatPatternResponse(NDRCALL):
    structure = (
		('PATTERN', BSTR),
    )
        

class SubdirectoryFormatPattern(NDRCALL):
    opnum = 32
    structure = (
		('PATTERN', BSTR),
    )

class SubdirectoryFormatPatternResponse(NDRCALL):
    structure = (

    )
        

class Task(NDRCALL):
    opnum = 33
    structure = (

    )

class TaskResponse(NDRCALL):
    structure = (
		('TASK', BSTR),
    )
        

class Task(NDRCALL):
    opnum = 34
    structure = (
		('TASK', BSTR),
    )

class TaskResponse(NDRCALL):
    structure = (

    )
        

class TaskRunAsSelf(NDRCALL):
    opnum = 35
    structure = (

    )

class TaskRunAsSelfResponse(NDRCALL):
    structure = (
		('RUNASSELF', VARIANT_BOOL),
    )
        

class TaskRunAsSelf(NDRCALL):
    opnum = 36
    structure = (
		('RUNASSELF', VARIANT_BOOL),
    )

class TaskRunAsSelfResponse(NDRCALL):
    structure = (

    )
        

class TaskArguments(NDRCALL):
    opnum = 37
    structure = (

    )

class TaskArgumentsResponse(NDRCALL):
    structure = (
		('TASK', BSTR),
    )
        

class TaskArguments(NDRCALL):
    opnum = 38
    structure = (
		('TASK', BSTR),
    )

class TaskArgumentsResponse(NDRCALL):
    structure = (

    )
        

class TaskUserTextArguments(NDRCALL):
    opnum = 39
    structure = (

    )

class TaskUserTextArgumentsResponse(NDRCALL):
    structure = (
		('USERTEXT', BSTR),
    )
        

class TaskUserTextArguments(NDRCALL):
    opnum = 40
    structure = (
		('USERTEXT', BSTR),
    )

class TaskUserTextArgumentsResponse(NDRCALL):
    structure = (

    )
        

class Schedules(NDRCALL):
    opnum = 41
    structure = (

    )

class SchedulesResponse(NDRCALL):
    structure = (
		('PPSCHEDULES', ISCHEDULECOLLECTION),
    )
        

class SchedulesEnabled(NDRCALL):
    opnum = 42
    structure = (

    )

class SchedulesEnabledResponse(NDRCALL):
    structure = (
		('ENABLED', VARIANT_BOOL),
    )
        

class SchedulesEnabled(NDRCALL):
    opnum = 43
    structure = (
		('ENABLED', VARIANT_BOOL),
    )

class SchedulesEnabledResponse(NDRCALL):
    structure = (

    )
        

class UserAccount(NDRCALL):
    opnum = 44
    structure = (

    )

class UserAccountResponse(NDRCALL):
    structure = (
		('USER', BSTR),
    )
        

class Xml(NDRCALL):
    opnum = 45
    structure = (

    )

class XmlResponse(NDRCALL):
    structure = (
		('XML', BSTR),
    )
        

class Security(NDRCALL):
    opnum = 46
    structure = (

    )

class SecurityResponse(NDRCALL):
    structure = (
		('PBSTRSECURITY', BSTR),
    )
        

class Security(NDRCALL):
    opnum = 47
    structure = (
		('BSTRSECURITY', BSTR),
    )

class SecurityResponse(NDRCALL):
    structure = (

    )
        

class StopOnCompletion(NDRCALL):
    opnum = 48
    structure = (

    )

class StopOnCompletionResponse(NDRCALL):
    structure = (
		('STOP', VARIANT_BOOL),
    )
        

class StopOnCompletion(NDRCALL):
    opnum = 49
    structure = (
		('STOP', VARIANT_BOOL),
    )

class StopOnCompletionResponse(NDRCALL):
    structure = (

    )
        

class DataManager(NDRCALL):
    opnum = 50
    structure = (

    )

class DataManagerResponse(NDRCALL):
    structure = (
		('DATAMANAGER', IDATAMANAGER),
    )
        

class SetCredentials(NDRCALL):
    opnum = 51
    structure = (

    )

class SetCredentialsResponse(NDRCALL):
    structure = (

    )
        

class Query(NDRCALL):
    opnum = 52
    structure = (
		('NAME', BSTR),
		('SERVER', BSTR),
    )

class QueryResponse(NDRCALL):
    structure = (

    )
        

class Commit(NDRCALL):
    opnum = 53
    structure = (
		('NAME', BSTR),
		('SERVER', BSTR),
    )

class CommitResponse(NDRCALL):
    structure = (
		('VALIDATION', IVALUEMAP),
    )
        

class Delete(NDRCALL):
    opnum = 54
    structure = (

    )

class DeleteResponse(NDRCALL):
    structure = (

    )
        

class Start(NDRCALL):
    opnum = 55
    structure = (
		('SYNCHRONOUS', VARIANT_BOOL),
    )

class StartResponse(NDRCALL):
    structure = (

    )
        

class Stop(NDRCALL):
    opnum = 56
    structure = (
		('SYNCHRONOUS', VARIANT_BOOL),
    )

class StopResponse(NDRCALL):
    structure = (

    )
        

class SetXml(NDRCALL):
    opnum = 57
    structure = (
		('XML', BSTR),
    )

class SetXmlResponse(NDRCALL):
    structure = (
		('VALIDATION', IVALUEMAP),
    )
        

class SetValue(NDRCALL):
    opnum = 58
    structure = (

    )

class SetValueResponse(NDRCALL):
    structure = (

    )
        

class GetValue(NDRCALL):
    opnum = 59
    structure = (

    )

class GetValueResponse(NDRCALL):
    structure = (
		('VALUE', BSTR),
    )
        
OPNUMS = {
0 : (DataCollectors,DataCollectorsResponse),
1 : (Duration,DurationResponse),
2 : (Description,DescriptionResponse),
3 : (DescriptionUnresolved,DescriptionUnresolvedResponse),
4 : (DisplayName,DisplayNameResponse),
5 : (DisplayNameUnresolved,DisplayNameUnresolvedResponse),
6 : (Keywords,KeywordsResponse),
7 : (LatestOutputLocation,LatestOutputLocationResponse),
8 : (Name,NameResponse),
9 : (OutputLocation,OutputLocationResponse),
10 : (RootPath,RootPathResponse),
11 : (Segment,SegmentResponse),
12 : (SegmentMaxDuration,SegmentMaxDurationResponse),
13 : (SegmentMaxSize,SegmentMaxSizeResponse),
14 : (SerialNumber,SerialNumberResponse),
15 : (Server,ServerResponse),
16 : (Status,StatusResponse),
17 : (Subdirectory,SubdirectoryResponse),
18 : (SubdirectoryFormat,SubdirectoryFormatResponse),
19 : (SubdirectoryFormatPattern,SubdirectoryFormatPatternResponse),
20 : (Task,TaskResponse),
21 : (TaskRunAsSelf,TaskRunAsSelfResponse),
22 : (TaskArguments,TaskArgumentsResponse),
23 : (TaskUserTextArguments,TaskUserTextArgumentsResponse),
24 : (Schedules,SchedulesResponse),
25 : (SchedulesEnabled,SchedulesEnabledResponse),
26 : (UserAccount,UserAccountResponse),
27 : (Xml,XmlResponse),
28 : (Security,SecurityResponse),
29 : (StopOnCompletion,StopOnCompletionResponse),
30 : (DataManager,DataManagerResponse),
31 : (SetCredentials,SetCredentialsResponse),
32 : (Query,QueryResponse),
33 : (Commit,CommitResponse),
34 : (Delete,DeleteResponse),
35 : (Start,StartResponse),
36 : (Stop,StopResponse),
37 : (SetXml,SetXmlResponse),
38 : (SetValue,SetValueResponse),
39 : (GetValue,GetValueResponse),
}

#################################################################################

#IDataManager Definition

#################################################################################

MSRPC_UUID_IDATAMANAGER = uuidtup_to_bin(('03837541-098b-11d8-9414-505054503030','0.0'))


class Enabled(NDRCALL):
    opnum = 0
    structure = (

    )

class EnabledResponse(NDRCALL):
    structure = (
		('PFENABLED', VARIANT_BOOL),
    )
        

class Enabled(NDRCALL):
    opnum = 1
    structure = (
		('FENABLED', VARIANT_BOOL),
    )

class EnabledResponse(NDRCALL):
    structure = (

    )
        

class CheckBeforeRunning(NDRCALL):
    opnum = 2
    structure = (

    )

class CheckBeforeRunningResponse(NDRCALL):
    structure = (
		('PFCHECK', VARIANT_BOOL),
    )
        

class CheckBeforeRunning(NDRCALL):
    opnum = 3
    structure = (
		('FCHECK', VARIANT_BOOL),
    )

class CheckBeforeRunningResponse(NDRCALL):
    structure = (

    )
        

class MinFreeDisk(NDRCALL):
    opnum = 4
    structure = (

    )

class MinFreeDiskResponse(NDRCALL):
    structure = (
		('MINFREEDISK', ULONG),
    )
        

class MinFreeDisk(NDRCALL):
    opnum = 5
    structure = (
		('MINFREEDISK', ULONG),
    )

class MinFreeDiskResponse(NDRCALL):
    structure = (

    )
        

class MaxSize(NDRCALL):
    opnum = 6
    structure = (

    )

class MaxSizeResponse(NDRCALL):
    structure = (
		('PULMAXSIZE', ULONG),
    )
        

class MaxSize(NDRCALL):
    opnum = 7
    structure = (
		('ULMAXSIZE', ULONG),
    )

class MaxSizeResponse(NDRCALL):
    structure = (

    )
        

class MaxFolderCount(NDRCALL):
    opnum = 8
    structure = (

    )

class MaxFolderCountResponse(NDRCALL):
    structure = (
		('PULMAXFOLDERCOUNT', ULONG),
    )
        

class MaxFolderCount(NDRCALL):
    opnum = 9
    structure = (
		('ULMAXFOLDERCOUNT', ULONG),
    )

class MaxFolderCountResponse(NDRCALL):
    structure = (

    )
        

class ResourcePolicy(NDRCALL):
    opnum = 10
    structure = (

    )

class ResourcePolicyResponse(NDRCALL):
    structure = (
		('PPOLICY', RESOURCEPOLICY),
    )
        

class ResourcePolicy(NDRCALL):
    opnum = 11
    structure = (
		('POLICY', RESOURCEPOLICY),
    )

class ResourcePolicyResponse(NDRCALL):
    structure = (

    )
        

class FolderActions(NDRCALL):
    opnum = 12
    structure = (

    )

class FolderActionsResponse(NDRCALL):
    structure = (
		('ACTIONS', IFOLDERACTIONCOLLECTION),
    )
        

class ReportSchema(NDRCALL):
    opnum = 13
    structure = (

    )

class ReportSchemaResponse(NDRCALL):
    structure = (
		('REPORTSCHEMA', BSTR),
    )
        

class ReportSchema(NDRCALL):
    opnum = 14
    structure = (
		('REPORTSCHEMA', BSTR),
    )

class ReportSchemaResponse(NDRCALL):
    structure = (

    )
        

class ReportFileName(NDRCALL):
    opnum = 15
    structure = (

    )

class ReportFileNameResponse(NDRCALL):
    structure = (
		('PBSTRFILENAME', BSTR),
    )
        

class ReportFileName(NDRCALL):
    opnum = 16
    structure = (
		('PBSTRFILENAME', BSTR),
    )

class ReportFileNameResponse(NDRCALL):
    structure = (

    )
        

class RuleTargetFileName(NDRCALL):
    opnum = 17
    structure = (

    )

class RuleTargetFileNameResponse(NDRCALL):
    structure = (
		('FILENAME', BSTR),
    )
        

class RuleTargetFileName(NDRCALL):
    opnum = 18
    structure = (
		('FILENAME', BSTR),
    )

class RuleTargetFileNameResponse(NDRCALL):
    structure = (

    )
        

class EventsFileName(NDRCALL):
    opnum = 19
    structure = (

    )

class EventsFileNameResponse(NDRCALL):
    structure = (
		('PBSTRFILENAME', BSTR),
    )
        

class EventsFileName(NDRCALL):
    opnum = 20
    structure = (
		('PBSTRFILENAME', BSTR),
    )

class EventsFileNameResponse(NDRCALL):
    structure = (

    )
        

class Rules(NDRCALL):
    opnum = 21
    structure = (

    )

class RulesResponse(NDRCALL):
    structure = (
		('PBSTRXML', BSTR),
    )
        

class Rules(NDRCALL):
    opnum = 22
    structure = (
		('BSTRXML', BSTR),
    )

class RulesResponse(NDRCALL):
    structure = (

    )
        

class Run(NDRCALL):
    opnum = 23
    structure = (
		('STEPS', DATAMANAGERSTEPS),
		('BSTRFOLDER', BSTR),
    )

class RunResponse(NDRCALL):
    structure = (
		('ERRORS', IVALUEMAP),
    )
        

class Extract(NDRCALL):
    opnum = 24
    structure = (
		('CABFILENAME', BSTR),
		('DESTINATIONPATH', BSTR),
    )

class ExtractResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Enabled,EnabledResponse),
1 : (CheckBeforeRunning,CheckBeforeRunningResponse),
2 : (MinFreeDisk,MinFreeDiskResponse),
3 : (MaxSize,MaxSizeResponse),
4 : (MaxFolderCount,MaxFolderCountResponse),
5 : (ResourcePolicy,ResourcePolicyResponse),
6 : (FolderActions,FolderActionsResponse),
7 : (ReportSchema,ReportSchemaResponse),
8 : (ReportFileName,ReportFileNameResponse),
9 : (RuleTargetFileName,RuleTargetFileNameResponse),
10 : (EventsFileName,EventsFileNameResponse),
11 : (Rules,RulesResponse),
12 : (Run,RunResponse),
13 : (Extract,ExtractResponse),
}

#################################################################################

#IFolderAction Definition

#################################################################################

MSRPC_UUID_IFOLDERACTION = uuidtup_to_bin(('03837543-098b-11d8-9414-505054503030','0.0'))


class Age(NDRCALL):
    opnum = 0
    structure = (

    )

class AgeResponse(NDRCALL):
    structure = (
		('PULAGE', ULONG),
    )
        

class Age(NDRCALL):
    opnum = 1
    structure = (
		('ULAGE', ULONG),
    )

class AgeResponse(NDRCALL):
    structure = (

    )
        

class Size(NDRCALL):
    opnum = 2
    structure = (

    )

class SizeResponse(NDRCALL):
    structure = (
		('PULAGE', ULONG),
    )
        

class Size(NDRCALL):
    opnum = 3
    structure = (
		('ULAGE', ULONG),
    )

class SizeResponse(NDRCALL):
    structure = (

    )
        

class Actions(NDRCALL):
    opnum = 4
    structure = (

    )

class ActionsResponse(NDRCALL):
    structure = (
		('STEPS', FOLDERACTIONSTEPS),
    )
        

class Actions(NDRCALL):
    opnum = 5
    structure = (
		('STEPS', FOLDERACTIONSTEPS),
    )

class ActionsResponse(NDRCALL):
    structure = (

    )
        

class SendCabTo(NDRCALL):
    opnum = 6
    structure = (

    )

class SendCabToResponse(NDRCALL):
    structure = (
		('PBSTRDESTINATION', BSTR),
    )
        

class SendCabTo(NDRCALL):
    opnum = 7
    structure = (
		('BSTRDESTINATION', BSTR),
    )

class SendCabToResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Age,AgeResponse),
1 : (Size,SizeResponse),
2 : (Actions,ActionsResponse),
3 : (SendCabTo,SendCabToResponse),
}

#################################################################################

#IFolderActionCollection Definition

#################################################################################

MSRPC_UUID_IFOLDERACTIONCOLLECTION = uuidtup_to_bin(('03837544-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('COUNT', ULONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('ACTION', IFOLDERACTION),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('ENUM', IUNKNOWN),
    )
        

class Add(NDRCALL):
    opnum = 3
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 4
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 5
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 6
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class CreateFolderAction(NDRCALL):
    opnum = 7
    structure = (

    )

class CreateFolderActionResponse(NDRCALL):
    structure = (
		('FOLDERACTION', IFOLDERACTION),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Add,AddResponse),
4 : (Remove,RemoveResponse),
5 : (Clear,ClearResponse),
6 : (AddRange,AddRangeResponse),
7 : (CreateFolderAction,CreateFolderActionResponse),
}

#################################################################################

#IDataCollector Definition

#################################################################################

MSRPC_UUID_IDATACOLLECTOR = uuidtup_to_bin(('038374ff-098b-11d8-9414-505054503030','0.0'))


class DataCollectorSet(NDRCALL):
    opnum = 0
    structure = (

    )

class DataCollectorSetResponse(NDRCALL):
    structure = (
		('GROUP', IDATACOLLECTORSET),
    )
        

class Opnum8NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum8NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class DataCollectorType(NDRCALL):
    opnum = 2
    structure = (

    )

class DataCollectorTypeResponse(NDRCALL):
    structure = (
		('TYPE', DATACOLLECTORTYPE),
    )
        

class FileName(NDRCALL):
    opnum = 3
    structure = (

    )

class FileNameResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class FileName(NDRCALL):
    opnum = 4
    structure = (
		('NAME', BSTR),
    )

class FileNameResponse(NDRCALL):
    structure = (

    )
        

class FileNameFormat(NDRCALL):
    opnum = 5
    structure = (

    )

class FileNameFormatResponse(NDRCALL):
    structure = (
		('FORMAT', AUTOPATHFORMAT),
    )
        

class FileNameFormat(NDRCALL):
    opnum = 6
    structure = (
		('FORMAT', AUTOPATHFORMAT),
    )

class FileNameFormatResponse(NDRCALL):
    structure = (

    )
        

class FileNameFormatPattern(NDRCALL):
    opnum = 7
    structure = (

    )

class FileNameFormatPatternResponse(NDRCALL):
    structure = (
		('PATTERN', BSTR),
    )
        

class FileNameFormatPattern(NDRCALL):
    opnum = 8
    structure = (
		('PATTERN', BSTR),
    )

class FileNameFormatPatternResponse(NDRCALL):
    structure = (

    )
        

class LatestOutputLocation(NDRCALL):
    opnum = 9
    structure = (

    )

class LatestOutputLocationResponse(NDRCALL):
    structure = (
		('PATH', BSTR),
    )
        

class LatestOutputLocation(NDRCALL):
    opnum = 10
    structure = (
		('PATH', BSTR),
    )

class LatestOutputLocationResponse(NDRCALL):
    structure = (

    )
        

class LogAppend(NDRCALL):
    opnum = 11
    structure = (

    )

class LogAppendResponse(NDRCALL):
    structure = (
		('APPEND', VARIANT_BOOL),
    )
        

class LogAppend(NDRCALL):
    opnum = 12
    structure = (
		('APPEND', VARIANT_BOOL),
    )

class LogAppendResponse(NDRCALL):
    structure = (

    )
        

class LogCircular(NDRCALL):
    opnum = 13
    structure = (

    )

class LogCircularResponse(NDRCALL):
    structure = (
		('CIRCULAR', VARIANT_BOOL),
    )
        

class LogCircular(NDRCALL):
    opnum = 14
    structure = (
		('CIRCULAR', VARIANT_BOOL),
    )

class LogCircularResponse(NDRCALL):
    structure = (

    )
        

class LogOverwrite(NDRCALL):
    opnum = 15
    structure = (

    )

class LogOverwriteResponse(NDRCALL):
    structure = (
		('OVERWRITE', VARIANT_BOOL),
    )
        

class LogOverwrite(NDRCALL):
    opnum = 16
    structure = (
		('OVERWRITE', VARIANT_BOOL),
    )

class LogOverwriteResponse(NDRCALL):
    structure = (

    )
        

class Name(NDRCALL):
    opnum = 17
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class Name(NDRCALL):
    opnum = 18
    structure = (
		('NAME', BSTR),
    )

class NameResponse(NDRCALL):
    structure = (

    )
        

class OutputLocation(NDRCALL):
    opnum = 19
    structure = (

    )

class OutputLocationResponse(NDRCALL):
    structure = (
		('PATH', BSTR),
    )
        

class Index(NDRCALL):
    opnum = 20
    structure = (

    )

class IndexResponse(NDRCALL):
    structure = (
		('INDEX', LONG),
    )
        

class Opnum28NotUsedOnWire(NDRCALL):
    opnum = 21
    structure = (

    )

class Opnum28NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Xml(NDRCALL):
    opnum = 22
    structure = (

    )

class XmlResponse(NDRCALL):
    structure = (
		('XML', BSTR),
    )
        

class SetXml(NDRCALL):
    opnum = 23
    structure = (
		('XML', BSTR),
    )

class SetXmlResponse(NDRCALL):
    structure = (
		('VALIDATION', IVALUEMAP),
    )
        

class Opnum31NotUsedOnWire(NDRCALL):
    opnum = 24
    structure = (

    )

class Opnum31NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (DataCollectorSet,DataCollectorSetResponse),
1 : (Opnum8NotUsedOnWire,Opnum8NotUsedOnWireResponse),
2 : (DataCollectorType,DataCollectorTypeResponse),
3 : (FileName,FileNameResponse),
4 : (FileNameFormat,FileNameFormatResponse),
5 : (FileNameFormatPattern,FileNameFormatPatternResponse),
6 : (LatestOutputLocation,LatestOutputLocationResponse),
7 : (LogAppend,LogAppendResponse),
8 : (LogCircular,LogCircularResponse),
9 : (LogOverwrite,LogOverwriteResponse),
10 : (Name,NameResponse),
11 : (OutputLocation,OutputLocationResponse),
12 : (Index,IndexResponse),
13 : (Opnum28NotUsedOnWire,Opnum28NotUsedOnWireResponse),
14 : (Xml,XmlResponse),
15 : (SetXml,SetXmlResponse),
16 : (Opnum31NotUsedOnWire,Opnum31NotUsedOnWireResponse),
}

#################################################################################

#IPerformanceCounterDataCollector Definition

#################################################################################

MSRPC_UUID_IPERFORMANCECOUNTERDATACOLLECTOR = uuidtup_to_bin(('03837506-098b-11d8-9414-505054503030','0.0'))


class DataSourceName(NDRCALL):
    opnum = 0
    structure = (

    )

class DataSourceNameResponse(NDRCALL):
    structure = (
		('DSN', BSTR),
    )
        

class DataSourceName(NDRCALL):
    opnum = 1
    structure = (
		('DSN', BSTR),
    )

class DataSourceNameResponse(NDRCALL):
    structure = (

    )
        

class PerformanceCounters(NDRCALL):
    opnum = 2
    structure = (

    )

class PerformanceCountersResponse(NDRCALL):
    structure = (
		('COUNTERS', SAFEARRAY ( BSTR )),
    )
        

class PerformanceCounters(NDRCALL):
    opnum = 3
    structure = (
		('COUNTERS', SAFEARRAY ( BSTR )),
    )

class PerformanceCountersResponse(NDRCALL):
    structure = (

    )
        

class LogFileFormat(NDRCALL):
    opnum = 4
    structure = (

    )

class LogFileFormatResponse(NDRCALL):
    structure = (
		('FORMAT', FILEFORMAT),
    )
        

class LogFileFormat(NDRCALL):
    opnum = 5
    structure = (
		('FORMAT', FILEFORMAT),
    )

class LogFileFormatResponse(NDRCALL):
    structure = (

    )
        

class SampleInterval(NDRCALL):
    opnum = 6
    structure = (

    )

class SampleIntervalResponse(NDRCALL):
    structure = (
		('INTERVAL', UNSIGNED_LONG),
    )
        

class SampleInterval(NDRCALL):
    opnum = 7
    structure = (
		('INTERVAL', UNSIGNED_LONG),
    )

class SampleIntervalResponse(NDRCALL):
    structure = (

    )
        

class SegmentMaxRecords(NDRCALL):
    opnum = 8
    structure = (

    )

class SegmentMaxRecordsResponse(NDRCALL):
    structure = (
		('RECORDS', UNSIGNED_LONG),
    )
        

class SegmentMaxRecords(NDRCALL):
    opnum = 9
    structure = (
		('RECORDS', UNSIGNED_LONG),
    )

class SegmentMaxRecordsResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (DataSourceName,DataSourceNameResponse),
1 : (PerformanceCounters,PerformanceCountersResponse),
2 : (LogFileFormat,LogFileFormatResponse),
3 : (SampleInterval,SampleIntervalResponse),
4 : (SegmentMaxRecords,SegmentMaxRecordsResponse),
}

#################################################################################

#IConfigurationDataCollector Definition

#################################################################################

MSRPC_UUID_ICONFIGURATIONDATACOLLECTOR = uuidtup_to_bin(('03837514-098b-11d8-9414-505054503030','0.0'))


class FileMaxCount(NDRCALL):
    opnum = 0
    structure = (

    )

class FileMaxCountResponse(NDRCALL):
    structure = (
		('COUNT', UNSIGNED_LONG),
    )
        

class FileMaxCount(NDRCALL):
    opnum = 1
    structure = (
		('COUNT', UNSIGNED_LONG),
    )

class FileMaxCountResponse(NDRCALL):
    structure = (

    )
        

class FileMaxRecursiveDepth(NDRCALL):
    opnum = 2
    structure = (

    )

class FileMaxRecursiveDepthResponse(NDRCALL):
    structure = (
		('DEPTH', UNSIGNED_LONG),
    )
        

class FileMaxRecursiveDepth(NDRCALL):
    opnum = 3
    structure = (
		('DEPTH', UNSIGNED_LONG),
    )

class FileMaxRecursiveDepthResponse(NDRCALL):
    structure = (

    )
        

class FileMaxTotalSize(NDRCALL):
    opnum = 4
    structure = (

    )

class FileMaxTotalSizeResponse(NDRCALL):
    structure = (
		('SIZE', UNSIGNED_LONG),
    )
        

class FileMaxTotalSize(NDRCALL):
    opnum = 5
    structure = (
		('SIZE', UNSIGNED_LONG),
    )

class FileMaxTotalSizeResponse(NDRCALL):
    structure = (

    )
        

class Files(NDRCALL):
    opnum = 6
    structure = (

    )

class FilesResponse(NDRCALL):
    structure = (
		('FILES', SAFEARRAY ( BSTR )),
    )
        

class Files(NDRCALL):
    opnum = 7
    structure = (
		('FILES', SAFEARRAY ( BSTR )),
    )

class FilesResponse(NDRCALL):
    structure = (

    )
        

class ManagementQueries(NDRCALL):
    opnum = 8
    structure = (

    )

class ManagementQueriesResponse(NDRCALL):
    structure = (
		('QUERIES', SAFEARRAY ( BSTR )),
    )
        

class ManagementQueries(NDRCALL):
    opnum = 9
    structure = (
		('QUERIES', SAFEARRAY ( BSTR )),
    )

class ManagementQueriesResponse(NDRCALL):
    structure = (

    )
        

class QueryNetworkAdapters(NDRCALL):
    opnum = 10
    structure = (

    )

class QueryNetworkAdaptersResponse(NDRCALL):
    structure = (
		('NETWORK', VARIANT_BOOL),
    )
        

class QueryNetworkAdapters(NDRCALL):
    opnum = 11
    structure = (
		('NETWORK', VARIANT_BOOL),
    )

class QueryNetworkAdaptersResponse(NDRCALL):
    structure = (

    )
        

class RegistryKeys(NDRCALL):
    opnum = 12
    structure = (

    )

class RegistryKeysResponse(NDRCALL):
    structure = (
		('QUERY', SAFEARRAY ( BSTR )),
    )
        

class RegistryKeys(NDRCALL):
    opnum = 13
    structure = (
		('QUERY', SAFEARRAY ( BSTR )),
    )

class RegistryKeysResponse(NDRCALL):
    structure = (

    )
        

class RegistryMaxRecursiveDepth(NDRCALL):
    opnum = 14
    structure = (

    )

class RegistryMaxRecursiveDepthResponse(NDRCALL):
    structure = (
		('DEPTH', UNSIGNED_LONG),
    )
        

class RegistryMaxRecursiveDepth(NDRCALL):
    opnum = 15
    structure = (
		('DEPTH', UNSIGNED_LONG),
    )

class RegistryMaxRecursiveDepthResponse(NDRCALL):
    structure = (

    )
        

class SystemStateFile(NDRCALL):
    opnum = 16
    structure = (

    )

class SystemStateFileResponse(NDRCALL):
    structure = (
		('FILENAME', BSTR),
    )
        

class SystemStateFile(NDRCALL):
    opnum = 17
    structure = (
		('FILENAME', BSTR),
    )

class SystemStateFileResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (FileMaxCount,FileMaxCountResponse),
1 : (FileMaxRecursiveDepth,FileMaxRecursiveDepthResponse),
2 : (FileMaxTotalSize,FileMaxTotalSizeResponse),
3 : (Files,FilesResponse),
4 : (ManagementQueries,ManagementQueriesResponse),
5 : (QueryNetworkAdapters,QueryNetworkAdaptersResponse),
6 : (RegistryKeys,RegistryKeysResponse),
7 : (RegistryMaxRecursiveDepth,RegistryMaxRecursiveDepthResponse),
8 : (SystemStateFile,SystemStateFileResponse),
}

#################################################################################

#IAlertDataCollector Definition

#################################################################################

MSRPC_UUID_IALERTDATACOLLECTOR = uuidtup_to_bin(('03837516-098b-11d8-9414-505054503030','0.0'))


class AlertThresholds(NDRCALL):
    opnum = 0
    structure = (

    )

class AlertThresholdsResponse(NDRCALL):
    structure = (
		('ALERTS', SAFEARRAY ( BSTR )),
    )
        

class AlertThresholds(NDRCALL):
    opnum = 1
    structure = (
		('ALERTS', SAFEARRAY ( BSTR )),
    )

class AlertThresholdsResponse(NDRCALL):
    structure = (

    )
        

class EventLog(NDRCALL):
    opnum = 2
    structure = (

    )

class EventLogResponse(NDRCALL):
    structure = (
		('LOG', VARIANT_BOOL),
    )
        

class EventLog(NDRCALL):
    opnum = 3
    structure = (
		('LOG', VARIANT_BOOL),
    )

class EventLogResponse(NDRCALL):
    structure = (

    )
        

class SampleInterval(NDRCALL):
    opnum = 4
    structure = (

    )

class SampleIntervalResponse(NDRCALL):
    structure = (
		('INTERVAL', UNSIGNED_LONG),
    )
        

class SampleInterval(NDRCALL):
    opnum = 5
    structure = (
		('INTERVAL', UNSIGNED_LONG),
    )

class SampleIntervalResponse(NDRCALL):
    structure = (

    )
        

class Task(NDRCALL):
    opnum = 6
    structure = (

    )

class TaskResponse(NDRCALL):
    structure = (
		('TASK', BSTR),
    )
        

class Task(NDRCALL):
    opnum = 7
    structure = (
		('TASK', BSTR),
    )

class TaskResponse(NDRCALL):
    structure = (

    )
        

class TaskRunAsSelf(NDRCALL):
    opnum = 8
    structure = (

    )

class TaskRunAsSelfResponse(NDRCALL):
    structure = (
		('RUNASSELF', VARIANT_BOOL),
    )
        

class TaskRunAsSelf(NDRCALL):
    opnum = 9
    structure = (
		('RUNASSELF', VARIANT_BOOL),
    )

class TaskRunAsSelfResponse(NDRCALL):
    structure = (

    )
        

class TaskArguments(NDRCALL):
    opnum = 10
    structure = (

    )

class TaskArgumentsResponse(NDRCALL):
    structure = (
		('TASK', BSTR),
    )
        

class TaskArguments(NDRCALL):
    opnum = 11
    structure = (
		('TASK', BSTR),
    )

class TaskArgumentsResponse(NDRCALL):
    structure = (

    )
        

class TaskUserTextArguments(NDRCALL):
    opnum = 12
    structure = (

    )

class TaskUserTextArgumentsResponse(NDRCALL):
    structure = (
		('TASK', BSTR),
    )
        

class TaskUserTextArguments(NDRCALL):
    opnum = 13
    structure = (
		('TASK', BSTR),
    )

class TaskUserTextArgumentsResponse(NDRCALL):
    structure = (

    )
        

class TriggerDataCollectorSet(NDRCALL):
    opnum = 14
    structure = (

    )

class TriggerDataCollectorSetResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class TriggerDataCollectorSet(NDRCALL):
    opnum = 15
    structure = (
		('NAME', BSTR),
    )

class TriggerDataCollectorSetResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (AlertThresholds,AlertThresholdsResponse),
1 : (EventLog,EventLogResponse),
2 : (SampleInterval,SampleIntervalResponse),
3 : (Task,TaskResponse),
4 : (TaskRunAsSelf,TaskRunAsSelfResponse),
5 : (TaskArguments,TaskArgumentsResponse),
6 : (TaskUserTextArguments,TaskUserTextArgumentsResponse),
7 : (TriggerDataCollectorSet,TriggerDataCollectorSetResponse),
}

#################################################################################

#ITraceDataCollector Definition

#################################################################################

MSRPC_UUID_ITRACEDATACOLLECTOR = uuidtup_to_bin(('0383750b-098b-11d8-9414-505054503030','0.0'))


class BufferSize(NDRCALL):
    opnum = 0
    structure = (

    )

class BufferSizeResponse(NDRCALL):
    structure = (
		('SIZE', UNSIGNED_LONG),
    )
        

class BufferSize(NDRCALL):
    opnum = 1
    structure = (
		('SIZE', UNSIGNED_LONG),
    )

class BufferSizeResponse(NDRCALL):
    structure = (

    )
        

class BuffersLost(NDRCALL):
    opnum = 2
    structure = (

    )

class BuffersLostResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class Opnum35NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum35NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class BuffersWritten(NDRCALL):
    opnum = 4
    structure = (

    )

class BuffersWrittenResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class Opnum37NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum37NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class ClockType(NDRCALL):
    opnum = 6
    structure = (

    )

class ClockTypeResponse(NDRCALL):
    structure = (
		('CLOCK', CLOCKTYPE),
    )
        

class ClockType(NDRCALL):
    opnum = 7
    structure = (
		('CLOCK', CLOCKTYPE),
    )

class ClockTypeResponse(NDRCALL):
    structure = (

    )
        

class EventsLost(NDRCALL):
    opnum = 8
    structure = (

    )

class EventsLostResponse(NDRCALL):
    structure = (
		('EVENTS', UNSIGNED_LONG),
    )
        

class Opnum41NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum41NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class ExtendedModes(NDRCALL):
    opnum = 10
    structure = (

    )

class ExtendedModesResponse(NDRCALL):
    structure = (
		('MODE', UNSIGNED_LONG),
    )
        

class ExtendedModes(NDRCALL):
    opnum = 11
    structure = (
		('MODE', UNSIGNED_LONG),
    )

class ExtendedModesResponse(NDRCALL):
    structure = (

    )
        

class FlushTimer(NDRCALL):
    opnum = 12
    structure = (

    )

class FlushTimerResponse(NDRCALL):
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )
        

class FlushTimer(NDRCALL):
    opnum = 13
    structure = (
		('SECONDS', UNSIGNED_LONG),
    )

class FlushTimerResponse(NDRCALL):
    structure = (

    )
        

class FreeBuffers(NDRCALL):
    opnum = 14
    structure = (

    )

class FreeBuffersResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class Opnum47NotUsedOnWire(NDRCALL):
    opnum = 15
    structure = (

    )

class Opnum47NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Guid(NDRCALL):
    opnum = 16
    structure = (

    )

class GuidResponse(NDRCALL):
    structure = (
		('GUID', GUID),
    )
        

class Guid(NDRCALL):
    opnum = 17
    structure = (
		('GUID', GUID),
    )

class GuidResponse(NDRCALL):
    structure = (

    )
        

class IsKernelTrace(NDRCALL):
    opnum = 18
    structure = (

    )

class IsKernelTraceResponse(NDRCALL):
    structure = (
		('KERNEL', VARIANT_BOOL),
    )
        

class MaximumBuffers(NDRCALL):
    opnum = 19
    structure = (

    )

class MaximumBuffersResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class MaximumBuffers(NDRCALL):
    opnum = 20
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )

class MaximumBuffersResponse(NDRCALL):
    structure = (

    )
        

class MinimumBuffers(NDRCALL):
    opnum = 21
    structure = (

    )

class MinimumBuffersResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class MinimumBuffers(NDRCALL):
    opnum = 22
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )

class MinimumBuffersResponse(NDRCALL):
    structure = (

    )
        

class NumberOfBuffers(NDRCALL):
    opnum = 23
    structure = (

    )

class NumberOfBuffersResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class NumberOfBuffers(NDRCALL):
    opnum = 24
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )

class NumberOfBuffersResponse(NDRCALL):
    structure = (

    )
        

class PreallocateFile(NDRCALL):
    opnum = 25
    structure = (

    )

class PreallocateFileResponse(NDRCALL):
    structure = (
		('ALLOCATE', VARIANT_BOOL),
    )
        

class PreallocateFile(NDRCALL):
    opnum = 26
    structure = (
		('ALLOCATE', VARIANT_BOOL),
    )

class PreallocateFileResponse(NDRCALL):
    structure = (

    )
        

class ProcessMode(NDRCALL):
    opnum = 27
    structure = (

    )

class ProcessModeResponse(NDRCALL):
    structure = (
		('PROCESS', VARIANT_BOOL),
    )
        

class ProcessMode(NDRCALL):
    opnum = 28
    structure = (
		('PROCESS', VARIANT_BOOL),
    )

class ProcessModeResponse(NDRCALL):
    structure = (

    )
        

class RealTimeBuffersLost(NDRCALL):
    opnum = 29
    structure = (

    )

class RealTimeBuffersLostResponse(NDRCALL):
    structure = (
		('BUFFERS', UNSIGNED_LONG),
    )
        

class Opnum62NotUsedOnWire(NDRCALL):
    opnum = 30
    structure = (

    )

class Opnum62NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class SessionId(NDRCALL):
    opnum = 31
    structure = (

    )

class SessionIdResponse(NDRCALL):
    structure = (
		('ID', ULONG64),
    )
        

class Opnum64NotUsedOnWire(NDRCALL):
    opnum = 32
    structure = (

    )

class Opnum64NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class SessionName(NDRCALL):
    opnum = 33
    structure = (

    )

class SessionNameResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class SessionName(NDRCALL):
    opnum = 34
    structure = (
		('NAME', BSTR),
    )

class SessionNameResponse(NDRCALL):
    structure = (

    )
        

class SessionThreadId(NDRCALL):
    opnum = 35
    structure = (

    )

class SessionThreadIdResponse(NDRCALL):
    structure = (
		('TID', UNSIGNED_LONG),
    )
        

class Opnum68NotUsedOnWire(NDRCALL):
    opnum = 36
    structure = (

    )

class Opnum68NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class StreamMode(NDRCALL):
    opnum = 37
    structure = (

    )

class StreamModeResponse(NDRCALL):
    structure = (
		('MODE', STREAMMODE),
    )
        

class StreamMode(NDRCALL):
    opnum = 38
    structure = (
		('MODE', STREAMMODE),
    )

class StreamModeResponse(NDRCALL):
    structure = (

    )
        

class TraceDataProviders(NDRCALL):
    opnum = 39
    structure = (

    )

class TraceDataProvidersResponse(NDRCALL):
    structure = (
		('PROVIDERS', ITRACEDATAPROVIDERCOLLECTION),
    )
        
OPNUMS = {
0 : (BufferSize,BufferSizeResponse),
1 : (BuffersLost,BuffersLostResponse),
2 : (Opnum35NotUsedOnWire,Opnum35NotUsedOnWireResponse),
3 : (BuffersWritten,BuffersWrittenResponse),
4 : (Opnum37NotUsedOnWire,Opnum37NotUsedOnWireResponse),
5 : (ClockType,ClockTypeResponse),
6 : (EventsLost,EventsLostResponse),
7 : (Opnum41NotUsedOnWire,Opnum41NotUsedOnWireResponse),
8 : (ExtendedModes,ExtendedModesResponse),
9 : (FlushTimer,FlushTimerResponse),
10 : (FreeBuffers,FreeBuffersResponse),
11 : (Opnum47NotUsedOnWire,Opnum47NotUsedOnWireResponse),
12 : (Guid,GuidResponse),
13 : (IsKernelTrace,IsKernelTraceResponse),
14 : (MaximumBuffers,MaximumBuffersResponse),
15 : (MinimumBuffers,MinimumBuffersResponse),
16 : (NumberOfBuffers,NumberOfBuffersResponse),
17 : (PreallocateFile,PreallocateFileResponse),
18 : (ProcessMode,ProcessModeResponse),
19 : (RealTimeBuffersLost,RealTimeBuffersLostResponse),
20 : (Opnum62NotUsedOnWire,Opnum62NotUsedOnWireResponse),
21 : (SessionId,SessionIdResponse),
22 : (Opnum64NotUsedOnWire,Opnum64NotUsedOnWireResponse),
23 : (SessionName,SessionNameResponse),
24 : (SessionThreadId,SessionThreadIdResponse),
25 : (Opnum68NotUsedOnWire,Opnum68NotUsedOnWireResponse),
26 : (StreamMode,StreamModeResponse),
27 : (TraceDataProviders,TraceDataProvidersResponse),
}

#################################################################################

#IApiTracingDataCollector Definition

#################################################################################

MSRPC_UUID_IAPITRACINGDATACOLLECTOR = uuidtup_to_bin(('0383751a-098b-11d8-9414-505054503030','0.0'))


class LogApiNamesOnly(NDRCALL):
    opnum = 0
    structure = (

    )

class LogApiNamesOnlyResponse(NDRCALL):
    structure = (
		('LOGAPINAMES', VARIANT_BOOL),
    )
        

class LogApiNamesOnly(NDRCALL):
    opnum = 1
    structure = (
		('LOGAPINAMES', VARIANT_BOOL),
    )

class LogApiNamesOnlyResponse(NDRCALL):
    structure = (

    )
        

class LogApisRecursively(NDRCALL):
    opnum = 2
    structure = (

    )

class LogApisRecursivelyResponse(NDRCALL):
    structure = (
		('LOGRECURSIVELY', VARIANT_BOOL),
    )
        

class LogApisRecursively(NDRCALL):
    opnum = 3
    structure = (
		('LOGRECURSIVELY', VARIANT_BOOL),
    )

class LogApisRecursivelyResponse(NDRCALL):
    structure = (

    )
        

class ExePath(NDRCALL):
    opnum = 4
    structure = (

    )

class ExePathResponse(NDRCALL):
    structure = (
		('EXEPATH', BSTR),
    )
        

class ExePath(NDRCALL):
    opnum = 5
    structure = (
		('EXEPATH', BSTR),
    )

class ExePathResponse(NDRCALL):
    structure = (

    )
        

class LogFilePath(NDRCALL):
    opnum = 6
    structure = (

    )

class LogFilePathResponse(NDRCALL):
    structure = (
		('LOGFILEPATH', BSTR),
    )
        

class LogFilePath(NDRCALL):
    opnum = 7
    structure = (
		('LOGFILEPATH', BSTR),
    )

class LogFilePathResponse(NDRCALL):
    structure = (

    )
        

class IncludeModules(NDRCALL):
    opnum = 8
    structure = (

    )

class IncludeModulesResponse(NDRCALL):
    structure = (
		('INCLUDEMODULES', SAFEARRAY ( BSTR )),
    )
        

class IncludeModules(NDRCALL):
    opnum = 9
    structure = (
		('INCLUDEMODULES', SAFEARRAY ( BSTR )),
    )

class IncludeModulesResponse(NDRCALL):
    structure = (

    )
        

class IncludeApis(NDRCALL):
    opnum = 10
    structure = (

    )

class IncludeApisResponse(NDRCALL):
    structure = (
		('INCLUDEAPIS', SAFEARRAY ( BSTR )),
    )
        

class IncludeApis(NDRCALL):
    opnum = 11
    structure = (
		('INCLUDEAPIS', SAFEARRAY ( BSTR )),
    )

class IncludeApisResponse(NDRCALL):
    structure = (

    )
        

class ExcludeApis(NDRCALL):
    opnum = 12
    structure = (

    )

class ExcludeApisResponse(NDRCALL):
    structure = (
		('EXCLUDEAPIS', SAFEARRAY ( BSTR )),
    )
        

class ExcludeApis(NDRCALL):
    opnum = 13
    structure = (
		('EXCLUDEAPIS', SAFEARRAY ( BSTR )),
    )

class ExcludeApisResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (LogApiNamesOnly,LogApiNamesOnlyResponse),
1 : (LogApisRecursively,LogApisRecursivelyResponse),
2 : (ExePath,ExePathResponse),
3 : (LogFilePath,LogFilePathResponse),
4 : (IncludeModules,IncludeModulesResponse),
5 : (IncludeApis,IncludeApisResponse),
6 : (ExcludeApis,ExcludeApisResponse),
}

#################################################################################

#ITraceDataProvider Definition

#################################################################################

MSRPC_UUID_ITRACEDATAPROVIDER = uuidtup_to_bin(('03837512-098b-11d8-9414-505054503030','0.0'))


class DisplayName(NDRCALL):
    opnum = 0
    structure = (

    )

class DisplayNameResponse(NDRCALL):
    structure = (
		('NAME', BSTR),
    )
        

class DisplayName(NDRCALL):
    opnum = 1
    structure = (
		('NAME', BSTR),
    )

class DisplayNameResponse(NDRCALL):
    structure = (

    )
        

class Guid(NDRCALL):
    opnum = 2
    structure = (

    )

class GuidResponse(NDRCALL):
    structure = (
		('GUID', GUID),
    )
        

class Guid(NDRCALL):
    opnum = 3
    structure = (
		('GUID', GUID),
    )

class GuidResponse(NDRCALL):
    structure = (

    )
        

class Level(NDRCALL):
    opnum = 4
    structure = (

    )

class LevelResponse(NDRCALL):
    structure = (
		('PPLEVEL', IVALUEMAP),
    )
        

class KeywordsAny(NDRCALL):
    opnum = 5
    structure = (

    )

class KeywordsAnyResponse(NDRCALL):
    structure = (
		('PPKEYWORDS', IVALUEMAP),
    )
        

class KeywordsAll(NDRCALL):
    opnum = 6
    structure = (

    )

class KeywordsAllResponse(NDRCALL):
    structure = (
		('PPKEYWORDS', IVALUEMAP),
    )
        

class Properties(NDRCALL):
    opnum = 7
    structure = (

    )

class PropertiesResponse(NDRCALL):
    structure = (
		('PPPROPERTIES', IVALUEMAP),
    )
        

class FilterEnabled(NDRCALL):
    opnum = 8
    structure = (

    )

class FilterEnabledResponse(NDRCALL):
    structure = (
		('FILTERENABLED', VARIANT_BOOL),
    )
        

class FilterEnabled(NDRCALL):
    opnum = 9
    structure = (
		('FILTERENABLED', VARIANT_BOOL),
    )

class FilterEnabledResponse(NDRCALL):
    structure = (

    )
        

class FilterType(NDRCALL):
    opnum = 10
    structure = (

    )

class FilterTypeResponse(NDRCALL):
    structure = (
		('PULTYPE', ULONG),
    )
        

class FilterType(NDRCALL):
    opnum = 11
    structure = (
		('ULTYPE', ULONG),
    )

class FilterTypeResponse(NDRCALL):
    structure = (

    )
        

class FilterData(NDRCALL):
    opnum = 12
    structure = (

    )

class FilterDataResponse(NDRCALL):
    structure = (
		('PPDATA', SAFEARRAY ( BYTE )),
    )
        

class FilterData(NDRCALL):
    opnum = 13
    structure = (
		('PDATA', SAFEARRAY ( BYTE )),
    )

class FilterDataResponse(NDRCALL):
    structure = (

    )
        

class Query(NDRCALL):
    opnum = 14
    structure = (
		('BSTRNAME', BSTR),
		('BSTRSERVER', BSTR),
    )

class QueryResponse(NDRCALL):
    structure = (

    )
        

class Resolve(NDRCALL):
    opnum = 15
    structure = (
		('PFROM', IDISPATCH),
    )

class ResolveResponse(NDRCALL):
    structure = (

    )
        

class SetSecurity(NDRCALL):
    opnum = 16
    structure = (
		('SDDL', BSTR),
    )

class SetSecurityResponse(NDRCALL):
    structure = (

    )
        

class GetSecurity(NDRCALL):
    opnum = 17
    structure = (
		('SECURITYINFO', ULONG),
    )

class GetSecurityResponse(NDRCALL):
    structure = (
		('SDDL', BSTR),
    )
        

class GetRegisteredProcesses(NDRCALL):
    opnum = 18
    structure = (

    )

class GetRegisteredProcessesResponse(NDRCALL):
    structure = (
		('PROCESSES', IVALUEMAP),
    )
        
OPNUMS = {
0 : (DisplayName,DisplayNameResponse),
1 : (Guid,GuidResponse),
2 : (Level,LevelResponse),
3 : (KeywordsAny,KeywordsAnyResponse),
4 : (KeywordsAll,KeywordsAllResponse),
5 : (Properties,PropertiesResponse),
6 : (FilterEnabled,FilterEnabledResponse),
7 : (FilterType,FilterTypeResponse),
8 : (FilterData,FilterDataResponse),
9 : (Query,QueryResponse),
10 : (Resolve,ResolveResponse),
11 : (SetSecurity,SetSecurityResponse),
12 : (GetSecurity,GetSecurityResponse),
13 : (GetRegisteredProcesses,GetRegisteredProcessesResponse),
}

#################################################################################

#ISchedule Definition

#################################################################################

MSRPC_UUID_ISCHEDULE = uuidtup_to_bin(('0383753a-098b-11d8-9414-505054503030','0.0'))


class StartDate(NDRCALL):
    opnum = 0
    structure = (

    )

class StartDateResponse(NDRCALL):
    structure = (
		('START', VARIANT),
    )
        

class StartDate(NDRCALL):
    opnum = 1
    structure = (
		('START', VARIANT),
    )

class StartDateResponse(NDRCALL):
    structure = (

    )
        

class EndDate(NDRCALL):
    opnum = 2
    structure = (

    )

class EndDateResponse(NDRCALL):
    structure = (
		('END', VARIANT),
    )
        

class EndDate(NDRCALL):
    opnum = 3
    structure = (
		('END', VARIANT),
    )

class EndDateResponse(NDRCALL):
    structure = (

    )
        

class StartTime(NDRCALL):
    opnum = 4
    structure = (

    )

class StartTimeResponse(NDRCALL):
    structure = (
		('START', VARIANT),
    )
        

class StartTime(NDRCALL):
    opnum = 5
    structure = (
		('START', VARIANT),
    )

class StartTimeResponse(NDRCALL):
    structure = (

    )
        

class Days(NDRCALL):
    opnum = 6
    structure = (

    )

class DaysResponse(NDRCALL):
    structure = (
		('DAYS', WEEKDAYS),
    )
        

class Days(NDRCALL):
    opnum = 7
    structure = (
		('DAYS', WEEKDAYS),
    )

class DaysResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (StartDate,StartDateResponse),
1 : (EndDate,EndDateResponse),
2 : (StartTime,StartTimeResponse),
3 : (Days,DaysResponse),
}

#################################################################################

#ITraceDataProviderCollection Definition

#################################################################################

MSRPC_UUID_ITRACEDATAPROVIDERCOLLECTION = uuidtup_to_bin(('03837510-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('RETVAL', LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('PPPROVIDER', ITRACEDATAPROVIDER),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('RETVAL', IUNKNOWN),
    )
        

class Add(NDRCALL):
    opnum = 3
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 4
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 5
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 6
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class CreateTraceDataProvider(NDRCALL):
    opnum = 7
    structure = (

    )

class CreateTraceDataProviderResponse(NDRCALL):
    structure = (
		('PROVIDER', ITRACEDATAPROVIDER),
    )
        

class GetTraceDataProviders(NDRCALL):
    opnum = 8
    structure = (
		('SERVER', BSTR),
    )

class GetTraceDataProvidersResponse(NDRCALL):
    structure = (

    )
        

class GetTraceDataProvidersByProcess(NDRCALL):
    opnum = 9
    structure = (
		('SERVER', BSTR),
		('PID', ULONG),
    )

class GetTraceDataProvidersByProcessResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Add,AddResponse),
4 : (Remove,RemoveResponse),
5 : (Clear,ClearResponse),
6 : (AddRange,AddRangeResponse),
7 : (CreateTraceDataProvider,CreateTraceDataProviderResponse),
8 : (GetTraceDataProviders,GetTraceDataProvidersResponse),
9 : (GetTraceDataProvidersByProcess,GetTraceDataProvidersByProcessResponse),
}

#################################################################################

#IScheduleCollection Definition

#################################################################################

MSRPC_UUID_ISCHEDULECOLLECTION = uuidtup_to_bin(('0383753d-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('RETVAL', LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('PPSCHEDULE', ISCHEDULE),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('RETVAL', IUNKNOWN),
    )
        

class Add(NDRCALL):
    opnum = 3
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 4
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 5
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 6
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class CreateSchedule(NDRCALL):
    opnum = 7
    structure = (

    )

class CreateScheduleResponse(NDRCALL):
    structure = (
		('SCHEDULE', ISCHEDULE),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Add,AddResponse),
4 : (Remove,RemoveResponse),
5 : (Clear,ClearResponse),
6 : (AddRange,AddRangeResponse),
7 : (CreateSchedule,CreateScheduleResponse),
}

#################################################################################

#IDataCollectorCollection Definition

#################################################################################

MSRPC_UUID_IDATACOLLECTORCOLLECTION = uuidtup_to_bin(('03837502-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('RETVAL', LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('COLLECTOR', IDATACOLLECTOR),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('RETVAL', IUNKNOWN),
    )
        

class Add(NDRCALL):
    opnum = 3
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 4
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 5
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 6
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class CreateDataCollectorFromXml(NDRCALL):
    opnum = 7
    structure = (
		('BSTRXML', BSTR),
    )

class CreateDataCollectorFromXmlResponse(NDRCALL):
    structure = (
		('PVALIDATION', IVALUEMAP),
		('PCOLLECTOR', IDATACOLLECTOR),
    )
        

class CreateDataCollector(NDRCALL):
    opnum = 8
    structure = (
		('TYPE', DATACOLLECTORTYPE),
    )

class CreateDataCollectorResponse(NDRCALL):
    structure = (
		('COLLECTOR', IDATACOLLECTOR),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Add,AddResponse),
4 : (Remove,RemoveResponse),
5 : (Clear,ClearResponse),
6 : (AddRange,AddRangeResponse),
7 : (CreateDataCollectorFromXml,CreateDataCollectorFromXmlResponse),
8 : (CreateDataCollector,CreateDataCollectorResponse),
}

#################################################################################

#IDataCollectorSetCollection Definition

#################################################################################

MSRPC_UUID_IDATACOLLECTORSETCOLLECTION = uuidtup_to_bin(('03837524-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('RETVAL', LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('SET', IDATACOLLECTORSET),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('RETVAL', IUNKNOWN),
    )
        

class Add(NDRCALL):
    opnum = 3
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 4
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 5
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 6
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class GetDataCollectorSets(NDRCALL):
    opnum = 7
    structure = (
		('SERVER', BSTR),
		('FILTER', BSTR),
    )

class GetDataCollectorSetsResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Add,AddResponse),
4 : (Remove,RemoveResponse),
5 : (Clear,ClearResponse),
6 : (AddRange,AddRangeResponse),
7 : (GetDataCollectorSets,GetDataCollectorSetsResponse),
}

#################################################################################

#IValueMapItem Definition

#################################################################################

MSRPC_UUID_IVALUEMAPITEM = uuidtup_to_bin(('03837533-098b-11d8-9414-505054503030','0.0'))


class Description(NDRCALL):
    opnum = 0
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('DESCRIPTION', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 1
    structure = (
		('DESCRIPTION', BSTR),
    )

class DescriptionResponse(NDRCALL):
    structure = (

    )
        

class Enabled(NDRCALL):
    opnum = 2
    structure = (

    )

class EnabledResponse(NDRCALL):
    structure = (
		('ENABLED', VARIANT_BOOL),
    )
        

class Enabled(NDRCALL):
    opnum = 3
    structure = (
		('ENABLED', VARIANT_BOOL),
    )

class EnabledResponse(NDRCALL):
    structure = (

    )
        

class Key(NDRCALL):
    opnum = 4
    structure = (

    )

class KeyResponse(NDRCALL):
    structure = (
		('KEY', BSTR),
    )
        

class Key(NDRCALL):
    opnum = 5
    structure = (
		('KEY', BSTR),
    )

class KeyResponse(NDRCALL):
    structure = (

    )
        

class Value(NDRCALL):
    opnum = 6
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('VALUE', VARIANT),
    )
        

class Value(NDRCALL):
    opnum = 7
    structure = (
		('VALUE', VARIANT),
    )

class ValueResponse(NDRCALL):
    structure = (

    )
        

class ValueMapType(NDRCALL):
    opnum = 8
    structure = (

    )

class ValueMapTypeResponse(NDRCALL):
    structure = (
		('TYPE', VALUEMAPTYPE),
    )
        

class ValueMapType(NDRCALL):
    opnum = 9
    structure = (
		('TYPE', VALUEMAPTYPE),
    )

class ValueMapTypeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Description,DescriptionResponse),
1 : (Enabled,EnabledResponse),
2 : (Key,KeyResponse),
3 : (Value,ValueResponse),
4 : (ValueMapType,ValueMapTypeResponse),
}

#################################################################################

#IValueMap Definition

#################################################################################

MSRPC_UUID_IVALUEMAP = uuidtup_to_bin(('03837534-098b-11d8-9414-505054503030','0.0'))


class Count(NDRCALL):
    opnum = 0
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('RETVAL', LONG),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('INDEX', VARIANT),
    )

class ItemResponse(NDRCALL):
    structure = (
		('VALUE', IVALUEMAPITEM),
    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('RETVAL', IUNKNOWN),
    )
        

class Description(NDRCALL):
    opnum = 3
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('DESCRIPTION', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 4
    structure = (
		('DESCRIPTION', BSTR),
    )

class DescriptionResponse(NDRCALL):
    structure = (

    )
        

class Value(NDRCALL):
    opnum = 5
    structure = (

    )

class ValueResponse(NDRCALL):
    structure = (
		('VALUE', VARIANT),
    )
        

class Value(NDRCALL):
    opnum = 6
    structure = (
		('VALUE', VARIANT),
    )

class ValueResponse(NDRCALL):
    structure = (

    )
        

class ValueMapType(NDRCALL):
    opnum = 7
    structure = (

    )

class ValueMapTypeResponse(NDRCALL):
    structure = (
		('TYPE', VALUEMAPTYPE),
    )
        

class ValueMapType(NDRCALL):
    opnum = 8
    structure = (
		('TYPE', VALUEMAPTYPE),
    )

class ValueMapTypeResponse(NDRCALL):
    structure = (

    )
        

class Add(NDRCALL):
    opnum = 9
    structure = (

    )

class AddResponse(NDRCALL):
    structure = (

    )
        

class Remove(NDRCALL):
    opnum = 10
    structure = (

    )

class RemoveResponse(NDRCALL):
    structure = (

    )
        

class Clear(NDRCALL):
    opnum = 11
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class AddRange(NDRCALL):
    opnum = 12
    structure = (

    )

class AddRangeResponse(NDRCALL):
    structure = (

    )
        

class CreateValueMapItem(NDRCALL):
    opnum = 13
    structure = (

    )

class CreateValueMapItemResponse(NDRCALL):
    structure = (
		('ITEM', IVALUEMAPITEM),
    )
        
OPNUMS = {
0 : (Count,CountResponse),
1 : (Item,ItemResponse),
2 : (_NewEnum,_NewEnumResponse),
3 : (Description,DescriptionResponse),
4 : (Value,ValueResponse),
5 : (ValueMapType,ValueMapTypeResponse),
6 : (Add,AddResponse),
7 : (Remove,RemoveResponse),
8 : (Clear,ClearResponse),
9 : (AddRange,AddRangeResponse),
10 : (CreateValueMapItem,CreateValueMapItemResponse),
}

