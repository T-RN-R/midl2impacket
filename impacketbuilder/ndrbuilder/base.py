from impacketbuilder.base import Writable, Writer
from abc import ABC, abstractmethod

"""This module contains base classes for ndrbuilder operations"""


class PythonTypingException(Exception):
    """Exception thrown when the ndrbuilder encounters a mistyped PythonDef"""

    pass


class PythonDef(Writable, ABC):
    """Root class that all Python language constructs share"""

    @abstractmethod
    def to_python_string(self, tab_level=0) -> str:
        pass

    def __str__(self) -> str:
        return self.to_python_string()


class PythonDefList(PythonDef):
    """Base class for lists of PythonDef objects

    This class exists to help with the construction and printing of various PythonDef types"""

    CONTAINED_CLASS = None  # The buddy class that the imlementing child class represents within the list

    def __init__(self, *args):
        assert self.CONTAINED_CLASS != None  # enforce the setting of CONTAINED_CLASS
        for arg in args:
            if not isinstance(arg, self.CONTAINED_CLASS):
                # Make sure all entries are the appropriate type
                raise PythonTypingException(
                    f"{self.__class__} expects type {self.CONTAINED_CLASS}, got {type(arg)}"
                )
        self.obj_list = list(args)


class PythonValue(PythonDef):
    """Base class that represents anything on the rhs of an assignment"""

    def __init__(self, value: str):
        self.value = value

    def to_python_string(self, tab_level=0) -> str:
        return self.value
