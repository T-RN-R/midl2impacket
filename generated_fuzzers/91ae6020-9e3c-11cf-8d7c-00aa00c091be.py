
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("91ae6020-9e3c-11cf-8d7c-00aa00c091be", "1.0",[
Method("CertServerRequest",
In(HANDLE_T),
In(DWORD),
In(PWCHAR_T),
InOut(PDWORD),
Out(PDWORD),
In(PCERTTRANSBLOB),
In(PCERTTRANSBLOB),
Out(PCERTTRANSBLOB),
Out(PCERTTRANSBLOB),
Out(PCERTTRANSBLOB),
),
])
