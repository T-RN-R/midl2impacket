from fuzzer.base import FuzzableMidl
from fuzzer.generators.basic import *

############################
## Procedure generator definition classes
###########################
class InOutParameter(FuzzableMidl):
    def __init__(self, param, *ignored):
        self.param = param


class InOut(InOutParameter):
    pass


class In(InOutParameter):
    pass


class Out(InOutParameter):
    pass


class Procedure(FuzzableMidl):
    def __init__(self, *parameters, **kwargs):
        for param in parameters:
            if isinstance(param, In):
                self.add_input(param)
            elif isinstance(param, Out):
                self.add_output(param)
            elif isinstance(param, InOut):
                self.add_input(param)
                self.add_output(param)
            else:
                raise Exception("UNREACHABLE")

    def add_input(self, param):
        pass

    def add_output(self, param):
        pass


##########################################
## NDR generator type definition classes
##########################################
class NdrType(FuzzableMidl):
    pass


class NdrByte(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        v = generate_int(8, range_min, range_max)
        return v


NdrSmall = NdrByte


class NdrShort(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        v = generate_int(16, range_min, range_max)
        return 0, v


NdrWChar = NdrShort


class NdrLong(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        v = generate_int(32, range_min, range_max)
        return 0, v


class NdrHyper(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        v = generate_int(64, range_min, range_max)
        return 0, v


class NdrCString(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        s = generate_str(False, range_min, range_max)
        return len(s), s


class NdrWString(NdrType):
    @classmethod
    def generate(cls, ctx, range_min, range_max):
        s = generate_str(True, range_min, range_max)
        return len(s) // 2, s


class NdrUnion:
    MEMBERS = {}
    SWITCHTYPE = {}

    @classmethod
    def generate(cls):
        key = "default"
        while key == "default":
            key = random.choice(cls.MEMBERS.keys())
        return key, cls.MEMBERS[key]

    @classmethod
    def pack(cls, tag, data):
        return cls.SWITCHTYPE.pack(tag) + data


class NdrStructure:
    pass
