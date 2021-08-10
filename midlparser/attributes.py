import enum

from midl import MidlAttribute
from .base import MidlBaseParser, MidlParserException

class AttributeState(enum.Enum):
    BEGIN = enum.auto()
    DEFAULT = enum.auto()
    PARAMETERS = enum.auto()
    END = enum.auto()

class MidlAttributesParser(MidlBaseParser):
    def __init__(self, token_generator, tokenizer):
        self.state = AttributeState.BEGIN
        super().__init__(token_generator=token_generator, end_state=AttributeState.END, tokenizer=tokenizer)
        self.cur_attr = None
        self.cur_attr_param = ''
        self.cur_attr_params = []
        self.attributes = {}

    def add_to_cur_param(self, token):            
        if self.state != AttributeState.PARAMETERS:
            self.invalid(token)
        self.cur_attr_param += token.data
    
    def symbol(self, token):
        self.add_to_cur_param(token)

    def numeric(self, token):
        self.add_to_cur_param(token)

    def guid(self, token):
        self.add_to_cur_param(token)

    def operator(self, token):
        self.add_to_cur_param(token)

    def sqbracket(self, token):
        if token.data == '[' and self.state == AttributeState.BEGIN:
            self.state = AttributeState.DEFAULT
        elif token.data == ']':
            if self.state != AttributeState.DEFAULT:
                self.invalid(token)
            if self.cur_attr:
                self.attributes[self.cur_attr] = MidlAttribute(self.cur_attr, self.cur_attr_params)
            self.state = AttributeState.END
        else:
            self.invalid(token)
        
    def rbracket(self, token):
        if token.data == '(':
            if self.state == AttributeState.PARAMETERS:
                self.invalid(token)
            self.state = AttributeState.PARAMETERS
        elif token.data == ')':
            if self.state != AttributeState.PARAMETERS:
                self.invalid(token)
            self.state = AttributeState.DEFAULT
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ''

    def comma(self, token):
        if self.state == AttributeState.PARAMETERS:
            # It's legal for this to be None in cases like size_is(,*numActualRecords)
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ''
        elif self.state == AttributeState.DEFAULT and self.cur_attr:
            # End of an attribute
            self.attributes[self.cur_attr] = MidlAttribute(self.cur_attr, self.cur_attr_params)
            self.cur_attr = None
            self.cur_attr_params = []
        else:
            self.invalid(token)

    def keyword(self, token):
        if self.state == AttributeState.PARAMETERS and not self.cur_attr_param:
            self.cur_attr_param = token.data
        elif self.state == AttributeState.DEFAULT and not self.cur_attr:
            self.cur_attr = token.data
        else:
            self.invalid(token)

    def directive(self, _):
        pass

    def string(self, token):
        if self.state == AttributeState.PARAMETERS and not self.cur_attr_param:
            self.cur_attr_param = token.data
        else:
            self.invalid(token)

    def finished(self) -> list[MidlAttribute]:
        if len(self.attributes) == 0:
            raise MidlParserException("No attributes were parsed")
        return self.attributes
