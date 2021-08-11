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

#lsarpc Definition

#################################################################################

MSRPC_UUID_LSARPC = uuidtup_to_bin(('12345778-1234-ABCD-EF00-0123456789AB','0.0'))

LSAPR_HANDLE = VOID
SECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
PSECURITY_CONTEXT_TRACKING_MODE = UNSIGNED_CHAR
SECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT
PSECURITY_DESCRIPTOR_CONTROL = UNSIGNED_SHORT

class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
    item = CHAR

class PTR_UNSIGNED_SHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_SHORT),
    )

class UNSIGNED_SHORT(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_UNSIGNED_SHORT),

    )
        

class LSAPR_ACL(NDRSTRUCT):
    structure = (
        ('AclRevision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('AclSize', UNSIGNED_SHORT),('Dummy1', UNSIGNED_CHAR),
    )
class PLSAPR_ACL(NDRPOINTER):
    referent = (
        ('Data', LSAPR_ACL),
    )    


class LSAPR_SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_CHAR),('Sbz1', UNSIGNED_CHAR),('Control', SECURITY_DESCRIPTOR_CONTROL),('Owner', PRPC_SID),('Group', PRPC_SID),('Sacl', PLSAPR_ACL),('Dacl', PLSAPR_ACL),
    )
class PLSAPR_SECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', LSAPR_SECURITY_DESCRIPTOR),
    )    


SecurityAnonymous = 0,
SecurityIdentification = 1,
SecurityImpersonation = 2,
SecurityDelegation = 3
        

class SECURITY_QUALITY_OF_SERVICE(NDRSTRUCT):
    structure = (
        ('Length', UNSIGNED_LONG),('ImpersonationLevel', SECURITY_IMPERSONATION_LEVEL),('ContextTrackingMode', SECURITY_CONTEXT_TRACKING_MODE),('EffectiveOnly', UNSIGNED_CHAR),
    )
class PSECURITY_QUALITY_OF_SERVICE(NDRPOINTER):
    referent = (
        ('Data', SECURITY_QUALITY_OF_SERVICE),
    )    


class LSAPR_OBJECT_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('Length', UNSIGNED_LONG),('RootDirectory', UNSIGNED_CHAR),('ObjectName', PSTRING),('Attributes', UNSIGNED_LONG),('SecurityDescriptor', PLSAPR_SECURITY_DESCRIPTOR),('SecurityQualityOfService', PSECURITY_QUALITY_OF_SERVICE),
    )
class PLSAPR_OBJECT_ATTRIBUTES(NDRPOINTER):
    referent = (
        ('Data', LSAPR_OBJECT_ATTRIBUTES),
    )    


class LSAPR_TRUST_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('Sid', PRPC_SID),
    )
class PLSAPR_TRUST_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUST_INFORMATION),
    )    


PolicyAuditLogInformation = 1,
PolicyAuditEventsInformation = 1,
PolicyPrimaryDomainInformation = 1,
PolicyPdAccountInformation = 1,
PolicyAccountDomainInformation = 1,
PolicyLsaServerRoleInformation = 1,
PolicyReplicaSourceInformation = 1,
PolicyInformationNotUsedOnWire = 1,
PolicyModificationInformation = 1,
PolicyAuditFullSetInformation = 1,
PolicyAuditFullQueryInformation = 1,
PolicyDnsDomainInformation = 1,
PolicyDnsDomainInformationInt = 1,
PolicyLocalAccountDomainInformation = 1,
PolicyMachineAccountInformation = 1
        

AuditCategorySystem = 0,
AuditCategoryLogon = 0,
AuditCategoryObjectAccess = 0,
AuditCategoryPrivilegeUse = 0,
AuditCategoryDetailedTracking = 0,
AuditCategoryPolicyChange = 0,
AuditCategoryAccountManagement = 0,
AuditCategoryDirectoryServiceAccess = 0
        
LSA_UNICODE_STRING = RPC_UNICODE_STRING
PLSA_UNICODE_STRING = RPC_UNICODE_STRING

class POLICY_AUDIT_LOG_INFO(NDRSTRUCT):
    structure = (
        ('AuditLogPercentFull', UNSIGNED_LONG),('MaximumLogSize', UNSIGNED_LONG),('AuditRetentionPeriod', LARGE_INTEGER),('AuditLogFullShutdownInProgress', UNSIGNED_CHAR),('TimeToShutdown', LARGE_INTEGER),('NextAuditRecordId', UNSIGNED_LONG),
    )
class PPOLICY_AUDIT_LOG_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_AUDIT_LOG_INFO),
    )    


PolicyServerRoleBackup = 2
        

class POLICY_LSA_SERVER_ROLE_INFO(NDRSTRUCT):
    structure = (
        ('LsaServerRole', POLICY_LSA_SERVER_ROLE),
    )
class PPOLICY_LSA_SERVER_ROLE_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_LSA_SERVER_ROLE_INFO),
    )    


class POLICY_MODIFICATION_INFO(NDRSTRUCT):
    structure = (
        ('ModifiedId', LARGE_INTEGER),('DatabaseCreationTime', LARGE_INTEGER),
    )
class PPOLICY_MODIFICATION_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_MODIFICATION_INFO),
    )    


class POLICY_AUDIT_FULL_SET_INFO(NDRSTRUCT):
    structure = (
        ('ShutDownOnFull', UNSIGNED_CHAR),
    )
class PPOLICY_AUDIT_FULL_SET_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_AUDIT_FULL_SET_INFO),
    )    


class POLICY_AUDIT_FULL_QUERY_INFO(NDRSTRUCT):
    structure = (
        ('ShutDownOnFull', UNSIGNED_CHAR),('LogIsFull', UNSIGNED_CHAR),
    )
class PPOLICY_AUDIT_FULL_QUERY_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_AUDIT_FULL_QUERY_INFO),
    )    


PolicyDomainQualityOfServiceInformation = 1,
PolicyDomainEfsInformation = 2,
PolicyDomainKerberosTicketInformation = 3
        

class POLICY_DOMAIN_KERBEROS_TICKET_INFO(NDRSTRUCT):
    structure = (
        ('AuthenticationOptions', UNSIGNED_LONG),('MaxServiceTicketAge', LARGE_INTEGER),('MaxTicketAge', LARGE_INTEGER),('MaxRenewAge', LARGE_INTEGER),('MaxClockSkew', LARGE_INTEGER),('Reserved', LARGE_INTEGER),
    )
class PPOLICY_DOMAIN_KERBEROS_TICKET_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_DOMAIN_KERBEROS_TICKET_INFO),
    )    


class TRUSTED_POSIX_OFFSET_INFO(NDRSTRUCT):
    structure = (
        ('Offset', UNSIGNED_LONG),
    )
class PTRUSTED_POSIX_OFFSET_INFO(NDRPOINTER):
    referent = (
        ('Data', TRUSTED_POSIX_OFFSET_INFO),
    )    


TrustedDomainNameInformation = 1,
TrustedControllersInformation = 1,
TrustedPosixOffsetInformation = 1,
TrustedPasswordInformation = 1,
TrustedDomainInformationBasic = 1,
TrustedDomainInformationEx = 1,
TrustedDomainAuthInformation = 1,
TrustedDomainFullInformation = 1,
TrustedDomainAuthInformationInternal = 1,
TrustedDomainFullInformationInternal = 1,
TrustedDomainInformationEx2Internal = 1,
TrustedDomainFullInformation2Internal = 1
        

ForestTrustTopLevelName = 0,
ForestTrustTopLevelNameEx = 1,
ForestTrustDomainInfo = 2,
ForestTrustRecordTypeLast = ForestTrustDomainInfo
        

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_LONG),	('Buffer', PTR_UNSIGNED_LONG),

    )
        

class LSA_FOREST_TRUST_DOMAIN_INFO(NDRSTRUCT):
    structure = (
        ('Sid', PRPC_SID),('DnsName', LSA_UNICODE_STRING),('NetbiosName', LSA_UNICODE_STRING),
    )
class PLSA_FOREST_TRUST_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', LSA_FOREST_TRUST_DOMAIN_INFO),
    )    


class FORESTTRUSTDATA(NDRUNION):
    union = {
        ForestTrustTopLevelName: ('TopLevelName',LSA_UNICODE_STRING),ForestTrustDomainInfo: ('DomainInfo',LSA_FOREST_TRUST_DOMAIN_INFO),3: ('Data',LSA_FOREST_TRUST_BINARY_DATA),
    }
        

class LSA_FOREST_TRUST_RECORD(NDRSTRUCT):
    structure = (
        ('Flags', UNSIGNED_LONG),('ForestTrustType', LSA_FOREST_TRUST_RECORD_TYPE),('Time', LARGE_INTEGER),('ForestTrustData', FORESTTRUSTDATA),
    )
class PLSA_FOREST_TRUST_RECORD(NDRPOINTER):
    referent = (
        ('Data', LSA_FOREST_TRUST_RECORD),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = PLSA_FOREST_TRUST_RECORD

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('RecordCount', UNSIGNED_LONG),	('Entries', PTR_UNSIGNED_LONG),

    )
        

CollisionTdo = 0,
CollisionXref = 0
        

class LSA_FOREST_TRUST_COLLISION_RECORD(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('Type', LSA_FOREST_TRUST_COLLISION_RECORD_TYPE),('Flags', UNSIGNED_LONG),('Name', LSA_UNICODE_STRING),
    )
class PLSA_FOREST_TRUST_COLLISION_RECORD(NDRPOINTER):
    referent = (
        ('Data', LSA_FOREST_TRUST_COLLISION_RECORD),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = PLSA_FOREST_TRUST_COLLISION_RECORD

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('RecordCount', UNSIGNED_LONG),	('Entries', PTR_UNSIGNED_LONG),

    )
        
PLSAPR_HANDLE = LSAPR_HANDLE

class LSAPR_ACCOUNT_INFORMATION(NDRSTRUCT):
    structure = (
        ('Sid', PRPC_SID),
    )
class PLSAPR_ACCOUNT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_ACCOUNT_INFORMATION),
    )    


class LSAPR_ACCOUNT_ENUM_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Information', PLSAPR_ACCOUNT_INFORMATION),
    )
class PLSAPR_ACCOUNT_ENUM_BUFFER(NDRPOINTER):
    referent = (
        ('Data', LSAPR_ACCOUNT_ENUM_BUFFER),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_LONG),	('SecurityDescriptor', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_LUID_AND_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('Luid', LUID),('Attributes', UNSIGNED_LONG),
    )
class PLSAPR_LUID_AND_ATTRIBUTES(NDRPOINTER):
    referent = (
        ('Data', LSAPR_LUID_AND_ATTRIBUTES),
    )    


class LSAPR_PRIVILEGE_SET(NDRSTRUCT):
    structure = (
        ('PrivilegeCount', UNSIGNED_LONG),('Control', UNSIGNED_LONG),('Privilege', LSAPR_LUID_AND_ATTRIBUTES),
    )
class PLSAPR_PRIVILEGE_SET(NDRPOINTER):
    referent = (
        ('Data', LSAPR_PRIVILEGE_SET),
    )    


class LSAPR_POLICY_PRIVILEGE_DEF(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('LocalValue', LUID),
    )
class PLSAPR_POLICY_PRIVILEGE_DEF(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_PRIVILEGE_DEF),
    )    


class LSAPR_PRIVILEGE_ENUM_BUFFER(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Privileges', PLSAPR_POLICY_PRIVILEGE_DEF),
    )
class PLSAPR_PRIVILEGE_ENUM_BUFFER(NDRPOINTER):
    referent = (
        ('Data', LSAPR_PRIVILEGE_ENUM_BUFFER),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_LONG),	('MaximumLength', UNSIGNED_LONG),	('Buffer', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_TRUSTED_ENUM_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Information', PLSAPR_TRUST_INFORMATION),
    )
class PLSAPR_TRUSTED_ENUM_BUFFER(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_ENUM_BUFFER),
    )    


class LSAPR_POLICY_ACCOUNT_DOM_INFO(NDRSTRUCT):
    structure = (
        ('DomainName', RPC_UNICODE_STRING),('DomainSid', PRPC_SID),
    )
class PLSAPR_POLICY_ACCOUNT_DOM_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_ACCOUNT_DOM_INFO),
    )    


class LSAPR_POLICY_PRIMARY_DOM_INFO(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('Sid', PRPC_SID),
    )
class PLSAPR_POLICY_PRIMARY_DOM_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_PRIMARY_DOM_INFO),
    )    


class LSAPR_POLICY_DNS_DOMAIN_INFO(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('DnsDomainName', RPC_UNICODE_STRING),('DnsForestName', RPC_UNICODE_STRING),('DomainGuid', GUID),('Sid', PRPC_SID),
    )
class PLSAPR_POLICY_DNS_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_DNS_DOMAIN_INFO),
    )    


class LSAPR_POLICY_PD_ACCOUNT_INFO(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),
    )
class PLSAPR_POLICY_PD_ACCOUNT_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_PD_ACCOUNT_INFO),
    )    


class LSAPR_POLICY_REPLICA_SRCE_INFO(NDRSTRUCT):
    structure = (
        ('ReplicaSource', RPC_UNICODE_STRING),('ReplicaAccountName', RPC_UNICODE_STRING),
    )
class PLSAPR_POLICY_REPLICA_SRCE_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_REPLICA_SRCE_INFO),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('AuditingMode', UNSIGNED_CHAR),	('EventAuditingOptions', PTR_UNSIGNED_CHAR),
	('MaximumAuditEventCount', UNSIGNED_LONG),
    )
        

class LSAPR_POLICY_MACHINE_ACCT_INFO(NDRSTRUCT):
    structure = (
        ('Rid', UNSIGNED_LONG),('Sid', PRPC_SID),
    )
class PLSAPR_POLICY_MACHINE_ACCT_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_MACHINE_ACCT_INFO),
    )    


class LSAPR_POLICY_INFORMATION(NDRUNION):
    union = {
        PolicyAuditLogInformation: ('PolicyAuditLogInfo',POLICY_AUDIT_LOG_INFO),PolicyAuditEventsInformation: ('PolicyAuditEventsInfo',LSAPR_POLICY_AUDIT_EVENTS_INFO),PolicyPrimaryDomainInformation: ('PolicyPrimaryDomainInfo',LSAPR_POLICY_PRIMARY_DOM_INFO),PolicyAccountDomainInformation: ('PolicyAccountDomainInfo',LSAPR_POLICY_ACCOUNT_DOM_INFO),PolicyPdAccountInformation: ('PolicyPdAccountInfo',LSAPR_POLICY_PD_ACCOUNT_INFO),PolicyLsaServerRoleInformation: ('PolicyServerRoleInfo',POLICY_LSA_SERVER_ROLE_INFO),PolicyReplicaSourceInformation: ('PolicyReplicaSourceInfo',LSAPR_POLICY_REPLICA_SRCE_INFO),PolicyModificationInformation: ('PolicyModificationInfo',POLICY_MODIFICATION_INFO),PolicyAuditFullSetInformation: ('PolicyAuditFullSetInfo',POLICY_AUDIT_FULL_SET_INFO),PolicyAuditFullQueryInformation: ('PolicyAuditFullQueryInfo',POLICY_AUDIT_FULL_QUERY_INFO),PolicyDnsDomainInformation: ('PolicyDnsDomainInfo',LSAPR_POLICY_DNS_DOMAIN_INFO),PolicyDnsDomainInformationInt: ('PolicyDnsDomainInfoInt',LSAPR_POLICY_DNS_DOMAIN_INFO),PolicyLocalAccountDomainInformation: ('PolicyLocalAccountDomainInfo',LSAPR_POLICY_ACCOUNT_DOM_INFO),PolicyMachineAccountInformation: ('PolicyMachineAccountInfo',LSAPR_POLICY_MACHINE_ACCT_INFO),
    }
        class PLSAPR_POLICY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_INFORMATION),
    )    


class POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO(NDRSTRUCT):
    structure = (
        ('QualityOfService', UNSIGNED_LONG),
    )
class PPOLICY_DOMAIN_QUALITY_OF_SERVICE_INFO(NDRPOINTER):
    referent = (
        ('Data', POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('InfoLength', UNSIGNED_LONG),	('EfsBlob', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_POLICY_DOMAIN_INFORMATION(NDRUNION):
    union = {
        PolicyDomainQualityOfServiceInformation: ('PolicyDomainQualityOfServiceInfo',POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO),PolicyDomainEfsInformation: ('PolicyDomainEfsInfo',LSAPR_POLICY_DOMAIN_EFS_INFO),PolicyDomainKerberosTicketInformation: ('PolicyDomainKerbTicketInfo',POLICY_DOMAIN_KERBEROS_TICKET_INFO),
    }
        class PLSAPR_POLICY_DOMAIN_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_POLICY_DOMAIN_INFORMATION),
    )    


class LSAPR_TRUSTED_DOMAIN_NAME_INFO(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),
    )
class PLSAPR_TRUSTED_DOMAIN_NAME_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_NAME_INFO),
    )    


class LSAPR_TRUSTED_CONTROLLERS_INFO(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('Names', PRPC_UNICODE_STRING),
    )
class PLSAPR_TRUSTED_CONTROLLERS_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_CONTROLLERS_INFO),
    )    


class LSAPR_TRUSTED_PASSWORD_INFO(NDRSTRUCT):
    structure = (
        ('Password', PLSAPR_CR_CIPHER_VALUE),('OldPassword', PLSAPR_CR_CIPHER_VALUE),
    )
class PLSAPR_TRUSTED_PASSWORD_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_PASSWORD_INFO),
    )    


class LSAPR_TRUSTED_DOMAIN_INFORMATION_EX(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('FlatName', RPC_UNICODE_STRING),('Sid', PRPC_SID),('TrustDirection', UNSIGNED_LONG),('TrustType', UNSIGNED_LONG),('TrustAttributes', UNSIGNED_LONG),
    )
class PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_INFORMATION_EX),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('LastUpdateTime', LARGE_INTEGER),	('AuthType', UNSIGNED_LONG),	('AuthInfoLength', UNSIGNED_LONG),	('AuthInfo', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION(NDRSTRUCT):
    structure = (
        ('IncomingAuthInfos', UNSIGNED_LONG),('IncomingAuthenticationInformation', PLSAPR_AUTH_INFORMATION),('IncomingPreviousAuthenticationInformation', PLSAPR_AUTH_INFORMATION),('OutgoingAuthInfos', UNSIGNED_LONG),('OutgoingAuthenticationInformation', PLSAPR_AUTH_INFORMATION),('OutgoingPreviousAuthenticationInformation', PLSAPR_AUTH_INFORMATION),
    )
class PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION),
    )    


class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION(NDRSTRUCT):
    structure = (
        ('Information', LSAPR_TRUSTED_DOMAIN_INFORMATION_EX),('PosixOffset', TRUSTED_POSIX_OFFSET_INFO),('AuthInformation', LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION),
    )
class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION),
    )    

LSAPR_TRUSTED_DOMAIN_INFORMATION_BASIC = LSAPR_TRUST_INFORMATION

class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('AuthSize', UNSIGNED_LONG),	('AuthBlob', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL(NDRSTRUCT):
    structure = (
        ('AuthBlob', LSAPR_TRUSTED_DOMAIN_AUTH_BLOB),
    )
class PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL),
    )    


class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL(NDRSTRUCT):
    structure = (
        ('Information', LSAPR_TRUSTED_DOMAIN_INFORMATION_EX),('PosixOffset', TRUSTED_POSIX_OFFSET_INFO),('AuthInformation', LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL),
    )
class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL),
    )    


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('Name', RPC_UNICODE_STRING),	('FlatName', RPC_UNICODE_STRING),	('Sid', PRPC_SID),	('TrustDirection', UNSIGNED_LONG),	('TrustType', UNSIGNED_LONG),	('TrustAttributes', UNSIGNED_LONG),	('ForestTrustLength', UNSIGNED_LONG),	('ForestTrustInfo', PTR_UNSIGNED_LONG),

    )
        

class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2(NDRSTRUCT):
    structure = (
        ('Information', LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2),('PosixOffset', TRUSTED_POSIX_OFFSET_INFO),('AuthInformation', LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION),
    )
class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2),
    )    


class TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES(NDRSTRUCT):
    structure = (
        ('SupportedEncryptionTypes', UNSIGNED_LONG),
    )
class PTRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES(NDRPOINTER):
    referent = (
        ('Data', TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES),
    )    


class LSAPR_TRUSTED_DOMAIN_INFO(NDRUNION):
    union = {
        TrustedDomainNameInformation: ('TrustedDomainNameInfo',LSAPR_TRUSTED_DOMAIN_NAME_INFO),TrustedControllersInformation: ('TrustedControllersInfo',LSAPR_TRUSTED_CONTROLLERS_INFO),TrustedPosixOffsetInformation: ('TrustedPosixOffsetInfo',TRUSTED_POSIX_OFFSET_INFO),TrustedPasswordInformation: ('TrustedPasswordInfo',LSAPR_TRUSTED_PASSWORD_INFO),TrustedDomainInformationBasic: ('TrustedDomainInfoBasic',LSAPR_TRUSTED_DOMAIN_INFORMATION_BASIC),TrustedDomainInformationEx: ('TrustedDomainInfoEx',LSAPR_TRUSTED_DOMAIN_INFORMATION_EX),TrustedDomainAuthInformation: ('TrustedAuthInfo',LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION),TrustedDomainFullInformation: ('TrustedFullInfo',LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION),TrustedDomainAuthInformationInternal: ('TrustedAuthInfoInternal',LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL),TrustedDomainFullInformationInternal: ('TrustedFullInfoInternal',LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL),TrustedDomainInformationEx2Internal: ('TrustedDomainInfoEx2',LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2),TrustedDomainFullInformation2Internal: ('TrustedFullInfo2',LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2),TrustedDomainSupportedEncryptionTypes: ('TrustedDomainSETs',TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES),
    }
        class PLSAPR_TRUSTED_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_DOMAIN_INFO),
    )    


class LSAPR_USER_RIGHT_SET(NDRSTRUCT):
    structure = (
        ('Entries', UNSIGNED_LONG),('UserRights', PRPC_UNICODE_STRING),
    )
class PLSAPR_USER_RIGHT_SET(NDRPOINTER):
    referent = (
        ('Data', LSAPR_USER_RIGHT_SET),
    )    


class LSAPR_TRUSTED_ENUM_BUFFER_EX(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('EnumerationBuffer', PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX),
    )
class PLSAPR_TRUSTED_ENUM_BUFFER_EX(NDRPOINTER):
    referent = (
        ('Data', LSAPR_TRUSTED_ENUM_BUFFER_EX),
    )    


class LsarClose(NDRCALL):
    opnum = 0
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
    )

class LsarCloseResponse(NDRCALL):
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarEnumeratePrivileges(NDRCALL):
    opnum = 2
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class LsarEnumeratePrivilegesResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('EnumerationBuffer', PLSAPR_PRIVILEGE_ENUM_BUFFER),
    )
        

class LsarQuerySecurityObject(NDRCALL):
    opnum = 3
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
		('SecurityInformation', SECURITY_INFORMATION),
    )

class LsarQuerySecurityObjectResponse(NDRCALL):
    structure = (
		('SecurityDescriptor', PLSAPR_SR_SECURITY_DESCRIPTOR),
    )
        

class LsarSetSecurityObject(NDRCALL):
    opnum = 4
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
		('SecurityInformation', SECURITY_INFORMATION),
		('SecurityDescriptor', PLSAPR_SR_SECURITY_DESCRIPTOR),
    )

class LsarSetSecurityObjectResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarOpenPolicy(NDRCALL):
    opnum = 6
    structure = (
		('SystemName', WCHAR_T),
		('ObjectAttributes', PLSAPR_OBJECT_ATTRIBUTES),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenPolicyResponse(NDRCALL):
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
    )
        

class LsarQueryInformationPolicy(NDRCALL):
    opnum = 7
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_INFORMATION_CLASS),
    )

class LsarQueryInformationPolicyResponse(NDRCALL):
    structure = (
		('PolicyInformation', PLSAPR_POLICY_INFORMATION),
    )
        

class LsarSetInformationPolicy(NDRCALL):
    opnum = 8
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_INFORMATION_CLASS),
		('PolicyInformation', PLSAPR_POLICY_INFORMATION),
    )

class LsarSetInformationPolicyResponse(NDRCALL):
    structure = (

    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarCreateAccount(NDRCALL):
    opnum = 10
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('AccountSid', PRPC_SID),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarCreateAccountResponse(NDRCALL):
    structure = (
		('AccountHandle', LSAPR_HANDLE),
    )
        

class LsarEnumerateAccounts(NDRCALL):
    opnum = 11
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class LsarEnumerateAccountsResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('EnumerationBuffer', PLSAPR_ACCOUNT_ENUM_BUFFER),
    )
        

class LsarCreateTrustedDomain(NDRCALL):
    opnum = 12
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainInformation', PLSAPR_TRUST_INFORMATION),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarCreateTrustedDomainResponse(NDRCALL):
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
    )
        

class LsarEnumerateTrustedDomains(NDRCALL):
    opnum = 13
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class LsarEnumerateTrustedDomainsResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('EnumerationBuffer', PLSAPR_TRUSTED_ENUM_BUFFER),
    )
        

class Lsar_LSA_TM_14(NDRCALL):
    opnum = 14
    structure = (

    )

class Lsar_LSA_TM_14Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_TM_15(NDRCALL):
    opnum = 15
    structure = (

    )

class Lsar_LSA_TM_15Response(NDRCALL):
    structure = (

    )
        

class LsarCreateSecret(NDRCALL):
    opnum = 16
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('SecretName', PRPC_UNICODE_STRING),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarCreateSecretResponse(NDRCALL):
    structure = (
		('SecretHandle', LSAPR_HANDLE),
    )
        

class LsarOpenAccount(NDRCALL):
    opnum = 17
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('AccountSid', PRPC_SID),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenAccountResponse(NDRCALL):
    structure = (
		('AccountHandle', LSAPR_HANDLE),
    )
        

class LsarEnumeratePrivilegesAccount(NDRCALL):
    opnum = 18
    structure = (
		('AccountHandle', LSAPR_HANDLE),
    )

class LsarEnumeratePrivilegesAccountResponse(NDRCALL):
    structure = (
		('Privileges', PLSAPR_PRIVILEGE_SET),
    )
        

class LsarAddPrivilegesToAccount(NDRCALL):
    opnum = 19
    structure = (
		('AccountHandle', LSAPR_HANDLE),
		('Privileges', PLSAPR_PRIVILEGE_SET),
    )

class LsarAddPrivilegesToAccountResponse(NDRCALL):
    structure = (

    )
        

class LsarRemovePrivilegesFromAccount(NDRCALL):
    opnum = 20
    structure = (
		('AccountHandle', LSAPR_HANDLE),
		('AllPrivileges', UNSIGNED_CHAR),
		('Privileges', PLSAPR_PRIVILEGE_SET),
    )

class LsarRemovePrivilegesFromAccountResponse(NDRCALL):
    structure = (

    )
        

class Opnum21NotUsedOnWire(NDRCALL):
    opnum = 21
    structure = (

    )

class Opnum21NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum22NotUsedOnWire(NDRCALL):
    opnum = 22
    structure = (

    )

class Opnum22NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarGetSystemAccessAccount(NDRCALL):
    opnum = 23
    structure = (
		('AccountHandle', LSAPR_HANDLE),
    )

class LsarGetSystemAccessAccountResponse(NDRCALL):
    structure = (
		('SystemAccess', UNSIGNED_LONG),
    )
        

class LsarSetSystemAccessAccount(NDRCALL):
    opnum = 24
    structure = (
		('AccountHandle', LSAPR_HANDLE),
		('SystemAccess', UNSIGNED_LONG),
    )

class LsarSetSystemAccessAccountResponse(NDRCALL):
    structure = (

    )
        

class LsarOpenTrustedDomain(NDRCALL):
    opnum = 25
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainSid', PRPC_SID),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenTrustedDomainResponse(NDRCALL):
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
    )
        

class LsarQueryInfoTrustedDomain(NDRCALL):
    opnum = 26
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
    )

class LsarQueryInfoTrustedDomainResponse(NDRCALL):
    structure = (
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )
        

class LsarSetInformationTrustedDomain(NDRCALL):
    opnum = 27
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )

class LsarSetInformationTrustedDomainResponse(NDRCALL):
    structure = (

    )
        

class LsarOpenSecret(NDRCALL):
    opnum = 28
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('SecretName', PRPC_UNICODE_STRING),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenSecretResponse(NDRCALL):
    structure = (
		('SecretHandle', LSAPR_HANDLE),
    )
        

class LsarSetSecret(NDRCALL):
    opnum = 29
    structure = (
		('SecretHandle', LSAPR_HANDLE),
		('EncryptedCurrentValue', PLSAPR_CR_CIPHER_VALUE),
		('EncryptedOldValue', PLSAPR_CR_CIPHER_VALUE),
    )

class LsarSetSecretResponse(NDRCALL):
    structure = (

    )
        

class LsarQuerySecret(NDRCALL):
    opnum = 30
    structure = (
		('SecretHandle', LSAPR_HANDLE),
		('EncryptedCurrentValue', PLSAPR_CR_CIPHER_VALUE),
		('CurrentValueSetTime', PLARGE_INTEGER),
		('EncryptedOldValue', PLSAPR_CR_CIPHER_VALUE),
		('OldValueSetTime', PLARGE_INTEGER),
    )

class LsarQuerySecretResponse(NDRCALL):
    structure = (
		('EncryptedCurrentValue', PLSAPR_CR_CIPHER_VALUE),
		('CurrentValueSetTime', PLARGE_INTEGER),
		('EncryptedOldValue', PLSAPR_CR_CIPHER_VALUE),
		('OldValueSetTime', PLARGE_INTEGER),
    )
        

class LsarLookupPrivilegeValue(NDRCALL):
    opnum = 31
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
    )

class LsarLookupPrivilegeValueResponse(NDRCALL):
    structure = (
		('Value', PLUID),
    )
        

class LsarLookupPrivilegeName(NDRCALL):
    opnum = 32
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('Value', PLUID),
    )

class LsarLookupPrivilegeNameResponse(NDRCALL):
    structure = (
		('Name', PRPC_UNICODE_STRING),
    )
        

class LsarLookupPrivilegeDisplayName(NDRCALL):
    opnum = 33
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
		('ClientLanguage', SHORT),
		('ClientSystemDefaultLanguage', SHORT),
    )

class LsarLookupPrivilegeDisplayNameResponse(NDRCALL):
    structure = (
		('DisplayName', PRPC_UNICODE_STRING),
		('LanguageReturned', UNSIGNED_SHORT),
    )
        

class LsarDeleteObject(NDRCALL):
    opnum = 34
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
    )

class LsarDeleteObjectResponse(NDRCALL):
    structure = (
		('ObjectHandle', LSAPR_HANDLE),
    )
        

class LsarEnumerateAccountsWithUserRight(NDRCALL):
    opnum = 35
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('UserRight', PRPC_UNICODE_STRING),
    )

class LsarEnumerateAccountsWithUserRightResponse(NDRCALL):
    structure = (
		('EnumerationBuffer', PLSAPR_ACCOUNT_ENUM_BUFFER),
    )
        

class LsarEnumerateAccountRights(NDRCALL):
    opnum = 36
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('AccountSid', PRPC_SID),
    )

class LsarEnumerateAccountRightsResponse(NDRCALL):
    structure = (
		('UserRights', PLSAPR_USER_RIGHT_SET),
    )
        

class LsarAddAccountRights(NDRCALL):
    opnum = 37
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('AccountSid', PRPC_SID),
		('UserRights', PLSAPR_USER_RIGHT_SET),
    )

class LsarAddAccountRightsResponse(NDRCALL):
    structure = (

    )
        

class LsarRemoveAccountRights(NDRCALL):
    opnum = 38
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('AccountSid', PRPC_SID),
		('AllRights', UNSIGNED_CHAR),
		('UserRights', PLSAPR_USER_RIGHT_SET),
    )

class LsarRemoveAccountRightsResponse(NDRCALL):
    structure = (

    )
        

class LsarQueryTrustedDomainInfo(NDRCALL):
    opnum = 39
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainSid', PRPC_SID),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
    )

class LsarQueryTrustedDomainInfoResponse(NDRCALL):
    structure = (
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )
        

class LsarSetTrustedDomainInfo(NDRCALL):
    opnum = 40
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainSid', PRPC_SID),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )

class LsarSetTrustedDomainInfoResponse(NDRCALL):
    structure = (

    )
        

class LsarDeleteTrustedDomain(NDRCALL):
    opnum = 41
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainSid', PRPC_SID),
    )

class LsarDeleteTrustedDomainResponse(NDRCALL):
    structure = (

    )
        

class LsarStorePrivateData(NDRCALL):
    opnum = 42
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('KeyName', PRPC_UNICODE_STRING),
		('EncryptedData', PLSAPR_CR_CIPHER_VALUE),
    )

class LsarStorePrivateDataResponse(NDRCALL):
    structure = (

    )
        

class LsarRetrievePrivateData(NDRCALL):
    opnum = 43
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('KeyName', PRPC_UNICODE_STRING),
		('EncryptedData', PLSAPR_CR_CIPHER_VALUE),
    )

class LsarRetrievePrivateDataResponse(NDRCALL):
    structure = (
		('EncryptedData', PLSAPR_CR_CIPHER_VALUE),
    )
        

class LsarOpenPolicy2(NDRCALL):
    opnum = 44
    structure = (
		('SystemName', WCHAR_T),
		('ObjectAttributes', PLSAPR_OBJECT_ATTRIBUTES),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenPolicy2Response(NDRCALL):
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
    )
        

class Lsar_LSA_TM_45(NDRCALL):
    opnum = 45
    structure = (

    )

class Lsar_LSA_TM_45Response(NDRCALL):
    structure = (

    )
        

class LsarQueryInformationPolicy2(NDRCALL):
    opnum = 46
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_INFORMATION_CLASS),
    )

class LsarQueryInformationPolicy2Response(NDRCALL):
    structure = (
		('PolicyInformation', PLSAPR_POLICY_INFORMATION),
    )
        

class LsarSetInformationPolicy2(NDRCALL):
    opnum = 47
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_INFORMATION_CLASS),
		('PolicyInformation', PLSAPR_POLICY_INFORMATION),
    )

class LsarSetInformationPolicy2Response(NDRCALL):
    structure = (

    )
        

class LsarQueryTrustedDomainInfoByName(NDRCALL):
    opnum = 48
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainName', PRPC_UNICODE_STRING),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
    )

class LsarQueryTrustedDomainInfoByNameResponse(NDRCALL):
    structure = (
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )
        

class LsarSetTrustedDomainInfoByName(NDRCALL):
    opnum = 49
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainName', PRPC_UNICODE_STRING),
		('InformationClass', TRUSTED_INFORMATION_CLASS),
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFO),
    )

class LsarSetTrustedDomainInfoByNameResponse(NDRCALL):
    structure = (

    )
        

class LsarEnumerateTrustedDomainsEx(NDRCALL):
    opnum = 50
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class LsarEnumerateTrustedDomainsExResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('EnumerationBuffer', PLSAPR_TRUSTED_ENUM_BUFFER_EX),
    )
        

class LsarCreateTrustedDomainEx(NDRCALL):
    opnum = 51
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX),
		('AuthenticationInformation', PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarCreateTrustedDomainExResponse(NDRCALL):
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
    )
        

class Opnum52NotUsedOnWire(NDRCALL):
    opnum = 52
    structure = (

    )

class Opnum52NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarQueryDomainInformationPolicy(NDRCALL):
    opnum = 53
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_DOMAIN_INFORMATION_CLASS),
    )

class LsarQueryDomainInformationPolicyResponse(NDRCALL):
    structure = (
		('PolicyDomainInformation', PLSAPR_POLICY_DOMAIN_INFORMATION),
    )
        

class LsarSetDomainInformationPolicy(NDRCALL):
    opnum = 54
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('InformationClass', POLICY_DOMAIN_INFORMATION_CLASS),
		('PolicyDomainInformation', PLSAPR_POLICY_DOMAIN_INFORMATION),
    )

class LsarSetDomainInformationPolicyResponse(NDRCALL):
    structure = (

    )
        

class LsarOpenTrustedDomainByName(NDRCALL):
    opnum = 55
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainName', PRPC_UNICODE_STRING),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarOpenTrustedDomainByNameResponse(NDRCALL):
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
    )
        

class Opnum56NotUsedOnWire(NDRCALL):
    opnum = 56
    structure = (

    )

class Opnum56NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_TM_57(NDRCALL):
    opnum = 57
    structure = (

    )

class Lsar_LSA_TM_57Response(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_TM_58(NDRCALL):
    opnum = 58
    structure = (

    )

class Lsar_LSA_TM_58Response(NDRCALL):
    structure = (

    )
        

class LsarCreateTrustedDomainEx2(NDRCALL):
    opnum = 59
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainInformation', PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX),
		('AuthenticationInformation', PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL),
		('DesiredAccess', ACCESS_MASK),
    )

class LsarCreateTrustedDomainEx2Response(NDRCALL):
    structure = (
		('TrustedDomainHandle', LSAPR_HANDLE),
    )
        

class Opnum60NotUsedOnWire(NDRCALL):
    opnum = 60
    structure = (

    )

class Opnum60NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum61NotUsedOnWire(NDRCALL):
    opnum = 61
    structure = (

    )

class Opnum61NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum62NotUsedOnWire(NDRCALL):
    opnum = 62
    structure = (

    )

class Opnum62NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum63NotUsedOnWire(NDRCALL):
    opnum = 63
    structure = (

    )

class Opnum63NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum64NotUsedOnWire(NDRCALL):
    opnum = 64
    structure = (

    )

class Opnum64NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum65NotUsedOnWire(NDRCALL):
    opnum = 65
    structure = (

    )

class Opnum65NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum66NotUsedOnWire(NDRCALL):
    opnum = 66
    structure = (

    )

class Opnum66NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum67NotUsedOnWire(NDRCALL):
    opnum = 67
    structure = (

    )

class Opnum67NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Lsar_LSA_TM_68(NDRCALL):
    opnum = 68
    structure = (

    )

class Lsar_LSA_TM_68Response(NDRCALL):
    structure = (

    )
        

class Opnum69NotUsedOnWire(NDRCALL):
    opnum = 69
    structure = (

    )

class Opnum69NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum70NotUsedOnWire(NDRCALL):
    opnum = 70
    structure = (

    )

class Opnum70NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum71NotUsedOnWire(NDRCALL):
    opnum = 71
    structure = (

    )

class Opnum71NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum72NotUsedOnWire(NDRCALL):
    opnum = 72
    structure = (

    )

class Opnum72NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class LsarQueryForestTrustInformation(NDRCALL):
    opnum = 73
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainName', PLSA_UNICODE_STRING),
		('HighestRecordType', LSA_FOREST_TRUST_RECORD_TYPE),
    )

class LsarQueryForestTrustInformationResponse(NDRCALL):
    structure = (
		('ForestTrustInfo', PLSA_FOREST_TRUST_INFORMATION),
    )
        

class LsarSetForestTrustInformation(NDRCALL):
    opnum = 74
    structure = (
		('PolicyHandle', LSAPR_HANDLE),
		('TrustedDomainName', PLSA_UNICODE_STRING),
		('HighestRecordType', LSA_FOREST_TRUST_RECORD_TYPE),
		('ForestTrustInfo', PLSA_FOREST_TRUST_INFORMATION),
		('CheckOnly', UNSIGNED_CHAR),
    )

class LsarSetForestTrustInformationResponse(NDRCALL):
    structure = (
		('CollisionInfo', PLSA_FOREST_TRUST_COLLISION_INFORMATION),
    )
        
OPNUMS = {
0 : (LsarClose,LsarCloseResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (LsarEnumeratePrivileges,LsarEnumeratePrivilegesResponse),
3 : (LsarQuerySecurityObject,LsarQuerySecurityObjectResponse),
4 : (LsarSetSecurityObject,LsarSetSecurityObjectResponse),
5 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
6 : (LsarOpenPolicy,LsarOpenPolicyResponse),
7 : (LsarQueryInformationPolicy,LsarQueryInformationPolicyResponse),
8 : (LsarSetInformationPolicy,LsarSetInformationPolicyResponse),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (LsarCreateAccount,LsarCreateAccountResponse),
11 : (LsarEnumerateAccounts,LsarEnumerateAccountsResponse),
12 : (LsarCreateTrustedDomain,LsarCreateTrustedDomainResponse),
13 : (LsarEnumerateTrustedDomains,LsarEnumerateTrustedDomainsResponse),
14 : (Lsar_LSA_TM_14,Lsar_LSA_TM_14Response),
15 : (Lsar_LSA_TM_15,Lsar_LSA_TM_15Response),
16 : (LsarCreateSecret,LsarCreateSecretResponse),
17 : (LsarOpenAccount,LsarOpenAccountResponse),
18 : (LsarEnumeratePrivilegesAccount,LsarEnumeratePrivilegesAccountResponse),
19 : (LsarAddPrivilegesToAccount,LsarAddPrivilegesToAccountResponse),
20 : (LsarRemovePrivilegesFromAccount,LsarRemovePrivilegesFromAccountResponse),
21 : (Opnum21NotUsedOnWire,Opnum21NotUsedOnWireResponse),
22 : (Opnum22NotUsedOnWire,Opnum22NotUsedOnWireResponse),
23 : (LsarGetSystemAccessAccount,LsarGetSystemAccessAccountResponse),
24 : (LsarSetSystemAccessAccount,LsarSetSystemAccessAccountResponse),
25 : (LsarOpenTrustedDomain,LsarOpenTrustedDomainResponse),
26 : (LsarQueryInfoTrustedDomain,LsarQueryInfoTrustedDomainResponse),
27 : (LsarSetInformationTrustedDomain,LsarSetInformationTrustedDomainResponse),
28 : (LsarOpenSecret,LsarOpenSecretResponse),
29 : (LsarSetSecret,LsarSetSecretResponse),
30 : (LsarQuerySecret,LsarQuerySecretResponse),
31 : (LsarLookupPrivilegeValue,LsarLookupPrivilegeValueResponse),
32 : (LsarLookupPrivilegeName,LsarLookupPrivilegeNameResponse),
33 : (LsarLookupPrivilegeDisplayName,LsarLookupPrivilegeDisplayNameResponse),
34 : (LsarDeleteObject,LsarDeleteObjectResponse),
35 : (LsarEnumerateAccountsWithUserRight,LsarEnumerateAccountsWithUserRightResponse),
36 : (LsarEnumerateAccountRights,LsarEnumerateAccountRightsResponse),
37 : (LsarAddAccountRights,LsarAddAccountRightsResponse),
38 : (LsarRemoveAccountRights,LsarRemoveAccountRightsResponse),
39 : (LsarQueryTrustedDomainInfo,LsarQueryTrustedDomainInfoResponse),
40 : (LsarSetTrustedDomainInfo,LsarSetTrustedDomainInfoResponse),
41 : (LsarDeleteTrustedDomain,LsarDeleteTrustedDomainResponse),
42 : (LsarStorePrivateData,LsarStorePrivateDataResponse),
43 : (LsarRetrievePrivateData,LsarRetrievePrivateDataResponse),
44 : (LsarOpenPolicy2,LsarOpenPolicy2Response),
45 : (Lsar_LSA_TM_45,Lsar_LSA_TM_45Response),
46 : (LsarQueryInformationPolicy2,LsarQueryInformationPolicy2Response),
47 : (LsarSetInformationPolicy2,LsarSetInformationPolicy2Response),
48 : (LsarQueryTrustedDomainInfoByName,LsarQueryTrustedDomainInfoByNameResponse),
49 : (LsarSetTrustedDomainInfoByName,LsarSetTrustedDomainInfoByNameResponse),
50 : (LsarEnumerateTrustedDomainsEx,LsarEnumerateTrustedDomainsExResponse),
51 : (LsarCreateTrustedDomainEx,LsarCreateTrustedDomainExResponse),
52 : (Opnum52NotUsedOnWire,Opnum52NotUsedOnWireResponse),
53 : (LsarQueryDomainInformationPolicy,LsarQueryDomainInformationPolicyResponse),
54 : (LsarSetDomainInformationPolicy,LsarSetDomainInformationPolicyResponse),
55 : (LsarOpenTrustedDomainByName,LsarOpenTrustedDomainByNameResponse),
56 : (Opnum56NotUsedOnWire,Opnum56NotUsedOnWireResponse),
57 : (Lsar_LSA_TM_57,Lsar_LSA_TM_57Response),
58 : (Lsar_LSA_TM_58,Lsar_LSA_TM_58Response),
59 : (LsarCreateTrustedDomainEx2,LsarCreateTrustedDomainEx2Response),
60 : (Opnum60NotUsedOnWire,Opnum60NotUsedOnWireResponse),
61 : (Opnum61NotUsedOnWire,Opnum61NotUsedOnWireResponse),
62 : (Opnum62NotUsedOnWire,Opnum62NotUsedOnWireResponse),
63 : (Opnum63NotUsedOnWire,Opnum63NotUsedOnWireResponse),
64 : (Opnum64NotUsedOnWire,Opnum64NotUsedOnWireResponse),
65 : (Opnum65NotUsedOnWire,Opnum65NotUsedOnWireResponse),
66 : (Opnum66NotUsedOnWire,Opnum66NotUsedOnWireResponse),
67 : (Opnum67NotUsedOnWire,Opnum67NotUsedOnWireResponse),
68 : (Lsar_LSA_TM_68,Lsar_LSA_TM_68Response),
69 : (Opnum69NotUsedOnWire,Opnum69NotUsedOnWireResponse),
70 : (Opnum70NotUsedOnWire,Opnum70NotUsedOnWireResponse),
71 : (Opnum71NotUsedOnWire,Opnum71NotUsedOnWireResponse),
72 : (Opnum72NotUsedOnWire,Opnum72NotUsedOnWireResponse),
73 : (LsarQueryForestTrustInformation,LsarQueryForestTrustInformationResponse),
74 : (LsarSetForestTrustInformation,LsarSetForestTrustInformationResponse),
}

