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

    def generate_init_method(self, assignments: PythonAssignmentList) -> PythonFunction:
        func_body_parts = [assn.to_python_string() for assn in assignments.obj_list]
        func_body_parts.append("super().__init__(*args, **kwargs)")
        return PythonFunction(
            name="__init__",
            args="self, *args, **kwargs",
            body=func_body_parts
        )

    def generate_prop_methods(self, props: PythonTuple) -> list[PythonFunction]:
        prop_methods = []
        for prop in props.values:
            prop_name = prop.values[0].value[1:-1]
            prop_type = prop.values[1].value
            if prop_type.startswith("'"):
                prop_type = 'str'
            prop_get = PythonFunction(
                name=prop_name,
                args="self",
                body=[f"return self['{prop_name}']"],
                decorator="@property",
                return_type=prop_type
            )
            prop_methods.append(prop_get)
            prop_set = PythonFunction(
                name=prop_name,
                args=f"self, prop:{prop_type}",
                body=[f"self['{prop_name}'] = prop"],
                decorator=f"@{prop_name}.setter",
            )
            prop_methods.append(prop_set)
        return prop_methods

class PythonNdrStruct(PythonNdrClassDefiniton):
    """Creates a simple NDRSTRUCT"""

    def __init__(self, name: str, structure: PythonTuple, align: str = "1"):
        align_assn = PythonAssignment(PythonName("align"), PythonValue(align))
        structure_assn = PythonAssignment(PythonValue("self.structure"), structure)
        init_props = PythonAssignmentList(structure_assn)
        functions = [self.generate_init_method(init_props)]
        functions.extend(self.generate_prop_methods(structure))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRSTRUCT")),
            class_props=PythonAssignmentList(align_assn),
            functions=PythonFunctionList(*functions),
        )

class PythonNdrPointer(PythonNdrClassDefiniton):
    """Creates a simple NDRPOINTER"""

    def __init__(self, name: str, referent_name: str):
        referent_assn = PythonAssignment(
            PythonName("self.referent"),
            PythonTuple(
                [PythonTuple([PythonValue("'Data'"), PythonValue(referent_name)])]
            ),
        )
        init_props = PythonAssignmentList(referent_assn)
        functions = [self.generate_init_method(init_props)]
        member_props = PythonTuple([PythonTuple([PythonValue("'Data'"), PythonValue(referent_name)])])
        functions.extend(self.generate_prop_methods(member_props))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRPOINTER")),
            functions=PythonFunctionList(*functions),
        )

class PythonNdrUnion(PythonNdrClassDefiniton):
    """Creates a simple NDRUNION"""

    def __init__(self, name: str, union_entries: PythonDictEntryList, tag=None):
        union_assn = PythonAssignment(PythonValue("self.union"), PythonDict(union_entries))
        init_assns = [union_assn]
        if tag:
            commonHdr = PythonAssignment(
                PythonName("self.commonHdr"),

                PythonTuple([PythonTuple([PythonValue("'tag'"), PythonValue(f"{tag}")])]),
            )
            init_assns.append(commonHdr)
        init_assns = PythonAssignmentList(*init_assns)
        functions = [self.generate_init_method(init_assns)]
        union_tup = PythonTuple([x.value for x in  union_entries.obj_list])
        functions.extend(self.generate_prop_methods(union_tup))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUNION")),
            functions=PythonFunctionList(*functions),
        )

class PythonNdrCall(PythonNdrClassDefiniton):
    """Creates a simple NDRCALL"""

    def __init__(self, name: str, structure: PythonTuple, opnum=None):
        init_assns = PythonAssignmentList(PythonAssignment(PythonName("self.structure"), structure))
        functions = PythonFunctionList(self.generate_init_method(init_assns))
        prop_list = []
        if opnum is not None:
            opnum_assn = PythonAssignment(PythonName("opnum"), PythonValue(str(opnum)))
            prop_list.append(opnum_assn)
        prop_list = PythonAssignmentList(*prop_list)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRCALL")),
            class_props=prop_list,
            functions=functions
        )
        
class PythonNdrUniFixedArray(PythonNdrClassDefiniton):
    """Creates a simple NDRUniFixedArray"""

    def __init__(self, name: str, length: str, underlying_type:str):
        init_assns = PythonAssignmentList(PythonAssignment(PythonValue("self.item"), PythonValue(underlying_type)))
        functions = [self.generate_init_method(init_assns)]
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
        functions.extend([get_data_len, get_data])
        functions = PythonFunctionList(*functions)
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniFixedArray")),
            functions=functions,
        )

class PythonNdrUniConformantArray(PythonNdrClassDefiniton):
    """Creates a simple NDRUniConformantArray"""

    def __init__(self, name: str, underlying_type:str):
        init_assns = PythonAssignmentList(PythonAssignment(PythonValue("self.item"), PythonName(underlying_type)))
        functions = PythonFunctionList(self.generate_init_method(init_assns))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniConformantArray")),
            functions=functions
        )

class PythonNdrUniVaryingArray(PythonNdrClassDefiniton):
    """Creates a NDRUniVaryingArray"""

    def __init__(self, name: str, underlying_type:str):
        init_assns = PythonAssignmentList(PythonAssignment(PythonValue("self.item"), PythonName(underlying_type)))
        functions = PythonFunctionList(self.generate_init_method(init_assns))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniVaryingArray")),
            functions=functions
        )

class PythonNdrUniConformantVaryingArray(PythonNdrClassDefiniton):
    """Creates a NDRUniConformantVaryingArray"""

    def __init__(self, name: str, underlying_type:str):
        init_assns = PythonAssignmentList(PythonAssignment(PythonValue("self.item"), PythonName(underlying_type)))
        functions = PythonFunctionList(self.generate_init_method(init_assns))
        self.clazz = PythonClass(
            name=PythonName(name),
            parent_classes=PythonNameList(PythonName("NDRUniConformantVaryingArray")),
            functions=functions
        )