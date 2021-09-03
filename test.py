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

v1 = b'\xff\xfe?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

v2 = RPC_UNICODE_STRING()
v2['Length'] = 16390
v2['MaximumLength'] = 11028
v2['Buffer'] = UC_WCHAR_ARRAY()
v2['Buffer'].append(8186)
v2['Buffer'].append(12410)
v2['Buffer'].append(4087)
v2['Buffer'].append(16384)
v2['Buffer'].append(251)
v2['Buffer'].append(26337)
v2['Buffer'].append(249)
v2['Buffer'].append(16390)
v2['Buffer'].append(57732)
v2['Buffer'].append(3366)
v2['Buffer'].append(60077)
v2['Buffer'].append(16376)
v2['Buffer'].append(61233)
v2['Buffer'].append(8184)
v2['Buffer'].append(25756)
v2['Buffer'].append(8197)
v2['Buffer'].append(16385)
v2['Buffer'].append(16380)
v2['Buffer'].append(3)
v2['Buffer'].append(8195)
v2['Buffer'].append(253)
v2['Buffer'].append(25191)
v2['Buffer'].append(60376)
v2['Buffer'].append(4099)
v2['Buffer'].append(8188)
v2['Buffer'].append(16376)
v2['Buffer'].append(5194)
v2['Buffer'].append(30005)
v2['Buffer'].append(8198)
v2['Buffer'].append(3366)
v2['Buffer'].append(59006)
v2['Buffer'].append(16380)
v2['Buffer'].append(5)
v2['Buffer'].append(65529)
v2['Buffer'].append(22948)
v2['Buffer'].append(4093)
v2['Buffer'].append(257)
v2['Buffer'].append(4094)
v2['Buffer'].append(256)
v2['Buffer'].append(4094)
v2['Buffer'].append(31568)
v2['Buffer'].append(258)
v2['Buffer'].append(8183)
v2['Buffer'].append(8187)
v2['Buffer'].append(7532)



v3 = 65531

req = ElfrRegisterEventSourceW()
req.UNCServerName = v1
req.ModuleName = v2
req.RegModuleName = v2
req.MajorVersion = v3
req.MinorVersion = v3
try:
	v4 = dce.request(req)
except Exception as e:
	print('Error at: v4 failing with: ' + str(e))
	print(req.dump())

v5 = b'\xff\xfe"\x00"\x00"\x00"\x00\x00\x00'.decode('utf-16')

v6 = RPC_STRING()
v6['Length'] = 257
v6['MaximumLength'] = 39001
v6['Buffer'] = UC_CHAR_ARRAY()
v6['Buffer'].append(255)
v6['Buffer'].append(133)
v6['Buffer'].append(188)
v6['Buffer'].append(230)
v6['Buffer'].append(112)
v6['Buffer'].append(240)
v6['Buffer'].append(56)
v6['Buffer'].append(246)
v6['Buffer'].append(224)
v6['Buffer'].append(66)
v6['Buffer'].append(65)
v6['Buffer'].append(210)
v6['Buffer'].append(246)
v6['Buffer'].append(43)
v6['Buffer'].append(103)
v6['Buffer'].append(112)
v6['Buffer'].append(255)
v6['Buffer'].append(37)
v6['Buffer'].append(75)
v6['Buffer'].append(10)
v6['Buffer'].append(20)
v6['Buffer'].append(7)
v6['Buffer'].append(29)
v6['Buffer'].append(61)
v6['Buffer'].append(224)
v6['Buffer'].append(100)
v6['Buffer'].append(12)
v6['Buffer'].append(24)
v6['Buffer'].append(112)
v6['Buffer'].append(11)
v6['Buffer'].append(62)
v6['Buffer'].append(31)
v6['Buffer'].append(230)
v6['Buffer'].append(103)
v6['Buffer'].append(224)
v6['Buffer'].append(183)
v6['Buffer'].append(43)
v6['Buffer'].append(7)
v6['Buffer'].append(61)
v6['Buffer'].append(2)
v6['Buffer'].append(24)
v6['Buffer'].append(151)
v6['Buffer'].append(20)
v6['Buffer'].append(32)
v6['Buffer'].append(58)
v6['Buffer'].append(14)
v6['Buffer'].append(25)
v6['Buffer'].append(64)
v6['Buffer'].append(20)
v6['Buffer'].append(16)
v6['Buffer'].append(238)
v6['Buffer'].append(98)
v6['Buffer'].append(247)
v6['Buffer'].append(247)
v6['Buffer'].append(252)
v6['Buffer'].append(246)
v6['Buffer'].append(45)
v6['Buffer'].append(36)
v6['Buffer'].append(183)
v6['Buffer'].append(3)
v6['Buffer'].append(103)
v6['Buffer'].append(130)
v6['Buffer'].append(63)
v6['Buffer'].append(10)
v6['Buffer'].append(254)
v6['Buffer'].append(98)
v6['Buffer'].append(249)
v6['Buffer'].append(18)
v6['Buffer'].append(57)
v6['Buffer'].append(103)
v6['Buffer'].append(29)
v6['Buffer'].append(24)
v6['Buffer'].append(151)
v6['Buffer'].append(28)
v6['Buffer'].append(249)
v6['Buffer'].append(139)
v6['Buffer'].append(230)
v6['Buffer'].append(7)
v6['Buffer'].append(56)
v6['Buffer'].append(0)
v6['Buffer'].append(89)
v6['Buffer'].append(30)
v6['Buffer'].append(26)
v6['Buffer'].append(210)
v6['Buffer'].append(60)
v6['Buffer'].append(248)
v6['Buffer'].append(36)
v6['Buffer'].append(18)
v6['Buffer'].append(2)
v6['Buffer'].append(124)
v6['Buffer'].append(12)
v6['Buffer'].append(247)
v6['Buffer'].append(206)
v6['Buffer'].append(19)
v6['Buffer'].append(28)
v6['Buffer'].append(24)
v6['Buffer'].append(0)
v6['Buffer'].append(135)
v6['Buffer'].append(21)
v6['Buffer'].append(249)
v6['Buffer'].append(7)
v6['Buffer'].append(20)
v6['Buffer'].append(133)
v6['Buffer'].append(206)
v6['Buffer'].append(170)
v6['Buffer'].append(246)
v6['Buffer'].append(238)
v6['Buffer'].append(253)
v6['Buffer'].append(20)
v6['Buffer'].append(238)
v6['Buffer'].append(28)
v6['Buffer'].append(18)
v6['Buffer'].append(103)
v6['Buffer'].append(66)
v6['Buffer'].append(24)
v6['Buffer'].append(247)
v6['Buffer'].append(26)
v6['Buffer'].append(189)
v6['Buffer'].append(146)
v6['Buffer'].append(98)
v6['Buffer'].append(28)
v6['Buffer'].append(67)
v6['Buffer'].append(251)
v6['Buffer'].append(188)
v6['Buffer'].append(29)
v6['Buffer'].append(57)
v6['Buffer'].append(5)
v6['Buffer'].append(103)
v6['Buffer'].append(25)
v6['Buffer'].append(15)
v6['Buffer'].append(240)



req = ElfrOpenBELA()
req.UNCServerName = v5
req.BackupFileName = v6
req.MajorVersion = v3
req.MinorVersion = v4['MajorVersion']
try:
	v7 = dce.request(req)
except Exception as e:
	print('Error at: v7 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v2
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v3
try:
	v8 = dce.request(req)
except Exception as e:
	print('Error at: v8 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v8['RegModuleName']
req.RegModuleName = v2
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v7['MajorVersion']
try:
	v9 = dce.request(req)
except Exception as e:
	print('Error at: v9 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v1
req.ModuleName = v9['ModuleName']
req.RegModuleName = v9['RegModuleName']
req.MajorVersion = v8['MinorVersion']
req.MinorVersion = v7['MinorVersion']
try:
	v10 = dce.request(req)
except Exception as e:
	print('Error at: v10 failing with: ' + str(e))
	print(req.dump())

v11 = 16777214

req = ElfrOpenELA()
req.UNCServerName = v5
req.ModuleName = v7['BackupFileName']
req.RegModuleName = v6
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v11
try:
	v12 = dce.request(req)
except Exception as e:
	print('Error at: v12 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v5
req.ModuleName = v12['ModuleName']
req.RegModuleName = v12['ModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v4['MajorVersion']
try:
	v13 = dce.request(req)
except Exception as e:
	print('Error at: v13 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v9['UNCServerName']
req.BackupFileName = v10['ModuleName']
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v10['MajorVersion']
try:
	v14 = dce.request(req)
except Exception as e:
	print('Error at: v14 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v9['RegModuleName']
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v12['MajorVersion']
try:
	v15 = dce.request(req)
except Exception as e:
	print('Error at: v15 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v14['BackupFileName']
req.RegModuleName = v8['ModuleName']
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v8['MajorVersion']
try:
	v16 = dce.request(req)
except Exception as e:
	print('Error at: v16 failing with: ' + str(e))
	print(req.dump())

