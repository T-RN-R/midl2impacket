from midltypes import (
    MidlDefinition,
    MidlEnumDef,
    MidlSimpleTypedef,
    MidlStructDef,
    MidlUnionDef,
)
from impacketbuilder.converters.typing import TypeMapper
from io import StringIO
import pathlib
from midlparser import parse_idl
from .datatype import IDL_TO_NDR

class FuzzerTemplateGenerator:
    """A class that generates fuzzing templates"""

    def __init__(self):
        self.io = StringIO()
        self.generated_classes = {}
        self.mapper = TypeMapper(None)
        self.static_imports = """
from fuzzer.midl import *
from fuzzer.core import *
"""
    def static(self):
        if self.static_imports == "":
            return
        mapping = ""
        for idl_name, py_name in IDL_TO_NDR.items():
            canonicalized_name, _ = self.mapper.canonicalize(idl_name)
            if canonicalized_name != py_name:
                mapping += f"{canonicalized_name} = {py_name}\n"
            self.mapper.add_type(canonicalized_name)
        self.io.write(mapping)

    def generate_import(self, _import, import_dir):
        in_file = pathlib.Path(import_dir + _import.file)
        self.generate(parse_idl(in_file), import_dir)

    def generate(self, midl_def: MidlDefinition, import_dir):
        """Generates a Python file that is a fuzzing template"""
        # TODO handle imports
        self.io.write(self.static_imports)
        self.static()
        self.static_imports = ""
        for _import in midl_def.imports:
            self.generate_import(_import, import_dir)

        first_uuid = None
        # TODO generate struct defs first, before generating interface defs
        for typedef in midl_def.typedefs:
            self.handle_typedef(typedef)
        for interface in midl_def.interfaces:
            if "uuid" in interface.attributes and first_uuid is None:
                first_uuid = interface.attributes["uuid"].params[0]
                self.generate_interface(interface)

        return self.io.getvalue(), first_uuid

    def handle_typedef(self, typedef):
        if isinstance(typedef, MidlUnionDef):
            self.generate_union(typedef)
        elif isinstance(typedef, MidlStructDef):
            self.generate_struct(typedef)
        elif isinstance(typedef, MidlEnumDef):
            self.generate_enum(typedef)
        elif isinstance(typedef, MidlSimpleTypedef):
            # TODO Add this typedef mapping to a type hierarchy lookup mapper
            return ""
        elif typedef is None:
            return ""
        else:
            raise Exception(f"Unhandled typedef {type(typedef)}")

    def generate_union(self, union: MidlUnionDef):
        output = ""
        # TODO add typedef mapping for all public names of this struct
        if len(union.public_names) > 0:
            name = union.public_names[0]
        else:
            name = union.private_name
        # TODO do a proper switch_type lookup
        switch_type = "DWORD"
        members = ""
        member_cnt = 1
        for member in union.members:
            type_name = member.type
            if isinstance(member.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                self.handle_typedef(member.type)
                if len(member.type.public_names) > 0:
                    type_name = member.type.public_names[0]
                else:
                    type_name = member.type.private_name

            if isinstance(type_name, str):
                members += f'{member_cnt} : ({self.mapper.canonicalize(type_name)[0]}, "{member.name}"),'
            member_cnt += 1

        class_def = f"""
class {self.mapper.canonicalize(name)[0]}(NdrUnion):
    SWITCHTYPE = {switch_type}
    MEMBERS = {{{members}}}

    
"""
        self.io.write(class_def)
        for n in union.public_names:
            if n != name:
                n = n.replace("*","")
                self.io.write(f"{self.mapper.canonicalize(n)[0]} = {self.mapper.canonicalize(name)[0]}")

    def generate_struct(self, struct):
        output = ""
        # TODO add typedef mapping for all public names of this struct
        if len(struct.public_names) > 0:
            name = struct.public_names[0]
        else:
            name = struct.private_name

        members = ""
        member_cnt = 1
        for member in struct.members:
            type_name = member.type
            if isinstance(member.type, (MidlUnionDef, MidlStructDef)):
                # handle nested unions/structs
                self.handle_typedef(member.type)
                if len(member.type.public_names) > 0:
                    type_name = member.type.public_names[0]
                else:
                    type_name = member.type.private_name

            if isinstance(type_name, str):
                members += (
                    f'({self.mapper.canonicalize(type_name)[0]}, "{member.name}"),'
                )
            member_cnt += 1

        class_def = f"""
class {self.mapper.canonicalize(name)[0]}(NdrStructure):
    MEMBERS = [{members}]

    
"""
        self.io.write(class_def)
        for n in struct.public_names:
            if n != name:
                n = n.replace("*","")
                self.io.write(f"{self.mapper.canonicalize(n)[0]} = {self.mapper.canonicalize(name)[0]}")


    def generate_enum(self, enum):
        output = ""
        # TODO add typedef mapping for all public names of this struct

    def generate_interface(self, midl_interface):
        output = ""
        if len(midl_interface.attributes) == 0:
            return ""
        uuid = midl_interface.attributes["uuid"].params[0]
        if "version" in midl_interface.attributes:
            version = midl_interface.attributes["version"].params[0]
        else:
            version = "1.0"
        procedures = ""
        for proc in midl_interface.procedures:
            procedures += f"{self.generate_procedure(proc)},\n"
        output += f'Interface("{uuid}", "{version}",[\n{procedures}])'
        return output

    def generate_procedure(self, procedure):
        output = ""
        params = ""
        for param in procedure.params:
            input_attr = "in" in param.attributes
            output_attr = "out" in param.attributes
            clz = (
                "InOut"
                if input_attr and output_attr
                else ("Out" if output_attr else "In")
            )
            params += f"{clz}({self.mapper.canonicalize(param.type)[0]}),\n"
        output += f'Method("{procedure.name}",\n{params}),'
        self.io.write(output)
