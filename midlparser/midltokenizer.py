from .midlreserved import MIDL_OPERATORS
import enum
import string
import uuid
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

    def __init__(self, midl: str, filename: str):
        self.midl = midl
        self.max_size = len(self.midl)
        self.ptr = 0
        self.filename = filename
        self.line_count = 1

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
            if self.iswspace(cur_char):
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
                elif cur_char == '-' and self.midl[self.ptr + 1] in string.digits:
                    s, is_guid = self.get_numeric()
                    if is_guid:
                        to_yield = Token(s, TokenType.GUID)
                    else:
                        to_yield = Token(s, TokenType.NUMERIC)
                else:
                    to_yield = Token(cur_char, TokenType.OPERATOR)
            elif cur_char == ";":
                to_yield = Token(cur_char, TokenType.SEMICOLON)
            elif cur_char in string.ascii_letters or cur_char == "_":
                # Some symbols may start with an underscore.
                s = self.get_keyword_or_symbol()
                if s in Token.keywords:
                    to_yield = Token(s, TokenType.KEYWORD)
                else:
                    to_yield = Token(s, TokenType.SYMBOL)
            elif cur_char in string.digits:
                s, is_guid = self.get_numeric()
                if is_guid:
                    to_yield = Token(s, TokenType.GUID)
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
        start_ptr = self.ptr
        is_hex = False
        is_octal = False
        has_decimal = False
        is_bin = False
        cur_char = self.midl[self.ptr]
        int_suffixes = 0
        numeric_str = ""

        # Check for guids first. Otherwise they could get confused with octal numbers e.g.
        # 01234567-8711-<rest of guid> might look like octal subtraction
        numeric_str = ""
        c = self.midl[self.ptr]
        while c.lower() in string.hexdigits + '-':
            numeric_str += c
            self.ptr += 1
            c = self.midl[self.ptr]
        try:
            uuid.UUID(numeric_str)
            # Rewind 1 to the end of the GUID
            self.ptr -= 1
            return numeric_str, True
        except ValueError:
            # Not a guid
            pass

        self.ptr = start_ptr
        numeric_str = ""

        # Check for a negative number
        if cur_char == '-':
            numeric_str += cur_char
            self.ptr += 1
            cur_char = self.midl[self.ptr]
        
        # Check for hex and octal
        if cur_char == '0':
            next_char = self.midl[self.ptr+1].lower()
            if next_char == 'x':
                numeric_str += self.midl[self.ptr:self.ptr+2]
                self.ptr += 2
                cur_char = self.midl[self.ptr]
                is_hex = True
            elif next_char == 'b':
                is_bin = True
            elif next_char in string.digits:
                is_octal = True
            
        while not self.iswspace(cur_char):
            if cur_char in Token.operators:
                if cur_char == '.':
                    if not has_decimal and not is_hex and not is_octal and int_suffixes == 0:
                        has_decimal = True
                        numeric_str += cur_char
                    else:
                        raise Exception(f"Invalid extra decimal in number")
                else:
                    # We have hit an operation, end the current tokenization step. Take a step back and return
                    self.ptr -= 1
                    break
            elif cur_char in [";", "]", "}", ")", ","]:
                # We have hit the end of the current MIDL statement. Take a step back and return
                self.ptr -= 1
                break
            
            if int_suffixes >= 2:
                raise Exception(f"Invalid character {cur_char} for numeric {numeric_str}")

            # Other stuff like suffixes and guids
            if cur_char not in string.digits:
                if cur_char.lower() in ['u', 'l']:
                    int_suffixes += 1
                elif not is_hex or (is_hex and cur_char not in string.hexdigits):
                    # End of the number!
                    break
            else:
                if is_bin and cur_char not in ['0', '1']:
                    print(self.midl)
                    raise Exception(f"Invalid character {cur_char} for binary numeric: {numeric_str}")
            
            # Continue reading the numeric
            numeric_str += cur_char
            self.ptr += 1
            cur_char = self.midl[self.ptr]

        return numeric_str, False

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
            self.line_count+=1
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
            self.line_count += 1

        comment = self.midl[self.ptr : comment_end].strip()
        self.ptr = comment_end + comment_offset
        return comment

    def get_keyword_or_symbol(self):
        """Gets the keyword or symbol

        Returns:
            str: Found keyword or symbol
        """
        cur_char = self.midl[self.ptr]
        s = ""
        valid_chars = string.ascii_letters + string.digits + '_'
        while not self.iswspace(cur_char):
            if cur_char not in valid_chars:
                self.ptr -= 1
                return s
            s += cur_char
            self.ptr += 1
            cur_char = self.midl[self.ptr]

        return s

    def iswspace(self, char):
        """Checks if the character is a whitespace

        Args:
            char (str): Character to check
        Returns:
            bool: Returns result of the whitespace check
        """
        wspace = [" ", "\n", "\r\n", "\r", "\t"]
        if char in ["\n", "\r\n", "\r"]:
            self.line_count += 1
        if char in wspace:
            return True
        return False


    def get_error(self):
        return 'In file: ' + self.filename +":"+str(self.line_count) + '\n\tAt: ' + self.midl[self.ptr-1:].split("\n")[0]