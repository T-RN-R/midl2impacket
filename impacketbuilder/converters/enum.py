from midl import MidlEnumDef
from .base import Converter

class MidlEnumConverter(Converter):
    def convert(self, e : MidlEnumDef) -> str:
        for k in e.map.keys():
            self.write(f"{k} = {e.map[k]}")