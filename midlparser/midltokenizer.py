from .state import State
from midl import MidlDefinition
from typing import TypedDict
import string

class Token():
    KEYWORD = 0x1
    SQBRACKET = 0x2
    RBRACKET = 0x3
    BRACE = 0x4
    QUOTE = 0x5
    SYMBOL = 0x6
    STRING = 0x7
    NUMERIC = 0x8
    OPERATOR = 0x9
    SEMICOLON = 0xA
    COMMA = 0xB

    def __init__(self, data:str, _t):
        self.type = _t
        self.data = data

class MidlTokenizer():
    keywords = ["import", "const", "int", "uuid", "version", "pointer_default", "typedef", "in", "out", "interface", "context_handle", "void", "void*", "struct", "DWORD"]
    operators = ["=", "/","*", "+","-"]

    def __init__(self, midl:str):
        self.midl = midl
        self.max_size = len(self.midl)
        self.ptr = 0

    def get_token(self):
        while self.ptr < self.max_size:
            cur_char = self.midl[self.ptr]
            to_yield = None
            if MidlTokenizer.iswspace(cur_char):
                self.ptr += 1
                continue
            if cur_char == "[" or cur_char == "]":
                to_yield =  Token(cur_char,Token.SQBRACKET)
            elif cur_char == "(" or cur_char == ")":
                to_yield =  Token(cur_char,Token.RBRACKET)
            elif cur_char == "{" or cur_char == "}":
                to_yield =  Token(cur_char,Token.BRACE)
            elif cur_char == "\"" :
                s = self.get_string()
                to_yield =  Token(s, Token.STRING)
            elif cur_char == "," :
                to_yield =  Token(",", Token.COMMA)
            elif cur_char in MidlTokenizer.operators:
                to_yield =  Token(cur_char, Token.OPERATOR)
            elif cur_char == ";":
                to_yield =  Token(cur_char, Token.SEMICOLON)
            elif cur_char in string.ascii_letters or cur_char == "_":
                s = self.get_keyword_or_symbol()
                if s in MidlTokenizer.keywords:
                    to_yield =  Token(s, Token.KEYWORD)
                else: 
                    to_yield =  Token(s, Token.SYMBOL)
            elif cur_char in string.digits:
                s = self.get_numeric()
                if s in MidlTokenizer.keywords:
                    to_yield =  Token(s, Token.KEYWORD)
                else: 
                    to_yield =  Token(s, Token.SYMBOL)
            else:
                raise Exception(f"Unhandled character {cur_char}")
            self.ptr+=1
            yield to_yield
    def get_numeric(self):
        cur_char = self.midl[self.ptr]
        s = ""
        while not MidlTokenizer.iswspace(cur_char):
            if cur_char in MidlTokenizer.operators:
                self.ptr-=1
                return s
            if cur_char == ";":
                self.ptr-=1
                return s
            if cur_char not in string.digits and cur_char !=".":
                self.ptr-=1
                return s
                raise Exception(f"Unexpected character {cur_char} at index {self.ptr}")
            s += cur_char
            self.ptr+=1
            cur_char = self.midl[self.ptr]
        return s

    def get_string(self):
        cur_char = self.midl[self.ptr]
        assert(cur_char == '\"')
        end_char = self.midl[self.ptr+1:].find("\"") + self.ptr + 1 # add self.ptr +1 here because that is the beginning of slice
        s = self.midl[self.ptr:end_char+1]
        self.ptr=end_char+1
        return s

    def get_keyword_or_symbol(self):
        cur_char = self.midl[self.ptr]
        illegal_chars = ["[", "{", "(", ")", "}", "]", ";", ","]
        s = ""
        while not MidlTokenizer.iswspace(cur_char):
            if cur_char in illegal_chars:
                self.ptr-=1
                return s
            s += cur_char
            self.ptr+=1
            cur_char = self.midl[self.ptr]

        return s

    def iswspace(char):
        wspace = [" ", "\n", "\r\n", "\r"]
        if char in wspace:
            return True
        return False

