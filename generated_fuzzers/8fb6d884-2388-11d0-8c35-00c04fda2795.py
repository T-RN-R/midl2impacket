
from fuzzer.midl import *
from fuzzer.core import *

class ('W32TIME_NTP_PEER_INFO', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulResolveAttempts"),(('UNSIGNED___INT64', None), "u64TimeRemaining"),(('UNSIGNED___INT64', None), "u64LastSuccessfulSync"),(('UNSIGNED___INT32', None), "ulLastSyncError"),(('UNSIGNED___INT32', None), "ulLastSyncErrorMsgId"),(('UNSIGNED___INT32', None), "ulValidDataCounter"),(('UNSIGNED___INT32', None), "ulAuthTypeMsgId"),(('PWCHAR_T', None), "wszUniqueName"),(('UNSIGNED_CHAR', None), "ulMode"),(('UNSIGNED_CHAR', None), "ulStratum"),(('UNSIGNED_CHAR', None), "ulReachability"),(('UNSIGNED_CHAR', None), "ulPeerPollInterval"),(('UNSIGNED_CHAR', None), "ulHostPollInterval"),]

    

class ('W32TIME_NTP_PROVIDER_DATA', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulError"),(('UNSIGNED___INT32', None), "ulErrorMsgId"),(('UNSIGNED___INT32', None), "cPeerInfo"),(('PW32TIME_NTP_PEER_INFO', None), "pPeerInfo"),]

    

class ('W32TIME_HARDWARE_PROVIDER_DATA', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulError"),(('UNSIGNED___INT32', None), "ulErrorMsgId"),(('PWCHAR_T', None), "wszReferenceIdentifier"),]

    

class ('W32TIME_PROVIDER_DATA', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PW32TIME_NTP_PROVIDER_DATA', None), pNtpProviderData),2 : (('PW32TIME_HARDWARE_PROVIDER_DATA', None), pHardwareProviderData),}

    

class ('W32TIME_PROVIDER_INFO', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulProviderType"),(('W32TIME_PROVIDER_DATA', None), "ProviderData"),]

    

class ('W32TIME_ENTRY', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('PWCHAR_T', None), "wszName"),(('PWCHAR_T', None), "wszValue"),(('PWCHAR_T', None), "wszHelp"),]

    

class ('W32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulAllowNonstandardModeCombinations"),(('UNSIGNED___INT32', None), "ulCrossSiteSyncFlags"),(('UNSIGNED___INT32', None), "ulResolvePeerBackoffMinutes"),(('UNSIGNED___INT32', None), "ulResolvePeerBackoffMaxTimes"),(('UNSIGNED___INT32', None), "ulCompatibilityFlags"),(('UNSIGNED___INT32', None), "ulEventLogFlags"),(('UNSIGNED___INT32', None), "ulLargeSampleSkew"),(('UNSIGNED___INT32', None), "ulSpecialPollInterval"),(('PWCHAR_T', None), "wszType"),(('PWCHAR_T', None), "wszNtpServer"),(('UNSIGNED___INT32', None), "ulAllowNonstandardModeCombinationsFlag"),(('UNSIGNED___INT32', None), "ulCrossSiteSyncFlagsFlag"),(('UNSIGNED___INT32', None), "ulResolvePeerBackoffMinutesFlag"),(('UNSIGNED___INT32', None), "ulResolvePeerBackoffMaxTimesFlag"),(('UNSIGNED___INT32', None), "ulCompatibilityFlagsFlag"),(('UNSIGNED___INT32', None), "ulEventLogFlagsFlag"),(('UNSIGNED___INT32', None), "ulLargeSampleSkewFlag"),(('UNSIGNED___INT32', None), "ulSpecialPollIntervalFlag"),(('UNSIGNED___INT32', None), "ulTypeFlag"),(('UNSIGNED___INT32', None), "ulNtpServerFlag"),(('UNSIGNED___INT32', None), "cEntries"),(('PW32TIME_ENTRY', None), "pEntries"),]

    

class ('W32TIME_NTPSERVER_PROVIDER_CONFIG_DATA', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulAllowNonstandardModeCombinations"),(('UNSIGNED___INT32', None), "ulAllowNonstandardModeCombinationsFlag"),(('UNSIGNED___INT32', None), "ulEventLogFlags"),(('UNSIGNED___INT32', None), "ulEventLogFlagsFlag"),(('UNSIGNED___INT32', None), "cEntries"),(('PW32TIME_ENTRY', None), "pEntries"),]

    

class ('W32TIME_PROVIDER_CONFIG_DATA', None)(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (('PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA', None), pNtpClientProviderConfigData),2 : (('PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA', None), pNtpServerProviderConfigData),}

    

class ('W32TIME_PROVIDER_CONFIG', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulProviderType"),(('PW32TIME_PROVIDER_CONFIG_DATA', None), "pProviderConfigData"),]

    

class ('W32TIME_CONFIGURATION_BASIC', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulEventLogFlags"),(('UNSIGNED___INT32', None), "ulAnnounceFlags"),(('UNSIGNED___INT32', None), "ulTimeJumpAuditOffset"),(('UNSIGNED___INT32', None), "ulMinPollInterval"),(('UNSIGNED___INT32', None), "ulMaxPollInterval"),(('UNSIGNED___INT32', None), "ulMaxNegPhaseCorrection"),(('UNSIGNED___INT32', None), "ulMaxPosPhaseCorrection"),(('UNSIGNED___INT32', None), "ulMaxAllowedPhaseOffset"),(('UNSIGNED___INT32', None), "ulEventLogFlagsFlag"),(('UNSIGNED___INT32', None), "ulAnnounceFlagsFlag"),(('UNSIGNED___INT32', None), "ulTimeJumpAuditOffsetFlag"),(('UNSIGNED___INT32', None), "ulMinPollIntervalFlag"),(('UNSIGNED___INT32', None), "ulMaxPollIntervalFlag"),(('UNSIGNED___INT32', None), "ulMaxNegPhaseCorrectionFlag"),(('UNSIGNED___INT32', None), "ulMaxPosPhaseCorrectionFlag"),(('UNSIGNED___INT32', None), "ulMaxAllowedPhaseOffsetFlag"),]

    

class ('W32TIME_CONFIGURATION_ADVANCED', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulFrequencyCorrectRate"),(('UNSIGNED___INT32', None), "ulPollAdjustFactor"),(('UNSIGNED___INT32', None), "ulLargePhaseOffset"),(('UNSIGNED___INT32', None), "ulSpikeWatchPeriod"),(('UNSIGNED___INT32', None), "ulLocalClockDispersion"),(('UNSIGNED___INT32', None), "ulHoldPeriod"),(('UNSIGNED___INT32', None), "ulPhaseCorrectRate"),(('UNSIGNED___INT32', None), "ulUpdateInterval"),(('UNSIGNED___INT32', None), "ulFrequencyCorrectRateFlag"),(('UNSIGNED___INT32', None), "ulPollAdjustFactorFlag"),(('UNSIGNED___INT32', None), "ulLargePhaseOffsetFlag"),(('UNSIGNED___INT32', None), "ulSpikeWatchPeriodFlag"),(('UNSIGNED___INT32', None), "ulLocalClockDispersionFlag"),(('UNSIGNED___INT32', None), "ulHoldPeriodFlag"),(('UNSIGNED___INT32', None), "ulPhaseCorrectRateFlag"),(('UNSIGNED___INT32', None), "ulUpdateIntervalFlag"),]

    

class ('W32TIME_CONFIGURATION_DEFAULT', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('PWCHAR_T', None), "wszFileLogName"),(('PWCHAR_T', None), "wszFileLogEntries"),(('UNSIGNED___INT32', None), "ulFileLogSize"),(('UNSIGNED___INT32', None), "ulFileLogFlags"),(('UNSIGNED___INT32', None), "ulFileLogNameFlag"),(('UNSIGNED___INT32', None), "ulFileLogEntriesFlag"),(('UNSIGNED___INT32', None), "ulFileLogSizeFlag"),(('UNSIGNED___INT32', None), "ulFileLogFlagsFlag"),]

    

class ('W32TIME_CONFIGURATION_PROVIDER', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "ulInputProvider"),(('UNSIGNED___INT32', None), "ulEnabled"),(('PWCHAR_T', None), "wszDllName"),(('PWCHAR_T', None), "wszProviderName"),(('UNSIGNED___INT32', None), "ulDllNameFlag"),(('UNSIGNED___INT32', None), "ulProviderNameFlag"),(('UNSIGNED___INT32', None), "ulInputProviderFlag"),(('UNSIGNED___INT32', None), "ulEnabledFlag"),(('PW32TIME_PROVIDER_CONFIG', None), "pProviderConfig"),]

    

class ('W32TIME_CONFIGURATION_INFO', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('W32TIME_CONFIGURATION_BASIC', None), "basicConfig"),(('W32TIME_CONFIGURATION_ADVANCED', None), "advancedConfig"),(('W32TIME_CONFIGURATION_DEFAULT', None), "defaultConfig"),(('UNSIGNED___INT32', None), "cProviderConfig"),(('PPW32TIME_CONFIGURATION_PROVIDER', None), "pProviderConfig"),(('UNSIGNED___INT32', None), "cEntries"),(('PW32TIME_ENTRY', None), "pEntries"),]

    

class ('W32TIME_STATUS_INFO', None)(NdrStructure):
    MEMBERS = [(('UNSIGNED___INT32', None), "ulSize"),(('UNSIGNED___INT32', None), "eLeapIndicator"),(('UNSIGNED___INT32', None), "nStratum"),(('SIGNED___INT32', None), "nPollInterval"),(('UNSIGNED___INT32', None), "refidSource"),(('UNSIGNED___INT64', None), "qwLastSyncTicks"),(('SIGNED___INT64', None), "toRootDelay"),(('UNSIGNED___INT64', None), "tpRootDispersion"),(('SIGNED___INT32', None), "nClockPrecision"),(('PWCHAR_T', None), "wszSource"),(('SIGNED___INT64', None), "toSysPhaseOffset"),(('UNSIGNED___INT32', None), "ulLcState"),(('UNSIGNED___INT32', None), "ulTSFlags"),(('UNSIGNED___INT32', None), "ulClockRate"),(('UNSIGNED___INT32', None), "ulNetlogonServiceBits"),(('UNSIGNED___INT32', None), "eLastSyncResult"),(('UNSIGNED___INT64', None), "tpTimeLastGoodSync"),(('UNSIGNED___INT32', None), "cEntries"),(('PW32TIME_ENTRY', None), "pEntries"),]

    
Method("W32TimeSync",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),Method("W32TimeGetNetlogonServiceBits",
In(HANDLE_T),
),Method("W32TimeQueryProviderStatus",
In(HANDLE_T),
In(UNSIGNED___INT32),
In(PWCHAR_T),
Out(PPW32TIME_PROVIDER_INFO),
),Method("W32TimeQuerySource",
In(HANDLE_T),
Out(PPWCHAR_T),
),Method("W32TimeQueryProviderConfiguration",
In(HANDLE_T),
In(UNSIGNED___INT32),
In(PWCHAR_T),
Out(PPW32TIME_CONFIGURATION_PROVIDER),
),Method("W32TimeQueryConfiguration",
In(HANDLE_T),
Out(PPW32TIME_CONFIGURATION_INFO),
),Method("W32TimeQueryStatus",
In(HANDLE_T),
Out(PPW32TIME_STATUS_INFO),
),Method("W32TimeLog",
In(HANDLE_T),
),