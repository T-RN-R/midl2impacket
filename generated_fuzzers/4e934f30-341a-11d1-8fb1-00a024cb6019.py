
from fuzzer.midl import *
from fuzzer.core import *

class ('FILETIME', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLowDateTime"),(('DWORD', None), "dwHighDateTime"),]

    

class ('GUID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_LONG', None), "Data1"),(('UNSIGNED_SHORT', None), "Data2"),(('UNSIGNED_SHORT', None), "Data3"),(('BYTE', None), "Data4"),]

    

class ('LARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('SIGNED___INT64', None), "QuadPart"),]

    

class ('EVENT_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Id"),(('UCHAR', None), "Version"),(('UCHAR', None), "Channel"),(('UCHAR', None), "Level"),(('UCHAR', None), "Opcode"),(('USHORT', None), "Task"),(('ULONGLONG', None), "Keyword"),]

    

class ('S0', None)(NdrStructure):
    MEMBERS = [(('ULONG', None), "KernelTime"),(('ULONG', None), "UserTime"),]

    

class ('U0', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('S0', None), s0),2 : (('ULONG64', None), ProcessorTime),}

    

class ('EVENT_HEADER', None)(NdrStructure):
    MEMBERS = [(('USHORT', None), "Size"),(('USHORT', None), "HeaderType"),(('USHORT', None), "Flags"),(('USHORT', None), "EventProperty"),(('ULONG', None), "ThreadId"),(('ULONG', None), "ProcessId"),(('LARGE_INTEGER', None), "TimeStamp"),(('GUID', None), "ProviderId"),(('EVENT_DESCRIPTOR', None), "EventDescriptor"),(('U0', None), "u0"),(('GUID', None), "ActivityId"),]

    

class ('LUID', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "LowPart"),(('LONG', None), "HighPart"),]

    

class ('MULTI_SZ', None)(NdrStructure):
    MEMBERS = [(('PWCHAR_T', None), "Value"),(('DWORD', None), "nChar"),]

    

class ('RPC_UNICODE_STRING', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_SHORT', None), "Length"),(('UNSIGNED_SHORT', None), "MaximumLength"),(('PWCHAR', None), "Buffer"),]

    

class ('SERVER_INFO_100', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv100_platform_id"),(('PWCHAR_T', None), "sv100_name"),]

    

class ('SERVER_INFO_101', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "sv101_platform_id"),(('PWCHAR_T', None), "sv101_name"),(('DWORD', None), "sv101_version_major"),(('DWORD', None), "sv101_version_minor"),(('DWORD', None), "sv101_version_type"),(('PWCHAR_T', None), "sv101_comment"),]

    

class ('SYSTEMTIME', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "wYear"),(('WORD', None), "wMonth"),(('WORD', None), "wDayOfWeek"),(('WORD', None), "wDay"),(('WORD', None), "wHour"),(('WORD', None), "wMinute"),(('WORD', None), "wSecond"),(('WORD', None), "wMilliseconds"),]

    

class ('UINT128', None)(NdrStructure):
    MEMBERS = [(('UINT64', None), "lower"),(('UINT64', None), "upper"),]

    

class ('ULARGE_INTEGER', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT64', None), "QuadPart"),]

    

class ('RPC_SID_IDENTIFIER_AUTHORITY', None)(NdrStructure):
    MEMBERS = [(('BYTE', None), "Value"),]

    

class ('OBJECT_TYPE_LIST', None)(NdrStructure):
    MEMBERS = [(('WORD', None), "Level"),(('ACCESS_MASK', None), "Remaining"),(('PGUID', None), "ObjectType"),]

    

class ('ACE_HEADER', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "AceType"),(('UCHAR', None), "AceFlags"),(('USHORT', None), "AceSize"),]

    

class ('SYSTEM_MANDATORY_LABEL_ACE', None)(NdrStructure):
    MEMBERS = [(('ACE_HEADER', None), "Header"),(('ACCESS_MASK', None), "Mask"),(('DWORD', None), "SidStart"),]

    

class ('TOKEN_MANDATORY_POLICY', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Policy"),]

    

class ('MANDATORY_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('ACCESS_MASK', None), "AllowedAccess"),(('BOOLEAN', None), "WriteAllowed"),(('BOOLEAN', None), "ReadAllowed"),(('BOOLEAN', None), "ExecuteAllowed"),(('TOKEN_MANDATORY_POLICY', None), "MandatoryPolicy"),]

    

class ('CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Length"),(('BYTE', None), "OctetString"),]

    

class ('VALUES', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PLONG64', None), pInt64),2 : (('PDWORD64', None), pUint64),3 : (('PWSTR', None), ppString),4 : (('PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE', None), pOctetString),}

    

class ('CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Name"),(('WORD', None), "ValueType"),(('WORD', None), "Reserved"),(('DWORD', None), "Flags"),(('DWORD', None), "ValueCount"),(('VALUES', None), "Values"),]

    

class ('RPC_SID', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "Revision"),(('UNSIGNED_CHAR', None), "SubAuthorityCount"),(('RPC_SID_IDENTIFIER_AUTHORITY', None), "IdentifierAuthority"),(('UNSIGNED_LONG', None), "SubAuthority"),]

    

class ('ACL', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED_CHAR', None), "AclRevision"),(('UNSIGNED_CHAR', None), "Sbz1"),(('UNSIGNED_SHORT', None), "AclSize"),(('UNSIGNED_SHORT', None), "AceCount"),(('UNSIGNED_SHORT', None), "Sbz2"),]

    

class ('SECURITY_DESCRIPTOR', None)(NdrStructure):
    MEMBERS = [(('UCHAR', None), "Revision"),(('UCHAR', None), "Sbz1"),(('USHORT', None), "Control"),(('PSID', None), "Owner"),(('PSID', None), "Group"),(('PACL', None), "Sacl"),(('PACL', None), "Dacl"),]

    

class ('NTMS_LIBRARYINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "LibraryType"),(('NTMS_GUID', None), "CleanerSlot"),(('NTMS_GUID', None), "CleanerSlotDefault"),(('BOOL', None), "LibrarySupportsDriveCleaning"),(('BOOL', None), "BarCodeReaderInstalled"),(('DWORD', None), "InventoryMethod"),(('DWORD', None), "dwCleanerUsesRemaining"),(('DWORD', None), "FirstDriveNumber"),(('DWORD', None), "dwNumberOfDrives"),(('DWORD', None), "FirstSlotNumber"),(('DWORD', None), "dwNumberOfSlots"),(('DWORD', None), "FirstDoorNumber"),(('DWORD', None), "dwNumberOfDoors"),(('DWORD', None), "FirstPortNumber"),(('DWORD', None), "dwNumberOfPorts"),(('DWORD', None), "FirstChangerNumber"),(('DWORD', None), "dwNumberOfChangers"),(('DWORD', None), "dwNumberOfMedia"),(('DWORD', None), "dwNumberOfMediaTypes"),(('DWORD', None), "dwNumberOfLibRequests"),(('GUID', None), "Reserved"),(('BOOL', None), "AutoRecovery"),(('DWORD', None), "dwFlags"),]

    

class ('SECURITY_ATTRIBUTES_NTMS', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "nLength"),(('PBYTE', None), "lpSecurityDescriptor"),(('BOOL', None), "bInheritHandle"),(('DWORD', None), "nDescriptorLength"),]

    

class ('NTMS_ALLOCATION_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('PBYTE', None), "lpReserved"),(('NTMS_GUID', None), "AllocatedFrom"),]

    

class ('NTMS_ASYNC_IO', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "OperationId"),(('NTMS_GUID', None), "EventId"),(('DWORD', None), "dwOperationType"),(('DWORD', None), "dwResult"),(('DWORD', None), "dwAsyncState"),(('PVOID', None), "hEvent"),(('BOOL', None), "bOnStateChange"),]

    

class ('NTMS_MOUNT_INFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('LPVOID', None), "lpReserved"),]

    

class ('NTMS_CHANGERINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('NTMS_GUID', None), "ChangerType"),(('CHAR', None), "szSerialNumber"),(('CHAR', None), "szRevision"),(('CHAR', None), "szDeviceName"),(('UNSIGNED_SHORT', None), "ScsiPort"),(('UNSIGNED_SHORT', None), "ScsiBus"),(('UNSIGNED_SHORT', None), "ScsiTarget"),(('UNSIGNED_SHORT', None), "ScsiLun"),(('NTMS_GUID', None), "Library"),]

    

class ('NTMS_CHANGERINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('NTMS_GUID', None), "ChangerType"),(('WCHAR_T', None), "szSerialNumber"),(('WCHAR_T', None), "szRevision"),(('WCHAR_T', None), "szDeviceName"),(('UNSIGNED_SHORT', None), "ScsiPort"),(('UNSIGNED_SHORT', None), "ScsiBus"),(('UNSIGNED_SHORT', None), "ScsiTarget"),(('UNSIGNED_SHORT', None), "ScsiLun"),(('NTMS_GUID', None), "Library"),]

    

class ('NTMS_CHANGERTYPEINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('CHAR', None), "szVendor"),(('CHAR', None), "szProduct"),(('DWORD', None), "DeviceType"),]

    

class ('NTMS_CHANGERTYPEINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('WCHAR_T', None), "szVendor"),(('WCHAR_T', None), "szProduct"),(('DWORD', None), "DeviceType"),]

    

class ('NTMS_DRIVEINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('DWORD', None), "State"),(('NTMS_GUID', None), "DriveType"),(('CHAR', None), "szDeviceName"),(('CHAR', None), "szSerialNumber"),(('CHAR', None), "szRevision"),(('UNSIGNED_SHORT', None), "ScsiPort"),(('UNSIGNED_SHORT', None), "ScsiBus"),(('UNSIGNED_SHORT', None), "ScsiTarget"),(('UNSIGNED_SHORT', None), "ScsiLun"),(('DWORD', None), "dwMountCount"),(('SYSTEMTIME', None), "LastCleanedTs"),(('NTMS_GUID', None), "SavedPartitionId"),(('NTMS_GUID', None), "Library"),(('GUID', None), "Reserved"),(('DWORD', None), "dwDeferDismountDelay"),]

    

class ('NTMS_DRIVEINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('DWORD', None), "State"),(('NTMS_GUID', None), "DriveType"),(('WCHAR_T', None), "szDeviceName"),(('WCHAR_T', None), "szSerialNumber"),(('WCHAR_T', None), "szRevision"),(('UNSIGNED_SHORT', None), "ScsiPort"),(('UNSIGNED_SHORT', None), "ScsiBus"),(('UNSIGNED_SHORT', None), "ScsiTarget"),(('UNSIGNED_SHORT', None), "ScsiLun"),(('DWORD', None), "dwMountCount"),(('SYSTEMTIME', None), "LastCleanedTs"),(('NTMS_GUID', None), "SavedPartitionId"),(('NTMS_GUID', None), "Library"),(('GUID', None), "Reserved"),(('DWORD', None), "dwDeferDismountDelay"),]

    

class ('NTMS_DRIVETYPEINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('CHAR', None), "szVendor"),(('CHAR', None), "szProduct"),(('DWORD', None), "NumberOfHeads"),(('DWORD', None), "DeviceType"),]

    

class ('NTMS_DRIVETYPEINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('WCHAR_T', None), "szVendor"),(('WCHAR_T', None), "szProduct"),(('DWORD', None), "NumberOfHeads"),(('DWORD', None), "DeviceType"),]

    

class ('NTMS_LIBREQUESTINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "OperationCode"),(('DWORD', None), "OperationOption"),(('DWORD', None), "State"),(('NTMS_GUID', None), "PartitionId"),(('NTMS_GUID', None), "DriveId"),(('NTMS_GUID', None), "PhysMediaId"),(('NTMS_GUID', None), "Library"),(('NTMS_GUID', None), "SlotId"),(('SYSTEMTIME', None), "TimeQueued"),(('SYSTEMTIME', None), "TimeCompleted"),(('CHAR', None), "szApplication"),(('CHAR', None), "szUser"),(('CHAR', None), "szComputer"),(('DWORD', None), "dwErrorCode"),(('NTMS_GUID', None), "WorkItemId"),(('DWORD', None), "dwPriority"),]

    

class ('NTMS_LIBREQUESTINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "OperationCode"),(('DWORD', None), "OperationOption"),(('DWORD', None), "State"),(('NTMS_GUID', None), "PartitionId"),(('NTMS_GUID', None), "DriveId"),(('NTMS_GUID', None), "PhysMediaId"),(('NTMS_GUID', None), "Library"),(('NTMS_GUID', None), "SlotId"),(('SYSTEMTIME', None), "TimeQueued"),(('SYSTEMTIME', None), "TimeCompleted"),(('WCHAR_T', None), "szApplication"),(('WCHAR_T', None), "szUser"),(('WCHAR_T', None), "szComputer"),(('DWORD', None), "dwErrorCode"),(('NTMS_GUID', None), "WorkItemId"),(('DWORD', None), "dwPriority"),]

    

class ('NTMS_MEDIAPOOLINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "PoolType"),(('NTMS_GUID', None), "MediaType"),(('NTMS_GUID', None), "Parent"),(('DWORD', None), "AllocationPolicy"),(('DWORD', None), "DeallocationPolicy"),(('DWORD', None), "dwMaxAllocates"),(('DWORD', None), "dwNumberOfPhysicalMedia"),(('DWORD', None), "dwNumberOfLogicalMedia"),(('DWORD', None), "dwNumberOfMediaPools"),]

    

class ('NTMS_MEDIATYPEINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "MediaType"),(('DWORD', None), "NumberOfSides"),(('DWORD', None), "ReadWriteCharacteristics"),(('DWORD', None), "DeviceType"),]

    

class ('NTMS_STORAGESLOTINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('DWORD', None), "State"),(('NTMS_GUID', None), "Library"),]

    

class ('NTMS_IEDOORINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('DWORD', None), "State"),(('UNSIGNED_SHORT', None), "MaxOpenSecs"),(('NTMS_GUID', None), "Library"),]

    

class ('NTMS_IEPORTINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Number"),(('DWORD', None), "Content"),(('DWORD', None), "Position"),(('UNSIGNED_SHORT', None), "MaxExtendSecs"),(('NTMS_GUID', None), "Library"),]

    

class ('NTMS_LMIDINFORMATION', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "MediaPool"),(('DWORD', None), "dwNumberOfPartitions"),]

    

class ('NTMS_COMPUTERINFORMATION', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwLibRequestPurgeTime"),(('DWORD', None), "dwOpRequestPurgeTime"),(('DWORD', None), "dwLibRequestFlags"),(('DWORD', None), "dwOpRequestFlags"),(('DWORD', None), "dwMediaPoolPolicy"),]

    

class ('NTMS_OPREQUESTINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Request"),(('SYSTEMTIME', None), "Submitted"),(('DWORD', None), "State"),(('CHAR', None), "szMessage"),(('DWORD', None), "Arg1Type"),(('NTMS_GUID', None), "Arg1"),(('DWORD', None), "Arg2Type"),(('NTMS_GUID', None), "Arg2"),(('CHAR', None), "szApplication"),(('CHAR', None), "szUser"),(('CHAR', None), "szComputer"),]

    

class ('NTMS_OPREQUESTINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "Request"),(('SYSTEMTIME', None), "Submitted"),(('DWORD', None), "State"),(('WCHAR_T', None), "szMessage"),(('DWORD', None), "Arg1Type"),(('NTMS_GUID', None), "Arg1"),(('DWORD', None), "Arg2Type"),(('NTMS_GUID', None), "Arg2"),(('WCHAR_T', None), "szApplication"),(('WCHAR_T', None), "szUser"),(('WCHAR_T', None), "szComputer"),]

    

class ('NTMS_PARTITIONINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "PhysicalMedia"),(('NTMS_GUID', None), "LogicalMedia"),(('DWORD', None), "State"),(('UNSIGNED_SHORT', None), "Side"),(('DWORD', None), "dwOmidLabelIdLength"),(('BYTE', None), "OmidLabelId"),(('CHAR', None), "szOmidLabelType"),(('CHAR', None), "szOmidLabelInfo"),(('DWORD', None), "dwMountCount"),(('DWORD', None), "dwAllocateCount"),(('LARGE_INTEGER', None), "Capacity"),]

    

class ('NTMS_PARTITIONINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "PhysicalMedia"),(('NTMS_GUID', None), "LogicalMedia"),(('DWORD', None), "State"),(('UNSIGNED_SHORT', None), "Side"),(('DWORD', None), "dwOmidLabelIdLength"),(('BYTE', None), "OmidLabelId"),(('WCHAR_T', None), "szOmidLabelType"),(('WCHAR_T', None), "szOmidLabelInfo"),(('DWORD', None), "dwMountCount"),(('DWORD', None), "dwAllocateCount"),(('LARGE_INTEGER', None), "Capacity"),]

    

class ('NTMS_PMIDINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "CurrentLibrary"),(('NTMS_GUID', None), "MediaPool"),(('NTMS_GUID', None), "Location"),(('DWORD', None), "LocationType"),(('NTMS_GUID', None), "MediaType"),(('NTMS_GUID', None), "HomeSlot"),(('CHAR', None), "szBarCode"),(('DWORD', None), "BarCodeState"),(('CHAR', None), "szSequenceNumber"),(('DWORD', None), "MediaState"),(('DWORD', None), "dwNumberOfPartitions"),(('DWORD', None), "dwMediaTypeCode"),(('DWORD', None), "dwDensityCode"),(('NTMS_GUID', None), "MountedPartition"),]

    

class ('NTMS_PMIDINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('NTMS_GUID', None), "CurrentLibrary"),(('NTMS_GUID', None), "MediaPool"),(('NTMS_GUID', None), "Location"),(('DWORD', None), "LocationType"),(('NTMS_GUID', None), "MediaType"),(('NTMS_GUID', None), "HomeSlot"),(('WCHAR_T', None), "szBarCode"),(('DWORD', None), "BarCodeState"),(('WCHAR_T', None), "szSequenceNumber"),(('DWORD', None), "MediaState"),(('DWORD', None), "dwNumberOfPartitions"),(('DWORD', None), "dwMediaTypeCode"),(('DWORD', None), "dwDensityCode"),(('NTMS_GUID', None), "MountedPartition"),]

    

class ('RSM_MESSAGE', None)(NdrStructure):
    MEMBERS = [(('LPGUID', None), "lpguidOperation"),(('DWORD', None), "dwNtmsType"),(('DWORD', None), "dwState"),(('DWORD', None), "dwFlags"),(('DWORD', None), "dwPriority"),(('DWORD', None), "dwErrorCode"),(('PWCHAR_T', None), "lpszComputerName"),(('PWCHAR_T', None), "lpszApplication"),(('PWCHAR_T', None), "lpszUser"),(('PWCHAR_T', None), "lpszTimeSubmitted"),(('PWCHAR_T', None), "lpszMessage"),]

    

class ('NTMS_OBJECTINFORMATIONA', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('DWORD', None), "dwType"),(('SYSTEMTIME', None), "Created"),(('SYSTEMTIME', None), "Modified"),(('NTMS_GUID', None), "ObjectGuid"),(('BOOL', None), "Enabled"),(('DWORD', None), "dwOperationalState"),(('CHAR', None), "szName"),(('CHAR', None), "szDescription"),(('INFO', None), "Info"),]

    

class ('NTMS_OBJECTINFORMATIONW', None)(NdrStructure):
    MEMBERS = [(('DWORD', None), "dwSize"),(('DWORD', None), "dwType"),(('SYSTEMTIME', None), "Created"),(('SYSTEMTIME', None), "Modified"),(('NTMS_GUID', None), "ObjectGuid"),(('BOOL', None), "Enabled"),(('DWORD', None), "dwOperationalState"),(('WCHAR_T', None), "szName"),(('WCHAR_T', None), "szDescription"),(('INFO', None), "Info"),]

    
Method("EjectNtmsMedia",
In(LPNTMS_GUID),
InOut(LPNTMS_GUID),
In(DWORD),
),Method("InjectNtmsMedia",
In(LPNTMS_GUID),
InOut(LPNTMS_GUID),
In(DWORD),
),Method("AccessNtmsLibraryDoor",
In(LPNTMS_GUID),
In(DWORD),
),Method("CleanNtmsDrive",
In(LPNTMS_GUID),
),Method("DismountNtmsDrive",
In(LPNTMS_GUID),
),Method("InventoryNtmsLibrary",
In(LPNTMS_GUID),
In(DWORD),
),Method("INtmsLibraryControl1_LocalOnlyOpnum09",
),Method("CancelNtmsLibraryRequest",
In(LPNTMS_GUID),
),Method("ReserveNtmsCleanerSlot",
In(LPNTMS_GUID),
In(LPNTMS_GUID),
),Method("ReleaseNtmsCleanerSlot",
In(LPNTMS_GUID),
),Method("InjectNtmsCleaner",
In(LPNTMS_GUID),
InOut(LPNTMS_GUID),
In(DWORD),
In(DWORD),
),Method("EjectNtmsCleaner",
In(LPNTMS_GUID),
InOut(LPNTMS_GUID),
In(DWORD),
),Method("DeleteNtmsLibrary",
In(LPNTMS_GUID),
),Method("DeleteNtmsDrive",
In(LPNTMS_GUID),
),Method("GetNtmsRequestOrder",
In(LPNTMS_GUID),
Out(PDWORD),
),Method("SetNtmsRequestOrder",
In(LPNTMS_GUID),
In(DWORD),
),Method("DeleteNtmsRequests",
In(LPNTMS_GUID),
In(DWORD),
In(DWORD),
),Method("BeginNtmsDeviceChangeDetection",
Out(PNTMS_HANDLE),
),Method("SetNtmsDeviceChangeDetection",
In(NTMS_HANDLE),
In(LPNTMS_GUID),
In(DWORD),
In(DWORD),
),Method("EndNtmsDeviceChangeDetection",
In(NTMS_HANDLE),
),