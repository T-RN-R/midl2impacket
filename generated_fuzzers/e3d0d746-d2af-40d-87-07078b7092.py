
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("e3d0d746-d2af-40d-87-07078b7092", "1.0",[
Method("ExchangePublicKeys",
In(HANDLE_T),
In(KEY_LENGTH),
In(PBYTE),
Out(PKEY_LENGTH),
Out(PPBYTE),
),
])
