from re import L
from midl import *


from io import StringIO


class Converter:
    NEWLINE = "\n"
    TAB = "\t"
    def __init__(self, strIO:StringIO, tab_level=0):
        self.tab_level = tab_level
        self.io = strIO
    
    def single_line_write(self, line):
        assert("\n" not in line), "Must use only a single line"
        l = "{0}{1}{2}".format( '\t' * self.tab_level, line, Converter.NEWLINE)
        self.io.write(l)

    def write(self, data):
        for line in data.split("\n"):
            self.single_line_write(line)

class MidlConstantConverter(Converter):
    SIZEOF_LOOKUP = {
                    "WCHAR":4,
                    "BOOL":1,
                    "UINT32":2,
                    "UINT64":4,
                    "GUID":16
                    }
    def convert(self,constant : MidlVariableInstantiation):
        rhs = constant.rhs
        while "sizeof" in rhs: # eliminate all sizeofs!
            rhs = self.calculate_sizeof(rhs)
        const = f"{constant.name.upper()} = {rhs}"
        self.write(const)

    def calculate_sizeof(self,rhs):
        so_idx = rhs.index("sizeof")
        lb_idx = rhs.index("(")
        rb_idx = rhs.index(")")
        type_str = rhs[lb_idx+1:rb_idx].strip()
        if type_str not in MidlConstantConverter.SIZEOF_LOOKUP:
            raise Exception(f"ImpacketBuilder: Could not get sizeof({type_str})")
        return rhs[:so_idx] + str(MidlConstantConverter.SIZEOF_LOOKUP[type_str]) + rhs[rb_idx+1:]


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
            return
            raise Exception("NDR_POINTER unimplemented")

    def handle_ndr_union(self,struct):
        if struct.public_names[0] == '':
            name = __class__.get_anonymous_name()
        else:
            name = struct.public_names[0]
        
        mem_str = ""
        count = 1
        for m in struct.members:
            mem_str += f"{count}: ('{m.name}',{m.type.replace('*','').upper()}),"
            count += 1

        union_def = """
class %s(NDRUNION):
    union = {
        %s
    }
        """ % (name.upper(), mem_str)
        self.io.write(union_def)
        return name

    def handle_ndr_struct(self,struct):
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
        self.io.write(class_def)
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

        if len(struct.members) != 2:
            raise Exception("We only handle array structs with 2 members:  count and array members!")

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
        ('{count_var.name}', {count_var.type.upper()}),
        ('{arr_var.name}', PTR_{name.upper()}),
    )
        """
        self.io.write(classes_str)
        return name.upper()

    def detect_ndr_type(self,struct):
        if type(struct) is MidlUnionDef:
            return MidlStructConverter.NDR_UNION
        types = [ vd.type for vd in struct.members]
        for t in types:
            if type(t) is str: # We can have MidlUnionDefs here!!!
                if "*" in t: # if there is a pointer, assume its an array
                    #TODO This may not actually be that case, find a better way to detect this!
                    return MidlStructConverter.NDR_ARRAY
        return MidlStructConverter.NDR_STRUCT

class MidlInterfaceConverter(Converter):
    def convert(self, interface):
        for td in interface.typedefs:
            self.handle_typedef(td)
            
    def handle_typedef(self, td):
        if type(td) is MidlTypeDef:
            self.handle_midl_td(td)
        elif type(td) is MidlStructDef:
            self.handle_midl_struct(td)
        elif type(td) is MidlEnumDef:
            self.handle_midl_enum(td)
        elif type(td) is MidlSimpleTypedef:
            self.handle_midl_td(td)
        else:
            raise Exception(f"MidlInterfaceConverter: Unhandled typedef type: {td.__class__}")


    def handle_midl_td(self, td:MidlTypeDef):
        print(td)
        attr_names = [td.attrs[k].name for k in td.attrs.keys()]
        if "context_handle" in attr_names:
            self.handle_context_handle(td)
        else:
            print(":asdDadssd")

    def handle_context_handle(self, td):
        pointer_name = td.name
        real_name = td.name
        if td.name[0] == "P":
            real_name = td.name[1:]
        class_def = f"""
class {real_name}(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )

class {pointer_name}(NDRPOINTER):
    referent = (
        ('Data', {real_name}),
    )        
        """
        self.io.write(class_def)

    def handle_midl_struct(self, td:MidlStructDef):
        struct_converter = MidlStructConverter(self.io,self.tab_level)
        struct_converter.convert(td)

    def handle_midl_enum(self, td:MidlEnumDef):
        vars = ""
        for key in td.map.keys():
            vars+="\t"+key + " = " + str(td.map[key])+",\n"
        vars = vars[:-2] #eliminate the final comma and newline

        class_def = f"""
class {td.public_names[0].upper()}:
{vars}
        """
        self.io.write(class_def)





class MidlDefinitionConverter:
    def convert(definition : MidlDefinition) -> str:
        strIO = StringIO()
        MidlDefinitionConverter.__header_comment_block(strIO)
        MidlDefinitionConverter.__default_imports(strIO)
        if len(definition.interfaces) != 1:
            raise Exception("ImpacketBuilder cannot handle MIDL files with multiple interface definitions")
        MidlDefinitionConverter.__banner_comment(strIO,"CONSTANTS")
        MidlDefinitionConverter.__uuid(strIO, definition.interfaces[0])
        const_converter = MidlConstantConverter(strIO, tab_level=0)
        for const in definition.instantiation:
            const_converter.convert(const)
        interface_converter = MidlInterfaceConverter(strIO, tab_level=0)
        interface_converter.convert(definition.interfaces[0])
        return strIO.getvalue()

    def __uuid(io : StringIO, interface : MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"

        io.write(f"{int_name} = uuidtup_to_bin(('{interface.attributes['uuid']}','0.0'))\n")

    def __banner_comment(io : StringIO, comment:str):
        MidlDefinitionConverter.__sl_comment(io,"#"*80)
        MidlDefinitionConverter.__sl_comment(io, comment)
        MidlDefinitionConverter.__sl_comment(io,"#"*80)

    def __sl_comment(io : StringIO, comment:str):
        io.write(f"#{comment}\n")

    def __default_imports(io : StringIO):
        imports = """
from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException
"""
        io.write(imports)

    def __header_comment_block(io : StringIO):
        comment = '"""Generated from MIDL2Impacket.py"""\n' 
        io.write(comment)

class ImpacketBuilder:
    def __init__(self):
        self.__midl_def = None

    def midl_def(self, definition : MidlDefinition):
        self.__midl_def = definition
        return self

    def build(self):
        assert(self.__midl_def != None)
        python_code = MidlDefinitionConverter.convert(self.__midl_def)
        return python_code