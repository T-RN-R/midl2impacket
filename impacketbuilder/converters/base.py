from io import StringIO

class ConversionException(Exception):
    pass

class UnreachableException(Exception):
    pass


class Writer:
    NEWLINE = "\n"
    TAB = "\t"
    def __init__(self, strIO = StringIO(), tab_level=0):
        self.tab_level = tab_level
        self.io = strIO or StringIO()
    
    def single_line_write(self, line):
        assert("\n" not in line), "Must use only a single line"
        l = "{0}{1}{2}".format( '\t' * self.tab_level, line, Converter.NEWLINE)
        self.io.write(l)

    def write(self, data):
        for line in data.split("\n"):
            self.single_line_write(line)

class Converter(Writer):
    def convert(self):
        raise UnreachableException(f"Class {__class__} must implement `convert()`")
