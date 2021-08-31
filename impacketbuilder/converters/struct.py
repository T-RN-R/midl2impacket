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

    def convert(self, struct, parent_struct=None):
        ndr_type = self.detect_ndr_type(struct)
        if ndr_type is MidlStructConverter.NDR_ARRAY:
            return self.handle_ndr_array(struct)
        elif ndr_type is MidlStructConverter.NDR_STRUCT:
            return self.handle_ndr_struct(struct)
        elif ndr_type is MidlStructConverter.NDR_UNION:
            return self.handle_ndr_union(struct, parent_struct)
        else:
            raise Exception("NDR_POINTER unimplemented")

    def handle_ndr_union(self, struct, parent_struct):
        """Create the Python definition for an NDRUnion
        """
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
            #TODO  switch_type can be an expression
        elif  tag := struct.attributes.get("switch_is"):
            tag = tag.params[0].upper() 
            #tag is now the switch_is parameter
            
            #lookup the variable name in the struct creating this union, and make that variable's type the tag name
            assert(parent_struct!=None), "Must pass in parent_struct!"
            new_tag = None
            for member in parent_struct.members:
                name = member.name
                if name == tag:
                    new_tag = member.type
                    assert(isinstance(tag,str)), "Handle cases where the union tag object is non-str(most likely VarDef)"
                    break
            if new_tag != None: tag = new_tag
            else: tag = "DWORD" #default to DWORD type
            
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
                type_name = struct_member.type.public_names[0]
                self.convert(struct_member.type, struct)
            elif isinstance(struct_member.type, MidlUnionDef):
                type_name = struct_member.type.public_names[0]
                self.convert(struct_member.type, struct)
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

        # Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for public_name in struct.public_names[1:]:
                star_count = public_name.count("*")
                if star_count == 1:
                    pointer_name = self.mapper.get_python_type(public_name[1:])[0]
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_name, referent_name=base_name
                    )
                    self.write(ndr_ptr.to_string())
                    self.mapper.add_type(pointer_name)
                elif star_count == 0:
                    alias_name = self.mapper.get_python_type(public_name)[0]
                    self.write(
                        PythonAssignment(
                            PythonName(alias_name),
                            PythonValue(base_name),
                        )
                    )
                    self.mapper.add_type(alias_name)
                else:
                    raise ConversionException(
                        f"Multiple asterisks encountered in name: {public_name}"
                    )
        return name

    def handle_ndr_struct(self, struct):
        """Create the Python definition for an NDRUnion"""
        struct_entries = []
        for var_def in struct.members:
            if isinstance(var_def.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                var_def.type = self.convert(var_def.type,struct)

            p_vd = VarDefConverter(self.io, self.tab_level, self.mapper).convert(
                var_def
            )
            struct_entries.append(p_vd)

        struct_tuple = PythonTuple(struct_entries)

        if len(struct.public_names) > 0:
            # If the first name is a pointer type, use the private name as the public one
            if struct.public_names[0].startswith('*'):
                struct.public_names.insert(0, struct.private_name)
            base_name = self.mapper.get_python_type(struct.public_names[0])[0]
        else:
            base_name = self.get_anonymous_name()

        ndr_class = PythonNdrStruct(name=base_name, structure=struct_tuple)
        self.write(ndr_class.to_string())

        # Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for public_name in struct.public_names[1:]:
                star_count = public_name.count("*")
                if star_count == 1:
                    pointer_name = self.mapper.get_python_type(public_name[1:])[0]
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_name, referent_name=base_name
                    )
                    self.write(ndr_ptr.to_string())
                    self.mapper.add_type(pointer_name)
                elif star_count == 0:
                    alias_name = self.mapper.get_python_type(public_name)[0]
                    self.write(
                        PythonAssignment(
                            PythonName(alias_name),
                            PythonValue(base_name),
                        )
                    )
                    self.mapper.add_type(alias_name)
                else:
                    raise ConversionException(
                        f"Multiple asterisks encountered in name: {public_name}"
                    )

        return base_name

    def handle_ndr_array(self, struct: MidlStructDef):
        """Create the Python defintion for an NDR Array"""
        # First step: Find the count and the array variables
        arr_var = None
        main_name = struct.public_names[0]
        for var_def in struct.members:
            for attr_name in var_def.attributes:
                if attr_name == "size_is":
                    arr_var = var_def

        struct_entries = []
        for var_def in struct.members:
            if isinstance(var_def.type, (MidlStructDef, MidlUnionDef)):
                # nested unions/structs
                var_def.type = self.convert(var_def.type,struct)
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
            underlying_type=array_member_name,
        )
        ndr_ptr = PythonNdrPointer(
            name=array_pointer_name, referent_name=array_name
        )
        ndr_struct = PythonNdrStruct(name=main_name, structure=struct_tuple)

        self.write(ndr_array.to_string())
        self.write(ndr_ptr.to_string())
        self.write(ndr_struct.to_string())
        # Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for public_name in struct.public_names[1:]:
                star_count = public_name.count("*")
                if star_count == 1:
                    pointer_name = self.mapper.get_python_type(public_name[1:])[0]
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_name, referent_name=main_name
                    )
                    self.write(ndr_ptr.to_string())
                    self.mapper.add_type(pointer_name)
                elif star_count == 0:
                    alias_name = self.mapper.get_python_type(public_name)[0]
                    self.write(
                        PythonAssignment(
                            PythonName(alias_name),
                            PythonValue(main_name),
                        )
                    )
                    self.mapper.add_type(alias_name)
                else:
                    raise ConversionException(
                        f"Multiple asterisks encountered in name: {public_name}"
                    )
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
