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

#logon Definition

#################################################################################

MSRPC_UUID_LOGON = uuidtup_to_bin(('12345678-1234-ABCD-EF00-01234567CFFB','0.0'))


class DATA_USHORT(NDRUniConformantArray):
    item = CHAR

class PTR_USHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_USHORT),
    )

class USHORT(NDRSTRUCT):
    structure = (
	('Length', USHORT),	('MaximumLength', USHORT),	('Buffer', PTR_USHORT),

    )
        

class OLD_LARGE_INTEGER(NDRSTRUCT):
    structure = (
        ('LowPart', ULONG),('HighPart', LONG),
    )
class POLD_LARGE_INTEGER(NDRPOINTER):
    referent = (
        ('Data', OLD_LARGE_INTEGER),
    )    


class CYPHER_BLOCK(NDRSTRUCT):
    structure = (
        ('data', CHAR),
    )
class PCYPHER_BLOCK(NDRPOINTER):
    referent = (
        ('Data', CYPHER_BLOCK),
    )    


class NT_OWF_PASSWORD(NDRSTRUCT):
    structure = (
        ('data', CYPHER_BLOCK),
    )
class PNT_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', NT_OWF_PASSWORD),
    )    
ENCRYPTED_NT_OWF_PASSWORD = NT_OWF_PASSWORD
class PENCRYPTED_NT_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', NT_OWF_PASSWORD),
    )    


class LM_OWF_PASSWORD(NDRSTRUCT):
    structure = (
        ('data', CYPHER_BLOCK),
    )
class PLM_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', LM_OWF_PASSWORD),
    )    
ENCRYPTED_LM_OWF_PASSWORD = LM_OWF_PASSWORD
class PENCRYPTED_LM_OWF_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', LM_OWF_PASSWORD),
    )    

LOGONSRV_HANDLE = WCHAR_T

class NLPR_SID_INFORMATION(NDRSTRUCT):
    structure = (
        ('SidPointer', PRPC_SID),
    )
class PNLPR_SID_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NLPR_SID_INFORMATION),
    )    


class NLPR_SID_ARRAY(NDRSTRUCT):
    structure = (
        ('Count', ULONG),('Sids', PNLPR_SID_INFORMATION),
    )
class PNLPR_SID_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NLPR_SID_ARRAY),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Length', ULONG),	('MaximumLength', ULONG),	('Buffer', PTR_ULONG),

    )
        

class DATA_USHORT(NDRUniConformantArray):
    item = UCHAR

class PTR_USHORT(NDRPOINTER):
    referent = (
        ('Data', DATA_USHORT),
    )

class USHORT(NDRSTRUCT):
    structure = (
	('UnitsPerWeek', USHORT),	('LogonHours', PTR_USHORT),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('SensitiveData', UCHAR),	('DataLength', ULONG),	('Data', PTR_ULONG),

    )
        

class NLPR_MODIFIED_COUNT(NDRSTRUCT):
    structure = (
        ('ModifiedCount', OLD_LARGE_INTEGER),
    )
class PNLPR_MODIFIED_COUNT(NDRPOINTER):
    referent = (
        ('Data', NLPR_MODIFIED_COUNT),
    )    


class NLPR_QUOTA_LIMITS(NDRSTRUCT):
    structure = (
        ('PagedPoolLimit', ULONG),('NonPagedPoolLimit', ULONG),('MinimumWorkingSetSize', ULONG),('MaximumWorkingSetSize', ULONG),('PagefileLimit', ULONG),('Reserved', OLD_LARGE_INTEGER),
    )
class PNLPR_QUOTA_LIMITS(NDRPOINTER):
    referent = (
        ('Data', NLPR_QUOTA_LIMITS),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('UserName', RPC_UNICODE_STRING),	('FullName', RPC_UNICODE_STRING),	('UserId', ULONG),	('PrimaryGroupId', ULONG),	('HomeDirectory', RPC_UNICODE_STRING),	('HomeDirectoryDrive', RPC_UNICODE_STRING),	('ScriptPath', RPC_UNICODE_STRING),	('AdminComment', RPC_UNICODE_STRING),	('WorkStations', RPC_UNICODE_STRING),	('LastLogon', OLD_LARGE_INTEGER),	('LastLogoff', OLD_LARGE_INTEGER),	('LogonHours', NLPR_LOGON_HOURS),	('BadPasswordCount', USHORT),	('LogonCount', USHORT),	('PasswordLastSet', OLD_LARGE_INTEGER),	('AccountExpires', OLD_LARGE_INTEGER),	('UserAccountControl', ULONG),	('EncryptedNtOwfPassword', ENCRYPTED_NT_OWF_PASSWORD),	('EncryptedLmOwfPassword', ENCRYPTED_LM_OWF_PASSWORD),	('NtPasswordPresent', UCHAR),	('LmPasswordPresent', UCHAR),	('PasswordExpired', UCHAR),	('UserComment', RPC_UNICODE_STRING),	('Parameters', RPC_UNICODE_STRING),	('CountryCode', USHORT),	('CodePage', USHORT),	('PrivateData', NLPR_USER_PRIVATE_INFO),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('ProfilePath', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Name', RPC_UNICODE_STRING),	('RelativeId', ULONG),	('Attributes', ULONG),	('AdminComment', RPC_UNICODE_STRING),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DummyString1', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = ULONG

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Members', ULONG),	('Attributes', PTR_ULONG),
	('MemberCount', ULONG),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Name', RPC_UNICODE_STRING),	('RelativeId', ULONG),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('Comment', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class NETLOGON_DELTA_ALIAS_MEMBER(NDRSTRUCT):
    structure = (
        ('Members', NLPR_SID_ARRAY),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_ALIAS_MEMBER(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_ALIAS_MEMBER),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('DomainName', RPC_UNICODE_STRING),	('OemInformation', RPC_UNICODE_STRING),	('ForceLogoff', OLD_LARGE_INTEGER),	('MinPasswordLength', USHORT),	('PasswordHistoryLength', USHORT),	('MaxPasswordAge', OLD_LARGE_INTEGER),	('MinPasswordAge', OLD_LARGE_INTEGER),	('DomainModifiedCount', OLD_LARGE_INTEGER),	('DomainCreationTime', OLD_LARGE_INTEGER),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DomainLockoutInformation', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('PasswordProperties', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class NETLOGON_RENAME_GROUP(NDRSTRUCT):
    structure = (
        ('OldName', RPC_UNICODE_STRING),('NewName', RPC_UNICODE_STRING),('DummyString1', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_RENAME_GROUP(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_RENAME_GROUP),
    )    


class NETLOGON_RENAME_USER(NDRSTRUCT):
    structure = (
        ('OldName', RPC_UNICODE_STRING),('NewName', RPC_UNICODE_STRING),('DummyString1', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_RENAME_USER(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_RENAME_USER),
    )    


class NETLOGON_RENAME_ALIAS(NDRSTRUCT):
    structure = (
        ('OldName', RPC_UNICODE_STRING),('NewName', RPC_UNICODE_STRING),('DummyString1', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_RENAME_ALIAS(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_RENAME_ALIAS),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('MaximumLogSize', ULONG),	('AuditRetentionPeriod', OLD_LARGE_INTEGER),	('AuditingMode', UCHAR),	('MaximumAuditEventCount', ULONG),	('EventAuditingOptions', ULONG),	('PrimaryDomainName', RPC_UNICODE_STRING),	('PrimaryDomainSid', PRPC_SID),	('QuotaLimits', NLPR_QUOTA_LIMITS),	('ModifiedId', OLD_LARGE_INTEGER),	('DatabaseCreationTime', OLD_LARGE_INTEGER),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DummyString1', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('DomainName', RPC_UNICODE_STRING),	('NumControllerEntries', ULONG),	('ControllerNames', PRPC_UNICODE_STRING),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DummyString1', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('TrustedPosixOffset', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('PrivilegeEntries', ULONG),	('PrivilegeControl', ULONG),	('PrivilegeAttributes', ULONG),	('PrivilegeNames', PRPC_UNICODE_STRING),	('QuotaLimits', NLPR_QUOTA_LIMITS),	('SystemAccessFlags', ULONG),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DummyString1', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('CurrentValue', NLPR_CR_CIPHER_VALUE),	('CurrentValueSetTime', OLD_LARGE_INTEGER),	('OldValue', NLPR_CR_CIPHER_VALUE),	('OldValueSetTime', OLD_LARGE_INTEGER),	('SecurityInformation', SECURITY_INFORMATION),	('SecuritySize', ULONG),	('SecurityDescriptor', PTR_ULONG),
	('DummyString1', RPC_UNICODE_STRING),	('DummyString2', RPC_UNICODE_STRING),	('DummyString3', RPC_UNICODE_STRING),	('DummyString4', RPC_UNICODE_STRING),	('DummyLong1', ULONG),	('DummyLong2', ULONG),	('DummyLong3', ULONG),	('DummyLong4', ULONG),
    )
        

class NETLOGON_DELTA_DELETE_GROUP(NDRSTRUCT):
    structure = (
        ('AccountName', WCHAR_T),('DummyString1', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_DELETE_GROUP(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_DELETE_GROUP),
    )    


class NETLOGON_DELTA_DELETE_USER(NDRSTRUCT):
    structure = (
        ('AccountName', WCHAR_T),('DummyString1', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DELTA_DELETE_USER(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_DELETE_USER),
    )    


AddOrChangeDomain = 1,
AddOrChangeGroup = 2,
DeleteGroup = 3,
RenameGroup = 4,
AddOrChangeUser = 5,
DeleteUser = 6,
RenameUser = 7,
ChangeGroupMembership = 8,
AddOrChangeAlias = 9,
DeleteAlias = 10,
RenameAlias = 11,
ChangeAliasMembership = 12,
AddOrChangeLsaPolicy = 13,
AddOrChangeLsaTDomain = 14,
DeleteLsaTDomain = 15,
AddOrChangeLsaAccount = 16,
DeleteLsaAccount = 17,
AddOrChangeLsaSecret = 18,
DeleteLsaSecret = 19,
DeleteGroupByName = 20,
DeleteUserByName = 21,
SerialNumberSkip = 22
        

class NETLOGON_DELTA_UNION(NDRUNION):
    union = {
        AddOrChangeDomain: ('DeltaDomain',PNETLOGON_DELTA_DOMAIN),AddOrChangeGroup: ('DeltaGroup',PNETLOGON_DELTA_GROUP),RenameGroup: ('DeltaRenameGroup',PNETLOGON_DELTA_RENAME_GROUP),AddOrChangeUser: ('DeltaUser',PNETLOGON_DELTA_USER),RenameUser: ('DeltaRenameUser',PNETLOGON_DELTA_RENAME_USER),ChangeGroupMembership: ('DeltaGroupMember',PNETLOGON_DELTA_GROUP_MEMBER),AddOrChangeAlias: ('DeltaAlias',PNETLOGON_DELTA_ALIAS),RenameAlias: ('DeltaRenameAlias',PNETLOGON_DELTA_RENAME_ALIAS),ChangeAliasMembership: ('DeltaAliasMember',PNETLOGON_DELTA_ALIAS_MEMBER),AddOrChangeLsaPolicy: ('DeltaPolicy',PNETLOGON_DELTA_POLICY),AddOrChangeLsaTDomain: ('DeltaTDomains',PNETLOGON_DELTA_TRUSTED_DOMAINS),AddOrChangeLsaAccount: ('DeltaAccounts',PNETLOGON_DELTA_ACCOUNTS),AddOrChangeLsaSecret: ('DeltaSecret',PNETLOGON_DELTA_SECRET),DeleteGroupByName: ('DeltaDeleteGroup',PNETLOGON_DELTA_DELETE_GROUP),DeleteUserByName: ('DeltaDeleteUser',PNETLOGON_DELTA_DELETE_USER),SerialNumberSkip: ('DeltaSerialNumberSkip',PNLPR_MODIFIED_COUNT),
    }
        class PNETLOGON_DELTA_UNION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_UNION),
    )    


class NETLOGON_DELTA_ID_UNION(NDRUNION):
    union = {
        AddOrChangeDomain: ('Rid',ULONG),AddOrChangeLsaPolicy: ('Sid',PRPC_SID),AddOrChangeLsaSecret: ('Name',WCHAR_T),
    }
        class PNETLOGON_DELTA_ID_UNION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_ID_UNION),
    )    


class NETLOGON_DELTA_ENUM(NDRSTRUCT):
    structure = (
        ('DeltaType', NETLOGON_DELTA_TYPE),('DeltaID', NETLOGON_DELTA_ID_UNION),('DeltaUnion', NETLOGON_DELTA_UNION),
    )
class PNETLOGON_DELTA_ENUM(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_ENUM),
    )    


class NETLOGON_DELTA_ENUM_ARRAY(NDRSTRUCT):
    structure = (
        ('CountReturned', DWORD),('Deltas', PNETLOGON_DELTA_ENUM),
    )
class PNETLOGON_DELTA_ENUM_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DELTA_ENUM_ARRAY),
    )    


class NETLOGON_LOGON_IDENTITY_INFO(NDRSTRUCT):
    structure = (
        ('LogonDomainName', RPC_UNICODE_STRING),('ParameterControl', ULONG),('Reserved', OLD_LARGE_INTEGER),('UserName', RPC_UNICODE_STRING),('Workstation', RPC_UNICODE_STRING),
    )
class PNETLOGON_LOGON_IDENTITY_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_LOGON_IDENTITY_INFO),
    )    


class NETLOGON_INTERACTIVE_INFO(NDRSTRUCT):
    structure = (
        ('Identity', NETLOGON_LOGON_IDENTITY_INFO),('LmOwfPassword', LM_OWF_PASSWORD),('NtOwfPassword', NT_OWF_PASSWORD),
    )
class PNETLOGON_INTERACTIVE_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_INTERACTIVE_INFO),
    )    


NetlogonInteractiveInformation = 1,
NetlogonNetworkInformation = 2,
NetlogonServiceInformation = 3,
NetlogonGenericInformation = 4,
NetlogonInteractiveTransitiveInformation = 5,
NetlogonNetworkTransitiveInformation = 6,
NetlogonServiceTransitiveInformation = 7
        

class NETLOGON_SERVICE_INFO(NDRSTRUCT):
    structure = (
        ('Identity', NETLOGON_LOGON_IDENTITY_INFO),('LmOwfPassword', LM_OWF_PASSWORD),('NtOwfPassword', NT_OWF_PASSWORD),
    )
class PNETLOGON_SERVICE_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_SERVICE_INFO),
    )    


class LM_CHALLENGE(NDRSTRUCT):
    structure = (
        ('data', CHAR),
    )


class NETLOGON_NETWORK_INFO(NDRSTRUCT):
    structure = (
        ('Identity', NETLOGON_LOGON_IDENTITY_INFO),('LmChallenge', LM_CHALLENGE),('NtChallengeResponse', STRING),('LmChallengeResponse', STRING),
    )
class PNETLOGON_NETWORK_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_NETWORK_INFO),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Identity', NETLOGON_LOGON_IDENTITY_INFO),	('PackageName', RPC_UNICODE_STRING),	('DataLength', ULONG),	('LogonData', PTR_ULONG),

    )
        

class NETLOGON_LEVEL(NDRUNION):
    union = {
        NetlogonInteractiveInformation: ('LogonInteractive',PNETLOGON_INTERACTIVE_INFO),NetlogonInteractiveTransitiveInformation: ('LogonInteractiveTransitive',PNETLOGON_INTERACTIVE_INFO),NetlogonServiceInformation: ('LogonService',PNETLOGON_SERVICE_INFO),NetlogonServiceTransitiveInformation: ('LogonServiceTransitive',PNETLOGON_SERVICE_INFO),NetlogonNetworkInformation: ('LogonNetwork',PNETLOGON_NETWORK_INFO),NetlogonNetworkTransitiveInformation: ('LogonNetworkTransitive',PNETLOGON_NETWORK_INFO),NetlogonGenericInformation: ('LogonGeneric',PNETLOGON_GENERIC_INFO),
    }
        class PNETLOGON_LEVEL(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_LEVEL),
    )    


NetlogonValidationUasInfo = 1,
NetlogonValidationSamInfo = 2,
NetlogonValidationSamInfo2 = 3,
NetlogonValidationGenericInfo = 4,
NetlogonValidationGenericInfo2 = 5,
NetlogonValidationSamInfo4 = 6
        

class GROUP_MEMBERSHIP(NDRSTRUCT):
    structure = (
        ('RelativeId', ULONG),('Attributes', ULONG),
    )
class PGROUP_MEMBERSHIP(NDRPOINTER):
    referent = (
        ('Data', GROUP_MEMBERSHIP),
    )    


class USER_SESSION_KEY(NDRSTRUCT):
    structure = (
        ('data', CYPHER_BLOCK),
    )
class PUSER_SESSION_KEY(NDRPOINTER):
    referent = (
        ('Data', USER_SESSION_KEY),
    )    


class NETLOGON_SID_AND_ATTRIBUTES(NDRSTRUCT):
    structure = (
        ('Sid', PRPC_SID),('Attributes', ULONG),
    )
class PNETLOGON_SID_AND_ATTRIBUTES(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_SID_AND_ATTRIBUTES),
    )    


class NETLOGON_VALIDATION_SAM_INFO(NDRSTRUCT):
    structure = (
        ('LogonTime', OLD_LARGE_INTEGER),('LogoffTime', OLD_LARGE_INTEGER),('KickOffTime', OLD_LARGE_INTEGER),('PasswordLastSet', OLD_LARGE_INTEGER),('PasswordCanChange', OLD_LARGE_INTEGER),('PasswordMustChange', OLD_LARGE_INTEGER),('EffectiveName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('LogonScript', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('LogonCount', USHORT),('BadPasswordCount', USHORT),('UserId', ULONG),('PrimaryGroupId', ULONG),('GroupCount', ULONG),('GroupIds', PGROUP_MEMBERSHIP),('UserFlags', ULONG),('UserSessionKey', USER_SESSION_KEY),('LogonServer', RPC_UNICODE_STRING),('LogonDomainName', RPC_UNICODE_STRING),('LogonDomainId', PRPC_SID),('ExpansionRoom', ULONG),
    )
class PNETLOGON_VALIDATION_SAM_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_VALIDATION_SAM_INFO),
    )    


class NETLOGON_VALIDATION_SAM_INFO2(NDRSTRUCT):
    structure = (
        ('LogonTime', OLD_LARGE_INTEGER),('LogoffTime', OLD_LARGE_INTEGER),('KickOffTime', OLD_LARGE_INTEGER),('PasswordLastSet', OLD_LARGE_INTEGER),('PasswordCanChange', OLD_LARGE_INTEGER),('PasswordMustChange', OLD_LARGE_INTEGER),('EffectiveName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('LogonScript', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('LogonCount', USHORT),('BadPasswordCount', USHORT),('UserId', ULONG),('PrimaryGroupId', ULONG),('GroupCount', ULONG),('GroupIds', PGROUP_MEMBERSHIP),('UserFlags', ULONG),('UserSessionKey', USER_SESSION_KEY),('LogonServer', RPC_UNICODE_STRING),('LogonDomainName', RPC_UNICODE_STRING),('LogonDomainId', PRPC_SID),('ExpansionRoom', ULONG),('SidCount', ULONG),('ExtraSids', PNETLOGON_SID_AND_ATTRIBUTES),
    )
class PNETLOGON_VALIDATION_SAM_INFO2(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_VALIDATION_SAM_INFO2),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('DataLength', ULONG),	('ValidationData', PTR_ULONG),

    )
        

class NETLOGON_VALIDATION_SAM_INFO4(NDRSTRUCT):
    structure = (
        ('LogonTime', OLD_LARGE_INTEGER),('LogoffTime', OLD_LARGE_INTEGER),('KickOffTime', OLD_LARGE_INTEGER),('PasswordLastSet', OLD_LARGE_INTEGER),('PasswordCanChange', OLD_LARGE_INTEGER),('PasswordMustChange', OLD_LARGE_INTEGER),('EffectiveName', RPC_UNICODE_STRING),('FullName', RPC_UNICODE_STRING),('LogonScript', RPC_UNICODE_STRING),('ProfilePath', RPC_UNICODE_STRING),('HomeDirectory', RPC_UNICODE_STRING),('HomeDirectoryDrive', RPC_UNICODE_STRING),('LogonCount', UNSIGNED_SHORT),('BadPasswordCount', UNSIGNED_SHORT),('UserId', UNSIGNED_LONG),('PrimaryGroupId', UNSIGNED_LONG),('GroupCount', UNSIGNED_LONG),('GroupIds', PGROUP_MEMBERSHIP),('UserFlags', UNSIGNED_LONG),('UserSessionKey', USER_SESSION_KEY),('LogonServer', RPC_UNICODE_STRING),('LogonDomainName', RPC_UNICODE_STRING),('LogonDomainId', PRPC_SID),('LMKey', UNSIGNED_CHAR),('UserAccountControl', ULONG),('SubAuthStatus', ULONG),('LastSuccessfulILogon', OLD_LARGE_INTEGER),('LastFailedILogon', OLD_LARGE_INTEGER),('FailedILogonCount', ULONG),('Reserved4', ULONG),('SidCount', UNSIGNED_LONG),('ExtraSids', PNETLOGON_SID_AND_ATTRIBUTES),('DnsLogonDomainName', RPC_UNICODE_STRING),('Upn', RPC_UNICODE_STRING),('ExpansionString1', RPC_UNICODE_STRING),('ExpansionString2', RPC_UNICODE_STRING),('ExpansionString3', RPC_UNICODE_STRING),('ExpansionString4', RPC_UNICODE_STRING),('ExpansionString5', RPC_UNICODE_STRING),('ExpansionString6', RPC_UNICODE_STRING),('ExpansionString7', RPC_UNICODE_STRING),('ExpansionString8', RPC_UNICODE_STRING),('ExpansionString9', RPC_UNICODE_STRING),('ExpansionString10', RPC_UNICODE_STRING),
    )
class PNETLOGON_VALIDATION_SAM_INFO4(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_VALIDATION_SAM_INFO4),
    )    


class NETLOGON_VALIDATION(NDRUNION):
    union = {
        NetlogonValidationSamInfo: ('ValidationSam',PNETLOGON_VALIDATION_SAM_INFO),NetlogonValidationSamInfo2: ('ValidationSam2',PNETLOGON_VALIDATION_SAM_INFO2),NetlogonValidationGenericInfo2: ('ValidationGeneric2',PNETLOGON_VALIDATION_GENERIC_INFO2),NetlogonValidationSamInfo4: ('ValidationSam4',PNETLOGON_VALIDATION_SAM_INFO4),
    }
        class PNETLOGON_VALIDATION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_VALIDATION),
    )    


class NETLOGON_CONTROL_DATA_INFORMATION(NDRUNION):
    union = {
        5: ('TrustedDomainName',WCHAR_T),65534: ('DebugFlag',DWORD),8: ('UserName',WCHAR_T),
    }
        class PNETLOGON_CONTROL_DATA_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_CONTROL_DATA_INFORMATION),
    )    


class NETLOGON_INFO_1(NDRSTRUCT):
    structure = (
        ('netlog1_flags', DWORD),('netlog1_pdc_connection_status', NET_API_STATUS),
    )
class PNETLOGON_INFO_1(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_INFO_1),
    )    


class NETLOGON_INFO_2(NDRSTRUCT):
    structure = (
        ('netlog2_flags', DWORD),('netlog2_pdc_connection_status', NET_API_STATUS),('netlog2_trusted_dc_name', WCHAR_T),('netlog2_tc_connection_status', NET_API_STATUS),
    )
class PNETLOGON_INFO_2(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_INFO_2),
    )    


class NETLOGON_INFO_3(NDRSTRUCT):
    structure = (
        ('netlog3_flags', DWORD),('netlog3_logon_attempts', DWORD),('netlog3_reserved1', DWORD),('netlog3_reserved2', DWORD),('netlog3_reserved3', DWORD),('netlog3_reserved4', DWORD),('netlog3_reserved5', DWORD),
    )
class PNETLOGON_INFO_3(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_INFO_3),
    )    


class NETLOGON_INFO_4(NDRSTRUCT):
    structure = (
        ('netlog4_trusted_dc_name', WCHAR_T),('netlog4_trusted_domain_name', WCHAR_T),
    )
class PNETLOGON_INFO_4(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_INFO_4),
    )    


class NETLOGON_CONTROL_QUERY_INFORMATION(NDRUNION):
    union = {
        1: ('NetlogonInfo1',PNETLOGON_INFO_1),2: ('NetlogonInfo2',PNETLOGON_INFO_2),3: ('NetlogonInfo3',PNETLOGON_INFO_3),4: ('NetlogonInfo4',PNETLOGON_INFO_4),
    }
        class PNETLOGON_CONTROL_QUERY_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_CONTROL_QUERY_INFORMATION),
    )    


NormalState = 0,
DomainState = 1,
GroupState = 2,
UasBuiltInGroupState = 3,
UserState = 4,
GroupMemberState = 5,
AliasState = 6,
AliasMemberState = 7,
SamDoneState = 8
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('DomainNameByteCount', ULONG),	('DomainNames', PTR_ULONG),

    )
        

class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('LsaPolicySize', ULONG),	('LsaPolicy', PTR_ULONG),

    )
        

class NETLOGON_ONE_DOMAIN_INFO(NDRSTRUCT):
    structure = (
        ('DomainName', RPC_UNICODE_STRING),('DnsDomainName', RPC_UNICODE_STRING),('DnsForestName', RPC_UNICODE_STRING),('DomainGuid', GUID),('DomainSid', PRPC_SID),('TrustExtension', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('DummyLong1', ULONG),('DummyLong2', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_ONE_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_ONE_DOMAIN_INFO),
    )    


class NETLOGON_DOMAIN_INFO(NDRSTRUCT):
    structure = (
        ('PrimaryDomain', NETLOGON_ONE_DOMAIN_INFO),('TrustedDomainCount', ULONG),('TrustedDomains', PNETLOGON_ONE_DOMAIN_INFO),('LsaPolicy', NETLOGON_LSA_POLICY_INFO),('DnsHostNameInDs', RPC_UNICODE_STRING),('DummyString2', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('WorkstationFlags', ULONG),('SupportedEncTypes', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DOMAIN_INFO),
    )    


class NETLOGON_DOMAIN_INFORMATION(NDRUNION):
    union = {
        1: ('DomainInfo',PNETLOGON_DOMAIN_INFO),2: ('LsaPolicyInfo',PNETLOGON_LSA_POLICY_INFO),
    }
        class PNETLOGON_DOMAIN_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_DOMAIN_INFORMATION),
    )    


class NETLOGON_WORKSTATION_INFO(NDRSTRUCT):
    structure = (
        ('LsaPolicy', NETLOGON_LSA_POLICY_INFO),('DnsHostName', WCHAR_T),('SiteName', WCHAR_T),('Dummy1', WCHAR_T),('Dummy2', WCHAR_T),('Dummy3', WCHAR_T),('Dummy4', WCHAR_T),('OsVersion', RPC_UNICODE_STRING),('OsName', RPC_UNICODE_STRING),('DummyString3', RPC_UNICODE_STRING),('DummyString4', RPC_UNICODE_STRING),('WorkstationFlags', ULONG),('KerberosSupportedEncryptionTypes', ULONG),('DummyLong3', ULONG),('DummyLong4', ULONG),
    )
class PNETLOGON_WORKSTATION_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_WORKSTATION_INFO),
    )    


class NETLOGON_WORKSTATION_INFORMATION(NDRUNION):
    union = {
        1: ('WorkstationInfo',PNETLOGON_WORKSTATION_INFO),2: ('LsaPolicyInfo',PNETLOGON_WORKSTATION_INFO),
    }
        class PNETLOGON_WORKSTATION_INFORMATION(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_WORKSTATION_INFORMATION),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('lpSockaddr', PTR_NL_SOCKET_ADDRESS),
	('iSockaddrLength', ULONG),
    )
        

class NL_SITE_NAME_ARRAY(NDRSTRUCT):
    structure = (
        ('EntryCount', ULONG),('SiteNames', PRPC_UNICODE_STRING),
    )
class PNL_SITE_NAME_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NL_SITE_NAME_ARRAY),
    )    


class DS_DOMAIN_TRUSTSW(NDRSTRUCT):
    structure = (
        ('NetbiosDomainName', WCHAR_T),('DnsDomainName', WCHAR_T),('Flags', ULONG),('ParentIndex', ULONG),('TrustType', ULONG),('TrustAttributes', ULONG),('DomainSid', PRPC_SID),('DomainGuid', GUID),
    )
class PDS_DOMAIN_TRUSTSW(NDRPOINTER):
    referent = (
        ('Data', DS_DOMAIN_TRUSTSW),
    )    


class NETLOGON_TRUSTED_DOMAIN_ARRAY(NDRSTRUCT):
    structure = (
        ('DomainCount', DWORD),('Domains', PDS_DOMAIN_TRUSTSW),
    )
class PNETLOGON_TRUSTED_DOMAIN_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_TRUSTED_DOMAIN_ARRAY),
    )    


class NL_SITE_NAME_EX_ARRAY(NDRSTRUCT):
    structure = (
        ('EntryCount', ULONG),('SiteNames', PRPC_UNICODE_STRING),('SubnetNames', PRPC_UNICODE_STRING),
    )
class PNL_SITE_NAME_EX_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NL_SITE_NAME_EX_ARRAY),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = PRPC_UNICODE_STRING

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('UlongEntryCount', ULONG),	('UlongData', ULONG),	('UnicodeStringEntryCount', ULONG),	('UnicodeStringData', PTR_ULONG),

    )
        

class NETLOGON_VALIDATION_UAS_INFO(NDRSTRUCT):
    structure = (
        ('usrlog1_eff_name', WCHAR_T),('usrlog1_priv', DWORD),('usrlog1_auth_flags', DWORD),('usrlog1_num_logons', DWORD),('usrlog1_bad_pw_count', DWORD),('usrlog1_last_logon', DWORD),('usrlog1_last_logoff', DWORD),('usrlog1_logoff_time', DWORD),('usrlog1_kickoff_time', DWORD),('usrlog1_password_age', DWORD),('usrlog1_pw_can_change', DWORD),('usrlog1_pw_must_change', DWORD),('usrlog1_computer', WCHAR_T),('usrlog1_domain', WCHAR_T),('usrlog1_script_path', WCHAR_T),('usrlog1_reserved1', DWORD),
    )
class PNETLOGON_VALIDATION_UAS_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_VALIDATION_UAS_INFO),
    )    


class NETLOGON_LOGOFF_UAS_INFO(NDRSTRUCT):
    structure = (
        ('Duration', DWORD),('LogonCount', USHORT),
    )
class PNETLOGON_LOGOFF_UAS_INFO(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_LOGOFF_UAS_INFO),
    )    


class NETLOGON_CAPABILITIES(NDRUNION):
    union = {
        1: ('ServerCapabilities',ULONG),
    }
        class PNETLOGON_CAPABILITIES(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_CAPABILITIES),
    )    


class NETLOGON_CREDENTIAL(NDRSTRUCT):
    structure = (
        ('data', CHAR),
    )
class PNETLOGON_CREDENTIAL(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_CREDENTIAL),
    )    


class NETLOGON_AUTHENTICATOR(NDRSTRUCT):
    structure = (
        ('Credential', NETLOGON_CREDENTIAL),('Timestamp', DWORD),
    )
class PNETLOGON_AUTHENTICATOR(NDRPOINTER):
    referent = (
        ('Data', NETLOGON_AUTHENTICATOR),
    )    


NullSecureChannel = 0,
MsvApSecureChannel = 1,
WorkstationSecureChannel = 2,
TrustedDnsDomainSecureChannel = 3,
TrustedDomainSecureChannel = 4,
UasServerSecureChannel = 5,
ServerSecureChannel = 6,
CdcServerSecureChannel = 7
        

class UAS_INFO_0(NDRSTRUCT):
    structure = (
        ('ComputerName', CHAR),('TimeCreated', ULONG),('SerialNumber', ULONG),
    )
class PUAS_INFO_0(NDRPOINTER):
    referent = (
        ('Data', UAS_INFO_0),
    )    


class DOMAIN_CONTROLLER_INFOW(NDRSTRUCT):
    structure = (
        ('DomainControllerName', WCHAR_T),('DomainControllerAddress', WCHAR_T),('DomainControllerAddressType', ULONG),('DomainGuid', GUID),('DomainName', WCHAR_T),('DnsForestName', WCHAR_T),('Flags', ULONG),('DcSiteName', WCHAR_T),('ClientSiteName', WCHAR_T),
    )
class PDOMAIN_CONTROLLER_INFOW(NDRPOINTER):
    referent = (
        ('Data', DOMAIN_CONTROLLER_INFOW),
    )    


class NL_TRUST_PASSWORD(NDRSTRUCT):
    structure = (
        ('Buffer', WCHAR),('Length', ULONG),
    )
class PNL_TRUST_PASSWORD(NDRPOINTER):
    referent = (
        ('Data', NL_TRUST_PASSWORD),
    )    


class NL_PASSWORD_VERSION(NDRSTRUCT):
    structure = (
        ('ReservedField', ULONG),('PasswordVersionNumber', ULONG),('PasswordVersionPresent', ULONG),
    )
class PNL_PASSWORD_VERSION(NDRPOINTER):
    referent = (
        ('Data', NL_PASSWORD_VERSION),
    )    


ForestTrustTopLevelName = 0,
ForestTrustTopLevelNameEx = 1,
ForestTrustDomainInfo = 2,
ForestTrustRecordTypeLast = ForestTrustDomainInfo
        
LSA_RPC_UNICODE_STRING = RPC_UNICODE_STRING
PLSA_RPC_UNICODE_STRING = RPC_UNICODE_STRING

class LSA_FOREST_TRUST_DOMAIN_INFO(NDRSTRUCT):
    structure = (
        ('Sid', PRPC_SID),('DnsName', LSA_RPC_UNICODE_STRING),('NetbiosName', LSA_RPC_UNICODE_STRING),
    )
class PLSA_FOREST_TRUST_DOMAIN_INFO(NDRPOINTER):
    referent = (
        ('Data', LSA_FOREST_TRUST_DOMAIN_INFO),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = UCHAR

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('Length', ULONG),	('Buffer', PTR_ULONG),

    )
        

class FORESTTRUSTDATA(NDRUNION):
    union = {
        ForestTrustTopLevelName: ('TopLevelName',LSA_RPC_UNICODE_STRING),ForestTrustDomainInfo: ('DomainInfo',LSA_FOREST_TRUST_DOMAIN_INFO),3: ('Data',LSA_FOREST_TRUST_BINARY_DATA),
    }
        

class LSA_FOREST_TRUST_RECORD(NDRSTRUCT):
    structure = (
        ('Flags', ULONG),('ForestTrustType', LSA_FOREST_TRUST_RECORD_TYPE),('Time', LARGE_INTEGER),('ForestTrustData', FORESTTRUSTDATA),
    )
class PLSA_FOREST_TRUST_RECORD(NDRPOINTER):
    referent = (
        ('Data', LSA_FOREST_TRUST_RECORD),
    )    


class DATA_ULONG(NDRUniConformantArray):
    item = PLSA_FOREST_TRUST_RECORD

class PTR_ULONG(NDRPOINTER):
    referent = (
        ('Data', DATA_ULONG),
    )

class ULONG(NDRSTRUCT):
    structure = (
	('RecordCount', ULONG),	('Entries', PTR_ULONG),

    )
        

class NL_DNS_NAME_INFO(NDRSTRUCT):
    structure = (
        ('Type', ULONG),('DnsDomainInfo', WCHAR_T),('DnsDomainInfoType', ULONG),('Priority', ULONG),('Weight', ULONG),('Port', ULONG),('Register', UCHAR),('Status', ULONG),
    )
class PNL_DNS_NAME_INFO(NDRPOINTER):
    referent = (
        ('Data', NL_DNS_NAME_INFO),
    )    


class NL_DNS_NAME_INFO_ARRAY(NDRSTRUCT):
    structure = (
        ('EntryCount', ULONG),('DnsNamesInfo', PNL_DNS_NAME_INFO),
    )
class PNL_DNS_NAME_INFO_ARRAY(NDRPOINTER):
    referent = (
        ('Data', NL_DNS_NAME_INFO_ARRAY),
    )    


class NL_OSVERSIONINFO_V1(NDRSTRUCT):
    structure = (
        ('dwOSVersionInfoSize', DWORD),('dwMajorVersion', DWORD),('dwMinorVersion', DWORD),('dwBuildNumber', DWORD),('dwPlatformId', DWORD),('szCSDVersion', WCHAR_T),('wServicePackMajor', USHORT),('wServicePackMinor', USHORT),('wSuiteMask', USHORT),('wProductType', UCHAR),('wReserved', UCHAR),
    )


class NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES_V1(NDRSTRUCT):
    structure = (
        ('ClientDnsHostName', WCHAR_T),('OsVersionInfo_V1', NL_OSVERSIONINFO_V1),('OsName', WCHAR_T),
    )


class NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES(NDRUNION):
    union = {
        1: ('V1',NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES_V1),
    }
        

class NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES_V1(NDRSTRUCT):
    structure = (
        ('HubName', WCHAR_T),('OldDnsHostName', WCHAR_T),('SupportedEncTypes', ULONG),
    )


class NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES(NDRUNION):
    union = {
        1: ('V1',NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES_V1),
    }
        

class NetrLogonUasLogon(NDRCALL):
    opnum = 0
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('UserName', WCHAR_T),
		('Workstation', WCHAR_T),
    )

class NetrLogonUasLogonResponse(NDRCALL):
    structure = (
		('ValidationInformation', PNETLOGON_VALIDATION_UAS_INFO),
    )
        

class NetrLogonUasLogoff(NDRCALL):
    opnum = 1
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('UserName', WCHAR_T),
		('Workstation', WCHAR_T),
    )

class NetrLogonUasLogoffResponse(NDRCALL):
    structure = (
		('LogoffInformation', PNETLOGON_LOGOFF_UAS_INFO),
    )
        

class NetrLogonSamLogon(NDRCALL):
    opnum = 2
    structure = (
		('LogonServer', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('LogonLevel', NETLOGON_LOGON_INFO_CLASS),
		('LogonInformation', PNETLOGON_LEVEL),
		('ValidationLevel', NETLOGON_VALIDATION_INFO_CLASS),
    )

class NetrLogonSamLogonResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('ValidationInformation', PNETLOGON_VALIDATION),
		('Authoritative', UCHAR),
    )
        

class NetrLogonSamLogoff(NDRCALL):
    opnum = 3
    structure = (
		('LogonServer', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('LogonLevel', NETLOGON_LOGON_INFO_CLASS),
		('LogonInformation', PNETLOGON_LEVEL),
    )

class NetrLogonSamLogoffResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
    )
        

class NetrServerReqChallenge(NDRCALL):
    opnum = 4
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('ClientChallenge', PNETLOGON_CREDENTIAL),
    )

class NetrServerReqChallengeResponse(NDRCALL):
    structure = (
		('ServerChallenge', PNETLOGON_CREDENTIAL),
    )
        

class NetrServerAuthenticate(NDRCALL):
    opnum = 5
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('ClientCredential', PNETLOGON_CREDENTIAL),
    )

class NetrServerAuthenticateResponse(NDRCALL):
    structure = (
		('ServerCredential', PNETLOGON_CREDENTIAL),
    )
        

class NetrServerPasswordSet(NDRCALL):
    opnum = 6
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('UasNewPassword', PENCRYPTED_NT_OWF_PASSWORD),
    )

class NetrServerPasswordSetResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
    )
        

class NetrDatabaseDeltas(NDRCALL):
    opnum = 7
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DatabaseID', DWORD),
		('DomainModifiedCount', PNLPR_MODIFIED_COUNT),
		('PreferredMaximumLength', DWORD),
    )

class NetrDatabaseDeltasResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DomainModifiedCount', PNLPR_MODIFIED_COUNT),
		('DeltaArray', PNETLOGON_DELTA_ENUM_ARRAY),
    )
        

class NetrDatabaseSync(NDRCALL):
    opnum = 8
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DatabaseID', DWORD),
		('SyncContext', ULONG),
		('PreferredMaximumLength', DWORD),
    )

class NetrDatabaseSyncResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('SyncContext', ULONG),
		('DeltaArray', PNETLOGON_DELTA_ENUM_ARRAY),
    )
        

class NetrAccountDeltas(NDRCALL):
    opnum = 9
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('RecordId', PUAS_INFO_0),
		('Count', DWORD),
		('Level', DWORD),
		('BufferSize', DWORD),
    )

class NetrAccountDeltasResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('Buffer', UCHAR),
		('CountReturned', ULONG),
		('TotalEntries', ULONG),
		('NextRecordId', PUAS_INFO_0),
    )
        

class NetrAccountSync(NDRCALL):
    opnum = 10
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('Reference', DWORD),
		('Level', DWORD),
		('BufferSize', DWORD),
    )

class NetrAccountSyncResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('Buffer', UCHAR),
		('CountReturned', ULONG),
		('TotalEntries', ULONG),
		('NextReference', ULONG),
		('LastRecordId', PUAS_INFO_0),
    )
        

class NetrGetDCName(NDRCALL):
    opnum = 11
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
    )

class NetrGetDCNameResponse(NDRCALL):
    structure = (
		('Buffer', WCHAR_T),
    )
        

class NetrLogonControl(NDRCALL):
    opnum = 12
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('FunctionCode', DWORD),
		('QueryLevel', DWORD),
    )

class NetrLogonControlResponse(NDRCALL):
    structure = (
		('Buffer', PNETLOGON_CONTROL_QUERY_INFORMATION),
    )
        

class NetrGetAnyDCName(NDRCALL):
    opnum = 13
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
    )

class NetrGetAnyDCNameResponse(NDRCALL):
    structure = (
		('Buffer', WCHAR_T),
    )
        

class NetrLogonControl2(NDRCALL):
    opnum = 14
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('FunctionCode', DWORD),
		('QueryLevel', DWORD),
		('Data', PNETLOGON_CONTROL_DATA_INFORMATION),
    )

class NetrLogonControl2Response(NDRCALL):
    structure = (
		('Buffer', PNETLOGON_CONTROL_QUERY_INFORMATION),
    )
        

class NetrServerAuthenticate2(NDRCALL):
    opnum = 15
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('ClientCredential', PNETLOGON_CREDENTIAL),
		('NegotiateFlags', ULONG),
    )

class NetrServerAuthenticate2Response(NDRCALL):
    structure = (
		('ServerCredential', PNETLOGON_CREDENTIAL),
		('NegotiateFlags', ULONG),
    )
        

class NetrDatabaseSync2(NDRCALL):
    opnum = 16
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DatabaseID', DWORD),
		('RestartState', SYNC_STATE),
		('SyncContext', ULONG),
		('PreferredMaximumLength', DWORD),
    )

class NetrDatabaseSync2Response(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('SyncContext', ULONG),
		('DeltaArray', PNETLOGON_DELTA_ENUM_ARRAY),
    )
        

class NetrDatabaseRedo(NDRCALL):
    opnum = 17
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('ChangeLogEntry', UCHAR),
		('ChangeLogEntrySize', DWORD),
    )

class NetrDatabaseRedoResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DeltaArray', PNETLOGON_DELTA_ENUM_ARRAY),
    )
        

class NetrLogonControl2Ex(NDRCALL):
    opnum = 18
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('FunctionCode', DWORD),
		('QueryLevel', DWORD),
		('Data', PNETLOGON_CONTROL_DATA_INFORMATION),
    )

class NetrLogonControl2ExResponse(NDRCALL):
    structure = (
		('Buffer', PNETLOGON_CONTROL_QUERY_INFORMATION),
    )
        

class NetrEnumerateTrustedDomains(NDRCALL):
    opnum = 19
    structure = (
		('ServerName', LOGONSRV_HANDLE),
    )

class NetrEnumerateTrustedDomainsResponse(NDRCALL):
    structure = (
		('DomainNameBuffer', PDOMAIN_NAME_BUFFER),
    )
        

class DsrGetDcName(NDRCALL):
    opnum = 20
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
		('DomainGuid', GUID),
		('SiteGuid', GUID),
		('Flags', ULONG),
    )

class DsrGetDcNameResponse(NDRCALL):
    structure = (
		('DomainControllerInfo', PDOMAIN_CONTROLLER_INFOW),
    )
        

class NetrLogonGetCapabilities(NDRCALL):
    opnum = 21
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('QueryLevel', DWORD),
    )

class NetrLogonGetCapabilitiesResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('ServerCapabilities', PNETLOGON_CAPABILITIES),
    )
        

class NetrLogonSetServiceBits(NDRCALL):
    opnum = 22
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('ServiceBitsOfInterest', DWORD),
		('ServiceBits', DWORD),
    )

class NetrLogonSetServiceBitsResponse(NDRCALL):
    structure = (

    )
        

class NetrLogonGetTrustRid(NDRCALL):
    opnum = 23
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
    )

class NetrLogonGetTrustRidResponse(NDRCALL):
    structure = (
		('Rid', ULONG),
    )
        

class NetrLogonComputeServerDigest(NDRCALL):
    opnum = 24
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('Rid', ULONG),
		('Message', UCHAR),
		('MessageSize', ULONG),
    )

class NetrLogonComputeServerDigestResponse(NDRCALL):
    structure = (
		('NewMessageDigest', CHAR),
		('OldMessageDigest', CHAR),
    )
        

class NetrLogonComputeClientDigest(NDRCALL):
    opnum = 25
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
		('Message', UCHAR),
		('MessageSize', ULONG),
    )

class NetrLogonComputeClientDigestResponse(NDRCALL):
    structure = (
		('NewMessageDigest', CHAR),
		('OldMessageDigest', CHAR),
    )
        

class NetrServerAuthenticate3(NDRCALL):
    opnum = 26
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('ClientCredential', PNETLOGON_CREDENTIAL),
		('NegotiateFlags', ULONG),
    )

class NetrServerAuthenticate3Response(NDRCALL):
    structure = (
		('ServerCredential', PNETLOGON_CREDENTIAL),
		('NegotiateFlags', ULONG),
		('AccountRid', ULONG),
    )
        

class DsrGetDcNameEx(NDRCALL):
    opnum = 27
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
		('DomainName', WCHAR_T),
		('DomainGuid', GUID),
		('SiteName', WCHAR_T),
		('Flags', ULONG),
    )

class DsrGetDcNameExResponse(NDRCALL):
    structure = (
		('DomainControllerInfo', PDOMAIN_CONTROLLER_INFOW),
    )
        

class DsrGetSiteName(NDRCALL):
    opnum = 28
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
    )

class DsrGetSiteNameResponse(NDRCALL):
    structure = (
		('SiteName', WCHAR_T),
    )
        

class NetrLogonGetDomainInfo(NDRCALL):
    opnum = 29
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('Level', DWORD),
		('WkstaBuffer', PNETLOGON_WORKSTATION_INFORMATION),
    )

class NetrLogonGetDomainInfoResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DomBuffer', PNETLOGON_DOMAIN_INFORMATION),
    )
        

class NetrServerPasswordSet2(NDRCALL):
    opnum = 30
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ClearNewPassword', PNL_TRUST_PASSWORD),
    )

class NetrServerPasswordSet2Response(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
    )
        

class NetrServerPasswordGet(NDRCALL):
    opnum = 31
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('AccountType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
    )

class NetrServerPasswordGetResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('EncryptedNtOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
    )
        

class NetrLogonSendToSam(NDRCALL):
    opnum = 32
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('OpaqueBuffer', UCHAR),
		('OpaqueBufferSize', ULONG),
    )

class NetrLogonSendToSamResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
    )
        

class DsrAddressToSiteNamesW(NDRCALL):
    opnum = 33
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
		('EntryCount', DWORD),
		('SocketAddresses', PNL_SOCKET_ADDRESS),
    )

class DsrAddressToSiteNamesWResponse(NDRCALL):
    structure = (
		('SiteNames', PNL_SITE_NAME_ARRAY),
    )
        

class DsrGetDcNameEx2(NDRCALL):
    opnum = 34
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('AllowableAccountControlBits', ULONG),
		('DomainName', WCHAR_T),
		('DomainGuid', GUID),
		('SiteName', WCHAR_T),
		('Flags', ULONG),
    )

class DsrGetDcNameEx2Response(NDRCALL):
    structure = (
		('DomainControllerInfo', PDOMAIN_CONTROLLER_INFOW),
    )
        

class NetrLogonGetTimeServiceParentDomain(NDRCALL):
    opnum = 35
    structure = (
		('ServerName', LOGONSRV_HANDLE),
    )

class NetrLogonGetTimeServiceParentDomainResponse(NDRCALL):
    structure = (
		('DomainName', WCHAR_T),
		('PdcSameSite', INT),
    )
        

class NetrEnumerateTrustedDomainsEx(NDRCALL):
    opnum = 36
    structure = (
		('ServerName', LOGONSRV_HANDLE),
    )

class NetrEnumerateTrustedDomainsExResponse(NDRCALL):
    structure = (
		('Domains', PNETLOGON_TRUSTED_DOMAIN_ARRAY),
    )
        

class DsrAddressToSiteNamesExW(NDRCALL):
    opnum = 37
    structure = (
		('ComputerName', LOGONSRV_HANDLE),
		('EntryCount', DWORD),
		('SocketAddresses', PNL_SOCKET_ADDRESS),
    )

class DsrAddressToSiteNamesExWResponse(NDRCALL):
    structure = (
		('SiteNames', PNL_SITE_NAME_EX_ARRAY),
    )
        

class DsrGetDcSiteCoverageW(NDRCALL):
    opnum = 38
    structure = (
		('ServerName', LOGONSRV_HANDLE),
    )

class DsrGetDcSiteCoverageWResponse(NDRCALL):
    structure = (
		('SiteNames', PNL_SITE_NAME_ARRAY),
    )
        

class NetrLogonSamLogonEx(NDRCALL):
    opnum = 39
    structure = (
		('ContextHandle', HANDLE_T),
		('LogonServer', WCHAR_T),
		('ComputerName', WCHAR_T),
		('LogonLevel', NETLOGON_LOGON_INFO_CLASS),
		('LogonInformation', PNETLOGON_LEVEL),
		('ValidationLevel', NETLOGON_VALIDATION_INFO_CLASS),
		('ExtraFlags', ULONG),
    )

class NetrLogonSamLogonExResponse(NDRCALL):
    structure = (
		('ValidationInformation', PNETLOGON_VALIDATION),
		('Authoritative', UCHAR),
		('ExtraFlags', ULONG),
    )
        

class DsrEnumerateDomainTrusts(NDRCALL):
    opnum = 40
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('Flags', ULONG),
    )

class DsrEnumerateDomainTrustsResponse(NDRCALL):
    structure = (
		('Domains', PNETLOGON_TRUSTED_DOMAIN_ARRAY),
    )
        

class DsrDeregisterDnsHostRecords(NDRCALL):
    opnum = 41
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('DnsDomainName', WCHAR_T),
		('DomainGuid', GUID),
		('DsaGuid', GUID),
		('DnsHostName', WCHAR_T),
    )

class DsrDeregisterDnsHostRecordsResponse(NDRCALL):
    structure = (

    )
        

class NetrServerTrustPasswordsGet(NDRCALL):
    opnum = 42
    structure = (
		('TrustedDcName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
    )

class NetrServerTrustPasswordsGetResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('EncryptedNewOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
		('EncryptedOldOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
    )
        

class DsrGetForestTrustInformation(NDRCALL):
    opnum = 43
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('TrustedDomainName', WCHAR_T),
		('Flags', DWORD),
    )

class DsrGetForestTrustInformationResponse(NDRCALL):
    structure = (
		('ForestTrustInfo', PLSA_FOREST_TRUST_INFORMATION),
    )
        

class NetrGetForestTrustInformation(NDRCALL):
    opnum = 44
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('Flags', DWORD),
    )

class NetrGetForestTrustInformationResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('ForestTrustInfo', PLSA_FOREST_TRUST_INFORMATION),
    )
        

class NetrLogonSamLogonWithFlags(NDRCALL):
    opnum = 45
    structure = (
		('LogonServer', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('LogonLevel', NETLOGON_LOGON_INFO_CLASS),
		('LogonInformation', PNETLOGON_LEVEL),
		('ValidationLevel', NETLOGON_VALIDATION_INFO_CLASS),
		('ExtraFlags', ULONG),
    )

class NetrLogonSamLogonWithFlagsResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('ValidationInformation', PNETLOGON_VALIDATION),
		('Authoritative', UCHAR),
		('ExtraFlags', ULONG),
    )
        

class NetrServerGetTrustInfo(NDRCALL):
    opnum = 46
    structure = (
		('TrustedDcName', LOGONSRV_HANDLE),
		('AccountName', WCHAR_T),
		('SecureChannelType', NETLOGON_SECURE_CHANNEL_TYPE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
    )

class NetrServerGetTrustInfoResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('EncryptedNewOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
		('EncryptedOldOwfPassword', PENCRYPTED_NT_OWF_PASSWORD),
		('TrustInfo', PNL_GENERIC_RPC_DATA),
    )
        

class OpnumUnused47(NDRCALL):
    opnum = 47
    structure = (

    )

class OpnumUnused47Response(NDRCALL):
    structure = (

    )
        

class DsrUpdateReadOnlyServerDnsRecords(NDRCALL):
    opnum = 48
    structure = (
		('ServerName', LOGONSRV_HANDLE),
		('ComputerName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('SiteName', WCHAR_T),
		('DnsTtl', ULONG),
		('DnsNames', PNL_DNS_NAME_INFO_ARRAY),
    )

class DsrUpdateReadOnlyServerDnsRecordsResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('DnsNames', PNL_DNS_NAME_INFO_ARRAY),
    )
        

class NetrChainSetClientAttributes(NDRCALL):
    opnum = 49
    structure = (
		('PrimaryName', LOGONSRV_HANDLE),
		('ChainedFromServerName', WCHAR_T),
		('ChainedForClientName', WCHAR_T),
		('Authenticator', PNETLOGON_AUTHENTICATOR),
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('dwInVersion', DWORD),
		('pmsgIn', NL_IN_CHAIN_SET_CLIENT_ATTRIBUTES),
		('pdwOutVersion', DWORD),
		('pmsgOut', NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES),
    )

class NetrChainSetClientAttributesResponse(NDRCALL):
    structure = (
		('ReturnAuthenticator', PNETLOGON_AUTHENTICATOR),
		('pdwOutVersion', DWORD),
		('pmsgOut', NL_OUT_CHAIN_SET_CLIENT_ATTRIBUTES),
    )
        
OPNUMS = {
0 : (NetrLogonUasLogon,NetrLogonUasLogonResponse),
1 : (NetrLogonUasLogoff,NetrLogonUasLogoffResponse),
2 : (NetrLogonSamLogon,NetrLogonSamLogonResponse),
3 : (NetrLogonSamLogoff,NetrLogonSamLogoffResponse),
4 : (NetrServerReqChallenge,NetrServerReqChallengeResponse),
5 : (NetrServerAuthenticate,NetrServerAuthenticateResponse),
6 : (NetrServerPasswordSet,NetrServerPasswordSetResponse),
7 : (NetrDatabaseDeltas,NetrDatabaseDeltasResponse),
8 : (NetrDatabaseSync,NetrDatabaseSyncResponse),
9 : (NetrAccountDeltas,NetrAccountDeltasResponse),
10 : (NetrAccountSync,NetrAccountSyncResponse),
11 : (NetrGetDCName,NetrGetDCNameResponse),
12 : (NetrLogonControl,NetrLogonControlResponse),
13 : (NetrGetAnyDCName,NetrGetAnyDCNameResponse),
14 : (NetrLogonControl2,NetrLogonControl2Response),
15 : (NetrServerAuthenticate2,NetrServerAuthenticate2Response),
16 : (NetrDatabaseSync2,NetrDatabaseSync2Response),
17 : (NetrDatabaseRedo,NetrDatabaseRedoResponse),
18 : (NetrLogonControl2Ex,NetrLogonControl2ExResponse),
19 : (NetrEnumerateTrustedDomains,NetrEnumerateTrustedDomainsResponse),
20 : (DsrGetDcName,DsrGetDcNameResponse),
21 : (NetrLogonGetCapabilities,NetrLogonGetCapabilitiesResponse),
22 : (NetrLogonSetServiceBits,NetrLogonSetServiceBitsResponse),
23 : (NetrLogonGetTrustRid,NetrLogonGetTrustRidResponse),
24 : (NetrLogonComputeServerDigest,NetrLogonComputeServerDigestResponse),
25 : (NetrLogonComputeClientDigest,NetrLogonComputeClientDigestResponse),
26 : (NetrServerAuthenticate3,NetrServerAuthenticate3Response),
27 : (DsrGetDcNameEx,DsrGetDcNameExResponse),
28 : (DsrGetSiteName,DsrGetSiteNameResponse),
29 : (NetrLogonGetDomainInfo,NetrLogonGetDomainInfoResponse),
30 : (NetrServerPasswordSet2,NetrServerPasswordSet2Response),
31 : (NetrServerPasswordGet,NetrServerPasswordGetResponse),
32 : (NetrLogonSendToSam,NetrLogonSendToSamResponse),
33 : (DsrAddressToSiteNamesW,DsrAddressToSiteNamesWResponse),
34 : (DsrGetDcNameEx2,DsrGetDcNameEx2Response),
35 : (NetrLogonGetTimeServiceParentDomain,NetrLogonGetTimeServiceParentDomainResponse),
36 : (NetrEnumerateTrustedDomainsEx,NetrEnumerateTrustedDomainsExResponse),
37 : (DsrAddressToSiteNamesExW,DsrAddressToSiteNamesExWResponse),
38 : (DsrGetDcSiteCoverageW,DsrGetDcSiteCoverageWResponse),
39 : (NetrLogonSamLogonEx,NetrLogonSamLogonExResponse),
40 : (DsrEnumerateDomainTrusts,DsrEnumerateDomainTrustsResponse),
41 : (DsrDeregisterDnsHostRecords,DsrDeregisterDnsHostRecordsResponse),
42 : (NetrServerTrustPasswordsGet,NetrServerTrustPasswordsGetResponse),
43 : (DsrGetForestTrustInformation,DsrGetForestTrustInformationResponse),
44 : (NetrGetForestTrustInformation,NetrGetForestTrustInformationResponse),
45 : (NetrLogonSamLogonWithFlags,NetrLogonSamLogonWithFlagsResponse),
46 : (NetrServerGetTrustInfo,NetrServerGetTrustInfoResponse),
47 : (OpnumUnused47,OpnumUnused47Response),
48 : (DsrUpdateReadOnlyServerDnsRecords,DsrUpdateReadOnlyServerDnsRecordsResponse),
49 : (NetrChainSetClientAttributes,NetrChainSetClientAttributesResponse),
}

