import enum

from midl import MidlInterface

from .attributes import MidlAttributesParser
from .base import MidlBaseParser, MidlParserException
from .midltokenizer import TokenType
from .procedures import MidlProcedureParser
from .structs import MidlStructParser
from .typedefs import MidlTypedefParser
from .unions import MidlUnionParser
from .variables import MidlVariableInstantiationParser
from .util import SkipClosureParser

class InterfaceState(enum.Enum):
    """Class used to handle state transitions for MidlInterfaceParser
    """
    BEGIN = enum.auto()
    NAME = enum.auto()
    INHERIT = enum.auto()
    INHERIT_NAME = enum.auto()
    BODY = enum.auto()
    DEFINITION = enum.auto()
    END = enum.auto()

class MidlInterfaceParser(MidlBaseParser):
    """Responsible for parsing an interface definiton.

        Mostly, this class delegates to other classes to handle parsing
    """

    def __init__(self, token_generator, tokenizer):
        self.tokens = token_generator
        super().__init__(token_generator=token_generator, end_state=InterfaceState.END, tokenizer=tokenizer)
        self.interface = MidlInterface()
        self.state = InterfaceState.BEGIN
        self.brace_level = 0
        self.cur_member_attrs = {}
        self.kw_handlers = {
            "typedef": self._typedef,
            "import": self._import,
            "cpp_quote": self._cpp_quote,
            "struct": self._struct,
            "union": self._union,
            "const": self._const,
        }

    def sqbracket(self, token):
        """ Handle attributes for procedures
        """
        if token.data == "[" and self.state == InterfaceState.DEFINITION:
            self.cur_member_attrs.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
        else: 
            self.invalid(token)
        
    def comment(self, token):
        if  '[MS-PAR]' in token.data:
            print("zx")
        self.interface.add_comment(token)       

    def _typedef(self, token):
        tds = MidlTypedefParser(self.tokens, self.tokenizer).parse(token)
        for td in tds:
            self.interface.add_typedef(td)

    def _import(self, _):
        import_token = next(self.tokens)
        assert(import_token.type == TokenType.STRING)
        self.interface.imports.append(import_token.data)
        assert(next(self.tokens).type == TokenType.SEMICOLON)

    def _cpp_quote(self, _):
        closure_token = next(self.tokens)
        assert( closure_token.data == '(')
        cpp_quote = SkipClosureParser(self.tokens, self.tokenizer, closure_open='(', closure_close=')').parse(closure_token)[1:-1]
        self.interface.cpp_quotes.append(cpp_quote)

    def _const(self, token):
        vd = MidlVariableInstantiationParser(self.tokens, self.tokenizer).parse(token)
        self.interface.add_vardef(vd)

    def _struct(self, token):
        # Create a typedef?
        std = MidlStructParser(self.tokens, self.tokenizer).parse(token)
        self.interface.add_typedef(std)
        
    def _union(self, token):
        # Create a typedef?
        utd = MidlUnionParser(self.tokens, self.tokenizer).parse(token)
        self.interface.add_typedef(utd)

    def _procedure(self, token):
        # Procedure declaration return type
        proc = MidlProcedureParser(self.tokens, self.tokenizer).parse(token)
        if proc:
            proc.attrs = self.cur_member_attrs
            self.interface.add_procedure(proc)
        self.cur_member_attrs = {}

    def keyword(self,token):
        if token.data == "interface" and self.state == InterfaceState.BEGIN:
            self.state = InterfaceState.NAME
        elif self.state == InterfaceState.DEFINITION:
            # Invoke the keyword handler. Anything else should be a procedure definition
            self.kw_handlers.get(token.data, self._procedure)(token)
        else:
            self.invalid(token)
    
    def brace(self, token):
        """Sets the brace level appropriately
        """
        if token.data == "{" and self.state in [InterfaceState.BODY, InterfaceState.INHERIT]:
            self.state = InterfaceState.DEFINITION
        elif token.data =="}" and self.state == InterfaceState.DEFINITION:
            self.state = InterfaceState.END
        else:
            self.invalid(token)

    def symbol(self, token):
        if self.state == InterfaceState.NAME:
            self.interface.name = token.data
            self.state = InterfaceState.INHERIT
        elif self.state == InterfaceState.INHERIT_NAME:
            self.interface.parents.append(token.data)
            self.state = InterfaceState.BODY
        elif self.state == InterfaceState.DEFINITION:
            self._procedure(token)
        else:
            self.invalid(token)

    def directive(self, token):
        # We keep #defines to be handled like cpp_quotes later on
        if token.data.startswith("#define"):
            self.interface.defines.append(token.data)

    def operator(self, token):
        if self.state == InterfaceState.INHERIT and token.data == ':':
            self.state = InterfaceState.INHERIT_NAME
        else:
            self.invalid(token)

    def finished(self) -> MidlInterface:
        """Parsing loop
        """
        if not self.interface:
            raise MidlParserException(f"Failed to parse interface!")
        return self.interface