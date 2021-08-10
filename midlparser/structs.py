import enum

from midl import MidlStructDef, MidlVarDef
from .attributes import MidlAttributesParser
from .arrays import MidlArrayParser
from .base import MidlBaseParser, MidlParserException

class StructState(enum.Enum):
    BEGIN = enum.auto()
    STRUCT_NAME = enum.auto()
    STRUCT_BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    MEMBER_REPEAT = enum.auto()
    MEMBER_ARRAY = enum.auto()
    STRUCT_END = enum.auto()
    END = enum.auto()


class MidlStructParser(MidlBaseParser):
    """class that parses a struct
    """

    def __init__(self, token_generator, tokenizer):
        self.state = StructState.BEGIN
        super().__init__(token_generator=token_generator, end_state=StructState.END, tokenizer=tokenizer)
        self.prev_member = None
        self.cur_member_attrs = []
        # This is a list because the type and name can be several symbols e.g. 'unsigned long long varname'
        self.cur_member_parts = [] 
        self.cur_member_array_info = []
        self.members = []
        self.comments = []
        self.private_name = None
        self.declared_names = ''
        self.embedded_struct_count = 0
        self.embedded_union_count = 0
        

    def add_current_member(self):
        """Add the currently tracked member to the structure
        """
        if self.state == StructState.MEMBER_REPEAT:
            # Add the repeated type. Make sure we have only read a name so far
            if len(self.cur_member_parts) > 1:
                raise MidlParserException(f"Repeated member should only have a name: {self.cur_member_parts}")
            # Since we're repeating, set the attributes
            member_name = self.cur_member_parts[0]
            member_type = self.prev_member.type
            member_attrs = self.prev_member.attrs
        else:
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
        if self.state == StructState.BEGIN:
            if token.data != 'struct':
                self.invalid(token)
            self.state = StructState.STRUCT_NAME
        elif self.state in [StructState.MEMBER_TYPE_OR_ATTR, StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
            # Embedded
            if token.data == 'struct':
                struct_type = MidlStructParser(self.tokens).parse(token)
                if not struct_type.public_names:
                    struct_type.public_names.append(f's{self.embedded_struct_count}')
                    self.embedded_struct_count += 1
                var_def = MidlVarDef(struct_type, struct_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = StructState.MEMBER_TYPE_OR_ATTR
            elif token.data == 'union':
                from .unions import MidlUnionParser
                union_type = MidlUnionParser(self.tokens).parse(token)
                if not union_type.public_names:
                    union_type.public_names.append(f'u{self.embedded_union_count}')
                    self.embedded_union_count += 1
                var_def = MidlVarDef(union_type, union_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = StructState.MEMBER_TYPE_OR_ATTR
            else:
                # This is part of the type/name e.g unsigned long ptr
                self.cur_member_parts.append(token.data)
        else:
            self.invalid(token)

    def symbol(self, token):
        if self.state == StructState.STRUCT_NAME:
            self.private_name = token.data
            self.state = StructState.STRUCT_BODY
        elif self.state in [StructState.MEMBER_TYPE_OR_ATTR, StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
            self.cur_member_parts.append(token.data)
            if self.state == StructState.MEMBER_TYPE_OR_ATTR:
                self.state = StructState.MEMBER_TYPE
        elif self.state == StructState.STRUCT_END:
            self.declared_names += token.data
        else:
            self.invalid(token)

    def comma(self, token):
        if self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
            # Add this member, and (re)enter repeat mode
            self.add_current_member()
            self.state = StructState.MEMBER_REPEAT
        elif self.state == StructState.STRUCT_END:
            self.declared_names += ','
        else:
            self.invalid(token)
    
    def sqbracket(self, token):
        if self.state == StructState.MEMBER_TYPE_OR_ATTR:
            self.cur_member_attrs = MidlAttributesParser(self.tokens).parse(token)
            self.state = StructState.MEMBER_TYPE
        elif self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_ARRAY]:
            # The member has (possibly additional) array dimensions specified..
            self.cur_member_array_info.append(MidlArrayParser(self.tokens).parse(token))
            self.state = StructState.MEMBER_ARRAY
        else:
            self.invalid(token)

    def brace(self, token):
        # The struct might be unnamed, so we might be in the STRUCT_NAME state.
        if token.data == '{' and self.state in [StructState.STRUCT_BODY, StructState.STRUCT_NAME]:
            self.state = StructState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == StructState.MEMBER_TYPE_OR_ATTR:
            self.state = StructState.STRUCT_END
        else:
            self.invalid(token)
        
    def semicolon(self, token):
        # End of variable definition, add the current type
        if self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT, StructState.MEMBER_ARRAY]:
            self.add_current_member()
            self.state = StructState.MEMBER_TYPE_OR_ATTR
        elif self.state == StructState.STRUCT_END:
            # End of structure definition and optional vars
            self.state = StructState.END
        else:
            self.invalid(token)

    def operator(self, token):
        if token.data == "*" and self.state in [StructState.MEMBER_TYPE, StructState.STRUCT_END]:
            if self.state == StructState.MEMBER_TYPE:
                # Encountered a pointer, append it to the current type
                self.cur_member_parts[-1] += "*"
            elif self.state == StructState.STRUCT_END:
                self.declared_names += '*'
        else:
            self.invalid(token)

    def comment(self, token):
        self.comments.append(token)

    def finished(self) -> MidlStructDef:
        if not len(self.members):
            raise MidlParserException("No members parsed in structure!")
        public_names = []
        if self.declared_names:
            public_names = self.declared_names.split(',')
        return MidlStructDef(public_names, self.private_name, self.members)

