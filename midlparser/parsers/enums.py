import enum

from midl import MidlEnumDef
from midlparser.keywords import RHS_OPERATORS
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.tokenizer import Token


class EnumState(enum.Enum):
    BEGIN = enum.auto()
    NAME = enum.auto()
    BODY = enum.auto()
    MEMBER_NAME = enum.auto()
    MEMBER_OP = enum.auto()
    MEMBER_VALUE = enum.auto()
    MEMBER_COMPLETE = enum.auto()
    ENUM_END = enum.auto()
    END = enum.auto()


class MidlEnumParser(MidlBaseParser):
    def __init__(self, token_generator, tokenizer):
        self.state = EnumState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=EnumState.END,
            tokenizer=tokenizer,
        )
        self.private_name = ""
        self.comments = []
        self.declared_names = ""
        self.cur_member_name = None
        self.cur_member_value = ""
        self.map = {}

    def comment(self, token: Token):
        self.comments.append(token)

    def keyword(self, token: Token):
        if self.state == EnumState.BEGIN:
            if token.data != "enum":
                self.invalid(token)
            self.state = EnumState.NAME
        else:
            self.invalid(token)

    def numeric(self, token: Token):
        if self.state == EnumState.MEMBER_VALUE:
            # We need to figure out what kind of integer this is.. TODO: move to a util module?
            # TODO Handle the case where a numeric ends in `L`
            numeric_str = token.data
            if numeric_str[-1] == "L":
                numeric_str = numeric_str[:-1]
            if numeric_str.lower().startswith("0x"):
                numeric_val = int(numeric_str, 16)
            elif numeric_str.lower().startswith("0b"):
                numeric_val = int(numeric_str, 2)
            elif numeric_str.startswith("0"):
                numeric_val = int(numeric_str, 8)
            else:
                numeric_val = int(numeric_str)
            self.cur_member_value = str(numeric_val)
        else:
            self.invalid(token)

    def symbol(self, token: Token):
        if self.state == EnumState.NAME:
            self.private_name = token.data
            self.state = EnumState.BODY
        elif self.state == EnumState.MEMBER_NAME:
            self.cur_member_name = token.data
            self.state = EnumState.MEMBER_OP
        elif self.state == EnumState.ENUM_END:
            self.declared_names += token.data
        elif self.state == EnumState.MEMBER_VALUE:
            self.cur_member_value = token.data
        else:
            self.invalid(token)

    def brace(self, token: Token):
        if token.data == "{" and self.state in [EnumState.BODY, EnumState.NAME]:
            self.state = EnumState.MEMBER_NAME
        elif token.data == "}" and self.state in [
            EnumState.MEMBER_NAME,
            EnumState.MEMBER_OP,
            EnumState.MEMBER_COMPLETE,
            EnumState.MEMBER_VALUE,
        ]:
            if self.state == EnumState.MEMBER_VALUE:
                self.map[self.cur_member_name] = self.cur_member_value
            self.state = EnumState.ENUM_END
        else:
            self.invalid(token)

    def rbracket(self, token: Token):
        if self.state == EnumState.MEMBER_VALUE:
            self.cur_member_value += token.data
        else:
            self.invalid(token)

    def comma(self, token: Token):
        if self.state in [
            EnumState.MEMBER_OP,
            EnumState.MEMBER_COMPLETE,
            EnumState.MEMBER_VALUE,
        ]:
            self.map[self.cur_member_name] = self.cur_member_value
            if type(self.cur_member_value) is int:
                self.cur_member_value += 1
            self.state = EnumState.MEMBER_NAME
        elif self.state == EnumState.ENUM_END:
            self.declared_names += ","
        else:
            self.invalid(token)

    def operator(self, token: Token):
        if token.data == "=" and self.state == EnumState.MEMBER_OP:
            self.state = EnumState.MEMBER_VALUE
        elif token.data == "*" and self.state == EnumState.ENUM_END:
            self.declared_names += "*"
        elif self.state == EnumState.MEMBER_VALUE:
            if token.data in RHS_OPERATORS:
                self.cur_member_value += token.data
            else:
                self.invalid(token)
        else:
            self.invalid(token)

    def semicolon(self, token: Token):
        if self.state == EnumState.ENUM_END:
            self.state = EnumState.END
        else:
            self.invalid(token)

    def finished(self) -> MidlEnumDef:
        if len(self.map.keys()) == 0:
            raise MidlParserException("Parsing enum failed. No members were parsed.")
        public_names = self.declared_names.split(",")
        return MidlEnumDef(public_names, self.private_name, self.map)
