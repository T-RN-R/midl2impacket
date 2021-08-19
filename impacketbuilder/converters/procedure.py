from impacketbuilder.ndrbuilder.ndr import PythonNdrCall
from impacketbuilder.ndrbuilder.python import (PythonFunction, PythonTuple,
                                               PythonValue)
from midltypes import MidlProcedure, MidlVarDef

from .base import Converter


class MidlProcedureConverter(Converter):
    def convert(self, procedure: MidlProcedure, count):
        proc_inputs = self.get_input(procedure)
        proc_outputs = self.get_output(procedure)

        input_list = []
        for i in proc_inputs:
            input_list.append(
                PythonTuple(
                    [
                        PythonValue(f"'{i.name}'"),
                        PythonValue(self.mapper.canonicalize(i.type)),
                    ]
                )
            )
        inputs = PythonTuple(input_list)

        ndr_request = PythonNdrCall(procedure.name, inputs, opnum=count)

        output_list = []
        for i in proc_outputs:
            output_list.append(
                PythonTuple(
                    [
                        PythonValue(f"'{i.name}'"),
                        PythonValue(self.mapper.canonicalize(i.type)),
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
