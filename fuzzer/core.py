from fuzzer.base import FuzzableMidl
from fuzzer.midl import In, Out, InOut


class Interface(FuzzableMidl):
    def __init__(self, uuid, version, methods):
        """Rpc Interface class"""
        self.uuid = uuid
        self.version = version
        self.methods = methods

class Procedure(FuzzableMidl):
    """A class whose instances represent Midl procudure invocation generator defintion"""

    def __init__(self,name, *parameters, **kwargs):
        self.name = name
        self.arguments = parameters

    def get_resp_str(self):
        return f"{self.name}Response"