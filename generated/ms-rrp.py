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

#TYPEDEFS

#################################################################################

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#winreg Definition

#################################################################################

MSRPC_UUID_WINREG = uuidtup_to_bin(('338CD001-2244-31F1-AAAA-900038001003','0.0'))

RRP_UNICODE_STRING = RPC_UNICODE_STRING
PRRP_UNICODE_STRING = RPC_UNICODE_STRING
RPC_HKEY = HANDLE
PRPC_HKEY = RPC_HKEY
PREGISTRY_SERVER_NAME = PWCHAR
SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD

class RVALENT(NDRSTRUCT):
    structure = (
        ('ve_valuename', PRPC_UNICODE_STRING),('ve_valuelen', DWORD),('ve_valueptr', LPDWORD),('ve_type', DWORD),
    )
class PRVALENT(NDRPOINTER):
    referent = (
        ('Data', RVALENT),
    )    

REGSAM = ULONG

class RPC_SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('lpSecurityDescriptor', PBYTE),('cbInSecurityDescriptor', DWORD),('cbOutSecurityDescriptor', DWORD),
    )
class PRPC_SECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', RPC_SECURITY_DESCRIPTOR),
    )    


class RPC_SECURITY_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('nLength', DWORD),('RpcSecurityDescriptor', RPC_SECURITY_DESCRIPTOR),('bInheritHandle', BOOLEAN),
    )
class PRPC_SECURITY_ATTRIBUTES(NDRPOINTER):
    referent = (
        ('Data', RPC_SECURITY_ATTRIBUTES),
    )    


class OpenClassesRoot(NDRCALL):
    opnum = 0
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenClassesRootResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class OpenCurrentUser(NDRCALL):
    opnum = 1
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenCurrentUserResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class OpenLocalMachine(NDRCALL):
    opnum = 2
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenLocalMachineResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class OpenPerformanceData(NDRCALL):
    opnum = 3
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenPerformanceDataResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class OpenUsers(NDRCALL):
    opnum = 4
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenUsersResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class BaseRegCloseKey(NDRCALL):
    opnum = 5
    structure = (
		('hKey', PRPC_HKEY),
    )

class BaseRegCloseKeyResponse(NDRCALL):
    structure = (
		('hKey', PRPC_HKEY),
    )
        

class BaseRegCreateKey(NDRCALL):
    opnum = 6
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
		('lpClass', PRRP_UNICODE_STRING),
		('dwOptions', DWORD),
		('samDesired', REGSAM),
		('lpSecurityAttributes', PRPC_SECURITY_ATTRIBUTES),
		('lpdwDisposition', LPDWORD),
    )

class BaseRegCreateKeyResponse(NDRCALL):
    structure = (
		('phkResult', PRPC_HKEY),
		('lpdwDisposition', LPDWORD),
    )
        

class BaseRegDeleteKey(NDRCALL):
    opnum = 7
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
    )

class BaseRegDeleteKeyResponse(NDRCALL):
    structure = (

    )
        

class BaseRegDeleteValue(NDRCALL):
    opnum = 8
    structure = (
		('hKey', RPC_HKEY),
		('lpValueName', PRRP_UNICODE_STRING),
    )

class BaseRegDeleteValueResponse(NDRCALL):
    structure = (

    )
        

class BaseRegEnumKey(NDRCALL):
    opnum = 9
    structure = (
		('hKey', RPC_HKEY),
		('dwIndex', DWORD),
		('lpNameIn', PRRP_UNICODE_STRING),
		('lpClassIn', PRRP_UNICODE_STRING),
		('lpftLastWriteTime', PFILETIME),
    )

class BaseRegEnumKeyResponse(NDRCALL):
    structure = (
		('lpNameOut', PRRP_UNICODE_STRING),
		('lplpClassOut', PRPC_UNICODE_STRING),
		('lpftLastWriteTime', PFILETIME),
    )
        

class BaseRegEnumValue(NDRCALL):
    opnum = 10
    structure = (
		('hKey', RPC_HKEY),
		('dwIndex', DWORD),
		('lpValueNameIn', PRRP_UNICODE_STRING),
		('lpType', LPDWORD),
		('lpData', LPBYTE),
		('lpcbData', LPDWORD),
		('lpcbLen', LPDWORD),
    )

class BaseRegEnumValueResponse(NDRCALL):
    structure = (
		('lpValueNameOut', PRPC_UNICODE_STRING),
		('lpType', LPDWORD),
		('lpData', LPBYTE),
		('lpcbData', LPDWORD),
		('lpcbLen', LPDWORD),
    )
        

class BaseRegFlushKey(NDRCALL):
    opnum = 11
    structure = (
		('hKey', RPC_HKEY),
    )

class BaseRegFlushKeyResponse(NDRCALL):
    structure = (

    )
        

class BaseRegGetKeySecurity(NDRCALL):
    opnum = 12
    structure = (
		('hKey', RPC_HKEY),
		('SecurityInformation', SECURITY_INFORMATION),
		('pRpcSecurityDescriptorIn', PRPC_SECURITY_DESCRIPTOR),
    )

class BaseRegGetKeySecurityResponse(NDRCALL):
    structure = (
		('pRpcSecurityDescriptorOut', PRPC_SECURITY_DESCRIPTOR),
    )
        

class BaseRegLoadKey(NDRCALL):
    opnum = 13
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
		('lpFile', PRRP_UNICODE_STRING),
    )

class BaseRegLoadKeyResponse(NDRCALL):
    structure = (

    )
        

class Opnum14NotImplemented(NDRCALL):
    opnum = 14
    structure = (

    )

class Opnum14NotImplementedResponse(NDRCALL):
    structure = (

    )
        

class BaseRegOpenKey(NDRCALL):
    opnum = 15
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
		('dwOptions', DWORD),
		('samDesired', REGSAM),
    )

class BaseRegOpenKeyResponse(NDRCALL):
    structure = (
		('phkResult', PRPC_HKEY),
    )
        

class BaseRegQueryInfoKey(NDRCALL):
    opnum = 16
    structure = (
		('hKey', RPC_HKEY),
		('lpClassIn', PRRP_UNICODE_STRING),
    )

class BaseRegQueryInfoKeyResponse(NDRCALL):
    structure = (
		('lpClassOut', PRPC_UNICODE_STRING),
		('lpcSubKeys', LPDWORD),
		('lpcbMaxSubKeyLen', LPDWORD),
		('lpcbMaxClassLen', LPDWORD),
		('lpcValues', LPDWORD),
		('lpcbMaxValueNameLen', LPDWORD),
		('lpcbMaxValueLen', LPDWORD),
		('lpcbSecurityDescriptor', LPDWORD),
		('lpftLastWriteTime', PFILETIME),
    )
        

class BaseRegQueryValue(NDRCALL):
    opnum = 17
    structure = (
		('hKey', RPC_HKEY),
		('lpValueName', PRRP_UNICODE_STRING),
		('lpType', LPDWORD),
		('lpData', LPBYTE),
		('lpcbData', LPDWORD),
		('lpcbLen', LPDWORD),
    )

class BaseRegQueryValueResponse(NDRCALL):
    structure = (
		('lpType', LPDWORD),
		('lpData', LPBYTE),
		('lpcbData', LPDWORD),
		('lpcbLen', LPDWORD),
    )
        

class BaseRegReplaceKey(NDRCALL):
    opnum = 18
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
		('lpNewFile', PRRP_UNICODE_STRING),
		('lpOldFile', PRRP_UNICODE_STRING),
    )

class BaseRegReplaceKeyResponse(NDRCALL):
    structure = (

    )
        

class BaseRegRestoreKey(NDRCALL):
    opnum = 19
    structure = (
		('hKey', RPC_HKEY),
		('lpFile', PRRP_UNICODE_STRING),
		('Flags', DWORD),
    )

class BaseRegRestoreKeyResponse(NDRCALL):
    structure = (

    )
        

class BaseRegSaveKey(NDRCALL):
    opnum = 20
    structure = (
		('hKey', RPC_HKEY),
		('lpFile', PRRP_UNICODE_STRING),
		('pSecurityAttributes', PRPC_SECURITY_ATTRIBUTES),
    )

class BaseRegSaveKeyResponse(NDRCALL):
    structure = (

    )
        

class BaseRegSetKeySecurity(NDRCALL):
    opnum = 21
    structure = (
		('hKey', RPC_HKEY),
		('SecurityInformation', SECURITY_INFORMATION),
		('pRpcSecurityDescriptor', PRPC_SECURITY_DESCRIPTOR),
    )

class BaseRegSetKeySecurityResponse(NDRCALL):
    structure = (

    )
        

class BaseRegSetValue(NDRCALL):
    opnum = 22
    structure = (
		('hKey', RPC_HKEY),
		('lpValueName', PRRP_UNICODE_STRING),
		('dwType', DWORD),
		('lpData', LPBYTE),
		('cbData', DWORD),
    )

class BaseRegSetValueResponse(NDRCALL):
    structure = (

    )
        

class BaseRegUnLoadKey(NDRCALL):
    opnum = 23
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
    )

class BaseRegUnLoadKeyResponse(NDRCALL):
    structure = (

    )
        

class Opnum24NotImplemented(NDRCALL):
    opnum = 24
    structure = (

    )

class Opnum24NotImplementedResponse(NDRCALL):
    structure = (

    )
        

class Opnum25NotImplemented(NDRCALL):
    opnum = 25
    structure = (

    )

class Opnum25NotImplementedResponse(NDRCALL):
    structure = (

    )
        

class BaseRegGetVersion(NDRCALL):
    opnum = 26
    structure = (
		('hKey', RPC_HKEY),
    )

class BaseRegGetVersionResponse(NDRCALL):
    structure = (
		('lpdwVersion', LPDWORD),
    )
        

class OpenCurrentConfig(NDRCALL):
    opnum = 27
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenCurrentConfigResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class Opnum28NotImplemented(NDRCALL):
    opnum = 28
    structure = (

    )

class Opnum28NotImplementedResponse(NDRCALL):
    structure = (

    )
        

class BaseRegQueryMultipleValues(NDRCALL):
    opnum = 29
    structure = (
		('hKey', RPC_HKEY),
		('val_listIn', PRVALENT),
		('num_vals', DWORD),
		('lpvalueBuf', CHAR),
		('ldwTotsize', LPDWORD),
    )

class BaseRegQueryMultipleValuesResponse(NDRCALL):
    structure = (
		('val_listOut', PRVALENT),
		('lpvalueBuf', CHAR),
		('ldwTotsize', LPDWORD),
    )
        

class Opnum30NotImplemented(NDRCALL):
    opnum = 30
    structure = (

    )

class Opnum30NotImplementedResponse(NDRCALL):
    structure = (

    )
        

class BaseRegSaveKeyEx(NDRCALL):
    opnum = 31
    structure = (
		('hKey', RPC_HKEY),
		('lpFile', PRRP_UNICODE_STRING),
		('pSecurityAttributes', PRPC_SECURITY_ATTRIBUTES),
		('Flags', DWORD),
    )

class BaseRegSaveKeyExResponse(NDRCALL):
    structure = (

    )
        

class OpenPerformanceText(NDRCALL):
    opnum = 32
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenPerformanceTextResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class OpenPerformanceNlsText(NDRCALL):
    opnum = 33
    structure = (
		('ServerName', PREGISTRY_SERVER_NAME),
		('samDesired', REGSAM),
    )

class OpenPerformanceNlsTextResponse(NDRCALL):
    structure = (
		('phKey', PRPC_HKEY),
    )
        

class BaseRegQueryMultipleValues2(NDRCALL):
    opnum = 34
    structure = (
		('hKey', RPC_HKEY),
		('val_listIn', PRVALENT),
		('num_vals', DWORD),
		('lpvalueBuf', CHAR),
		('ldwTotsize', LPDWORD),
    )

class BaseRegQueryMultipleValues2Response(NDRCALL):
    structure = (
		('val_listOut', PRVALENT),
		('lpvalueBuf', CHAR),
		('ldwRequiredSize', LPDWORD),
    )
        

class BaseRegDeleteKeyEx(NDRCALL):
    opnum = 35
    structure = (
		('hKey', RPC_HKEY),
		('lpSubKey', PRRP_UNICODE_STRING),
		('AccessMask', REGSAM),
		('Reserved', DWORD),
    )

class BaseRegDeleteKeyExResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OpenClassesRoot,OpenClassesRootResponse),
1 : (OpenCurrentUser,OpenCurrentUserResponse),
2 : (OpenLocalMachine,OpenLocalMachineResponse),
3 : (OpenPerformanceData,OpenPerformanceDataResponse),
4 : (OpenUsers,OpenUsersResponse),
5 : (BaseRegCloseKey,BaseRegCloseKeyResponse),
6 : (BaseRegCreateKey,BaseRegCreateKeyResponse),
7 : (BaseRegDeleteKey,BaseRegDeleteKeyResponse),
8 : (BaseRegDeleteValue,BaseRegDeleteValueResponse),
9 : (BaseRegEnumKey,BaseRegEnumKeyResponse),
10 : (BaseRegEnumValue,BaseRegEnumValueResponse),
11 : (BaseRegFlushKey,BaseRegFlushKeyResponse),
12 : (BaseRegGetKeySecurity,BaseRegGetKeySecurityResponse),
13 : (BaseRegLoadKey,BaseRegLoadKeyResponse),
14 : (Opnum14NotImplemented,Opnum14NotImplementedResponse),
15 : (BaseRegOpenKey,BaseRegOpenKeyResponse),
16 : (BaseRegQueryInfoKey,BaseRegQueryInfoKeyResponse),
17 : (BaseRegQueryValue,BaseRegQueryValueResponse),
18 : (BaseRegReplaceKey,BaseRegReplaceKeyResponse),
19 : (BaseRegRestoreKey,BaseRegRestoreKeyResponse),
20 : (BaseRegSaveKey,BaseRegSaveKeyResponse),
21 : (BaseRegSetKeySecurity,BaseRegSetKeySecurityResponse),
22 : (BaseRegSetValue,BaseRegSetValueResponse),
23 : (BaseRegUnLoadKey,BaseRegUnLoadKeyResponse),
24 : (Opnum24NotImplemented,Opnum24NotImplementedResponse),
25 : (Opnum25NotImplemented,Opnum25NotImplementedResponse),
26 : (BaseRegGetVersion,BaseRegGetVersionResponse),
27 : (OpenCurrentConfig,OpenCurrentConfigResponse),
28 : (Opnum28NotImplemented,Opnum28NotImplementedResponse),
29 : (BaseRegQueryMultipleValues,BaseRegQueryMultipleValuesResponse),
30 : (Opnum30NotImplemented,Opnum30NotImplementedResponse),
31 : (BaseRegSaveKeyEx,BaseRegSaveKeyExResponse),
32 : (OpenPerformanceText,OpenPerformanceTextResponse),
33 : (OpenPerformanceNlsText,OpenPerformanceNlsTextResponse),
34 : (BaseRegQueryMultipleValues2,BaseRegQueryMultipleValues2Response),
35 : (BaseRegDeleteKeyEx,BaseRegDeleteKeyExResponse),
}

