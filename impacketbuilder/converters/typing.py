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
    "pvoid",
    "__int3264",
    "unsigned __int3264",
    "const unsigned long",
    "unsigned hyper",
    "hyper",
    "dwordlong",
    "long ptr",
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
    "pvoid": "CONTEXT_HANDLE",
    "__int3264": "NDRHYPER",
    "unsigned __int3264": "NDRUHYPER",
    "const unsigned long": "NDRULONG",
    "unsigned hyper": "NDRUHYPER",
    "hyper": "NDRHYPER",
    "dwordlong": "NDRUHYPER",
    "long ptr": "NDRHYPER",
    "ulong ptr": "NDRUHYPER",
}

SIZEOF_LOOKUP = {
    "WCHAR": 4,
    "WCHAR_T": 4,
    "CHAR": 2,
    "BOOL": 1,
    "UINT32": 2,
    "UINT64": 4,
    "UNSIGNEDLONG": 4,
    "GUID": 16,
}


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
            raise TypeError(f"Expecting str, got {type(type_name)} instead")
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

    def exists(self, type_name):
        return type_name in self._type_lookup

class TypeMapper:
    def __init__(self, default_names):
        self.idl2python = IDLTypeToPythonType()
        self.idl2python.set_defaults(default_names)


    def fixup_name(self, type_name: str):
        type_name = type_name.replace("const", "").strip()
        while type_name[-1] == '*':
            type_name = f"P{type_name[:-1]}"
        # Get rid of leading *s and spaces
        return type_name.lstrip('*').replace(' ', '_')

    def canonicalize(self, name: str) -> str:
        """canonicalizes an IDL typename into the Python typename format"""
        type_name = self.fixup_name(name)
        if (py_name := self.idl2python.get_python_type_name(type_name)) is not None:
            return py_name
        return type_name.upper()

    def calculate_sizeof(self, rhs):
        if "sizeof" not in rhs:
            return rhs
        return SizeofCalculator(rhs).calculate()

    def exists(self, type_name):
        return self.idl2python.exists(type_name)

    def add_entry(self, idl_name: str, python_name: str):
        return self.idl2python.add_entry(idl_name, python_name)


class SizeofCalculator:
    OPERATORS = ["+", "-", "*", "/"]

    def __init__(self, expression):
        self.expression = expression

    def eval_size_of(self):
        ex = self.expression
        for i in range(0, len(self.expression)):
            if ex[i:].startswith("sizeof"):
                tmp = ex[i:]
                lb_idx = tmp.index("(")
                rb_idx = tmp.index(")")
                type_str = tmp[lb_idx + 1 : rb_idx].strip()
                type_str = TypeMapper(IDL_TYPES).canonicalize(type_str)
                if type_str not in SIZEOF_LOOKUP:
                    raise Exception(f"Could not get sizeof({type_str})")
                ex = ex[:i] + str(SIZEOF_LOOKUP[type_str]) + tmp[rb_idx + 1 :]
        self.expression = ex

    def calculate(self):
        self.expression = "".join(self.expression.split(" "))
        self.eval_size_of()
        return self.expression
