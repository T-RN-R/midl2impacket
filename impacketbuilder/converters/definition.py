from impacketbuilder.converters.imports import MidlImportsConverter
from impacketbuilder.converters.comments import MidlCommentWriter
from midl import *

from .base import *
from .constants import MidlConstantConverter
from .interface import MidlInterfaceConverter
from .comments import MidlCommentWriter
from .static import MidlStaticConverter

class MidlDefinitionConverter(Converter):
    def convert(self, definition : MidlDefinition, import_dir:str) -> str:
        const_converter = MidlConstantConverter(self.io, tab_level=self.tab_level, mapper=self.mapper)
        interface_converter = MidlInterfaceConverter(self.io, tab_level=self.tab_level, mapper=self.mapper)
        imports_converter = MidlImportsConverter(self.io, self.tab_level, mapper=self.mapper)
        static_converter = MidlStaticConverter(self.io, self.tab_level, mapper=self.mapper)
        comment_writer = MidlCommentWriter(self.io, self.tab_level)

        static_converter.convert(definition.imports)
        imports_converter.convert(definition.imports, import_dir, self)
        comment_writer.banner_comment("TYPEDEFS")
        for td in definition.typedefs:
            interface_converter.handle_typedef(td)

        if len(definition.instantiation) > 0:
            comment_writer.banner_comment("CONSTANTS")
        for const in definition.instantiation:
            const_converter.convert(const)
        if len(definition.interfaces) > 0:
            comment_writer.banner_comment("INTERFACE DEFINITION")
        for interface in definition.interfaces:
            comment_writer.banner_comment(f"{interface.name} Definition")
            interface_converter.convert(interface)
        return self.io.getvalue()

