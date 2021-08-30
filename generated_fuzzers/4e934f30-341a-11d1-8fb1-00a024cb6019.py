from fuzzer.midl import *
from fuzzer.core import *


class FILETIME(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLowDateTime"),
        (DWORD, "dwHighDateTime"),
    ]


class GUID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_LONG, "Data1"),
        (UNSIGNED_SHORT, "Data2"),
        (UNSIGNED_SHORT, "Data3"),
        (BYTE, "Data4"),
    ]


class LARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (SIGNED___INT64, "QuadPart"),
    ]


class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (USHORT, "Id"),
        (UCHAR, "Version"),
        (UCHAR, "Channel"),
        (UCHAR, "Level"),
        (UCHAR, "Opcode"),
        (USHORT, "Task"),
        (ULONGLONG, "Keyword"),
    ]


class S0(NdrStructure):
    MEMBERS = [
        (ULONG, "KernelTime"),
        (ULONG, "UserTime"),
    ]


class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (S0, "s0"),
        2: (ULONG64, "ProcessorTime"),
    }


class EVENT_HEADER(NdrStructure):
    MEMBERS = [
        (USHORT, "Size"),
        (USHORT, "HeaderType"),
        (USHORT, "Flags"),
        (USHORT, "EventProperty"),
        (ULONG, "ThreadId"),
        (ULONG, "ProcessId"),
        (LARGE_INTEGER, "TimeStamp"),
        (GUID, "ProviderId"),
        (EVENT_DESCRIPTOR, "EventDescriptor"),
        (U0, "u0"),
        (GUID, "ActivityId"),
    ]


class LUID(NdrStructure):
    MEMBERS = [
        (DWORD, "LowPart"),
        (LONG, "HighPart"),
    ]


class MULTI_SZ(NdrStructure):
    MEMBERS = [
        (PWCHAR_T, "Value"),
        (DWORD, "nChar"),
    ]


class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [
        (UNSIGNED_SHORT, "Length"),
        (UNSIGNED_SHORT, "MaximumLength"),
        (PWCHAR, "Buffer"),
    ]


class SERVER_INFO_100(NdrStructure):
    MEMBERS = [
        (DWORD, "sv100_platform_id"),
        (PWCHAR_T, "sv100_name"),
    ]


class SERVER_INFO_101(NdrStructure):
    MEMBERS = [
        (DWORD, "sv101_platform_id"),
        (PWCHAR_T, "sv101_name"),
        (DWORD, "sv101_version_major"),
        (DWORD, "sv101_version_minor"),
        (DWORD, "sv101_version_type"),
        (PWCHAR_T, "sv101_comment"),
    ]


class SYSTEMTIME(NdrStructure):
    MEMBERS = [
        (WORD, "wYear"),
        (WORD, "wMonth"),
        (WORD, "wDayOfWeek"),
        (WORD, "wDay"),
        (WORD, "wHour"),
        (WORD, "wMinute"),
        (WORD, "wSecond"),
        (WORD, "wMilliseconds"),
    ]


class UINT128(NdrStructure):
    MEMBERS = [
        (UINT64, "lower"),
        (UINT64, "upper"),
    ]


class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [
        (UNSIGNED___INT64, "QuadPart"),
    ]


class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [
        (BYTE, "Value"),
    ]


class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [
        (WORD, "Level"),
        (ACCESS_MASK, "Remaining"),
        (PGUID, "ObjectType"),
    ]


class ACE_HEADER(NdrStructure):
    MEMBERS = [
        (UCHAR, "AceType"),
        (UCHAR, "AceFlags"),
        (USHORT, "AceSize"),
    ]


class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [
        (ACE_HEADER, "Header"),
        (ACCESS_MASK, "Mask"),
        (DWORD, "SidStart"),
    ]


class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [
        (DWORD, "Policy"),
    ]


class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [
        (ACCESS_MASK, "AllowedAccess"),
        (BOOLEAN, "WriteAllowed"),
        (BOOLEAN, "ReadAllowed"),
        (BOOLEAN, "ExecuteAllowed"),
        (TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),
    ]


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [
        (DWORD, "Length"),
        (BYTE, "OctetString"),
    ]


class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {
        1: (PLONG64, "pInt64"),
        2: (PDWORD64, "pUint64"),
        3: (PWSTR, "ppString"),
        4: (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),
    }


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [
        (DWORD, "Name"),
        (WORD, "ValueType"),
        (WORD, "Reserved"),
        (DWORD, "Flags"),
        (DWORD, "ValueCount"),
        (VALUES, "Values"),
    ]


class RPC_SID(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "Revision"),
        (UNSIGNED_CHAR, "SubAuthorityCount"),
        (RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),
        (UNSIGNED_LONG, "SubAuthority"),
    ]


class ACL(NdrStructure):
    MEMBERS = [
        (UNSIGNED_CHAR, "AclRevision"),
        (UNSIGNED_CHAR, "Sbz1"),
        (UNSIGNED_SHORT, "AclSize"),
        (UNSIGNED_SHORT, "AceCount"),
        (UNSIGNED_SHORT, "Sbz2"),
    ]


class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [
        (UCHAR, "Revision"),
        (UCHAR, "Sbz1"),
        (USHORT, "Control"),
        (PSID, "Owner"),
        (PSID, "Group"),
        (PACL, "Sacl"),
        (PACL, "Dacl"),
    ]


class NTMS_LIBRARYINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "LibraryType"),
        (NTMS_GUID, "CleanerSlot"),
        (NTMS_GUID, "CleanerSlotDefault"),
        (BOOL, "LibrarySupportsDriveCleaning"),
        (BOOL, "BarCodeReaderInstalled"),
        (DWORD, "InventoryMethod"),
        (DWORD, "dwCleanerUsesRemaining"),
        (DWORD, "FirstDriveNumber"),
        (DWORD, "dwNumberOfDrives"),
        (DWORD, "FirstSlotNumber"),
        (DWORD, "dwNumberOfSlots"),
        (DWORD, "FirstDoorNumber"),
        (DWORD, "dwNumberOfDoors"),
        (DWORD, "FirstPortNumber"),
        (DWORD, "dwNumberOfPorts"),
        (DWORD, "FirstChangerNumber"),
        (DWORD, "dwNumberOfChangers"),
        (DWORD, "dwNumberOfMedia"),
        (DWORD, "dwNumberOfMediaTypes"),
        (DWORD, "dwNumberOfLibRequests"),
        (GUID, "Reserved"),
        (BOOL, "AutoRecovery"),
        (DWORD, "dwFlags"),
    ]


class SECURITY_ATTRIBUTES_NTMS(NdrStructure):
    MEMBERS = [
        (DWORD, "nLength"),
        (PBYTE, "lpSecurityDescriptor"),
        (BOOL, "bInheritHandle"),
        (DWORD, "nDescriptorLength"),
    ]


class NTMS_ALLOCATION_INFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "dwSize"),
        (PBYTE, "lpReserved"),
        (NTMS_GUID, "AllocatedFrom"),
    ]


class NTMS_ASYNC_IO(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "OperationId"),
        (NTMS_GUID, "EventId"),
        (DWORD, "dwOperationType"),
        (DWORD, "dwResult"),
        (DWORD, "dwAsyncState"),
        (PVOID, "hEvent"),
        (BOOL, "bOnStateChange"),
    ]


class NTMS_MOUNT_INFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "dwSize"),
        (LPVOID, "lpReserved"),
    ]


class NTMS_CHANGERINFORMATIONA(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (NTMS_GUID, "ChangerType"),
        (CHAR, "szSerialNumber"),
        (CHAR, "szRevision"),
        (CHAR, "szDeviceName"),
        (UNSIGNED_SHORT, "ScsiPort"),
        (UNSIGNED_SHORT, "ScsiBus"),
        (UNSIGNED_SHORT, "ScsiTarget"),
        (UNSIGNED_SHORT, "ScsiLun"),
        (NTMS_GUID, "Library"),
    ]


class NTMS_CHANGERINFORMATIONW(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (NTMS_GUID, "ChangerType"),
        (WCHAR_T, "szSerialNumber"),
        (WCHAR_T, "szRevision"),
        (WCHAR_T, "szDeviceName"),
        (UNSIGNED_SHORT, "ScsiPort"),
        (UNSIGNED_SHORT, "ScsiBus"),
        (UNSIGNED_SHORT, "ScsiTarget"),
        (UNSIGNED_SHORT, "ScsiLun"),
        (NTMS_GUID, "Library"),
    ]


class NTMS_CHANGERTYPEINFORMATIONA(NdrStructure):
    MEMBERS = [
        (CHAR, "szVendor"),
        (CHAR, "szProduct"),
        (DWORD, "DeviceType"),
    ]


class NTMS_CHANGERTYPEINFORMATIONW(NdrStructure):
    MEMBERS = [
        (WCHAR_T, "szVendor"),
        (WCHAR_T, "szProduct"),
        (DWORD, "DeviceType"),
    ]


class NTMS_DRIVEINFORMATIONA(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (DWORD, "State"),
        (NTMS_GUID, "DriveType"),
        (CHAR, "szDeviceName"),
        (CHAR, "szSerialNumber"),
        (CHAR, "szRevision"),
        (UNSIGNED_SHORT, "ScsiPort"),
        (UNSIGNED_SHORT, "ScsiBus"),
        (UNSIGNED_SHORT, "ScsiTarget"),
        (UNSIGNED_SHORT, "ScsiLun"),
        (DWORD, "dwMountCount"),
        (SYSTEMTIME, "LastCleanedTs"),
        (NTMS_GUID, "SavedPartitionId"),
        (NTMS_GUID, "Library"),
        (GUID, "Reserved"),
        (DWORD, "dwDeferDismountDelay"),
    ]


class NTMS_DRIVEINFORMATIONW(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (DWORD, "State"),
        (NTMS_GUID, "DriveType"),
        (WCHAR_T, "szDeviceName"),
        (WCHAR_T, "szSerialNumber"),
        (WCHAR_T, "szRevision"),
        (UNSIGNED_SHORT, "ScsiPort"),
        (UNSIGNED_SHORT, "ScsiBus"),
        (UNSIGNED_SHORT, "ScsiTarget"),
        (UNSIGNED_SHORT, "ScsiLun"),
        (DWORD, "dwMountCount"),
        (SYSTEMTIME, "LastCleanedTs"),
        (NTMS_GUID, "SavedPartitionId"),
        (NTMS_GUID, "Library"),
        (GUID, "Reserved"),
        (DWORD, "dwDeferDismountDelay"),
    ]


class NTMS_DRIVETYPEINFORMATIONA(NdrStructure):
    MEMBERS = [
        (CHAR, "szVendor"),
        (CHAR, "szProduct"),
        (DWORD, "NumberOfHeads"),
        (DWORD, "DeviceType"),
    ]


class NTMS_DRIVETYPEINFORMATIONW(NdrStructure):
    MEMBERS = [
        (WCHAR_T, "szVendor"),
        (WCHAR_T, "szProduct"),
        (DWORD, "NumberOfHeads"),
        (DWORD, "DeviceType"),
    ]


class NTMS_LIBREQUESTINFORMATIONA(NdrStructure):
    MEMBERS = [
        (DWORD, "OperationCode"),
        (DWORD, "OperationOption"),
        (DWORD, "State"),
        (NTMS_GUID, "PartitionId"),
        (NTMS_GUID, "DriveId"),
        (NTMS_GUID, "PhysMediaId"),
        (NTMS_GUID, "Library"),
        (NTMS_GUID, "SlotId"),
        (SYSTEMTIME, "TimeQueued"),
        (SYSTEMTIME, "TimeCompleted"),
        (CHAR, "szApplication"),
        (CHAR, "szUser"),
        (CHAR, "szComputer"),
        (DWORD, "dwErrorCode"),
        (NTMS_GUID, "WorkItemId"),
        (DWORD, "dwPriority"),
    ]


class NTMS_LIBREQUESTINFORMATIONW(NdrStructure):
    MEMBERS = [
        (DWORD, "OperationCode"),
        (DWORD, "OperationOption"),
        (DWORD, "State"),
        (NTMS_GUID, "PartitionId"),
        (NTMS_GUID, "DriveId"),
        (NTMS_GUID, "PhysMediaId"),
        (NTMS_GUID, "Library"),
        (NTMS_GUID, "SlotId"),
        (SYSTEMTIME, "TimeQueued"),
        (SYSTEMTIME, "TimeCompleted"),
        (WCHAR_T, "szApplication"),
        (WCHAR_T, "szUser"),
        (WCHAR_T, "szComputer"),
        (DWORD, "dwErrorCode"),
        (NTMS_GUID, "WorkItemId"),
        (DWORD, "dwPriority"),
    ]


class NTMS_MEDIAPOOLINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "PoolType"),
        (NTMS_GUID, "MediaType"),
        (NTMS_GUID, "Parent"),
        (DWORD, "AllocationPolicy"),
        (DWORD, "DeallocationPolicy"),
        (DWORD, "dwMaxAllocates"),
        (DWORD, "dwNumberOfPhysicalMedia"),
        (DWORD, "dwNumberOfLogicalMedia"),
        (DWORD, "dwNumberOfMediaPools"),
    ]


class NTMS_MEDIATYPEINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "MediaType"),
        (DWORD, "NumberOfSides"),
        (DWORD, "ReadWriteCharacteristics"),
        (DWORD, "DeviceType"),
    ]


class NTMS_STORAGESLOTINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (DWORD, "State"),
        (NTMS_GUID, "Library"),
    ]


class NTMS_IEDOORINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (DWORD, "State"),
        (UNSIGNED_SHORT, "MaxOpenSecs"),
        (NTMS_GUID, "Library"),
    ]


class NTMS_IEPORTINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "Number"),
        (DWORD, "Content"),
        (DWORD, "Position"),
        (UNSIGNED_SHORT, "MaxExtendSecs"),
        (NTMS_GUID, "Library"),
    ]


class NTMS_LMIDINFORMATION(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "MediaPool"),
        (DWORD, "dwNumberOfPartitions"),
    ]


class NTMS_COMPUTERINFORMATION(NdrStructure):
    MEMBERS = [
        (DWORD, "dwLibRequestPurgeTime"),
        (DWORD, "dwOpRequestPurgeTime"),
        (DWORD, "dwLibRequestFlags"),
        (DWORD, "dwOpRequestFlags"),
        (DWORD, "dwMediaPoolPolicy"),
    ]


class NTMS_OPREQUESTINFORMATIONA(NdrStructure):
    MEMBERS = [
        (DWORD, "Request"),
        (SYSTEMTIME, "Submitted"),
        (DWORD, "State"),
        (CHAR, "szMessage"),
        (DWORD, "Arg1Type"),
        (NTMS_GUID, "Arg1"),
        (DWORD, "Arg2Type"),
        (NTMS_GUID, "Arg2"),
        (CHAR, "szApplication"),
        (CHAR, "szUser"),
        (CHAR, "szComputer"),
    ]


class NTMS_OPREQUESTINFORMATIONW(NdrStructure):
    MEMBERS = [
        (DWORD, "Request"),
        (SYSTEMTIME, "Submitted"),
        (DWORD, "State"),
        (WCHAR_T, "szMessage"),
        (DWORD, "Arg1Type"),
        (NTMS_GUID, "Arg1"),
        (DWORD, "Arg2Type"),
        (NTMS_GUID, "Arg2"),
        (WCHAR_T, "szApplication"),
        (WCHAR_T, "szUser"),
        (WCHAR_T, "szComputer"),
    ]


class NTMS_PARTITIONINFORMATIONA(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "PhysicalMedia"),
        (NTMS_GUID, "LogicalMedia"),
        (DWORD, "State"),
        (UNSIGNED_SHORT, "Side"),
        (DWORD, "dwOmidLabelIdLength"),
        (BYTE, "OmidLabelId"),
        (CHAR, "szOmidLabelType"),
        (CHAR, "szOmidLabelInfo"),
        (DWORD, "dwMountCount"),
        (DWORD, "dwAllocateCount"),
        (LARGE_INTEGER, "Capacity"),
    ]


class NTMS_PARTITIONINFORMATIONW(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "PhysicalMedia"),
        (NTMS_GUID, "LogicalMedia"),
        (DWORD, "State"),
        (UNSIGNED_SHORT, "Side"),
        (DWORD, "dwOmidLabelIdLength"),
        (BYTE, "OmidLabelId"),
        (WCHAR_T, "szOmidLabelType"),
        (WCHAR_T, "szOmidLabelInfo"),
        (DWORD, "dwMountCount"),
        (DWORD, "dwAllocateCount"),
        (LARGE_INTEGER, "Capacity"),
    ]


class NTMS_PMIDINFORMATIONA(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "CurrentLibrary"),
        (NTMS_GUID, "MediaPool"),
        (NTMS_GUID, "Location"),
        (DWORD, "LocationType"),
        (NTMS_GUID, "MediaType"),
        (NTMS_GUID, "HomeSlot"),
        (CHAR, "szBarCode"),
        (DWORD, "BarCodeState"),
        (CHAR, "szSequenceNumber"),
        (DWORD, "MediaState"),
        (DWORD, "dwNumberOfPartitions"),
        (DWORD, "dwMediaTypeCode"),
        (DWORD, "dwDensityCode"),
        (NTMS_GUID, "MountedPartition"),
    ]


class NTMS_PMIDINFORMATIONW(NdrStructure):
    MEMBERS = [
        (NTMS_GUID, "CurrentLibrary"),
        (NTMS_GUID, "MediaPool"),
        (NTMS_GUID, "Location"),
        (DWORD, "LocationType"),
        (NTMS_GUID, "MediaType"),
        (NTMS_GUID, "HomeSlot"),
        (WCHAR_T, "szBarCode"),
        (DWORD, "BarCodeState"),
        (WCHAR_T, "szSequenceNumber"),
        (DWORD, "MediaState"),
        (DWORD, "dwNumberOfPartitions"),
        (DWORD, "dwMediaTypeCode"),
        (DWORD, "dwDensityCode"),
        (NTMS_GUID, "MountedPartition"),
    ]


class RSM_MESSAGE(NdrStructure):
    MEMBERS = [
        (LPGUID, "lpguidOperation"),
        (DWORD, "dwNtmsType"),
        (DWORD, "dwState"),
        (DWORD, "dwFlags"),
        (DWORD, "dwPriority"),
        (DWORD, "dwErrorCode"),
        (PWCHAR_T, "lpszComputerName"),
        (PWCHAR_T, "lpszApplication"),
        (PWCHAR_T, "lpszUser"),
        (PWCHAR_T, "lpszTimeSubmitted"),
        (PWCHAR_T, "lpszMessage"),
    ]


class NTMS_OBJECTINFORMATIONA(NdrStructure):
    MEMBERS = [
        (DWORD, "dwSize"),
        (DWORD, "dwType"),
        (SYSTEMTIME, "Created"),
        (SYSTEMTIME, "Modified"),
        (NTMS_GUID, "ObjectGuid"),
        (BOOL, "Enabled"),
        (DWORD, "dwOperationalState"),
        (CHAR, "szName"),
        (CHAR, "szDescription"),
        (INFO, "Info"),
    ]


class NTMS_OBJECTINFORMATIONW(NdrStructure):
    MEMBERS = [
        (DWORD, "dwSize"),
        (DWORD, "dwType"),
        (SYSTEMTIME, "Created"),
        (SYSTEMTIME, "Modified"),
        (NTMS_GUID, "ObjectGuid"),
        (BOOL, "Enabled"),
        (DWORD, "dwOperationalState"),
        (WCHAR_T, "szName"),
        (WCHAR_T, "szDescription"),
        (INFO, "Info"),
    ]


Method("EjectNtmsMedia", In(LPNTMS_GUID), InOut(LPNTMS_GUID), In(DWORD),), Method(
    "InjectNtmsMedia",
    In(LPNTMS_GUID),
    InOut(LPNTMS_GUID),
    In(DWORD),
), Method("AccessNtmsLibraryDoor", In(LPNTMS_GUID), In(DWORD),), Method(
    "CleanNtmsDrive",
    In(LPNTMS_GUID),
), Method(
    "DismountNtmsDrive",
    In(LPNTMS_GUID),
), Method(
    "InventoryNtmsLibrary",
    In(LPNTMS_GUID),
    In(DWORD),
), Method(
    "INtmsLibraryControl1_LocalOnlyOpnum09",
), Method(
    "CancelNtmsLibraryRequest",
    In(LPNTMS_GUID),
), Method(
    "ReserveNtmsCleanerSlot",
    In(LPNTMS_GUID),
    In(LPNTMS_GUID),
), Method(
    "ReleaseNtmsCleanerSlot",
    In(LPNTMS_GUID),
), Method(
    "InjectNtmsCleaner",
    In(LPNTMS_GUID),
    InOut(LPNTMS_GUID),
    In(DWORD),
    In(DWORD),
), Method(
    "EjectNtmsCleaner",
    In(LPNTMS_GUID),
    InOut(LPNTMS_GUID),
    In(DWORD),
), Method(
    "DeleteNtmsLibrary",
    In(LPNTMS_GUID),
), Method(
    "DeleteNtmsDrive",
    In(LPNTMS_GUID),
), Method(
    "GetNtmsRequestOrder",
    In(LPNTMS_GUID),
    Out(PDWORD),
), Method(
    "SetNtmsRequestOrder",
    In(LPNTMS_GUID),
    In(DWORD),
), Method(
    "DeleteNtmsRequests",
    In(LPNTMS_GUID),
    In(DWORD),
    In(DWORD),
), Method(
    "BeginNtmsDeviceChangeDetection",
    Out(PNTMS_HANDLE),
), Method(
    "SetNtmsDeviceChangeDetection",
    In(NTMS_HANDLE),
    In(LPNTMS_GUID),
    In(DWORD),
    In(DWORD),
), Method(
    "EndNtmsDeviceChangeDetection",
    In(NTMS_HANDLE),
),
