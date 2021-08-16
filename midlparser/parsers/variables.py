import enum

from midltypes import MidlVariableInstantiation
from midlparser.parsers.arrays import MidlArrayParser
from midlparser.parsers.base import MidlBaseParser
from midlparser.tokenizer import Token


class VariableInstantiationState(enum.Enum):
    TYPE = enum.auto()
    TYPE_ARRAY = enum.auto()
    VALUE = enum.auto()
    END = enum.auto()


class MidlVariableInstantiationParser(MidlBaseParser):
    def __init__(self, token_generator, tokenizer):
        self.state = VariableInstantiationState.TYPE
        super().__init__(
            token_generator=token_generator,
            end_state=VariableInstantiationState.END,
            tokenizer=tokenizer,
        )
        self.rbracket_level = 0
        self.brace_level = 0
        self.type_parts = []
        self.value_parts = []

    def add_state_data(self, token: Token):
        if self.state == VariableInstantiationState.TYPE:
            self.type_parts.append(token.data)
        elif self.state == VariableInstantiationState.VALUE:
            self.value_parts.append(token.data)
        else:
            self.invalid(token)

    def keyword(self, token: Token):
        self.add_state_data(token)

    def symbol(self, token: Token):
        self.add_state_data(token)

    def numeric(self, token: Token):
        if self.state != VariableInstantiationState.VALUE:
            self.invalid(token)
        self.value_parts.append(token.data)

    def rbracket(self, token: Token):
        if self.state == VariableInstantiationState.VALUE:
            # Just make sure they're balanced since we're not evaluating
            if token.data == "(":
                self.rbracket_level += 1
            elif token.data == ")" and self.rbracket_level > 0:
                self.rbracket_level -= 1
            else:
                self.invalid(token)
            self.value_parts += token.data
        else:
            self.invalid(token)

    def sqbracket(self, token: Token):
        if token.data == "[" and self.state in [
            VariableInstantiationState.TYPE,
            VariableInstantiationState.TYPE_ARRAY,
        ]:
            # Grab the array dimensions for the type
            self.value_dimensions.append(MidlArrayParser(self.tokens).parse(token))
            self.state = VariableInstantiationState.TYPE_ARRAY
            self.type_parts.append(token.data)
        elif self.state == VariableInstantiationState.VALUE:
            self.value_parts.append(token.data)
        else:
            self.invalid(token)

    def brace(self, token: Token):
        if self.state == VariableInstantiationState.VALUE:
            # Just make sure they're balanced since we're not evaluating
            if token.data == "{":
                self.brace_level += 1
            elif token.data == "}" and self.brace_level > 0:
                self.brace_level -= 1
            else:
                self.invalid(token)
            self.value_parts += token.data
        else:
            self.invalid(token)

    def operator(self, token: Token):
        if (
            self.state
            in [VariableInstantiationState.TYPE, VariableInstantiationState.TYPE_ARRAY]
            and token.data == "="
        ):
            # Make sure there is data for our name and type
            if not len(self.type_parts) > 1:
                self.invalid(token)
            self.name = self.type_parts[-1]
            self.type = self.type_parts[:-1]
            self.state = VariableInstantiationState.VALUE
        elif self.state == VariableInstantiationState.VALUE:
            # Operator that's part of the value
            self.value_parts.append(token.data)
        else:
            self.invalid(token)

    def semicolon(self, token: Token):
        # Make sure we have some value data
        if self.state in [
            VariableInstantiationState.TYPE,
            VariableInstantiationState.TYPE_ARRAY,
        ]:
            # There's no value for this.. Might just be a forward declaration?
            if "interface" in self.type_parts:
                self.state = VariableInstantiationState.END
            else:
                self.invalid(token)
        elif self.state == VariableInstantiationState.VALUE and len(self.value_parts):
            self.state = VariableInstantiationState.END
        else:
            self.invalid(token)

    def finished(self) -> MidlVariableInstantiation:
        var_name = self.type_parts[-1]
        var_type = " ".join(self.type_parts[:-1])
        var_value = " ".join(self.value_parts)
        instantiation = MidlVariableInstantiation(
            var_type, var_name, rhs=var_value, const=var_type[0] == "const"
        )
        return instantiation
