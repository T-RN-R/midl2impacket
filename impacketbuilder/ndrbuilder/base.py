from impacketbuilder.base import Writable, Writer
from abc import ABC, abstractmethod


class PythonTypingException(Exception):
    pass


class PythonDef(Writable, ABC):
    @abstractmethod
    def to_python_string(self,tab_level=0) -> str:
        pass

    def __str__(self) -> str:
        return self.to_python_string()


class PythonDefList(PythonDef):
    CONTAINED_CLASS = None

    def __init__(self, *args):
        assert self.CONTAINED_CLASS != None
        for arg in args:
            if type(arg) != self.CONTAINED_CLASS:
                raise PythonTypingException(
                    f"{self.__class__} expects type {self.CONTAINED_CLASS}, got {type(arg)}"
                )
        self.obj_list = list(args)


class PythonValue(PythonDef):
    """Base class that represents anything on the rhs of an assignment

    Args:
        PythonDef ([type]): [description]
    """

    def __init__(self, value: str):
        self.value = value

    def to_python_string(self, tab_level=0) -> str:
        return self.value