import abc
from fuzzer.datatype import DataTypeLookup
from fuzzer.config import creds, hostname, rand as random

"""Base classes for fuzzer generator generation code
"""


class Fuzzable(abc.ABC):
    "Class that acts as a registry for mapping types to generators"
    __REGISTRY = DataTypeLookup()

    def registry(self):
        """returns the static __REGISTRY to be used across child classes"""
        return Fuzzable.__REGISTRY

    def add_mapping(self, type_name, target_type):
        """Inserts a type mapping into the registry"""
        Fuzzable.__REGISTRY.insert(type_name, target_type)

    @abc.abstractmethod
    def generate(self):
        pass

    def get_one_of_type(self, requested_type):
        # TODO: Add a coinflip here to decided whether to generate a new isntance of the given type,
        #  or to do a lookup through previous defined variables and objects to find and instance
        pass


class NDRINTERFACE:
    INSTANCES = []

    def __init__(self, uuid, version, methods):
        """Rpc Interface class"""
        self.uuid = uuid
        self.version = version
        self.methods = list(filter(lambda m: "NotUsedOnWire" not in m.__name__ , methods))
        NDRINTERFACE.INSTANCES.append(self)

    @classmethod
    def generate(cls, iters, fuzzer):
        """Generate an invocation of a function from one interface"""
        # CONNECT HERE
        interface = random.choice(NDRINTERFACE.INSTANCES)
        testcase = Testcase()
        testcase.add(f"from {fuzzer.server} import *\n")
        interface.connect(testcase)
        for i in range(0, iters):
            method = random.choice(interface.methods)
            if len(method().structure) > 0:
                while method().structure[0][1].is_context_handle() == True:
                    method = random.choice(interface.methods)
                    if len(method().structure) == 0:
                        break

            testcase.add(method.generate(testcase, fuzzer))
        return testcase

    def connect(self,testcase):
        username, password = creds
        host = hostname
        testcase.add("""
from impacket.dcerpc.v5 import  epm
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE, DCERPCException
from impacket.dcerpc.v5.transport import DCERPCTransportFactory""")
        #TODO hardcoded version numbers until the version bug is fixed.
        testcase.add(f"""
try:
    stringBinding = epm.hept_map('{host}', uuidtup_to_bin(('{self.uuid}', '0.0')), protocol='ncacn_ip_tcp')
except impacket.dcerpc.v5.rpcrt.DCERPCException:
    from fuzzer.epm import get_mapping
    stringBinding = get_mapping('{self.uuid}', '{host}')
rpctransport = DCERPCTransportFactory(stringBinding)
rpctransport.set_credentials('{username}', '{password}', '', '', '')
dce = rpctransport.get_dce_rpc()
#dce.set_auth_level(RPC_C_AUTHN_LEVEL_PKT_PRIVACY)
dce.connect()
dce.bind(uuidtup_to_bin(('{self.uuid}', '0.0')))
""")


class Testcase:
    def __init__(self):
        # holds variable definitions and invocations
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def __str__(self):
        out = ""
        for s in self.statements:
            out += str(s) + "\n"
        return out
