from base import Visitor


class Preprocessor(Visitor):
    def preprocess(self):
        raise Exception(f"Class {__class__} must implement `preprocess()`")