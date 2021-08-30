
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("B60040E0-BCF3-111-861-0080729264", "1.0",[
Method("Opnum3NotUsedOnWire",
),
Method("GetContainerData",
Out(PDWORD),
Out(PPCONTAINERDATA),
),
Method("GetComponentDataByContainer",
In(DWORD),
Out(PDWORD),
Out(PPCOMPONENTDATA),
),
Method("GetComponentDataByContainerAndCLSID",
In(DWORD),
In(GUID),
Out(PPCOMPONENTDATA),
),
Method("Opnum7NotUsedOnWire",
),
])
interface_1 = Interface("4E6CDCC9-FB25-4FD5-9CC5-C9F4B6559CEC", "1.0",[
Method("OnNewTrackingInfo",
In(PIUNKNOWN),
),
])
interface_2 = Interface("23C9DD26-2355-4FE2-84DE-F779A238ADBD", "1.0",[
Method("IsSupported",
),
Method("DumpProcess",
In(BSTR),
In(BSTR),
In(DWORD),
Out(PBSTR),
),
])
