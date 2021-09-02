from generated.ms_even import *


from impacket.dcerpc.v5 import  epm
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE, DCERPCException
from impacket.dcerpc.v5.transport import DCERPCTransportFactory

try:
    stringBinding = epm.hept_map('localhost', uuidtup_to_bin(('82273FDC-E32A-18C3-3F78-827929DC23EA', '0.0')), protocol='ncacn_ip_tcp')
except impacket.dcerpc.v5.rpcrt.DCERPCException:
    from fuzzer.epm import get_mapping
    stringBinding = get_mapping('82273FDC-E32A-18C3-3F78-827929DC23EA', 'localhost')
rpctransport = DCERPCTransportFactory(stringBinding)
rpctransport.set_credentials('m', 'password', '', '', '')
dce = rpctransport.get_dce_rpc()
#dce.set_auth_level(RPC_C_AUTHN_LEVEL_PKT_PRIVACY)
dce.connect()
dce.bind(uuidtup_to_bin(('82273FDC-E32A-18C3-3F78-827929DC23EA', '0.0')))

v1 = LPWSTR

v2 = None # TODO PRPC_UNICODE_STRING

v3 = 1073741815.75

req = ElfrOpenBELW()
req.UNCServerName = v1
req.BackupFileName = v2
req.MajorVersion = v3
req.MinorVersion = v3
v4 = dce.request(req)

v5 = None # TODO LPWSTR

req = ElfrOpenBELW()
req.UNCServerName = v5
req.BackupFileName = v2
req.MajorVersion = v3
req.MinorVersion = v4['MinorVersion']
v6 = dce.request(req)

v7 = 134217724.96875

v8 = 536870909.875

req = ElfrOpenELW()
req.UNCServerName = v5
req.ModuleName = v2
req.RegModuleName = v6['BackupFileName']
req.MajorVersion = v7
req.MinorVersion = v8
v9 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v1
req.ModuleName = v4['BackupFileName']
req.RegModuleName = v9['ModuleName']
req.MajorVersion = v6['MajorVersion']
req.MinorVersion = v4['MinorVersion']
v10 = dce.request(req)

v11 = None # TODO LPSTR

v12 = None # TODO PRPC_STRING

v13 = None # TODO PRPC_STRING

req = ElfrOpenELA()
req.UNCServerName = v11
req.ModuleName = v12
req.RegModuleName = v13
req.MajorVersion = v6['MajorVersion']
req.MinorVersion = v10['MinorVersion']
v14 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v6['UNCServerName']
req.ModuleName = v10['RegModuleName']
req.RegModuleName = v10['ModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v10['MajorVersion']
v15 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v6['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v15['RegModuleName']
req.MajorVersion = v7
req.MinorVersion = v10['MajorVersion']
v16 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v9['ModuleName']
req.RegModuleName = v15['RegModuleName']
req.MajorVersion = v8
req.MinorVersion = v3
v17 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v11
req.ModuleName = v14['RegModuleName']
req.RegModuleName = v12
req.MajorVersion = v6['MajorVersion']
req.MinorVersion = v6['MajorVersion']
v18 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v9['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v9['RegModuleName']
req.MajorVersion = v17['MajorVersion']
req.MinorVersion = v16['MinorVersion']
v19 = dce.request(req)