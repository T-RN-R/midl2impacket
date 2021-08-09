import traceback
from midl import MidlAttribute, MidlDefinition, MidlInterface, MidlSimpleTypedef, MidlStructDef, MidlTypeDef, MidlUnionDef, MidlVarDef, MidlEnumDef, MidlProcedure, MidlParameter
from .state import ArrayState, AttributeState, EnumState, InterfaceState, ProcedureState, State, StructState, TypedefState, UnionState
from . import midltokenizer as mt

"""This file contains a series of classes that are responsible for parsing discrete parts of a MIDL file.

    MidlParser
    MidlVarDefParser
    MidlTypeDefParse
    MidlInterfaceParser
    TODO: MidlProcedureParser

""" 

class MidlParser():
    """Parses a complete MIDL file into a MidlDefiniton object

        This class maintains a state machine.
    """
    def handle_instantiation(self, const = False):
        """Handles instantiation statements.
        """
        #TODO this function should be split off into its own class.
        # next(self.tokens) should only ever be invoked from a `parse()` function.
        tok = next(self.tokens)
        if tok.data == "int":
            name = next(self.tokens)
            if name.type != mt.Token.SYMBOL:
                raise Exception(f"Expecting SYMBOL, got {name.type}")
            eq = next(self.tokens)
            if eq.data != "=":
                raise Exception(f"Expecting EQUALS, got {eq.data}")
            rhs = ""
            rhs_tok = next(self.tokens)
            while rhs_tok.type != mt.Token.SEMICOLON:
                rhs += " "
                rhs += rhs_tok.data
                rhs_tok = next(self.tokens)
            self.definition.add_instantiation(tok.data, name.data, rhs, const)
            self.state = State.DEFAULT
                
    def handle_keyword(self,token):
        """Handles encountered keywords
        """
        # Only 2 keywords should ever be encountered here: [const, import]
        if token.data == "import":
            self.state = State.IMPORT
        elif token.data == "const":
            self.state = State.DEFINTION
            self.handle_instantiation(const=True)
        else:
            raise Exception(f"Unhandled keyword: {token.data}")

    def handle_string(self,token):
        """Encountered a string. Should only ever be imports encountered here.
        """
        if self.state == State.IMPORT:
            # Encountered an import statement so add it to the definiton's imports
            assert(token.type == mt.Token.STRING), f"Unexpected token in import definition: {token.data}"
            self.definition.add_import(token.data)
            # Reset the state
            self.state = State.DEFAULT
        else:
            # If a string is encountered outside of the import statements, raise an exception
            # TODO This may not necessarily be true, there can be variable instantiations that are strings!
            raise Exception(f"Unhandled state : {self.state}")

    def handle_sqbracket(self, token):
        """Encountered a square bracket. Only opening brackets are handled here.
        """
        if token.data == "[":
            if self.state == State.DEFAULT:
                # we hit the start of an interface definition, specifically the header, spin up a parser
                interface = MidlInterfaceParser(self.tokens).parse(token)
                self.definition.add_interface(interface)
            else:
                # Somehow we ended up in an invalid state when encountering an opening square bracket
                raise Exception(f"Invalid State for `{token.data}` in MidlParser")
        else:
            # Note that the closing square bracket is handled within the MidlInterfaceParser
            raise Exception(f"Invalid token data `{token.data}` for token type")


    def handle_comment(self, token):
        """Record the comment
        """
        self.definition.add_comment(token)
        return
            

    def handle_semicolon(self,token):
        """A semicolon was encountered, so reset the parsing state.
        """
        self.state = State.DEFAULT

    def __init__(self):
        self.state = State.DEFAULT # Current state of the parsing
        self.definition = MidlDefinition() # data to be returned by calling parse()
        self.tok_handlers = { # Jump table to handle different token types
            mt.Token.KEYWORD : MidlParser.handle_keyword,
            mt.Token.STRING : MidlParser.handle_string,
            mt.Token.SQBRACKET : MidlParser.handle_sqbracket,
            mt.Token.SEMICOLON : MidlParser.handle_semicolon,
            mt.Token.COMMENT : MidlParser.handle_comment,
        }
        self.sqbracket_lvl  = 0 # Maintains the embedding level of square brackets `[]`
        self.tokens = None # The generator that yields tokens to parse

    def parse(self, data:str ) -> MidlDefinition:
        """Parsing loop that iterates over tokens and invokes their handler function.
             If an unhandled token does not have a registered handler, an out of bounds access will occur in the tok_handlers dict.
             Note that this should never happen with a well formed test case (unless something hasn't been considered.)

        Args:
            data (str): [description]

        Returns:
            MidlDefinition: [description]
        """
        tokenizer = mt.MidlTokenizer(data)
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
            mt.Token.KEYWORD : MidlUnionParser.handle_keyword,
            mt.Token.SQBRACKET : MidlUnionParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlUnionParser.handle_symbol,
            mt.Token.SEMICOLON : MidlUnionParser.handle_semicolon,
            mt.Token.BRACE : MidlUnionParser.handle_brace,
            mt.Token.OPERATOR : MidlUnionParser.handle_operator,
            mt.Token.COMMENT: MidlUnionParser.handle_comment,
        }
    
    def add_current_member(self):
        """Add the currently tracked member to the union
        """
        member_name = self.cur_member_parts[-1]
        member_type = ' '.join(self.cur_member_parts[:-1])
        member_attrs = self.cur_member_attrs[:]
        member_def = MidlVarDef(member_type, member_name, member_attrs)
        self.members.append(member_def)
        self.prev_member = member_def
        self.cur_member_parts = []
        self.cur_member_attrs = []

    def handle_keyword(self, token):
        if self.state == UnionState.BEGIN:
            if token.data != 'union':
                raise Exception(f"Unexpected token: {token.data}. Expected 'union'")
            self.state = UnionState.UNION_BODY
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_TYPE_OR_ATTR]:
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
            if self.cur_member_attrs[0].name != 'case':
                self.state == UnionState.MEMBER_TYPE
        elif self.state in [UnionState.MEMBER_TYPE, UnionState.MEMBER_ARRAY]:
            # The member has (possibly additional?) array dimensions specified..
            array_parser = MidlArrayParser(self.tokens)
            self.cur_member_array_info.append(array_parser.parse(token))
            self.state = UnionState.MEMBER_ARRAY
        else:
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_brace(self, token):
        if token.data == '{' and self.state in [UnionState.UNION_BODY, UnionState.UNION_NAME]:
            self.state = UnionState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == UnionState.MEMBER_TYPE_OR_ATTR:
            self.state = UnionState.UNION_END
        else:
            raise Exception(f"Illegal brace in state {self.state}")

    def handle_semicolon(self, _):
        # End of variable definition, add the current type
        if self.state in [UnionState.MEMBER_TYPE]:
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
        self.state = StructState.BEGIN
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlStructParser.handle_keyword,
            mt.Token.SQBRACKET : MidlStructParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlStructParser.handle_symbol,
            mt.Token.COMMA : MidlStructParser.handle_comma,
            mt.Token.SEMICOLON : MidlStructParser.handle_semicolon,
            mt.Token.BRACE : MidlStructParser.handle_brace,
            mt.Token.OPERATOR : MidlStructParser.handle_operator,
            mt.Token.COMMENT: MidlStructParser.handle_comment,
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
            member_attrs = self.prev_member.attrs[:]
        else:
            member_name = self.cur_member_parts[-1]
            member_type = ' '.join(self.cur_member_parts[:-1])
            member_attrs = self.cur_member_attrs[:]
        
        member_def = MidlVarDef(member_type, member_name, member_attrs)
        self.members.append(member_def)
        self.prev_member = member_def
        self.cur_member_parts = []
        self.cur_member_attrs = []

    def handle_keyword(self, token):
        if self.state == StructState.BEGIN:
            if token.data != 'struct':
                raise Exception(f"Unexpected keyword {token.data}. Struct definition should start with 'struct'")
            self.state = StructState.STRUCT_NAME
        elif self.state in [StructState.MEMBER_TYPE_OR_ATTR, StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
            # Embedded
            if token.data == 'struct':
                pass
            elif token.data == 'union':
                union_type = MidlUnionParser(self.tokens).parse(token)
                if not union_type.public_names:
                    union_type.public_names.append('anonymous')
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
            array_parser = MidlArrayParser(self.tokens)
            self.cur_member_array_info.append(array_parser.parse(token))
            self.state = StructState.MEMBER_ARRAY
        else:
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_brace(self, token):
        if token.data == '{' and self.state == StructState.STRUCT_BODY:
            self.state = StructState.MEMBER_TYPE_OR_ATTR
        elif token.data == '}' and self.state == StructState.MEMBER_TYPE_OR_ATTR:
            self.state = StructState.STRUCT_END
        else:
            raise Exception(f"Illegal brace in state {self.state}")
        
    def handle_semicolon(self, _):
        # End of variable definition, add the current type
        if self.state in [StructState.MEMBER_TYPE, StructState.MEMBER_REPEAT]:
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
        self.attributes = []
        self.state = AttributeState.BEGIN
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlAttributesParser.handle_keyword,
            mt.Token.RBRACKET: MidlAttributesParser.handle_rbracket,
            mt.Token.SQBRACKET: MidlAttributesParser.handle_sqbracket,
            mt.Token.COMMA: MidlAttributesParser.handle_comma,
            mt.Token.SYMBOL: MidlAttributesParser.handle_symbol_and_numeric,
            mt.Token.NUMERIC: MidlAttributesParser.handle_symbol_and_numeric,
            mt.Token.OPERATOR: MidlAttributesParser.handle_operator,
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
        else:
            raise Exception(f"Unexpected square bracket in attribute state {self.state}")

    def handle_symbol_and_numeric(self, token):            
        if self.state != AttributeState.PARAMETERS:
            raise Exception(f"Unexpected symbol {token.data}. Expected an attribute keyword.")
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
        elif self.state == AttributeState.DEFAULT:
            # End of an attribute - make sure we parsed one
            if not self.cur_attr:
                raise Exception("Empty attribute name")
            self.attributes.append(MidlAttribute(self.cur_attr, self.cur_attr_params))
            self.cur_attr = None
            self.cur_attr_params = []
        else:
            raise Exception(f"Unexpected comma in state {self.state}")

    def handle_keyword(self, token):
        if self.cur_attr:
            raise Exception("Unexpected keyword within an attribute declaration")
        self.cur_attr = token.data

    def parse(self, cur_token) -> list[MidlAttribute]:
        while cur_token is not None:
            try:
                if cur_token.data == "]":
                    # We're done, make sure the last attribute was parsed correctly
                    if not self.cur_attr:
                        raise Exception("Missing last attribute")
                    self.attributes.append(MidlAttribute(self.cur_attr, self.cur_attr_params))
                    break
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()
        if len(self.attributes) == 0 :
            raise Exception("Parsing attributes failed")
        return self.attributes

class MidlArrayParser():
    """Array dimensionality parser
    https://docs.microsoft.com/en-us/windows/win32/midl/midl-arrays
    """
    def __init__(self, token_generator):
        self.tokens = token_generator
        self.state = ArrayState.BEGIN
        self.dimensions = (-1, -1) # min, max
        self.cur_dim = ''
        self.tok_handlers = {
            mt.Token.SQBRACKET: MidlArrayParser.handle_sqbracket,
            mt.Token.NUMERIC : MidlArrayParser.handle_numeric,
            mt.Token.OPERATOR : MidlArrayParser.handle_operator,
            mt.Token.ELLIPSIS : MidlArrayParser.handle_ellipsis,
            mt.Token.RBRACKET: MidlArrayParser.handle_rbracket,
        }

    def handle_sqbracket(self, token):
        if token.data == '[':
            if self.state == ArrayState.BEGIN:
                self.state = ArrayState.RANGE_MIN
                return
        raise Exception("Unexpected bracket in array range definition")

    def handle_numeric(self, token):
        if self.state == ArrayState.RANGE_MIN:
            self.dimensions[0] = token.data
            self.state = ArrayState.RANGE_ELLIPSIS
        elif self.state == ArrayState.RANGE_MAX:
            self.dimensions[1] = token.data
            self.state = ArrayState.END
        else:
            raise Exception("Unexpected number in array definition")
    
    def handle_operator(self,token):
        if token.data != '*':
            raise Exception("Unexpected operator in array definition")
        if self.state == ArrayState.RANGE_MIN:
            self.dimensions[0] = -1
            self.state = ArrayState.RANGE_ELLIPSIS
        elif self.state == ArrayState.RANGE_MAX:
            self.dimensions[1] = -1
            self.state = ArrayState.END
        else:
            raise Exception("Unexpected '*' parameter in array definition")

    def handle_ellipsis(self, _):
        if self.state != ArrayState.RANGE_ELLIPSIS:
            raise Exception("Unexpected ellipsis in array definition")
        self.state = ArrayState.RANGE_MAX

    def handle_rbracket(self, token):
        if token.data == '(':
            self.rbracket_level += 1
        elif token.data == ')' and self.rbracket_level >= 1:
            self.rbracket_level -= 1
        else:
            raise Exception("Unexpected closing bracket in array definition")

        # If we're at zero, the current dimension is done
        if self.rbracket_level == 0:
            if self.state == ArrayState.RANGE_MIN:
                self.dimensions[0] = self.cur_dim
                self.cur_dim = ''
                self.state = ArrayState.RANGE_ELLIPSIS
            elif self.state == ArrayState.RANGE_MAX:
                self.dimensions[1] = self.cur_dim
                self.cur_dim = ''
                self.state = ArrayState.END
            else:
                raise Exception("Unexpected closing bracket in array definition")
        # Otherwise, just capture the data for the dimension string
        else:
            self.cur_dim += token.data

    def handle_symbol(self, token):
        if self.state in [ArrayState.RANGE_MIN, ArrayState.RANGE_MAX]:
            self.cur_dim += token.data
        else:
            raise Exception("Unexpected symbol in array definition")

    def parse(self, cur_token):
        """parsing loop
        """
        while cur_token is not None:
            try:
                if cur_token.data == "]" and self.state == ArrayState.RANGE:
                    return self.dimensions
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)
            except Exception:
                traceback.print_exc()
                exit()

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
            mt.Token.RBRACKET : MidlProcedureParser.handle_rbracket,
            mt.Token.SQBRACKET : MidlProcedureParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlProcedureParser.handle_symbol,
            mt.Token.KEYWORD : MidlProcedureParser.handle_keyword,
            mt.Token.COMMA : MidlProcedureParser.handle_comma,
            mt.Token.OPERATOR : MidlProcedureParser.handle_operator,
            mt.Token.COMMENT: MidlProcedureParser.handle_comment,
            mt.Token.SEMICOLON: MidlProcedureParser.handle_semicolon,
        }

    def finish_cur_param(self):
        param_name = self.cur_param_type_parts[-1]
        param_type = ' '.join(self.cur_param_type_parts[:-1])
        self.parameters.append(MidlParameter(param_name, param_type,  self.cur_param_attrs))
        self.cur_param_type_parts = []
        self.cur_param_attrs = []
        self.cur_param_array_info = []

    def handle_semicolon(self, _):
        if self.state == ProcedureState.PROC_END:
            self.state = ProcedureState.END
        else:
            raise Exception("Unexpected semicolon in procedure definition")

    def handle_keyword(self, token):
        # Parameters can be named/typed using reserved keywords
        if self.state == ProcedureState.PARAM_TYPE:
            # Add the type data
            self.cur_param_type_parts.append(token.data)
        else:
            raise Exception(f"Unexpected keyword in state {self.state}")

    def handle_rbracket(self, token):
        if token.data == '(' and self.state == ProcedureState.PROC_TYPE:
            # We can now set our name and type
            self.name = self.type_parts[-1]
            self.type = ' '.join(self.type_parts[:-1])
            self.state = ProcedureState.PARAM_ATTRS
        elif token.data == ')' and self.state in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            self.finish_cur_param()
            self.state = ProcedureState.PROC_END
        else:
            raise Exception(f"Unexpected rbracket in state {self.state}")

    def handle_symbol(self, token):
        if self.state in [ProcedureState.PROC_TYPE, ProcedureState.PROC_TYPE_OR_ATTRS]:
            self.type_parts.append(token.data)
            self.state = ProcedureState.PROC_TYPE
        elif self.state == ProcedureState.PARAM_TYPE:
            self.cur_param_type_parts.append(token.data)
        else:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")

    def handle_comma(self, _):
        if self.state not in [ProcedureState.PARAM_TYPE, ProcedureState.PARAM_ARRAY]:
            raise Exception(f"Unexpected comma in state {self.state}")
        # Add the parameter to the list
        self.finish_cur_param()
        self.state = ProcedureState.PARAM_ATTRS
    
    def handle_sqbracket(self, token):
        if self.state == ProcedureState.PROC_TYPE_OR_ATTRS:
            if token.data == "[":
                self.attrs = MidlAttributesParser(self.tokens).parse(token)
                self.state = ProcedureState.PROC_TYPE
            else:
                raise Exception("Unexpected bracket in procedure declaration")
        elif self.state == ProcedureState.PARAM_ATTRS:
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
            mt.Token.BRACE : MidlEnumParser.handle_brace,
            mt.Token.SYMBOL : MidlEnumParser.handle_symbol,
            mt.Token.KEYWORD : MidlEnumParser.handle_keyword,
            mt.Token.COMMA : MidlEnumParser.handle_comma,
            mt.Token.OPERATOR : MidlEnumParser.handle_operator,
            mt.Token.COMMENT: MidlEnumParser.handle_comment,
            mt.Token.SEMICOLON: MidlEnumParser.handle_semicolon,
            mt.Token.NUMERIC: MidlEnumParser.handle_numeric,
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
        if token.data == '{' and self.state == EnumState.BODY:
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
        self.td = None
        self.tok_handlers = {
            mt.Token.SYMBOL: MidlTypedefParser.handle_symbol,
            mt.Token.KEYWORD : MidlTypedefParser.handle_keyword,
            mt.Token.SQBRACKET: MidlTypedefParser.handle_sqbracket,
            mt.Token.SEMICOLON: MidlTypedefParser.handle_semicolon,
        }
        self.kw_handlers = {
            'struct': MidlStructParser,
            'enum': MidlEnumParser,
        }

    def handle_context_handle(self,token):
        """Handles the simple case of a context_handle definition.
        TODO: verify if its valid MIDL to have a non-context_handle simple typedef
        """
        tok_closing_sqbracket = next(self.tokens)
        if tok_closing_sqbracket.data != "]":
            raise Exception(f"Malformed typedef, expecting closing `]`, got {tok_closing_sqbracket.data}")
        tok_type = next(self.tokens)
        tok_name = next(self.tokens)
        self.td = MidlTypeDef(tok_type.data, tok_name.data, is_context_handle=True)

    def handle_brace(self, token):
        if token.data =="}":
            assert(self.brace_level > 0)
            self.brace_level -= 1
        elif token.data == "{":
            self.brace_level += 1
        else:
            #should never happen because of the tokenizer, but just in case...
            raise Exception("Illegal Brace")

    def handle_keyword(self, token):
        """Handles the various kinds of typedefs
            TODO: handle unions
        """
        if self.state == TypedefState.BEGIN and token.data == 'typedef':
            self.state = TypedefState.TYPE_OR_ATTRS
        elif self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            self.state = TypedefState.DEFINITION
            self.td = self.kw_handlers[token.data](self.tokens).parse(token)
            self.state = TypedefState.END
        else:
            raise Exception(f"Unexpected keyword {token.data} in state {self.state}")
        
        # if token.data == "context_handle":
        #     self.handle_context_handle(token)
        # elif token.data == "struct":
        #     self.handle_struct_def(token)
        # elif token.data == "enum":
        #     self.handle_enum_def(token)

    def handle_symbol(self, token):
        if self.state in [TypedefState.TYPE_OR_ATTRS, TypedefState.TYPE]:
            self.state = TypedefState.DEFINITION
        if self.state == TypedefState.DEFINITION:
            self.td_parts.append(token.data) 
        else:
            raise Exception(f"Unexpected symbol {token.data} in state {self.state}")


    def handle_comment(self, token):
        self.comments.append(token)

    def no_op(self, _):
        pass

    def handle_sqbracket(self, token):
        """ Handles typedef attributes e.g. [v1_enum]
        """
        if self.state == TypedefState.TYPE_OR_ATTRS:
            self.attrs = MidlAttributesParser(self.tokens).parse(token)
            self.state = TypedefState.TYPE
        else:
            raise Exception(f"Unexpected sqbracket in state {self.state}")

    def handle_semicolon(self, _):
        if self.state in [TypedefState.DEFINITION]:
            # We're done. If it was a simple type we need to create it here
            if not self.td:
                td_name = self.td_parts[-1]
                td_type = ' '.join(self.td_parts[:-1])
                simple_type = MidlSimpleTypedef(td_name, td_type)
                self.td = MidlTypeDef(simple_type, self.attrs)
            self.state = TypedefState.END
        else:
            raise Exception("Unexpected semicolon in type definition")



    def parse(self, cur_token) -> MidlTypeDef:
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
        
        # There are 2 types of definitions that can be parsed here, either an enum, or a typdef.
        # poorly written way of handling these cases below.
        if self.td is None:
            if self.enums is not None:
                self.td = MidlEnumDef(self.public_name, self.enums)
            else:
                self.td = MidlTypeDef(self.vds, self.public_name, is_complex=True)
                self.td.private_name = self.private_name
        return self.td


class MidlInterfaceParser():
    """Responsible for parsing an interface definiton.

        Mostly, this class delegates to other classes to handle parsing
    """
    def handle_sqbracket(self, token):
        """Detected the beginning of an interface header, set the current state appropriately
        """
        if token.data == "[":
            if self.state == InterfaceState.BEGIN:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.BODY:
                # Procedure declaration attributes
                proc = MidlProcedureParser(self.tokens).parse(token)
                if proc:
                    self.interface.add_procedure(proc)
            else:
                raise Exception("Unexpected sqbracket")

        elif token.data == "]" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.BODY
        else: 
            raise Exception("Unexpected token")

    def handle_rbracket(self,token):
        """Round brackets detected

            Sets the appropriate header variable, or reverts the state.
        """
        if token.data == "(":
            if self.state == InterfaceState.UUID:
                tok = next(self.tokens)
                self.interface.uuid = tok.data
            elif self.state == InterfaceState.VERSION:
                tok = next(self.tokens)
                self.interface.version = tok.data
            elif self.state == InterfaceState.POINTER_DEFAULT:
                tok = next(self.tokens)
                self.interface.pointer_default = tok.data
            elif self.state == InterfaceState.CPP_QUOTE:
                #tok = next(self.tokens)
                pass
                #TODO handle cpp_quote, not really urgent and super hard to convert to Python
            else:
                raise Exception("Illegal state transition")
        elif token.data == ")":
            if self.state == InterfaceState.UUID:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.VERSION:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.POINTER_DEFAULT:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.CPP_QUOTE:
                self.state = InterfaceState.BODY
            else:
                raise Exception("Illegal state transition")

    def handle_comment(self, token):
        self.interface.add_comment(token)
        
    def handle_keyword(self,token):
        """Parses keywords [uuid, version, pointer_default,interface, error_status_t, typedef, cpp_quote]
        """
        if token.data == "uuid" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.UUID
        elif token.data == "version" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.VERSION
        elif token.data == "pointer_default" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.POINTER_DEFAULT
        elif token.data == "interface" and self.state == InterfaceState.BODY:
            tok = next(self.tokens)
            assert(tok.type == mt.Token.SYMBOL)
            self.interface.name = tok.data
        elif token.data == "typedef" and self.state == InterfaceState.BODY:
            # spin up a TypeDef parser to parse out typedefs
            td = MidlTypedefParser(self.tokens).parse(token)
            self.interface.add_typedef(td)
        elif token.data == "cpp_quote":
            self.state = InterfaceState.CPP_QUOTE
        else:
            raise Exception(f"Unhandled keyword: {token.data} in state InterfaceState: {self.state}")

    def handle_comma(self, token):
        """no-op to handle encountered commas
        """
        pass

    def handle_string(self, token):
        if self.state == InterfaceState.CPP_QUOTE:
            #TODO handle CPP_QUOTE
            # no-op for now
            return
        else:
            raise Exception("Unexpected string")
    
    def handle_brace(self,token):
        """Sets the brace level appropriately
        """
        if token.data == "{":
            self.brace_level +=1
        elif token.data =="}":
            assert(self.brace_level >0), "Something went terribly wrong, you ended up with a brace imbalance!"
            self.brace_level -=1

    def handle_symbol(self, token):
        if self.state == InterfaceState.BODY:
            # Procedure declaration return type
            proc = MidlProcedureParser(self.tokens).parse(token)
            if proc:
                self.interface.add_procedure(proc)

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.interface = MidlInterface()
        self.state = InterfaceState.BEGIN
        self.brace_level = 0
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlInterfaceParser.handle_keyword,
            mt.Token.STRING : MidlInterfaceParser.handle_string,
            mt.Token.SQBRACKET : MidlInterfaceParser.handle_sqbracket,
            mt.Token.RBRACKET : MidlInterfaceParser.handle_rbracket,
            mt.Token.COMMA : MidlInterfaceParser.handle_comma,
            mt.Token.BRACE : MidlInterfaceParser.handle_brace,
            mt.Token.COMMENT: MidlInterfaceParser.handle_comment,
            mt.Token.SYMBOL: MidlInterfaceParser.handle_symbol,
        }

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