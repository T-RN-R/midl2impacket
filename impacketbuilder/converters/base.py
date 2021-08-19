from impacketbuilder.ndrbuilder.ndr import PythonNdrPointer
from impacketbuilder.ndrbuilder.io import PythonWriter
from io import StringIO
from impacketbuilder.base import Writer
from impacketbuilder.ndrbuilder.io import PythonWriter
from .typing import IDLTypeToPythonType, TypeMapper


class ConversionException(Exception):
    pass


class UnreachableException(Exception):
    pass


class Converter(Writer):
    def __init__(self, io=None, tab_level=0, mapper: TypeMapper = None):
        super().__init__(io, tab_level)
        self.python_writer = PythonWriter(strIO=self.io)
        assert mapper is not None, "Must pass a mapper!"
        self.mapper = mapper

    def convert(self):
        raise UnreachableException(f"Class {__class__} must implement `convert()`")

    def write(self, data: str):
        if not isinstance(data, str):
            data = data.to_python_string()
        for line in data.split("\n"):
            self.single_line_write(line)

    def generate_pointers(self, idl_type, ref_base=None):
        """ Handle the creation of pointer types which aren't explicitly declared in IDL """
        pointer_type = self.mapper.canonicalize(idl_type)
        base_type = idl_type
        pointers_to_create = []
        if not self.mapper.exists(pointer_type):
            if base_type.endswith('*'):
                # Remove trailing '*' and create a pointer type for the corresponding name
                # e.g. GUID* results in a pointer type of PGUID and a base type of GUID
                # while GUID** results in a pointer type of PPGUID with a base type of PGUID*
                # which means we'll need to create pointer types for PGUID and PPGUID
                while base_type.endswith('*'):
                    pointer_type = self.mapper.canonicalize(base_type)
                    pointee_type = self.mapper.canonicalize(base_type[:-1])
                    pointers_to_create.append((pointer_type, pointee_type))
                    base_type = base_type[:-1]
            elif base_type.startswith('*') and ref_base:
                # Remove leading '*' character and create pointer type
                # e.g. *PGUID results in PGUID being created with a reference to GUID
                pointer_type = self.mapper.canonicalize(base_type)
                base_type = base_type[1:]
                pointee_type = self.mapper.canonicalize(ref_base)
                pointers_to_create.append((pointer_type, pointee_type))

            # Go backwards since we create PPGUID before PGUID, for example..
            for pointer_type, pointee_type in pointers_to_create[::-1]:
                if not self.mapper.exists(pointer_type):
                    ndr_ptr = PythonNdrPointer(
                        name=pointer_type, referent_name=pointee_type
                    )
                    self.write(ndr_ptr.to_string())
                    self.mapper.add_entry(pointer_type, pointer_type)
