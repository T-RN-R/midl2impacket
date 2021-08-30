class DataTypeLookup:
    """Maintains a dictionary of all RPC objects created during the execution of a given testcase.

    This allows passing output datatypes into input fields.
    TBD: Figure out a way to map aliased types. ie. typeddef-ed context_handles"""

    def __init__(self):
        # mapping of datatype : [generated data]
        self.map = {}
        # mapping of type : [aliased types]
        self.alias_map = {}

    def insert(self, datatype, data):
        if datatype in self.map:
            self.map[datatype].extend([data])
        else:
            self.map[datatype] = [data]

    def get(self, datatype):
        return self.map[datatype] if datatype in self.map else []

    def get_valid_aliases(self, datatype):
        aliases = set()
        # TODO this does not include cases where there are multiple levels of typedef indirection.
        for item in self.alias_map:
            entry = self.alias_map[item]
            if datatype in entry:
                aliases.add(*entry)
                aliases.add(item)
        return aliases
