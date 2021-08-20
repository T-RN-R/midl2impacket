from impacketbuilder.converters.vardef import VarDefConverter
from .base import Converter
from midltypes import MidlProcedure
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
        proc_inputs, proc_outputs = self.get_io(procedure)
        # Create request
        python_inputs = PythonTuple(proc_inputs)
        ndr_request = PythonNdrCall(procedure.name, python_inputs, opnum=count)
        self.write(ndr_request.to_string())
        
        # Create response
        python_outputs = PythonTuple(proc_outputs)
        ndr_response = PythonNdrCall(procedure.name + "Response", python_outputs, opnum=None)
        self.write(ndr_response.to_string())       

    def get_io(self, procedure: MidlProcedure):
        """ Get inputs and outputs from a procedure """
        inputs = []
        outputs = []
        converter = VarDefConverter(io=self.io, tab_level=self.tab_level, mapper=self.mapper)
        for param in procedure.params:
            python_vardef = converter.convert(param)
            if "in" in param.attributes:
                inputs.append(python_vardef)
            if "out" in param.attributes:
                outputs.append(python_vardef)
        return inputs, outputs
