from midltypes import MidlPointerType, MidlStructDef, MidlUnionDef
from impacketbuilder.ndrbuilder.ndr import PythonNdrPointer
from impacketbuilder.ndrbuilder.io import PythonWriter

IDL_TO_NDR = {
    "unsigned short": "NDRUSHORT",
    "unsigned char": "NDRCHAR",
    "unsigned long": "NDRULONG",
    "unsignedlong": "NDRULONG",
    "unsigned int": "NDRULONG",
    "unsigned __int64": "NDRUHYPER",
    "signed __int64": "NDRHYPER",
    "signed int": "NDRSHORT",
    "signed long": "NDRLONG",
    "signed char": "NDRCHAR",
    "signed short": "NDRSHORT",
    "wchar_t": "WSTR",
    "char": "NDRCHAR",
    "int": "NDRLONG",
    "void": "CONTEXT_HANDLE",
    "long": "NDRLONG",
    "__int3264": "NDRHYPER",
    "unsigned __int3264": "NDRUHYPER",
    "unsigned hyper": "NDRUHYPER",
    "hyper": "NDRHYPER",
    "dwordlong": "NDRUHYPER",
    "long ptr": "NDRHYPER",
    "ulong ptr": "NDRUHYPER",
    "LARGE_INTEGER": "LARGE_INTEGER",  # impacket type
    "LPSTR": "LPSTR",  # impacket type
    "LPWSTR": "LPWSTR",  # impacket type
    "LPCSTR": "LPSTR",  # impacket type
    "LPCWSTR": "LPWSTR",  # impacket type
    "LMSTR": "LPWSTR",  # impacket type
    "PWSTR": "LPWSTR",  # TODO validate that this is correct
    "WCHAR": "WSTR",  # impacket type
    "PBYTE": "PBYTE",  # impacket type
    "GUID": "GUID",  # impacket type
    "DWORD": "DWORD", # impacket type
    "HRESULT": "HRESULT", # impacket type
    "__INT64": "__INT64", # impacket type
}

SIZEOF_LOOKUP = {
    "BYTE": 1,
    "UCHAR": 1,
    "CHAR": 1,
    "UNSIGNED_CHAR": 1,
    "BOOL": 1,
    "BOOLEAN": 1,
    "USHORT": 2,
    "UNSIGNED_SHORT": 2,
    "SHORT": 2,
    "WCHAR": 2,
    "WORD": 2,
    "WCHAR_T": 2,
    "UINT32": 4,
    "UINT": 4,
    "INT": 4,
    "DWORD": 4,
    "LONG": 4,
    "UNSIGNEDLONG": 4,
    "UNSIGNED_LONG": 4,
    "UNSIGNED_INT": 4,
    "ULONG": 4,
    "HRESULT": 4,
    "UINT64": 8,
    "FLOAT": 8,
    "DOUBLE": 8,
    "ULONG_PTR": 8,
    "ULONGLONG": 8,
    "LONGLONG": 8,
    "LPWSTR": 8,
    "PRPC_UNICODE_STRING": 8,
    "PRPC_STRING": 8,
    "UNSIGNED_HYPER": 8,
    "UNSIGNED___INT64": 8,
    "__INT64": 8,
    "HYPER": 8,
    "CLSID": 16,
    "GUID": 16,
    "RPC_UNICODE_STRING": 16,
}

SIZEOF_LOOKUP.update({f"P{k}":8 for k in SIZEOF_LOOKUP.keys()})

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

    def get_python_type_name(self, type_name: str) -> str:
        if not isinstance(type_name, str):
            raise TypeError(f"Expecting str, got {type(type_name)} instead")
        type_name = type_name.strip()
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

    def exists(self, idl_name):
        return idl_name in self._type_lookup.keys()

    def set_defaults(self, words):
        for word in words:
            self.add_entry(word, "_".join(word.split(" ")).upper())


class TypeMapper:
    def __init__(self, writer: PythonWriter = None):
        self.writer = writer
        self.types = {}
        self.calculator = SizeofCalculator(self)

    def pointerize(self, pointer_type: str) -> str:
        """Replaces asterisks in pointer names, creating intermediate types if they don't exist
            e.g. DWORD* becomes PDWORD and DWORD** becomes PPDWORD
        Args:
            name (str): The name, which may contain pointers

        Returns:
            [str]: python-friendly pointer name
        """
        pointer_type = pointer_type.upper()
        pointer_count = pointer_type.count("*")
        root_type = pointer_type.rstrip("*").lstrip("*")
        pointer_type = "P" * pointer_count + root_type
        pointers_to_create = []
        while pointer_count > 0:
            pointer_name = "P" * pointer_count + root_type
            pointee_name = "P" * (pointer_count - 1) + root_type
            pointers_to_create.append((pointer_name, pointee_name))
            pointer_count -= 1

        if pointers_to_create and self.writer:
            for pointer_to_create, pointee_to_create in pointers_to_create[::-1]:
                if pointer_to_create not in self.types:
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_to_create, referent_name=pointee_to_create
                    )
                    self.writer.write(ndr_ptr.to_string())
                    self.add_type(
                        pointer_to_create,
                        MidlPointerType(name=pointer_to_create, pointee=pointee_to_create)
                    )
        return pointer_type

    def canonicalize(self, name: str, array_size: str = None, is_func_param=False) -> tuple[str, str]:
        """Canonicalizes an IDL typename into the Python typename format"""

        if name is None:
            print("z")

        py_name = name
        # Default fixup for function calls: remove first level of indirection
        if is_func_param:
            # TODO: this should really get the actual type and read the referent
            if py_name.endswith('*'):
                py_name = py_name[:-1]

        # Now remove const and spaces then uppercase the name
        py_name = py_name.replace("const", "").strip().replace(" ", "_").upper()
        
        py_member_name = None
        # Check array information:
        # Pointers to arrays e.g. DWORD* become DWORD_ARRAY
        # Known-size pointers to arrays e.g. [size_is(5)] DWORD* pDwords becomes DWORD_ARRAY_5
        # For a pointer to a pointer array, e.g. [size(5)] DWORD** ppDwords becomes PDWORD_ARRAY_5
        # Similarly, PDWORD* ppDwords would result in the same name, PDWORD_ARRAY_5
        if array_size is not None:
            if py_name.endswith("*"):
                py_name = py_name[:-1]
            py_member_name = self.pointerize(py_name)
            suffix = ""
            if array_size.isnumeric() and int(array_size) > 0:
                suffix = f"_{array_size}"
            py_name = f"{py_member_name}_ARRAY{suffix}"
        else:
            py_name = self.pointerize(py_name)

        return py_name, py_member_name

    def get_python_array_type(
        self, idl_type: str, array_size: str, is_func_param=False
    ) -> tuple[str, str, bool]:
        """Returns the array type name, the member name, and whether the type exists

        Args:
            idl_type (str): IDL type name
            array_size (str): Length of the array

        Returns:
            tuple[str, str, bool]:
                Tuple containing the array name, the member name, and whether the array type exists,
        """
        # Convert to python-friendly names
        py_array_name, py_member_name = self.canonicalize(
            idl_type, array_size=array_size, is_func_param=is_func_param
        )
        return py_array_name, py_member_name, py_array_name in self.types

    def get_python_type(self, idl_type: str, is_func_param=False) -> tuple[str, bool]:
        """Returns python-friendly names for IDL names, along with a boolean indicating whether the
           data structure for the type exists or not.

        Args:
            idl_type (str): IDL type name

        Returns:
            tuple[str, bool]: tuple containing the python-friendly name, and whether the type exists
        """
        # Convert this to a python name and see if we know about it
        py_name, _ = self.canonicalize(idl_type, is_func_param=is_func_param)
        return py_name, py_name in self.types

    def add_type(self, py_name: str, py_type):
        """Adds a type to the dict of known types.
        Args:
            py_name (str): The python-friendly name of the class or variable
        """
        self.types[py_name] = py_type

    def get_type(self, py_name):
        return self.types[py_name]

    def calculate_sizeof(self, obj):
        # String values e.g. something in an attribute
        if isinstance(obj, str):
            # Default to just returning the string itself
            size = obj
            if not obj:
                size = "0"
            elif "sizeof" in obj:
                size = self.calculator.evaluate(obj)
            elif obj in self.types:
                # It might be a simple type with a known size (or an impacket type)
                size = self.calculator.sizeof(obj)
                if not size:
                    # It must be a complex type
                    size = self.calculate_sizeof(self.types[obj])
            # We can't calculate this, maybe it's just a symbol
            return size
        # Structs and Unions
        elif isinstance(obj, (MidlStructDef, MidlUnionDef)):
            size = 0
            for member in obj.members:
                if member.type:
                    member_size_str = self.calculate_sizeof(member)
                    size += int(member_size_str)
            return str(size)
        # Pointers
        elif isinstance(obj, MidlPointerType):
            # 64-bit pointers
            return "8"
        else:
            py_type = self.canonicalize(obj.type)[0]
            if obj_size := self.calculator.sizeof(py_type):
                return obj_size
            # This is likely a vardef representing a struct/union member
            # who is itself a struct/union etc.
            if py_type not in self.types or not self.types[py_type]:
                raise Exception(f"DEVELOPER ERROR: Need to add known size for {py_type}")
            return self.calculate_sizeof(self.types[py_type])

    def exists(self, type_name):
        return type_name in self.types


class SizeofCalculator:
    OPERATORS = ["+", "-", "*", "/"]

    def __init__(self, mapper: TypeMapper):
        self.mapper = mapper

    def evaluate(self, expression:str):
        ex = expression
        for i in range(0, len(expression)):
            if ex[i:].startswith("sizeof"):
                tmp = ex[i:]
                lb_idx = tmp.index("(")
                rb_idx = tmp.index(")")
                type_str = tmp[lb_idx + 1 : rb_idx].strip()
                type_str, _ = self.mapper.canonicalize(type_str)
                type_size = self.sizeof(type_str)
                ex = ex[:i] + type_size + tmp[rb_idx + 1 :]
        return ex

    def sizeof(self, type_str: str):
        type_str = self.mapper.canonicalize(type_str)[0]
        if type_str not in SIZEOF_LOOKUP:
            return None
        return str(SIZEOF_LOOKUP[type_str])
