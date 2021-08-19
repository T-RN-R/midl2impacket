from .base import ConversionException, Converter
from midltypes import *
import enum
from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonDictEntry,
    PythonDictEntryList,
    PythonDict,
    PythonValue,
    PythonName,
    PythonTuple,
)
from impacketbuilder.ndrbuilder.ndr import (
    PythonNdrStruct,
    PythonNdrPointer,
    PythonNdrUnion,
    PythonNdrUniConformantArray,
    PythonNdrUniFixedArray,
)


class Dimensionality(enum.Enum):
    """A set of enums that specify how a type mapping should be handled
    SARR -> Scalar array
    PARR -> Pointer array
    CONST -> Constant cardinality
    VAR -> Varying cardinality
    D* -> Dimensionality
    """

    SCALAR = (
        enum.auto()
    )  # Not a pointer, not an array. Just a good old raw type ie. short b
    CONST_D1_SARR = (
        enum.auto()
    )  # A constant sized unidimensional array. ie. short b[10];
    VAR_D1_SARR = (
        enum.auto()
    )  # A variable sized unidimensional array. ie. [size_is(m)] short b[m];
    VAR_D1_PARR = (
        enum.auto()
    )  # A variable sized unidimensional array. ie. [size_is(m)] short * b;
    PTR_PTR_VAR_D1_SARR = (
        enum.auto()
    )  # Pointer to a pointer of a variable sized uni-array ie. [size_is(,m)] short ** b;
    PTR_VAR_D1_PARR = (
        enum.auto()
    )  # Variable sized array of pointers to scalar ie. [size_is(m,)] short ** b;
    VAR_D2_PARR_VAR_D1_SARR = (
        enum.auto()
    )  # Variable sized arr of ptrs, each pointing to a variable sized array of scalars ie. [size_is(m,n)] short ** b;


class VarDefConverter(Converter):
    def convert(self, var_def: MidlVarDef):
        # detect the appropriate handler function
        is_string = False
        is_arr = False
        for attr in var_def.attributes:
            if attr == "switch_is":
                continue
            elif attr == "string":
                is_string = True
                break
            elif attr == "size_is":
                is_arr = True
            else:
                raise Exception(f"Unhandled attr {attr}")

        if is_string:
            return self.handle_string(var_def)
        elif is_arr:
            return self.handle_arr(var_def)
        else:
            return self.handle_scalar(var_def)
    def python_vardef(self, var_name, type_name):
        return PythonTuple(
            [
                PythonValue(f"'{var_name}'"),
                PythonValue(type_name)
            ]
        )
    def handle_scalar(self, var_def: MidlVarDef):
        if len(var_def.array_info) > 0:
            # This array handling should never be hit, it is old code TODO
            raise Exception("Unreachable")
            if len(var_def.array_info) == 1:
                arr_inf = var_def.array_info[0]
                if arr_inf.min != -1  and arr_inf.max == -1:
                    #NDRUniFixedArrays
                    if type(arr_inf.min) == str:
                        size = self.mapper.calculate_sizeof(arr_inf.min)
                    else:
                        size = arr_inf.min
                    type_name = f"ARR_{self.mapper.canonicalize(type_name)}"
                    PythonNdrUniFixedArray(type_name, size)
                else:
                    # NDRUniConformantArrays
                    array_item_name = type_name
                    if type(arr_inf.max) == str:
                        size = self.mapper.calculate_sizeof(arr_inf.max)
                    else:
                        size = arr_inf.max
                    type_name = f"{self.mapper.canonicalize(array_item_name)}_ARRAY"
                    arr = PythonNdrUniConformantArray(type_name, f"{self.mapper.canonicalize(array_item_name)}", size)
                    self.write(arr.to_string())
            else:
                #TODO handle multidimensional arrays here
                raise Exception("Multi-dimensional arrays are unhandled")
        return self.python_vardef(var_def.name, self.mapper.canonicalize(var_def.type))
    

    def handle_string(self, var_def: MidlVarDef):
        # determine if the string is variable or const sized
        is_variable = False
        for attr in var_def.attributes:
            assert attr not in [
                "first_is",
                "max_is",
                "length_is",
            ], f"Invalid MIDL, attributes `string` and `{attr}` are mutually exclusive"
            if attr == "size_is":
                is_variable = True

        if is_variable:
            return self.handle_variable_sized_string(var_def)
        else:
            if(len(var_def.array_info) == 0):
                # This case is beyond our skill and knowledge. Fallback to the impacket NDR type (WSTR)
                type_name = self.mapper.canonicalize(var_def.type.replace("*",''))
                return self.python_vardef(var_name=var_def.name, type_name=type_name)

            return self.handle_constant_sized_string(var_def)

    def handle_variable_sized_string(self, var_def: MidlVarDef):
        raise Exception("Unhandled")

    def handle_constant_sized_string(self, var_def: MidlVarDef):
        raise Exception("Unhandled")


    def handle_arr(self, var_def: MidlVarDef):
        raise Exception("Unhandled")


    def detect_dimensionality(self, var_def: MidlVarDef) -> str:
        type_name = var_def.type
        attributes = var_def.attributes
        is_scalar = False
        is_string = False
        has_size_is = False
        size_attr = None
        # Detect if there are any 'size_is'
        for attr in attributes:
            if attr is str:
                if attr == "string":
                    is_string = True
            if attr == "size_is":
                has_size_is = True
                size_attr = attr
                break
        # Detect if it is a simple scalar
        if "*" not in type_name:
            is_scalar = True

        # If it is a scalar string, we probably stuffed away the dimensions
        if is_scalar and is_string:
            if len(var_def.array_info) > 0:
                pass
            else:
                raise Exception(
                    "Probable invalid MIDL, got string definition without dimenstionality"
                )

        if is_scalar and not has_size_is and not is_string:
            return Dimensionality.SCALAR

        raise Exception("Couldn't detect dimensionality")
