import enum

from midl import MidlProcedure, MidlVarDef
from .attributes import MidlAttributesParser
from .arrays import MidlArrayParser
from .base import MidlBaseParser, MidlParserException
from .midltokenizer import Token

class ProcedureState(enum.Enum):
    PROC_TYPE_OR_ATTRS = enum.auto()
    PROC_TYPE = enum.auto()
    PARAM_TYPE_OR_ATTRS = enum.auto()
    PARAM_TYPE = enum.auto()
    PARAM_ARRAY = enum.auto()
    PARAM_DEFINED = enum.auto() # Special case when a keyword is used as the param name
    PROC_END = enum.auto()
    END = enum.auto()

class MidlProcedureParser(MidlBaseParser):
    """Parse a function declaration
    
    [ [function-attribute-list] ] type-specifier [pointer-declarator] function-name(
    [ in [ , parameter-attribute-list ] ] type-specifier [declarator]
    , ...);
    
    References: https://docs.microsoft.com/en-us/windows/win32/midl/function-call-attributes
    """
    def __init__(self, token_generator, tokenizer):
        self.state = ProcedureState.PROC_TYPE_OR_ATTRS
        super().__init__(token_generator=token_generator, end_state=ProcedureState.END, tokenizer=tokenizer)
        self.cur_param_type_parts = []
        self.cur_param_attrs = {}
        self.cur_param_array_info = []
        self.type_parts = []
        self.attributes = {}
        self.parameters = []
        self.comments = []
        self.name = None
        self.type = None
        self.void = False
        self.rbracket_depth = 0

    def finish_cur_param(self):
        param_name = self.cur_param_type_parts[-1]
        param_type = ' '.join(self.cur_param_type_parts[:-1])
        self.parameters.append(MidlVarDef(param_type, param_name, self.cur_param_attrs, self.cur_param_array_info))
        self.cur_param_type_parts = []
        self.cur_param_attrs = {}
        self.cur_param_array_info = []

    def semicolon(self, token: Token):
        if self.state == ProcedureState.PROC_END:
            self.state = ProcedureState.END
        else:
            self.invalid(token)

    def keyword(self, token):
        # Like symbols, keywords can be part of the proc name or param names
        self.symbol(token)

    def symbol(self, token):
        if self.state in [ProcedureState.PROC_TYPE, ProcedureState.PROC_TYPE_OR_ATTRS]:
            self.type_parts.append(token.data)
            self.state = ProcedureState.PROC_TYPE
        elif self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_TYPE_OR_ATTRS]:
            self.cur_param_type_parts.append(token.data)
            self.state = ProcedureState.PARAM_TYPE
        else:
            self.invalid(token)

    def rbracket(self, token):
        if token.data == '(':
            if self.state == ProcedureState.PROC_TYPE:
                # We can now set our name and type
                self.name = self.type_parts[-1]
                self.type = ' '.join(self.type_parts[:-1])
                self.state = ProcedureState.PARAM_TYPE_OR_ATTRS
            elif self.state in [ProcedureState.PARAM_TYPE_OR_ATTRS, ProcedureState.PARAM_TYPE]:
                self.cur_param_type_parts += '('
                self.rbracket_depth += 1
                self.state = ProcedureState.PARAM_TYPE
        elif token.data == ')':
            if self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY] and self.rbracket_depth == 0:
                self.finish_cur_param()
                self.state = ProcedureState.PROC_END
            elif self.state == ProcedureState.PARAM_TYPE:
                self.cur_param_type_parts += ')'
                self.rbracket_depth -= 1
            elif self.state == ProcedureState.PARAM_TYPE_OR_ATTRS and not len(self.parameters):
                # This function takes no parameters
                self.void = True
                self.state = ProcedureState.PROC_END
            else:
                self.invalid()
        else:
            self.invalid(token)

    def comma(self, token):
        if self.state not in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            self.invalid(token)
        # Add the parameter to the list
        self.finish_cur_param()
        self.state = ProcedureState.PARAM_TYPE_OR_ATTRS
    
    def sqbracket(self, token):
        if self.state == ProcedureState.PROC_TYPE_OR_ATTRS:
            if token.data == "[":
                self.attributes.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
            else:
                self.invalid(token)
        elif self.state == ProcedureState.PARAM_TYPE_OR_ATTRS:
            if token.data == "[":
                self.cur_param_attrs.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
            else:
                self.invalid(token)
        elif self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            # The parameter has (possibly additional) array dimensions specified..
            array_parser = MidlArrayParser(self.tokens, self.tokenizer)
            self.cur_param_array_info.append(array_parser.parse(token))
            self.state = ProcedureState.PARAM_ARRAY
        else:
            self.invalid(token)

    def operator(self, token):
        if token.data == "*" and self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_TYPE_OR_ATTRS]:
            # Encountered a pointer, append it to the current type
            self.cur_param_type_parts[-1] += "*"
            self.state = ProcedureState.PARAM_TYPE
        else:
            self.invalid(token)

    def comment(self, token):
        self.comments.append(token)

    def finished(self) -> MidlProcedure:
        if not self.name:
            raise MidlParserException("No name was parsed")
        elif not self.parameters and not self.void:
            raise MidlParserException("No parameters were parsed")
        return MidlProcedure(self.name, self.attributes, self.parameters)

