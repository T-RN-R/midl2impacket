import impacket.dcerpc.v5.ndr 
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

New classes:
-NDRINTERFACE

"""



# NDR overrides
def generate_ndr(cls, ctx, range_min=0, range_max=0xFFFFFFFFFFFFFFFF):
    """Hotpatch generation function for NDR impacket class
    """
    v = generate_int(cls.align*8, range_min, range_max)
    return 0, v

# NDRSTRUCT overrides
class_layout_cache = {}
@classmethod
def generate_ndrstruct(cls, ctx, range_min=0, range_max=256):
    output = ""
    obj_name = cls.__name__
    output+=f"{obj_name}()\n"
    for member in cls.structure:
        name, type_ = member
        entry = f"{ctx}['{name}']"
        output+= entry +" = " + str(type_.generate(f'{entry}')[1]) + "\n"

    return None,output
@classmethod
def get_child_fields_of_type(cls, type_info, ident=""):
    """Builds a lookup path to get object of given type from the struct"""
    try:
        if cls.class_layout_cache == {}:
            pass
    except AttributeError:
        cls.class_layout_cache = {}

    if type_info in cls.class_layout_cache:
        #Cache this operation because it is expensive
        return cls.class_layout_cache[type_info]

    types = []
    for m in cls.structure:
        name, type_ = m
        if issubclass(type_, impacket.dcerpc.v5.ndr.NDRSTRUCT):
            types += cls.get_child_fields_of_type(type_info,ident+"['"+name+"']")
        else:
            if type_ == type_info:
                types.append(ident+"['"+name+"']")

    cls.class_layout_cache[type_info] = types
    return types


# NDRUNION overrides
@classmethod
def generate_ndrunion(cls, ctx, range_min=0, range_max=256):
    return ""

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
    return MethodInvocation(cls.__class__, args, resp_name)

@classmethod
def get_arguments(cls, testcase, fuzzer):
    """Generates the arguments to the function"""
    out_args = {}
    for arg in cls.structure:
        name, type_ = arg
        out_args[name] = fuzzer.get_of_type(testcase, type_)
    return out_args
    
@classmethod
def add_out_args(cls,resp,fuzzer):
    for arg in cls.structure:
        name, type_ = arg
        fuzzer.lookup_mapper.insert(type_, f"{resp}['{name}']")


#python __str__ overrides :/ *spooky_face.exe.gif*
def generate_ndrstr(self, ctx, range_min=0, range_max=256):
    return self
#Apply hotpatches
setattr(str, 'generate', generate_ndrstr)

setattr(impacket.dcerpc.v5.ndr.NDR, 'generate', generate_ndr)
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, 'class_layout_cache', class_layout_cache)
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, 'generate', generate_ndrstruct)
setattr(impacket.dcerpc.v5.ndr.NDRSTRUCT, 'get_child_fields_of_type', get_child_fields_of_type)
setattr(impacket.dcerpc.v5.ndr.NDRUNION, 'generate', generate_ndrunion)
setattr(impacket.dcerpc.v5.ndr.NDRCALL, 'generate', generate_ndrcall)
setattr(impacket.dcerpc.v5.ndr.NDRCALL, 'get_arguments', get_arguments)
setattr(impacket.dcerpc.v5.ndr.NDRCALL, 'add_out_args', add_out_args)

