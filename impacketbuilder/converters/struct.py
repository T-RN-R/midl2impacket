from .base import ConversionException, Converter
from midltypes import *
from .vardef import VarDefConverter
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

        tag: MidlAttribute
        if tag := struct.attributes.get("switch_type"):
            tag = tag.params[0].upper()

        count = 1
        entries = []
        for m in struct.members:
            # VarDefConverter(self.io,self.tab_level,self.mapper).convert(m)
            key = None
            if m.attributes:
                if "case" in m.attributes:
                    key = m.attributes["case"].params[0]
            type_name = None
            if isinstance(m.type, str):
                type_name = m.type
            elif isinstance(m.type, MidlStructDef):
                type_name = m.type.public_names[0]
                self.convert(m.type)
            elif isinstance(m.type, MidlUnionDef):
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
                    self.write(
                        PythonAssignment(
                            PythonName(self.mapper.canonicalize(pn)),
                            PythonValue(base_name),
                        )
                    )
                else:
                    raise ConversionException(
                        "Multiple asterisks encountered in name: {pn}"
                    )
        return name

    def create_ndr_uni_fixed_array_class(self, name, length):
        uni_arr = PythonNdrUniFixedArray(name=name, length=length)
        self.write(uni_arr.to_string())

    def handle_ndr_struct(self, struct):
        struct_entries = []
        for var_def in struct.members:
            type_name = None
            if isinstance(var_def.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                if type_name is None:
                    type_name = self.convert(var_def.type)
                var_def.type = type_name
            elif isinstance(var_def.type, str):
                if type_name is None:
                    type_name = var_def.type

            p_vd = VarDefConverter(self.io, self.tab_level, self.mapper).convert(
                var_def
            )
            struct_entries.append(p_vd)

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
                    self.write(
                        PythonAssignment(
                            PythonName(self.mapper.canonicalize(pn)),
                            PythonValue(base_name),
                        )
                    )
                else:
                    raise ConversionException(
                        "Multiple asterisks encountered in name: {pn}"
                    )

        return base_name

    def handle_ndr_array(self, struct):
        # First step: Find the count and the array variables
        arr_var = None
        main_name = struct.public_names[0]
        for vd in struct.members:
            for attr_name in vd.attributes:
                if attr_name == "size_is":
                    arr_var = vd

        struct_entries = []
        for vd in struct.members:
            if vd is arr_var:
                struct_entries.append(
                    PythonTuple(
                        [
                            PythonValue(f"'{arr_var.name}'"),
                            PythonValue(f"PTR_{self.mapper.canonicalize(main_name)}"),
                        ]
                    )
                )
            else:
                name = None
                if isinstance(vd.type, str):
                    name = vd.type
                else:
                    name = vd.type.public_names[0]

                struct_entries.append(
                    PythonTuple(
                        [
                            PythonValue(f"'{vd.name}'"),
                            PythonValue(f"{self.mapper.canonicalize(name)}"),
                        ]
                    )
                )

        underlying_type = arr_var.type.replace("*", "")
        main_name = self.mapper.canonicalize(main_name)

        struct_tuple = PythonTuple(struct_entries)
        ndr_array = PythonNdrUniConformantArray(
            name=f"DATA_{main_name}",
            underlying_type_name=self.mapper.canonicalize(underlying_type),
        )
        ndr_ptr = PythonNdrPointer(
            name=f"PTR_{main_name}", referent_name=f"DATA_{main_name}"
        )
        ndr_struct = PythonNdrStruct(name=main_name, structure=struct_tuple)

        self.write(ndr_array.to_string())
        self.write(ndr_ptr.to_string())
        self.write(ndr_struct.to_string())
        # Now handle the cases where there are multiple public names, including pointers
        base_name = main_name
        if len(struct.public_names) > 1:
            for pn in struct.public_names[1:]:
                star_count = pn.count("*")
                if star_count == 1:
                    ndr_ptr = PythonNdrPointer(
                        name=self.mapper.canonicalize(pn), referent_name=base_name
                    )
                    self.write(ndr_ptr.to_string())
                elif star_count == 0:
                    self.write(
                        PythonAssignment(
                            PythonName(self.mapper.canonicalize(pn)),
                            PythonValue(base_name),
                        )
                    )
                else:
                    raise ConversionException(
                        "Multiple asterisks encountered in name: {pn}"
                    )
        return name

    def detect_ndr_type(self, struct):
        if isinstance(struct, MidlUnionDef):
            return MidlStructConverter.NDR_UNION
        for vd in struct.members:
            t = vd.type
            if isinstance(t, str):  # We can have MidlUnionDefs here!!!
                if (
                    "*" in t and "size_is" in vd.attributes
                ):  # if there is a pointer, assume its an array
                    # TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT
