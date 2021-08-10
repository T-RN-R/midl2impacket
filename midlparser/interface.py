import enum

from midl import MidlInterface
from .attributes import MidlAttributesParser
from .base import MidlBaseParser, MidlParserException
from .procedures import MidlProcedureParser
from .typedefs import MidlTypedefParser

class InterfaceState(enum.Enum):
    """Class used to handle state transitions for MidlInterfaceParser
    """
    ATTRIBUTES = enum.auto()
    TYPE = enum.auto()
    NAME = enum.auto()
    INHERIT = enum.auto()
    INHERIT_NAME = enum.auto()
    BODY = enum.auto()
    DEFINITION = enum.auto()
    CPP_QUOTE = enum.auto()
    CPP_QUOTE_STRING = enum.auto()
    CPP_QUOTE_END = enum.auto()
    END = enum.auto()

class MidlInterfaceParser(MidlBaseParser):
    """Responsible for parsing an interface definiton.

        Mostly, this class delegates to other classes to handle parsing
    """

    def __init__(self, token_generator, tokenizer):
        self.tokens = token_generator
        super().__init__(token_generator=token_generator, end_state=InterfaceState.END, tokenizer=tokenizer)
        self.interface = MidlInterface()
        self.state = InterfaceState.ATTRIBUTES
        self.brace_level = 0

    def sqbracket(self, token):
        """ Handle attributes (interface or procedure)
        """
        if token.data == "[":
            if self.state == InterfaceState.ATTRIBUTES:
                self.interface.attributes = MidlAttributesParser(self.tokens, self.tokenizer).parse(token)
                self.state = InterfaceState.TYPE
            elif self.state == InterfaceState.DEFINITION:
                # Procedure declaration attributes
                proc = MidlProcedureParser(self.tokens, self.tokenizer).parse(token)
                if proc:
                    self.interface.add_procedure(proc)
            else:
                self.invalid(token)
        else: 
            self.invalid(token)

    def rbracket(self, token):
        """ Round brackets are only valid in CPP_QUOTES """
        if token.data == '(' and self.state == InterfaceState.CPP_QUOTE:
            self.state = InterfaceState.CPP_QUOTE_STRING
        elif token.data == ')' and self.state == InterfaceState.CPP_QUOTE_END:
            self.state = InterfaceState.DEFINITION
        else:
            self.invalid(token)
        
    def comment(self, token):
        self.interface.add_comment(token)
        
    def keyword(self,token):
        """Parses keywords [uuid, version, pointer_default,interface, error_status_t, typedef, cpp_quote]
        """
        if token.data == "interface" and self.state == InterfaceState.TYPE:
            self.state = InterfaceState.NAME
        elif token.data == "typedef" and self.state == InterfaceState.DEFINITION:
            # spin up a TypeDef parser to parse out typedefs
            tds = MidlTypedefParser(self.tokens).parse(token)
            for td in tds:
                self.interface.add_typedef(td)
        elif self.state == InterfaceState.DEFINITION:
            if token.data == "cpp_quote":
                self.state = InterfaceState.CPP_QUOTE
            else:
                # Treat it as the return type of a procedure?
                proc = MidlProcedureParser(self.tokens).parse(token)
                if proc:
                    self.interface.procedures.append(proc)
        else:
            self.invalid(token)

    def string(self, token):
        if self.state == InterfaceState.CPP_QUOTE_STRING:
            self.interface.cpp_quotes.append(token.data)
            self.state = InterfaceState.CPP_QUOTE_END
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
            # Procedure declaration return type
            proc = MidlProcedureParser(self.tokens, self.tokenizer).parse(token)
            if proc:
                self.interface.add_procedure(proc)
        else:
            self.invalid(token)

    def directive(self, token):
        # We keep #defines to be handled like cpp_quotes later on
        if token.data.startswith("#define"):
            self.interface.defines.append(token.data)

    def colon(self, token):
        if self.state == InterfaceState.INHERIT:
            self.state = InterfaceState.INHERIT_NAME
        else:
            self.invalid(token)

    def finished(self) -> MidlInterface:
        """Parsing loop
        """
        if not self.interface:
            raise MidlParserException(f"Failed to parse interface!")
        return self.interface