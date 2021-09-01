
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
__INT64 = NdrHyper
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
__INT3264 = NdrHyper
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
LONG_PTR = __INT3264
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
REFIID = GUID
LPGUID = GUID
LPNTMS_GUID = GUID
NTMS_GUID = GUID
PSECURITY_DESCRIPTOR_NTMS = BYTE
NTMS_HANDLE = ULONG_PTR

class (NdrEnum):
    MAP = ((0 , 'NTMS_UNKNOWN'),(1 , 'NTMS_OBJECT'),(2 , 'NTMS_CHANGER'),(3 , 'NTMS_CHANGER_TYPE'),(4 , 'NTMS_COMPUTER'),(5 , 'NTMS_DRIVE'),(6 , 'NTMS_DRIVE_TYPE'),(7 , 'NTMS_IEDOOR'),(8 , 'NTMS_IEPORT'),(9 , 'NTMS_LIBRARY'),(10 , 'NTMS_LIBREQUEST'),(11 , 'NTMS_LOGICAL_MEDIA'),(12 , 'NTMS_MEDIA_POOL'),(13 , 'NTMS_MEDIA_TYPE'),(14 , 'NTMS_PARTITION'),(15 , 'NTMS_PHYSICAL_MEDIA'),(16 , 'NTMS_STORAGESLOT'),(17 , 'NTMS_OPREQUEST'),(18 , 'NTMS_UI_DESTINATION'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_OPREQ_UNKNOWN'),(1 , 'NTMS_OPREQ_NEWMEDIA'),(2 , 'NTMS_OPREQ_CLEANER'),(3 , 'NTMS_OPREQ_DEVICESERVICE'),(4 , 'NTMS_OPREQ_MOVEMEDIA'),(5 , 'NTMS_OPREQ_MESSAGE'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_OBJ_UPDATE'),(2 , 'NTMS_OBJ_INSERT'),(3 , 'NTMS_OBJ_DELETE'),(4 , 'NTMS_EVENT_SIGNAL'),(5 , 'NTMS_EVENT_COMPLETE'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_DISMOUNT_DEFERRED'),(2 , 'NTMS_DISMOUNT_IMMEDIATE'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_LM_QUEUED'),(1 , 'NTMS_LM_INPROCESS'),(2 , 'NTMS_LM_PASSED'),(3 , 'NTMS_LM_FAILED'),(4 , 'NTMS_LM_INVALID'),(5 , 'NTMS_LM_WAITING'),(7 , 'NTMS_LM_CANCELLED'),(8 , 'NTMS_LM_STOPPED'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_EJECT_START'),(1 , 'NTMS_EJECT_STOP'),(2 , 'NTMS_EJECT_QUEUE'),(3 , 'NTMS_EJECT_FORCE'),(4 , 'NTMS_EJECT_IMMEDIATE'),(5 , 'NTMS_EJECT_ASK_USER'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_INJECT_START'),(1 , 'NTMS_INJECT_STOP'),(2 , 'NTMS_INJECT_RETRACT'),(3 , 'NTMS_INJECT_STARTMANY'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_INVENTORY_NONE'),(1 , 'NTMS_INVENTORY_FAST'),(2 , 'NTMS_INVENTORY_OMID'),(3 , 'NTMS_INVENTORY_DEFAULT'),(4 , 'NTMS_INVENTORY_SLOT'),(5 , 'NTMS_INVENTORY_STOP'),(6 , 'NTMS_INVENTORY_MAX'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_ALLOCATE_NEW'),(2 , 'NTMS_ALLOCATE_NEXT'),(4 , 'NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_OPEN_EXISTING'),(2 , 'NTMS_CREATE_NEW'),(3 , 'NTMS_OPEN_ALWAYS'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_MOUNT_READ'),(2 , 'NTMS_MOUNT_WRITE'),(4 , 'NTMS_MOUNT_ERROR_NOT_AVAILABLE'),(8 , 'NTMS_MOUNT_ERROR_OFFLINE'),(16 , 'NTMS_MOUNT_SPECIFIC_DRIVE'),(32 , 'NTMS_MOUNT_NOWAIT'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_PRIORITY_DEFAULT'),(15 , 'NTMS_PRIORITY_HIGHEST'),(7 , 'NTMS_PRIORITY_HIGH'),(3 , 'NTMS_PRIORITY_NORMAL'),(7-7 , 'NTMS_PRIORITY_LOW'),(15-15 , 'NTMS_PRIORITY_LOWEST'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_BARCODESTATE_OK'),(2 , 'NTMS_BARCODESTATE_UNREADABLE'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_DRIVESTATE_DISMOUNTED'),(1 , 'NTMS_DRIVESTATE_MOUNTED'),(2 , 'NTMS_DRIVESTATE_LOADED'),(5 , 'NTMS_DRIVESTATE_UNLOADED'),(6 , 'NTMS_DRIVESTATE_BEING_CLEANED'),(7 , 'NTMS_DRIVESTATE_DISMOUNTABLE'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_LM_REMOVE'),(1 , 'NTMS_LM_DISABLECHANGER'),(1 , 'NTMS_LM_DISABLELIBRARY'),(2 , 'NTMS_LM_ENABLECHANGER'),(2 , 'NTMS_LM_ENABLELIBRARY'),(3 , 'NTMS_LM_DISABLEDRIVE'),(4 , 'NTMS_LM_ENABLEDRIVE'),(5 , 'NTMS_LM_DISABLEMEDIA'),(6 , 'NTMS_LM_ENABLEMEDIA'),(7 , 'NTMS_LM_UPDATEOMID'),(8 , 'NTMS_LM_INVENTORY'),(9 , 'NTMS_LM_DOORACCESS'),(10 , 'NTMS_LM_EJECT'),(11 , 'NTMS_LM_EJECTCLEANER'),(12 , 'NTMS_LM_INJECT'),(13 , 'NTMS_LM_INJECTCLEANER'),(14 , 'NTMS_LM_PROCESSOMID'),(15 , 'NTMS_LM_CLEANDRIVE'),(16 , 'NTMS_LM_DISMOUNT'),(17 , 'NTMS_LM_MOUNT'),(18 , 'NTMS_LM_WRITESCRATCH'),(19 , 'NTMS_LM_CLASSIFY'),(20 , 'NTMS_LM_RESERVECLEANER'),(21 , 'NTMS_LM_RELEASECLEANER'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_MEDIASTATE_IDLE'),(1 , 'NTMS_MEDIASTATE_INUSE'),(2 , 'NTMS_MEDIASTATE_MOUNTED'),(3 , 'NTMS_MEDIASTATE_LOADED'),(4 , 'NTMS_MEDIASTATE_UNLOADED'),(5 , 'NTMS_MEDIASTATE_OPERROR'),(6 , 'NTMS_MEDIASTATE_OPREQ'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_READY'),(10 , 'NTMS_INITIALIZING'),(20 , 'NTMS_NEEDS_SERVICE'),(21 , 'NTMS_NOT_PRESENT'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_OPSTATE_UNKNOWN'),(1 , 'NTMS_OPSTATE_SUBMITTED'),(2 , 'NTMS_OPSTATE_ACTIVE'),(3 , 'NTMS_OPSTATE_INPROGRESS'),(4 , 'NTMS_OPSTATE_REFUSED'),(5 , 'NTMS_OPSTATE_COMPLETE'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_PARTSTATE_UNKNOWN'),(1 , 'NTMS_PARTSTATE_UNPREPARED'),(2 , 'NTMS_PARTSTATE_INCOMPATIBLE'),(3 , 'NTMS_PARTSTATE_DECOMMISSIONED'),(4 , 'NTMS_PARTSTATE_AVAILABLE'),(5 , 'NTMS_PARTSTATE_ALLOCATED'),(6 , 'NTMS_PARTSTATE_COMPLETE'),(7 , 'NTMS_PARTSTATE_FOREIGN'),(8 , 'NTMS_PARTSTATE_IMPORT'),(9 , 'NTMS_PARTSTATE_RESERVED'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_UIDEST_ADD'),(2 , 'NTMS_UIDEST_DELETE'),(3 , 'NTMS_UIDEST_DELETEALL'),)        

class (NdrEnum):
    MAP = ((0 , 'NTMS_UITYPE_INVALID'),(1 , 'NTMS_UITYPE_INFO'),(2 , 'NTMS_UITYPE_REQ'),(3 , 'NTMS_UITYPE_ERR'),(4 , 'NTMS_UITYPE_MAX'),)        

class (NdrEnum):
    MAP = ((1 , 'NTMS_USE_ACCESS'),(2 , 'NTMS_MODIFY_ACCESS'),(3 , 'NTMS_CONTROL_ACCESS'),)        

class NTMS_LIBRARYINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "LibraryType"),(NTMS_GUID, "CleanerSlot"),(NTMS_GUID, "CleanerSlotDefault"),(BOOL, "LibrarySupportsDriveCleaning"),(BOOL, "BarCodeReaderInstalled"),(DWORD, "InventoryMethod"),(DWORD, "dwCleanerUsesRemaining"),(DWORD, "FirstDriveNumber"),(DWORD, "dwNumberOfDrives"),(DWORD, "FirstSlotNumber"),(DWORD, "dwNumberOfSlots"),(DWORD, "FirstDoorNumber"),(DWORD, "dwNumberOfDoors"),(DWORD, "FirstPortNumber"),(DWORD, "dwNumberOfPorts"),(DWORD, "FirstChangerNumber"),(DWORD, "dwNumberOfChangers"),(DWORD, "dwNumberOfMedia"),(DWORD, "dwNumberOfMediaTypes"),(DWORD, "dwNumberOfLibRequests"),(GUID, "Reserved"),(BOOL, "AutoRecovery"),(DWORD, "dwFlags"),]

    

class SECURITY_ATTRIBUTES_NTMS(NdrStructure):
    MEMBERS = [(DWORD, "nLength"),(PBYTE, "lpSecurityDescriptor"),(BOOL, "bInheritHandle"),(DWORD, "nDescriptorLength"),]

    
LPSECURITY_ATTRIBUTES_NTMS = SECURITY_ATTRIBUTES_NTMS

class NTMS_ALLOCATION_INFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(PBYTE, "lpReserved"),(NTMS_GUID, "AllocatedFrom"),]

    
LPNTMS_ALLOCATION_INFORMATION = NTMS_ALLOCATION_INFORMATION

class NTMS_ASYNC_IO(NdrStructure):
    MEMBERS = [(NTMS_GUID, "OperationId"),(NTMS_GUID, "EventId"),(DWORD, "dwOperationType"),(DWORD, "dwResult"),(DWORD, "dwAsyncState"),(PVOID, "hEvent"),(BOOL, "bOnStateChange"),]

    
LPNTMS_ASYNC_IO = NTMS_ASYNC_IO

class NTMS_MOUNT_INFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(LPVOID, "lpReserved"),]

    
LPNTMS_MOUNT_INFORMATION = NTMS_MOUNT_INFORMATION

class NTMS_CHANGERINFORMATIONA(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(NTMS_GUID, "ChangerType"),(CHAR, "szSerialNumber"),(CHAR, "szRevision"),(CHAR, "szDeviceName"),(UNSIGNED_SHORT, "ScsiPort"),(UNSIGNED_SHORT, "ScsiBus"),(UNSIGNED_SHORT, "ScsiTarget"),(UNSIGNED_SHORT, "ScsiLun"),(NTMS_GUID, "Library"),]

    

class NTMS_CHANGERINFORMATIONW(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(NTMS_GUID, "ChangerType"),(WCHAR_T, "szSerialNumber"),(WCHAR_T, "szRevision"),(WCHAR_T, "szDeviceName"),(UNSIGNED_SHORT, "ScsiPort"),(UNSIGNED_SHORT, "ScsiBus"),(UNSIGNED_SHORT, "ScsiTarget"),(UNSIGNED_SHORT, "ScsiLun"),(NTMS_GUID, "Library"),]

    

class NTMS_CHANGERTYPEINFORMATIONA(NdrStructure):
    MEMBERS = [(CHAR, "szVendor"),(CHAR, "szProduct"),(DWORD, "DeviceType"),]

    

class NTMS_CHANGERTYPEINFORMATIONW(NdrStructure):
    MEMBERS = [(WCHAR_T, "szVendor"),(WCHAR_T, "szProduct"),(DWORD, "DeviceType"),]

    

class NTMS_DRIVEINFORMATIONA(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(DWORD, "State"),(NTMS_GUID, "DriveType"),(CHAR, "szDeviceName"),(CHAR, "szSerialNumber"),(CHAR, "szRevision"),(UNSIGNED_SHORT, "ScsiPort"),(UNSIGNED_SHORT, "ScsiBus"),(UNSIGNED_SHORT, "ScsiTarget"),(UNSIGNED_SHORT, "ScsiLun"),(DWORD, "dwMountCount"),(SYSTEMTIME, "LastCleanedTs"),(NTMS_GUID, "SavedPartitionId"),(NTMS_GUID, "Library"),(GUID, "Reserved"),(DWORD, "dwDeferDismountDelay"),]

    

class NTMS_DRIVEINFORMATIONW(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(DWORD, "State"),(NTMS_GUID, "DriveType"),(WCHAR_T, "szDeviceName"),(WCHAR_T, "szSerialNumber"),(WCHAR_T, "szRevision"),(UNSIGNED_SHORT, "ScsiPort"),(UNSIGNED_SHORT, "ScsiBus"),(UNSIGNED_SHORT, "ScsiTarget"),(UNSIGNED_SHORT, "ScsiLun"),(DWORD, "dwMountCount"),(SYSTEMTIME, "LastCleanedTs"),(NTMS_GUID, "SavedPartitionId"),(NTMS_GUID, "Library"),(GUID, "Reserved"),(DWORD, "dwDeferDismountDelay"),]

    

class NTMS_DRIVETYPEINFORMATIONA(NdrStructure):
    MEMBERS = [(CHAR, "szVendor"),(CHAR, "szProduct"),(DWORD, "NumberOfHeads"),(DWORD, "DeviceType"),]

    

class NTMS_DRIVETYPEINFORMATIONW(NdrStructure):
    MEMBERS = [(WCHAR_T, "szVendor"),(WCHAR_T, "szProduct"),(DWORD, "NumberOfHeads"),(DWORD, "DeviceType"),]

    

class NTMS_LIBREQUESTINFORMATIONA(NdrStructure):
    MEMBERS = [(DWORD, "OperationCode"),(DWORD, "OperationOption"),(DWORD, "State"),(NTMS_GUID, "PartitionId"),(NTMS_GUID, "DriveId"),(NTMS_GUID, "PhysMediaId"),(NTMS_GUID, "Library"),(NTMS_GUID, "SlotId"),(SYSTEMTIME, "TimeQueued"),(SYSTEMTIME, "TimeCompleted"),(CHAR, "szApplication"),(CHAR, "szUser"),(CHAR, "szComputer"),(DWORD, "dwErrorCode"),(NTMS_GUID, "WorkItemId"),(DWORD, "dwPriority"),]

    

class NTMS_LIBREQUESTINFORMATIONW(NdrStructure):
    MEMBERS = [(DWORD, "OperationCode"),(DWORD, "OperationOption"),(DWORD, "State"),(NTMS_GUID, "PartitionId"),(NTMS_GUID, "DriveId"),(NTMS_GUID, "PhysMediaId"),(NTMS_GUID, "Library"),(NTMS_GUID, "SlotId"),(SYSTEMTIME, "TimeQueued"),(SYSTEMTIME, "TimeCompleted"),(WCHAR_T, "szApplication"),(WCHAR_T, "szUser"),(WCHAR_T, "szComputer"),(DWORD, "dwErrorCode"),(NTMS_GUID, "WorkItemId"),(DWORD, "dwPriority"),]

    

class NTMS_MEDIAPOOLINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "PoolType"),(NTMS_GUID, "MediaType"),(NTMS_GUID, "Parent"),(DWORD, "AllocationPolicy"),(DWORD, "DeallocationPolicy"),(DWORD, "dwMaxAllocates"),(DWORD, "dwNumberOfPhysicalMedia"),(DWORD, "dwNumberOfLogicalMedia"),(DWORD, "dwNumberOfMediaPools"),]

    

class NTMS_MEDIATYPEINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "MediaType"),(DWORD, "NumberOfSides"),(DWORD, "ReadWriteCharacteristics"),(DWORD, "DeviceType"),]

    

class NTMS_STORAGESLOTINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(DWORD, "State"),(NTMS_GUID, "Library"),]

    

class NTMS_IEDOORINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(DWORD, "State"),(UNSIGNED_SHORT, "MaxOpenSecs"),(NTMS_GUID, "Library"),]

    

class NTMS_IEPORTINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "Number"),(DWORD, "Content"),(DWORD, "Position"),(UNSIGNED_SHORT, "MaxExtendSecs"),(NTMS_GUID, "Library"),]

    

class NTMS_LMIDINFORMATION(NdrStructure):
    MEMBERS = [(NTMS_GUID, "MediaPool"),(DWORD, "dwNumberOfPartitions"),]

    

class NTMS_COMPUTERINFORMATION(NdrStructure):
    MEMBERS = [(DWORD, "dwLibRequestPurgeTime"),(DWORD, "dwOpRequestPurgeTime"),(DWORD, "dwLibRequestFlags"),(DWORD, "dwOpRequestFlags"),(DWORD, "dwMediaPoolPolicy"),]

    

class NTMS_OPREQUESTINFORMATIONA(NdrStructure):
    MEMBERS = [(DWORD, "Request"),(SYSTEMTIME, "Submitted"),(DWORD, "State"),(CHAR, "szMessage"),(DWORD, "Arg1Type"),(NTMS_GUID, "Arg1"),(DWORD, "Arg2Type"),(NTMS_GUID, "Arg2"),(CHAR, "szApplication"),(CHAR, "szUser"),(CHAR, "szComputer"),]

    

class NTMS_OPREQUESTINFORMATIONW(NdrStructure):
    MEMBERS = [(DWORD, "Request"),(SYSTEMTIME, "Submitted"),(DWORD, "State"),(WCHAR_T, "szMessage"),(DWORD, "Arg1Type"),(NTMS_GUID, "Arg1"),(DWORD, "Arg2Type"),(NTMS_GUID, "Arg2"),(WCHAR_T, "szApplication"),(WCHAR_T, "szUser"),(WCHAR_T, "szComputer"),]

    

class NTMS_PARTITIONINFORMATIONA(NdrStructure):
    MEMBERS = [(NTMS_GUID, "PhysicalMedia"),(NTMS_GUID, "LogicalMedia"),(DWORD, "State"),(UNSIGNED_SHORT, "Side"),(DWORD, "dwOmidLabelIdLength"),(BYTE, "OmidLabelId"),(CHAR, "szOmidLabelType"),(CHAR, "szOmidLabelInfo"),(DWORD, "dwMountCount"),(DWORD, "dwAllocateCount"),(LARGE_INTEGER, "Capacity"),]

    

class NTMS_PARTITIONINFORMATIONW(NdrStructure):
    MEMBERS = [(NTMS_GUID, "PhysicalMedia"),(NTMS_GUID, "LogicalMedia"),(DWORD, "State"),(UNSIGNED_SHORT, "Side"),(DWORD, "dwOmidLabelIdLength"),(BYTE, "OmidLabelId"),(WCHAR_T, "szOmidLabelType"),(WCHAR_T, "szOmidLabelInfo"),(DWORD, "dwMountCount"),(DWORD, "dwAllocateCount"),(LARGE_INTEGER, "Capacity"),]

    

class NTMS_PMIDINFORMATIONA(NdrStructure):
    MEMBERS = [(NTMS_GUID, "CurrentLibrary"),(NTMS_GUID, "MediaPool"),(NTMS_GUID, "Location"),(DWORD, "LocationType"),(NTMS_GUID, "MediaType"),(NTMS_GUID, "HomeSlot"),(CHAR, "szBarCode"),(DWORD, "BarCodeState"),(CHAR, "szSequenceNumber"),(DWORD, "MediaState"),(DWORD, "dwNumberOfPartitions"),(DWORD, "dwMediaTypeCode"),(DWORD, "dwDensityCode"),(NTMS_GUID, "MountedPartition"),]

    

class NTMS_PMIDINFORMATIONW(NdrStructure):
    MEMBERS = [(NTMS_GUID, "CurrentLibrary"),(NTMS_GUID, "MediaPool"),(NTMS_GUID, "Location"),(DWORD, "LocationType"),(NTMS_GUID, "MediaType"),(NTMS_GUID, "HomeSlot"),(WCHAR_T, "szBarCode"),(DWORD, "BarCodeState"),(WCHAR_T, "szSequenceNumber"),(DWORD, "MediaState"),(DWORD, "dwNumberOfPartitions"),(DWORD, "dwMediaTypeCode"),(DWORD, "dwDensityCode"),(NTMS_GUID, "MountedPartition"),]

    

class RSM_MESSAGE(NdrStructure):
    MEMBERS = [(LPGUID, "lpguidOperation"),(DWORD, "dwNtmsType"),(DWORD, "dwState"),(DWORD, "dwFlags"),(DWORD, "dwPriority"),(DWORD, "dwErrorCode"),(PWCHAR_T, "lpszComputerName"),(PWCHAR_T, "lpszApplication"),(PWCHAR_T, "lpszUser"),(PWCHAR_T, "lpszTimeSubmitted"),(PWCHAR_T, "lpszMessage"),]

    
LPRSM_MESSAGE = RSM_MESSAGE

class NTMS_OBJECTINFORMATIONA(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(DWORD, "dwType"),(SYSTEMTIME, "Created"),(SYSTEMTIME, "Modified"),(NTMS_GUID, "ObjectGuid"),(BOOL, "Enabled"),(DWORD, "dwOperationalState"),(CHAR, "szName"),(CHAR, "szDescription"),(INFO, "Info"),]

    
LPNTMS_OBJECTINFORMATIONA = NTMS_OBJECTINFORMATIONA

class NTMS_OBJECTINFORMATIONW(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(DWORD, "dwType"),(SYSTEMTIME, "Created"),(SYSTEMTIME, "Modified"),(NTMS_GUID, "ObjectGuid"),(BOOL, "Enabled"),(DWORD, "dwOperationalState"),(WCHAR_T, "szName"),(WCHAR_T, "szDescription"),(INFO, "Info"),]

    
LPNTMS_OBJECTINFORMATIONW = NTMS_OBJECTINFORMATIONW
Interface("4e934f30-341a-11d1-8fb1-00a024cb6019", "1.0",[Method("EjectNtmsMedia",
In((LPNTMS_GUID,'lpMediaId')),
InOut((LPNTMS_GUID,'lpEjectOperation')),
In((DWORD,'dwAction')),
),Method("InjectNtmsMedia",
In((LPNTMS_GUID,'lpLibraryId')),
InOut((LPNTMS_GUID,'lpInjectOperation')),
In((DWORD,'dwAction')),
),Method("AccessNtmsLibraryDoor",
In((LPNTMS_GUID,'lpLibraryId')),
In((DWORD,'dwAction')),
),Method("CleanNtmsDrive",
In((LPNTMS_GUID,'lpDriveId')),
),Method("DismountNtmsDrive",
In((LPNTMS_GUID,'lpDriveId')),
),Method("InventoryNtmsLibrary",
In((LPNTMS_GUID,'lpLibraryId')),
In((DWORD,'dwAction')),
),Method("INtmsLibraryControl1_LocalOnlyOpnum09",
),Method("CancelNtmsLibraryRequest",
In((LPNTMS_GUID,'lpRequestId')),
),Method("ReserveNtmsCleanerSlot",
In((LPNTMS_GUID,'lpLibrary')),
In((LPNTMS_GUID,'lpSlot')),
),Method("ReleaseNtmsCleanerSlot",
In((LPNTMS_GUID,'lpLibrary')),
),Method("InjectNtmsCleaner",
In((LPNTMS_GUID,'lpLibrary')),
InOut((LPNTMS_GUID,'lpInjectOperation')),
In((DWORD,'dwNumberOfCleansLeft')),
In((DWORD,'dwAction')),
),Method("EjectNtmsCleaner",
In((LPNTMS_GUID,'lpLibrary')),
InOut((LPNTMS_GUID,'lpEjectOperation')),
In((DWORD,'dwAction')),
),Method("DeleteNtmsLibrary",
In((LPNTMS_GUID,'lpLibraryId')),
),Method("DeleteNtmsDrive",
In((LPNTMS_GUID,'lpDriveId')),
),Method("GetNtmsRequestOrder",
In((LPNTMS_GUID,'lpRequestId')),
Out((PDWORD,'lpdwOrderNumber')),
),Method("SetNtmsRequestOrder",
In((LPNTMS_GUID,'lpRequestId')),
In((DWORD,'dwOrderNumber')),
),Method("DeleteNtmsRequests",
In((LPNTMS_GUID,'lpRequestId')),
In((DWORD,'dwType')),
In((DWORD,'dwCount')),
),Method("BeginNtmsDeviceChangeDetection",
Out((PNTMS_HANDLE,'lpDetectHandle')),
),Method("SetNtmsDeviceChangeDetection",
In((NTMS_HANDLE,'DetectHandle')),
In((LPNTMS_GUID,'lpObjectId')),
In((DWORD,'dwType')),
In((DWORD,'dwCount')),
),Method("EndNtmsDeviceChangeDetection",
In((NTMS_HANDLE,'DetectHandle')),
),])