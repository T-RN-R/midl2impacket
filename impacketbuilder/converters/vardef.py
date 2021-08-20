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
    """Converts MidlVarDef objects into Python definitions"""

    def convert(self, var_def: MidlVarDef) -> PythonTuple:
        """Delegate handling depending upon attributes"""
        is_string = "string" in var_def.attributes
        is_arr = "size_is" in var_def.attributes or var_def.array_info
        if is_string:
            return self.handle_string(var_def)
        elif is_arr:
            return self.handle_arr(var_def)
        else:
            return self.handle_scalar(var_def)

    def python_vardef(self, var_name, type_name) -> PythonTuple:
        """Helper function to generate PythonDef"""
        return PythonTuple([PythonValue(f"'{var_name}'"), PythonValue(type_name)])

    def handle_scalar(self, var_def: MidlVarDef) -> PythonTuple:
        """Handles the scalar case"""
        if len(var_def.array_info) > 0:
            # This array handling should never be hit, it is old code TODO
            raise Exception("Unreachable")
        return self.python_vardef(var_def.name, self.mapper.canonicalize(var_def.type))

    def handle_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Handles the string case"""
        # determine if the string is variable or const sized
        is_variable = False
        for attr in var_def.attributes:
            assert attr not in [
                "first_is",
                "last_is",
                "length_is",
            ], f"Invalid MIDL, attributes `string` and `{attr}` are mutually exclusive"
            if attr == "size_is" or attr == "max_is":
                is_variable = True

        if is_variable:
            return self.handle_variable_sized_string(var_def)
        else:
            if len(var_def.array_info) == 0:
                # This case is beyond our ability. Fallback to the impacket NDR type (WSTR)
                type_name = self.mapper.canonicalize(var_def.type.replace("*", ""))
                return self.python_vardef(var_name=var_def.name, type_name=type_name)

            return self.handle_constant_sized_string(var_def)

    def handle_variable_sized_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Creates a PythonDef for string attributed MidlVarDefs that have a valid size_is"""
        size_is = None
        max_is = None
        for attr in var_def.attributes:
            if attr == "size_is":
                size_is = var_def.attributes[attr]
        assert (
            size_is != None or max_is != None
        ), "Calling handle_variable_sized_string with no size_is!"

        number_of_ptrs = 0
        for c in var_def.type:
            if c == "*":
                number_of_ptrs += 1

        # Continue implementation ========================================================
        # TODO properly handle these cases. There can be multidimensional arrays of these!
        return self.python_vardef(
            var_name=var_def.name, type_name=self.mapper.canonicalize(var_def.type)
        )

    def handle_constant_sized_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Creates a PythonDef for string attributed MidlVarDefs that have a constant size"""

        # Continue implementation ========================================================
        # TODO properly handle these cases. There can be multidimensional arrays of these!
        return self.python_vardef(
            var_name=var_def.name, type_name=self.mapper.canonicalize(var_def.type)
        )

    def handle_arr(self, var_def: MidlVarDef) -> PythonTuple:
        """Delegates array creation depending on the case"""
        dimensionality = len(var_def.array_info)
        if dimensionality > 0:
            # C-style array definiton
            return self.handle_square_array(var_def)
        else:
            # Pointer style arrays
            size_is = var_def.attributes["size_is"]
            dimensionality = len(size_is.params)
            return self.handle_pointer_array(var_def)

    def handle_square_array(self, var_def: MidlVarDef) -> PythonTuple:
        """Handles the following cases:
        UNI : [size_is(m)] short a[]);
        MULTI : [size_is(m)] short b[][20]);
        """
        dimensionality = len(var_def.array_info)
        if dimensionality == 1:
            type_name = var_def.type
            arr_inf = var_def.array_info[0]
            if arr_inf.min != -1 and arr_inf.max == -1:
                # NDRUniFixedArrays
                if isinstance(arr_inf.min,str):
                    size = self.mapper.calculate_sizeof(arr_inf.min)
                else:
                    size = arr_inf.min
                # TODO Create better typenames
                type_name = f"ARR_{self.mapper.canonicalize(type_name)}"
                arr = PythonNdrUniFixedArray(type_name, size)
            else:
                # NDRUniConformantArrays
                if isinstance(arr_inf.max,str):
                    size = self.mapper.calculate_sizeof(arr_inf.max)
                else:
                    size = arr_inf.max
                # TODO Create better typenames
                type_name = f"ARR_{self.mapper.canonicalize(type_name)}"
                arr = PythonNdrUniConformantArray(
                    type_name, f"{self.mapper.canonicalize(var_def.type)}", size
                )
            self.write(arr.to_string())
            return self.python_vardef(
                var_name=var_def.name, type_name=self.mapper.canonicalize(type_name)
            )
        else:
            raise Exception("Multidimensional arrays are unimplemented")

    def handle_pointer_array(self, var_def: MidlVarDef) -> PythonTuple:
        """Handles the following cases:
        POINTER_TO_SCALAR_ARRAY                     : [size_is(m)] short * pshort);
        POINTER_TO_POINTER_TO_SCALAR_ARRAY          : [size_is( , m)] short ** ppshort);
        ARRAY_OF_POINTERS_TO_SCALARS                : [size_is(m ,)] short ** ppshort);
        POINTER_TO_ARRAY_OF_POINTER_TO_SCALAR_ARRAY : [size_is(m,n)] short ** ppshort);
        POINTER_TO_SIZED_POINTER_TO_SCALAR          : [size_is( , *pSize)] my_type ** ppMyType);
        """
        # TODO handle more than the 1 and 2 dimensional cases
        dimensionality = var_def.attributes['size_is'].type
        if dimensionality == SizeIsType.POINTER_TO_SCALAR_ARRAY:
            size_var = var_def.attributes["size_is"].params[0]
            # size_var can be either a numeric,  or variable name or an expression.
            if isinstance(size_var, str):
                #Handle expression and variable case
                size = self.mapper.calculate_sizeof(size_var)
            elif size_var.isnumeric():
                size = size_var

            # TODO Create better typenames
            type_name = f"ARR_{self.mapper.canonicalize(var_def.type)}"
             
            arr = PythonNdrUniConformantArray(
                    type_name, f"{self.mapper.canonicalize(var_def.type)}", size
                )
            self.write(arr.to_string())
            return self.python_vardef(
                var_name=var_def.name, type_name=self.mapper.canonicalize(type_name)
            )
        elif dimensionality == SizeIsType.POINTER_TO_POINTER_TO_SCALAR_ARRAY:
            raise NotImplementedError(f"Unhandled dimensionality {dimensionality}")
        elif dimensionality == SizeIsType.ARRAY_OF_POINTERS_TO_SCALARS:
            raise NotImplementedError(f"Unhandled dimensionality {dimensionality}")
        elif dimensionality == SizeIsType.POINTER_TO_ARRAY_OF_POINTER_TO_SCALAR_ARRAY:
            raise NotImplementedError(f"Unhandled dimensionality {dimensionality}")
        elif dimensionality == SizeIsType.POINTER_TO_SIZED_POINTER_TO_SCALAR:
            raise NotImplementedError(f"Unhandled dimensionality {dimensionality}")
        
        raise Exception(f"Unrecognized dimensionality {dimensionality}")
