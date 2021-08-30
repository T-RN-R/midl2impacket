
from fuzzer.midl import *
from fuzzer.core import *

class W32TIME_PROVIDER_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : ('PW32TIME_NTP_PROVIDER_DATA', None),2 : ('PW32TIME_HARDWARE_PROVIDER_DATA', None),}

    

class W32TIME_PROVIDER_CONFIG_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : ('PW32TIME_NTPCLIENT_PROVIDER_CONFIG_DATA', None),2 : ('PW32TIME_NTPSERVER_PROVIDER_CONFIG_DATA', None),}

    
interface_0 = Interface("8fb6d884-2388-11d0-8c35-00c04fda2795", "4.1",[
Method("W32TimeSync",
In(HANDLE_T),
In(UNSIGNED_LONG),
In(UNSIGNED_LONG),
),
Method("W32TimeGetNetlogonServiceBits",
In(HANDLE_T),
),
Method("W32TimeQueryProviderStatus",
In(HANDLE_T),
In(UNSIGNED___INT32),
In(PWCHAR_T),
Out(PPW32TIME_PROVIDER_INFO),
),
Method("W32TimeQuerySource",
In(HANDLE_T),
Out(PPWCHAR_T),
),
Method("W32TimeQueryProviderConfiguration",
In(HANDLE_T),
In(UNSIGNED___INT32),
In(PWCHAR_T),
Out(PPW32TIME_CONFIGURATION_PROVIDER),
),
Method("W32TimeQueryConfiguration",
In(HANDLE_T),
Out(PPW32TIME_CONFIGURATION_INFO),
),
Method("W32TimeQueryStatus",
In(HANDLE_T),
Out(PPW32TIME_STATUS_INFO),
),
Method("W32TimeLog",
In(HANDLE_T),
),
])
