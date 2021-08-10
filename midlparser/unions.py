
import enum

from midl import MidlUnionDef, MidlVarDef
from .attributes import MidlAttributesParser
from .arrays import MidlArrayParser
from .base import MidlBaseParser, MidlParserException

class UnionState(enum.Enum):
    BEGIN = enum.auto()
    UNION_NAME = enum.auto()
    UNION_BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    MEMBER_ARRAY = enum.auto()
    UNION_END = enum.auto()
    END = enum.auto()

class MidlUnionParser(MidlBaseParser):
    """class that parses a union
    """
    def __init__(self, token_generator, tokenizer):
        self.state = UnionState.BEGIN
        super().__init__(token_generator=token_generator, end_state=UnionState.END, tokenizer=tokenizer)
        self.cur_member_attrs = []
        # This is a list because the type and name can be several tokens e.g. 'unsigned long long varname'
        self.cur_member_parts = [] 
        self.cur_member_array_info = []
        self.members = []
        self.comments = []
        self.private_name = None
        self.declared_names = ''
        self.embedded_struct_count = 0
        self.embedded_union_count = 0
    
    def add_current_member(self):
        """Add the currently tracked member to the union
        """
        member_name = self.cur_member_parts[-1]
        member_type = ' '.join(self.cur_member_parts[:-1])
        member_attrs = self.cur_member_attrs[:]
        member_def = MidlVarDef(member_type, member_name, member_attrs, self.cur_member_array_info)
        self.members.append(member_def)
        self.prev_member = member_def
        self.cur_member_parts = []
        self.cur_member_attrs = []
        self.cur_member_array_info = []

    def keyword(self, token):
        if self.state == UnionState.BEGIN:
            if token.data != 'union':
                self.invalid(token)
            self.state = UnionState.UNION_BODY
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_TYPE_OR_ATTR]:
            # Embedded
            if token.data == 'struct':
                from .structs import MidlStructParser
                struct_type = MidlStructParser(self.tokens).parse(token)
                if not len(struct_type.public_names):
                    struct_type.public_names.append(f's{self.embedded_struct_count}')
                    self.embedded_struct_count += 1
                var_def = MidlVarDef(struct_type, struct_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            elif token.data == 'union':
                union_type = MidlUnionParser(self.tokens).parse(token)
                if not len(union_type.public_names):
                    union_type.public_names.append(f'u{self.embedded_union_count}')
                    self.embedded_union_count += 1
                var_def = MidlVarDef(union_type, union_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            else:
                self.cur_member_parts.append(token.data)
        else:
            self.invalid(token)

    def symbol(self, token):
        if self.state == UnionState.UNION_NAME:
            self.private_name = token.data
            self.state = UnionState.UNION_BODY
        elif self.state in [UnionState.MEMBER_TYPE_OR_ATTR, UnionState.MEMBER_TYPE]:
            self.cur_member_parts.append(token.data)
            if self.state == UnionState.MEMBER_TYPE_OR_ATTR:
                self.state = UnionState.MEMBER_TYPE
        elif self.state == UnionState.UNION_END:
            self.declared_names += token.data
        else:
            self.invalid(token)

    def sqbracket(self, token):
        if self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            self.cur_member_attrs.extend(MidlAttributesParser(self.tokens).parse(token))
            # Don't transition out of the TYPE_OR_ATTR if the attributes was a switch-case
            if 'case' in self.cur_member_attrs:
                self.state == UnionState.MEMBER_TYPE
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_ARRAY]:
            # The member has (possibly additional?) array dimensions specified..
            array_parser = MidlArrayParser(self.tokens)
            self.cur_member_array_info.append(array_parser.parse(token))
            self.state = UnionState.MEMBER_ARRAY
        else:
            self.invalid(token)

    def brace(self, token):
        # Unions can be unnamed
        if token.data == '{' and self.state in [UnionState.UNION_BODY, UnionState.UNION_NAME]:
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            self.state = UnionState.UNION_END
        else:
            self.invalid(token)

    def semicolon(self, token):
        # End of variable definition, add the current type
        if self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_ARRAY]:
            self.add_current_member()
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        elif self.state == UnionState.UNION_END:
            # End of structure definition and optional vars
            self.state = UnionState.END
        else:
            self.invalid(token)

    def operator(self, token):
        if token.data == "*" and self.state in [UnionState.MEMBER_TYPE, UnionState.UNION_END]:
            if self.state == UnionState.MEMBER_TYPE:
                # Encountered a pointer, append it to the current type
                self.cur_member_parts[-1] += "*"
            elif self.state == UnionState.UNION_END:
                self.declared_names += '*'
        else:
            self.invalid(token)

    def comment(self, token):
        self.comments.append(token)

    def finished(self) -> MidlUnionDef:
        if not len(self.members):
            raise MidlParserException("No members parsed in structure!")
        public_names = []
        if self.declared_names:
            public_names = self.declared_names.split(',')
        return MidlUnionDef(public_names, self.private_name, self.members)
    
