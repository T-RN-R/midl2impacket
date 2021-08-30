
from fuzzer.midl import *
from fuzzer.core import *
interface_0 = Interface("4da1c422-943d-11d1-acae-00c04fc2aa3f", "1.0",[
Method("LnkSvrMessage",
In(HANDLE_T),
InOut(PTRKSVR_MESSAGE_UNION),
),
Method("LnkSvrMessageCallback",
InOut(PTRKSVR_MESSAGE_UNION),
),
])
