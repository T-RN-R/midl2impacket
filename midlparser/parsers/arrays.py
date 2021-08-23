import enum

from midltypes import MidlArrayDimensions
from midlparser.parsers.expression import MidlBaseParser, MidlExpressionParser
from midlparser.tokenizer import Token


class ArrayState(enum.Enum):
    BEGIN = enum.auto()
    RANGE_MIN = enum.auto()
    RANGE_MIN_IN_PROGRESS = enum.auto()
    RANGE_MAX = enum.auto()
    RANGE_MAX_IN_PROGRESS = enum.auto()
    END = enum.auto()


class MidlArrayParser(MidlBaseParser):
    """Array dimensionality parser
    https://docs.microsoft.com/en-us/windows/win32/midl/midl-arrays
    """

    def __init__(self, token_generator, tokenizer):
        self.state = ArrayState.BEGIN
        super().__init__(
            token_generator=token_generator,
            end_state=ArrayState.END,
            tokenizer=tokenizer,
        )
        self.dimensions = ["", ""]  # min, max
        self.cur_dim = ""
        self.rbracket_level = 0
        self.defined_max = False

    def add_data_to_dimension(self, token: Token):
        if self.state not in [ArrayState.BEGIN, ArrayState.END]:
            # Mark that we have *some* data for the current dimension
            if self.state == ArrayState.RANGE_MIN:
                self.state = ArrayState.RANGE_MIN_IN_PROGRESS
            elif self.state == ArrayState.RANGE_MAX:
                self.state = ArrayState.RANGE_MAX_IN_PROGRESS
                self.defined_max = True
            self.cur_dim += token.data
        else:
            self.invalid(token)

    def numeric(self, token: Token):
        self.add_data_to_dimension(token)

    def symbol(self, token: Token):
        self.add_data_to_dimension(token)

    def keyword(self, token: Token):
        self.add_data_to_dimension(token)

    def operator(self, token: Token):
        self.add_data_to_dimension(token)

    def sqbracket(self, token: Token):
        if self.state == ArrayState.BEGIN and token.data == "[":
            self.state = ArrayState.RANGE_MIN
        elif token.data == "]":
            if self.state == ArrayState.RANGE_MIN:
                # This is just an empty [] declaration. We're done
                pass
            elif self.state == ArrayState.RANGE_MIN_IN_PROGRESS:
                self.dimensions[0] = self.cur_dim
            elif self.state == ArrayState.RANGE_MAX_IN_PROGRESS:
                self.dimensions[1] = self.cur_dim
            else:
                self.invalid(token)
            self.state = ArrayState.END
        else:
            self.invalid(token)

    def ellipsis(self, token: Token):
        if self.state == ArrayState.RANGE_MIN_IN_PROGRESS:
            self.dimensions[0] = self.cur_dim
            self.cur_dim = ""
            self.state = ArrayState.RANGE_MAX
        else:
            self.invalid(token)

    def rbracket(self, token: Token):
        if token.data == "(" and self.state not in [ArrayState.BEGIN, ArrayState.END]:
            self.cur_dim += MidlExpressionParser(self.tokens, self.tokenizer).parse(
                token
            )
            if self.state == ArrayState.RANGE_MAX:
                self.state = ArrayState.RANGE_MAX_IN_PROGRESS
                self.defined_max = True
        else:
            self.invalid(token)

    def finished(self) -> MidlArrayDimensions:
        dims = MidlArrayDimensions(self.dimensions[0], self.dimensions[1])
        return dims
