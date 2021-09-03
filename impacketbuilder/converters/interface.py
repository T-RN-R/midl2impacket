from fuzzer.base import NDRINTERFACE
from impacketbuilder.converters.enum import MidlEnumConverter
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
    PythonAssignmentList,
    PythonDictEntry,
    PythonDictEntryList,
    PythonDict,
    PythonValue,
    PythonName,
    PythonTuple,
    PythonClass,
    PythonNameList,
)

from impacketbuilder.ndrbuilder.ndr import PythonNdrStruct, PythonNdrPointer


class MidlInterfaceConverter(Converter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.const_converter = MidlConstantConverter(
            self.io, self.tab_level, self.mapper
        )
        self.imports_converter = MidlImportsConverter(
            self.io, self.tab_level, mapper=self.mapper
        )
        self.proc_converter = MidlProcedureConverter(
            self.io, self.tab_level, mapper=self.mapper
        )

    def convert(self, interface: MidlInterface, import_dir, import_converter):
        if interface.imports:
            self.imports_converter.convert(
                interface.imports, import_dir, import_converter
            )
        # write interface context handles
        interface_names = [interface.name.upper()]
        interface_names.extend([parent.upper() for parent in interface.parents])
        for interface_name in interface_names:
            if not self.mapper.exists(interface_name):
                clz = PythonClass(
                    PythonName(f"{interface.name.upper()}"),
                    PythonNameList(PythonName("CONTEXT_HANDLE")),
                    PythonAssignmentList(
                        PythonAssignment(
                            PythonName("is_ctx_handle"), PythonValue("True")
                        )
                    ),
                )
                self.write(clz.to_python_string())
                self.mapper.add_type(interface_name)

        # write uuid def
        # self.uuid(interface)
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

        iface_uuid = None
        iface_ver = None
        if "uuid" in interface.attributes:
            iface_uuid = interface.attributes["uuid"].params[0]
        if iface_ver := interface.attributes.get("version"):
            iface_ver = iface_ver.params[0]
        else:
            iface_ver = "0.0"
        if not iface_uuid:
            return
        methods = ""
        for proc in interface.procedures:
            methods += proc.name + ","
        self.write(
            f"{interface.name} = NDRINTERFACE('{iface_uuid}', '{iface_ver}',[{methods}])"
        )

    def uuid(self, interface: MidlInterface):
        int_name = f"MSRPC_UUID_{interface.name.upper()}"
        # TODO: Prune forward declarations so they don't end up here
        if "uuid" in interface.attributes:
            iface_uuid = interface.attributes["uuid"].params[0]
            if iface_ver := interface.attributes.get("version"):
                iface_ver = iface_ver.params[0]
                print(iface_ver)
            else:
                iface_ver = "0.0"
            self.write(
                PythonAssignment(
                    PythonValue(int_name),
                    PythonValue(f"uuidtup_to_bin(('{iface_uuid}','{iface_ver}'))"),
                )
            )

    def handle_procedure(self, proc, count):
        self.proc_converter.convert(proc, count)

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

    def handle_handle_td(self,td:MidlTypeDef):
        return self.handle_context_handle(td)

    def handle_midl_td(self, td: MidlTypeDef):
        py_td_type, _ = self.mapper.get_python_type(td.type)
        if isinstance(td, MidlTypeDef):
            if "context_handle" in td.attributes:
                self.handle_context_handle(td)

            else:
                raise Exception(f"Unrecognized type: {td}")
        elif isinstance(td, MidlSimpleTypedef):

            # Context handles are special cases
            if "context_handle" in td.attributes:
                return self.handle_context_handle(td)
            elif "handle" in td.attributes:
                pass
                #return self.handle_handle_td(td)
 
            # Otherwise just create the typedef here
            if td.name.startswith("*"):
                # e.g. typedef RPC_UNICODE_STRING LSA_UNICODE_STRING, *PLSA_UNICODE_STRING
                py_td_name, py_td_name_exists = self.mapper.get_python_type(td.name[1:])
                if not py_td_name_exists:
                    ndr_ptr = PythonNdrPointer(
                        name=py_td_name, referent_name=py_td_type
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

        td_name, td_exists = self.mapper.get_python_type(td.name)
        td_ptr_name = f"P{td_name}"
        if not td_exists:
            structure = PythonTuple(
                PythonTuple([PythonValue("'Data'"), PythonValue("'20s=\"\"'")])
            )
            is_ctx_handle = PythonAssignmentList(
                PythonAssignment(PythonName("is_context_handle"), PythonValue("True"))
            )
            ndr_struct = PythonNdrStruct(
                name=td_name, structure=structure, other_props=is_ctx_handle
            )
            self.write(ndr_struct.to_string())
            self.mapper.add_type(td_name)
        if not self.mapper.exists(td_ptr_name):
            ndr_pointer = PythonNdrPointer(name=td_ptr_name, referent_name=td_name)
            self.write(ndr_pointer.to_string())
            self.mapper.add_type(td_ptr_name)

    def handle_midl_struct(self, td: MidlStructDef):
        struct_converter = MidlStructConverter(
            self.io, self.tab_level, mapper=self.mapper
        )
        struct_converter.convert(td)

    def handle_midl_enum(self, td: MidlEnumDef):
        enum_converter = MidlEnumConverter(self.io, self.tab_level, mapper=self.mapper)
        enum_converter.convert(td)
