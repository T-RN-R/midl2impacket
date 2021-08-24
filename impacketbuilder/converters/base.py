from impacketbuilder.ndrbuilder.io import PythonWriter
from io import StringIO
from impacketbuilder.base import Writer
from impacketbuilder.ndrbuilder.io import PythonWriter
from .typing import TypeMapper


class ConversionException(Exception):
    pass


class UnreachableException(Exception):
    pass


class Converter(Writer):
    def __init__(self, io=None, tab_level=0, mapper: TypeMapper = None):
        self.tab_level = tab_level
        self.io = io or StringIO()
        self.python_writer = PythonWriter(strIO=self.io)
        assert mapper is not None, "Must pass a mapper!"
        self.mapper = mapper

    def convert(self):
        raise UnreachableException(f"Class {__class__} must implement `convert()`")

    def write(self, data: str):
        if not isinstance(data,str):
            data = data.to_python_string()
        for line in data.split("\n"):
            self.single_line_write(line)
