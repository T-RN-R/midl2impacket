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


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
    item = WCHAR

class PTR_RPC_UNICODE_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_UNICODE_STRING),
    )

class RPC_UNICODE_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_UNICODE_STRING),

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


class TRUSTPOINT_STATE:
	TRUSTPOINT_STATE_INITIALIZED = 0,
	TRUSTPOINT_STATE_DSPENDING = 1,
	TRUSTPOINT_STATE_ACTIVE = 2,
	TRUSTPOINT_STATE_DELETE_PENDING = 3
        

class TRUSTANCHOR_STATE:
	TRUSTANCHOR_STATE_INITIALIZED = 0,
	TRUSTANCHOR_STATE_DSPENDING = 1,
	TRUSTANCHOR_STATE_DSINVALID = 2,
	TRUSTANCHOR_STATE_ADDPEND = 3,
	TRUSTANCHOR_STATE_VALID = 4,
	TRUSTANCHOR_STATE_MISSING = 5,
	TRUSTANCHOR_STATE_REVOKED = 6
        

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


class KEYSIGNSCOPE:
	SIGN_SCOPE_DEFAULT = 0,
	SIGN_SCOPE_DNSKEY_ONLY = 1,
	SIGN_SCOPE_ALL_RECORDS = 2,
	SIGN_SCOPE_ADD_ONLY = 3,
	SIGN_SCOPE_DO_NOT_PUBLISH = 4
        

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


class DATA_DNS_RPC_UTF8_STRING_LIST(NDRUniConformantArray):
    item = CHAR

class PTR_DNS_RPC_UTF8_STRING_LIST(NDRPOINTER):
    referent = (
        ('Data', DATA_DNS_RPC_UTF8_STRING_LIST),
    )

class DNS_RPC_UTF8_STRING_LIST(NDRSTRUCT):
    structure = (
	('dwCount', DWORD),	('pszStrings', PTR_DNS_RPC_UTF8_STRING_LIST),

    )
        

class DATA_DNS_RPC_UNICODE_STRING_LIST(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DNS_RPC_UNICODE_STRING_LIST(NDRPOINTER):
    referent = (
        ('Data', DATA_DNS_RPC_UNICODE_STRING_LIST),
    )

class DNS_RPC_UNICODE_STRING_LIST(NDRSTRUCT):
    structure = (
	('dwCount', DWORD),	('pwszStrings', PTR_DNS_RPC_UNICODE_STRING_LIST),

    )
        

class DNS_RPC_CRITERIA_COMPARATOR:
	Equals=1 = 0
        

class DNS_RPC_POLICY_CONDITION:
	DNS_AND = 0
        

class DNS_RPC_POLICY_LEVEL:
	DnsPolicyServerLevel = 0,
	DnsPolicyZoneLevel = 1
        

class DNS_RPC_POLICY_ACTION_TYPE:
	DnsPolicyDeny = 0,
	DnsPolicyAllow = 1,
	DnsPolicyIgnore = 2
        

class DNS_RPC_POLICY_TYPE:
	DnsPolicyQueryProcessing = 0,
	DnsPolicyZoneTransfer = 1,
	DnsPolicyDynamicUpdate = 2,
	DnsPolicyRecursion = 3
        

class DNS_RPC_CRITERIA_ENUM:
	DnsPolicyCriteriaSubnet = 0,
	DnsPolicyCriteriaTransportProtocol = 1,
	DnsPolicyCriteriaNetworkProtocol = 2,
	DnsPolicyCriteriaInterface = 3,
	DnsPolicyCriteriaFqdn = 4,
	DnsPolicyCriteriaQtype = 5,
	DnsPolicyCriteriaTime = 6
        

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


class DNS_RRL_MODE_ENUM:
	DnsRRLLogOnly = 0,
	DnsRRLEnabled = 1
        

class DNS_RPC_RRL_PARAMS(NDRSTRUCT):
    structure = (
        ('dwResponsesPerSecond', DWORD),('dwErrorsPerSecond', DWORD),('dwLeakRate', DWORD),('dwTCRate', DWORD),('dwTotalResponsesInWindow', DWORD),('dwWindowSize', DWORD),('dwIPv4PrefixLength', DWORD),('dwIPv6PrefixLength', DWORD),('eMode', DNS_RRL_MODE_ENUM),('dwFlags', DWORD),('fSetDefault', BOOL),
    )
class PDNS_RPC_RRL_PARAMS(NDRPOINTER):
    referent = (
        ('Data', DNS_RPC_RRL_PARAMS),
    )    

