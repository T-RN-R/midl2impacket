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
        

class ANONYMOUS28(NDRUNION):
    union = {
        SF_BSTR: ('BstrStr',SAFEARR_BSTR),SF_UNKNOWN: ('UnknownStr',SAFEARR_UNKNOWN),SF_DISPATCH: ('DispatchStr',SAFEARR_DISPATCH),SF_VARIANT: ('VariantStr',SAFEARR_VARIANT),SF_RECORD: ('RecordStr',SAFEARR_BRECORD),SF_HAVEIID: ('HaveIidStr',SAFEARR_HAVEIID),SF_I1: ('ByteStr',BYTE_SIZEDARR),SF_I2: ('WordStr',WORD_SIZEDARR),SF_I4: ('LongStr',DWORD_SIZEDARR),SF_I8: ('HyperStr',HYPER_SIZEDARR),
    }
        

class SAFEARRAYUNION(NDRSTRUCT):
    structure = (
        ('sfType', UNSIGNED_LONG),('Anonymous28', ANONYMOUS28),
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

REFGUID = GUID
HRESULT = LONG

WBEM_FLAG_DEEP = 0,
WBEM_FLAG_SHALLOW = 1,
WBEM_FLAG_PROTOTYPE = 2
        

WBEM_FLAG_CREATE_OR_UPDATE = 0,
WBEM_FLAG_UPDATE_ONLY = 1,
WBEM_FLAG_CREATE_ONLY = 2,
WBEM_FLAG_UPDATE_SAFE_MODE = 32,
WBEM_FLAG_UPDATE_FORCE_MODE = 64
        

WBEM_FLAG_CONNECT_REPOSITORY_ONLY = 64,
WBEM_FLAG_CONNECT_PROVIDERS = 256
        

WBEM_FLAG_RETURN_WBEM_COMPLETE = 0,
WBEM_FLAG_RETURN_IMMEDIATELY = 16,
WBEM_FLAG_FORWARD_ONLY = 32,
WBEM_FLAG_NO_ERROR_OBJECT = 64,
WBEM_FLAG_SEND_STATUS = 128,
WBEM_FLAG_ENSURE_LOCATABLE = 256,
WBEM_FLAG_DIRECT_READ = 512,
WBEM_MASK_RESERVED_FLAGS = 126976,
WBEM_FLAG_USE_AMENDED_QUALIFIERS = 131072,
WBEM_FLAG_STRONG_VALIDATION = 1048576
        

WBEM_STATUS_COMPLETE = 0,
WBEM_STATUS_REQUIREMENTS = 1,
WBEM_STATUS_PROGRESS = 2
        

WBEM_NO_WAIT = 0,
WBEM_INFINITE = 4294967295
        

WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN = 1
        

WBEM_S_NO_ERROR = 0,
WBEM_S_FALSE = 1,
WBEM_S_TIMEDOUT = 262148,
WBEM_S_NEW_STYLE = 262399,
WBEM_S_PARTIAL_RESULTS = 262160,
WBEM_E_FAILED = 2147749889,
WBEM_E_NOT_FOUND = 2147749890,
WBEM_E_ACCESS_DENIED = 2147749891,
WBEM_E_PROVIDER_FAILURE = 2147749892,
WBEM_E_TYPE_MISMATCH = 2147749893,
WBEM_E_OUT_OF_MEMORY = 2147749894,
WBEM_E_INVALID_CONTEXT = 2147749895,
WBEM_E_INVALID_PARAMETER = 2147749896,
WBEM_E_NOT_AVAILABLE = 2147749897,
WBEM_E_CRITICAL_ERROR = 2147749898,
WBEM_E_NOT_SUPPORTED = 2147749900,
WBEM_E_PROVIDER_NOT_FOUND = 2147749905,
WBEM_E_INVALID_PROVIDER_REGISTRATION = 2147749906,
WBEM_E_PROVIDER_LOAD_FAILURE = 2147749907,
WBEM_E_INITIALIZATION_FAILURE = 2147749908,
WBEM_E_TRANSPORT_FAILURE = 2147749909,
WBEM_E_INVALID_OPERATION = 2147749910,
WBEM_E_ALREADY_EXISTS = 2147749913,
WBEM_E_UNEXPECTED = 2147749917,
WBEM_E_INCOMPLETE_CLASS = 2147749920,
WBEM_E_SHUTTING_DOWN = 2147749939,
E_NOTIMPL = 2147500033,
WBEM_E_INVALID_SUPERCLASS = 2147749901,
WBEM_E_INVALID_NAMESPACE = 2147749902,
WBEM_E_INVALID_OBJECT = 2147749903,
WBEM_E_INVALID_CLASS = 2147749904,
WBEM_E_INVALID_QUERY = 2147749911,
WBEM_E_INVALID_QUERY_TYPE = 2147749912,
WBEM_E_PROVIDER_NOT_CAPABLE = 2147749924,
WBEM_E_CLASS_HAS_CHILDREN = 2147749925,
WBEM_E_CLASS_HAS_INSTANCES = 2147749926,
WBEM_E_ILLEGAL_NULL = 2147749928,
WBEM_E_INVALID_CIM_TYPE = 2147749933,
WBEM_E_INVALID_METHOD = 2147749934,
WBEM_E_INVALID_METHOD_PARAMETERS = 2147749935,
WBEM_E_INVALID_PROPERTY = 2147749937,
WBEM_E_CALL_CANCELLED = 2147749938,
WBEM_E_INVALID_OBJECT_PATH = 2147749946,
WBEM_E_OUT_OF_DISK_SPACE = 2147749947,
WBEM_E_UNSUPPORTED_PUT_EXTENSION = 2147749949,
WBEM_E_QUOTA_VIOLATION = 2147749996,
WBEM_E_SERVER_TOO_BUSY = 2147749957,
WBEM_E_METHOD_NOT_IMPLEMENTED = 2147749973,
WBEM_E_METHOD_DISABLED = 2147749974,
WBEM_E_UNPARSABLE_QUERY = 2147749976,
WBEM_E_NOT_EVENT_CLASS = 2147749977,
WBEM_E_MISSING_GROUP_WITHIN = 2147749978,
WBEM_E_MISSING_AGGREGATION_LIST = 2147749979,
WBEM_E_PROPERTY_NOT_AN_OBJECT = 2147749980,
WBEM_E_AGGREGATING_BY_OBJECT = 2147749981,
WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING = 2147749984,
WBEM_E_QUEUE_OVERFLOW = 2147749985,
WBEM_E_PRIVILEGE_NOT_HELD = 2147749986,
WBEM_E_INVALID_OPERATOR = 2147749987,
WBEM_E_CANNOT_BE_ABSTRACT = 2147749989,
WBEM_E_AMENDED_OBJECT = 2147749990,
WBEM_E_VETO_PUT = 2147750010,
WBEM_E_PROVIDER_SUSPENDED = 2147750017,
WBEM_E_ENCRYPTED_CONNECTION_REQUIRED = 2147750023,
WBEM_E_PROVIDER_TIMED_OUT = 2147750024,
WBEM_E_NO_KEY = 2147750025,
WBEM_E_PROVIDER_DISABLED = 2147750026,
WBEM_E_REGISTRATION_TOO_BROAD = 2147753985,
WBEM_E_REGISTRATION_TOO_PRECISE = 2147753986
        

WBEM_REFRESHER_VERSION = 2
        

WBEM_BLOB_TYPE_ALL = 2,
WBEM_BLOB_TYPE_ERROR = 3,
WBEM_BLOB_TYPE_ENUM = 4
        

class DATA_WBEM_REFRESHED_OBJECT(NDRUniConformantArray):
    item = BYTE

class PTR_WBEM_REFRESHED_OBJECT(NDRPOINTER):
    referent = (
        ('Data', DATA_WBEM_REFRESHED_OBJECT),
    )

class WBEM_REFRESHED_OBJECT(NDRSTRUCT):
    structure = (
	('m_lRequestId', LONG),	('m_lBlobType', WBEM_INSTANCE_BLOB_TYPE),	('m_lBlobLength', LONG),	('m_pbBlob', PTR_WBEM_REFRESHED_OBJECT),

    )
        

class _WBEM_REFRESH_INFO_REMOTE(NDRSTRUCT):
    structure = (
        ('m_pRefresher', IWBEMREMOTEREFRESHER),('m_pTemplate', IWBEMCLASSOBJECT),('m_Guid', GUID),
    )


class _WBEM_REFRESH_INFO_NON_HIPERF(NDRSTRUCT):
    structure = (
        ('m_wszNamespace', WCHAR_T),('m_pTemplate', IWBEMCLASSOBJECT),
    )


WBEM_REFRESH_TYPE_INVALID = 0,
WBEM_REFRESH_TYPE_REMOTE = 3,
WBEM_REFRESH_TYPE_NON_HIPERF = 6
        

class WBEM_REFRESH_INFO_UNION(NDRUNION):
    union = {
        WBEM_REFRESH_TYPE_REMOTE: ('m_Remote',_WBEM_REFRESH_INFO_REMOTE),WBEM_REFRESH_TYPE_NON_HIPERF: ('m_NonHiPerf',_WBEM_REFRESH_INFO_NON_HIPERF),WBEM_REFRESH_TYPE_INVALID: ('m_hres',HRESULT),
    }
        

class _WBEM_REFRESH_INFO(NDRSTRUCT):
    structure = (
        ('m_lType', LONG),('m_Info', WBEM_REFRESH_INFO_UNION),('m_lCancelId', LONG),
    )


class _WBEM_REFRESHER_ID(NDRSTRUCT):
    structure = (
        ('m_szMachineName', LPSTR),('m_dwProcessId', DWORD),('m_guidRefresherId', GUID),
    )


WBEM_RECONNECT_TYPE_OBJECT = 0,
WBEM_RECONNECT_TYPE_ENUM = 1,
WBEM_RECONNECT_TYPE_LAST = 2
        

class _WBEM_RECONNECT_INFO(NDRSTRUCT):
    structure = (
        ('m_lType', LONG),('m_pwcsPath', LPCWSTR),
    )


class _WBEM_RECONNECT_RESULTS(NDRSTRUCT):
    structure = (
        ('m_lId', LONG),('m_hr', HRESULT),
    )

#################################################################################

#CONSTANTS

#################################################################################

IWBEMCLASSOBJECT = 
IWBEMSERVICES = 
IWBEMOBJECTSINK = 
IENUMWBEMCLASSOBJECT = 
IWBEMCALLRESULT = 
IWBEMCONTEXT = 
IWBEMBACKUPRESTORE = 
IWBEMBACKUPRESTOREEX = 
IWBEMLOGINCLIENTID = 
IWBEMLEVEL1LOGIN = 
IWBEMLOGINHELPER = 
IWBEMQUALIFIERSET = 
IWBEMSERVICES = 
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IWbemClassObject Definition

#################################################################################

MSRPC_UUID_IWBEMCLASSOBJECT = uuidtup_to_bin(('dc12a681-737-11f-884-00a004b2e24','0.0'))

OPNUMS = {
}

#################################################################################

#IWbemObjectSink Definition

#################################################################################

MSRPC_UUID_IWBEMOBJECTSINK = uuidtup_to_bin(('7c857801-7381-11cf-884d-00aa004b2e24','0.0'))


class Indicate(NDRCALL):
    opnum = 0
    structure = (
		('lObjectCount', LONG),
		('apObjArray', IWBEMCLASSOBJECT),
    )

class IndicateResponse(NDRCALL):
    structure = (

    )
        

class SetStatus(NDRCALL):
    opnum = 1
    structure = (
		('lFlags', LONG),
		('hResult', HRESULT),
		('strParam', BSTR),
		('pObjParam', IWBEMCLASSOBJECT),
    )

class SetStatusResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Indicate,IndicateResponse),
1 : (SetStatus,SetStatusResponse),
}

#################################################################################

#IEnumWbemClassObject Definition

#################################################################################

MSRPC_UUID_IENUMWBEMCLASSOBJECT = uuidtup_to_bin(('027947e1-d731-11ce-a357-000000000001','0.0'))


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
		('lTimeout', LONG),
		('uCount', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('apObjects', IWBEMCLASSOBJECT),
		('puReturned', ULONG),
    )
        

class NextAsync(NDRCALL):
    opnum = 2
    structure = (
		('uCount', ULONG),
		('pSink', IWBEMOBJECTSINK),
    )

class NextAsyncResponse(NDRCALL):
    structure = (

    )
        

class Clone(NDRCALL):
    opnum = 3
    structure = (

    )

class CloneResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMWBEMCLASSOBJECT),
    )
        

class Skip(NDRCALL):
    opnum = 4
    structure = (
		('lTimeout', LONG),
		('nCount', ULONG),
    )

class SkipResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Reset,ResetResponse),
1 : (Next,NextResponse),
2 : (NextAsync,NextAsyncResponse),
3 : (Clone,CloneResponse),
4 : (Skip,SkipResponse),
}

#################################################################################

#IWbemContext Definition

#################################################################################

MSRPC_UUID_IWBEMCONTEXT = uuidtup_to_bin(('44aca674-e8fc-11d0-a07c-00c04fb68820','0.0'))

OPNUMS = {
}

#################################################################################

#IWbemCallResult Definition

#################################################################################

MSRPC_UUID_IWBEMCALLRESULT = uuidtup_to_bin(('44aca675-e8fc-11d0-a07c-00c04fb68820','0.0'))


class GetResultObject(NDRCALL):
    opnum = 0
    structure = (
		('lTimeout', LONG),
    )

class GetResultObjectResponse(NDRCALL):
    structure = (
		('ppResultObject', IWBEMCLASSOBJECT),
    )
        

class GetResultString(NDRCALL):
    opnum = 1
    structure = (
		('lTimeout', LONG),
    )

class GetResultStringResponse(NDRCALL):
    structure = (
		('pstrResultString', BSTR),
    )
        

class GetResultServices(NDRCALL):
    opnum = 2
    structure = (
		('lTimeout', LONG),
    )

class GetResultServicesResponse(NDRCALL):
    structure = (
		('ppServices', IWBEMSERVICES),
    )
        

class GetCallStatus(NDRCALL):
    opnum = 3
    structure = (
		('lTimeout', LONG),
    )

class GetCallStatusResponse(NDRCALL):
    structure = (
		('plStatus', LONG),
    )
        
OPNUMS = {
0 : (GetResultObject,GetResultObjectResponse),
1 : (GetResultString,GetResultStringResponse),
2 : (GetResultServices,GetResultServicesResponse),
3 : (GetCallStatus,GetCallStatusResponse),
}

#################################################################################

#IWbemServices Definition

#################################################################################

MSRPC_UUID_IWBEMSERVICES = uuidtup_to_bin(('9556dc99-828c-11cf-a37e-00aa003240c7','0.0'))


class OpenNamespace(NDRCALL):
    opnum = 0
    structure = (
		('strNamespace',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppWorkingNamespace', IWBEMSERVICES),
		('ppResult', IWBEMCALLRESULT),
    )

class OpenNamespaceResponse(NDRCALL):
    structure = (
		('ppWorkingNamespace', IWBEMSERVICES),
		('ppResult', IWBEMCALLRESULT),
    )
        

class CancelAsyncCall(NDRCALL):
    opnum = 1
    structure = (
		('pSink', IWBEMOBJECTSINK),
    )

class CancelAsyncCallResponse(NDRCALL):
    structure = (

    )
        

class QueryObjectSink(NDRCALL):
    opnum = 2
    structure = (
		('lFlags', LONG),
    )

class QueryObjectSinkResponse(NDRCALL):
    structure = (
		('ppResponseHandler', IWBEMOBJECTSINK),
    )
        

class GetObject(NDRCALL):
    opnum = 3
    structure = (
		('strObjectPath',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppObject', IWBEMCLASSOBJECT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class GetObjectResponse(NDRCALL):
    structure = (
		('ppObject', IWBEMCLASSOBJECT),
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class GetObjectAsync(NDRCALL):
    opnum = 4
    structure = (
		('strObjectPath',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class GetObjectAsyncResponse(NDRCALL):
    structure = (

    )
        

class PutClass(NDRCALL):
    opnum = 5
    structure = (
		('pObject', IWBEMCLASSOBJECT),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class PutClassResponse(NDRCALL):
    structure = (
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class PutClassAsync(NDRCALL):
    opnum = 6
    structure = (
		('pObject', IWBEMCLASSOBJECT),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class PutClassAsyncResponse(NDRCALL):
    structure = (

    )
        

class DeleteClass(NDRCALL):
    opnum = 7
    structure = (
		('strClass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class DeleteClassResponse(NDRCALL):
    structure = (
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class DeleteClassAsync(NDRCALL):
    opnum = 8
    structure = (
		('strClass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class DeleteClassAsyncResponse(NDRCALL):
    structure = (

    )
        

class CreateClassEnum(NDRCALL):
    opnum = 9
    structure = (
		('strSuperclass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
    )

class CreateClassEnumResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMWBEMCLASSOBJECT),
    )
        

class CreateClassEnumAsync(NDRCALL):
    opnum = 10
    structure = (
		('strSuperclass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class CreateClassEnumAsyncResponse(NDRCALL):
    structure = (

    )
        

class PutInstance(NDRCALL):
    opnum = 11
    structure = (
		('pInst', IWBEMCLASSOBJECT),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class PutInstanceResponse(NDRCALL):
    structure = (
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class PutInstanceAsync(NDRCALL):
    opnum = 12
    structure = (
		('pInst', IWBEMCLASSOBJECT),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class PutInstanceAsyncResponse(NDRCALL):
    structure = (

    )
        

class DeleteInstance(NDRCALL):
    opnum = 13
    structure = (
		('strObjectPath',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class DeleteInstanceResponse(NDRCALL):
    structure = (
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class DeleteInstanceAsync(NDRCALL):
    opnum = 14
    structure = (
		('strObjectPath',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class DeleteInstanceAsyncResponse(NDRCALL):
    structure = (

    )
        

class CreateInstanceEnum(NDRCALL):
    opnum = 15
    structure = (
		('strSuperClass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
    )

class CreateInstanceEnumResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMWBEMCLASSOBJECT),
    )
        

class CreateInstanceEnumAsync(NDRCALL):
    opnum = 16
    structure = (
		('strSuperClass',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class CreateInstanceEnumAsyncResponse(NDRCALL):
    structure = (

    )
        

class ExecQuery(NDRCALL):
    opnum = 17
    structure = (
		('strQueryLanguage',  BSTR),
		('strQuery',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
    )

class ExecQueryResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMWBEMCLASSOBJECT),
    )
        

class ExecQueryAsync(NDRCALL):
    opnum = 18
    structure = (
		('strQueryLanguage',  BSTR),
		('strQuery',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class ExecQueryAsyncResponse(NDRCALL):
    structure = (

    )
        

class ExecNotificationQuery(NDRCALL):
    opnum = 19
    structure = (
		('strQueryLanguage',  BSTR),
		('strQuery',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
    )

class ExecNotificationQueryResponse(NDRCALL):
    structure = (
		('ppEnum', IENUMWBEMCLASSOBJECT),
    )
        

class ExecNotificationQueryAsync(NDRCALL):
    opnum = 20
    structure = (
		('strQueryLanguage',  BSTR),
		('strQuery',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class ExecNotificationQueryAsyncResponse(NDRCALL):
    structure = (

    )
        

class ExecMethod(NDRCALL):
    opnum = 21
    structure = (
		('strObjectPath',  BSTR),
		('strMethodName',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pInParams', IWBEMCLASSOBJECT),
		('ppOutParams', IWBEMCLASSOBJECT),
		('ppCallResult', IWBEMCALLRESULT),
    )

class ExecMethodResponse(NDRCALL):
    structure = (
		('ppOutParams', IWBEMCLASSOBJECT),
		('ppCallResult', IWBEMCALLRESULT),
    )
        

class ExecMethodAsync(NDRCALL):
    opnum = 22
    structure = (
		('strObjectPath',  BSTR),
		('strMethodName',  BSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
		('pInParams', IWBEMCLASSOBJECT),
		('pResponseHandler', IWBEMOBJECTSINK),
    )

class ExecMethodAsyncResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OpenNamespace,OpenNamespaceResponse),
1 : (CancelAsyncCall,CancelAsyncCallResponse),
2 : (QueryObjectSink,QueryObjectSinkResponse),
3 : (GetObject,GetObjectResponse),
4 : (GetObjectAsync,GetObjectAsyncResponse),
5 : (PutClass,PutClassResponse),
6 : (PutClassAsync,PutClassAsyncResponse),
7 : (DeleteClass,DeleteClassResponse),
8 : (DeleteClassAsync,DeleteClassAsyncResponse),
9 : (CreateClassEnum,CreateClassEnumResponse),
10 : (CreateClassEnumAsync,CreateClassEnumAsyncResponse),
11 : (PutInstance,PutInstanceResponse),
12 : (PutInstanceAsync,PutInstanceAsyncResponse),
13 : (DeleteInstance,DeleteInstanceResponse),
14 : (DeleteInstanceAsync,DeleteInstanceAsyncResponse),
15 : (CreateInstanceEnum,CreateInstanceEnumResponse),
16 : (CreateInstanceEnumAsync,CreateInstanceEnumAsyncResponse),
17 : (ExecQuery,ExecQueryResponse),
18 : (ExecQueryAsync,ExecQueryAsyncResponse),
19 : (ExecNotificationQuery,ExecNotificationQueryResponse),
20 : (ExecNotificationQueryAsync,ExecNotificationQueryAsyncResponse),
21 : (ExecMethod,ExecMethodResponse),
22 : (ExecMethodAsync,ExecMethodAsyncResponse),
}

#################################################################################

#IWbemBackupRestore Definition

#################################################################################

MSRPC_UUID_IWBEMBACKUPRESTORE = uuidtup_to_bin(('C49E32C7-BC8B-112-854-0010518304','0.0'))


class Backup(NDRCALL):
    opnum = 0
    structure = (
		('strBackupToFile', LPCWSTR),
		('lFlags', LONG),
    )

class BackupResponse(NDRCALL):
    structure = (

    )
        

class Restore(NDRCALL):
    opnum = 1
    structure = (
		('strRestoreFromFile', LPCWSTR),
		('lFlags', LONG),
    )

class RestoreResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Backup,BackupResponse),
1 : (Restore,RestoreResponse),
}

#################################################################################

#IWbemBackupRestoreEx Definition

#################################################################################

MSRPC_UUID_IWBEMBACKUPRESTOREEX = uuidtup_to_bin(('A359DEC5-E813-4834-82-BA7F1D777D76','0.0'))


class Pause(NDRCALL):
    opnum = 0
    structure = (

    )

class PauseResponse(NDRCALL):
    structure = (

    )
        

class Resume(NDRCALL):
    opnum = 1
    structure = (

    )

class ResumeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Pause,PauseResponse),
1 : (Resume,ResumeResponse),
}

#################################################################################

#IWbemRemoteRefresher Definition

#################################################################################

MSRPC_UUID_IWBEMREMOTEREFRESHER = uuidtup_to_bin(('F1E9C5B2-F59B-112-B362-0010518177','0.0'))


class RemoteRefresh(NDRCALL):
    opnum = 0
    structure = (
		('lFlags', LONG),
    )

class RemoteRefreshResponse(NDRCALL):
    structure = (
		('plNumObjects', LONG),
		('paObjects', WBEM_REFRESHED_OBJECT),
    )
        

class StopRefreshing(NDRCALL):
    opnum = 1
    structure = (
		('lNumIds', LONG),
		('aplIds', LONG),
		('lFlags', LONG),
    )

class StopRefreshingResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (
		('lFlags', LONG),
    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (
		('pGuid', GUID),
    )
        
OPNUMS = {
0 : (RemoteRefresh,RemoteRefreshResponse),
1 : (StopRefreshing,StopRefreshingResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
}

#################################################################################

#IWbemRefreshingServices Definition

#################################################################################

MSRPC_UUID_IWBEMREFRESHINGSERVICES = uuidtup_to_bin(('2C9273E0-1DC3-11d3-B364-00105A1F8177','0.0'))


class AddObjectToRefresher(NDRCALL):
    opnum = 0
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('wszPath', LPCWSTR),
		('lFlags', LONG),
		('pContext', IWBEMCONTEXT),
		('dwClientRefrVersion', DWORD),
    )

class AddObjectToRefresherResponse(NDRCALL):
    structure = (
		('pInfo', _WBEM_REFRESH_INFO),
		('pdwSvrRefrVersion', DWORD),
    )
        

class AddObjectToRefresherByTemplate(NDRCALL):
    opnum = 1
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('pTemplate', IWBEMCLASSOBJECT),
		('lFlags', LONG),
		('pContext', IWBEMCONTEXT),
		('dwClientRefrVersion', DWORD),
    )

class AddObjectToRefresherByTemplateResponse(NDRCALL):
    structure = (
		('pInfo', _WBEM_REFRESH_INFO),
		('pdwSvrRefrVersion', DWORD),
    )
        

class AddEnumToRefresher(NDRCALL):
    opnum = 2
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('wszClass', LPCWSTR),
		('lFlags', LONG),
		('pContext', IWBEMCONTEXT),
		('dwClientRefrVersion', DWORD),
    )

class AddEnumToRefresherResponse(NDRCALL):
    structure = (
		('pInfo', _WBEM_REFRESH_INFO),
		('pdwSvrRefrVersion', DWORD),
    )
        

class RemoveObjectFromRefresher(NDRCALL):
    opnum = 3
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('lId', LONG),
		('lFlags', LONG),
		('dwClientRefrVersion', DWORD),
    )

class RemoveObjectFromRefresherResponse(NDRCALL):
    structure = (
		('pdwSvrRefrVersion', DWORD),
    )
        

class GetRemoteRefresher(NDRCALL):
    opnum = 4
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('lFlags', LONG),
		('dwClientRefrVersion', DWORD),
    )

class GetRemoteRefresherResponse(NDRCALL):
    structure = (
		('ppRemRefresher', IWBEMREMOTEREFRESHER),
		('pGuid', GUID),
		('pdwSvrRefrVersion', DWORD),
    )
        

class ReconnectRemoteRefresher(NDRCALL):
    opnum = 5
    structure = (
		('pRefresherId', _WBEM_REFRESHER_ID),
		('lFlags', LONG),
		('lNumObjects', LONG),
		('dwClientRefrVersion', DWORD),
		('apReconnectInfo', _WBEM_RECONNECT_INFO),
		('apReconnectResults', _WBEM_RECONNECT_RESULTS),
    )

class ReconnectRemoteRefresherResponse(NDRCALL):
    structure = (
		('apReconnectResults', _WBEM_RECONNECT_RESULTS),
		('pdwSvrRefrVersion', DWORD),
    )
        
OPNUMS = {
0 : (AddObjectToRefresher,AddObjectToRefresherResponse),
1 : (AddObjectToRefresherByTemplate,AddObjectToRefresherByTemplateResponse),
2 : (AddEnumToRefresher,AddEnumToRefresherResponse),
3 : (RemoveObjectFromRefresher,RemoveObjectFromRefresherResponse),
4 : (GetRemoteRefresher,GetRemoteRefresherResponse),
5 : (ReconnectRemoteRefresher,ReconnectRemoteRefresherResponse),
}

#################################################################################

#IWbemWCOSmartEnum Definition

#################################################################################

MSRPC_UUID_IWBEMWCOSMARTENUM = uuidtup_to_bin(('423EC01E-2E35-11d2-B604-00104B703EFD','0.0'))


class Next(NDRCALL):
    opnum = 0
    structure = (
		('proxyGUID', REFGUID),
		('lTimeout', LONG),
		('uCount', ULONG),
    )

class NextResponse(NDRCALL):
    structure = (
		('puReturned', ULONG),
		('pdwBuffSize', ULONG),
		('pBuffer', BYTE),
    )
        
OPNUMS = {
0 : (Next,NextResponse),
}

#################################################################################

#IWbemFetchSmartEnum Definition

#################################################################################

MSRPC_UUID_IWBEMFETCHSMARTENUM = uuidtup_to_bin(('1C1C45EE-4395-11d2-B60B-00104B703EFD','0.0'))


class GetSmartEnum(NDRCALL):
    opnum = 0
    structure = (

    )

class GetSmartEnumResponse(NDRCALL):
    structure = (
		('ppSmartEnum', IWBEMWCOSMARTENUM),
    )
        
OPNUMS = {
0 : (GetSmartEnum,GetSmartEnumResponse),
}

#################################################################################

#IWbemLoginClientID Definition

#################################################################################

MSRPC_UUID_IWBEMLOGINCLIENTID = uuidtup_to_bin(('d4781cd6-e5d3-44f-ad94-930fe48a887','0.0'))


class SetClientInfo(NDRCALL):
    opnum = 0
    structure = (
		('wszClientMachine', LPWSTR),
		('lClientProcId', LONG),
		('lReserved', LONG),
    )

class SetClientInfoResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SetClientInfo,SetClientInfoResponse),
}

#################################################################################

#IWbemLevel1Login Definition

#################################################################################

MSRPC_UUID_IWBEMLEVEL1LOGIN = uuidtup_to_bin(('F309AD18-D86A-110-A075-0004B68820','0.0'))


class EstablishPosition(NDRCALL):
    opnum = 0
    structure = (
		('reserved1', WCHAR_T),
		('reserved2', DWORD),
    )

class EstablishPositionResponse(NDRCALL):
    structure = (
		('LocaleVersion', DWORD),
    )
        

class RequestChallenge(NDRCALL):
    opnum = 1
    structure = (
		('reserved1', WCHAR_T),
		('reserved2', WCHAR_T),
    )

class RequestChallengeResponse(NDRCALL):
    structure = (
		('reserved3', UNSIGNED_CHAR),
    )
        

class WBEMLogin(NDRCALL):
    opnum = 2
    structure = (
		('reserved1', WCHAR_T),
		('reserved2', UNSIGNED_CHAR),
		('reserved3', LONG),
		('reserved4', IWBEMCONTEXT),
    )

class WBEMLoginResponse(NDRCALL):
    structure = (
		('reserved5', IWBEMSERVICES),
    )
        

class NTLMLogin(NDRCALL):
    opnum = 3
    structure = (
		('wszNetworkResource', LPWSTR),
		('wszPreferredLocale', LPWSTR),
		('lFlags', LONG),
		('pCtx', IWBEMCONTEXT),
    )

class NTLMLoginResponse(NDRCALL):
    structure = (
		('ppNamespace', IWBEMSERVICES),
    )
        
OPNUMS = {
0 : (EstablishPosition,EstablishPositionResponse),
1 : (RequestChallenge,RequestChallengeResponse),
2 : (WBEMLogin,WBEMLoginResponse),
3 : (NTLMLogin,NTLMLoginResponse),
}

#################################################################################

#IWbemLoginHelper Definition

#################################################################################

MSRPC_UUID_IWBEMLOGINHELPER = uuidtup_to_bin(('541679AB-2E5F-11d3-B34E-00104BCC4B4A','0.0'))


class SetEvent(NDRCALL):
    opnum = 0
    structure = (
		('sEventToSet', LPCSTR),
    )

class SetEventResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SetEvent,SetEventResponse),
}

