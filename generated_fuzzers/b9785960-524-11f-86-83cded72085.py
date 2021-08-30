
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("b9785960-524-11f-86-83cded72085", "1.0",[
Method("GetKey",
In(HANDLE_T),
In(ULONG),
In(PCHAR),
In(PGUID),
In(LONG),
In(LONG),
In(LONG),
Out(PUNSIGNED_LONG),
Out(PPBYTE),
),
])
