import enum
import string

from midltypes import MidlEnumDef
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
        self.prev_member_value = "-1"
        self.cur_sym_counter = 1
        self.map = {}

    def add_member(self):
        if not self.cur_member_value:
            # We didn't have a value specified. Set it to the previous member value and increment
            self.cur_member_value = self.prev_member_value
            cv = (
                self.cur_member_value[1:]
                if self.cur_member_value.startswith("-")
                else self.cur_member_value
            )
            if cv.isnumeric():
                self.cur_member_value = str(int(self.cur_member_value) + 1)
                self.cur_sym_counter = 0
            else:
                # The previous member is a symbol.. Just increment based on a counter
                self.cur_member_value = (
                    self.cur_member_value + f" + {self.cur_sym_counter}"
                )
                self.cur_sym_counter += 1
        self.map[self.cur_member_name] = self.cur_member_value
        self.prev_member_value = self.cur_member_value
        self.state = EnumState.MEMBER_NAME
        self.cur_member_value = ""

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
            numeric_str = token.data
            is_negative = False
            # Parse
            if numeric_str.startswith("-"):
                is_negative = True
                numeric_str = numeric_str[1:]
            # Strip off integer suffixes (U,u,L,l)
            while numeric_str[-1].lower() in ["u", "l"]:
                numeric_str = numeric_str[:-1]
            # Convert
            if numeric_str.lower().startswith("0x"):
                numeric_val = int(numeric_str, 16)
            elif numeric_str.lower().startswith("0b"):
                numeric_val = int(numeric_str, 2)
            elif numeric_str.startswith("0"):
                numeric_val = int(numeric_str, 8)
            elif numeric_str[0] in string.digits:
                numeric_val = int(numeric_str)
            else:
                self.invalid(token)
            self.cur_member_value += str(numeric_val)
            if is_negative:
                self.cur_member_value += '-' + self.cur_member_value
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
            self.cur_member_value += token.data
        else:
            self.invalid(token)

    def brace(self, token: Token):
        if token.data == "{" and self.state in [EnumState.BODY, EnumState.NAME]:
            self.state = EnumState.MEMBER_NAME
        elif token.data == "}" and self.state in [
            EnumState.MEMBER_NAME,
            EnumState.MEMBER_OP,
            EnumState.MEMBER_VALUE,
        ]:
            if self.state == EnumState.MEMBER_OP or (
                self.state == EnumState.MEMBER_VALUE and self.cur_member_value
            ):
                self.add_member()
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
            EnumState.MEMBER_VALUE,
        ]:
            self.add_member()
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
