
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("22e5386d-8b12-4bf0-b0ec-6a1ea419e366", "1.0",[
Method("RpcNetEventOpenSession",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPSESSION_HANDLE),
),
Method("RpcNetEventReceiveData",
In(PSESSION_HANDLE),
Out(PEVENT_BUFFER),
),
Method("RpcNetEventCloseSession",
InOut(PPSESSION_HANDLE),
),
])
