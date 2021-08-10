from .base import Converter
from .struct import MidlStructConverter
from midl import *


class MidlInterfaceConverter(Converter):
    def convert(self, interface):
        for td in interface.typedefs:
            self.handle_typedef(td)
        count = 0
        mapping = {}
        for proc in interface.procedures:
            self.handle_procedure(proc, count)
            mapping[proc.name] = proc.name+"Response"
            count +=1
        opnum_map = "OPNUMS = {\n"
        count = 0
        for k in mapping:
            opnum_map += f"{count} : ({k},{mapping[k]}),\n"
            count +=1
        opnum_map += "}\n"
        self.write(opnum_map)


    def handle_procedure(self, proc, count):
        MidlProcedureConverter(self.io, self.tab_level).convert(proc, count)

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
        if type(td) is MidlTypeDef:
            attr_names = [td.attrs[k].name for k in td.attrs.keys()]
            if "context_handle" in attr_names:
                self.handle_context_handle(td)
            else:
                print(":asdDadssd")
        elif type(td) is MidlSimpleTypedef:
            self.write(f"{td.name.replace('*','').upper()} = {td.type.replace('*','').upper()}")


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
        self.write(class_def)

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
        self.write(class_def)



