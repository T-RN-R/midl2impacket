from impacketbuilder.ndrbuilder.python import PythonAssignment
from midltypes import MidlEnumDef
from .base import Converter
from impacketbuilder.ndrbuilder.python import PythonAssignment, PythonValue, PythonName


class MidlEnumConverter(Converter):
    def convert(self, e: MidlEnumDef) -> str:
        for k in e.map.keys():
            self.write(PythonAssignment(PythonName(k), PythonValue(e.map[k])))
