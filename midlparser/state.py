class State:
    """Class used to handle state transitions for top level MidlParser
    """
    DEFAULT = 0x1
    IMPORT = 0x2
    DEFINTION = 0x3
    OPEN_SQBRACKET = 0x4
    CLOSE_SQBRACKET=0x5
    COMMENT=0x6

class InterfaceState:
    """Class used to handle state transitions for MidlInterfaceParser
    """
    BEGIN = 0x0
    HEADER_START = 0x1
    UUID = 0x2
    VERSION = 0x3
    POINTER_DEFAULT = 0x4
    BODY = 0x5
    CPP_QUOTE = 0x6

class TypedefState:
    """Semi-unused, handles transitions for MidlTypedefs. Currently a lot of state transitions 
    are based off of context and what the previous token was. This is a bit hacky and might break.
    """
    DEFAULT = 0x00
    

class ProcedureState:
    PROC_TYPE_OR_ATTRS = 0x1
    PROC_TYPE = 0x2
    PARAM_ATTRS = 0x3
    PARAM_TYPE = 0x4
    PARAM_ARRAY = 0x5
    PARAM_DEFINED = 0x6 # Special case when a keyword is used as the param name
    PROC_END = 0x7
    END = 0x8

class TypedefState:
    BEGIN = 0x0
    TYPE_OR_ATTRS = 0x1
    TYPE = 0x2
    DEFINITION = 0x3
    END = 0x5

class StructState:
    BEGIN = 0x0
    STRUCT_NAME = 0x1
    STRUCT_BODY = 0x2
    MEMBER_TYPE_OR_ATTR = 0x3
    MEMBER_TYPE = 0x4
    MEMBER_REPEAT = 0x5
    MEMBER_ARRAY = 0x6
    STRUCT_END = 0x7
    END = 0x8

class UnionState:
    BEGIN = 0x0
    UNION_NAME = 0x1
    UNION_BODY = 0x2
    MEMBER_TYPE_OR_ATTR = 0x3
    MEMBER_TYPE = 0x4
    MEMBER_ARRAY = 0x5
    UNION_END = 0x6
    END = 0x7

class EnumState:
    BEGIN = 0x0
    NAME = 0x1
    BODY = 0x2
    MEMBER_NAME = 0x3
    MEMBER_OP = 0x4
    MEMBER_VALUE = 0x5
    MEMBER_COMPLETE = 0x6
    ENUM_END = 0x7
    END = 0x8

class AttributeState:
    BEGIN = 0x0
    DEFAULT = 0x1
    PARAMETERS = 0x2

class ArrayState:
    BEGIN = 0x0
    RANGE_MIN = 0x1
    RANGE_ELLIPSIS = 0x2
    RANGE_MAX = 0x3
    END = 0x4