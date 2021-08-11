import enum
from midl import MidlArrayDimensions
from .base import MidlBaseParser
from .midltokenizer import Token

class SkipClosureState(enum.Enum):
    BEGIN = enum.auto()
    END = enum.auto()

class SkipClosureParser(MidlBaseParser):
    """Skip over closures we don't care about parsing internally and return the whole blob
    """
    def __init__(self, token_generator, tokenizer, closure_open, closure_close):
        self.state = SkipClosureState.BEGIN
        super().__init__(token_generator=token_generator, end_state=SkipClosureState.END, tokenizer=tokenizer)
        self.data = ''
        self.closure_level = 0
        self.closure_open = closure_open
        self.closure_close = closure_close
        self.handle_any = True

    def any(self, token: Token):
        if token.data == self.closure_open:
            self.closure_level += 1
        elif token.data == self.closure_close:
            if self.closure_level <= 0:
                self.invalid(token)
            self.closure_level -= 1
        self.data += token.data + ' '
        if self.closure_level == 0:
            self.state = SkipClosureState.END

    def finished(self):
        return self.data.strip()[1:-1].strip()
