

class DataTypeLookup:
    """Maintains a dictionary of all RPC objects created during the execution of a given testcase.
    
    This allows passing output datatypes into input fields.
    TBD: Figure out a way to map aliased types. ie. typeddef-ed context_handles"""
    def __init__(self):
        self.map = {}

    def insert(self, datatype, data):
        if datatype in self.map:
            self.map[datatype].extend([data])
        else:
            self.map[datatype] = [data]

    def get(self, datatype):
        return self.map[datatype] if datatype in self.map else []
        