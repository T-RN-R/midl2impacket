from impacketbuilder.ndrbuilder.base import PythonValue
from impacketbuilder.ndrbuilder.python import PythonAssignment, PythonName
import re
from impacket.dcerpc.v5.dtypes import LPSTR, LPWSTR, STR, WSTR
from impacket.dcerpc.v5.ndr import (NDRBOOLEAN, NDRDOUBLEFLOAT, NDRFLOAT,
                                    NDRHYPER, NDRLONG, NDRPOINTERNULL, NDRSHORT, NDRSMALL,
                                    NDRUHYPER, NDRULONG, NDRUSHORT, NDRUSMALL, NULL)
from impacketbuilder.ndrbuilder.io import PythonWriter
from impacketbuilder.ndrbuilder.ndr import PythonNdrPointer

# Implemented in static
class CONTEXT_HANDLE():
    pass

IDL_TO_NDR = {

    # Language Primitives
    "BOOLEAN": NDRBOOLEAN,
    "CHAR": NDRSMALL,
    "DOUBLE": NDRDOUBLEFLOAT,
    "FLOAT": NDRFLOAT,
    "HYPER": NDRHYPER,
    "INT": NDRLONG,
    "LONG": NDRLONG,
    "LONG_LONG": NDRHYPER,
    "SHORT": NDRSMALL,
    "SIGNED_CHAR": NDRSMALL,
    "SIGNED HYPER": NDRHYPER,
    "SIGNED_INT": NDRLONG,
    "SIGNED___INT3264": NDRHYPER,
    "SIGNED___INT64": NDRHYPER,
    "SIGNED_LONG": NDRLONG,
    "SIGNED_SHORT": NDRSMALL,
    "UNSIGNED_CHAR": NDRUSMALL,
    "UNSIGNED_SHORT": NDRUSHORT,
    "UNSIGNED HYPER": NDRUHYPER,
    "UNSIGNED_INT": NDRULONG,
    "UNSIGNED_LONG": NDRULONG,
    "UNSIGNED_LONG_LONG": NDRUHYPER,
    "UNSIGNED___INT3264": NDRUHYPER,
    "UNSIGNED___INT64": NDRUHYPER,
    "VOID": NDRPOINTERNULL,
    "PVOID": CONTEXT_HANDLE,
    "WCHAR": NDRSHORT,
    "WORD": NDRSHORT,
    "__INT3264": NDRHYPER,
    "__INT64": NDRHYPER,

    # Special cases for string types implemented by impacket
    "PWCHAR": LPWSTR,
    "PWCHAR_T": LPWSTR,
    "PCHAR": LPSTR,
    "PCHAR_T": LPSTR,
    "LPWSTR": LPWSTR,
    "LPSTR": LPSTR,
    "STR": STR,
    "WSTR": WSTR,

    # Constructed types
    "DWORD__ENUM": NDRULONG,
}
IDL_TO_NDR = {k:v.__name__ for k,v in IDL_TO_NDR.items()}


SIZEOF_LOOKUP = {
    "WCHAR": 2,
    "WCHAR_T": 2,
    "CHAR": 1,
    "BOOL": 1,
    "UINT32": 4,
    "DWORD": 4,
    "UINT64": 8,
    "UNSIGNEDLONG": 4,
    "GUID": 16,
}

STRING_PARAM_TYPES = {
    "PWCHAR_T": "WSTR",
    "PWCHAR": "WSTR",
    "PCHAR_T": "STR",
    "PCHAR": "STR",
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
                    # If the pointee doesn't exist, create a "forward declaration"
                    if pointee_to_create not in self.types:
                        pointee_fwd_dec = PythonAssignment(
                            name=PythonName(pointee_to_create),
                            rhs=PythonValue("None")
                        )
                        self.writer.write(pointee_fwd_dec.to_python_string() + '\n')
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_to_create, referent_name=pointee_to_create
                    )
                    self.writer.write(ndr_ptr.to_string())
                    self.add_type(pointer_to_create)
        return pointer_type

    def canonicalize(
        self, name: str, array_size: str = None, is_func_param=False
    ) -> tuple[str, str]:
        """Canonicalizes an IDL typename into the Python typename format"""

        # Strip const and spaces
        py_name = re.sub(r'\s*CONST[*\s]+', '', name.upper())
        py_name = py_name.strip().replace(" ", "_")

        # Default fixup for function calls: remove first level of indirection
        if is_func_param:
            # TODO: this should really get the actual type and read the referent
            if py_name.endswith('*'):
                ptr_type = self.pointerize(py_name)
                if ptr_type in STRING_PARAM_TYPES:
                    py_name = STRING_PARAM_TYPES[ptr_type]
                else:
                    py_name = py_name[:-1]


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
        self, idl_type: str, array_size: str, is_func_param=False, array_prefix:str=''
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
        py_array_name = array_prefix + py_array_name
        return py_array_name, py_member_name, (py_array_name in self.types)

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

    def add_type(self, py_name: str):
        """Adds a type to the dict of known types.
        Args:
            py_name (str): The python-friendly name of the class or variable
        """
        self.types[py_name] = True

    def calculate_sizeof(self, rhs):
        if "sizeof" not in rhs:
            return rhs
        return SizeofCalculator(rhs).calculate()

    def exists(self, type_name):
        return type_name in self.types


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
                type_str, _ = TypeMapper().canonicalize(type_str)
                if type_str not in SIZEOF_LOOKUP:
                    raise Exception(f"Could not get sizeof({type_str})")
                ex = ex[:i] + str(SIZEOF_LOOKUP[type_str]) + tmp[rb_idx + 1 :]
        self.expression = ex

    def calculate(self):
        self.expression = "".join(self.expression.split(" "))
        self.eval_size_of()
        return self.expression
