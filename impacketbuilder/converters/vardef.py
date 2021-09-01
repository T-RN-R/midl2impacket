from .base import Converter
from midltypes import *
import enum
from impacketbuilder.ndrbuilder.python import (

    PythonValue,

    PythonTuple,
)
from impacketbuilder.ndrbuilder.ndr import (
    
    PythonNdrPointer,
    PythonNdrUniConformantVaryingArray,
    PythonNdrUniVaryingArray,
    
    PythonNdrUniConformantArray,
    PythonNdrUniFixedArray,
)

UNI_FIXED_PREFIX = 'UF_'
UNI_CONFORMANT_PREFIX = 'UC_'
UNI_VARYING_PREFIX = 'UV_'
UNI_CONFORMANT_VARYING_PREFIX = 'UCV_'

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
        type_name = self.mapper.get_python_type(var_def.type, is_func_param=self.func_params)[0]
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
                    var_def.type,
                    is_func_param=self.func_params
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
        ) = self.mapper.get_python_array_type(var_def.type, array_size=array_size, is_func_param=self.func_params)
        if not array_type_exists:
            arr = PythonNdrUniConformantArray(
                array_type_name, array_member_name
            )
            self.write(arr.to_string())
            self.mapper.add_type(array_type_name)
        return self.python_vardef(var_name=var_def.name, type_name=array_type_name)

    def handle_constant_sized_string(self, var_def: MidlVarDef) -> PythonTuple:
        """Creates a PythonDef for string attributed MidlVarDefs that have a constant size"""

        # Continue implementation ========================================================
        # TODO properly handle these cases. There can be multidimensional arrays of these!
        type_name, _ = self.mapper.get_python_type(var_def.type, is_func_param=self.func_params)
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
        """
        Reference: https://docs.microsoft.com/en-us/windows/win32/midl/midl-arrays

        Handles the following cases:
        UNI : [size_is(m)] short a[]);
        MULTI : [size_is(m)] short b[][20]);

        ## CONFORMANT ARRAYS

        An array is called "conformant" if the upper bound of any dimension is determined at
        runtime. Only upper bounds can be determined at runtime. To determine the upper bound,
        the array declaration must include a size_is or max_is attribute.

        ## VARYING ARRAYS

        An array is called "varying" when its bounds are determined at compile time, but the range
        of transmitted elements is determined at runtime. To determine the range of transmitted
        elements, the array declaration must include a *length_is*, *first_is*, or *last_is*
        attribute.

        """

        # We only handle 1D arrays at present
        dimensionality = len(var_def.array_info)
        if dimensionality != 1:
            raise Exception("Multidimensional arrays are unimplemented")

        lower_bound = self.mapper.calculate_sizeof(var_def.array_info[0].min)
        upper_bound = self.mapper.calculate_sizeof(var_def.array_info[0].max)
        bound = upper_bound or lower_bound

        conformance = None
        variance = None

        # Conformance checks
        if size_is := var_def.attributes.get('size_is'):
            conformance = self.mapper.calculate_sizeof(size_is.params[0])
        elif max_is := var_def.attributes.get('size_is'):
            conformance = self.mapper.calculate_sizeof(max_is.params[0])

        # Variance attributes
        if length_is := var_def.attributes.get('length_is'):
            variance = self.mapper.calculate_sizeof(length_is.params[0])
        else:
            if first_is := var_def.attributes.get('first_is'):
                first_is = self.mapper.calculate_sizeof(first_is.params[0]) 
            if last_is := var_def.attributes.get('last_is'):
                last_is = self.mapper.calculate_sizeof(last_is.params[0]) 

            # Infer the length_is based on first_is and last_is
            if first_is and last_is:
                variance = f"{last_is} - {first_is} + 1"
            elif first_is:
                variance = f"{upper_bound} - {first_is} + 1"
            elif last_is:
                variance = f"{last_is} + 1"

        if upper_bound and lower_bound != "0":
            raise Exception("Microsoft RPC requires a lower bound of zero")

        # Create the array
        if not conformance and not variance:
            # Regular old array
            (
                array_type_name,
                array_member_name,
                array_type_exists,
            ) = self.mapper.get_python_array_type(var_def.type, array_size=lower_bound, is_func_param=self.func_params, array_prefix=UNI_FIXED_PREFIX)
            arr = PythonNdrUniFixedArray(array_type_name, lower_bound, array_member_name)
        elif conformance:
            if variance:
                # Open array (conformant and varying)
                (
                    array_type_name,
                    array_member_name,
                    array_type_exists,
                ) = self.mapper.get_python_array_type(var_def.type, array_size=conformance, is_func_param=self.func_params, array_prefix=UNI_CONFORMANT_VARYING_PREFIX)
                arr = PythonNdrUniConformantVaryingArray(array_type_name, array_member_name)
            else:
                # Conformant array
                (
                    array_type_name,
                    array_member_name,
                    array_type_exists,
                ) = self.mapper.get_python_array_type(var_def.type, array_size=conformance, is_func_param=self.func_params, array_prefix=UNI_CONFORMANT_PREFIX)
                arr = PythonNdrUniConformantArray(array_type_name, array_member_name)
        else:
            # Varying array
            (
                array_type_name,
                array_member_name,
                array_type_exists,
            ) = self.mapper.get_python_array_type(var_def.type, array_size=bound, is_func_param=self.func_params, array_prefix=UNI_VARYING_PREFIX)
            arr = PythonNdrUniVaryingArray(array_type_name, array_member_name)

        if not array_type_exists:
            self.write(arr.to_string())
            self.mapper.add_type(array_type_name)
        return self.python_vardef(var_name=var_def.name, type_name=array_type_name)

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
            ) = self.mapper.get_python_array_type(var_def.type, array_size=size, is_func_param=self.func_params, array_prefix=UNI_CONFORMANT_PREFIX)
            if not array_type_exists:
                arr = PythonNdrUniConformantArray(
                    array_type_name, array_member_name
                )
                self.write(arr.to_string())
                self.mapper.add_type(array_type_name)
            # Create the pointer to the array type:
            pointer_type_name = f"P{array_type_name}"
            pointee_type_name = array_type_name
            if not self.mapper.exists(pointer_type_name):
                ndr_ptr = PythonNdrPointer(
                    name=pointer_type_name,
                    referent_name=pointee_type_name
                )
                self.write(ndr_ptr.to_string())
                self.mapper.add_type(pointer_type_name)
            return_type_name = array_type_name if self.func_params else pointer_type_name
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
            ) = self.mapper.get_python_array_type(var_def.type, array_size=size, is_func_param=self.func_params, array_prefix=UNI_CONFORMANT_PREFIX)
            if not array_type_exists:
                arr = PythonNdrUniConformantArray(
                    array_type_name, array_member_name
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
            return_type_name = array_type_name if self.func_params else pointer_type_name
            return self.python_vardef(var_name=var_def.name, type_name=return_type_name)
        elif dimensionality == SizeIsType.POINTER_TO_SIZED_POINTER_TO_SCALAR:
            raise NotImplementedError(
                f"Unhandled dimensionality {dimensionality} for {var_def}"
            )

        raise Exception(f"Unrecognized dimensionality {dimensionality}")
