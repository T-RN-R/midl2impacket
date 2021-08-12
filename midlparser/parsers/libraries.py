import enum

from midl import MidlLibrary
from midlparser.parsers.attributes import MidlAttributesParser
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.parsers.coclass import MidlCoclassParser
from midlparser.parsers.variables import MidlVariableInstantiationParser
from midlparser.tokenizer import Token


class LibraryState(enum.Enum):
    """Class used to handle state transitions for MidlInterfaceParser"""

    BEGIN = enum.auto()
    NAME = enum.auto()
    BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    END = enum.auto()


class MidlLibraryParser(MidlBaseParser):
    """Responsible for parsing an interface definiton.

    Mostly, this class delegates to other classes to handle parsing
    """

    def __init__(self, token_generator, tokenizer):
        self.tokens = token_generator
        super().__init__(
            token_generator=token_generator,
            end_state=LibraryState.END,
            tokenizer=tokenizer,
        )
        self.library = MidlLibrary()
        self.state = LibraryState.BEGIN
        self.cur_member_attrs = {}

    def sqbracket(self, token: Token):
        """Handle attributes for procedures"""
        if token.data == "[" and self.state == LibraryState.MEMBER_TYPE_OR_ATTR:
            self.cur_member_attrs.update(
                MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
            )
        else:
            self.invalid(token)

    def comment(self, token: Token):
        self.library.comments.append(token)

    def default_type_handler(self, token: Token):
        if self.cur_member_attrs:
            self.invalid(token)
        self.library.members.append(
            MidlVariableInstantiationParser(self.tokens, self.tokenizer).parse(token)
        )
        self.cur_member_attrs = {}
        self.state = LibraryState.MEMBER_TYPE_OR_ATTR

    def keyword(self, token):
        if token.data == "library" and self.state == LibraryState.BEGIN:
            self.state = LibraryState.NAME
        elif self.state in [LibraryState.MEMBER_TYPE_OR_ATTR, LibraryState.MEMBER_TYPE]:
            if token.data == "coclass":
                coclass = MidlCoclassParser(self.tokens, self.tokenizer).parse(token)
                coclass.attributes = self.cur_member_attrs
                self.library.members.append(coclass)
                self.cur_member_attrs = {}
                self.state = LibraryState.MEMBER_TYPE_OR_ATTR
            else:
                self.default_type_handler(token)
        else:
            self.invalid(token)

    def symbol(self, token: Token):
        if self.state == LibraryState.NAME:
            self.library.name = token.data
            self.state = LibraryState.BODY
        elif self.state in [LibraryState.MEMBER_TYPE_OR_ATTR, LibraryState.MEMBER_TYPE]:
            self.default_type_handler(token)

    def brace(self, token: Token):
        if token.data == "{" and self.state == LibraryState.BODY:
            self.state = LibraryState.MEMBER_TYPE_OR_ATTR
        elif (
            token.data == "}"
            and self.state == LibraryState.MEMBER_TYPE_OR_ATTR
            and not self.cur_member_attrs
        ):
            self.state = LibraryState.END
        else:
            self.invalid(token)

    def finished(self) -> MidlLibrary:
        """Parsing loop"""
        if not self.library:
            raise MidlParserException(f"Failed to parse library!")
        return self.library
