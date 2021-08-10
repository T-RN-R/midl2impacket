from .base import Converter
from midl import *
class MidlProcedureConverter(Converter):
    def convert(self, procedure:MidlProcedure, count):
        input = self.get_input(procedure)
        output = self.get_output(procedure)


        input_str = ""
        for i in input:
            input_str += f"\t\t('{i.name}', {i.type.replace('*','').upper()}),\n"
        input_str = input_str[:-1]

        output_str = ""
        for i in output:
            output_str += f"\t\t('{i.name}', {i.type.replace('*','').upper()}),\n"
        output_str = output_str[:-1]
        proc_str = f"""
class {procedure.name}(NDRCALL):
    opnum = {count}
    structure = (
{input_str}
    )

class {procedure.name}Response(NDRCALL):
    structure = (
{output_str}
    )
        """
        self.write(proc_str)
        
    def get_input(self, procedure:MidlProcedure):
        inp = []
        for param in procedure.params:
            if "in" in param.attrs.keys():
                if param.type == "void**": #TODO Stop cheating here
                    param.type = "CONTEXT_HANDLE"
                inp.append(param)
        return inp

    def get_output(self, procedure:MidlProcedure):
        outp = []
        for param in procedure.params:
            if "out" in param.attrs.keys():
                if param.type == "void**": #TODO Stop cheating here
                    param.type = "CONTEXT_HANDLE"
                outp.append(param)
        return outp
