
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("C3FCC19E-A970-112-85-0009794", "1.0",[
Method("GetSerializedBuffer",
Out(PBSTR),
),
Method("GetObjectIdentity",
Out(PBSTR),
Out(PINT),
Out(CCW_PTR),
),
])
interface_1 = Interface("6619a740-8154-43be-a186-0319578e02db", "1.0",[
Method("RemoteDispatchAutoDone",
In(BSTR),
Out(PBSTR),
),
Method("RemoteDispatchNotAutoDone",
In(BSTR),
Out(PBSTR),
),
])
interface_2 = Interface("8165B19E-8D3A-4d0b-80C8-97DE310DB583", "1.0",[
Method("GetComponentInfo",
InOut(PINT),
Out(PSAFEARRAY),
),
])
