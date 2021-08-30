from impacketbuilder.converters.vardef import VarDefConverter
from impacketbuilder.ndrbuilder.ndr import PythonNdrCall
from impacketbuilder.ndrbuilder.python import PythonFunction, PythonTuple
from midltypes import MidlProcedure, MidlVarDef

from .base import Converter


class MidlProcedureConverter(Converter):
    """Convert MIDL procedures to python"""

    def convert(self, procedure: MidlProcedure, count):
        # Get all "in" and "out" parameters
        in_params, out_params = self.get_io(procedure)

        # Generate vardefs for input/outputs
        converter = VarDefConverter(
            io=self.io, tab_level=self.tab_level, mapper=self.mapper, func_params=True
        )
        vardef_inputs = [converter.convert(in_param) for in_param in in_params]
        vardef_outputs = [converter.convert(out_param) for out_param in out_params]
        # Outputs always has ErrorCode
        vardef_outputs.append(converter.python_vardef(var_name="ErrorCode", type_name="ULONG"))

        # Generate the request
        python_inputs = PythonTuple(vardef_inputs)
        ndr_request = PythonNdrCall(procedure.name, python_inputs, opnum=count)
        self.write(ndr_request.to_string())

        # Create response
        python_outputs = PythonTuple(vardef_outputs)
        ndr_response = PythonNdrCall(
            procedure.name + "Response", python_outputs, opnum=None
        )
        self.write(ndr_response.to_string())
        self.generate_helper(procedure, vardef_inputs)

    def get_io(self, procedure: MidlProcedure):
        """Get inputs and outputs from a procedure"""
        inputs = []
        outputs = []
        for param in procedure.params:
            if "in" in param.attributes:
                inputs.append(param)
            if "out" in param.attributes:
                outputs.append(param)
        return inputs, outputs

    def generate_helper(self, procedure: MidlProcedure, input_list: list[PythonTuple]):
        arguments = ['dce: DCERPC_v5']
        assignments = []
        for input_tup in input_list:
            arg_name = input_tup.values[0].value[1:-1]
            arg_type = input_tup.values[1].value
            arguments.append(f"{arg_name}: {arg_type}")
            assignments.append(f'request["{arg_name}"] = {arg_name}')
        arguments = ", ".join(arguments)
        function_body_parts = [f"request = {procedure.name}()"]
        function_body_parts.extend(assignments)
        function_body_parts.append("return dce.request(request)")
        helper = PythonFunction(
            name=f"h{procedure.name}", args=arguments, body=function_body_parts
        )
        self.write(helper.to_python_string())
