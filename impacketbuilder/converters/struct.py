from midlparser.parsers import attributes
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
        
        name = struct.name

        tag: MidlAttribute
        if tag := struct.attributes.get("switch_type"):
            tag = tag.params[0].upper()
        elif  tag := struct.attributes.get("switch_is"):
            tag = tag.params[0].upper()

        count = 1
        entries = []
        for struct_member in struct.members:
            # VarDefConverter(self.io,self.tab_level,self.mapper).convert(m)
            key = None
            if struct_member.attributes:
                if "case" in struct_member.attributes:
                    key = struct_member.attributes["case"].params[0]
            type_name = None
            if isinstance(struct_member.type, str):
                type_name = struct_member.type
            elif isinstance(struct_member.type, MidlStructDef):
                type_name = struct_member.type.name
                self.convert(struct_member.type)
            elif isinstance(struct_member.type, MidlUnionDef):
                type_name = struct_member.type.name
                self.convert(struct_member.type)
            elif isinstance(struct_member.type, MidlPointerType):
                type_name = struct_member.type.pointee + '*'
            elif struct_member.type is None:
                continue
            else:
                raise Exception(f"Unexpected type: {type(struct_member.type)}")
            if key is None:
                key = count
            type_name = self.mapper.get_python_type(type_name)[0]
            entries.append(
                PythonDictEntry(
                    key=PythonValue(key),
                    value=PythonTuple(
                        [
                            PythonValue(f"'{struct_member.name}'"),
                            PythonValue(type_name),
                        ]
                    ),
                )
            )
            count += 1
        base_name, base_exists = self.mapper.get_python_type(name)
        dentries = PythonDictEntryList(*entries)
        if not base_exists:
            union_def = PythonNdrUnion(name=base_name, union_entries=dentries, tag=tag)
            self.write(union_def.to_string())
            self.mapper.add_type(base_name, struct)
        return name

    def handle_ndr_struct(self, struct):
        struct_entries = []
        for var_def in struct.members:
            if isinstance(var_def.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                var_def.type = self.convert(var_def.type)

            p_vd = VarDefConverter(self.io, self.tab_level, self.mapper).convert(
                var_def
            )
            struct_entries.append(p_vd)

        struct_tuple = PythonTuple(struct_entries)

        base_name = struct.name

        struct_size = self.mapper.calculate_sizeof(struct)
        ndr_class = PythonNdrStruct(name=base_name, structure=struct_tuple, size=struct_size)
        self.write(ndr_class.to_string())
        self.mapper.add_type(base_name, struct)

        return base_name

    def handle_ndr_array(self, struct: MidlStructDef):
        # First step: Find the count and the array variables
        arr_var = None
        main_name = struct.name
        for var_def in struct.members:
            for attr_name in var_def.attributes:
                if attr_name == "size_is":
                    arr_var = var_def

        struct_entries = []
        for var_def in struct.members:
            if isinstance(var_def.type, (MidlStructDef, MidlUnionDef)):
                # nested unions/structs
                var_def.type = self.convert(var_def.type)
            p_vd = VarDefConverter(self.io, self.tab_level, self.mapper).convert(
                var_def
            )
            struct_entries.append(p_vd)

        underlying_type = arr_var.type.replace("*", "")
        main_name = self.mapper.get_python_type(main_name)[0]

        struct_tuple = PythonTuple(struct_entries)
        array_name = f"{main_name}_ARRAY"
        array_member_name = self.mapper.get_python_type(underlying_type)[0]
        array_pointer_name = f"P{array_name}"

        ndr_array = PythonNdrUniConformantArray(
            name=array_name,
            underlying_type_name=array_member_name,
        )
        ndr_ptr = PythonNdrPointer(
            name=array_pointer_name, referent_name=array_name
        )
        ndr_struct = PythonNdrStruct(name=main_name, structure=struct_tuple)

        self.write(ndr_array.to_string())
        self.mapper.add_type(array_name, None)

        self.write(ndr_ptr.to_string())
        self.mapper.add_type(array_name, MidlPointerType(array_pointer_name, array_name))

        self.write(ndr_struct.to_string())
        self.mapper.add_type(main_name, struct)

        return main_name

    def detect_ndr_type(self, struct):
        if isinstance(struct, MidlUnionDef):
            return MidlStructConverter.NDR_UNION
        for var_def in struct.members:
            var_type = var_def.type
            if isinstance(var_type, str):  # We can have MidlUnionDefs here!!!
                if (
                    "*" in var_type and "size_is" in var_def.attributes
                ):  # if there is a pointer, assume its an array
                    # TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT
