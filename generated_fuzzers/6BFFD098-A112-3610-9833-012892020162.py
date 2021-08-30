
from fuzzer.midl import *
from fuzzer.core import *
import .server
BYTE = NdrByte
USHORT = NdrShort
UCHAR = NdrByte
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
__INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
INT = NdrLong
VOID = CONTEXT_HANDLE
LONG = NdrLong
__INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte
Method("Opnum0NotUsedOnWire",
In(),
),Method("Opnum1NotUsedOnWire",
In(),
),Method("I_BrowserrQueryOtherDomains",
In(BROWSER_IDENTIFY_HANDLE),
InOut(LPSERVER_ENUM_STRUCT),
Out(LPDWORD),
),Method("Opnum3NotUsedOnWire",
In(),
),Method("Opnum4NotUsedOnWire",
In(),
),Method("Opnum5NotUsedOnWire",
In(),
),Method("Opnum6NotUsedOnWire",
In(),
),Method("Opnum7NotUsedOnWire",
In(),
),Method("Opnum8NotUsedOnWire",
In(),
),Method("Opnum9NotUsedOnWire",
In(),
),Method("Opnum10NotUsedOnWire",
In(),
),Method("Opnum11NotUsedOnWire",
In(),
),