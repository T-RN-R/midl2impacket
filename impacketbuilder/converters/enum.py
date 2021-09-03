from impacketbuilder.ndrbuilder.ndr import PythonNdrPointer
from impacketbuilder.ndrbuilder.python import PythonAssignment
from midltypes import MidlEnumDef
from .base import ConversionException, Converter
from impacketbuilder.ndrbuilder.python import PythonAssignment, PythonValue, PythonName


class MidlEnumConverter(Converter):
    def convert(self, enum_def : MidlEnumDef) -> str:
        enum_private_name = self.mapper.get_python_type(enum_def.private_name)[0]
        if enum_def.public_names:
            enum_name = self.mapper.get_python_type(enum_def.public_names[0])[0]
        else:
            enum_name = enum_private_name
        # Create the enum type

        self.write(
            PythonAssignment(
                PythonName(enum_name),
                PythonValue("DWORD__ENUM"),
            )
        )
        self.mapper.add_type(enum_name)
        # This is for handling forward declarations
        if enum_name != enum_private_name and enum_private_name != "":
            self.write(
                PythonAssignment(
                    PythonName(enum_private_name),
                    PythonValue(enum_name),
                )
            )

        # Handle other public names and pointers:
        if len(enum_def.public_names) > 1:
            for public_name in enum_def.public_names[1:]:
                star_count = public_name.count("*")
                if star_count == 1:
                    pointer_name = self.mapper.get_python_type(public_name[1:])[0]
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_name, referent_name=enum_name
                    )
                    self.write(ndr_ptr.to_string())
                    self.mapper.add_type(pointer_name)
                elif star_count == 0:
                    alias_name = self.mapper.get_python_type(public_name)[0]
                    self.write(
                        PythonAssignment(
                            PythonName(alias_name),
                            PythonValue(enum_name),
                        )
                    )
                    self.mapper.add_type(alias_name)
                else:
                    raise ConversionException(
                        f"Multiple asterisks encountered in name: {public_name}"
                    )

        # Write the values
        val = enum_def.map[list(enum_def.map.keys())[0]]
        # Handle the case where the first enum entry has no value.
        if val == None or val == "" or val == "0":
            # default enum value case
            value = 0
            for key in enum_def.map.keys():
                val = enum_def.map[key]
                if val == None or val == "" or val == "0":
                    enum_def.map.update({key: value})
                    value += 1
                else:
                    enum_def.map.update({key: val})
                    value += 1
        enum_items = ""
        for key in enum_def.map.keys():
            val = enum_def.map[key]
            enum_items += f"        {key} = {val}\n"
            enum = PythonAssignment(PythonName(key), PythonValue(str(val)))
            self.write(enum)


        clz = f"""
class {enum_name}(NDRENUM):
    class enumItems(Enum):
{enum_items}
"""
        self.write(clz)
