import enum

from midltypes import MidlAttribute
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.parsers.util import SkipClosureParser
from midlparser.tokenizer import Token


class AttributeState(enum.Enum):
    BEGIN = enum.auto()
    DEFAULT = enum.auto()
    PARAMETERS = enum.auto()
    END = enum.auto()


class MidlAttributesParser(MidlBaseParser):
    def __init__(self, token_generator, tokenizer):
        self.state = AttributeState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=AttributeState.END,
            tokenizer=tokenizer,
        )
        self.cur_attr = None
        self.cur_attr_param = ""
        self.cur_attr_params = []
        self.attributes = {}

    def add_to_cur_param(self, token: Token):
        if self.state != AttributeState.PARAMETERS:
            self.invalid(token)
        self.cur_attr_param += token.data

    def symbol(self, token: Token):
        self.add_to_cur_param(token)

    def numeric(self, token: Token):
        self.add_to_cur_param(token)

    def guid(self, token: Token):
        self.add_to_cur_param(token)

    def operator(self, token: Token):
        self.add_to_cur_param(token)

    def sqbracket(self, token: Token):
        if token.data == "[" and self.state == AttributeState.BEGIN:
            self.state = AttributeState.DEFAULT
        elif token.data == "]":
            if self.state != AttributeState.DEFAULT:
                self.invalid(token)
            if self.cur_attr:
                self.attributes[self.cur_attr] = MidlAttribute(
                    self.cur_attr, self.cur_attr_params
                )
            self.state = AttributeState.END
        else:
            self.invalid(token)

    def rbracket(self, token: Token):
        if token.data == "(":
            if self.state == AttributeState.DEFAULT:
                self.state = AttributeState.PARAMETERS
            elif self.state == AttributeState.PARAMETERS:
                # Just grab the whole blob and add it to the current member
                self.cur_attr_param += SkipClosureParser(
                    self.tokens, self.tokenizer, closure_open="(", closure_close=")"
                ).parse(token)
            else:
                self.invalid(token)
        elif token.data == ")" and self.state == AttributeState.PARAMETERS:
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ""
            self.state = AttributeState.DEFAULT
        else:
            self.invalid(token)

    def comma(self, token: Token):
        if self.state == AttributeState.PARAMETERS:
            # It's legal for this to be None in cases like size_is(,*numActualRecords)
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ""
        elif self.state == AttributeState.DEFAULT and self.cur_attr:
            # End of an attribute
            self.attributes[self.cur_attr] = MidlAttribute(
                self.cur_attr, self.cur_attr_params
            )
            self.cur_attr = None
            self.cur_attr_params = []
        else:
            self.invalid(token)

    def keyword(self, token: Token):
        if self.state == AttributeState.PARAMETERS:
            self.add_to_cur_param(token)
        elif self.state == AttributeState.DEFAULT and not self.cur_attr:
            self.cur_attr = token.data
        else:
            self.invalid(token)

    def comment(self, _):
        pass

    def string(self, token: Token):
        if self.state == AttributeState.PARAMETERS:
            self.cur_attr_param += token.data
        else:
            self.invalid(token)

    def finished(self) -> list[MidlAttribute]:
        if len(self.attributes) == 0:
            raise MidlParserException("No attributes were parsed")
        return self.attributes
