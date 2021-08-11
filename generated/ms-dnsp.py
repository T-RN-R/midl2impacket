"""
Generated from MIDL2Impacket.py
"""


from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG
CONST_UNSIGNED_LONG = NDRULONG
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER

#################################################################################

#"ms-dtyp.idl"

#################################################################################

#################################################################################

#TYPEDEFS

#################################################################################

WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PBOOL = INT
LPBOOL = INT
BYTE = UNSIGNED_CHAR
PBYTE = UNSIGNED_CHAR
LPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PBOOLEAN = BYTE
WCHAR = WCHAR_T
PWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PDWORD = UNSIGNED_LONG
LPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
LPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = CONST_WCHAR_T
LMSTR = WCHAR
LONG = LONG
PLONG = LONG
LPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = __INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PLONG64 = SIGNED___INT64
LPCSTR = CONST_CHAR
LPCVOID = CONST_VOID
LPCWSTR = CONST_WCHAR_T
PSTR = CHAR
LPSTR = CHAR
LPWSTR = WCHAR_T
PWSTR = WCHAR_T
NET_API_STATUS = DWORD
NTSTATUS = LONG
PCONTEXT_HANDLE = VOID
PPCONTEXT_HANDLE = PCONTEXT_HANDLE
QWORD = UNSIGNED___INT64
RPC_BINDING_HANDLE = VOID
STRING = UCHAR
UINT = UNSIGNED_INT
UINT8 = UNSIGNED_CHAR
UINT16 = UNSIGNED_SHORT
UINT32 = UNSIGNED_INT
UINT64 = UNSIGNED___INT64
ULONG = UNSIGNED_LONG
PULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PVOID = VOID
LPVOID = VOID
WORD = UNSIGNED_SHORT
PWORD = UNSIGNED_SHORT
LPWORD = UNSIGNED_SHORT

class FILETIME(NDRSTRUCT):
    structure = (
        ('dwLowDateTime', DWORD),('dwHighDateTime', DWORD),
    )
class PFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    
class LPFILETIME(NDRPOINTER):
    referent = (
        ('Data', FILETIME),
    )    


class GUID(NDRSTRUCT):
    structure = (
        ('Data1', UNSIGNED_LONG),('Data2', UNSIGNED_SHORT),('Data3', UNSIGNED_SHORT),('Data4', BYTE),
    )
UUID = GUID
class PGUID(NDRPOINTER):
    referent = (
        ('Data', GUID),
    )    


class LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', SIGNED___INT64),
    )
class PLARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', LARGE_INTEGER),
    )    


class EVENT_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Id', USHORT),('Version', UCHAR),('Channel', UCHAR),('Level', UCHAR),('Opcode', UCHAR),('Task', USHORT),('Keyword', ULONGLONG),
    )
class PEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    
class PCEVENT_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', EVENT_DESCRIPTOR),
    )    


class S0(NDRSTRUCT):
    structure = (
        ('KernelTime', ULONG),('UserTime', ULONG),
    )


class U0(NDRUNION):
    union = {
        1: ('s0',S0),2: ('ProcessorTime',ULONG64),
    }
        

class EVENT_HEADER(NDRSTRUCT):
    structure = (
        ('Size', USHORT),('HeaderType', USHORT),('Flags', USHORT),('EventProperty', USHORT),('ThreadId', ULONG),('ProcessId', ULONG),('TimeStamp', LARGE_INTEGER),('ProviderId', GUID),('EventDescriptor', EVENT_DESCRIPTOR),('u0', U0),('ActivityId', GUID),
    )
class PEVENT_HEADER(NDRPOINTER):
    referent = (
        ('Data', EVENT_HEADER),
    )    

LCID = DWORD

class LUID(NDRSTRUCT):
    structure = (
        ('LowPart', DWORD),('HighPart', LONG),
    )
class PLUID(NDRPOINTER):
    referent = (
        ('Data', LUID),
    )    


class MULTI_SZ(NDRSTRUCT):
    structure = (
        ('Value', WCHAR_T),('nChar', DWORD),
    )


class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
    item = WCHAR

class PTR_UNSIGNED_SHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_SHORT),
    )

class UNSIGNED_SHORT(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_UNSIGNED_SHORT),

    )
        

class SERVER_INFO_100(NDRSTRUCT):
    structure = (
        ('sv100_platform_id', DWORD),('sv100_name', WCHAR_T),
    )
class PSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    
class LPSERVER_INFO_100(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100),
    )    


class SERVER_INFO_101(NDRSTRUCT):
    structure = (
        ('sv101_platform_id', DWORD),('sv101_name', WCHAR_T),('sv101_version_major', DWORD),('sv101_version_minor', DWORD),('sv101_version_type', DWORD),('sv101_comment', WCHAR_T),
    )
class PSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    
class LPSERVER_INFO_101(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_101),
    )    


class SYSTEMTIME(NDRSTRUCT):
    structure = (
        ('wYear', WORD),('wMonth', WORD),('wDayOfWeek', WORD),('wDay', WORD),('wHour', WORD),('wMinute', WORD),('wSecond', WORD),('wMilliseconds', WORD),
    )
class PSYSTEMTIME(NDRPOINTER):
    referent = (
        ('Data', SYSTEMTIME),
    )    


class UINT128(NDRSTRUCT):
    structure = (
        ('lower', UINT64),('upper', UINT64),
    )
class PUINT128(NDRPOINTER):
    referent = (
        ('Data', UINT128),
    )    


class ULARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('QuadPart', UNSIGNED___INT64),
    )
class PULARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', ULARGE_INTEGER),
    )    


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
    structure = (
        ('Value', BYTE),
    )

ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NDRSTRUCT):
    structure = (
        ('Level', WORD),('Remaining', ACCESS_MASK),('ObjectType', GUID),
    )
class POBJECT_TYPE_LIST(NDRPOINTER):
    referent = (
        ('Data', OBJECT_TYPE_LIST),
    )    


class ACE_HEADER(NDRSTRUCT):
    structure = (
        ('AceType', UCHAR),('AceFlags', UCHAR),('AceSize', USHORT),
    )
class PACE_HEADER(NDRPOINTER):
    referent = (
        ('Data', ACE_HEADER),
    )    


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
    structure = (
        ('Header', ACE_HEADER),('Mask', ACCESS_MASK),('SidStart', DWORD),
    )
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
    referent = (
        ('Data', SYSTEM_MANDATORY_LABEL_ACE),
    )    


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
    structure = (
        ('Policy', DWORD),
    )
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
    referent = (
        ('Data', TOKEN_MANDATORY_POLICY),
    )    


class MANDATORY_INFORMATION(NDRSTRUCT):
    structure = (
        ('AllowedAccess', ACCESS_MASK),('WriteAllowed', BOOLEAN),('ReadAllowed', BOOLEAN),('ExecuteAllowed', BOOLEAN),('MandatoryPolicy', TOKEN_MANDATORY_POLICY),
    )
class PMANDATORY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', MANDATORY_INFORMATION),
    )    


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
    structure = (
        ('Length', DWORD),('OctetString', BYTE),
    )
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    )    


class VALUES(NDRUNION):
    union = {
        1: ('pInt64',PLONG64),2: ('pUint64',PDWORD64),3: ('ppString',PWSTR),4: ('pOctetString',PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE),
    }
        

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
    structure = (
        ('Name', DWORD),('ValueType', WORD),('Reserved', WORD),('Flags', DWORD),('ValueCount', DWORD),('Values', VALUES),
    )
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
    referent = (
        ('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1),
    )    

SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD

class RPC_SID(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('SubAuthorityCount', UNSIGNED_CHAR),('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),('SubAuthority', UNSIGNED_LONG),
    )
class PRPC_SID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    
class PSID(NDRPOINTER):
    referent = (
        ('Data', RPC_SID),
    )    


class ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('AceCount', UNSIGNED_SHORT),('Sbz2', UNSIGNED_SHORT),
    )
class PACL(NDRPOINTER):
    referent = (
        ('Data', ACL),
    )    


class SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UCHAR),('Sbz1', UCHAR),('Control', USHORT),('Owner', PSID),('Group', PSID),('Sacl', PACL),('Dacl', PACL),
    )
class PSECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', SECURITY_DESCRIPTOR),
    )    

#################################################################################

#TYPEDEFS

#################################################################################


class DNSSRV_STAT_HEADER(NDRSTRUCT):
    structure = (
        ('StatId', DWORD),('wLength', WORD),('fClear', BOOLEAN),('fReserved', UCHAR),
    )
class PDNSSRV_STAT_HEADER(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_STAT_HEADER),
    )    


class DNSSRV_STAT(NDRSTRUCT):
    structure = (
        ('Header', DNSSRV_STAT_HEADER),('Buffer', BYTE),
    )
class PDNSSRV_STAT(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_STAT),
    )    
class PDNSSRV_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_STAT),
    )    


class IP4_ARRAY(NDRSTRUCT):
    structure = (
        ('AddrCount', DWORD),('AddrArray', DWORD),
    )
class PIP4_ARRAY(NDRPOINTER):
    referent = (
        ('Data', IP4_ARRAY),
    )    


class DNS_ADDR(NDRSTRUCT):
    structure = (
        ('MaxSa', CHAR),('DnsAddrUserDword', DWORD),
    )
class PDNS_ADDR(NDRPOINTER):
    referent = (
        ('Data', DNS_ADDR),
    )    


class DNS_ADDR_ARRAY(NDRSTRUCT):
    structure = (
        ('MaxCount', DWORD),('AddrCount', DWORD),('Tag', DWORD),('Family', WORD),('WordReserved', WORD),('Flags', DWORD),('MatchFlag', DWORD),('Reserved1', DWORD),('Reserved2', DWORD),('AddrArray', DNS_ADDR),
    )
class PDNS_ADDR_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DNS_ADDR_ARRAY),
    )    


class DNS_RPC_BUFFER(NDRSTRUCT):
    structure = (
        ('dwLength', DWORD),('Buffer', BYTE),
    )
class PDNS_RPC_BUFFER(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_BUFFER),
    )    


class DNS_RPC_SERVER_INFO_W2K(NDRSTRUCT):
    structure = (
        ('dwVersion', DWORD),('fBootMethod', UCHAR),('fAdminConfigured', BOOLEAN),('fAllowUpdate', BOOLEAN),('fDsAvailable', BOOLEAN),('pszServerName', CHAR),('pszDsContainer', WCHAR_T),('aipServerAddrs', PIP4_ARRAY),('aipListenAddrs', PIP4_ARRAY),('aipForwarders', PIP4_ARRAY),('pExtension1', PDWORD),('pExtension2', PDWORD),('pExtension3', PDWORD),('pExtension4', PDWORD),('pExtension5', PDWORD),('dwLogLevel', DWORD),('dwDebugLevel', DWORD),('dwForwardTimeout', DWORD),('dwRpcProtocol', DWORD),('dwNameCheckFlag', DWORD),('cAddressAnswerLimit', DWORD),('dwRecursionRetry', DWORD),('dwRecursionTimeout', DWORD),('dwMaxCacheTtl', DWORD),('dwDsPollingInterval', DWORD),('dwScavengingInterval', DWORD),('dwDefaultRefreshInterval', DWORD),('dwDefaultNoRefreshInterval', DWORD),('dwReserveArray', DWORD),('fAutoReverseZones', BOOLEAN),('fAutoCacheUpdate', BOOLEAN),('fRecurseAfterForwarding', BOOLEAN),('fForwardDelegations', BOOLEAN),('fNoRecursion', BOOLEAN),('fSecureResponses', BOOLEAN),('fRoundRobin', BOOLEAN),('fLocalNetPriority', BOOLEAN),('fBindSecondaries', BOOLEAN),('fWriteAuthorityNs', BOOLEAN),('fStrictFileParsing', BOOLEAN),('fLooseWildcarding', BOOLEAN),('fDefaultAgingState', BOOLEAN),('fReserveArray', BOOLEAN),
    )
class PDNS_RPC_SERVER_INFO_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SERVER_INFO_W2K),
    )    


class DNS_RPC_SERVER_INFO_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwVersion', DWORD),('fBootMethod', UCHAR),('fAdminConfigured', BOOLEAN),('fAllowUpdate', BOOLEAN),('fDsAvailable', BOOLEAN),('pszServerName', CHAR),('pszDsContainer', WCHAR_T),('aipServerAddrs', PIP4_ARRAY),('aipListenAddrs', PIP4_ARRAY),('aipForwarders', PIP4_ARRAY),('aipLogFilter', PIP4_ARRAY),('pwszLogFilePath', WCHAR_T),('pszDomainName', CHAR),('pszForestName', CHAR),('pszDomainDirectoryPartition', CHAR),('pszForestDirectoryPartition', CHAR),('pExtensions', CHAR),('dwLogLevel', DWORD),('dwDebugLevel', DWORD),('dwForwardTimeout', DWORD),('dwRpcProtocol', DWORD),('dwNameCheckFlag', DWORD),('cAddressAnswerLimit', DWORD),('dwRecursionRetry', DWORD),('dwRecursionTimeout', DWORD),('dwMaxCacheTtl', DWORD),('dwDsPollingInterval', DWORD),('dwLocalNetPriorityNetMask', DWORD),('dwScavengingInterval', DWORD),('dwDefaultRefreshInterval', DWORD),('dwDefaultNoRefreshInterval', DWORD),('dwLastScavengeTime', DWORD),('dwEventLogLevel', DWORD),('dwLogFileMaxSize', DWORD),('dwDsForestVersion', DWORD),('dwDsDomainVersion', DWORD),('dwDsDsaVersion', DWORD),('dwReserveArray', DWORD),('fAutoReverseZones', BOOLEAN),('fAutoCacheUpdate', BOOLEAN),('fRecurseAfterForwarding', BOOLEAN),('fForwardDelegations', BOOLEAN),('fNoRecursion', BOOLEAN),('fSecureResponses', BOOLEAN),('fRoundRobin', BOOLEAN),('fLocalNetPriority', BOOLEAN),('fBindSecondaries', BOOLEAN),('fWriteAuthorityNs', BOOLEAN),('fStrictFileParsing', BOOLEAN),('fLooseWildcarding', BOOLEAN),('fDefaultAgingState', BOOLEAN),('fReserveArray', BOOLEAN),
    )
class PDNS_RPC_SERVER_INFO_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SERVER_INFO_DOTNET),
    )    


class DNS_RPC_SERVER_INFO_LONGHORN(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwVersion', DWORD),('fBootMethod', UCHAR),('fAdminConfigured', BOOLEAN),('fAllowUpdate', BOOLEAN),('fDsAvailable', BOOLEAN),('pszServerName', CHAR),('pszDsContainer', WCHAR_T),('aipServerAddrs', PDNS_ADDR_ARRAY),('aipListenAddrs', PDNS_ADDR_ARRAY),('aipForwarders', PDNS_ADDR_ARRAY),('aipLogFilter', PDNS_ADDR_ARRAY),('pwszLogFilePath', WCHAR_T),('pszDomainName', CHAR),('pszForestName', CHAR),('pszDomainDirectoryPartition', CHAR),('pszForestDirectoryPartition', CHAR),('pExtensions', CHAR),('dwLogLevel', DWORD),('dwDebugLevel', DWORD),('dwForwardTimeout', DWORD),('dwRpcProtocol', DWORD),('dwNameCheckFlag', DWORD),('cAddressAnswerLimit', DWORD),('dwRecursionRetry', DWORD),('dwRecursionTimeout', DWORD),('dwMaxCacheTtl', DWORD),('dwDsPollingInterval', DWORD),('dwLocalNetPriorityNetMask', DWORD),('dwScavengingInterval', DWORD),('dwDefaultRefreshInterval', DWORD),('dwDefaultNoRefreshInterval', DWORD),('dwLastScavengeTime', DWORD),('dwEventLogLevel', DWORD),('dwLogFileMaxSize', DWORD),('dwDsForestVersion', DWORD),('dwDsDomainVersion', DWORD),('dwDsDsaVersion', DWORD),('fReadOnlyDC', BOOLEAN),('dwReserveArray', DWORD),('fAutoReverseZones', BOOLEAN),('fAutoCacheUpdate', BOOLEAN),('fRecurseAfterForwarding', BOOLEAN),('fForwardDelegations', BOOLEAN),('fNoRecursion', BOOLEAN),('fSecureResponses', BOOLEAN),('fRoundRobin', BOOLEAN),('fLocalNetPriority', BOOLEAN),('fBindSecondaries', BOOLEAN),('fWriteAuthorityNs', BOOLEAN),('fStrictFileParsing', BOOLEAN),('fLooseWildcarding', BOOLEAN),('fDefaultAgingState', BOOLEAN),('fReserveArray', BOOLEAN),
    )
class PDNS_RPC_SERVER_INFO_LONGHORN(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SERVER_INFO_LONGHORN),
    )    
DNS_RPC_SERVER_INFO = DNS_RPC_SERVER_INFO_LONGHORN
class PDNS_RPC_SERVER_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SERVER_INFO_LONGHORN),
    )    


class DNS_RPC_FORWARDERS_W2K(NDRSTRUCT):
    structure = (
        ('fRecurseAfterForwarding', DWORD),('dwForwardTimeout', DWORD),('aipForwarders', PIP4_ARRAY),
    )
class PDNS_RPC_FORWARDERS_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_FORWARDERS_W2K),
    )    


class DNS_RPC_FORWARDERS_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fRecurseAfterForwarding', DWORD),('dwForwardTimeout', DWORD),('aipForwarders', PIP4_ARRAY),
    )
class PDNS_RPC_FORWARDERS_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_FORWARDERS_DOTNET),
    )    


class DNS_RPC_FORWARDERS_LONGHORN(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fRecurseAfterForwarding', DWORD),('dwForwardTimeout', DWORD),('aipForwarders', PDNS_ADDR_ARRAY),
    )
class PDNS_RPC_FORWARDERS_LONGHORN(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_FORWARDERS_LONGHORN),
    )    
DNS_RPC_FORWARDERS = DNS_RPC_FORWARDERS_LONGHORN
class PDNS_RPC_FORWARDERS(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_FORWARDERS_LONGHORN),
    )    

DNS_RPC_ZONE_FLAGS = DWORD
PDNS_RPC_ZONE_FLAGS = DWORD

class DNS_RPC_ZONE_W2K(NDRSTRUCT):
    structure = (
        ('pszZoneName', WCHAR_T),('Flags', DNS_RPC_ZONE_FLAGS),('ZoneType', UCHAR),('Version', UCHAR),
    )
class PDNS_RPC_ZONE_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_W2K),
    )    


class DNS_RPC_ZONE_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneName', WCHAR_T),('Flags', DNS_RPC_ZONE_FLAGS),('ZoneType', UCHAR),('Version', UCHAR),('dwDpFlags', DWORD),('pszDpFqdn', CHAR),
    )
class PDNS_RPC_ZONE_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DOTNET),
    )    
DNS_RPC_ZONE = DNS_RPC_ZONE_DOTNET
class PDNS_RPC_ZONE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DOTNET),
    )    


class DNS_RPC_ZONE_LIST_W2K(NDRSTRUCT):
    structure = (
        ('dwZoneCount', DWORD),('ZoneArray', PDNS_RPC_ZONE_W2K),
    )
class PDNS_RPC_ZONE_LIST_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_LIST_W2K),
    )    


class DNS_RPC_ZONE_LIST_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwZoneCount', DWORD),('ZoneArray', PDNS_RPC_ZONE_DOTNET),
    )
class PDNS_RPC_ZONE_LIST_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_LIST_DOTNET),
    )    
DNS_RPC_ZONE_LIST = DNS_RPC_ZONE_LIST_DOTNET
class PDNS_RPC_ZONE_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_LIST_DOTNET),
    )    


TRUSTPOINT_STATE_INITIALIZED = ,
TRUSTPOINT_STATE_DSPENDING = ,
TRUSTPOINT_STATE_ACTIVE = ,
TRUSTPOINT_STATE_DELETE_PENDING = 
        

TRUSTANCHOR_STATE_INITIALIZED = ,
TRUSTANCHOR_STATE_DSPENDING = ,
TRUSTANCHOR_STATE_DSINVALID = ,
TRUSTANCHOR_STATE_ADDPEND = ,
TRUSTANCHOR_STATE_VALID = ,
TRUSTANCHOR_STATE_MISSING = ,
TRUSTANCHOR_STATE_REVOKED = 
        

class DNS_RPC_TRUST_POINT(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszTrustPointName', CHAR),('eTrustPointState', TRUSTPOINT_STATE),('i64LastActiveRefreshTime', __INT64),('i64NextActiveRefreshTime', __INT64),('i64LastSuccessfulActiveRefreshTime', __INT64),('dwLastActiveRefreshResult', DWORD),('dwReserved', DWORD),
    )
class PDNS_RPC_TRUST_POINT(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_TRUST_POINT),
    )    


class DNS_RPC_TRUST_POINT_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwTrustPointCount', DWORD),('TrustPointArray', PDNS_RPC_TRUST_POINT),
    )
class PDNS_RPC_TRUST_POINT_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_TRUST_POINT_LIST),
    )    


class DNS_RPC_SKD(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('Guid', GUID),('pwszKeyStorageProvider', WCHAR_T),('fStoreKeysInDirectory', BOOL),('fIsKSK', BOOL),('bSigningAlgorithm', BYTE),('dwKeyLength', DWORD),('dwInitialRolloverOffset', DWORD),('dwDNSKEYSignatureValidityPeriod', DWORD),('dwDSSignatureValidityPeriod', DWORD),('dwStandardSignatureValidityPeriod', DWORD),('dwRolloverType', DWORD),('dwRolloverPeriod', DWORD),('dwNextRolloverAction', DWORD),('dwReserved', DWORD),
    )
class PDNS_RPC_SKD(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SKD),
    )    


SIGN_SCOPE_DEFAULT = ,
SIGN_SCOPE_DNSKEY_ONLY = ,
SIGN_SCOPE_ALL_RECORDS = ,
SIGN_SCOPE_ADD_ONLY = ,
SIGN_SCOPE_DO_NOT_PUBLISH = 
        

class DNS_RPC_SKD_STATE_EX(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('Guid', GUID),('dwCurrentRollState', DWORD),('fManualTrigger', DWORD),('dwPreRollEventFired', DWORD),('ftNextKeyGenerationTime', FILETIME),('dwRevokedOrSwappedDnskeysLength', DWORD),('pRevokedOrSwappedDnskeysBuffer', PBYTE),('dwFinalDnskeysLength', DWORD),('pFinalDnskeys', PBYTE),('eActiveKeyScope', KEYSIGNSCOPE),('eStandByKeyScope', KEYSIGNSCOPE),('eNextKeyScope', KEYSIGNSCOPE),
    )
class PDNS_RPC_SKD_STATE_EX(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SKD_STATE_EX),
    )    


class DNS_RPC_SKD_STATE(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('Guid', GUID),('ftLastRolloverTime', FILETIME),('ftNextRolloverTime', FILETIME),('dwState', DWORD),('dwCurrentRolloverStatus', DWORD),('pwszActiveKey', WCHAR_T),('pwszStandbyKey', WCHAR_T),('pwszNextKey', WCHAR_T),('dwReserved', DWORD),
    )
class PDNS_RPC_SKD_STATE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SKD_STATE),
    )    


class DNS_RPC_ZONE_SKD(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pSkd', PDNS_RPC_SKD),('pSkdState', PDNS_RPC_SKD_STATE),('pSkdStateEx', PDNS_RPC_SKD_STATE_EX),
    )
class PDNS_RPC_ZONE_SKD(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SKD),
    )    


class DNS_RPC_ZONE_DNSSEC_SETTINGS(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fIsSigned', DWORD),('fSignWithNSEC3', DWORD),('fNSEC3OptOut', DWORD),('dwMaintainTrustAnchor', DWORD),('fParentHasSecureDelegation', DWORD),('dwDSRecordAlgorithms', DWORD),('fRFC5011KeyRollovers', DWORD),('bNSEC3HashAlgorithm', BYTE),('bNSEC3RandomSaltLength', BYTE),('wNSEC3IterationCount', WORD),('pwszNSEC3UserSalt', LPWSTR),('dwDNSKEYRecordSetTtl', DWORD),('dwDSRecordSetTtl', DWORD),('dwSignatureInceptionOffset', DWORD),('dwSecureDelegationPollingPeriod', DWORD),('dwPropagationTime', DWORD),('cbNSEC3CurrentSaltLength', DWORD),('pbNSEC3CurrentSalt', PBYTE),('CurrentRollingSKDGuid', GUID),('dwBufferLength', DWORD),('pBuffer', PBYTE),('dwCount', DWORD),('pZoneSkdArray', PDNS_RPC_ZONE_SKD),
    )
class PDNS_RPC_ZONE_DNSSEC_SETTINGS(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DNSSEC_SETTINGS),
    )    


class DNS_RPC_TRUST_ANCHOR(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('wTrustAnchorType', WORD),('wKeyTag', WORD),('wRRLength', WORD),('eTrustAnchorState', TRUSTANCHOR_STATE),('i64EnteredStateTime', __INT64),('i64NextStateTime', __INT64),('dwReserved', DWORD),('RRData', BYTE),
    )
class PDNS_RPC_TRUST_ANCHOR(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_TRUST_ANCHOR),
    )    


class DNS_RPC_TRUST_ANCHOR_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwTrustAnchorCount', DWORD),('TrustAnchorArray', PDNS_RPC_TRUST_ANCHOR),
    )
class PDNS_RPC_TRUST_ANCHOR_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_TRUST_ANCHOR_LIST),
    )    


class DNS_RPC_DP_ENUM(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszDpFqdn', CHAR),('dwFlags', DWORD),('dwZoneCount', DWORD),
    )
class PDNS_RPC_DP_ENUM(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_DP_ENUM),
    )    


class DNS_RPC_DP_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwDpCount', DWORD),('DpArray', PDNS_RPC_DP_ENUM),
    )
class PDNS_RPC_DP_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_DP_LIST),
    )    


class DNS_RPC_DP_REPLICA(NDRSTRUCT):
    structure = (
        ('pszReplicaDn', WCHAR_T),
    )
class PDNS_RPC_DP_REPLICA(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_DP_REPLICA),
    )    


class DNS_RPC_DP_INFO(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszDpFqdn', CHAR),('pszDpDn', WCHAR_T),('pszCrDn', WCHAR_T),('dwFlags', DWORD),('dwZoneCount', DWORD),('dwState', DWORD),('dwReserved', DWORD),('pwszReserved', WCHAR_T),('dwReplicaCount', DWORD),('ReplicaArray', PDNS_RPC_DP_REPLICA),
    )
class PDNS_RPC_DP_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_DP_INFO),
    )    


class DNS_RPC_ENLIST_DP(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszDpFqdn', CHAR),('dwOperation', DWORD),
    )
class PDNS_RPC_ENLIST_DP(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENLIST_DP),
    )    


class DNS_RPC_ZONE_EXPORT_INFO(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneExportFile', CHAR),
    )
class PDNS_RPC_ZONE_EXPORT_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_EXPORT_INFO),
    )    


class DNS_RPC_ZONE_SECONDARIES_W2K(NDRSTRUCT):
    structure = (
        ('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PIP4_ARRAY),('aipNotify', PIP4_ARRAY),
    )
class PDNS_RPC_ZONE_SECONDARIES_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SECONDARIES_W2K),
    )    


class DNS_RPC_ZONE_SECONDARIES_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PIP4_ARRAY),('aipNotify', PIP4_ARRAY),
    )
class PDNS_RPC_ZONE_SECONDARIES_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SECONDARIES_DOTNET),
    )    


class DNS_RPC_ZONE_SECONDARIES_LONGHORN(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PDNS_ADDR_ARRAY),('aipNotify', PDNS_ADDR_ARRAY),
    )
class PDNS_RPC_ZONE_SECONDARIES_LONGHORN(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SECONDARIES_LONGHORN),
    )    
DNS_RPC_ZONE_SECONDARIES = DNS_RPC_ZONE_SECONDARIES_LONGHORN
class PDNS_RPC_ZONE_SECONDARIES(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SECONDARIES_LONGHORN),
    )    


class DNS_RPC_ZONE_DATABASE_W2K(NDRSTRUCT):
    structure = (
        ('fDsIntegrated', DWORD),('pszFileName', CHAR),
    )
class PDNS_RPC_ZONE_DATABASE_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DATABASE_W2K),
    )    


class DNS_RPC_ZONE_DATABASE_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('fDsIntegrated', DWORD),('pszFileName', CHAR),
    )
class PDNS_RPC_ZONE_DATABASE_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DATABASE_DOTNET),
    )    
DNS_RPC_ZONE_DATABASE = DNS_RPC_ZONE_DATABASE_DOTNET
class PDNS_RPC_ZONE_DATABASE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_DATABASE_DOTNET),
    )    


class DNS_RPC_ZONE_CHANGE_DP(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszDestPartition', CHAR),
    )
class PDNS_RPC_ZONE_CHANGE_DP(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_CHANGE_DP),
    )    


class DNS_RPC_ZONE_INFO_W2K(NDRSTRUCT):
    structure = (
        ('pszZoneName', CHAR),('dwZoneType', DWORD),('fReverse', DWORD),('fAllowUpdate', DWORD),('fPaused', DWORD),('fShutdown', DWORD),('fAutoCreated', DWORD),('fUseDatabase', DWORD),('pszDataFile', CHAR),('aipMasters', PIP4_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PIP4_ARRAY),('aipNotify', PIP4_ARRAY),('fUseWins', DWORD),('fUseNbstat', DWORD),('fAging', DWORD),('dwNoRefreshInterval', DWORD),('dwRefreshInterval', DWORD),('dwAvailForScavengeTime', DWORD),('aipScavengeServers', PIP4_ARRAY),('pvReserved1', DWORD),('pvReserved2', DWORD),('pvReserved3', DWORD),('pvReserved4', DWORD),
    )
class PDNS_RPC_ZONE_INFO_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_INFO_W2K),
    )    


class DNS_RPC_ZONE_INFO_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneName', CHAR),('dwZoneType', DWORD),('fReverse', DWORD),('fAllowUpdate', DWORD),('fPaused', DWORD),('fShutdown', DWORD),('fAutoCreated', DWORD),('fUseDatabase', DWORD),('pszDataFile', CHAR),('aipMasters', PIP4_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PIP4_ARRAY),('aipNotify', PIP4_ARRAY),('fUseWins', DWORD),('fUseNbstat', DWORD),('fAging', DWORD),('dwNoRefreshInterval', DWORD),('dwRefreshInterval', DWORD),('dwAvailForScavengeTime', DWORD),('aipScavengeServers', PIP4_ARRAY),('dwForwarderTimeout', DWORD),('fForwarderSlave', DWORD),('aipLocalMasters', PIP4_ARRAY),('dwDpFlags', DWORD),('pszDpFqdn', CHAR),('pwszZoneDn', WCHAR_T),('dwLastSuccessfulSoaCheck', DWORD),('dwLastSuccessfulXfr', DWORD),('dwReserved1', DWORD),('dwReserved2', DWORD),('dwReserved3', DWORD),('dwReserved4', DWORD),('dwReserved5', DWORD),('pReserved1', CHAR),('pReserved2', CHAR),('pReserved3', CHAR),('pReserved4', CHAR),
    )
class PDNS_RPC_ZONE_INFO_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_INFO_DOTNET),
    )    


class DNS_RPC_ZONE_INFO_LONGHORN(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneName', CHAR),('dwZoneType', DWORD),('fReverse', DWORD),('fAllowUpdate', DWORD),('fPaused', DWORD),('fShutdown', DWORD),('fAutoCreated', DWORD),('fUseDatabase', DWORD),('pszDataFile', CHAR),('aipMasters', PDNS_ADDR_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('aipSecondaries', PDNS_ADDR_ARRAY),('aipNotify', PDNS_ADDR_ARRAY),('fUseWins', DWORD),('fUseNbstat', DWORD),('fAging', DWORD),('dwNoRefreshInterval', DWORD),('dwRefreshInterval', DWORD),('dwAvailForScavengeTime', DWORD),('aipScavengeServers', PDNS_ADDR_ARRAY),('dwForwarderTimeout', DWORD),('fForwarderSlave', DWORD),('aipLocalMasters', PDNS_ADDR_ARRAY),('dwDpFlags', DWORD),('pszDpFqdn', CHAR),('pwszZoneDn', WCHAR_T),('dwLastSuccessfulSoaCheck', DWORD),('dwLastSuccessfulXfr', DWORD),('fQueuedForBackgroundLoad', DWORD),('fBackgroundLoadInProgress', DWORD),('fReadOnlyZone', BOOL),('dwLastXfrAttempt', DWORD),('dwLastXfrResult', DWORD),
    )
class PDNS_RPC_ZONE_INFO_LONGHORN(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_INFO_LONGHORN),
    )    
DNS_RPC_ZONE_INFO = DNS_RPC_ZONE_INFO_LONGHORN
class PDNS_RPC_ZONE_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_INFO_LONGHORN),
    )    


class DNS_RPC_ZONE_CREATE_INFO_W2K(NDRSTRUCT):
    structure = (
        ('pszZoneName', CHAR),('dwZoneType', DWORD),('fAllowUpdate', DWORD),('fAging', DWORD),('dwFlags', DWORD),('pszDataFile', CHAR),('fDsIntegrated', DWORD),('fLoadExisting', DWORD),('pszAdmin', CHAR),('aipMasters', PIP4_ARRAY),('aipSecondaries', PIP4_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('pvReserved1', CHAR),('pvReserved2', CHAR),('pvReserved3', CHAR),('pvReserved4', CHAR),('pvReserved5', CHAR),('pvReserved6', CHAR),('pvReserved7', CHAR),('pvReserved8', CHAR),('dwReserved1', DWORD),('dwReserved2', DWORD),('dwReserved3', DWORD),('dwReserved4', DWORD),('dwReserved5', DWORD),('dwReserved6', DWORD),('dwReserved7', DWORD),('dwReserved8', DWORD),
    )
class PDNS_RPC_ZONE_CREATE_INFO_W2K(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_CREATE_INFO_W2K),
    )    


class DNS_RPC_ZONE_CREATE_INFO_DOTNET(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneName', CHAR),('dwZoneType', DWORD),('fAllowUpdate', DWORD),('fAging', DWORD),('dwFlags', DWORD),('pszDataFile', CHAR),('fDsIntegrated', DWORD),('fLoadExisting', DWORD),('pszAdmin', CHAR),('aipMasters', PIP4_ARRAY),('aipSecondaries', PIP4_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('dwTimeout', DWORD),('fRecurseAfterForwarding', DWORD),('dwDpFlags', DWORD),('pszDpFqdn', CHAR),('dwReserved', DWORD),
    )
class PDNS_RPC_ZONE_CREATE_INFO_DOTNET(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_CREATE_INFO_DOTNET),
    )    


class DNS_RPC_ZONE_CREATE_INFO_LONGHORN(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('pszZoneName', CHAR),('dwZoneType', DWORD),('fAllowUpdate', DWORD),('fAging', DWORD),('dwFlags', DWORD),('pszDataFile', CHAR),('fDsIntegrated', DWORD),('fLoadExisting', DWORD),('pszAdmin', CHAR),('aipMasters', PDNS_ADDR_ARRAY),('aipSecondaries', PDNS_ADDR_ARRAY),('fSecureSecondaries', DWORD),('fNotifyLevel', DWORD),('dwTimeout', DWORD),('fRecurseAfterForwarding', DWORD),('dwDpFlags', DWORD),('pszDpFqdn', CHAR),('dwReserved', DWORD),
    )
class PDNS_RPC_ZONE_CREATE_INFO_LONGHORN(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_CREATE_INFO_LONGHORN),
    )    
DNS_RPC_ZONE_CREATE_INFO = DNS_RPC_ZONE_CREATE_INFO_LONGHORN
class PDNS_RPC_ZONE_CREATE_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_CREATE_INFO_LONGHORN),
    )    


class DNS_RPC_SKD_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwCount', DWORD),('SkdArray', PDNS_RPC_SKD),
    )
class PDNS_RPC_SKD_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SKD_LIST),
    )    


class DNS_RPC_SIGNING_VALIDATION_ERROR(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('guidSKD', GUID),('pwszSigningKeyPointerString', WCHAR_T),('dwExtendedError', DWORD),('dwReserved', DWORD),
    )
class PDNS_RPC_SIGNING_VALIDATION_ERROR(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_SIGNING_VALIDATION_ERROR),
    )    


class DNS_RPC_AUTOCONFIGURE(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwAutoConfigFlags', DWORD),('dwReserved1', DWORD),('pszNewDomainName', CHAR),
    )
class PDNS_RPC_AUTOCONFIGURE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_AUTOCONFIGURE),
    )    


class DNS_RPC_ENUM_ZONES_FILTER(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwFilter', DWORD),('pszPartitionFqdn', CHAR),('pszQueryString', CHAR),('pszReserved', CHAR),
    )
class PDNS_RPC_ENUM_ZONES_FILTER(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENUM_ZONES_FILTER),
    )    


class DNS_RPC_RECORD(NDRSTRUCT):
    structure = (
        ('wDataLength', WORD),('wType', WORD),('dwFlags', DWORD),('dwSerial', DWORD),('dwTtlSeconds', DWORD),('dwTimeStamp', DWORD),('dwReserved', DWORD),('Buffer', BYTE),
    )
class PDNS_RPC_RECORD(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_RECORD),
    )    
DNS_FLAT_RECORD = DNS_RPC_RECORD
class PDNS_FLAT_RECORD(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_RECORD),
    )    


class DNS_RPC_NAME_AND_PARAM(NDRSTRUCT):
    structure = (
        ('dwParam', DWORD),('pszNodeName', CHAR),
    )
class PDNS_RPC_NAME_AND_PARAM(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_NAME_AND_PARAM),
    )    


class DNS_RPC_IP_VALIDATE(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved0', DWORD),('dwContext', DWORD),('dwReserved1', DWORD),('pszContextName', CHAR),('aipValidateAddrs', PDNS_ADDR_ARRAY),
    )
class PDNS_RPC_IP_VALIDATE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_IP_VALIDATE),
    )    


class DATA_DWORD(NDRUniConformantArray):
    item = CHAR

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('dwCount', DWORD),	('pszStrings', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('dwCount', DWORD),	('pwszStrings', PTR_DWORD),

    )
        

Equals = 1
        

DNS_AND = 
        

DnsPolicyServerLevel = ,
DnsPolicyZoneLevel = 
        

DnsPolicyDeny = ,
DnsPolicyAllow = ,
DnsPolicyIgnore = 
        

DnsPolicyQueryProcessing = ,
DnsPolicyZoneTransfer = ,
DnsPolicyDynamicUpdate = ,
DnsPolicyRecursion = 
        

DnsPolicyCriteriaSubnet = ,
DnsPolicyCriteriaTransportProtocol = ,
DnsPolicyCriteriaNetworkProtocol = ,
DnsPolicyCriteriaInterface = ,
DnsPolicyCriteriaFqdn = ,
DnsPolicyCriteriaQtype = ,
DnsPolicyCriteriaTime = 
        

class DNS_RPC_CLIENT_SUBNET_RECORD(NDRSTRUCT):
    structure = (
        ('pwszClientSubnetName', LPWSTR),('pIPAddr', PDNS_ADDR_ARRAY),('pIPv6Addr', PDNS_ADDR_ARRAY),
    )
class PDNS_RPC_CLIENT_SUBNET_RECORD(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_CLIENT_SUBNET_RECORD),
    )    


class DNS_RPC_POLICY_CONTENT(NDRSTRUCT):
    structure = (
        ('pwszScopeName', LPWSTR),('dwWeight', DWORD),
    )
class PDNS_RPC_POLICY_CONTENT(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_POLICY_CONTENT),
    )    


class DNS_RPC_POLICY_CONTENT_LIST(NDRSTRUCT):
    structure = (
        ('dwContentCount', DWORD),('pContent', PDNS_RPC_POLICY_CONTENT),
    )
class PDNS_RPC_POLICY_CONTENT_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_POLICY_CONTENT_LIST),
    )    


class DNS_RPC_CRITERIA(NDRSTRUCT):
    structure = (
        ('type', DNS_RPC_CRITERIA_ENUM),('pCriteria', LPWSTR),
    )
class PDNS_RPC_CRITERIA(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_CRITERIA),
    )    


class DNS_RPC_POLICY(NDRSTRUCT):
    structure = (
        ('pwszPolicyName', LPWSTR),('level', DNS_RPC_POLICY_LEVEL),('appliesOn', DNS_RPC_POLICY_TYPE),('action', DNS_RPC_POLICY_ACTION_TYPE),('condition', DNS_RPC_POLICY_CONDITION),('isEnabled', BOOL),('dwProcessingOrder', DWORD),('pszZoneName', LPSTR),('pContentList', PDNS_RPC_POLICY_CONTENT_LIST),('flags', DWORDLONG),('dwCriteriaCount', DWORD),('pCriteriaList', PDNS_RPC_CRITERIA),
    )
class PDNS_RPC_POLICY(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_POLICY),
    )    


class DNS_RPC_POLICY_NAME(NDRSTRUCT):
    structure = (
        ('pwszPolicyName', LPWSTR),('appliesOn', DNS_RPC_POLICY_TYPE),('fEnabled', BOOL),('processingOrder', DWORD),
    )
class PDNS_RPC_POLICY_NAME(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_POLICY_NAME),
    )    


class DNS_RPC_ENUMERATE_POLICY_LIST(NDRSTRUCT):
    structure = (
        ('dwPolicyCount', DWORD),('pPolicyArray', PDNS_RPC_POLICY_NAME),
    )
class PDNS_RPC_ENUMERATE_POLICY_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENUMERATE_POLICY_LIST),
    )    


DnsRRLLogOnly = ,
DnsRRLEnabled = 
        

class DNS_RPC_RRL_PARAMS(NDRSTRUCT):
    structure = (
        ('dwResponsesPerSecond', DWORD),('dwErrorsPerSecond', DWORD),('dwLeakRate', DWORD),('dwTCRate', DWORD),('dwTotalResponsesInWindow', DWORD),('dwWindowSize', DWORD),('dwIPv4PrefixLength', DWORD),('dwIPv6PrefixLength', DWORD),('eMode', DNS_RRL_MODE_ENUM),('dwFlags', DWORD),('fSetDefault', BOOL),
    )
class PDNS_RPC_RRL_PARAMS(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_RRL_PARAMS),
    )    


class DNS_RPC_VIRTUALIZATION_INSTANCE(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwReserved', DWORD),('dwFlags', DWORD),('pwszVirtualizationID', LPWSTR),('pwszFriendlyName', LPWSTR),('pwszDescription', LPWSTR),
    )
class PDNS_RPC_VIRTUALIZATION_INSTANCE(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_VIRTUALIZATION_INSTANCE),
    )    


class DNS_RPC_VIRTUALIZATION_INSTANCE_INFO(NDRSTRUCT):
    structure = (
        ('pwszVirtualizationID', LPWSTR),('pwszFriendlyName', LPWSTR),('pwszDescription', LPWSTR),
    )
class PDNS_RPC_VIRTUALIZATION_INSTANCE_INFO(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_VIRTUALIZATION_INSTANCE_INFO),
    )    


class DNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwVirtualizationInstanceCount', DWORD),('VirtualizationInstanceArray', PDNS_RPC_VIRTUALIZATION_INSTANCE_INFO),
    )
class PDNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST),
    )    


DNSSRV_TYPEID_ANY = -1),
DNSSRV_TYPEID_NULL = 0,
DNSSRV_TYPEID_DWORD = 0,
DNSSRV_TYPEID_LPSTR = 0,
DNSSRV_TYPEID_LPWSTR = 0,
DNSSRV_TYPEID_IPARRAY = 0,
DNSSRV_TYPEID_BUFFER = 0,
DNSSRV_TYPEID_SERVER_INFO_W2K = 0,
DNSSRV_TYPEID_STATS = 0,
DNSSRV_TYPEID_FORWARDERS_W2K = 0,
DNSSRV_TYPEID_ZONE_W2K = 0,
DNSSRV_TYPEID_ZONE_INFO_W2K = 0,
DNSSRV_TYPEID_ZONE_SECONDARIES_W2K = 0,
DNSSRV_TYPEID_ZONE_DATABASE_W2K = 0,
DNSSRV_TYPEID_ZONE_TYPE_RESET_W2K = 0,
DNSSRV_TYPEID_ZONE_CREATE_W2K = 0,
DNSSRV_TYPEID_NAME_AND_PARAM = 0,
DNSSRV_TYPEID_ZONE_LIST_W2K = 0,
DNSSRV_TYPEID_ZONE_RENAME = 0,
DNSSRV_TYPEID_ZONE_EXPORT = 0,
DNSSRV_TYPEID_SERVER_INFO_DOTNET = 0,
DNSSRV_TYPEID_FORWARDERS_DOTNET = 0,
DNSSRV_TYPEID_ZONE = 0,
DNSSRV_TYPEID_ZONE_INFO_DOTNET = 0,
DNSSRV_TYPEID_ZONE_SECONDARIES_DOTNET = 0,
DNSSRV_TYPEID_ZONE_DATABASE = 0,
DNSSRV_TYPEID_ZONE_TYPE_RESET_DOTNET = 0,
DNSSRV_TYPEID_ZONE_CREATE_DOTNET = 0,
DNSSRV_TYPEID_ZONE_LIST = 0,
DNSSRV_TYPEID_DP_ENUM = 0,
DNSSRV_TYPEID_DP_INFO = 0,
DNSSRV_TYPEID_DP_LIST = 0,
DNSSRV_TYPEID_ENLIST_DP = 0,
DNSSRV_TYPEID_ZONE_CHANGE_DP = 0,
DNSSRV_TYPEID_ENUM_ZONES_FILTER = 0,
DNSSRV_TYPEID_ADDRARRAY = 0,
DNSSRV_TYPEID_SERVER_INFO = 0,
DNSSRV_TYPEID_ZONE_INFO = 0,
DNSSRV_TYPEID_FORWARDERS = 0,
DNSSRV_TYPEID_ZONE_SECONDARIES = 0,
DNSSRV_TYPEID_ZONE_TYPE_RESET = 0,
DNSSRV_TYPEID_ZONE_CREATE = 0,
DNSSRV_TYPEID_IP_VALIDATE = 0,
DNSSRV_TYPEID_AUTOCONFIGURE = 0,
DNSSRV_TYPEID_UTF8_STRING_LIST = 0,
DNSSRV_TYPEID_UNICODE_STRING_LIST = 0,
DNSSRV_TYPEID_SKD = 0,
DNSSRV_TYPEID_SKD_LIST = 0,
DNSSRV_TYPEID_SKD_STATE = 0,
DNSSRV_TYPEID_SIGNING_VALIDATION_ERROR = 0,
DNSSRV_TYPEID_TRUST_POINT_LIST = 0,
DNSSRV_TYPEID_TRUST_ANCHOR_LIST = 0,
DNSSRV_TYPEID_ZONE_SIGNING_SETTINGS = 0,
DNSSRV_TYPEID_ZONE_SCOPE_ENUM = 0,
DNSSRV_TYPEID_ZONE_STATS = 0,
DNSSRV_TYPEID_ZONE_SCOPE_CREATE = 0,
DNSSRV_TYPEID_ZONE_SCOPE_INFO = 0,
DNSSRV_TYPEID_SCOPE_ENUM = 0,
DNSSRV_TYPEID_CLIENT_SUBNET_RECORD = 0,
DNSSRV_TYPEID_POLICY = 0,
DNSSRV_TYPEID_POLICY_NAME = 0,
DNSSRV_TYPEID_POLICY_ENUM = 0,
DNSSRV_TYPEID_RRL = 0,
DNSSRV_TYPEID_VIRTUALIZATION_INSTANCE = 0
        

class DNS_RPC_ENUM_ZONE_SCOPE_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwZoneScopeCount', DWORD),('ZoneScopeArray', LPWSTR),
    )
class PDNS_RPC_ENUM_ZONE_SCOPE_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENUM_ZONE_SCOPE_LIST),
    )    


class DNS_SYSTEMTIME(NDRSTRUCT):
    structure = (
        ('wYear', WORD),('wMonth', WORD),('wDayOfWeek', WORD),('wDay', WORD),('wHour', WORD),('wMinute', WORD),('wSecond', WORD),('wMilliseconds', WORD),
    )


class DNSSRV_ZONE_TIME_STATS(NDRSTRUCT):
    structure = (
        ('StatsCollectionStartTime', DNS_SYSTEMTIME),
    )
class PDNSSRV_ZONE_TIME_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_ZONE_TIME_STATS),
    )    


ZONE_STATS_TYPE_RECORD_A = 0,
ZONE_STATS_TYPE_RECORD_AAAA = 0,
ZONE_STATS_TYPE_RECORD_PTR = 0,
ZONE_STATS_TYPE_RECORD_CNAME = 0,
ZONE_STATS_TYPE_RECORD_MX = 0,
ZONE_STATS_TYPE_RECORD_AFSDB = 0,
ZONE_STATS_TYPE_RECORD_ATMA = 0,
ZONE_STATS_TYPE_RECORD_DHCID = 0,
ZONE_STATS_TYPE_RECORD_DNAME = 0,
ZONE_STATS_TYPE_RECORD_HINFO = 0,
ZONE_STATS_TYPE_RECORD_ISDN = 0,
ZONE_STATS_TYPE_RECORD_MG = 0,
ZONE_STATS_TYPE_RECORD_MB = 0,
ZONE_STATS_TYPE_RECORD_MINFO = 0,
ZONE_STATS_TYPE_RECORD_NAPTR = 0,
ZONE_STATS_TYPE_RECORD_NXT = 0,
ZONE_STATS_TYPE_RECORD_KEY = 0,
ZONE_STATS_TYPE_RECORD_MR = 0,
ZONE_STATS_TYPE_RECORD_RP = 0,
ZONE_STATS_TYPE_RECORD_RT = 0,
ZONE_STATS_TYPE_RECORD_SRV = 0,
ZONE_STATS_TYPE_RECORD_SIG = 0,
ZONE_STATS_TYPE_RECORD_TEXT = 0,
ZONE_STATS_TYPE_RECORD_WKS = 0,
ZONE_STATS_TYPE_RECORD_X25 = 0,
ZONE_STATS_TYPE_RECORD_DNSKEY = 0,
ZONE_STATS_TYPE_RECORD_DS = 0,
ZONE_STATS_TYPE_RECORD_NS = 0,
ZONE_STATS_TYPE_RECORD_SOA = 0,
ZONE_STATS_TYPE_RECORD_TLSA = 0,
ZONE_STATS_TYPE_RECORD_ALL = 0,
ZONE_STATS_TYPE_RECORD_OTHERS = 0,
ZONE_STATS_TYPE_TRANSFER_AXFR = 0,
ZONE_STATS_TYPE_TRANSFER_IXFR = 0,
ZONE_STATS_TYPE_UPDATE = 0,
ZONE_STATS_TYPE_RRL = 0
        

class DNSSRV_ZONE_QUERY_STATS(NDRSTRUCT):
    structure = (
        ('RecordType', DNS_ZONE_STATS_TYPE),('QueriesResponded', ULONG64),('QueriesReceived', ULONG64),('QueriesFailure', ULONG64),('QueriesNameError', ULONG64),
    )
class PDNSSRV_ZONE_QUERY_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_ZONE_QUERY_STATS),
    )    


class DNSSRV_RRL_STATS(NDRSTRUCT):
    structure = (
        ('Header', DNSSRV_STAT_HEADER),('TotalResponsesSent', DWORD),('TotalResponsesDropped', DWORD),('TotalResponsesTruncated', DWORD),('TotalResponsesLeaked', DWORD),
    )
class PDNSSRV_RRL_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_RRL_STATS),
    )    


class DNSSRV_ZONE_TRANSFER_STATS(NDRSTRUCT):
    structure = (
        ('TransferType', DNS_ZONE_STATS_TYPE),('RequestReceived', ULONG64),('RequestSent', ULONG64),('ResponseReceived', ULONG64),('SuccessReceived', ULONG64),('SuccessSent', ULONG64),
    )
class PDNSSRV_ZONE_TRANSFER_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_ZONE_TRANSFER_STATS),
    )    


class DNSSRV_ZONE_UPDATE_STATS(NDRSTRUCT):
    structure = (
        ('Type', DNS_ZONE_STATS_TYPE),('DynamicUpdateReceived', ULONG64),('DynamicUpdateRejected', ULONG64),
    )
class PDNSSRV_ZONE_UPDATE_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_ZONE_UPDATE_STATS),
    )    


class DNSSRV_ZONE_RRL_STATS(NDRSTRUCT):
    structure = (
        ('Type', DNS_ZONE_STATS_TYPE),('TotalResponsesSent', DWORD),('TotalResponsesDropped', DWORD),('TotalResponsesTruncated', DWORD),('TotalResponsesLeaked', DWORD),
    )
class PDNSSRV_ZONE_RRL_STATS(NDRPOINTER):
    referent = (
        ('Data', DNSSRV_ZONE_RRL_STATS),
    )    


class DNS_RPC_ZONE_STATS_V1(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('ZoneTimeStats', DNSSRV_ZONE_TIME_STATS),('ZoneQueryStats', DNSSRV_ZONE_QUERY_STATS),('ZoneTransferStats', DNSSRV_ZONE_TRANSFER_STATS),('ZoneUpdateStats', DNSSRV_ZONE_UPDATE_STATS),('ZoneRRLStats', DNSSRV_ZONE_RRL_STATS),
    )
class PDNS_RPC_ZONE_STATS_V1(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_STATS_V1),
    )    


class DNS_RPC_ZONE_SCOPE_CREATE_INFO_V1(NDRSTRUCT):
    structure = (
        ('dwFlags', DWORD),('pwszScopeName', LPWSTR),
    )
class PDNS_RPC_ZONE_SCOPE_CREATE_INFO_V1(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SCOPE_CREATE_INFO_V1),
    )    


class DNS_RPC_ZONE_SCOPE_INFO_V1(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('pwszScopeName', LPWSTR),('pwszDataFile', LPWSTR),
    )
class PDNS_RPC_ZONE_SCOPE_INFO_V1(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ZONE_SCOPE_INFO_V1),
    )    


class DNS_RPC_ENUM_SCOPE_LIST(NDRSTRUCT):
    structure = (
        ('dwRpcStructureVersion', DWORD),('dwScopeCount', DWORD),('ScopeArray', LPWSTR),
    )
class PDNS_RPC_ENUM_SCOPE_LIST(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_ENUM_SCOPE_LIST),
    )    


class DNSSRV_RPC_UNION(NDRUNION):
    union = {
        DNSSRV_TYPEID_NULL: ('Null',PBYTE),DNSSRV_TYPEID_DWORD: ('Dword',DWORD),DNSSRV_TYPEID_LPSTR: ('String',CHAR),DNSSRV_TYPEID_LPWSTR: ('WideString',WCHAR_T),DNSSRV_TYPEID_IPARRAY: ('IpArray',PIP4_ARRAY),DNSSRV_TYPEID_BUFFER: ('Buffer',PDNS_RPC_BUFFER),DNSSRV_TYPEID_SERVER_INFO_W2K: ('ServerInfoW2K',PDNS_RPC_SERVER_INFO_W2K),DNSSRV_TYPEID_STATS: ('Stats',PDNSSRV_STATS),DNSSRV_TYPEID_FORWARDERS_W2K: ('ForwardersW2K',PDNS_RPC_FORWARDERS_W2K),DNSSRV_TYPEID_ZONE_W2K: ('ZoneW2K',PDNS_RPC_ZONE_W2K),DNSSRV_TYPEID_ZONE_INFO_W2K: ('ZoneInfoW2K',PDNS_RPC_ZONE_INFO_W2K),DNSSRV_TYPEID_ZONE_SECONDARIES_W2K: ('SecondariesW2K',PDNS_RPC_ZONE_SECONDARIES_W2K),DNSSRV_TYPEID_ZONE_DATABASE_W2K: ('DatabaseW2K',PDNS_RPC_ZONE_DATABASE_W2K),DNSSRV_TYPEID_ZONE_CREATE_W2K: ('ZoneCreateW2K',PDNS_RPC_ZONE_CREATE_INFO_W2K),DNSSRV_TYPEID_NAME_AND_PARAM: ('NameAndParam',PDNS_RPC_NAME_AND_PARAM),DNSSRV_TYPEID_ZONE_LIST_W2K: ('ZoneListW2K',PDNS_RPC_ZONE_LIST_W2K),DNSSRV_TYPEID_SERVER_INFO_DOTNET: ('ServerInfoDotNet',PDNS_RPC_SERVER_INFO_DOTNET),DNSSRV_TYPEID_FORWARDERS_DOTNET: ('ForwardersDotNet',PDNS_RPC_FORWARDERS_DOTNET),DNSSRV_TYPEID_ZONE: ('Zone',PDNS_RPC_ZONE),DNSSRV_TYPEID_ZONE_INFO_DOTNET: ('ZoneInfoDotNet',PDNS_RPC_ZONE_INFO_DOTNET),DNSSRV_TYPEID_ZONE_SECONDARIES_DOTNET: ('SecondariesDotNet',PDNS_RPC_ZONE_SECONDARIES_DOTNET),DNSSRV_TYPEID_ZONE_DATABASE: ('Database',PDNS_RPC_ZONE_DATABASE),DNSSRV_TYPEID_ZONE_CREATE_DOTNET: ('ZoneCreateDotNet',PDNS_RPC_ZONE_CREATE_INFO_DOTNET),DNSSRV_TYPEID_ZONE_LIST: ('ZoneList',PDNS_RPC_ZONE_LIST),DNSSRV_TYPEID_ZONE_EXPORT: ('ZoneExport',PDNS_RPC_ZONE_EXPORT_INFO),DNSSRV_TYPEID_DP_INFO: ('DirectoryPartition',PDNS_RPC_DP_INFO),DNSSRV_TYPEID_DP_ENUM: ('DirectoryPartitionEnum',PDNS_RPC_DP_ENUM),DNSSRV_TYPEID_DP_LIST: ('DirectoryPartitionList',PDNS_RPC_DP_LIST),DNSSRV_TYPEID_ENLIST_DP: ('EnlistDirectoryPartition',PDNS_RPC_ENLIST_DP),DNSSRV_TYPEID_ZONE_CHANGE_DP: ('ZoneChangeDirectoryPartition',PDNS_RPC_ZONE_CHANGE_DP),DNSSRV_TYPEID_ENUM_ZONES_FILTER: ('EnumZonesFilter',PDNS_RPC_ENUM_ZONES_FILTER),DNSSRV_TYPEID_ADDRARRAY: ('AddrArray',PDNS_ADDR_ARRAY),DNSSRV_TYPEID_SERVER_INFO: ('ServerInfo',PDNS_RPC_SERVER_INFO),DNSSRV_TYPEID_ZONE_CREATE: ('ZoneCreate',PDNS_RPC_ZONE_CREATE_INFO),DNSSRV_TYPEID_FORWARDERS: ('Forwarders',PDNS_RPC_FORWARDERS),DNSSRV_TYPEID_ZONE_SECONDARIES: ('Secondaries',PDNS_RPC_ZONE_SECONDARIES),DNSSRV_TYPEID_IP_VALIDATE: ('IpValidate',PDNS_RPC_IP_VALIDATE),DNSSRV_TYPEID_ZONE_INFO: ('ZoneInfo',PDNS_RPC_ZONE_INFO),DNSSRV_TYPEID_AUTOCONFIGURE: ('AutoConfigure',PDNS_RPC_AUTOCONFIGURE),DNSSRV_TYPEID_UTF8_STRING_LIST: ('Utf8StringList',PDNS_RPC_UTF8_STRING_LIST),DNSSRV_TYPEID_UNICODE_STRING_LIST: ('UnicodeStringList',PDNS_RPC_UNICODE_STRING_LIST),DNSSRV_TYPEID_SKD: ('Skd',PDNS_RPC_SKD),DNSSRV_TYPEID_SKD_LIST: ('SkdList',PDNS_RPC_SKD_LIST),DNSSRV_TYPEID_SKD_STATE: ('SkdState',PDNS_RPC_SKD_STATE),DNSSRV_TYPEID_SIGNING_VALIDATION_ERROR: ('SigningValidationError',PDNS_RPC_SIGNING_VALIDATION_ERROR),DNSSRV_TYPEID_TRUST_POINT_LIST: ('TrustPointList',PDNS_RPC_TRUST_POINT_LIST),DNSSRV_TYPEID_TRUST_ANCHOR_LIST: ('TrustAnchorList',PDNS_RPC_TRUST_ANCHOR_LIST),DNSSRV_TYPEID_ZONE_SIGNING_SETTINGS: ('ZoneDnsSecSettings',PDNS_RPC_ZONE_DNSSEC_SETTINGS),DNSSRV_TYPEID_ZONE_SCOPE_ENUM: ('ZoneScopeList',PDNS_RPC_ENUM_ZONE_SCOPE_LIST),DNSSRV_TYPEID_ZONE_STATS: ('ZoneStats',PDNS_RPC_ZONE_STATS),DNSSRV_TYPEID_ZONE_SCOPE_CREATE: ('ScopeCreate',PDNS_RPC_ZONE_SCOPE_CREATE_INFO),DNSSRV_TYPEID_ZONE_SCOPE_INFO: ('ScopeInfo',PDNS_RPC_ZONE_SCOPE_INFO),DNSSRV_TYPEID_SCOPE_ENUM: ('ScopeList',PDNS_RPC_ENUM_SCOPE_LIST),DNSSRV_TYPEID_CLIENT_SUBNET_RECORD: ('SubnetList',PDNS_RPC_CLIENT_SUBNET_RECORD),DNSSRV_TYPEID_POLICY: ('pPolicy',PDNS_RPC_POLICY),DNSSRV_TYPEID_POLICY_NAME: ('pPolicyName',PDNS_RPC_POLICY_NAME),DNSSRV_TYPEID_POLICY_ENUM: ('pPolicyList',PDNS_RPC_ENUMERATE_POLICY_LIST),DNSSRV_TYPEID_RRL: ('pRRLParams',PDNS_RPC_RRL_PARAMS),DNSSRV_TYPEID_VIRTUALIZATION_INSTANCE: ('VirtualizationInstance',PDNS_RPC_VIRTUALIZATION_INSTANCE),DNSSRV_TYPEID_VIRTUALIZATION_INSTANCE_ENUM: ('VirtualizationInstanceList',PDNS_RPC_ENUM_VIRTUALIZATION_INSTANCE_LIST),
    }
        

IMPORT_STATUS_NOOP = ,
IMPORT_STATUS_SIGNING_READY = ,
IMPORT_STATUS_UNSIGNING_READY = 
        
#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#DnsServer Definition

#################################################################################

MSRPC_UUID_DNSSERVER = uuidtup_to_bin(('50abc2a4-574d-40b3-9d66-ee4fd5fba076','0.0'))


class R_DnssrvOperation(NDRCALL):
    opnum = 0
    structure = (
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('dwContext', DWORD),
		('pszOperation', LPCSTR),
		('dwTypeId', DWORD),
		('pData', DNSSRV_RPC_UNION),
    )

class R_DnssrvOperationResponse(NDRCALL):
    structure = (

    )
        

class R_DnssrvQuery(NDRCALL):
    opnum = 1
    structure = (
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszOperation', LPCSTR),
    )

class R_DnssrvQueryResponse(NDRCALL):
    structure = (
		('pdwTypeId', PDWORD),
		('ppData', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvComplexOperation(NDRCALL):
    opnum = 2
    structure = (
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszOperation', LPCSTR),
		('dwTypeIn', DWORD),
		('pDataIn', DNSSRV_RPC_UNION),
    )

class R_DnssrvComplexOperationResponse(NDRCALL):
    structure = (
		('pdwTypeOut', PDWORD),
		('ppDataOut', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvEnumRecords(NDRCALL):
    opnum = 3
    structure = (
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszNodeName', LPCSTR),
		('pszStartChild', LPCSTR),
		('wRecordType', WORD),
		('fSelectFlag', DWORD),
		('pszFilterStart', LPCSTR),
		('pszFilterStop', LPCSTR),
    )

class R_DnssrvEnumRecordsResponse(NDRCALL):
    structure = (
		('pdwBufferLength', PDWORD),
		('ppBuffer', PBYTE),
    )
        

class R_DnssrvUpdateRecord(NDRCALL):
    opnum = 4
    structure = (
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszNodeName', LPCSTR),
		('pAddRecord', PDNS_RPC_RECORD),
		('pDeleteRecord', PDNS_RPC_RECORD),
    )

class R_DnssrvUpdateRecordResponse(NDRCALL):
    structure = (

    )
        

class R_DnssrvOperation2(NDRCALL):
    opnum = 5
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('dwContext', DWORD),
		('pszOperation', LPCSTR),
		('dwTypeId', DWORD),
		('pData', DNSSRV_RPC_UNION),
    )

class R_DnssrvOperation2Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvQuery2(NDRCALL):
    opnum = 6
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszOperation', LPCSTR),
    )

class R_DnssrvQuery2Response(NDRCALL):
    structure = (
		('pdwTypeId', PDWORD),
		('ppData', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvComplexOperation2(NDRCALL):
    opnum = 7
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszOperation', LPCSTR),
		('dwTypeIn', DWORD),
		('pDataIn', DNSSRV_RPC_UNION),
    )

class R_DnssrvComplexOperation2Response(NDRCALL):
    structure = (
		('pdwTypeOut', PDWORD),
		('ppDataOut', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvEnumRecords2(NDRCALL):
    opnum = 8
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszNodeName', LPCSTR),
		('pszStartChild', LPCSTR),
		('wRecordType', WORD),
		('fSelectFlag', DWORD),
		('pszFilterStart', LPCSTR),
		('pszFilterStop', LPCSTR),
    )

class R_DnssrvEnumRecords2Response(NDRCALL):
    structure = (
		('pdwBufferLength', PDWORD),
		('ppBuffer', PBYTE),
    )
        

class R_DnssrvUpdateRecord2(NDRCALL):
    opnum = 9
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszNodeName', LPCSTR),
		('pAddRecord', PDNS_RPC_RECORD),
		('pDeleteRecord', PDNS_RPC_RECORD),
    )

class R_DnssrvUpdateRecord2Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvUpdateRecord3(NDRCALL):
    opnum = 10
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScope', LPCWSTR),
		('pszNodeName', LPCSTR),
		('pAddRecord', PDNS_RPC_RECORD),
		('pDeleteRecord', PDNS_RPC_RECORD),
    )

class R_DnssrvUpdateRecord3Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvEnumRecords3(NDRCALL):
    opnum = 11
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScope', LPCWSTR),
		('pszNodeName', LPCSTR),
		('pszStartChild', LPCSTR),
		('wRecordType', WORD),
		('fSelectFlag', DWORD),
		('pszFilterStart', LPCSTR),
		('pszFilterStop', LPCSTR),
    )

class R_DnssrvEnumRecords3Response(NDRCALL):
    structure = (
		('pdwBufferLength', PDWORD),
		('ppBuffer', PBYTE),
    )
        

class R_DnssrvOperation3(NDRCALL):
    opnum = 12
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScopeName', LPCWSTR),
		('dwContext', DWORD),
		('pszOperation', LPCSTR),
		('dwTypeId', DWORD),
		('pData', DNSSRV_RPC_UNION),
    )

class R_DnssrvOperation3Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvQuery3(NDRCALL):
    opnum = 13
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pszZone', LPCSTR),
		('pszZoneScopeName', LPCWSTR),
		('pszOperation', LPCSTR),
    )

class R_DnssrvQuery3Response(NDRCALL):
    structure = (
		('pdwTypeId', PDWORD),
		('ppData', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvComplexOperation3(NDRCALL):
    opnum = 14
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pwszVirtualizationInstanceID', LPCWSTR),
		('pszZone', LPCSTR),
		('pszOperation', LPCSTR),
		('dwTypeIn', DWORD),
		('pDataIn', DNSSRV_RPC_UNION),
    )

class R_DnssrvComplexOperation3Response(NDRCALL):
    structure = (
		('pdwTypeOut', PDWORD),
		('ppDataOut', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvOperation4(NDRCALL):
    opnum = 15
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pwszVirtualizationInstanceID', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScopeName', LPCWSTR),
		('dwContext', DWORD),
		('pszOperation', LPCSTR),
		('dwTypeId', DWORD),
		('pData', DNSSRV_RPC_UNION),
    )

class R_DnssrvOperation4Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvQuery4(NDRCALL):
    opnum = 16
    structure = (
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pwszVirtualizationInstanceID', LPCWSTR),
		('pszZone', LPCSTR),
		('pszZoneScopeName', LPCWSTR),
		('pszOperation', LPCSTR),
    )

class R_DnssrvQuery4Response(NDRCALL):
    structure = (
		('pdwTypeId', PDWORD),
		('ppData', DNSSRV_RPC_UNION),
    )
        

class R_DnssrvUpdateRecord4(NDRCALL):
    opnum = 17
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pwszVirtualizationInstanceID', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScope', LPCWSTR),
		('pszNodeName', LPCSTR),
		('pAddRecord', PDNS_RPC_RECORD),
		('pDeleteRecord', PDNS_RPC_RECORD),
    )

class R_DnssrvUpdateRecord4Response(NDRCALL):
    structure = (

    )
        

class R_DnssrvEnumRecords4(NDRCALL):
    opnum = 18
    structure = (
		('hBindingHandle', HANDLE_T),
		('dwClientVersion', DWORD),
		('dwSettingFlags', DWORD),
		('pwszServerName', LPCWSTR),
		('pwszVirtualizationInstanceID', LPCWSTR),
		('pszZone', LPCSTR),
		('pwszZoneScope', LPCWSTR),
		('pszNodeName', LPCSTR),
		('pszStartChild', LPCSTR),
		('wRecordType', WORD),
		('fSelectFlag', DWORD),
		('pszFilterStart', LPCSTR),
		('pszFilterStop', LPCSTR),
    )

class R_DnssrvEnumRecords4Response(NDRCALL):
    structure = (
		('pdwBufferLength', PDWORD),
		('ppBuffer', PBYTE),
    )
        
OPNUMS = {
0 : (R_DnssrvOperation,R_DnssrvOperationResponse),
1 : (R_DnssrvQuery,R_DnssrvQueryResponse),
2 : (R_DnssrvComplexOperation,R_DnssrvComplexOperationResponse),
3 : (R_DnssrvEnumRecords,R_DnssrvEnumRecordsResponse),
4 : (R_DnssrvUpdateRecord,R_DnssrvUpdateRecordResponse),
5 : (R_DnssrvOperation2,R_DnssrvOperation2Response),
6 : (R_DnssrvQuery2,R_DnssrvQuery2Response),
7 : (R_DnssrvComplexOperation2,R_DnssrvComplexOperation2Response),
8 : (R_DnssrvEnumRecords2,R_DnssrvEnumRecords2Response),
9 : (R_DnssrvUpdateRecord2,R_DnssrvUpdateRecord2Response),
10 : (R_DnssrvUpdateRecord3,R_DnssrvUpdateRecord3Response),
11 : (R_DnssrvEnumRecords3,R_DnssrvEnumRecords3Response),
12 : (R_DnssrvOperation3,R_DnssrvOperation3Response),
13 : (R_DnssrvQuery3,R_DnssrvQuery3Response),
14 : (R_DnssrvComplexOperation3,R_DnssrvComplexOperation3Response),
15 : (R_DnssrvOperation4,R_DnssrvOperation4Response),
16 : (R_DnssrvQuery4,R_DnssrvQuery4Response),
17 : (R_DnssrvUpdateRecord4,R_DnssrvUpdateRecord4Response),
18 : (R_DnssrvEnumRecords4,R_DnssrvEnumRecords4Response),
}

