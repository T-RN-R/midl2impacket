from .base import Converter
from midl import *

class MidlStructConverter(Converter):
    NDR_ARRAY = 0x1
    NDR_POINTER = 0x2
    NDR_STRUCT = 0x3
    NDR_UNION = 0x4
    Anonymous_Count = 0

    def get_anonymous_name():
        __class__.Anonymous_Count+=1
        return "Anonymous"+str(__class__.Anonymous_Count)
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

    def handle_ndr_union(self,struct):
        #TODO if a union has multiple public_names, create Python mappings for them as well
        if struct.public_names[0] == '':
            name = __class__.get_anonymous_name()
        else:
            name = struct.public_names[0]
        
        mem_str = ""
        count = 1
        for m in struct.members:
            type_name = None
            if type(m.type) is str:
                type_name = m.type
            elif type(m.type) is MidlStructDef:
                type_name = m.type.public_names[0]
                self.convert(m.type)
            elif type(m.type) is MidlUnionDef:
                type_name = m.type.public_names[0]
                self.convert(m.type)
            else:
                raise Exception(f"Unexpected type: {type(m.type)}")
            mem_str += f"{count}: ('{m.name}',{type_name.replace('*','').upper()}),"
            count += 1

        union_def = """
class %s(NDRUNION):
    union = {
        %s
    }
        """ % (name.upper(), mem_str)
        self.write(union_def)
        return name

    def handle_ndr_struct(self,struct):
        #TODO if a struct has multiple public_names, create a Pyhton mapping for them too
        vars = ""
        for vd in struct.members:
            if type(vd.type) is MidlUnionDef or type(vd.type) is MidlStructDef:
                #handle nested unions/structs
                data_type = self.convert(vd.type)
                vd.name=data_type
            elif type(vd.type) is str:
                data_type = vd.type
            vars+=f"('{vd.name}', {data_type.upper()}),"

        class_def = f"""
class {struct.public_names[0].upper()}(NDRSTRUCT):
    structure = (
        {vars}
    )
        """
        self.write(class_def)
        return {struct.public_names[0]}

    def handle_ndr_array(self,struct):
        # First step: Find the count and the array variables
        count_name = None
        arr_var = None
        count_var = None
        name = struct.public_names[0]
        for vd in struct.members:
            for attr_name in vd.attrs:
                if attr_name == "size_is":
                    arr_var = vd
                    count_name = vd.attrs[attr_name].params[0]
        for vd in struct.members:
            if vd.name == count_name:
                count_var = vd

        #if len(struct.members) != 2:
            #raise Exception("We only handle array structs with 2 members:  count and array members!")

        core_struct_fields = ""
        for vd in struct.members:
            if vd is arr_var:
                core_struct_fields += f"\t('{arr_var.name}', PTR_{name.upper()}),\n"
            else:
                core_struct_fields += f"\t('{vd.name}', {vd.type.upper()}),"

        underlying_type = arr_var.type.replace("*","")

        classes_str = f"""
class DATA_{name.upper()}(NDRUniConformantArray):
    item = {underlying_type.upper()}

class PTR_{name.upper()}(NDRPOINTER):
    referent = (
        ('Data', DATA_{name.upper()}),
    )

class {name.upper()}(NDRSTRUCT):
    structure = (
{core_struct_fields}
    )
        """
        self.write(classes_str)
        return name.upper()

    def detect_ndr_type(self,struct):
        if type(struct) is MidlUnionDef:
            return MidlStructConverter.NDR_UNION
        types = [ vd.type for vd in struct.members]
        for vd in struct.members:
            t = vd.type
            if type(t) is str: # We can have MidlUnionDefs here!!!
                if "*" in t  and 'size_is' in vd.attrs: # if there is a pointer, assume its an array
                    #TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT
