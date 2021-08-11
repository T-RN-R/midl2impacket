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

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#inetinfo Definition

#################################################################################

MSRPC_UUID_INETINFO = uuidtup_to_bin(('82ad4280-036b-11cf-972c-00aa006887b0','0.0'))

INET_INFO_IMPERSONATE_HANDLE = LPWSTR

class INET_INFO_CAP_FLAGS(NDRSTRUCT):
    structure = (
        ('Flag', DWORD),('Mask', DWORD),
    )
class LPINET_INFO_CAP_FLAGS(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_CAP_FLAGS),
    )    


class INET_INFO_CAPABILITIES_STRUCT(NDRSTRUCT):
    structure = (
        ('CapVersion', DWORD),('ProductType', DWORD),('MajorVersion', DWORD),('MinorVersion', DWORD),('BuildNumber', DWORD),('NumCapFlags', DWORD),('CapFlags', LPINET_INFO_CAP_FLAGS),
    )
class LPINET_INFO_CAPABILITIES_STRUCT(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_CAPABILITIES_STRUCT),
    )    


class INET_LOG_CONFIGURATION(NDRSTRUCT):
    structure = (
        ('inetLogType', DWORD),('ilPeriod', DWORD),('rgchLogFileDirectory', WCHAR),('cbSizeForTruncation', DWORD),('rgchDataSource', WCHAR),('rgchTableName', WCHAR),('rgchUserName', WCHAR),('rgchPassword', WCHAR),
    )
class LPINET_LOG_CONFIGURATION(NDRPOINTER):
    referent = (
        ('Data', INET_LOG_CONFIGURATION),
    )    


class INET_INFO_IP_SEC_ENTRY(NDRSTRUCT):
    structure = (
        ('dwMask', DWORD),('dwNetwork', DWORD),
    )
class LPINET_INFO_IP_SEC_ENTRY(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_IP_SEC_ENTRY),
    )    


class INET_INFO_IP_SEC_LIST(NDRSTRUCT):
    structure = (
        ('cEntries', DWORD),('aIPSecEntry', INET_INFO_IP_SEC_ENTRY),
    )
class LPINET_INFO_IP_SEC_LIST(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_IP_SEC_LIST),
    )    


class INET_INFO_VIRTUAL_ROOT_ENTRY(NDRSTRUCT):
    structure = (
        ('pszRoot', LPWSTR),('pszAddress', LPWSTR),('pszDirectory', LPWSTR),('dwMask', DWORD),('pszAccountName', LPWSTR),('AccountPassword', WCHAR),('dwError', DWORD),
    )
class LPINET_INFO_VIRTUAL_ROOT_ENTRY(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_VIRTUAL_ROOT_ENTRY),
    )    


class INET_INFO_VIRTUAL_ROOT_LIST(NDRSTRUCT):
    structure = (
        ('cEntries', DWORD),('aVirtRootEntry', INET_INFO_VIRTUAL_ROOT_ENTRY),
    )
class LPINET_INFO_VIRTUAL_ROOT_LIST(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_VIRTUAL_ROOT_LIST),
    )    


class INET_INFO_CONFIG_INFO(NDRSTRUCT):
    structure = (
        ('FieldControl', DWORD),('dwConnectionTimeout', DWORD),('dwMaxConnections', DWORD),('lpszAdminName', LPWSTR),('lpszAdminEmail', LPWSTR),('lpszServerComment', LPWSTR),('lpLogConfig', LPINET_LOG_CONFIGURATION),('LangId', WORD),('LocalId', LCID),('ProductId', BYTE),('fLogAnonymous', BOOL),('fLogNonAnonymous', BOOL),('lpszAnonUserName', LPWSTR),('szAnonPassword', WCHAR),('dwAuthentication', DWORD),('sPort', SHORT),('DenyIPList', LPINET_INFO_IP_SEC_LIST),('GrantIPList', LPINET_INFO_IP_SEC_LIST),('VirtualRoots', LPINET_INFO_VIRTUAL_ROOT_LIST),
    )
class LPINET_INFO_CONFIG_INFO(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_CONFIG_INFO),
    )    


class INET_INFO_SITE_ENTRY(NDRSTRUCT):
    structure = (
        ('pszComment', LPWSTR),('dwInstance', DWORD),
    )
class LPINET_INFO_SITE_ENTRY(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_SITE_ENTRY),
    )    


class INET_INFO_SITE_LIST(NDRSTRUCT):
    structure = (
        ('cEntries', DWORD),('aSiteEntry', INET_INFO_SITE_ENTRY),
    )
class LPINET_INFO_SITE_LIST(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_SITE_LIST),
    )    


class INET_INFO_GLOBAL_CONFIG_INFO(NDRSTRUCT):
    structure = (
        ('FieldControl', DWORD),('BandwidthLevel', DWORD),('cbMemoryCacheSize', DWORD),
    )
class LPINET_INFO_GLOBAL_CONFIG_INFO(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_GLOBAL_CONFIG_INFO),
    )    


class INETA_CACHE_STATISTICS(NDRSTRUCT):
    structure = (
        ('FilesCached', DWORD),('TotalFilesCached', DWORD),('FileHits', DWORD),('FileMisses', DWORD),('FileFlushes', DWORD),('CurrentFileCacheSize', DWORDLONG),('MaximumFileCacheSize', DWORDLONG),('FlushedEntries', DWORD),('TotalFlushed', DWORD),('URICached', DWORD),('TotalURICached', DWORD),('URIHits', DWORD),('URIMisses', DWORD),('URIFlushes', DWORD),('TotalURIFlushed', DWORD),('BlobCached', DWORD),('TotalBlobCached', DWORD),('BlobHits', DWORD),('BlobMisses', DWORD),('BlobFlushes', DWORD),('TotalBlobFlushed', DWORD),
    )
class LPINETA_CACHE_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', INETA_CACHE_STATISTICS),
    )    


class INETA_ATQ_STATISTICS(NDRSTRUCT):
    structure = (
        ('TotalBlockedRequests', DWORD),('TotalRejectedRequests', DWORD),('TotalAllowedRequests', DWORD),('CurrentBlockedRequests', DWORD),('MeasuredBandwidth', DWORD),
    )
class LPINETA_ATQ_STATISTICS(NDRPOINTER):
    referent = (
        ('Data', INETA_ATQ_STATISTICS),
    )    


class INET_INFO_STATISTICS_0(NDRSTRUCT):
    structure = (
        ('CacheCtrs', INETA_CACHE_STATISTICS),('AtqCtrs', INETA_ATQ_STATISTICS),('nAuxCounters', DWORD),('rgCounters', DWORD),
    )
class LPINET_INFO_STATISTICS_0(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_STATISTICS_0),
    )    


class INET_INFO_STATISTICS_INFO(NDRUNION):
    union = {
        0: ('InetStats0',LPINET_INFO_STATISTICS_0),
    }
        class LPINET_INFO_STATISTICS_INFO(NDRPOINTER):
    referent = (
        ('Data', INET_INFO_STATISTICS_INFO),
    )    


class W3_STATISTICS_1(NDRSTRUCT):
    structure = (
        ('TotalBytesSent', LARGE_INTEGER),('TotalBytesReceived', LARGE_INTEGER),('TotalFilesSent', DWORD),('TotalFilesReceived', DWORD),('CurrentAnonymousUsers', DWORD),('CurrentNonAnonymousUsers', DWORD),('TotalAnonymousUsers', DWORD),('TotalNonAnonymousUsers', DWORD),('MaxAnonymousUsers', DWORD),('MaxNonAnonymousUsers', DWORD),('CurrentConnections', DWORD),('MaxConnections', DWORD),('ConnectionAttempts', DWORD),('LogonAttempts', DWORD),('TotalOptions', DWORD),('TotalGets', DWORD),('TotalPosts', DWORD),('TotalHeads', DWORD),('TotalPuts', DWORD),('TotalDeletes', DWORD),('TotalTraces', DWORD),('TotalMove', DWORD),('TotalCopy', DWORD),('TotalMkcol', DWORD),('TotalPropfind', DWORD),('TotalProppatch', DWORD),('TotalSearch', DWORD),('TotalLock', DWORD),('TotalUnlock', DWORD),('TotalOthers', DWORD),('TotalCGIRequests', DWORD),('TotalBGIRequests', DWORD),('TotalNotFoundErrors', DWORD),('TotalLockedErrors', DWORD),('CurrentCalAuth', DWORD),('MaxCalAuth', DWORD),('TotalFailedCalAuth', DWORD),('CurrentCalSsl', DWORD),('MaxCalSsl', DWORD),('TotalFailedCalSsl', DWORD),('CurrentCGIRequests', DWORD),('CurrentBGIRequests', DWORD),('MaxCGIRequests', DWORD),('MaxBGIRequests', DWORD),('CurrentBlockedRequests', DWORD),('TotalBlockedRequests', DWORD),('TotalAllowedRequests', DWORD),('TotalRejectedRequests', DWORD),('MeasuredBw', DWORD),('ServiceUptime', DWORD),('TimeOfLastClear', DWORD),('nAuxCounters', DWORD),('rgCounters', DWORD),
    )
class LPW3_STATISTICS_1(NDRPOINTER):
    referent = (
        ('Data', W3_STATISTICS_1),
    )    


class W3_STATISTICS_STRUCT(NDRUNION):
    union = {
        0: ('StatInfo1',LPW3_STATISTICS_1),
    }
        class LPW3_STATISTICS_STRUCT(NDRPOINTER):
    referent = (
        ('Data', W3_STATISTICS_STRUCT),
    )    


class FTP_STATISTICS_0(NDRSTRUCT):
    structure = (
        ('TotalBytesSent', LARGE_INTEGER),('TotalBytesReceived', LARGE_INTEGER),('TotalFilesSent', DWORD),('TotalFilesReceived', DWORD),('CurrentAnonymousUsers', DWORD),('CurrentNonAnonymousUsers', DWORD),('TotalAnonymousUsers', DWORD),('TotalNonAnonymousUsers', DWORD),('MaxAnonymousUsers', DWORD),('MaxNonAnonymousUsers', DWORD),('CurrentConnections', DWORD),('MaxConnections', DWORD),('ConnectionAttempts', DWORD),('LogonAttempts', DWORD),('ServiceUptime', DWORD),('TotalAllowedRequests', DWORD),('TotalRejectedRequests', DWORD),('TotalBlockedRequests', DWORD),('CurrentBlockedRequests', DWORD),('MeasuredBandwidth', DWORD),('TimeOfLastClear', DWORD),
    )
class LPFTP_STATISTICS_0(NDRPOINTER):
    referent = (
        ('Data', FTP_STATISTICS_0),
    )    


class FTP_STATISTICS_STRUCT(NDRUNION):
    union = {
        0: ('StatInfo0',LPFTP_STATISTICS_0),
    }
        class LPFTP_STATISTICS_STRUCT(NDRPOINTER):
    referent = (
        ('Data', FTP_STATISTICS_STRUCT),
    )    


class IIS_USER_INFO_1(NDRSTRUCT):
    structure = (
        ('idUser', DWORD),('pszUser', LPWSTR),('fAnonymous', BOOL),('inetHost', DWORD),('tConnect', DWORD),
    )
class LPIIS_USER_INFO_1(NDRPOINTER):
    referent = (
        ('Data', IIS_USER_INFO_1),
    )    


class IIS_USER_INFO_1_CONTAINER(NDRSTRUCT):
    structure = (
        ('EntriesRead', DWORD),('Buffer', LPIIS_USER_INFO_1),
    )
class LPIIS_USER_INFO_1_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', IIS_USER_INFO_1_CONTAINER),
    )    


class CONFIGINFO(NDRUNION):
    union = {
        1: ('Level1',LPIIS_USER_INFO_1_CONTAINER),
    }
        

class IIS_USER_ENUM_STRUCT(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('ConfigInfo', CONFIGINFO),
    )
class LPIIS_USER_ENUM_STRUCT(NDRPOINTER):
    referent = (
        ('Data', IIS_USER_ENUM_STRUCT),
    )    


class R_InetInfoGetVersion(NDRCALL):
    opnum = 0
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwReserved', DWORD),
    )

class R_InetInfoGetVersionResponse(NDRCALL):
    structure = (
		('pdwVersion', DWORD),
    )
        

class R_InetInfoGetAdminInformation(NDRCALL):
    opnum = 1
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
    )

class R_InetInfoGetAdminInformationResponse(NDRCALL):
    structure = (
		('ppConfig', LPINET_INFO_CONFIG_INFO),
    )
        

class R_InetInfoGetSites(NDRCALL):
    opnum = 2
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
    )

class R_InetInfoGetSitesResponse(NDRCALL):
    structure = (
		('ppSites', LPINET_INFO_SITE_LIST),
    )
        

class R_InetInfoSetAdminInformation(NDRCALL):
    opnum = 3
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
		('pConfig', INET_INFO_CONFIG_INFO),
    )

class R_InetInfoSetAdminInformationResponse(NDRCALL):
    structure = (

    )
        

class R_InetInfoGetGlobalAdminInformation(NDRCALL):
    opnum = 4
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
    )

class R_InetInfoGetGlobalAdminInformationResponse(NDRCALL):
    structure = (
		('ppConfig', LPINET_INFO_GLOBAL_CONFIG_INFO),
    )
        

class R_InetInfoSetGlobalAdminInformation(NDRCALL):
    opnum = 5
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
		('pConfig', INET_INFO_GLOBAL_CONFIG_INFO),
    )

class R_InetInfoSetGlobalAdminInformationResponse(NDRCALL):
    structure = (

    )
        

class R_InetInfoQueryStatistics(NDRCALL):
    opnum = 6
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('Level', DWORD),
		('dwServerMask', DWORD),
    )

class R_InetInfoQueryStatisticsResponse(NDRCALL):
    structure = (
		('StatsInfo', LPINET_INFO_STATISTICS_INFO),
    )
        

class R_InetInfoClearStatistics(NDRCALL):
    opnum = 7
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
    )

class R_InetInfoClearStatisticsResponse(NDRCALL):
    structure = (

    )
        

class R_InetInfoFlushMemoryCache(NDRCALL):
    opnum = 8
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServerMask', DWORD),
    )

class R_InetInfoFlushMemoryCacheResponse(NDRCALL):
    structure = (

    )
        

class R_InetInfoGetServerCapabilities(NDRCALL):
    opnum = 9
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwReserved', DWORD),
    )

class R_InetInfoGetServerCapabilitiesResponse(NDRCALL):
    structure = (
		('ppCap', LPINET_INFO_CAPABILITIES_STRUCT),
    )
        

class R_W3QueryStatistics2(NDRCALL):
    opnum = 10
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwLevel', DWORD),
		('dwInstance', DWORD),
		('dwReserved', DWORD),
    )

class R_W3QueryStatistics2Response(NDRCALL):
    structure = (
		('InfoStruct', LPW3_STATISTICS_STRUCT),
    )
        

class R_W3ClearStatistics2(NDRCALL):
    opnum = 11
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwInstance', DWORD),
    )

class R_W3ClearStatistics2Response(NDRCALL):
    structure = (

    )
        

class R_FtpQueryStatistics2(NDRCALL):
    opnum = 12
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwLevel', DWORD),
		('dwInstance', DWORD),
		('dwReserved', DWORD),
    )

class R_FtpQueryStatistics2Response(NDRCALL):
    structure = (
		('InfoStruct', LPFTP_STATISTICS_STRUCT),
    )
        

class R_FtpClearStatistics2(NDRCALL):
    opnum = 13
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwInstance', DWORD),
    )

class R_FtpClearStatistics2Response(NDRCALL):
    structure = (

    )
        

class R_IISEnumerateUsers(NDRCALL):
    opnum = 14
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServiceId', DWORD),
		('dwInstance', DWORD),
		('InfoStruct', LPIIS_USER_ENUM_STRUCT),
    )

class R_IISEnumerateUsersResponse(NDRCALL):
    structure = (
		('InfoStruct', LPIIS_USER_ENUM_STRUCT),
    )
        

class R_IISDisconnectUser(NDRCALL):
    opnum = 15
    structure = (
		('pszServer', INET_INFO_IMPERSONATE_HANDLE),
		('dwServiceId', DWORD),
		('dwInstance', DWORD),
		('dwIdUser', DWORD),
    )

class R_IISDisconnectUserResponse(NDRCALL):
    structure = (

    )
        

class Opnum16NotUsedOnWire(NDRCALL):
    opnum = 16
    structure = (

    )

class Opnum16NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum17NotUsedOnWire(NDRCALL):
    opnum = 17
    structure = (

    )

class Opnum17NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (R_InetInfoGetVersion,R_InetInfoGetVersionResponse),
1 : (R_InetInfoGetAdminInformation,R_InetInfoGetAdminInformationResponse),
2 : (R_InetInfoGetSites,R_InetInfoGetSitesResponse),
3 : (R_InetInfoSetAdminInformation,R_InetInfoSetAdminInformationResponse),
4 : (R_InetInfoGetGlobalAdminInformation,R_InetInfoGetGlobalAdminInformationResponse),
5 : (R_InetInfoSetGlobalAdminInformation,R_InetInfoSetGlobalAdminInformationResponse),
6 : (R_InetInfoQueryStatistics,R_InetInfoQueryStatisticsResponse),
7 : (R_InetInfoClearStatistics,R_InetInfoClearStatisticsResponse),
8 : (R_InetInfoFlushMemoryCache,R_InetInfoFlushMemoryCacheResponse),
9 : (R_InetInfoGetServerCapabilities,R_InetInfoGetServerCapabilitiesResponse),
10 : (R_W3QueryStatistics2,R_W3QueryStatistics2Response),
11 : (R_W3ClearStatistics2,R_W3ClearStatistics2Response),
12 : (R_FtpQueryStatistics2,R_FtpQueryStatistics2Response),
13 : (R_FtpClearStatistics2,R_FtpClearStatistics2Response),
14 : (R_IISEnumerateUsers,R_IISEnumerateUsersResponse),
15 : (R_IISDisconnectUser,R_IISDisconnectUserResponse),
16 : (Opnum16NotUsedOnWire,Opnum16NotUsedOnWireResponse),
17 : (Opnum17NotUsedOnWire,Opnum17NotUsedOnWireResponse),
}

