from impacketbuilder.ndrbuilder.ndr import PythonNdrCall
from impacketbuilder.ndrbuilder.python import PythonFunction, PythonTuple, PythonValue
from midltypes import MidlProcedure, MidlVarDef

from .base import Converter


class MidlProcedureConverter(Converter):
    def convert(self, procedure: MidlProcedure, count):
        proc_inputs = self.get_input(procedure)
        proc_outputs = self.get_output(procedure)

        # Generate the request structure
        input_list = []
        for in_param in proc_inputs:
            if "*" in in_param.type:
                self.generate_pointers(in_param.type)
            input_list.append(
                PythonTuple(
                    [
                        PythonValue(f"'{in_param.name}'"),
                        PythonValue(self.mapper.canonicalize(in_param.type)),
                    ]
                )
            )
        inputs = PythonTuple(input_list)
        ndr_request = PythonNdrCall(procedure.name, inputs, opnum=count)

        # Generate the response structure
        output_list = []
        for out_param in proc_outputs:
            if "*" in out_param.type:
                self.generate_pointers(out_param.type)
            output_list.append(
                PythonTuple(
                    [
                        PythonValue(f"'{out_param.name}'"),
                        PythonValue(self.mapper.canonicalize(out_param.type)),
                    ]
                )
            )
        outputs = PythonTuple(output_list)
        ndr_response = PythonNdrCall(procedure.name + "Response", outputs, opnum=None)

        self.write(ndr_request.to_string())
        self.write(ndr_response.to_string())
        self.generate_helper(procedure, proc_inputs)

    def get_input(self, procedure: MidlProcedure):
        inp = []
        for param in procedure.params:
            if "in" in param.attributes.keys():
                if param.type == "void**":  # TODO Stop cheating here
                    param.type = "CONTEXT_HANDLE"
                inp.append(param)
        return inp

    def get_output(self, procedure: MidlProcedure):
        outp = []
        for param in procedure.params:
            if "out" in param.attributes.keys():
                if param.type == "void**":  # TODO Stop cheating here
                    param.type = "CONTEXT_HANDLE"
                outp.append(param)
        return outp

    def generate_helper(self, procedure: MidlProcedure, input_list: list[MidlVarDef]):
        arguments = ', '.join(['dce'] + [arg.name for arg in input_list])
        function_body_parts = [f"request = {procedure.name}()"]
        assignments = [f'request["{arg.name}"] = {arg.name}' for arg in input_list]
        function_body_parts.extend(assignments)
        function_body_parts.append("return dce.request(request)")        
        helper = PythonFunction(
            name=f"h{procedure.name}",
            args=arguments,
            body=function_body_parts
        )
        self.write(helper.to_python_string())

