import abc
import typing

from midlparser.logs import get_logger
from midlparser.tokenizer import MidlTokenizer, Token, TokenType


class MidlInvalidTokenException(Exception):
    pass


class MidlParserException(Exception):
    pass


class MidlBaseParser(abc.ABC):
    state = None

    def __init__(self, token_generator, end_state, tokenizer: MidlTokenizer):
        self.logger = get_logger(self.__class__.__name__)
        self.tokens = token_generator
        self.end_state = end_state
        self.handle_any = False
        self.handlers = {
            TokenType.KEYWORD: self.keyword,
            TokenType.SQBRACKET: self.sqbracket,
            TokenType.RBRACKET: self.rbracket,
            TokenType.BRACE: self.brace,
            TokenType.QUOTE: self.quote,
            TokenType.SYMBOL: self.symbol,
            TokenType.STRING: self.string,
            TokenType.NUMERIC: self.numeric,
            TokenType.OPERATOR: self.operator,
            TokenType.SEMICOLON: self.semicolon,
            TokenType.COMMA: self.comma,
            TokenType.GUID: self.guid,
            TokenType.COMMENT: self.comment,
            TokenType.ELLIPSIS: self.ellipsis,
            TokenType.DIRECTIVE: self.directive,
        }
        self.tokenizer = tokenizer

    def invalid(self, token: Token):
        try:
            finished = self.finished()
        except:
            finished = ""
        ts = self.tokenizer.get_state()
        fmt_error = (
            f"\nUnexpected: [{token.type}: {token.data}]\n"
            f"File: {ts.filename}:{ts.lineno}\n"
            f"{self.__class__.__name__} State [{self.state}]:\n{finished}\n"
        )
        raise MidlInvalidTokenException(fmt_error)

    def keyword(self, token: Token):
        self.invalid(token)

    def sqbracket(self, token: Token):
        self.invalid(token)

    def rbracket(self, token: Token):
        self.invalid(token)

    def brace(self, token: Token):
        self.invalid(token)

    def quote(self, token: Token):
        self.invalid(token)

    def symbol(self, token: Token):
        self.invalid(token)

    def string(self, token: Token):
        self.invalid(token)

    def numeric(self, token: Token):
        self.invalid(token)

    def operator(self, token: Token):
        self.invalid(token)

    def semicolon(self, token: Token):
        self.invalid(token)

    def comma(self, token: Token):
        self.invalid(token)

    def guid(self, token: Token):
        self.invalid(token)

    def comment(self, token: Token):
        self.invalid(token)

    def ellipsis(self, token: Token):
        self.invalid(token)

    def directive(self, token: Token):
        self.invalid(token)

    def any(self, token: Token):
        self.invalid(token)

    def parse(self, cur_token: Token) -> typing.Any:
        """
        Base parsing loop that iterates over tokens and invokes their handler function.
        The default handlers all raise an exception to indicate that they have not been handled appropriately.
        NOTE: This should never happen with a well formed test case (unless something hasn't been considered.)

        Args:
            cur_token (str): This is the initial token for the parser type
        Returns:
            Any: return type depends on the extending class.
        """
        while cur_token:
            try:
                # Handle the current token
                if self.handle_any:
                    self.any(cur_token)
                else:
                    self.handlers[cur_token.type](cur_token)
                # Check if we're done
                if self.state == self.end_state:
                    break
                cur_token = next(self.tokens, None)
            except Exception as e:
                self.logger.exception(e)
                exit()
        return self.finished()

    @abc.abstractmethod
    def finished(self):
        raise NotImplementedError()
