IDL_TO_NDR = {
    "DWORD64" : "NdrHyper",
    "DWORD" : "NdrLong",
    "__INT64" : "NdrHyper",
    "unsigned short": "NdrShort",
    "unsigned char": "NdrByte",
    "unsigned long": "NdrLong",
    "unsignedlong": "NdrLong",
    "unsigned int": "NdrLong",
    "unsigned __int64": "NdrHyper",
    "signed __int64": "NdrHyper",
    "signed int": "NdrShort",
    "signed long": "NdrLong",
    "signed char": "NdrByte",
    "signed short": "NdrShort",
    "wchar_t": "NdrWString",
    "char": "NdrByte",
    "int": "NdrLong",
    "void": "CONTEXT_HANDLE",
    "long": "NdrLong",
    "__int3264": "NdrHyper",
    "unsigned __int3264": "NdrHyper",
    "unsigned hyper": "NdrHyper",
    "hyper": "NdrHyper",
    "dwordlong": "NdrHyper",
    "long ptr": "NdrHyper",
    "ulong ptr": "NdrHyper",
    "LARGE_INTEGER": "LARGE_INTEGER",  # impacket type
    "LPSTR": "NdrCString",  # impacket type
    "LPWSTR": "NdrWString",  # impacket type
    "LPCSTR": "NdrCString",  # impacket type
    "LPCWSTR": "NdrWString",  # impacket type
    "LMSTR": "NdrWString",  # impacket type
    "PWSTR": "NdrWString",  # TODO validate that this is correct
    "WCHAR": "NdrWString",  # impacket type
    "PBYTE": "NdrByte",  # impacket type
}

class DataTypeLookup:
    """Maintains a dictionary of all RPC objects created during the execution of a given testcase.

    This allows passing output datatypes into input fields.
    TBD: Figure out a way to map aliased types. ie. typeddef-ed context_handles"""

    def __init__(self):
        # mapping of datatype : [generated data]
        self.map = {}
        # mapping of type : [aliased types]
        self.alias_map = {}

    def insert(self, datatype, data):
        if datatype in self.map:
            self.map[datatype].extend([data])
        else:
            self.map[datatype] = [data]

    def get(self, datatype):
        return self.map[datatype] if datatype in self.map else []

    def get_valid_aliases(self, datatype):
        aliases = set()
        # TODO this does not include cases where there are multiple levels of typedef indirection.
        for item in self.alias_map:
            entry = self.alias_map[item]
            if datatype in entry:
                aliases.add(*entry)
                aliases.add(item)
        return aliases
