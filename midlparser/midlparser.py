import traceback
from midl import MidlDefinition, MidlInterface, MidlTypeDef, MidlVarDef
from .state import InterfaceState, State
import string
from . import midltokenizer as mt


class MidlParser():
    def handle_definition(self, const = False):
            tok = next(self.tokens)
            if tok.data == "int":
                name = next(self.tokens)
                if name.type != mt.Token.SYMBOL:
                    raise Exception(f"Expecting SYMBOL, got {name.type}")
                eq = next(self.tokens)
                if eq.data != "=":
                    raise Exception(f"Expecting equals, got {eq.data}")
                rhs = ""
                rhs_tok = next(self.tokens)
                while rhs_tok.type != mt.Token.SEMICOLON:
                    rhs += rhs_tok.data
                    rhs_tok = next(self.tokens)
                self.definition.add_definition(tok.data, name.data, rhs, const)
                self.state=State.DEFAULT
                
                
    def handle_keyword(self,token):
        if token.data == "import":
            self.state = State.IMPORT
        elif token.data == "const":
            self.state = State.DEFINTION
            self.handle_definition(const=True)
        elif token.data == "uuid":
            assert(self.state == State.OPEN_SQBRACKET)
            self.state = State.UUID
        else:
            raise Exception(f"Unhandled keyword: {token.data}")

    def handle_string(self,token):
        if self.state == State.IMPORT:
            self.definition.add_import(token.data)
            self.state = State.DEFAULT
        else:
            raise Exception(f"Unhandled state : {self.state}")

    def handle_sqbracket(self, token):
        if token.data == "[":
            if self.state == State.DEFAULT:
                # we hit the start of an interface definition, spin up a parser
                interface = MidlInterfaceParser(self.tokens).parse(token)
                self.definition.add_interface(interface)
            else:
                raise Exception(f"Invalid State for `{token.data}` in MidlParser")
        else:
            raise Exception(f"Invalid token data `{token.data}`for token type")

    def handle_rbracket(self, token):
        if token.data == "(":
            if self.state == State.UUID:
                tok = next(self.tokens)
                print(tok.data)
        elif token.data == ")":
            assert(self.sqbracket_lvl >0)
            self.state = State.CLOSE_SQBRACKET
            self.sqbracket_lvl-=1
        else:
            raise Exception(f"Invalid token data `{token.data}`for token type")

    def __init__(self):
        self.state = State.DEFAULT
        self.definition = MidlDefinition()
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlParser.handle_keyword,
            mt.Token.STRING : MidlParser.handle_string,
            mt.Token.SQBRACKET : MidlParser.handle_sqbracket,
            mt.Token.RBRACKET : MidlParser.handle_rbracket,

        }
        self.sqbracket_lvl  = 0
        self.tokens = None


    def handle_state(self):
        pass

    def parse(self, data:str ) -> MidlDefinition:
        tokenizer = mt.MidlTokenizer(data)
        self.tokens = tokenizer.get_token()
        cur_token = next(self.tokens)
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                self.handle_state()
                cur_token = next(self.tokens)
            except Exception:
                print(str(self.definition))
                traceback.print_exc()
                exit()
        return self.definition
            
class MidlVarDefParser():
    def handle_keyword(self,cur_tok):
        if self.sq_bracket_level == 0:
            self.cur_type = cur_tok.data
        else:
            pass
    def handle_symbol(self,cur_tok):
        self.vds.append(MidlVarDef(self.cur_type,cur_tok.data))

    def handle_comma(self,cur_tok):
        pass

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.vds = []
        self.cur_type = None
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.sq_bracket_level = 0
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlVarDefParser.handle_keyword,
            #mt.Token.SQBRACKET : MidlVarDefParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlVarDefParser.handle_symbol,
            mt.Token.COMMA : MidlVarDefParser.handle_comma,
            #mt.Token.BRACE : MidlTypedefParser.handle_brace,
        }

    def parse(self, cur_tok) -> MidlVarDef:
        cur_token = cur_tok
        while cur_token is not None:
            try:
                if cur_token.type == mt.Token.SEMICOLON: #exit once the def is done
                    break
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)

            except Exception:
                #print(str(self.interface))
                traceback.print_exc()
                exit()
        if len(self.vds) == 0 :
            raise Exception("Parsing Typedef failed")
        return self.vds


class MidlTypedefParser():
    def handle_context_handle(self,token):
        tok_closing_sqbracket = next(self.tokens)
        if tok_closing_sqbracket.data != "]":
            raise Exception("Malformed typedef")
        tok_type = next(self.tokens)
        tok_name = next(self.tokens)
        self.td = MidlTypeDef(tok_type.data, tok_name.data, is_context_handle=True)

    def handle_var_defs(self):
        vds =  MidlVarDefParser(self.tokens).parse(next(self.tokens))
        return vds

    def handle_struct_def(self,token):
        tok_private_name = next(self.tokens)
        if tok_private_name.type != mt.Token.SYMBOL:
            raise Exception(f"Invalid struct name {tok_private_name.data}")
        else:
            self.private_name =  tok_private_name.data
        if next(self.tokens).data != "{":
            raise Exception("Expecting '{'")
        self.brace_level += 1
        var_defs = self.handle_var_defs()
        self.vds.extend( var_defs)

    def handle_brace(self, token):
        if token.data =="}":
            self.brace_level -= 1
        else:
            raise Exception("Illegal Brace")
    def handle_keyword(self,token):
        if token.data == "context_handle":
            self.handle_context_handle(token)
        elif token.data == "struct":
            self.handle_struct_def(token)
        pass
    def handle_sqbracket(self,token):
        #print(token.data)
        pass

    def handle_symbol(self,token):
        self.public_name = token.data

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.td = None
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.vds = []
        self.private_name = None
        self.public_name = None
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlTypedefParser.handle_keyword,
            #mt.Token.STRING : MidlTypedefParser.handle_string,
            mt.Token.SQBRACKET : MidlTypedefParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlTypedefParser.handle_symbol,
            #mt.Token.RBRACKET : MidlTypedefParser.handle_rbracket,
            #mt.Token.COMMA : MidlTypedefParser.handle_comma,
            mt.Token.BRACE : MidlTypedefParser.handle_brace,
        }

    def parse(self, cur_tok) -> MidlTypeDef:
        cur_token = cur_tok
        while cur_token is not None:
            try:
                if cur_token.type == mt.Token.SEMICOLON and self.brace_level == 0:
                    break
                print(cur_token.data, self.brace_level)
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)

            except Exception:
                #print(str(self.interface))
                traceback.print_exc()
                exit()

        if self.td is None:
            self.td = MidlTypeDef(self.vds, self.public_name, is_complex=True)
            self.td.private_name = self.private_name
        return self.td


class MidlInterfaceParser():
    def handle_sqbracket(self,token):
        if token.data == "[":
            self.state = InterfaceState.HEADER_START
        elif token.data =="]":
            self.state = InterfaceState.DEFAULT
        else: 
            raise Exception("Illegal token, expecting sqbracket")

    def handle_rbracket(self,token):
        if token.data == "(":
            if self.state == InterfaceState.UUID:
                tok = next(self.tokens)
                self.interface.uuid = tok.data
            elif self.state == InterfaceState.VERSION:
                tok = next(self.tokens)
                self.interface.version = tok.data
            elif self.state == InterfaceState.POINTER_DEFAULT:
                tok = next(self.tokens)
                self.interface.uuid = tok.data
            else:
                raise Exception("Illegal state transition")
        if token.data == ")":
            if self.state == InterfaceState.UUID:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.VERSION:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.POINTER_DEFAULT:
                self.state = InterfaceState.HEADER_START
            else:
                raise Exception("Illegal state transition")
            
    def handle_keyword(self,token):
        if token.data == "uuid" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.UUID
        elif token.data == "version" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.VERSION
        elif token.data == "pointer_default" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.POINTER_DEFAULT
        elif token.data == "interface" and self.state == InterfaceState.DEFAULT:
            tok = next(self.tokens)
            assert(tok.type == mt.Token.SYMBOL)
            self.interface.name = tok.data
        elif token.data == "typedef" and self.state == InterfaceState.DEFAULT:
            # spin up a TypeDef parser to parse out typedefs
            td = MidlTypedefParser(self.tokens).parse(token)
            self.interface.add_typedef(td)
        else:
            raise Exception(f"Unhandled keyword: {token.data} in state InterfaceState: {self.state}")

    def handle_comma(self, token):
        pass

    def handle_brace(self,token):
        if token.data == "{":
            self.brace_level +=1
        elif token.data =="}":
            assert(self.brace_level >0)
            self.brace_level -=1

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.interface = MidlInterface()
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlInterfaceParser.handle_keyword,
            #mt.Token.STRING : MidlInterfaceParser.handle_string,
            mt.Token.SQBRACKET : MidlInterfaceParser.handle_sqbracket,
            mt.Token.RBRACKET : MidlInterfaceParser.handle_rbracket,
            mt.Token.COMMA : MidlInterfaceParser.handle_comma,
            mt.Token.BRACE : MidlInterfaceParser.handle_brace,
        }

    def parse(self, cur_tok) -> MidlInterface:
        cur_token = cur_tok
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)
            except Exception:
                #print(str(self.interface))
                traceback.print_exc()
                exit()

        return self.interface