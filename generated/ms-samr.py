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

#samr Definition

#################################################################################

MSRPC_UUID_SAMR = uuidtup_to_bin(('12345778-1234-ABCD-EF00-0123456789AC','0.0'))


class DATA_RPC_STRING(NDRUniConformantArray):
    item = CHAR

class PTR_RPC_STRING(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_STRING),
    )

class RPC_STRING(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_STRING),

    )
        

class OLD_LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('LowPart', UNSIGNED_LONG),('HighPart', LONG),
    )
class POLD_LARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', OLD_LARGE_INTEGER),
    )    

PSAMPR_SERVER_NAME = WCHAR_T
SAMPR_HANDLE = VOID

class ENCRYPTED_LM_OWF_PASSWORD(NDRSTRUCT):
    structure = (
        ('data', CHAR),
    )
class PENCRYPTED_LM_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', ENCRYPTED_LM_OWF_PASSWORD),
    )    
ENCRYPTED_NT_OWF_PASSWORD = ENCRYPTED_LM_OWF_PASSWORD
class PENCRYPTED_NT_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', ENCRYPTED_LM_OWF_PASSWORD),
    )    


class DATA_SAMPR_ULONG_ARRAY(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_SAMPR_ULONG_ARRAY(NDRPOINTER):
    referent = (
        ('Data', DATA_SAMPR_ULONG_ARRAY),
    )

class SAMPR_ULONG_ARRAY(NDRSTRUCT):
    structure = (
	('Count', UNSIGNED_LONG),	('Element', PTR_SAMPR_ULONG_ARRAY),

    )
        

class SAMPR_SID_INFORMATION(NDRSTRUCT):
    structure = (
        ('SidPointer', PRPC_SID),
    )
class PSAMPR_SID_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_SID_INFORMATION),
    )    


class SAMPR_PSID_ARRAY(NDRSTRUCT):
    structure = (
        ('Count', UNSIGNED_LONG),('Sids', PSAMPR_SID_INFORMATION),
    )
class PSAMPR_PSID_ARRAY(NDRPOINTER):
    referent = (
        ('Data', SAMPR_PSID_ARRAY),
    )    


class SAMPR_PSID_ARRAY_OUT(NDRSTRUCT):
    structure = (
        ('Count', UNSIGNED_LONG),('Sids', PSAMPR_SID_INFORMATION),
    )
class PSAMPR_PSID_ARRAY_OUT(NDRPOINTER):
    referent = (
        ('Data', SAMPR_PSID_ARRAY_OUT),
    )    


class SAMPR_RETURNED_USTRING_ARRAY(NDRSTRUCT):
    structure = (
        ('Count', UNSIGNED_LONG),('Element', PRPC_UNICODE_STRING),
    )
class PSAMPR_RETURNED_USTRING_ARRAY(NDRPOINTER):
    referent = (
        ('Data', SAMPR_RETURNED_USTRING_ARRAY),
    )    


SidTypeUser = 1,
SidTypeGroup = 1,
SidTypeDomain = 1,
SidTypeAlias = 1,
SidTypeWellKnownGroup = 1,
SidTypeDeletedAccount = 1,
SidTypeInvalid = 1,
SidTypeUnknown = 1,
SidTypeComputer = 1
        

class DATA_RPC_SHORT_BLOB(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_RPC_SHORT_BLOB(NDRPOINTER):
    referent = (
        ('Data', DATA_RPC_SHORT_BLOB),
    )

class RPC_SHORT_BLOB(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_SHORT),	('MaximumLength', UNSIGNED_SHORT),	('Buffer', PTR_RPC_SHORT_BLOB),

    )
        

class SAMPR_RID_ENUMERATION(NDRSTRUCT):
    structure = (
        ('RelativeId', UNSIGNED_LONG),('Name', RPC_UNICODE_STRING),
    )
class PSAMPR_RID_ENUMERATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_RID_ENUMERATION),
    )    


class SAMPR_ENUMERATION_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_RID_ENUMERATION),
    )
class PSAMPR_ENUMERATION_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ENUMERATION_BUFFER),
    )    


class DATA_SAMPR_SR_SECURITY_DESCRIPTOR(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_SAMPR_SR_SECURITY_DESCRIPTOR(NDRPOINTER):
    referent = (
        ('Data', DATA_SAMPR_SR_SECURITY_DESCRIPTOR),
    )

class SAMPR_SR_SECURITY_DESCRIPTOR(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_LONG),	('SecurityDescriptor', PTR_SAMPR_SR_SECURITY_DESCRIPTOR),

    )
        

class GROUP_MEMBERSHIP(NDRSTRUCT):
    structure = (
        ('RelativeId', UNSIGNED_LONG),('Attributes', UNSIGNED_LONG),
    )
class PGROUP_MEMBERSHIP(NDRPOINTER):
    referent = (
        ('Data', GROUP_MEMBERSHIP),
    )    


class SAMPR_GET_GROUPS_BUFFER(NDRSTRUCT):
    structure = (
        ('MembershipCount', UNSIGNED_LONG),('Groups', PGROUP_MEMBERSHIP),
    )
class PSAMPR_GET_GROUPS_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_GET_GROUPS_BUFFER),
    )    


class DATA_SAMPR_GET_MEMBERS_BUFFER(NDRUniConformantArray):
    item = UNSIGNED_LONG

class PTR_SAMPR_GET_MEMBERS_BUFFER(NDRPOINTER):
    referent = (
        ('Data', DATA_SAMPR_GET_MEMBERS_BUFFER),
    )

class SAMPR_GET_MEMBERS_BUFFER(NDRSTRUCT):
    structure = (
	('MemberCount', UNSIGNED_LONG),	('Members', UNSIGNED_LONG),	('Attributes', PTR_SAMPR_GET_MEMBERS_BUFFER),

    )
        

class SAMPR_REVISION_INFO_V1(NDRSTRUCT):
    structure = (
        ('Revision', UNSIGNED_LONG),('SupportedFeatures', UNSIGNED_LONG),
    )
class PSAMPR_REVISION_INFO_V1(NDRPOINTER):
    referent = (
        ('Data', SAMPR_REVISION_INFO_V1),
    )    


class SAMPR_REVISION_INFO(NDRUNION):
    union = {
        1: ('V1',SAMPR_REVISION_INFO_V1),
    }
        class PSAMPR_REVISION_INFO(NDRPOINTER):
    referent = (
        ('Data', SAMPR_REVISION_INFO),
    )    


class USER_DOMAIN_PASSWORD_INFORMATION(NDRSTRUCT):
    structure = (
        ('MinPasswordLength', UNSIGNED_SHORT),('PasswordProperties', UNSIGNED_LONG),
    )
class PUSER_DOMAIN_PASSWORD_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', USER_DOMAIN_PASSWORD_INFORMATION),
    )    


DomainServerEnabled = 1
        

class DOMAIN_STATE_INFORMATION(NDRSTRUCT):
    structure = (
        ('DomainServerState', DOMAIN_SERVER_ENABLE_STATE),
    )
class PDOMAIN_STATE_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_STATE_INFORMATION),
    )    


DomainServerRoleBackup = 2,
DomainServerRolePrimary = 3
        

class DOMAIN_PASSWORD_INFORMATION(NDRSTRUCT):
    structure = (
        ('MinPasswordLength', UNSIGNED_SHORT),('PasswordHistoryLength', UNSIGNED_SHORT),('PasswordProperties', UNSIGNED_LONG),('MaxPasswordAge', OLD_LARGE_INTEGER),('MinPasswordAge', OLD_LARGE_INTEGER),
    )
class PDOMAIN_PASSWORD_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_PASSWORD_INFORMATION),
    )    


class DOMAIN_LOGOFF_INFORMATION(NDRSTRUCT):
    structure = (
        ('ForceLogoff', OLD_LARGE_INTEGER),
    )
class PDOMAIN_LOGOFF_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_LOGOFF_INFORMATION),
    )    


class DOMAIN_SERVER_ROLE_INFORMATION(NDRSTRUCT):
    structure = (
        ('DomainServerRole', DOMAIN_SERVER_ROLE),
    )
class PDOMAIN_SERVER_ROLE_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_SERVER_ROLE_INFORMATION),
    )    


class DOMAIN_MODIFIED_INFORMATION(NDRSTRUCT):
    structure = (
        ('DomainModifiedCount', OLD_LARGE_INTEGER),('CreationTime', OLD_LARGE_INTEGER),
    )
class PDOMAIN_MODIFIED_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_MODIFIED_INFORMATION),
    )    


class DOMAIN_MODIFIED_INFORMATION2(NDRSTRUCT):
    structure = (
        ('DomainModifiedCount', OLD_LARGE_INTEGER),('CreationTime', OLD_LARGE_INTEGER),('ModifiedCountAtLastPromotion', OLD_LARGE_INTEGER),
    )
class PDOMAIN_MODIFIED_INFORMATION2(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_MODIFIED_INFORMATION2),
    )    


class SAMPR_DOMAIN_GENERAL_INFORMATION(NDRSTRUCT):
    structure = (
        ('ForceLogoff', OLD_LARGE_INTEGER),('OemInformation', RPC_UNICODE_STRING),('DomainName', RPC_UNICODE_STRING),('ReplicaSourceNodeName', RPC_UNICODE_STRING),('DomainModifiedCount', OLD_LARGE_INTEGER),('DomainServerState', UNSIGNED_LONG),('DomainServerRole', UNSIGNED_LONG),('UasCompatibilityRequired', UNSIGNED_CHAR),('UserCount', UNSIGNED_LONG),('GroupCount', UNSIGNED_LONG),('AliasCount', UNSIGNED_LONG),
    )
class PSAMPR_DOMAIN_GENERAL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_GENERAL_INFORMATION),
    )    


class SAMPR_DOMAIN_GENERAL_INFORMATION2(NDRSTRUCT):
    structure = (
        ('I1', SAMPR_DOMAIN_GENERAL_INFORMATION),('LockoutDuration', LARGE_INTEGER),('LockoutObservationWindow', LARGE_INTEGER),('LockoutThreshold', UNSIGNED_SHORT),
    )
class PSAMPR_DOMAIN_GENERAL_INFORMATION2(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_GENERAL_INFORMATION2),
    )    


class SAMPR_DOMAIN_OEM_INFORMATION(NDRSTRUCT):
    structure = (
        ('OemInformation', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_OEM_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_OEM_INFORMATION),
    )    


class SAMPR_DOMAIN_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('DomainName', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_NAME_INFORMATION),
    )    


class SAMPR_DOMAIN_REPLICATION_INFORMATION(NDRSTRUCT):
    structure = (
        ('ReplicaSourceNodeName', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_REPLICATION_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_REPLICATION_INFORMATION),
    )    


class SAMPR_DOMAIN_LOCKOUT_INFORMATION(NDRSTRUCT):
    structure = (
        ('LockoutDuration', LARGE_INTEGER),('LockoutObservationWindow', LARGE_INTEGER),('LockoutThreshold', UNSIGNED_SHORT),
    )
class PSAMPR_DOMAIN_LOCKOUT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_LOCKOUT_INFORMATION),
    )    


DomainPasswordInformation = 1,
DomainGeneralInformation = 2,
DomainLogoffInformation = 3,
DomainOemInformation = 4,
DomainNameInformation = 5,
DomainReplicationInformation = 6,
DomainServerRoleInformation = 7,
DomainModifiedInformation = 8,
DomainStateInformation = 9,
DomainGeneralInformation2 = 11,
DomainLockoutInformation = 12,
DomainModifiedInformation2 = 13
        

class SAMPR_DOMAIN_INFO_BUFFER(NDRUNION):
    union = {
        DomainPasswordInformation: ('Password',DOMAIN_PASSWORD_INFORMATION),DomainGeneralInformation: ('General',SAMPR_DOMAIN_GENERAL_INFORMATION),DomainLogoffInformation: ('Logoff',DOMAIN_LOGOFF_INFORMATION),DomainOemInformation: ('Oem',SAMPR_DOMAIN_OEM_INFORMATION),DomainNameInformation: ('Name',SAMPR_DOMAIN_NAME_INFORMATION),DomainServerRoleInformation: ('Role',DOMAIN_SERVER_ROLE_INFORMATION),DomainReplicationInformation: ('Replication',SAMPR_DOMAIN_REPLICATION_INFORMATION),DomainModifiedInformation: ('Modified',DOMAIN_MODIFIED_INFORMATION),DomainStateInformation: ('State',DOMAIN_STATE_INFORMATION),DomainGeneralInformation2: ('General2',SAMPR_DOMAIN_GENERAL_INFORMATION2),DomainLockoutInformation: ('Lockout',SAMPR_DOMAIN_LOCKOUT_INFORMATION),DomainModifiedInformation2: ('Modified2',DOMAIN_MODIFIED_INFORMATION2),
    }
        class PSAMPR_DOMAIN_INFO_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_INFO_BUFFER),
    )    


DomainDisplayUser = 1,
DomainDisplayMachine = 1,
DomainDisplayGroup = 1,
DomainDisplayOemUser = 1
        

class SAMPR_DOMAIN_DISPLAY_USER(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('Rid', UNSIGNED_LONG),('AccountControl', UNSIGNED_LONG),('AccountName', RPC_UNICODE_STRING),('AdminComment', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_DISPLAY_USER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_USER),
    )    


class SAMPR_DOMAIN_DISPLAY_MACHINE(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('Rid', UNSIGNED_LONG),('AccountControl', UNSIGNED_LONG),('AccountName', RPC_UNICODE_STRING),('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_DISPLAY_MACHINE(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_MACHINE),
    )    


class SAMPR_DOMAIN_DISPLAY_GROUP(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('Rid', UNSIGNED_LONG),('Attributes', UNSIGNED_LONG),('AccountName', RPC_UNICODE_STRING),('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_DOMAIN_DISPLAY_GROUP(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_GROUP),
    )    


class SAMPR_DOMAIN_DISPLAY_OEM_USER(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('OemAccountName', RPC_STRING),
    )
class PSAMPR_DOMAIN_DISPLAY_OEM_USER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_OEM_USER),
    )    


class SAMPR_DOMAIN_DISPLAY_OEM_GROUP(NDRSTRUCT):
    structure = (
        ('Index', UNSIGNED_LONG),('OemAccountName', RPC_STRING),
    )
class PSAMPR_DOMAIN_DISPLAY_OEM_GROUP(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_OEM_GROUP),
    )    


class SAMPR_DOMAIN_DISPLAY_USER_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_DOMAIN_DISPLAY_USER),
    )
class PSAMPR_DOMAIN_DISPLAY_USER_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_USER_BUFFER),
    )    


class SAMPR_DOMAIN_DISPLAY_MACHINE_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_DOMAIN_DISPLAY_MACHINE),
    )
class PSAMPR_DOMAIN_DISPLAY_MACHINE_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_MACHINE_BUFFER),
    )    


class SAMPR_DOMAIN_DISPLAY_GROUP_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_DOMAIN_DISPLAY_GROUP),
    )
class PSAMPR_DOMAIN_DISPLAY_GROUP_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_GROUP_BUFFER),
    )    


class SAMPR_DOMAIN_DISPLAY_OEM_USER_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_DOMAIN_DISPLAY_OEM_USER),
    )
class PSAMPR_DOMAIN_DISPLAY_OEM_USER_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_OEM_USER_BUFFER),
    )    


class SAMPR_DOMAIN_DISPLAY_OEM_GROUP_BUFFER(NDRSTRUCT):
    structure = (
        ('EntriesRead', UNSIGNED_LONG),('Buffer', PSAMPR_DOMAIN_DISPLAY_OEM_GROUP),
    )
class PSAMPR_DOMAIN_DISPLAY_OEM_GROUP_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DOMAIN_DISPLAY_OEM_GROUP_BUFFER),
    )    


class SAMPR_DISPLAY_INFO_BUFFER(NDRUNION):
    union = {
        DomainDisplayUser: ('UserInformation',SAMPR_DOMAIN_DISPLAY_USER_BUFFER),DomainDisplayMachine: ('MachineInformation',SAMPR_DOMAIN_DISPLAY_MACHINE_BUFFER),DomainDisplayGroup: ('GroupInformation',SAMPR_DOMAIN_DISPLAY_GROUP_BUFFER),DomainDisplayOemUser: ('OemUserInformation',SAMPR_DOMAIN_DISPLAY_OEM_USER_BUFFER),DomainDisplayOemGroup: ('OemGroupInformation',SAMPR_DOMAIN_DISPLAY_OEM_GROUP_BUFFER),
    }
        class PSAMPR_DISPLAY_INFO_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_DISPLAY_INFO_BUFFER),
    )    


class GROUP_ATTRIBUTE_INFORMATION(NDRSTRUCT):
    structure = (
        ('Attributes', UNSIGNED_LONG),
    )
class PGROUP_ATTRIBUTE_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', GROUP_ATTRIBUTE_INFORMATION),
    )    


class SAMPR_GROUP_GENERAL_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('Attributes', UNSIGNED_LONG),('MemberCount', UNSIGNED_LONG),('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_GROUP_GENERAL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_GROUP_GENERAL_INFORMATION),
    )    


class SAMPR_GROUP_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),
    )
class PSAMPR_GROUP_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_GROUP_NAME_INFORMATION),
    )    


class SAMPR_GROUP_ADM_COMMENT_INFORMATION(NDRSTRUCT):
    structure = (
        ('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_GROUP_ADM_COMMENT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_GROUP_ADM_COMMENT_INFORMATION),
    )    


GroupGeneralInformation = 1,
GroupNameInformation = 1,
GroupAttributeInformation = 1,
GroupAdminCommentInformation = 1
        

class SAMPR_GROUP_INFO_BUFFER(NDRUNION):
    union = {
        GroupGeneralInformation: ('General',SAMPR_GROUP_GENERAL_INFORMATION),GroupNameInformation: ('Name',SAMPR_GROUP_NAME_INFORMATION),GroupAttributeInformation: ('Attribute',GROUP_ATTRIBUTE_INFORMATION),GroupAdminCommentInformation: ('AdminComment',SAMPR_GROUP_ADM_COMMENT_INFORMATION),GroupReplicationInformation: ('DoNotUse',SAMPR_GROUP_GENERAL_INFORMATION),
    }
        class PSAMPR_GROUP_INFO_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_GROUP_INFO_BUFFER),
    )    


class SAMPR_ALIAS_GENERAL_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),('MemberCount', UNSIGNED_LONG),('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_ALIAS_GENERAL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ALIAS_GENERAL_INFORMATION),
    )    


class SAMPR_ALIAS_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('Name', RPC_UNICODE_STRING),
    )
class PSAMPR_ALIAS_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ALIAS_NAME_INFORMATION),
    )    


class SAMPR_ALIAS_ADM_COMMENT_INFORMATION(NDRSTRUCT):
    structure = (
        ('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_ALIAS_ADM_COMMENT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ALIAS_ADM_COMMENT_INFORMATION),
    )    


AliasGeneralInformation = 1,
AliasNameInformation = 1
        

class SAMPR_ALIAS_INFO_BUFFER(NDRUNION):
    union = {
        AliasGeneralInformation: ('General',SAMPR_ALIAS_GENERAL_INFORMATION),AliasNameInformation: ('Name',SAMPR_ALIAS_NAME_INFORMATION),AliasAdminCommentInformation: ('AdminComment',SAMPR_ALIAS_ADM_COMMENT_INFORMATION),
    }
        class PSAMPR_ALIAS_INFO_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ALIAS_INFO_BUFFER),
    )    


class SAMPR_ENCRYPTED_USER_PASSWORD(NDRSTRUCT):
    structure = (
        ('Buffer', UNSIGNED_CHAR),
    )
class PSAMPR_ENCRYPTED_USER_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ENCRYPTED_USER_PASSWORD),
    )    


class SAMPR_ENCRYPTED_USER_PASSWORD_NEW(NDRSTRUCT):
    structure = (
        ('Buffer', UNSIGNED_CHAR),
    )
class PSAMPR_ENCRYPTED_USER_PASSWORD_NEW(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ENCRYPTED_USER_PASSWORD_NEW),
    )    


class USER_PRIMARY_GROUP_INFORMATION(NDRSTRUCT):
    structure = (
        ('PrimaryGroupId', UNSIGNED_LONG),
    )
class PUSER_PRIMARY_GROUP_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', USER_PRIMARY_GROUP_INFORMATION),
    )    


class USER_CONTROL_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserAccountControl', UNSIGNED_LONG),
    )
class PUSER_CONTROL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', USER_CONTROL_INFORMATION),
    )    


class USER_EXPIRES_INFORMATION(NDRSTRUCT):
    structure = (
        ('AccountExpires', OLD_LARGE_INTEGER),
    )
class PUSER_EXPIRES_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', USER_EXPIRES_INFORMATION),
    )    


class DATA_SAMPR_LOGON_HOURS(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_SAMPR_LOGON_HOURS(NDRPOINTER):
    referent = (
        ('Data', DATA_SAMPR_LOGON_HOURS),
    )

class SAMPR_LOGON_HOURS(NDRSTRUCT):
    structure = (
	('UnitsPerWeek', UNSIGNED_SHORT),	('LogonHours', PTR_SAMPR_LOGON_HOURS),

    )
        

class SAMPR_USER_ALL_INFORMATION(NDRSTRUCT):
    structure = (
        ('LastLogon', OLD_LARGE_INTEGER),('LastLogoff', OLD_LARGE_INTEGER),('PasswordLastSet', OLD_LARGE_INTEGER),('AccountExpires', OLD_LARGE_INTEGER),('PasswordCanChange', OLD_LARGE_INTEGER),('PasswordMustChange', OLD_LARGE_INTEGER),('UserName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('ScriptPath', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('AdminComment', RPC_UNICODE_STRING),('WorkStations', RPC_UNICODE_STRING),('UserComment', RPC_UNICODE_STRING),('Parameters', RPC_UNICODE_STRING),('LmOwfPassword', RPC_SHORT_BLOB),('NtOwfPassword', RPC_SHORT_BLOB),('PrivateData', RPC_UNICODE_STRING),('SecurityDescriptor', SAMPR_SR_SECURITY_DESCRIPTOR),('UserId', UNSIGNED_LONG),('PrimaryGroupId', UNSIGNED_LONG),('UserAccountControl', UNSIGNED_LONG),('WhichFields', UNSIGNED_LONG),('LogonHours', SAMPR_LOGON_HOURS),('BadPasswordCount', UNSIGNED_SHORT),('LogonCount', UNSIGNED_SHORT),('CountryCode', UNSIGNED_SHORT),('CodePage', UNSIGNED_SHORT),('LmPasswordPresent', UNSIGNED_CHAR),('NtPasswordPresent', UNSIGNED_CHAR),('PasswordExpired', UNSIGNED_CHAR),('PrivateDataSensitive', UNSIGNED_CHAR),
    )
class PSAMPR_USER_ALL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_ALL_INFORMATION),
    )    


class SAMPR_USER_GENERAL_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('PrimaryGroupId', UNSIGNED_LONG),('AdminComment', RPC_UNICODE_STRING),('UserComment', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_GENERAL_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_GENERAL_INFORMATION),
    )    


class SAMPR_USER_PREFERENCES_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserComment', RPC_UNICODE_STRING),('Reserved1', RPC_UNICODE_STRING),('CountryCode', UNSIGNED_SHORT),('CodePage', UNSIGNED_SHORT),
    )
class PSAMPR_USER_PREFERENCES_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_PREFERENCES_INFORMATION),
    )    


class SAMPR_USER_PARAMETERS_INFORMATION(NDRSTRUCT):
    structure = (
        ('Parameters', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_PARAMETERS_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_PARAMETERS_INFORMATION),
    )    


class SAMPR_USER_LOGON_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('UserId', UNSIGNED_LONG),('PrimaryGroupId', UNSIGNED_LONG),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('ScriptPath', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('WorkStations', RPC_UNICODE_STRING),('LastLogon', OLD_LARGE_INTEGER),('LastLogoff', OLD_LARGE_INTEGER),('PasswordLastSet', OLD_LARGE_INTEGER),('PasswordCanChange', OLD_LARGE_INTEGER),('PasswordMustChange', OLD_LARGE_INTEGER),('LogonHours', SAMPR_LOGON_HOURS),('BadPasswordCount', UNSIGNED_SHORT),('LogonCount', UNSIGNED_SHORT),('UserAccountControl', UNSIGNED_LONG),
    )
class PSAMPR_USER_LOGON_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_LOGON_INFORMATION),
    )    


class SAMPR_USER_ACCOUNT_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('UserId', UNSIGNED_LONG),('PrimaryGroupId', UNSIGNED_LONG),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('ScriptPath', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('AdminComment', RPC_UNICODE_STRING),('WorkStations', RPC_UNICODE_STRING),('LastLogon', OLD_LARGE_INTEGER),('LastLogoff', OLD_LARGE_INTEGER),('LogonHours', SAMPR_LOGON_HOURS),('BadPasswordCount', UNSIGNED_SHORT),('LogonCount', UNSIGNED_SHORT),('PasswordLastSet', OLD_LARGE_INTEGER),('AccountExpires', OLD_LARGE_INTEGER),('UserAccountControl', UNSIGNED_LONG),
    )
class PSAMPR_USER_ACCOUNT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_ACCOUNT_INFORMATION),
    )    


class SAMPR_USER_A_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserName', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_A_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_A_NAME_INFORMATION),
    )    


class SAMPR_USER_F_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('FullName', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_F_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_F_NAME_INFORMATION),
    )    


class SAMPR_USER_NAME_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_NAME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_NAME_INFORMATION),
    )    


class SAMPR_USER_HOME_INFORMATION(NDRSTRUCT):
    structure = (
        ('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_HOME_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_HOME_INFORMATION),
    )    


class SAMPR_USER_SCRIPT_INFORMATION(NDRSTRUCT):
    structure = (
        ('ScriptPath', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_SCRIPT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_SCRIPT_INFORMATION),
    )    


class SAMPR_USER_PROFILE_INFORMATION(NDRSTRUCT):
    structure = (
        ('ProfilePath', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_PROFILE_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_PROFILE_INFORMATION),
    )    


class SAMPR_USER_ADMIN_COMMENT_INFORMATION(NDRSTRUCT):
    structure = (
        ('AdminComment', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_ADMIN_COMMENT_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_ADMIN_COMMENT_INFORMATION),
    )    


class SAMPR_USER_WORKSTATIONS_INFORMATION(NDRSTRUCT):
    structure = (
        ('WorkStations', RPC_UNICODE_STRING),
    )
class PSAMPR_USER_WORKSTATIONS_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_WORKSTATIONS_INFORMATION),
    )    


class SAMPR_USER_LOGON_HOURS_INFORMATION(NDRSTRUCT):
    structure = (
        ('LogonHours', SAMPR_LOGON_HOURS),
    )
class PSAMPR_USER_LOGON_HOURS_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_LOGON_HOURS_INFORMATION),
    )    


class SAMPR_USER_INTERNAL1_INFORMATION(NDRSTRUCT):
    structure = (
        ('EncryptedNtOwfPassword', ENCRYPTED_NT_OWF_PASSWORD),('EncryptedLmOwfPassword', ENCRYPTED_LM_OWF_PASSWORD),('NtPasswordPresent', UNSIGNED_CHAR),('LmPasswordPresent', UNSIGNED_CHAR),('PasswordExpired', UNSIGNED_CHAR),
    )
class PSAMPR_USER_INTERNAL1_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL1_INFORMATION),
    )    


class SAMPR_USER_INTERNAL4_INFORMATION(NDRSTRUCT):
    structure = (
        ('I1', SAMPR_USER_ALL_INFORMATION),('UserPassword', SAMPR_ENCRYPTED_USER_PASSWORD),
    )
class PSAMPR_USER_INTERNAL4_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL4_INFORMATION),
    )    


class SAMPR_USER_INTERNAL4_INFORMATION_NEW(NDRSTRUCT):
    structure = (
        ('I1', SAMPR_USER_ALL_INFORMATION),('UserPassword', SAMPR_ENCRYPTED_USER_PASSWORD_NEW),
    )
class PSAMPR_USER_INTERNAL4_INFORMATION_NEW(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL4_INFORMATION_NEW),
    )    


class SAMPR_USER_INTERNAL5_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserPassword', SAMPR_ENCRYPTED_USER_PASSWORD),('PasswordExpired', UNSIGNED_CHAR),
    )
class PSAMPR_USER_INTERNAL5_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL5_INFORMATION),
    )    


class SAMPR_USER_INTERNAL5_INFORMATION_NEW(NDRSTRUCT):
    structure = (
        ('UserPassword', SAMPR_ENCRYPTED_USER_PASSWORD_NEW),('PasswordExpired', UNSIGNED_CHAR),
    )
class PSAMPR_USER_INTERNAL5_INFORMATION_NEW(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL5_INFORMATION_NEW),
    )    


class SAMPR_ENCRYPTED_PASSWORD_AES(NDRSTRUCT):
    structure = (
        ('AuthData', UCHAR),('Salt', UCHAR),('cbCipher', ULONG),('Cipher', PUCHAR),('PBKDF2Iterations', ULONGLONG),
    )
class PSAMPR_ENCRYPTED_PASSWORD_AES(NDRPOINTER):
    referent = (
        ('Data', SAMPR_ENCRYPTED_PASSWORD_AES),
    )    


class SAMPR_USER_INTERNAL7_INFORMATION(NDRSTRUCT):
    structure = (
        ('UserPassword', SAMPR_ENCRYPTED_PASSWORD_AES),('PasswordExpired', BOOLEAN),
    )
class PSAMPR_USER_INTERNAL7_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL7_INFORMATION),
    )    


class SAMPR_USER_INTERNAL8_INFORMATION(NDRSTRUCT):
    structure = (
        ('I1', SAMPR_USER_ALL_INFORMATION),('UserPassword', SAMPR_ENCRYPTED_PASSWORD_AES),
    )
class PSAMPR_USER_INTERNAL8_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INTERNAL8_INFORMATION),
    )    


UserGeneralInformation = 1,
UserPreferencesInformation = 2,
UserLogonInformation = 3,
UserLogonHoursInformation = 4,
UserAccountInformation = 5,
UserNameInformation = 6,
UserAccountNameInformation = 7,
UserFullNameInformation = 8,
UserPrimaryGroupInformation = 9,
UserHomeInformation = 10,
UserScriptInformation = 11,
UserProfileInformation = 12,
UserAdminCommentInformation = 13,
UserWorkStationsInformation = 14,
UserControlInformation = 16,
UserExpiresInformation = 17,
UserInternal1Information = 18,
UserParametersInformation = 20,
UserAllInformation = 21,
UserInternal4Information = 23,
UserInternal5Information = 24,
UserInternal4InformationNew = 25,
UserInternal5InformationNew = 26,
UserInternal7Information = 31,
UserInternal8Information = 32
        

class SAMPR_USER_INFO_BUFFER(NDRUNION):
    union = {
        UserGeneralInformation: ('General',SAMPR_USER_GENERAL_INFORMATION),UserPreferencesInformation: ('Preferences',SAMPR_USER_PREFERENCES_INFORMATION),UserLogonInformation: ('Logon',SAMPR_USER_LOGON_INFORMATION),UserLogonHoursInformation: ('LogonHours',SAMPR_USER_LOGON_HOURS_INFORMATION),UserAccountInformation: ('Account',SAMPR_USER_ACCOUNT_INFORMATION),UserNameInformation: ('Name',SAMPR_USER_NAME_INFORMATION),UserAccountNameInformation: ('AccountName',SAMPR_USER_A_NAME_INFORMATION),UserFullNameInformation: ('FullName',SAMPR_USER_F_NAME_INFORMATION),UserPrimaryGroupInformation: ('PrimaryGroup',USER_PRIMARY_GROUP_INFORMATION),UserHomeInformation: ('Home',SAMPR_USER_HOME_INFORMATION),UserScriptInformation: ('Script',SAMPR_USER_SCRIPT_INFORMATION),UserProfileInformation: ('Profile',SAMPR_USER_PROFILE_INFORMATION),UserAdminCommentInformation: ('AdminComment',SAMPR_USER_ADMIN_COMMENT_INFORMATION),UserWorkStationsInformation: ('WorkStations',SAMPR_USER_WORKSTATIONS_INFORMATION),UserControlInformation: ('Control',USER_CONTROL_INFORMATION),UserExpiresInformation: ('Expires',USER_EXPIRES_INFORMATION),UserInternal1Information: ('Internal1',SAMPR_USER_INTERNAL1_INFORMATION),UserParametersInformation: ('Parameters',SAMPR_USER_PARAMETERS_INFORMATION),UserAllInformation: ('All',SAMPR_USER_ALL_INFORMATION),UserInternal4Information: ('Internal4',SAMPR_USER_INTERNAL4_INFORMATION),UserInternal5Information: ('Internal5',SAMPR_USER_INTERNAL5_INFORMATION),UserInternal4InformationNew: ('Internal4New',SAMPR_USER_INTERNAL4_INFORMATION_NEW),UserInternal5InformationNew: ('Internal5New',SAMPR_USER_INTERNAL5_INFORMATION_NEW),UserInternal7Information: ('Internal7',SAMPR_USER_INTERNAL7_INFORMATION),UserInternal8Information: ('Internal8',SAMPR_USER_INTERNAL8_INFORMATION),
    }
        class PSAMPR_USER_INFO_BUFFER(NDRPOINTER):
    referent = (
        ('Data', SAMPR_USER_INFO_BUFFER),
    )    


SamValidateAuthentication = 1,
SamValidatePasswordChange = 1
        

class DATA_SAM_VALIDATE_PASSWORD_HASH(NDRUniConformantArray):
    item = UNSIGNED_CHAR

class PTR_SAM_VALIDATE_PASSWORD_HASH(NDRPOINTER):
    referent = (
        ('Data', DATA_SAM_VALIDATE_PASSWORD_HASH),
    )

class SAM_VALIDATE_PASSWORD_HASH(NDRSTRUCT):
    structure = (
	('Length', UNSIGNED_LONG),	('Hash', PTR_SAM_VALIDATE_PASSWORD_HASH),

    )
        

class SAM_VALIDATE_PERSISTED_FIELDS(NDRSTRUCT):
    structure = (
        ('PresentFields', UNSIGNED_LONG),('PasswordLastSet', LARGE_INTEGER),('BadPasswordTime', LARGE_INTEGER),('LockoutTime', LARGE_INTEGER),('BadPasswordCount', UNSIGNED_LONG),('PasswordHistoryLength', UNSIGNED_LONG),('PasswordHistory', PSAM_VALIDATE_PASSWORD_HASH),
    )
class PSAM_VALIDATE_PERSISTED_FIELDS(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_PERSISTED_FIELDS),
    )    


SamValidateSuccess = 0,
SamValidatePasswordMustChange = 0,
SamValidateAccountLockedOut = 0,
SamValidatePasswordExpired = 0,
SamValidatePasswordIncorrect = 0,
SamValidatePasswordIsInHistory = 0,
SamValidatePasswordTooShort = 0,
SamValidatePasswordTooLong = 0,
SamValidatePasswordNotComplexEnough = 0,
SamValidatePasswordTooRecent = 0
        

class SAM_VALIDATE_STANDARD_OUTPUT_ARG(NDRSTRUCT):
    structure = (
        ('ChangedPersistedFields', SAM_VALIDATE_PERSISTED_FIELDS),('ValidationStatus', SAM_VALIDATE_VALIDATION_STATUS),
    )
class PSAM_VALIDATE_STANDARD_OUTPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_STANDARD_OUTPUT_ARG),
    )    


class SAM_VALIDATE_AUTHENTICATION_INPUT_ARG(NDRSTRUCT):
    structure = (
        ('InputPersistedFields', SAM_VALIDATE_PERSISTED_FIELDS),('PasswordMatched', UNSIGNED_CHAR),
    )
class PSAM_VALIDATE_AUTHENTICATION_INPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_AUTHENTICATION_INPUT_ARG),
    )    


class SAM_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(NDRSTRUCT):
    structure = (
        ('InputPersistedFields', SAM_VALIDATE_PERSISTED_FIELDS),('ClearPassword', RPC_UNICODE_STRING),('UserAccountName', RPC_UNICODE_STRING),('HashedPassword', SAM_VALIDATE_PASSWORD_HASH),('PasswordMatch', UNSIGNED_CHAR),
    )
class PSAM_VALIDATE_PASSWORD_CHANGE_INPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_PASSWORD_CHANGE_INPUT_ARG),
    )    


class SAM_VALIDATE_PASSWORD_RESET_INPUT_ARG(NDRSTRUCT):
    structure = (
        ('InputPersistedFields', SAM_VALIDATE_PERSISTED_FIELDS),('ClearPassword', RPC_UNICODE_STRING),('UserAccountName', RPC_UNICODE_STRING),('HashedPassword', SAM_VALIDATE_PASSWORD_HASH),('PasswordMustChangeAtNextLogon', UNSIGNED_CHAR),('ClearLockout', UNSIGNED_CHAR),
    )
class PSAM_VALIDATE_PASSWORD_RESET_INPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_PASSWORD_RESET_INPUT_ARG),
    )    


class SAM_VALIDATE_INPUT_ARG(NDRUNION):
    union = {
        SamValidateAuthentication: ('ValidateAuthenticationInput',SAM_VALIDATE_AUTHENTICATION_INPUT_ARG),SamValidatePasswordChange: ('ValidatePasswordChangeInput',SAM_VALIDATE_PASSWORD_CHANGE_INPUT_ARG),SamValidatePasswordReset: ('ValidatePasswordResetInput',SAM_VALIDATE_PASSWORD_RESET_INPUT_ARG),
    }
        class PSAM_VALIDATE_INPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_INPUT_ARG),
    )    


class SAM_VALIDATE_OUTPUT_ARG(NDRUNION):
    union = {
        SamValidateAuthentication: ('ValidateAuthenticationOutput',SAM_VALIDATE_STANDARD_OUTPUT_ARG),SamValidatePasswordChange: ('ValidatePasswordChangeOutput',SAM_VALIDATE_STANDARD_OUTPUT_ARG),SamValidatePasswordReset: ('ValidatePasswordResetOutput',SAM_VALIDATE_STANDARD_OUTPUT_ARG),
    }
        class PSAM_VALIDATE_OUTPUT_ARG(NDRPOINTER):
    referent = (
        ('Data', SAM_VALIDATE_OUTPUT_ARG),
    )    


class SamrConnect(NDRCALL):
    opnum = 0
    structure = (
		('ServerName', PSAMPR_SERVER_NAME),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrConnectResponse(NDRCALL):
    structure = (
		('ServerHandle', SAMPR_HANDLE),
    )
        

class SamrCloseHandle(NDRCALL):
    opnum = 1
    structure = (
		('SamHandle', SAMPR_HANDLE),
    )

class SamrCloseHandleResponse(NDRCALL):
    structure = (
		('SamHandle', SAMPR_HANDLE),
    )
        

class SamrSetSecurityObject(NDRCALL):
    opnum = 2
    structure = (
		('ObjectHandle', SAMPR_HANDLE),
		('SecurityInformation', SECURITY_INFORMATION),
		('SecurityDescriptor', PSAMPR_SR_SECURITY_DESCRIPTOR),
    )

class SamrSetSecurityObjectResponse(NDRCALL):
    structure = (

    )
        

class SamrQuerySecurityObject(NDRCALL):
    opnum = 3
    structure = (
		('ObjectHandle', SAMPR_HANDLE),
		('SecurityInformation', SECURITY_INFORMATION),
    )

class SamrQuerySecurityObjectResponse(NDRCALL):
    structure = (
		('SecurityDescriptor', PSAMPR_SR_SECURITY_DESCRIPTOR),
    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class SamrLookupDomainInSamServer(NDRCALL):
    opnum = 5
    structure = (
		('ServerHandle', SAMPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
    )

class SamrLookupDomainInSamServerResponse(NDRCALL):
    structure = (
		('DomainId', PRPC_SID),
    )
        

class SamrEnumerateDomainsInSamServer(NDRCALL):
    opnum = 6
    structure = (
		('ServerHandle', SAMPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class SamrEnumerateDomainsInSamServerResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('Buffer', PSAMPR_ENUMERATION_BUFFER),
		('CountReturned', UNSIGNED_LONG),
    )
        

class SamrOpenDomain(NDRCALL):
    opnum = 7
    structure = (
		('ServerHandle', SAMPR_HANDLE),
		('DesiredAccess', UNSIGNED_LONG),
		('DomainId', PRPC_SID),
    )

class SamrOpenDomainResponse(NDRCALL):
    structure = (
		('DomainHandle', SAMPR_HANDLE),
    )
        

class SamrQueryInformationDomain(NDRCALL):
    opnum = 8
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DomainInformationClass', DOMAIN_INFORMATION_CLASS),
    )

class SamrQueryInformationDomainResponse(NDRCALL):
    structure = (
		('Buffer', PSAMPR_DOMAIN_INFO_BUFFER),
    )
        

class SamrSetInformationDomain(NDRCALL):
    opnum = 9
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DomainInformationClass', DOMAIN_INFORMATION_CLASS),
		('DomainInformation', PSAMPR_DOMAIN_INFO_BUFFER),
    )

class SamrSetInformationDomainResponse(NDRCALL):
    structure = (

    )
        

class SamrCreateGroupInDomain(NDRCALL):
    opnum = 10
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrCreateGroupInDomainResponse(NDRCALL):
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('RelativeId', UNSIGNED_LONG),
    )
        

class SamrEnumerateGroupsInDomain(NDRCALL):
    opnum = 11
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class SamrEnumerateGroupsInDomainResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('Buffer', PSAMPR_ENUMERATION_BUFFER),
		('CountReturned', UNSIGNED_LONG),
    )
        

class SamrCreateUserInDomain(NDRCALL):
    opnum = 12
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrCreateUserInDomainResponse(NDRCALL):
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('RelativeId', UNSIGNED_LONG),
    )
        

class SamrEnumerateUsersInDomain(NDRCALL):
    opnum = 13
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('UserAccountControl', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class SamrEnumerateUsersInDomainResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('Buffer', PSAMPR_ENUMERATION_BUFFER),
		('CountReturned', UNSIGNED_LONG),
    )
        

class SamrCreateAliasInDomain(NDRCALL):
    opnum = 14
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('AccountName', PRPC_UNICODE_STRING),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrCreateAliasInDomainResponse(NDRCALL):
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('RelativeId', UNSIGNED_LONG),
    )
        

class SamrEnumerateAliasesInDomain(NDRCALL):
    opnum = 15
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('EnumerationContext', UNSIGNED_LONG),
		('PreferedMaximumLength', UNSIGNED_LONG),
    )

class SamrEnumerateAliasesInDomainResponse(NDRCALL):
    structure = (
		('EnumerationContext', UNSIGNED_LONG),
		('Buffer', PSAMPR_ENUMERATION_BUFFER),
		('CountReturned', UNSIGNED_LONG),
    )
        

class SamrGetAliasMembership(NDRCALL):
    opnum = 16
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('SidArray', PSAMPR_PSID_ARRAY),
    )

class SamrGetAliasMembershipResponse(NDRCALL):
    structure = (
		('Membership', PSAMPR_ULONG_ARRAY),
    )
        

class SamrLookupNamesInDomain(NDRCALL):
    opnum = 17
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('Count', UNSIGNED_LONG),
		('Names', RPC_UNICODE_STRING),
    )

class SamrLookupNamesInDomainResponse(NDRCALL):
    structure = (
		('RelativeIds', PSAMPR_ULONG_ARRAY),
		('Use', PSAMPR_ULONG_ARRAY),
    )
        

class SamrLookupIdsInDomain(NDRCALL):
    opnum = 18
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('Count', UNSIGNED_LONG),
		('RelativeIds', UNSIGNED_LONG),
    )

class SamrLookupIdsInDomainResponse(NDRCALL):
    structure = (
		('Names', PSAMPR_RETURNED_USTRING_ARRAY),
		('Use', PSAMPR_ULONG_ARRAY),
    )
        

class SamrOpenGroup(NDRCALL):
    opnum = 19
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DesiredAccess', UNSIGNED_LONG),
		('GroupId', UNSIGNED_LONG),
    )

class SamrOpenGroupResponse(NDRCALL):
    structure = (
		('GroupHandle', SAMPR_HANDLE),
    )
        

class SamrQueryInformationGroup(NDRCALL):
    opnum = 20
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('GroupInformationClass', GROUP_INFORMATION_CLASS),
    )

class SamrQueryInformationGroupResponse(NDRCALL):
    structure = (
		('Buffer', PSAMPR_GROUP_INFO_BUFFER),
    )
        

class SamrSetInformationGroup(NDRCALL):
    opnum = 21
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('GroupInformationClass', GROUP_INFORMATION_CLASS),
		('Buffer', PSAMPR_GROUP_INFO_BUFFER),
    )

class SamrSetInformationGroupResponse(NDRCALL):
    structure = (

    )
        

class SamrAddMemberToGroup(NDRCALL):
    opnum = 22
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('MemberId', UNSIGNED_LONG),
		('Attributes', UNSIGNED_LONG),
    )

class SamrAddMemberToGroupResponse(NDRCALL):
    structure = (

    )
        

class SamrDeleteGroup(NDRCALL):
    opnum = 23
    structure = (
		('GroupHandle', SAMPR_HANDLE),
    )

class SamrDeleteGroupResponse(NDRCALL):
    structure = (
		('GroupHandle', SAMPR_HANDLE),
    )
        

class SamrRemoveMemberFromGroup(NDRCALL):
    opnum = 24
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('MemberId', UNSIGNED_LONG),
    )

class SamrRemoveMemberFromGroupResponse(NDRCALL):
    structure = (

    )
        

class SamrGetMembersInGroup(NDRCALL):
    opnum = 25
    structure = (
		('GroupHandle', SAMPR_HANDLE),
    )

class SamrGetMembersInGroupResponse(NDRCALL):
    structure = (
		('Members', PSAMPR_GET_MEMBERS_BUFFER),
    )
        

class SamrSetMemberAttributesOfGroup(NDRCALL):
    opnum = 26
    structure = (
		('GroupHandle', SAMPR_HANDLE),
		('MemberId', UNSIGNED_LONG),
		('Attributes', UNSIGNED_LONG),
    )

class SamrSetMemberAttributesOfGroupResponse(NDRCALL):
    structure = (

    )
        

class SamrOpenAlias(NDRCALL):
    opnum = 27
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DesiredAccess', UNSIGNED_LONG),
		('AliasId', UNSIGNED_LONG),
    )

class SamrOpenAliasResponse(NDRCALL):
    structure = (
		('AliasHandle', SAMPR_HANDLE),
    )
        

class SamrQueryInformationAlias(NDRCALL):
    opnum = 28
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('AliasInformationClass', ALIAS_INFORMATION_CLASS),
    )

class SamrQueryInformationAliasResponse(NDRCALL):
    structure = (
		('Buffer', PSAMPR_ALIAS_INFO_BUFFER),
    )
        

class SamrSetInformationAlias(NDRCALL):
    opnum = 29
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('AliasInformationClass', ALIAS_INFORMATION_CLASS),
		('Buffer', PSAMPR_ALIAS_INFO_BUFFER),
    )

class SamrSetInformationAliasResponse(NDRCALL):
    structure = (

    )
        

class SamrDeleteAlias(NDRCALL):
    opnum = 30
    structure = (
		('AliasHandle', SAMPR_HANDLE),
    )

class SamrDeleteAliasResponse(NDRCALL):
    structure = (
		('AliasHandle', SAMPR_HANDLE),
    )
        

class SamrAddMemberToAlias(NDRCALL):
    opnum = 31
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('MemberId', PRPC_SID),
    )

class SamrAddMemberToAliasResponse(NDRCALL):
    structure = (

    )
        

class SamrRemoveMemberFromAlias(NDRCALL):
    opnum = 32
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('MemberId', PRPC_SID),
    )

class SamrRemoveMemberFromAliasResponse(NDRCALL):
    structure = (

    )
        

class SamrGetMembersInAlias(NDRCALL):
    opnum = 33
    structure = (
		('AliasHandle', SAMPR_HANDLE),
    )

class SamrGetMembersInAliasResponse(NDRCALL):
    structure = (
		('Members', PSAMPR_PSID_ARRAY_OUT),
    )
        

class SamrOpenUser(NDRCALL):
    opnum = 34
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DesiredAccess', UNSIGNED_LONG),
		('UserId', UNSIGNED_LONG),
    )

class SamrOpenUserResponse(NDRCALL):
    structure = (
		('UserHandle', SAMPR_HANDLE),
    )
        

class SamrDeleteUser(NDRCALL):
    opnum = 35
    structure = (
		('UserHandle', SAMPR_HANDLE),
    )

class SamrDeleteUserResponse(NDRCALL):
    structure = (
		('UserHandle', SAMPR_HANDLE),
    )
        

class SamrQueryInformationUser(NDRCALL):
    opnum = 36
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('UserInformationClass', USER_INFORMATION_CLASS),
    )

class SamrQueryInformationUserResponse(NDRCALL):
    structure = (
		('Buffer', PSAMPR_USER_INFO_BUFFER),
    )
        

class SamrSetInformationUser(NDRCALL):
    opnum = 37
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('UserInformationClass', USER_INFORMATION_CLASS),
		('Buffer', PSAMPR_USER_INFO_BUFFER),
    )

class SamrSetInformationUserResponse(NDRCALL):
    structure = (

    )
        

class SamrChangePasswordUser(NDRCALL):
    opnum = 38
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('LmPresent', UNSIGNED_CHAR),
		('OldLmEncryptedWithNewLm', PENCRYPTED_LM_OWF_PASSWORD),
		('NewLmEncryptedWithOldLm', PENCRYPTED_LM_OWF_PASSWORD),
		('NtPresent', UNSIGNED_CHAR),
		('OldNtEncryptedWithNewNt', PENCRYPTED_NT_OWF_PASSWORD),
		('NewNtEncryptedWithOldNt', PENCRYPTED_NT_OWF_PASSWORD),
		('NtCrossEncryptionPresent', UNSIGNED_CHAR),
		('NewNtEncryptedWithNewLm', PENCRYPTED_NT_OWF_PASSWORD),
		('LmCrossEncryptionPresent', UNSIGNED_CHAR),
		('NewLmEncryptedWithNewNt', PENCRYPTED_LM_OWF_PASSWORD),
    )

class SamrChangePasswordUserResponse(NDRCALL):
    structure = (

    )
        

class SamrGetGroupsForUser(NDRCALL):
    opnum = 39
    structure = (
		('UserHandle', SAMPR_HANDLE),
    )

class SamrGetGroupsForUserResponse(NDRCALL):
    structure = (
		('Groups', PSAMPR_GET_GROUPS_BUFFER),
    )
        

class SamrQueryDisplayInformation(NDRCALL):
    opnum = 40
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DisplayInformationClass', DOMAIN_DISPLAY_INFORMATION),
		('Index', UNSIGNED_LONG),
		('EntryCount', UNSIGNED_LONG),
		('PreferredMaximumLength', UNSIGNED_LONG),
    )

class SamrQueryDisplayInformationResponse(NDRCALL):
    structure = (
		('TotalAvailable', UNSIGNED_LONG),
		('TotalReturned', UNSIGNED_LONG),
		('Buffer', PSAMPR_DISPLAY_INFO_BUFFER),
    )
        

class SamrGetDisplayEnumerationIndex(NDRCALL):
    opnum = 41
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DisplayInformationClass', DOMAIN_DISPLAY_INFORMATION),
		('Prefix', PRPC_UNICODE_STRING),
    )

class SamrGetDisplayEnumerationIndexResponse(NDRCALL):
    structure = (
		('Index', UNSIGNED_LONG),
    )
        

class Opnum42NotUsedOnWire(NDRCALL):
    opnum = 42
    structure = (

    )

class Opnum42NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum43NotUsedOnWire(NDRCALL):
    opnum = 43
    structure = (

    )

class Opnum43NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class SamrGetUserDomainPasswordInformation(NDRCALL):
    opnum = 44
    structure = (
		('UserHandle', SAMPR_HANDLE),
    )

class SamrGetUserDomainPasswordInformationResponse(NDRCALL):
    structure = (
		('PasswordInformation', PUSER_DOMAIN_PASSWORD_INFORMATION),
    )
        

class SamrRemoveMemberFromForeignDomain(NDRCALL):
    opnum = 45
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('MemberSid', PRPC_SID),
    )

class SamrRemoveMemberFromForeignDomainResponse(NDRCALL):
    structure = (

    )
        

class SamrQueryInformationDomain2(NDRCALL):
    opnum = 46
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DomainInformationClass', DOMAIN_INFORMATION_CLASS),
    )

class SamrQueryInformationDomain2Response(NDRCALL):
    structure = (
		('Buffer', PSAMPR_DOMAIN_INFO_BUFFER),
    )
        

class SamrQueryInformationUser2(NDRCALL):
    opnum = 47
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('UserInformationClass', USER_INFORMATION_CLASS),
    )

class SamrQueryInformationUser2Response(NDRCALL):
    structure = (
		('Buffer', PSAMPR_USER_INFO_BUFFER),
    )
        

class SamrQueryDisplayInformation2(NDRCALL):
    opnum = 48
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DisplayInformationClass', DOMAIN_DISPLAY_INFORMATION),
		('Index', UNSIGNED_LONG),
		('EntryCount', UNSIGNED_LONG),
		('PreferredMaximumLength', UNSIGNED_LONG),
    )

class SamrQueryDisplayInformation2Response(NDRCALL):
    structure = (
		('TotalAvailable', UNSIGNED_LONG),
		('TotalReturned', UNSIGNED_LONG),
		('Buffer', PSAMPR_DISPLAY_INFO_BUFFER),
    )
        

class SamrGetDisplayEnumerationIndex2(NDRCALL):
    opnum = 49
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DisplayInformationClass', DOMAIN_DISPLAY_INFORMATION),
		('Prefix', PRPC_UNICODE_STRING),
    )

class SamrGetDisplayEnumerationIndex2Response(NDRCALL):
    structure = (
		('Index', UNSIGNED_LONG),
    )
        

class SamrCreateUser2InDomain(NDRCALL):
    opnum = 50
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('Name', PRPC_UNICODE_STRING),
		('AccountType', UNSIGNED_LONG),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrCreateUser2InDomainResponse(NDRCALL):
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('GrantedAccess', UNSIGNED_LONG),
		('RelativeId', UNSIGNED_LONG),
    )
        

class SamrQueryDisplayInformation3(NDRCALL):
    opnum = 51
    structure = (
		('DomainHandle', SAMPR_HANDLE),
		('DisplayInformationClass', DOMAIN_DISPLAY_INFORMATION),
		('Index', UNSIGNED_LONG),
		('EntryCount', UNSIGNED_LONG),
		('PreferredMaximumLength', UNSIGNED_LONG),
    )

class SamrQueryDisplayInformation3Response(NDRCALL):
    structure = (
		('TotalAvailable', UNSIGNED_LONG),
		('TotalReturned', UNSIGNED_LONG),
		('Buffer', PSAMPR_DISPLAY_INFO_BUFFER),
    )
        

class SamrAddMultipleMembersToAlias(NDRCALL):
    opnum = 52
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('MembersBuffer', PSAMPR_PSID_ARRAY),
    )

class SamrAddMultipleMembersToAliasResponse(NDRCALL):
    structure = (

    )
        

class SamrRemoveMultipleMembersFromAlias(NDRCALL):
    opnum = 53
    structure = (
		('AliasHandle', SAMPR_HANDLE),
		('MembersBuffer', PSAMPR_PSID_ARRAY),
    )

class SamrRemoveMultipleMembersFromAliasResponse(NDRCALL):
    structure = (

    )
        

class SamrOemChangePasswordUser2(NDRCALL):
    opnum = 54
    structure = (
		('BindingHandle', HANDLE_T),
		('ServerName', PRPC_STRING),
		('UserName', PRPC_STRING),
		('NewPasswordEncryptedWithOldLm', PSAMPR_ENCRYPTED_USER_PASSWORD),
		('OldLmOwfPasswordEncryptedWithNewLm', PENCRYPTED_LM_OWF_PASSWORD),
    )

class SamrOemChangePasswordUser2Response(NDRCALL):
    structure = (

    )
        

class SamrUnicodeChangePasswordUser2(NDRCALL):
    opnum = 55
    structure = (
		('BindingHandle', HANDLE_T),
		('ServerName', PRPC_UNICODE_STRING),
		('UserName', PRPC_UNICODE_STRING),
		('NewPasswordEncryptedWithOldNt', PSAMPR_ENCRYPTED_USER_PASSWORD),
		('OldNtOwfPasswordEncryptedWithNewNt', PENCRYPTED_NT_OWF_PASSWORD),
		('LmPresent', UNSIGNED_CHAR),
		('NewPasswordEncryptedWithOldLm', PSAMPR_ENCRYPTED_USER_PASSWORD),
		('OldLmOwfPasswordEncryptedWithNewNt', PENCRYPTED_LM_OWF_PASSWORD),
    )

class SamrUnicodeChangePasswordUser2Response(NDRCALL):
    structure = (

    )
        

class SamrGetDomainPasswordInformation(NDRCALL):
    opnum = 56
    structure = (
		('BindingHandle', HANDLE_T),
		('Unused', PRPC_UNICODE_STRING),
    )

class SamrGetDomainPasswordInformationResponse(NDRCALL):
    structure = (
		('PasswordInformation', PUSER_DOMAIN_PASSWORD_INFORMATION),
    )
        

class SamrConnect2(NDRCALL):
    opnum = 57
    structure = (
		('ServerName', PSAMPR_SERVER_NAME),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrConnect2Response(NDRCALL):
    structure = (
		('ServerHandle', SAMPR_HANDLE),
    )
        

class SamrSetInformationUser2(NDRCALL):
    opnum = 58
    structure = (
		('UserHandle', SAMPR_HANDLE),
		('UserInformationClass', USER_INFORMATION_CLASS),
		('Buffer', PSAMPR_USER_INFO_BUFFER),
    )

class SamrSetInformationUser2Response(NDRCALL):
    structure = (

    )
        

class Opnum59NotUsedOnWire(NDRCALL):
    opnum = 59
    structure = (

    )

class Opnum59NotUsedOnWireResponse(NDRCALL):
    structure = (

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
        

class SamrConnect4(NDRCALL):
    opnum = 62
    structure = (
		('ServerName', PSAMPR_SERVER_NAME),
		('ClientRevision', UNSIGNED_LONG),
		('DesiredAccess', UNSIGNED_LONG),
    )

class SamrConnect4Response(NDRCALL):
    structure = (
		('ServerHandle', SAMPR_HANDLE),
    )
        

class Opnum63NotUsedOnWire(NDRCALL):
    opnum = 63
    structure = (

    )

class Opnum63NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class SamrConnect5(NDRCALL):
    opnum = 64
    structure = (
		('ServerName', PSAMPR_SERVER_NAME),
		('DesiredAccess', UNSIGNED_LONG),
		('InVersion', UNSIGNED_LONG),
		('InRevisionInfo', SAMPR_REVISION_INFO),
    )

class SamrConnect5Response(NDRCALL):
    structure = (
		('OutVersion', UNSIGNED_LONG),
		('OutRevisionInfo', SAMPR_REVISION_INFO),
		('ServerHandle', SAMPR_HANDLE),
    )
        

class SamrRidToSid(NDRCALL):
    opnum = 65
    structure = (
		('ObjectHandle', SAMPR_HANDLE),
		('Rid', UNSIGNED_LONG),
    )

class SamrRidToSidResponse(NDRCALL):
    structure = (
		('Sid', PRPC_SID),
    )
        

class SamrSetDSRMPassword(NDRCALL):
    opnum = 66
    structure = (
		('BindingHandle', HANDLE_T),
		('Unused', PRPC_UNICODE_STRING),
		('UserId', UNSIGNED_LONG),
		('EncryptedNtOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
    )

class SamrSetDSRMPasswordResponse(NDRCALL):
    structure = (

    )
        

class SamrValidatePassword(NDRCALL):
    opnum = 67
    structure = (
		('Handle', HANDLE_T),
		('ValidationType', PASSWORD_POLICY_VALIDATION_TYPE),
		('InputArg', PSAM_VALIDATE_INPUT_ARG),
    )

class SamrValidatePasswordResponse(NDRCALL):
    structure = (
		('OutputArg', PSAM_VALIDATE_OUTPUT_ARG),
    )
        

class Opnum68NotUsedOnWire(NDRCALL):
    opnum = 68
    structure = (

    )

class Opnum68NotUsedOnWireResponse(NDRCALL):
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
        

class SamrUnicodeChangePasswordUser4(NDRCALL):
    opnum = 73
    structure = (
		('BindingHandle', HANDLE_T),
		('ServerName', PRPC_UNICODE_STRING),
		('UserName', PRPC_UNICODE_STRING),
		('EncryptedPassword', PSAMPR_ENCRYPTED_PASSWORD_AES),
    )

class SamrUnicodeChangePasswordUser4Response(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (SamrConnect,SamrConnectResponse),
1 : (SamrCloseHandle,SamrCloseHandleResponse),
2 : (SamrSetSecurityObject,SamrSetSecurityObjectResponse),
3 : (SamrQuerySecurityObject,SamrQuerySecurityObjectResponse),
4 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
5 : (SamrLookupDomainInSamServer,SamrLookupDomainInSamServerResponse),
6 : (SamrEnumerateDomainsInSamServer,SamrEnumerateDomainsInSamServerResponse),
7 : (SamrOpenDomain,SamrOpenDomainResponse),
8 : (SamrQueryInformationDomain,SamrQueryInformationDomainResponse),
9 : (SamrSetInformationDomain,SamrSetInformationDomainResponse),
10 : (SamrCreateGroupInDomain,SamrCreateGroupInDomainResponse),
11 : (SamrEnumerateGroupsInDomain,SamrEnumerateGroupsInDomainResponse),
12 : (SamrCreateUserInDomain,SamrCreateUserInDomainResponse),
13 : (SamrEnumerateUsersInDomain,SamrEnumerateUsersInDomainResponse),
14 : (SamrCreateAliasInDomain,SamrCreateAliasInDomainResponse),
15 : (SamrEnumerateAliasesInDomain,SamrEnumerateAliasesInDomainResponse),
16 : (SamrGetAliasMembership,SamrGetAliasMembershipResponse),
17 : (SamrLookupNamesInDomain,SamrLookupNamesInDomainResponse),
18 : (SamrLookupIdsInDomain,SamrLookupIdsInDomainResponse),
19 : (SamrOpenGroup,SamrOpenGroupResponse),
20 : (SamrQueryInformationGroup,SamrQueryInformationGroupResponse),
21 : (SamrSetInformationGroup,SamrSetInformationGroupResponse),
22 : (SamrAddMemberToGroup,SamrAddMemberToGroupResponse),
23 : (SamrDeleteGroup,SamrDeleteGroupResponse),
24 : (SamrRemoveMemberFromGroup,SamrRemoveMemberFromGroupResponse),
25 : (SamrGetMembersInGroup,SamrGetMembersInGroupResponse),
26 : (SamrSetMemberAttributesOfGroup,SamrSetMemberAttributesOfGroupResponse),
27 : (SamrOpenAlias,SamrOpenAliasResponse),
28 : (SamrQueryInformationAlias,SamrQueryInformationAliasResponse),
29 : (SamrSetInformationAlias,SamrSetInformationAliasResponse),
30 : (SamrDeleteAlias,SamrDeleteAliasResponse),
31 : (SamrAddMemberToAlias,SamrAddMemberToAliasResponse),
32 : (SamrRemoveMemberFromAlias,SamrRemoveMemberFromAliasResponse),
33 : (SamrGetMembersInAlias,SamrGetMembersInAliasResponse),
34 : (SamrOpenUser,SamrOpenUserResponse),
35 : (SamrDeleteUser,SamrDeleteUserResponse),
36 : (SamrQueryInformationUser,SamrQueryInformationUserResponse),
37 : (SamrSetInformationUser,SamrSetInformationUserResponse),
38 : (SamrChangePasswordUser,SamrChangePasswordUserResponse),
39 : (SamrGetGroupsForUser,SamrGetGroupsForUserResponse),
40 : (SamrQueryDisplayInformation,SamrQueryDisplayInformationResponse),
41 : (SamrGetDisplayEnumerationIndex,SamrGetDisplayEnumerationIndexResponse),
42 : (Opnum42NotUsedOnWire,Opnum42NotUsedOnWireResponse),
43 : (Opnum43NotUsedOnWire,Opnum43NotUsedOnWireResponse),
44 : (SamrGetUserDomainPasswordInformation,SamrGetUserDomainPasswordInformationResponse),
45 : (SamrRemoveMemberFromForeignDomain,SamrRemoveMemberFromForeignDomainResponse),
46 : (SamrQueryInformationDomain2,SamrQueryInformationDomain2Response),
47 : (SamrQueryInformationUser2,SamrQueryInformationUser2Response),
48 : (SamrQueryDisplayInformation2,SamrQueryDisplayInformation2Response),
49 : (SamrGetDisplayEnumerationIndex2,SamrGetDisplayEnumerationIndex2Response),
50 : (SamrCreateUser2InDomain,SamrCreateUser2InDomainResponse),
51 : (SamrQueryDisplayInformation3,SamrQueryDisplayInformation3Response),
52 : (SamrAddMultipleMembersToAlias,SamrAddMultipleMembersToAliasResponse),
53 : (SamrRemoveMultipleMembersFromAlias,SamrRemoveMultipleMembersFromAliasResponse),
54 : (SamrOemChangePasswordUser2,SamrOemChangePasswordUser2Response),
55 : (SamrUnicodeChangePasswordUser2,SamrUnicodeChangePasswordUser2Response),
56 : (SamrGetDomainPasswordInformation,SamrGetDomainPasswordInformationResponse),
57 : (SamrConnect2,SamrConnect2Response),
58 : (SamrSetInformationUser2,SamrSetInformationUser2Response),
59 : (Opnum59NotUsedOnWire,Opnum59NotUsedOnWireResponse),
60 : (Opnum60NotUsedOnWire,Opnum60NotUsedOnWireResponse),
61 : (Opnum61NotUsedOnWire,Opnum61NotUsedOnWireResponse),
62 : (SamrConnect4,SamrConnect4Response),
63 : (Opnum63NotUsedOnWire,Opnum63NotUsedOnWireResponse),
64 : (SamrConnect5,SamrConnect5Response),
65 : (SamrRidToSid,SamrRidToSidResponse),
66 : (SamrSetDSRMPassword,SamrSetDSRMPasswordResponse),
67 : (SamrValidatePassword,SamrValidatePasswordResponse),
68 : (Opnum68NotUsedOnWire,Opnum68NotUsedOnWireResponse),
69 : (Opnum69NotUsedOnWire,Opnum69NotUsedOnWireResponse),
70 : (Opnum70NotUsedOnWire,Opnum70NotUsedOnWireResponse),
71 : (Opnum71NotUsedOnWire,Opnum71NotUsedOnWireResponse),
72 : (Opnum72NotUsedOnWire,Opnum72NotUsedOnWireResponse),
73 : (SamrUnicodeChangePasswordUser4,SamrUnicodeChangePasswordUser4Response),
}

