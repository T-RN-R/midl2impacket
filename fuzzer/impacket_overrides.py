from impacketbuilder.converters.typing import CONTEXT_HANDLE
import impacket.dcerpc.v5.ndr
import impacket.dcerpc.v5.dtypes

from fuzzer.core import MethodInvocation
from fuzzer.basic import *

"""This file overrides the default impacket classes for the purposes of fuzzing, but still implements the same functionality

Overridden classes:
-NDRSTRUCT
-NDRUNION
-NDR
    -Unless explicitly overriden, this will fallback to a generation function utilizing the `align`
    field to dictate the size of the value to generate
-NDRENUM
-NDRCALL
"""


# NDR overrides
@classmethod
def generate_ndr(cls, ctx=None, range_min=0, range_max=0xFFFFFFFFFFFFFFFF):
    """Hotpatch generation function for NDR impacket classes"""
    v = generate_int(cls.align * 8, range_min, range_max)
    return 0, v


# NDRSTRUCT overrides
class_layout_cache = {}


@classmethod
def generate_ndrstruct(cls, ctx, range_min=0, range_max=256):
    output = ""
    obj_name = cls.__name__
    output += f"{obj_name}()\n"
    inst = cls()
    for member in inst.structure:
        name, type_ = member
        entry = f"{ctx}['{name}']"
        if isinstance(type_, str):
            # TODO: parse the packing strings in impacket
            continue
        output += entry + " = " + str(type_.generate(f"{entry}")[1]) + "\n"

    return None, output


@classmethod
def is_context_handle(cls):
    if hasattr(cls, 'is_ctx_handle'):
        is_ctx = getattr(cls,"is_ctx_handle")
        if is_ctx: # shortcut for idl defined handles
            return True
    inst = cls()
    for member in inst.structure:
        name, type_ = member
        if name == "Data" and isinstance(type_, str):
            return True
    return False


@classmethod
def get_child_fields_of_type(cls, type_info, ident=""):
    """Builds a lookup path to get object of given type from the struct"""
    try:
        if cls.class_layout_cache == {}:
            pass
    except AttributeError:
        cls.class_layout_cache = {}

    if type_info in cls.class_layout_cache:
        # Cache this operation because it is expensive
        return cls.class_layout_cache[type_info]

    types = []
    inst = cls()
    for m in inst.structure:
        name, type_ = m
        if isinstance(type_, str):
            continue
        if issubclass(type_, impacket.dcerpc.v5.ndr.NDRSTRUCT):
            types += cls.get_child_fields_of_type(type_info, ident + "['" + name + "']")
        else:
            if type_ == type_info:
                types.append(ident + "['" + name + "']")

    cls.class_layout_cache[type_info] = types
    return types


# NDRUNION overrides
@classmethod
def generate_ndrunion(cls, ctx, range_min=0, range_max=256):
    inst = cls()
    kind = random.choice(inst.union.keys())
    output = f"{cls.__name__}()\n"
    name, type_ = inst.union[kind]
    entry = f"{ctx}['{name}']\n"
    output += entry + " = " + str(type_.generate(f"{entry}")[1]) + "\n"
    return 0, output


# NDRCALL overrides
@classmethod
def generate_ndrcall(cls, testcase, fuzzer):
    """Generates an invocation of the testcase

    Args:
        testcase ([type]): testcase object to append to
    """
    args = cls.get_arguments(testcase, fuzzer)
    resp_name = fuzzer.get_var_name()
    cls.add_out_args(resp_name, fuzzer)
    return MethodInvocation(str(cls.__name__), args, resp_name)


@classmethod
def get_arguments(cls, testcase, fuzzer):
    """Generates the arguments to the function"""
    out_args = {}
    inst = cls()
    for arg in inst.structure:
        name, type_ = arg
        out_args[name] = fuzzer.get_of_type(testcase, type_)
    return out_args


@classmethod
def add_out_args(cls, resp, fuzzer):
    inst = cls()
    for arg in inst.structure:
        name, type_ = arg
        fuzzer.lookup_mapper.insert(type_, f"{resp}['{name}']")


@classmethod
def generate_ndrpointer(cls, ctx, range_min=0, range_max=256):
    ref = cls.referent
    assert len(ref) == 1, "Cannot handle referents longer than 1!"
    name, type_ = ref[0]
    assert name == "Data", "Encountered a referent without a 'Data' entry!"
    if (
        type_ == ":"
    ):  # Check to make sure we aren't falling back to the NDRPOINTER defintion for referent
        ref = cls().referent
        assert len(ref) == 1, "Cannot handle referents longer than 1!"
        name, type_ = ref[0]
        assert name == "Data", "Encountered a referent without a 'Data' entry!"
    return type_.generate(ctx, range_min, range_max)


@classmethod
def generate_todo(cls, ctx, range_min=0, range_max=256):
    return 0, f"None # TODO {cls.__name__}"


@classmethod
def generate_wstr_impl(cls, ctx, range_min=0, range_max=256):
    return 0, f"{generate_str(wide=True, range_min=range_min, range_max=range_max)}"


@classmethod
def generate_str_impl(cls, ctx, range_min=0, range_max=256):
    return 0, f"{generate_str(wide=False, range_min=range_min, range_max=range_max)}"


@classmethod
def generate_ndruniconformantarray(cls, ctx, range_min=0, range_max=256):
    #TODO determine some way of getting the PROPER min/max sizes here...
    inner_type = cls.item
    if isinstance(inner_type, str):
        inner_type = cls().item
    output = f"{cls.__name__}()\n"
    for _ in range(range_min, random.randint(range_min,range_max)):
        output += f"{ctx}.append({inner_type.generate(ctx)[1]})\n"
    return 0, output


# Apply hotpatches
# Primitive NDR overrides
setattr(impacket.dcerpc.v5.ndr.NDRSMALL, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRUSMALL, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRBOOLEAN, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRCHAR, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRSHORT, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRUSHORT, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRLONG, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRULONG, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRHYPER, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRUHYPER, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRFLOAT, "generate", generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRDOUBLEFLOAT, "generate", generate_ndr)

# Problematic dtype overrides
setattr(impacket.dcerpc.v5.dtypes.WSTR, "generate", generate_wstr_impl)
setattr(impacket.dcerpc.v5.dtypes.STR, "generate", generate_str_impl)

# NDRSTRUCT overrides
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, "class_layout_cache", class_layout_cache)
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, "generate", generate_ndrstruct)
setattr(
    impacket.dcerpc.v5.ndr.NDRSTRUCT,
    "get_child_fields_of_type",
    get_child_fields_of_type,
)
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, "is_context_handle", is_context_handle)

# NDRUNION
setattr(impacket.dcerpc.v5.ndr.NDRUNION, "generate", generate_ndrunion)

# NDRCALL
setattr(impacket.dcerpc.v5.ndr.NDRCALL, "generate", generate_ndrcall)
setattr(impacket.dcerpc.v5.ndr.NDRCALL, "get_arguments", get_arguments)
setattr(impacket.dcerpc.v5.ndr.NDRCALL, "add_out_args", add_out_args)

# NDRPOINTER
setattr(impacket.dcerpc.v5.ndr.NDRPOINTER, "generate", generate_ndrpointer)


# NDUniConformantArray
setattr(
    impacket.dcerpc.v5.ndr.NDRUniConformantArray,
    "generate",
    generate_ndruniconformantarray,
)
# TODO, unimplemented:s
setattr(impacket.dcerpc.v5.ndr.NDRUniConformantVaryingArray, "generate", generate_todo)
setattr(impacket.dcerpc.v5.ndr.NDRUniFixedArray, "generate", generate_todo)
setattr(impacket.dcerpc.v5.ndr.NDRUniVaryingArray, "generate", generate_todo)
