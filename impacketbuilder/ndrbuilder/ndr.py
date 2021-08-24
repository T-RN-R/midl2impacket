from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonAssignmentList,
    PythonDictEntryList,
    PythonFunction,
    PythonFunctionList,
    PythonNameList,
    PythonValue,
    PythonName,
    PythonTuple,
    PythonClass,
    PythonAssignmentList,
    PythonDict,
)

"""This module defines a series of helper classes that build the Python definitons for various Impacket NDR extensions
"""


class PythonNdrClassDefiniton:
    """Base class for Impacket NDR class definitions"""

    def __init__(self):
        self.clazz = None

    def to_string(self):
        return self.clazz.to_python_string(0)


class PythonNdrStruct(PythonNdrClassDefiniton):
    """Creates a simple NDRSTRUCT"""

    def __init__(self, name: str, structure: PythonTuple, align: str = "1"):
        align = PythonAssignment(PythonName("align"), PythonValue(align))
        structure = PythonAssignment(PythonValue("structure"), structure)
        prop_list = [align, structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRSTRUCT")),
            class_props=props,
            functions=PythonFunctionList(),
        )


class PythonNdrPointer(PythonNdrClassDefiniton):
    """Creates a simple NDRPOINTER"""

    def __init__(self, name: str, referent_name: str):
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
            functions=PythonFunctionList(),
        )


class PythonNdrUnion(PythonNdrClassDefiniton):
    """Creates a simple NDRUNION"""

    def __init__(self, name: str, union_entries: PythonDictEntryList, tag=None):
        prop_list = []
        if tag:
            commonHdr =  PythonAssignment(
                PythonName('commonHdr'),
                PythonTuple(
                    [PythonTuple([PythonValue("'tag'"), PythonValue(tag)])]
                ),
            )
            prop_list.append(commonHdr)
        structure = PythonAssignment(PythonValue("union"), PythonDict(union_entries))
        prop_list.append(structure)
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUNION")),
            class_props=props,
            functions=PythonFunctionList(),
        )


class PythonNdrCall(PythonNdrClassDefiniton):
    """Creates a simple NDRCALL"""

    def __init__(self, name: str, structure: PythonTuple, opnum=None):
        structure = PythonAssignment(PythonName("structure"), structure)
        if opnum is not None:
            op = PythonAssignment(PythonName("opnum"), PythonValue(str(opnum)))
            prop_list = [op, structure]
        else:
            prop_list = [structure]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRCALL")),
            class_props=props,
            functions=PythonFunctionList(),
        )


class PythonNdrUniConformantArray(PythonNdrClassDefiniton):
    """Creates a simple NDRUniConformantArray"""

    def __init__(self, name: str, underlying_type_name: str, maximum_length=None):
        item = PythonAssignment(PythonValue("item"), PythonName(underlying_type_name))
        # TODO: Sort out whether we can safely use maximum length?
        # class CHAR_ARRAY(NDRUniConformantArray):
	    #   item = CHAR
	    #   structure = (
		#       'MaximumCount',
		#       MaximumLength,
		#   )
        structure = PythonAssignment(
            PythonValue("structure"),
            PythonTuple(
                [PythonName("'MaximumCount'"), PythonValue(str(maximum_length))]
            ),
        )
        # if maximum_length != None:
        #     prop_list = [item, structure]
        # else:
        prop_list = [item]
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniConformantArray")),
            class_props=props,
            functions=PythonFunctionList(),
        )


class PythonNdrUniFixedArray(PythonNdrClassDefiniton):
    """Creates a simple NDRUniFixedArray"""

    def __init__(self, name: str, length: str):
        align = PythonAssignment(PythonValue("align"), PythonValue("1"))
        prop_list = [align]
        props = PythonAssignmentList(*prop_list)
        getDataLen = PythonFunction(
            "getDataLen", args="self,data,offset=0", body=f"return {length}"
        )
        func_list = [getDataLen]
        funcs = PythonFunctionList(*func_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniFixedArray")),
            class_props=props,
            functions=funcs,
        )
