from fuzzer.base import FuzzableMidl
from fuzzer.basic import *


"""Defines class used to build generator templates."""


############################
## Procedure generator definition classes
###########################
class InOutParameter(FuzzableMidl):
    """Parent class of Midl Procedure parameters"""

    def __init__(self, param, *ignored):
        self.param = param

    def generate(self):
        pass
class InOut(InOutParameter):
    """Represents an In/Out parameter"""


class In(InOutParameter):
    """Represents an In parameter"""


class Out(InOutParameter):
    """Represents an Out parameter"""


##########################################
## NDR generator type definition classes
##########################################
class NdrType(FuzzableMidl):
    pass

class NdrBoolean(NdrType):
    pass
class NdrByte(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFF):
        v = generate_int(8, range_min, range_max)
        return 0, v


NdrSmall = NdrByte


class NdrShort(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFF):
        v = generate_int(16, range_min, range_max)
        return 0, v


NdrWChar = NdrShort


class NdrLong(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFFFFFF):
        v = generate_int(32, range_min, range_max)
        return 0, v
class NdrDouble(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFFFFFFFFFFFFFF):
        v = generate_int(32, range_min, range_max)
        return 0, v
class NdrFloat(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFFFFFF):
        v = generate_int(32, range_min, range_max)
        return 0, v

class NdrHyper(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFFFFFFFFFFFFFF):
        v = generate_int(64, range_min, range_max)
        return 0, v


class NdrCString(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=256):
        s = generate_str(False, range_min, range_max)
        return len(s), s


class NdrWString(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=256):
        s = generate_str(True, range_min, range_max)
        return len(s) // 2, s


class NdrUnion:
    MEMBERS = {}
    SWITCHTYPE = {}

    @classmethod
    def generate(cls, ctx, range_min=0, range_max=256):
        return None,"None"
        key = "default"
        while key == "default":
            key = random.choice(cls.MEMBERS.keys())
        return key, cls.MEMBERS[key]

    @classmethod
    def pack(cls, tag, data):
        return cls.SWITCHTYPE.pack(tag) + data


class NdrStructure:
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=256):
        output = ""
        obj_name = cls.__name__
        output+=f"{obj_name}()\n"
        for member in cls.MEMBERS:
            entry = f"{ctx}['{member[1]}']"
            output+= entry +" = " + str(member[0].generate(f'"{entry}"')[1]) + "\n"

        return None,output


class NdrEnum:
    pass


class NdrContextHandle(NdrType):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=256):
        return None,"None"
