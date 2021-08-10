import abc
import traceback
from .midltokenizer import Token, TokenType

class MidlInvalidTokenException(Exception):
    pass

class MidlParserException(Exception):
    pass

class MidlBaseParser(abc.ABC):
    def __init__(self, token_generator, end_state, tokenizer):
        self.tokens = token_generator
        self.end_state = end_state
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
            TokenType.COLON: self.colon,
            TokenType.COMMA: self.comma,
            TokenType.GUID: self.guid,
            TokenType.COMMENT: self.comment,
            TokenType.ELLIPSIS: self.ellipsis,
            TokenType.DIRECTIVE: self.directive,
        }
        self.tokenizer=tokenizer
    def invalid(self, token):
        raise MidlInvalidTokenException(f"Unexpected token [{token.type}: {token.data}] in state {self.state} \n\tAt input: {self.tokenizer.get_error()}")

    def keyword(self, token):
        self.invalid(token)

    def sqbracket(self, token):
        self.invalid(token)
        
    def rbracket(self, token):
        self.invalid(token)
        
    def brace(self, token):
        self.invalid(token)
        
    def quote(self, token):
        self.invalid(token)
        
    def symbol(self, token):
        self.invalid(token)
        
    def string(self, token):
        self.invalid(token)
        
    def numeric(self, token):
        self.invalid(token)
        
    def operator(self, token):
        self.invalid(token)
        
    def semicolon(self, token):
        self.invalid(token)
        
    def colon(self, token):
        self.invalid(token)
        
    def comma(self, token):
        self.invalid(token)
        
    def guid(self, token):
        self.invalid(token)
        
    def comment(self, token):
        self.invalid(token)
        
    def ellipsis(self, token):
        self.invalid(token)

    def directive(self, token):
        self.invalid(token)

    def parse(self, cur_token:Token):
        while cur_token:
            try:
                self.handlers[cur_token.type](cur_token)
                if self.state == self.end_state:
                    break
                cur_token = next(self.tokens, None)
            except Exception:
                traceback.print_exc()
                exit()
        return self.finished()

    @abc.abstractmethod
    def finished(self):
        raise NotImplementedError()