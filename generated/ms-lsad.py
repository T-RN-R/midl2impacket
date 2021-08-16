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
DWORD__ENUM = DWORD
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
	align = 1
	structure = (
			(
			'dwLowDateTime',
			DWORD
			),
			(
			'dwHighDateTime',
			DWORD
			)
		)


class PFILETIME(NDRPOINTER):
	referent = (
			(
			'Data',
			FILETIME
			)
		)


class LPFILETIME(NDRPOINTER):
	referent = (
			(
			'Data',
			FILETIME
			)
		)


class GUID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Data1',
			UNSIGNED_LONG
			),
			(
			'Data2',
			UNSIGNED_SHORT
			),
			(
			'Data3',
			UNSIGNED_SHORT
			),
			(
			'Data4',
			BYTE
			)
		)


UUID = GUID
class PGUID(NDRPOINTER):
	referent = (
			(
			'Data',
			GUID
			)
		)


class LARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'QuadPart',
			SIGNED___INT64
			)
		)


class PLARGE_INTEGER(NDRPOINTER):
	referent = (
			(
			'Data',
			LARGE_INTEGER
			)
		)


class EVENT_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Id',
			USHORT
			),
			(
			'Version',
			UCHAR
			),
			(
			'Channel',
			UCHAR
			),
			(
			'Level',
			UCHAR
			),
			(
			'Opcode',
			UCHAR
			),
			(
			'Task',
			USHORT
			),
			(
			'Keyword',
			ULONGLONG
			)
		)


class PEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_DESCRIPTOR
			)
		)


class PCEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_DESCRIPTOR
			)
		)


class S0(NDRSTRUCT):
	align = 1
	structure = (
			(
			'KernelTime',
			ULONG
			),
			(
			'UserTime',
			ULONG
			)
		)


class U0(NDRUNION):
	union = {1 : (
		's0',
		S0
		),2 : (
		'ProcessorTime',
		ULONG64
		)}


class EVENT_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			USHORT
			),
			(
			'HeaderType',
			USHORT
			),
			(
			'Flags',
			USHORT
			),
			(
			'EventProperty',
			USHORT
			),
			(
			'ThreadId',
			ULONG
			),
			(
			'ProcessId',
			ULONG
			),
			(
			'TimeStamp',
			LARGE_INTEGER
			),
			(
			'ProviderId',
			GUID
			),
			(
			'EventDescriptor',
			EVENT_DESCRIPTOR
			),
			(
			'u0',
			U0
			),
			(
			'ActivityId',
			GUID
			)
		)


class PEVENT_HEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			EVENT_HEADER
			)
		)


LCID = DWORD
class LUID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LowPart',
			DWORD
			),
			(
			'HighPart',
			LONG
			)
		)


class PLUID(NDRPOINTER):
	referent = (
			(
			'Data',
			LUID
			)
		)


class MULTI_SZ(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Value',
			WCHAR_T
			),
			(
			'nChar',
			DWORD
			)
		)


class DATA_RPC_UNICODE_STRING(NDRUniConformantArray):
	item = WCHAR


class PTR_RPC_UNICODE_STRING(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_UNICODE_STRING
			)
		)


class RPC_UNICODE_STRING(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_SHORT
			),
			(
			'MaximumLength',
			UNSIGNED_SHORT
			),
			(
			'Buffer',
			PTR_RPC_UNICODE_STRING
			)
		)


class SERVER_INFO_100(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv100_platform_id',
			DWORD
			),
			(
			'sv100_name',
			WCHAR_T
			)
		)


class PSERVER_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_100
			)
		)


class LPSERVER_INFO_100(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_100
			)
		)


class SERVER_INFO_101(NDRSTRUCT):
	align = 1
	structure = (
			(
			'sv101_platform_id',
			DWORD
			),
			(
			'sv101_name',
			WCHAR_T
			),
			(
			'sv101_version_major',
			DWORD
			),
			(
			'sv101_version_minor',
			DWORD
			),
			(
			'sv101_version_type',
			DWORD
			),
			(
			'sv101_comment',
			WCHAR_T
			)
		)


class PSERVER_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_101
			)
		)


class LPSERVER_INFO_101(NDRPOINTER):
	referent = (
			(
			'Data',
			SERVER_INFO_101
			)
		)


class SYSTEMTIME(NDRSTRUCT):
	align = 1
	structure = (
			(
			'wYear',
			WORD
			),
			(
			'wMonth',
			WORD
			),
			(
			'wDayOfWeek',
			WORD
			),
			(
			'wDay',
			WORD
			),
			(
			'wHour',
			WORD
			),
			(
			'wMinute',
			WORD
			),
			(
			'wSecond',
			WORD
			),
			(
			'wMilliseconds',
			WORD
			)
		)


class PSYSTEMTIME(NDRPOINTER):
	referent = (
			(
			'Data',
			SYSTEMTIME
			)
		)


class UINT128(NDRSTRUCT):
	align = 1
	structure = (
			(
			'lower',
			UINT64
			),
			(
			'upper',
			UINT64
			)
		)


class PUINT128(NDRPOINTER):
	referent = (
			(
			'Data',
			UINT128
			)
		)


class ULARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'QuadPart',
			UNSIGNED___INT64
			)
		)


class PULARGE_INTEGER(NDRPOINTER):
	referent = (
			(
			'Data',
			ULARGE_INTEGER
			)
		)


class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Value',
			BYTE
			)
		)


ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK
class OBJECT_TYPE_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			WORD
			),
			(
			'Remaining',
			ACCESS_MASK
			),
			(
			'ObjectType',
			GUID
			)
		)


class POBJECT_TYPE_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			OBJECT_TYPE_LIST
			)
		)


class ACE_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AceType',
			UCHAR
			),
			(
			'AceFlags',
			UCHAR
			),
			(
			'AceSize',
			USHORT
			)
		)


class PACE_HEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			ACE_HEADER
			)
		)


class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Header',
			ACE_HEADER
			),
			(
			'Mask',
			ACCESS_MASK
			),
			(
			'SidStart',
			DWORD
			)
		)


class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
	referent = (
			(
			'Data',
			SYSTEM_MANDATORY_LABEL_ACE
			)
		)


class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Policy',
			DWORD
			)
		)


class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
	referent = (
			(
			'Data',
			TOKEN_MANDATORY_POLICY
			)
		)


class MANDATORY_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AllowedAccess',
			ACCESS_MASK
			),
			(
			'WriteAllowed',
			BOOLEAN
			),
			(
			'ReadAllowed',
			BOOLEAN
			),
			(
			'ExecuteAllowed',
			BOOLEAN
			),
			(
			'MandatoryPolicy',
			TOKEN_MANDATORY_POLICY
			)
		)


class PMANDATORY_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			MANDATORY_INFORMATION
			)
		)


class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			DWORD
			),
			(
			'OctetString',
			BYTE
			)
		)


class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
	referent = (
			(
			'Data',
			CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE
			)
		)


class VALUES(NDRUNION):
	union = {1 : (
		'pInt64',
		PLONG64
		),2 : (
		'pUint64',
		PDWORD64
		),3 : (
		'ppString',
		PWSTR
		),4 : (
		'pOctetString',
		PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE
		)}


class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			DWORD
			),
			(
			'ValueType',
			WORD
			),
			(
			'Reserved',
			WORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'ValueCount',
			DWORD
			),
			(
			'Values',
			VALUES
			)
		)


class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
	referent = (
			(
			'Data',
			CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
			)
		)


SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD
class RPC_SID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Revision',
			UNSIGNED_CHAR
			),
			(
			'SubAuthorityCount',
			UNSIGNED_CHAR
			),
			(
			'IdentifierAuthority',
			RPC_SID_IDENTIFIER_AUTHORITY
			),
			(
			'SubAuthority',
			UNSIGNED_LONG
			)
		)


class PRPC_SID(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_SID
			)
		)


class PSID(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_SID
			)
		)


class ACL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AclRevision',
			UNSIGNED_CHAR
			),
			(
			'Sbz1',
			UNSIGNED_CHAR
			),
			(
			'AclSize',
			UNSIGNED_SHORT
			),
			(
			'AceCount',
			UNSIGNED_SHORT
			),
			(
			'Sbz2',
			UNSIGNED_SHORT
			)
		)


class PACL(NDRPOINTER):
	referent = (
			(
			'Data',
			ACL
			)
		)


class SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Revision',
			UCHAR
			),
			(
			'Sbz1',
			UCHAR
			),
			(
			'Control',
			USHORT
			),
			(
			'Owner',
			PSID
			),
			(
			'Group',
			PSID
			),
			(
			'Sacl',
			PACL
			),
			(
			'Dacl',
			PACL
			)
		)


class PSECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			SECURITY_DESCRIPTOR
			)
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
class DATA_STRING(NDRUniConformantArray):
	item = CHAR


class PTR_STRING(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_STRING
			)
		)


class STRING(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_SHORT
			),
			(
			'MaximumLength',
			UNSIGNED_SHORT
			),
			(
			'Buffer',
			PTR_STRING
			)
		)


class LSAPR_ACL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AclRevision',
			UNSIGNED_CHAR
			),
			(
			'Sbz1',
			UNSIGNED_CHAR
			),
			(
			'AclSize',
			UNSIGNED_SHORT
			),
			(
			'Dummy1',
			UNSIGNED_CHAR
			)
		)


class PLSAPR_ACL(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_ACL
			)
		)


class LSAPR_SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Revision',
			UNSIGNED_CHAR
			),
			(
			'Sbz1',
			UNSIGNED_CHAR
			),
			(
			'Control',
			SECURITY_DESCRIPTOR_CONTROL
			),
			(
			'Owner',
			PRPC_SID
			),
			(
			'Group',
			PRPC_SID
			),
			(
			'Sacl',
			PLSAPR_ACL
			),
			(
			'Dacl',
			PLSAPR_ACL
			)
		)


class PLSAPR_SECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_SECURITY_DESCRIPTOR
			)
		)


SECURITY_IMPERSONATION_LEVEL = DWORD__ENUM
SecurityAnonymous = 0
SecurityIdentification = 1
SecurityImpersonation = 2
SecurityDelegation = 3
class SECURITY_QUALITY_OF_SERVICE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_LONG
			),
			(
			'ImpersonationLevel',
			SECURITY_IMPERSONATION_LEVEL
			),
			(
			'ContextTrackingMode',
			SECURITY_CONTEXT_TRACKING_MODE
			),
			(
			'EffectiveOnly',
			UNSIGNED_CHAR
			)
		)


class PSECURITY_QUALITY_OF_SERVICE(NDRPOINTER):
	referent = (
			(
			'Data',
			SECURITY_QUALITY_OF_SERVICE
			)
		)


class LSAPR_OBJECT_ATTRIBUTES(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_LONG
			),
			(
			'RootDirectory',
			UNSIGNED_CHAR
			),
			(
			'ObjectName',
			PSTRING
			),
			(
			'Attributes',
			UNSIGNED_LONG
			),
			(
			'SecurityDescriptor',
			PLSAPR_SECURITY_DESCRIPTOR
			),
			(
			'SecurityQualityOfService',
			PSECURITY_QUALITY_OF_SERVICE
			)
		)


class PLSAPR_OBJECT_ATTRIBUTES(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_OBJECT_ATTRIBUTES
			)
		)


class LSAPR_TRUST_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'Sid',
			PRPC_SID
			)
		)


class PLSAPR_TRUST_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUST_INFORMATION
			)
		)


POLICY_INFORMATION_CLASS = DWORD__ENUM
PolicyAuditLogInformation = 1
PolicyAuditEventsInformation = 1
PolicyPrimaryDomainInformation = 1
PolicyPdAccountInformation = 1
PolicyAccountDomainInformation = 1
PolicyLsaServerRoleInformation = 1
PolicyReplicaSourceInformation = 1
PolicyInformationNotUsedOnWire = 1
PolicyModificationInformation = 1
PolicyAuditFullSetInformation = 1
PolicyAuditFullQueryInformation = 1
PolicyDnsDomainInformation = 1
PolicyDnsDomainInformationInt = 1
PolicyLocalAccountDomainInformation = 1
PolicyMachineAccountInformation = 1
POLICY_AUDIT_EVENT_TYPE = DWORD__ENUM
AuditCategorySystem = 0
AuditCategoryLogon = 0
AuditCategoryObjectAccess = 0
AuditCategoryPrivilegeUse = 0
AuditCategoryDetailedTracking = 0
AuditCategoryPolicyChange = 0
AuditCategoryAccountManagement = 0
AuditCategoryDirectoryServiceAccess = 0
LSA_UNICODE_STRING = RPC_UNICODE_STRING
PLSA_UNICODE_STRING = RPC_UNICODE_STRING
class POLICY_AUDIT_LOG_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AuditLogPercentFull',
			UNSIGNED_LONG
			),
			(
			'MaximumLogSize',
			UNSIGNED_LONG
			),
			(
			'AuditRetentionPeriod',
			LARGE_INTEGER
			),
			(
			'AuditLogFullShutdownInProgress',
			UNSIGNED_CHAR
			),
			(
			'TimeToShutdown',
			LARGE_INTEGER
			),
			(
			'NextAuditRecordId',
			UNSIGNED_LONG
			)
		)


class PPOLICY_AUDIT_LOG_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_AUDIT_LOG_INFO
			)
		)


POLICY_LSA_SERVER_ROLE = DWORD__ENUM
PolicyServerRoleBackup = 2
class POLICY_LSA_SERVER_ROLE_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LsaServerRole',
			POLICY_LSA_SERVER_ROLE
			)
		)


class PPOLICY_LSA_SERVER_ROLE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_LSA_SERVER_ROLE_INFO
			)
		)


class POLICY_MODIFICATION_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ModifiedId',
			LARGE_INTEGER
			),
			(
			'DatabaseCreationTime',
			LARGE_INTEGER
			)
		)


class PPOLICY_MODIFICATION_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_MODIFICATION_INFO
			)
		)


class POLICY_AUDIT_FULL_SET_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ShutDownOnFull',
			UNSIGNED_CHAR
			)
		)


class PPOLICY_AUDIT_FULL_SET_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_AUDIT_FULL_SET_INFO
			)
		)


class POLICY_AUDIT_FULL_QUERY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ShutDownOnFull',
			UNSIGNED_CHAR
			),
			(
			'LogIsFull',
			UNSIGNED_CHAR
			)
		)


class PPOLICY_AUDIT_FULL_QUERY_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_AUDIT_FULL_QUERY_INFO
			)
		)


POLICY_DOMAIN_INFORMATION_CLASS = DWORD__ENUM
PolicyDomainQualityOfServiceInformation = 1
PolicyDomainEfsInformation = 2
PolicyDomainKerberosTicketInformation = 3
class POLICY_DOMAIN_KERBEROS_TICKET_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AuthenticationOptions',
			UNSIGNED_LONG
			),
			(
			'MaxServiceTicketAge',
			LARGE_INTEGER
			),
			(
			'MaxTicketAge',
			LARGE_INTEGER
			),
			(
			'MaxRenewAge',
			LARGE_INTEGER
			),
			(
			'MaxClockSkew',
			LARGE_INTEGER
			),
			(
			'Reserved',
			LARGE_INTEGER
			)
		)


class PPOLICY_DOMAIN_KERBEROS_TICKET_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_DOMAIN_KERBEROS_TICKET_INFO
			)
		)


class TRUSTED_POSIX_OFFSET_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Offset',
			UNSIGNED_LONG
			)
		)


class PTRUSTED_POSIX_OFFSET_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			TRUSTED_POSIX_OFFSET_INFO
			)
		)


TRUSTED_INFORMATION_CLASS = DWORD__ENUM
TrustedDomainNameInformation = 1
TrustedControllersInformation = 1
TrustedPosixOffsetInformation = 1
TrustedPasswordInformation = 1
TrustedDomainInformationBasic = 1
TrustedDomainInformationEx = 1
TrustedDomainAuthInformation = 1
TrustedDomainFullInformation = 1
TrustedDomainAuthInformationInternal = 1
TrustedDomainFullInformationInternal = 1
TrustedDomainInformationEx2Internal = 1
TrustedDomainFullInformation2Internal = 1
LSA_FOREST_TRUST_RECORD_TYPE = DWORD__ENUM
ForestTrustTopLevelName = 0
ForestTrustTopLevelNameEx = 1
ForestTrustDomainInfo = 2
ForestTrustRecordTypeLast = ForestTrustDomainInfo
class DATA_LSA_FOREST_TRUST_BINARY_DATA(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSA_FOREST_TRUST_BINARY_DATA(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSA_FOREST_TRUST_BINARY_DATA
			)
		)


class LSA_FOREST_TRUST_BINARY_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			PTR_LSA_FOREST_TRUST_BINARY_DATA
			)
		)


class LSA_FOREST_TRUST_DOMAIN_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Sid',
			PRPC_SID
			),
			(
			'DnsName',
			LSA_UNICODE_STRING
			),
			(
			'NetbiosName',
			LSA_UNICODE_STRING
			)
		)


class PLSA_FOREST_TRUST_DOMAIN_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSA_FOREST_TRUST_DOMAIN_INFO
			)
		)


class FORESTTRUSTDATA(NDRUNION):
	union = {ForestTrustTopLevelName : (
		'TopLevelName',
		LSA_UNICODE_STRING
		),ForestTrustDomainInfo : (
		'DomainInfo',
		LSA_FOREST_TRUST_DOMAIN_INFO
		),3 : (
		'Data',
		LSA_FOREST_TRUST_BINARY_DATA
		)}


class LSA_FOREST_TRUST_RECORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			UNSIGNED_LONG
			),
			(
			'ForestTrustType',
			LSA_FOREST_TRUST_RECORD_TYPE
			),
			(
			'Time',
			LARGE_INTEGER
			),
			(
			'ForestTrustData',
			FORESTTRUSTDATA
			)
		)


class PLSA_FOREST_TRUST_RECORD(NDRPOINTER):
	referent = (
			(
			'Data',
			LSA_FOREST_TRUST_RECORD
			)
		)


class DATA_LSA_FOREST_TRUST_INFORMATION(NDRUniConformantArray):
	item = PLSA_FOREST_TRUST_RECORD


class PTR_LSA_FOREST_TRUST_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSA_FOREST_TRUST_INFORMATION
			)
		)


class LSA_FOREST_TRUST_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'RecordCount',
			UNSIGNED_LONG
			),
			(
			'Entries',
			PTR_LSA_FOREST_TRUST_INFORMATION
			)
		)


LSA_FOREST_TRUST_COLLISION_RECORD_TYPE = DWORD__ENUM
CollisionTdo = 0
CollisionXref = 0
class LSA_FOREST_TRUST_COLLISION_RECORD(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Index',
			UNSIGNED_LONG
			),
			(
			'Type',
			LSA_FOREST_TRUST_COLLISION_RECORD_TYPE
			),
			(
			'Flags',
			UNSIGNED_LONG
			),
			(
			'Name',
			LSA_UNICODE_STRING
			)
		)


class PLSA_FOREST_TRUST_COLLISION_RECORD(NDRPOINTER):
	referent = (
			(
			'Data',
			LSA_FOREST_TRUST_COLLISION_RECORD
			)
		)


class DATA_LSA_FOREST_TRUST_COLLISION_INFORMATION(NDRUniConformantArray):
	item = PLSA_FOREST_TRUST_COLLISION_RECORD


class PTR_LSA_FOREST_TRUST_COLLISION_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSA_FOREST_TRUST_COLLISION_INFORMATION
			)
		)


class LSA_FOREST_TRUST_COLLISION_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'RecordCount',
			UNSIGNED_LONG
			),
			(
			'Entries',
			PTR_LSA_FOREST_TRUST_COLLISION_INFORMATION
			)
		)


PLSAPR_HANDLE = LSAPR_HANDLE
class LSAPR_ACCOUNT_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Sid',
			PRPC_SID
			)
		)


class PLSAPR_ACCOUNT_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_ACCOUNT_INFORMATION
			)
		)


class LSAPR_ACCOUNT_ENUM_BUFFER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Information',
			PLSAPR_ACCOUNT_INFORMATION
			)
		)


class PLSAPR_ACCOUNT_ENUM_BUFFER(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_ACCOUNT_ENUM_BUFFER
			)
		)


class DATA_LSAPR_SR_SECURITY_DESCRIPTOR(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_SR_SECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_SR_SECURITY_DESCRIPTOR
			)
		)


class LSAPR_SR_SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_LONG
			),
			(
			'SecurityDescriptor',
			PTR_LSAPR_SR_SECURITY_DESCRIPTOR
			)
		)


class LSAPR_LUID_AND_ATTRIBUTES(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Luid',
			LUID
			),
			(
			'Attributes',
			UNSIGNED_LONG
			)
		)


class PLSAPR_LUID_AND_ATTRIBUTES(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_LUID_AND_ATTRIBUTES
			)
		)


class LSAPR_PRIVILEGE_SET(NDRSTRUCT):
	align = 1
	structure = (
			(
			'PrivilegeCount',
			UNSIGNED_LONG
			),
			(
			'Control',
			UNSIGNED_LONG
			),
			(
			'Privilege',
			LSAPR_LUID_AND_ATTRIBUTES
			)
		)


class PLSAPR_PRIVILEGE_SET(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_PRIVILEGE_SET
			)
		)


class LSAPR_POLICY_PRIVILEGE_DEF(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'LocalValue',
			LUID
			)
		)


class PLSAPR_POLICY_PRIVILEGE_DEF(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_PRIVILEGE_DEF
			)
		)


class LSAPR_PRIVILEGE_ENUM_BUFFER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Entries',
			UNSIGNED_LONG
			),
			(
			'Privileges',
			PLSAPR_POLICY_PRIVILEGE_DEF
			)
		)


class PLSAPR_PRIVILEGE_ENUM_BUFFER(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_PRIVILEGE_ENUM_BUFFER
			)
		)


class DATA_LSAPR_CR_CIPHER_VALUE(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_CR_CIPHER_VALUE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_CR_CIPHER_VALUE
			)
		)


class LSAPR_CR_CIPHER_VALUE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_LONG
			),
			(
			'MaximumLength',
			UNSIGNED_LONG
			),
			(
			'Buffer',
			PTR_LSAPR_CR_CIPHER_VALUE
			)
		)


class LSAPR_TRUSTED_ENUM_BUFFER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'Information',
			PLSAPR_TRUST_INFORMATION
			)
		)


class PLSAPR_TRUSTED_ENUM_BUFFER(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_ENUM_BUFFER
			)
		)


class LSAPR_POLICY_ACCOUNT_DOM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'DomainName',
			RPC_UNICODE_STRING
			),
			(
			'DomainSid',
			PRPC_SID
			)
		)


class PLSAPR_POLICY_ACCOUNT_DOM_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_ACCOUNT_DOM_INFO
			)
		)


class LSAPR_POLICY_PRIMARY_DOM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'Sid',
			PRPC_SID
			)
		)


class PLSAPR_POLICY_PRIMARY_DOM_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_PRIMARY_DOM_INFO
			)
		)


class LSAPR_POLICY_DNS_DOMAIN_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'DnsDomainName',
			RPC_UNICODE_STRING
			),
			(
			'DnsForestName',
			RPC_UNICODE_STRING
			),
			(
			'DomainGuid',
			GUID
			),
			(
			'Sid',
			PRPC_SID
			)
		)


class PLSAPR_POLICY_DNS_DOMAIN_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_DNS_DOMAIN_INFO
			)
		)


class LSAPR_POLICY_PD_ACCOUNT_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			)
		)


class PLSAPR_POLICY_PD_ACCOUNT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_PD_ACCOUNT_INFO
			)
		)


class LSAPR_POLICY_REPLICA_SRCE_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ReplicaSource',
			RPC_UNICODE_STRING
			),
			(
			'ReplicaAccountName',
			RPC_UNICODE_STRING
			)
		)


class PLSAPR_POLICY_REPLICA_SRCE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_REPLICA_SRCE_INFO
			)
		)


class DATA_LSAPR_POLICY_AUDIT_EVENTS_INFO(NDRUniConformantArray):
	item = UNSIGNED_LONG


class PTR_LSAPR_POLICY_AUDIT_EVENTS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_POLICY_AUDIT_EVENTS_INFO
			)
		)


class LSAPR_POLICY_AUDIT_EVENTS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AuditingMode',
			UNSIGNED_CHAR
			),
			(
			'EventAuditingOptions',
			PTR_LSAPR_POLICY_AUDIT_EVENTS_INFO
			),
			(
			'MaximumAuditEventCount',
			UNSIGNED_LONG
			)
		)


class LSAPR_POLICY_MACHINE_ACCT_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Rid',
			UNSIGNED_LONG
			),
			(
			'Sid',
			PRPC_SID
			)
		)


class PLSAPR_POLICY_MACHINE_ACCT_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_MACHINE_ACCT_INFO
			)
		)


class LSAPR_POLICY_INFORMATION(NDRUNION):
	union = {PolicyAuditLogInformation : (
		'PolicyAuditLogInfo',
		POLICY_AUDIT_LOG_INFO
		),PolicyAuditEventsInformation : (
		'PolicyAuditEventsInfo',
		LSAPR_POLICY_AUDIT_EVENTS_INFO
		),PolicyPrimaryDomainInformation : (
		'PolicyPrimaryDomainInfo',
		LSAPR_POLICY_PRIMARY_DOM_INFO
		),PolicyAccountDomainInformation : (
		'PolicyAccountDomainInfo',
		LSAPR_POLICY_ACCOUNT_DOM_INFO
		),PolicyPdAccountInformation : (
		'PolicyPdAccountInfo',
		LSAPR_POLICY_PD_ACCOUNT_INFO
		),PolicyLsaServerRoleInformation : (
		'PolicyServerRoleInfo',
		POLICY_LSA_SERVER_ROLE_INFO
		),PolicyReplicaSourceInformation : (
		'PolicyReplicaSourceInfo',
		LSAPR_POLICY_REPLICA_SRCE_INFO
		),PolicyModificationInformation : (
		'PolicyModificationInfo',
		POLICY_MODIFICATION_INFO
		),PolicyAuditFullSetInformation : (
		'PolicyAuditFullSetInfo',
		POLICY_AUDIT_FULL_SET_INFO
		),PolicyAuditFullQueryInformation : (
		'PolicyAuditFullQueryInfo',
		POLICY_AUDIT_FULL_QUERY_INFO
		),PolicyDnsDomainInformation : (
		'PolicyDnsDomainInfo',
		LSAPR_POLICY_DNS_DOMAIN_INFO
		),PolicyDnsDomainInformationInt : (
		'PolicyDnsDomainInfoInt',
		LSAPR_POLICY_DNS_DOMAIN_INFO
		),PolicyLocalAccountDomainInformation : (
		'PolicyLocalAccountDomainInfo',
		LSAPR_POLICY_ACCOUNT_DOM_INFO
		),PolicyMachineAccountInformation : (
		'PolicyMachineAccountInfo',
		LSAPR_POLICY_MACHINE_ACCT_INFO
		)}


class PLSAPR_POLICY_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_INFORMATION
			)
		)


class POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'QualityOfService',
			UNSIGNED_LONG
			)
		)


class PPOLICY_DOMAIN_QUALITY_OF_SERVICE_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO
			)
		)


class DATA_LSAPR_POLICY_DOMAIN_EFS_INFO(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_POLICY_DOMAIN_EFS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_POLICY_DOMAIN_EFS_INFO
			)
		)


class LSAPR_POLICY_DOMAIN_EFS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'InfoLength',
			UNSIGNED_LONG
			),
			(
			'EfsBlob',
			PTR_LSAPR_POLICY_DOMAIN_EFS_INFO
			)
		)


class LSAPR_POLICY_DOMAIN_INFORMATION(NDRUNION):
	union = {PolicyDomainQualityOfServiceInformation : (
		'PolicyDomainQualityOfServiceInfo',
		POLICY_DOMAIN_QUALITY_OF_SERVICE_INFO
		),PolicyDomainEfsInformation : (
		'PolicyDomainEfsInfo',
		LSAPR_POLICY_DOMAIN_EFS_INFO
		),PolicyDomainKerberosTicketInformation : (
		'PolicyDomainKerbTicketInfo',
		POLICY_DOMAIN_KERBEROS_TICKET_INFO
		)}


class PLSAPR_POLICY_DOMAIN_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_POLICY_DOMAIN_INFORMATION
			)
		)


class LSAPR_TRUSTED_DOMAIN_NAME_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			)
		)


class PLSAPR_TRUSTED_DOMAIN_NAME_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_NAME_INFO
			)
		)


class LSAPR_TRUSTED_CONTROLLERS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Entries',
			UNSIGNED_LONG
			),
			(
			'Names',
			PRPC_UNICODE_STRING
			)
		)


class PLSAPR_TRUSTED_CONTROLLERS_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_CONTROLLERS_INFO
			)
		)


class LSAPR_TRUSTED_PASSWORD_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Password',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'OldPassword',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class PLSAPR_TRUSTED_PASSWORD_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_PASSWORD_INFO
			)
		)


class LSAPR_TRUSTED_DOMAIN_INFORMATION_EX(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'FlatName',
			RPC_UNICODE_STRING
			),
			(
			'Sid',
			PRPC_SID
			),
			(
			'TrustDirection',
			UNSIGNED_LONG
			),
			(
			'TrustType',
			UNSIGNED_LONG
			),
			(
			'TrustAttributes',
			UNSIGNED_LONG
			)
		)


class PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			)
		)


class DATA_LSAPR_AUTH_INFORMATION(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_AUTH_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_AUTH_INFORMATION
			)
		)


class LSAPR_AUTH_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LastUpdateTime',
			LARGE_INTEGER
			),
			(
			'AuthType',
			UNSIGNED_LONG
			),
			(
			'AuthInfoLength',
			UNSIGNED_LONG
			),
			(
			'AuthInfo',
			PTR_LSAPR_AUTH_INFORMATION
			)
		)


class LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'IncomingAuthInfos',
			UNSIGNED_LONG
			),
			(
			'IncomingAuthenticationInformation',
			PLSAPR_AUTH_INFORMATION
			),
			(
			'IncomingPreviousAuthenticationInformation',
			PLSAPR_AUTH_INFORMATION
			),
			(
			'OutgoingAuthInfos',
			UNSIGNED_LONG
			),
			(
			'OutgoingAuthenticationInformation',
			PLSAPR_AUTH_INFORMATION
			),
			(
			'OutgoingPreviousAuthenticationInformation',
			PLSAPR_AUTH_INFORMATION
			)
		)


class PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
			)
		)


class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Information',
			LSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'PosixOffset',
			TRUSTED_POSIX_OFFSET_INFO
			),
			(
			'AuthInformation',
			LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
			)
		)


class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION
			)
		)


LSAPR_TRUSTED_DOMAIN_INFORMATION_BASIC = LSAPR_TRUST_INFORMATION
class DATA_LSAPR_TRUSTED_DOMAIN_AUTH_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_TRUSTED_DOMAIN_AUTH_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_TRUSTED_DOMAIN_AUTH_BLOB
			)
		)


class LSAPR_TRUSTED_DOMAIN_AUTH_BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AuthSize',
			UNSIGNED_LONG
			),
			(
			'AuthBlob',
			PTR_LSAPR_TRUSTED_DOMAIN_AUTH_BLOB
			)
		)


class LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'AuthBlob',
			LSAPR_TRUSTED_DOMAIN_AUTH_BLOB
			)
		)


class PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL
			)
		)


class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Information',
			LSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'PosixOffset',
			TRUSTED_POSIX_OFFSET_INFO
			),
			(
			'AuthInformation',
			LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL
			)
		)


class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL
			)
		)


class DATA_LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2
			)
		)


class LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Name',
			RPC_UNICODE_STRING
			),
			(
			'FlatName',
			RPC_UNICODE_STRING
			),
			(
			'Sid',
			PRPC_SID
			),
			(
			'TrustDirection',
			UNSIGNED_LONG
			),
			(
			'TrustType',
			UNSIGNED_LONG
			),
			(
			'TrustAttributes',
			UNSIGNED_LONG
			),
			(
			'ForestTrustLength',
			UNSIGNED_LONG
			),
			(
			'ForestTrustInfo',
			PTR_LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2
			)
		)


class LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Information',
			LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2
			),
			(
			'PosixOffset',
			TRUSTED_POSIX_OFFSET_INFO
			),
			(
			'AuthInformation',
			LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
			)
		)


class PLSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2
			)
		)


class TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES(NDRSTRUCT):
	align = 1
	structure = (
			(
			'SupportedEncryptionTypes',
			UNSIGNED_LONG
			)
		)


class PTRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES(NDRPOINTER):
	referent = (
			(
			'Data',
			TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES
			)
		)


class LSAPR_TRUSTED_DOMAIN_INFO(NDRUNION):
	union = {TrustedDomainNameInformation : (
		'TrustedDomainNameInfo',
		LSAPR_TRUSTED_DOMAIN_NAME_INFO
		),TrustedControllersInformation : (
		'TrustedControllersInfo',
		LSAPR_TRUSTED_CONTROLLERS_INFO
		),TrustedPosixOffsetInformation : (
		'TrustedPosixOffsetInfo',
		TRUSTED_POSIX_OFFSET_INFO
		),TrustedPasswordInformation : (
		'TrustedPasswordInfo',
		LSAPR_TRUSTED_PASSWORD_INFO
		),TrustedDomainInformationBasic : (
		'TrustedDomainInfoBasic',
		LSAPR_TRUSTED_DOMAIN_INFORMATION_BASIC
		),TrustedDomainInformationEx : (
		'TrustedDomainInfoEx',
		LSAPR_TRUSTED_DOMAIN_INFORMATION_EX
		),TrustedDomainAuthInformation : (
		'TrustedAuthInfo',
		LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
		),TrustedDomainFullInformation : (
		'TrustedFullInfo',
		LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION
		),TrustedDomainAuthInformationInternal : (
		'TrustedAuthInfoInternal',
		LSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL
		),TrustedDomainFullInformationInternal : (
		'TrustedFullInfoInternal',
		LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION_INTERNAL
		),TrustedDomainInformationEx2Internal : (
		'TrustedDomainInfoEx2',
		LSAPR_TRUSTED_DOMAIN_INFORMATION_EX2
		),TrustedDomainFullInformation2Internal : (
		'TrustedFullInfo2',
		LSAPR_TRUSTED_DOMAIN_FULL_INFORMATION2
		),TrustedDomainSupportedEncryptionTypes : (
		'TrustedDomainSETs',
		TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES
		)}


class PLSAPR_TRUSTED_DOMAIN_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LSAPR_USER_RIGHT_SET(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Entries',
			UNSIGNED_LONG
			),
			(
			'UserRights',
			PRPC_UNICODE_STRING
			)
		)


class PLSAPR_USER_RIGHT_SET(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_USER_RIGHT_SET
			)
		)


class LSAPR_TRUSTED_ENUM_BUFFER_EX(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EntriesRead',
			UNSIGNED_LONG
			),
			(
			'EnumerationBuffer',
			PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			)
		)


class PLSAPR_TRUSTED_ENUM_BUFFER_EX(NDRPOINTER):
	referent = (
			(
			'Data',
			LSAPR_TRUSTED_ENUM_BUFFER_EX
			)
		)


class LsarClose(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			)
		)


class LsarCloseResponse(NDRCALL):
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			)
		)


class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (

		)


class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarEnumeratePrivileges(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarEnumeratePrivilegesResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarQuerySecurityObject(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			)
		)


class LsarQuerySecurityObjectResponse(NDRCALL):
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			)
		)


class LsarSetSecurityObject(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			),
			(
			'SecurityDescriptor',
			PLSAPR_SR_SECURITY_DESCRIPTOR
			)
		)


class LsarSetSecurityObjectResponse(NDRCALL):
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			),
			(
			'SecurityInformation',
			SECURITY_INFORMATION
			),
			(
			'SecurityDescriptor',
			PLSAPR_SR_SECURITY_DESCRIPTOR
			)
		)


class Opnum5NotUsedOnWire(NDRCALL):
	OPNUM = 5
	structure = (

		)


class Opnum5NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarOpenPolicy(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'SystemName',
			WCHAR_T
			),
			(
			'ObjectAttributes',
			PLSAPR_OBJECT_ATTRIBUTES
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenPolicyResponse(NDRCALL):
	structure = (
			(
			'SystemName',
			WCHAR_T
			),
			(
			'ObjectAttributes',
			PLSAPR_OBJECT_ATTRIBUTES
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarQueryInformationPolicy(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			)
		)


class LsarQueryInformationPolicyResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			)
		)


class LsarSetInformationPolicy(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			),
			(
			'PolicyInformation',
			PLSAPR_POLICY_INFORMATION
			)
		)


class LsarSetInformationPolicyResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			),
			(
			'PolicyInformation',
			PLSAPR_POLICY_INFORMATION
			)
		)


class Opnum9NotUsedOnWire(NDRCALL):
	OPNUM = 9
	structure = (

		)


class Opnum9NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarCreateAccount(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarCreateAccountResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarEnumerateAccounts(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarEnumerateAccountsResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarCreateTrustedDomain(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUST_INFORMATION
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarCreateTrustedDomainResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUST_INFORMATION
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarEnumerateTrustedDomains(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarEnumerateTrustedDomainsResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class Lsar_LSA_TM_14(NDRCALL):
	OPNUM = 14
	structure = (

		)


class Lsar_LSA_TM_14Response(NDRCALL):
	structure = (

		)


class Lsar_LSA_TM_15(NDRCALL):
	OPNUM = 15
	structure = (

		)


class Lsar_LSA_TM_15Response(NDRCALL):
	structure = (

		)


class LsarCreateSecret(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'SecretName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarCreateSecretResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'SecretName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenAccount(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenAccountResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarEnumeratePrivilegesAccount(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			)
		)


class LsarEnumeratePrivilegesAccountResponse(NDRCALL):
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			)
		)


class LsarAddPrivilegesToAccount(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'Privileges',
			PLSAPR_PRIVILEGE_SET
			)
		)


class LsarAddPrivilegesToAccountResponse(NDRCALL):
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'Privileges',
			PLSAPR_PRIVILEGE_SET
			)
		)


class LsarRemovePrivilegesFromAccount(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'AllPrivileges',
			UNSIGNED_CHAR
			),
			(
			'Privileges',
			PLSAPR_PRIVILEGE_SET
			)
		)


class LsarRemovePrivilegesFromAccountResponse(NDRCALL):
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'AllPrivileges',
			UNSIGNED_CHAR
			),
			(
			'Privileges',
			PLSAPR_PRIVILEGE_SET
			)
		)


class Opnum21NotUsedOnWire(NDRCALL):
	OPNUM = 21
	structure = (

		)


class Opnum21NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum22NotUsedOnWire(NDRCALL):
	OPNUM = 22
	structure = (

		)


class Opnum22NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarGetSystemAccessAccount(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			)
		)


class LsarGetSystemAccessAccountResponse(NDRCALL):
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			)
		)


class LsarSetSystemAccessAccount(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'SystemAccess',
			UNSIGNED_LONG
			)
		)


class LsarSetSystemAccessAccountResponse(NDRCALL):
	structure = (
			(
			'AccountHandle',
			LSAPR_HANDLE
			),
			(
			'SystemAccess',
			UNSIGNED_LONG
			)
		)


class LsarOpenTrustedDomain(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenTrustedDomainResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarQueryInfoTrustedDomain(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'TrustedDomainHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarQueryInfoTrustedDomainResponse(NDRCALL):
	structure = (
			(
			'TrustedDomainHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarSetInformationTrustedDomain(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'TrustedDomainHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarSetInformationTrustedDomainResponse(NDRCALL):
	structure = (
			(
			'TrustedDomainHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarOpenSecret(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'SecretName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenSecretResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'SecretName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarSetSecret(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'SecretHandle',
			LSAPR_HANDLE
			),
			(
			'EncryptedCurrentValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'EncryptedOldValue',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarSetSecretResponse(NDRCALL):
	structure = (
			(
			'SecretHandle',
			LSAPR_HANDLE
			),
			(
			'EncryptedCurrentValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'EncryptedOldValue',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarQuerySecret(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'SecretHandle',
			LSAPR_HANDLE
			),
			(
			'EncryptedCurrentValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'CurrentValueSetTime',
			PLARGE_INTEGER
			),
			(
			'EncryptedOldValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'OldValueSetTime',
			PLARGE_INTEGER
			)
		)


class LsarQuerySecretResponse(NDRCALL):
	structure = (
			(
			'SecretHandle',
			LSAPR_HANDLE
			),
			(
			'EncryptedCurrentValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'CurrentValueSetTime',
			PLARGE_INTEGER
			),
			(
			'EncryptedOldValue',
			PLSAPR_CR_CIPHER_VALUE
			),
			(
			'OldValueSetTime',
			PLARGE_INTEGER
			)
		)


class LsarLookupPrivilegeValue(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Name',
			PRPC_UNICODE_STRING
			)
		)


class LsarLookupPrivilegeValueResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Name',
			PRPC_UNICODE_STRING
			)
		)


class LsarLookupPrivilegeName(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Value',
			PLUID
			)
		)


class LsarLookupPrivilegeNameResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Value',
			PLUID
			)
		)


class LsarLookupPrivilegeDisplayName(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Name',
			PRPC_UNICODE_STRING
			),
			(
			'ClientLanguage',
			SHORT
			),
			(
			'ClientSystemDefaultLanguage',
			SHORT
			)
		)


class LsarLookupPrivilegeDisplayNameResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'Name',
			PRPC_UNICODE_STRING
			),
			(
			'ClientLanguage',
			SHORT
			),
			(
			'ClientSystemDefaultLanguage',
			SHORT
			)
		)


class LsarDeleteObject(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			)
		)


class LsarDeleteObjectResponse(NDRCALL):
	structure = (
			(
			'ObjectHandle',
			LSAPR_HANDLE
			)
		)


class LsarEnumerateAccountsWithUserRight(NDRCALL):
	OPNUM = 35
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'UserRight',
			PRPC_UNICODE_STRING
			)
		)


class LsarEnumerateAccountsWithUserRightResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'UserRight',
			PRPC_UNICODE_STRING
			)
		)


class LsarEnumerateAccountRights(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			)
		)


class LsarEnumerateAccountRightsResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			)
		)


class LsarAddAccountRights(NDRCALL):
	OPNUM = 37
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'UserRights',
			PLSAPR_USER_RIGHT_SET
			)
		)


class LsarAddAccountRightsResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'UserRights',
			PLSAPR_USER_RIGHT_SET
			)
		)


class LsarRemoveAccountRights(NDRCALL):
	OPNUM = 38
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'AllRights',
			UNSIGNED_CHAR
			),
			(
			'UserRights',
			PLSAPR_USER_RIGHT_SET
			)
		)


class LsarRemoveAccountRightsResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'AccountSid',
			PRPC_SID
			),
			(
			'AllRights',
			UNSIGNED_CHAR
			),
			(
			'UserRights',
			PLSAPR_USER_RIGHT_SET
			)
		)


class LsarQueryTrustedDomainInfo(NDRCALL):
	OPNUM = 39
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarQueryTrustedDomainInfoResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarSetTrustedDomainInfo(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarSetTrustedDomainInfoResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarDeleteTrustedDomain(NDRCALL):
	OPNUM = 41
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			)
		)


class LsarDeleteTrustedDomainResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainSid',
			PRPC_SID
			)
		)


class LsarStorePrivateData(NDRCALL):
	OPNUM = 42
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'KeyName',
			PRPC_UNICODE_STRING
			),
			(
			'EncryptedData',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarStorePrivateDataResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'KeyName',
			PRPC_UNICODE_STRING
			),
			(
			'EncryptedData',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarRetrievePrivateData(NDRCALL):
	OPNUM = 43
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'KeyName',
			PRPC_UNICODE_STRING
			),
			(
			'EncryptedData',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarRetrievePrivateDataResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'KeyName',
			PRPC_UNICODE_STRING
			),
			(
			'EncryptedData',
			PLSAPR_CR_CIPHER_VALUE
			)
		)


class LsarOpenPolicy2(NDRCALL):
	OPNUM = 44
	structure = (
			(
			'SystemName',
			WCHAR_T
			),
			(
			'ObjectAttributes',
			PLSAPR_OBJECT_ATTRIBUTES
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenPolicy2Response(NDRCALL):
	structure = (
			(
			'SystemName',
			WCHAR_T
			),
			(
			'ObjectAttributes',
			PLSAPR_OBJECT_ATTRIBUTES
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class Lsar_LSA_TM_45(NDRCALL):
	OPNUM = 45
	structure = (

		)


class Lsar_LSA_TM_45Response(NDRCALL):
	structure = (

		)


class LsarQueryInformationPolicy2(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			)
		)


class LsarQueryInformationPolicy2Response(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			)
		)


class LsarSetInformationPolicy2(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			),
			(
			'PolicyInformation',
			PLSAPR_POLICY_INFORMATION
			)
		)


class LsarSetInformationPolicy2Response(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_INFORMATION_CLASS
			),
			(
			'PolicyInformation',
			PLSAPR_POLICY_INFORMATION
			)
		)


class LsarQueryTrustedDomainInfoByName(NDRCALL):
	OPNUM = 48
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarQueryTrustedDomainInfoByNameResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			)
		)


class LsarSetTrustedDomainInfoByName(NDRCALL):
	OPNUM = 49
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarSetTrustedDomainInfoByNameResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'InformationClass',
			TRUSTED_INFORMATION_CLASS
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFO
			)
		)


class LsarEnumerateTrustedDomainsEx(NDRCALL):
	OPNUM = 50
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarEnumerateTrustedDomainsExResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'EnumerationContext',
			UNSIGNED_LONG
			),
			(
			'PreferedMaximumLength',
			UNSIGNED_LONG
			)
		)


class LsarCreateTrustedDomainEx(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'AuthenticationInformation',
			PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarCreateTrustedDomainExResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'AuthenticationInformation',
			PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class Opnum52NotUsedOnWire(NDRCALL):
	OPNUM = 52
	structure = (

		)


class Opnum52NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarQueryDomainInformationPolicy(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_DOMAIN_INFORMATION_CLASS
			)
		)


class LsarQueryDomainInformationPolicyResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_DOMAIN_INFORMATION_CLASS
			)
		)


class LsarSetDomainInformationPolicy(NDRCALL):
	OPNUM = 54
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_DOMAIN_INFORMATION_CLASS
			),
			(
			'PolicyDomainInformation',
			PLSAPR_POLICY_DOMAIN_INFORMATION
			)
		)


class LsarSetDomainInformationPolicyResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'InformationClass',
			POLICY_DOMAIN_INFORMATION_CLASS
			),
			(
			'PolicyDomainInformation',
			PLSAPR_POLICY_DOMAIN_INFORMATION
			)
		)


class LsarOpenTrustedDomainByName(NDRCALL):
	OPNUM = 55
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarOpenTrustedDomainByNameResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PRPC_UNICODE_STRING
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class Opnum56NotUsedOnWire(NDRCALL):
	OPNUM = 56
	structure = (

		)


class Opnum56NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Lsar_LSA_TM_57(NDRCALL):
	OPNUM = 57
	structure = (

		)


class Lsar_LSA_TM_57Response(NDRCALL):
	structure = (

		)


class Lsar_LSA_TM_58(NDRCALL):
	OPNUM = 58
	structure = (

		)


class Lsar_LSA_TM_58Response(NDRCALL):
	structure = (

		)


class LsarCreateTrustedDomainEx2(NDRCALL):
	OPNUM = 59
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'AuthenticationInformation',
			PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class LsarCreateTrustedDomainEx2Response(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainInformation',
			PLSAPR_TRUSTED_DOMAIN_INFORMATION_EX
			),
			(
			'AuthenticationInformation',
			PLSAPR_TRUSTED_DOMAIN_AUTH_INFORMATION_INTERNAL
			),
			(
			'DesiredAccess',
			ACCESS_MASK
			)
		)


class Opnum60NotUsedOnWire(NDRCALL):
	OPNUM = 60
	structure = (

		)


class Opnum60NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum61NotUsedOnWire(NDRCALL):
	OPNUM = 61
	structure = (

		)


class Opnum61NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum62NotUsedOnWire(NDRCALL):
	OPNUM = 62
	structure = (

		)


class Opnum62NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum63NotUsedOnWire(NDRCALL):
	OPNUM = 63
	structure = (

		)


class Opnum63NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum64NotUsedOnWire(NDRCALL):
	OPNUM = 64
	structure = (

		)


class Opnum64NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum65NotUsedOnWire(NDRCALL):
	OPNUM = 65
	structure = (

		)


class Opnum65NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum66NotUsedOnWire(NDRCALL):
	OPNUM = 66
	structure = (

		)


class Opnum66NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum67NotUsedOnWire(NDRCALL):
	OPNUM = 67
	structure = (

		)


class Opnum67NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Lsar_LSA_TM_68(NDRCALL):
	OPNUM = 68
	structure = (

		)


class Lsar_LSA_TM_68Response(NDRCALL):
	structure = (

		)


class Opnum69NotUsedOnWire(NDRCALL):
	OPNUM = 69
	structure = (

		)


class Opnum69NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum70NotUsedOnWire(NDRCALL):
	OPNUM = 70
	structure = (

		)


class Opnum70NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum71NotUsedOnWire(NDRCALL):
	OPNUM = 71
	structure = (

		)


class Opnum71NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum72NotUsedOnWire(NDRCALL):
	OPNUM = 72
	structure = (

		)


class Opnum72NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class LsarQueryForestTrustInformation(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PLSA_UNICODE_STRING
			),
			(
			'HighestRecordType',
			LSA_FOREST_TRUST_RECORD_TYPE
			)
		)


class LsarQueryForestTrustInformationResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PLSA_UNICODE_STRING
			),
			(
			'HighestRecordType',
			LSA_FOREST_TRUST_RECORD_TYPE
			)
		)


class LsarSetForestTrustInformation(NDRCALL):
	OPNUM = 74
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PLSA_UNICODE_STRING
			),
			(
			'HighestRecordType',
			LSA_FOREST_TRUST_RECORD_TYPE
			),
			(
			'ForestTrustInfo',
			PLSA_FOREST_TRUST_INFORMATION
			),
			(
			'CheckOnly',
			UNSIGNED_CHAR
			)
		)


class LsarSetForestTrustInformationResponse(NDRCALL):
	structure = (
			(
			'PolicyHandle',
			LSAPR_HANDLE
			),
			(
			'TrustedDomainName',
			PLSA_UNICODE_STRING
			),
			(
			'HighestRecordType',
			LSA_FOREST_TRUST_RECORD_TYPE
			),
			(
			'ForestTrustInfo',
			PLSA_FOREST_TRUST_INFORMATION
			),
			(
			'CheckOnly',
			UNSIGNED_CHAR
			)
		)


OPNUMS = {0 : (
	LsarClose,
	LsarCloseResponse
	),1 : (
	Opnum1NotUsedOnWire,
	Opnum1NotUsedOnWireResponse
	),2 : (
	LsarEnumeratePrivileges,
	LsarEnumeratePrivilegesResponse
	),3 : (
	LsarQuerySecurityObject,
	LsarQuerySecurityObjectResponse
	),4 : (
	LsarSetSecurityObject,
	LsarSetSecurityObjectResponse
	),5 : (
	Opnum5NotUsedOnWire,
	Opnum5NotUsedOnWireResponse
	),6 : (
	LsarOpenPolicy,
	LsarOpenPolicyResponse
	),7 : (
	LsarQueryInformationPolicy,
	LsarQueryInformationPolicyResponse
	),8 : (
	LsarSetInformationPolicy,
	LsarSetInformationPolicyResponse
	),9 : (
	Opnum9NotUsedOnWire,
	Opnum9NotUsedOnWireResponse
	),10 : (
	LsarCreateAccount,
	LsarCreateAccountResponse
	),11 : (
	LsarEnumerateAccounts,
	LsarEnumerateAccountsResponse
	),12 : (
	LsarCreateTrustedDomain,
	LsarCreateTrustedDomainResponse
	),13 : (
	LsarEnumerateTrustedDomains,
	LsarEnumerateTrustedDomainsResponse
	),14 : (
	Lsar_LSA_TM_14,
	Lsar_LSA_TM_14Response
	),15 : (
	Lsar_LSA_TM_15,
	Lsar_LSA_TM_15Response
	),16 : (
	LsarCreateSecret,
	LsarCreateSecretResponse
	),17 : (
	LsarOpenAccount,
	LsarOpenAccountResponse
	),18 : (
	LsarEnumeratePrivilegesAccount,
	LsarEnumeratePrivilegesAccountResponse
	),19 : (
	LsarAddPrivilegesToAccount,
	LsarAddPrivilegesToAccountResponse
	),20 : (
	LsarRemovePrivilegesFromAccount,
	LsarRemovePrivilegesFromAccountResponse
	),21 : (
	Opnum21NotUsedOnWire,
	Opnum21NotUsedOnWireResponse
	),22 : (
	Opnum22NotUsedOnWire,
	Opnum22NotUsedOnWireResponse
	),23 : (
	LsarGetSystemAccessAccount,
	LsarGetSystemAccessAccountResponse
	),24 : (
	LsarSetSystemAccessAccount,
	LsarSetSystemAccessAccountResponse
	),25 : (
	LsarOpenTrustedDomain,
	LsarOpenTrustedDomainResponse
	),26 : (
	LsarQueryInfoTrustedDomain,
	LsarQueryInfoTrustedDomainResponse
	),27 : (
	LsarSetInformationTrustedDomain,
	LsarSetInformationTrustedDomainResponse
	),28 : (
	LsarOpenSecret,
	LsarOpenSecretResponse
	),29 : (
	LsarSetSecret,
	LsarSetSecretResponse
	),30 : (
	LsarQuerySecret,
	LsarQuerySecretResponse
	),31 : (
	LsarLookupPrivilegeValue,
	LsarLookupPrivilegeValueResponse
	),32 : (
	LsarLookupPrivilegeName,
	LsarLookupPrivilegeNameResponse
	),33 : (
	LsarLookupPrivilegeDisplayName,
	LsarLookupPrivilegeDisplayNameResponse
	),34 : (
	LsarDeleteObject,
	LsarDeleteObjectResponse
	),35 : (
	LsarEnumerateAccountsWithUserRight,
	LsarEnumerateAccountsWithUserRightResponse
	),36 : (
	LsarEnumerateAccountRights,
	LsarEnumerateAccountRightsResponse
	),37 : (
	LsarAddAccountRights,
	LsarAddAccountRightsResponse
	),38 : (
	LsarRemoveAccountRights,
	LsarRemoveAccountRightsResponse
	),39 : (
	LsarQueryTrustedDomainInfo,
	LsarQueryTrustedDomainInfoResponse
	),40 : (
	LsarSetTrustedDomainInfo,
	LsarSetTrustedDomainInfoResponse
	),41 : (
	LsarDeleteTrustedDomain,
	LsarDeleteTrustedDomainResponse
	),42 : (
	LsarStorePrivateData,
	LsarStorePrivateDataResponse
	),43 : (
	LsarRetrievePrivateData,
	LsarRetrievePrivateDataResponse
	),44 : (
	LsarOpenPolicy2,
	LsarOpenPolicy2Response
	),45 : (
	Lsar_LSA_TM_45,
	Lsar_LSA_TM_45Response
	),46 : (
	LsarQueryInformationPolicy2,
	LsarQueryInformationPolicy2Response
	),47 : (
	LsarSetInformationPolicy2,
	LsarSetInformationPolicy2Response
	),48 : (
	LsarQueryTrustedDomainInfoByName,
	LsarQueryTrustedDomainInfoByNameResponse
	),49 : (
	LsarSetTrustedDomainInfoByName,
	LsarSetTrustedDomainInfoByNameResponse
	),50 : (
	LsarEnumerateTrustedDomainsEx,
	LsarEnumerateTrustedDomainsExResponse
	),51 : (
	LsarCreateTrustedDomainEx,
	LsarCreateTrustedDomainExResponse
	),52 : (
	Opnum52NotUsedOnWire,
	Opnum52NotUsedOnWireResponse
	),53 : (
	LsarQueryDomainInformationPolicy,
	LsarQueryDomainInformationPolicyResponse
	),54 : (
	LsarSetDomainInformationPolicy,
	LsarSetDomainInformationPolicyResponse
	),55 : (
	LsarOpenTrustedDomainByName,
	LsarOpenTrustedDomainByNameResponse
	),56 : (
	Opnum56NotUsedOnWire,
	Opnum56NotUsedOnWireResponse
	),57 : (
	Lsar_LSA_TM_57,
	Lsar_LSA_TM_57Response
	),58 : (
	Lsar_LSA_TM_58,
	Lsar_LSA_TM_58Response
	),59 : (
	LsarCreateTrustedDomainEx2,
	LsarCreateTrustedDomainEx2Response
	),60 : (
	Opnum60NotUsedOnWire,
	Opnum60NotUsedOnWireResponse
	),61 : (
	Opnum61NotUsedOnWire,
	Opnum61NotUsedOnWireResponse
	),62 : (
	Opnum62NotUsedOnWire,
	Opnum62NotUsedOnWireResponse
	),63 : (
	Opnum63NotUsedOnWire,
	Opnum63NotUsedOnWireResponse
	),64 : (
	Opnum64NotUsedOnWire,
	Opnum64NotUsedOnWireResponse
	),65 : (
	Opnum65NotUsedOnWire,
	Opnum65NotUsedOnWireResponse
	),66 : (
	Opnum66NotUsedOnWire,
	Opnum66NotUsedOnWireResponse
	),67 : (
	Opnum67NotUsedOnWire,
	Opnum67NotUsedOnWireResponse
	),68 : (
	Lsar_LSA_TM_68,
	Lsar_LSA_TM_68Response
	),69 : (
	Opnum69NotUsedOnWire,
	Opnum69NotUsedOnWireResponse
	),70 : (
	Opnum70NotUsedOnWire,
	Opnum70NotUsedOnWireResponse
	),71 : (
	Opnum71NotUsedOnWire,
	Opnum71NotUsedOnWireResponse
	),72 : (
	Opnum72NotUsedOnWire,
	Opnum72NotUsedOnWireResponse
	),73 : (
	LsarQueryForestTrustInformation,
	LsarQueryForestTrustInformationResponse
	),74 : (
	LsarSetForestTrustInformation,
	LsarSetForestTrustInformationResponse
	)}
