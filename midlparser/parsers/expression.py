import enum

from midltypes import MidlAttribute
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.tokenizer import Token


class ExpressionState(enum.Enum):
    BEGIN = enum.auto()
    PARAMETERS = enum.auto()
    END = enum.auto()


class MidlExpressionParser(MidlBaseParser):
    def __init__(self, token_generator, tokenizer):
        self.state = ExpressionState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=ExpressionState.END,
            tokenizer=tokenizer,
        )
        self.expression_parts = []

    def add_expression_parts(self, token: Token):
        if self.state != ExpressionState.PARAMETERS:
            self.invalid(token)
        self.expression_parts.append(token.data)

    def symbol(self, token: Token):
        self.add_expression_parts(token)

    def keyword(self, token: Token):
        self.add_expression_parts(token)

    def numeric(self, token: Token):
        self.add_expression_parts(token)

    def guid(self, token: Token):
        self.add_expression_parts(token)

    def operator(self, token: Token):
        self.add_expression_parts(token)

    def string(self, token: Token):
        self.add_expression_parts(token)

    def rbracket(self, token: Token):
        if token.data == "(":
            if self.state == ExpressionState.BEGIN:
                self.expression_parts.append(token.data)
                self.state = ExpressionState.PARAMETERS
            elif self.state == ExpressionState.PARAMETERS:
                # Nested expression
                self.expression_parts.append(
                    MidlExpressionParser(self.tokens, self.tokenizer).parse(token)
                )
            else:
                self.invalid(token)
        elif token.data == ")" and self.state == ExpressionState.PARAMETERS:
            self.expression_parts.append(token.data)
            self.state = ExpressionState.END
        else:
            self.invalid(token)

    def finished(self) -> list[MidlAttribute]:
        if len(self.expression_parts) == 0:
            raise MidlParserException("Empty expression?")
        return " ".join(self.expression_parts)
