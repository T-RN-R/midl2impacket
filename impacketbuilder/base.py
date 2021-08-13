from io import StringIO


class Writer:
    NEWLINE = "\n"
    TAB = "\t"

    def __init__(self, strIO=StringIO(), tab_level=0):
        self.tab_level = tab_level
        self.io = strIO or StringIO()

    def single_line_write(self, line: str):
        assert "\n" not in line, "Must use only a single line"
        l = "{0}{1}{2}".format("\t" * self.tab_level, line, Writer.NEWLINE)
        self.io.write(l)

    def write(self, data: str):
        for line in data.split("\n"):
            self.single_line_write(line)


class Writable:
    def write(self, writer: Writer):
        writer.write(str(self))
