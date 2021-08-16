IDL_TYPES = [
    "unsigned short",
    "unsigned char",
    "unsigned long",
    "unsigned int",
    "unsigned __int64",
    "signed __int64",
    "signed int",
    "signed long",
    "signed char",
    "signed short",
    "const wchar_t",
    "const char",
    "const int",
    "const void",
    "const long",
    "void",
    "__int3264",
    "unsigned __int3264",
    "const unsigned long",
    "unsigned hyper",
    "hyper",
]

IDL_TO_NDR = {
    "unsigned short": "NDRUSHORT",
    "unsigned char": "NDRCHAR",
    "unsigned long": "NDRULONG",
    "unsigned int": "NDRULONG",
    "unsigned __int64": "NDRUHYPER",
    "signed __int64": "NDRHYPER",
    "signed int": "NDRSHORT",
    "signed long": "NDRLONG",
    "signed char": "NDRCHAR",
    "signed short": "NDRSHORT",
    "const wchar_t": "WSTR",
    "const char": "NDRCHAR",
    "const int": "NDRLONG",
    "const void": "CONTEXT_HANDLE",
    "const long": "NDRLONG",
    "void": "CONTEXT_HANDLE",
    "__int3264": "NDRLONG",
    "unsigned __int3264": "NDRULONG",
    "const unsigned long": "NDRULONG",
    "unsigned hyper": "NDRUHYPER",
    "hyper": "NDRHYPER",
}
SIZEOF_LOOKUP = {"WCHAR": 4, "BOOL": 1, "UINT32": 2, "UINT64": 4, "GUID": 16}


class TypeMappingException(Exception):
    pass


class PythonTypeAssociation:
    """A datatype that holds Python variable names"""

    def __init__(self, raw_names: list[str]):
        self.raw_names = raw_names

    def add_mapping(self, idl_name):
        self.raw_names.append(idl_name)

    def raw(self):
        return self.raw_names


class IDLTypeToPythonType:
    """A class that maps an IDL type name to a PythonTypeAssociation"""

    def __init__(self):
        self._type_lookup = {}

    def get_python_type_name(self, type_name: str):
        if type(type_name) is not str:
            print(type_name)
            raise TypeError(f"Expecting str, got {type(type_name)} instead")
        type_name = type_name.replace("*", "")
        if type_name not in self._type_lookup:
            return None
        return self._type_lookup[type_name].raw()[0]

    def add_entry(self, idl_name: str, python_name: str):
        if idl_name not in self._type_lookup:
            assoc = PythonTypeAssociation([])
            assoc.add_mapping(python_name)
        else:
            assoc = self._type_lookup[idl_name]
            assoc.add_mapping(python_name)
        self._type_lookup[idl_name] = assoc

    def set_defaults(self, words):
        for word in words:
            self.add_entry(word, "_".join(word.split(" ")).upper())


class TypeMapper:
    def __init__(self, default_names):
        self.idl2python = IDLTypeToPythonType()
        self.idl2python.set_defaults(default_names)

    def canonicalize(self, name: str) -> str:
        """canonicalizes an IDL typename into the Python typename format"""
        type_name = self.idl2python.get_python_type_name(name)
        if type_name != None:
            return type_name
        name = name.replace("const", "")
        return name.replace("*", "").upper()

    def calculate_sizeof(self, rhs):
        if "sizeof" not in rhs:
            return rhs

        so_idx = rhs.index("sizeof")
        lb_idx = rhs.index("(")
        rb_idx = rhs.index(")")
        type_str = rhs[lb_idx + 1 : rb_idx].strip()
        print(type_str)
        if type_str not in SIZEOF_LOOKUP:
            type_str=self.calculate_sizeof(type_str)
            #raise Exception(f"Could not get sizeof({type_str})")
        return (
            rhs[:so_idx]
            + str(SIZEOF_LOOKUP[type_str])
            + rhs[rb_idx + 1 :]
        )
