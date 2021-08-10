
import enum
from midl import MidlSimpleTypedef, MidlTypeDef
from .attributes import MidlAttributesParser
from .base import MidlBaseParser, MidlParserException
from .enums import MidlEnumParser
from .structs import MidlStructParser
from .unions import MidlUnionParser

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
        super().__init__(token_generator=token_generator, end_state=TypedefState.END, tokenizer=tokenizer)
        self.attrs = []
        self.td_parts = []
        self.comments = []
        self.cur_additional_name = ''
        self.additional_names = []
        self.tds = []
        self.kw_handlers = {
            'struct': MidlStructParser,
            'enum': MidlEnumParser,
            'union': MidlUnionParser
        }

    def keyword(self, token):
        """Handles the various kinds of typedefs
            TODO: handle unions
        """
        if self.state == TypedefState.BEGIN and token.data == 'typedef':
            self.state = TypedefState.TYPE_OR_ATTRS
        elif self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            if token.data in self.kw_handlers:
                self.state = TypedefState.DEFINITION
                self.tds.append(self.kw_handlers[token.data](self.tokens,self.tokenizer).parse(token))
                self.state = TypedefState.END
            else:
                return self.symbol(token)
        elif self.state == TypedefState.DEFINITION:
            self.symbol(token)
        else:
            self.invalid(token)

    def symbol(self, token):
        if self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            self.td_parts.append(token.data)
            self.state = TypedefState.DEFINITION
        elif self.state == TypedefState.DEFINITION:
            self.td_parts.append(token.data) 
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.cur_additional_name += token.data
        else:
            self.invalid(token)

    def operator(self, token):
        if self.state == TypedefState.DEFINITION and token.data == '*':
            self.td_parts[-1] += '*'
        elif self.state == TypedefState.ADDITIONAL_NAMES and token.data == '*':
            self.cur_additional_name += '*'
        else:
            self.invalid(token)

    def comment(self, token):
        self.comments.append(token)

    def comma(self, token):
        if self.state == TypedefState.DEFINITION:
            self.state = TypedefState.ADDITIONAL_NAMES
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.additional_names.append(self.cur_additional_name)
            self.cur_additional_name = ''
        else:
            self.invalid(token)

    def sqbracket(self, token):
        """ Handles typedef attributes e.g. [v1_enum]
        """
        if self.state == TypedefState.TYPE_OR_ATTRS:
            self.attrs = MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
            self.state = TypedefState.TYPE
        else:
            self.invalid(token)

    def semicolon(self, token):
        if self.state == TypedefState.DEFINITION:
            pass
        elif self.state == TypedefState.ADDITIONAL_NAMES and self.cur_additional_name:
            self.additional_names.append(self.cur_additional_name)
        else:
            self.invalid(token)
        
        self.state = TypedefState.END
        # If we're a simple type we need to create it here
        if not self.tds:
            td_name = self.td_parts[-1]
            td_type = ' '.join(self.td_parts[:-1])
            self.tds.append(MidlSimpleTypedef(td_name, td_type))
            for additional_name in self.additional_names:
                self.tds.append(MidlSimpleTypedef(additional_name, td_type))

    def finished(self) -> list[MidlTypeDef]:
        """parsing loop
        """
        if not len(self.tds):
            raise MidlParserException(f"No typedefs were created.")
        # Slap some attributes on these bad boys
        for td in self.tds:
            td.attrs = self.attrs
        return self.tds
