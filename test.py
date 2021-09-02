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

v1 = b'\xff\xfe)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00)\x00\x00\x00\x00\x00'.decode('utf-16')

v2 = RPC_STRING()
v2['Length'] = 19605
v2['MaximumLength'] = 16382
v2['Buffer'] = UC_CHAR_ARRAY()
v2['Buffer'].append(93)
v2['Buffer'].append(219)
v2['Buffer'].append(152)
v2['Buffer'].append(31)



v3 = 2147483647

req = ElfrOpenELA()
req.UNCServerName = v1
req.ModuleName = v2
req.RegModuleName = v2
req.MajorVersion = v3
req.MinorVersion = v3
v4 = dce.request(req)

v5 = b'\xff\xfe>\x00\x00\x00>\x00\x00\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

v6 = RPC_UNICODE_STRING()
v6['Length'] = 59445
v6['MaximumLength'] = 16382
v6['Buffer'] = UC_WCHAR_ARRAY()
v6['Buffer'].append(256)
v6['Buffer'].append(8183)
v6['Buffer'].append(4096)
v6['Buffer'].append(259)
v6['Buffer'].append(3)
v6['Buffer'].append(16384)
v6['Buffer'].append(258)
v6['Buffer'].append(8193)



req = ElfrOpenBELW()
req.UNCServerName = v5
req.BackupFileName = v6
req.MajorVersion = v3
req.MinorVersion = v4['MajorVersion']
v7 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v2
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v7['MinorVersion']
v8 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v2
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v3
v9 = dce.request(req)

v10 = RPC_STRING()
v10['Length'] = 4092
v10['MaximumLength'] = 16386
v10['Buffer'] = UC_CHAR_ARRAY()
v10['Buffer'].append(126)
v10['Buffer'].append(24)
v10['Buffer'].append(254)
v10['Buffer'].append(115)
v10['Buffer'].append(26)
v10['Buffer'].append(253)
v10['Buffer'].append(12)
v10['Buffer'].append(32)
v10['Buffer'].append(5)
v10['Buffer'].append(12)
v10['Buffer'].append(3)
v10['Buffer'].append(26)
v10['Buffer'].append(4)
v10['Buffer'].append(57)
v10['Buffer'].append(180)
v10['Buffer'].append(29)
v10['Buffer'].append(33)
v10['Buffer'].append(66)
v10['Buffer'].append(212)
v10['Buffer'].append(89)
v10['Buffer'].append(59)
v10['Buffer'].append(253)
v10['Buffer'].append(67)
v10['Buffer'].append(30)
v10['Buffer'].append(150)
v10['Buffer'].append(88)
v10['Buffer'].append(195)
v10['Buffer'].append(11)
v10['Buffer'].append(126)
v10['Buffer'].append(169)
v10['Buffer'].append(101)
v10['Buffer'].append(38)
v10['Buffer'].append(248)
v10['Buffer'].append(4)
v10['Buffer'].append(208)
v10['Buffer'].append(17)
v10['Buffer'].append(247)
v10['Buffer'].append(6)
v10['Buffer'].append(82)
v10['Buffer'].append(57)
v10['Buffer'].append(157)
v10['Buffer'].append(5)
v10['Buffer'].append(230)
v10['Buffer'].append(101)
v10['Buffer'].append(35)
v10['Buffer'].append(58)
v10['Buffer'].append(19)
v10['Buffer'].append(63)
v10['Buffer'].append(171)
v10['Buffer'].append(30)
v10['Buffer'].append(212)
v10['Buffer'].append(58)
v10['Buffer'].append(98)
v10['Buffer'].append(27)
v10['Buffer'].append(83)
v10['Buffer'].append(5)
v10['Buffer'].append(48)
v10['Buffer'].append(61)
v10['Buffer'].append(0)
v10['Buffer'].append(20)
v10['Buffer'].append(48)
v10['Buffer'].append(28)
v10['Buffer'].append(113)
v10['Buffer'].append(25)
v10['Buffer'].append(35)
v10['Buffer'].append(169)
v10['Buffer'].append(21)
v10['Buffer'].append(169)
v10['Buffer'].append(65)
v10['Buffer'].append(16)
v10['Buffer'].append(191)
v10['Buffer'].append(69)
v10['Buffer'].append(212)
v10['Buffer'].append(36)
v10['Buffer'].append(222)
v10['Buffer'].append(3)
v10['Buffer'].append(15)
v10['Buffer'].append(115)
v10['Buffer'].append(4)
v10['Buffer'].append(83)
v10['Buffer'].append(196)
v10['Buffer'].append(25)
v10['Buffer'].append(76)
v10['Buffer'].append(252)
v10['Buffer'].append(56)
v10['Buffer'].append(26)
v10['Buffer'].append(8)
v10['Buffer'].append(69)
v10['Buffer'].append(133)
v10['Buffer'].append(88)
v10['Buffer'].append(171)
v10['Buffer'].append(98)
v10['Buffer'].append(246)
v10['Buffer'].append(7)
v10['Buffer'].append(0)
v10['Buffer'].append(219)
v10['Buffer'].append(31)
v10['Buffer'].append(133)
v10['Buffer'].append(0)
v10['Buffer'].append(27)
v10['Buffer'].append(1)
v10['Buffer'].append(23)
v10['Buffer'].append(180)



req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v8['BackupFileName']
req.RegModuleName = v10
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v4['MinorVersion']
v11 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v5
req.ModuleName = v6
req.RegModuleName = v6
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v9['MinorVersion']
v12 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v12['ModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v7['MinorVersion']
v13 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v13['BackupFileName']
req.RegModuleName = v12['ModuleName']
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v9['MajorVersion']
v14 = dce.request(req)

v15 = RPC_UNICODE_STRING()
v15['Length'] = 56186
v15['MaximumLength'] = 259
v15['Buffer'] = UC_WCHAR_ARRAY()
v15['Buffer'].append(255)
v15['Buffer'].append(260)
v15['Buffer'].append(37769)
v15['Buffer'].append(4098)
v15['Buffer'].append(22448)
v15['Buffer'].append(16379)
v15['Buffer'].append(8193)
v15['Buffer'].append(4093)
v15['Buffer'].append(15029)
v15['Buffer'].append(8183)
v15['Buffer'].append(257)
v15['Buffer'].append(4090)
v15['Buffer'].append(4092)
v15['Buffer'].append(1)
v15['Buffer'].append(249)
v15['Buffer'].append(4987)
v15['Buffer'].append(262)
v15['Buffer'].append(2)
v15['Buffer'].append(45892)
v15['Buffer'].append(250)
v15['Buffer'].append(8189)
v15['Buffer'].append(8185)
v15['Buffer'].append(37769)
v15['Buffer'].append(4097)
v15['Buffer'].append(251)
v15['Buffer'].append(37067)
v15['Buffer'].append(8909)
v15['Buffer'].append(8183)
v15['Buffer'].append(4097)



req = ElfrRegisterEventSourceW()
req.UNCServerName = v12['UNCServerName']
req.ModuleName = v15
req.RegModuleName = v7['BackupFileName']
req.MajorVersion = v11['MinorVersion']
req.MinorVersion = v9['MajorVersion']
v16 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v11['RegModuleName']
req.RegModuleName = v9['RegModuleName']
req.MajorVersion = v16['MajorVersion']
req.MinorVersion = v3
v17 = dce.request(req)

v18 = 3672137681

req = ElfrOpenBELA()
req.UNCServerName = v1
req.BackupFileName = v11['ModuleName']
req.MajorVersion = v13['MinorVersion']
req.MinorVersion = v18
v19 = dce.request(req)

v20 = b'\xff\xfe1\x00\x00\x00;\x00\x00\x00S\x00\x00\x00E\x00\x00\x00L\x00\x00\x00E\x00\x00\x00C\x00\x00\x00T\x00\x00\x00%\x00\x00\x002\x00\x00\x000\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenBELW()
req.UNCServerName = v20
req.BackupFileName = v7['BackupFileName']
req.MajorVersion = v3
req.MinorVersion = v4['MinorVersion']
v21 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v21['UNCServerName']
req.ModuleName = v12['RegModuleName']
req.RegModuleName = v14['RegModuleName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v19['MajorVersion']
v22 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v17['UNCServerName']
req.BackupFileName = v4['RegModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v4['MinorVersion']
v23 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v15
req.RegModuleName = v21['BackupFileName']
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v22['MinorVersion']
v24 = dce.request(req)

v25 = RPC_STRING()
v25['Length'] = 28246
v25['MaximumLength'] = 16387
v25['Buffer'] = UC_CHAR_ARRAY()
v25['Buffer'].append(48)
v25['Buffer'].append(249)
v25['Buffer'].append(89)
v25['Buffer'].append(58)
v25['Buffer'].append(66)
v25['Buffer'].append(2)
v25['Buffer'].append(180)
v25['Buffer'].append(29)
v25['Buffer'].append(251)
v25['Buffer'].append(34)
v25['Buffer'].append(83)
v25['Buffer'].append(76)
v25['Buffer'].append(252)
v25['Buffer'].append(76)
v25['Buffer'].append(59)
v25['Buffer'].append(98)
v25['Buffer'].append(58)
v25['Buffer'].append(157)
v25['Buffer'].append(196)
v25['Buffer'].append(64)
v25['Buffer'].append(252)
v25['Buffer'].append(66)
v25['Buffer'].append(212)
v25['Buffer'].append(254)
v25['Buffer'].append(19)
v25['Buffer'].append(24)
v25['Buffer'].append(56)
v25['Buffer'].append(1)
v25['Buffer'].append(17)
v25['Buffer'].append(247)
v25['Buffer'].append(252)
v25['Buffer'].append(115)
v25['Buffer'].append(193)
v25['Buffer'].append(3)
v25['Buffer'].append(2)
v25['Buffer'].append(19)
v25['Buffer'].append(66)
v25['Buffer'].append(14)
v25['Buffer'].append(76)
v25['Buffer'].append(203)
v25['Buffer'].append(62)
v25['Buffer'].append(76)
v25['Buffer'].append(101)
v25['Buffer'].append(219)
v25['Buffer'].append(32)
v25['Buffer'].append(33)
v25['Buffer'].append(65)
v25['Buffer'].append(193)
v25['Buffer'].append(62)
v25['Buffer'].append(57)
v25['Buffer'].append(23)
v25['Buffer'].append(21)
v25['Buffer'].append(255)
v25['Buffer'].append(0)
v25['Buffer'].append(250)
v25['Buffer'].append(98)
v25['Buffer'].append(63)
v25['Buffer'].append(57)
v25['Buffer'].append(249)
v25['Buffer'].append(115)
v25['Buffer'].append(36)
v25['Buffer'].append(193)
v25['Buffer'].append(251)
v25['Buffer'].append(37)
v25['Buffer'].append(33)
v25['Buffer'].append(113)
v25['Buffer'].append(16)
v25['Buffer'].append(15)
v25['Buffer'].append(61)
v25['Buffer'].append(14)
v25['Buffer'].append(93)
v25['Buffer'].append(9)
v25['Buffer'].append(3)
v25['Buffer'].append(21)
v25['Buffer'].append(5)
v25['Buffer'].append(195)
v25['Buffer'].append(59)
v25['Buffer'].append(9)
v25['Buffer'].append(14)
v25['Buffer'].append(212)
v25['Buffer'].append(11)
v25['Buffer'].append(38)
v25['Buffer'].append(15)
v25['Buffer'].append(16)
v25['Buffer'].append(34)
v25['Buffer'].append(106)
v25['Buffer'].append(196)
v25['Buffer'].append(63)
v25['Buffer'].append(193)
v25['Buffer'].append(24)
v25['Buffer'].append(106)
v25['Buffer'].append(57)
v25['Buffer'].append(255)
v25['Buffer'].append(36)
v25['Buffer'].append(246)
v25['Buffer'].append(76)
v25['Buffer'].append(37)
v25['Buffer'].append(31)
v25['Buffer'].append(219)
v25['Buffer'].append(6)
v25['Buffer'].append(197)
v25['Buffer'].append(203)
v25['Buffer'].append(35)
v25['Buffer'].append(69)
v25['Buffer'].append(187)



req = ElfrRegisterEventSourceA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v8['BackupFileName']
req.RegModuleName = v25
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v24['MinorVersion']
v26 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v9['RegModuleName']
req.MajorVersion = v22['MajorVersion']
req.MinorVersion = v14['MajorVersion']
v27 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v4['ModuleName']
req.RegModuleName = v10
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v22['MajorVersion']
v28 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v22['UNCServerName']
req.BackupFileName = v24['ModuleName']
req.MajorVersion = v8['MinorVersion']
req.MinorVersion = v8['MinorVersion']
v29 = dce.request(req)

v30 = 536870908

req = ElfrOpenBELW()
req.UNCServerName = v20
req.BackupFileName = v22['ModuleName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v30
v31 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v19['BackupFileName']
req.RegModuleName = v8['BackupFileName']
req.MajorVersion = v23['MajorVersion']
req.MinorVersion = v24['MajorVersion']
v32 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v9['ModuleName']
req.RegModuleName = v28['ModuleName']
req.MajorVersion = v19['MinorVersion']
req.MinorVersion = v27['MajorVersion']
v33 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v21['UNCServerName']
req.ModuleName = v22['ModuleName']
req.RegModuleName = v12['RegModuleName']
req.MajorVersion = v26['MinorVersion']
req.MinorVersion = v27['MinorVersion']
v34 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v27['UNCServerName']
req.ModuleName = v11['ModuleName']
req.RegModuleName = v26['RegModuleName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v34['MajorVersion']
v35 = dce.request(req)

v36 = 65541

req = ElfrOpenBELA()
req.UNCServerName = v33['UNCServerName']
req.BackupFileName = v9['RegModuleName']
req.MajorVersion = v28['MinorVersion']
req.MinorVersion = v36
v37 = dce.request(req)

v38 = RPC_UNICODE_STRING()
v38['Length'] = 46862
v38['MaximumLength'] = 16378
v38['Buffer'] = UC_WCHAR_ARRAY()
v38['Buffer'].append(61179)
v38['Buffer'].append(56544)
v38['Buffer'].append(8193)
v38['Buffer'].append(39148)
v38['Buffer'].append(25767)
v38['Buffer'].append(16383)
v38['Buffer'].append(4101)
v38['Buffer'].append(8198)
v38['Buffer'].append(257)
v38['Buffer'].append(255)
v38['Buffer'].append(5)
v38['Buffer'].append(8192)
v38['Buffer'].append(249)
v38['Buffer'].append(63920)
v38['Buffer'].append(65534)
v38['Buffer'].append(2)
v38['Buffer'].append(4)
v38['Buffer'].append(36317)
v38['Buffer'].append(28246)
v38['Buffer'].append(16714)
v38['Buffer'].append(34618)
v38['Buffer'].append(4101)
v38['Buffer'].append(4)
v38['Buffer'].append(37067)
v38['Buffer'].append(261)
v38['Buffer'].append(46044)
v38['Buffer'].append(4102)
v38['Buffer'].append(249)
v38['Buffer'].append(22448)
v38['Buffer'].append(16383)
v38['Buffer'].append(56544)
v38['Buffer'].append(60958)
v38['Buffer'].append(4087)
v38['Buffer'].append(39148)
v38['Buffer'].append(37067)
v38['Buffer'].append(22448)
v38['Buffer'].append(16378)
v38['Buffer'].append(0)
v38['Buffer'].append(4095)
v38['Buffer'].append(4)
v38['Buffer'].append(254)
v38['Buffer'].append(1634)
v38['Buffer'].append(7)
v38['Buffer'].append(8188)
v38['Buffer'].append(16382)
v38['Buffer'].append(24883)
v38['Buffer'].append(16385)
v38['Buffer'].append(16375)
v38['Buffer'].append(61179)
v38['Buffer'].append(16376)
v38['Buffer'].append(4089)
v38['Buffer'].append(8185)
v38['Buffer'].append(4088)
v38['Buffer'].append(20726)
v38['Buffer'].append(59445)
v38['Buffer'].append(16714)
v38['Buffer'].append(57955)
v38['Buffer'].append(8188)
v38['Buffer'].append(16385)
v38['Buffer'].append(16378)
v38['Buffer'].append(11378)
v38['Buffer'].append(4102)
v38['Buffer'].append(60958)
v38['Buffer'].append(19605)
v38['Buffer'].append(4098)
v38['Buffer'].append(16376)
v38['Buffer'].append(45892)
v38['Buffer'].append(56544)
v38['Buffer'].append(8186)
v38['Buffer'].append(56373)
v38['Buffer'].append(36317)
v38['Buffer'].append(19202)
v38['Buffer'].append(2)
v38['Buffer'].append(16850)
v38['Buffer'].append(8193)
v38['Buffer'].append(28246)
v38['Buffer'].append(65533)
v38['Buffer'].append(5)
v38['Buffer'].append(16389)
v38['Buffer'].append(65534)
v38['Buffer'].append(2)
v38['Buffer'].append(22448)
v38['Buffer'].append(27815)
v38['Buffer'].append(56186)
v38['Buffer'].append(8188)
v38['Buffer'].append(16385)
v38['Buffer'].append(16714)
v38['Buffer'].append(34618)
v38['Buffer'].append(20726)
v38['Buffer'].append(256)
v38['Buffer'].append(27815)
v38['Buffer'].append(8197)
v38['Buffer'].append(8197)
v38['Buffer'].append(65534)
v38['Buffer'].append(19202)
v38['Buffer'].append(15173)
v38['Buffer'].append(65531)
v38['Buffer'].append(4987)
v38['Buffer'].append(8187)
v38['Buffer'].append(47627)
v38['Buffer'].append(8196)
v38['Buffer'].append(1)
v38['Buffer'].append(39148)
v38['Buffer'].append(2)
v38['Buffer'].append(65528)
v38['Buffer'].append(25767)
v38['Buffer'].append(45343)
v38['Buffer'].append(45343)
v38['Buffer'].append(252)
v38['Buffer'].append(16389)
v38['Buffer'].append(38807)
v38['Buffer'].append(7)
v38['Buffer'].append(2854)
v38['Buffer'].append(14980)
v38['Buffer'].append(4094)
v38['Buffer'].append(46044)
v38['Buffer'].append(15029)
v38['Buffer'].append(258)
v38['Buffer'].append(1)
v38['Buffer'].append(4092)
v38['Buffer'].append(253)
v38['Buffer'].append(38005)
v38['Buffer'].append(8195)
v38['Buffer'].append(4098)
v38['Buffer'].append(13212)
v38['Buffer'].append(16388)
v38['Buffer'].append(252)
v38['Buffer'].append(4088)
v38['Buffer'].append(4094)
v38['Buffer'].append(11378)
v38['Buffer'].append(56186)
v38['Buffer'].append(254)
v38['Buffer'].append(254)
v38['Buffer'].append(22522)
v38['Buffer'].append(60958)
v38['Buffer'].append(38807)
v38['Buffer'].append(16384)
v38['Buffer'].append(16382)
v38['Buffer'].append(16384)
v38['Buffer'].append(38807)
v38['Buffer'].append(65529)
v38['Buffer'].append(59445)
v38['Buffer'].append(4)
v38['Buffer'].append(13212)
v38['Buffer'].append(36989)
v38['Buffer'].append(63920)
v38['Buffer'].append(2)
v38['Buffer'].append(20726)
v38['Buffer'].append(65532)
v38['Buffer'].append(8190)
v38['Buffer'].append(11378)
v38['Buffer'].append(16379)
v38['Buffer'].append(4098)
v38['Buffer'].append(7)
v38['Buffer'].append(8183)
v38['Buffer'].append(16381)
v38['Buffer'].append(57955)
v38['Buffer'].append(49931)
v38['Buffer'].append(45343)
v38['Buffer'].append(65529)
v38['Buffer'].append(4101)
v38['Buffer'].append(37769)
v38['Buffer'].append(37925)
v38['Buffer'].append(2)
v38['Buffer'].append(2)
v38['Buffer'].append(56544)
v38['Buffer'].append(65530)
v38['Buffer'].append(46862)
v38['Buffer'].append(251)
v38['Buffer'].append(37769)
v38['Buffer'].append(52405)
v38['Buffer'].append(39148)
v38['Buffer'].append(247)
v38['Buffer'].append(4093)
v38['Buffer'].append(16850)
v38['Buffer'].append(8187)



req = ElfrOpenBELW()
req.UNCServerName = v29['UNCServerName']
req.BackupFileName = v38
req.MajorVersion = v13['MajorVersion']
req.MinorVersion = v37['MinorVersion']
v39 = dce.request(req)

v40 = 536870913

req = ElfrOpenELW()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v31['BackupFileName']
req.RegModuleName = v14['RegModuleName']
req.MajorVersion = v21['MinorVersion']
req.MinorVersion = v40
v41 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v4['RegModuleName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v29['MinorVersion']
v42 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v9['UNCServerName']
req.BackupFileName = v33['RegModuleName']
req.MajorVersion = v34['MinorVersion']
req.MinorVersion = v28['MinorVersion']
v43 = dce.request(req)

v44 = b'\xff\xfe\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenBELW()
req.UNCServerName = v44
req.BackupFileName = v13['BackupFileName']
req.MajorVersion = v37['MinorVersion']
req.MinorVersion = v29['MajorVersion']
v45 = dce.request(req)

v46 = RPC_STRING()
v46['Length'] = 248
v46['MaximumLength'] = 251
v46['Buffer'] = UC_CHAR_ARRAY()
v46['Buffer'].append(33)
v46['Buffer'].append(95)
v46['Buffer'].append(30)
v46['Buffer'].append(36)
v46['Buffer'].append(32)
v46['Buffer'].append(248)
v46['Buffer'].append(197)
v46['Buffer'].append(4)
v46['Buffer'].append(249)
v46['Buffer'].append(150)
v46['Buffer'].append(197)
v46['Buffer'].append(58)
v46['Buffer'].append(25)
v46['Buffer'].append(64)
v46['Buffer'].append(115)
v46['Buffer'].append(18)
v46['Buffer'].append(17)
v46['Buffer'].append(89)
v46['Buffer'].append(1)
v46['Buffer'].append(191)
v46['Buffer'].append(66)
v46['Buffer'].append(2)
v46['Buffer'].append(16)
v46['Buffer'].append(14)
v46['Buffer'].append(252)
v46['Buffer'].append(14)
v46['Buffer'].append(195)
v46['Buffer'].append(0)
v46['Buffer'].append(187)
v46['Buffer'].append(14)
v46['Buffer'].append(13)
v46['Buffer'].append(113)
v46['Buffer'].append(17)
v46['Buffer'].append(65)
v46['Buffer'].append(2)
v46['Buffer'].append(35)
v46['Buffer'].append(131)
v46['Buffer'].append(230)
v46['Buffer'].append(21)
v46['Buffer'].append(3)
v46['Buffer'].append(10)
v46['Buffer'].append(98)
v46['Buffer'].append(9)
v46['Buffer'].append(230)
v46['Buffer'].append(254)
v46['Buffer'].append(15)
v46['Buffer'].append(22)
v46['Buffer'].append(230)
v46['Buffer'].append(133)
v46['Buffer'].append(2)
v46['Buffer'].append(62)
v46['Buffer'].append(187)
v46['Buffer'].append(169)
v46['Buffer'].append(115)
v46['Buffer'].append(70)
v46['Buffer'].append(196)
v46['Buffer'].append(93)
v46['Buffer'].append(21)
v46['Buffer'].append(157)
v46['Buffer'].append(126)
v46['Buffer'].append(31)
v46['Buffer'].append(76)
v46['Buffer'].append(95)
v46['Buffer'].append(131)
v46['Buffer'].append(14)
v46['Buffer'].append(62)
v46['Buffer'].append(29)
v46['Buffer'].append(93)
v46['Buffer'].append(33)
v46['Buffer'].append(76)
v46['Buffer'].append(253)
v46['Buffer'].append(113)
v46['Buffer'].append(252)
v46['Buffer'].append(255)
v46['Buffer'].append(248)
v46['Buffer'].append(246)
v46['Buffer'].append(34)
v46['Buffer'].append(24)
v46['Buffer'].append(203)
v46['Buffer'].append(37)
v46['Buffer'].append(69)
v46['Buffer'].append(48)
v46['Buffer'].append(65)
v46['Buffer'].append(15)
v46['Buffer'].append(196)
v46['Buffer'].append(32)
v46['Buffer'].append(10)
v46['Buffer'].append(60)
v46['Buffer'].append(180)
v46['Buffer'].append(62)
v46['Buffer'].append(16)
v46['Buffer'].append(36)
v46['Buffer'].append(62)
v46['Buffer'].append(61)
v46['Buffer'].append(69)
v46['Buffer'].append(253)
v46['Buffer'].append(57)
v46['Buffer'].append(187)
v46['Buffer'].append(254)
v46['Buffer'].append(27)
v46['Buffer'].append(64)
v46['Buffer'].append(18)
v46['Buffer'].append(157)
v46['Buffer'].append(15)
v46['Buffer'].append(93)
v46['Buffer'].append(57)
v46['Buffer'].append(88)



req = ElfrOpenELA()
req.UNCServerName = v23['UNCServerName']
req.ModuleName = v46
req.RegModuleName = v26['ModuleName']
req.MajorVersion = v11['MajorVersion']
req.MinorVersion = v8['MajorVersion']
v47 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v16['UNCServerName']
req.BackupFileName = v7['BackupFileName']
req.MajorVersion = v42['MinorVersion']
req.MinorVersion = v40
v48 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v28['RegModuleName']
req.RegModuleName = v2
req.MajorVersion = v33['MinorVersion']
req.MinorVersion = v30
v49 = dce.request(req)

v50 = 4294967288

v51 = 2722882118

req = ElfrRegisterEventSourceA()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v28['ModuleName']
req.MajorVersion = v50
req.MinorVersion = v51
v52 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v42['BackupFileName']
req.MajorVersion = v11['MajorVersion']
req.MinorVersion = v13['MajorVersion']
v53 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v19['UNCServerName']
req.ModuleName = v10
req.RegModuleName = v4['ModuleName']
req.MajorVersion = v26['MinorVersion']
req.MinorVersion = v28['MinorVersion']
v54 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v22['UNCServerName']
req.BackupFileName = v34['ModuleName']
req.MajorVersion = v36
req.MinorVersion = v23['MinorVersion']
v55 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v31['UNCServerName']
req.BackupFileName = v14['ModuleName']
req.MajorVersion = v11['MinorVersion']
req.MinorVersion = v8['MajorVersion']
v56 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v42['UNCServerName']
req.BackupFileName = v23['BackupFileName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v26['MinorVersion']
v57 = dce.request(req)

v58 = b"\xff\xfe'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00\x00\x00\x00\x00".decode('utf-16')

req = ElfrOpenBELA()
req.UNCServerName = v58
req.BackupFileName = v54['ModuleName']
req.MajorVersion = v42['MajorVersion']
req.MinorVersion = v17['MajorVersion']
v59 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v11['UNCServerName']
req.BackupFileName = v35['ModuleName']
req.MajorVersion = v18
req.MinorVersion = v29['MinorVersion']
v60 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v55['UNCServerName']
req.ModuleName = v34['RegModuleName']
req.RegModuleName = v41['RegModuleName']
req.MajorVersion = v45['MinorVersion']
req.MinorVersion = v49['MinorVersion']
v61 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v59['BackupFileName']
req.RegModuleName = v33['ModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v17['MajorVersion']
v62 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v41['UNCServerName']
req.BackupFileName = v24['RegModuleName']
req.MajorVersion = v62['MajorVersion']
req.MinorVersion = v52['MinorVersion']
v63 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v47['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v54['ModuleName']
req.MajorVersion = v8['MinorVersion']
req.MinorVersion = v29['MinorVersion']
v64 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v35['ModuleName']
req.RegModuleName = v11['RegModuleName']
req.MajorVersion = v57['MinorVersion']
req.MinorVersion = v35['MajorVersion']
v65 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v61['RegModuleName']
req.RegModuleName = v29['BackupFileName']
req.MajorVersion = v47['MajorVersion']
req.MinorVersion = v60['MinorVersion']
v66 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v41['UNCServerName']
req.ModuleName = v41['ModuleName']
req.RegModuleName = v7['BackupFileName']
req.MajorVersion = v60['MajorVersion']
req.MinorVersion = v4['MajorVersion']
v67 = dce.request(req)

v68 = 144486743

req = ElfrOpenBELW()
req.UNCServerName = v39['UNCServerName']
req.BackupFileName = v56['BackupFileName']
req.MajorVersion = v68
req.MinorVersion = v59['MinorVersion']
v69 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v57['UNCServerName']
req.ModuleName = v27['BackupFileName']
req.RegModuleName = v62['ModuleName']
req.MajorVersion = v48['MinorVersion']
req.MinorVersion = v26['MinorVersion']
v70 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v26['UNCServerName']
req.ModuleName = v33['ModuleName']
req.RegModuleName = v47['RegModuleName']
req.MajorVersion = v60['MajorVersion']
req.MinorVersion = v22['MinorVersion']
v71 = dce.request(req)

v72 = 268435453

req = ElfrOpenELW()
req.UNCServerName = v55['UNCServerName']
req.ModuleName = v31['BackupFileName']
req.RegModuleName = v66['RegModuleName']
req.MajorVersion = v72
req.MinorVersion = v55['MajorVersion']
v73 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v39['BackupFileName']
req.RegModuleName = v63['BackupFileName']
req.MajorVersion = v40
req.MinorVersion = v47['MinorVersion']
v74 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v20
req.ModuleName = v6
req.RegModuleName = v61['RegModuleName']
req.MajorVersion = v62['MajorVersion']
req.MinorVersion = v57['MajorVersion']
v75 = dce.request(req)

v76 = 268435447

req = ElfrOpenELW()
req.UNCServerName = v44
req.ModuleName = v29['BackupFileName']
req.RegModuleName = v75['RegModuleName']
req.MajorVersion = v74['MinorVersion']
req.MinorVersion = v76
v77 = dce.request(req)

v78 = RPC_STRING()
v78['Length'] = 16386
v78['MaximumLength'] = 251
v78['Buffer'] = UC_CHAR_ARRAY()
v78['Buffer'].append(150)
v78['Buffer'].append(9)
v78['Buffer'].append(34)
v78['Buffer'].append(131)
v78['Buffer'].append(68)
v78['Buffer'].append(93)
v78['Buffer'].append(27)
v78['Buffer'].append(19)
v78['Buffer'].append(23)
v78['Buffer'].append(14)
v78['Buffer'].append(6)
v78['Buffer'].append(5)
v78['Buffer'].append(17)
v78['Buffer'].append(187)
v78['Buffer'].append(38)
v78['Buffer'].append(35)
v78['Buffer'].append(249)



req = ElfrRegisterEventSourceA()
req.UNCServerName = v26['UNCServerName']
req.ModuleName = v78
req.RegModuleName = v17['ModuleName']
req.MajorVersion = v32['MinorVersion']
req.MinorVersion = v24['MinorVersion']
v79 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v17['UNCServerName']
req.BackupFileName = v10
req.MajorVersion = v32['MajorVersion']
req.MinorVersion = v49['MinorVersion']
v80 = dce.request(req)

v81 = RPC_STRING()
v81['Length'] = 65529
v81['MaximumLength'] = 4099
v81['Buffer'] = UC_CHAR_ARRAY()
v81['Buffer'].append(13)
v81['Buffer'].append(133)
v81['Buffer'].append(19)
v81['Buffer'].append(249)
v81['Buffer'].append(10)
v81['Buffer'].append(28)
v81['Buffer'].append(69)
v81['Buffer'].append(13)
v81['Buffer'].append(48)
v81['Buffer'].append(11)
v81['Buffer'].append(25)
v81['Buffer'].append(4)
v81['Buffer'].append(195)
v81['Buffer'].append(61)
v81['Buffer'].append(65)
v81['Buffer'].append(101)
v81['Buffer'].append(16)
v81['Buffer'].append(70)
v81['Buffer'].append(21)
v81['Buffer'].append(12)
v81['Buffer'].append(197)
v81['Buffer'].append(19)
v81['Buffer'].append(15)
v81['Buffer'].append(133)
v81['Buffer'].append(55)
v81['Buffer'].append(89)
v81['Buffer'].append(98)
v81['Buffer'].append(63)
v81['Buffer'].append(196)
v81['Buffer'].append(113)
v81['Buffer'].append(3)
v81['Buffer'].append(113)
v81['Buffer'].append(196)
v81['Buffer'].append(29)
v81['Buffer'].append(66)
v81['Buffer'].append(95)
v81['Buffer'].append(76)
v81['Buffer'].append(30)
v81['Buffer'].append(37)
v81['Buffer'].append(12)
v81['Buffer'].append(88)
v81['Buffer'].append(20)
v81['Buffer'].append(133)
v81['Buffer'].append(26)
v81['Buffer'].append(253)
v81['Buffer'].append(19)
v81['Buffer'].append(33)
v81['Buffer'].append(62)
v81['Buffer'].append(98)
v81['Buffer'].append(248)
v81['Buffer'].append(106)
v81['Buffer'].append(157)
v81['Buffer'].append(246)
v81['Buffer'].append(150)
v81['Buffer'].append(65)
v81['Buffer'].append(197)
v81['Buffer'].append(83)
v81['Buffer'].append(23)



req = ElfrOpenBELA()
req.UNCServerName = v79['UNCServerName']
req.BackupFileName = v81
req.MajorVersion = v17['MajorVersion']
req.MinorVersion = v21['MinorVersion']
v82 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v48['BackupFileName']
req.RegModuleName = v55['BackupFileName']
req.MajorVersion = v64['MinorVersion']
req.MinorVersion = v59['MinorVersion']
v83 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v35['UNCServerName']
req.ModuleName = v62['ModuleName']
req.RegModuleName = v42['BackupFileName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v83['MinorVersion']
v84 = dce.request(req)

v85 = RPC_UNICODE_STRING()
v85['Length'] = 16385
v85['MaximumLength'] = 16383
v85['Buffer'] = UC_WCHAR_ARRAY()
v85['Buffer'].append(8196)
v85['Buffer'].append(60729)
v85['Buffer'].append(4100)
v85['Buffer'].append(20726)
v85['Buffer'].append(65531)
v85['Buffer'].append(253)
v85['Buffer'].append(8198)
v85['Buffer'].append(37067)
v85['Buffer'].append(19202)
v85['Buffer'].append(7)
v85['Buffer'].append(252)
v85['Buffer'].append(38005)
v85['Buffer'].append(1634)
v85['Buffer'].append(4102)
v85['Buffer'].append(19605)
v85['Buffer'].append(25767)
v85['Buffer'].append(56373)
v85['Buffer'].append(248)
v85['Buffer'].append(4094)
v85['Buffer'].append(46862)
v85['Buffer'].append(5)
v85['Buffer'].append(1)
v85['Buffer'].append(0)
v85['Buffer'].append(2)
v85['Buffer'].append(4090)
v85['Buffer'].append(16380)
v85['Buffer'].append(4099)
v85['Buffer'].append(254)
v85['Buffer'].append(8196)
v85['Buffer'].append(16009)
v85['Buffer'].append(8186)
v85['Buffer'].append(24883)
v85['Buffer'].append(16384)
v85['Buffer'].append(16377)
v85['Buffer'].append(16389)
v85['Buffer'].append(16383)
v85['Buffer'].append(16850)
v85['Buffer'].append(4101)
v85['Buffer'].append(4090)
v85['Buffer'].append(4987)
v85['Buffer'].append(16375)
v85['Buffer'].append(255)
v85['Buffer'].append(257)
v85['Buffer'].append(3)
v85['Buffer'].append(250)
v85['Buffer'].append(65532)
v85['Buffer'].append(16376)
v85['Buffer'].append(16378)
v85['Buffer'].append(4100)
v85['Buffer'].append(8189)
v85['Buffer'].append(8195)
v85['Buffer'].append(13212)
v85['Buffer'].append(261)
v85['Buffer'].append(4987)
v85['Buffer'].append(8187)
v85['Buffer'].append(24883)
v85['Buffer'].append(37769)
v85['Buffer'].append(3)
v85['Buffer'].append(16387)
v85['Buffer'].append(1634)
v85['Buffer'].append(4091)
v85['Buffer'].append(4102)
v85['Buffer'].append(60729)
v85['Buffer'].append(4095)
v85['Buffer'].append(257)
v85['Buffer'].append(4096)
v85['Buffer'].append(6)
v85['Buffer'].append(28246)
v85['Buffer'].append(49931)
v85['Buffer'].append(28246)



v86 = RPC_UNICODE_STRING()
v86['Length'] = 8191
v86['MaximumLength'] = 262
v86['Buffer'] = UC_WCHAR_ARRAY()
v86['Buffer'].append(4100)
v86['Buffer'].append(65534)
v86['Buffer'].append(24883)
v86['Buffer'].append(16387)
v86['Buffer'].append(8184)
v86['Buffer'].append(65527)
v86['Buffer'].append(65528)
v86['Buffer'].append(4089)
v86['Buffer'].append(46044)
v86['Buffer'].append(16378)
v86['Buffer'].append(52405)
v86['Buffer'].append(4099)
v86['Buffer'].append(65529)
v86['Buffer'].append(8197)
v86['Buffer'].append(4087)
v86['Buffer'].append(7)
v86['Buffer'].append(16382)
v86['Buffer'].append(6)
v86['Buffer'].append(47627)
v86['Buffer'].append(259)
v86['Buffer'].append(16379)
v86['Buffer'].append(56544)
v86['Buffer'].append(45343)
v86['Buffer'].append(65533)
v86['Buffer'].append(65527)
v86['Buffer'].append(27815)
v86['Buffer'].append(16380)
v86['Buffer'].append(60958)
v86['Buffer'].append(4087)
v86['Buffer'].append(8189)
v86['Buffer'].append(56544)
v86['Buffer'].append(47627)
v86['Buffer'].append(16378)
v86['Buffer'].append(56186)
v86['Buffer'].append(22522)
v86['Buffer'].append(247)
v86['Buffer'].append(0)
v86['Buffer'].append(56373)
v86['Buffer'].append(8189)
v86['Buffer'].append(4097)
v86['Buffer'].append(19202)
v86['Buffer'].append(36317)
v86['Buffer'].append(251)
v86['Buffer'].append(24883)
v86['Buffer'].append(8188)
v86['Buffer'].append(4097)
v86['Buffer'].append(8192)
v86['Buffer'].append(260)



req = ElfrOpenELW()
req.UNCServerName = v48['UNCServerName']
req.ModuleName = v85
req.RegModuleName = v86
req.MajorVersion = v34['MajorVersion']
req.MinorVersion = v77['MinorVersion']
v87 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v44
req.ModuleName = v22['ModuleName']
req.RegModuleName = v67['ModuleName']
req.MajorVersion = v39['MajorVersion']
req.MinorVersion = v50
v88 = dce.request(req)

v89 = 2147483648

req = ElfrOpenELW()
req.UNCServerName = v87['UNCServerName']
req.ModuleName = v41['RegModuleName']
req.RegModuleName = v61['RegModuleName']
req.MajorVersion = v89
req.MinorVersion = v64['MajorVersion']
v90 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v34['UNCServerName']
req.ModuleName = v34['RegModuleName']
req.RegModuleName = v38
req.MajorVersion = v63['MajorVersion']
req.MinorVersion = v69['MinorVersion']
v91 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v84['UNCServerName']
req.BackupFileName = v28['ModuleName']
req.MajorVersion = v57['MinorVersion']
req.MinorVersion = v12['MinorVersion']
v92 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v57['UNCServerName']
req.ModuleName = v27['BackupFileName']
req.RegModuleName = v42['BackupFileName']
req.MajorVersion = v27['MajorVersion']
req.MinorVersion = v53['MajorVersion']
v93 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v88['UNCServerName']
req.ModuleName = v66['RegModuleName']
req.RegModuleName = v74['RegModuleName']
req.MajorVersion = v13['MinorVersion']
req.MinorVersion = v53['MajorVersion']
v94 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v94['UNCServerName']
req.ModuleName = v29['BackupFileName']
req.RegModuleName = v73['ModuleName']
req.MajorVersion = v88['MajorVersion']
req.MinorVersion = v55['MinorVersion']
v95 = dce.request(req)

v96 = b'\xff\xfe\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrRegisterEventSourceW()
req.UNCServerName = v96
req.ModuleName = v88['ModuleName']
req.RegModuleName = v75['ModuleName']
req.MajorVersion = v29['MinorVersion']
req.MinorVersion = v87['MinorVersion']
v97 = dce.request(req)

v98 = 268435456

req = ElfrOpenBELA()
req.UNCServerName = v53['UNCServerName']
req.BackupFileName = v10
req.MajorVersion = v98
req.MinorVersion = v19['MajorVersion']
v99 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v12['UNCServerName']
req.ModuleName = v87['RegModuleName']
req.RegModuleName = v75['RegModuleName']
req.MajorVersion = v92['MajorVersion']
req.MinorVersion = v32['MajorVersion']
v100 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v39['UNCServerName']
req.ModuleName = v63['BackupFileName']
req.RegModuleName = v87['RegModuleName']
req.MajorVersion = v74['MinorVersion']
req.MinorVersion = v82['MinorVersion']
v101 = dce.request(req)

v102 = 16777217

req = ElfrRegisterEventSourceW()
req.UNCServerName = v63['UNCServerName']
req.ModuleName = v14['RegModuleName']
req.RegModuleName = v34['ModuleName']
req.MajorVersion = v102
req.MinorVersion = v51
v103 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v95['UNCServerName']
req.ModuleName = v74['RegModuleName']
req.RegModuleName = v66['RegModuleName']
req.MajorVersion = v62['MajorVersion']
req.MinorVersion = v4['MinorVersion']
v104 = dce.request(req)

v105 = 65532

req = ElfrOpenBELA()
req.UNCServerName = v19['UNCServerName']
req.BackupFileName = v9['ModuleName']
req.MajorVersion = v105
req.MinorVersion = v14['MajorVersion']
v106 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v16['ModuleName']
req.RegModuleName = v61['ModuleName']
req.MajorVersion = v19['MinorVersion']
req.MinorVersion = v83['MajorVersion']
v107 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v35['UNCServerName']
req.ModuleName = v8['BackupFileName']
req.RegModuleName = v53['ModuleName']
req.MajorVersion = v88['MinorVersion']
req.MinorVersion = v61['MinorVersion']
v108 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v87['UNCServerName']
req.BackupFileName = v100['ModuleName']
req.MajorVersion = v83['MajorVersion']
req.MinorVersion = v79['MajorVersion']
v109 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v87['UNCServerName']
req.BackupFileName = v41['RegModuleName']
req.MajorVersion = v108['MinorVersion']
req.MinorVersion = v79['MinorVersion']
v110 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v100['UNCServerName']
req.ModuleName = v77['RegModuleName']
req.RegModuleName = v67['RegModuleName']
req.MajorVersion = v93['MinorVersion']
req.MinorVersion = v72
v111 = dce.request(req)

v112 = RPC_UNICODE_STRING()
v112['Length'] = 259
v112['MaximumLength'] = 4092
v112['Buffer'] = UC_WCHAR_ARRAY()
v112['Buffer'].append(254)
v112['Buffer'].append(16383)
v112['Buffer'].append(65533)
v112['Buffer'].append(256)
v112['Buffer'].append(256)
v112['Buffer'].append(8189)
v112['Buffer'].append(16009)
v112['Buffer'].append(56186)
v112['Buffer'].append(4093)
v112['Buffer'].append(4094)
v112['Buffer'].append(4087)
v112['Buffer'].append(20726)
v112['Buffer'].append(247)
v112['Buffer'].append(8187)
v112['Buffer'].append(60958)
v112['Buffer'].append(37769)
v112['Buffer'].append(16382)
v112['Buffer'].append(0)
v112['Buffer'].append(16379)
v112['Buffer'].append(16379)
v112['Buffer'].append(16384)
v112['Buffer'].append(258)
v112['Buffer'].append(3)
v112['Buffer'].append(257)
v112['Buffer'].append(13212)
v112['Buffer'].append(4095)
v112['Buffer'].append(16381)
v112['Buffer'].append(4102)
v112['Buffer'].append(24883)
v112['Buffer'].append(22522)
v112['Buffer'].append(60729)
v112['Buffer'].append(4094)
v112['Buffer'].append(8190)
v112['Buffer'].append(65532)
v112['Buffer'].append(16385)
v112['Buffer'].append(4094)
v112['Buffer'].append(4095)
v112['Buffer'].append(16382)
v112['Buffer'].append(34618)
v112['Buffer'].append(49931)
v112['Buffer'].append(38520)
v112['Buffer'].append(63164)
v112['Buffer'].append(3)
v112['Buffer'].append(16009)
v112['Buffer'].append(27815)
v112['Buffer'].append(8198)
v112['Buffer'].append(261)
v112['Buffer'].append(45343)
v112['Buffer'].append(16714)
v112['Buffer'].append(250)
v112['Buffer'].append(249)
v112['Buffer'].append(36989)
v112['Buffer'].append(260)
v112['Buffer'].append(8194)
v112['Buffer'].append(59445)
v112['Buffer'].append(65529)
v112['Buffer'].append(253)
v112['Buffer'].append(5)
v112['Buffer'].append(4)
v112['Buffer'].append(8189)
v112['Buffer'].append(251)
v112['Buffer'].append(59445)
v112['Buffer'].append(4091)
v112['Buffer'].append(250)
v112['Buffer'].append(8185)
v112['Buffer'].append(8189)
v112['Buffer'].append(65534)
v112['Buffer'].append(6)
v112['Buffer'].append(38005)



req = ElfrOpenELW()
req.UNCServerName = v90['UNCServerName']
req.ModuleName = v83['RegModuleName']
req.RegModuleName = v112
req.MajorVersion = v21['MinorVersion']
req.MinorVersion = v91['MinorVersion']
v113 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v6
req.RegModuleName = v73['RegModuleName']
req.MajorVersion = v113['MajorVersion']
req.MinorVersion = v82['MinorVersion']
v114 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v66['UNCServerName']
req.BackupFileName = v74['RegModuleName']
req.MajorVersion = v113['MajorVersion']
req.MinorVersion = v77['MajorVersion']
v115 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v37['UNCServerName']
req.BackupFileName = v32['RegModuleName']
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v12['MajorVersion']
v116 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v28['UNCServerName']
req.ModuleName = v33['RegModuleName']
req.RegModuleName = v82['BackupFileName']
req.MajorVersion = v114['MajorVersion']
req.MinorVersion = v82['MinorVersion']
v117 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v53['UNCServerName']
req.ModuleName = v62['ModuleName']
req.RegModuleName = v54['ModuleName']
req.MajorVersion = v69['MajorVersion']
req.MinorVersion = v19['MajorVersion']
v118 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v57['UNCServerName']
req.ModuleName = v80['BackupFileName']
req.RegModuleName = v23['BackupFileName']
req.MajorVersion = v77['MinorVersion']
req.MinorVersion = v62['MinorVersion']
v119 = dce.request(req)

v120 = 509488247

req = ElfrOpenBELA()
req.UNCServerName = v92['UNCServerName']
req.BackupFileName = v47['RegModuleName']
req.MajorVersion = v120
req.MinorVersion = v56['MajorVersion']
v121 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v1
req.BackupFileName = v108['RegModuleName']
req.MajorVersion = v74['MajorVersion']
req.MinorVersion = v87['MinorVersion']
v122 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v8['UNCServerName']
req.BackupFileName = v84['ModuleName']
req.MajorVersion = v114['MajorVersion']
req.MinorVersion = v49['MajorVersion']
v123 = dce.request(req)

v124 = 0

req = ElfrOpenBELA()
req.UNCServerName = v117['UNCServerName']
req.BackupFileName = v2
req.MajorVersion = v124
req.MinorVersion = v59['MajorVersion']
v125 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v95['UNCServerName']
req.BackupFileName = v94['ModuleName']
req.MajorVersion = v88['MajorVersion']
req.MinorVersion = v80['MajorVersion']
v126 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v126['UNCServerName']
req.ModuleName = v66['RegModuleName']
req.RegModuleName = v91['RegModuleName']
req.MajorVersion = v118['MinorVersion']
req.MinorVersion = v41['MinorVersion']
v127 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v14['UNCServerName']
req.BackupFileName = v127['RegModuleName']
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v74['MinorVersion']
v128 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v1
req.BackupFileName = v17['RegModuleName']
req.MajorVersion = v117['MajorVersion']
req.MinorVersion = v128['MinorVersion']
v129 = dce.request(req)

v130 = RPC_STRING()
v130['Length'] = 16383
v130['MaximumLength'] = 37769
v130['Buffer'] = UC_CHAR_ARRAY()
v130['Buffer'].append(67)
v130['Buffer'].append(33)
v130['Buffer'].append(150)
v130['Buffer'].append(32)
v130['Buffer'].append(62)
v130['Buffer'].append(64)
v130['Buffer'].append(82)
v130['Buffer'].append(22)
v130['Buffer'].append(247)
v130['Buffer'].append(2)
v130['Buffer'].append(5)
v130['Buffer'].append(5)
v130['Buffer'].append(197)
v130['Buffer'].append(255)
v130['Buffer'].append(66)
v130['Buffer'].append(126)
v130['Buffer'].append(0)
v130['Buffer'].append(222)
v130['Buffer'].append(76)
v130['Buffer'].append(212)
v130['Buffer'].append(12)
v130['Buffer'].append(10)
v130['Buffer'].append(76)
v130['Buffer'].append(38)
v130['Buffer'].append(26)
v130['Buffer'].append(31)
v130['Buffer'].append(11)
v130['Buffer'].append(208)
v130['Buffer'].append(28)
v130['Buffer'].append(5)
v130['Buffer'].append(59)
v130['Buffer'].append(18)
v130['Buffer'].append(29)
v130['Buffer'].append(113)
v130['Buffer'].append(255)
v130['Buffer'].append(212)
v130['Buffer'].append(17)
v130['Buffer'].append(18)
v130['Buffer'].append(253)
v130['Buffer'].append(35)
v130['Buffer'].append(95)
v130['Buffer'].append(36)
v130['Buffer'].append(8)
v130['Buffer'].append(61)
v130['Buffer'].append(208)
v130['Buffer'].append(150)
v130['Buffer'].append(254)
v130['Buffer'].append(36)
v130['Buffer'].append(66)
v130['Buffer'].append(252)
v130['Buffer'].append(89)
v130['Buffer'].append(16)
v130['Buffer'].append(23)
v130['Buffer'].append(13)
v130['Buffer'].append(59)
v130['Buffer'].append(57)
v130['Buffer'].append(8)
v130['Buffer'].append(57)
v130['Buffer'].append(20)
v130['Buffer'].append(62)
v130['Buffer'].append(2)
v130['Buffer'].append(254)
v130['Buffer'].append(14)
v130['Buffer'].append(64)
v130['Buffer'].append(203)
v130['Buffer'].append(35)
v130['Buffer'].append(5)
v130['Buffer'].append(64)
v130['Buffer'].append(58)
v130['Buffer'].append(67)
v130['Buffer'].append(14)
v130['Buffer'].append(17)
v130['Buffer'].append(64)
v130['Buffer'].append(64)
v130['Buffer'].append(0)
v130['Buffer'].append(250)
v130['Buffer'].append(2)
v130['Buffer'].append(254)
v130['Buffer'].append(66)
v130['Buffer'].append(197)
v130['Buffer'].append(150)
v130['Buffer'].append(254)
v130['Buffer'].append(17)
v130['Buffer'].append(131)
v130['Buffer'].append(6)
v130['Buffer'].append(10)
v130['Buffer'].append(254)
v130['Buffer'].append(212)
v130['Buffer'].append(27)
v130['Buffer'].append(82)
v130['Buffer'].append(212)
v130['Buffer'].append(98)



v131 = 16777210

req = ElfrOpenBELA()
req.UNCServerName = v92['UNCServerName']
req.BackupFileName = v130
req.MajorVersion = v61['MinorVersion']
req.MinorVersion = v131
v132 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v95['UNCServerName']
req.BackupFileName = v55['BackupFileName']
req.MajorVersion = v28['MinorVersion']
req.MinorVersion = v45['MinorVersion']
v133 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v9['UNCServerName']
req.ModuleName = v119['RegModuleName']
req.RegModuleName = v116['BackupFileName']
req.MajorVersion = v115['MajorVersion']
req.MinorVersion = v101['MinorVersion']
v134 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v94['UNCServerName']
req.ModuleName = v74['ModuleName']
req.RegModuleName = v7['BackupFileName']
req.MajorVersion = v8['MajorVersion']
req.MinorVersion = v69['MajorVersion']
v135 = dce.request(req)

v136 = 1073741815

req = ElfrRegisterEventSourceW()
req.UNCServerName = v97['UNCServerName']
req.ModuleName = v90['ModuleName']
req.RegModuleName = v127['RegModuleName']
req.MajorVersion = v136
req.MinorVersion = v37['MinorVersion']
v137 = dce.request(req)

