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

REFIID = GUID
LPGUID = GUID
LPNTMS_GUID = GUID
NTMS_GUID = GUID
PSECURITY_DESCRIPTOR_NTMS = BYTE
NTMS_HANDLE = ULONG_PTR

NTMS_UNKNOWN = 0,
NTMS_OBJECT = 1,
NTMS_CHANGER = 2,
NTMS_CHANGER_TYPE = 3,
NTMS_COMPUTER = 4,
NTMS_DRIVE = 5,
NTMS_DRIVE_TYPE = 6,
NTMS_IEDOOR = 7,
NTMS_IEPORT = 8,
NTMS_LIBRARY = 9,
NTMS_LIBREQUEST = 10,
NTMS_LOGICAL_MEDIA = 11,
NTMS_MEDIA_POOL = 12,
NTMS_MEDIA_TYPE = 13,
NTMS_PARTITION = 14,
NTMS_PHYSICAL_MEDIA = 15,
NTMS_STORAGESLOT = 16,
NTMS_OPREQUEST = 17,
NTMS_UI_DESTINATION = 18
        

NTMS_OPREQ_UNKNOWN = 0,
NTMS_OPREQ_NEWMEDIA = 1,
NTMS_OPREQ_CLEANER = 2,
NTMS_OPREQ_DEVICESERVICE = 3,
NTMS_OPREQ_MOVEMEDIA = 4,
NTMS_OPREQ_MESSAGE = 5
        

NTMS_OBJ_UPDATE = 1,
NTMS_OBJ_INSERT = 2,
NTMS_OBJ_DELETE = 3,
NTMS_EVENT_SIGNAL = 4,
NTMS_EVENT_COMPLETE = 5
        

NTMS_DISMOUNT_DEFERRED = 1,
NTMS_DISMOUNT_IMMEDIATE = 2
        

NTMS_LM_QUEUED = 0,
NTMS_LM_INPROCESS = 1,
NTMS_LM_PASSED = 2,
NTMS_LM_FAILED = 3,
NTMS_LM_INVALID = 4,
NTMS_LM_WAITING = 5,
NTMS_LM_CANCELLED = 7,
NTMS_LM_STOPPED = 8
        

NTMS_EJECT_START = 0,
NTMS_EJECT_STOP = 1,
NTMS_EJECT_QUEUE = 2,
NTMS_EJECT_FORCE = 3,
NTMS_EJECT_IMMEDIATE = 4,
NTMS_EJECT_ASK_USER = 5
        

NTMS_INJECT_START = 0,
NTMS_INJECT_STOP = 1,
NTMS_INJECT_RETRACT = 2,
NTMS_INJECT_STARTMANY = 3
        

NTMS_INVENTORY_NONE = 0,
NTMS_INVENTORY_FAST = 1,
NTMS_INVENTORY_OMID = 2,
NTMS_INVENTORY_DEFAULT = 3,
NTMS_INVENTORY_SLOT = 4,
NTMS_INVENTORY_STOP = 5,
NTMS_INVENTORY_MAX = 6
        

NTMS_ALLOCATE_NEW = 1,
NTMS_ALLOCATE_NEXT = 2,
NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE = 4
        

NTMS_OPEN_EXISTING = 1,
NTMS_CREATE_NEW = 2,
NTMS_OPEN_ALWAYS = 3
        

NTMS_MOUNT_READ = 1,
NTMS_MOUNT_WRITE = 2,
NTMS_MOUNT_ERROR_NOT_AVAILABLE = 4,
NTMS_MOUNT_ERROR_OFFLINE = 8,
NTMS_MOUNT_SPECIFIC_DRIVE = 16,
NTMS_MOUNT_NOWAIT = 32
        

NTMS_PRIORITY_DEFAULT = 0,
NTMS_PRIORITY_HIGHEST = 15,
NTMS_PRIORITY_HIGH = 7,
NTMS_PRIORITY_NORMAL = 0,
NTMS_PRIORITY_LOW = -7,
NTMS_PRIORITY_LOWEST = -15
        

NTMS_BARCODESTATE_OK = 1,
NTMS_BARCODESTATE_UNREADABLE = 2
        

NTMS_DRIVESTATE_DISMOUNTED = 0,
NTMS_DRIVESTATE_MOUNTED = 1,
NTMS_DRIVESTATE_LOADED = 2,
NTMS_DRIVESTATE_UNLOADED = 5,
NTMS_DRIVESTATE_BEING_CLEANED = 6,
NTMS_DRIVESTATE_DISMOUNTABLE = 7
        

NTMS_LM_REMOVE = 0,
NTMS_LM_DISABLECHANGER = 1,
NTMS_LM_DISABLELIBRARY = 1,
NTMS_LM_ENABLECHANGER = 2,
NTMS_LM_ENABLELIBRARY = 2,
NTMS_LM_DISABLEDRIVE = 3,
NTMS_LM_ENABLEDRIVE = 4,
NTMS_LM_DISABLEMEDIA = 5,
NTMS_LM_ENABLEMEDIA = 6,
NTMS_LM_UPDATEOMID = 7,
NTMS_LM_INVENTORY = 8,
NTMS_LM_DOORACCESS = 9,
NTMS_LM_EJECT = 10,
NTMS_LM_EJECTCLEANER = 11,
NTMS_LM_INJECT = 12,
NTMS_LM_INJECTCLEANER = 13,
NTMS_LM_PROCESSOMID = 14,
NTMS_LM_CLEANDRIVE = 15,
NTMS_LM_DISMOUNT = 16,
NTMS_LM_MOUNT = 17,
NTMS_LM_WRITESCRATCH = 18,
NTMS_LM_CLASSIFY = 19,
NTMS_LM_RESERVECLEANER = 20,
NTMS_LM_RELEASECLEANER = 21
        

NTMS_MEDIASTATE_IDLE = 0,
NTMS_MEDIASTATE_INUSE = 1,
NTMS_MEDIASTATE_MOUNTED = 2,
NTMS_MEDIASTATE_LOADED = 3,
NTMS_MEDIASTATE_UNLOADED = 4,
NTMS_MEDIASTATE_OPERROR = 5,
NTMS_MEDIASTATE_OPREQ = 6
        

NTMS_READY = 0,
NTMS_INITIALIZING = 10,
NTMS_NEEDS_SERVICE = 20,
NTMS_NOT_PRESENT = 21
        

NTMS_OPSTATE_UNKNOWN = 0,
NTMS_OPSTATE_SUBMITTED = 1,
NTMS_OPSTATE_ACTIVE = 2,
NTMS_OPSTATE_INPROGRESS = 3,
NTMS_OPSTATE_REFUSED = 4,
NTMS_OPSTATE_COMPLETE = 5
        

NTMS_PARTSTATE_UNKNOWN = 0,
NTMS_PARTSTATE_UNPREPARED = 1,
NTMS_PARTSTATE_INCOMPATIBLE = 2,
NTMS_PARTSTATE_DECOMMISSIONED = 3,
NTMS_PARTSTATE_AVAILABLE = 4,
NTMS_PARTSTATE_ALLOCATED = 5,
NTMS_PARTSTATE_COMPLETE = 6,
NTMS_PARTSTATE_FOREIGN = 7,
NTMS_PARTSTATE_IMPORT = 8,
NTMS_PARTSTATE_RESERVED = 9
        

NTMS_UIDEST_ADD = 1,
NTMS_UIDEST_DELETE = 2,
NTMS_UIDEST_DELETEALL = 3
        

NTMS_UITYPE_INVALID = 0,
NTMS_UITYPE_INFO = 1,
NTMS_UITYPE_REQ = 2,
NTMS_UITYPE_ERR = 3,
NTMS_UITYPE_MAX = 4
        

NTMS_USE_ACCESS = 1,
NTMS_MODIFY_ACCESS = 2,
NTMS_CONTROL_ACCESS = 3
        

class NTMS_LIBRARYINFORMATION(NDRSTRUCT):
    structure = (
        ('LibraryType', DWORD),('CleanerSlot', NTMS_GUID),('CleanerSlotDefault', NTMS_GUID),('LibrarySupportsDriveCleaning', BOOL),('BarCodeReaderInstalled', BOOL),('InventoryMethod', DWORD),('dwCleanerUsesRemaining', DWORD),('FirstDriveNumber', DWORD),('dwNumberOfDrives', DWORD),('FirstSlotNumber', DWORD),('dwNumberOfSlots', DWORD),('FirstDoorNumber', DWORD),('dwNumberOfDoors', DWORD),('FirstPortNumber', DWORD),('dwNumberOfPorts', DWORD),('FirstChangerNumber', DWORD),('dwNumberOfChangers', DWORD),('dwNumberOfMedia', DWORD),('dwNumberOfMediaTypes', DWORD),('dwNumberOfLibRequests', DWORD),('Reserved', GUID),('AutoRecovery', BOOL),('dwFlags', DWORD),
    )


class DATA_SECURITY_ATTRIBUTES_NTMS(NDRUniConformantArray):
    item = BYTE

class PTR_SECURITY_ATTRIBUTES_NTMS(NDRPOINTER):
    referent = (
        ('Data', DATA_SECURITY_ATTRIBUTES_NTMS),
    )

class SECURITY_ATTRIBUTES_NTMS(NDRSTRUCT):
    structure = (
	('nLength', DWORD),	('lpSecurityDescriptor', PTR_SECURITY_ATTRIBUTES_NTMS),
	('bInheritHandle', BOOL),	('nDescriptorLength', DWORD),
    )
        

class NTMS_ALLOCATION_INFORMATION(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('lpReserved', BYTE),('AllocatedFrom', NTMS_GUID),
    )
class LPNTMS_ALLOCATION_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NTMS_ALLOCATION_INFORMATION),
    )    


class NTMS_ASYNC_IO(NDRSTRUCT):
    structure = (
        ('OperationId', NTMS_GUID),('EventId', NTMS_GUID),('dwOperationType', DWORD),('dwResult', DWORD),('dwAsyncState', DWORD),('hEvent', NTMS_HANDLE),('hEvent', PVOID),('bOnStateChange', BOOL),
    )
class LPNTMS_ASYNC_IO(NDRPOINTER):
    referent = (
        ('Data', NTMS_ASYNC_IO),
    )    


class NTMS_MOUNT_INFORMATION(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('lpReserved', LPNTMS_ASYNC_IO),('lpReserved', LPVOID),
    )
class LPNTMS_MOUNT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NTMS_MOUNT_INFORMATION),
    )    


class NTMS_CHANGERINFORMATIONA(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('ChangerType', NTMS_GUID),('szSerialNumber', CHAR),('szRevision', CHAR),('szDeviceName', CHAR),('ScsiPort', UNSIGNED_SHORT),('ScsiBus', UNSIGNED_SHORT),('ScsiTarget', UNSIGNED_SHORT),('ScsiLun', UNSIGNED_SHORT),('Library', NTMS_GUID),
    )


class NTMS_CHANGERINFORMATIONW(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('ChangerType', NTMS_GUID),('szSerialNumber', WCHAR_T),('szRevision', WCHAR_T),('szDeviceName', WCHAR_T),('ScsiPort', UNSIGNED_SHORT),('ScsiBus', UNSIGNED_SHORT),('ScsiTarget', UNSIGNED_SHORT),('ScsiLun', UNSIGNED_SHORT),('Library', NTMS_GUID),
    )


class NTMS_CHANGERTYPEINFORMATIONA(NDRSTRUCT):
    structure = (
        ('szVendor', CHAR),('szProduct', CHAR),('DeviceType', DWORD),
    )


class NTMS_CHANGERTYPEINFORMATIONW(NDRSTRUCT):
    structure = (
        ('szVendor', WCHAR_T),('szProduct', WCHAR_T),('DeviceType', DWORD),
    )


class NTMS_DRIVEINFORMATIONA(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('State', DWORD),('DriveType', NTMS_GUID),('szDeviceName', CHAR),('szSerialNumber', CHAR),('szRevision', CHAR),('ScsiPort', UNSIGNED_SHORT),('ScsiBus', UNSIGNED_SHORT),('ScsiTarget', UNSIGNED_SHORT),('ScsiLun', UNSIGNED_SHORT),('dwMountCount', DWORD),('LastCleanedTs', SYSTEMTIME),('SavedPartitionId', NTMS_GUID),('Library', NTMS_GUID),('Reserved', GUID),('dwDeferDismountDelay', DWORD),
    )


class NTMS_DRIVEINFORMATIONW(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('State', DWORD),('DriveType', NTMS_GUID),('szDeviceName', WCHAR_T),('szSerialNumber', WCHAR_T),('szRevision', WCHAR_T),('ScsiPort', UNSIGNED_SHORT),('ScsiBus', UNSIGNED_SHORT),('ScsiTarget', UNSIGNED_SHORT),('ScsiLun', UNSIGNED_SHORT),('dwMountCount', DWORD),('LastCleanedTs', SYSTEMTIME),('SavedPartitionId', NTMS_GUID),('Library', NTMS_GUID),('Reserved', GUID),('dwDeferDismountDelay', DWORD),
    )


class NTMS_DRIVETYPEINFORMATIONA(NDRSTRUCT):
    structure = (
        ('szVendor', CHAR),('szProduct', CHAR),('NumberOfHeads', DWORD),('DeviceType', DWORD),
    )


class NTMS_DRIVETYPEINFORMATIONW(NDRSTRUCT):
    structure = (
        ('szVendor', WCHAR_T),('szProduct', WCHAR_T),('NumberOfHeads', DWORD),('DeviceType', DWORD),
    )


class NTMS_LIBREQUESTINFORMATIONA(NDRSTRUCT):
    structure = (
        ('OperationCode', DWORD),('OperationOption', DWORD),('State', DWORD),('PartitionId', NTMS_GUID),('DriveId', NTMS_GUID),('PhysMediaId', NTMS_GUID),('Library', NTMS_GUID),('SlotId', NTMS_GUID),('TimeQueued', SYSTEMTIME),('TimeCompleted', SYSTEMTIME),('szApplication', CHAR),('szUser', CHAR),('szComputer', CHAR),('dwErrorCode', DWORD),('WorkItemId', NTMS_GUID),('dwPriority', DWORD),
    )


class NTMS_LIBREQUESTINFORMATIONW(NDRSTRUCT):
    structure = (
        ('OperationCode', DWORD),('OperationOption', DWORD),('State', DWORD),('PartitionId', NTMS_GUID),('DriveId', NTMS_GUID),('PhysMediaId', NTMS_GUID),('Library', NTMS_GUID),('SlotId', NTMS_GUID),('TimeQueued', SYSTEMTIME),('TimeCompleted', SYSTEMTIME),('szApplication', WCHAR_T),('szUser', WCHAR_T),('szComputer', WCHAR_T),('dwErrorCode', DWORD),('WorkItemId', NTMS_GUID),('dwPriority', DWORD),
    )


class NTMS_MEDIAPOOLINFORMATION(NDRSTRUCT):
    structure = (
        ('PoolType', DWORD),('MediaType', NTMS_GUID),('Parent', NTMS_GUID),('AllocationPolicy', DWORD),('DeallocationPolicy', DWORD),('dwMaxAllocates', DWORD),('dwNumberOfPhysicalMedia', DWORD),('dwNumberOfLogicalMedia', DWORD),('dwNumberOfMediaPools', DWORD),
    )


class NTMS_MEDIATYPEINFORMATION(NDRSTRUCT):
    structure = (
        ('MediaType', DWORD),('NumberOfSides', DWORD),('ReadWriteCharacteristics', DWORD),('DeviceType', DWORD),
    )


class NTMS_STORAGESLOTINFORMATION(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('State', DWORD),('Library', NTMS_GUID),
    )


class NTMS_IEDOORINFORMATION(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('State', DWORD),('MaxOpenSecs', UNSIGNED_SHORT),('Library', NTMS_GUID),
    )


class NTMS_IEPORTINFORMATION(NDRSTRUCT):
    structure = (
        ('Number', DWORD),('Content', DWORD),('Position', DWORD),('MaxExtendSecs', UNSIGNED_SHORT),('Library', NTMS_GUID),
    )


class NTMS_LMIDINFORMATION(NDRSTRUCT):
    structure = (
        ('MediaPool', NTMS_GUID),('dwNumberOfPartitions', DWORD),
    )


class NTMS_COMPUTERINFORMATION(NDRSTRUCT):
    structure = (
        ('dwLibRequestPurgeTime', DWORD),('dwOpRequestPurgeTime', DWORD),('dwLibRequestFlags', DWORD),('dwOpRequestFlags', DWORD),('dwMediaPoolPolicy', DWORD),
    )


class NTMS_OPREQUESTINFORMATIONA(NDRSTRUCT):
    structure = (
        ('Request', DWORD),('Submitted', SYSTEMTIME),('State', DWORD),('szMessage', CHAR),('Arg1Type', DWORD),('Arg1', NTMS_GUID),('Arg2Type', DWORD),('Arg2', NTMS_GUID),('szApplication', CHAR),('szUser', CHAR),('szComputer', CHAR),
    )


class NTMS_OPREQUESTINFORMATIONW(NDRSTRUCT):
    structure = (
        ('Request', DWORD),('Submitted', SYSTEMTIME),('State', DWORD),('szMessage', WCHAR_T),('Arg1Type', DWORD),('Arg1', NTMS_GUID),('Arg2Type', DWORD),('Arg2', NTMS_GUID),('szApplication', WCHAR_T),('szUser', WCHAR_T),('szComputer', WCHAR_T),
    )


class NTMS_PARTITIONINFORMATIONA(NDRSTRUCT):
    structure = (
        ('PhysicalMedia', NTMS_GUID),('LogicalMedia', NTMS_GUID),('State', DWORD),('Side', UNSIGNED_SHORT),('dwOmidLabelIdLength', DWORD),('OmidLabelId', BYTE),('szOmidLabelType', CHAR),('szOmidLabelInfo', CHAR),('dwMountCount', DWORD),('dwAllocateCount', DWORD),('Capacity', LARGE_INTEGER),
    )


class NTMS_PARTITIONINFORMATIONW(NDRSTRUCT):
    structure = (
        ('PhysicalMedia', NTMS_GUID),('LogicalMedia', NTMS_GUID),('State', DWORD),('Side', UNSIGNED_SHORT),('dwOmidLabelIdLength', DWORD),('OmidLabelId', BYTE),('szOmidLabelType', WCHAR_T),('szOmidLabelInfo', WCHAR_T),('dwMountCount', DWORD),('dwAllocateCount', DWORD),('Capacity', LARGE_INTEGER),
    )


class NTMS_PMIDINFORMATIONA(NDRSTRUCT):
    structure = (
        ('CurrentLibrary', NTMS_GUID),('MediaPool', NTMS_GUID),('Location', NTMS_GUID),('LocationType', DWORD),('MediaType', NTMS_GUID),('HomeSlot', NTMS_GUID),('szBarCode', CHAR),('BarCodeState', DWORD),('szSequenceNumber', CHAR),('MediaState', DWORD),('dwNumberOfPartitions', DWORD),('dwMediaTypeCode', DWORD),('dwDensityCode', DWORD),('MountedPartition', NTMS_GUID),
    )


class NTMS_PMIDINFORMATIONW(NDRSTRUCT):
    structure = (
        ('CurrentLibrary', NTMS_GUID),('MediaPool', NTMS_GUID),('Location', NTMS_GUID),('LocationType', DWORD),('MediaType', NTMS_GUID),('HomeSlot', NTMS_GUID),('szBarCode', WCHAR_T),('BarCodeState', DWORD),('szSequenceNumber', WCHAR_T),('MediaState', DWORD),('dwNumberOfPartitions', DWORD),('dwMediaTypeCode', DWORD),('dwDensityCode', DWORD),('MountedPartition', NTMS_GUID),
    )


class RSM_MESSAGE(NDRSTRUCT):
    structure = (
        ('lpguidOperation', LPGUID),('dwNtmsType', DWORD),('dwState', DWORD),('dwFlags', DWORD),('dwPriority', DWORD),('dwErrorCode', DWORD),('lpszComputerName', WCHAR_T),('lpszApplication', WCHAR_T),('lpszUser', WCHAR_T),('lpszTimeSubmitted', WCHAR_T),('lpszMessage', WCHAR_T),
    )
class LPRSM_MESSAGE(NDRPOINTER):
    referent = (
        ('Data', RSM_MESSAGE),
    )    


class INFO(NDRUNION):
    union = {
        NTMS_DRIVE: ('Drive',NTMS_DRIVEINFORMATIONA),NTMS_DRIVE_TYPE: ('DriveType',NTMS_DRIVETYPEINFORMATIONA),NTMS_LIBRARY: ('Library',NTMS_LIBRARYINFORMATION),NTMS_CHANGER: ('Changer',NTMS_CHANGERINFORMATIONA),NTMS_CHANGER_TYPE: ('ChangerType',NTMS_CHANGERTYPEINFORMATIONA),NTMS_STORAGESLOT: ('StorageSlot',NTMS_STORAGESLOTINFORMATION),NTMS_IEDOOR: ('IEDoor',NTMS_IEDOORINFORMATION),NTMS_IEPORT: ('IEPort',NTMS_IEPORTINFORMATION),NTMS_PHYSICAL_MEDIA: ('PhysicalMedia',NTMS_PMIDINFORMATIONA),NTMS_LOGICAL_MEDIA: ('LogicalMedia',NTMS_LMIDINFORMATION),NTMS_PARTITION: ('Partition',NTMS_PARTITIONINFORMATIONA),NTMS_MEDIA_POOL: ('MediaPool',NTMS_MEDIAPOOLINFORMATION),NTMS_MEDIA_TYPE: ('MediaType',NTMS_MEDIATYPEINFORMATION),NTMS_LIBREQUEST: ('LibRequest',NTMS_LIBREQUESTINFORMATIONA),NTMS_OPREQUEST: ('OpRequest',NTMS_OPREQUESTINFORMATIONA),NTMS_COMPUTER: ('Computer',NTMS_COMPUTERINFORMATION),
    }
        

class NTMS_OBJECTINFORMATIONA(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('dwType', DWORD),('Created', SYSTEMTIME),('Modified', SYSTEMTIME),('ObjectGuid', NTMS_GUID),('Enabled', BOOL),('dwOperationalState', DWORD),('szName', CHAR),('szDescription', CHAR),('Info', INFO),
    )
class LPNTMS_OBJECTINFORMATIONA(NDRPOINTER):
    referent = (
        ('Data', NTMS_OBJECTINFORMATIONA),
    )    


class INFO(NDRUNION):
    union = {
        NTMS_DRIVE: ('Drive',NTMS_DRIVEINFORMATIONW),NTMS_DRIVE_TYPE: ('DriveType',NTMS_DRIVETYPEINFORMATIONW),NTMS_LIBRARY: ('Library',NTMS_LIBRARYINFORMATION),NTMS_CHANGER: ('Changer',NTMS_CHANGERINFORMATIONW),NTMS_CHANGER_TYPE: ('ChangerType',NTMS_CHANGERTYPEINFORMATIONW),NTMS_STORAGESLOT: ('StorageSlot',NTMS_STORAGESLOTINFORMATION),NTMS_IEDOOR: ('IEDoor',NTMS_IEDOORINFORMATION),NTMS_IEPORT: ('IEPort',NTMS_IEPORTINFORMATION),NTMS_PHYSICAL_MEDIA: ('PhysicalMedia',NTMS_PMIDINFORMATIONW),NTMS_LOGICAL_MEDIA: ('LogicalMedia',NTMS_LMIDINFORMATION),NTMS_PARTITION: ('Partition',NTMS_PARTITIONINFORMATIONW),NTMS_MEDIA_POOL: ('MediaPool',NTMS_MEDIAPOOLINFORMATION),NTMS_MEDIA_TYPE: ('MediaType',NTMS_MEDIATYPEINFORMATION),NTMS_LIBREQUEST: ('LibRequest',NTMS_LIBREQUESTINFORMATIONW),NTMS_OPREQUEST: ('OpRequest',NTMS_OPREQUESTINFORMATIONW),NTMS_COMPUTER: ('Computer',NTMS_COMPUTERINFORMATION),
    }
        

class NTMS_OBJECTINFORMATIONW(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('dwType', DWORD),('Created', SYSTEMTIME),('Modified', SYSTEMTIME),('ObjectGuid', NTMS_GUID),('Enabled', BOOL),('dwOperationalState', DWORD),('szName', WCHAR_T),('szDescription', WCHAR_T),('Info', INFO),
    )
class LPNTMS_OBJECTINFORMATIONW(NDRPOINTER):
    referent = (
        ('Data', NTMS_OBJECTINFORMATIONW),
    )    

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#INtmsLibraryControl1 Definition

#################################################################################

MSRPC_UUID_INTMSLIBRARYCONTROL1 = uuidtup_to_bin(('4e934f30-341a-11d1-8fb1-00a024cb6019','0.0'))


class EjectNtmsMedia(NDRCALL):
    opnum = 0
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('lpEjectOperation', LPNTMS_GUID),
		('dwAction', DWORD),
    )

class EjectNtmsMediaResponse(NDRCALL):
    structure = (
		('lpEjectOperation', LPNTMS_GUID),
    )
        

class InjectNtmsMedia(NDRCALL):
    opnum = 1
    structure = (
		('lpLibraryId', LPNTMS_GUID),
		('lpInjectOperation', LPNTMS_GUID),
		('dwAction', DWORD),
    )

class InjectNtmsMediaResponse(NDRCALL):
    structure = (
		('lpInjectOperation', LPNTMS_GUID),
    )
        

class AccessNtmsLibraryDoor(NDRCALL):
    opnum = 2
    structure = (
		('lpLibraryId', LPNTMS_GUID),
		('dwAction', DWORD),
    )

class AccessNtmsLibraryDoorResponse(NDRCALL):
    structure = (

    )
        

class CleanNtmsDrive(NDRCALL):
    opnum = 3
    structure = (
		('lpDriveId', LPNTMS_GUID),
    )

class CleanNtmsDriveResponse(NDRCALL):
    structure = (

    )
        

class DismountNtmsDrive(NDRCALL):
    opnum = 4
    structure = (
		('lpDriveId', LPNTMS_GUID),
    )

class DismountNtmsDriveResponse(NDRCALL):
    structure = (

    )
        

class InventoryNtmsLibrary(NDRCALL):
    opnum = 5
    structure = (
		('lpLibraryId', LPNTMS_GUID),
		('dwAction', DWORD),
    )

class InventoryNtmsLibraryResponse(NDRCALL):
    structure = (

    )
        

class INtmsLibraryControl1_LocalOnlyOpnum09(NDRCALL):
    opnum = 6
    structure = (

    )

class INtmsLibraryControl1_LocalOnlyOpnum09Response(NDRCALL):
    structure = (

    )
        

class CancelNtmsLibraryRequest(NDRCALL):
    opnum = 7
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )

class CancelNtmsLibraryRequestResponse(NDRCALL):
    structure = (

    )
        

class ReserveNtmsCleanerSlot(NDRCALL):
    opnum = 8
    structure = (
		('lpLibrary', LPNTMS_GUID),
		('lpSlot', LPNTMS_GUID),
    )

class ReserveNtmsCleanerSlotResponse(NDRCALL):
    structure = (

    )
        

class ReleaseNtmsCleanerSlot(NDRCALL):
    opnum = 9
    structure = (
		('lpLibrary', LPNTMS_GUID),
    )

class ReleaseNtmsCleanerSlotResponse(NDRCALL):
    structure = (

    )
        

class InjectNtmsCleaner(NDRCALL):
    opnum = 10
    structure = (
		('lpLibrary', LPNTMS_GUID),
		('lpInjectOperation', LPNTMS_GUID),
		('dwNumberOfCleansLeft', DWORD),
		('dwAction', DWORD),
    )

class InjectNtmsCleanerResponse(NDRCALL):
    structure = (
		('lpInjectOperation', LPNTMS_GUID),
    )
        

class EjectNtmsCleaner(NDRCALL):
    opnum = 11
    structure = (
		('lpLibrary', LPNTMS_GUID),
		('lpEjectOperation', LPNTMS_GUID),
		('dwAction', DWORD),
    )

class EjectNtmsCleanerResponse(NDRCALL):
    structure = (
		('lpEjectOperation', LPNTMS_GUID),
    )
        

class DeleteNtmsLibrary(NDRCALL):
    opnum = 12
    structure = (
		('lpLibraryId', LPNTMS_GUID),
    )

class DeleteNtmsLibraryResponse(NDRCALL):
    structure = (

    )
        

class DeleteNtmsDrive(NDRCALL):
    opnum = 13
    structure = (
		('lpDriveId', LPNTMS_GUID),
    )

class DeleteNtmsDriveResponse(NDRCALL):
    structure = (

    )
        

class GetNtmsRequestOrder(NDRCALL):
    opnum = 14
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )

class GetNtmsRequestOrderResponse(NDRCALL):
    structure = (
		('lpdwOrderNumber', DWORD),
    )
        

class SetNtmsRequestOrder(NDRCALL):
    opnum = 15
    structure = (
		('lpRequestId', LPNTMS_GUID),
		('dwOrderNumber', DWORD),
    )

class SetNtmsRequestOrderResponse(NDRCALL):
    structure = (

    )
        

class DeleteNtmsRequests(NDRCALL):
    opnum = 16
    structure = (
		('lpRequestId', LPNTMS_GUID),
		('dwType', DWORD),
		('dwCount', DWORD),
    )

class DeleteNtmsRequestsResponse(NDRCALL):
    structure = (

    )
        

class BeginNtmsDeviceChangeDetection(NDRCALL):
    opnum = 17
    structure = (

    )

class BeginNtmsDeviceChangeDetectionResponse(NDRCALL):
    structure = (
		('lpDetectHandle', NTMS_HANDLE),
    )
        

class SetNtmsDeviceChangeDetection(NDRCALL):
    opnum = 18
    structure = (
		('DetectHandle', NTMS_HANDLE),
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('dwCount', DWORD),
    )

class SetNtmsDeviceChangeDetectionResponse(NDRCALL):
    structure = (

    )
        

class EndNtmsDeviceChangeDetection(NDRCALL):
    opnum = 19
    structure = (
		('DetectHandle', NTMS_HANDLE),
    )

class EndNtmsDeviceChangeDetectionResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (EjectNtmsMedia,EjectNtmsMediaResponse),
1 : (InjectNtmsMedia,InjectNtmsMediaResponse),
2 : (AccessNtmsLibraryDoor,AccessNtmsLibraryDoorResponse),
3 : (CleanNtmsDrive,CleanNtmsDriveResponse),
4 : (DismountNtmsDrive,DismountNtmsDriveResponse),
5 : (InventoryNtmsLibrary,InventoryNtmsLibraryResponse),
6 : (INtmsLibraryControl1_LocalOnlyOpnum09,INtmsLibraryControl1_LocalOnlyOpnum09Response),
7 : (CancelNtmsLibraryRequest,CancelNtmsLibraryRequestResponse),
8 : (ReserveNtmsCleanerSlot,ReserveNtmsCleanerSlotResponse),
9 : (ReleaseNtmsCleanerSlot,ReleaseNtmsCleanerSlotResponse),
10 : (InjectNtmsCleaner,InjectNtmsCleanerResponse),
11 : (EjectNtmsCleaner,EjectNtmsCleanerResponse),
12 : (DeleteNtmsLibrary,DeleteNtmsLibraryResponse),
13 : (DeleteNtmsDrive,DeleteNtmsDriveResponse),
14 : (GetNtmsRequestOrder,GetNtmsRequestOrderResponse),
15 : (SetNtmsRequestOrder,SetNtmsRequestOrderResponse),
16 : (DeleteNtmsRequests,DeleteNtmsRequestsResponse),
17 : (BeginNtmsDeviceChangeDetection,BeginNtmsDeviceChangeDetectionResponse),
18 : (SetNtmsDeviceChangeDetection,SetNtmsDeviceChangeDetectionResponse),
19 : (EndNtmsDeviceChangeDetection,EndNtmsDeviceChangeDetectionResponse),
}

#################################################################################

#INtmsMediaServices1 Definition

#################################################################################

MSRPC_UUID_INTMSMEDIASERVICES1 = uuidtup_to_bin(('d02e4be0-3419-111-8b1-00024b6019','0.0'))


class MountNtmsMedia(NDRCALL):
    opnum = 0
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('lpDriveId', LPNTMS_GUID),
		('dwCount', DWORD),
		('dwOptions', DWORD),
		('dwPriority', INT),
		('dwTimeout', DWORD),
		('lpMountInformation', LPNTMS_MOUNT_INFORMATION),
    )

class MountNtmsMediaResponse(NDRCALL):
    structure = (
		('lpDriveId', LPNTMS_GUID),
		('lpMountInformation', LPNTMS_MOUNT_INFORMATION),
    )
        

class DismountNtmsMedia(NDRCALL):
    opnum = 1
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('dwCount', DWORD),
		('dwOptions', DWORD),
    )

class DismountNtmsMediaResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 2
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class AllocateNtmsMedia(NDRCALL):
    opnum = 3
    structure = (
		('lpMediaPool', LPNTMS_GUID),
		('lpPartition', LPNTMS_GUID),
		('lpMediaId', LPNTMS_GUID),
		('dwOptions', DWORD),
		('dwTimeout', DWORD),
		('lpAllocateInformation', LPNTMS_ALLOCATION_INFORMATION),
    )

class AllocateNtmsMediaResponse(NDRCALL):
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('lpAllocateInformation', LPNTMS_ALLOCATION_INFORMATION),
    )
        

class DeallocateNtmsMedia(NDRCALL):
    opnum = 4
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('dwOptions', DWORD),
    )

class DeallocateNtmsMediaResponse(NDRCALL):
    structure = (

    )
        

class SwapNtmsMedia(NDRCALL):
    opnum = 5
    structure = (
		('lpMediaId1', LPNTMS_GUID),
		('lpMediaId2', LPNTMS_GUID),
    )

class SwapNtmsMediaResponse(NDRCALL):
    structure = (

    )
        

class DecommissionNtmsMedia(NDRCALL):
    opnum = 6
    structure = (
		('lpMediaId', LPNTMS_GUID),
    )

class DecommissionNtmsMediaResponse(NDRCALL):
    structure = (

    )
        

class SetNtmsMediaComplete(NDRCALL):
    opnum = 7
    structure = (
		('lpMediaId', LPNTMS_GUID),
    )

class SetNtmsMediaCompleteResponse(NDRCALL):
    structure = (

    )
        

class DeleteNtmsMedia(NDRCALL):
    opnum = 8
    structure = (
		('lpMediaId', LPNTMS_GUID),
    )

class DeleteNtmsMediaResponse(NDRCALL):
    structure = (

    )
        

class CreateNtmsMediaPoolA(NDRCALL):
    opnum = 9
    structure = (
		('lpPoolName', CONST_CHAR),
		('lpMediaType', LPNTMS_GUID),
		('dwOptions', DWORD),
		('lpSecurityAttributes', LPSECURITY_ATTRIBUTES_NTMS),
    )

class CreateNtmsMediaPoolAResponse(NDRCALL):
    structure = (
		('lpPoolId', LPNTMS_GUID),
    )
        

class CreateNtmsMediaPoolW(NDRCALL):
    opnum = 10
    structure = (
		('lpPoolName', CONST_WCHAR_T),
		('lpMediaType', LPNTMS_GUID),
		('dwOptions', DWORD),
		('lpSecurityAttributes', LPSECURITY_ATTRIBUTES_NTMS),
    )

class CreateNtmsMediaPoolWResponse(NDRCALL):
    structure = (
		('lpPoolId', LPNTMS_GUID),
    )
        

class GetNtmsMediaPoolNameA(NDRCALL):
    opnum = 11
    structure = (
		('lpPoolId', LPNTMS_GUID),
		('lpdwNameSizeBuf', DWORD),
    )

class GetNtmsMediaPoolNameAResponse(NDRCALL):
    structure = (
		('lpBufName', UNSIGNED_CHAR),
		('lpdwNameSize', DWORD),
    )
        

class GetNtmsMediaPoolNameW(NDRCALL):
    opnum = 12
    structure = (
		('lpPoolId', LPNTMS_GUID),
		('lpdwNameSizeBuf', DWORD),
    )

class GetNtmsMediaPoolNameWResponse(NDRCALL):
    structure = (
		('lpBufName', WCHAR_T),
		('lpdwNameSize', DWORD),
    )
        

class MoveToNtmsMediaPool(NDRCALL):
    opnum = 13
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('lpPoolId', LPNTMS_GUID),
    )

class MoveToNtmsMediaPoolResponse(NDRCALL):
    structure = (

    )
        

class DeleteNtmsMediaPool(NDRCALL):
    opnum = 14
    structure = (
		('lpPoolId', LPNTMS_GUID),
    )

class DeleteNtmsMediaPoolResponse(NDRCALL):
    structure = (

    )
        

class AddNtmsMediaType(NDRCALL):
    opnum = 15
    structure = (
		('lpMediaTypeId', LPNTMS_GUID),
		('lpLibId', LPNTMS_GUID),
    )

class AddNtmsMediaTypeResponse(NDRCALL):
    structure = (

    )
        

class DeleteNtmsMediaType(NDRCALL):
    opnum = 16
    structure = (
		('lpMediaTypeId', LPNTMS_GUID),
		('lpLibId', LPNTMS_GUID),
    )

class DeleteNtmsMediaTypeResponse(NDRCALL):
    structure = (

    )
        

class ChangeNtmsMediaType(NDRCALL):
    opnum = 17
    structure = (
		('lpMediaId', LPNTMS_GUID),
		('lpPoolId', LPNTMS_GUID),
    )

class ChangeNtmsMediaTypeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (MountNtmsMedia,MountNtmsMediaResponse),
1 : (DismountNtmsMedia,DismountNtmsMediaResponse),
2 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
3 : (AllocateNtmsMedia,AllocateNtmsMediaResponse),
4 : (DeallocateNtmsMedia,DeallocateNtmsMediaResponse),
5 : (SwapNtmsMedia,SwapNtmsMediaResponse),
6 : (DecommissionNtmsMedia,DecommissionNtmsMediaResponse),
7 : (SetNtmsMediaComplete,SetNtmsMediaCompleteResponse),
8 : (DeleteNtmsMedia,DeleteNtmsMediaResponse),
9 : (CreateNtmsMediaPoolA,CreateNtmsMediaPoolAResponse),
10 : (CreateNtmsMediaPoolW,CreateNtmsMediaPoolWResponse),
11 : (GetNtmsMediaPoolNameA,GetNtmsMediaPoolNameAResponse),
12 : (GetNtmsMediaPoolNameW,GetNtmsMediaPoolNameWResponse),
13 : (MoveToNtmsMediaPool,MoveToNtmsMediaPoolResponse),
14 : (DeleteNtmsMediaPool,DeleteNtmsMediaPoolResponse),
15 : (AddNtmsMediaType,AddNtmsMediaTypeResponse),
16 : (DeleteNtmsMediaType,DeleteNtmsMediaTypeResponse),
17 : (ChangeNtmsMediaType,ChangeNtmsMediaTypeResponse),
}

#################################################################################

#INtmsObjectInfo1 Definition

#################################################################################

MSRPC_UUID_INTMSOBJECTINFO1 = uuidtup_to_bin(('69ab7050-3059-11d1-8faf-00a024cb6019','0.0'))


class GetNtmsServerObjectInformationA(NDRCALL):
    opnum = 0
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('dwSize', DWORD),
    )

class GetNtmsServerObjectInformationAResponse(NDRCALL):
    structure = (
		('lpInfo', LPNTMS_OBJECTINFORMATIONA),
    )
        

class GetNtmsServerObjectInformationW(NDRCALL):
    opnum = 1
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('dwSize', DWORD),
    )

class GetNtmsServerObjectInformationWResponse(NDRCALL):
    structure = (
		('lpInfo', LPNTMS_OBJECTINFORMATIONW),
    )
        

class SetNtmsObjectInformationA(NDRCALL):
    opnum = 2
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('lpInfo', LPNTMS_OBJECTINFORMATIONA),
    )

class SetNtmsObjectInformationAResponse(NDRCALL):
    structure = (

    )
        

class SetNtmsObjectInformationW(NDRCALL):
    opnum = 3
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('lpInfo', LPNTMS_OBJECTINFORMATIONW),
    )

class SetNtmsObjectInformationWResponse(NDRCALL):
    structure = (

    )
        

class CreateNtmsMediaA(NDRCALL):
    opnum = 4
    structure = (
		('lpMedia', LPNTMS_OBJECTINFORMATIONA),
		('lpList', LPNTMS_OBJECTINFORMATIONA),
		('lpdwListBufferSize', DWORD),
		('dwListCount', DWORD),
		('dwOptions', DWORD),
    )

class CreateNtmsMediaAResponse(NDRCALL):
    structure = (
		('lpMedia', LPNTMS_OBJECTINFORMATIONA),
		('lpList', LPNTMS_OBJECTINFORMATIONA),
    )
        

class CreateNtmsMediaW(NDRCALL):
    opnum = 5
    structure = (
		('lpMedia', LPNTMS_OBJECTINFORMATIONW),
		('lpList', LPNTMS_OBJECTINFORMATIONW),
		('lpdwListBufferSize', DWORD),
		('dwListCount', DWORD),
		('dwOptions', DWORD),
    )

class CreateNtmsMediaWResponse(NDRCALL):
    structure = (
		('lpMedia', LPNTMS_OBJECTINFORMATIONW),
		('lpList', LPNTMS_OBJECTINFORMATIONW),
    )
        
OPNUMS = {
0 : (GetNtmsServerObjectInformationA,GetNtmsServerObjectInformationAResponse),
1 : (GetNtmsServerObjectInformationW,GetNtmsServerObjectInformationWResponse),
2 : (SetNtmsObjectInformationA,SetNtmsObjectInformationAResponse),
3 : (SetNtmsObjectInformationW,SetNtmsObjectInformationWResponse),
4 : (CreateNtmsMediaA,CreateNtmsMediaAResponse),
5 : (CreateNtmsMediaW,CreateNtmsMediaWResponse),
}

#################################################################################

#INtmsObjectManagement1 Definition

#################################################################################

MSRPC_UUID_INTMSOBJECTMANAGEMENT1 = uuidtup_to_bin(('b057dc50-3059-111-8af-00024b6019','0.0'))


class GetNtmsObjectSecurity(NDRCALL):
    opnum = 0
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('SecurityInformation', DWORD),
		('nLength', DWORD),
    )

class GetNtmsObjectSecurityResponse(NDRCALL):
    structure = (
		('lpSecurityDescriptor', PSECURITY_DESCRIPTOR_NTMS),
		('lpnLengthNeeded', DWORD),
    )
        

class SetNtmsObjectSecurity(NDRCALL):
    opnum = 1
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('SecurityInformation', DWORD),
		('lpSecurityDescriptor', PSECURITY_DESCRIPTOR_NTMS),
		('nLength', DWORD),
    )

class SetNtmsObjectSecurityResponse(NDRCALL):
    structure = (

    )
        

class GetNtmsObjectAttributeA(NDRCALL):
    opnum = 2
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_CHAR),
		('lpdwAttributeBufferSize', DWORD),
    )

class GetNtmsObjectAttributeAResponse(NDRCALL):
    structure = (
		('lpAttributeData', BYTE),
		('lpAttributeSize', DWORD),
    )
        

class GetNtmsObjectAttributeW(NDRCALL):
    opnum = 3
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_WCHAR_T),
		('lpdwAttributeBufferSize', DWORD),
    )

class GetNtmsObjectAttributeWResponse(NDRCALL):
    structure = (
		('lpAttributeData', BYTE),
		('lpAttributeSize', DWORD),
    )
        

class SetNtmsObjectAttributeA(NDRCALL):
    opnum = 4
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_CHAR),
		('lpAttributeData', BYTE),
		('AttributeSize', DWORD),
    )

class SetNtmsObjectAttributeAResponse(NDRCALL):
    structure = (

    )
        

class SetNtmsObjectAttributeW(NDRCALL):
    opnum = 5
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_WCHAR_T),
		('lpAttributeData', BYTE),
		('AttributeSize', DWORD),
    )

class SetNtmsObjectAttributeWResponse(NDRCALL):
    structure = (

    )
        

class EnumerateNtmsObject(NDRCALL):
    opnum = 6
    structure = (
		('lpContainerId',  LPNTMS_GUID),
		('lpdwListBufferSize', DWORD),
		('dwType', DWORD),
		('dwOptions', DWORD),
    )

class EnumerateNtmsObjectResponse(NDRCALL):
    structure = (
		('lpList', LPNTMS_GUID),
		('lpdwListSize', DWORD),
    )
        

class DisableNtmsObject(NDRCALL):
    opnum = 7
    structure = (
		('dwType', DWORD),
		('lpObjectId', LPNTMS_GUID),
    )

class DisableNtmsObjectResponse(NDRCALL):
    structure = (

    )
        

class EnableNtmsObject(NDRCALL):
    opnum = 8
    structure = (
		('dwType', DWORD),
		('lpObjectId', LPNTMS_GUID),
    )

class EnableNtmsObjectResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (GetNtmsObjectSecurity,GetNtmsObjectSecurityResponse),
1 : (SetNtmsObjectSecurity,SetNtmsObjectSecurityResponse),
2 : (GetNtmsObjectAttributeA,GetNtmsObjectAttributeAResponse),
3 : (GetNtmsObjectAttributeW,GetNtmsObjectAttributeWResponse),
4 : (SetNtmsObjectAttributeA,SetNtmsObjectAttributeAResponse),
5 : (SetNtmsObjectAttributeW,SetNtmsObjectAttributeWResponse),
6 : (EnumerateNtmsObject,EnumerateNtmsObjectResponse),
7 : (DisableNtmsObject,DisableNtmsObjectResponse),
8 : (EnableNtmsObject,EnableNtmsObjectResponse),
}

#################################################################################

#INtmsSession1 Definition

#################################################################################

MSRPC_UUID_INTMSSESSION1 = uuidtup_to_bin(('8da03f40-3419-11d1-8fb1-00a024cb6019','0.0'))


class OpenNtmsServerSessionW(NDRCALL):
    opnum = 0
    structure = (
		('lpServer', CONST_WCHAR_T),
		('lpApplication', CONST_WCHAR_T),
		('lpClientName', CONST_WCHAR_T),
		('lpUserName', CONST_WCHAR_T),
		('dwOptions', DWORD),
    )

class OpenNtmsServerSessionWResponse(NDRCALL):
    structure = (

    )
        

class OpenNtmsServerSessionA(NDRCALL):
    opnum = 1
    structure = (
		('lpServer', CONST_CHAR),
		('lpApplication', CONST_CHAR),
		('lpClientName', CONST_CHAR),
		('lpUserName', CONST_CHAR),
		('dwOptions', DWORD),
    )

class OpenNtmsServerSessionAResponse(NDRCALL):
    structure = (

    )
        

class CloseNtmsSession(NDRCALL):
    opnum = 2
    structure = (

    )

class CloseNtmsSessionResponse(NDRCALL):
    structure = (

    )
        

class SubmitNtmsOperatorRequestW(NDRCALL):
    opnum = 3
    structure = (
		('dwRequest', DWORD),
		('lpMessage', CONST_WCHAR_T),
		('lpArg1Id', LPNTMS_GUID),
		('lpArg2Id', LPNTMS_GUID),
    )

class SubmitNtmsOperatorRequestWResponse(NDRCALL):
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )
        

class SubmitNtmsOperatorRequestA(NDRCALL):
    opnum = 4
    structure = (
		('dwRequest', DWORD),
		('lpMessage', CONST_CHAR),
		('lpArg1Id', LPNTMS_GUID),
		('lpArg2Id', LPNTMS_GUID),
    )

class SubmitNtmsOperatorRequestAResponse(NDRCALL):
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )
        

class WaitForNtmsOperatorRequest(NDRCALL):
    opnum = 5
    structure = (
		('lpRequestId', LPNTMS_GUID),
		('dwTimeout', DWORD),
    )

class WaitForNtmsOperatorRequestResponse(NDRCALL):
    structure = (

    )
        

class CancelNtmsOperatorRequest(NDRCALL):
    opnum = 6
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )

class CancelNtmsOperatorRequestResponse(NDRCALL):
    structure = (

    )
        

class SatisfyNtmsOperatorRequest(NDRCALL):
    opnum = 7
    structure = (
		('lpRequestId', LPNTMS_GUID),
    )

class SatisfyNtmsOperatorRequestResponse(NDRCALL):
    structure = (

    )
        

class ImportNtmsDatabase(NDRCALL):
    opnum = 8
    structure = (

    )

class ImportNtmsDatabaseResponse(NDRCALL):
    structure = (

    )
        

class ExportNtmsDatabase(NDRCALL):
    opnum = 9
    structure = (

    )

class ExportNtmsDatabaseResponse(NDRCALL):
    structure = (

    )
        

class Opnum13NotUsedOnWire(NDRCALL):
    opnum = 10
    structure = (

    )

class Opnum13NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class AddNotification(NDRCALL):
    opnum = 11
    structure = (
		('dwType', DWORD),
    )

class AddNotificationResponse(NDRCALL):
    structure = (

    )
        

class RemoveNotification(NDRCALL):
    opnum = 12
    structure = (
		('dwType', DWORD),
    )

class RemoveNotificationResponse(NDRCALL):
    structure = (

    )
        

class DispatchNotification(NDRCALL):
    opnum = 13
    structure = (
		('dwType', DWORD),
		('dwOperation', DWORD),
		('lpIdentifier', LPNTMS_GUID),
    )

class DispatchNotificationResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OpenNtmsServerSessionW,OpenNtmsServerSessionWResponse),
1 : (OpenNtmsServerSessionA,OpenNtmsServerSessionAResponse),
2 : (CloseNtmsSession,CloseNtmsSessionResponse),
3 : (SubmitNtmsOperatorRequestW,SubmitNtmsOperatorRequestWResponse),
4 : (SubmitNtmsOperatorRequestA,SubmitNtmsOperatorRequestAResponse),
5 : (WaitForNtmsOperatorRequest,WaitForNtmsOperatorRequestResponse),
6 : (CancelNtmsOperatorRequest,CancelNtmsOperatorRequestResponse),
7 : (SatisfyNtmsOperatorRequest,SatisfyNtmsOperatorRequestResponse),
8 : (ImportNtmsDatabase,ImportNtmsDatabaseResponse),
9 : (ExportNtmsDatabase,ExportNtmsDatabaseResponse),
10 : (Opnum13NotUsedOnWire,Opnum13NotUsedOnWireResponse),
11 : (AddNotification,AddNotificationResponse),
12 : (RemoveNotification,RemoveNotificationResponse),
13 : (DispatchNotification,DispatchNotificationResponse),
}

#################################################################################

#IClientSink Definition

#################################################################################

MSRPC_UUID_ICLIENTSINK = uuidtup_to_bin(('879C8BBE-41B0-11d1-BE11-00C04FB6BF70','0.0'))


class OnNotify(NDRCALL):
    opnum = 0
    structure = (
		('dwType', DWORD),
		('dwOperation', DWORD),
		('lpIdentifier', LPNTMS_GUID),
    )

class OnNotifyResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (OnNotify,OnNotifyResponse),
}

#################################################################################

#INtmsLibraryControl2 Definition

#################################################################################

MSRPC_UUID_INTMSLIBRARYCONTROL2 = uuidtup_to_bin(('DB90832F-6910-446-95-9D6BFA73903','0.0'))


class IdentifyNtmsSlot(NDRCALL):
    opnum = 0
    structure = (
		('lpSlotId', LPNTMS_GUID),
		('dwOption', DWORD),
    )

class IdentifyNtmsSlotResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (IdentifyNtmsSlot,IdentifyNtmsSlotResponse),
}

#################################################################################

#INtmsObjectManagement2 Definition

#################################################################################

MSRPC_UUID_INTMSOBJECTMANAGEMENT2 = uuidtup_to_bin(('895A2C86-270D-489d-A6C0-DC2A9B35280E','0.0'))


class EnumerateNtmsObjectR(NDRCALL):
    opnum = 0
    structure = (
		('lpContainerId',  LPNTMS_GUID),
		('lpdwListBufferSize', DWORD),
		('dwType', DWORD),
		('dwOptions', DWORD),
    )

class EnumerateNtmsObjectRResponse(NDRCALL):
    structure = (
		('lpList', LPNTMS_GUID),
		('lpdwListSize', DWORD),
		('lpdwOutputSize', DWORD),
    )
        

class GetNtmsUIOptionsA(NDRCALL):
    opnum = 1
    structure = (
		('lpObjectId',  LPNTMS_GUID),
		('dwType', DWORD),
		('lpdwBufSize', DWORD),
    )

class GetNtmsUIOptionsAResponse(NDRCALL):
    structure = (
		('lpszDestination', UNSIGNED_CHAR),
		('lpdwDataSize', DWORD),
		('lpdwOutSize', DWORD),
    )
        

class GetNtmsUIOptionsW(NDRCALL):
    opnum = 2
    structure = (
		('lpObjectId',  LPNTMS_GUID),
		('dwType', DWORD),
		('lpdwBufSize', DWORD),
    )

class GetNtmsUIOptionsWResponse(NDRCALL):
    structure = (
		('lpszDestination', WCHAR_T),
		('lpdwDataSize', DWORD),
		('lpdwOutSize', DWORD),
    )
        

class SetNtmsUIOptionsA(NDRCALL):
    opnum = 3
    structure = (
		('lpObjectId',  LPNTMS_GUID),
		('dwType', DWORD),
		('dwOperation', DWORD),
		('lpszDestination', CONST_CHAR),
    )

class SetNtmsUIOptionsAResponse(NDRCALL):
    structure = (

    )
        

class SetNtmsUIOptionsW(NDRCALL):
    opnum = 4
    structure = (
		('lpObjectId',  LPNTMS_GUID),
		('dwType', DWORD),
		('dwOperation', DWORD),
		('lpszDestination', CONST_WCHAR_T),
    )

class SetNtmsUIOptionsWResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (EnumerateNtmsObjectR,EnumerateNtmsObjectRResponse),
1 : (GetNtmsUIOptionsA,GetNtmsUIOptionsAResponse),
2 : (GetNtmsUIOptionsW,GetNtmsUIOptionsWResponse),
3 : (SetNtmsUIOptionsA,SetNtmsUIOptionsAResponse),
4 : (SetNtmsUIOptionsW,SetNtmsUIOptionsWResponse),
}

#################################################################################

#INtmsObjectManagement3 Definition

#################################################################################

MSRPC_UUID_INTMSOBJECTMANAGEMENT3 = uuidtup_to_bin(('3BBED8D9-2C9A-4b21-8936-ACB2F995BE6C','0.0'))


class GetNtmsObjectAttributeAR(NDRCALL):
    opnum = 0
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_CHAR),
		('lpdwAttributeBufferSize', DWORD),
    )

class GetNtmsObjectAttributeARResponse(NDRCALL):
    structure = (
		('lpAttributeData', BYTE),
		('lpAttributeSize', DWORD),
		('lpActualAttributeSize', DWORD),
    )
        

class GetNtmsObjectAttributeWR(NDRCALL):
    opnum = 1
    structure = (
		('lpObjectId', LPNTMS_GUID),
		('dwType', DWORD),
		('lpAttributeName', CONST_WCHAR_T),
		('lpdwAttributeBufferSize', DWORD),
    )

class GetNtmsObjectAttributeWRResponse(NDRCALL):
    structure = (
		('lpAttributeData', BYTE),
		('lpAttributeSize', DWORD),
		('lpActualAttributeSize', DWORD),
    )
        
OPNUMS = {
0 : (GetNtmsObjectAttributeAR,GetNtmsObjectAttributeARResponse),
1 : (GetNtmsObjectAttributeWR,GetNtmsObjectAttributeWRResponse),
}

#################################################################################

#IRobustNtmsMediaServices1 Definition

#################################################################################

MSRPC_UUID_IROBUSTNTMSMEDIASERVICES1 = uuidtup_to_bin(('7D07F313-A53F-459a-BB12-012C15B1846E','0.0'))


class GetNtmsMediaPoolNameAR(NDRCALL):
    opnum = 0
    structure = (
		('lpPoolId', LPNTMS_GUID),
		('lpdwNameSizeBuf', DWORD),
    )

class GetNtmsMediaPoolNameARResponse(NDRCALL):
    structure = (
		('lpBufName', UNSIGNED_CHAR),
		('lpdwNameSize', DWORD),
		('lpdwOutputSize', DWORD),
    )
        

class GetNtmsMediaPoolNameWR(NDRCALL):
    opnum = 1
    structure = (
		('lpPoolId', LPNTMS_GUID),
		('lpdwNameSizeBuf', DWORD),
    )

class GetNtmsMediaPoolNameWRResponse(NDRCALL):
    structure = (
		('lpBufName', WCHAR_T),
		('lpdwNameSize', DWORD),
		('lpdwOutputSize', DWORD),
    )
        
OPNUMS = {
0 : (GetNtmsMediaPoolNameAR,GetNtmsMediaPoolNameARResponse),
1 : (GetNtmsMediaPoolNameWR,GetNtmsMediaPoolNameWRResponse),
}

#################################################################################

#IUnknown Definition

#################################################################################

MSRPC_UUID_IUNKNOWN = uuidtup_to_bin(('00000000-0000-0000-C000-000000000046','0.0'))

LPUNKNOWN = IUNKNOWN

class QueryInterface(NDRCALL):
    opnum = 0
    structure = (
		('riid', REFIID),
    )

class QueryInterfaceResponse(NDRCALL):
    structure = (
		('ppvObject', CONTEXT_HANDLE),
    )
        

class AddRef(NDRCALL):
    opnum = 1
    structure = (

    )

class AddRefResponse(NDRCALL):
    structure = (

    )
        

class Release(NDRCALL):
    opnum = 2
    structure = (

    )

class ReleaseResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (QueryInterface,QueryInterfaceResponse),
1 : (AddRef,AddRefResponse),
2 : (Release,ReleaseResponse),
}

#################################################################################

#IMessenger Definition

#################################################################################

MSRPC_UUID_IMESSENGER = uuidtup_to_bin(('081E7188-C080-4FF3-9238-29F66D6CABFD','0.0'))


class SendMessage(NDRCALL):
    opnum = 0
    structure = (
		('lpRsmMessage', LPRSM_MESSAGE),
    )

class SendMessageResponse(NDRCALL):
    structure = (

    )
        

class RecallMessage(NDRCALL):
    opnum = 1
    structure = (
		('lpGuid', LPGUID),
    )

class RecallMessageResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SendMessage,SendMessageResponse),
1 : (RecallMessage,RecallMessageResponse),
}

#################################################################################

#INtmsNotifySink Definition

#################################################################################

MSRPC_UUID_INTMSNOTIFYSINK = uuidtup_to_bin(('BB39332C-BFEE-4380-AD8A-BADC8AFF5BB6','0.0'))


class ConnectCallback(NDRCALL):
    opnum = 0
    structure = (
		('pUnkCP', IUNKNOWN),
		('pUnkSink', IUNKNOWN),
    )

class ConnectCallbackResponse(NDRCALL):
    structure = (

    )
        

class OnNotify(NDRCALL):
    opnum = 1
    structure = (
		('dwType', DWORD),
		('dwOperation', DWORD),
		('lpIdentifier', LPGUID),
    )

class OnNotifyResponse(NDRCALL):
    structure = (

    )
        

class ReleaseCallback(NDRCALL):
    opnum = 2
    structure = (

    )

class ReleaseCallbackResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (ConnectCallback,ConnectCallbackResponse),
1 : (OnNotify,OnNotifyResponse),
2 : (ReleaseCallback,ReleaseCallbackResponse),
}

