import traceback
from midl import *
from .state import *
from .midltokenizer import Token, TokenType, MidlTokenizer

"""This file contains a series of classes that are responsible for parsing discrete parts of a MIDL file.

    MidlParser
    MidlVarDefParser
    MidlTypeDefParse
    MidlInterfaceParser
    TODO: MidlProcedureParser

""" 

class MidlVariableInstantiationParser():
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.state = VariableInstantiationState.TYPE
        self.rbracket_level = 0
        self.brace_level = 0
        self.type_parts = []
        self.value_parts = []
        self.tok_handlers = { 
            TokenType.KEYWORD : MidlVariableInstantiationParser.handle_keyword,
            TokenType.SYMBOL : MidlVariableInstantiationParser.handle_symbol,
            TokenType.NUMERIC : MidlVariableInstantiationParser.handle_numeric,
            TokenType.SQBRACKET : MidlVariableInstantiationParser.handle_sqbracket,
            TokenType.RBRACKET : MidlVariableInstantiationParser.handle_rbracket,
            TokenType.BRACE : MidlVariableInstantiationParser.handle_brace,
            TokenType.SEMICOLON : MidlVariableInstantiationParser.handle_semicolon,
            TokenType.OPERATOR : MidlVariableInstantiationParser.handle_operator,
        }

    def add_state_data(self, token: Token):
        if self.state == VariableInstantiationState.TYPE:
            self.type_parts.append(token.data)
        elif self.state == VariableInstantiationState.VALUE:
            self.value_parts.append(token.data)
        else:
            raise Exception(f"Unexpected token [{token.type}: {token.data}] in state {self.state}")

    def handle_keyword(self, token: Token):
        self.add_state_data(token)

    def handle_symbol(self, token: Token):
        self.add_state_data(token)

    def handle_numeric(self, token: Token):
        if self.state != VariableInstantiationState.VALUE:
            raise Exception(f"Unexpected numeric {token.data} in state {self.state}")
        self.value_parts.append(token.data)

    def handle_rbracket(self, token):
        if self.state == VariableInstantiationState.VALUE:
            # Just make sure they're balanced since we're not evaluating
            if token.data == '(': 
                self.rbracket_level += 1
            elif token.data == ')' and self.rbracket_level > 0: 
                self.rbracket_level -= 1
            else: 
                raise Exception(f"Unexpected rbracket {token.data} in state {self.state}")
            self.value_parts += token.data
        else:
            raise Exception(f"Unexpected rbracket {token.data} in state {self.state}")   

    def handle_sqbracket(self, token):
        if token.data == '[' and self.state in [VariableInstantiationState.TYPE, VariableInstantiationState.TYPE_ARRAY]:
            # Grab the array dimensions for the type
            self.value_dimensions.append(MidlArrayParser(self.tokens).parse(token))
            self.state = VariableInstantiationState.TYPE_ARRAY
            self.type_parts.append(token.data)
        elif self.state == VariableInstantiationState.VALUE:
            self.value_parts.append(token.data)
        else:
            raise Exception(f"Unexpected sqbracket {token.data} in state {self.state}")

    def handle_brace(self, token):
        if self.state == VariableInstantiationState.VALUE:
            # Just make sure they're balanced since we're not evaluating
            if token.data == '{': 
                self.brace_level += 1
            elif token.data == '}' and self.brace_level > 0: 
                self.brace_level -= 1
            else: 
                raise Exception(f"Unexpected brace {token.data} in state {self.state}")
            self.value_parts += token.data
        else:
            raise Exception(f"Unexpected brace {token.data} in state {self.state}")   

    def handle_operator(self, token):
        if self.state in [VariableInstantiationState.TYPE, VariableInstantiationState.TYPE_ARRAY] and token.data == '=':
            # Make sure there is data for our name and type
            if not len(self.type_parts) > 1:
                raise Exception(f"No type data before '='")
            self.name = self.type_parts[-1]
            self.type = self.type_parts [:-1]
            self.state = VariableInstantiationState.VALUE
        elif self.state == VariableInstantiationState.VALUE:
            # Operator that's part of the value
            self.value_parts.append(token.data)
        else:
            raise Exception(f"Unexpected operator {token.data} in state {self.state}")

    def handle_semicolon(self, _):
        # Make sure we have some value data
        if self.state == VariableInstantiationState.VALUE and len(self.value_parts):
            self.state = VariableInstantiationState.END
        else:
            raise Exception(f"Unexpected semicolon in state {self.state}")

    def parse(self, cur_token) -> MidlVariableInstantiation:
        while cur_token:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == VariableInstantiationState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                print(self.type_parts, self.value_parts)
                print(cur_token.data)
                exit()
        var_name = self.type_parts[-1]
        var_type = ' '.join(self.type_parts[:-1])
        var_value = ' '.join(self.value_parts)
        instantiation = MidlVariableInstantiation(var_type, var_name, rhs=var_value, const=var_type[0]=='const')
        return instantiation

class MidlParser():
    """Parses a complete MIDL file into a MidlDefiniton object
        This class maintains a state machine.
    """

    def __init__(self):
        self.state = MidlState.DEFAULT # Current state of the parsing
        self.definition = MidlDefinition() # data to be returned by calling parse()
        self.tok_handlers = { # Jump table to handle different token types
            TokenType.KEYWORD : MidlParser.handle_keyword,
            TokenType.STRING : MidlParser.handle_string,
            TokenType.SQBRACKET : MidlParser.handle_sqbracket,
            TokenType.COMMENT : MidlParser.handle_comment,
            TokenType.SEMICOLON : MidlParser.handle_semicolon,
        }

    def handle_keyword(self, token):
        """Handles encountered keywords
        """
        if token.data == "import":
            self.state = MidlState.IMPORT
        elif token.data == 'typedef':
            self.definition.typedefs.append(
                MidlTypedefParser(self.tokens).parse(token)
            )
        else:
            self.state = MidlState.DEFINITION
            self.definition.instantiation.append(
                MidlVariableInstantiationParser(self.tokens).parse(token)
            )
            self.state = MidlState.DEFAULT

    def handle_string(self, token):
        """Encountered a string. Should only ever be imports encountered here.
        """
        if self.state == MidlState.IMPORT:
            # Encountered an import statement so add it to the definition's imports
            self.definition.add_import(token.data)
            self.state = MidlState.IMPORT_COMPLETE
        else:
            raise Exception(f"Unexpected string {token.data} in state {self.state}")

    def handle_sqbracket(self, token):
        """Encountered a square bracket. Only opening brackets are handled here.
        """
        if token.data == "[" and self.state == MidlState.DEFAULT:
            # We hit the start of an interface definition, specifically the header, spin up a parser
            interface = MidlInterfaceParser(self.tokens).parse(token)
            self.definition.add_interface(interface)
        else:
            # Note that the closing square bracket is handled within the MidlInterfaceParser
            raise Exception(f"Unexpected sqbracket {token.data} in state {self.state}")

    def handle_semicolon(self, _):
        if self.state != MidlState.IMPORT_COMPLETE:
            raise Exception(f"Unexpected semicolon in state {self.state}")
        self.state = MidlState.DEFAULT

    def handle_comment(self, token):
        """Record the comment
        """
        self.definition.add_comment(token)
        return

    def parse(self, data:str ) -> MidlDefinition:
        """Parsing loop that iterates over tokens and invokes their handler function.
             If an unhandled token does not have a registered handler, an out of bounds access will occur in the tok_handlers dict.
             Note that this should never happen with a well formed test case (unless something hasn't been considered.)

        Args:
            data (str): [description]

        Returns:
            MidlDefinition: [description]
        """
        tokenizer = MidlTokenizer(data)
        self.tokens = tokenizer.get_token()
        cur_token = next(self.tokens)
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens, None)
            except Exception:
                traceback.print_exc()
                print(self.definition)
                print(cur_token.data)
                exit()
        return self.definition

class MidlUnionParser():
    """class that parses a union
    """
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.cur_member_attrs = []
        # This is a list because the type and name can be several tokens e.g. 'unsigned long long varname'
        self.cur_member_parts = [] 
        self.cur_member_array_info = []
        self.members = []
        self.comments = []
        self.private_name = None
        self.declared_names = ''
        self.state = UnionState.BEGIN
        self.tok_handlers = {
            TokenType.KEYWORD : MidlUnionParser.handle_keyword,
            TokenType.SQBRACKET : MidlUnionParser.handle_sqbracket,
            TokenType.SYMBOL : MidlUnionParser.handle_symbol,
            TokenType.SEMICOLON : MidlUnionParser.handle_semicolon,
            TokenType.BRACE : MidlUnionParser.handle_brace,
            TokenType.OPERATOR : MidlUnionParser.handle_operator,
            TokenType.COMMENT: MidlUnionParser.handle_comment,
        }
    
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
        self.embedded_struct_count = 0
        self.embedded_union_count = 0

    def handle_keyword(self, token):
        if self.state == UnionState.BEGIN:
            if token.data != 'union':
                raise Exception(f"Unexpected token: {token.data}. Expected 'union'")
            self.state = UnionState.UNION_BODY
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_TYPE_OR_ATTR]:
            # Embedded
            if token.data == 'struct':
                struct_type = MidlStructParser(self.tokens).parse(token)
                if not struct_type.public_names:
                    struct_type.public_names.append(f's{self.embedded_struct_count}')
                    self.embedded_struct_count += 1
                var_def = MidlVarDef(struct_type, struct_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            elif token.data == 'union':
                union_type = MidlUnionParser(self.tokens).parse(token)
                if not union_type.public_names:
                    union_type.public_names.append(f'u{self.embedded_union_count}')
                    self.embedded_union_count += 1
                var_def = MidlVarDef(union_type, union_type.public_names[0], self.cur_member_attrs)
                self.members.append(var_def)
                self.state = UnionState.MEMBER_TYPE_OR_ATTR
            else:
                self.cur_member_parts.append(token.data)
        else:
            raise Exception(f"Unexpected keyword: {token.data} in state {self.state}")

    def handle_symbol(self, token):
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
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_sqbracket(self, token):
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
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_brace(self, token):
        # Unions can be unnamed
        if token.data == '{' and self.state in [UnionState.UNION_BODY, UnionState.UNION_NAME]:
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            self.state = UnionState.UNION_END
        else:
            raise Exception(f"Illegal brace in state {self.state}")

    def handle_semicolon(self, _):
        # End of variable definition, add the current type
        if self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_ARRAY]:
            self.add_current_member()
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        elif self.state == UnionState.UNION_END:
            # End of structure definition and optional vars
            self.state = UnionState.END
        else:
            raise Exception(f"Unexpected semicolon in union definition during state {self.state}")

    def handle_operator(self, token):
        if token.data == "*" and self.state in [UnionState.MEMBER_TYPE, UnionState.UNION_END]:
            if self.state == UnionState.MEMBER_TYPE:
                # Encountered a pointer, append it to the current type
                self.cur_member_parts[-1] += "*"
            elif self.state == UnionState.UNION_END:
                self.declared_names += '*'
        else:
            raise Exception(f"Illegal Operator '{token.data}' in union definition state {self.state}")

    def handle_comment(self, token):
        self.comments.append(token)

    def parse(self, cur_token) -> MidlUnionDef:
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == UnionState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if not len(self.members):
            raise Exception("No members parsed in structure!")
        public_names = self.declared_names.split(',')
        return MidlUnionDef(public_names, self.private_name, self.members)
    
class MidlStructParser():
    """class that parses a struct
    """

    def __init__(self, token_generator):
        self.tokens = token_generator
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
        self.state = StructState.BEGIN
        self.tok_handlers = {
            TokenType.KEYWORD : MidlStructParser.handle_keyword,
            TokenType.SQBRACKET : MidlStructParser.handle_sqbracket,
            TokenType.SYMBOL : MidlStructParser.handle_symbol,
            TokenType.COMMA : MidlStructParser.handle_comma,
            TokenType.SEMICOLON : MidlStructParser.handle_semicolon,
            TokenType.BRACE : MidlStructParser.handle_brace,
            TokenType.OPERATOR : MidlStructParser.handle_operator,
            TokenType.COMMENT: MidlStructParser.handle_comment,
        }

    def add_current_member(self):
        """Add the currently tracked member to the structure
        """
        if self.state == StructState.MEMBER_REPEAT:
            # Add the repeated type. Make sure we have only read a name so far
            if len(self.cur_member_parts) > 1:
                raise Exception(f"Repeated member should only have a name: {self.cur_member_parts}")
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

    def handle_keyword(self, token):
        if self.state == StructState.BEGIN:
            if token.data != 'struct':
                raise Exception(f"Unexpected keyword {token.data}. Struct definition should start with 'struct'")
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
            raise Exception(f"Unexpected keyword: {token.data}")

    def handle_symbol(self, token):
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
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_comma(self, _):
        if self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
            # Add this member, and (re)enter repeat mode
            self.add_current_member()
            self.state = StructState.MEMBER_REPEAT
        elif self.state == StructState.STRUCT_END:
            self.declared_names += ','
        else:
            raise Exception(f"Unexpected comma in state {self.state}")
    
    def handle_sqbracket(self, token):
        if self.state == StructState.MEMBER_TYPE_OR_ATTR:
            self.cur_member_attrs = MidlAttributesParser(self.tokens).parse(token)
            self.state = StructState.MEMBER_TYPE
        elif self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_ARRAY]:
            # The member has (possibly additional) array dimensions specified..
            self.cur_member_array_info.append(MidlArrayParser(self.tokens).parse(token))
            self.state = StructState.MEMBER_ARRAY
        else:
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_brace(self, token):
        # The struct might be unnamed, so we might be in the STRUCT_NAME state.
        if token.data == '{' and self.state in [StructState.STRUCT_BODY, StructState.STRUCT_NAME]:
            self.state = StructState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == StructState.MEMBER_TYPE_OR_ATTR:
            self.state = StructState.STRUCT_END
        else:
            raise Exception(f"Illegal brace in state {self.state}")
        
    def handle_semicolon(self, _):
        # End of variable definition, add the current type
        if self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT, StructState.MEMBER_ARRAY]:
            self.add_current_member()
            self.state = StructState.MEMBER_TYPE_OR_ATTR
        elif self.state == StructState.STRUCT_END:
            # End of structure definition and optional vars
            self.state = StructState.END
        else:
            raise Exception(f"Unexpected semicolon in struct definition during state {self.state}")

    def handle_operator(self, token):
        if token.data == "*" and self.state in [StructState.MEMBER_TYPE, StructState.STRUCT_END]:
            if self.state == StructState.MEMBER_TYPE:
                # Encountered a pointer, append it to the current type
                self.cur_member_parts[-1] += "*"
            elif self.state == StructState.STRUCT_END:
                self.declared_names += '*'
        else:
            raise Exception(f"Illegal Operator '{token.data}' in struct definition state {self.state}")

    def handle_comment(self, token):
        self.comments.append(token)

    def parse(self, cur_token) -> MidlStructDef:
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == StructState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if not len(self.members):
            raise Exception("No members parsed in structure!")
        struct_names = self.declared_names.split(',')
        return MidlStructDef(struct_names, self.private_name, self.members)

class MidlAttributesParser():
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.cur_attr = None
        self.cur_attr_param = ''
        self.cur_attr_params = []
        self.attributes = {}
        self.state = AttributeState.BEGIN
        self.tok_handlers = {
            TokenType.KEYWORD : MidlAttributesParser.handle_keyword,
            TokenType.RBRACKET: MidlAttributesParser.handle_rbracket,
            TokenType.SQBRACKET: MidlAttributesParser.handle_sqbracket,
            TokenType.COMMA: MidlAttributesParser.handle_comma,
            TokenType.SYMBOL: MidlAttributesParser.handle_symbol_and_numeric,
            TokenType.NUMERIC: MidlAttributesParser.handle_symbol_and_numeric,
            TokenType.GUID: MidlAttributesParser.handle_symbol_and_numeric,
            TokenType.OPERATOR: MidlAttributesParser.handle_operator,
            TokenType.DIRECTIVE: MidlAttributesParser.handle_directive,
            
        }

    def handle_operator(self, token):
        if token.data == '*' and self.state == AttributeState.PARAMETERS:
            # It's a pointer
            self.cur_attr_param += token.data
        else:
            raise Exception(f"Unexpected operator {token.data} in attribute state {self.state}")

    def handle_sqbracket(self, token):
        if token.data == '[' and self.state == AttributeState.BEGIN:
            self.state = AttributeState.DEFAULT
        elif token.data == ']' and self.cur_attr:
            self.attributes[self.cur_attr] = MidlAttribute(self.cur_attr, self.cur_attr_params)
            self.state = AttributeState.END
        else:
            raise Exception(f"Unexpected square bracket in attribute state {self.state}")

    def handle_symbol_and_numeric(self, token):            
        if self.state != AttributeState.PARAMETERS:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}.")
        self.cur_attr_param += token.data
        
    def handle_rbracket(self, token):
        if token.data == '(':
            if self.state == AttributeState.PARAMETERS:
                raise Exception("Unexpected bracket within attribute parameter list")
            self.state = AttributeState.PARAMETERS
        elif token.data == ')':
            if self.state != AttributeState.PARAMETERS:
                raise Exception("Unexpected bracket within attribute list")
            self.state = AttributeState.DEFAULT
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ''

    def handle_comma(self, _):
        if self.state == AttributeState.PARAMETERS:
            # It's legal for this to be None in cases like size_is(,*numActualRecords)
            self.cur_attr_params.append(self.cur_attr_param)
            self.cur_attr_param = ''
            return
        elif self.state == AttributeState.DEFAULT and self.cur_attr:
            # End of an attribute
            self.attributes[self.cur_attr] = MidlAttribute(self.cur_attr, self.cur_attr_params)
            self.cur_attr = None
            self.cur_attr_params = []
        else:
            raise Exception(f"Unexpected comma in state {self.state}")

    def handle_keyword(self, token):
        if self.state == AttributeState.PARAMETERS and not self.cur_attr_param:
            self.cur_attr_param = token.data
        elif self.state == AttributeState.DEFAULT and not self.cur_attr:
            self.cur_attr = token.data
        else:
            raise Exception(f"Unexpected keyword {token.data} in state {self.state}")

    def handle_directive(self, token):
        pass

    def parse(self, cur_token) -> list[MidlAttribute]:
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == AttributeState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if len(self.attributes) == 0:
            raise Exception("Parsing attributes failed")
        return self.attributes

class MidlDirectiveParser():
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.state = DirectiveState.BEGIN
        self.tok_handlers = {
            TokenType.POUND: self.handle_pound,
            TokenType.SYMBOL: self.handle_symbol,
        }

    def handle_pound(self, _):
        if self.state == DirectiveState.BEGIN:
            self.state = DirectiveState.TYPE
        else:
            raise Exception(f"Unexpected # in state {self.state}")

    def handle_symbol(self, token):
        if self.state == DirectiveState.TYPE:
            self.type = token.data



    def parse(self, token):
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == AttributeState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if len(self.attributes) == 0:
            raise Exception("Parsing attributes failed")
        return self.attributes


class MidlArrayParser():
    """Array dimensionality parser
    https://docs.microsoft.com/en-us/windows/win32/midl/midl-arrays
    """
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.state = ArrayState.BEGIN
        self.dimensions = [-1, -1] # min, max
        self.cur_dim = ''
        self.tok_handlers = {
            TokenType.SQBRACKET: MidlArrayParser.handle_sqbracket,
            TokenType.NUMERIC : MidlArrayParser.add_data_to_dimension,
            TokenType.OPERATOR : MidlArrayParser.add_data_to_dimension,
            TokenType.SYMBOL: MidlArrayParser.add_data_to_dimension,
            TokenType.ELLIPSIS : MidlArrayParser.handle_ellipsis,
            TokenType.RBRACKET: MidlArrayParser.handle_rbracket,
        }

    def add_data_to_dimension(self, token):
        if self.state not in [ArrayState.BEGIN, ArrayState.END]:
            # Mark that we have *some* data for the current dimension
            if self.state == ArrayState.RANGE_MIN:
                self.state = ArrayState.RANGE_MIN_IN_PROGRESS
            elif self.state == ArrayState.RANGE_MAX:
                self.state = ArrayState.RANGE_MAX_IN_PROGRESS
            self.cur_dim += token.data
        else:
            raise Exception(f"Unexpected {token.type}: {token.data} in state {self.state}")

    def handle_sqbracket(self, token):
        if self.state == ArrayState.BEGIN and token.data == '[':
            self.state = ArrayState.RANGE_MIN
        elif token.data == ']':
            if self.state == ArrayState.RANGE_MIN:
                # This is just an empty [] declaration. We're done
                pass
            elif self.state == ArrayState.RANGE_MIN_IN_PROGRESS:
                self.dimensions[0] = self.cur_dim
            elif self.state == ArrayState.RANGE_MIN_IN_PROGRESS:
                self.dimensions[1] = self.cur_dim
            else:
                raise Exception(f"Unexpected sqbracket in array state {self.state}")    
            self.state = ArrayState.END
        else:
            raise Exception(f"Unexpected sqbracket in array state {self.state}")

    def handle_ellipsis(self, _):
        if self.state == ArrayState.RANGE_MIN_IN_PROGRESS:
            self.dimensions[0] = self.cur_dim
            self.cur_dim = ''
            self.state = ArrayState.RANGE_MAX
        else:
            raise Exception(f"Unexpected ellipsis in state {self.state}")

    def handle_rbracket(self, token):
        if token.data == '(':
            self.rbracket_level += 1
        elif token.data == ')' and self.rbracket_level >= 1:
            self.rbracket_level -= 1
        else:
            raise Exception(f"Unexpected closing bracket in state {self.state}")
        self.cur_dim += token.data

    def parse(self, cur_token) -> MidlArrayDimensions:
        """parsing loop
        """
        while cur_token is not None:
            try:                    
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == ArrayState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        dims = MidlArrayDimensions(self.dimensions[0], self.dimensions[1])
        return dims

class MidlProcedureParser():
    """Parse a function declaration
    
    [ [function-attribute-list] ] type-specifier [pointer-declarator] function-name(
    [ in [ , parameter-attribute-list ] ] type-specifier [declarator]
    , ...);
    
    References: https://docs.microsoft.com/en-us/windows/win32/midl/function-call-attributes
    """
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.cur_param_type_parts = []
        self.cur_param_attrs = []
        self.cur_param_array_info = []
        self.type_parts = []
        self.state = ProcedureState.PROC_TYPE_OR_ATTRS
        self.attrs = []
        self.parameters = []
        self.comments = []
        self.name = None
        self.type = None
        self.tok_handlers = {
            TokenType.RBRACKET : MidlProcedureParser.handle_rbracket,
            TokenType.SQBRACKET : MidlProcedureParser.handle_sqbracket,
            TokenType.SYMBOL : MidlProcedureParser.handle_symbol,
            TokenType.KEYWORD : MidlProcedureParser.handle_keyword,
            TokenType.COMMA : MidlProcedureParser.handle_comma,
            TokenType.OPERATOR : MidlProcedureParser.handle_operator,
            TokenType.COMMENT: MidlProcedureParser.handle_comment,
            TokenType.SEMICOLON: MidlProcedureParser.handle_semicolon,
        }

    def finish_cur_param(self):
        param_name = self.cur_param_type_parts[-1]
        param_type = ' '.join(self.cur_param_type_parts[:-1])
        self.parameters.append(MidlVarDef(param_type, param_name, self.cur_param_attrs, self.cur_param_array_info))
        self.cur_param_type_parts = []
        self.cur_param_attrs = []
        self.cur_param_array_info = []

    def handle_semicolon(self, _):
        if self.state == ProcedureState.PROC_END:
            self.state = ProcedureState.END
        else:
            raise Exception("Unexpected semicolon in procedure definition")

    def handle_keyword(self, token):
        # Like symbols, keywords can be part of the proc name or param names
        self.handle_symbol(token)

    def handle_rbracket(self, token):
        if token.data == '(' and self.state == ProcedureState.PROC_TYPE:
            # We can now set our name and type
            self.name = self.type_parts[-1]
            self.type = ' '.join(self.type_parts[:-1])
            self.state = ProcedureState.PARAM_TYPE_OR_ATTRS
        elif token.data == ')' and self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            self.finish_cur_param()
            self.state = ProcedureState.PROC_END
        else:
            raise Exception(f"Unexpected rbracket in state {self.state}")

    def handle_symbol(self, token):
        if self.state in [ProcedureState.PROC_TYPE, ProcedureState.PROC_TYPE_OR_ATTRS]:
            self.type_parts.append(token.data)
            self.state = ProcedureState.PROC_TYPE
        elif self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_TYPE_OR_ATTRS]:
            self.cur_param_type_parts.append(token.data)
            self.state = ProcedureState.PARAM_TYPE
        else:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_comma(self, _):
        if self.state not in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            raise Exception(f"Unexpected comma in state {self.state}")
        # Add the parameter to the list
        self.finish_cur_param()
        self.state = ProcedureState.PARAM_TYPE_OR_ATTRS
    
    def handle_sqbracket(self, token):
        if self.state == ProcedureState.PROC_TYPE_OR_ATTRS:
            if token.data == "[":
                self.attrs = MidlAttributesParser(self.tokens).parse(token)
                self.state = ProcedureState.PROC_TYPE
            else:
                raise Exception("Unexpected bracket in procedure declaration")
        elif self.state == ProcedureState.PARAM_TYPE_OR_ATTRS:
            if token.data == "[":
                self.cur_param_attrs = MidlAttributesParser(self.tokens).parse(token)
                self.state = ProcedureState.PARAM_TYPE
            else:
                raise Exception("Unexpected bracket in parameter list")
        elif self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            # The parameter has (possibly additional) array dimensions specified..
            array_parser = MidlArrayParser(self.tokens)
            self.cur_param_array_info.append(array_parser.parse(token))
            self.state = ProcedureState.PARAM_ARRAY
        else:
            raise Exception("Unexpected square bracket in procedure definition.")

    def handle_operator(self, token):
        if token.data == "*" and self.state == ProcedureState.PARAM_TYPE:
            # Encountered a pointer, append it to the current type
            self.cur_param_type_parts[-1] += "*"
        else:
            raise Exception(f"Illegal Operator '{token.data}' in state {self.state}")

    def handle_comment(self, token):
        self.comments.append(token)

    def parse(self, cur_token) -> MidlProcedure:
        """parsing loop
        """
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == ProcedureState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                print(f"Failed parsing procedure:")
                print(self.name)
                [print('\t' + param.name) for param in self.parameters]
                exit()
        if len(self.parameters) == 0 :
            raise Exception("Parsing Procedure failed")
        return MidlProcedure(self.name, self.attrs, self.parameters)

class MidlEnumParser():
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.state = EnumState.BEGIN
        self.private_name = None
        self.comments = []
        self.declared_names = ''
        self.cur_member_name = None
        self.cur_member_value = 0
        self.map = {}
        self.tok_handlers = {
            TokenType.BRACE : MidlEnumParser.handle_brace,
            TokenType.SYMBOL : MidlEnumParser.handle_symbol,
            TokenType.KEYWORD : MidlEnumParser.handle_keyword,
            TokenType.COMMA : MidlEnumParser.handle_comma,
            TokenType.OPERATOR : MidlEnumParser.handle_operator,
            TokenType.COMMENT: MidlEnumParser.handle_comment,
            TokenType.SEMICOLON: MidlEnumParser.handle_semicolon,
            TokenType.NUMERIC: MidlEnumParser.handle_numeric,
        }

    def handle_comment(self, token):
        self.comments.append(token)

    def handle_keyword(self, token):
        if self.state == EnumState.BEGIN:
            if token.data != 'enum':
                raise Exception(f"Unexpected keyword {token.data}. Enum definition should start with 'enum'")
            self.state = EnumState.NAME
        else:
            raise Exception(f"Unexpected keyword {token.data} in state {self.state}")

    def handle_numeric(self, token):
        if self.state == EnumState.MEMBER_VALUE:
            self.cur_member_value = int(token.data)
            self.state = EnumState.MEMBER_COMPLETE
        else:
            raise Exception(f"Unexpected numeric value {token.data} in state {self.state}")

    def handle_symbol(self, token):
        if self.state == EnumState.NAME:
            self.private_name = token.data
            self.state = EnumState.BODY
        elif self.state == EnumState.MEMBER_NAME:
            self.cur_member_name = token.data
            self.state = EnumState.MEMBER_OP
        elif self.state == EnumState.ENUM_END:
            self.declared_names += token.data
        else:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_brace(self, token):
        if token.data == '{' and self.state in [EnumState.BODY, EnumState.NAME]:
            self.state = EnumState.MEMBER_NAME
        elif token.data == '}' and self.state in [EnumState.MEMBER_OP, EnumState.MEMBER_COMPLETE]:
            self.state = EnumState.ENUM_END
        else:
            raise Exception(f"Unexpected brace {token.data} in state {self.state}")

    def handle_comma(self, _):
        if self.state in [EnumState.MEMBER_OP, EnumState.MEMBER_COMPLETE]:
            self.map[self.cur_member_name] = self.cur_member_value
            self.state = EnumState.MEMBER_NAME
        elif self.state == EnumState.ENUM_END:
            self.declared_names += ','
        else:
            raise Exception(f"Unexpected comma in state {self.state}")
    
    def handle_operator(self, token):
        if token.data == '=' and self.state == EnumState.MEMBER_OP:
            self.state = EnumState.MEMBER_VALUE
        elif token.data == "*" and self.state == EnumState.ENUM_END:
                self.declared_names += '*'
        else:
            raise Exception(f"Unexpected operator {token.data} in state {self.state}")

    def handle_semicolon(self, _):
        if self.state == EnumState.ENUM_END:
            self.state = EnumState.END
        else:
            raise Exception(f"Unexpected semicolon in state {self.state}")

    def parse(self, cur_token):
        """parsing loop
        """
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == EnumState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if len(self.map.keys()) == 0 :
            raise Exception("Parsing enum failed")
        public_names = self.declared_names.split(',')
        return MidlEnumDef(public_names, self.private_name, self.map)

class MidlTypedefParser():
    """Parses the various kinds of typedefs (structs, enums, inline, and (not yet) unions)
        TODO Those 4 should be in their own parser, but for now keep them this way.
        TODO This class is chaotic because it doesn't maintain a state enum
    """

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.attrs = []
        self.state = TypedefState.BEGIN
        self.td_parts = []
        self.comments = []
        self.cur_additional_name = ''
        self.additional_names = []
        self.tds = []
        self.tok_handlers = {
            TokenType.SYMBOL: MidlTypedefParser.handle_symbol,
            TokenType.KEYWORD : MidlTypedefParser.handle_keyword,
            TokenType.SQBRACKET: MidlTypedefParser.handle_sqbracket,
            TokenType.SEMICOLON: MidlTypedefParser.handle_semicolon,
            TokenType.OPERATOR: MidlTypedefParser.handle_operator,
            TokenType.COMMENT: MidlTypedefParser.handle_comment,
            TokenType.COMMA: MidlTypedefParser.handle_comma,
        }
        self.kw_handlers = {
            'struct': MidlStructParser,
            'enum': MidlEnumParser,
            'union': MidlUnionParser
        }

    def handle_keyword(self, token):
        """Handles the various kinds of typedefs
            TODO: handle unions
        """
        if self.state == TypedefState.BEGIN and token.data == 'typedef':
            self.state = TypedefState.TYPE_OR_ATTRS
        elif self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            if token.data in self.kw_handlers:
                self.state = TypedefState.DEFINITION
                self.tds.append(self.kw_handlers[token.data](self.tokens).parse(token))
                self.state = TypedefState.END
            else:
                return self.handle_symbol(token)
        elif self.state == TypedefState.DEFINITION:
            self.handle_symbol(token)
        else:
            raise Exception(f"Unexpected keyword {token.data} in state {self.state}")

    def handle_symbol(self, token):
        if self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            self.td_parts.append(token.data)
            self.state = TypedefState.DEFINITION
        elif self.state == TypedefState.DEFINITION:
            self.td_parts.append(token.data) 
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.cur_additional_name += token.data
        else:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_operator(self, token):
        if self.state == TypedefState.DEFINITION and token.data == '*':
            self.td_parts[-1] += '*'
        elif self.state == TypedefState.ADDITIONAL_NAMES and token.data == '*':
            self.cur_additional_name += '*'
        else:
            raise Exception(f"Unexpected operator {token.data} in state {self.state}")

    def handle_comment(self, token):
        self.comments.append(token)

    def handle_comma(self, _):
        if self.state == TypedefState.DEFINITION:
            self.state = TypedefState.ADDITIONAL_NAMES
        elif self.state == TypedefState.ADDITIONAL_NAMES:
            self.additional_names.append(self.cur_additional_name)
            self.cur_additional_name = ''
        else:
            raise Exception(f"Unexpected comma in state {self.state}")


    def handle_sqbracket(self, token):
        """ Handles typedef attributes e.g. [v1_enum]
        """
        if self.state == TypedefState.TYPE_OR_ATTRS:
            self.attrs = MidlAttributesParser(self.tokens).parse(token)
            self.state = TypedefState.TYPE
        else:
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_semicolon(self, _):
        if self.state == TypedefState.DEFINITION:
            pass
        elif self.state == TypedefState.ADDITIONAL_NAMES and self.cur_additional_name:
            self.additional_names.append(self.cur_additional_name)
        else:
            raise Exception("Unexpected semicolon in type definition")
        
        self.state = TypedefState.END
        # If we're a simple type we need to create it here
        if not self.tds:
            td_name = self.td_parts[-1]
            td_type = ' '.join(self.td_parts[:-1])
            self.tds.append(MidlSimpleTypedef(td_name, td_type))
            for additional_name in self.additional_names:
                self.tds.append(MidlSimpleTypedef(additional_name, td_type))

    def parse(self, cur_token) -> list[MidlTypeDef]:
        """parsing loop
        """
        while cur_token is not None:
            try:
                #print(cur_token.data, cur_token.type, self.brace_level)
                self.tok_handlers[cur_token.type](self, cur_token)
                if self.state == TypedefState.END:
                    break
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        
        if not len(self.tds):
            raise Exception(f"No typedefs were created.")
        return self.tds


class MidlInterfaceParser():
    """Responsible for parsing an interface definiton.

        Mostly, this class delegates to other classes to handle parsing
    """

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.interface = MidlInterface()
        self.state = InterfaceState.BEGIN
        self.brace_level = 0
        self.tok_handlers = {
            TokenType.KEYWORD : MidlInterfaceParser.handle_keyword,
            TokenType.STRING : MidlInterfaceParser.handle_string,
            TokenType.SQBRACKET : MidlInterfaceParser.handle_sqbracket,
            TokenType.RBRACKET : MidlInterfaceParser.handle_rbracket,
            TokenType.BRACE : MidlInterfaceParser.handle_brace,
            TokenType.COMMENT: MidlInterfaceParser.handle_comment,
            TokenType.SYMBOL: MidlInterfaceParser.handle_symbol,
            TokenType.DIRECTIVE: MidlInterfaceParser.handle_directive,
        }

    def handle_sqbracket(self, token):
        """ Handle attributes (interface or procedure)
        """
        if token.data == "[":
            if self.state == InterfaceState.BEGIN:
                self.interface.attributes = MidlAttributesParser(self.tokens).parse(token)
                self.state = InterfaceState.BODY
            elif self.state == InterfaceState.BODY:
                # Procedure declaration attributes
                proc = MidlProcedureParser(self.tokens).parse(token)
                if proc:
                    self.interface.add_procedure(proc)
            else:
                raise Exception(f"Unexpected sqbracket in state {self.state}")
        else: 
            raise Exception(f"Unexpected '{token.data}' in state {self.state}")

    def handle_rbracket(self, token):
        """ Round brackets are only valid in CPP_QUOTES """
        if token.data == '(' and self.state == InterfaceState.CPP_QUOTE:
            self.state = InterfaceState.CPP_QUOTE_STRING
        elif token.data == ')' and self.state == InterfaceState.CPP_QUOTE_END:
            self.state = InterfaceState.BODY
        else:
            raise Exception(f"Unexpected '{token.data}' in state {self.state}")    
        
    def handle_comment(self, token):
        self.interface.add_comment(token)
        
    def handle_keyword(self,token):
        """Parses keywords [uuid, version, pointer_default,interface, error_status_t, typedef, cpp_quote]
        """
        if token.data == "interface" and self.state == InterfaceState.BODY:
            tok = next(self.tokens)
            assert(tok.type == TokenType.SYMBOL)
            self.interface.name = tok.data
        elif token.data == "typedef" and self.state == InterfaceState.BODY:
            # spin up a TypeDef parser to parse out typedefs
            tds = MidlTypedefParser(self.tokens).parse(token)
            for td in tds:
                self.interface.add_typedef(td)
        elif self.state == InterfaceState.BODY:
            if token.data == "cpp_quote":
                self.state = InterfaceState.CPP_QUOTE
            else:
                # Treat it as the return type of a procedure?
                proc = MidlProcedureParser(self.tokens).parse(token)
                if proc:
                    self.interface.procedures.append(proc)
        else:
            raise Exception(f"Unhandled keyword: {token.data} in state InterfaceState: {self.state}")

    def handle_string(self, token):
        if self.state == InterfaceState.CPP_QUOTE_STRING:
            self.interface.cpp_quotes.append(token.data)
            self.state = InterfaceState.CPP_QUOTE_END
        else:
            raise Exception("Unexpected string")
    
    def handle_brace(self,token):
        """Sets the brace level appropriately
        """
        if token.data == "{":
            self.brace_level +=1
        elif token.data =="}":
            assert(self.brace_level > 0), "Something went terribly wrong, you ended up with a brace imbalance!"
            self.brace_level -= 1

    def handle_symbol(self, token):
        if self.state == InterfaceState.BODY:
            # Procedure declaration return type
            proc = MidlProcedureParser(self.tokens).parse(token)
            if proc:
                self.interface.add_procedure(proc)

    def handle_directive(self, token):
        # We keep #defines to be handled like cpp_quotes later on
        if token.data.startswith("#define"):
            self.interface.defines.append(token.data)

    def parse(self, cur_tok) -> MidlInterface:
        """Parsing loop
        """
        cur_token = cur_tok
        while cur_token is not None:
            try:
                #print(cur_token.data, cur_token.type, self.brace_level)
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens, None)
            except Exception:
                print("Interface parsing failed.")
                traceback.print_exc()
                exit()
                # return self.interface
        return self.interface