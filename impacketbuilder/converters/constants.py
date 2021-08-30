from impacketbuilder.ndrbuilder.base import PythonValue
from midltypes import MidlVariableInstantiation
from .base import Converter, ConversionException
from impacketbuilder.ndrbuilder.python import PythonAssignment, PythonValue, PythonName


class MidlConstantConverter(Converter):
    SIZEOF_LOOKUP = {"WCHAR": 4, "BOOL": 1, "UINT32": 2, "UINT64": 4, "GUID": 16}

    def convert(self, constant: MidlVariableInstantiation):
        rhs = constant.rhs
        while "sizeof" in rhs:  # eliminate all sizeofs!
            rhs = self.calculate_sizeof(rhs)
        type_name, type_exists = self.mapper.get_python_type(constant.name)
        if not type_exists:
            const = PythonAssignment(PythonName(type_name), PythonValue(rhs))
        self.write(const)

    def calculate_sizeof(self, rhs):
        so_idx = rhs.index("sizeof")
        lb_idx = rhs.index("(")
        rb_idx = rhs.index(")")
        type_str = rhs[lb_idx + 1 : rb_idx].strip()
        if type_str not in MidlConstantConverter.SIZEOF_LOOKUP:
            raise ConversionException(f"Could not get sizeof({type_str})")
        return (
            rhs[:so_idx]
            + str(MidlConstantConverter.SIZEOF_LOOKUP[type_str])
            + rhs[rb_idx + 1 :]
        )
