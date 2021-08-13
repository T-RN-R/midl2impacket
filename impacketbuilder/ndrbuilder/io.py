from impacketbuilder.base import Writer
from impacketbuilder.ndrbuilder.base import PythonDef


class PythonWriter(Writer):
    def write(self, python_def: PythonDef):
        python_def.write(self.io)
