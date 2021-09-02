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

v1 = b'\xff\xfe1\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x001\x00\x00\x00'.decode('utf-16')

v2 = RPC_STRING()
v2['Length'] = 61590
v2['MaximumLength'] = 14984
v2['Buffer'] = None # TODO UC_CHAR_ARRAY


v3 = 18162186689443334396

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v2
req.RegModuleName = v2
req.MajorVersion = v3
req.MinorVersion = v3
v4 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v2
req.RegModuleName = v4['RegModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v4['MinorVersion']
v5 = dce.request(req)

v6 = b'\xff\xfe?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

v7 = RPC_UNICODE_STRING()
v7['Length'] = 4612366630185475174
v7['MaximumLength'] = 8185.875
v7['Buffer'] = None # TODO UC_WCHAR_ARRAY


v8 = 134217736.96875

req = ElfrOpenELW()
req.UNCServerName = v6
req.ModuleName = v7
req.RegModuleName = v7
req.MajorVersion = v8
req.MinorVersion = v3
v9 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v5['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v5['ModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v5['MajorVersion']
v10 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v5['UNCServerName']
req.ModuleName = v10['RegModuleName']
req.RegModuleName = v10['RegModuleName']
req.MajorVersion = v9['MinorVersion']
req.MinorVersion = v5['MinorVersion']
v11 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v5['UNCServerName']
req.BackupFileName = v4['RegModuleName']
req.MajorVersion = v9['MinorVersion']
req.MinorVersion = v4['MajorVersion']
v12 = dce.request(req)

v13 = b'\xff\xfe+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00+\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenBELA()
req.UNCServerName = v13
req.BackupFileName = v12['BackupFileName']
req.MajorVersion = v8
req.MinorVersion = v3
v14 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v14['BackupFileName']
req.RegModuleName = v4['ModuleName']
req.MajorVersion = v3
req.MinorVersion = v11['MajorVersion']
v15 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v11['RegModuleName']
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v11['MinorVersion']
v16 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v6
req.BackupFileName = v9['RegModuleName']
req.MajorVersion = v8
req.MinorVersion = v5['MajorVersion']
v17 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v6
req.ModuleName = v17['BackupFileName']
req.RegModuleName = v7
req.MajorVersion = v15['MajorVersion']
req.MinorVersion = v11['MajorVersion']
v18 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v1
req.ModuleName = v15['RegModuleName']
req.RegModuleName = v12['BackupFileName']
req.MajorVersion = v5['MinorVersion']
req.MinorVersion = v4['MinorVersion']
v19 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v11['ModuleName']
req.MajorVersion = v8
req.MinorVersion = v14['MinorVersion']
v20 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v18['UNCServerName']
req.BackupFileName = v7
req.MajorVersion = v3
req.MinorVersion = v14['MinorVersion']
v21 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v6
req.ModuleName = v18['ModuleName']
req.RegModuleName = v7
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v12['MajorVersion']
v22 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v18['UNCServerName']
req.ModuleName = v7
req.RegModuleName = v9['RegModuleName']
req.MajorVersion = v22['MinorVersion']
req.MinorVersion = v5['MajorVersion']
v23 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v10['RegModuleName']
req.RegModuleName = v19['RegModuleName']
req.MajorVersion = v3
req.MinorVersion = v3
v24 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v2
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v12['MinorVersion']
v25 = dce.request(req)

v26 = 2147483643.5

req = ElfrRegisterEventSourceA()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v11['RegModuleName']
req.RegModuleName = v16['BackupFileName']
req.MajorVersion = v26
req.MinorVersion = v22['MajorVersion']
v27 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v16['UNCServerName']
req.BackupFileName = v24['ModuleName']
req.MajorVersion = v26
req.MinorVersion = v25['MajorVersion']
v28 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v21['UNCServerName']
req.ModuleName = v22['ModuleName']
req.RegModuleName = v7
req.MajorVersion = v5['MajorVersion']
req.MinorVersion = v16['MinorVersion']
v29 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v19['UNCServerName']
req.BackupFileName = v24['RegModuleName']
req.MajorVersion = v23['MajorVersion']
req.MinorVersion = v25['MinorVersion']
v30 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v20['BackupFileName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v26
v31 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v18['UNCServerName']
req.BackupFileName = v18['RegModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v29['MajorVersion']
v32 = dce.request(req)

v33 = 4294967291

req = ElfrOpenBELW()
req.UNCServerName = v9['UNCServerName']
req.BackupFileName = v21['BackupFileName']
req.MajorVersion = v16['MinorVersion']
req.MinorVersion = v33
v34 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v31['UNCServerName']
req.ModuleName = v15['ModuleName']
req.RegModuleName = v27['RegModuleName']
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v17['MinorVersion']
v35 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v23['UNCServerName']
req.BackupFileName = v23['RegModuleName']
req.MajorVersion = v11['MinorVersion']
req.MinorVersion = v21['MajorVersion']
v36 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v17['BackupFileName']
req.RegModuleName = v21['BackupFileName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v35['MajorVersion']
v37 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v11['UNCServerName']
req.BackupFileName = v35['RegModuleName']
req.MajorVersion = v34['MajorVersion']
req.MinorVersion = v34['MinorVersion']
v38 = dce.request(req)

v39 = 2147483637.5

req = ElfrOpenELW()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v17['BackupFileName']
req.RegModuleName = v7
req.MajorVersion = v28['MajorVersion']
req.MinorVersion = v39
v40 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v32['UNCServerName']
req.ModuleName = v40['ModuleName']
req.RegModuleName = v29['ModuleName']
req.MajorVersion = v37['MinorVersion']
req.MinorVersion = v38['MinorVersion']
v41 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v22['UNCServerName']
req.ModuleName = v7
req.RegModuleName = v22['RegModuleName']
req.MajorVersion = v10['MajorVersion']
req.MinorVersion = v30['MinorVersion']
v42 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v24['RegModuleName']
req.RegModuleName = v10['RegModuleName']
req.MajorVersion = v19['MinorVersion']
req.MinorVersion = v15['MajorVersion']
v43 = dce.request(req)

v44 = RPC_UNICODE_STRING()
v44['Length'] = 2050.96875
v44['MaximumLength'] = 8194.875
v44['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenELW()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v44
req.RegModuleName = v23['ModuleName']
req.MajorVersion = v40['MinorVersion']
req.MinorVersion = v37['MinorVersion']
v45 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v36['UNCServerName']
req.BackupFileName = v29['RegModuleName']
req.MajorVersion = v8
req.MinorVersion = v45['MinorVersion']
v46 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v29['UNCServerName']
req.ModuleName = v45['ModuleName']
req.RegModuleName = v29['RegModuleName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v29['MinorVersion']
v47 = dce.request(req)

v48 = 134217736.96875

req = ElfrOpenELW()
req.UNCServerName = v32['UNCServerName']
req.ModuleName = v29['RegModuleName']
req.RegModuleName = v23['ModuleName']
req.MajorVersion = v9['MajorVersion']
req.MinorVersion = v48
v49 = dce.request(req)

v50 = RPC_STRING()
v50['Length'] = 4584502319604871398
v50['MaximumLength'] = 65529
v50['Buffer'] = None # TODO UC_CHAR_ARRAY


req = ElfrOpenELA()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v50
req.MajorVersion = v19['MinorVersion']
req.MinorVersion = v37['MajorVersion']
v51 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v9['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v32['BackupFileName']
req.MajorVersion = v17['MajorVersion']
req.MinorVersion = v51['MajorVersion']
v52 = dce.request(req)

v53 = 536870919.875

req = ElfrOpenBELA()
req.UNCServerName = v13
req.BackupFileName = v51['RegModuleName']
req.MajorVersion = v53
req.MinorVersion = v35['MajorVersion']
v54 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v18['UNCServerName']
req.BackupFileName = v22['ModuleName']
req.MajorVersion = v17['MajorVersion']
req.MinorVersion = v41['MajorVersion']
v55 = dce.request(req)

v56 = 4294967287

req = ElfrOpenBELW()
req.UNCServerName = v49['UNCServerName']
req.BackupFileName = v47['ModuleName']
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v56
v57 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v40['UNCServerName']
req.ModuleName = v7
req.RegModuleName = v40['ModuleName']
req.MajorVersion = v17['MajorVersion']
req.MinorVersion = v47['MinorVersion']
v58 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v20['UNCServerName']
req.ModuleName = v20['BackupFileName']
req.RegModuleName = v19['ModuleName']
req.MajorVersion = v43['MinorVersion']
req.MinorVersion = v36['MajorVersion']
v59 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v52['UNCServerName']
req.BackupFileName = v40['ModuleName']
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v19['MajorVersion']
v60 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v15['ModuleName']
req.RegModuleName = v28['BackupFileName']
req.MajorVersion = v18['MajorVersion']
req.MinorVersion = v46['MinorVersion']
v61 = dce.request(req)

v62 = b'\xff\xfe\x14\x00\x14\x00\x14\x00\x14\x00\x14\x00\x14\x00\x00\x00\x00\x00'.decode('utf-16')

v63 = 2147483637.5

req = ElfrOpenELA()
req.UNCServerName = v62
req.ModuleName = v35['RegModuleName']
req.RegModuleName = v35['RegModuleName']
req.MajorVersion = v63
req.MinorVersion = v35['MajorVersion']
v64 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v62
req.ModuleName = v31['ModuleName']
req.RegModuleName = v64['RegModuleName']
req.MajorVersion = v10['MajorVersion']
req.MinorVersion = v45['MajorVersion']
v65 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v24['UNCServerName']
req.ModuleName = v4['ModuleName']
req.RegModuleName = v30['BackupFileName']
req.MajorVersion = v60['MinorVersion']
req.MinorVersion = v18['MajorVersion']
v66 = dce.request(req)

v67 = 268435462.9375

req = ElfrOpenELW()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v41['RegModuleName']
req.RegModuleName = v41['ModuleName']
req.MajorVersion = v67
req.MinorVersion = v8
v68 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v28['UNCServerName']
req.BackupFileName = v59['RegModuleName']
req.MajorVersion = v58['MajorVersion']
req.MinorVersion = v11['MinorVersion']
v69 = dce.request(req)

v70 = 10418893593947693832

req = ElfrOpenELW()
req.UNCServerName = v60['UNCServerName']
req.ModuleName = v42['ModuleName']
req.RegModuleName = v45['ModuleName']
req.MajorVersion = v37['MajorVersion']
req.MinorVersion = v70
v71 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v20['UNCServerName']
req.BackupFileName = v35['ModuleName']
req.MajorVersion = v66['MajorVersion']
req.MinorVersion = v58['MajorVersion']
v72 = dce.request(req)

v73 = RPC_UNICODE_STRING()
v73['Length'] = 32767.5
v73['MaximumLength'] = 8186.875
v73['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenELW()
req.UNCServerName = v57['UNCServerName']
req.ModuleName = v37['RegModuleName']
req.RegModuleName = v73
req.MajorVersion = v60['MajorVersion']
req.MinorVersion = v37['MajorVersion']
v74 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v18['UNCServerName']
req.ModuleName = v9['RegModuleName']
req.RegModuleName = v68['RegModuleName']
req.MajorVersion = v35['MajorVersion']
req.MinorVersion = v10['MinorVersion']
v75 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v64['UNCServerName']
req.ModuleName = v61['RegModuleName']
req.RegModuleName = v66['ModuleName']
req.MajorVersion = v58['MinorVersion']
req.MinorVersion = v9['MajorVersion']
v76 = dce.request(req)

v77 = b'\xff\xfe%\x00\x00\x000\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenELW()
req.UNCServerName = v77
req.ModuleName = v18['RegModuleName']
req.RegModuleName = v68['ModuleName']
req.MajorVersion = v46['MajorVersion']
req.MinorVersion = v75['MinorVersion']
v78 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v24['UNCServerName']
req.BackupFileName = v35['RegModuleName']
req.MajorVersion = v31['MajorVersion']
req.MinorVersion = v36['MajorVersion']
v79 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v69['UNCServerName']
req.ModuleName = v51['RegModuleName']
req.RegModuleName = v50
req.MajorVersion = v27['MajorVersion']
req.MinorVersion = v40['MinorVersion']
v80 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v25['UNCServerName']
req.ModuleName = v19['ModuleName']
req.RegModuleName = v10['ModuleName']
req.MajorVersion = v24['MinorVersion']
req.MinorVersion = v23['MajorVersion']
v81 = dce.request(req)

v82 = RPC_UNICODE_STRING()
v82['Length'] = 21839.0
v82['MaximumLength'] = 65527
v82['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrRegisterEventSourceW()
req.UNCServerName = v40['UNCServerName']
req.ModuleName = v47['ModuleName']
req.RegModuleName = v82
req.MajorVersion = v35['MinorVersion']
req.MinorVersion = v21['MinorVersion']
v83 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v45['UNCServerName']
req.ModuleName = v73
req.RegModuleName = v45['ModuleName']
req.MajorVersion = v17['MinorVersion']
req.MinorVersion = v38['MajorVersion']
v84 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v46['UNCServerName']
req.BackupFileName = v73
req.MajorVersion = v51['MinorVersion']
req.MinorVersion = v72['MinorVersion']
v85 = dce.request(req)

v86 = RPC_UNICODE_STRING()
v86['Length'] = 9
v86['MaximumLength'] = 4091.9375
v86['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrRegisterEventSourceW()
req.UNCServerName = v71['UNCServerName']
req.ModuleName = v86
req.RegModuleName = v45['RegModuleName']
req.MajorVersion = v65['MinorVersion']
req.MinorVersion = v55['MajorVersion']
v87 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v23['UNCServerName']
req.BackupFileName = v52['ModuleName']
req.MajorVersion = v85['MinorVersion']
req.MinorVersion = v71['MinorVersion']
v88 = dce.request(req)

v89 = b"\xff\xfe'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00'\x00\x00\x00".decode('utf-16')

req = ElfrOpenELA()
req.UNCServerName = v89
req.ModuleName = v51['ModuleName']
req.RegModuleName = v79['BackupFileName']
req.MajorVersion = v87['MajorVersion']
req.MinorVersion = v51['MinorVersion']
v90 = dce.request(req)

v91 = b'\xff\xfe[\x00[\x00[\x00[\x00[\x00[\x00[\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrRegisterEventSourceA()
req.UNCServerName = v91
req.ModuleName = v66['RegModuleName']
req.RegModuleName = v15['RegModuleName']
req.MajorVersion = v49['MinorVersion']
req.MinorVersion = v47['MinorVersion']
v92 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v30['UNCServerName']
req.ModuleName = v14['BackupFileName']
req.RegModuleName = v65['ModuleName']
req.MajorVersion = v74['MinorVersion']
req.MinorVersion = v46['MajorVersion']
v93 = dce.request(req)

v94 = RPC_STRING()
v94['Length'] = 6175079613352738545
v94['MaximumLength'] = 32765.5
v94['Buffer'] = None # TODO UC_CHAR_ARRAY


req = ElfrOpenBELA()
req.UNCServerName = v93['UNCServerName']
req.BackupFileName = v94
req.MajorVersion = v68['MinorVersion']
req.MinorVersion = v46['MajorVersion']
v95 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v88['UNCServerName']
req.ModuleName = v83['RegModuleName']
req.RegModuleName = v23['ModuleName']
req.MajorVersion = v32['MajorVersion']
req.MinorVersion = v31['MajorVersion']
v96 = dce.request(req)

v97 = 2187554224

req = ElfrOpenBELW()
req.UNCServerName = v36['UNCServerName']
req.BackupFileName = v52['ModuleName']
req.MajorVersion = v88['MajorVersion']
req.MinorVersion = v97
v98 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v5['UNCServerName']
req.ModuleName = v61['ModuleName']
req.RegModuleName = v5['RegModuleName']
req.MajorVersion = v54['MinorVersion']
req.MinorVersion = v85['MinorVersion']
v99 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v59['UNCServerName']
req.ModuleName = v80['ModuleName']
req.RegModuleName = v19['RegModuleName']
req.MajorVersion = v84['MajorVersion']
req.MinorVersion = v36['MinorVersion']
v100 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v43['UNCServerName']
req.ModuleName = v11['RegModuleName']
req.RegModuleName = v92['ModuleName']
req.MajorVersion = v98['MinorVersion']
req.MinorVersion = v37['MinorVersion']
v101 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v81['UNCServerName']
req.ModuleName = v100['RegModuleName']
req.RegModuleName = v15['ModuleName']
req.MajorVersion = v39
req.MinorVersion = v96['MajorVersion']
v102 = dce.request(req)

v103 = 1431655761.0

req = ElfrOpenELA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v65['ModuleName']
req.RegModuleName = v11['ModuleName']
req.MajorVersion = v95['MinorVersion']
req.MinorVersion = v103
v104 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v46['UNCServerName']
req.ModuleName = v23['RegModuleName']
req.RegModuleName = v71['ModuleName']
req.MajorVersion = v87['MinorVersion']
req.MinorVersion = v101['MajorVersion']
v105 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v57['UNCServerName']
req.ModuleName = v58['RegModuleName']
req.RegModuleName = v47['RegModuleName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v97
v106 = dce.request(req)

v107 = 4406714337972463699

req = ElfrRegisterEventSourceW()
req.UNCServerName = v6
req.ModuleName = v42['RegModuleName']
req.RegModuleName = v49['RegModuleName']
req.MajorVersion = v107
req.MinorVersion = v28['MinorVersion']
v108 = dce.request(req)

v109 = b'\xff\xfe]\x00\x00\x00]\x00\x00\x00]\x00\x00\x00]\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrOpenELW()
req.UNCServerName = v109
req.ModuleName = v34['BackupFileName']
req.RegModuleName = v60['BackupFileName']
req.MajorVersion = v79['MinorVersion']
req.MinorVersion = v11['MinorVersion']
v110 = dce.request(req)

v111 = 4294967286

req = ElfrOpenBELA()
req.UNCServerName = v62
req.BackupFileName = v51['ModuleName']
req.MajorVersion = v103
req.MinorVersion = v111
v112 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v74['UNCServerName']
req.ModuleName = v37['ModuleName']
req.RegModuleName = v45['ModuleName']
req.MajorVersion = v24['MinorVersion']
req.MinorVersion = v99['MinorVersion']
v113 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v98['UNCServerName']
req.BackupFileName = v58['ModuleName']
req.MajorVersion = v100['MajorVersion']
req.MinorVersion = v14['MajorVersion']
v114 = dce.request(req)

v115 = 1073741829.75

req = ElfrOpenBELA()
req.UNCServerName = v10['UNCServerName']
req.BackupFileName = v12['BackupFileName']
req.MajorVersion = v115
req.MinorVersion = v51['MajorVersion']
v116 = dce.request(req)

v117 = 2036167218

req = ElfrOpenBELA()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v101['ModuleName']
req.MajorVersion = v92['MajorVersion']
req.MinorVersion = v117
v118 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v113['UNCServerName']
req.BackupFileName = v9['RegModuleName']
req.MajorVersion = v43['MajorVersion']
req.MinorVersion = v65['MinorVersion']
v119 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v106['UNCServerName']
req.ModuleName = v45['RegModuleName']
req.RegModuleName = v32['BackupFileName']
req.MajorVersion = v37['MinorVersion']
req.MinorVersion = v52['MinorVersion']
v120 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v99['UNCServerName']
req.BackupFileName = v64['RegModuleName']
req.MajorVersion = v83['MajorVersion']
req.MinorVersion = v78['MinorVersion']
v121 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v64['UNCServerName']
req.ModuleName = v38['BackupFileName']
req.RegModuleName = v20['BackupFileName']
req.MajorVersion = v49['MinorVersion']
req.MinorVersion = v58['MinorVersion']
v122 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v93['UNCServerName']
req.ModuleName = v99['RegModuleName']
req.RegModuleName = v14['BackupFileName']
req.MajorVersion = v72['MajorVersion']
req.MinorVersion = v96['MajorVersion']
v123 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v11['UNCServerName']
req.BackupFileName = v65['ModuleName']
req.MajorVersion = v120['MajorVersion']
req.MinorVersion = v22['MinorVersion']
v124 = dce.request(req)

v125 = 12097838795221964291

req = ElfrRegisterEventSourceW()
req.UNCServerName = v58['UNCServerName']
req.ModuleName = v47['RegModuleName']
req.RegModuleName = v36['BackupFileName']
req.MajorVersion = v61['MinorVersion']
req.MinorVersion = v125
v126 = dce.request(req)

v127 = 134217719.96875

req = ElfrOpenELW()
req.UNCServerName = v40['UNCServerName']
req.ModuleName = v40['ModuleName']
req.RegModuleName = v9['RegModuleName']
req.MajorVersion = v127
req.MinorVersion = v45['MinorVersion']
v128 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v101['RegModuleName']
req.MajorVersion = v59['MajorVersion']
req.MinorVersion = v46['MinorVersion']
v129 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v1
req.ModuleName = v50
req.RegModuleName = v19['ModuleName']
req.MajorVersion = v71['MinorVersion']
req.MinorVersion = v54['MajorVersion']
v130 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v124['UNCServerName']
req.ModuleName = v14['BackupFileName']
req.RegModuleName = v54['BackupFileName']
req.MajorVersion = v32['MinorVersion']
req.MinorVersion = v98['MinorVersion']
v131 = dce.request(req)

v132 = b'\xff\xfe]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00]\x00\x00\x00\x00\x00'.decode('utf-16')

req = ElfrRegisterEventSourceA()
req.UNCServerName = v132
req.ModuleName = v61['RegModuleName']
req.RegModuleName = v124['BackupFileName']
req.MajorVersion = v118['MinorVersion']
req.MinorVersion = v31['MajorVersion']
v133 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v59['UNCServerName']
req.BackupFileName = v24['ModuleName']
req.MajorVersion = v99['MajorVersion']
req.MinorVersion = v37['MajorVersion']
v134 = dce.request(req)

v135 = RPC_UNICODE_STRING()
v135['Length'] = 1258413529579676166
v135['MaximumLength'] = 4100.9375
v135['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenELW()
req.UNCServerName = v42['UNCServerName']
req.ModuleName = v135
req.RegModuleName = v22['ModuleName']
req.MajorVersion = v127
req.MinorVersion = v98['MinorVersion']
v136 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v13
req.ModuleName = v27['RegModuleName']
req.RegModuleName = v19['ModuleName']
req.MajorVersion = v114['MinorVersion']
req.MinorVersion = v99['MajorVersion']
v137 = dce.request(req)

