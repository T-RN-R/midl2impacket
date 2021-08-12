import enum

from midl import MidlCoclass, MidlVarDef
from midlparser.parsers.attributes import MidlAttributesParser
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.tokenizer import Token


class CoclassState(enum.Enum):
    BEGIN = enum.auto()
    NAME = enum.auto()
    BODY = enum.auto()
    ATTR_OR_TYPE = enum.auto()
    TYPE = enum.auto()
    END = enum.auto()


class MidlCoclassParser(MidlBaseParser):
    """Array dimensionality parser
    https://docs.microsoft.com/en-us/windows/win32/midl/midl-arrays
    """

    def __init__(self, token_generator, tokenizer):
        self.state = CoclassState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=CoclassState.END,
            tokenizer=tokenizer,
        )
        self.cur_iface_parts = []
        self.cur_iface_attrs = {}
        self.interfaces = []

    def keyword(self, token: Token):
        if self.state == CoclassState.BEGIN:
            if token.data != "coclass":
                self.invalid()
            self.state = CoclassState.NAME
        elif self.state == CoclassState.NAME:
            self.name = token.data
            self.state = CoclassState.BODY
        elif self.state in [CoclassState.ATTR_OR_TYPE, CoclassState.TYPE]:
            self.cur_iface_parts.append(token.data)
            self.state = CoclassState.TYPE
        else:
            self.invalid(token)

    def symbol(self, token: Token):
        if self.state == CoclassState.NAME:
            self.name = token.data
            self.state = CoclassState.BODY
        elif self.state in [CoclassState.ATTR_OR_TYPE, CoclassState.TYPE]:
            self.cur_iface_parts.append(token.data)
            self.state = CoclassState.TYPE
        else:
            self.invalid(token)

    def brace(self, token: Token):
        if self.state == CoclassState.BODY and token.data == "{":
            self.state = CoclassState.ATTR_OR_TYPE
        elif self.state == CoclassState.ATTR_OR_TYPE and token.data == "}":
            self.state = CoclassState.END
        else:
            self.invalid(token)

    def sqbracket(self, token: Token):
        if self.state == CoclassState.ATTR_OR_TYPE and token.data == "[":
            self.cur_iface_attrs.update(
                MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
            )
        else:
            self.invalid(token)

    def rbracket(self, token: Token):
        if self.state != CoclassState.TYPE:
            self.invalid(token)
        if token.data == "(":
            self.rbracket_level += 1
        elif token.data == ")" and self.rbracket_level >= 1:
            self.rbracket_level -= 1
        else:
            self.invalid(token)
        self.cur_iface_parts += token.data

    def semicolon(self, token: Token):
        if self.state == CoclassState.TYPE:
            cur_iface_name = self.cur_iface_parts[-1]
            cur_iface_type = self.cur_iface_parts[:-1]
            self.interfaces.append(
                MidlVarDef(cur_iface_type, cur_iface_name, self.cur_iface_attrs)
            )
            self.cur_iface_parts = []
            self.cur_iface_attrs = {}
            self.state = CoclassState.ATTR_OR_TYPE
        else:
            self.invalid(token)

    def finished(self) -> MidlCoclass:
        if not self.interfaces:
            raise MidlParserException(f"Empty coclass?")
        return MidlCoclass(self.name, self.interfaces)
