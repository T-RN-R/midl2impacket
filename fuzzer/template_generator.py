from midltypes import MidlDefinition
from impacketbuilder.converters.typing import TypeMapper

class FuzzerTemplateGenerator:
    """A class that generates fuzzing templates"""

    def __init__(self):
        self.generated_classes = {}
        self.mapper = TypeMapper(None)

    def generate(self, midl_def: MidlDefinition, import_dir):
        """Generates a Python file that is a fuzzing template"""
        #TODO handle imports
        output = ""

        static_imports = """
from fuzzer.midl import *
from fuzzer.core import *
"""
        output += static_imports
        cnt = 0
        first_uuid = None
        #TODO generate struct defs first, before generating interface defs

        for interface in midl_def.interfaces:
            if "uuid" in interface.attributes and first_uuid is None:
                first_uuid = interface.attributes["uuid"].params[0]
            interface = self.generate_interface(interface)
            if interface != "":
                output += f"interface_{cnt} = {interface}\n"
                cnt += 1

        return output, first_uuid

    def generate_interface(self, midl_interface):
        output = ""
        if len(midl_interface.attributes) == 0:
            return ""
        uuid = midl_interface.attributes["uuid"].params[0]
        if "version" in midl_interface.attributes:
            version = midl_interface.attributes["version"].params[0]
        else:
            version = "1.0"
        procedures = ""
        for proc in midl_interface.procedures:
            procedures += f"{self.generate_procedure(proc)},\n"
        output += f"Interface(\"{uuid}\", \"{version}\",[\n{procedures}])"
        return output

    def generate_procedure(self,procedure):
        output = ""
        params = ""
        for param in procedure.params:
            input_attr  = "in" in param.attributes
            output_attr = "out" in param.attributes
            clz = "InOut" if input_attr and output_attr else ("Out" if output_attr else "In")
            #TODO canonicalize types!
            params += f"{clz}({self.mapper.canonicalize(param.type)[0]}),\n"
        output += f"Method(\"{procedure.name}\",\n{params})"
        return output