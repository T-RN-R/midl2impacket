import enum

class MidlState(enum.Enum):
    """Class used to handle state transitions for top level MidlParser
    """
    DEFAULT = enum.auto()
    IMPORT = enum.auto()
    IMPORT_COMPLETE = enum.auto()
    DEFINITION = enum.auto()
    OPEN_SQBRACKET = enum.auto()
    CLOSE_SQBRACKET= enum.auto()
    COMMENT = enum.auto()

class InterfaceState(enum.Enum):
    """Class used to handle state transitions for MidlInterfaceParser
    """
    BEGIN = enum.auto()
    BODY = enum.auto()
    CPP_QUOTE = enum.auto()
    CPP_QUOTE_STRING = enum.auto()
    CPP_QUOTE_END = enum.auto()

class TypedefState(enum.Enum):
    """Semi-unused, handles transitions for MidlTypedefs. Currently a lot of state transitions 
    are based off of context and what the previous token was. This is a bit hacky and might break.
    """
    DEFAULT = enum.auto()
    

class ProcedureState(enum.Enum):
    PROC_TYPE_OR_ATTRS = enum.auto()
    PROC_TYPE = enum.auto()
    PARAM_TYPE_OR_ATTRS = enum.auto()
    PARAM_TYPE = enum.auto()
    PARAM_ARRAY = enum.auto()
    PARAM_DEFINED = enum.auto() # Special case when a keyword is used as the param name
    PROC_END = enum.auto()
    END = enum.auto()

class TypedefState(enum.Enum):
    BEGIN = enum.auto()
    TYPE_OR_ATTRS = enum.auto()
    TYPE = enum.auto()
    DEFINITION = enum.auto()
    END = enum.auto()

class StructState(enum.Enum):
    BEGIN = enum.auto()
    STRUCT_NAME = enum.auto()
    STRUCT_BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    MEMBER_REPEAT = enum.auto()
    MEMBER_ARRAY = enum.auto()
    STRUCT_END = enum.auto()
    END = enum.auto()

class UnionState(enum.Enum):
    BEGIN = enum.auto()
    UNION_NAME = enum.auto()
    UNION_BODY = enum.auto()
    MEMBER_TYPE_OR_ATTR = enum.auto()
    MEMBER_TYPE = enum.auto()
    MEMBER_ARRAY = enum.auto()
    UNION_END = enum.auto()
    END = enum.auto()

class EnumState(enum.Enum):
    BEGIN = enum.auto()
    NAME = enum.auto()
    BODY = enum.auto()
    MEMBER_NAME = enum.auto()
    MEMBER_OP = enum.auto()
    MEMBER_VALUE = enum.auto()
    MEMBER_COMPLETE = enum.auto()
    ENUM_END = enum.auto()
    END = enum.auto()

class AttributeState(enum.Enum):
    BEGIN = enum.auto()
    DEFAULT = enum.auto()
    PARAMETERS = enum.auto()
    END = enum.auto()

class ArrayState(enum.Enum):
    BEGIN = enum.auto()
    RANGE_MIN = enum.auto()
    RANGE_MIN_IN_PROGRESS = enum.auto()
    RANGE_MAX = enum.auto()
    RANGE_MAX_IN_PROGRESS = enum.auto()
    END = enum.auto()

class VariableInstantiationState(enum.Enum):
    TYPE = enum.auto()
    TYPE_ARRAY = enum.auto()
    VALUE = enum.auto()
    END = enum.auto()

class DirectiveState(enum.Enum):
    BEGIN = enum.auto()
    TYPE = enum.auto()
    END = enum.auto()