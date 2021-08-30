
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("41208ee0-e970-11d1-9b9e-00e02c064c39", "1.0",[
Method("R_QMMgmtGetInfo",
In(HANDLE_T),
In(PMGMT_OBJECT),
In(DWORD),
In(ULONG),
InOut(PROPVARIANT),
),
Method("R_QMMgmtAction",
In(HANDLE_T),
In(PMGMT_OBJECT),
In(PWCHAR_T),
),
])
