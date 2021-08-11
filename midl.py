from base import Visitable, Visitor
import string

class Macroable(Visitable):
    def apply_macro(self, visitor:Visitor, macro):
        raise Exception(f"Class {self.__class__} must implement `apply_macro()`")


    def _do_macro(self, s:str, macro):
        idx = s.find(macro[0])
        if idx == -1:
            return s
        invalid_prev = string.ascii_letters + string.digits + "_"

        substr = s[:idx+len(macro[0])]
        valid_replacement = True
        if idx > 0:
            if s[idx-1] in invalid_prev:
                valid_replacement = False
        if idx != len(s)-1:
            if s[idx+1] in invalid_prev:
                valid_replacement = False
        if valid_replacement:
            substr = substr.replace(macro[0], macro[1])
        cont = s[idx+len(macro[0])+1:]
        if len(cont) > 1:
            s = substr + self._do_macro(s[idx+len(macro[0])+1:], macro)
        else:
            s = substr
        return s

    def _do_macro_iterable(self, iterable, macro):
        iterable[:] = [self._do_macro(i, macro) for i in iterable]
        return iterable

class MidlImport:
    """Represents a MIDL import statement

    Example:
        `import "ms-dtyp.idl";`
    """

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return f"import {self.file}"


class MidlArrayDimensions:
    def __init__(self, array_min=-1, array_max=-1):
        self.min = array_min
        self.max = array_max


class MidlVariableInstantiation(Macroable):
    """Represents a MIDL variable instantiation

    Example:
        `const int MAX_PAYLOAD = 2 * 1024 * 1024;`
    """

    def __init__(self, var_type, name, rhs, const: bool):
        self.type = var_type  # typing of the variable
        self.name = name  # name of the variable
        self.rhs = rhs  # un-parsed righthandside of the statement
        self.const = const  # boolean whether it is a constant

    def __str__(self):
        out = ""
        if self.const == True:
            out += "const "
        out += f"{self.type} {self.name} = {self.rhs};"
        return out

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.type = self._do_macro(self.type, macro)
        self.name = self._do_macro(self.name, macro)
        self.rhs = self._do_macro(self.rhs, macro)

class MidlDefinition(Macroable):
    """Represents a MIDL Definition. Maps directly to a MIDL file"""

    def __init__(self):
        self.imports = []  # Imports
        self.comments = []
        self.instantiation = []  # Variable instantiation
        self.interfaces = []  # Interface defintions. Usually only 1 per file...
        self.dispinterfaces = []  # Interface defintions. Usually only 1 per file...
        self.coclasses = []
        self.typedefs = []
        self.defines = []
        self.cpp_quotes = []

    def add_import(self, imp: str):
        self.imports.append(MidlImport(imp))

    def add_instantiation(self, var_type, name, rhs, const=False):
        self.instantiation.append(MidlVariableInstantiation(var_type, name, rhs, const))

    def add_interface(self, interface):
        self.interfaces.append(interface)

    def add_comment(self, comment):
        self.comments.append(comment)

    def apply_macro(self, visitor:Visitor, macro:tuple):
        # replace the entries in the defines list
        self.defines = self._do_macro_iterable(self.defines, macro)
        self.instantiation[:] = [x.accept(visitor) for x in self.instantiation]
        self.interfaces[:] = [x.accept(visitor) for x in self.interfaces]
        self.dispinterfaces[:] = [x.accept(visitor) for x in self.dispinterfaces]
        self.coclasses[:] = [x.accept(visitor) for x in self.coclasses]
        self.typedefs[:] = [x.accept(visitor) for x in self.typedefs]

    def __str__(self):
        out = ""
        for i in self.imports:
            out += str(i) + "\n"
        for i in self.instantiation:
            out += str(i) + "\n"
        for i in self.interfaces:
            out += str(i) + "\n"
        for i in self.dispinterfaces:
            out += str(i) + "\n"
        for i in self.coclasses:
            out += str(i) + "\n"
        return out


class MidlInterface(Macroable):
    """Represents a MIDL interface

    Truncated example:
        ` [
            uuid (f6beaff7-1e19-4fbb-9f8f-b89e2018337c),
            version(1.0),
            pointer_default(unique)
           ]
            interface IEventService
            {
                typedef [context_handle] void* PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION;
                typedef [context_handle] void* PCONTEXT_HANDLE_LOG_QUERY;
                typedef [context_handle] void* PCONTEXT_HANDLE_LOG_HANDLE;
                typedef [context_handle] void* PCONTEXT_HANDLE_OPERATION_CONTROL;
                typedef [context_handle] void* PCONTEXT_HANDLE_PUBLISHER_METADATA;
                typedef [context_handle] void* PCONTEXT_HANDLE_EVENT_METADATA_ENUM;





                typedef struct tag_RpcInfo
                {
                DWORD m_error,
                        m_subErr,
                        m_subErrParam;
                } RpcInfo;
                error_status_t EvtRpcRegisterRemoteSubscription(
                /* [in] RPC_BINDING_HANDLE binding, {the binding handle will be generated by MIDL} */
                [in, unique, range(0, MAX_RPC_CHANNEL_NAME_LENGTH),string] LPCWSTR channelPath,
                [in, range(1, MAX_RPC_QUERY_LENGTH),string] LPCWSTR query,
                [in, unique, range(0, MAX_RPC_BOOKMARK_LENGTH),string] LPCWSTR bookmarkXml,
                [in] DWORD flags,
                [out, context_handle] PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION* handle,
                [out, context_handle] PCONTEXT_HANDLE_OPERATION_CONTROL* control,
                [out] DWORD* queryChannelInfoSize,
                [out, size_is(,*queryChannelInfoSize),
                    range(0, MAX_RPC_QUERY_CHANNEL_SIZE)]
                        EvtRpcQueryChannelInfo** queryChannelInfo,
                [out] RpcInfo *error);
            }
        `
    """

    def __init__(self):
        self.attributes = {}
        self.imports = []
        self.name = None
        self.typedefs = []
        self.procedures = []
        self.comments = []
        self.cpp_quotes = []
        self.defines = []
        self.parents = []
        self.vardefs = []
    
    def add_vardef(self, vd):
        self.vardefs.append(vd)

    def add_typedef(self, td):
        self.typedefs.append(td)

    def add_procedure(self, p):
        self.procedures.append(p)

    def add_comment(self, c):
        self.comments.append(c)

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.name = self._do_macro(self.name, macro)
        # replace the entries in the defines list
        self.defines = self._do_macro_iterable(self.defines, macro)
        self.procedures[:] = [x.accept(visitor) for x in self.procedures]
        self.parents = self._do_macro_iterable(self.parents, macro)
        self.vardefs[:] = [x.accept(visitor) for x in self.vardefs]
        self.typedefs[:] = [x.accept(visitor) for x in self.typedefs]

    def __str__(self):
        if "version" in self.attributes:
            version = self.attributes["version"].params[0]
        else:
            version = '-1'
        if "uuid" in self.attributes:
            iface_uuid = self.attributes["uuid"].params[0]
        else:
            iface_uuid = ''
        out = ""
        out += "UUID: " + iface_uuid + ";\n"
        out += "Version: " + version + ";\n"
        out += "interface " + self.name + "{\n"
        for imp in self.imports:
            out += imp + '\n'
        for td in self.typedefs:
            out += str(td)
        for p in self.procedures:
            out += str(p)
        return out

class MidlDispInterface(Macroable):
    def __init__(self, name=None, interface=None, properties=None, methods=None):
        self.name = name
        self.interface = interface
        self.properties = properties or []
        self.methods = methods or []
        self.comments = []

    def __str__(self):
        out = f"dispinterface {self.name}\n"
        out += f"interface: {self.interface}"
        out += "properties\n"
        out += '\n    '.join([str(property) for property in self.properties])
        out += "methods\n"
        out += '\n    '.join([str(method) for method in self.methods])
        return out


class MidlCoclass(Macroable):
    def __init__(self, name, interfaces):
        self.name = name
        self.interfaces = interfaces
        self.attributes = {}

    def __str__(self):
        out = f'coclass {self.name}\n'
        out += 'interfaces:\n    '
        out += '\n    '.join([str(iface) for iface in self.interfaces])
        return out

class MidlAttribute(Macroable):
    """MIDL Attribute definition
    e.g. size_is(5)
    """

    def __init__(self, name, params=None):
        self.name = name
        self.params = params or []

    def __str__(self):
        out = ""
        out += self.name
        if self.params != []:
            out += "("
            for param in self.params:
                out += str(param)
                out += ", "
            out = out[:-1]
            out+=")"
        return out

class MidlVarDef(Macroable):
    """Struct member or function parameter
    Example:
        `[size_is(count)] EvtRpcVariant* props;`
    """

    def __init__(
        self,
        var_type,
        name,
        attrs: dict[str, MidlAttribute] = None,
        array_info=list[MidlArrayDimensions],
    ):
        self.type = var_type
        self.name = name
        self.attrs = attrs or {}
        self.array_info = array_info or []

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.name = self._do_macro(self.name, macro)
        self.type = self._do_macro(self.type, macro)

    def __str__(self):
        out = f"{self.type} {self.name}"
        return out


class MidlTypeDef(Macroable):
    """Represents a typedef, can either be a simple mapping, or a complex struct definition."""

    def __init__(self, td, attrs):
        self.type = td
        self.name = td.name
        self.attrs = attrs

    def __str__(self):
        out = "typedef "
        out += f"{self.type.type} {self.name};\n"
        return out


class MidlStructDef(Macroable):
    def __init__(self, public_names, private_name, members: list[MidlVarDef]):
        self.public_names = public_names
        self.private_name = private_name
        self.members = members

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.public_names = self._do_macro_iterable(self.public_names, macro)
        if self.private_name != None:
            self.private_name = self._do_macro(self.private_name, macro)
        self.members[:] = [x.accept(visitor) for x in self.members]

    def __str__(self):
        out = "typedef struct "
        out += self.private_name +"\n{\n"
        for member in self.members:
            out += str(member)
            out += ",\n"
        out = out[:-2]
        out += "\n} "
        for pub_name in self.public_names:
            out += pub_name +","
        out = out[:-1]
        out+=";\n"
        return out

class MidlUnionDef(Macroable):
    def __init__(self, public_names, private_name, members: list[MidlVarDef]):
        self.public_names = public_names
        self.private_name = private_name or ''
        self.members = members

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.public_names = self._do_macro_iterable(self.public_names, macro)
        if self.private_name != None:
            self.private_name = self._do_macro(self.private_name, macro)
        self.members[:] = [x.accept(visitor) for x in self.members]

    def __str__(self):
        out = "typedef union "
        out += self.private_name +"\n{\n"
        for member in self.members:
            out += str(member)
            out += ",\n"
        out = out[:-2]
        out += "\n} "
        for pub_name in self.public_names:
            out += pub_name +","
        out = out[:-1]
        out+=";\n"
        return out

class MidlSimpleTypedef(Macroable):
    def __init__(self, name, simple_type):
        self.name = name
        self.type = simple_type

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.name = self._do_macro(self.name, macro)
        self.type = self._do_macro(self.type, macro)

    def __str__(self):
        out = ""
        out = "typedef " + self.name + " " + self.type +";"
        return out

class MidlEnumDef(Macroable):
    """Definition of a MIDL enum.

    Example:
        `
        typedef [v1_enum] enum tag_EvtRpcVariantType
        {
            EvtRpcVarTypeNull = 0,
            EvtRpcVarTypeBoolean,
            EvtRpcVarTypeUInt32,
            EvtRpcVarTypeUInt64,
            EvtRpcVarTypeString,
            EvtRpcVarTypeGuid,
            EvtRpcVarTypeBooleanArray,
            EvtRpcVarTypeUInt32Array,
            EvtRpcVarTypeUInt64Array,
            EvtRpcVarTypeStringArray,
            EvtRpcVarTypeGuidArray

        } EvtRpcVariantType;
        `
    """

    def __init__(self, public_names, private_name, map):
        self.public_names = public_names
        self.private_name = private_name
        self.map = map

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.public_names = self._do_macro_iterable(self.public_names, macro)
        if self.private_name != None:
            self.private_name = self._do_macro(self.private_name, macro)
        for k in self.map:
            self.map[k] = self._do_macro(self.map[k], macro)

    def __str__(self):

        out = "enum " + self.private_name + f"[{self.public_names}]" + "\n{\n"

        if self.map is None:
            return ""
        for k in self.map.keys():
            out += k
            if self.map[k] is not None:

                out += " = " + str(self.map[k])
            out +=",\n"
        out += "}\n"
        return out


class MidlProcedure(Macroable):
    """MIDL Procedure definition

    Example:
        `
        error_status_t EvtRpcRemoteSubscriptionWaitAsync(
        [in, context_handle] PCONTEXT_HANDLE_REMOTE_SUBSCRIPTION handle );
        `
    """

    def __init__(self, name, attrs, params):
        self.name = name
        self.attrs = attrs
        self.params = params

    def apply_macro(self, visitor:Visitor, macro:tuple):
        self.name = self._do_macro(self.name, macro)
        self.params[:] = [x.accept(visitor) for x in self.params]

    def __str__(self):
        out = ""
        out += self.name +" (\n"
        for i in self.params:
            out += "    " + str(i)
            out +=",\n"
        
        if len(self.params) >0:
            out = out[:-2] #Trim off the last comma and newline
        out += ");\n"
       
        
        return out

        



class MidlParameter(Macroable):
    def __init__(
        self, name=None, data_type=None, attributes: list[MidlAttribute] = None
    ):
        self.name = name
        self.type = data_type
        self.attributes = attributes or []

    def __str__(self):
        out = ""
        has_attrs = len(self.attributes) > 0

        if has_attrs:
            out += "["
            for attr in self.attributes:
                out += str(attr) +","
            out = out[:-1]
            out += "] "
        
        out += self.type + " "
        out += self.name
        return out
