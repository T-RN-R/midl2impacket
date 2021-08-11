
import enum
from typing import Union
from midlparser.midltokenizer import TokenType

from midl import MidlAttribute, MidlStructDef, MidlUnionDef, MidlVarDef
from .attributes import MidlAttributesParser
from .arrays import MidlArrayParser
from .base import MidlBaseParser
from .util import SkipClosureParser

class UnionState(enum.Enum):
    BEGIN = enum.auto()
    UNION_NAME = enum.auto()
    UNION_BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    MEMBER_CASE = enum.auto()
    MEMBER_ARRAY = enum.auto()
    UNION_END = enum.auto()
    END = enum.auto()

class MidlUnionParser(MidlBaseParser):
    """class that parses a union
    """
    def __init__(self, token_generator, tokenizer):
        self.state = UnionState.BEGIN
        super().__init__(token_generator=token_generator, end_state=UnionState.END, tokenizer=tokenizer)
        self.cur_member_attrs = {}
        # This is a list because the type and name can be several tokens e.g. 'unsigned long long varname'
        self.cur_member_parts = [] 
        self.cur_member_array_info = []
        self.members = []
        self.comments = []
        self.private_name = ''
        self.declared_names = ''
        self.embedded_struct_count = 0
        self.embedded_union_count = 0
        # If we're actually a switched struct
        self.switch_param = None
        self.struct_private_name = None
    
    def add_current_member(self):
        """Add the currently tracked member to the union
        """
        member_name = self.cur_member_parts[-1]
        member_type = ' '.join(self.cur_member_parts[:-1])
        member_attrs = self.cur_member_attrs
        member_def = MidlVarDef(member_type, member_name, member_attrs, self.cur_member_array_info)
        self.members.append(member_def)
        self.prev_member = member_def
        self.cur_member_parts = []
        self.cur_member_attrs = {}
        self.cur_member_array_info = []

    def keyword(self, token):
        if self.state == UnionState.BEGIN:
            if token.data != 'union':
                self.invalid(token)
            self.state = UnionState.UNION_NAME
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_TYPE_OR_ATTR]:
            # Embedded
            if token.data == 'struct':
                from .structs import MidlStructParser
                struct_type = MidlStructParser(self.tokens, self.tokenizer).parse(token)
                if not len(struct_type.public_names):
                    struct_type.public_names.append(f's{self.embedded_struct_count}')
                    self.embedded_struct_count += 1
                var_def = MidlVarDef(struct_type, struct_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            elif token.data == 'union':
                union_type = MidlUnionParser(self.tokens, self.tokenizer).parse(token)
                if not len(union_type.public_names):
                    union_type.public_names.append(f'u{self.embedded_union_count}')
                    self.embedded_union_count += 1
                var_def = MidlVarDef(union_type, union_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            elif self.state == UnionState.MEMBER_TYPE_OR_ATTR and token.data in ["case", "default"]:
                if token.data == "case":
                    self.state = UnionState.MEMBER_CASE
                else:
                    self.cur_member_attrs['default'] = MidlAttribute(name="default")
                    assert(next(self.tokens).data == ':')
            else:
                self.cur_member_parts.append(token.data)
        elif self.state == UnionState.UNION_BODY and token.data == "switch":
            # We're actually a struct with a switched union inside of it.
            # Our union discriminant is the switch parameter
            switch_param_token = next(self.tokens)
            assert(switch_param_token.data == '(')
            switch_param = SkipClosureParser(self.tokens, self.tokenizer, '(', ')').parse(switch_param_token)
            # Grab the discriminant type/name as it will be a parameter in the struct
            switch_param_parts = switch_param.rsplit(' ', 1)
            switch_param_name = switch_param_parts[-1]
            switch_param_type = ' '.join(switch_param_parts[:-1])
            self.switch_param = MidlVarDef(switch_param_type, switch_param_name)
            # Reset our state so that we'll parse our union member starting here
            self.struct_private_name = self.private_name
            self.private_name = ''
            self.state = UnionState.UNION_NAME
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
        elif self.state == UnionState.MEMBER_CASE:
            self.cur_member_attrs['case'] = MidlAttribute(name="case", params=[token.data])
            assert(next(self.tokens).data == ':')
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        else:
            self.invalid(token)

    def sqbracket(self, token):
        if self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            self.cur_member_attrs.update(MidlAttributesParser(self.tokens, self.tokenizer).parse(token))
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_ARRAY]:
            # The member has (possibly additional?) array dimensions specified..
            array_parser = MidlArrayParser(self.tokens, self.tokenizer)
            self.cur_member_array_info.append(array_parser.parse(token))
            self.state = UnionState.MEMBER_ARRAY
        else:
            self.invalid(token)

    def comma(self, token):
        if self.state == UnionState.UNION_END:
            self.declared_names += ','
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
        elif self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            if 'default' not in self.cur_member_attrs and 'case' not in self.cur_member_attrs:
                self.invalid()
            # Add an empty parameter with the case/default attribute
            member_def = MidlVarDef(None, None, self.cur_member_attrs, None)
            self.members.append(member_def)
            self.prev_member = member_def
            self.cur_member_attrs = {}
        else:
            self.invalid(token)

    def operator(self, token):
        if token.data == "*" and self.state in [UnionState.MEMBER_TYPE, UnionState.UNION_END, UnionState.MEMBER_TYPE_OR_ATTR]:
            if self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_TYPE_OR_ATTR]:
                # Encountered a pointer, append it to the current type
                self.cur_member_parts[-1] += "*"
                self.state = UnionState.MEMBER_TYPE
            elif self.state == UnionState.UNION_END:
                self.declared_names += '*'
        else:
            self.invalid(token)

    def comment(self, token):
        self.comments.append(token)

    def finished(self) -> MidlUnionDef:
        public_names = []
        if self.declared_names:
            public_names = self.declared_names.split(',')
        if self.switch_param and self.struct_private_name:
            switch_union = MidlUnionDef([], self.private_name, self.members)
            switch_var = MidlVarDef(switch_union, switch_union.private_name)
            struct_members = [self.switch_param, switch_var]
            return MidlStructDef(public_names, self.struct_private_name, struct_members)
        else:
            return MidlUnionDef(public_names, self.private_name, self.members)
        
    
