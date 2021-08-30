import enum

from midlparser.parsers.attributes import MidlAttributesParser
from midlparser.parsers.base import MidlBaseParser, MidlParserException
from midlparser.parsers.coclass import MidlCoclassParser
from midlparser.parsers.dispinterface import MidlDispInterfaceParser
from midlparser.parsers.enums import MidlEnumParser
from midlparser.parsers.interface import MidlInterfaceParser
from midlparser.parsers.libraries import MidlLibraryParser
from midlparser.parsers.typedefs import MidlTypedefParser
from midlparser.parsers.util import SkipClosureParser
from midlparser.parsers.variables import MidlVariableInstantiationParser
from midlparser.tokenizer import Token

from midltypes import MidlDefinition


class MidlState(enum.Enum):
    """Class used to handle state transitions for top level MidlParser
    """
    DEFAULT = enum.auto()
    IMPORT = enum.auto()
    IMPORT_COMPLETE = enum.auto()
    DEF_COMPLETE = enum.auto()
    MIDL_PRAGMA = enum.auto()
    DEFINITION = enum.auto()
    OPEN_SQBRACKET = enum.auto()
    CLOSE_SQBRACKET= enum.auto()
    COMMENT = enum.auto()
    END = enum.auto()

class MidlParser(MidlBaseParser):
    """Parses a complete MIDL file into a MidlDefiniton object
        This class maintains a state machine.
    """

    def __init__(self, token_generator,tokenizer):
        self.state = MidlState.DEFAULT # Current state of the parsing
        super().__init__(token_generator=token_generator, end_state=MidlState.END,tokenizer=tokenizer)
        self.definition = MidlDefinition() # data to be returned by calling parse()
        self.cur_def_attrs = {}
        self.kw_handlers = {
            'import': self._import,
            'typedef': self._typedef,
            'enum': self._enum,
            'midl_pragma': self._midl_pragma,
            'interface': self._interface,
            'coclass': self._coclass,
            'dispinterface': self._dispinterface,
            'cpp_quote': self._cpp_quote,
            'library' : self._library,
        }

    def _library(self, token: Token):
        lib = MidlLibraryParser(self.tokens, self.tokenizer).parse(token)
        lib.attributes = self.cur_def_attrs
        self.definition.libraries.append(lib)
        self.cur_def_attrs = {}
        self.state = MidlState.DEF_COMPLETE
        
    def _import(self, _):
        self.state = MidlState.IMPORT

    def _typedef(self, token: Token):
        self.definition.typedefs.extend(
                MidlTypedefParser(self.tokens, self.tokenizer).parse(token)
            )
        self.cur_def_attrs = {}

    def _enum(self, token: Token):
        self.definition.typedefs.extend(
                MidlEnumParser(self.tokens, self.tokenizer).parse(token)
            )
        self.cur_def_attrs = {}

    def _midl_pragma(self, _):
        assert(next(self.tokens).data == 'warning')
        SkipClosureParser(self.tokens, self.tokenizer, '(', ')').parse(next(self.tokens))

    def _interface(self, token: Token):
        iface = MidlInterfaceParser(self.tokens, self.tokenizer).parse(token)
        iface.attributes = self.cur_def_attrs
        self.definition.interfaces.append(iface)
        self.cur_def_attrs = {}
        self.state = MidlState.DEF_COMPLETE

    def _coclass(self, token: Token):
        coclass = MidlCoclassParser(self.tokens, self.tokenizer).parse(token)
        coclass.attributes = self.cur_def_attrs
        self.definition.coclasses.append(coclass)
        self.cur_def_attrs = {}
        self.state = MidlState.DEF_COMPLETE

    def _dispinterface(self, token: Token):
        dispinterface = MidlDispInterfaceParser(self.tokens, self.tokenizer).parse(token)
        dispinterface.attributes = self.cur_def_attrs
        self.definition.dispinterfaces.append(dispinterface)
        self.cur_def_attrs = {}
        self.state = MidlState.DEF_COMPLETE

    def _cpp_quote(self, _):
        closure_token = next(self.tokens)
        assert( closure_token.data == '(')
        cpp_quote = SkipClosureParser(self.tokens, self.tokenizer, closure_open='(', closure_close=')').parse(closure_token)[1:-1]
        self.definition.cpp_quotes.append(cpp_quote)

    def default_kw_handler(self, token: Token):
        self.state = MidlState.DEFINITION
        self.definition.instantiation.append(
            MidlVariableInstantiationParser(self.tokens, self.tokenizer).parse(token)
        )
        self.state = MidlState.DEFAULT
        self.cur_def_attrs = {}

    def keyword(self, token: Token):
        """Handles encountered keywords
        """
        if self.state not in [MidlState.DEFAULT, MidlState.DEF_COMPLETE]:
            self.invalid(token)
        self.kw_handlers.get(token.data, self.default_kw_handler)(token)

    def string(self, token: Token):
        """Encountered a string. Should only ever be imports encountered here.
        """
        if self.state == MidlState.IMPORT:
            # Encountered an import statement so add it to the definition's imports
            self.definition.add_import(token.data[1:-1])
            self.state = MidlState.DEF_COMPLETE
        else:
            self.invalid(token)

    def sqbracket(self, token: Token):
        """Encountered a square bracket. Only opening brackets are handled here.
        """
        if token.data == "[" and self.state in [MidlState.DEFAULT, MidlState.DEF_COMPLETE]:
            self.cur_def_attrs.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
            self.state = MidlState.DEFAULT
        else:
            # Note that the closing square bracket is handled within the MidlInterfaceParser
            self.invalid(token)

    def semicolon(self, token: Token):
        if self.state != MidlState.DEF_COMPLETE:
            self.invalid(token)
        self.state = MidlState.DEFAULT

    def comment(self, token: Token):
        """Record the comment
        """
        self.definition.add_comment(token)
        return

    def directive(self, token: Token):
        self.definition.directives.append(token.data)   

    def parse(self, cur_token):
        try:
            return super().parse(cur_token)
        except StopIteration:
            return self.finished()

    def finished(self) -> MidlDefinition:
        if not self.definition:
            raise MidlParserException(f"Failed to parse definition.")
        return self.definition
