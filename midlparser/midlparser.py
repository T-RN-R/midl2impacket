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
from .midltokenizer import MidlTokenizer

class MidlState(enum.Enum):
    """Class used to handle state transitions for top level MidlParser
    """
    DEFAULT = enum.auto()
    IMPORT = enum.auto()
    IMPORT_COMPLETE = enum.auto()
    DEF_COMPLETE = enum.auto()
    ATTR_DEFINITION = enum.auto()
    DEFINITION = enum.auto()
    OPEN_SQBRACKET = enum.auto()
    CLOSE_SQBRACKET= enum.auto()
    COMMENT = enum.auto()
    END = enum.auto()

class MidlParser(MidlBaseParser):
    """Parses a complete MIDL file into a MidlDefiniton object
        This class maintains a state machine.
    """

    def __init__(self, token_generator):
        self.state = MidlState.DEFAULT # Current state of the parsing
        super().__init__(token_generator=token_generator, end_state=MidlState.END)
        self.definition = MidlDefinition() # data to be returned by calling parse()
        self.cur_def_attrs = {}

    def keyword(self, token):
        """Handles encountered keywords
        """
        if token.data == "import":
            self.state = MidlState.IMPORT
        elif token.data == 'typedef':
            self.definition.typedefs.extend(
                MidlTypedefParser(self.tokens).parse(token)
            )
        elif token.data == 'enum':
            self.definition.typedefs.append(
                MidlEnumParser(self.tokens).parse(token)
            )
        elif self.state == MidlState.ATTR_DEFINITION:
            if token.data == 'interface':
                iface = MidlInterfaceParser(self.tokens).parse(token)
                iface.attributes = self.cur_def_attrs
                self.definition.interfaces.append(iface)
                self.cur_def_attrs = {}
                self.state = MidlState.DEF_COMPLETE
            elif token.data == 'coclass':
                coclass = MidlCoclassParser(self.tokens).parse(token)
                self.definition.coclasses.append(coclass)
                self.state = MidlState.DEF_COMPLETE
            elif token.data == 'dispinterface':
                dispinterface = MidlDispInterfaceParser(self.tokens).parse(token)
                self.definition.dispinterfaces.append(dispinterface)
                self.state = MidlState.DEF_COMPLETE
            else:
                self.invalid(token)
        else:
            self.state = MidlState.DEFINITION
            self.definition.instantiation.append(
                MidlVariableInstantiationParser(self.tokens).parse(token)
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
            self.cur_def_attrs = MidlAttributesParser(self.tokens).parse(token)
            self.state = MidlState.ATTR_DEFINITION
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

    def parse(self, cur_token):
        try:
            return super().parse(cur_token)
        except StopIteration:
            return self.finished()

    def finished(self) -> MidlDefinition:
        """Parsing loop that iterates over tokens and invokes their handler function.
             If an unhandled token does not have a registered handler, an out of bounds access will occur in the tok_handlers dict.
             Note that this should never happen with a well formed test case (unless something hasn't been considered.)

        Args:
            data (str): [description]

        Returns:
            MidlDefinition: [description]
        """
        if not self.definition:
            raise MidlParserException(f"Failed to parse definition.")
        return self.definition

def parse_idl(idl_file: pathlib.Path):
    data = idl_file.read_text()
    if not data:
        raise MidlParserException(f"File `{idl_file}` is empty")
    tokenizer = MidlTokenizer(data)
    tokens = tokenizer.get_token()
    first_token = next(tokens)
    return MidlParser(tokens).parse(first_token)