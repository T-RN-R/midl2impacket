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

#TYPEDEFS

#################################################################################

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#svcctl Definition

#################################################################################

MSRPC_UUID_SVCCTL = uuidtup_to_bin(('367ABB81-9844-35F1-AD32-98F038001003','0.0'))

MAX_SERVICE_NAME_LENGTH =  UNSIGNED INT
SC_MAX_DEPEND_SIZE =  UNSIGNED SHORT
SC_MAX_NAME_LENGTH =  UNSIGNED SHORT
SC_MAX_PATH_LENGTH =  UNSIGNED SHORT
SC_MAX_PWD_SIZE =  UNSIGNED SHORT
SC_MAX_COMPUTER_NAME_LENGTH =  UNSIGNED SHORT
SC_MAX_ACCOUNT_NAME_LENGTH =  UNSIGNED SHORT
SC_MAX_COMMENT_LENGTH =  UNSIGNED SHORT
SC_MAX_ARGUMENT_LENGTH =  UNSIGNED SHORT
SC_MAX_ARGUMENTS =  UNSIGNED SHORT
SVCCTL_HANDLEW = WCHAR_T
SVCCTL_HANDLEA = LPSTR
SC_RPC_HANDLE = PVOID
SC_RPC_LOCK = PVOID
SC_NOTIFY_RPC_HANDLE = PVOID
LPSC_RPC_HANDLE = SC_RPC_HANDLE
LPSC_RPC_LOCK = SC_RPC_LOCK
LPSC_NOTIFY_RPC_HANDLE = SC_NOTIFY_RPC_HANDLE

class STRING_PTRSA(NDRSTRUCT):
    structure = (
        ('StringPtr', LPSTR),
    )
class PSTRING_PTRSA(NDRPOINTER):
    referent = (
        ('Data', STRING_PTRSA),
    )    
class LPSTRING_PTRSA(NDRPOINTER):
    referent = (
        ('Data', STRING_PTRSA),
    )    


class STRING_PTRSW(NDRSTRUCT):
    structure = (
        ('StringPtr', WCHAR_T),
    )
class PSTRING_PTRSW(NDRPOINTER):
    referent = (
        ('Data', STRING_PTRSW),
    )    
class LPSTRING_PTRSW(NDRPOINTER):
    referent = (
        ('Data', STRING_PTRSW),
    )    

BOUNDED_DWORD_4K = DWORD
LPBOUNDED_DWORD_4K = BOUNDED_DWORD_4K
BOUNDED_DWORD_8K = DWORD
LPBOUNDED_DWORD_8K = BOUNDED_DWORD_8K
BOUNDED_DWORD_256K = DWORD
LPBOUNDED_DWORD_256K = BOUNDED_DWORD_256K

class SERVICE_STATUS(NDRSTRUCT):
    structure = (
        ('dwServiceType', DWORD),('dwCurrentState', DWORD),('dwControlsAccepted', DWORD),('dwWin32ExitCode', DWORD),('dwServiceSpecificExitCode', DWORD),('dwCheckPoint', DWORD),('dwWaitHint', DWORD),
    )
class LPSERVICE_STATUS(NDRPOINTER):
    referent = (
        ('Data', SERVICE_STATUS),
    )    


class SERVICE_STATUS_PROCESS(NDRSTRUCT):
    structure = (
        ('dwServiceType', DWORD),('dwCurrentState', DWORD),('dwControlsAccepted', DWORD),('dwWin32ExitCode', DWORD),('dwServiceSpecificExitCode', DWORD),('dwCheckPoint', DWORD),('dwWaitHint', DWORD),('dwProcessId', DWORD),('dwServiceFlags', DWORD),
    )
class LPSERVICE_STATUS_PROCESS(NDRPOINTER):
    referent = (
        ('Data', SERVICE_STATUS_PROCESS),
    )    


class QUERY_SERVICE_CONFIGW(NDRSTRUCT):
    structure = (
        ('dwServiceType', DWORD),('dwStartType', DWORD),('dwErrorControl', DWORD),('lpBinaryPathName', LPWSTR),('lpLoadOrderGroup', LPWSTR),('dwTagId', DWORD),('lpDependencies', LPWSTR),('lpServiceStartName', LPWSTR),('lpDisplayName', LPWSTR),
    )
class LPQUERY_SERVICE_CONFIGW(NDRPOINTER):
    referent = (
        ('Data', QUERY_SERVICE_CONFIGW),
    )    


class QUERY_SERVICE_LOCK_STATUSW(NDRSTRUCT):
    structure = (
        ('fIsLocked', DWORD),('lpLockOwner', LPWSTR),('dwLockDuration', DWORD),
    )
class LPQUERY_SERVICE_LOCK_STATUSW(NDRPOINTER):
    referent = (
        ('Data', QUERY_SERVICE_LOCK_STATUSW),
    )    


class QUERY_SERVICE_CONFIGA(NDRSTRUCT):
    structure = (
        ('dwServiceType', DWORD),('dwStartType', DWORD),('dwErrorControl', DWORD),('lpBinaryPathName', LPSTR),('lpLoadOrderGroup', LPSTR),('dwTagId', DWORD),('lpDependencies', LPSTR),('lpServiceStartName', LPSTR),('lpDisplayName', LPSTR),
    )
class LPQUERY_SERVICE_CONFIGA(NDRPOINTER):
    referent = (
        ('Data', QUERY_SERVICE_CONFIGA),
    )    


class QUERY_SERVICE_LOCK_STATUSA(NDRSTRUCT):
    structure = (
        ('fIsLocked', DWORD),('lpLockOwner', CHAR),('dwLockDuration', DWORD),
    )
class LPQUERY_SERVICE_LOCK_STATUSA(NDRPOINTER):
    referent = (
        ('Data', QUERY_SERVICE_LOCK_STATUSA),
    )    


class SERVICE_DESCRIPTIONA(NDRSTRUCT):
    structure = (
        ('lpDescription', LPSTR),
    )
class LPSERVICE_DESCRIPTIONA(NDRPOINTER):
    referent = (
        ('Data', SERVICE_DESCRIPTIONA),
    )    


SC_ACTION_NONE = 0,
SC_ACTION_RESTART = 1,
SC_ACTION_REBOOT = 2,
SC_ACTION_RUN_COMMAND = 3
        

class SC_ACTION(NDRSTRUCT):
    structure = (
        ('Type', SC_ACTION_TYPE),('Delay', DWORD),
    )
class LPSC_ACTION(NDRPOINTER):
    referent = (
        ('Data', SC_ACTION),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = SC_ACTION

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('dwResetPeriod', DWORD),	('lpRebootMsg', LPSTR),	('lpCommand', LPSTR),	('cActions', DWORD),	('lpsaActions', PTR_DWORD),

    )
        

class SERVICE_DELAYED_AUTO_START_INFO(NDRSTRUCT):
    structure = (
        ('fDelayedAutostart', BOOL),
    )
class LPSERVICE_DELAYED_AUTO_START_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_DELAYED_AUTO_START_INFO),
    )    


class SERVICE_FAILURE_ACTIONS_FLAG(NDRSTRUCT):
    structure = (
        ('fFailureActionsOnNonCrashFailures', BOOL),
    )
class LPSERVICE_FAILURE_ACTIONS_FLAG(NDRPOINTER):
    referent = (
        ('Data', SERVICE_FAILURE_ACTIONS_FLAG),
    )    


class SERVICE_SID_INFO(NDRSTRUCT):
    structure = (
        ('dwServiceSidType', DWORD),
    )
class LPSERVICE_SID_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_SID_INFO),
    )    


class SERVICE_PRESHUTDOWN_INFO(NDRSTRUCT):
    structure = (
        ('dwPreshutdownTimeout', DWORD),
    )
class LPSERVICE_PRESHUTDOWN_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_PRESHUTDOWN_INFO),
    )    


class SERVICE_DESCRIPTIONW(NDRSTRUCT):
    structure = (
        ('lpDescription', LPWSTR),
    )
class LPSERVICE_DESCRIPTIONW(NDRPOINTER):
    referent = (
        ('Data', SERVICE_DESCRIPTIONW),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = SC_ACTION

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('dwResetPeriod', DWORD),	('lpRebootMsg', LPWSTR),	('lpCommand', LPWSTR),	('cActions', DWORD),	('lpsaActions', PTR_DWORD),

    )
        

SC_STATUS_PROCESS_INFO = 0
        

SC_ENUM_PROCESS_INFO = 0
        

class SERVICE_PREFERRED_NODE_INFO(NDRSTRUCT):
    structure = (
        ('usPreferredNode', USHORT),('fDelete', BOOLEAN),
    )
class LPSERVICE_PREFERRED_NODE_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_PREFERRED_NODE_INFO),
    )    


class SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(NDRSTRUCT):
    structure = (
        ('dwDataType', DWORD),('cbData', DWORD),('pData', PBYTE),
    )
class PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM(NDRPOINTER):
    referent = (
        ('Data', SERVICE_TRIGGER_SPECIFIC_DATA_ITEM),
    )    


class SERVICE_TRIGGER(NDRSTRUCT):
    structure = (
        ('dwTriggerType', DWORD),('dwAction', DWORD),('pTriggerSubtype', GUID),('cDataItems', DWORD),('pDataItems', PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM),
    )
class PSERVICE_TRIGGER(NDRPOINTER):
    referent = (
        ('Data', SERVICE_TRIGGER),
    )    


class SERVICE_TRIGGER_INFO(NDRSTRUCT):
    structure = (
        ('cTriggers', DWORD),('pTriggers', PSERVICE_TRIGGER),('pReserved', PBYTE),
    )
class PSERVICE_TRIGGER_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_TRIGGER_INFO),
    )    

SECURITY_INFORMATION = ULONG
PSECURITY_INFORMATION = ULONG

class ENUM_SERVICE_STATUSA(NDRSTRUCT):
    structure = (
        ('lpServiceName', LPSTR),('lpDisplayName', LPSTR),('ServiceStatus', SERVICE_STATUS),
    )
class LPENUM_SERVICE_STATUSA(NDRPOINTER):
    referent = (
        ('Data', ENUM_SERVICE_STATUSA),
    )    


class ENUM_SERVICE_STATUSW(NDRSTRUCT):
    structure = (
        ('lpServiceName', LPWSTR),('lpDisplayName', LPWSTR),('ServiceStatus', SERVICE_STATUS),
    )
class LPENUM_SERVICE_STATUSW(NDRPOINTER):
    referent = (
        ('Data', ENUM_SERVICE_STATUSW),
    )    


class ENUM_SERVICE_STATUS_PROCESSA(NDRSTRUCT):
    structure = (
        ('lpServiceName', LPSTR),('lpDisplayName', LPSTR),('ServiceStatusProcess', SERVICE_STATUS_PROCESS),
    )
class LPENUM_SERVICE_STATUS_PROCESSA(NDRPOINTER):
    referent = (
        ('Data', ENUM_SERVICE_STATUS_PROCESSA),
    )    


class ENUM_SERVICE_STATUS_PROCESSW(NDRSTRUCT):
    structure = (
        ('lpServiceName', LPWSTR),('lpDisplayName', LPWSTR),('ServiceStatusProcess', SERVICE_STATUS_PROCESS),
    )
class LPENUM_SERVICE_STATUS_PROCESSW(NDRPOINTER):
    referent = (
        ('Data', ENUM_SERVICE_STATUS_PROCESSW),
    )    


class SERVICE_DESCRIPTION_WOW64(NDRSTRUCT):
    structure = (
        ('dwDescriptionOffset', DWORD),
    )
class LPSERVICE_DESCRIPTION_WOW64(NDRPOINTER):
    referent = (
        ('Data', SERVICE_DESCRIPTION_WOW64),
    )    


class SERVICE_FAILURE_ACTIONS_WOW64(NDRSTRUCT):
    structure = (
        ('dwResetPeriod', DWORD),('dwRebootMsgOffset', DWORD),('dwCommandOffset', DWORD),('cActions', DWORD),('dwsaActionsOffset', DWORD),
    )
class LPSERVICE_FAILURE_ACTIONS_WOW64(NDRPOINTER):
    referent = (
        ('Data', SERVICE_FAILURE_ACTIONS_WOW64),
    )    


class SERVICE_REQUIRED_PRIVILEGES_INFO_WOW64(NDRSTRUCT):
    structure = (
        ('dwRequiredPrivilegesOffset', DWORD),
    )
class LPSERVICE_REQUIRED_PRIVILEGES_INFO_WOW64(NDRPOINTER):
    referent = (
        ('Data', SERVICE_REQUIRED_PRIVILEGES_INFO_WOW64),
    )    


class SERVICE_RPC_REQUIRED_PRIVILEGES_INFO(NDRSTRUCT):
    structure = (
        ('cbRequiredPrivileges', DWORD),('pRequiredPrivileges', PBYTE),
    )
class LPSERVICE_RPC_REQUIRED_PRIVILEGES_INFO(NDRPOINTER):
    referent = (
        ('Data', SERVICE_RPC_REQUIRED_PRIVILEGES_INFO),
    )    


class U0(NDRUNION):
    union = {
        1: ('psd',LPSERVICE_DESCRIPTIONA),2: ('psfa',LPSERVICE_FAILURE_ACTIONSA),3: ('psda',LPSERVICE_DELAYED_AUTO_START_INFO),4: ('psfaf',LPSERVICE_FAILURE_ACTIONS_FLAG),5: ('pssid',LPSERVICE_SID_INFO),6: ('psrp',LPSERVICE_RPC_REQUIRED_PRIVILEGES_INFO),7: ('psps',LPSERVICE_PRESHUTDOWN_INFO),8: ('psti',PSERVICE_TRIGGER_INFO),9: ('pspn',LPSERVICE_PREFERRED_NODE_INFO),
    }
        

class SC_RPC_CONFIG_INFOA(NDRSTRUCT):
    structure = (
        ('dwInfoLevel', DWORD),('u0', U0),
    )


class U0(NDRUNION):
    union = {
        1: ('psd',LPSERVICE_DESCRIPTIONW),2: ('psfa',LPSERVICE_FAILURE_ACTIONSW),3: ('psda',LPSERVICE_DELAYED_AUTO_START_INFO),4: ('psfaf',LPSERVICE_FAILURE_ACTIONS_FLAG),5: ('pssid',LPSERVICE_SID_INFO),6: ('psrp',LPSERVICE_RPC_REQUIRED_PRIVILEGES_INFO),7: ('psps',LPSERVICE_PRESHUTDOWN_INFO),8: ('psti',PSERVICE_TRIGGER_INFO),9: ('pspn',LPSERVICE_PREFERRED_NODE_INFO),
    }
        

class SC_RPC_CONFIG_INFOW(NDRSTRUCT):
    structure = (
        ('dwInfoLevel', DWORD),('u0', U0),
    )


class SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1(NDRSTRUCT):
    structure = (
        ('ullThreadId', ULONGLONG),('dwNotifyMask', DWORD),('CallbackAddressArray', UCHAR),('CallbackParamAddressArray', UCHAR),('ServiceStatus', SERVICE_STATUS_PROCESS),('dwNotificationStatus', DWORD),('dwSequence', DWORD),
    )
class PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1(NDRPOINTER):
    referent = (
        ('Data', SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1),
    )    


class SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2(NDRSTRUCT):
    structure = (
        ('ullThreadId', ULONGLONG),('dwNotifyMask', DWORD),('CallbackAddressArray', UCHAR),('CallbackParamAddressArray', UCHAR),('ServiceStatus', SERVICE_STATUS_PROCESS),('dwNotificationStatus', DWORD),('dwSequence', DWORD),('dwNotificationTriggered', DWORD),('pszServiceNames', PWSTR),
    )
class PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2(NDRPOINTER):
    referent = (
        ('Data', SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2),
    )    

SERVICE_NOTIFY_STATUS_CHANGE_PARAMS = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2
PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2

class U0(NDRUNION):
    union = {
        1: ('pStatusChangeParam1',PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1),2: ('pStatusChangeParams',PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2),
    }
        

class SC_RPC_NOTIFY_PARAMS(NDRSTRUCT):
    structure = (
        ('dwInfoLevel', DWORD),('u0', U0),
    )


class SC_RPC_NOTIFY_PARAMS_LIST(NDRSTRUCT):
    structure = (
        ('cElements', BOUNDED_DWORD_4K),('NotifyParamsArray', SC_RPC_NOTIFY_PARAMS),
    )
class PSC_RPC_NOTIFY_PARAMS_LIST(NDRPOINTER):
    referent = (
        ('Data', SC_RPC_NOTIFY_PARAMS_LIST),
    )    


class SERVICE_CONTROL_STATUS_REASON_IN_PARAMSA(NDRSTRUCT):
    structure = (
        ('dwReason', DWORD),('pszComment', LPSTR),
    )
class PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSA(NDRPOINTER):
    referent = (
        ('Data', SERVICE_CONTROL_STATUS_REASON_IN_PARAMSA),
    )    


class SERVICE_CONTROL_STATUS_REASON_OUT_PARAMS(NDRSTRUCT):
    structure = (
        ('ServiceStatus', SERVICE_STATUS_PROCESS),
    )
class PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS(NDRPOINTER):
    referent = (
        ('Data', SERVICE_CONTROL_STATUS_REASON_OUT_PARAMS),
    )    


class SC_RPC_SERVICE_CONTROL_IN_PARAMSA(NDRUNION):
    union = {
        1: ('psrInParams',PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSA),
    }
        class PSC_RPC_SERVICE_CONTROL_IN_PARAMSA(NDRPOINTER):
    referent = (
        ('Data', SC_RPC_SERVICE_CONTROL_IN_PARAMSA),
    )    


class SC_RPC_SERVICE_CONTROL_OUT_PARAMSA(NDRUNION):
    union = {
        1: ('psrOutParams',PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS),
    }
        class PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA(NDRPOINTER):
    referent = (
        ('Data', SC_RPC_SERVICE_CONTROL_OUT_PARAMSA),
    )    


class SERVICE_CONTROL_STATUS_REASON_IN_PARAMSW(NDRSTRUCT):
    structure = (
        ('dwReason', DWORD),('pszComment', LPWSTR),
    )
class PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSW(NDRPOINTER):
    referent = (
        ('Data', SERVICE_CONTROL_STATUS_REASON_IN_PARAMSW),
    )    


class SC_RPC_SERVICE_CONTROL_IN_PARAMSW(NDRUNION):
    union = {
        1: ('psrInParams',PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSW),
    }
        class PSC_RPC_SERVICE_CONTROL_IN_PARAMSW(NDRPOINTER):
    referent = (
        ('Data', SC_RPC_SERVICE_CONTROL_IN_PARAMSW),
    )    


class SC_RPC_SERVICE_CONTROL_OUT_PARAMSW(NDRUNION):
    union = {
        1: ('psrOutParams',PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS),
    }
        class PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW(NDRPOINTER):
    referent = (
        ('Data', SC_RPC_SERVICE_CONTROL_OUT_PARAMSW),
    )    


class RCloseServiceHandle(NDRCALL):
    opnum = 0
    structure = (
		('hSCObject', LPSC_RPC_HANDLE),
    )

class RCloseServiceHandleResponse(NDRCALL):
    structure = (
		('hSCObject', LPSC_RPC_HANDLE),
    )
        

class RControlService(NDRCALL):
    opnum = 1
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwControl', DWORD),
    )

class RControlServiceResponse(NDRCALL):
    structure = (
		('lpServiceStatus', LPSERVICE_STATUS),
    )
        

class RDeleteService(NDRCALL):
    opnum = 2
    structure = (
		('hService', SC_RPC_HANDLE),
    )

class RDeleteServiceResponse(NDRCALL):
    structure = (

    )
        

class RLockServiceDatabase(NDRCALL):
    opnum = 3
    structure = (
		('hSCManager', SC_RPC_HANDLE),
    )

class RLockServiceDatabaseResponse(NDRCALL):
    structure = (
		('lpLock', LPSC_RPC_LOCK),
    )
        

class RQueryServiceObjectSecurity(NDRCALL):
    opnum = 4
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwSecurityInformation', SECURITY_INFORMATION),
		('cbBufSize', DWORD),
    )

class RQueryServiceObjectSecurityResponse(NDRCALL):
    structure = (
		('lpSecurityDescriptor', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
    )
        

class RSetServiceObjectSecurity(NDRCALL):
    opnum = 5
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwSecurityInformation', SECURITY_INFORMATION),
		('lpSecurityDescriptor', LPBYTE),
		('cbBufSize', DWORD),
    )

class RSetServiceObjectSecurityResponse(NDRCALL):
    structure = (

    )
        

class RQueryServiceStatus(NDRCALL):
    opnum = 6
    structure = (
		('hService', SC_RPC_HANDLE),
    )

class RQueryServiceStatusResponse(NDRCALL):
    structure = (
		('lpServiceStatus', LPSERVICE_STATUS),
    )
        

class RSetServiceStatus(NDRCALL):
    opnum = 7
    structure = (
		('hServiceStatus', SC_RPC_HANDLE),
		('lpServiceStatus', LPSERVICE_STATUS),
    )

class RSetServiceStatusResponse(NDRCALL):
    structure = (

    )
        

class RUnlockServiceDatabase(NDRCALL):
    opnum = 8
    structure = (
		('Lock', LPSC_RPC_LOCK),
    )

class RUnlockServiceDatabaseResponse(NDRCALL):
    structure = (
		('Lock', LPSC_RPC_LOCK),
    )
        

class RNotifyBootConfigStatus(NDRCALL):
    opnum = 9
    structure = (
		('lpMachineName', SVCCTL_HANDLEW),
		('BootAcceptable', DWORD),
    )

class RNotifyBootConfigStatusResponse(NDRCALL):
    structure = (

    )
        

class Opnum10NotUsedOnWire(NDRCALL):
    opnum = 10
    structure = (

    )

class Opnum10NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RChangeServiceConfigW(NDRCALL):
    opnum = 11
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', WCHAR_T),
		('lpLoadOrderGroup', WCHAR_T),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', WCHAR_T),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
		('lpDisplayName', WCHAR_T),
    )

class RChangeServiceConfigWResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
    )
        

class RCreateServiceW(NDRCALL):
    opnum = 12
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', WCHAR_T),
		('lpDisplayName', WCHAR_T),
		('dwDesiredAccess', DWORD),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', WCHAR_T),
		('lpLoadOrderGroup', WCHAR_T),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', WCHAR_T),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
    )

class RCreateServiceWResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class REnumDependentServicesW(NDRCALL):
    opnum = 13
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
    )

class REnumDependentServicesWResponse(NDRCALL):
    structure = (
		('lpServices', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
    )
        

class REnumServicesStatusW(NDRCALL):
    opnum = 14
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('dwServiceType', DWORD),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )

class REnumServicesStatusWResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )
        

class ROpenSCManagerW(NDRCALL):
    opnum = 15
    structure = (
		('lpMachineName', SVCCTL_HANDLEW),
		('lpDatabaseName', WCHAR_T),
		('dwDesiredAccess', DWORD),
    )

class ROpenSCManagerWResponse(NDRCALL):
    structure = (
		('lpScHandle', LPSC_RPC_HANDLE),
    )
        

class ROpenServiceW(NDRCALL):
    opnum = 16
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', WCHAR_T),
		('dwDesiredAccess', DWORD),
    )

class ROpenServiceWResponse(NDRCALL):
    structure = (
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class RQueryServiceConfigW(NDRCALL):
    opnum = 17
    structure = (
		('hService', SC_RPC_HANDLE),
		('cbBufSize', DWORD),
    )

class RQueryServiceConfigWResponse(NDRCALL):
    structure = (
		('lpServiceConfig', LPQUERY_SERVICE_CONFIGW),
		('pcbBytesNeeded', LPBOUNDED_DWORD_8K),
    )
        

class RQueryServiceLockStatusW(NDRCALL):
    opnum = 18
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('cbBufSize', DWORD),
    )

class RQueryServiceLockStatusWResponse(NDRCALL):
    structure = (
		('lpLockStatus', LPQUERY_SERVICE_LOCK_STATUSW),
		('pcbBytesNeeded', LPBOUNDED_DWORD_4K),
    )
        

class RStartServiceW(NDRCALL):
    opnum = 19
    structure = (
		('hService', SC_RPC_HANDLE),
		('argc', DWORD),
		('argv', LPSTRING_PTRSW),
    )

class RStartServiceWResponse(NDRCALL):
    structure = (

    )
        

class RGetServiceDisplayNameW(NDRCALL):
    opnum = 20
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', WCHAR_T),
		('lpcchBuffer', DWORD),
    )

class RGetServiceDisplayNameWResponse(NDRCALL):
    structure = (
		('lpDisplayName', WCHAR_T),
		('lpcchBuffer', DWORD),
    )
        

class RGetServiceKeyNameW(NDRCALL):
    opnum = 21
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpDisplayName', WCHAR_T),
		('lpcchBuffer', DWORD),
    )

class RGetServiceKeyNameWResponse(NDRCALL):
    structure = (
		('lpServiceName', WCHAR_T),
		('lpcchBuffer', DWORD),
    )
        

class Opnum22NotUsedOnWire(NDRCALL):
    opnum = 22
    structure = (

    )

class Opnum22NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RChangeServiceConfigA(NDRCALL):
    opnum = 23
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', LPSTR),
		('lpLoadOrderGroup', LPSTR),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', LPSTR),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
		('lpDisplayName', LPSTR),
    )

class RChangeServiceConfigAResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
    )
        

class RCreateServiceA(NDRCALL):
    opnum = 24
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', LPSTR),
		('lpDisplayName', LPSTR),
		('dwDesiredAccess', DWORD),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', LPSTR),
		('lpLoadOrderGroup', LPSTR),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', LPSTR),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
    )

class RCreateServiceAResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class REnumDependentServicesA(NDRCALL):
    opnum = 25
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
    )

class REnumDependentServicesAResponse(NDRCALL):
    structure = (
		('lpServices', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
    )
        

class REnumServicesStatusA(NDRCALL):
    opnum = 26
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('dwServiceType', DWORD),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )

class REnumServicesStatusAResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )
        

class ROpenSCManagerA(NDRCALL):
    opnum = 27
    structure = (
		('lpMachineName', SVCCTL_HANDLEA),
		('lpDatabaseName', LPSTR),
		('dwDesiredAccess', DWORD),
    )

class ROpenSCManagerAResponse(NDRCALL):
    structure = (
		('lpScHandle', LPSC_RPC_HANDLE),
    )
        

class ROpenServiceA(NDRCALL):
    opnum = 28
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', LPSTR),
		('dwDesiredAccess', DWORD),
    )

class ROpenServiceAResponse(NDRCALL):
    structure = (
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class RQueryServiceConfigA(NDRCALL):
    opnum = 29
    structure = (
		('hService', SC_RPC_HANDLE),
		('cbBufSize', DWORD),
    )

class RQueryServiceConfigAResponse(NDRCALL):
    structure = (
		('lpServiceConfig', LPQUERY_SERVICE_CONFIGA),
		('pcbBytesNeeded', LPBOUNDED_DWORD_8K),
    )
        

class RQueryServiceLockStatusA(NDRCALL):
    opnum = 30
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('cbBufSize', DWORD),
    )

class RQueryServiceLockStatusAResponse(NDRCALL):
    structure = (
		('lpLockStatus', LPQUERY_SERVICE_LOCK_STATUSA),
		('pcbBytesNeeded', LPBOUNDED_DWORD_4K),
    )
        

class RStartServiceA(NDRCALL):
    opnum = 31
    structure = (
		('hService', SC_RPC_HANDLE),
		('argc', DWORD),
		('argv', LPSTRING_PTRSA),
    )

class RStartServiceAResponse(NDRCALL):
    structure = (

    )
        

class RGetServiceDisplayNameA(NDRCALL):
    opnum = 32
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', LPSTR),
		('lpcchBuffer', LPBOUNDED_DWORD_4K),
    )

class RGetServiceDisplayNameAResponse(NDRCALL):
    structure = (
		('lpDisplayName', LPSTR),
		('lpcchBuffer', LPBOUNDED_DWORD_4K),
    )
        

class RGetServiceKeyNameA(NDRCALL):
    opnum = 33
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpDisplayName', LPSTR),
		('lpcchBuffer', LPBOUNDED_DWORD_4K),
    )

class RGetServiceKeyNameAResponse(NDRCALL):
    structure = (
		('lpKeyName', LPSTR),
		('lpcchBuffer', LPBOUNDED_DWORD_4K),
    )
        

class Opnum34NotUsedOnWire(NDRCALL):
    opnum = 34
    structure = (

    )

class Opnum34NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class REnumServiceGroupW(NDRCALL):
    opnum = 35
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('dwServiceType', DWORD),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
		('pszGroupName', LPCWSTR),
    )

class REnumServiceGroupWResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )
        

class RChangeServiceConfig2A(NDRCALL):
    opnum = 36
    structure = (
		('hService', SC_RPC_HANDLE),
		('Info', SC_RPC_CONFIG_INFOA),
    )

class RChangeServiceConfig2AResponse(NDRCALL):
    structure = (

    )
        

class RChangeServiceConfig2W(NDRCALL):
    opnum = 37
    structure = (
		('hService', SC_RPC_HANDLE),
		('Info', SC_RPC_CONFIG_INFOW),
    )

class RChangeServiceConfig2WResponse(NDRCALL):
    structure = (

    )
        

class RQueryServiceConfig2A(NDRCALL):
    opnum = 38
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwInfoLevel', DWORD),
		('cbBufSize', DWORD),
    )

class RQueryServiceConfig2AResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_8K),
    )
        

class RQueryServiceConfig2W(NDRCALL):
    opnum = 39
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwInfoLevel', DWORD),
		('cbBufSize', DWORD),
    )

class RQueryServiceConfig2WResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_8K),
    )
        

class RQueryServiceStatusEx(NDRCALL):
    opnum = 40
    structure = (
		('hService', SC_RPC_HANDLE),
		('InfoLevel', SC_STATUS_TYPE),
		('cbBufSize', DWORD),
    )

class RQueryServiceStatusExResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_8K),
    )
        

class REnumServicesStatusExA(NDRCALL):
    opnum = 41
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('InfoLevel', SC_ENUM_TYPE),
		('dwServiceType', DWORD),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
		('pszGroupName', LPCSTR),
    )

class REnumServicesStatusExAResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )
        

class REnumServicesStatusExW(NDRCALL):
    opnum = 42
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('InfoLevel', SC_ENUM_TYPE),
		('dwServiceType', DWORD),
		('dwServiceState', DWORD),
		('cbBufSize', DWORD),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
		('pszGroupName', LPCWSTR),
    )

class REnumServicesStatusExWResponse(NDRCALL):
    structure = (
		('lpBuffer', LPBYTE),
		('pcbBytesNeeded', LPBOUNDED_DWORD_256K),
		('lpServicesReturned', LPBOUNDED_DWORD_256K),
		('lpResumeIndex', LPBOUNDED_DWORD_256K),
    )
        

class Opnum43NotUsedOnWire(NDRCALL):
    opnum = 43
    structure = (

    )

class Opnum43NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RCreateServiceWOW64A(NDRCALL):
    opnum = 44
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', LPSTR),
		('lpDisplayName', LPSTR),
		('dwDesiredAccess', DWORD),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', LPSTR),
		('lpLoadOrderGroup', LPSTR),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', LPSTR),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
    )

class RCreateServiceWOW64AResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class RCreateServiceWOW64W(NDRCALL):
    opnum = 45
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', WCHAR_T),
		('lpDisplayName', WCHAR_T),
		('dwDesiredAccess', DWORD),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', WCHAR_T),
		('lpLoadOrderGroup', WCHAR_T),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', WCHAR_T),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
    )

class RCreateServiceWOW64WResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class Opnum46NotUsedOnWire(NDRCALL):
    opnum = 46
    structure = (

    )

class Opnum46NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RNotifyServiceStatusChange(NDRCALL):
    opnum = 47
    structure = (
		('hService', SC_RPC_HANDLE),
		('NotifyParams', SC_RPC_NOTIFY_PARAMS),
		('pClientProcessGuid', GUID),
    )

class RNotifyServiceStatusChangeResponse(NDRCALL):
    structure = (
		('pSCMProcessGuid', GUID),
		('pfCreateRemoteQueue', PBOOL),
		('phNotify', LPSC_NOTIFY_RPC_HANDLE),
    )
        

class RGetNotifyResults(NDRCALL):
    opnum = 48
    structure = (
		('hNotify', SC_NOTIFY_RPC_HANDLE),
    )

class RGetNotifyResultsResponse(NDRCALL):
    structure = (
		('ppNotifyParams', PSC_RPC_NOTIFY_PARAMS_LIST),
    )
        

class RCloseNotifyHandle(NDRCALL):
    opnum = 49
    structure = (
		('phNotify', LPSC_NOTIFY_RPC_HANDLE),
    )

class RCloseNotifyHandleResponse(NDRCALL):
    structure = (
		('phNotify', LPSC_NOTIFY_RPC_HANDLE),
		('pfApcFired', PBOOL),
    )
        

class RControlServiceExA(NDRCALL):
    opnum = 50
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwControl', DWORD),
		('dwInfoLevel', DWORD),
		('pControlInParams', PSC_RPC_SERVICE_CONTROL_IN_PARAMSA),
    )

class RControlServiceExAResponse(NDRCALL):
    structure = (
		('pControlOutParams', PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA),
    )
        

class RControlServiceExW(NDRCALL):
    opnum = 51
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwControl', DWORD),
		('dwInfoLevel', DWORD),
		('pControlInParams', PSC_RPC_SERVICE_CONTROL_IN_PARAMSW),
    )

class RControlServiceExWResponse(NDRCALL):
    structure = (
		('pControlOutParams', PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW),
    )
        

class Opnum52NotUsedOnWire(NDRCALL):
    opnum = 52
    structure = (

    )

class Opnum52NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum53NotUsedOnWire(NDRCALL):
    opnum = 53
    structure = (

    )

class Opnum53NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum54NotUsedOnWire(NDRCALL):
    opnum = 54
    structure = (

    )

class Opnum54NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum55NotUsedOnWire(NDRCALL):
    opnum = 55
    structure = (

    )

class Opnum55NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RQueryServiceConfigEx(NDRCALL):
    opnum = 56
    structure = (
		('hService', SC_RPC_HANDLE),
		('dwInfoLevel', DWORD),
    )

class RQueryServiceConfigExResponse(NDRCALL):
    structure = (
		('pInfo', SC_RPC_CONFIG_INFOW),
    )
        

class Opnum57NotUsedOnWire(NDRCALL):
    opnum = 57
    structure = (

    )

class Opnum57NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum58NotUsedOnWire(NDRCALL):
    opnum = 58
    structure = (

    )

class Opnum58NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum59NotUsedOnWire(NDRCALL):
    opnum = 59
    structure = (

    )

class Opnum59NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class RCreateWowService(NDRCALL):
    opnum = 60
    structure = (
		('hSCManager', SC_RPC_HANDLE),
		('lpServiceName', WCHAR_T),
		('lpDisplayName', WCHAR_T),
		('dwDesiredAccess', DWORD),
		('dwServiceType', DWORD),
		('dwStartType', DWORD),
		('dwErrorControl', DWORD),
		('lpBinaryPathName', WCHAR_T),
		('lpLoadOrderGroup', WCHAR_T),
		('lpdwTagId', LPDWORD),
		('lpDependencies', LPBYTE),
		('dwDependSize', DWORD),
		('lpServiceStartName', WCHAR_T),
		('lpPassword', LPBYTE),
		('dwPwSize', DWORD),
		('dwServiceWowType', USHORT),
    )

class RCreateWowServiceResponse(NDRCALL):
    structure = (
		('lpdwTagId', LPDWORD),
		('lpServiceHandle', LPSC_RPC_HANDLE),
    )
        

class ROpenSCManager2(NDRCALL):
    opnum = 61
    structure = (
		('BindingHandle', HANDLE_T),
		('DatabaseName', WCHAR_T),
		('DesiredAccess', DWORD),
    )

class ROpenSCManager2Response(NDRCALL):
    structure = (
		('ScmHandle', LPSC_RPC_HANDLE),
    )
        
OPNUMS = {
0 : (RCloseServiceHandle,RCloseServiceHandleResponse),
1 : (RControlService,RControlServiceResponse),
2 : (RDeleteService,RDeleteServiceResponse),
3 : (RLockServiceDatabase,RLockServiceDatabaseResponse),
4 : (RQueryServiceObjectSecurity,RQueryServiceObjectSecurityResponse),
5 : (RSetServiceObjectSecurity,RSetServiceObjectSecurityResponse),
6 : (RQueryServiceStatus,RQueryServiceStatusResponse),
7 : (RSetServiceStatus,RSetServiceStatusResponse),
8 : (RUnlockServiceDatabase,RUnlockServiceDatabaseResponse),
9 : (RNotifyBootConfigStatus,RNotifyBootConfigStatusResponse),
10 : (Opnum10NotUsedOnWire,Opnum10NotUsedOnWireResponse),
11 : (RChangeServiceConfigW,RChangeServiceConfigWResponse),
12 : (RCreateServiceW,RCreateServiceWResponse),
13 : (REnumDependentServicesW,REnumDependentServicesWResponse),
14 : (REnumServicesStatusW,REnumServicesStatusWResponse),
15 : (ROpenSCManagerW,ROpenSCManagerWResponse),
16 : (ROpenServiceW,ROpenServiceWResponse),
17 : (RQueryServiceConfigW,RQueryServiceConfigWResponse),
18 : (RQueryServiceLockStatusW,RQueryServiceLockStatusWResponse),
19 : (RStartServiceW,RStartServiceWResponse),
20 : (RGetServiceDisplayNameW,RGetServiceDisplayNameWResponse),
21 : (RGetServiceKeyNameW,RGetServiceKeyNameWResponse),
22 : (Opnum22NotUsedOnWire,Opnum22NotUsedOnWireResponse),
23 : (RChangeServiceConfigA,RChangeServiceConfigAResponse),
24 : (RCreateServiceA,RCreateServiceAResponse),
25 : (REnumDependentServicesA,REnumDependentServicesAResponse),
26 : (REnumServicesStatusA,REnumServicesStatusAResponse),
27 : (ROpenSCManagerA,ROpenSCManagerAResponse),
28 : (ROpenServiceA,ROpenServiceAResponse),
29 : (RQueryServiceConfigA,RQueryServiceConfigAResponse),
30 : (RQueryServiceLockStatusA,RQueryServiceLockStatusAResponse),
31 : (RStartServiceA,RStartServiceAResponse),
32 : (RGetServiceDisplayNameA,RGetServiceDisplayNameAResponse),
33 : (RGetServiceKeyNameA,RGetServiceKeyNameAResponse),
34 : (Opnum34NotUsedOnWire,Opnum34NotUsedOnWireResponse),
35 : (REnumServiceGroupW,REnumServiceGroupWResponse),
36 : (RChangeServiceConfig2A,RChangeServiceConfig2AResponse),
37 : (RChangeServiceConfig2W,RChangeServiceConfig2WResponse),
38 : (RQueryServiceConfig2A,RQueryServiceConfig2AResponse),
39 : (RQueryServiceConfig2W,RQueryServiceConfig2WResponse),
40 : (RQueryServiceStatusEx,RQueryServiceStatusExResponse),
41 : (REnumServicesStatusExA,REnumServicesStatusExAResponse),
42 : (REnumServicesStatusExW,REnumServicesStatusExWResponse),
43 : (Opnum43NotUsedOnWire,Opnum43NotUsedOnWireResponse),
44 : (RCreateServiceWOW64A,RCreateServiceWOW64AResponse),
45 : (RCreateServiceWOW64W,RCreateServiceWOW64WResponse),
46 : (Opnum46NotUsedOnWire,Opnum46NotUsedOnWireResponse),
47 : (RNotifyServiceStatusChange,RNotifyServiceStatusChangeResponse),
48 : (RGetNotifyResults,RGetNotifyResultsResponse),
49 : (RCloseNotifyHandle,RCloseNotifyHandleResponse),
50 : (RControlServiceExA,RControlServiceExAResponse),
51 : (RControlServiceExW,RControlServiceExWResponse),
52 : (Opnum52NotUsedOnWire,Opnum52NotUsedOnWireResponse),
53 : (Opnum53NotUsedOnWire,Opnum53NotUsedOnWireResponse),
54 : (Opnum54NotUsedOnWire,Opnum54NotUsedOnWireResponse),
55 : (Opnum55NotUsedOnWire,Opnum55NotUsedOnWireResponse),
56 : (RQueryServiceConfigEx,RQueryServiceConfigExResponse),
57 : (Opnum57NotUsedOnWire,Opnum57NotUsedOnWireResponse),
58 : (Opnum58NotUsedOnWire,Opnum58NotUsedOnWireResponse),
59 : (Opnum59NotUsedOnWire,Opnum59NotUsedOnWireResponse),
60 : (RCreateWowService,RCreateWowServiceResponse),
61 : (ROpenSCManager2,ROpenSCManager2Response),
}

