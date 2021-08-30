
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("E8FB8620-588-112-961-0004795E", "1.0",[
Method("Stop",
In(DWORD),
In(DWORD),
),
Method("Start",
In(DWORD),
),
Method("Reboot",
In(DWORD),
In(DWORD),
),
Method("Status",
In(DWORD),
Out(PUNSIGNED_CHAR),
Out(PDWORD),
Out(PDWORD),
),
Method("Kill",
),
])
