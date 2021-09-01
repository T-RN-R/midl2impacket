
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

class W32TIME_NTP_PEER_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulResolveAttempts"),(UNSIGNED___INT64, "u64TimeRemaining"),(UNSIGNED___INT64, "u64LastSuccessfulSync"),(UNSIGNED___INT32, "ulLastSyncError"),(UNSIGNED___INT32, "ulLastSyncErrorMsgId"),(UNSIGNED___INT32, "ulValidDataCounter"),(UNSIGNED___INT32, "ulAuthTypeMsgId"),(PWCHAR_T, "wszUniqueName"),(UNSIGNED_CHAR, "ulMode"),(UNSIGNED_CHAR, "ulStratum"),(UNSIGNED_CHAR, "ulReachability"),(UNSIGNED_CHAR, "ulPeerPollInterval"),(UNSIGNED_CHAR, "ulHostPollInterval"),]

    
PW32TIME_NTP_PEER_INFO = W32TIME_NTP_PEER_INFO

class W32TIME_NTP_PROVIDER_DATA(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulError"),(UNSIGNED___INT32, "ulErrorMsgId"),(UNSIGNED___INT32, "cPeerInfo"),(PW32TIME_NTP_PEER_INFO, "pPeerInfo"),]

    
PW32TIME_NTP_PROVIDER_DATA = W32TIME_NTP_PROVIDER_DATA

class W32TIME_HARDWARE_PROVIDER_DATA(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulError"),(UNSIGNED___INT32, "ulErrorMsgId"),(PWCHAR_T, "wszReferenceIdentifier"),]

    
PW32TIME_HARDWARE_PROVIDER_DATA = W32TIME_HARDWARE_PROVIDER_DATA

class W32TIME_PROVIDER_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PW32TIME_NTP_PROVIDER_DATA, "pNtpProviderData"),2 : (PW32TIME_HARDWARE_PROVIDER_DATA, "pHardwareProviderData"),}

    

class W32TIME_PROVIDER_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulProviderType"),(W32TIME_PROVIDER_DATA, "ProviderData"),]

    
PW32TIME_PROVIDER_INFO = W32TIME_PROVIDER_INFO

class W32TIME_ENTRY(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(PWCHAR_T, "wszName"),(PWCHAR_T, "wszValue"),(PWCHAR_T, "wszHelp"),]

    
PW32TIME_ENTRY = W32TIME_ENTRY

class W32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulAllowNonstandardModeCombinations"),(UNSIGNED___INT32, "ulCrossSiteSyncFlags"),(UNSIGNED___INT32, "ulResolvePeerBackoffMinutes"),(UNSIGNED___INT32, "ulResolvePeerBackoffMaxTimes"),(UNSIGNED___INT32, "ulCompatibilityFlags"),(UNSIGNED___INT32, "ulEventLogFlags"),(UNSIGNED___INT32, "ulLargeSampleSkew"),(UNSIGNED___INT32, "ulSpecialPollInterval"),(PWCHAR_T, "wszType"),(PWCHAR_T, "wszNtpServer"),(UNSIGNED___INT32, "ulAllowNonstandardModeCombinationsFlag"),(UNSIGNED___INT32, "ulCrossSiteSyncFlagsFlag"),(UNSIGNED___INT32, "ulResolvePeerBackoffMinutesFlag"),(UNSIGNED___INT32, "ulResolvePeerBackoffMaxTimesFlag"),(UNSIGNED___INT32, "ulCompatibilityFlagsFlag"),(UNSIGNED___INT32, "ulEventLogFlagsFlag"),(UNSIGNED___INT32, "ulLargeSampleSkewFlag"),(UNSIGNED___INT32, "ulSpecialPollIntervalFlag"),(UNSIGNED___INT32, "ulTypeFlag"),(UNSIGNED___INT32, "ulNtpServerFlag"),(UNSIGNED___INT32, "cEntries"),(PW32TIME_ENTRY, "pEntries"),]

    
PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA = W32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA

class W32TIME_NTPSERVER_PROVIDER_CONFIG_DATA(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulAllowNonstandardModeCombinations"),(UNSIGNED___INT32, "ulAllowNonstandardModeCombinationsFlag"),(UNSIGNED___INT32, "ulEventLogFlags"),(UNSIGNED___INT32, "ulEventLogFlagsFlag"),(UNSIGNED___INT32, "cEntries"),(PW32TIME_ENTRY, "pEntries"),]

    
PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA = W32TIME_NTPSERVER_PROVIDER_CONFIG_DATA

class W32TIME_PROVIDER_CONFIG_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA, "pNtpClientProviderConfigData"),2 : (PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA, "pNtpServerProviderConfigData"),}

    
PW32TIME_PROVIDER_CONFIG_DATA = W32TIME_PROVIDER_CONFIG_DATA

class W32TIME_PROVIDER_CONFIG(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulProviderType"),(PW32TIME_PROVIDER_CONFIG_DATA, "pProviderConfigData"),]

    
PW32TIME_PROVIDER_CONFIG = W32TIME_PROVIDER_CONFIG

class W32TIME_CONFIGURATION_BASIC(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulEventLogFlags"),(UNSIGNED___INT32, "ulAnnounceFlags"),(UNSIGNED___INT32, "ulTimeJumpAuditOffset"),(UNSIGNED___INT32, "ulMinPollInterval"),(UNSIGNED___INT32, "ulMaxPollInterval"),(UNSIGNED___INT32, "ulMaxNegPhaseCorrection"),(UNSIGNED___INT32, "ulMaxPosPhaseCorrection"),(UNSIGNED___INT32, "ulMaxAllowedPhaseOffset"),(UNSIGNED___INT32, "ulEventLogFlagsFlag"),(UNSIGNED___INT32, "ulAnnounceFlagsFlag"),(UNSIGNED___INT32, "ulTimeJumpAuditOffsetFlag"),(UNSIGNED___INT32, "ulMinPollIntervalFlag"),(UNSIGNED___INT32, "ulMaxPollIntervalFlag"),(UNSIGNED___INT32, "ulMaxNegPhaseCorrectionFlag"),(UNSIGNED___INT32, "ulMaxPosPhaseCorrectionFlag"),(UNSIGNED___INT32, "ulMaxAllowedPhaseOffsetFlag"),]

    
PW32TIME_CONFIGURATION_BASIC = W32TIME_CONFIGURATION_BASIC

class W32TIME_CONFIGURATION_ADVANCED(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulFrequencyCorrectRate"),(UNSIGNED___INT32, "ulPollAdjustFactor"),(UNSIGNED___INT32, "ulLargePhaseOffset"),(UNSIGNED___INT32, "ulSpikeWatchPeriod"),(UNSIGNED___INT32, "ulLocalClockDispersion"),(UNSIGNED___INT32, "ulHoldPeriod"),(UNSIGNED___INT32, "ulPhaseCorrectRate"),(UNSIGNED___INT32, "ulUpdateInterval"),(UNSIGNED___INT32, "ulFrequencyCorrectRateFlag"),(UNSIGNED___INT32, "ulPollAdjustFactorFlag"),(UNSIGNED___INT32, "ulLargePhaseOffsetFlag"),(UNSIGNED___INT32, "ulSpikeWatchPeriodFlag"),(UNSIGNED___INT32, "ulLocalClockDispersionFlag"),(UNSIGNED___INT32, "ulHoldPeriodFlag"),(UNSIGNED___INT32, "ulPhaseCorrectRateFlag"),(UNSIGNED___INT32, "ulUpdateIntervalFlag"),]

    
PW32TIME_CONFIGURATION_ADVANCED = W32TIME_CONFIGURATION_ADVANCED

class W32TIME_CONFIGURATION_DEFAULT(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(PWCHAR_T, "wszFileLogName"),(PWCHAR_T, "wszFileLogEntries"),(UNSIGNED___INT32, "ulFileLogSize"),(UNSIGNED___INT32, "ulFileLogFlags"),(UNSIGNED___INT32, "ulFileLogNameFlag"),(UNSIGNED___INT32, "ulFileLogEntriesFlag"),(UNSIGNED___INT32, "ulFileLogSizeFlag"),(UNSIGNED___INT32, "ulFileLogFlagsFlag"),]

    
PW32TIME_CONFIGURATION_DEFAULT = W32TIME_CONFIGURATION_DEFAULT

class W32TIME_CONFIGURATION_PROVIDER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "ulInputProvider"),(UNSIGNED___INT32, "ulEnabled"),(PWCHAR_T, "wszDllName"),(PWCHAR_T, "wszProviderName"),(UNSIGNED___INT32, "ulDllNameFlag"),(UNSIGNED___INT32, "ulProviderNameFlag"),(UNSIGNED___INT32, "ulInputProviderFlag"),(UNSIGNED___INT32, "ulEnabledFlag"),(PW32TIME_PROVIDER_CONFIG, "pProviderConfig"),]

    
PW32TIME_CONFIGURATION_PROVIDER = W32TIME_CONFIGURATION_PROVIDER

class W32TIME_CONFIGURATION_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(W32TIME_CONFIGURATION_BASIC, "basicConfig"),(W32TIME_CONFIGURATION_ADVANCED, "advancedConfig"),(W32TIME_CONFIGURATION_DEFAULT, "defaultConfig"),(UNSIGNED___INT32, "cProviderConfig"),(PPW32TIME_CONFIGURATION_PROVIDER, "pProviderConfig"),(UNSIGNED___INT32, "cEntries"),(PW32TIME_ENTRY, "pEntries"),]

    
PW32TIME_CONFIGURATION_INFO = W32TIME_CONFIGURATION_INFO

class W32TIME_STATUS_INFO(NdrStructure):
    MEMBERS = [(UNSIGNED___INT32, "ulSize"),(UNSIGNED___INT32, "eLeapIndicator"),(UNSIGNED___INT32, "nStratum"),(SIGNED___INT32, "nPollInterval"),(UNSIGNED___INT32, "refidSource"),(UNSIGNED___INT64, "qwLastSyncTicks"),(SIGNED___INT64, "toRootDelay"),(UNSIGNED___INT64, "tpRootDispersion"),(SIGNED___INT32, "nClockPrecision"),(PWCHAR_T, "wszSource"),(SIGNED___INT64, "toSysPhaseOffset"),(UNSIGNED___INT32, "ulLcState"),(UNSIGNED___INT32, "ulTSFlags"),(UNSIGNED___INT32, "ulClockRate"),(UNSIGNED___INT32, "ulNetlogonServiceBits"),(UNSIGNED___INT32, "eLastSyncResult"),(UNSIGNED___INT64, "tpTimeLastGoodSync"),(UNSIGNED___INT32, "cEntries"),(PW32TIME_ENTRY, "pEntries"),]

    
PW32TIME_STATUS_INFO = W32TIME_STATUS_INFO
Interface("8fb6d884-2388-11d0-8c35-00c04fda2795", "4.1",[Method("W32TimeSync",
In((HANDLE_T,'hBinding')),
In((UNSIGNED_LONG,'uWait')),
In((UNSIGNED_LONG,'ulFlags')),
),Method("W32TimeGetNetlogonServiceBits",
In((HANDLE_T,'hBinding')),
),Method("W32TimeQueryProviderStatus",
In((HANDLE_T,'hRPCBinding')),
In((UNSIGNED___INT32,'ulFlags')),
In((PWCHAR_T,'pwszProvider')),
Out((PPW32TIME_PROVIDER_INFO,'pProviderInfo')),
),Method("W32TimeQuerySource",
In((HANDLE_T,'hBinding')),
Out((PPWCHAR_T,'pwszSource')),
),Method("W32TimeQueryProviderConfiguration",
In((HANDLE_T,'hBinding')),
In((UNSIGNED___INT32,'ulFlags')),
In((PWCHAR_T,'pwszProvider')),
Out((PPW32TIME_CONFIGURATION_PROVIDER,'pConfigurationProviderInfo')),
),Method("W32TimeQueryConfiguration",
In((HANDLE_T,'hBinding')),
Out((PPW32TIME_CONFIGURATION_INFO,'pConfigurationInfo')),
),Method("W32TimeQueryStatus",
In((HANDLE_T,'hBinding')),
Out((PPW32TIME_STATUS_INFO,'pStatusInfo')),
),Method("W32TimeLog",
In((HANDLE_T,'hBinding')),
),])