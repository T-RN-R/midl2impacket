
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("034634FD-BA3F-11D1-856A-00A0C944138C", "1.0",[
Method("GetTelnetSessions",
Out(PBSTR),
),
Method("TerminateSession",
In(DWORD),
),
Method("SendMsgToASession",
In(DWORD),
In(BSTR),
),
])
