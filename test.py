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

v1 = b'\xff\xfe]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00\x00\x00\x00\x00'.decode('utf-16')

v2 = RPC_STRING()
v2['Length'] = 38896
v2['MaximumLength'] = 65530
v2['Buffer'] = UC_CHAR_ARRAY()
v2['Buffer'].append(40)
v2['Buffer'].append(3)
v2['Buffer'].append(11)
v2['Buffer'].append(169)
v2['Buffer'].append(50)
v2['Buffer'].append(38)
v2['Buffer'].append(74)
v2['Buffer'].append(13)
v2['Buffer'].append(216)
v2['Buffer'].append(69)
v2['Buffer'].append(30)
v2['Buffer'].append(147)
v2['Buffer'].append(5)
v2['Buffer'].append(6)
v2['Buffer'].append(67)
v2['Buffer'].append(111)
v2['Buffer'].append(70)
v2['Buffer'].append(31)
v2['Buffer'].append(132)
v2['Buffer'].append(38)
v2['Buffer'].append(34)
v2['Buffer'].append(5)
v2['Buffer'].append(24)
v2['Buffer'].append(238)
v2['Buffer'].append(63)
v2['Buffer'].append(253)
v2['Buffer'].append(237)
v2['Buffer'].append(25)
v2['Buffer'].append(32)
v2['Buffer'].append(197)
v2['Buffer'].append(29)
v2['Buffer'].append(63)
v2['Buffer'].append(56)
v2['Buffer'].append(16)
v2['Buffer'].append(94)
v2['Buffer'].append(74)
v2['Buffer'].append(29)
v2['Buffer'].append(24)
v2['Buffer'].append(17)
v2['Buffer'].append(60)
v2['Buffer'].append(36)
v2['Buffer'].append(2)
v2['Buffer'].append(6)
v2['Buffer'].append(4)
v2['Buffer'].append(32)
v2['Buffer'].append(248)
v2['Buffer'].append(121)
v2['Buffer'].append(216)
v2['Buffer'].append(41)
v2['Buffer'].append(24)
v2['Buffer'].append(111)
v2['Buffer'].append(67)
v2['Buffer'].append(2)
v2['Buffer'].append(120)
v2['Buffer'].append(206)
v2['Buffer'].append(205)
v2['Buffer'].append(70)
v2['Buffer'].append(154)
v2['Buffer'].append(6)
v2['Buffer'].append(18)
v2['Buffer'].append(20)
v2['Buffer'].append(32)
v2['Buffer'].append(40)
v2['Buffer'].append(34)
v2['Buffer'].append(248)
v2['Buffer'].append(9)
v2['Buffer'].append(0)
v2['Buffer'].append(63)
v2['Buffer'].append(57)
v2['Buffer'].append(201)
v2['Buffer'].append(120)
v2['Buffer'].append(8)
v2['Buffer'].append(17)
v2['Buffer'].append(216)
v2['Buffer'].append(169)
v2['Buffer'].append(12)
v2['Buffer'].append(36)
v2['Buffer'].append(250)
v2['Buffer'].append(19)
v2['Buffer'].append(120)
v2['Buffer'].append(1)
v2['Buffer'].append(94)
v2['Buffer'].append(254)
v2['Buffer'].append(52)
v2['Buffer'].append(237)
v2['Buffer'].append(50)
v2['Buffer'].append(24)
v2['Buffer'].append(35)
v2['Buffer'].append(123)
v2['Buffer'].append(20)
v2['Buffer'].append(37)
v2['Buffer'].append(10)
v2['Buffer'].append(33)
v2['Buffer'].append(111)
v2['Buffer'].append(74)
v2['Buffer'].append(82)
v2['Buffer'].append(41)
v2['Buffer'].append(23)
v2['Buffer'].append(25)
v2['Buffer'].append(22)
v2['Buffer'].append(4)
v2['Buffer'].append(58)
v2['Buffer'].append(120)
v2['Buffer'].append(21)
v2['Buffer'].append(13)
v2['Buffer'].append(64)
v2['Buffer'].append(22)
v2['Buffer'].append(6)
v2['Buffer'].append(52)
v2['Buffer'].append(4)
v2['Buffer'].append(66)
v2['Buffer'].append(142)
v2['Buffer'].append(11)
v2['Buffer'].append(97)
v2['Buffer'].append(123)
v2['Buffer'].append(35)
v2['Buffer'].append(1)
v2['Buffer'].append(120)
v2['Buffer'].append(247)
v2['Buffer'].append(120)
v2['Buffer'].append(8)
v2['Buffer'].append(11)
v2['Buffer'].append(247)
v2['Buffer'].append(74)
v2['Buffer'].append(67)
v2['Buffer'].append(12)
v2['Buffer'].append(65)
v2['Buffer'].append(63)
v2['Buffer'].append(37)
v2['Buffer'].append(13)
v2['Buffer'].append(248)
v2['Buffer'].append(237)
v2['Buffer'].append(77)
v2['Buffer'].append(19)
v2['Buffer'].append(93)
v2['Buffer'].append(241)
v2['Buffer'].append(253)
v2['Buffer'].append(248)
v2['Buffer'].append(12)
v2['Buffer'].append(41)
v2['Buffer'].append(15)
v2['Buffer'].append(132)
v2['Buffer'].append(253)
v2['Buffer'].append(64)
v2['Buffer'].append(36)
v2['Buffer'].append(7)
v2['Buffer'].append(21)
v2['Buffer'].append(38)
v2['Buffer'].append(22)
v2['Buffer'].append(237)
v2['Buffer'].append(34)
v2['Buffer'].append(94)
v2['Buffer'].append(243)
v2['Buffer'].append(19)
v2['Buffer'].append(23)
v2['Buffer'].append(71)
v2['Buffer'].append(67)
v2['Buffer'].append(15)
v2['Buffer'].append(30)
v2['Buffer'].append(90)
v2['Buffer'].append(195)
v2['Buffer'].append(132)
v2['Buffer'].append(8)
v2['Buffer'].append(6)
v2['Buffer'].append(254)
v2['Buffer'].append(22)
v2['Buffer'].append(32)
v2['Buffer'].append(56)
v2['Buffer'].append(201)
v2['Buffer'].append(56)
v2['Buffer'].append(15)
v2['Buffer'].append(25)
v2['Buffer'].append(31)
v2['Buffer'].append(65)
v2['Buffer'].append(69)
v2['Buffer'].append(107)
v2['Buffer'].append(154)
v2['Buffer'].append(30)
v2['Buffer'].append(243)
v2['Buffer'].append(93)
v2['Buffer'].append(216)
v2['Buffer'].append(71)
v2['Buffer'].append(107)
v2['Buffer'].append(67)


print(v1)
v3 = 197124615

req = ElfrOpenBELA()
req.UNCServerName = v1
req.BackupFileName = v2
req.MajorVersion = v3
req.MinorVersion = v3
try:
	v4 = dce.request(req)
except Exception as e:
	print('Error at: v4 failing with: ' + str(e))
	print(req.dump())

v5 = b'\xff\xfe%\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

v6 = RPC_UNICODE_STRING()
v6['Length'] = 3
v6['MaximumLength'] = 247
v6['Buffer'] = UC_WCHAR_ARRAY()
v6['Buffer'].append(16382)
v6['Buffer'].append(8183)
v6['Buffer'].append(10123)
v6['Buffer'].append(3)
v6['Buffer'].append(63568)
v6['Buffer'].append(8183)
v6['Buffer'].append(4096)
v6['Buffer'].append(4093)
v6['Buffer'].append(247)
v6['Buffer'].append(16601)
v6['Buffer'].append(4087)
v6['Buffer'].append(4090)
v6['Buffer'].append(262)
v6['Buffer'].append(21186)
v6['Buffer'].append(20539)
v6['Buffer'].append(32994)
v6['Buffer'].append(16387)
v6['Buffer'].append(37502)
v6['Buffer'].append(253)
v6['Buffer'].append(260)
v6['Buffer'].append(4092)
v6['Buffer'].append(65529)
v6['Buffer'].append(4101)
v6['Buffer'].append(250)
v6['Buffer'].append(65528)
v6['Buffer'].append(11546)
v6['Buffer'].append(1)
v6['Buffer'].append(16386)
v6['Buffer'].append(8195)
v6['Buffer'].append(4095)
v6['Buffer'].append(8184)
v6['Buffer'].append(17124)
v6['Buffer'].append(5)
v6['Buffer'].append(64782)
v6['Buffer'].append(4089)
v6['Buffer'].append(8184)
v6['Buffer'].append(8193)
v6['Buffer'].append(16376)
v6['Buffer'].append(8185)
v6['Buffer'].append(4095)
v6['Buffer'].append(65529)
v6['Buffer'].append(262)
v6['Buffer'].append(8197)
v6['Buffer'].append(60492)
v6['Buffer'].append(4090)
v6['Buffer'].append(65528)
v6['Buffer'].append(37502)
v6['Buffer'].append(16390)
v6['Buffer'].append(8193)
v6['Buffer'].append(3)
v6['Buffer'].append(16375)
v6['Buffer'].append(4088)
v6['Buffer'].append(250)
v6['Buffer'].append(4089)
v6['Buffer'].append(37502)
v6['Buffer'].append(26238)
v6['Buffer'].append(34908)
v6['Buffer'].append(16388)
v6['Buffer'].append(65531)



req = ElfrOpenELW()
req.UNCServerName = v5
req.ModuleName = v6
req.RegModuleName = v6
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v4['MajorVersion']
try:
	v7 = dce.request(req)
except Exception as e:
	print('Error at: v7 failing with: ' + str(e))
	print(req.dump())

v8 = 1073741824

req = ElfrOpenBELW()
req.UNCServerName = v7['UNCServerName']
req.BackupFileName = v7['RegModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v8
try:
	v9 = dce.request(req)
except Exception as e:
	print('Error at: v9 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v4['BackupFileName']
req.RegModuleName = v2
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v4['MajorVersion']
try:
	v10 = dce.request(req)
except Exception as e:
	print('Error at: v10 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v9['UNCServerName']
req.BackupFileName = v6
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v9['MajorVersion']
try:
	v11 = dce.request(req)
except Exception as e:
	print('Error at: v11 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v5
req.ModuleName = v7['RegModuleName']
req.RegModuleName = v11['BackupFileName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v9['MinorVersion']
try:
	v12 = dce.request(req)
except Exception as e:
	print('Error at: v12 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v1
req.ModuleName = v4['BackupFileName']
req.RegModuleName = v10['ModuleName']
req.MajorVersion = v12['MinorVersion']
req.MinorVersion = v10['MinorVersion']
try:
	v13 = dce.request(req)
except Exception as e:
	print('Error at: v13 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v4['BackupFileName']
req.MajorVersion = v10['MajorVersion']
req.MinorVersion = v11['MinorVersion']
try:
	v14 = dce.request(req)
except Exception as e:
	print('Error at: v14 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v5
req.ModuleName = v7['ModuleName']
req.RegModuleName = v7['ModuleName']
req.MajorVersion = v14['MajorVersion']
req.MinorVersion = v10['MinorVersion']
try:
	v15 = dce.request(req)
except Exception as e:
	print('Error at: v15 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v6
req.RegModuleName = v9['BackupFileName']
req.MajorVersion = v14['MinorVersion']
req.MinorVersion = v14['MajorVersion']
try:
	v16 = dce.request(req)
except Exception as e:
	print('Error at: v16 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v13['UNCServerName']
req.BackupFileName = v10['RegModuleName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v11['MinorVersion']
try:
	v17 = dce.request(req)
except Exception as e:
	print('Error at: v17 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v6
req.RegModuleName = v7['ModuleName']
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v4['MinorVersion']
try:
	v18 = dce.request(req)
except Exception as e:
	print('Error at: v18 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v1
req.ModuleName = v10['RegModuleName']
req.RegModuleName = v10['RegModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v12['MinorVersion']
try:
	v19 = dce.request(req)
except Exception as e:
	print('Error at: v19 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v9['BackupFileName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v8
try:
	v20 = dce.request(req)
except Exception as e:
	print('Error at: v20 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v18['ModuleName']
req.RegModuleName = v18['RegModuleName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v12['MajorVersion']
try:
	v21 = dce.request(req)
except Exception as e:
	print('Error at: v21 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v4['BackupFileName']
req.RegModuleName = v10['ModuleName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v7['MinorVersion']
try:
	v22 = dce.request(req)
except Exception as e:
	print('Error at: v22 failing with: ' + str(e))
	print(req.dump())

v23 = RPC_STRING()
v23['Length'] = 38896
v23['MaximumLength'] = 47231
v23['Buffer'] = UC_CHAR_ARRAY()
v23['Buffer'].append(255)
v23['Buffer'].append(52)
v23['Buffer'].append(61)
v23['Buffer'].append(22)
v23['Buffer'].append(29)
v23['Buffer'].append(254)
v23['Buffer'].append(254)
v23['Buffer'].append(3)
v23['Buffer'].append(68)
v23['Buffer'].append(24)
v23['Buffer'].append(112)
v23['Buffer'].append(37)
v23['Buffer'].append(10)
v23['Buffer'].append(12)
v23['Buffer'].append(123)
v23['Buffer'].append(4)
v23['Buffer'].append(237)
v23['Buffer'].append(12)
v23['Buffer'].append(0)
v23['Buffer'].append(249)
v23['Buffer'].append(57)
v23['Buffer'].append(73)
v23['Buffer'].append(243)
v23['Buffer'].append(6)
v23['Buffer'].append(247)
v23['Buffer'].append(123)
v23['Buffer'].append(12)
v23['Buffer'].append(169)
v23['Buffer'].append(251)
v23['Buffer'].append(70)
v23['Buffer'].append(33)
v23['Buffer'].append(90)
v23['Buffer'].append(255)
v23['Buffer'].append(205)
v23['Buffer'].append(111)
v23['Buffer'].append(17)
v23['Buffer'].append(252)
v23['Buffer'].append(8)
v23['Buffer'].append(33)
v23['Buffer'].append(3)
v23['Buffer'].append(20)
v23['Buffer'].append(6)
v23['Buffer'].append(27)
v23['Buffer'].append(247)
v23['Buffer'].append(13)
v23['Buffer'].append(37)
v23['Buffer'].append(241)
v23['Buffer'].append(3)
v23['Buffer'].append(59)
v23['Buffer'].append(253)
v23['Buffer'].append(58)
v23['Buffer'].append(61)
v23['Buffer'].append(255)
v23['Buffer'].append(56)
v23['Buffer'].append(57)
v23['Buffer'].append(37)
v23['Buffer'].append(58)
v23['Buffer'].append(19)
v23['Buffer'].append(121)
v23['Buffer'].append(17)
v23['Buffer'].append(111)
v23['Buffer'].append(68)
v23['Buffer'].append(18)
v23['Buffer'].append(65)
v23['Buffer'].append(19)
v23['Buffer'].append(250)
v23['Buffer'].append(15)
v23['Buffer'].append(248)
v23['Buffer'].append(197)
v23['Buffer'].append(28)
v23['Buffer'].append(11)
v23['Buffer'].append(250)
v23['Buffer'].append(14)
v23['Buffer'].append(255)
v23['Buffer'].append(111)
v23['Buffer'].append(69)
v23['Buffer'].append(73)
v23['Buffer'].append(55)
v23['Buffer'].append(112)
v23['Buffer'].append(10)
v23['Buffer'].append(7)
v23['Buffer'].append(55)
v23['Buffer'].append(11)
v23['Buffer'].append(28)
v23['Buffer'].append(37)
v23['Buffer'].append(52)
v23['Buffer'].append(248)
v23['Buffer'].append(66)
v23['Buffer'].append(13)
v23['Buffer'].append(147)
v23['Buffer'].append(32)
v23['Buffer'].append(57)
v23['Buffer'].append(70)
v23['Buffer'].append(10)
v23['Buffer'].append(31)
v23['Buffer'].append(18)
v23['Buffer'].append(35)
v23['Buffer'].append(112)
v23['Buffer'].append(32)
v23['Buffer'].append(154)
v23['Buffer'].append(9)
v23['Buffer'].append(20)



req = ElfrRegisterEventSourceA()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v23
req.RegModuleName = v10['RegModuleName']
req.MajorVersion = v22['MajorVersion']
req.MinorVersion = v15['MajorVersion']
try:
	v24 = dce.request(req)
except Exception as e:
	print('Error at: v24 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v11['BackupFileName']
req.RegModuleName = v12['RegModuleName']
req.MajorVersion = v12['MinorVersion']
req.MinorVersion = v10['MajorVersion']
try:
	v25 = dce.request(req)
except Exception as e:
	print('Error at: v25 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v12['UNCServerName']
req.ModuleName = v9['BackupFileName']
req.RegModuleName = v7['ModuleName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v7['MajorVersion']
try:
	v26 = dce.request(req)
except Exception as e:
	print('Error at: v26 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v17['BackupFileName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v26['MajorVersion']
try:
	v27 = dce.request(req)
except Exception as e:
	print('Error at: v27 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v13['RegModuleName']
req.RegModuleName = v22['ModuleName']
req.MajorVersion = v18['MinorVersion']
req.MinorVersion = v26['MajorVersion']
try:
	v28 = dce.request(req)
except Exception as e:
	print('Error at: v28 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v25['UNCServerName']
req.ModuleName = v18['RegModuleName']
req.RegModuleName = v21['RegModuleName']
req.MajorVersion = v22['MajorVersion']
req.MinorVersion = v7['MinorVersion']
try:
	v29 = dce.request(req)
except Exception as e:
	print('Error at: v29 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v13['UNCServerName']
req.BackupFileName = v22['RegModuleName']
req.MajorVersion = v22['MinorVersion']
req.MinorVersion = v29['MinorVersion']
try:
	v30 = dce.request(req)
except Exception as e:
	print('Error at: v30 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v25['UNCServerName']
req.ModuleName = v21['RegModuleName']
req.RegModuleName = v26['RegModuleName']
req.MajorVersion = v14['MinorVersion']
req.MinorVersion = v14['MinorVersion']
try:
	v31 = dce.request(req)
except Exception as e:
	print('Error at: v31 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v5
req.ModuleName = v20['BackupFileName']
req.RegModuleName = v6
req.MajorVersion = v11['MajorVersion']
req.MinorVersion = v10['MinorVersion']
try:
	v32 = dce.request(req)
except Exception as e:
	print('Error at: v32 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v25['UNCServerName']
req.ModuleName = v29['ModuleName']
req.RegModuleName = v32['ModuleName']
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v16['MinorVersion']
try:
	v33 = dce.request(req)
except Exception as e:
	print('Error at: v33 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v14['UNCServerName']
req.BackupFileName = v13['ModuleName']
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v9['MinorVersion']
try:
	v34 = dce.request(req)
except Exception as e:
	print('Error at: v34 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v5
req.BackupFileName = v29['ModuleName']
req.MajorVersion = v25['MajorVersion']
req.MinorVersion = v10['MajorVersion']
try:
	v35 = dce.request(req)
except Exception as e:
	print('Error at: v35 failing with: ' + str(e))
	print(req.dump())

v36 = RPC_UNICODE_STRING()
v36['Length'] = 59036
v36['MaximumLength'] = 32994
v36['Buffer'] = UC_WCHAR_ARRAY()
v36['Buffer'].append(16379)
v36['Buffer'].append(254)
v36['Buffer'].append(38896)
v36['Buffer'].append(25696)
v36['Buffer'].append(11546)
v36['Buffer'].append(10898)
v36['Buffer'].append(49383)
v36['Buffer'].append(16379)
v36['Buffer'].append(16382)
v36['Buffer'].append(8187)
v36['Buffer'].append(262)
v36['Buffer'].append(11546)
v36['Buffer'].append(4098)
v36['Buffer'].append(32994)
v36['Buffer'].append(8186)
v36['Buffer'].append(16601)
v36['Buffer'].append(37502)
v36['Buffer'].append(37502)
v36['Buffer'].append(57556)
v36['Buffer'].append(10123)
v36['Buffer'].append(32994)
v36['Buffer'].append(4095)
v36['Buffer'].append(8190)
v36['Buffer'].append(254)
v36['Buffer'].append(5071)
v36['Buffer'].append(1)
v36['Buffer'].append(4091)
v36['Buffer'].append(60492)
v36['Buffer'].append(260)
v36['Buffer'].append(16383)
v36['Buffer'].append(8192)
v36['Buffer'].append(8194)
v36['Buffer'].append(53770)
v36['Buffer'].append(4096)
v36['Buffer'].append(259)
v36['Buffer'].append(58996)
v36['Buffer'].append(64782)
v36['Buffer'].append(6)
v36['Buffer'].append(8193)
v36['Buffer'].append(254)
v36['Buffer'].append(4090)
v36['Buffer'].append(250)
v36['Buffer'].append(47456)
v36['Buffer'].append(4091)
v36['Buffer'].append(3)
v36['Buffer'].append(65530)
v36['Buffer'].append(262)
v36['Buffer'].append(4099)
v36['Buffer'].append(65528)
v36['Buffer'].append(4)
v36['Buffer'].append(16389)
v36['Buffer'].append(16375)
v36['Buffer'].append(31215)
v36['Buffer'].append(16389)
v36['Buffer'].append(37530)
v36['Buffer'].append(16383)
v36['Buffer'].append(9052)
v36['Buffer'].append(60492)
v36['Buffer'].append(8186)
v36['Buffer'].append(260)
v36['Buffer'].append(4097)
v36['Buffer'].append(247)
v36['Buffer'].append(8194)
v36['Buffer'].append(8197)
v36['Buffer'].append(16387)
v36['Buffer'].append(8190)
v36['Buffer'].append(4089)
v36['Buffer'].append(4089)
v36['Buffer'].append(16386)
v36['Buffer'].append(55025)
v36['Buffer'].append(65528)
v36['Buffer'].append(37502)
v36['Buffer'].append(252)
v36['Buffer'].append(65527)
v36['Buffer'].append(65528)
v36['Buffer'].append(0)
v36['Buffer'].append(40895)
v36['Buffer'].append(59036)
v36['Buffer'].append(58555)
v36['Buffer'].append(4087)
v36['Buffer'].append(254)
v36['Buffer'].append(4102)
v36['Buffer'].append(260)
v36['Buffer'].append(253)
v36['Buffer'].append(37502)
v36['Buffer'].append(8193)
v36['Buffer'].append(63568)
v36['Buffer'].append(65527)
v36['Buffer'].append(5071)
v36['Buffer'].append(65530)
v36['Buffer'].append(4096)
v36['Buffer'].append(8188)
v36['Buffer'].append(34908)
v36['Buffer'].append(58996)
v36['Buffer'].append(4101)
v36['Buffer'].append(8195)
v36['Buffer'].append(16377)
v36['Buffer'].append(55844)
v36['Buffer'].append(65533)
v36['Buffer'].append(21186)
v36['Buffer'].append(16390)
v36['Buffer'].append(9899)
v36['Buffer'].append(21807)
v36['Buffer'].append(6)
v36['Buffer'].append(8198)
v36['Buffer'].append(48541)
v36['Buffer'].append(65532)
v36['Buffer'].append(4095)
v36['Buffer'].append(259)
v36['Buffer'].append(10898)
v36['Buffer'].append(16382)
v36['Buffer'].append(8186)
v36['Buffer'].append(16379)
v36['Buffer'].append(16384)
v36['Buffer'].append(20420)
v36['Buffer'].append(16601)
v36['Buffer'].append(20539)
v36['Buffer'].append(16381)
v36['Buffer'].append(40049)
v36['Buffer'].append(11546)
v36['Buffer'].append(7)
v36['Buffer'].append(60492)
v36['Buffer'].append(34908)
v36['Buffer'].append(65527)
v36['Buffer'].append(65533)
v36['Buffer'].append(64782)
v36['Buffer'].append(261)
v36['Buffer'].append(2)
v36['Buffer'].append(4100)
v36['Buffer'].append(257)
v36['Buffer'].append(32994)
v36['Buffer'].append(60492)
v36['Buffer'].append(8198)
v36['Buffer'].append(38975)
v36['Buffer'].append(31215)
v36['Buffer'].append(255)
v36['Buffer'].append(40049)
v36['Buffer'].append(16389)
v36['Buffer'].append(261)
v36['Buffer'].append(261)
v36['Buffer'].append(37530)
v36['Buffer'].append(256)
v36['Buffer'].append(4093)
v36['Buffer'].append(4089)
v36['Buffer'].append(53770)
v36['Buffer'].append(20420)
v36['Buffer'].append(256)
v36['Buffer'].append(36122)
v36['Buffer'].append(63568)
v36['Buffer'].append(4093)
v36['Buffer'].append(4098)
v36['Buffer'].append(19814)
v36['Buffer'].append(65530)
v36['Buffer'].append(10123)
v36['Buffer'].append(16389)
v36['Buffer'].append(16376)
v36['Buffer'].append(261)
v36['Buffer'].append(4092)
v36['Buffer'].append(38896)
v36['Buffer'].append(65531)
v36['Buffer'].append(4099)
v36['Buffer'].append(36072)
v36['Buffer'].append(4101)
v36['Buffer'].append(48397)
v36['Buffer'].append(8184)
v36['Buffer'].append(4)
v36['Buffer'].append(47456)
v36['Buffer'].append(16387)
v36['Buffer'].append(21807)
v36['Buffer'].append(55844)
v36['Buffer'].append(55025)
v36['Buffer'].append(4091)
v36['Buffer'].append(55844)
v36['Buffer'].append(4099)
v36['Buffer'].append(258)
v36['Buffer'].append(4102)
v36['Buffer'].append(258)
v36['Buffer'].append(4097)
v36['Buffer'].append(22736)
v36['Buffer'].append(251)
v36['Buffer'].append(65528)
v36['Buffer'].append(16377)
v36['Buffer'].append(260)
v36['Buffer'].append(8183)
v36['Buffer'].append(60746)
v36['Buffer'].append(8190)
v36['Buffer'].append(16386)
v36['Buffer'].append(4100)
v36['Buffer'].append(8198)
v36['Buffer'].append(16383)
v36['Buffer'].append(4102)
v36['Buffer'].append(31215)
v36['Buffer'].append(4090)
v36['Buffer'].append(48541)
v36['Buffer'].append(19814)
v36['Buffer'].append(8191)
v36['Buffer'].append(253)
v36['Buffer'].append(251)
v36['Buffer'].append(249)
v36['Buffer'].append(55025)
v36['Buffer'].append(53770)
v36['Buffer'].append(251)
v36['Buffer'].append(49383)
v36['Buffer'].append(254)
v36['Buffer'].append(256)
v36['Buffer'].append(47231)
v36['Buffer'].append(4092)
v36['Buffer'].append(60746)
v36['Buffer'].append(6)
v36['Buffer'].append(8196)
v36['Buffer'].append(20420)
v36['Buffer'].append(249)
v36['Buffer'].append(20539)



req = ElfrOpenELW()
req.UNCServerName = v18['UNCServerName']
req.ModuleName = v36
req.RegModuleName = v7['ModuleName']
req.MajorVersion = v3
req.MinorVersion = v17['MinorVersion']
try:
	v37 = dce.request(req)
except Exception as e:
	print('Error at: v37 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v21['ModuleName']
req.RegModuleName = v15['RegModuleName']
req.MajorVersion = v33['MinorVersion']
req.MinorVersion = v17['MinorVersion']
try:
	v38 = dce.request(req)
except Exception as e:
	print('Error at: v38 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v9['UNCServerName']
req.ModuleName = v18['RegModuleName']
req.RegModuleName = v21['ModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v37['MajorVersion']
try:
	v39 = dce.request(req)
except Exception as e:
	print('Error at: v39 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v28['UNCServerName']
req.ModuleName = v27['ModuleName']
req.RegModuleName = v22['RegModuleName']
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v9['MinorVersion']
try:
	v40 = dce.request(req)
except Exception as e:
	print('Error at: v40 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v9['BackupFileName']
req.RegModuleName = v29['ModuleName']
req.MajorVersion = v30['MinorVersion']
req.MinorVersion = v3
try:
	v41 = dce.request(req)
except Exception as e:
	print('Error at: v41 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v33['RegModuleName']
req.RegModuleName = v33['ModuleName']
req.MajorVersion = v13['MinorVersion']
req.MinorVersion = v20['MajorVersion']
try:
	v42 = dce.request(req)
except Exception as e:
	print('Error at: v42 failing with: ' + str(e))
	print(req.dump())

v43 = b'\xff\xfe-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00-\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenELW()
req.UNCServerName = v43
req.ModuleName = v12['ModuleName']
req.RegModuleName = v35['BackupFileName']
req.MajorVersion = v31['MajorVersion']
req.MinorVersion = v26['MinorVersion']
try:
	v44 = dce.request(req)
except Exception as e:
	print('Error at: v44 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v16['UNCServerName']
req.BackupFileName = v25['RegModuleName']
req.MajorVersion = v25['MinorVersion']
req.MinorVersion = v34['MajorVersion']
try:
	v45 = dce.request(req)
except Exception as e:
	print('Error at: v45 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v13['UNCServerName']
req.ModuleName = v28['RegModuleName']
req.RegModuleName = v40['RegModuleName']
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v34['MinorVersion']
try:
	v46 = dce.request(req)
except Exception as e:
	print('Error at: v46 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v29['UNCServerName']
req.ModuleName = v44['RegModuleName']
req.RegModuleName = v15['ModuleName']
req.MajorVersion = v25['MajorVersion']
req.MinorVersion = v34['MajorVersion']
try:
	v47 = dce.request(req)
except Exception as e:
	print('Error at: v47 failing with: ' + str(e))
	print(req.dump())

v48 = b'\xff\xfe*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenELW()
req.UNCServerName = v48
req.ModuleName = v26['RegModuleName']
req.RegModuleName = v47['ModuleName']
req.MajorVersion = v31['MajorVersion']
req.MinorVersion = v15['MinorVersion']
try:
	v49 = dce.request(req)
except Exception as e:
	print('Error at: v49 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v32['ModuleName']
req.RegModuleName = v41['RegModuleName']
req.MajorVersion = v22['MajorVersion']
req.MinorVersion = v32['MajorVersion']
try:
	v50 = dce.request(req)
except Exception as e:
	print('Error at: v50 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v13['ModuleName']
req.RegModuleName = v28['RegModuleName']
req.MajorVersion = v35['MajorVersion']
req.MinorVersion = v15['MinorVersion']
try:
	v51 = dce.request(req)
except Exception as e:
	print('Error at: v51 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v7['UNCServerName']
req.BackupFileName = v15['ModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v42['MinorVersion']
try:
	v52 = dce.request(req)
except Exception as e:
	print('Error at: v52 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v17['BackupFileName']
req.RegModuleName = v40['ModuleName']
req.MajorVersion = v9['MinorVersion']
req.MinorVersion = v17['MinorVersion']
try:
	v53 = dce.request(req)
except Exception as e:
	print('Error at: v53 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v31['UNCServerName']
req.ModuleName = v20['BackupFileName']
req.RegModuleName = v26['RegModuleName']
req.MajorVersion = v50['MinorVersion']
req.MinorVersion = v16['MajorVersion']
try:
	v54 = dce.request(req)
except Exception as e:
	print('Error at: v54 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v37['RegModuleName']
req.RegModuleName = v39['RegModuleName']
req.MajorVersion = v33['MajorVersion']
req.MinorVersion = v28['MajorVersion']
try:
	v55 = dce.request(req)
except Exception as e:
	print('Error at: v55 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v46['RegModuleName']
req.RegModuleName = v27['RegModuleName']
req.MajorVersion = v33['MajorVersion']
req.MinorVersion = v24['MinorVersion']
try:
	v56 = dce.request(req)
except Exception as e:
	print('Error at: v56 failing with: ' + str(e))
	print(req.dump())

v57 = RPC_STRING()
v57['Length'] = 22736
v57['MaximumLength'] = 4095
v57['Buffer'] = UC_CHAR_ARRAY()
v57['Buffer'].append(65)
v57['Buffer'].append(35)
v57['Buffer'].append(24)
v57['Buffer'].append(50)
v57['Buffer'].append(0)
v57['Buffer'].append(70)
v57['Buffer'].append(90)
v57['Buffer'].append(123)
v57['Buffer'].append(17)
v57['Buffer'].append(21)
v57['Buffer'].append(35)
v57['Buffer'].append(206)
v57['Buffer'].append(17)
v57['Buffer'].append(23)
v57['Buffer'].append(93)
v57['Buffer'].append(20)
v57['Buffer'].append(71)
v57['Buffer'].append(123)
v57['Buffer'].append(63)
v57['Buffer'].append(201)
v57['Buffer'].append(29)
v57['Buffer'].append(243)
v57['Buffer'].append(195)
v57['Buffer'].append(250)
v57['Buffer'].append(61)
v57['Buffer'].append(71)
v57['Buffer'].append(35)
v57['Buffer'].append(107)
v57['Buffer'].append(1)
v57['Buffer'].append(3)
v57['Buffer'].append(57)
v57['Buffer'].append(94)
v57['Buffer'].append(26)
v57['Buffer'].append(62)
v57['Buffer'].append(238)
v57['Buffer'].append(132)
v57['Buffer'].append(12)
v57['Buffer'].append(28)
v57['Buffer'].append(26)
v57['Buffer'].append(41)
v57['Buffer'].append(24)
v57['Buffer'].append(3)
v57['Buffer'].append(50)
v57['Buffer'].append(21)
v57['Buffer'].append(8)
v57['Buffer'].append(70)
v57['Buffer'].append(57)
v57['Buffer'].append(48)
v57['Buffer'].append(121)
v57['Buffer'].append(142)
v57['Buffer'].append(26)
v57['Buffer'].append(3)
v57['Buffer'].append(66)
v57['Buffer'].append(18)
v57['Buffer'].append(16)
v57['Buffer'].append(195)
v57['Buffer'].append(132)
v57['Buffer'].append(195)
v57['Buffer'].append(206)
v57['Buffer'].append(17)
v57['Buffer'].append(37)
v57['Buffer'].append(32)
v57['Buffer'].append(33)
v57['Buffer'].append(65)
v57['Buffer'].append(249)
v57['Buffer'].append(97)
v57['Buffer'].append(7)
v57['Buffer'].append(159)
v57['Buffer'].append(52)
v57['Buffer'].append(3)
v57['Buffer'].append(14)
v57['Buffer'].append(70)
v57['Buffer'].append(4)
v57['Buffer'].append(3)
v57['Buffer'].append(6)
v57['Buffer'].append(6)
v57['Buffer'].append(251)
v57['Buffer'].append(169)
v57['Buffer'].append(63)
v57['Buffer'].append(159)
v57['Buffer'].append(111)
v57['Buffer'].append(36)
v57['Buffer'].append(97)
v57['Buffer'].append(50)
v57['Buffer'].append(120)
v57['Buffer'].append(36)
v57['Buffer'].append(17)
v57['Buffer'].append(38)
v57['Buffer'].append(71)
v57['Buffer'].append(112)
v57['Buffer'].append(159)
v57['Buffer'].append(33)
v57['Buffer'].append(90)
v57['Buffer'].append(36)
v57['Buffer'].append(36)
v57['Buffer'].append(3)
v57['Buffer'].append(57)
v57['Buffer'].append(62)
v57['Buffer'].append(248)
v57['Buffer'].append(107)
v57['Buffer'].append(24)
v57['Buffer'].append(13)
v57['Buffer'].append(111)
v57['Buffer'].append(0)
v57['Buffer'].append(216)
v57['Buffer'].append(28)
v57['Buffer'].append(159)
v57['Buffer'].append(50)
v57['Buffer'].append(10)
v57['Buffer'].append(17)
v57['Buffer'].append(1)
v57['Buffer'].append(5)
v57['Buffer'].append(1)
v57['Buffer'].append(142)
v57['Buffer'].append(73)
v57['Buffer'].append(16)
v57['Buffer'].append(8)
v57['Buffer'].append(142)
v57['Buffer'].append(37)
v57['Buffer'].append(62)
v57['Buffer'].append(159)
v57['Buffer'].append(19)
v57['Buffer'].append(248)
v57['Buffer'].append(206)
v57['Buffer'].append(10)
v57['Buffer'].append(38)
v57['Buffer'].append(14)
v57['Buffer'].append(19)
v57['Buffer'].append(123)
v57['Buffer'].append(6)
v57['Buffer'].append(252)
v57['Buffer'].append(3)
v57['Buffer'].append(64)
v57['Buffer'].append(56)
v57['Buffer'].append(60)
v57['Buffer'].append(56)
v57['Buffer'].append(94)
v57['Buffer'].append(70)
v57['Buffer'].append(250)
v57['Buffer'].append(123)
v57['Buffer'].append(9)
v57['Buffer'].append(247)
v57['Buffer'].append(11)
v57['Buffer'].append(56)
v57['Buffer'].append(63)
v57['Buffer'].append(33)
v57['Buffer'].append(13)
v57['Buffer'].append(111)
v57['Buffer'].append(13)
v57['Buffer'].append(58)
v57['Buffer'].append(197)
v57['Buffer'].append(50)
v57['Buffer'].append(36)
v57['Buffer'].append(132)
v57['Buffer'].append(48)
v57['Buffer'].append(59)
v57['Buffer'].append(3)
v57['Buffer'].append(1)
v57['Buffer'].append(22)
v57['Buffer'].append(32)
v57['Buffer'].append(216)
v57['Buffer'].append(33)
v57['Buffer'].append(70)
v57['Buffer'].append(111)
v57['Buffer'].append(57)
v57['Buffer'].append(41)
v57['Buffer'].append(13)
v57['Buffer'].append(147)
v57['Buffer'].append(40)
v57['Buffer'].append(3)
v57['Buffer'].append(132)
v57['Buffer'].append(249)
v57['Buffer'].append(8)
v57['Buffer'].append(71)
v57['Buffer'].append(250)
v57['Buffer'].append(48)
v57['Buffer'].append(252)
v57['Buffer'].append(63)
v57['Buffer'].append(14)
v57['Buffer'].append(255)
v57['Buffer'].append(154)
v57['Buffer'].append(60)
v57['Buffer'].append(11)
v57['Buffer'].append(18)
v57['Buffer'].append(247)
v57['Buffer'].append(112)
v57['Buffer'].append(111)
v57['Buffer'].append(31)
v57['Buffer'].append(82)
v57['Buffer'].append(60)
v57['Buffer'].append(17)
v57['Buffer'].append(73)
v57['Buffer'].append(61)
v57['Buffer'].append(64)
v57['Buffer'].append(10)
v57['Buffer'].append(247)
v57['Buffer'].append(93)
v57['Buffer'].append(65)
v57['Buffer'].append(74)
v57['Buffer'].append(111)
v57['Buffer'].append(249)
v57['Buffer'].append(97)
v57['Buffer'].append(247)
v57['Buffer'].append(71)
v57['Buffer'].append(25)
v57['Buffer'].append(70)
v57['Buffer'].append(123)
v57['Buffer'].append(97)
v57['Buffer'].append(56)
v57['Buffer'].append(123)
v57['Buffer'].append(195)
v57['Buffer'].append(24)
v57['Buffer'].append(195)
v57['Buffer'].append(201)
v57['Buffer'].append(71)
v57['Buffer'].append(57)
v57['Buffer'].append(9)
v57['Buffer'].append(17)
v57['Buffer'].append(111)
v57['Buffer'].append(68)
v57['Buffer'].append(61)
v57['Buffer'].append(0)
v57['Buffer'].append(9)
v57['Buffer'].append(70)
v57['Buffer'].append(66)
v57['Buffer'].append(29)
v57['Buffer'].append(253)
v57['Buffer'].append(62)
v57['Buffer'].append(26)
v57['Buffer'].append(3)



req = ElfrOpenELA()
req.UNCServerName = v56['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v57
req.MajorVersion = v38['MinorVersion']
req.MinorVersion = v45['MinorVersion']
try:
	v58 = dce.request(req)
except Exception as e:
	print('Error at: v58 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v17['UNCServerName']
req.BackupFileName = v14['BackupFileName']
req.MajorVersion = v38['MinorVersion']
req.MinorVersion = v11['MajorVersion']
try:
	v59 = dce.request(req)
except Exception as e:
	print('Error at: v59 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v22['UNCServerName']
req.ModuleName = v58['ModuleName']
req.RegModuleName = v51['RegModuleName']
req.MajorVersion = v54['MajorVersion']
req.MinorVersion = v35['MinorVersion']
try:
	v60 = dce.request(req)
except Exception as e:
	print('Error at: v60 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v50['UNCServerName']
req.ModuleName = v7['RegModuleName']
req.RegModuleName = v6
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v20['MajorVersion']
try:
	v61 = dce.request(req)
except Exception as e:
	print('Error at: v61 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v30['UNCServerName']
req.ModuleName = v30['BackupFileName']
req.RegModuleName = v14['BackupFileName']
req.MajorVersion = v20['MinorVersion']
req.MinorVersion = v55['MinorVersion']
try:
	v62 = dce.request(req)
except Exception as e:
	print('Error at: v62 failing with: ' + str(e))
	print(req.dump())

v63 = 197124615

req = ElfrOpenBELW()
req.UNCServerName = v48
req.BackupFileName = v41['ModuleName']
req.MajorVersion = v63
req.MinorVersion = v15['MinorVersion']
try:
	v64 = dce.request(req)
except Exception as e:
	print('Error at: v64 failing with: ' + str(e))
	print(req.dump())

v65 = b'\xff\xfea\x00\x00\x00=\x00\x00\x00a\x00\x00\x00=\x00\x00\x00a\x00\x00\x00=\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenELW()
req.UNCServerName = v65
req.ModuleName = v55['RegModuleName']
req.RegModuleName = v25['ModuleName']
req.MajorVersion = v22['MinorVersion']
req.MinorVersion = v31['MajorVersion']
try:
	v66 = dce.request(req)
except Exception as e:
	print('Error at: v66 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v46['ModuleName']
req.RegModuleName = v28['ModuleName']
req.MajorVersion = v60['MinorVersion']
req.MinorVersion = v13['MajorVersion']
try:
	v67 = dce.request(req)
except Exception as e:
	print('Error at: v67 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v30['UNCServerName']
req.BackupFileName = v40['RegModuleName']
req.MajorVersion = v26['MajorVersion']
req.MinorVersion = v53['MinorVersion']
try:
	v68 = dce.request(req)
except Exception as e:
	print('Error at: v68 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v9['UNCServerName']
req.ModuleName = v52['BackupFileName']
req.RegModuleName = v50['RegModuleName']
req.MajorVersion = v9['MinorVersion']
req.MinorVersion = v62['MajorVersion']
try:
	v69 = dce.request(req)
except Exception as e:
	print('Error at: v69 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v35['UNCServerName']
req.ModuleName = v54['RegModuleName']
req.RegModuleName = v7['RegModuleName']
req.MajorVersion = v42['MinorVersion']
req.MinorVersion = v11['MajorVersion']
try:
	v70 = dce.request(req)
except Exception as e:
	print('Error at: v70 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v67['UNCServerName']
req.ModuleName = v60['RegModuleName']
req.RegModuleName = v10['ModuleName']
req.MajorVersion = v52['MajorVersion']
req.MinorVersion = v69['MinorVersion']
try:
	v71 = dce.request(req)
except Exception as e:
	print('Error at: v71 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v31['ModuleName']
req.MajorVersion = v71['MajorVersion']
req.MinorVersion = v26['MajorVersion']
try:
	v72 = dce.request(req)
except Exception as e:
	print('Error at: v72 failing with: ' + str(e))
	print(req.dump())

v73 = 4294967294

req = ElfrRegisterEventSourceA()
req.UNCServerName = v34['UNCServerName']
req.ModuleName = v68['BackupFileName']
req.RegModuleName = v27['ModuleName']
req.MajorVersion = v41['MinorVersion']
req.MinorVersion = v73
try:
	v74 = dce.request(req)
except Exception as e:
	print('Error at: v74 failing with: ' + str(e))
	print(req.dump())

v75 = RPC_UNICODE_STRING()
v75['Length'] = 55025
v75['MaximumLength'] = 8189
v75['Buffer'] = UC_WCHAR_ARRAY()
v75['Buffer'].append(248)
v75['Buffer'].append(4095)
v75['Buffer'].append(254)
v75['Buffer'].append(4092)
v75['Buffer'].append(58996)



req = ElfrOpenBELW()
req.UNCServerName = v72['UNCServerName']
req.BackupFileName = v75
req.MajorVersion = v46['MinorVersion']
req.MinorVersion = v21['MajorVersion']
try:
	v76 = dce.request(req)
except Exception as e:
	print('Error at: v76 failing with: ' + str(e))
	print(req.dump())

v77 = b'\xff\xfe"\x00"\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenBELA()
req.UNCServerName = v77
req.BackupFileName = v46['RegModuleName']
req.MajorVersion = v35['MajorVersion']
req.MinorVersion = v19['MajorVersion']
try:
	v78 = dce.request(req)
except Exception as e:
	print('Error at: v78 failing with: ' + str(e))
	print(req.dump())

v79 = RPC_UNICODE_STRING()
v79['Length'] = 4095
v79['MaximumLength'] = 32994
v79['Buffer'] = UC_WCHAR_ARRAY()
v79['Buffer'].append(255)
v79['Buffer'].append(40895)
v79['Buffer'].append(55025)
v79['Buffer'].append(16387)
v79['Buffer'].append(65532)
v79['Buffer'].append(36122)
v79['Buffer'].append(256)
v79['Buffer'].append(4)
v79['Buffer'].append(65533)
v79['Buffer'].append(31215)
v79['Buffer'].append(48397)
v79['Buffer'].append(37530)
v79['Buffer'].append(48397)
v79['Buffer'].append(248)
v79['Buffer'].append(4093)
v79['Buffer'].append(10123)
v79['Buffer'].append(4100)
v79['Buffer'].append(16389)
v79['Buffer'].append(65527)
v79['Buffer'].append(21807)
v79['Buffer'].append(16376)
v79['Buffer'].append(48397)
v79['Buffer'].append(4093)
v79['Buffer'].append(21807)
v79['Buffer'].append(251)
v79['Buffer'].append(260)
v79['Buffer'].append(9052)
v79['Buffer'].append(48397)
v79['Buffer'].append(48397)
v79['Buffer'].append(65534)
v79['Buffer'].append(251)
v79['Buffer'].append(8188)
v79['Buffer'].append(16601)
v79['Buffer'].append(6)
v79['Buffer'].append(65529)
v79['Buffer'].append(248)
v79['Buffer'].append(9899)
v79['Buffer'].append(53770)
v79['Buffer'].append(55844)
v79['Buffer'].append(64782)
v79['Buffer'].append(8192)
v79['Buffer'].append(4092)
v79['Buffer'].append(65534)
v79['Buffer'].append(48397)
v79['Buffer'].append(32994)
v79['Buffer'].append(258)
v79['Buffer'].append(4100)
v79['Buffer'].append(20539)
v79['Buffer'].append(4087)
v79['Buffer'].append(8195)
v79['Buffer'].append(4092)
v79['Buffer'].append(37530)
v79['Buffer'].append(21807)
v79['Buffer'].append(255)
v79['Buffer'].append(26238)
v79['Buffer'].append(20420)
v79['Buffer'].append(60492)
v79['Buffer'].append(22736)
v79['Buffer'].append(260)
v79['Buffer'].append(252)
v79['Buffer'].append(20539)
v79['Buffer'].append(60492)
v79['Buffer'].append(21186)
v79['Buffer'].append(260)
v79['Buffer'].append(255)
v79['Buffer'].append(257)
v79['Buffer'].append(16383)
v79['Buffer'].append(261)
v79['Buffer'].append(249)
v79['Buffer'].append(65527)
v79['Buffer'].append(16381)
v79['Buffer'].append(8198)
v79['Buffer'].append(19814)
v79['Buffer'].append(64782)
v79['Buffer'].append(8188)
v79['Buffer'].append(65533)
v79['Buffer'].append(16380)
v79['Buffer'].append(65532)
v79['Buffer'].append(8195)
v79['Buffer'].append(58555)
v79['Buffer'].append(63568)
v79['Buffer'].append(25696)
v79['Buffer'].append(38896)
v79['Buffer'].append(8185)
v79['Buffer'].append(55844)
v79['Buffer'].append(64661)
v79['Buffer'].append(250)
v79['Buffer'].append(22736)
v79['Buffer'].append(4088)
v79['Buffer'].append(34908)
v79['Buffer'].append(259)
v79['Buffer'].append(35278)
v79['Buffer'].append(55844)
v79['Buffer'].append(247)
v79['Buffer'].append(4100)
v79['Buffer'].append(49383)
v79['Buffer'].append(20539)
v79['Buffer'].append(255)
v79['Buffer'].append(65527)
v79['Buffer'].append(4092)
v79['Buffer'].append(260)
v79['Buffer'].append(5)
v79['Buffer'].append(49383)
v79['Buffer'].append(65534)
v79['Buffer'].append(38896)
v79['Buffer'].append(31215)
v79['Buffer'].append(4089)
v79['Buffer'].append(60746)
v79['Buffer'].append(20420)
v79['Buffer'].append(4100)
v79['Buffer'].append(16377)
v79['Buffer'].append(4097)
v79['Buffer'].append(47231)
v79['Buffer'].append(253)
v79['Buffer'].append(16377)
v79['Buffer'].append(258)
v79['Buffer'].append(8191)
v79['Buffer'].append(8196)
v79['Buffer'].append(19814)
v79['Buffer'].append(10123)
v79['Buffer'].append(21807)
v79['Buffer'].append(247)
v79['Buffer'].append(11546)
v79['Buffer'].append(4100)
v79['Buffer'].append(10123)
v79['Buffer'].append(252)
v79['Buffer'].append(60492)
v79['Buffer'].append(39155)
v79['Buffer'].append(48541)
v79['Buffer'].append(20420)
v79['Buffer'].append(17124)
v79['Buffer'].append(8188)
v79['Buffer'].append(22736)
v79['Buffer'].append(47231)
v79['Buffer'].append(16377)
v79['Buffer'].append(55025)
v79['Buffer'].append(8190)
v79['Buffer'].append(8189)
v79['Buffer'].append(9899)
v79['Buffer'].append(19814)
v79['Buffer'].append(8185)
v79['Buffer'].append(11546)
v79['Buffer'].append(252)
v79['Buffer'].append(16390)
v79['Buffer'].append(4093)
v79['Buffer'].append(9052)
v79['Buffer'].append(47456)
v79['Buffer'].append(4089)
v79['Buffer'].append(16377)
v79['Buffer'].append(257)
v79['Buffer'].append(16385)
v79['Buffer'].append(38896)
v79['Buffer'].append(258)
v79['Buffer'].append(58555)
v79['Buffer'].append(16377)
v79['Buffer'].append(58555)
v79['Buffer'].append(34908)
v79['Buffer'].append(34499)
v79['Buffer'].append(19814)
v79['Buffer'].append(8191)
v79['Buffer'].append(58996)
v79['Buffer'].append(9052)
v79['Buffer'].append(4096)
v79['Buffer'].append(7)
v79['Buffer'].append(8194)
v79['Buffer'].append(10123)
v79['Buffer'].append(257)
v79['Buffer'].append(40049)
v79['Buffer'].append(8198)
v79['Buffer'].append(8185)
v79['Buffer'].append(8196)
v79['Buffer'].append(256)
v79['Buffer'].append(49383)
v79['Buffer'].append(3)
v79['Buffer'].append(3)
v79['Buffer'].append(22736)
v79['Buffer'].append(261)
v79['Buffer'].append(251)
v79['Buffer'].append(16377)
v79['Buffer'].append(9899)
v79['Buffer'].append(36122)
v79['Buffer'].append(8183)
v79['Buffer'].append(36072)
v79['Buffer'].append(16386)
v79['Buffer'].append(4089)
v79['Buffer'].append(10123)
v79['Buffer'].append(38896)
v79['Buffer'].append(38896)
v79['Buffer'].append(8193)
v79['Buffer'].append(8183)
v79['Buffer'].append(4093)
v79['Buffer'].append(249)
v79['Buffer'].append(0)
v79['Buffer'].append(10123)
v79['Buffer'].append(20420)
v79['Buffer'].append(4098)
v79['Buffer'].append(4099)
v79['Buffer'].append(9052)
v79['Buffer'].append(36122)
v79['Buffer'].append(4090)
v79['Buffer'].append(4100)
v79['Buffer'].append(16381)
v79['Buffer'].append(48397)
v79['Buffer'].append(57556)
v79['Buffer'].append(26238)
v79['Buffer'].append(19814)
v79['Buffer'].append(65534)
v79['Buffer'].append(16388)
v79['Buffer'].append(4087)
v79['Buffer'].append(258)
v79['Buffer'].append(8194)
v79['Buffer'].append(8191)
v79['Buffer'].append(11509)
v79['Buffer'].append(4096)
v79['Buffer'].append(48397)
v79['Buffer'].append(11546)
v79['Buffer'].append(37502)
v79['Buffer'].append(5071)
v79['Buffer'].append(4098)
v79['Buffer'].append(19814)
v79['Buffer'].append(65528)
v79['Buffer'].append(20539)
v79['Buffer'].append(34499)
v79['Buffer'].append(250)
v79['Buffer'].append(65529)
v79['Buffer'].append(255)
v79['Buffer'].append(10123)
v79['Buffer'].append(22736)
v79['Buffer'].append(4092)
v79['Buffer'].append(17124)
v79['Buffer'].append(248)
v79['Buffer'].append(255)
v79['Buffer'].append(16380)
v79['Buffer'].append(17124)
v79['Buffer'].append(21807)
v79['Buffer'].append(37530)
v79['Buffer'].append(5)
v79['Buffer'].append(260)
v79['Buffer'].append(260)
v79['Buffer'].append(9899)
v79['Buffer'].append(11546)
v79['Buffer'].append(8190)
v79['Buffer'].append(255)
v79['Buffer'].append(8194)
v79['Buffer'].append(17124)
v79['Buffer'].append(16385)
v79['Buffer'].append(55025)



req = ElfrRegisterEventSourceW()
req.UNCServerName = v44['UNCServerName']
req.ModuleName = v79
req.RegModuleName = v49['ModuleName']
req.MajorVersion = v22['MinorVersion']
req.MinorVersion = v39['MinorVersion']
try:
	v80 = dce.request(req)
except Exception as e:
	print('Error at: v80 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELW()
req.UNCServerName = v26['UNCServerName']
req.BackupFileName = v35['BackupFileName']
req.MajorVersion = v47['MinorVersion']
req.MinorVersion = v56['MajorVersion']
try:
	v81 = dce.request(req)
except Exception as e:
	print('Error at: v81 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v33['UNCServerName']
req.ModuleName = v16['ModuleName']
req.RegModuleName = v55['ModuleName']
req.MajorVersion = v67['MinorVersion']
req.MinorVersion = v17['MajorVersion']
try:
	v82 = dce.request(req)
except Exception as e:
	print('Error at: v82 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v33['UNCServerName']
req.ModuleName = v11['BackupFileName']
req.RegModuleName = v69['RegModuleName']
req.MajorVersion = v29['MinorVersion']
req.MinorVersion = v61['MajorVersion']
try:
	v83 = dce.request(req)
except Exception as e:
	print('Error at: v83 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v10['UNCServerName']
req.BackupFileName = v59['BackupFileName']
req.MajorVersion = v18['MajorVersion']
req.MinorVersion = v58['MinorVersion']
try:
	v84 = dce.request(req)
except Exception as e:
	print('Error at: v84 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v58['UNCServerName']
req.ModuleName = v22['ModuleName']
req.RegModuleName = v78['BackupFileName']
req.MajorVersion = v82['MinorVersion']
req.MinorVersion = v34['MajorVersion']
try:
	v85 = dce.request(req)
except Exception as e:
	print('Error at: v85 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v30['UNCServerName']
req.ModuleName = v23
req.RegModuleName = v57
req.MajorVersion = v37['MajorVersion']
req.MinorVersion = v27['MinorVersion']
try:
	v86 = dce.request(req)
except Exception as e:
	print('Error at: v86 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v17['UNCServerName']
req.BackupFileName = v58['RegModuleName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v45['MajorVersion']
try:
	v87 = dce.request(req)
except Exception as e:
	print('Error at: v87 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v74['UNCServerName']
req.ModuleName = v56['ModuleName']
req.RegModuleName = v28['RegModuleName']
req.MajorVersion = v54['MinorVersion']
req.MinorVersion = v74['MajorVersion']
try:
	v88 = dce.request(req)
except Exception as e:
	print('Error at: v88 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v86['UNCServerName']
req.ModuleName = v10['ModuleName']
req.RegModuleName = v71['RegModuleName']
req.MajorVersion = v72['MajorVersion']
req.MinorVersion = v26['MinorVersion']
try:
	v89 = dce.request(req)
except Exception as e:
	print('Error at: v89 failing with: ' + str(e))
	print(req.dump())

v90 = 359266861

req = ElfrRegisterEventSourceA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v57
req.RegModuleName = v51['ModuleName']
req.MajorVersion = v64['MajorVersion']
req.MinorVersion = v90
try:
	v91 = dce.request(req)
except Exception as e:
	print('Error at: v91 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v49['UNCServerName']
req.ModuleName = v26['RegModuleName']
req.RegModuleName = v61['RegModuleName']
req.MajorVersion = v10['MajorVersion']
req.MinorVersion = v56['MajorVersion']
try:
	v92 = dce.request(req)
except Exception as e:
	print('Error at: v92 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v74['UNCServerName']
req.BackupFileName = v67['ModuleName']
req.MajorVersion = v49['MinorVersion']
req.MinorVersion = v10['MinorVersion']
try:
	v93 = dce.request(req)
except Exception as e:
	print('Error at: v93 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v80['UNCServerName']
req.ModuleName = v76['BackupFileName']
req.RegModuleName = v7['RegModuleName']
req.MajorVersion = v30['MajorVersion']
req.MinorVersion = v84['MajorVersion']
try:
	v94 = dce.request(req)
except Exception as e:
	print('Error at: v94 failing with: ' + str(e))
	print(req.dump())

v95 = RPC_STRING()
v95['Length'] = 48397
v95['MaximumLength'] = 16378
v95['Buffer'] = UC_CHAR_ARRAY()
v95['Buffer'].append(63)
v95['Buffer'].append(71)
v95['Buffer'].append(93)
v95['Buffer'].append(11)
v95['Buffer'].append(195)
v95['Buffer'].append(15)
v95['Buffer'].append(73)
v95['Buffer'].append(6)
v95['Buffer'].append(247)
v95['Buffer'].append(29)
v95['Buffer'].append(111)
v95['Buffer'].append(63)
v95['Buffer'].append(60)
v95['Buffer'].append(205)
v95['Buffer'].append(50)
v95['Buffer'].append(50)
v95['Buffer'].append(159)
v95['Buffer'].append(16)
v95['Buffer'].append(29)
v95['Buffer'].append(52)
v95['Buffer'].append(13)
v95['Buffer'].append(21)
v95['Buffer'].append(64)
v95['Buffer'].append(93)
v95['Buffer'].append(107)
v95['Buffer'].append(17)
v95['Buffer'].append(15)
v95['Buffer'].append(66)
v95['Buffer'].append(120)
v95['Buffer'].append(17)
v95['Buffer'].append(50)
v95['Buffer'].append(142)
v95['Buffer'].append(93)
v95['Buffer'].append(197)
v95['Buffer'].append(10)
v95['Buffer'].append(252)
v95['Buffer'].append(13)
v95['Buffer'].append(70)
v95['Buffer'].append(111)
v95['Buffer'].append(90)
v95['Buffer'].append(61)
v95['Buffer'].append(6)
v95['Buffer'].append(132)
v95['Buffer'].append(71)
v95['Buffer'].append(250)
v95['Buffer'].append(238)
v95['Buffer'].append(18)
v95['Buffer'].append(254)
v95['Buffer'].append(17)
v95['Buffer'].append(1)
v95['Buffer'].append(71)
v95['Buffer'].append(132)
v95['Buffer'].append(7)
v95['Buffer'].append(8)
v95['Buffer'].append(250)
v95['Buffer'].append(195)
v95['Buffer'].append(82)
v95['Buffer'].append(66)
v95['Buffer'].append(147)
v95['Buffer'].append(197)
v95['Buffer'].append(247)
v95['Buffer'].append(55)
v95['Buffer'].append(16)
v95['Buffer'].append(27)
v95['Buffer'].append(71)
v95['Buffer'].append(90)
v95['Buffer'].append(0)
v95['Buffer'].append(56)
v95['Buffer'].append(17)
v95['Buffer'].append(41)
v95['Buffer'].append(147)
v95['Buffer'].append(62)
v95['Buffer'].append(6)
v95['Buffer'].append(111)
v95['Buffer'].append(132)
v95['Buffer'].append(252)
v95['Buffer'].append(142)
v95['Buffer'].append(62)
v95['Buffer'].append(0)
v95['Buffer'].append(254)
v95['Buffer'].append(7)
v95['Buffer'].append(237)
v95['Buffer'].append(33)
v95['Buffer'].append(0)
v95['Buffer'].append(67)
v95['Buffer'].append(25)
v95['Buffer'].append(50)
v95['Buffer'].append(123)
v95['Buffer'].append(32)
v95['Buffer'].append(28)
v95['Buffer'].append(250)
v95['Buffer'].append(36)
v95['Buffer'].append(70)
v95['Buffer'].append(64)
v95['Buffer'].append(25)
v95['Buffer'].append(65)
v95['Buffer'].append(123)
v95['Buffer'].append(15)
v95['Buffer'].append(3)
v95['Buffer'].append(2)
v95['Buffer'].append(248)
v95['Buffer'].append(70)
v95['Buffer'].append(29)
v95['Buffer'].append(250)
v95['Buffer'].append(22)
v95['Buffer'].append(201)
v95['Buffer'].append(142)
v95['Buffer'].append(63)
v95['Buffer'].append(3)
v95['Buffer'].append(25)
v95['Buffer'].append(27)
v95['Buffer'].append(58)
v95['Buffer'].append(121)
v95['Buffer'].append(14)
v95['Buffer'].append(250)
v95['Buffer'].append(30)
v95['Buffer'].append(248)
v95['Buffer'].append(56)
v95['Buffer'].append(48)
v95['Buffer'].append(14)
v95['Buffer'].append(68)
v95['Buffer'].append(107)
v95['Buffer'].append(17)
v95['Buffer'].append(23)
v95['Buffer'].append(58)
v95['Buffer'].append(251)
v95['Buffer'].append(93)
v95['Buffer'].append(26)
v95['Buffer'].append(248)
v95['Buffer'].append(237)
v95['Buffer'].append(40)
v95['Buffer'].append(7)
v95['Buffer'].append(250)
v95['Buffer'].append(216)
v95['Buffer'].append(254)
v95['Buffer'].append(205)
v95['Buffer'].append(25)
v95['Buffer'].append(237)
v95['Buffer'].append(57)
v95['Buffer'].append(111)
v95['Buffer'].append(252)
v95['Buffer'].append(7)
v95['Buffer'].append(159)
v95['Buffer'].append(111)
v95['Buffer'].append(248)
v95['Buffer'].append(68)
v95['Buffer'].append(1)
v95['Buffer'].append(59)
v95['Buffer'].append(255)
v95['Buffer'].append(6)
v95['Buffer'].append(63)
v95['Buffer'].append(201)
v95['Buffer'].append(142)
v95['Buffer'].append(123)
v95['Buffer'].append(16)
v95['Buffer'].append(238)
v95['Buffer'].append(57)
v95['Buffer'].append(58)
v95['Buffer'].append(250)
v95['Buffer'].append(94)
v95['Buffer'].append(93)
v95['Buffer'].append(12)
v95['Buffer'].append(24)
v95['Buffer'].append(17)
v95['Buffer'].append(10)
v95['Buffer'].append(32)
v95['Buffer'].append(3)
v95['Buffer'].append(19)
v95['Buffer'].append(132)
v95['Buffer'].append(24)
v95['Buffer'].append(18)
v95['Buffer'].append(33)
v95['Buffer'].append(82)
v95['Buffer'].append(29)
v95['Buffer'].append(15)
v95['Buffer'].append(74)
v95['Buffer'].append(18)
v95['Buffer'].append(9)
v95['Buffer'].append(25)
v95['Buffer'].append(18)
v95['Buffer'].append(112)
v95['Buffer'].append(159)
v95['Buffer'].append(94)
v95['Buffer'].append(123)
v95['Buffer'].append(57)
v95['Buffer'].append(3)
v95['Buffer'].append(28)
v95['Buffer'].append(52)
v95['Buffer'].append(3)
v95['Buffer'].append(19)
v95['Buffer'].append(82)
v95['Buffer'].append(237)
v95['Buffer'].append(11)
v95['Buffer'].append(111)
v95['Buffer'].append(10)
v95['Buffer'].append(9)
v95['Buffer'].append(56)
v95['Buffer'].append(112)
v95['Buffer'].append(111)
v95['Buffer'].append(18)
v95['Buffer'].append(12)
v95['Buffer'].append(62)
v95['Buffer'].append(112)
v95['Buffer'].append(70)
v95['Buffer'].append(0)
v95['Buffer'].append(70)
v95['Buffer'].append(32)
v95['Buffer'].append(48)
v95['Buffer'].append(35)
v95['Buffer'].append(123)
v95['Buffer'].append(41)
v95['Buffer'].append(201)
v95['Buffer'].append(6)
v95['Buffer'].append(15)
v95['Buffer'].append(25)
v95['Buffer'].append(90)
v95['Buffer'].append(243)
v95['Buffer'].append(31)
v95['Buffer'].append(250)
v95['Buffer'].append(32)
v95['Buffer'].append(15)
v95['Buffer'].append(48)
v95['Buffer'].append(71)
v95['Buffer'].append(13)
v95['Buffer'].append(19)
v95['Buffer'].append(112)
v95['Buffer'].append(62)
v95['Buffer'].append(29)
v95['Buffer'].append(251)
v95['Buffer'].append(11)
v95['Buffer'].append(70)
v95['Buffer'].append(13)
v95['Buffer'].append(249)
v95['Buffer'].append(55)
v95['Buffer'].append(59)
v95['Buffer'].append(248)
v95['Buffer'].append(201)
v95['Buffer'].append(238)
v95['Buffer'].append(7)
v95['Buffer'].append(159)
v95['Buffer'].append(48)
v95['Buffer'].append(19)
v95['Buffer'].append(82)
v95['Buffer'].append(14)
v95['Buffer'].append(32)
v95['Buffer'].append(29)
v95['Buffer'].append(59)



req = ElfrOpenELA()
req.UNCServerName = v34['UNCServerName']
req.ModuleName = v95
req.RegModuleName = v24['RegModuleName']
req.MajorVersion = v82['MinorVersion']
req.MinorVersion = v15['MinorVersion']
try:
	v96 = dce.request(req)
except Exception as e:
	print('Error at: v96 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v77
req.ModuleName = v59['BackupFileName']
req.RegModuleName = v96['RegModuleName']
req.MajorVersion = v63
req.MinorVersion = v39['MinorVersion']
try:
	v97 = dce.request(req)
except Exception as e:
	print('Error at: v97 failing with: ' + str(e))
	print(req.dump())

v98 = 3657043599

req = ElfrOpenELW()
req.UNCServerName = v72['UNCServerName']
req.ModuleName = v42['RegModuleName']
req.RegModuleName = v15['RegModuleName']
req.MajorVersion = v98
req.MinorVersion = v40['MajorVersion']
try:
	v99 = dce.request(req)
except Exception as e:
	print('Error at: v99 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v67['UNCServerName']
req.ModuleName = v84['BackupFileName']
req.RegModuleName = v62['RegModuleName']
req.MajorVersion = v26['MinorVersion']
req.MinorVersion = v7['MajorVersion']
try:
	v100 = dce.request(req)
except Exception as e:
	print('Error at: v100 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v87['UNCServerName']
req.ModuleName = v34['BackupFileName']
req.RegModuleName = v58['ModuleName']
req.MajorVersion = v82['MinorVersion']
req.MinorVersion = v52['MinorVersion']
try:
	v101 = dce.request(req)
except Exception as e:
	print('Error at: v101 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v22['UNCServerName']
req.BackupFileName = v62['RegModuleName']
req.MajorVersion = v54['MajorVersion']
req.MinorVersion = v100['MinorVersion']
try:
	v102 = dce.request(req)
except Exception as e:
	print('Error at: v102 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELA()
req.UNCServerName = v85['UNCServerName']
req.ModuleName = v28['RegModuleName']
req.RegModuleName = v84['BackupFileName']
req.MajorVersion = v14['MinorVersion']
req.MinorVersion = v62['MinorVersion']
try:
	v103 = dce.request(req)
except Exception as e:
	print('Error at: v103 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v31['UNCServerName']
req.ModuleName = v33['ModuleName']
req.RegModuleName = v20['BackupFileName']
req.MajorVersion = v69['MajorVersion']
req.MinorVersion = v94['MajorVersion']
try:
	v104 = dce.request(req)
except Exception as e:
	print('Error at: v104 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v62['UNCServerName']
req.BackupFileName = v95
req.MajorVersion = v31['MajorVersion']
req.MinorVersion = v27['MinorVersion']
try:
	v105 = dce.request(req)
except Exception as e:
	print('Error at: v105 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v38['UNCServerName']
req.ModuleName = v26['RegModuleName']
req.RegModuleName = v26['ModuleName']
req.MajorVersion = v91['MinorVersion']
req.MinorVersion = v33['MajorVersion']
try:
	v106 = dce.request(req)
except Exception as e:
	print('Error at: v106 failing with: ' + str(e))
	print(req.dump())

v107 = b'\xff\xfe}\x00}\x00}\x00\x00\x00'.decode('utf-16')

req = ElfrOpenBELA()
req.UNCServerName = v107
req.BackupFileName = v105['BackupFileName']
req.MajorVersion = v83['MinorVersion']
req.MinorVersion = v4['MinorVersion']
try:
	v108 = dce.request(req)
except Exception as e:
	print('Error at: v108 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v54['UNCServerName']
req.ModuleName = v79
req.RegModuleName = v92['ModuleName']
req.MajorVersion = v68['MajorVersion']
req.MinorVersion = v47['MinorVersion']
try:
	v109 = dce.request(req)
except Exception as e:
	print('Error at: v109 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v27['UNCServerName']
req.ModuleName = v23
req.RegModuleName = v62['RegModuleName']
req.MajorVersion = v15['MajorVersion']
req.MinorVersion = v10['MinorVersion']
try:
	v110 = dce.request(req)
except Exception as e:
	print('Error at: v110 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v50['UNCServerName']
req.ModuleName = v41['RegModuleName']
req.RegModuleName = v64['BackupFileName']
req.MajorVersion = v42['MajorVersion']
req.MinorVersion = v81['MajorVersion']
try:
	v111 = dce.request(req)
except Exception as e:
	print('Error at: v111 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v24['UNCServerName']
req.BackupFileName = v89['RegModuleName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v109['MajorVersion']
try:
	v112 = dce.request(req)
except Exception as e:
	print('Error at: v112 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v71['UNCServerName']
req.BackupFileName = v4['BackupFileName']
req.MajorVersion = v92['MajorVersion']
req.MinorVersion = v69['MajorVersion']
try:
	v113 = dce.request(req)
except Exception as e:
	print('Error at: v113 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v93['UNCServerName']
req.ModuleName = v24['RegModuleName']
req.RegModuleName = v62['RegModuleName']
req.MajorVersion = v28['MajorVersion']
req.MinorVersion = v26['MinorVersion']
try:
	v114 = dce.request(req)
except Exception as e:
	print('Error at: v114 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v81['UNCServerName']
req.ModuleName = v104['RegModuleName']
req.RegModuleName = v9['BackupFileName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v84['MajorVersion']
try:
	v115 = dce.request(req)
except Exception as e:
	print('Error at: v115 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v44['UNCServerName']
req.ModuleName = v33['RegModuleName']
req.RegModuleName = v70['RegModuleName']
req.MajorVersion = v81['MinorVersion']
req.MinorVersion = v29['MinorVersion']
try:
	v116 = dce.request(req)
except Exception as e:
	print('Error at: v116 failing with: ' + str(e))
	print(req.dump())

v117 = RPC_UNICODE_STRING()
v117['Length'] = 34499
v117['MaximumLength'] = 16386
v117['Buffer'] = UC_WCHAR_ARRAY()
v117['Buffer'].append(5)
v117['Buffer'].append(4092)
v117['Buffer'].append(60492)
v117['Buffer'].append(65533)
v117['Buffer'].append(3)
v117['Buffer'].append(60746)
v117['Buffer'].append(11546)
v117['Buffer'].append(58996)
v117['Buffer'].append(8184)
v117['Buffer'].append(35278)
v117['Buffer'].append(8196)
v117['Buffer'].append(6)
v117['Buffer'].append(21186)
v117['Buffer'].append(16389)
v117['Buffer'].append(65528)
v117['Buffer'].append(16377)
v117['Buffer'].append(4089)
v117['Buffer'].append(2)
v117['Buffer'].append(4094)
v117['Buffer'].append(16387)
v117['Buffer'].append(49383)
v117['Buffer'].append(37530)
v117['Buffer'].append(8192)
v117['Buffer'].append(16386)
v117['Buffer'].append(4097)
v117['Buffer'].append(5)
v117['Buffer'].append(8187)
v117['Buffer'].append(252)
v117['Buffer'].append(20539)
v117['Buffer'].append(16390)
v117['Buffer'].append(0)
v117['Buffer'].append(261)
v117['Buffer'].append(10123)
v117['Buffer'].append(19814)
v117['Buffer'].append(11546)
v117['Buffer'].append(261)
v117['Buffer'].append(4)
v117['Buffer'].append(16379)
v117['Buffer'].append(35278)
v117['Buffer'].append(8194)
v117['Buffer'].append(16382)
v117['Buffer'].append(4098)
v117['Buffer'].append(65530)
v117['Buffer'].append(16376)
v117['Buffer'].append(58996)
v117['Buffer'].append(22736)
v117['Buffer'].append(60492)
v117['Buffer'].append(39155)
v117['Buffer'].append(8190)
v117['Buffer'].append(36122)
v117['Buffer'].append(8186)
v117['Buffer'].append(16389)
v117['Buffer'].append(4100)
v117['Buffer'].append(55844)
v117['Buffer'].append(4091)
v117['Buffer'].append(21186)
v117['Buffer'].append(4)
v117['Buffer'].append(247)
v117['Buffer'].append(8198)
v117['Buffer'].append(16390)
v117['Buffer'].append(16385)
v117['Buffer'].append(60746)
v117['Buffer'].append(0)
v117['Buffer'].append(16388)
v117['Buffer'].append(8193)
v117['Buffer'].append(22736)
v117['Buffer'].append(8197)
v117['Buffer'].append(22736)
v117['Buffer'].append(8187)
v117['Buffer'].append(36122)
v117['Buffer'].append(4088)
v117['Buffer'].append(9899)
v117['Buffer'].append(8190)
v117['Buffer'].append(37530)
v117['Buffer'].append(5)
v117['Buffer'].append(8192)
v117['Buffer'].append(63568)
v117['Buffer'].append(16390)
v117['Buffer'].append(4097)
v117['Buffer'].append(248)
v117['Buffer'].append(34499)
v117['Buffer'].append(4091)
v117['Buffer'].append(254)
v117['Buffer'].append(4087)
v117['Buffer'].append(60492)
v117['Buffer'].append(4099)
v117['Buffer'].append(37530)
v117['Buffer'].append(16390)
v117['Buffer'].append(59036)
v117['Buffer'].append(8187)
v117['Buffer'].append(4094)
v117['Buffer'].append(16376)
v117['Buffer'].append(55844)
v117['Buffer'].append(8189)
v117['Buffer'].append(21807)
v117['Buffer'].append(16375)
v117['Buffer'].append(16385)
v117['Buffer'].append(58555)
v117['Buffer'].append(1)
v117['Buffer'].append(64661)
v117['Buffer'].append(47231)
v117['Buffer'].append(39155)
v117['Buffer'].append(254)
v117['Buffer'].append(8190)
v117['Buffer'].append(26238)
v117['Buffer'].append(4089)
v117['Buffer'].append(16378)
v117['Buffer'].append(65528)
v117['Buffer'].append(250)
v117['Buffer'].append(53770)
v117['Buffer'].append(11546)
v117['Buffer'].append(262)
v117['Buffer'].append(10898)
v117['Buffer'].append(64661)
v117['Buffer'].append(65530)
v117['Buffer'].append(252)
v117['Buffer'].append(60746)
v117['Buffer'].append(8185)
v117['Buffer'].append(34908)
v117['Buffer'].append(8192)
v117['Buffer'].append(59036)
v117['Buffer'].append(8189)
v117['Buffer'].append(36072)
v117['Buffer'].append(16381)
v117['Buffer'].append(255)
v117['Buffer'].append(25696)
v117['Buffer'].append(16382)
v117['Buffer'].append(8186)
v117['Buffer'].append(4093)
v117['Buffer'].append(2)
v117['Buffer'].append(55844)
v117['Buffer'].append(8189)
v117['Buffer'].append(64782)
v117['Buffer'].append(64782)
v117['Buffer'].append(21186)
v117['Buffer'].append(8198)
v117['Buffer'].append(5071)
v117['Buffer'].append(65534)
v117['Buffer'].append(38896)
v117['Buffer'].append(10898)
v117['Buffer'].append(9899)
v117['Buffer'].append(35278)
v117['Buffer'].append(11546)
v117['Buffer'].append(11546)
v117['Buffer'].append(8197)
v117['Buffer'].append(259)
v117['Buffer'].append(248)
v117['Buffer'].append(250)
v117['Buffer'].append(47456)
v117['Buffer'].append(16382)
v117['Buffer'].append(256)
v117['Buffer'].append(48397)
v117['Buffer'].append(0)
v117['Buffer'].append(11546)
v117['Buffer'].append(253)
v117['Buffer'].append(20539)
v117['Buffer'].append(37530)
v117['Buffer'].append(26238)
v117['Buffer'].append(16378)
v117['Buffer'].append(5)
v117['Buffer'].append(16379)
v117['Buffer'].append(258)
v117['Buffer'].append(16375)
v117['Buffer'].append(8184)
v117['Buffer'].append(4095)
v117['Buffer'].append(16383)
v117['Buffer'].append(60746)
v117['Buffer'].append(55025)
v117['Buffer'].append(59036)
v117['Buffer'].append(55844)
v117['Buffer'].append(4)
v117['Buffer'].append(16377)
v117['Buffer'].append(5)
v117['Buffer'].append(8190)
v117['Buffer'].append(16381)
v117['Buffer'].append(8184)
v117['Buffer'].append(65528)
v117['Buffer'].append(8191)
v117['Buffer'].append(2)
v117['Buffer'].append(16390)
v117['Buffer'].append(261)
v117['Buffer'].append(16388)
v117['Buffer'].append(9899)
v117['Buffer'].append(34499)
v117['Buffer'].append(248)
v117['Buffer'].append(16386)
v117['Buffer'].append(16385)
v117['Buffer'].append(16386)
v117['Buffer'].append(16380)
v117['Buffer'].append(58555)
v117['Buffer'].append(8185)
v117['Buffer'].append(16381)
v117['Buffer'].append(40895)
v117['Buffer'].append(16377)
v117['Buffer'].append(25696)
v117['Buffer'].append(40049)
v117['Buffer'].append(16390)
v117['Buffer'].append(16389)
v117['Buffer'].append(16380)
v117['Buffer'].append(252)
v117['Buffer'].append(4100)
v117['Buffer'].append(8185)



req = ElfrOpenBELW()
req.UNCServerName = v38['UNCServerName']
req.BackupFileName = v117
req.MajorVersion = v20['MajorVersion']
req.MinorVersion = v58['MinorVersion']
try:
	v118 = dce.request(req)
except Exception as e:
	print('Error at: v118 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceW()
req.UNCServerName = v32['UNCServerName']
req.ModuleName = v54['ModuleName']
req.RegModuleName = v18['ModuleName']
req.MajorVersion = v111['MajorVersion']
req.MinorVersion = v19['MajorVersion']
try:
	v119 = dce.request(req)
except Exception as e:
	print('Error at: v119 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenBELA()
req.UNCServerName = v85['UNCServerName']
req.BackupFileName = v10['ModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v93['MinorVersion']
try:
	v120 = dce.request(req)
except Exception as e:
	print('Error at: v120 failing with: ' + str(e))
	print(req.dump())

req = ElfrRegisterEventSourceA()
req.UNCServerName = v107
req.ModuleName = v62['RegModuleName']
req.RegModuleName = v97['ModuleName']
req.MajorVersion = v78['MinorVersion']
req.MinorVersion = v50['MajorVersion']
try:
	v121 = dce.request(req)
except Exception as e:
	print('Error at: v121 failing with: ' + str(e))
	print(req.dump())

req = ElfrOpenELW()
req.UNCServerName = v54['UNCServerName']
req.ModuleName = v94['ModuleName']
req.RegModuleName = v82['ModuleName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v42['MinorVersion']
try:
	v122 = dce.request(req)
except Exception as e:
	print('Error at: v122 failing with: ' + str(e))
	print(req.dump())

