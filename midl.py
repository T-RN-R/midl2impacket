
class MidlImport():
    def __init__(self, file):
        self.file = file
    def __str__(self):
        return f"import {self.file}"

class MidlVariableDefinition():
    def __init__(self, type, name, rhs, const):
        self.type = type
        self.name = name
        self.rhs = rhs
        self.const = const
    def __str__(self):
        out = ""
        if self.const == True:
            out+="const "
        out += f"{self.type} {self.name} = {self.rhs};"
        return out

class MidlDefinition:
    def __init__(self):
        self.imports = []
        self.definitions = []
        self.interfaces = []
    
    def add_import(self, imp:str):
        self.imports.append(MidlImport(imp))

    def add_definition(self, type, name, rhs, const=False):
        self.definitions.append(MidlVariableDefinition(type,name,rhs,const))

    def add_interface(self,interface):
        self.interfaces.append(interface)
    def __str__(self):
        out = ""
        for i in self.imports:
            out+=str(i) +"\n"
        for i in self.definitions:
            out+=str(i) +"\n"
        return out
              

class MidlInterface:
    def __init__(self):
        self.uuid =  None
        self.version = None
        self.pointer_default = None
        self.name = None
        self.typedefs = []
        self.procedures = []
    def add_typedef(self, td):
        self.typedefs.append(td)
    def add_procedure(self, p):
        self.procedures.append(p)
    def __str__(self):
        out = ""
        out += "UUID: " + self.uuid +";\n"
        out += "Version: " + self.version +";\n"
        out += "interface " + self.name +"{\n"
        for td in self.typedefs:
            out+=str(td)
        for p in self.procedures:
            out+=str(p)
        return out



class MidlTypeDef:
    def __init__(self, type, name, is_context_handle=False, is_complex = False):
        self.type=type
        self.name=name
        self.is_context_handle = is_context_handle
        self.is_complex = is_complex
        self.private_name = None
        
    def get_complex_str(self):
        out = "struct "
        out += self.private_name + " {\n"
        for vd in self.type:
            out+= str(vd)
        out += "} "
        out += self.name +";"
        return out

    def __str__(self):
        out = "typedef "
        if self.is_complex:
            out+= self.get_complex_str()
        else:
            out += f"{self.type} {self.name};\n"
        return out
class MidlVarDef:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    def __str__(self):
        out = f"{self.type} {self.name};\n"
        return out
class MidlProcedure:
    def __init__(self):
        pass