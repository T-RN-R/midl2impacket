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

#TYPEDEFS

#################################################################################


class W32TIME_NTP_PEER_INFO(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulResolveAttempts', UNSIGNED __INT32),('u64TimeRemaining', UNSIGNED___INT64),('u64LastSuccessfulSync', UNSIGNED___INT64),('ulLastSyncError', UNSIGNED __INT32),('ulLastSyncErrorMsgId', UNSIGNED __INT32),('ulValidDataCounter', UNSIGNED __INT32),('ulAuthTypeMsgId', UNSIGNED __INT32),('wszUniqueName', WCHAR_T),('ulMode', UNSIGNED_CHAR),('ulStratum', UNSIGNED_CHAR),('ulReachability', UNSIGNED_CHAR),('ulPeerPollInterval', UNSIGNED_CHAR),('ulHostPollInterval', UNSIGNED_CHAR),
    )
class PW32TIME_NTP_PEER_INFO(NDRPOINTER):
    referent = (
        ('Data', W32TIME_NTP_PEER_INFO),
    )    


class W32TIME_NTP_PROVIDER_DATA(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulError', UNSIGNED __INT32),('ulErrorMsgId', UNSIGNED __INT32),('cPeerInfo', UNSIGNED __INT32),('pPeerInfo', PW32TIME_NTP_PEER_INFO),
    )
class PW32TIME_NTP_PROVIDER_DATA(NDRPOINTER):
    referent = (
        ('Data', W32TIME_NTP_PROVIDER_DATA),
    )    


class W32TIME_HARDWARE_PROVIDER_DATA(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulError', UNSIGNED __INT32),('ulErrorMsgId', UNSIGNED __INT32),('wszReferenceIdentifier', WCHAR_T),
    )
class PW32TIME_HARDWARE_PROVIDER_DATA(NDRPOINTER):
    referent = (
        ('Data', W32TIME_HARDWARE_PROVIDER_DATA),
    )    


class W32TIME_PROVIDER_DATA(NDRUNION):
    union = {
        0: ('pNtpProviderData',W32TIME_NTP_PROVIDER_DATA),1: ('pHardwareProviderData',W32TIME_HARDWARE_PROVIDER_DATA),
    }
        

class W32TIME_PROVIDER_INFO(NDRSTRUCT):
    structure = (
        ('ulProviderType', UNSIGNED __INT32),('ProviderData', W32TIME_PROVIDER_DATA),
    )
class PW32TIME_PROVIDER_INFO(NDRPOINTER):
    referent = (
        ('Data', W32TIME_PROVIDER_INFO),
    )    


class W32TIME_ENTRY(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('wszName', WCHAR_T),('wszValue', WCHAR_T),('wszHelp', WCHAR_T),
    )
class PW32TIME_ENTRY(NDRPOINTER):
    referent = (
        ('Data', W32TIME_ENTRY),
    )    


class W32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulAllowNonstandardModeCombinations', UNSIGNED __INT32),('ulCrossSiteSyncFlags', UNSIGNED __INT32),('ulResolvePeerBackoffMinutes', UNSIGNED __INT32),('ulResolvePeerBackoffMaxTimes', UNSIGNED __INT32),('ulCompatibilityFlags', UNSIGNED __INT32),('ulEventLogFlags', UNSIGNED __INT32),('ulLargeSampleSkew', UNSIGNED __INT32),('ulSpecialPollInterval', UNSIGNED __INT32),('wszType', WCHAR_T),('wszNtpServer', WCHAR_T),('ulAllowNonstandardModeCombinationsFlag', UNSIGNED __INT32),('ulCrossSiteSyncFlagsFlag', UNSIGNED __INT32),('ulResolvePeerBackoffMinutesFlag', UNSIGNED __INT32),('ulResolvePeerBackoffMaxTimesFlag', UNSIGNED __INT32),('ulCompatibilityFlagsFlag', UNSIGNED __INT32),('ulEventLogFlagsFlag', UNSIGNED __INT32),('ulLargeSampleSkewFlag', UNSIGNED __INT32),('ulSpecialPollIntervalFlag', UNSIGNED __INT32),('ulTypeFlag', UNSIGNED __INT32),('ulNtpServerFlag', UNSIGNED __INT32),('cEntries', UNSIGNED __INT32),('pEntries', PW32TIME_ENTRY),
    )
class PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA(NDRPOINTER):
    referent = (
        ('Data', W32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA),
    )    


class W32TIME_NTPSERVER_PROVIDER_CONFIG_DATA(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulAllowNonstandardModeCombinations', UNSIGNED __INT32),('ulAllowNonstandardModeCombinationsFlag', UNSIGNED __INT32),('ulEventLogFlags', UNSIGNED __INT32),('ulEventLogFlagsFlag', UNSIGNED __INT32),('cEntries', UNSIGNED __INT32),('pEntries', PW32TIME_ENTRY),
    )
class PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA(NDRPOINTER):
    referent = (
        ('Data', W32TIME_NTPSERVER_PROVIDER_CONFIG_DATA),
    )    


class W32TIME_PROVIDER_CONFIG_DATA(NDRUNION):
    union = {
        0: ('pNtpClientProviderConfigData',PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA),1: ('pNtpServerProviderConfigData',PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA),
    }
        class PW32TIME_PROVIDER_CONFIG_DATA(NDRPOINTER):
    referent = (
        ('Data', W32TIME_PROVIDER_CONFIG_DATA),
    )    


class W32TIME_PROVIDER_CONFIG(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulProviderType', UNSIGNED __INT32),('pProviderConfigData', PW32TIME_PROVIDER_CONFIG_DATA),
    )
class PW32TIME_PROVIDER_CONFIG(NDRPOINTER):
    referent = (
        ('Data', W32TIME_PROVIDER_CONFIG),
    )    


class W32TIME_CONFIGURATION_BASIC(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulEventLogFlags', UNSIGNED __INT32),('ulAnnounceFlags', UNSIGNED __INT32),('ulTimeJumpAuditOffset', UNSIGNED __INT32),('ulMinPollInterval', UNSIGNED __INT32),('ulMaxPollInterval', UNSIGNED __INT32),('ulMaxNegPhaseCorrection', UNSIGNED __INT32),('ulMaxPosPhaseCorrection', UNSIGNED __INT32),('ulMaxAllowedPhaseOffset', UNSIGNED __INT32),('ulEventLogFlagsFlag', UNSIGNED __INT32),('ulAnnounceFlagsFlag', UNSIGNED __INT32),('ulTimeJumpAuditOffsetFlag', UNSIGNED __INT32),('ulMinPollIntervalFlag', UNSIGNED __INT32),('ulMaxPollIntervalFlag', UNSIGNED __INT32),('ulMaxNegPhaseCorrectionFlag', UNSIGNED __INT32),('ulMaxPosPhaseCorrectionFlag', UNSIGNED __INT32),('ulMaxAllowedPhaseOffsetFlag', UNSIGNED __INT32),
    )
class PW32TIME_CONFIGURATION_BASIC(NDRPOINTER):
    referent = (
        ('Data', W32TIME_CONFIGURATION_BASIC),
    )    


class W32TIME_CONFIGURATION_ADVANCED(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulFrequencyCorrectRate', UNSIGNED __INT32),('ulPollAdjustFactor', UNSIGNED __INT32),('ulLargePhaseOffset', UNSIGNED __INT32),('ulSpikeWatchPeriod', UNSIGNED __INT32),('ulLocalClockDispersion', UNSIGNED __INT32),('ulHoldPeriod', UNSIGNED __INT32),('ulPhaseCorrectRate', UNSIGNED __INT32),('ulUpdateInterval', UNSIGNED __INT32),('ulFrequencyCorrectRateFlag', UNSIGNED __INT32),('ulPollAdjustFactorFlag', UNSIGNED __INT32),('ulLargePhaseOffsetFlag', UNSIGNED __INT32),('ulSpikeWatchPeriodFlag', UNSIGNED __INT32),('ulLocalClockDispersionFlag', UNSIGNED __INT32),('ulHoldPeriodFlag', UNSIGNED __INT32),('ulPhaseCorrectRateFlag', UNSIGNED __INT32),('ulUpdateIntervalFlag', UNSIGNED __INT32),
    )
class PW32TIME_CONFIGURATION_ADVANCED(NDRPOINTER):
    referent = (
        ('Data', W32TIME_CONFIGURATION_ADVANCED),
    )    


class W32TIME_CONFIGURATION_DEFAULT(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('wszFileLogName', WCHAR_T),('wszFileLogEntries', WCHAR_T),('ulFileLogSize', UNSIGNED __INT32),('ulFileLogFlags', UNSIGNED __INT32),('ulFileLogNameFlag', UNSIGNED __INT32),('ulFileLogEntriesFlag', UNSIGNED __INT32),('ulFileLogSizeFlag', UNSIGNED __INT32),('ulFileLogFlagsFlag', UNSIGNED __INT32),
    )
class PW32TIME_CONFIGURATION_DEFAULT(NDRPOINTER):
    referent = (
        ('Data', W32TIME_CONFIGURATION_DEFAULT),
    )    


class W32TIME_CONFIGURATION_PROVIDER(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('ulInputProvider', UNSIGNED __INT32),('ulEnabled', UNSIGNED __INT32),('wszDllName', WCHAR_T),('wszProviderName', WCHAR_T),('ulDllNameFlag', UNSIGNED __INT32),('ulProviderNameFlag', UNSIGNED __INT32),('ulInputProviderFlag', UNSIGNED __INT32),('ulEnabledFlag', UNSIGNED __INT32),('pProviderConfig', PW32TIME_PROVIDER_CONFIG),
    )
class PW32TIME_CONFIGURATION_PROVIDER(NDRPOINTER):
    referent = (
        ('Data', W32TIME_CONFIGURATION_PROVIDER),
    )    


class DATA_UNSIGNED __INT32(NDRUniConformantArray):
    item = PW32TIME_ENTRY

class PTR_UNSIGNED __INT32(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED __INT32),
    )

class UNSIGNED __INT32(NDRSTRUCT):
    structure = (
	('ulSize', UNSIGNED __INT32),	('basicConfig', W32TIME_CONFIGURATION_BASIC),	('advancedConfig', W32TIME_CONFIGURATION_ADVANCED),	('defaultConfig', W32TIME_CONFIGURATION_DEFAULT),	('cProviderConfig', UNSIGNED __INT32),	('pProviderConfig', PW32TIME_CONFIGURATION_PROVIDER),	('cEntries', UNSIGNED __INT32),	('pEntries', PTR_UNSIGNED __INT32),

    )
        

class W32TIME_STATUS_INFO(NDRSTRUCT):
    structure = (
        ('ulSize', UNSIGNED __INT32),('eLeapIndicator', UNSIGNED __INT32),('nStratum', UNSIGNED __INT32),('nPollInterval', SIGNED __INT32),('refidSource', UNSIGNED __INT32),('qwLastSyncTicks', UNSIGNED___INT64),('toRootDelay', SIGNED___INT64),('tpRootDispersion', UNSIGNED___INT64),('nClockPrecision', SIGNED __INT32),('wszSource', WCHAR_T),('toSysPhaseOffset', SIGNED___INT64),('ulLcState', UNSIGNED __INT32),('ulTSFlags', UNSIGNED __INT32),('ulClockRate', UNSIGNED __INT32),('ulNetlogonServiceBits', UNSIGNED __INT32),('eLastSyncResult', UNSIGNED __INT32),('tpTimeLastGoodSync', UNSIGNED___INT64),('cEntries', UNSIGNED __INT32),('pEntries', PW32TIME_ENTRY),
    )
class PW32TIME_STATUS_INFO(NDRPOINTER):
    referent = (
        ('Data', W32TIME_STATUS_INFO),
    )    

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#W32Time Definition

#################################################################################

MSRPC_UUID_W32TIME = uuidtup_to_bin(('8fb6d884-2388-11d0-8c35-00c04fda2795','0.0'))


class W32TimeSync(NDRCALL):
    opnum = 0
    structure = (
		('hBinding', HANDLE_T),
		('uWait', UNSIGNED_LONG),
		('ulFlags', UNSIGNED_LONG),
    )

class W32TimeSyncResponse(NDRCALL):
    structure = (

    )
        

class W32TimeGetNetlogonServiceBits(NDRCALL):
    opnum = 1
    structure = (
		('hBinding', HANDLE_T),
    )

class W32TimeGetNetlogonServiceBitsResponse(NDRCALL):
    structure = (

    )
        

class W32TimeQueryProviderStatus(NDRCALL):
    opnum = 2
    structure = (
		('hRPCBinding', HANDLE_T),
		('ulFlags', UNSIGNED __INT32),
		('pwszProvider', WCHAR_T),
    )

class W32TimeQueryProviderStatusResponse(NDRCALL):
    structure = (
		('pProviderInfo', PW32TIME_PROVIDER_INFO),
    )
        

class W32TimeQuerySource(NDRCALL):
    opnum = 3
    structure = (
		('hBinding', HANDLE_T),
    )

class W32TimeQuerySourceResponse(NDRCALL):
    structure = (
		('pwszSource', WCHAR_T),
    )
        

class W32TimeQueryProviderConfiguration(NDRCALL):
    opnum = 4
    structure = (
		('hBinding', HANDLE_T),
		('ulFlags', UNSIGNED __INT32),
		('pwszProvider', WCHAR_T),
    )

class W32TimeQueryProviderConfigurationResponse(NDRCALL):
    structure = (
		('pConfigurationProviderInfo', PW32TIME_CONFIGURATION_PROVIDER),
    )
        

class W32TimeQueryConfiguration(NDRCALL):
    opnum = 5
    structure = (
		('hBinding', HANDLE_T),
    )

class W32TimeQueryConfigurationResponse(NDRCALL):
    structure = (
		('pConfigurationInfo', PW32TIME_CONFIGURATION_INFO),
    )
        

class W32TimeQueryStatus(NDRCALL):
    opnum = 6
    structure = (
		('hBinding', HANDLE_T),
    )

class W32TimeQueryStatusResponse(NDRCALL):
    structure = (
		('pStatusInfo', PW32TIME_STATUS_INFO),
    )
        

class W32TimeLog(NDRCALL):
    opnum = 7
    structure = (
		('hBinding', HANDLE_T),
    )

class W32TimeLogResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (W32TimeSync,W32TimeSyncResponse),
1 : (W32TimeGetNetlogonServiceBits,W32TimeGetNetlogonServiceBitsResponse),
2 : (W32TimeQueryProviderStatus,W32TimeQueryProviderStatusResponse),
3 : (W32TimeQuerySource,W32TimeQuerySourceResponse),
4 : (W32TimeQueryProviderConfiguration,W32TimeQueryProviderConfigurationResponse),
5 : (W32TimeQueryConfiguration,W32TimeQueryConfigurationResponse),
6 : (W32TimeQueryStatus,W32TimeQueryStatusResponse),
7 : (W32TimeLog,W32TimeLogResponse),
}

