import enum
from midlparser.parsers.expression import MidlExpressionParser

from midltypes import MidlAttribute, SizeIsAttribute
from midlparser.parsers.base import MidlBaseParser, MidlParserException
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
        self.cur_attr_name = None
        self.cur_attr_param_parts = []
        self.cur_attr_params = []
        self.attributes = {}
        self.attr_handlers = {
            "size_is": self.size_is,
        }

    def add_to_cur_param(self, token: Token):
        if self.state != AttributeState.PARAMETERS:
            self.invalid(token)
        self.cur_attr_param_parts.append(token.data)

    def symbol(self, token: Token):
        self.add_to_cur_param(token)

    def numeric(self, token: Token):
        self.add_to_cur_param(token)

    def guid(self, token: Token):
        self.add_to_cur_param(token)

    def operator(self, token: Token):
        self.add_to_cur_param(token)

    def string(self, token: Token):
        self.add_to_cur_param(token)

    def guid(self, token: Token):
        self.add_to_cur_param(token)

    def finish_param(self):
        self.cur_attr_params.append(' '.join(self.cur_attr_param_parts))
        self.cur_attr_param_parts = []

    def sqbracket(self, token: Token):
        if token.data == "[" and self.state == AttributeState.BEGIN:
            self.state = AttributeState.DEFAULT
        elif token.data == "]":
            if self.state != AttributeState.DEFAULT:
                self.invalid(token)
            if self.cur_attr_name:
                self.attributes[self.cur_attr_name] = MidlAttribute(
                    self.cur_attr_name, self.cur_attr_params
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
                self.cur_attr_param_parts.append(MidlExpressionParser(
                    self.tokens, self.tokenizer).parse(token))
            else:
                self.invalid(token)
        elif token.data == ")" and self.state == AttributeState.PARAMETERS:
            self.finish_param()
            self.state = AttributeState.DEFAULT
        else:
            self.invalid(token)

    def comma(self, token: Token):
        if self.state == AttributeState.PARAMETERS:
            # It's legal for this to be None in cases like size_is(,*numActualRecords)
            self.finish_param()
        elif self.state == AttributeState.DEFAULT and self.cur_attr_name:
            # End of an attribute
            self.attributes[self.cur_attr_name] = MidlAttribute(
                self.cur_attr_name, self.cur_attr_params
            )
            self.cur_attr_name = None
            self.cur_attr_params = []
        else:
            self.invalid(token)

    def keyword(self, token: Token):
        if self.state == AttributeState.PARAMETERS:
            self.add_to_cur_param(token)
        elif self.state == AttributeState.DEFAULT and not self.cur_attr_name:
            self.cur_attr_name = token.data
        else:
            self.invalid(token)

    def comment(self, _):
        pass

    def size_is(self, attribute: MidlAttribute):
        return SizeIsAttribute(attribute.name, attribute.params)

    def default(self, attribute: MidlAttribute):
        return attribute

    def finished(self) -> dict[str:MidlAttribute]:
        if len(self.attributes) == 0:
            raise MidlParserException("No attributes were parsed")
        # Post-process attributes
        for name, attr in self.attributes.items():
            self.attributes[name] = self.attr_handlers.get(name, self.default)(attr)
        return self.attributes
