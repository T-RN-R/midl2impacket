from impacketbuilder.converters.typing import TypeMapper
from impacketbuilder.converters.constants import MidlConstantConverter
from impacketbuilder.converters.imports import MidlImportsConverter
from .base import Converter
from .struct import MidlStructConverter
from .procedure import MidlProcedureConverter
from midltypes import (
    MidlInterface,
    MidlTypeDef,
    MidlSimpleTypedef,
    MidlStructDef,
    MidlUnionDef,
    MidlEnumDef,
    MidlVarDef,
)
from impacketbuilder.ndrbuilder.python import (
    PythonAssignment,
    PythonDictEntry,
    PythonDictEntryList,
    PythonDict,
    PythonValue,
    PythonName,
    PythonTuple,
)

from impacketbuilder.ndrbuilder.ndr import PythonNdrStruct, PythonNdrPointer


class MidlInterfaceConverter(Converter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.const_converter = MidlConstantConverter(self.io, self.tab_level, self.mapper)
        self.imports_converter = MidlImportsConverter(self.io, self.tab_level, mapper=self.mapper)
        self.proc_converter = MidlProcedureConverter(self.io, self.tab_level, mapper=self.mapper)


    def convert(self, interface, import_dir, import_converter):
        if interface.imports:
            self.imports_converter.convert(
                interface.imports, import_dir, import_converter
            )
        # write uuid def
        self.uuid(interface)
        for vd in interface.vardefs:
            self.handle_vardef(vd)
        for td in interface.typedefs:
            self.handle_typedef(td)

        count = 0
        mapping = {}
        for proc in interface.procedures:
            self.handle_procedure(proc, count)
            mapping[proc.name] = proc.name + "Response"
            count += 1

        dentries = []
        count = 0
        for k in mapping:
            dentries.append(
                PythonDictEntry(
                    PythonValue(count),
                    PythonTuple([PythonValue(k), PythonValue(mapping[k])]),
                )
            )
            count += 1

        rhs = PythonDict(PythonDictEntryList(*dentries))
        opnum_map = PythonAssignment(PythonName("OPNUMS"), rhs)

        self.write(opnum_map)

    def uuid(self, interface: MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"
        if "uuid" in interface.attributes:
            self.write(
                PythonAssignment(
                    PythonValue(int_name),
                    PythonValue(
                        f"uuidtup_to_bin(('{interface.attributes['uuid'].params[0]}','0.0'))"
                    ),
                )
            )

    def handle_procedure(self, proc, count):
        self.proc_converter.convert(
            proc, count
        )

    def handle_typedef(self, td):
        if isinstance(td, MidlTypeDef):
            self.handle_midl_td(td)
        elif isinstance(td, (MidlStructDef, MidlUnionDef)):
            self.handle_midl_struct(td)
        elif isinstance(td, MidlEnumDef):
            self.handle_midl_enum(td)
        elif isinstance(td, MidlSimpleTypedef):
            self.handle_midl_td(td)
        else:
            raise Exception(
                f"MidlInterfaceConverter: Unhandled typedef type: {td.__class__}"
            )

    def handle_vardef(self, vd: MidlVarDef):
        self.const_converter.convert(vd)

    def handle_midl_td(self, td: MidlTypeDef):
        py_td_type, _ = self.mapper.get_python_type(td.type)
        if isinstance(td, MidlTypeDef):
            if "context_handle" in td.attributes:
                self.handle_context_handle(td)
            else:
                print("skipping??")
        elif isinstance(td, MidlSimpleTypedef):
            if td.name.startswith('*'):
                # e.g. typedef RPC_UNICODE_STRING LSA_UNICODE_STRING, *PLSA_UNICODE_STRING
                py_td_name, py_td_name_exists = self.mapper.get_python_type(td.name[1:])
                if not py_td_name_exists:
                    ndr_ptr = PythonNdrPointer(
                        name=py_td_name,
                        referent_name=py_td_type
                    )
                    self.write(ndr_ptr.to_string())
            else:
                py_td_name, py_td_name_exists = self.mapper.get_python_type(td.name)

                if not py_td_name_exists:
                    self.write(
                        PythonAssignment(
                            PythonValue(py_td_name),
                            PythonValue(py_td_type),
                        )
                    )

            self.mapper.add_type(py_td_name)

    def handle_context_handle(self, td):
        pointer_name = td.name
        real_name = td.name
        if td.name[0] == "P":
            real_name = td.name[1:]

        structure = PythonTuple(
            PythonTuple([PythonValue("'Data'"), PythonValue("'20s=\"\"'")])
        )
        ndr_struct = PythonNdrStruct(name=real_name, structure=structure)
        self.write(ndr_struct.to_string())

        ndr_pointer = PythonNdrPointer(name=pointer_name, referent_name=real_name)
        self.write(ndr_pointer.to_string())

    def handle_midl_struct(self, td: MidlStructDef):
        struct_converter = MidlStructConverter(
            self.io, self.tab_level, mapper=self.mapper
        )
        struct_converter.convert(td)

    def handle_midl_enum(self, td: MidlEnumDef):
        if len(td.public_names) > 0:
            if td.public_names[0] == "":
                self.write(
                    PythonAssignment(
                        PythonName(td.private_name.upper()), PythonValue("DWORD__ENUM")
                    )
                )
            else:
                # If it has a public name, the enum may be used inside of an interface definition, so create a typdef for it to "DWORD__ENUM"
                self.write(
                    PythonAssignment(
                        PythonName(td.public_names[0].upper()),
                        PythonValue("DWORD__ENUM"),
                    )
                )
        else:
            self.write(
                PythonAssignment(
                    PythonName(td.private_name.upper()), PythonValue("DWORD__ENUM")
                )
            )

        val = td.map[list(td.map.keys())[0]]
        # Handle the case where the first enum entry has no value.
        if val == None or val == "" or val == "0":
            # default enum value case
            value = 0
            for key in td.map.keys():
                val = td.map[key]
                if val == None or val == "" or val == "0":
                    td.map.update({key: value})
                    value += 1
                else:
                    td.map.update({key: val})
                    value += 1

        for key in td.map.keys():
            val = td.map[key]
            enum = PythonAssignment(PythonName(key), PythonValue(str(val)))
            self.write(enum)
