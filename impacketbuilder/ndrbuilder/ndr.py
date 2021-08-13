from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonAssignmentList,
    PythonDictEntryList,
    PythonNameList,
    PythonValue,
    PythonName,
    PythonTuple,
    PythonClass,
    PythonAssignmentList,
    PythonDict,
)


class PythonNdrClassDefiniton:
    def __init__(self):
        self.clazz = None

    def to_string(self):
        return self.clazz.to_python_string()


class PythonNdrStruct(PythonNdrClassDefiniton):
    def __init__(self, name:str, structure: PythonTuple, align:str="1"):
        align = PythonAssignment(PythonName("align"), PythonValue(align))
        structure = PythonAssignment(PythonValue("structure"), structure)
        prop_list = [align, structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRSTRUCT")),
            class_props=props,
            functions=None,
        )


class PythonNdrPointer(PythonNdrClassDefiniton):
    def __init__(self, name:str, referent_name:str):
        referent = PythonAssignment(
            PythonName("referent"),
            PythonTuple(
                [PythonTuple([PythonValue("'Data'"), PythonValue(referent_name)])]
            ),
        )
        prop_list = [referent]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRPOINTER")),
            class_props=props,
            functions=None,
        )


class PythonNdrUnion(PythonNdrClassDefiniton):
    def __init__(self, name:str, union_entries: PythonDictEntryList):
        structure = PythonAssignment(PythonValue("union"), PythonDict(union_entries))
        prop_list = [structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUNION")),
            class_props=props,
            functions=None,
        )


class PythonNdrCall(PythonNdrClassDefiniton):
    def __init__(self, name:str, structure:PythonTuple, opnum=None):
        structure = PythonAssignment(PythonName("structure"), structure)
        if opnum is not None:
            op = PythonAssignment(PythonName("OPNUM"), PythonValue(str(opnum)))
            prop_list = [op, structure]
        else:
            prop_list = [structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRCALL")),
            class_props=props,
            functions=None,
        )


class PythonNdrUniConformantArray(PythonNdrClassDefiniton):
    def __init__(self, name: str, underlying_type_name: str):
        structure = PythonAssignment(
            PythonValue("item"), PythonName(underlying_type_name)
        )
        prop_list = [structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniConformantArray")),
            class_props=props,
            functions=None,
        )
