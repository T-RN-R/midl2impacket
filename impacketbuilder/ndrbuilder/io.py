from impacketbuilder.base import Writer
from impacketbuilder.ndrbuilder.base import PythonDef


class PythonWriter(Writer):
    def write_python(self, python_def: PythonDef):
        self.write(python_def.to_python_string())

    def getvalue(self):
        return self.io.getvalue()