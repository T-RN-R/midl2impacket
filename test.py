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

v1 = "b'\xff\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')"

v2 = RPC_UNICODE_STRING()
v2['Length'] = 8193.875
v2['MaximumLength'] = 47155
v2['Buffer'] = None # TODO UC_WCHAR_ARRAY


v3 = 18278107141511364464

req = ElfrRegisterEventSourceW()
req.UNCServerName = v1
req.ModuleName = v2
req.RegModuleName = v2
req.MajorVersion = v3
req.MinorVersion = v3
v4 = dce.request(req)

v5 = STR()


v6 = RPC_STRING()
v6['Length'] = 2047.96875
v6['MaximumLength'] = 32770.5
v6['Buffer'] = None # TODO UC_CHAR_ARRAY


req = ElfrOpenELA()
req.UNCServerName = v5
req.ModuleName = v6
req.RegModuleName = v6
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v4['MinorVersion']
v7 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v5
req.BackupFileName = v6
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v3
v8 = dce.request(req)

v9 = 13106047992873025243

req = ElfrOpenELA()
req.UNCServerName = v5
req.ModuleName = v7['ModuleName']
req.RegModuleName = v8['BackupFileName']
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v9
v10 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v1
req.BackupFileName = v2
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v8['MajorVersion']
v11 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v11['UNCServerName']
req.ModuleName = v11['BackupFileName']
req.RegModuleName = v4['RegModuleName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v10['MinorVersion']
v12 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v7['RegModuleName']
req.RegModuleName = v8['BackupFileName']
req.MajorVersion = v7['MajorVersion']
req.MinorVersion = v12['MajorVersion']
v13 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v11['BackupFileName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v11['MinorVersion']
v14 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v7['UNCServerName']
req.BackupFileName = v7['RegModuleName']
req.MajorVersion = v11['MinorVersion']
req.MinorVersion = v11['MinorVersion']
v15 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v13['UNCServerName']
req.ModuleName = v7['ModuleName']
req.RegModuleName = v15['BackupFileName']
req.MajorVersion = v9
req.MinorVersion = v12['MajorVersion']
v16 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v7['ModuleName']
req.RegModuleName = v6
req.MajorVersion = v11['MajorVersion']
req.MinorVersion = v12['MinorVersion']
v17 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v7['UNCServerName']
req.BackupFileName = v10['RegModuleName']
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v17['MinorVersion']
v18 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v2
req.MajorVersion = v17['MinorVersion']
req.MinorVersion = v8['MajorVersion']
v19 = dce.request(req)

v20 = RPC_UNICODE_STRING()
v20['Length'] = 32759.5
v20['MaximumLength'] = 9
v20['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenBELW()
req.UNCServerName = v12['UNCServerName']
req.BackupFileName = v20
req.MajorVersion = v11['MinorVersion']
req.MinorVersion = v12['MajorVersion']
v21 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v10['ModuleName']
req.RegModuleName = v16['RegModuleName']
req.MajorVersion = v15['MinorVersion']
req.MinorVersion = v19['MinorVersion']
v22 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v5
req.BackupFileName = v8['BackupFileName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v17['MajorVersion']
v23 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v4['UNCServerName']
req.ModuleName = v11['BackupFileName']
req.RegModuleName = v19['RegModuleName']
req.MajorVersion = v15['MajorVersion']
req.MinorVersion = v15['MajorVersion']
v24 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v10['UNCServerName']
req.ModuleName = v16['RegModuleName']
req.RegModuleName = v13['ModuleName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v15['MajorVersion']
v25 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v5
req.ModuleName = v22['RegModuleName']
req.RegModuleName = v22['RegModuleName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v9
v26 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v13['UNCServerName']
req.BackupFileName = v25['ModuleName']
req.MajorVersion = v24['MajorVersion']
req.MinorVersion = v25['MajorVersion']
v27 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v17['UNCServerName']
req.ModuleName = v16['RegModuleName']
req.RegModuleName = v10['RegModuleName']
req.MajorVersion = v19['MajorVersion']
req.MinorVersion = v18['MinorVersion']
v28 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v14['UNCServerName']
req.BackupFileName = v2
req.MajorVersion = v19['MinorVersion']
req.MinorVersion = v25['MinorVersion']
v29 = dce.request(req)

v30 = 17092851642722576343

req = ElfrRegisterEventSourceA()
req.UNCServerName = v27['UNCServerName']
req.ModuleName = v7['ModuleName']
req.RegModuleName = v7['ModuleName']
req.MajorVersion = v30
req.MinorVersion = v26['MinorVersion']
v31 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v14['RegModuleName']
req.RegModuleName = v4['RegModuleName']
req.MajorVersion = v14['MajorVersion']
req.MinorVersion = v22['MinorVersion']
v32 = dce.request(req)

v33 = RPC_UNICODE_STRING()
v33['Length'] = 8
v33['MaximumLength'] = 16388.75
v33['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenELW()
req.UNCServerName = v32['UNCServerName']
req.ModuleName = v33
req.RegModuleName = v32['RegModuleName']
req.MajorVersion = v25['MinorVersion']
req.MinorVersion = v4['MajorVersion']
v34 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v16['UNCServerName']
req.ModuleName = v18['BackupFileName']
req.RegModuleName = v13['RegModuleName']
req.MajorVersion = v4['MinorVersion']
req.MinorVersion = v8['MajorVersion']
v35 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v13['UNCServerName']
req.ModuleName = v13['RegModuleName']
req.RegModuleName = v13['RegModuleName']
req.MajorVersion = v30
req.MinorVersion = v10['MajorVersion']
v36 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v18['UNCServerName']
req.BackupFileName = v36['ModuleName']
req.MajorVersion = v21['MajorVersion']
req.MinorVersion = v3
v37 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v13['UNCServerName']
req.ModuleName = v13['RegModuleName']
req.RegModuleName = v36['ModuleName']
req.MajorVersion = v37['MajorVersion']
req.MinorVersion = v23['MajorVersion']
v38 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v22['UNCServerName']
req.BackupFileName = v38['ModuleName']
req.MajorVersion = v3
req.MinorVersion = v3
v39 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v36['UNCServerName']
req.ModuleName = v18['BackupFileName']
req.RegModuleName = v35['ModuleName']
req.MajorVersion = v36['MajorVersion']
req.MinorVersion = v8['MajorVersion']
v40 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v19['UNCServerName']
req.ModuleName = v34['ModuleName']
req.RegModuleName = v11['BackupFileName']
req.MajorVersion = v22['MajorVersion']
req.MinorVersion = v31['MinorVersion']
v41 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v34['UNCServerName']
req.ModuleName = v19['RegModuleName']
req.RegModuleName = v14['RegModuleName']
req.MajorVersion = v27['MajorVersion']
req.MinorVersion = v24['MinorVersion']
v42 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v36['UNCServerName']
req.ModuleName = v26['RegModuleName']
req.RegModuleName = v35['RegModuleName']
req.MajorVersion = v24['MinorVersion']
req.MinorVersion = v9
v43 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v13['UNCServerName']
req.BackupFileName = v18['BackupFileName']
req.MajorVersion = v7['MinorVersion']
req.MinorVersion = v14['MajorVersion']
v44 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v29['UNCServerName']
req.ModuleName = v33
req.RegModuleName = v21['BackupFileName']
req.MajorVersion = v9
req.MinorVersion = v10['MajorVersion']
v45 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v22['UNCServerName']
req.ModuleName = v17['RegModuleName']
req.RegModuleName = v8['BackupFileName']
req.MajorVersion = v3
req.MinorVersion = v7['MinorVersion']
v46 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v40['UNCServerName']
req.ModuleName = v38['RegModuleName']
req.RegModuleName = v31['ModuleName']
req.MajorVersion = v42['MinorVersion']
req.MinorVersion = v24['MinorVersion']
v47 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v45['UNCServerName']
req.ModuleName = v2
req.RegModuleName = v12['RegModuleName']
req.MajorVersion = v15['MajorVersion']
req.MinorVersion = v30
v48 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v27['UNCServerName']
req.ModuleName = v38['ModuleName']
req.RegModuleName = v36['ModuleName']
req.MajorVersion = v30
req.MinorVersion = v40['MajorVersion']
v49 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v24['UNCServerName']
req.BackupFileName = v45['RegModuleName']
req.MajorVersion = v45['MajorVersion']
req.MinorVersion = v16['MajorVersion']
v50 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v45['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v42['RegModuleName']
req.MajorVersion = v32['MinorVersion']
req.MinorVersion = v9
v51 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v34['UNCServerName']
req.BackupFileName = v29['BackupFileName']
req.MajorVersion = v40['MinorVersion']
req.MinorVersion = v17['MajorVersion']
v52 = dce.request(req)

v53 = 2147483638.5

req = ElfrRegisterEventSourceW()
req.UNCServerName = v29['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v45['ModuleName']
req.MajorVersion = v39['MajorVersion']
req.MinorVersion = v53
v54 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v41['ModuleName']
req.RegModuleName = v24['ModuleName']
req.MajorVersion = v31['MinorVersion']
req.MinorVersion = v16['MinorVersion']
v55 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v28['UNCServerName']
req.ModuleName = v10['ModuleName']
req.RegModuleName = v47['ModuleName']
req.MajorVersion = v10['MajorVersion']
req.MinorVersion = v42['MajorVersion']
v56 = dce.request(req)

v57 = 3730965423

req = ElfrOpenELW()
req.UNCServerName = v32['UNCServerName']
req.ModuleName = v45['RegModuleName']
req.RegModuleName = v20
req.MajorVersion = v57
req.MinorVersion = v29['MajorVersion']
v58 = dce.request(req)

v59 = RPC_UNICODE_STRING()
v59['Length'] = 11841
v59['MaximumLength'] = 16052720902978175627
v59['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenBELW()
req.UNCServerName = v45['UNCServerName']
req.BackupFileName = v59
req.MajorVersion = v22['MinorVersion']
req.MinorVersion = v35['MajorVersion']
v60 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v24['RegModuleName']
req.MajorVersion = v57
req.MinorVersion = v8['MajorVersion']
v61 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v51['UNCServerName']
req.ModuleName = v50['BackupFileName']
req.RegModuleName = v45['RegModuleName']
req.MajorVersion = v44['MinorVersion']
req.MinorVersion = v51['MajorVersion']
v62 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v23['UNCServerName']
req.ModuleName = v22['RegModuleName']
req.RegModuleName = v26['ModuleName']
req.MajorVersion = v12['MajorVersion']
req.MinorVersion = v49['MinorVersion']
v63 = dce.request(req)

v64 = 268435448.9375

req = ElfrRegisterEventSourceW()
req.UNCServerName = v12['UNCServerName']
req.ModuleName = v41['ModuleName']
req.RegModuleName = v45['ModuleName']
req.MajorVersion = v64
req.MinorVersion = v14['MinorVersion']
v65 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v29['UNCServerName']
req.ModuleName = v32['RegModuleName']
req.RegModuleName = v50['BackupFileName']
req.MajorVersion = v39['MajorVersion']
req.MinorVersion = v64
v66 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v44['UNCServerName']
req.BackupFileName = v63['RegModuleName']
req.MajorVersion = v51['MinorVersion']
req.MinorVersion = v17['MajorVersion']
v67 = dce.request(req)

v68 = "b'\xff\xfe=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00=\x00\x00\x00\x00\x00\x00\x00'.decode('utf-16')"

req = ElfrOpenBELW()
req.UNCServerName = v68
req.BackupFileName = v52['BackupFileName']
req.MajorVersion = v56['MajorVersion']
req.MinorVersion = v41['MajorVersion']
v69 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v60['UNCServerName']
req.ModuleName = v21['BackupFileName']
req.RegModuleName = v4['ModuleName']
req.MajorVersion = v52['MinorVersion']
req.MinorVersion = v21['MinorVersion']
v70 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v8['UNCServerName']
req.ModuleName = v56['RegModuleName']
req.RegModuleName = v28['RegModuleName']
req.MajorVersion = v18['MajorVersion']
req.MinorVersion = v49['MinorVersion']
v71 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v42['UNCServerName']
req.ModuleName = v33
req.RegModuleName = v60['BackupFileName']
req.MajorVersion = v41['MinorVersion']
req.MinorVersion = v22['MajorVersion']
v72 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v66['UNCServerName']
req.BackupFileName = v48['ModuleName']
req.MajorVersion = v43['MajorVersion']
req.MinorVersion = v50['MinorVersion']
v73 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v18['UNCServerName']
req.ModuleName = v40['RegModuleName']
req.RegModuleName = v40['RegModuleName']
req.MajorVersion = v29['MajorVersion']
req.MinorVersion = v64
v74 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v26['UNCServerName']
req.BackupFileName = v17['ModuleName']
req.MajorVersion = v30
req.MinorVersion = v27['MajorVersion']
v75 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v4['UNCServerName']
req.BackupFileName = v34['ModuleName']
req.MajorVersion = v52['MinorVersion']
req.MinorVersion = v7['MajorVersion']
v76 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v60['UNCServerName']
req.ModuleName = v59
req.RegModuleName = v34['ModuleName']
req.MajorVersion = v16['MajorVersion']
req.MinorVersion = v48['MajorVersion']
v77 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v54['UNCServerName']
req.ModuleName = v45['RegModuleName']
req.RegModuleName = v33
req.MajorVersion = v30
req.MinorVersion = v54['MajorVersion']
v78 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v21['UNCServerName']
req.ModuleName = v51['ModuleName']
req.RegModuleName = v4['RegModuleName']
req.MajorVersion = v47['MinorVersion']
req.MinorVersion = v62['MajorVersion']
v79 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v52['UNCServerName']
req.BackupFileName = v24['RegModuleName']
req.MajorVersion = v74['MinorVersion']
req.MinorVersion = v28['MinorVersion']
v80 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v68
req.BackupFileName = v62['RegModuleName']
req.MajorVersion = v55['MajorVersion']
req.MinorVersion = v36['MajorVersion']
v81 = dce.request(req)

v82 = RPC_UNICODE_STRING()
v82['Length'] = 2039.96875
v82['MaximumLength'] = 0
v82['Buffer'] = None # TODO UC_WCHAR_ARRAY


req = ElfrOpenBELW()
req.UNCServerName = v41['UNCServerName']
req.BackupFileName = v82
req.MajorVersion = v29['MajorVersion']
req.MinorVersion = v4['MinorVersion']
v83 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v62['UNCServerName']
req.ModuleName = v4['RegModuleName']
req.RegModuleName = v19['ModuleName']
req.MajorVersion = v35['MinorVersion']
req.MinorVersion = v31['MajorVersion']
v84 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v14['UNCServerName']
req.ModuleName = v59
req.RegModuleName = v14['ModuleName']
req.MajorVersion = v8['MinorVersion']
req.MinorVersion = v19['MajorVersion']
v85 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v46['UNCServerName']
req.ModuleName = v10['ModuleName']
req.RegModuleName = v23['BackupFileName']
req.MajorVersion = v43['MajorVersion']
req.MinorVersion = v42['MinorVersion']
v86 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v13['UNCServerName']
req.ModuleName = v25['RegModuleName']
req.RegModuleName = v22['RegModuleName']
req.MajorVersion = v28['MinorVersion']
req.MinorVersion = v52['MajorVersion']
v87 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v27['UNCServerName']
req.ModuleName = v16['ModuleName']
req.RegModuleName = v35['RegModuleName']
req.MajorVersion = v32['MajorVersion']
req.MinorVersion = v69['MajorVersion']
v88 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v62['UNCServerName']
req.ModuleName = v72['RegModuleName']
req.RegModuleName = v55['ModuleName']
req.MajorVersion = v65['MajorVersion']
req.MinorVersion = v3
v89 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v71['UNCServerName']
req.ModuleName = v67['BackupFileName']
req.RegModuleName = v71['RegModuleName']
req.MajorVersion = v34['MajorVersion']
req.MinorVersion = v48['MajorVersion']
v90 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v50['UNCServerName']
req.BackupFileName = v78['ModuleName']
req.MajorVersion = v85['MinorVersion']
req.MinorVersion = v15['MinorVersion']
v91 = dce.request(req)

v92 = 3441416113734018898

req = ElfrRegisterEventSourceW()
req.UNCServerName = v60['UNCServerName']
req.ModuleName = v91['BackupFileName']
req.RegModuleName = v84['RegModuleName']
req.MajorVersion = v92
req.MinorVersion = v11['MajorVersion']
v93 = dce.request(req)

v94 = STR()


req = ElfrRegisterEventSourceA()
req.UNCServerName = v94
req.ModuleName = v25['ModuleName']
req.RegModuleName = v35['ModuleName']
req.MajorVersion = v4['MajorVersion']
req.MinorVersion = v56['MinorVersion']
v95 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v1
req.ModuleName = v77['ModuleName']
req.RegModuleName = v4['ModuleName']
req.MajorVersion = v44['MajorVersion']
req.MinorVersion = v31['MajorVersion']
v96 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v78['UNCServerName']
req.ModuleName = v70['ModuleName']
req.RegModuleName = v14['RegModuleName']
req.MajorVersion = v25['MinorVersion']
req.MinorVersion = v4['MajorVersion']
v97 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v91['UNCServerName']
req.ModuleName = v62['ModuleName']
req.RegModuleName = v79['RegModuleName']
req.MajorVersion = v25['MajorVersion']
req.MinorVersion = v91['MajorVersion']
v98 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v54['UNCServerName']
req.ModuleName = v24['ModuleName']
req.RegModuleName = v82
req.MajorVersion = v11['MajorVersion']
req.MinorVersion = v98['MinorVersion']
v99 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v26['RegModuleName']
req.RegModuleName = v13['RegModuleName']
req.MajorVersion = v67['MajorVersion']
req.MinorVersion = v51['MajorVersion']
v100 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v62['UNCServerName']
req.ModuleName = v65['ModuleName']
req.RegModuleName = v83['BackupFileName']
req.MajorVersion = v67['MinorVersion']
req.MinorVersion = v98['MajorVersion']
v101 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v37['UNCServerName']
req.ModuleName = v40['RegModuleName']
req.RegModuleName = v40['ModuleName']
req.MajorVersion = v73['MinorVersion']
req.MinorVersion = v14['MinorVersion']
v102 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v74['UNCServerName']
req.BackupFileName = v63['ModuleName']
req.MajorVersion = v87['MinorVersion']
req.MinorVersion = v36['MajorVersion']
v103 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v100['UNCServerName']
req.ModuleName = v8['BackupFileName']
req.RegModuleName = v86['ModuleName']
req.MajorVersion = v90['MinorVersion']
req.MinorVersion = v15['MajorVersion']
v104 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v22['UNCServerName']
req.BackupFileName = v31['RegModuleName']
req.MajorVersion = v61['MajorVersion']
req.MinorVersion = v91['MajorVersion']
v105 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v86['UNCServerName']
req.ModuleName = v35['RegModuleName']
req.RegModuleName = v17['RegModuleName']
req.MajorVersion = v39['MajorVersion']
req.MinorVersion = v37['MinorVersion']
v106 = dce.request(req)

req = ElfrOpenELA()
req.UNCServerName = v75['UNCServerName']
req.ModuleName = v28['ModuleName']
req.RegModuleName = v56['ModuleName']
req.MajorVersion = v90['MajorVersion']
req.MinorVersion = v96['MinorVersion']
v107 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v15['UNCServerName']
req.BackupFileName = v22['RegModuleName']
req.MajorVersion = v56['MinorVersion']
req.MinorVersion = v17['MajorVersion']
v108 = dce.request(req)

req = ElfrRegisterEventSourceW()
req.UNCServerName = v78['UNCServerName']
req.ModuleName = v29['BackupFileName']
req.RegModuleName = v42['ModuleName']
req.MajorVersion = v28['MajorVersion']
req.MinorVersion = v10['MajorVersion']
v109 = dce.request(req)

v110 = 1

req = ElfrRegisterEventSourceA()
req.UNCServerName = v103['UNCServerName']
req.ModuleName = v90['ModuleName']
req.RegModuleName = v49['ModuleName']
req.MajorVersion = v110
req.MinorVersion = v109['MajorVersion']
v111 = dce.request(req)

v112 = RPC_STRING()
v112['Length'] = 4085.9375
v112['MaximumLength'] = 4097.9375
v112['Buffer'] = None # TODO UC_CHAR_ARRAY


v113 = 134217726.96875

req = ElfrOpenELA()
req.UNCServerName = v7['UNCServerName']
req.ModuleName = v112
req.RegModuleName = v56['ModuleName']
req.MajorVersion = v113
req.MinorVersion = v97['MajorVersion']
v114 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v50['UNCServerName']
req.BackupFileName = v32['RegModuleName']
req.MajorVersion = v53
req.MinorVersion = v57
v115 = dce.request(req)

req = ElfrOpenBELW()
req.UNCServerName = v14['UNCServerName']
req.BackupFileName = v99['RegModuleName']
req.MajorVersion = v26['MinorVersion']
req.MinorVersion = v69['MinorVersion']
v116 = dce.request(req)

req = ElfrOpenELW()
req.UNCServerName = v115['UNCServerName']
req.ModuleName = v93['ModuleName']
req.RegModuleName = v54['ModuleName']
req.MajorVersion = v41['MajorVersion']
req.MinorVersion = v56['MinorVersion']
v117 = dce.request(req)

req = ElfrRegisterEventSourceA()
req.UNCServerName = v106['UNCServerName']
req.ModuleName = v37['BackupFileName']
req.RegModuleName = v22['ModuleName']
req.MajorVersion = v90['MinorVersion']
req.MinorVersion = v102['MinorVersion']
v118 = dce.request(req)

req = ElfrOpenBELA()
req.UNCServerName = v63['UNCServerName']
req.BackupFileName = v106['RegModuleName']
req.MajorVersion = v10['MinorVersion']
req.MinorVersion = v16['MinorVersion']
v119 = dce.request(req)

v120 = RPC_STRING()
v120['Length'] = 21842.0
v120['MaximumLength'] = 21853.0
v120['Buffer'] = None # TODO UC_CHAR_ARRAY


req = ElfrRegisterEventSourceA()
req.UNCServerName = v15['UNCServerName']
req.ModuleName = v114['ModuleName']
req.RegModuleName = v120
req.MajorVersion = v58['MinorVersion']
req.MinorVersion = v19['MinorVersion']
v121 = dce.request(req)

