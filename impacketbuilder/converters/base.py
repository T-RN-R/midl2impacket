from io import StringIO
from impacketbuilder.base import Writer
from .typing import IDLTypeToPythonType


class ConversionException(Exception):
    pass


class UnreachableException(Exception):
    pass


class Converter(Writer):
    def __init__(
        self, strIO=StringIO(), tab_level=0, mapper: IDLTypeToPythonType = None
    ):
        self.tab_level = tab_level
        self.io = strIO or StringIO()
        assert mapper is not None, "Must pass a mapper!"
        self.mapper = mapper

    def convert(self):
        raise UnreachableException(f"Class {__class__} must implement `convert()`")
