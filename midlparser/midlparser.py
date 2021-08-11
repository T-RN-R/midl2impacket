import enum
import pathlib

from midl import MidlDefinition
from .attributes import MidlAttributesParser
from .base import MidlBaseParser, MidlParserException
from .coclass import MidlCoclassParser
from .dispinterface import MidlDispInterfaceParser
from .enums import MidlEnumParser
from .interface import MidlInterfaceParser
from .typedefs import MidlTypedefParser
from .variables import MidlVariableInstantiationParser
from .util import SkipClosureParser
from .midltokenizer import MidlTokenizer

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

    def keyword(self, token):
        """Handles encountered keywords
        """
        if self.state not in [MidlState.DEFAULT, MidlState.DEF_COMPLETE]:
            self.invalid(token)
        if token.data == "import":
            self.state = MidlState.IMPORT
        elif token.data == 'typedef':
            self.definition.typedefs.extend(
                MidlTypedefParser(self.tokens, self.tokenizer).parse(token)
            )
        elif token.data == 'enum':
            self.definition.typedefs.append(
                MidlEnumParser(self.tokens, self.tokenizer).parse(token)
            )
        elif token.data == 'midl_pragma':
            assert(next(self.tokens).data == 'warning')
            SkipClosureParser(self.tokens, self.tokenizer, '(', ')').parse(next(self.tokens))
        elif token.data == 'interface' and self.cur_def_attrs:
            iface = MidlInterfaceParser(self.tokens, self.tokenizer).parse(token)
            iface.attributes = self.cur_def_attrs
            self.definition.interfaces.append(iface)
            self.cur_def_attrs = {}
            self.state = MidlState.DEF_COMPLETE
        elif token.data == 'coclass':
            coclass = MidlCoclassParser(self.tokens, self.tokenizer).parse(token)
            coclass.attributes = self.cur_def_attrs
            self.definition.coclasses.append(coclass)
            self.cur_def_attrs = {}
            self.state = MidlState.DEF_COMPLETE
        elif token.data == 'dispinterface':
            dispinterface = MidlDispInterfaceParser(self.tokens, self.tokenizer).parse(token)
            dispinterface.attributes = self.cur_def_attrs
            self.definition.dispinterfaces.append(dispinterface)
            self.cur_def_attrs = {}
            self.state = MidlState.DEF_COMPLETE
        else:
            self.state = MidlState.DEFINITION
            self.definition.instantiation.append(
                MidlVariableInstantiationParser(self.tokens, self.tokenizer).parse(token)
            )
            self.state = MidlState.DEFAULT

    def string(self, token):
        """Encountered a string. Should only ever be imports encountered here.
        """
        if self.state == MidlState.IMPORT:
            # Encountered an import statement so add it to the definition's imports
            self.definition.add_import(token.data)
            self.state = MidlState.DEF_COMPLETE
        else:
            self.invalid(token)

    def sqbracket(self, token):
        """Encountered a square bracket. Only opening brackets are handled here.
        """
        if token.data == "[" and self.state in [MidlState.DEFAULT, MidlState.DEF_COMPLETE]:
            self.cur_def_attrs.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
            self.state = MidlState.DEFAULT
        else:
            # Note that the closing square bracket is handled within the MidlInterfaceParser
            self.invalid(token)

    def semicolon(self, token):
        if self.state != MidlState.DEF_COMPLETE:
            self.invalid(token)
        self.state = MidlState.DEFAULT

    def comment(self, token):
        """Record the comment
        """
        self.definition.add_comment(token)
        return

    def directive(self, token):
        if token.data.startswith("#define"):
            self.definition.defines.append(token.data)
            self.state = MidlState.DEFAULT

    def parse(self, cur_token):
        try:
            return super().parse(cur_token)
        except StopIteration:
            return self.finished()

    def finished(self) -> MidlDefinition:
        if not self.definition:
            raise MidlParserException(f"Failed to parse definition.")
        return self.definition

def parse_idl(idl_file: pathlib.Path):
    data = idl_file.read_text()
    if not data:
        raise MidlParserException(f"File `{idl_file}` is empty")
    tokenizer = MidlTokenizer(data, idl_file.name)
    tokens = tokenizer.get_token()
    first_token = next(tokens)
    return MidlParser(tokens,tokenizer).parse(first_token)