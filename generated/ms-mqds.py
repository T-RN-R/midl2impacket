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

#"ms-mqmq.idl"

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

PROPVARIANT = TAG_INNER_PROPVARIANT
PROPID = UNSIGNED_LONG
VARIANT_BOOL = SHORT

class XACTUOW(NDRSTRUCT):
    structure = (
        ('rgb', UNSIGNED_CHAR),
    )


class DATA_BLOB(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_BLOB(NDRPOINTER):
    referent = (
        ('Data', DATA_BLOB),
    )

class BLOB(NDRSTRUCT):
    structure = (
	('cbSize', UNSIGNED_LONG),	('pBlobData', PTR_BLOB),

    )
        

class DATA_CAUB(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_CAUB(NDRPOINTER):
    referent = (
        ('Data', DATA_CAUB),
    )

class CAUB(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAUB),

    )
        

class DATA_CAUI(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_CAUI(NDRPOINTER):
    referent = (
        ('Data', DATA_CAUI),
    )

class CAUI(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAUI),

    )
        

class DATA_CAL(NDRUniConformantArray):
    item = LONG

class PTR_CAL(NDRPOINTER):
    referent = (
        ('Data', DATA_CAL),
    )

class CAL(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAL),

    )
        

class DATA_CAUL(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_CAUL(NDRPOINTER):
    referent = (
        ('Data', DATA_CAUL),
    )

class CAUL(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAUL),

    )
        

class DATA_CAUH(NDRUniConformantArray):
    item = ULARGE_INTEGER

class PTR_CAUH(NDRPOINTER):
    referent = (
        ('Data', DATA_CAUH),
    )

class CAUH(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAUH),

    )
        

class DATA_CACLSID(NDRUniConformantArray):
    item = GUID

class PTR_CACLSID(NDRPOINTER):
    referent = (
        ('Data', DATA_CACLSID),
    )

class CACLSID(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CACLSID),

    )
        

class DATA_CALPWSTR(NDRUniConformantArray):
    item = WCHAR_T

class PTR_CALPWSTR(NDRPOINTER):
    referent = (
        ('Data', DATA_CALPWSTR),
    )

class CALPWSTR(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CALPWSTR),

    )
        

class DATA_CAPROPVARIANT(NDRUniConformantArray):
    item = PROPVARIANT

class PTR_CAPROPVARIANT(NDRPOINTER):
    referent = (
        ('Data', DATA_CAPROPVARIANT),
    )

class CAPROPVARIANT(NDRSTRUCT):
    structure = (
	('cElems', UNSIGNED_LONG),	('pElems', PTR_CAPROPVARIANT),

    )
        

VT_EMPTY = 0,
VT_NULL = 1,
VT_I2 = 2,
VT_I4 = 3,
VT_BOOL = 11,
VT_VARIANT = 12,
VT_I1 = 16,
VT_UI1 = 17,
VT_UI2 = 18,
VT_UI4 = 19,
VT_I8 = 20,
VT_UI8 = 21,
VT_LPWSTR = 31,
VT_BLOB = 65,
VT_CLSID = 72,
VT_VECTOR = 4096
        
VARTYPE = UNSIGNED_SHORT

class _VARUNION(NDRUNION):
    union = {
        VT_I1: ('cVal',CHAR),VT_UI1: ('bVal',UCHAR),VT_I2: ('iVal',SHORT),VT_UI2: ('uiVal',USHORT),VT_I4: ('lVal',LONG),VT_UI4: ('ulVal',ULONG),VT_I8: ('hVal',LARGE_INTEGER),VT_UI8: ('uhVal',ULARGE_INTEGER),VT_BOOL: ('boolVal',VARIANT_BOOL),VT_CLSID: ('puuid',GUID),VT_BLOB: ('blob',BLOB),VT_LPWSTR: ('pwszVal',WCHAR_T),VT_VECTOR|VT_UI1: ('caub',CAUB),VT_VECTOR|VT_UI2: ('caui',CAUI),VT_VECTOR|VT_I4: ('cal',CAL),VT_VECTOR|VT_UI4: ('caul',CAUL),VT_VECTOR|VT_UI8: ('cauh',CAUH),VT_VECTOR|VT_CLSID: ('cauuid',CACLSID),VT_VECTOR|VT_LPWSTR: ('calpwstr',CALPWSTR),VT_VECTOR|VT_VARIANT: ('capropvar',CAPROPVARIANT),
    }
        

class TAG_INNER_PROPVARIANT(NDRSTRUCT):
    structure = (
        ('vt', VARTYPE),('wReserved1', UCHAR),('wReserved2', UCHAR),('wReserved3', ULONG),('_varUnion', _VARUNION),
    )


class DL_ID(NDRSTRUCT):
    structure = (
        ('m_DlGuid', GUID),('m_pwzDomain', WCHAR_T),
    )


class MULTICAST_ID(NDRSTRUCT):
    structure = (
        ('m_address', ULONG),('m_port', ULONG),
    )


class OBJECTID(NDRSTRUCT):
    structure = (
        ('Lineage', GUID),('Uniquifier', DWORD),
    )


QUEUE_FORMAT_TYPE_UNKNOWN = 0,
QUEUE_FORMAT_TYPE_PUBLIC = 1,
QUEUE_FORMAT_TYPE_PRIVATE = 2,
QUEUE_FORMAT_TYPE_DIRECT = 3,
QUEUE_FORMAT_TYPE_MACHINE = 4,
QUEUE_FORMAT_TYPE_CONNECTOR = 5,
QUEUE_FORMAT_TYPE_DL = 6,
QUEUE_FORMAT_TYPE_MULTICAST = 7,
QUEUE_FORMAT_TYPE_SUBQUEUE = 8
        

class U0(NDRUNION):
    union = {
        QUEUE_FORMAT_TYPE_PUBLIC: ('m_gPublicID',GUID),QUEUE_FORMAT_TYPE_PRIVATE: ('m_oPrivateID',OBJECTID),QUEUE_FORMAT_TYPE_DIRECT: ('m_pDirectID',WCHAR_T),QUEUE_FORMAT_TYPE_MACHINE: ('m_gMachineID',GUID),QUEUE_FORMAT_TYPE_CONNECTOR: ('m_GConnectorID',GUID),QUEUE_FORMAT_TYPE_DL: ('m_DlID',DL_ID),QUEUE_FORMAT_TYPE_MULTICAST: ('m_MulticastID',MULTICAST_ID),QUEUE_FORMAT_TYPE_SUBQUEUE: ('m_pDirectSubqueueID',WCHAR_T),
    }
        

class QUEUE_FORMAT(NDRSTRUCT):
    structure = (
        ('m_qft', UNSIGNED_CHAR),('m_SuffixAndFlags', UNSIGNED_CHAR),('m_reserved', UNSIGNED_SHORT),('u0', U0),
    )

#################################################################################

#TYPEDEFS

#################################################################################


class MQPROPERTYRESTRICTION(NDRSTRUCT):
    structure = (
        ('rel', UNSIGNED_LONG),('prop', UNSIGNED_LONG),('prval', PROPVARIANT),
    )


class DATA_MQRESTRICTION(NDRUniConformantArray):
    item = MQPROPERTYRESTRICTION

class PTR_MQRESTRICTION(NDRPOINTER):
    referent = (
        ('Data', DATA_MQRESTRICTION),
    )

class MQRESTRICTION(NDRSTRUCT):
    structure = (
	('cRes', UNSIGNED_LONG),	('paPropRes', PTR_MQRESTRICTION),

    )
        

class DATA_MQCOLUMNSET(NDRUniConformantArray):
    item = PROPID

class PTR_MQCOLUMNSET(NDRPOINTER):
    referent = (
        ('Data', DATA_MQCOLUMNSET),
    )

class MQCOLUMNSET(NDRSTRUCT):
    structure = (
	('cCol', UNSIGNED_LONG),	('aCol', PTR_MQCOLUMNSET),

    )
        

class MQSORTKEY(NDRSTRUCT):
    structure = (
        ('propColumn', UNSIGNED_LONG),('dwOrder', UNSIGNED_LONG),
    )


class DATA_MQSORTSET(NDRUniConformantArray):
    item = MQSORTKEY

class PTR_MQSORTSET(NDRPOINTER):
    referent = (
        ('Data', DATA_MQSORTSET),
    )

class MQSORTSET(NDRSTRUCT):
    structure = (
	('cCol', UNSIGNED_LONG),	('aCol', PTR_MQSORTSET),

    )
        
#################################################################################

#CONSTANTS

#################################################################################

PRLT = 0
PRLE = 1
PRGT = 2
PRGE = 3
PREQ = 4
PRNE = 5
QUERY_SORTASCEND = 0
QUERY_SORTDESCEND = 1
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#dscomm Definition

#################################################################################

MSRPC_UUID_DSCOMM = uuidtup_to_bin(('77df7a80-f298-11d0-8358-00a024c480a8','0.0'))

BOUNDED_SIGNATURE_SIZE = UNSIGNED_LONG
LPBOUNDED_SIGNATURE_SIZE = BOUNDED_SIGNATURE_SIZE
BOUNDED_PROPERTIES = DWORD
LPBOUNDED_PROPERTIES = BOUNDED_PROPERTIES
PCONTEXT_HANDLE_TYPE = VOID
PPCONTEXT_HANDLE_TYPE = PCONTEXT_HANDLE_TYPE
PCONTEXT_HANDLE_SERVER_AUTH_TYPE = VOID
PPCONTEXT_HANDLE_SERVER_AUTH_TYPE = PCONTEXT_HANDLE_SERVER_AUTH_TYPE
PCONTEXT_HANDLE_DELETE_TYPE = VOID
PPCONTEXT_HANDLE_DELETE_TYPE = PCONTEXT_HANDLE_DELETE_TYPE

class S_DSCreateObject(NDRCALL):
    opnum = 0
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
		('dwSDLength', UNSIGNED_LONG),
		('SecurityDescriptor', UNSIGNED_CHAR),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
		('pObjGuid', GUID),
    )

class S_DSCreateObjectResponse(NDRCALL):
    structure = (
		('pObjGuid', GUID),
    )
        

class S_DSDeleteObject(NDRCALL):
    opnum = 1
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
    )

class S_DSDeleteObjectResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetProps(NDRCALL):
    opnum = 2
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetPropsResponse(NDRCALL):
    structure = (
		('apVar', PROPVARIANT),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSSetProps(NDRCALL):
    opnum = 3
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
    )

class S_DSSetPropsResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetObjectSecurity(NDRCALL):
    opnum = 4
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
		('SecurityInformation', UNSIGNED_LONG),
		('nLength', UNSIGNED_LONG),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetObjectSecurityResponse(NDRCALL):
    structure = (
		('pSecurityDescriptor', UNSIGNED_CHAR),
		('lpnLengthNeeded', UNSIGNED_LONG),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSSetObjectSecurity(NDRCALL):
    opnum = 5
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pwcsPathName', CONST_WCHAR_T),
		('SecurityInformation', UNSIGNED_LONG),
		('pSecurityDescriptor', UNSIGNED_CHAR),
		('nLength', UNSIGNED_LONG),
    )

class S_DSSetObjectSecurityResponse(NDRCALL):
    structure = (

    )
        

class S_DSLookupBegin(NDRCALL):
    opnum = 6
    structure = (
		('hBind', HANDLE_T),
		('pwcsContext', WCHAR_T),
		('pRestriction', MQRESTRICTION),
		('pColumns', MQCOLUMNSET),
		('pSort', MQSORTSET),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
    )

class S_DSLookupBeginResponse(NDRCALL):
    structure = (
		('pHandle', PPCONTEXT_HANDLE_TYPE),
    )
        

class S_DSLookupNext(NDRCALL):
    opnum = 7
    structure = (
		('hBind', HANDLE_T),
		('Handle', PCONTEXT_HANDLE_TYPE),
		('dwSize', LPBOUNDED_PROPERTIES),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSLookupNextResponse(NDRCALL):
    structure = (
		('dwOutSize', UNSIGNED_LONG),
		('pbBuffer', PROPVARIANT),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSLookupEnd(NDRCALL):
    opnum = 8
    structure = (
		('hBind', HANDLE_T),
		('phContext', PPCONTEXT_HANDLE_TYPE),
    )

class S_DSLookupEndResponse(NDRCALL):
    structure = (
		('phContext', PPCONTEXT_HANDLE_TYPE),
    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class S_DSDeleteObjectGuid(NDRCALL):
    opnum = 10
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
    )

class S_DSDeleteObjectGuidResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetPropsGuid(NDRCALL):
    opnum = 11
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetPropsGuidResponse(NDRCALL):
    structure = (
		('apVar', PROPVARIANT),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSSetPropsGuid(NDRCALL):
    opnum = 12
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
    )

class S_DSSetPropsGuidResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetObjectSecurityGuid(NDRCALL):
    opnum = 13
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
		('SecurityInformation', UNSIGNED_LONG),
		('nLength', UNSIGNED_LONG),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetObjectSecurityGuidResponse(NDRCALL):
    structure = (
		('pSecurityDescriptor', UNSIGNED_CHAR),
		('lpnLengthNeeded', UNSIGNED_LONG),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSSetObjectSecurityGuid(NDRCALL):
    opnum = 14
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
		('SecurityInformation', UNSIGNED_LONG),
		('pSecurityDescriptor', UNSIGNED_CHAR),
		('nLength', UNSIGNED_LONG),
    )

class S_DSSetObjectSecurityGuidResponse(NDRCALL):
    structure = (

    )
        

class Opnum15NotUsedOnWire(NDRCALL):
    opnum = 15
    structure = (

    )

class Opnum15NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum16NotUsedOnWire(NDRCALL):
    opnum = 16
    structure = (

    )

class Opnum16NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum17NotUsedOnWire(NDRCALL):
    opnum = 17
    structure = (

    )

class Opnum17NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum18NotUsedOnWire(NDRCALL):
    opnum = 18
    structure = (

    )

class Opnum18NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class S_DSQMSetMachineProperties(NDRCALL):
    opnum = 19
    structure = (
		('hBind', HANDLE_T),
		('pwcsPathName', CONST_WCHAR_T),
		('cp', UNSIGNED_LONG),
		('aProp', UNSIGNED_LONG),
		('apVar', PROPVARIANT),
		('dwContext', UNSIGNED_LONG),
    )

class S_DSQMSetMachinePropertiesResponse(NDRCALL):
    structure = (

    )
        

class S_DSCreateServersCache(NDRCALL):
    opnum = 20
    structure = (
		('hBind', HANDLE_T),
		('pdwIndex', UNSIGNED_LONG),
		('lplpSiteServers', WCHAR_T),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSCreateServersCacheResponse(NDRCALL):
    structure = (
		('pdwIndex', UNSIGNED_LONG),
		('lplpSiteServers', WCHAR_T),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSQMSetMachinePropertiesSignProc(NDRCALL):
    opnum = 21
    structure = (
		('abChallenge', BYTE),
		('dwCallengeSize', UNSIGNED_LONG),
		('dwContext', UNSIGNED_LONG),
		('abSignature', BYTE),
		('pdwSignatureSize', UNSIGNED_LONG),
		('dwSignatureMaxSize', UNSIGNED_LONG),
    )

class S_DSQMSetMachinePropertiesSignProcResponse(NDRCALL):
    structure = (
		('abSignature', BYTE),
		('pdwSignatureSize', UNSIGNED_LONG),
    )
        

class S_DSQMGetObjectSecurity(NDRCALL):
    opnum = 22
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', UNSIGNED_LONG),
		('pGuid',  GUID),
		('SecurityInformation', UNSIGNED_LONG),
		('nLength', UNSIGNED_LONG),
		('dwContext', UNSIGNED_LONG),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSQMGetObjectSecurityResponse(NDRCALL):
    structure = (
		('pSecurityDescriptor', UNSIGNED_CHAR),
		('lpnLengthNeeded', UNSIGNED_LONG),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSQMGetObjectSecurityChallengeResponceProc(NDRCALL):
    opnum = 23
    structure = (
		('abChallenge', BYTE),
		('dwCallengeSize', UNSIGNED_LONG),
		('dwContext', UNSIGNED_LONG),
		('abCallengeResponce', BYTE),
		('pdwCallengeResponceSize', UNSIGNED_LONG),
		('dwCallengeResponceMaxSize', UNSIGNED_LONG),
    )

class S_DSQMGetObjectSecurityChallengeResponceProcResponse(NDRCALL):
    structure = (
		('abCallengeResponce', BYTE),
		('pdwCallengeResponceSize', UNSIGNED_LONG),
    )
        

class S_InitSecCtx(NDRCALL):
    opnum = 24
    structure = (
		('dwContext', UNSIGNED_LONG),
		('pServerbuff', UNSIGNED_CHAR),
		('dwServerBuffSize', UNSIGNED_LONG),
		('dwClientBuffMaxSize', UNSIGNED_LONG),
    )

class S_InitSecCtxResponse(NDRCALL):
    structure = (
		('pClientBuff', UNSIGNED_CHAR),
		('pdwClientBuffSize', UNSIGNED_LONG),
    )
        

class S_DSValidateServer(NDRCALL):
    opnum = 25
    structure = (
		('hBind', HANDLE_T),
		('pguidEnterpriseId',  GUID),
		('fSetupMode', BOOL),
		('dwContext', UNSIGNED_LONG),
		('dwClientBuffMaxSize', UNSIGNED_LONG),
		('pClientBuff', UNSIGNED_CHAR),
		('dwClientBuffSize', UNSIGNED_LONG),
    )

class S_DSValidateServerResponse(NDRCALL):
    structure = (
		('pphServerAuth', PPCONTEXT_HANDLE_SERVER_AUTH_TYPE),
    )
        

class S_DSCloseServerHandle(NDRCALL):
    opnum = 26
    structure = (
		('pphServerAuth', PPCONTEXT_HANDLE_SERVER_AUTH_TYPE),
    )

class S_DSCloseServerHandleResponse(NDRCALL):
    structure = (
		('pphServerAuth', PPCONTEXT_HANDLE_SERVER_AUTH_TYPE),
    )
        

class Opnum24NotUsedOnWire(NDRCALL):
    opnum = 27
    structure = (

    )

class Opnum24NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum25NotUsedOnWire(NDRCALL):
    opnum = 28
    structure = (

    )

class Opnum25NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum26NotUsedOnWire(NDRCALL):
    opnum = 29
    structure = (

    )

class Opnum26NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetServerPort(NDRCALL):
    opnum = 30
    structure = (
		('hBind', HANDLE_T),
		('fIP', UNSIGNED_LONG),
    )

class S_DSGetServerPortResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (S_DSCreateObject,S_DSCreateObjectResponse),
1 : (S_DSDeleteObject,S_DSDeleteObjectResponse),
2 : (S_DSGetProps,S_DSGetPropsResponse),
3 : (S_DSSetProps,S_DSSetPropsResponse),
4 : (S_DSGetObjectSecurity,S_DSGetObjectSecurityResponse),
5 : (S_DSSetObjectSecurity,S_DSSetObjectSecurityResponse),
6 : (S_DSLookupBegin,S_DSLookupBeginResponse),
7 : (S_DSLookupNext,S_DSLookupNextResponse),
8 : (S_DSLookupEnd,S_DSLookupEndResponse),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (S_DSDeleteObjectGuid,S_DSDeleteObjectGuidResponse),
11 : (S_DSGetPropsGuid,S_DSGetPropsGuidResponse),
12 : (S_DSSetPropsGuid,S_DSSetPropsGuidResponse),
13 : (S_DSGetObjectSecurityGuid,S_DSGetObjectSecurityGuidResponse),
14 : (S_DSSetObjectSecurityGuid,S_DSSetObjectSecurityGuidResponse),
15 : (Opnum15NotUsedOnWire,Opnum15NotUsedOnWireResponse),
16 : (Opnum16NotUsedOnWire,Opnum16NotUsedOnWireResponse),
17 : (Opnum17NotUsedOnWire,Opnum17NotUsedOnWireResponse),
18 : (Opnum18NotUsedOnWire,Opnum18NotUsedOnWireResponse),
19 : (S_DSQMSetMachineProperties,S_DSQMSetMachinePropertiesResponse),
20 : (S_DSCreateServersCache,S_DSCreateServersCacheResponse),
21 : (S_DSQMSetMachinePropertiesSignProc,S_DSQMSetMachinePropertiesSignProcResponse),
22 : (S_DSQMGetObjectSecurity,S_DSQMGetObjectSecurityResponse),
23 : (S_DSQMGetObjectSecurityChallengeResponceProc,S_DSQMGetObjectSecurityChallengeResponceProcResponse),
24 : (S_InitSecCtx,S_InitSecCtxResponse),
25 : (S_DSValidateServer,S_DSValidateServerResponse),
26 : (S_DSCloseServerHandle,S_DSCloseServerHandleResponse),
27 : (Opnum24NotUsedOnWire,Opnum24NotUsedOnWireResponse),
28 : (Opnum25NotUsedOnWire,Opnum25NotUsedOnWireResponse),
29 : (Opnum26NotUsedOnWire,Opnum26NotUsedOnWireResponse),
30 : (S_DSGetServerPort,S_DSGetServerPortResponse),
}

#################################################################################

#dscomm2 Definition

#################################################################################

MSRPC_UUID_DSCOMM2 = uuidtup_to_bin(('708cca10-9569-11d1-b2a5-0060977d8118','0.0'))


class S_DSGetComputerSites(NDRCALL):
    opnum = 0
    structure = (
		('hBind', HANDLE_T),
		('pwcsPathName', CONST_WCHAR_T),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetComputerSitesResponse(NDRCALL):
    structure = (
		('pdwNumberOfSites', DWORD),
		('ppguidSites', GUID),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSGetPropsEx(NDRCALL):
    opnum = 1
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', DWORD),
		('pwcsPathName', CONST_WCHAR_T),
		('cp', DWORD),
		('aProp', PROPID),
		('apVar', PROPVARIANT),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetPropsExResponse(NDRCALL):
    structure = (
		('apVar', PROPVARIANT),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSGetPropsGuidEx(NDRCALL):
    opnum = 2
    structure = (
		('hBind', HANDLE_T),
		('dwObjectType', DWORD),
		('pGuid',  GUID),
		('cp', DWORD),
		('aProp', PROPID),
		('apVar', PROPVARIANT),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetPropsGuidExResponse(NDRCALL):
    structure = (
		('apVar', PROPVARIANT),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        

class S_DSBeginDeleteNotification(NDRCALL):
    opnum = 3
    structure = (
		('hBind', HANDLE_T),
		('pwcsPathName', CONST_WCHAR_T),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
    )

class S_DSBeginDeleteNotificationResponse(NDRCALL):
    structure = (
		('pHandle', PPCONTEXT_HANDLE_DELETE_TYPE),
    )
        

class S_DSNotifyDelete(NDRCALL):
    opnum = 4
    structure = (
		('hBind', HANDLE_T),
		('Handle', PCONTEXT_HANDLE_DELETE_TYPE),
    )

class S_DSNotifyDeleteResponse(NDRCALL):
    structure = (

    )
        

class S_DSEndDeleteNotification(NDRCALL):
    opnum = 5
    structure = (
		('hBind', HANDLE_T),
		('pHandle', PPCONTEXT_HANDLE_DELETE_TYPE),
    )

class S_DSEndDeleteNotificationResponse(NDRCALL):
    structure = (
		('pHandle', PPCONTEXT_HANDLE_DELETE_TYPE),
    )
        

class S_DSIsServerGC(NDRCALL):
    opnum = 6
    structure = (
		('hBind', HANDLE_T),
    )

class S_DSIsServerGCResponse(NDRCALL):
    structure = (

    )
        

class Opnum7NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum7NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class S_DSGetGCListInDomain(NDRCALL):
    opnum = 8
    structure = (
		('hBind', HANDLE_T),
		('lpwszComputerName', CONST_WCHAR_T),
		('lpwszDomainName', CONST_WCHAR_T),
		('phServerAuth', PCONTEXT_HANDLE_SERVER_AUTH_TYPE),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )

class S_DSGetGCListInDomainResponse(NDRCALL):
    structure = (
		('lplpwszGCList', WCHAR_T),
		('pbServerSignature', UNSIGNED_CHAR),
		('pdwServerSignatureSize', LPBOUNDED_SIGNATURE_SIZE),
    )
        
OPNUMS = {
0 : (S_DSGetComputerSites,S_DSGetComputerSitesResponse),
1 : (S_DSGetPropsEx,S_DSGetPropsExResponse),
2 : (S_DSGetPropsGuidEx,S_DSGetPropsGuidExResponse),
3 : (S_DSBeginDeleteNotification,S_DSBeginDeleteNotificationResponse),
4 : (S_DSNotifyDelete,S_DSNotifyDeleteResponse),
5 : (S_DSEndDeleteNotification,S_DSEndDeleteNotificationResponse),
6 : (S_DSIsServerGC,S_DSIsServerGCResponse),
7 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
8 : (S_DSGetGCListInDomain,S_DSGetGCListInDomainResponse),
}

