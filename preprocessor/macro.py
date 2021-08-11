from midl import *
from .base import Preprocessor
class MidlPreprocessor(Preprocessor):
    def preprocess(self, definition:MidlDefinition):
        # O(n*m) algo incoming
        self.obj = definition
        if len(self.obj.defines) == 0:
            return self.obj
        
        while len(self.obj.defines) > 0:
            d = self.map(self.obj.defines[0])
            self.obj.defines.pop(0)
            self.macro = d
            self.obj.accept(self)

        return self.obj


    def visit(self, visitee: Visitable):
        visitee.apply_macro(self, self.macro)

    def map(self, define:str) -> tuple:
        # TODO handle the case of multiline macros
        str_spl = define.split(" ")
        assert(len(str_spl) >=3), "Invalid macro"
        return (str_spl[1].strip()," ".join(str_spl[2:]).strip())




