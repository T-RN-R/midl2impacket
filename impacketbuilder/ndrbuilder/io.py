from impacketbuilder.base import Writer
from impacketbuilder.ndrbuilder.base import PythonDef

"""This module  contains IO classes for the ndrbuilder
"""


class PythonWriter(Writer):
    """Helper that enables writing PythonDef classes without having to call to_python_string()"""

    def write_python(self, python_def: PythonDef):
        self.write(python_def.to_python_string())

    def getvalue(self):
        return self.io.getvalue()
