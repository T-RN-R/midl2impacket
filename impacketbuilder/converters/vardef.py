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

    def __init__(self, *args, func_params=False, **kwargs):
        super().__init__(*args, **kwargs)
        # Are we converting parameter names? Important for name conversion
        self.func_params = func_params

    def convert(self, var_def: MidlVarDef) -> PythonTuple:
        """Delegate handling depending upon attributes"""
        is_string = "string" in var_def.attributes
        is_arr = "size_is" in var_def.attributes or var_def.array_info
        # Check arrays first, as they can be marked with strings
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
        if len(var_def.array_info):
            # This array handling should never be hit, it is old code TODO
            raise Exception(f"Invalid scalar (has array information): {var_def}")
        elif not isinstance(var_def.type, str):
            raise Exception(f"Invalid scalar - is non-string type: {var_def}")
        type_name = self.mapper.get_python_type(
            var_def.type, is_func_param=self.func_params
        )[0]
        return self.python_vardef(var_def.name, type_name)

    def handle_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Handles the string case"""
        # determine if the string is variable or const sized
        is_variable = "size_is" in var_def.attributes or "max_is" in var_def.attributes
        if is_variable:
            return self.handle_variable_sized_string(var_def)
        else:
            if len(var_def.array_info) == 0:
                # This is already handled by impacket
                type_name, type_exists = self.mapper.get_python_type(
                    var_def.type, is_func_param=self.func_params
                )
                if not type_exists:
                    raise Exception(
                        f"Type {type_name} doesn't have an impacket mapping?"
                    )
                return self.python_vardef(var_name=var_def.name, type_name=type_name)

            return self.handle_constant_sized_string(var_def)

    def handle_variable_sized_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Creates a PythonDef for string attributed MidlVarDefs that have a valid size_is"""
        size_is = var_def.attributes.get("size_is")
        max_is = var_def.attributes.get("max_is")
        if not size_is and not max_is:
            raise Exception(f"Calling handle_variable_sized_string with no size_is!")
        array_size = size_is.params[0] if size_is else max_is.params[0]

        # Refs:
        # https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/77f2250d-500a-40ee-be18-c82f7079c4f0
        # https://github.com/SecureAuthCorp/impacket/blob/cd4fe47cfcb72d7d35237a99e3df95cedf96e94f/impacket/dcerpc/v5/tsch.py#L505
        (
            array_type_name,
            array_member_name,
            array_type_exists,
        ) = self.mapper.get_python_array_type(
            var_def.type, array_size=array_size, is_func_param=self.func_params
        )
        if not array_type_exists:
            arr = PythonNdrUniConformantArray(
                array_type_name, array_member_name, array_size
            )
            self.write(arr.to_string())
            self.mapper.add_type(array_type_name)
        return self.python_vardef(var_name=var_def.name, type_name=array_type_name)

    def handle_constant_sized_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Creates a PythonDef for string attributed MidlVarDefs that have a constant size"""

        # Continue implementation ========================================================
        # TODO properly handle these cases. There can be multidimensional arrays of these!
        type_name, _ = self.mapper.get_python_type(
            var_def.type, is_func_param=self.func_params
        )
        return self.python_vardef(var_name=var_def.name, type_name=type_name)

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
            arr_inf = var_def.array_info[0]
            if arr_inf.min and not arr_inf.max:
                # NDRUniFixedArrays
                size = self.mapper.calculate_sizeof(arr_inf.min)
                (
                    array_type_name,
                    array_member_name,
                    array_type_exists,
                ) = self.mapper.get_python_array_type(
                    var_def.type, array_size=size, is_func_param=self.func_params
                )
                arr = PythonNdrUniFixedArray(array_type_name, size)
            else:
                # NDRUniConformantArrays
                size = self.mapper.calculate_sizeof(arr_inf.max)
                (
                    array_type_name,
                    array_member_name,
                    array_type_exists,
                ) = self.mapper.get_python_array_type(
                    var_def.type, array_size=size, is_func_param=self.func_params
                )
                arr = PythonNdrUniConformantArray(
                    array_type_name, array_member_name, size
                )
            if not array_type_exists:
                self.write(arr.to_string())
                self.mapper.add_type(array_type_name)
            return self.python_vardef(var_name=var_def.name, type_name=array_type_name)
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
        dimensionality = var_def.attributes["size_is"].type
        if dimensionality == SizeIsType.POINTER_TO_SCALAR_ARRAY:
            size_var = var_def.attributes["size_is"].params[0]
            # size_var can be either a numeric,  or variable name or an expression.
            if isinstance(size_var, str):
                # Handle expression and variable case
                size = self.mapper.calculate_sizeof(size_var)
            elif size_var.isnumeric():
                size = size_var

            # Get the python type
            (
                array_type_name,
                array_member_name,
                array_type_exists,
            ) = self.mapper.get_python_array_type(
                var_def.type, array_size=size, is_func_param=self.func_params
            )
            if not array_type_exists:
                arr = PythonNdrUniConformantArray(
                    array_type_name, array_member_name, size
                )
                self.write(arr.to_string())
                self.mapper.add_type(array_type_name)
            # Create the pointer to the array type:
            pointer_type_name = f"P{array_type_name}"
            pointee_type_name = array_type_name
            if not self.mapper.exists(pointer_type_name):
                ndr_ptr = PythonNdrPointer(
                    name=pointer_type_name, referent_name=pointee_type_name
                )
                self.write(ndr_ptr.to_string())
                self.mapper.add_type(pointer_type_name)
            return_type_name = (
                array_type_name if self.func_params else pointer_type_name
            )
            return self.python_vardef(var_name=var_def.name, type_name=return_type_name)
        elif dimensionality == SizeIsType.POINTER_TO_POINTER_TO_SCALAR_ARRAY:
            raise NotImplementedError(
                f"Unhandled dimensionality {dimensionality} for {var_def}"
            )
        elif dimensionality == SizeIsType.ARRAY_OF_POINTERS_TO_SCALARS:
            raise NotImplementedError(
                f"Unhandled dimensionality {dimensionality} for {var_def}"
            )
        elif dimensionality == SizeIsType.POINTER_TO_ARRAY_OF_POINTER_TO_SCALAR_ARRAY:
            size_var = var_def.attributes["size_is"].params[1]
            if isinstance(size_var, str):
                # Handle expression and variable case
                size = self.mapper.calculate_sizeof(size_var)
            elif size_var.isnumeric():
                size = size_var
            (
                array_type_name,
                array_member_name,
                array_type_exists,
            ) = self.mapper.get_python_array_type(
                var_def.type, array_size=size, is_func_param=self.func_params
            )
            if not array_type_exists:
                arr = PythonNdrUniConformantArray(
                    array_type_name, array_member_name, size
                )
                self.write(arr.to_string())
                self.mapper.add_type(array_type_name)
            pointer_type_name = f"P{array_type_name}"
            pointee_type_name = array_type_name
            if not self.mapper.exists(pointer_type_name):
                ndr_ptr = PythonNdrPointer(
                    name=pointer_type_name, referent_name=pointee_type_name
                )
                self.write(ndr_ptr.to_string())
                self.mapper.add_type(pointer_type_name)
            return_type_name = (
                array_type_name if self.func_params else pointer_type_name
            )
            return self.python_vardef(var_name=var_def.name, type_name=return_type_name)
        elif dimensionality == SizeIsType.POINTER_TO_SIZED_POINTER_TO_SCALAR:
            raise NotImplementedError(
                f"Unhandled dimensionality {dimensionality} for {var_def}"
            )

        raise Exception(f"Unrecognized dimensionality {dimensionality}")
