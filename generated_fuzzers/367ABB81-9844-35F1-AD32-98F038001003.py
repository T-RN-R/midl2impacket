
from fuzzer.midl import *
from fuzzer.core import *
ULONGLONG = NdrHyper
BYTE = NdrByte
USHORT = NdrShort
SHORT = NdrShort
UCHAR = NdrByte
PCHAR = NdrByte
PUCHAR = NdrByte
PLONG64 = NdrHyper
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
PDWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
PUNSIGNED_LONG = NdrLong
PUNSIGNED_CHAR = NdrByte
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
PWCHAR = NdrCString
INT = NdrLong
PVOID = NdrContextHandle
VOID = NdrContextHandle
CONTEXT_HANDLE = NdrContextHandle
PPCONTEXT_HANDLE = NdrContextHandle
LONG = NdrLong
INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LARGE_INTEGER = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte
DOUBLE = NdrDouble
FLOAT = NdrFloat

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')]

class LUID(NdrStructure):
    MEMBERS = [(DWORD,'LowPart'),(LONG,'HighPart')]

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),]
WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PPBOOL = INT
PLPBOOL = INT
BYTE = UNSIGNED_CHAR
PPBYTE = UNSIGNED_CHAR
PLPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PPBOOLEAN = BYTE
WCHAR = WCHAR_T
PPWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PPCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PPDWORD = UNSIGNED_LONG
PLPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PPDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PPDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PPUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
PLPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = WCHAR_T
LMSTR = WCHAR
LONG = LONG
PPLONG = LONG
PLPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PPLONG64 = SIGNED___INT64
LPCSTR = CHAR
LPCVOID = VOID
LPCWSTR = WCHAR_T
PSTR = CHAR
PLPSTR = CHAR
LPWSTR = WCHAR_T
PPWSTR = WCHAR_T
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
PPULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PPVOID = VOID
PLPVOID = VOID
WORD = UNSIGNED_SHORT
PPWORD = UNSIGNED_SHORT
PLPWORD = UNSIGNED_SHORT

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
PFILETIME = FILETIME
LPFILETIME = FILETIME

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    
UUID = GUID
PGUID = GUID

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    
PLARGE_INTEGER = LARGE_INTEGER

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    
PEVENT_DESCRIPTOR = EVENT_DESCRIPTOR
PCEVENT_DESCRIPTOR = EVENT_DESCRIPTOR

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    
PEVENT_HEADER = EVENT_HEADER
LCID = DWORD

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    
PLUID = LUID

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    
PRPC_UNICODE_STRING = RPC_UNICODE_STRING

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    
PSERVER_INFO_100 = SERVER_INFO_100
LPSERVER_INFO_100 = SERVER_INFO_100

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    
PSERVER_INFO_101 = SERVER_INFO_101
LPSERVER_INFO_101 = SERVER_INFO_101

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    
PSYSTEMTIME = SYSTEMTIME

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    
PUINT128 = UINT128

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    
PULARGE_INTEGER = ULARGE_INTEGER

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    
ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    
POBJECT_TYPE_LIST = OBJECT_TYPE_LIST

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    
PACE_HEADER = ACE_HEADER

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    
PSYSTEM_MANDATORY_LABEL_ACE = SYSTEM_MANDATORY_LABEL_ACE

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    
PTOKEN_MANDATORY_POLICY = TOKEN_MANDATORY_POLICY

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    
PMANDATORY_INFORMATION = MANDATORY_INFORMATION

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    
PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE = CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    
PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 = CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
SECURITY_INFORMATION = DWORD
PPSECURITY_INFORMATION = DWORD

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    
PRPC_SID = RPC_SID
PSID = RPC_SID

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    
PACL = ACL

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
PSECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR
SVCCTL_HANDLEW = WCHAR_T
SVCCTL_HANDLEA = LPSTR
SC_RPC_HANDLE = PVOID
SC_RPC_LOCK = PVOID
SC_NOTIFY_RPC_HANDLE = PVOID
LPSC_RPC_HANDLE = SC_RPC_HANDLE
LPSC_RPC_LOCK = SC_RPC_LOCK
LPSC_NOTIFY_RPC_HANDLE = SC_NOTIFY_RPC_HANDLE

class STRING_PTRSA(NdrStructure):
    MEMBERS = [(LPSTR, "StringPtr"),]

    
PSTRING_PTRSA = STRING_PTRSA
LPSTRING_PTRSA = STRING_PTRSA

class STRING_PTRSW(NdrStructure):
    MEMBERS = [(PWCHAR_T, "StringPtr"),]

    
PSTRING_PTRSW = STRING_PTRSW
LPSTRING_PTRSW = STRING_PTRSW
BOUNDED_DWORD_4K = DWORD
LPBOUNDED_DWORD_4K = BOUNDED_DWORD_4K
BOUNDED_DWORD_8K = DWORD
LPBOUNDED_DWORD_8K = BOUNDED_DWORD_8K
BOUNDED_DWORD_256K = DWORD
LPBOUNDED_DWORD_256K = BOUNDED_DWORD_256K

class SERVICE_STATUS(NdrStructure):
    MEMBERS = [(DWORD, "dwServiceType"),(DWORD, "dwCurrentState"),(DWORD, "dwControlsAccepted"),(DWORD, "dwWin32ExitCode"),(DWORD, "dwServiceSpecificExitCode"),(DWORD, "dwCheckPoint"),(DWORD, "dwWaitHint"),]

    
LPSERVICE_STATUS = SERVICE_STATUS

class SERVICE_STATUS_PROCESS(NdrStructure):
    MEMBERS = [(DWORD, "dwServiceType"),(DWORD, "dwCurrentState"),(DWORD, "dwControlsAccepted"),(DWORD, "dwWin32ExitCode"),(DWORD, "dwServiceSpecificExitCode"),(DWORD, "dwCheckPoint"),(DWORD, "dwWaitHint"),(DWORD, "dwProcessId"),(DWORD, "dwServiceFlags"),]

    
LPSERVICE_STATUS_PROCESS = SERVICE_STATUS_PROCESS

class QUERY_SERVICE_CONFIGW(NdrStructure):
    MEMBERS = [(DWORD, "dwServiceType"),(DWORD, "dwStartType"),(DWORD, "dwErrorControl"),(LPWSTR, "lpBinaryPathName"),(LPWSTR, "lpLoadOrderGroup"),(DWORD, "dwTagId"),(LPWSTR, "lpDependencies"),(LPWSTR, "lpServiceStartName"),(LPWSTR, "lpDisplayName"),]

    
LPQUERY_SERVICE_CONFIGW = QUERY_SERVICE_CONFIGW

class QUERY_SERVICE_LOCK_STATUSW(NdrStructure):
    MEMBERS = [(DWORD, "fIsLocked"),(LPWSTR, "lpLockOwner"),(DWORD, "dwLockDuration"),]

    
LPQUERY_SERVICE_LOCK_STATUSW = QUERY_SERVICE_LOCK_STATUSW

class QUERY_SERVICE_CONFIGA(NdrStructure):
    MEMBERS = [(DWORD, "dwServiceType"),(DWORD, "dwStartType"),(DWORD, "dwErrorControl"),(LPSTR, "lpBinaryPathName"),(LPSTR, "lpLoadOrderGroup"),(DWORD, "dwTagId"),(LPSTR, "lpDependencies"),(LPSTR, "lpServiceStartName"),(LPSTR, "lpDisplayName"),]

    
LPQUERY_SERVICE_CONFIGA = QUERY_SERVICE_CONFIGA

class QUERY_SERVICE_LOCK_STATUSA(NdrStructure):
    MEMBERS = [(DWORD, "fIsLocked"),(PCHAR, "lpLockOwner"),(DWORD, "dwLockDuration"),]

    
LPQUERY_SERVICE_LOCK_STATUSA = QUERY_SERVICE_LOCK_STATUSA

class SERVICE_DESCRIPTIONA(NdrStructure):
    MEMBERS = [(LPSTR, "lpDescription"),]

    
LPSERVICE_DESCRIPTIONA = SERVICE_DESCRIPTIONA

class SC_ACTION_TYPE(NdrEnum):
    MAP = ((0 , 'SC_ACTION_NONE'),(1 , 'SC_ACTION_RESTART'),(2 , 'SC_ACTION_REBOOT'),(3 , 'SC_ACTION_RUN_COMMAND'),)        

class SC_ACTION(NdrStructure):
    MEMBERS = [(SC_ACTION_TYPE, "Type"),(DWORD, "Delay"),]

    
LPSC_ACTION = SC_ACTION

class SERVICE_FAILURE_ACTIONSA(NdrStructure):
    MEMBERS = [(DWORD, "dwResetPeriod"),(LPSTR, "lpRebootMsg"),(LPSTR, "lpCommand"),(DWORD, "cActions"),(PSC_ACTION, "lpsaActions"),]

    
LPSERVICE_FAILURE_ACTIONSA = SERVICE_FAILURE_ACTIONSA

class SERVICE_DELAYED_AUTO_START_INFO(NdrStructure):
    MEMBERS = [(BOOL, "fDelayedAutostart"),]

    
LPSERVICE_DELAYED_AUTO_START_INFO = SERVICE_DELAYED_AUTO_START_INFO

class SERVICE_FAILURE_ACTIONS_FLAG(NdrStructure):
    MEMBERS = [(BOOL, "fFailureActionsOnNonCrashFailures"),]

    
LPSERVICE_FAILURE_ACTIONS_FLAG = SERVICE_FAILURE_ACTIONS_FLAG

class SERVICE_SID_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwServiceSidType"),]

    
LPSERVICE_SID_INFO = SERVICE_SID_INFO

class SERVICE_PRESHUTDOWN_INFO(NdrStructure):
    MEMBERS = [(DWORD, "dwPreshutdownTimeout"),]

    
LPSERVICE_PRESHUTDOWN_INFO = SERVICE_PRESHUTDOWN_INFO

class SERVICE_DESCRIPTIONW(NdrStructure):
    MEMBERS = [(LPWSTR, "lpDescription"),]

    
LPSERVICE_DESCRIPTIONW = SERVICE_DESCRIPTIONW

class SERVICE_FAILURE_ACTIONSW(NdrStructure):
    MEMBERS = [(DWORD, "dwResetPeriod"),(LPWSTR, "lpRebootMsg"),(LPWSTR, "lpCommand"),(DWORD, "cActions"),(PSC_ACTION, "lpsaActions"),]

    
LPSERVICE_FAILURE_ACTIONSW = SERVICE_FAILURE_ACTIONSW

class SC_STATUS_TYPE(NdrEnum):
    MAP = ((0 , 'SC_STATUS_PROCESS_INFO'),)        

class SC_ENUM_TYPE(NdrEnum):
    MAP = ((0 , 'SC_ENUM_PROCESS_INFO'),)        

class SERVICE_PREFERRED_NODE_INFO(NdrStructure):
    MEMBERS = [(USHORT, "usPreferredNode"),(BOOLEAN, "fDelete"),]

    
LPSERVICE_PREFERRED_NODE_INFO = SERVICE_PREFERRED_NODE_INFO

class SERVICE_TRIGGER_SPECIFIC_DATA_ITEM(NdrStructure):
    MEMBERS = [(DWORD, "dwDataType"),(DWORD, "cbData"),(PBYTE, "pData"),]

    
PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM = SERVICE_TRIGGER_SPECIFIC_DATA_ITEM

class SERVICE_TRIGGER(NdrStructure):
    MEMBERS = [(DWORD, "dwTriggerType"),(DWORD, "dwAction"),(PGUID, "pTriggerSubtype"),(DWORD, "cDataItems"),(PSERVICE_TRIGGER_SPECIFIC_DATA_ITEM, "pDataItems"),]

    
PSERVICE_TRIGGER = SERVICE_TRIGGER

class SERVICE_TRIGGER_INFO(NdrStructure):
    MEMBERS = [(DWORD, "cTriggers"),(PSERVICE_TRIGGER, "pTriggers"),(PBYTE, "pReserved"),]

    
PSERVICE_TRIGGER_INFO = SERVICE_TRIGGER_INFO
SECURITY_INFORMATION = ULONG
PPSECURITY_INFORMATION = ULONG

class ENUM_SERVICE_STATUSA(NdrStructure):
    MEMBERS = [(LPSTR, "lpServiceName"),(LPSTR, "lpDisplayName"),(SERVICE_STATUS, "ServiceStatus"),]

    
LPENUM_SERVICE_STATUSA = ENUM_SERVICE_STATUSA

class ENUM_SERVICE_STATUSW(NdrStructure):
    MEMBERS = [(LPWSTR, "lpServiceName"),(LPWSTR, "lpDisplayName"),(SERVICE_STATUS, "ServiceStatus"),]

    
LPENUM_SERVICE_STATUSW = ENUM_SERVICE_STATUSW

class ENUM_SERVICE_STATUS_PROCESSA(NdrStructure):
    MEMBERS = [(LPSTR, "lpServiceName"),(LPSTR, "lpDisplayName"),(SERVICE_STATUS_PROCESS, "ServiceStatusProcess"),]

    
LPENUM_SERVICE_STATUS_PROCESSA = ENUM_SERVICE_STATUS_PROCESSA

class ENUM_SERVICE_STATUS_PROCESSW(NdrStructure):
    MEMBERS = [(LPWSTR, "lpServiceName"),(LPWSTR, "lpDisplayName"),(SERVICE_STATUS_PROCESS, "ServiceStatusProcess"),]

    
LPENUM_SERVICE_STATUS_PROCESSW = ENUM_SERVICE_STATUS_PROCESSW

class SERVICE_DESCRIPTION_WOW64(NdrStructure):
    MEMBERS = [(DWORD, "dwDescriptionOffset"),]

    
LPSERVICE_DESCRIPTION_WOW64 = SERVICE_DESCRIPTION_WOW64

class SERVICE_FAILURE_ACTIONS_WOW64(NdrStructure):
    MEMBERS = [(DWORD, "dwResetPeriod"),(DWORD, "dwRebootMsgOffset"),(DWORD, "dwCommandOffset"),(DWORD, "cActions"),(DWORD, "dwsaActionsOffset"),]

    
LPSERVICE_FAILURE_ACTIONS_WOW64 = SERVICE_FAILURE_ACTIONS_WOW64

class SERVICE_REQUIRED_PRIVILEGES_INFO_WOW64(NdrStructure):
    MEMBERS = [(DWORD, "dwRequiredPrivilegesOffset"),]

    
LPSERVICE_REQUIRED_PRIVILEGES_INFO_WOW64 = SERVICE_REQUIRED_PRIVILEGES_INFO_WOW64

class SERVICE_RPC_REQUIRED_PRIVILEGES_INFO(NdrStructure):
    MEMBERS = [(DWORD, "cbRequiredPrivileges"),(PBYTE, "pRequiredPrivileges"),]

    
LPSERVICE_RPC_REQUIRED_PRIVILEGES_INFO = SERVICE_RPC_REQUIRED_PRIVILEGES_INFO

class SC_RPC_CONFIG_INFOA(NdrStructure):
    MEMBERS = [(DWORD, "dwInfoLevel"),(U0, "u0"),]

    

class SC_RPC_CONFIG_INFOW(NdrStructure):
    MEMBERS = [(DWORD, "dwInfoLevel"),(U0, "u0"),]

    

class SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1(NdrStructure):
    MEMBERS = [(ULONGLONG, "ullThreadId"),(DWORD, "dwNotifyMask"),(UCHAR, "CallbackAddressArray"),(UCHAR, "CallbackParamAddressArray"),(SERVICE_STATUS_PROCESS, "ServiceStatus"),(DWORD, "dwNotificationStatus"),(DWORD, "dwSequence"),]

    
PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1 = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_1

class SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2(NdrStructure):
    MEMBERS = [(ULONGLONG, "ullThreadId"),(DWORD, "dwNotifyMask"),(UCHAR, "CallbackAddressArray"),(UCHAR, "CallbackParamAddressArray"),(SERVICE_STATUS_PROCESS, "ServiceStatus"),(DWORD, "dwNotificationStatus"),(DWORD, "dwSequence"),(DWORD, "dwNotificationTriggered"),(PWSTR, "pszServiceNames"),]

    
PSERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2 = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2
SERVICE_NOTIFY_STATUS_CHANGE_PARAMS = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2
PPSERVICE_NOTIFY_STATUS_CHANGE_PARAMS = SERVICE_NOTIFY_STATUS_CHANGE_PARAMS_2

class SC_RPC_NOTIFY_PARAMS(NdrStructure):
    MEMBERS = [(DWORD, "dwInfoLevel"),(U0, "u0"),]

    

class SC_RPC_NOTIFY_PARAMS_LIST(NdrStructure):
    MEMBERS = [(BOUNDED_DWORD_4K, "cElements"),(SC_RPC_NOTIFY_PARAMS, "NotifyParamsArray"),]

    
PSC_RPC_NOTIFY_PARAMS_LIST = SC_RPC_NOTIFY_PARAMS_LIST

class SERVICE_CONTROL_STATUS_REASON_IN_PARAMSA(NdrStructure):
    MEMBERS = [(DWORD, "dwReason"),(LPSTR, "pszComment"),]

    
PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSA = SERVICE_CONTROL_STATUS_REASON_IN_PARAMSA

class SERVICE_CONTROL_STATUS_REASON_OUT_PARAMS(NdrStructure):
    MEMBERS = [(SERVICE_STATUS_PROCESS, "ServiceStatus"),]

    
PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS = SERVICE_CONTROL_STATUS_REASON_OUT_PARAMS

class SC_RPC_SERVICE_CONTROL_IN_PARAMSA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSA, "psrInParams"),}

    
PSC_RPC_SERVICE_CONTROL_IN_PARAMSA = SC_RPC_SERVICE_CONTROL_IN_PARAMSA

class SC_RPC_SERVICE_CONTROL_OUT_PARAMSA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS, "psrOutParams"),}

    
PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA = SC_RPC_SERVICE_CONTROL_OUT_PARAMSA

class SERVICE_CONTROL_STATUS_REASON_IN_PARAMSW(NdrStructure):
    MEMBERS = [(DWORD, "dwReason"),(LPWSTR, "pszComment"),]

    
PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSW = SERVICE_CONTROL_STATUS_REASON_IN_PARAMSW

class SC_RPC_SERVICE_CONTROL_IN_PARAMSW(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSERVICE_CONTROL_STATUS_REASON_IN_PARAMSW, "psrInParams"),}

    
PSC_RPC_SERVICE_CONTROL_IN_PARAMSW = SC_RPC_SERVICE_CONTROL_IN_PARAMSW

class SC_RPC_SERVICE_CONTROL_OUT_PARAMSW(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PSERVICE_CONTROL_STATUS_REASON_OUT_PARAMS, "psrOutParams"),}

    
PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW = SC_RPC_SERVICE_CONTROL_OUT_PARAMSW
Interface("367ABB81-9844-35F1-AD32-98F038001003", "2.0",[Method("RCloseServiceHandle",
InOut((LPSC_RPC_HANDLE,'hSCObject')),
),Method("RControlService",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwControl')),
Out((LPSERVICE_STATUS,'lpServiceStatus')),
),Method("RDeleteService",
In((SC_RPC_HANDLE,'hService')),
),Method("RLockServiceDatabase",
In((SC_RPC_HANDLE,'hSCManager')),
Out((LPSC_RPC_LOCK,'lpLock')),
),Method("RQueryServiceObjectSecurity",
In((SC_RPC_HANDLE,'hService')),
In((SECURITY_INFORMATION,'dwSecurityInformation')),
Out((LPBYTE,'lpSecurityDescriptor')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
),Method("RSetServiceObjectSecurity",
In((SC_RPC_HANDLE,'hService')),
In((SECURITY_INFORMATION,'dwSecurityInformation')),
In((LPBYTE,'lpSecurityDescriptor')),
In((DWORD,'cbBufSize')),
),Method("RQueryServiceStatus",
In((SC_RPC_HANDLE,'hService')),
Out((LPSERVICE_STATUS,'lpServiceStatus')),
),Method("RSetServiceStatus",
In((SC_RPC_HANDLE,'hServiceStatus')),
In((LPSERVICE_STATUS,'lpServiceStatus')),
),Method("RUnlockServiceDatabase",
InOut((LPSC_RPC_LOCK,'Lock')),
),Method("RNotifyBootConfigStatus",
In((SVCCTL_HANDLEW,'lpMachineName')),
In((DWORD,'BootAcceptable')),
),Method("Opnum10NotUsedOnWire",
),Method("RChangeServiceConfigW",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((PWCHAR_T,'lpBinaryPathName')),
In((PWCHAR_T,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((PWCHAR_T,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
In((PWCHAR_T,'lpDisplayName')),
),Method("RCreateServiceW",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpServiceName')),
In((PWCHAR_T,'lpDisplayName')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((PWCHAR_T,'lpBinaryPathName')),
In((PWCHAR_T,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((PWCHAR_T,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("REnumDependentServicesW",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpServices')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
),Method("REnumServicesStatusW",
In((SC_RPC_HANDLE,'hSCManager')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
InOut((LPBOUNDED_DWORD_256K,'lpResumeIndex')),
),Method("ROpenSCManagerW",
In((SVCCTL_HANDLEW,'lpMachineName')),
In((PWCHAR_T,'lpDatabaseName')),
In((DWORD,'dwDesiredAccess')),
Out((LPSC_RPC_HANDLE,'lpScHandle')),
),Method("ROpenServiceW",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpServiceName')),
In((DWORD,'dwDesiredAccess')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("RQueryServiceConfigW",
In((SC_RPC_HANDLE,'hService')),
Out((LPQUERY_SERVICE_CONFIGW,'lpServiceConfig')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_8K,'pcbBytesNeeded')),
),Method("RQueryServiceLockStatusW",
In((SC_RPC_HANDLE,'hSCManager')),
Out((LPQUERY_SERVICE_LOCK_STATUSW,'lpLockStatus')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_4K,'pcbBytesNeeded')),
),Method("RStartServiceW",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'argc')),
In((LPSTRING_PTRSW,'argv')),
),Method("RGetServiceDisplayNameW",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpServiceName')),
Out((PWCHAR_T,'lpDisplayName')),
InOut((PDWORD,'lpcchBuffer')),
),Method("RGetServiceKeyNameW",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpDisplayName')),
Out((PWCHAR_T,'lpServiceName')),
InOut((PDWORD,'lpcchBuffer')),
),Method("Opnum22NotUsedOnWire",
),Method("RChangeServiceConfigA",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((LPSTR,'lpBinaryPathName')),
In((LPSTR,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((LPSTR,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
In((LPSTR,'lpDisplayName')),
),Method("RCreateServiceA",
In((SC_RPC_HANDLE,'hSCManager')),
In((LPSTR,'lpServiceName')),
In((LPSTR,'lpDisplayName')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((LPSTR,'lpBinaryPathName')),
In((LPSTR,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((LPSTR,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("REnumDependentServicesA",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpServices')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
),Method("REnumServicesStatusA",
In((SC_RPC_HANDLE,'hSCManager')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
InOut((LPBOUNDED_DWORD_256K,'lpResumeIndex')),
),Method("ROpenSCManagerA",
In((SVCCTL_HANDLEA,'lpMachineName')),
In((LPSTR,'lpDatabaseName')),
In((DWORD,'dwDesiredAccess')),
Out((LPSC_RPC_HANDLE,'lpScHandle')),
),Method("ROpenServiceA",
In((SC_RPC_HANDLE,'hSCManager')),
In((LPSTR,'lpServiceName')),
In((DWORD,'dwDesiredAccess')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("RQueryServiceConfigA",
In((SC_RPC_HANDLE,'hService')),
Out((LPQUERY_SERVICE_CONFIGA,'lpServiceConfig')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_8K,'pcbBytesNeeded')),
),Method("RQueryServiceLockStatusA",
In((SC_RPC_HANDLE,'hSCManager')),
Out((LPQUERY_SERVICE_LOCK_STATUSA,'lpLockStatus')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_4K,'pcbBytesNeeded')),
),Method("RStartServiceA",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'argc')),
In((LPSTRING_PTRSA,'argv')),
),Method("RGetServiceDisplayNameA",
In((SC_RPC_HANDLE,'hSCManager')),
In((LPSTR,'lpServiceName')),
Out((LPSTR,'lpDisplayName')),
InOut((LPBOUNDED_DWORD_4K,'lpcchBuffer')),
),Method("RGetServiceKeyNameA",
In((SC_RPC_HANDLE,'hSCManager')),
In((LPSTR,'lpDisplayName')),
Out((LPSTR,'lpKeyName')),
InOut((LPBOUNDED_DWORD_4K,'lpcchBuffer')),
),Method("Opnum34NotUsedOnWire",
),Method("REnumServiceGroupW",
In((SC_RPC_HANDLE,'hSCManager')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
InOut((LPBOUNDED_DWORD_256K,'lpResumeIndex')),
In((LPCWSTR,'pszGroupName')),
),Method("RChangeServiceConfig2A",
In((SC_RPC_HANDLE,'hService')),
In((SC_RPC_CONFIG_INFOA,'Info')),
),Method("RChangeServiceConfig2W",
In((SC_RPC_HANDLE,'hService')),
In((SC_RPC_CONFIG_INFOW,'Info')),
),Method("RQueryServiceConfig2A",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwInfoLevel')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_8K,'pcbBytesNeeded')),
),Method("RQueryServiceConfig2W",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwInfoLevel')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_8K,'pcbBytesNeeded')),
),Method("RQueryServiceStatusEx",
In((SC_RPC_HANDLE,'hService')),
In((SC_STATUS_TYPE,'InfoLevel')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_8K,'pcbBytesNeeded')),
),Method("REnumServicesStatusExA",
In((SC_RPC_HANDLE,'hSCManager')),
In((SC_ENUM_TYPE,'InfoLevel')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
InOut((LPBOUNDED_DWORD_256K,'lpResumeIndex')),
In((LPCSTR,'pszGroupName')),
),Method("REnumServicesStatusExW",
In((SC_RPC_HANDLE,'hSCManager')),
In((SC_ENUM_TYPE,'InfoLevel')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwServiceState')),
Out((LPBYTE,'lpBuffer')),
In((DWORD,'cbBufSize')),
Out((LPBOUNDED_DWORD_256K,'pcbBytesNeeded')),
Out((LPBOUNDED_DWORD_256K,'lpServicesReturned')),
InOut((LPBOUNDED_DWORD_256K,'lpResumeIndex')),
In((LPCWSTR,'pszGroupName')),
),Method("Opnum43NotUsedOnWire",
),Method("RCreateServiceWOW64A",
In((SC_RPC_HANDLE,'hSCManager')),
In((LPSTR,'lpServiceName')),
In((LPSTR,'lpDisplayName')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((LPSTR,'lpBinaryPathName')),
In((LPSTR,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((LPSTR,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("RCreateServiceWOW64W",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpServiceName')),
In((PWCHAR_T,'lpDisplayName')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((PWCHAR_T,'lpBinaryPathName')),
In((PWCHAR_T,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((PWCHAR_T,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("Opnum46NotUsedOnWire",
),Method("RNotifyServiceStatusChange",
In((SC_RPC_HANDLE,'hService')),
In((SC_RPC_NOTIFY_PARAMS,'NotifyParams')),
In((PGUID,'pClientProcessGuid')),
Out((PGUID,'pSCMProcessGuid')),
Out((PBOOL,'pfCreateRemoteQueue')),
Out((LPSC_NOTIFY_RPC_HANDLE,'phNotify')),
),Method("RGetNotifyResults",
In((SC_NOTIFY_RPC_HANDLE,'hNotify')),
Out((PPSC_RPC_NOTIFY_PARAMS_LIST,'ppNotifyParams')),
),Method("RCloseNotifyHandle",
InOut((LPSC_NOTIFY_RPC_HANDLE,'phNotify')),
Out((PBOOL,'pfApcFired')),
),Method("RControlServiceExA",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwControl')),
In((DWORD,'dwInfoLevel')),
In((PSC_RPC_SERVICE_CONTROL_IN_PARAMSA,'pControlInParams')),
Out((PSC_RPC_SERVICE_CONTROL_OUT_PARAMSA,'pControlOutParams')),
),Method("RControlServiceExW",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwControl')),
In((DWORD,'dwInfoLevel')),
In((PSC_RPC_SERVICE_CONTROL_IN_PARAMSW,'pControlInParams')),
Out((PSC_RPC_SERVICE_CONTROL_OUT_PARAMSW,'pControlOutParams')),
),Method("Opnum52NotUsedOnWire",
),Method("Opnum53NotUsedOnWire",
),Method("Opnum54NotUsedOnWire",
),Method("Opnum55NotUsedOnWire",
),Method("RQueryServiceConfigEx",
In((SC_RPC_HANDLE,'hService')),
In((DWORD,'dwInfoLevel')),
Out((PSC_RPC_CONFIG_INFOW,'pInfo')),
),Method("Opnum57NotUsedOnWire",
),Method("Opnum58NotUsedOnWire",
),Method("Opnum59NotUsedOnWire",
),Method("RCreateWowService",
In((SC_RPC_HANDLE,'hSCManager')),
In((PWCHAR_T,'lpServiceName')),
In((PWCHAR_T,'lpDisplayName')),
In((DWORD,'dwDesiredAccess')),
In((DWORD,'dwServiceType')),
In((DWORD,'dwStartType')),
In((DWORD,'dwErrorControl')),
In((PWCHAR_T,'lpBinaryPathName')),
In((PWCHAR_T,'lpLoadOrderGroup')),
InOut((LPDWORD,'lpdwTagId')),
In((LPBYTE,'lpDependencies')),
In((DWORD,'dwDependSize')),
In((PWCHAR_T,'lpServiceStartName')),
In((LPBYTE,'lpPassword')),
In((DWORD,'dwPwSize')),
In((USHORT,'dwServiceWowType')),
Out((LPSC_RPC_HANDLE,'lpServiceHandle')),
),Method("ROpenSCManager2",
In((HANDLE_T,'BindingHandle')),
In((PWCHAR_T,'DatabaseName')),
In((DWORD,'DesiredAccess')),
Out((LPSC_RPC_HANDLE,'ScmHandle')),
),])