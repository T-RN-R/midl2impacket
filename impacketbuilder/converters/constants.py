from .base import *
from midl import *

class MidlConstantConverter(Converter):
    SIZEOF_LOOKUP = {
                    "WCHAR":4,
                    "BOOL":1,
                    "UINT32":2,
                    "UINT64":4,
                    "GUID":16
                    }
    def convert(self,constant : MidlVariableInstantiation):
        rhs = constant.rhs
        while "sizeof" in rhs: # eliminate all sizeofs!
            rhs = self.calculate_sizeof(rhs)
        const = f"{self.mapper.canonicalize(constant.name)} = {rhs}"
        self.write(const)

    def calculate_sizeof(self,rhs):
        so_idx = rhs.index("sizeof")
        lb_idx = rhs.index("(")
        rb_idx = rhs.index(")")
        type_str = rhs[lb_idx+1:rb_idx].strip()
        if type_str not in MidlConstantConverter.SIZEOF_LOOKUP:
            raise ConversionException(f"Could not get sizeof({type_str})")
        return rhs[:so_idx] + str(MidlConstantConverter.SIZEOF_LOOKUP[type_str]) + rhs[rb_idx+1:]
