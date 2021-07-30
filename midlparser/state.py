class State:
    """Class used to handle state transitions for top level MidlParser
    """
    DEFAULT = 0x1
    IMPORT = 0x2
    DEFINTION = 0x3
    OPEN_SQBRACKET = 0x4
    CLOSE_SQBRACKET=0x5

class InterfaceState:
    """Class used to handle state transitions for MidlInterfaceParser
    """
    DEFAULT = 0x0
    HEADER_START = 0x1
    UUID = 0x3
    VERSION = 0x4
    POINTER_DEFAULT = 0x5
    CPP_QUOTE = 0x6

class TypedefState:
    """Semi-unused, handles transitions for MidlTypedefs. Currently a lot of state transitions 
    are based off of context and what the previous token was. This is a bit hacky and might break.
    """
    DEFAULT = 0x00
    
