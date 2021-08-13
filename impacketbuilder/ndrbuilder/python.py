from impacketbuilder.ndrbuilder.base import PythonDef, PythonDefList, PythonValue


class PythonName(PythonValue):
    """Represents a simple python variable name"""

    def __init__(self, name: str):
        self.name = name

    def to_python_string(self, tab_level=0) -> str:
        return self.name


class PythonNameList(PythonDefList):
    CONTAINED_CLASS = PythonName

    def to_python_string(self, tab_level=0) -> str:
        names = ""
        for name in self.obj_list:
            names += f"{name.to_python_string(tab_level)},"
        if names != "":
            names = names[:-1]  # Trim off the last comma
        return names


class PythonTuple(PythonValue):
    def __init__(self, values: list[PythonValue]):
        if type(values) != list:
            assert(isinstance(values,PythonValue))
            values = [values]
        self.values = values

    def to_python_string(self, tab_level=0) -> str:
        if len(self.values) == 2:
            out = "\t" * tab_level + f"\t({self.values[0].to_python_string(tab_level)}, {self.values[1].to_python_string(tab_level)})"
            return out
        out = "(\n"
        for val in self.values:
            out += "\t"* tab_level+ f"{val.to_python_string(tab_level)},\n"
        if out[-2:] == ",\n":
            out = out[:-2] 
        out+= "\n\t\t)"
        return out


class PythonList(PythonValue):
    def to_python_string(self,tab_level=0) -> str:
        return ""


class PythonDictEntry(PythonDef):
    def __init__(self, key: PythonValue, value: PythonValue):
        self.key = key
        self.value = value

    def to_python_string(self, tab_level=0) -> str:
        return f"{self.key.to_python_string(tab_level)} : {self.value.to_python_string(tab_level)}"


class PythonDictEntryList(PythonDefList):
    CONTAINED_CLASS = PythonDictEntry

    def to_python_string(self, tab_level=0) -> str:
        out = ""
        for de in self.obj_list:
            out += f"{de.to_python_string(tab_level)},"
        out = out[:-1]
        return out


class PythonDict(PythonValue):
    def __init__(self, dict_entries: PythonDictEntryList):
        self.entries = dict_entries

    def to_python_string(self, tab_level=0) -> str:
        return f"{{{self.entries.to_python_string(tab_level)}}}"


class PythonAssignment(PythonDef):
    def __init__(self, name: PythonName, rhs: PythonValue):
        self.name = name
        self.rhs = rhs

    def to_python_string(self, tab_level=0) -> str:
        return f"{self.name.to_python_string(tab_level)} = {self.rhs.to_python_string(tab_level)}"


class PythonAssignmentList(PythonDefList):
    CONTAINED_CLASS = PythonAssignment

    def to_python_string(self, tab_level=0) -> str:
        assignments = ""
        for assignment in self.obj_list:
            assignments += "\t"*tab_level + f"{assignment.to_python_string(tab_level)}\n"
        return assignments


class PythonFunction(PythonDef):
    def to_python_string(self, tab_level=0) -> str:
        return ""


class PythonFunctionList(PythonDef):
    CONTAINED_CLASS = PythonFunction

    def to_python_string(self, tab_level=0) -> str:
        return ""


class PythonClass(PythonDef):
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
