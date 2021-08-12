import nose
from nose.tools import with_setup

from midlparser.tokenizer import *

Tokenizer = MidlTokenizer


class test_Tokenizer:

    def test_imports(self):
        t = Tokenizer('import "test.idl"').get_token()
        tok = next(t)
        assert tok.data == "import"
        assert tok.type == TokenType.KEYWORD

        tok = next(t)
        assert tok.data == '"test.idl"'
        assert tok.type == TokenType.STRING

