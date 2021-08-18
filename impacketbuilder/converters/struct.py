from .base import ConversionException, Converter
from midltypes import *

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


class MidlStructConverter(Converter):
    NDR_ARRAY = 0x1
    NDR_POINTER = 0x2
    NDR_STRUCT = 0x3
    NDR_UNION = 0x4
    Anonymous_Count = 0

    def get_anonymous_name(self):
        __class__.Anonymous_Count += 1
        return "Anonymous" + str(__class__.Anonymous_Count)

    def convert(self, struct):
        ndr_type = self.detect_ndr_type(struct)
        if ndr_type is MidlStructConverter.NDR_ARRAY:
            return self.handle_ndr_array(struct)
        elif ndr_type is MidlStructConverter.NDR_STRUCT:
            return self.handle_ndr_struct(struct)
        elif ndr_type is MidlStructConverter.NDR_UNION:
            return self.handle_ndr_union(struct)
        else:
            raise Exception("NDR_POINTER unimplemented")

    def handle_ndr_union(self, struct):
        if len(struct.public_names) > 0:
            if struct.public_names[0] == "":
                name = self.get_anonymous_name()
            else:
                name = struct.public_names[0]
        else:
            name = self.get_anonymous_name()

        tag:MidlAttribute
        if tag := struct.attributes.get('switch_type'):
            tag = tag.params[0].upper()

        count = 1
        entries = []
        for m in struct.members:
            key = None
            if m.attributes:
                if "case" in m.attributes.keys():
                    key = m.attributes["case"].params[0]
            type_name = None
            if type(m.type) is str:
                type_name = m.type
            elif type(m.type) is MidlStructDef:
                type_name = m.type.public_names[0]
                self.convert(m.type)
            elif type(m.type) is MidlUnionDef:
                type_name = m.type.public_names[0]
                self.convert(m.type)
            elif m.type is None:
                continue
            else:
                raise Exception(f"Unexpected type: {type(m.type)}")
            if key is None:
                key = count
            entries.append(
                PythonDictEntry(
                    key=PythonValue(key),
                    value=PythonTuple(
                        [
                            PythonValue(f"'{m.name}'"),
                            PythonValue(self.mapper.canonicalize(type_name)),
                        ]
                    ),
                )
            )
            count += 1
        base_name = self.mapper.canonicalize(name)
        dentries = PythonDictEntryList(*entries)
        union_def = PythonNdrUnion(name=base_name, union_entries=dentries, tag=tag)
        self.write(union_def.to_string())

        # Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for pn in struct.public_names[1:]:
                star_count = pn.count("*")
                if star_count == 1:
                    ndr_ptr = PythonNdrPointer(
                        name=self.mapper.canonicalize(pn), referent_name=base_name
                    )
                    self.write(ndr_ptr.to_string())
                elif star_count == 0:
                    self.write(PythonAssignment(PythonName(pn), PythonValue(base_name)))
                else:
                    raise ConversionException(
                        "Multiple asterisks encountered in name: {pn}"
                    )
        return name
    def create_ndr_uni_fixed_array_class(self, name, length):
        uni_arr = PythonNdrUniFixedArray(name=name,length=length)
        self.write(uni_arr.to_string())

    def handle_ndr_struct(self, struct):
        struct_entries = []
        for vd in struct.members:
            type_name = None
            if type(vd.type) is MidlUnionDef or type(vd.type) is MidlStructDef:
                # handle nested unions/structs
                if type_name is None:
                    type_name = self.convert(vd.type)
                vd.name = type_name
            elif type(vd.type) is str:
                if type_name is None:
                    type_name = vd.type
            if len(vd.array_info) > 0:
                if len(vd.array_info) == 1:
                    arr_inf = vd.array_info[0]
                    if arr_inf.min != -1  and arr_inf.max == -1:
                        #NDRUniFixedArrays
                        if type(arr_inf.min) == str:
                            size = self.mapper.calculate_sizeof(arr_inf.min)
                        else:
                            size = arr_inf.min
                        type_name = f"ARR_{self.mapper.canonicalize(type_name)}"
                        self.create_ndr_uni_fixed_array_class(type_name, size)
                    else:
                        # NDRUniConformantArrays
                        array_item_name = type_name
                        if type(arr_inf.max) == str:
                            size = self.mapper.calculate_sizeof(arr_inf.max)
                        else:
                            size = arr_inf.max
                        type_name = f"{self.mapper.canonicalize(array_item_name)}_ARRAY"
                        arr = PythonNdrUniConformantArray(type_name, f"{self.mapper.canonicalize(array_item_name)}", size)
                        self.write(arr.to_string())
                else:
                    #TODO handle multidimensional arrays here
                    raise Exception("Multi-dimensional arrays are unhandled")

            struct_entries.append(
                PythonTuple(
                    [
                        PythonValue(f"'{vd.name}'"),
                        PythonValue(self.mapper.canonicalize(type_name)),
                    ]
                )
            )

        struct_tuple = PythonTuple(struct_entries)

        if len(struct.public_names) > 0:
            base_name = self.mapper.canonicalize(struct.public_names[0])
        else:
            base_name = self.get_anonymous_name()

        ndr_class = PythonNdrStruct(name=base_name, structure=struct_tuple)
        self.write(ndr_class.to_string())

        # Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for pn in struct.public_names[1:]:
                star_count = pn.count("*")
                if star_count == 1:
                    ndr_ptr = PythonNdrPointer(
                        name=self.mapper.canonicalize(pn), referent_name=base_name
                    )
                    self.write(ndr_ptr.to_string())
                elif star_count == 0:
                    self.write(PythonAssignment(PythonName(pn), PythonValue(base_name)))
                else:
                    raise ConversionException(
                        "Multiple asterisks encountered in name: {pn}"
                    )

        return base_name

    def handle_ndr_array(self, struct):
        # First step: Find the count and the array variables
        count_name = None
        arr_var = None
        main_name = struct.public_names[0]
        for vd in struct.members:
            for attr_name in vd.attributes:
                if attr_name == "size_is":
                    arr_var = vd
                    count_name = vd.attributes[attr_name].params[0]
        for vd in struct.members:
            if vd.name == count_name:
                count_var = vd

        struct_entries = []
        for vd in struct.members:
            if vd is arr_var:
                struct_entries.append(PythonTuple([PythonValue(f"'{arr_var.name}'"),PythonValue(f"PTR_{self.mapper.canonicalize(main_name)}")]))
            else:
                name = None
                if type(vd.type) is str:
                    name = vd.type
                else:
                    name = vd.type.public_names[0]

                struct_entries.append(PythonTuple([PythonValue(f"'{vd.name}'"),PythonValue(f"{self.mapper.canonicalize(name)}")]))

        underlying_type = arr_var.type.replace("*", "")
        main_name = self.mapper.canonicalize(main_name)

        struct_tuple = PythonTuple(struct_entries)
        ndr_array = PythonNdrUniConformantArray(
            name=f"DATA_{main_name}",
            underlying_type_name=self.mapper.canonicalize(underlying_type),
        )
        ndr_ptr = PythonNdrPointer(name=f"PTR_{main_name}", referent_name=f"DATA_{main_name}")
        ndr_struct = PythonNdrStruct(name = main_name, structure=struct_tuple)

        self.write(ndr_array.to_string())
        self.write(ndr_ptr.to_string())
        self.write(ndr_struct.to_string())
        return name

    def detect_ndr_type(self, struct):
        if type(struct) is MidlUnionDef:
            return MidlStructConverter.NDR_UNION
        types = [vd.type for vd in struct.members]
        for vd in struct.members:
            t = vd.type
            if type(t) is str:  # We can have MidlUnionDefs here!!!
                if (
                    "*" in t and "size_is" in vd.attributes
                ):  # if there is a pointer, assume its an array
                    # TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT
