from impacket.dcerpc.v5.ndr import NDRPOINTER
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
        prop_functions = self.generate_prop_functions(structure)
        props = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRSTRUCT")),
            class_props=props,
            functions=prop_functions,
        )

    def generate_prop_functions(self, structure: PythonTuple) -> PythonFunctionList:
        prop_functions = []
        for struct_member in structure.rhs.values:
            prop_name = struct_member.values[0].value[1:-1]
            prop_type = struct_member.values[1].value
            if prop_type.startswith("'"):
                prop_type = 'str'
            prop_get_fn = PythonFunction(
                name=prop_name,
                args="self",
                body=[f"return self['{prop_name}']"],
                decorator="@property",
                return_type=prop_type
            )
            prop_functions.append(prop_get_fn)
            prop_set_fn = PythonFunction(
                name=prop_name,
                args=f"self, prop:{prop_type}",
                body=[f"self['{prop_name}'] = prop"],
                decorator=f"@{prop_name}.setter",
            )
            prop_functions.append(prop_set_fn)
        return PythonFunctionList(*prop_functions)


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
        prop_functions = self.generate_prop_functions(referent_name)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRPOINTER")),
            class_props=props,
            functions=prop_functions,
        )

    def generate_prop_functions(self, referent_type:str):
        prop_setter = PythonFunction(
            name="Data",
            args=f"self, prop:{referent_type}",
            body=["self['Data'] = prop"],
            decorator="@Data.setter",
        )
        prop_getter = PythonFunction(
            name="Data",
            args="self",
            body=["return self['Data']"],
            decorator="@property",
            return_type=referent_type
        )
        return PythonFunctionList(prop_getter, prop_setter)


class PythonNdrUnion(PythonNdrClassDefiniton):
    """Creates a simple NDRUNION"""

    def __init__(self, name: str, union_entries: PythonDictEntryList, tag=None):
        prop_list = []
        if tag:
            commonHdr = PythonAssignment(
                PythonName("commonHdr"),

                PythonTuple([PythonTuple([PythonValue(f"'tag'"), PythonValue(f"{tag}")])]),
            )
            prop_list.append(commonHdr)
        structure = PythonAssignment(PythonValue("union"), PythonDict(union_entries))
        prop_list.append(structure)
        props = PythonAssignmentList(*prop_list)
        prop_functions = self.generate_prop_functions(structure)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUNION")),
            class_props=props,
            functions=prop_functions,
        )

    def generate_prop_functions(self, union_entries: PythonDictEntryList) -> PythonFunctionList:
        prop_functions = []
        for union_member in union_entries.rhs.entries.obj_list:
            prop_name = union_member.value.values[0].value[1:-1]
            prop_type = union_member.value.values[1].value
            if prop_type.startswith("'"):
                prop_type = 'str'
            prop_get_fn = PythonFunction(
                name=prop_name,
                args="self",
                body=[f"return self['{prop_name}']"],
                decorator="@property",
                return_type=prop_type
            )
            prop_functions.append(prop_get_fn)
            prop_set_fn = PythonFunction(
                name=prop_name,
                args=f"self, prop:{prop_type}",
                body=[f"self['{prop_name}'] = prop"],
                decorator=f"@{prop_name}.setter",
            )
            prop_functions.append(prop_set_fn)
        return PythonFunctionList(*prop_functions)

class PythonNdrCall(PythonNdrClassDefiniton):
    """Creates a simple NDRCALL"""

    def __init__(self, name: str, structure: PythonTuple, opnum=None):
        structure = PythonAssignment(PythonName("structure"), structure)
        if opnum is not None:
            opnum_assn = PythonAssignment(PythonName("opnum"), PythonValue(str(opnum)))
            prop_list = [opnum_assn, structure]
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

    def __init__(self, name: str, length: str, underlying_type):
        item = PythonAssignment(PythonValue("item"), PythonValue(underlying_type))
        prop_list = [item]
        props = PythonAssignmentList(*prop_list)
        get_data_len = PythonFunction(
            "getDataLen", args="self, data, offset=0", body=[
                "type_size = len(self.item())",
                f"return {length} * type_size"
            ]
        )
        get_data = PythonFunction(
            "getData", args="self, _", body=[
                "# This is the length of our fixed array",
                "containerLength = self.getDataLen(None)",
                "# Truncate extra data provided beyond the maximum length",
                "raw = self.fields['Data'][:containerLength]",
                "# Add padding if necessary",
                "paddingLength = containerLength - (len(raw) % containerLength)",
                "raw += b'\\x00' * paddingLength",
                "return raw"
            ]
        )
        func_list = [get_data_len, get_data]
        funcs = PythonFunctionList(*func_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniFixedArray")),
            class_props=props,
            functions=funcs,
        )
