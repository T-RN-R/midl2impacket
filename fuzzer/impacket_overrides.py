import impacket.dcerpc.v5.ndr 

from fuzzer.basic import *

"""This file overrides the default impacket classes for the purposes of fuzzing, but still implements the same functionality

Overridden classes:
-NDRSTRUCT
-NDRUNION
-NDR
    -Unless explicitly overriden, this will fallback to a generation function utilizing the `align`
    field to dictate the size of the value to generate


New classes:
-NDRENUM

"""

class NDR(impacket.dcerpc.v5.ndr.NDR):
    @classmethod
    def generate(cls, ctx, range_min=0, range_max=0xFFFFFFFFFFFFFFFF):
        v = generate_int(cls.align*8, range_min, range_max)
        return 0, v