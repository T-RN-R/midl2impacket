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

#"ms-dltw.idl"

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

SEQUENCENUMBER = SIGNED_LONG

class COBJID(NDRSTRUCT):
    structure = (
        ('_object', GUID),
    )


class CVOLUMEID(NDRSTRUCT):
    structure = (
        ('_volume', GUID),
    )


class CMACHINEID(NDRSTRUCT):
    structure = (
        ('_szMachine', CHAR),
    )


class CDOMAINRELATIVEOBJID(NDRSTRUCT):
    structure = (
        ('_volume', CVOLUMEID),('_object', COBJID),
    )

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#trkwks Definition

#################################################################################

MSRPC_UUID_TRKWKS = uuidtup_to_bin(('300f3532-38cc-11d0-a3f0-0020af6b0add','0.0'))


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
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
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
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum10NotUsedOnWire(NDRCALL):
    opnum = 10
    structure = (

    )

class Opnum10NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum11NotUsedOnWire(NDRCALL):
    opnum = 11
    structure = (

    )

class Opnum11NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LnkSearchMachine(NDRCALL):
    opnum = 12
    structure = (
		('Restrictions', UNSIGNED_LONG),
		('pdroidBirthLast',  CDOMAINRELATIVEOBJID),
		('pdroidLast',  CDOMAINRELATIVEOBJID),
    )

class LnkSearchMachineResponse(NDRCALL):
    structure = (
		('pdroidBirthNext', CDOMAINRELATIVEOBJID),
		('pdroidNext', CDOMAINRELATIVEOBJID),
		('pmcidNext', CMACHINEID),
		('ptszPath', WCHAR_T),
    )
        
OPNUMS = {
0 : (Opnum0NotUsedOnWire,Opnum0NotUsedOnWireResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (Opnum2NotUsedOnWire,Opnum2NotUsedOnWireResponse),
3 : (Opnum3NotUsedOnWire,Opnum3NotUsedOnWireResponse),
4 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
5 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
6 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
7 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
8 : (Opnum8NotUsedOnWire,Opnum8NotUsedOnWireResponse),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (Opnum10NotUsedOnWire,Opnum10NotUsedOnWireResponse),
11 : (Opnum11NotUsedOnWire,Opnum11NotUsedOnWireResponse),
12 : (LnkSearchMachine,LnkSearchMachineResponse),
}

#################################################################################

#TYPEDEFS

#################################################################################

SEQUENCENUMBER = SIGNED_LONG

class CVOLUMESECRET(NDRSTRUCT):
    structure = (
        ('_abSecret', BYTE),
    )


class OLD_TRK_FILE_TRACKING_INFORMATION(NDRSTRUCT):
    structure = (
        ('tszFilePath', WCHAR),('droidBirth', CDOMAINRELATIVEOBJID),('droidLast', CDOMAINRELATIVEOBJID),('hr', HRESULT),
    )


class TRK_FILE_TRACKING_INFORMATION(NDRSTRUCT):
    structure = (
        ('droidBirth', CDOMAINRELATIVEOBJID),('droidLast', CDOMAINRELATIVEOBJID),('mcidLast', CMACHINEID),('hr', HRESULT),
    )


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = OLD_TRK_FILE_TRACKING_INFORMATION

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('cSearch', UNSIGNED_LONG),	('pSearches', PTR_UNSIGNED_LONG),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = TRK_FILE_TRACKING_INFORMATION

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('cSearch', UNSIGNED_LONG),	('pSearches', PTR_UNSIGNED_LONG),

    )
        

class DATA_CDOMAINRELATIVEOBJID(NDRUniConformantArray):
    item = CDOMAINRELATIVEOBJID

class PTR_CDOMAINRELATIVEOBJID(NDRPOINTER):
    referent = (
        ('Data', DATA_CDOMAINRELATIVEOBJID),
    )

class CDOMAINRELATIVEOBJID(NDRSTRUCT):
    structure = (
	('cNotifications', UNSIGNED_LONG),	('cProcessed', UNSIGNED_LONG),	('seq', SEQUENCENUMBER),	('fForceSeqNumber', LONG),	('pvolid', CVOLUMEID),	('rgobjidCurrent', COBJID),	('rgdroidBirth', CDOMAINRELATIVEOBJID),	('rgdroidNew', PTR_CDOMAINRELATIVEOBJID),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = CVOLUMEID

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('cSources', UNSIGNED_LONG),	('adroidBirth', CDOMAINRELATIVEOBJID),	('cVolumes', UNSIGNED_LONG),	('avolid', PTR_UNSIGNED_LONG),

    )
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = CVOLUMEID

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('cdroidBirth', UNSIGNED_LONG),	('adroidBirth', CDOMAINRELATIVEOBJID),	('cVolumes', UNSIGNED_LONG),	('pVolumes', PTR_UNSIGNED_LONG),

    )
        

CREATE_VOLUME = 0,
QUERY_VOLUME = 1,
CLAIM_VOLUME = 2,
FIND_VOLUME = 3,
TEST_VOLUME = 4,
DELETE_VOLUME = 5
        

class TRKSVR_SYNC_VOLUME(NDRSTRUCT):
    structure = (
        ('hr', HRESULT),('SyncType', TRKSVR_SYNC_TYPE),('volume', CVOLUMEID),('secret', CVOLUMESECRET),('secretOld', CVOLUMESECRET),('seq', SEQUENCENUMBER),('ftLastRefresh', FILETIME),('machine', CMACHINEID),
    )


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = TRKSVR_SYNC_VOLUME

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('cVolumes', UNSIGNED_LONG),	('pVolumes', PTR_UNSIGNED_LONG),

    )
        

class VERSION(NDRSTRUCT):
    structure = (
        ('dwMajor', UNSIGNED_LONG),('dwMinor', UNSIGNED_LONG),('dwBuildNumber', UNSIGNED_LONG),
    )


class TRKSVR_STATISTICS(NDRSTRUCT):
    structure = (
        ('cSyncVolumeRequests', UNSIGNED_LONG),('cSyncVolumeErrors', UNSIGNED_LONG),('cSyncVolumeThreads', UNSIGNED_LONG),('cCreateVolumeRequests', UNSIGNED_LONG),('cCreateVolumeErrors', UNSIGNED_LONG),('cClaimVolumeRequests', UNSIGNED_LONG),('cClaimVolumeErrors', UNSIGNED_LONG),('cQueryVolumeRequests', UNSIGNED_LONG),('cQueryVolumeErrors', UNSIGNED_LONG),('cFindVolumeRequests', UNSIGNED_LONG),('cFindVolumeErrors', UNSIGNED_LONG),('cTestVolumeRequests', UNSIGNED_LONG),('cTestVolumeErrors', UNSIGNED_LONG),('cSearchRequests', UNSIGNED_LONG),('cSearchErrors', UNSIGNED_LONG),('cSearchThreads', UNSIGNED_LONG),('cMoveNotifyRequests', UNSIGNED_LONG),('cMoveNotifyErrors', UNSIGNED_LONG),('cMoveNotifyThreads', UNSIGNED_LONG),('cRefreshRequests', UNSIGNED_LONG),('cRefreshErrors', UNSIGNED_LONG),('cRefreshThreads', UNSIGNED_LONG),('cDeleteNotifyRequests', UNSIGNED_LONG),('cDeleteNotifyErrors', UNSIGNED_LONG),('cDeleteNotifyThreads', UNSIGNED_LONG),('ulGCIterationPeriod', UNSIGNED_LONG),('ftLastSuccessfulRequest', FILETIME),('hrLastError', HRESULT),('dwMoveLimit', UNSIGNED_LONG),('lRefreshCounter', LONG),('dwCachedVolumeTableCount', UNSIGNED_LONG),('dwCachedMoveTableCount', UNSIGNED_LONG),('ftCachedLastUpdated', FILETIME),('fIsDesignatedDc', LONG),('ftNextGC', FILETIME),('ftServiceStart', FILETIME),('cMaxRPCThreads', UNSIGNED_LONG),('cAvailableRPCThreads', UNSIGNED_LONG),('cLowestAvailableRPCThreads', UNSIGNED_LONG),('cNumThreadPoolThreads', UNSIGNED_LONG),('cMostThreadPoolThreads', UNSIGNED_LONG),('cEntriesToGC', SHORT),('cEntriesGCed', SHORT),('cMaxDsWriteEvents', SHORT),('cCurrentFailedWrites', SHORT),('VERSION', VERSION),
    )


class TRKWKS_CONFIG(NDRSTRUCT):
    structure = (
        ('dwParameter', UNSIGNED_LONG),('dwNewValue', UNSIGNED_LONG),
    )


old_SEARCH = ,
MOVE_NOTIFICATION = 1,
REFRESH = 2,
SYNC_VOLUMES = 3,
DELETE_NOTIFY = 4,
STATISTICS = 5,
SEARCH = 6,
WKS_CONFIG = 6
        

PRI_0 = 0,
PRI_1 = 1,
PRI_2 = 2,
PRI_3 = 3,
PRI_4 = 4,
PRI_5 = 5,
PRI_6 = 6,
PRI_7 = 7,
PRI_8 = 8,
PRI_9 = 9
        

class U0(NDRUNION):
    union = {
        old_SEARCH: ('old_Search',OLD_TRKSVR_CALL_SEARCH),MOVE_NOTIFICATION: ('MoveNotification',TRKSVR_CALL_MOVE_NOTIFICATION),REFRESH: ('Refresh',TRKSVR_CALL_REFRESH),SYNC_VOLUMES: ('SyncVolumes',TRKSVR_CALL_SYNC_VOLUMES),DELETE_NOTIFY: ('Delete',TRKSVR_CALL_DELETE),STATISTICS: ('Statistics',TRKSVR_STATISTICS),SEARCH: ('Search',TRKSVR_CALL_SEARCH),WKS_CONFIG: ('WksConfig',TRKWKS_CONFIG),WKS_VOLUME_REFRESH: ('WksRefresh',UNSIGNED_LONG),
    }
        

class TRKSVR_MESSAGE_UNION(NDRSTRUCT):
    structure = (
        ('MessageType', TRKSVR_MESSAGE_TYPE),('Priority', TRKSVR_MESSAGE_PRIORITY),('u0', U0),('ptszMachineID', WCHAR),
    )

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#trksvr Definition

#################################################################################

MSRPC_UUID_TRKSVR = uuidtup_to_bin(('4da1c422-943d-11d1-acae-00c04fc2aa3f','0.0'))


class LnkSvrMessage(NDRCALL):
    opnum = 0
    structure = (
		('IDL_handle', HANDLE_T),
		('pMsg', TRKSVR_MESSAGE_UNION),
    )

class LnkSvrMessageResponse(NDRCALL):
    structure = (
		('pMsg', TRKSVR_MESSAGE_UNION),
    )
        

class LnkSvrMessageCallback(NDRCALL):
    opnum = 1
    structure = (
		('pMsg', TRKSVR_MESSAGE_UNION),
    )

class LnkSvrMessageCallbackResponse(NDRCALL):
    structure = (
		('pMsg', TRKSVR_MESSAGE_UNION),
    )
        
OPNUMS = {
0 : (LnkSvrMessage,LnkSvrMessageResponse),
1 : (LnkSvrMessageCallback,LnkSvrMessageCallbackResponse),
}

