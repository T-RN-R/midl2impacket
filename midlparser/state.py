class State:
    DEFAULT = 0x1
    IMPORT = 0x2
    DEFINTION = 0x3
    OPEN_SQBRACKET = 0x4
    CLOSE_SQBRACKET=0x5

class InterfaceState:
    DEFAULT = 0x0
    HEADER_START = 0x1
    UUID = 0x3
    VERSION = 0x4
    POINTER_DEFAULT = 0x5
    CPP_QUOTE = 0x6

class TypedefState:
    DEFAULT = 0x00
    
