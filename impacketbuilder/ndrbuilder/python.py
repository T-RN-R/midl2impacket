from impacketbuilder.ndrbuilder.base import PythonDef, PythonDefList, PythonValue

"""This module contains data structures that represent various Python constructs."""


class PythonName(PythonValue):
    """Represents a simple python variable name"""

    def __init__(self, name: str):
        self.name = name

    def to_python_string(self, tab_level=0) -> str:
        return self.name


class PythonNameList(PythonDefList):
    """List representation of PythonName objects"""

    CONTAINED_CLASS = PythonName

    def to_python_string(self, tab_level=0) -> str:
        names = ""
        for name in self.obj_list:
            names += f"{name.to_python_string(tab_level)},"
        if names != "":
            names = names[:-1]  # Trim off the last comma
        return names


class PythonTuple(PythonValue):
    """Python tuple implementation"""

    def __init__(self, values: list[PythonValue]):
        if type(values) != list:
            assert isinstance(values, PythonValue)
            values = [values]
        self.values = values

    def to_python_string(self, tab_level=0) -> str:

        out = "\t"*(tab_level-1) + "(\n"
        tab_level+=1
        for val in self.values:
            out += "\t" * (tab_level) + f"{val.to_python_string(tab_level)},\n"
        if out[-2:] == ",\n":
            out = out[:-2]
        out += "\n"+"\t"*(tab_level)+")"
        return out


class PythonList(PythonValue):
    """Represents Python lists"""

    def to_python_string(self, tab_level=0) -> str:
        raise Exception("Unimplemented")


class PythonDictEntry(PythonDef):
    """Represents key:value pairs within a Python dictionary"""

    def __init__(self, key: PythonValue, value: PythonValue):
        self.key = key
        self.value = value

    def to_python_string(self, tab_level=0) -> str:
        return f"{self.key.to_python_string(tab_level)} : {self.value.to_python_string(tab_level)}"


class PythonDictEntryList(PythonDefList):
    """List representation of dictionary entries"""

    CONTAINED_CLASS = PythonDictEntry

    def to_python_string(self, tab_level=0) -> str:
        out = ""
        for de in self.obj_list:
            out += f"{de.to_python_string(tab_level)},"
        out = out[:-1]
        return out


class PythonDict(PythonValue):
    """Python dictionary representation"""

    def __init__(self, dict_entries: PythonDictEntryList):
        self.entries = dict_entries

    def to_python_string(self, tab_level=0) -> str:
        return f"{{{self.entries.to_python_string(tab_level)}}}"


class PythonAssignment(PythonDef):
    """Represents a Python assignment expression"""

    def __init__(self, name: PythonName, rhs: PythonValue):
        self.name = name
        self.rhs = rhs

    def to_python_string(self, tab_level=0) -> str:
        return f"{self.name.to_python_string(tab_level)} = {self.rhs.to_python_string(tab_level)}"


class PythonAssignmentList(PythonDefList):
    """Represents a list of assignment expressions"""

    CONTAINED_CLASS = PythonAssignment

    def to_python_string(self, tab_level=0) -> str:
        assignments = ""
        for assignment in self.obj_list:
            assignments += (
                "\t" * tab_level + f"{assignment.to_python_string(tab_level)}\n"
            )
        return assignments


class PythonFunction(PythonDef):
    """Represents a Python function"""

    def to_python_string(self, tab_level=0) -> str:
        raise Exception("Unimplemented")


class PythonFunctionList(PythonDef):
    """Represents a list of Python functions"""

    CONTAINED_CLASS = PythonFunction

    def to_python_string(self, tab_level=0) -> str:
        raise Exception("Unimplemented")


class PythonClass(PythonDef):
    """Represents a Python class"""

    def __init__(
        self,
        name: PythonName,
        parent_classes: PythonNameList = [],
        class_props: PythonAssignmentList = [],
        functions: PythonFunctionList = [],
    ):
        self.name = name
        self.parent_classes = parent_classes
        self.class_props = class_props
        self.functions = functions

    def to_python_string(self, tab_level=0) -> str:
        output = (
            f"class {self.name.to_python_string(tab_level)}({self.parent_classes.to_python_string(tab_level)}):\n"
            f"{self.class_props.to_python_string(1)}\n"
        )
        return output
