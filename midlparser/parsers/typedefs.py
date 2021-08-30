import enum

from midltypes import MidlPointerType, MidlSimpleTypedef, MidlTypeDef
from midlparser.parsers.attributes import MidlAttributesParser
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.parsers.enums import MidlEnumParser
from midlparser.parsers.structs import MidlStructParser
from midlparser.parsers.unions import MidlUnionParser
from midlparser.tokenizer import Token


class TypedefState(enum.Enum):
    BEGIN = enum.auto()
    TYPE_OR_ATTRS = enum.auto()
    TYPE = enum.auto()
    DEFINITION = enum.auto()
    ADDITIONAL_NAMES = enum.auto()
    END = enum.auto()


class MidlTypedefParser(MidlBaseParser):
    """Parses the various kinds of typedefs (structs, enums, inline, and unions)"""

    def __init__(self, token_generator, tokenizer):
        self.state = TypedefState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=TypedefState.END,
            tokenizer=tokenizer,
        )
        self.attributes = {}
        self.td_parts = []
        self.is_pointer = False
        self.comments = []
        self.cur_additional_name = ""
        self.additional_names = []
        self.typedefs = []
        self.kw_handlers = {
            "struct": MidlStructParser,
            "enum": MidlEnumParser,
            "union": MidlUnionParser,
        }

    def keyword(self, token: Token):
        """Handles the various kinds of typedefs"""
        if self.state == TypedefState.BEGIN and token.data == "typedef":
            self.state = TypedefState.TYPE_OR_ATTRS
        elif self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            if token.data in self.kw_handlers:
                self.state = TypedefState.DEFINITION
                self.typedefs.extend(
                    self.kw_handlers[token.data](self.tokens, self.tokenizer).parse(
                        token
                    )
                )
                self.state = TypedefState.END
            else:
                return self.symbol(token)
        elif self.state == TypedefState.DEFINITION:
            self.symbol(token)
        else:
            self.invalid(token)

    def symbol(self, token: Token):
        if self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            self.td_parts.append(token.data)
            self.state = TypedefState.DEFINITION
        elif self.state == TypedefState.DEFINITION:
            self.td_parts.append(token.data)
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.cur_additional_name += token.data
        else:
            self.invalid(token)

    def operator(self, token: Token):
        if self.state == TypedefState.DEFINITION and token.data == "*":
            self.td_parts[-1] += "*"
            self.is_pointer = True
        elif self.state == TypedefState.ADDITIONAL_NAMES and token.data == "*":
            self.cur_additional_name += "*"
        else:
            self.invalid(token)

    def comment(self, token: Token):
        self.comments.append(token)

    def comma(self, token: Token):
        if self.state == TypedefState.DEFINITION:
            self.state = TypedefState.ADDITIONAL_NAMES
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.additional_names.append(self.cur_additional_name)
            self.cur_additional_name = ""
        else:
            self.invalid(token)

    def sqbracket(self, token: Token):
        """Handles typedef attributes e.g. [v1_enum]"""
        if self.state == TypedefState.TYPE_OR_ATTRS:
            self.attributes.update(
                MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
            )
        else:
            self.invalid(token)

    def semicolon(self, token: Token):
        if self.state == TypedefState.DEFINITION:
            pass
        elif self.state == TypedefState.ADDITIONAL_NAMES and self.cur_additional_name:
            self.additional_names.append(self.cur_additional_name)
        else:
            self.invalid(token)

        self.state = TypedefState.END
        # If we're a simple type we need to create it here
        if not self.typedefs:
            td_name = self.td_parts[-1]
            td_type = " ".join(self.td_parts[:-1])
            if self.is_pointer:
                td_type = td_type[:-1]
                self.typedefs.append(MidlPointerType(td_name, td_type, self.attributes))
            else:
                self.typedefs.append(MidlSimpleTypedef(td_name, td_type, self.attributes))
            for additional_name in self.additional_names:
                if additional_name.startswith('*'):
                    self.typedefs.append(MidlPointerType(additional_name[1:], td_type, self.attributes))
                else:
                    self.typedefs.append(MidlSimpleTypedef(additional_name, td_type, self.attributes))

    def finished(self) -> list[MidlTypeDef]:
        """parsing loop"""
        if not self.typedefs:
            raise MidlParserException("No typedefs were created.")
        # Slap some attributes on these bad boys
        for typedef in self.typedefs:
            if typedef is not None:
                typedef.attributes.update(self.attributes)
        return self.typedefs
