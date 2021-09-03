import abc
from fuzzer.datatype import DataTypeLookup
from fuzzer.config import creds, hostname, rand as random

"""Base classes for fuzzer generator generation code
"""


class NDRINTERFACE:
    INSTANCES = []

    def __init__(self, uuid, version, methods):
        """Rpc Interface class"""
        self.uuid = uuid
        self.version = version
        self.methods = list(
            filter(lambda m: "NotUsedOnWire" not in m.__name__, methods)
        )
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
                first_entry = method().structure[0][1]
                if hasattr(first_entry, "is_context_handle"):
                    while first_entry.is_context_handle() == True:
                        method = random.choice(interface.methods)
                        first_entry = method().structure[0][1]
                        if len(method().structure) == 0 or hasattr(
                            first_entry, "is_context_handle"
                        ):
                            break

            testcase.add(method.generate(testcase, fuzzer))
        return testcase

    def connect(self, testcase):
        username, password = creds
        host = hostname
        testcase.add(
            """
from impacket.dcerpc.v5 import  epm
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE, DCERPCException
from impacket.dcerpc.v5.transport import DCERPCTransportFactory"""
        )
        # TODO hardcoded version numbers until the version bug is fixed.
        testcase.add(
            f"""
try:
    stringBinding = epm.hept_map('{host}', uuidtup_to_bin(('{self.uuid}', '2.0')))
except impacket.dcerpc.v5.rpcrt.DCERPCException:
    from fuzzer.epm import get_mapping
    stringBinding = get_mapping('{self.uuid}', '{host}')
rpctransport = DCERPCTransportFactory(stringBinding)
rpctransport.set_credentials('{username}', '{password}', '', '', '')
dce = rpctransport.get_dce_rpc()
#dce.set_auth_level(RPC_C_AUTHN_LEVEL_PKT_PRIVACY)
dce.connect()
dce.bind(uuidtup_to_bin(('{self.uuid}', '2.0')))
"""
        )


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
