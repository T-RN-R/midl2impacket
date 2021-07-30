from .state import State
from midl import MidlDefinition
from typing import TypedDict
import string

class Token():
    """Representation of Token types.
    """
    KEYWORD = 0x1 # see Token.keywords list
    SQBRACKET = 0x2 # Square brackets
    RBRACKET = 0x3 # round brackets
    BRACE = 0x4 # curly braces
    QUOTE = 0x5 # double quotes
    SYMBOL = 0x6 # Words that are not keywords
    STRING = 0x7 # everything inside of a pair of quotes, including the quotes themselves
    NUMERIC = 0x8 # Float or integer
    OPERATOR = 0x9 # Mathematic operaros, see Token.operators
    SEMICOLON = 0xA 
    COMMA = 0xB

    keywords = ["import", "const", "int", "uuid", "version", "pointer_default", "typedef", "in", "out", "interface", "context_handle", "enum",  "struct", "cpp_quote", "error_status_t"]
    operators = ["=", "/","*", "+","-"]

    def __init__(self, data:str, _t):
        """Initializes the token

        Args:
            data (str): The python string represention the Token data
            _t (int): Enum representing the Token type
        """
        self.type = _t
        self.data = data

class MidlTokenizer():
    """Class that tokenizes the raw MIDL string
        
        Has a cursor {self.ptr} that maintains the tokenization state.
    """
    def __init__(self, midl:str):
        self.midl = midl
        self.max_size = len(self.midl)
        self.ptr = 0

    def get_token(self):
        """[summary]

        Raises:
            Exception: Raises an exception if there is some unhandled character in the provided MIDL

        Yields:
            Token: yields a token to be parsed
        """
        # Loop until end of the MIDL
        while self.ptr < self.max_size: 
            cur_char = self.midl[self.ptr]
            to_yield = None
            if MidlTokenizer.iswspace(cur_char):
                # Clear out extraneous whitespace
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
                self.ptr -=1 # take a step back before continuing
                to_yield =  Token(s, Token.STRING)
            elif cur_char == "," :
                to_yield =  Token(",", Token.COMMA)
            elif cur_char in Token.operators:
                to_yield =  Token(cur_char, Token.OPERATOR)
            elif cur_char == ";":
                to_yield =  Token(cur_char, Token.SEMICOLON)
            elif cur_char in string.ascii_letters or cur_char == "_": 
                # Some symbols may start with an underscore. 
                s = self.get_keyword_or_symbol()
                if s in Token.keywords:
                    to_yield =  Token(s, Token.KEYWORD)
                else: 
                    to_yield =  Token(s, Token.SYMBOL)
            elif cur_char in string.digits:
                s = self.get_numeric()
                if s in Token.keywords:
                    to_yield =  Token(s, Token.KEYWORD)
                else: 
                    to_yield =  Token(s, Token.SYMBOL)
            else:
                raise Exception(f"Unhandled character {cur_char}")
            self.ptr+=1
            assert(to_yield is not None), "Must set the Token to be yielded by the generator"
            yield to_yield

    def get_numeric(self):
        """Returns a numeric value 

        Raises:
            Exception: If there is an unexpected character within the number, raise this exception

        Returns:
            str: The numeric 
        """
        cur_char = self.midl[self.ptr]
        s = ""
        while not MidlTokenizer.iswspace(cur_char):
            if cur_char in Token.operators: 
                # We have hit a mathematical operation, end the current tokenization step. Take a step back and return
                self.ptr-=1
                return s
            if cur_char == ";":
                # We have hit the end of the current MIDL statement. Take a step back and return
                self.ptr-=1
                return s
            if cur_char not in string.digits and cur_char !=".":
                #TODO This is where GUIDs may break if they start with a digit, since they have hexadecimal digits. 
                # Find a way to handle GUIDs at the tokenization level
                
                #We have hit a non numeric digit, or non-decimal point. Take a step back and return
                self.ptr-=1
                return s
            # Continue reading the numeric  
            s += cur_char
            self.ptr+=1
            cur_char = self.midl[self.ptr]
        return s

    def get_string(self):
        """Gets a string 

        Returns:
            str: Returns the found string
        """
        cur_char = self.midl[self.ptr]
        assert(cur_char == '\"') # Validation check to ensure this function is called from the right spot.

        #Find the next occurence of a quotation mark. 
        # TODO: This will cause parsing issues if the mark is preceded by a slash ('\"'), which should actually be treated as part of the string
        end_char = self.midl[self.ptr+1:].find("\"") + self.ptr + 1 # add self.ptr +1 here because that is the beginning of slice
        s = self.midl[self.ptr:end_char+1]
        self.ptr=end_char+1
        return s

    def get_keyword_or_symbol(self):
        """Gets the keyword or symbol

        Returns:
            str: Found keyword or symbol
        """
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
        """Checks if the character is a whitespace

        Args:
            char (str): Character to check
        Returns:
            bool: Returns result of the whitespace check
        """
        wspace = [" ", "\n", "\r\n", "\r"]
        if char in wspace:
            return True
        return False

