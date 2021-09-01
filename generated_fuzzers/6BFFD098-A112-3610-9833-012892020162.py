
from fuzzer.midl import *
from fuzzer.core import *
ULONGLONG = NdrHyper
BYTE = NdrByte
USHORT = NdrShort
SHORT = NdrShort
UCHAR = NdrByte
PCHAR = NdrByte
PUCHAR = NdrByte
PLONG64 = NdrHyper
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
PDWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
PUNSIGNED_LONG = NdrLong
PUNSIGNED_CHAR = NdrByte
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
PWCHAR = NdrCString
INT = NdrLong
PVOID = NdrContextHandle
VOID = NdrContextHandle
CONTEXT_HANDLE = NdrContextHandle
PPCONTEXT_HANDLE = NdrContextHandle
LONG = NdrLong
INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LARGE_INTEGER = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte
DOUBLE = NdrDouble
FLOAT = NdrFloat

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')]

class LUID(NdrStructure):
    MEMBERS = [(DWORD,'LowPart'),(LONG,'HighPart')]

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),]
LPWSTR = WCHAR
BROWSER_IDENTIFY_HANDLE = LPWSTR

class SERVER_INFO_100_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "EntriesRead"),(LPSERVER_INFO_100, "Buffer"),]

    
PSERVER_INFO_100_CONTAINER = SERVER_INFO_100_CONTAINER
LPSERVER_INFO_100_CONTAINER = SERVER_INFO_100_CONTAINER

class SERVER_ENUM_STRUCT(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(SERVERINFO, "ServerInfo"),]

    
PSERVER_ENUM_STRUCT = SERVER_ENUM_STRUCT
LPSERVER_ENUM_STRUCT = SERVER_ENUM_STRUCT
Interface("6BFFD098-A112-3610-9833-012892020162", "0.0",[Method("Opnum0NotUsedOnWire",
),Method("Opnum1NotUsedOnWire",
),Method("I_BrowserrQueryOtherDomains",
In((BROWSER_IDENTIFY_HANDLE,'ServerName')),
InOut((LPSERVER_ENUM_STRUCT,'InfoStruct')),
Out((LPDWORD,'TotalEntries')),
),Method("Opnum3NotUsedOnWire",
),Method("Opnum4NotUsedOnWire",
),Method("Opnum5NotUsedOnWire",
),Method("Opnum6NotUsedOnWire",
),Method("Opnum7NotUsedOnWire",
),Method("Opnum8NotUsedOnWire",
),Method("Opnum9NotUsedOnWire",
),Method("Opnum10NotUsedOnWire",
),Method("Opnum11NotUsedOnWire",
),])