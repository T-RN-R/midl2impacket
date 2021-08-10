from .midlreserved import MIDL_OPERATORS
import enum
import string
from .midlreserved import *


class TokenType(enum.Enum):
    KEYWORD = enum.auto()  # see Token.keywords list
    SQBRACKET = enum.auto()  # Square brackets
    RBRACKET = enum.auto()  # round brackets
    BRACE = enum.auto()  # curly braces
    QUOTE = enum.auto()  # double quotes
    SYMBOL = enum.auto()  # Words that are not keywords
    STRING = enum.auto() # everything inside of a pair of quotes, including the quotes themselves
    NUMERIC = enum.auto()  # Float or integer
    OPERATOR = enum.auto()  # Mathematic operators, see Token.operators
    SEMICOLON = enum.auto()
    COLON = enum.auto()
    COMMA = enum.auto()
    GUID = enum.auto()
    COMMENT = enum.auto()
    ELLIPSIS = enum.auto()
    DIRECTIVE = enum.auto()

class Token:
    """Representation of Token types."""

    keywords = MIDL_KEYWORDS
    operators = MIDL_OPERATORS

    def __init__(self, data: str, token_type):
        """Initializes the token

        Args:
            data (str): The python string represention the Token data
            _t (int): Enum representing the Token type
        """
        self.type = token_type
        self.data = data


class MidlTokenizer:
    """Class that tokenizes the raw MIDL string

    Has a cursor {self.ptr} that maintains the tokenization state.
    """

    def __init__(self, midl: str):
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
                to_yield = Token(cur_char, TokenType.SQBRACKET)
            elif cur_char == "(" or cur_char == ")":
                to_yield = Token(cur_char, TokenType.RBRACKET)
            elif cur_char == "{" or cur_char == "}":
                to_yield = Token(cur_char, TokenType.BRACE)
            elif cur_char == "#" and self.midl[self.ptr + 1] != '#':
                directive = self.get_directive()
                to_yield = Token(directive, TokenType.DIRECTIVE)
            elif cur_char == '"':
                s = self.get_string()
                self.ptr -= 1  # take a step back before continuing
                to_yield = Token(s, TokenType.STRING)
            elif cur_char == ",":
                to_yield = Token(",", TokenType.COMMA)
            elif (
                cur_char == "."
                and self.midl[self.ptr + 1] == "."
                and self.midl[self.ptr + 2] != "."
            ):
                to_yield = Token(cur_char, TokenType.ELLIPSIS)
                # Skip to the end of the ellipsis
                self.ptr += 1
            elif cur_char in Token.operators:
                # Check comments
                if cur_char == "/" and self.midl[self.ptr + 1] in ["/", "*"]:
                    comment = self.get_comment()
                    to_yield = Token(comment, TokenType.COMMENT)
                else:
                    to_yield = Token(cur_char, TokenType.OPERATOR)
            elif cur_char == ";":
                to_yield = Token(cur_char, TokenType.SEMICOLON)
            elif cur_char == ':':
                to_yield = Token(cur_char, TokenType.COLON)
            elif cur_char in string.ascii_letters or cur_char == "_":
                # Some symbols may start with an underscore.
                s = self.get_keyword_or_symbol()
                if s in Token.keywords:
                    to_yield = Token(s, TokenType.KEYWORD)
                else:
                    to_yield = Token(s, TokenType.SYMBOL)
            elif cur_char in string.digits:
                s = self.get_numeric()
                if "-" in s:  # TODO Will break with negative numbers
                    to_yield = Token(s, TokenType.GUID)
                elif s in Token.keywords:
                    to_yield = Token(s, TokenType.KEYWORD)
                else:
                    to_yield = Token(s, TokenType.NUMERIC)
            else:
                raise Exception(f"Unhandled character {cur_char}")
            self.ptr += 1
            assert (
                to_yield is not None
            ), "Must set the Token to be yielded by the generator"
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
                self.ptr -= 1
                return s
            if cur_char == ";":
                # We have hit the end of the current MIDL statement. Take a step back and return
                self.ptr -= 1
                return s
            if cur_char not in string.digits and cur_char != ".":
                # Handle the GUID case
                guid_chars = "abcdef-"
                while True:
                    if cur_char not in string.digits and cur_char not in guid_chars:
                        break
                    s += cur_char
                    self.ptr += 1
                    cur_char = self.midl[self.ptr]
                # We have hit a non numeric digit, non-decimal point, or non guid. Take a step back and return
                self.ptr -= 1
                return s
            # Continue reading the numeric
            s += cur_char
            self.ptr += 1
            cur_char = self.midl[self.ptr]
        return s

    def get_string(self):
        """Gets a string

        Returns:
            str: Returns the found string
        """
        cur_char = self.midl[self.ptr]
        assert (
            cur_char == '"'
        )  # Validation check to ensure this function is called from the right spot.

        # Find the next occurence of a quotation mark.
        # TODO: This will cause parsing issues if the mark is preceded by a slash ('\"'), which should actually be treated as part of the string
        end_char = (
            self.midl[self.ptr + 1 :].find('"') + self.ptr + 1
        )  # add self.ptr +1 here because that is the beginning of slice
        s = self.midl[self.ptr : end_char + 1]
        self.ptr = end_char + 1
        return s

    def get_directive(self):
        cur_char = self.midl[self.ptr]
        assert(cur_char == "#")
        directive_pos = self.ptr
        while True:
            directive_end = self.midl[directive_pos:].find("\n") + directive_pos
            # Make sure it wasn't escaped (multi-line macros)
            if self.midl[directive_end-1] != '\\':
                break
            directive_pos = directive_end+1
        
        directive = self.midl[self.ptr:directive_end]
        self.ptr = directive_end
        return directive

    def get_comment(self):
        """Gets a comment

        Returns:
            str: Returns the found comment
        """
        cur_char = self.midl[self.ptr]
        comment_type_char = self.midl[self.ptr + 1]
        assert (
            cur_char == "/"
        )  # Validation check to ensure this function is called from the right spot.
        assert comment_type_char in ["/", "*"]
        self.ptr += 2  # Start searching inside the comment.
        if comment_type_char == "*":
            # Look for the end of the block comment
            comment_end = self.midl[self.ptr :].find("*/") + self.ptr
            comment_offset = 2
        else:
            # Look for the next line ending
            comment_end = self.midl[self.ptr :].find("\n") + self.ptr
            comment_offset = 1
        comment = self.midl[self.ptr : comment_end].strip()
        self.ptr = comment_end + comment_offset
        return comment

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
                self.ptr -= 1
                return s
            s += cur_char
            self.ptr += 1
            cur_char = self.midl[self.ptr]

        return s

    def iswspace(char):
        """Checks if the character is a whitespace

        Args:
            char (str): Character to check
        Returns:
            bool: Returns result of the whitespace check
        """
        wspace = [" ", "\n", "\r\n", "\r", "\t"]
        if char in wspace:
            return True
        return False
