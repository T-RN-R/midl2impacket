import pathlib

from midlparser.parsers.base import MidlParserException
from midlparser.parsers.midl import MidlParser
from midlparser.tokenizer import MidlTokenizer


def parse_idl(idl_file: pathlib.Path):
    data = idl_file.read_text()
    if not data:
        raise MidlParserException(f"File `{idl_file}` is empty")
    tokenizer = MidlTokenizer(data, idl_file.name)
    tokens = tokenizer.get_token()
    first_token = next(tokens)
    return MidlParser(tokens, tokenizer).parse(first_token)
