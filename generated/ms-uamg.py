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
        

class ANONYMOUS29(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous29', ANONYMOUS29),
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


dpLow = 1,
dpNormal = 2,
dpHigh = 3,
dpExtraHigh = 4
        

asLetWindowsUpdateDecide = 0,
asAutoSelectIfDownloaded = 1,
asNeverAutoSelect = 2,
asAlwaysAutoSelect = 3
        

adLetWindowsUpdateDecide = 0,
adNeverAutoDownload = 1,
adAlwaysAutoDownload = 2
        

iiNormal = 0,
iiMinor = 1,
iiRequiresExclusiveHandling = 2
        

irbNeverReboots = 0,
irbAlwaysRequiresReboot = 1,
irbCanRequestReboot = 2
        

orcNotStarted = 0,
orcInProgress = 1,
orcSucceeded = 2,
orcSucceededWithErrors = 3,
orcFailed = 4,
orcAborted = 5
        

ssDefault = 0,
ssManagedServer = 1,
ssWindowsUpdate = 2,
ssOthers = 3
        

utSoftware = 1,
utDriver = 2
        

uoInstallation = 1,
uoUninstallation = 2
        

daNone = 0,
daInstallation = 1,
daUninstallation = 2,
daDetection = 3
        

uecGeneral = 1,
uecWindowsDriver = 2,
uecWindowsInstaller = 3
        

usrsNotRegistered = 1,
usrsRegistrationPending = 2,
usrsRegistered = 3
        

searchScopeDefault = 0,
searchScopeMachineOnly = 1,
searchScopeCurrentUserOnly = 2,
searchScopeMachineAndCurrentUser = 3,
searchScopeMachineAndAllUsers = 4,
searchScopeAllUsers = 5
        

asfAllowPendingRegistration = 1,
asfAllowOnlineRegistration = 2,
asfRegisterServiceWithAU = 4
        

usoNonVolatileService = 1
        
DECIMAL = DECIMAL
#################################################################################

#CONSTANTS

#################################################################################

IUPDATECOLLECTION = 
IUPDATE = 
IUPDATESERVICEMANAGER2 = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#ICategoryCollection Definition

#################################################################################

OPNUMS = {
}

#################################################################################

#IStringCollection Definition

#################################################################################

MSRPC_UUID_ISTRINGCOLLECTION = uuidtup_to_bin(('eff90582-2dc-480-a06d-603bc362c3','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('index', LONG),
		('value', BSTR),
    )

class ItemResponse(NDRCALL):
    structure = (

    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 3
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class ReadOnly(NDRCALL):
    opnum = 4
    structure = (

    )

class ReadOnlyResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Add(NDRCALL):
    opnum = 5
    structure = (
		('value', BSTR),
    )

class AddResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Clear(NDRCALL):
    opnum = 6
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class Copy(NDRCALL):
    opnum = 7
    structure = (

    )

class CopyResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class Insert(NDRCALL):
    opnum = 8
    structure = (
		('index', LONG),
		('value', BSTR),
    )

class InsertResponse(NDRCALL):
    structure = (

    )
        

class RemoveAt(NDRCALL):
    opnum = 9
    structure = (
		('index', LONG),
    )

class RemoveAtResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
3 : (ReadOnly,ReadOnlyResponse),
4 : (Add,AddResponse),
5 : (Clear,ClearResponse),
6 : (Copy,CopyResponse),
7 : (Insert,InsertResponse),
8 : (RemoveAt,RemoveAtResponse),
}

#################################################################################

#IWindowsUpdateAgentInfo Definition

#################################################################################

MSRPC_UUID_IWINDOWSUPDATEAGENTINFO = uuidtup_to_bin(('85713fa1-7796-4fa2-be3b-e2d6124dd373','0.0'))


class GetInfo(NDRCALL):
    opnum = 0
    structure = (
		('varInfoIdentifier', VARIANT),
    )

class GetInfoResponse(NDRCALL):
    structure = (
		('retval', VARIANT),
    )
        
OPNUMS = {
0 : (GetInfo,GetInfoResponse),
}

#################################################################################

#IAutomaticUpdatesResults Definition

#################################################################################

MSRPC_UUID_IAUTOMATICUPDATESRESULTS = uuidtup_to_bin(('E7A4D634-7942-4D9-A111-82228A33901','0.0'))


class LastSearchSuccessDate(NDRCALL):
    opnum = 0
    structure = (

    )

class LastSearchSuccessDateResponse(NDRCALL):
    structure = (
		('retval', VARIANT),
    )
        

class LastInstallationSuccessDate(NDRCALL):
    opnum = 1
    structure = (

    )

class LastInstallationSuccessDateResponse(NDRCALL):
    structure = (
		('retval', VARIANT),
    )
        
OPNUMS = {
0 : (LastSearchSuccessDate,LastSearchSuccessDateResponse),
1 : (LastInstallationSuccessDate,LastInstallationSuccessDateResponse),
}

#################################################################################

#IAutomaticUpdates Definition

#################################################################################

MSRPC_UUID_IAUTOMATICUPDATES = uuidtup_to_bin(('673425bf-c082-4c7c-bdfd-569464b8e0ce','0.0'))


class DetectNow(NDRCALL):
    opnum = 0
    structure = (

    )

class DetectNowResponse(NDRCALL):
    structure = (

    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum10NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum10NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum11NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum11NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum12NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum12NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum13NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum13NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum14NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum14NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (DetectNow,DetectNowResponse),
1 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
2 : (Opnum10NotUsedOnWire,Opnum10NotUsedOnWireResponse),
3 : (Opnum11NotUsedOnWire,Opnum11NotUsedOnWireResponse),
4 : (Opnum12NotUsedOnWire,Opnum12NotUsedOnWireResponse),
5 : (Opnum13NotUsedOnWire,Opnum13NotUsedOnWireResponse),
6 : (Opnum14NotUsedOnWire,Opnum14NotUsedOnWireResponse),
}

#################################################################################

#IAutomaticUpdates2 Definition

#################################################################################

MSRPC_UUID_IAUTOMATICUPDATES2 = uuidtup_to_bin(('4A2F5C31-CFD9-410E-B7FB-29A653973A0F','0.0'))


class Results(NDRCALL):
    opnum = 0
    structure = (

    )

class ResultsResponse(NDRCALL):
    structure = (
		('retval', IAUTOMATICUPDATESRESULTS),
    )
        
OPNUMS = {
0 : (Results,ResultsResponse),
}

#################################################################################

#IUpdateIdentity Definition

#################################################################################

MSRPC_UUID_IUPDATEIDENTITY = uuidtup_to_bin(('46297823-9940-4c09-aed9-cd3ea6d05968','0.0'))


class RevisionNumber(NDRCALL):
    opnum = 0
    structure = (

    )

class RevisionNumberResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class UpdateID(NDRCALL):
    opnum = 1
    structure = (

    )

class UpdateIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        
OPNUMS = {
0 : (RevisionNumber,RevisionNumberResponse),
1 : (UpdateID,UpdateIDResponse),
}

#################################################################################

#IImageInformation Definition

#################################################################################

MSRPC_UUID_IIMAGEINFORMATION = uuidtup_to_bin(('7c907864-346c-4aeb-8f3f-57da289f969f','0.0'))


class AltText(NDRCALL):
    opnum = 0
    structure = (

    )

class AltTextResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Height(NDRCALL):
    opnum = 1
    structure = (

    )

class HeightResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Source(NDRCALL):
    opnum = 2
    structure = (

    )

class SourceResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Width(NDRCALL):
    opnum = 3
    structure = (

    )

class WidthResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (AltText,AltTextResponse),
1 : (Height,HeightResponse),
2 : (Source,SourceResponse),
3 : (Width,WidthResponse),
}

#################################################################################

#ICategory Definition

#################################################################################

MSRPC_UUID_ICATEGORY = uuidtup_to_bin(('81ddc1b8-9d35-47a6-b471-5b80f519223b','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class CategoryID(NDRCALL):
    opnum = 1
    structure = (

    )

class CategoryIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Children(NDRCALL):
    opnum = 2
    structure = (

    )

class ChildrenResponse(NDRCALL):
    structure = (
		('retval', ICATEGORYCOLLECTION),
    )
        

class Description(NDRCALL):
    opnum = 3
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Image(NDRCALL):
    opnum = 4
    structure = (

    )

class ImageResponse(NDRCALL):
    structure = (
		('retval', IIMAGEINFORMATION),
    )
        

class Order(NDRCALL):
    opnum = 5
    structure = (

    )

class OrderResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Parent(NDRCALL):
    opnum = 6
    structure = (

    )

class ParentResponse(NDRCALL):
    structure = (
		('retval', ICATEGORY),
    )
        

class Type(NDRCALL):
    opnum = 7
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Updates(NDRCALL):
    opnum = 8
    structure = (

    )

class UpdatesResponse(NDRCALL):
    structure = (
		('retval', IUPDATECOLLECTION),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (CategoryID,CategoryIDResponse),
2 : (Children,ChildrenResponse),
3 : (Description,DescriptionResponse),
4 : (Image,ImageResponse),
5 : (Order,OrderResponse),
6 : (Parent,ParentResponse),
7 : (Type,TypeResponse),
8 : (Updates,UpdatesResponse),
}

#################################################################################

#ICategoryCollection Definition

#################################################################################

MSRPC_UUID_ICATEGORYCOLLECTION = uuidtup_to_bin(('3a56bfb8-576c-43f7-9335-fe4838fd7e37','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', ICATEGORY),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#IInstallationBehavior Definition

#################################################################################

MSRPC_UUID_IINSTALLATIONBEHAVIOR = uuidtup_to_bin(('d9a59339-e245-4bd-9686-4576339624','0.0'))


class CanRequestUserInput(NDRCALL):
    opnum = 0
    structure = (

    )

class CanRequestUserInputResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Impact(NDRCALL):
    opnum = 1
    structure = (

    )

class ImpactResponse(NDRCALL):
    structure = (
		('retval', INSTALLATIONIMPACT),
    )
        

class RebootBehavior(NDRCALL):
    opnum = 2
    structure = (

    )

class RebootBehaviorResponse(NDRCALL):
    structure = (
		('retval', INSTALLATIONREBOOTBEHAVIOR),
    )
        

class RequiresNetworkConnectivity(NDRCALL):
    opnum = 3
    structure = (

    )

class RequiresNetworkConnectivityResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (CanRequestUserInput,CanRequestUserInputResponse),
1 : (Impact,ImpactResponse),
2 : (RebootBehavior,RebootBehaviorResponse),
3 : (RequiresNetworkConnectivity,RequiresNetworkConnectivityResponse),
}

#################################################################################

#IUpdateDownloadContent Definition

#################################################################################

MSRPC_UUID_IUPDATEDOWNLOADCONTENT = uuidtup_to_bin(('54a2cb2d-9a0c-48b6-8a50-9abb69ee2d02','0.0'))


class DownloadUrl(NDRCALL):
    opnum = 0
    structure = (

    )

class DownloadUrlResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        
OPNUMS = {
0 : (DownloadUrl,DownloadUrlResponse),
}

#################################################################################

#IUpdateDownloadContent2 Definition

#################################################################################

MSRPC_UUID_IUPDATEDOWNLOADCONTENT2 = uuidtup_to_bin(('c97ad11b-f257-420-99-377733668','0.0'))


class IsDeltaCompressedContent(NDRCALL):
    opnum = 0
    structure = (

    )

class IsDeltaCompressedContentResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (IsDeltaCompressedContent,IsDeltaCompressedContentResponse),
}

#################################################################################

#IUpdateDownloadContentCollection Definition

#################################################################################

MSRPC_UUID_IUPDATEDOWNLOADCONTENTCOLLECTION = uuidtup_to_bin(('bc5513c8-b3b8-4f7-a4d4-3610888a','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IUPDATEDOWNLOADCONTENT),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#IUpdate Definition

#################################################################################

MSRPC_UUID_IUPDATE = uuidtup_to_bin(('6a92b07a-d821-4682-b423-5c805022cc4d','0.0'))


class Title(NDRCALL):
    opnum = 0
    structure = (

    )

class TitleResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class AutoSelectOnWebSites(NDRCALL):
    opnum = 1
    structure = (

    )

class AutoSelectOnWebSitesResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class BundledUpdates(NDRCALL):
    opnum = 2
    structure = (

    )

class BundledUpdatesResponse(NDRCALL):
    structure = (
		('retval', IUPDATECOLLECTION),
    )
        

class CanRequireSource(NDRCALL):
    opnum = 3
    structure = (

    )

class CanRequireSourceResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Categories(NDRCALL):
    opnum = 4
    structure = (

    )

class CategoriesResponse(NDRCALL):
    structure = (
		('retval', ICATEGORYCOLLECTION),
    )
        

class Deadline(NDRCALL):
    opnum = 5
    structure = (

    )

class DeadlineResponse(NDRCALL):
    structure = (
		('retval', VARIANT),
    )
        

class DeltaCompressedContentAvailable(NDRCALL):
    opnum = 6
    structure = (

    )

class DeltaCompressedContentAvailableResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class DeltaCompressedContentPreferred(NDRCALL):
    opnum = 7
    structure = (

    )

class DeltaCompressedContentPreferredResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Description(NDRCALL):
    opnum = 8
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class EulaAccepted(NDRCALL):
    opnum = 9
    structure = (

    )

class EulaAcceptedResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class EulaText(NDRCALL):
    opnum = 10
    structure = (

    )

class EulaTextResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class HandlerID(NDRCALL):
    opnum = 11
    structure = (

    )

class HandlerIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Identity(NDRCALL):
    opnum = 12
    structure = (

    )

class IdentityResponse(NDRCALL):
    structure = (
		('retval', IUPDATEIDENTITY),
    )
        

class Image(NDRCALL):
    opnum = 13
    structure = (

    )

class ImageResponse(NDRCALL):
    structure = (
		('retval', IIMAGEINFORMATION),
    )
        

class InstallationBehavior(NDRCALL):
    opnum = 14
    structure = (

    )

class InstallationBehaviorResponse(NDRCALL):
    structure = (
		('retval', IINSTALLATIONBEHAVIOR),
    )
        

class IsBeta(NDRCALL):
    opnum = 15
    structure = (

    )

class IsBetaResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsDownloaded(NDRCALL):
    opnum = 16
    structure = (

    )

class IsDownloadedResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsHidden(NDRCALL):
    opnum = 17
    structure = (

    )

class IsHiddenResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Opnum26NotUsedOnWire(NDRCALL):
    opnum = 18
    structure = (

    )

class Opnum26NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class IsInstalled(NDRCALL):
    opnum = 19
    structure = (

    )

class IsInstalledResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsMandatory(NDRCALL):
    opnum = 20
    structure = (

    )

class IsMandatoryResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsUninstallable(NDRCALL):
    opnum = 21
    structure = (

    )

class IsUninstallableResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Languages(NDRCALL):
    opnum = 22
    structure = (

    )

class LanguagesResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class LastDeploymentChangeTime(NDRCALL):
    opnum = 23
    structure = (

    )

class LastDeploymentChangeTimeResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class MaxDownloadSize(NDRCALL):
    opnum = 24
    structure = (

    )

class MaxDownloadSizeResponse(NDRCALL):
    structure = (
		('retval', DECIMAL),
    )
        

class MinDownloadSize(NDRCALL):
    opnum = 25
    structure = (

    )

class MinDownloadSizeResponse(NDRCALL):
    structure = (
		('retval', DECIMAL),
    )
        

class MoreInfoUrls(NDRCALL):
    opnum = 26
    structure = (

    )

class MoreInfoUrlsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class MsrcSeverity(NDRCALL):
    opnum = 27
    structure = (

    )

class MsrcSeverityResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class RecommendedCpuSpeed(NDRCALL):
    opnum = 28
    structure = (

    )

class RecommendedCpuSpeedResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class RecommendedHardDiskSpace(NDRCALL):
    opnum = 29
    structure = (

    )

class RecommendedHardDiskSpaceResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class RecommendedMemory(NDRCALL):
    opnum = 30
    structure = (

    )

class RecommendedMemoryResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class ReleaseNotes(NDRCALL):
    opnum = 31
    structure = (

    )

class ReleaseNotesResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class SecurityBulletinIDs(NDRCALL):
    opnum = 32
    structure = (

    )

class SecurityBulletinIDsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class SupersededUpdateIDs(NDRCALL):
    opnum = 33
    structure = (

    )

class SupersededUpdateIDsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class SupportUrl(NDRCALL):
    opnum = 34
    structure = (

    )

class SupportUrlResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Type(NDRCALL):
    opnum = 35
    structure = (

    )

class TypeResponse(NDRCALL):
    structure = (
		('retval', UPDATETYPE),
    )
        

class UninstallationNotes(NDRCALL):
    opnum = 36
    structure = (

    )

class UninstallationNotesResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class UninstallationBehavior(NDRCALL):
    opnum = 37
    structure = (

    )

class UninstallationBehaviorResponse(NDRCALL):
    structure = (
		('retval', IINSTALLATIONBEHAVIOR),
    )
        

class UninstallationSteps(NDRCALL):
    opnum = 38
    structure = (

    )

class UninstallationStepsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class KBArticleIDs(NDRCALL):
    opnum = 39
    structure = (

    )

class KBArticleIDsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class Opnum48NotUsedOnWire(NDRCALL):
    opnum = 40
    structure = (

    )

class Opnum48NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class DeploymentAction(NDRCALL):
    opnum = 41
    structure = (

    )

class DeploymentActionResponse(NDRCALL):
    structure = (
		('retval', DEPLOYMENTACTION),
    )
        

class Opnum50NotUsedOnWire(NDRCALL):
    opnum = 42
    structure = (

    )

class Opnum50NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class DownloadPriority(NDRCALL):
    opnum = 43
    structure = (

    )

class DownloadPriorityResponse(NDRCALL):
    structure = (
		('retval', DOWNLOADPRIORITY),
    )
        

class DownloadContents(NDRCALL):
    opnum = 44
    structure = (

    )

class DownloadContentsResponse(NDRCALL):
    structure = (
		('retval', IUPDATEDOWNLOADCONTENTCOLLECTION),
    )
        
OPNUMS = {
0 : (Title,TitleResponse),
1 : (AutoSelectOnWebSites,AutoSelectOnWebSitesResponse),
2 : (BundledUpdates,BundledUpdatesResponse),
3 : (CanRequireSource,CanRequireSourceResponse),
4 : (Categories,CategoriesResponse),
5 : (Deadline,DeadlineResponse),
6 : (DeltaCompressedContentAvailable,DeltaCompressedContentAvailableResponse),
7 : (DeltaCompressedContentPreferred,DeltaCompressedContentPreferredResponse),
8 : (Description,DescriptionResponse),
9 : (EulaAccepted,EulaAcceptedResponse),
10 : (EulaText,EulaTextResponse),
11 : (HandlerID,HandlerIDResponse),
12 : (Identity,IdentityResponse),
13 : (Image,ImageResponse),
14 : (InstallationBehavior,InstallationBehaviorResponse),
15 : (IsBeta,IsBetaResponse),
16 : (IsDownloaded,IsDownloadedResponse),
17 : (IsHidden,IsHiddenResponse),
18 : (Opnum26NotUsedOnWire,Opnum26NotUsedOnWireResponse),
19 : (IsInstalled,IsInstalledResponse),
20 : (IsMandatory,IsMandatoryResponse),
21 : (IsUninstallable,IsUninstallableResponse),
22 : (Languages,LanguagesResponse),
23 : (LastDeploymentChangeTime,LastDeploymentChangeTimeResponse),
24 : (MaxDownloadSize,MaxDownloadSizeResponse),
25 : (MinDownloadSize,MinDownloadSizeResponse),
26 : (MoreInfoUrls,MoreInfoUrlsResponse),
27 : (MsrcSeverity,MsrcSeverityResponse),
28 : (RecommendedCpuSpeed,RecommendedCpuSpeedResponse),
29 : (RecommendedHardDiskSpace,RecommendedHardDiskSpaceResponse),
30 : (RecommendedMemory,RecommendedMemoryResponse),
31 : (ReleaseNotes,ReleaseNotesResponse),
32 : (SecurityBulletinIDs,SecurityBulletinIDsResponse),
33 : (SupersededUpdateIDs,SupersededUpdateIDsResponse),
34 : (SupportUrl,SupportUrlResponse),
35 : (Type,TypeResponse),
36 : (UninstallationNotes,UninstallationNotesResponse),
37 : (UninstallationBehavior,UninstallationBehaviorResponse),
38 : (UninstallationSteps,UninstallationStepsResponse),
39 : (KBArticleIDs,KBArticleIDsResponse),
40 : (Opnum48NotUsedOnWire,Opnum48NotUsedOnWireResponse),
41 : (DeploymentAction,DeploymentActionResponse),
42 : (Opnum50NotUsedOnWire,Opnum50NotUsedOnWireResponse),
43 : (DownloadPriority,DownloadPriorityResponse),
44 : (DownloadContents,DownloadContentsResponse),
}

#################################################################################

#IWindowsDriverUpdate Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATE = uuidtup_to_bin(('b383cd1a-5e9-4504-963-7641236191','0.0'))


class DriverClass(NDRCALL):
    opnum = 0
    structure = (

    )

class DriverClassResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverHardwareID(NDRCALL):
    opnum = 1
    structure = (

    )

class DriverHardwareIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverManufacturer(NDRCALL):
    opnum = 2
    structure = (

    )

class DriverManufacturerResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverModel(NDRCALL):
    opnum = 3
    structure = (

    )

class DriverModelResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverProvider(NDRCALL):
    opnum = 4
    structure = (

    )

class DriverProviderResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverVerDate(NDRCALL):
    opnum = 5
    structure = (

    )

class DriverVerDateResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class DeviceProblemNumber(NDRCALL):
    opnum = 6
    structure = (

    )

class DeviceProblemNumberResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class DeviceStatus(NDRCALL):
    opnum = 7
    structure = (

    )

class DeviceStatusResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (DriverClass,DriverClassResponse),
1 : (DriverHardwareID,DriverHardwareIDResponse),
2 : (DriverManufacturer,DriverManufacturerResponse),
3 : (DriverModel,DriverModelResponse),
4 : (DriverProvider,DriverProviderResponse),
5 : (DriverVerDate,DriverVerDateResponse),
6 : (DeviceProblemNumber,DeviceProblemNumberResponse),
7 : (DeviceStatus,DeviceStatusResponse),
}

#################################################################################

#IUpdate2 Definition

#################################################################################

MSRPC_UUID_IUPDATE2 = uuidtup_to_bin(('144fe9b0-d23d-4a8b-8634-fb4457533b7a','0.0'))


class RebootRequired(NDRCALL):
    opnum = 0
    structure = (

    )

class RebootRequiredResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsPresent(NDRCALL):
    opnum = 1
    structure = (

    )

class IsPresentResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class CveIDs(NDRCALL):
    opnum = 2
    structure = (

    )

class CveIDsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class Opnum56NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum56NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RebootRequired,RebootRequiredResponse),
1 : (IsPresent,IsPresentResponse),
2 : (CveIDs,CveIDsResponse),
3 : (Opnum56NotUsedOnWire,Opnum56NotUsedOnWireResponse),
}

#################################################################################

#IUpdate3 Definition

#################################################################################

MSRPC_UUID_IUPDATE3 = uuidtup_to_bin(('112EDA6B-95B3-476F-9D90-AEE82C6B8181','0.0'))


class BrowseOnly(NDRCALL):
    opnum = 0
    structure = (

    )

class BrowseOnlyResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (BrowseOnly,BrowseOnlyResponse),
}

#################################################################################

#IUpdate4 Definition

#################################################################################

MSRPC_UUID_IUPDATE4 = uuidtup_to_bin(('27e94b0d-5139-49a2-9a61-93522dc54652','0.0'))


class PerUser(NDRCALL):
    opnum = 0
    structure = (

    )

class PerUserResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (PerUser,PerUserResponse),
}

#################################################################################

#IUpdate5 Definition

#################################################################################

MSRPC_UUID_IUPDATE5 = uuidtup_to_bin(('C1C2F21A-D2F4-4902-B5C6-808119890','0.0'))


class AutoSelection(NDRCALL):
    opnum = 0
    structure = (

    )

class AutoSelectionResponse(NDRCALL):
    structure = (
		('retval', AUTOSELECTIONMODE),
    )
        

class AutoDownload(NDRCALL):
    opnum = 1
    structure = (

    )

class AutoDownloadResponse(NDRCALL):
    structure = (
		('retval', AUTODOWNLOADMODE),
    )
        
OPNUMS = {
0 : (AutoSelection,AutoSelectionResponse),
1 : (AutoDownload,AutoDownloadResponse),
}

#################################################################################

#IWindowsDriverUpdateEntry Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATEENTRY = uuidtup_to_bin(('ED8BFE40-A60B-42a-9652-817FCFA23EC','0.0'))


class DriverClass(NDRCALL):
    opnum = 0
    structure = (

    )

class DriverClassResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverHardwareID(NDRCALL):
    opnum = 1
    structure = (

    )

class DriverHardwareIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverManufacturer(NDRCALL):
    opnum = 2
    structure = (

    )

class DriverManufacturerResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverModel(NDRCALL):
    opnum = 3
    structure = (

    )

class DriverModelResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverProvider(NDRCALL):
    opnum = 4
    structure = (

    )

class DriverProviderResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class DriverVerDate(NDRCALL):
    opnum = 5
    structure = (

    )

class DriverVerDateResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class DeviceProblemNumber(NDRCALL):
    opnum = 6
    structure = (

    )

class DeviceProblemNumberResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class DeviceStatus(NDRCALL):
    opnum = 7
    structure = (

    )

class DeviceStatusResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (DriverClass,DriverClassResponse),
1 : (DriverHardwareID,DriverHardwareIDResponse),
2 : (DriverManufacturer,DriverManufacturerResponse),
3 : (DriverModel,DriverModelResponse),
4 : (DriverProvider,DriverProviderResponse),
5 : (DriverVerDate,DriverVerDateResponse),
6 : (DeviceProblemNumber,DeviceProblemNumberResponse),
7 : (DeviceStatus,DeviceStatusResponse),
}

#################################################################################

#IWindowsDriverUpdateEntryCollection Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATEENTRYCOLLECTION = uuidtup_to_bin(('0D521700-A372-4bef-828B-3D00C10ADEBD','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IWINDOWSDRIVERUPDATEENTRY),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#IWindowsDriverUpdate2 Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATE2 = uuidtup_to_bin(('615c4269-7a48-43bd-96b7-bf6ca27d6c3e','0.0'))


class RebootRequired(NDRCALL):
    opnum = 0
    structure = (

    )

class RebootRequiredResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsPresent(NDRCALL):
    opnum = 1
    structure = (

    )

class IsPresentResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class CveIDs(NDRCALL):
    opnum = 2
    structure = (

    )

class CveIDsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class Opnum64NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum64NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RebootRequired,RebootRequiredResponse),
1 : (IsPresent,IsPresentResponse),
2 : (CveIDs,CveIDsResponse),
3 : (Opnum64NotUsedOnWire,Opnum64NotUsedOnWireResponse),
}

#################################################################################

#IWindowsDriverUpdate3 Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATE3 = uuidtup_to_bin(('49EBD502-4A96-41BD-9E3E-4C5057F4250C','0.0'))


class BrowseOnly(NDRCALL):
    opnum = 0
    structure = (

    )

class BrowseOnlyResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (BrowseOnly,BrowseOnlyResponse),
}

#################################################################################

#IWindowsDriverUpdate4 Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATE4 = uuidtup_to_bin(('004C6A2B-0C19-4c69-9F5C-A269B2560DB9','0.0'))


class WindowsDriverUpdateEntries(NDRCALL):
    opnum = 0
    structure = (

    )

class WindowsDriverUpdateEntriesResponse(NDRCALL):
    structure = (
		('retval', IWINDOWSDRIVERUPDATEENTRYCOLLECTION),
    )
        

class PerUser(NDRCALL):
    opnum = 1
    structure = (

    )

class PerUserResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (WindowsDriverUpdateEntries,WindowsDriverUpdateEntriesResponse),
1 : (PerUser,PerUserResponse),
}

#################################################################################

#IWindowsDriverUpdate5 Definition

#################################################################################

MSRPC_UUID_IWINDOWSDRIVERUPDATE5 = uuidtup_to_bin(('70CF5C82-8642-42bb-9DBC-0CFD263C6C4F','0.0'))


class AutoSelection(NDRCALL):
    opnum = 0
    structure = (

    )

class AutoSelectionResponse(NDRCALL):
    structure = (
		('retval', AUTOSELECTIONMODE),
    )
        

class AutoDownload(NDRCALL):
    opnum = 1
    structure = (

    )

class AutoDownloadResponse(NDRCALL):
    structure = (
		('retval', AUTODOWNLOADMODE),
    )
        
OPNUMS = {
0 : (AutoSelection,AutoSelectionResponse),
1 : (AutoDownload,AutoDownloadResponse),
}

#################################################################################

#IUpdateCollection Definition

#################################################################################

MSRPC_UUID_IUPDATECOLLECTION = uuidtup_to_bin(('07f7438c-7709-4ca5-b518-91279288134e','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IUPDATE),
    )
        

class Item(NDRCALL):
    opnum = 1
    structure = (
		('index', LONG),
		('value', IUPDATE),
    )

class ItemResponse(NDRCALL):
    structure = (

    )
        

class _NewEnum(NDRCALL):
    opnum = 2
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 3
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class ReadOnly(NDRCALL):
    opnum = 4
    structure = (

    )

class ReadOnlyResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Add(NDRCALL):
    opnum = 5
    structure = (
		('value', IUPDATE),
    )

class AddResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Clear(NDRCALL):
    opnum = 6
    structure = (

    )

class ClearResponse(NDRCALL):
    structure = (

    )
        

class Opnum15NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum15NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Insert(NDRCALL):
    opnum = 8
    structure = (
		('index', LONG),
		('value', IUPDATE),
    )

class InsertResponse(NDRCALL):
    structure = (

    )
        

class RemoveAt(NDRCALL):
    opnum = 9
    structure = (
		('index', LONG),
    )

class RemoveAtResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
3 : (ReadOnly,ReadOnlyResponse),
4 : (Add,AddResponse),
5 : (Clear,ClearResponse),
6 : (Opnum15NotUsedOnWire,Opnum15NotUsedOnWireResponse),
7 : (Insert,InsertResponse),
8 : (RemoveAt,RemoveAtResponse),
}

#################################################################################

#IUpdateException Definition

#################################################################################

MSRPC_UUID_IUPDATEEXCEPTION = uuidtup_to_bin(('a376dd5e-094-427-af7c-fed5b6e1c1d6','0.0'))


class Message(NDRCALL):
    opnum = 0
    structure = (

    )

class MessageResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class HResult(NDRCALL):
    opnum = 1
    structure = (

    )

class HResultResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Context(NDRCALL):
    opnum = 2
    structure = (

    )

class ContextResponse(NDRCALL):
    structure = (
		('retval', UPDATEEXCEPTIONCONTEXT),
    )
        
OPNUMS = {
0 : (Message,MessageResponse),
1 : (HResult,HResultResponse),
2 : (Context,ContextResponse),
}

#################################################################################

#IUpdateExceptionCollection Definition

#################################################################################

MSRPC_UUID_IUPDATEEXCEPTIONCOLLECTION = uuidtup_to_bin(('503626a3-8e14-4729-9355-0fe664bd2321','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IUPDATEEXCEPTION),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#ISearchResult Definition

#################################################################################

MSRPC_UUID_ISEARCHRESULT = uuidtup_to_bin(('d40cff62-e08c-4498-941-01250d33c','0.0'))


class ResultCode(NDRCALL):
    opnum = 0
    structure = (

    )

class ResultCodeResponse(NDRCALL):
    structure = (
		('retval', OPERATIONRESULTCODE),
    )
        

class RootCategories(NDRCALL):
    opnum = 1
    structure = (

    )

class RootCategoriesResponse(NDRCALL):
    structure = (
		('retval', ICATEGORYCOLLECTION),
    )
        

class Updates(NDRCALL):
    opnum = 2
    structure = (

    )

class UpdatesResponse(NDRCALL):
    structure = (
		('retval', IUPDATECOLLECTION),
    )
        

class Warnings(NDRCALL):
    opnum = 3
    structure = (

    )

class WarningsResponse(NDRCALL):
    structure = (
		('retval', IUPDATEEXCEPTIONCOLLECTION),
    )
        
OPNUMS = {
0 : (ResultCode,ResultCodeResponse),
1 : (RootCategories,RootCategoriesResponse),
2 : (Updates,UpdatesResponse),
3 : (Warnings,WarningsResponse),
}

#################################################################################

#IUpdateHistoryEntry Definition

#################################################################################

MSRPC_UUID_IUPDATEHISTORYENTRY = uuidtup_to_bin(('be56a644-af0e-40-a311-c1d8e695cbff','0.0'))


class Operation(NDRCALL):
    opnum = 0
    structure = (

    )

class OperationResponse(NDRCALL):
    structure = (
		('retval', UPDATEOPERATION),
    )
        

class ResultCode(NDRCALL):
    opnum = 1
    structure = (

    )

class ResultCodeResponse(NDRCALL):
    structure = (
		('retval', OPERATIONRESULTCODE),
    )
        

class HResult(NDRCALL):
    opnum = 2
    structure = (

    )

class HResultResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class Date(NDRCALL):
    opnum = 3
    structure = (

    )

class DateResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class UpdateIdentity(NDRCALL):
    opnum = 4
    structure = (

    )

class UpdateIdentityResponse(NDRCALL):
    structure = (
		('retval', IUPDATEIDENTITY),
    )
        

class Title(NDRCALL):
    opnum = 5
    structure = (

    )

class TitleResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class Description(NDRCALL):
    opnum = 6
    structure = (

    )

class DescriptionResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class UnmappedResultCode(NDRCALL):
    opnum = 7
    structure = (

    )

class UnmappedResultCodeResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class ClientApplicationID(NDRCALL):
    opnum = 8
    structure = (

    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ServerSelection(NDRCALL):
    opnum = 9
    structure = (

    )

class ServerSelectionResponse(NDRCALL):
    structure = (
		('retval', SERVERSELECTION),
    )
        

class ServiceID(NDRCALL):
    opnum = 10
    structure = (

    )

class ServiceIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class UninstallationSteps(NDRCALL):
    opnum = 11
    structure = (

    )

class UninstallationStepsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class UninstallationNotes(NDRCALL):
    opnum = 12
    structure = (

    )

class UninstallationNotesResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class SupportUrl(NDRCALL):
    opnum = 13
    structure = (

    )

class SupportUrlResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        
OPNUMS = {
0 : (Operation,OperationResponse),
1 : (ResultCode,ResultCodeResponse),
2 : (HResult,HResultResponse),
3 : (Date,DateResponse),
4 : (UpdateIdentity,UpdateIdentityResponse),
5 : (Title,TitleResponse),
6 : (Description,DescriptionResponse),
7 : (UnmappedResultCode,UnmappedResultCodeResponse),
8 : (ClientApplicationID,ClientApplicationIDResponse),
9 : (ServerSelection,ServerSelectionResponse),
10 : (ServiceID,ServiceIDResponse),
11 : (UninstallationSteps,UninstallationStepsResponse),
12 : (UninstallationNotes,UninstallationNotesResponse),
13 : (SupportUrl,SupportUrlResponse),
}

#################################################################################

#IUpdateHistoryEntry2 Definition

#################################################################################

MSRPC_UUID_IUPDATEHISTORYENTRY2 = uuidtup_to_bin(('c2bfb780-4539-4132-ab8c-08772013b6','0.0'))


class Categories(NDRCALL):
    opnum = 0
    structure = (

    )

class CategoriesResponse(NDRCALL):
    structure = (
		('retval', ICATEGORYCOLLECTION),
    )
        
OPNUMS = {
0 : (Categories,CategoriesResponse),
}

#################################################################################

#IUpdateHistoryEntryCollection Definition

#################################################################################

MSRPC_UUID_IUPDATEHISTORYENTRYCOLLECTION = uuidtup_to_bin(('a7f04f3c-a290-435-aadf-a116c3357a5c','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IUPDATEHISTORYENTRY),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#IUpdateSearcher Definition

#################################################################################

MSRPC_UUID_IUPDATESEARCHER = uuidtup_to_bin(('8f45abf1-f9ae-4b95-a933-f0f66e5056ea','0.0'))


class CanAutomaticallyUpgradeService(NDRCALL):
    opnum = 0
    structure = (

    )

class CanAutomaticallyUpgradeServiceResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class CanAutomaticallyUpgradeService(NDRCALL):
    opnum = 1
    structure = (
		('value', VARIANT_BOOL),
    )

class CanAutomaticallyUpgradeServiceResponse(NDRCALL):
    structure = (

    )
        

class ClientApplicationID(NDRCALL):
    opnum = 2
    structure = (

    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ClientApplicationID(NDRCALL):
    opnum = 3
    structure = (
		('value', BSTR),
    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (

    )
        

class IncludePotentiallySupersededUpdates(NDRCALL):
    opnum = 4
    structure = (

    )

class IncludePotentiallySupersededUpdatesResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IncludePotentiallySupersededUpdates(NDRCALL):
    opnum = 5
    structure = (
		('value', VARIANT_BOOL),
    )

class IncludePotentiallySupersededUpdatesResponse(NDRCALL):
    structure = (

    )
        

class ServerSelection(NDRCALL):
    opnum = 6
    structure = (

    )

class ServerSelectionResponse(NDRCALL):
    structure = (
		('retval', SERVERSELECTION),
    )
        

class ServerSelection(NDRCALL):
    opnum = 7
    structure = (
		('value', SERVERSELECTION),
    )

class ServerSelectionResponse(NDRCALL):
    structure = (

    )
        

class Opnum16NotUsedOnWire(NDRCALL):
    opnum = 8
    structure = (

    )

class Opnum16NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum17NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum17NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class EscapeString(NDRCALL):
    opnum = 10
    structure = (
		('unescaped', BSTR),
    )

class EscapeStringResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class QueryHistory(NDRCALL):
    opnum = 11
    structure = (
		('startIndex', LONG),
		('count', LONG),
    )

class QueryHistoryResponse(NDRCALL):
    structure = (
		('retval', IUPDATEHISTORYENTRYCOLLECTION),
    )
        

class Search(NDRCALL):
    opnum = 12
    structure = (
		('criteria', BSTR),
    )

class SearchResponse(NDRCALL):
    structure = (
		('retval', ISEARCHRESULT),
    )
        

class Online(NDRCALL):
    opnum = 13
    structure = (

    )

class OnlineResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Online(NDRCALL):
    opnum = 14
    structure = (
		('value', VARIANT_BOOL),
    )

class OnlineResponse(NDRCALL):
    structure = (

    )
        

class GetTotalHistoryCount(NDRCALL):
    opnum = 15
    structure = (

    )

class GetTotalHistoryCountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        

class ServiceID(NDRCALL):
    opnum = 16
    structure = (

    )

class ServiceIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ServiceID(NDRCALL):
    opnum = 17
    structure = (
		('value', BSTR),
    )

class ServiceIDResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (CanAutomaticallyUpgradeService,CanAutomaticallyUpgradeServiceResponse),
1 : (ClientApplicationID,ClientApplicationIDResponse),
2 : (IncludePotentiallySupersededUpdates,IncludePotentiallySupersededUpdatesResponse),
3 : (ServerSelection,ServerSelectionResponse),
4 : (Opnum16NotUsedOnWire,Opnum16NotUsedOnWireResponse),
5 : (Opnum17NotUsedOnWire,Opnum17NotUsedOnWireResponse),
6 : (EscapeString,EscapeStringResponse),
7 : (QueryHistory,QueryHistoryResponse),
8 : (Search,SearchResponse),
9 : (Online,OnlineResponse),
10 : (GetTotalHistoryCount,GetTotalHistoryCountResponse),
11 : (ServiceID,ServiceIDResponse),
}

#################################################################################

#IUpdateSearcher2 Definition

#################################################################################

MSRPC_UUID_IUPDATESEARCHER2 = uuidtup_to_bin(('4cbdcb2d-1589-4beb-bd1c-3e582ff0add0','0.0'))


class IgnoreDownloadPriority(NDRCALL):
    opnum = 0
    structure = (

    )

class IgnoreDownloadPriorityResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IgnoreDownloadPriority(NDRCALL):
    opnum = 1
    structure = (
		('value', VARIANT_BOOL),
    )

class IgnoreDownloadPriorityResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (IgnoreDownloadPriority,IgnoreDownloadPriorityResponse),
}

#################################################################################

#IUpdateSearcher3 Definition

#################################################################################

MSRPC_UUID_IUPDATESEARCHER3 = uuidtup_to_bin(('04C6895D-EAF2-4034-97F3-311DE9BE413A','0.0'))


class SearchScope(NDRCALL):
    opnum = 0
    structure = (

    )

class SearchScopeResponse(NDRCALL):
    structure = (
		('retval', SEARCHSCOPE),
    )
        

class SearchScope(NDRCALL):
    opnum = 1
    structure = (
		('value', SEARCHSCOPE),
    )

class SearchScopeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SearchScope,SearchScopeResponse),
}

#################################################################################

#IUpdateSession Definition

#################################################################################

MSRPC_UUID_IUPDATESESSION = uuidtup_to_bin(('816858a4-260d-4260-933a-2585f1abc76b','0.0'))


class ClientApplicationID(NDRCALL):
    opnum = 0
    structure = (

    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ClientApplicationID(NDRCALL):
    opnum = 1
    structure = (
		('value', BSTR),
    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (

    )
        

class ReadOnly(NDRCALL):
    opnum = 2
    structure = (

    )

class ReadOnlyResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Opnum11NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum11NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum12NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum12NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class CreateUpdateSearcher(NDRCALL):
    opnum = 5
    structure = (

    )

class CreateUpdateSearcherResponse(NDRCALL):
    structure = (
		('retval', IUPDATESEARCHER),
    )
        

class Opnum14NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum14NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum15NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum15NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ClientApplicationID,ClientApplicationIDResponse),
1 : (ReadOnly,ReadOnlyResponse),
2 : (Opnum11NotUsedOnWire,Opnum11NotUsedOnWireResponse),
3 : (Opnum12NotUsedOnWire,Opnum12NotUsedOnWireResponse),
4 : (CreateUpdateSearcher,CreateUpdateSearcherResponse),
5 : (Opnum14NotUsedOnWire,Opnum14NotUsedOnWireResponse),
6 : (Opnum15NotUsedOnWire,Opnum15NotUsedOnWireResponse),
}

#################################################################################

#IUpdateSession2 Definition

#################################################################################

MSRPC_UUID_IUPDATESESSION2 = uuidtup_to_bin(('91caf7b0-eb23-49ed-9937-c52d817f46f7','0.0'))


class UserLocale(NDRCALL):
    opnum = 0
    structure = (

    )

class UserLocaleResponse(NDRCALL):
    structure = (
		('retval', LCID),
    )
        

class UserLocale(NDRCALL):
    opnum = 1
    structure = (
		('lcid', LCID),
    )

class UserLocaleResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (UserLocale,UserLocaleResponse),
}

#################################################################################

#IUpdateSession3 Definition

#################################################################################

MSRPC_UUID_IUPDATESESSION3 = uuidtup_to_bin(('918EFD1E-B5D8-4c90-8540-AEB9BDC56F9D','0.0'))


class CreateUpdateServiceManager(NDRCALL):
    opnum = 0
    structure = (

    )

class CreateUpdateServiceManagerResponse(NDRCALL):
    structure = (
		('retval', IUPDATESERVICEMANAGER2),
    )
        

class QueryHistory(NDRCALL):
    opnum = 1
    structure = (
		('criteria', BSTR),
		('startIndex', LONG),
		('count', LONG),
    )

class QueryHistoryResponse(NDRCALL):
    structure = (
		('retval', IUPDATEHISTORYENTRYCOLLECTION),
    )
        
OPNUMS = {
0 : (CreateUpdateServiceManager,CreateUpdateServiceManagerResponse),
1 : (QueryHistory,QueryHistoryResponse),
}

#################################################################################

#IUpdateService Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICE = uuidtup_to_bin(('76b3b17e-aed6-4da5-85f0-83587f81abe3','0.0'))


class Name(NDRCALL):
    opnum = 0
    structure = (

    )

class NameResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ContentValidationCert(NDRCALL):
    opnum = 1
    structure = (

    )

class ContentValidationCertResponse(NDRCALL):
    structure = (
		('retval', VARIANT),
    )
        

class ExpirationDate(NDRCALL):
    opnum = 2
    structure = (

    )

class ExpirationDateResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class IsManaged(NDRCALL):
    opnum = 3
    structure = (

    )

class IsManagedResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IsRegisteredWithAU(NDRCALL):
    opnum = 4
    structure = (

    )

class IsRegisteredWithAUResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class IssueDate(NDRCALL):
    opnum = 5
    structure = (

    )

class IssueDateResponse(NDRCALL):
    structure = (
		('retval', DATE),
    )
        

class OffersWindowsUpdates(NDRCALL):
    opnum = 6
    structure = (

    )

class OffersWindowsUpdatesResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class RedirectUrls(NDRCALL):
    opnum = 7
    structure = (

    )

class RedirectUrlsResponse(NDRCALL):
    structure = (
		('retval', ISTRINGCOLLECTION),
    )
        

class ServiceID(NDRCALL):
    opnum = 8
    structure = (

    )

class ServiceIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class IsScanPackageService(NDRCALL):
    opnum = 9
    structure = (

    )

class IsScanPackageServiceResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class CanRegisterWithAU(NDRCALL):
    opnum = 10
    structure = (

    )

class CanRegisterWithAUResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class ServiceUrl(NDRCALL):
    opnum = 11
    structure = (

    )

class ServiceUrlResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class SetupPrefix(NDRCALL):
    opnum = 12
    structure = (

    )

class SetupPrefixResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        
OPNUMS = {
0 : (Name,NameResponse),
1 : (ContentValidationCert,ContentValidationCertResponse),
2 : (ExpirationDate,ExpirationDateResponse),
3 : (IsManaged,IsManagedResponse),
4 : (IsRegisteredWithAU,IsRegisteredWithAUResponse),
5 : (IssueDate,IssueDateResponse),
6 : (OffersWindowsUpdates,OffersWindowsUpdatesResponse),
7 : (RedirectUrls,RedirectUrlsResponse),
8 : (ServiceID,ServiceIDResponse),
9 : (IsScanPackageService,IsScanPackageServiceResponse),
10 : (CanRegisterWithAU,CanRegisterWithAUResponse),
11 : (ServiceUrl,ServiceUrlResponse),
12 : (SetupPrefix,SetupPrefixResponse),
}

#################################################################################

#IUpdateService2 Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICE2 = uuidtup_to_bin(('1518b460-6518-4172-940f-c75883b24ceb','0.0'))


class IsDefaultAUService(NDRCALL):
    opnum = 0
    structure = (

    )

class IsDefaultAUServiceResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        
OPNUMS = {
0 : (IsDefaultAUService,IsDefaultAUServiceResponse),
}

#################################################################################

#IUpdateServiceCollection Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICECOLLECTION = uuidtup_to_bin(('9b0353aa-0e52-44ff-b8b0-1f7fa0437f88','0.0'))


class Item(NDRCALL):
    opnum = 0
    structure = (
		('index', LONG),
    )

class ItemResponse(NDRCALL):
    structure = (
		('retval', IUPDATESERVICE),
    )
        

class _NewEnum(NDRCALL):
    opnum = 1
    structure = (

    )

class _NewEnumResponse(NDRCALL):
    structure = (
		('retval', IUNKNOWN),
    )
        

class Count(NDRCALL):
    opnum = 2
    structure = (

    )

class CountResponse(NDRCALL):
    structure = (
		('retval', LONG),
    )
        
OPNUMS = {
0 : (Item,ItemResponse),
1 : (_NewEnum,_NewEnumResponse),
2 : (Count,CountResponse),
}

#################################################################################

#IUpdateServiceRegistration Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICEREGISTRATION = uuidtup_to_bin(('dde02280-123-40-937-67476cb286','0.0'))


class RegistrationState(NDRCALL):
    opnum = 0
    structure = (

    )

class RegistrationStateResponse(NDRCALL):
    structure = (
		('retval', UPDATESERVICEREGISTRATIONSTATE),
    )
        

class ServiceID(NDRCALL):
    opnum = 1
    structure = (

    )

class ServiceIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class IsPendingRegistrationWithAU(NDRCALL):
    opnum = 2
    structure = (

    )

class IsPendingRegistrationWithAUResponse(NDRCALL):
    structure = (
		('retval', VARIANT_BOOL),
    )
        

class Service(NDRCALL):
    opnum = 3
    structure = (

    )

class ServiceResponse(NDRCALL):
    structure = (
		('retval', IUPDATESERVICE2),
    )
        
OPNUMS = {
0 : (RegistrationState,RegistrationStateResponse),
1 : (ServiceID,ServiceIDResponse),
2 : (IsPendingRegistrationWithAU,IsPendingRegistrationWithAUResponse),
3 : (Service,ServiceResponse),
}

#################################################################################

#IUpdateServiceManager Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICEMANAGER = uuidtup_to_bin(('23857e3c-02ba-44a3-9423-b1c900805f37','0.0'))


class Services(NDRCALL):
    opnum = 0
    structure = (

    )

class ServicesResponse(NDRCALL):
    structure = (
		('retval', IUPDATESERVICECOLLECTION),
    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RegisterServiceWithAU(NDRCALL):
    opnum = 2
    structure = (
		('serviceID', BSTR),
    )

class RegisterServiceWithAUResponse(NDRCALL):
    structure = (

    )
        

class RemoveService(NDRCALL):
    opnum = 3
    structure = (
		('serviceID', BSTR),
    )

class RemoveServiceResponse(NDRCALL):
    structure = (

    )
        

class Opnum12NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum12NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class AddScanPackageService(NDRCALL):
    opnum = 5
    structure = (
		('serviceName', BSTR),
		('scanFileLocation', BSTR),
		('flags', LONG),
    )

class AddScanPackageServiceResponse(NDRCALL):
    structure = (
		('ppService', IUPDATESERVICE),
    )
        

class SetOption(NDRCALL):
    opnum = 6
    structure = (
		('optionName', BSTR),
		('optionValue', VARIANT),
    )

class SetOptionResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Services,ServicesResponse),
1 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
2 : (RegisterServiceWithAU,RegisterServiceWithAUResponse),
3 : (RemoveService,RemoveServiceResponse),
4 : (Opnum12NotUsedOnWire,Opnum12NotUsedOnWireResponse),
5 : (AddScanPackageService,AddScanPackageServiceResponse),
6 : (SetOption,SetOptionResponse),
}

#################################################################################

#IUpdateServiceManager2 Definition

#################################################################################

MSRPC_UUID_IUPDATESERVICEMANAGER2 = uuidtup_to_bin(('0bb8531d-7e8d-424f-986c-a0b8f60a3e7b','0.0'))


class ClientApplicationID(NDRCALL):
    opnum = 0
    structure = (

    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (
		('retval', BSTR),
    )
        

class ClientApplicationID(NDRCALL):
    opnum = 1
    structure = (
		('value', BSTR),
    )

class ClientApplicationIDResponse(NDRCALL):
    structure = (

    )
        

class QueryServiceRegistration(NDRCALL):
    opnum = 2
    structure = (
		('serviceID', BSTR),
    )

class QueryServiceRegistrationResponse(NDRCALL):
    structure = (
		('retval', IUPDATESERVICEREGISTRATION),
    )
        

class AddService2(NDRCALL):
    opnum = 3
    structure = (
		('serviceID', BSTR),
		('flags', LONG),
		('authorizationCabPath', BSTR),
    )

class AddService2Response(NDRCALL):
    structure = (
		('retval', IUPDATESERVICEREGISTRATION),
    )
        
OPNUMS = {
0 : (ClientApplicationID,ClientApplicationIDResponse),
1 : (QueryServiceRegistration,QueryServiceRegistrationResponse),
2 : (AddService2,AddService2Response),
}

