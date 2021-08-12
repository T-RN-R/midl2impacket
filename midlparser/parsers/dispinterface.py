import enum

from midl import MidlDispInterface, MidlVariableInstantiation
from midlparser.parsers.attributes import MidlAttributesParser
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.parsers.procedures import MidlProcedureParser
from midlparser.tokenizer import Token, TokenType


class DispInterfaceState(enum.Enum):
    """Class used to handle state transitions for MidlInterfaceParser"""

    BEGIN = enum.auto()
    NAME = enum.auto()
    BODY = enum.auto()
    DEFINITION = enum.auto()
    PROP_ATTR_OR_TYPE = enum.auto()
    PROP_TYPE = enum.auto()
    METHOD_ATTR_OR_TYPE = enum.auto()
    METHOD_TYPE = enum.auto()
    END = enum.auto()


class MidlDispInterfaceParser(MidlBaseParser):
    """Responsible for parsing an interface definiton.

    Mostly, this class delegates to other classes to handle parsing
    """

    def __init__(self, token_generator, tokenizer):
        self.tokens = token_generator
        super().__init__(
            token_generator=token_generator,
            end_state=DispInterfaceState.END,
            tokenizer=tokenizer,
        )
        self.dispinterface = MidlDispInterface()
        self.state = DispInterfaceState.BEGIN
        self.brace_level = 0
        self.cur_method_attrs = {}
        self.cur_prop_attrs = {}

    def sqbracket(self, token: Token):
        """Handle attributes for procedures"""
        if token.data == "[":
            if self.state == DispInterfaceState.PROP_ATTR_OR_TYPE:
                self.cur_prop_attrs.update(
                    MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
                )
            elif self.state == DispInterfaceState.METHOD_ATTR_OR_TYPE:
                self.cur_method_attrs.update(
                    MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
                )
                self.state = DispInterfaceState.METHOD_TYPE
            else:
                self.invalid(token)
        else:
            self.invalid(token)

    def comment(self, token: Token):
        self.dispinterface.comments.append(token)

    def keyword(self, token: Token):
        if token.data == "dispinterface" and self.state == DispInterfaceState.BEGIN:
            self.state = DispInterfaceState.NAME
        elif token.data == "properties" and self.state in [
            DispInterfaceState.DEFINITION,
            DispInterfaceState.METHOD_ATTR_OR_TYPE,
        ]:
            next_token = next(self.tokens)
            assert next_token.type == TokenType.OPERATOR and next_token.data == ":"
            self.state = DispInterfaceState.PROP_ATTR_OR_TYPE
        elif token.data == "methods" and self.state in [
            DispInterfaceState.DEFINITION,
            DispInterfaceState.PROP_ATTR_OR_TYPE,
        ]:
            next_token = next(self.tokens)
            assert next_token.type == TokenType.OPERATOR and next_token.data == ":"
            self.state = DispInterfaceState.METHOD_ATTR_OR_TYPE
        elif self.state in [
            DispInterfaceState.METHOD_ATTR_OR_TYPE,
            DispInterfaceState.METHOD_TYPE,
        ]:
            # Procedure declaration return type
            method = MidlProcedureParser(self.tokens, self.tokenizer).parse(token)
            if method:
                method.attributes = self.cur_method_attrs
                self.dispinterface.methods.append(method)
            self.cur_method_attrs = {}
            self.state = DispInterfaceState.METHOD_ATTR_OR_TYPE
        elif self.state in [
            DispInterfaceState.PROP_ATTR_OR_TYPE,
            DispInterfaceState.PROP_TYPE,
        ]:
            # Procedure declaration return type
            prop = MidlVariableInstantiation(self.tokens, self.tokenizer).parse(token)
            if prop:
                prop.attributes = self.cur_prop_attrs
                self.dispinterface.properties.append(prop)
            self.cur_prop_attrs = {}
            self.state = DispInterfaceState.PROP_ATTR_OR_TYPE
        else:
            self.invalid(token)

    def symbol(self, token: Token):
        if self.state == DispInterfaceState.NAME:
            self.dispinterface.name = token.data
            self.state = DispInterfaceState.BODY
        elif self.state in [
            DispInterfaceState.METHOD_ATTR_OR_TYPE,
            DispInterfaceState.METHOD_TYPE,
        ]:
            # Procedure declaration return type
            method = MidlProcedureParser(self.tokens, self.tokenizer).parse(token)
            if method:
                method.attributes = self.cur_method_attrs
                self.dispinterface.methods.append(method)
            self.cur_method_attrs = {}
            self.state = DispInterfaceState.METHOD_ATTR_OR_TYPE
        elif self.state in [
            DispInterfaceState.PROP_ATTR_OR_TYPE,
            DispInterfaceState.PROP_TYPE,
        ]:
            # Procedure declaration return type
            prop = MidlVariableInstantiation(self.tokens, self.tokenizer).parse(token)
            if prop:
                prop.attributes = self.cur_prop_attrs
                self.dispinterface.properties.append(prop)
            self.cur_prop_attrs = {}
            self.state = DispInterfaceState.PROP_ATTR_OR_TYPE
        else:
            self.invalid(token)

    def brace(self, token: Token):
        if token.data == "{" and self.state == DispInterfaceState.BODY:
            self.state = DispInterfaceState.DEFINITION
        elif token.data == "}" and self.state in [
            DispInterfaceState.DEFINITION,
            DispInterfaceState.PROP_ATTR_OR_TYPE,
            DispInterfaceState.METHOD_ATTR_OR_TYPE,
        ]:
            self.state = DispInterfaceState.END
        else:
            self.invalid(token)

    def finished(self) -> MidlDispInterface:
        """Parsing loop"""
        if not self.dispinterface:
            raise MidlParserException(f"Failed to parse interface!")
        return self.dispinterface
