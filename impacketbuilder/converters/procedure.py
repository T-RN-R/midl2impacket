from .base import Converter
from midl import MidlProcedure
from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonAssignmentList,
    PythonNameList,
    PythonValue,
    PythonName,
    PythonTuple,
    PythonClass,
    PythonAssignmentList,
)
from impacketbuilder.ndrbuilder.ndr import PythonNdrCall


class MidlProcedureConverter(Converter):
    def convert(self, procedure: MidlProcedure, count):
        input = self.get_input(procedure)
        output = self.get_output(procedure)

        input_list = []
        for i in input:
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
        for i in output:
            output_list.append(
                PythonTuple(
                    [
                        PythonValue(f"'{i.name}'"),
                        PythonValue(self.mapper.canonicalize(i.type)),
                    ]
                )
            )
        outputs = PythonTuple(input_list)

        ndr_response = PythonNdrCall(procedure.name + "Response", outputs, opnum=None)

        self.write(ndr_request.to_string())
        self.write(ndr_response.to_string())

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
