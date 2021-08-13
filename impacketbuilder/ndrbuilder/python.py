from impacketbuilder.ndrbuilder.base import PythonDef, PythonDefList, PythonValue


class PythonName(PythonValue):
    """Represents a simple python variable name"""

    def __init__(self, name: str):
        self.name = name

    def to_python_string(self) -> str:
        return self.name


class PythonNameList(PythonDefList):
    CONTAINED_CLASS = PythonName

    def to_python_string(self) -> str:
        names = ""
        for name in self.obj_list:
            names += f"{name.to_python_string()},"
        if names != "":
            names = names[:-1]  # Trim off the last comma
        return names


class PythonTuple(PythonValue):
    def __init__(self, values: list[PythonValue]):
        self.values = values

    def to_python_string(self) -> str:
        out = "(\n"
        for val in self.values:
            out += f"\t{val.to_python_string()},\n"
        out = out[:-2] + "\n)"
        return out


class PythonList(PythonValue):
    def to_python_string(self) -> str:
        return ""


class PythonDictEntry(PythonDef):
    def __init__(self, key: PythonValue, value: PythonValue):
        self.key = key
        self.value = value

    def to_python_string(self) -> str:
        return f"{self.key.to_python_string()} : {self.value.to_python_string()}"


class PythonDictEntryList(PythonDefList):
    CONTAINED_CLASS = PythonDictEntry

    def to_python_string(self) -> str:
        out = ""
        for de in self.obj_list:
            out += f"{de.to_python_string()},"
        out = out[:-1]
        return out


class PythonDict(PythonValue):
    def __init__(self, dict_entries: PythonDictEntryList):
        self.entries = dict_entries

    def to_python_string(self) -> str:
        return f"{{{self.entries.to_python_string()}}}"


class PythonAssignment(PythonDef):
    def __init__(self, name: PythonName, rhs: PythonValue):
        self.name = name
        self.rhs = rhs

    def to_python_string(self) -> str:
        return f"{self.name.to_python_string()} = {self.rhs.to_python_string()}"


class PythonAssignmentList(PythonDefList):
    CONTAINED_CLASS = PythonAssignment

    def to_python_string(self) -> str:
        assignments = ""
        for assignment in self.obj_list:
            assignments += f"{assignment.to_python_string()}\n"
        return assignments


class PythonFunction(PythonDef):
    def to_python_string(self) -> str:
        return ""


class PythonFunctionList(PythonDef):
    CONTAINED_CLASS = PythonFunction

    def to_python_string(self) -> str:
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

    def to_python_string(self) -> str:

        output = (
            f"class {self.name.to_python_string()}({self.parent_classes.to_python_string()}):\n",
            f"\t{self.class_props.to_python_string()}\n",
        )
        return output
