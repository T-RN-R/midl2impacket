
from fuzzer.midl import *
from fuzzer.core import *

class DNSSRV_RPC_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : ('PBYTE', None),2 : ('DWORD', None),3 : ('PCHAR', None),4 : ('PWCHAR_T', None),5 : ('PIP4_ARRAY', None),6 : ('PDNS_RPC_BUFFER', None),7 : ('PDNS_RPC_SERVER_INFO_W2K', None),8 : ('PDNSSRV_STATS', None),9 : ('PDNS_RPC_FORWARDERS_W2K', None),10 : ('PDNS_RPC_ZONE_W2K', None),11 : ('PDNS_RPC_ZONE_INFO_W2K', None),12 : ('PDNS_RPC_ZONE_SECONDARIES_W2K', None),13 : ('PDNS_RPC_ZONE_DATABASE_W2K', None),14 : ('PDNS_RPC_ZONE_CREATE_INFO_W2K', None),15 : ('PDNS_RPC_NAME_AND_PARAM', None),16 : ('PDNS_RPC_ZONE_LIST_W2K', None),17 : ('PDNS_RPC_SERVER_INFO_DOTNET', None),18 : ('PDNS_RPC_FORWARDERS_DOTNET', None),19 : ('PDNS_RPC_ZONE', None),20 : ('PDNS_RPC_ZONE_INFO_DOTNET', None),21 : ('PDNS_RPC_ZONE_SECONDARIES_DOTNET', None),22 : ('PDNS_RPC_ZONE_DATABASE', None),23 : ('PDNS_RPC_ZONE_CREATE_INFO_DOTNET', None),24 : ('PDNS_RPC_ZONE_LIST', None),25 : ('PDNS_RPC_ZONE_EXPORT_INFO', None),26 : ('PDNS_RPC_DP_INFO', None),27 : ('PDNS_RPC_DP_ENUM', None),28 : ('PDNS_RPC_DP_LIST', None),29 : ('PDNS_RPC_ENLIST_DP', None),30 : ('PDNS_RPC_ZONE_CHANGE_DP', None),31 : ('PDNS_RPC_ENUM_ZONES_FILTER', None),32 : ('PDNS_ADDR_ARRAY', None),33 : ('PDNS_RPC_SERVER_INFO', None),34 : ('PDNS_RPC_ZONE_CREATE_INFO', None),35 : ('PDNS_RPC_FORWARDERS', None),36 : ('PDNS_RPC_ZONE_SECONDARIES', None),37 : ('PDNS_RPC_IP_VALIDATE', None),38 : ('PDNS_RPC_ZONE_INFO', None),39 : ('PDNS_RPC_AUTOCONFIGURE', None),40 : ('PDNS_RPC_UTF8_STRING_LIST', None),41 : ('PDNS_RPC_UNICODE_STRING_LIST', None),42 : ('PDNS_RPC_SKD', None),43 : ('PDNS_RPC_SKD_LIST', None),44 : ('PDNS_RPC_SKD_STATE', None),45 : ('PDNS_RPC_SIGNING_VALIDATION_ERROR', None),46 : ('PDNS_RPC_TRUST_POINT_LIST', None),47 : ('PDNS_RPC_TRUST_ANCHOR_LIST', None),48 : ('PDNS_RPC_ZONE_DNSSEC_SETTINGS', None),49 : ('PDNS_RPC_ENUM_ZONE_SCOPE_LIST', None),50 : ('PDNS_RPC_ZONE_STATS_V1', None),51 : ('PDNS_RPC_ZONE_SCOPE_CREATE_INFO_V1', None),52 : ('PDNS_RPC_ZONE_SCOPE_INFO_V1', None),53 : ('PDNS_RPC_ENUM_SCOPE_LIST', None),54 : ('PDNS_RPC_CLIENT_SUBNET_RECORD', None),55 : ('PDNS_RPC_POLICY', None),56 : ('PDNS_RPC_POLICY_NAME', None),57 : ('PDNS_RPC_ENUMERATE_POLICY_LIST', None),58 : ('PDNS_RPC_RRL_PARAMS', None),59 : ('PDNS_RPC_VIRTUALIZATION_INSTANCE', None),60 : ('PDNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST', None),}

    
interface_0 = Interface("50abc2a4-574d-40b3-9d66-ee4fd5fba076", "5.0",[
Method("R_DnssrvOperation",
In(LPCWSTR),
In(LPCSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),
Method("R_DnssrvQuery",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvComplexOperation",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvEnumRecords",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),
Method("R_DnssrvUpdateRecord",
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),
Method("R_DnssrvOperation2",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),
Method("R_DnssrvQuery2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvComplexOperation2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvEnumRecords2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),
Method("R_DnssrvUpdateRecord2",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),
Method("R_DnssrvUpdateRecord3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),
Method("R_DnssrvEnumRecords3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),
Method("R_DnssrvOperation3",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),
Method("R_DnssrvQuery3",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvComplexOperation3",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvOperation4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(DWORD),
In(LPCSTR),
In(DWORD),
In(DNSSRV_RPC_UNION),
),
Method("R_DnssrvQuery4",
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
Out(PDWORD),
Out(PDNSSRV_RPC_UNION),
),
Method("R_DnssrvUpdateRecord4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(PDNS_RPC_RECORD),
In(PDNS_RPC_RECORD),
),
Method("R_DnssrvEnumRecords4",
In(HANDLE_T),
In(DWORD),
In(DWORD),
In(LPCWSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCWSTR),
In(LPCSTR),
In(LPCSTR),
In(WORD),
In(DWORD),
In(LPCSTR),
In(LPCSTR),
Out(PDWORD),
Out(PPBYTE),
),
])
