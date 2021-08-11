from .base import ConversionException, Converter
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

    def handle_ndr_union(self, struct):
        #TODO if a union has multiple public_names, create Python mappings for them as well
        if struct.public_names[0] == '':
            name = __class__.get_anonymous_name()
        else:
            name = struct.public_names[0]
        

        mem_str = ""
        count = 1
        for m in struct.members:
            if m.attributes:
                if m.attributes["case"]:
                    # TODO handle the case attributes and set the appropriate NDRUNION key
                    pass
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
            mem_str += f"{count}: ('{m.name}',{self.mapper.canonicalize(type_name)}),"
            count += 1
        base_name = self.mapper.canonicalize(name)
        union_def = """
class %s(NDRUNION):
    union = {
        %s
    }
        """ % (base_name, mem_str)

        #Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for pn in struct.public_names[1:]:
                star_count = pn.count("*")
                if star_count == 1:
                    union_def += f"""class {self.mapper.canonicalize(pn)}(NDRPOINTER):
    referent = (
        ('Data', {base_name}),
    )    
"""
                elif star_count == 0:
                    union_def += f"{pn} = {base_name}\n"
                else:
                    raise ConversionException("Multiple asterisks encountered in name: {pn}")



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
            vars+=f"('{vd.name}', {self.mapper.canonicalize(data_type)}),"
        base_name = self.mapper.canonicalize(struct.public_names[0])
        class_def = f"""
class {base_name}(NDRSTRUCT):
    structure = (
        {vars}
    )
"""
        
        #Now handle the cases where there are multiple public names, including pointers
        if len(struct.public_names) > 1:
            for pn in struct.public_names[1:]:
                star_count = pn.count("*")
                if star_count == 1:
                    class_def += f"""class {self.mapper.canonicalize(pn)}(NDRPOINTER):
    referent = (
        ('Data', {base_name}),
    )    
"""
                elif star_count == 0:
                    class_def += f"{pn} = {base_name}\n"
                else:
                    raise ConversionException("Multiple asterisks encountered in name: {pn}")


        self.write(class_def)
        return {struct.public_names[0]}

    def handle_ndr_array(self,struct):
        # First step: Find the count and the array variables
        count_name = None
        arr_var = None
        count_var = None
        name = struct.public_names[0]
        for vd in struct.members:
            for attr_name in vd.attributes:
                if attr_name == "size_is":
                    arr_var = vd
                    count_name = vd.attributes[attr_name].params[0]
        for vd in struct.members:
            if vd.name == count_name:
                count_var = vd

        #if len(struct.members) != 2:
            #raise Exception("We only handle array structs with 2 members:  count and array members!")
        core_struct_fields = ""
        for vd in struct.members:
            if vd is arr_var:
                core_struct_fields += f"\t('{arr_var.name}', PTR_{self.mapper.canonicalize(name)}),\n"
            else:
                core_struct_fields += f"\t('{vd.name}', {self.mapper.canonicalize(vd.type)}),"

        underlying_type = arr_var.type.replace("*","")
        name = self.mapper.canonicalize(name)
        classes_str = f"""
class DATA_{name}(NDRUniConformantArray):
    item = {self.mapper.canonicalize(underlying_type)}

class PTR_{name}(NDRPOINTER):
    referent = (
        ('Data', DATA_{name}),
    )

class {name}(NDRSTRUCT):
    structure = (
{core_struct_fields}
    )
        """
        self.write(classes_str)
        return name

    def detect_ndr_type(self,struct):
        if type(struct) is MidlUnionDef:
            return MidlStructConverter.NDR_UNION
        types = [ vd.type for vd in struct.members]
        for vd in struct.members:
            t = vd.type
            if type(t) is str: # We can have MidlUnionDefs here!!!
                if "*" in t  and 'size_is' in vd.attributes: # if there is a pointer, assume its an array
                    #TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT
