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

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#netdfs Definition

#################################################################################

MSRPC_UUID_NETDFS = uuidtup_to_bin(('4fc742e0-4a10-11cf-8273-00aa004ae673','0.0'))

NET_API_STATUS = DWORD
NETDFS_SERVER_OR_DOMAIN_HANDLE = WCHAR

DfsInvalidPriorityClass = -1,
DfsSiteCostNormalPriorityClass = 0,
DfsGlobalHighPriorityClass = 1,
DfsSiteCostHighPriorityClass = 2,
DfsSiteCostLowPriorityClass = 3,
DfsGlobalLowPriorityClass = 4
        

class DFS_TARGET_PRIORITY(NDRSTRUCT):
    structure = (
        ('TargetPriorityClass', DFS_TARGET_PRIORITY_CLASS),('TargetPriorityRank', UNSIGNED_SHORT),('Reserved', UNSIGNED_SHORT),
    )


class DFS_STORAGE_INFO(NDRSTRUCT):
    structure = (
        ('State', UNSIGNED_LONG),('ServerName', WCHAR),('ShareName', WCHAR),
    )


class DFS_STORAGE_INFO_1(NDRSTRUCT):
    structure = (
        ('State', UNSIGNED_LONG),('ServerName', WCHAR),('ShareName', WCHAR),('TargetPriority', DFS_TARGET_PRIORITY),
    )
class PDFS_STORAGE_INFO_1(NDRPOINTER):
    referent = (
        ('Data', DFS_STORAGE_INFO_1),
    )    
class LPDFS_STORAGE_INFO_1(NDRPOINTER):
    referent = (
        ('Data', DFS_STORAGE_INFO_1),
    )    


class DFSM_ROOT_LIST_ENTRY(NDRSTRUCT):
    structure = (
        ('ServerShare', WCHAR),
    )


class DFSM_ROOT_LIST(NDRSTRUCT):
    structure = (
        ('cEntries', DWORD),('Entry', DFSM_ROOT_LIST_ENTRY),
    )


DFS_NAMESPACE_VERSION_ORIGIN_COMBINED = 0,
DFS_NAMESPACE_VERSION_ORIGIN_SERVER = 0
        

class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(NDRSTRUCT):
    structure = (
        ('DomainDfsMajorVersion', UNSIGNED_LONG),('DomainDfsMinorVersion', UNSIGNED_LONG),('DomainDfsCapabilities', ULONGLONG),('StandaloneDfsMajorVersion', UNSIGNED_LONG),('StandaloneDfsMinorVersion', UNSIGNED_LONG),('StandaloneDfsCapabilities', ULONGLONG),
    )
class PDFS_SUPPORTED_NAMESPACE_VERSION_INFO(NDRPOINTER):
    referent = (
        ('Data', DFS_SUPPORTED_NAMESPACE_VERSION_INFO),
    )    


class DFS_INFO_1(NDRSTRUCT):
    structure = (
        ('EntryPath', WCHAR),
    )


class DFS_INFO_2(NDRSTRUCT):
    structure = (
        ('EntryPath', WCHAR),('Comment', WCHAR),('State', DWORD),('NumberOfStorages', DWORD),
    )


class DATA_DFS_INFO_3(NDRUniConformantArray):
    item = DFS_STORAGE_INFO

class PTR_DFS_INFO_3(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_3),
    )

class DFS_INFO_3(NDRSTRUCT):
    structure = (
	('EntryPath', WCHAR),	('Comment', WCHAR),	('State', DWORD),	('NumberOfStorages', DWORD),	('Storage', PTR_DFS_INFO_3),

    )
        

class DATA_DFS_INFO_4(NDRUniConformantArray):
    item = DFS_STORAGE_INFO

class PTR_DFS_INFO_4(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_4),
    )

class DFS_INFO_4(NDRSTRUCT):
    structure = (
	('EntryPath', WCHAR),	('Comment', WCHAR),	('State', DWORD),	('Timeout', UNSIGNED_LONG),	('Guid', GUID),	('NumberOfStorages', DWORD),	('Storage', PTR_DFS_INFO_4),

    )
        

class DFS_INFO_5(NDRSTRUCT):
    structure = (
        ('EntryPath', WCHAR),('Comment', WCHAR),('State', DWORD),('Timeout', UNSIGNED_LONG),('Guid', GUID),('PropertyFlags', UNSIGNED_LONG),('MetadataSize', UNSIGNED_LONG),('NumberOfStorages', DWORD),
    )


class DATA_DFS_INFO_6(NDRUniConformantArray):
    item = DFS_STORAGE_INFO_1

class PTR_DFS_INFO_6(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_6),
    )

class DFS_INFO_6(NDRSTRUCT):
    structure = (
	('EntryPath', WCHAR),	('Comment', WCHAR),	('State', DWORD),	('Timeout', UNSIGNED_LONG),	('Guid', GUID),	('PropertyFlags', UNSIGNED_LONG),	('MetadataSize', UNSIGNED_LONG),	('NumberOfStorages', DWORD),	('Storage', PTR_DFS_INFO_6),

    )
        

class DFS_INFO_7(NDRSTRUCT):
    structure = (
        ('GenerationGuid', GUID),
    )


class DFS_INFO_8(NDRSTRUCT):
    structure = (
        ('EntryPath', WCHAR),('Comment', WCHAR),('State', DWORD),('Timeout', UNSIGNED_LONG),('Guid', GUID),('PropertyFlags', UNSIGNED_LONG),('MetadataSize', UNSIGNED_LONG),('SecurityDescriptorLength', ULONG),('pSecurityDescriptor', PUCHAR),('NumberOfStorages', DWORD),
    )
class LPDFS_INFO_8(NDRPOINTER):
    referent = (
        ('Data', DFS_INFO_8),
    )    


class DFS_INFO_9(NDRSTRUCT):
    structure = (
        ('EntryPath', WCHAR),('Comment', WCHAR),('State', DWORD),('Timeout', UNSIGNED_LONG),('Guid', GUID),('PropertyFlags', UNSIGNED_LONG),('MetadataSize', UNSIGNED_LONG),('SecurityDescriptorLength', ULONG),('pSecurityDescriptor', PUCHAR),('NumberOfStorages', DWORD),('Storage', LPDFS_STORAGE_INFO_1),
    )
class LPDFS_INFO_9(NDRPOINTER):
    referent = (
        ('Data', DFS_INFO_9),
    )    


class DFS_INFO_50(NDRSTRUCT):
    structure = (
        ('NamespaceMajorVersion', UNSIGNED_LONG),('NamespaceMinorVersion', UNSIGNED_LONG),('NamespaceCapabilities', UNSIGNED___INT64),
    )


class DFS_INFO_100(NDRSTRUCT):
    structure = (
        ('Comment', WCHAR),
    )


class DFS_INFO_101(NDRSTRUCT):
    structure = (
        ('State', UNSIGNED_LONG),
    )


class DFS_INFO_102(NDRSTRUCT):
    structure = (
        ('Timeout', UNSIGNED_LONG),
    )


class DFS_INFO_103(NDRSTRUCT):
    structure = (
        ('PropertyFlagMask', UNSIGNED_LONG),('PropertyFlags', UNSIGNED_LONG),
    )


class DFS_INFO_104(NDRSTRUCT):
    structure = (
        ('TargetPriority', DFS_TARGET_PRIORITY),
    )


class DFS_INFO_105(NDRSTRUCT):
    structure = (
        ('Comment', WCHAR),('State', DWORD),('Timeout', UNSIGNED_LONG),('PropertyFlagMask', UNSIGNED_LONG),('PropertyFlags', UNSIGNED_LONG),
    )


class DFS_INFO_106(NDRSTRUCT):
    structure = (
        ('State', DWORD),('TargetPriority', DFS_TARGET_PRIORITY),
    )


class DFS_INFO_107(NDRSTRUCT):
    structure = (
        ('Comment', WCHAR),('State', DWORD),('Timeout', UNSIGNED_LONG),('PropertyFlagMask', UNSIGNED_LONG),('PropertyFlags', UNSIGNED_LONG),('SecurityDescriptorLength', ULONG),('pSecurityDescriptor', PUCHAR),
    )


class DFS_INFO_150(NDRSTRUCT):
    structure = (
        ('SecurityDescriptorLength', ULONG),('pSecurityDescriptor', PUCHAR),
    )


class DFS_INFO_200(NDRSTRUCT):
    structure = (
        ('FtDfsName', WCHAR),
    )


class DFS_INFO_300(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('DfsName', WCHAR),
    )


class DFS_INFO_STRUCT(NDRUNION):
    union = {
        1: ('DfsInfo1',DFS_INFO_1),2: ('DfsInfo2',DFS_INFO_2),3: ('DfsInfo3',DFS_INFO_3),4: ('DfsInfo4',DFS_INFO_4),5: ('DfsInfo5',DFS_INFO_5),6: ('DfsInfo6',DFS_INFO_6),7: ('DfsInfo7',DFS_INFO_7),8: ('DfsInfo8',DFS_INFO_8),9: ('DfsInfo9',DFS_INFO_9),50: ('DfsInfo50',DFS_INFO_50),100: ('DfsInfo100',DFS_INFO_100),101: ('DfsInfo101',DFS_INFO_101),102: ('DfsInfo102',DFS_INFO_102),103: ('DfsInfo103',DFS_INFO_103),104: ('DfsInfo104',DFS_INFO_104),105: ('DfsInfo105',DFS_INFO_105),106: ('DfsInfo106',DFS_INFO_106),107: ('DfsInfo107',DFS_INFO_107),150: ('DfsInfo150',DFS_INFO_150),
    }
        

class DATA_DFS_INFO_1_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_1

class PTR_DFS_INFO_1_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_1_CONTAINER),
    )

class DFS_INFO_1_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_1_CONTAINER),

    )
        

class DATA_DFS_INFO_2_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_2

class PTR_DFS_INFO_2_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_2_CONTAINER),
    )

class DFS_INFO_2_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_2_CONTAINER),

    )
        

class DATA_DFS_INFO_3_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_3

class PTR_DFS_INFO_3_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_3_CONTAINER),
    )

class DFS_INFO_3_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_3_CONTAINER),

    )
        

class DATA_DFS_INFO_4_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_4

class PTR_DFS_INFO_4_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_4_CONTAINER),
    )

class DFS_INFO_4_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_4_CONTAINER),

    )
        

class DATA_DFS_INFO_5_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_5

class PTR_DFS_INFO_5_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_5_CONTAINER),
    )

class DFS_INFO_5_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_5_CONTAINER),

    )
        

class DATA_DFS_INFO_6_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_6

class PTR_DFS_INFO_6_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_6_CONTAINER),
    )

class DFS_INFO_6_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_6_CONTAINER),

    )
        

class DFS_INFO_8_CONTAINER(NDRSTRUCT):
    structure = (
        ('EntriesRead', DWORD),('Buffer', LPDFS_INFO_8),
    )
class LPDFS_INFO_8_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DFS_INFO_8_CONTAINER),
    )    


class DFS_INFO_9_CONTAINER(NDRSTRUCT):
    structure = (
        ('EntriesRead', DWORD),('Buffer', LPDFS_INFO_9),
    )
class LPDFS_INFO_9_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DFS_INFO_9_CONTAINER),
    )    


class DATA_DFS_INFO_200_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_200

class PTR_DFS_INFO_200_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_200_CONTAINER),
    )

class DFS_INFO_200_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_200_CONTAINER),

    )
        

class DATA_DFS_INFO_300_CONTAINER(NDRUniConformantArray):
    item = DFS_INFO_300

class PTR_DFS_INFO_300_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', DATA_DFS_INFO_300_CONTAINER),
    )

class DFS_INFO_300_CONTAINER(NDRSTRUCT):
    structure = (
	('EntriesRead', DWORD),	('Buffer', PTR_DFS_INFO_300_CONTAINER),

    )
        

class DFSINFOCONTAINER(NDRUNION):
    union = {
        1: ('DfsInfo1Container',DFS_INFO_1_CONTAINER),2: ('DfsInfo2Container',DFS_INFO_2_CONTAINER),3: ('DfsInfo3Container',DFS_INFO_3_CONTAINER),4: ('DfsInfo4Container',DFS_INFO_4_CONTAINER),5: ('DfsInfo5Container',DFS_INFO_5_CONTAINER),6: ('DfsInfo6Container',DFS_INFO_6_CONTAINER),8: ('DfsInfo8Container',DFS_INFO_8_CONTAINER),9: ('DfsInfo9Container',DFS_INFO_9_CONTAINER),200: ('DfsInfo200Container',DFS_INFO_200_CONTAINER),300: ('DfsInfo300Container',DFS_INFO_300_CONTAINER),
    }
        

class DFS_INFO_ENUM_STRUCT(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('DfsInfoContainer', DFSINFOCONTAINER),
    )


class NetrDfsManagerGetVersion(NDRCALL):
    opnum = 0
    structure = (

    )

class NetrDfsManagerGetVersionResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsAdd(NDRCALL):
    opnum = 1
    structure = (
		('DfsEntryPath', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('Comment', WCHAR),
		('Flags', DWORD),
    )

class NetrDfsAddResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsRemove(NDRCALL):
    opnum = 2
    structure = (
		('DfsEntryPath', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
    )

class NetrDfsRemoveResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsSetInfo(NDRCALL):
    opnum = 3
    structure = (
		('DfsEntryPath', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('Level', DWORD),
		('DfsInfo', DFS_INFO_STRUCT),
    )

class NetrDfsSetInfoResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsGetInfo(NDRCALL):
    opnum = 4
    structure = (
		('DfsEntryPath', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('Level', DWORD),
    )

class NetrDfsGetInfoResponse(NDRCALL):
    structure = (
		('DfsInfo', DFS_INFO_STRUCT),
    )
        

class NetrDfsEnum(NDRCALL):
    opnum = 5
    structure = (
		('Level', DWORD),
		('PrefMaxLen', DWORD),
		('DfsEnum', DFS_INFO_ENUM_STRUCT),
		('ResumeHandle', DWORD),
    )

class NetrDfsEnumResponse(NDRCALL):
    structure = (
		('DfsEnum', DFS_INFO_ENUM_STRUCT),
		('ResumeHandle', DWORD),
    )
        

class NetrDfsMove(NDRCALL):
    opnum = 6
    structure = (
		('DfsEntryPath', WCHAR),
		('NewDfsEntryPath', WCHAR),
		('Flags', UNSIGNED_LONG),
    )

class NetrDfsMoveResponse(NDRCALL):
    structure = (

    )
        

class Opnum7NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum7NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum8NotUsedOnWire(NDRCALL):
    opnum = 8
    structure = (

    )

class Opnum8NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsAddFtRoot(NDRCALL):
    opnum = 10
    structure = (
		('ServerName', WCHAR),
		('DcName', WCHAR),
		('RootShare', WCHAR),
		('FtDfsName', WCHAR),
		('Comment', WCHAR),
		('ConfigDN', WCHAR),
		('NewFtDfs', BOOLEAN),
		('ApiFlags', DWORD),
		('ppRootList', DFSM_ROOT_LIST),
    )

class NetrDfsAddFtRootResponse(NDRCALL):
    structure = (
		('ppRootList', DFSM_ROOT_LIST),
    )
        

class NetrDfsRemoveFtRoot(NDRCALL):
    opnum = 11
    structure = (
		('ServerName', WCHAR),
		('DcName', WCHAR),
		('RootShare', WCHAR),
		('FtDfsName', WCHAR),
		('ApiFlags', DWORD),
		('ppRootList', DFSM_ROOT_LIST),
    )

class NetrDfsRemoveFtRootResponse(NDRCALL):
    structure = (
		('ppRootList', DFSM_ROOT_LIST),
    )
        

class NetrDfsAddStdRoot(NDRCALL):
    opnum = 12
    structure = (
		('ServerName', WCHAR),
		('RootShare', WCHAR),
		('Comment', WCHAR),
		('ApiFlags', DWORD),
    )

class NetrDfsAddStdRootResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsRemoveStdRoot(NDRCALL):
    opnum = 13
    structure = (
		('ServerName', WCHAR),
		('RootShare', WCHAR),
		('ApiFlags', DWORD),
    )

class NetrDfsRemoveStdRootResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsManagerInitialize(NDRCALL):
    opnum = 14
    structure = (
		('ServerName', WCHAR),
		('Flags', DWORD),
    )

class NetrDfsManagerInitializeResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsAddStdRootForced(NDRCALL):
    opnum = 15
    structure = (
		('ServerName', WCHAR),
		('RootShare', WCHAR),
		('Comment', WCHAR),
		('Share', WCHAR),
    )

class NetrDfsAddStdRootForcedResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsGetDcAddress(NDRCALL):
    opnum = 16
    structure = (
		('ServerName', WCHAR),
		('DcName', WCHAR),
		('IsRoot', BOOLEAN),
		('Timeout', UNSIGNED_LONG),
    )

class NetrDfsGetDcAddressResponse(NDRCALL):
    structure = (
		('DcName', WCHAR),
		('IsRoot', BOOLEAN),
		('Timeout', UNSIGNED_LONG),
    )
        

class NetrDfsSetDcAddress(NDRCALL):
    opnum = 17
    structure = (
		('ServerName', WCHAR),
		('DcName', WCHAR),
		('Timeout', DWORD),
		('Flags', DWORD),
    )

class NetrDfsSetDcAddressResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsFlushFtTable(NDRCALL):
    opnum = 18
    structure = (
		('DcName', WCHAR),
		('wszFtDfsName', WCHAR),
    )

class NetrDfsFlushFtTableResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsAdd2(NDRCALL):
    opnum = 19
    structure = (
		('DfsEntryPath', WCHAR),
		('DcName', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('Comment', WCHAR),
		('Flags', DWORD),
		('ppRootList', DFSM_ROOT_LIST),
    )

class NetrDfsAdd2Response(NDRCALL):
    structure = (
		('ppRootList', DFSM_ROOT_LIST),
    )
        

class NetrDfsRemove2(NDRCALL):
    opnum = 20
    structure = (
		('DfsEntryPath', WCHAR),
		('DcName', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('ppRootList', DFSM_ROOT_LIST),
    )

class NetrDfsRemove2Response(NDRCALL):
    structure = (
		('ppRootList', DFSM_ROOT_LIST),
    )
        

class NetrDfsEnumEx(NDRCALL):
    opnum = 21
    structure = (
		('DfsEntryPath', WCHAR),
		('Level', DWORD),
		('PrefMaxLen', DWORD),
		('DfsEnum', DFS_INFO_ENUM_STRUCT),
		('ResumeHandle', DWORD),
    )

class NetrDfsEnumExResponse(NDRCALL):
    structure = (
		('DfsEnum', DFS_INFO_ENUM_STRUCT),
		('ResumeHandle', DWORD),
    )
        

class NetrDfsSetInfo2(NDRCALL):
    opnum = 22
    structure = (
		('DfsEntryPath', WCHAR),
		('DcName', WCHAR),
		('ServerName', WCHAR),
		('ShareName', WCHAR),
		('Level', DWORD),
		('pDfsInfo', DFS_INFO_STRUCT),
		('ppRootList', DFSM_ROOT_LIST),
    )

class NetrDfsSetInfo2Response(NDRCALL):
    structure = (
		('ppRootList', DFSM_ROOT_LIST),
    )
        

class NetrDfsAddRootTarget(NDRCALL):
    opnum = 23
    structure = (
		('pDfsPath', LPWSTR),
		('pTargetPath', LPWSTR),
		('MajorVersion', ULONG),
		('pComment', LPWSTR),
		('NewNamespace', BOOLEAN),
		('Flags', ULONG),
    )

class NetrDfsAddRootTargetResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsRemoveRootTarget(NDRCALL):
    opnum = 24
    structure = (
		('pDfsPath', LPWSTR),
		('pTargetPath', LPWSTR),
		('Flags', ULONG),
    )

class NetrDfsRemoveRootTargetResponse(NDRCALL):
    structure = (

    )
        

class NetrDfsGetSupportedNamespaceVersion(NDRCALL):
    opnum = 25
    structure = (
		('Origin', DFS_NAMESPACE_VERSION_ORIGIN),
		('pName', NETDFS_SERVER_OR_DOMAIN_HANDLE),
    )

class NetrDfsGetSupportedNamespaceVersionResponse(NDRCALL):
    structure = (
		('pVersionInfo', PDFS_SUPPORTED_NAMESPACE_VERSION_INFO),
    )
        
OPNUMS = {
0 : (NetrDfsManagerGetVersion,NetrDfsManagerGetVersionResponse),
1 : (NetrDfsAdd,NetrDfsAddResponse),
2 : (NetrDfsRemove,NetrDfsRemoveResponse),
3 : (NetrDfsSetInfo,NetrDfsSetInfoResponse),
4 : (NetrDfsGetInfo,NetrDfsGetInfoResponse),
5 : (NetrDfsEnum,NetrDfsEnumResponse),
6 : (NetrDfsMove,NetrDfsMoveResponse),
7 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
8 : (Opnum8NotUsedOnWire,Opnum8NotUsedOnWireResponse),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (NetrDfsAddFtRoot,NetrDfsAddFtRootResponse),
11 : (NetrDfsRemoveFtRoot,NetrDfsRemoveFtRootResponse),
12 : (NetrDfsAddStdRoot,NetrDfsAddStdRootResponse),
13 : (NetrDfsRemoveStdRoot,NetrDfsRemoveStdRootResponse),
14 : (NetrDfsManagerInitialize,NetrDfsManagerInitializeResponse),
15 : (NetrDfsAddStdRootForced,NetrDfsAddStdRootForcedResponse),
16 : (NetrDfsGetDcAddress,NetrDfsGetDcAddressResponse),
17 : (NetrDfsSetDcAddress,NetrDfsSetDcAddressResponse),
18 : (NetrDfsFlushFtTable,NetrDfsFlushFtTableResponse),
19 : (NetrDfsAdd2,NetrDfsAdd2Response),
20 : (NetrDfsRemove2,NetrDfsRemove2Response),
21 : (NetrDfsEnumEx,NetrDfsEnumExResponse),
22 : (NetrDfsSetInfo2,NetrDfsSetInfo2Response),
23 : (NetrDfsAddRootTarget,NetrDfsAddRootTargetResponse),
24 : (NetrDfsRemoveRootTarget,NetrDfsRemoveRootTargetResponse),
25 : (NetrDfsGetSupportedNamespaceVersion,NetrDfsGetSupportedNamespaceVersionResponse),
}

