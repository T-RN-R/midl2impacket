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
	align = 1
	structure = 		(		('dwLowDateTime', DWORD), 		('dwHighDateTime', DWORD))
class PFILETIME(NDRPOINTER):
	referent = (
			('Data', FILETIME)
		)
class LPFILETIME(NDRPOINTER):
	referent = (
			('Data', FILETIME)
		)
class GUID(NDRSTRUCT):
	align = 1
	structure = (
			('Data1', UNSIGNED_LONG),
			('Data2', UNSIGNED_SHORT),
			('Data3', UNSIGNED_SHORT),
			('Data4', BYTE)
		)
UUID = GUID
class PGUID(NDRPOINTER):
	referent = (
			('Data', GUID)
		)
class LARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			('QuadPart', SIGNED___INT64)
		)
class PLARGE_INTEGER(NDRPOINTER):
	referent = (
			('Data', LARGE_INTEGER)
		)
class EVENT_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			('Id', USHORT),
			('Version', UCHAR),
			('Channel', UCHAR),
			('Level', UCHAR),
			('Opcode', UCHAR),
			('Task', USHORT),
			('Keyword', ULONGLONG)
		)
class PEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', EVENT_DESCRIPTOR)
		)
class PCEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', EVENT_DESCRIPTOR)
		)
class S0(NDRSTRUCT):
	align = 1
	structure = 		(		('KernelTime', ULONG), 		('UserTime', ULONG))
class U0(NDRUNION):
	union = {1 : 		('s0', S0),2 : 		('ProcessorTime', ULONG64)}
class EVENT_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			('Size', USHORT),
			('HeaderType', USHORT),
			('Flags', USHORT),
			('EventProperty', USHORT),
			('ThreadId', ULONG),
			('ProcessId', ULONG),
			('TimeStamp', LARGE_INTEGER),
			('ProviderId', GUID),
			('EventDescriptor', EVENT_DESCRIPTOR),
			('u0', U0),
			('ActivityId', GUID)
		)
class PEVENT_HEADER(NDRPOINTER):
	referent = (
			('Data', EVENT_HEADER)
		)
LCID = DWORD
class LUID(NDRSTRUCT):
	align = 1
	structure = 		(		('LowPart', DWORD), 		('HighPart', LONG))
class PLUID(NDRPOINTER):
	referent = (
			('Data', LUID)
		)
class MULTI_SZ(NDRSTRUCT):
	align = 1
	structure = 		(		('Value', WCHAR_T), 		('nChar', DWORD))
class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
	item = WCHAR
class PTR_UNSIGNED_SHORT(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_SHORT)
		)
class UNSIGNED_SHORT(NDRSTRUCT):
	align = 1
	structure = (
			('Length', UNSIGNED_SHORT),
			('MaximumLength', UNSIGNED_SHORT),
			('Buffer', PTR_UNSIGNED_SHORT)
		)
class SERVER_INFO_100(NDRSTRUCT):
	align = 1
	structure = 		(		('sv100_platform_id', DWORD), 		('sv100_name', WCHAR_T))
class PSERVER_INFO_100(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_100)
		)
class LPSERVER_INFO_100(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_100)
		)
class SERVER_INFO_101(NDRSTRUCT):
	align = 1
	structure = (
			('sv101_platform_id', DWORD),
			('sv101_name', WCHAR_T),
			('sv101_version_major', DWORD),
			('sv101_version_minor', DWORD),
			('sv101_version_type', DWORD),
			('sv101_comment', WCHAR_T)
		)
class PSERVER_INFO_101(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_101)
		)
class LPSERVER_INFO_101(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_101)
		)
class SYSTEMTIME(NDRSTRUCT):
	align = 1
	structure = (
			('wYear', WORD),
			('wMonth', WORD),
			('wDayOfWeek', WORD),
			('wDay', WORD),
			('wHour', WORD),
			('wMinute', WORD),
			('wSecond', WORD),
			('wMilliseconds', WORD)
		)
class PSYSTEMTIME(NDRPOINTER):
	referent = (
			('Data', SYSTEMTIME)
		)
class UINT128(NDRSTRUCT):
	align = 1
	structure = 		(		('lower', UINT64), 		('upper', UINT64))
class PUINT128(NDRPOINTER):
	referent = (
			('Data', UINT128)
		)
class ULARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			('QuadPart', UNSIGNED___INT64)
		)
class PULARGE_INTEGER(NDRPOINTER):
	referent = (
			('Data', ULARGE_INTEGER)
		)
class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
	align = 1
	structure = (
			('Value', BYTE)
		)
ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK
class OBJECT_TYPE_LIST(NDRSTRUCT):
	align = 1
	structure = (
			('Level', WORD),
			('Remaining', ACCESS_MASK),
			('ObjectType', GUID)
		)
class POBJECT_TYPE_LIST(NDRPOINTER):
	referent = (
			('Data', OBJECT_TYPE_LIST)
		)
class ACE_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			('AceType', UCHAR),
			('AceFlags', UCHAR),
			('AceSize', USHORT)
		)
class PACE_HEADER(NDRPOINTER):
	referent = (
			('Data', ACE_HEADER)
		)
class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
	align = 1
	structure = (
			('Header', ACE_HEADER),
			('Mask', ACCESS_MASK),
			('SidStart', DWORD)
		)
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
	referent = (
			('Data', SYSTEM_MANDATORY_LABEL_ACE)
		)
class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
	align = 1
	structure = (
			('Policy', DWORD)
		)
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
	referent = (
			('Data', TOKEN_MANDATORY_POLICY)
		)
class MANDATORY_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			('AllowedAccess', ACCESS_MASK),
			('WriteAllowed', BOOLEAN),
			('ReadAllowed', BOOLEAN),
			('ExecuteAllowed', BOOLEAN),
			('MandatoryPolicy', TOKEN_MANDATORY_POLICY)
		)
class PMANDATORY_INFORMATION(NDRPOINTER):
	referent = (
			('Data', MANDATORY_INFORMATION)
		)
class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
	align = 1
	structure = 		(		('Length', DWORD), 		('OctetString', BYTE))
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
	referent = (
			('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE)
		)
class VALUES(NDRUNION):
	union = {1 : 		('pInt64', PLONG64),2 : 		('pUint64', PDWORD64),3 : 		('ppString', PWSTR),4 : 		('pOctetString', PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE)}
class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
	align = 1
	structure = (
			('Name', DWORD),
			('ValueType', WORD),
			('Reserved', WORD),
			('Flags', DWORD),
			('ValueCount', DWORD),
			('Values', VALUES)
		)
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
	referent = (
			('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1)
		)
SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD
class RPC_SID(NDRSTRUCT):
	align = 1
	structure = (
			('Revision', UNSIGNED_CHAR),
			('SubAuthorityCount', UNSIGNED_CHAR),
			('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),
			('SubAuthority', UNSIGNED_LONG)
		)
class PRPC_SID(NDRPOINTER):
	referent = (
			('Data', RPC_SID)
		)
class PSID(NDRPOINTER):
	referent = (
			('Data', RPC_SID)
		)
class ACL(NDRSTRUCT):
	align = 1
	structure = (
			('AclRevision', UNSIGNED_CHAR),
			('Sbz1', UNSIGNED_CHAR),
			('AclSize', UNSIGNED_SHORT),
			('AceCount', UNSIGNED_SHORT),
			('Sbz2', UNSIGNED_SHORT)
		)
class PACL(NDRPOINTER):
	referent = (
			('Data', ACL)
		)
class SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			('Revision', UCHAR),
			('Sbz1', UCHAR),
			('Control', USHORT),
			('Owner', PSID),
			('Group', PSID),
			('Sacl', PACL),
			('Dacl', PACL)
		)
class PSECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', SECURITY_DESCRIPTOR)
		)
#################################################################################
#"ms-dcom.idl"
#################################################################################
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
	structure = 		(		('dwLowDateTime', DWORD), 		('dwHighDateTime', DWORD))
class PFILETIME(NDRPOINTER):
	referent = (
			('Data', FILETIME)
		)
class LPFILETIME(NDRPOINTER):
	referent = (
			('Data', FILETIME)
		)
class GUID(NDRSTRUCT):
	align = 1
	structure = (
			('Data1', UNSIGNED_LONG),
			('Data2', UNSIGNED_SHORT),
			('Data3', UNSIGNED_SHORT),
			('Data4', BYTE)
		)
UUID = GUID
class PGUID(NDRPOINTER):
	referent = (
			('Data', GUID)
		)
class LARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			('QuadPart', SIGNED___INT64)
		)
class PLARGE_INTEGER(NDRPOINTER):
	referent = (
			('Data', LARGE_INTEGER)
		)
class EVENT_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			('Id', USHORT),
			('Version', UCHAR),
			('Channel', UCHAR),
			('Level', UCHAR),
			('Opcode', UCHAR),
			('Task', USHORT),
			('Keyword', ULONGLONG)
		)
class PEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', EVENT_DESCRIPTOR)
		)
class PCEVENT_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', EVENT_DESCRIPTOR)
		)
class S0(NDRSTRUCT):
	align = 1
	structure = 		(		('KernelTime', ULONG), 		('UserTime', ULONG))
class U0(NDRUNION):
	union = {1 : 		('s0', S0),2 : 		('ProcessorTime', ULONG64)}
class EVENT_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			('Size', USHORT),
			('HeaderType', USHORT),
			('Flags', USHORT),
			('EventProperty', USHORT),
			('ThreadId', ULONG),
			('ProcessId', ULONG),
			('TimeStamp', LARGE_INTEGER),
			('ProviderId', GUID),
			('EventDescriptor', EVENT_DESCRIPTOR),
			('u0', U0),
			('ActivityId', GUID)
		)
class PEVENT_HEADER(NDRPOINTER):
	referent = (
			('Data', EVENT_HEADER)
		)
LCID = DWORD
class LUID(NDRSTRUCT):
	align = 1
	structure = 		(		('LowPart', DWORD), 		('HighPart', LONG))
class PLUID(NDRPOINTER):
	referent = (
			('Data', LUID)
		)
class MULTI_SZ(NDRSTRUCT):
	align = 1
	structure = 		(		('Value', WCHAR_T), 		('nChar', DWORD))
class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
	item = WCHAR
class PTR_UNSIGNED_SHORT(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_SHORT)
		)
class UNSIGNED_SHORT(NDRSTRUCT):
	align = 1
	structure = (
			('Length', UNSIGNED_SHORT),
			('MaximumLength', UNSIGNED_SHORT),
			('Buffer', PTR_UNSIGNED_SHORT)
		)
class SERVER_INFO_100(NDRSTRUCT):
	align = 1
	structure = 		(		('sv100_platform_id', DWORD), 		('sv100_name', WCHAR_T))
class PSERVER_INFO_100(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_100)
		)
class LPSERVER_INFO_100(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_100)
		)
class SERVER_INFO_101(NDRSTRUCT):
	align = 1
	structure = (
			('sv101_platform_id', DWORD),
			('sv101_name', WCHAR_T),
			('sv101_version_major', DWORD),
			('sv101_version_minor', DWORD),
			('sv101_version_type', DWORD),
			('sv101_comment', WCHAR_T)
		)
class PSERVER_INFO_101(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_101)
		)
class LPSERVER_INFO_101(NDRPOINTER):
	referent = (
			('Data', SERVER_INFO_101)
		)
class SYSTEMTIME(NDRSTRUCT):
	align = 1
	structure = (
			('wYear', WORD),
			('wMonth', WORD),
			('wDayOfWeek', WORD),
			('wDay', WORD),
			('wHour', WORD),
			('wMinute', WORD),
			('wSecond', WORD),
			('wMilliseconds', WORD)
		)
class PSYSTEMTIME(NDRPOINTER):
	referent = (
			('Data', SYSTEMTIME)
		)
class UINT128(NDRSTRUCT):
	align = 1
	structure = 		(		('lower', UINT64), 		('upper', UINT64))
class PUINT128(NDRPOINTER):
	referent = (
			('Data', UINT128)
		)
class ULARGE_INTEGER(NDRSTRUCT):
	align = 1
	structure = (
			('QuadPart', UNSIGNED___INT64)
		)
class PULARGE_INTEGER(NDRPOINTER):
	referent = (
			('Data', ULARGE_INTEGER)
		)
class RPC_SID_IDENTIFIER_AUTHORITY(NDRSTRUCT):
	align = 1
	structure = (
			('Value', BYTE)
		)
ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK
class OBJECT_TYPE_LIST(NDRSTRUCT):
	align = 1
	structure = (
			('Level', WORD),
			('Remaining', ACCESS_MASK),
			('ObjectType', GUID)
		)
class POBJECT_TYPE_LIST(NDRPOINTER):
	referent = (
			('Data', OBJECT_TYPE_LIST)
		)
class ACE_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			('AceType', UCHAR),
			('AceFlags', UCHAR),
			('AceSize', USHORT)
		)
class PACE_HEADER(NDRPOINTER):
	referent = (
			('Data', ACE_HEADER)
		)
class SYSTEM_MANDATORY_LABEL_ACE(NDRSTRUCT):
	align = 1
	structure = (
			('Header', ACE_HEADER),
			('Mask', ACCESS_MASK),
			('SidStart', DWORD)
		)
class PSYSTEM_MANDATORY_LABEL_ACE(NDRPOINTER):
	referent = (
			('Data', SYSTEM_MANDATORY_LABEL_ACE)
		)
class TOKEN_MANDATORY_POLICY(NDRSTRUCT):
	align = 1
	structure = (
			('Policy', DWORD)
		)
class PTOKEN_MANDATORY_POLICY(NDRPOINTER):
	referent = (
			('Data', TOKEN_MANDATORY_POLICY)
		)
class MANDATORY_INFORMATION(NDRSTRUCT):
	align = 1
	structure = (
			('AllowedAccess', ACCESS_MASK),
			('WriteAllowed', BOOLEAN),
			('ReadAllowed', BOOLEAN),
			('ExecuteAllowed', BOOLEAN),
			('MandatoryPolicy', TOKEN_MANDATORY_POLICY)
		)
class PMANDATORY_INFORMATION(NDRPOINTER):
	referent = (
			('Data', MANDATORY_INFORMATION)
		)
class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRSTRUCT):
	align = 1
	structure = 		(		('Length', DWORD), 		('OctetString', BYTE))
class PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NDRPOINTER):
	referent = (
			('Data', CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE)
		)
class VALUES(NDRUNION):
	union = {1 : 		('pInt64', PLONG64),2 : 		('pUint64', PDWORD64),3 : 		('ppString', PWSTR),4 : 		('pOctetString', PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE)}
class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRSTRUCT):
	align = 1
	structure = (
			('Name', DWORD),
			('ValueType', WORD),
			('Reserved', WORD),
			('Flags', DWORD),
			('ValueCount', DWORD),
			('Values', VALUES)
		)
class PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NDRPOINTER):
	referent = (
			('Data', CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1)
		)
SECURITY_INFORMATION = DWORD
PSECURITY_INFORMATION = DWORD
class RPC_SID(NDRSTRUCT):
	align = 1
	structure = (
			('Revision', UNSIGNED_CHAR),
			('SubAuthorityCount', UNSIGNED_CHAR),
			('IdentifierAuthority', RPC_SID_IDENTIFIER_AUTHORITY),
			('SubAuthority', UNSIGNED_LONG)
		)
class PRPC_SID(NDRPOINTER):
	referent = (
			('Data', RPC_SID)
		)
class PSID(NDRPOINTER):
	referent = (
			('Data', RPC_SID)
		)
class ACL(NDRSTRUCT):
	align = 1
	structure = (
			('AclRevision', UNSIGNED_CHAR),
			('Sbz1', UNSIGNED_CHAR),
			('AclSize', UNSIGNED_SHORT),
			('AceCount', UNSIGNED_SHORT),
			('Sbz2', UNSIGNED_SHORT)
		)
class PACL(NDRPOINTER):
	referent = (
			('Data', ACL)
		)
class SECURITY_DESCRIPTOR(NDRSTRUCT):
	align = 1
	structure = (
			('Revision', UCHAR),
			('Sbz1', UCHAR),
			('Control', USHORT),
			('Owner', PSID),
			('Group', PSID),
			('Sacl', PACL),
			('Dacl', PACL)
		)
class PSECURITY_DESCRIPTOR(NDRPOINTER):
	referent = (
			('Data', SECURITY_DESCRIPTOR)
		)
#################################################################################
#TYPEDEFS
#################################################################################
CLSID = GUID
IID = GUID
ID = UNSIGNED_HYPER
OXID = UNSIGNED_HYPER
OID = UNSIGNED_HYPER
SETID = UNSIGNED_HYPER
IPID = GUID
CID = GUID
REFIPID = REFGUID
class COMVERSION(NDRSTRUCT):
	align = 1
	structure = 		(		('MajorVersion', UNSIGNED_SHORT), 		('MinorVersion', UNSIGNED_SHORT))
class ORPC_EXTENT(NDRSTRUCT):
	align = 1
	structure = (
			('id', GUID),
			('size', UNSIGNED_LONG),
			('data', BYTE)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = ORPC_EXTENT
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = (
			('size', UNSIGNED_LONG),
			('reserved', UNSIGNED_LONG),
			('extent', PTR_UNSIGNED_LONG)
		)
class ORPCTHIS(NDRSTRUCT):
	align = 1
	structure = (
			('version', COMVERSION),
			('flags', UNSIGNED_LONG),
			('reserved1', UNSIGNED_LONG),
			('cid', CID),
			('extensions', ORPC_EXTENT_ARRAY)
		)
class ORPCTHAT(NDRSTRUCT):
	align = 1
	structure = 		(		('flags', UNSIGNED_LONG), 		('extensions', ORPC_EXTENT_ARRAY))
class DUALSTRINGARRAY(NDRSTRUCT):
	align = 1
	structure = (
			('wNumEntries', UNSIGNED_SHORT),
			('wSecurityOffset', UNSIGNED_SHORT),
			('aStringArray', UNSIGNED_SHORT)
		)
CPFLAG_PROPAGATE = 1
CPFLAG_EXPOSE = 2
CPFLAG_ENVOY = 4
class MINTERFACEPOINTER(NDRSTRUCT):
	align = 1
	structure = 		(		('ulCntData', UNSIGNED_LONG), 		('abData', BYTE))
PMINTERFACEPOINTER = MINTERFACEPOINTER
class ERROROBJECTDATA(NDRSTRUCT):
	align = 1
	structure = (
			('dwVersion', DWORD),
			('dwHelpContext', DWORD),
			('iid', IID),
			('pszSource', WCHAR_T),
			('pszDescription', WCHAR_T),
			('pszHelpFile', WCHAR_T)
		)
class STDOBJREF(NDRSTRUCT):
	align = 1
	structure = (
			('flags', UNSIGNED_LONG),
			('cPublicRefs', UNSIGNED_LONG),
			('oxid', OXID),
			('oid', OID),
			('ipid', IPID)
		)
class REMQIRESULT(NDRSTRUCT):
	align = 1
	structure = 		(		('hResult', HRESULT), 		('std', STDOBJREF))
class REMINTERFACEREF(NDRSTRUCT):
	align = 1
	structure = (
			('ipid', IPID),
			('cPublicRefs', UNSIGNED_LONG),
			('cPrivateRefs', UNSIGNED_LONG)
		)
PREMQIRESULT = REMQIRESULT
PMINTERFACEPOINTERINTERNAL = MINTERFACEPOINTER
class COSERVERINFO(NDRSTRUCT):
	align = 1
	structure = (
			('dwReserved1', DWORD),
			('pwszName', WCHAR_T),
			('pdwReserved', DWORD),
			('dwReserved2', DWORD)
		)
class DATA_UNSIGNED_SHORT(NDRUniConformantArray):
	item = UNSIGNED_SHORT
class PTR_UNSIGNED_SHORT(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_SHORT)
		)
class UNSIGNED_SHORT(NDRSTRUCT):
	align = 1
	structure = (
			('ClientImpLevel', DWORD),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('pRequestedProtseqs', PTR_UNSIGNED_SHORT)
		)
class CUSTOMREMOTE_REPLY_SCM_INFO(NDRSTRUCT):
	align = 1
	structure = (
			('Oxid', OXID),
			('pdsaOxidBindings', DUALSTRINGARRAY),
			('ipidRemUnknown', IPID),
			('authnHint', DWORD),
			('serverVersion', COMVERSION)
		)
class DATA_COMVERSION(NDRUniConformantArray):
	item = IID
class PTR_COMVERSION(NDRPOINTER):
	referent = (
			('Data', DATA_COMVERSION)
		)
class COMVERSION(NDRSTRUCT):
	align = 1
	structure = (
			('classId', CLSID),
			('classCtx', DWORD),
			('actvflags', DWORD),
			('fIsSurrogate', LONG),
			('cIID', DWORD),
			('instFlag', DWORD),
			('pIID', PTR_DWORD),
			('thisSize', DWORD),
			('clientCOMVersion', COMVERSION)
		)
class LOCATIONINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			('machineName', WCHAR_T),
			('processId', DWORD),
			('apartmentId', DWORD),
			('contextId', DWORD)
		)
class ACTIVATIONCONTEXTINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			('clientOK', LONG),
			('bReserved1', LONG),
			('dwReserved1', DWORD),
			('dwReserved2', DWORD),
			('pIFDClientCtx', MINTERFACEPOINTER),
			('pIFDPrototypeCtx', MINTERFACEPOINTER)
		)
class DATA_DWORD(NDRUniConformantArray):
	item = DWORD
class PTR_DWORD(NDRPOINTER):
	referent = (
			('Data', DATA_DWORD)
		)
class DWORD(NDRSTRUCT):
	align = 1
	structure = (
			('totalSize', DWORD),
			('headerSize', DWORD),
			('dwReserved', DWORD),
			('destCtx', DWORD),
			('cIfs', DWORD),
			('classInfoClsid', CLSID),
			('pclsid', CLSID),
			('pSizes', PTR_CLSID),
			('pdwReserved', DWORD)
		)
class DATA_HRESULT(NDRUniConformantArray):
	item = MINTERFACEPOINTER
class PTR_HRESULT(NDRPOINTER):
	referent = (
			('Data', DATA_HRESULT)
		)
class HRESULT(NDRSTRUCT):
	align = 1
	structure = (
			('cIfs', DWORD),
			('piid', IID),
			('phresults', HRESULT),
			('ppIntfData', PTR_HRESULT)
		)
class SECURITYINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			('dwAuthnFlags', DWORD),
			('pServerInfo', COSERVERINFO),
			('pdwReserved', DWORD)
		)
class SCMREQUESTINFODATA(NDRSTRUCT):
	align = 1
	structure = 		(		('pdwReserved', DWORD), 		('remoteRequest', CUSTOMREMOTE_REQUEST_SCM_INFO))
class SCMREPLYINFODATA(NDRSTRUCT):
	align = 1
	structure = 		(		('pdwReserved', DWORD), 		('remoteReply', CUSTOMREMOTE_REPLY_SCM_INFO))
class INSTANCEINFODATA(NDRSTRUCT):
	align = 1
	structure = (
			('fileName', WCHAR_T),
			('mode', DWORD),
			('ifdROT', MINTERFACEPOINTER),
			('ifdStg', MINTERFACEPOINTER)
		)
SPD_FLAG_USE_CONSOLE_SESSION = 1
SPD_FLAG_USE_DEFAULT_AUTHN_LVL = 2
class SPECIALPROPERTIESDATA(NDRSTRUCT):
	align = 1
	structure = (
			('dwSessionId', UNSIGNED_LONG),
			('fRemoteThisSessionId', LONG),
			('fClientImpersonating', LONG),
			('fPartitionIDPresent', LONG),
			('dwDefaultAuthnLvl', DWORD),
			('guidPartition', GUID),
			('dwPRTFlags', DWORD),
			('dwOrigClsctx', DWORD),
			('dwFlags', DWORD),
			('Reserved1', DWORD),
			('Reserved2', UNSIGNED___INT64),
			('Reserved3', DWORD)
		)
class SPECIALPROPERTIESDATA_ALTERNATE(NDRSTRUCT):
	align = 1
	structure = (
			('dwSessionId', UNSIGNED_LONG),
			('fRemoteThisSessionId', LONG),
			('fClientImpersonating', LONG),
			('fPartitionIDPresent', LONG),
			('dwDefaultAuthnLvl', DWORD),
			('guidPartition', GUID),
			('dwPRTFlags', DWORD),
			('dwOrigClsctx', DWORD),
			('dwFlags', DWORD),
			('Reserved3', DWORD)
		)
#################################################################################
#CONSTANTS
#################################################################################
MIN_ACTPROP_LIMIT = 1
MAX_ACTPROP_LIMIT = 10
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#IActivation Definition
#################################################################################
MSRPC_UUID_IACTIVATION = uuidtup_to_bin(('4d9f4ab8-7d1c-11cf-861e-0020af6e7c57','0.0'))
MAX_REQUESTED_INTERFACES = CONST_UNSIGNED_LONG
MAX_REQUESTED_PROTSEQS = CONST_UNSIGNED_LONG
class RemoteActivation(NDRCALL):
	OPNUM = 0
	structure = (
			('hRpc', HANDLE_T),
			('ORPCthis', ORPCTHIS),
			('Clsid', GUID),
			('pwszObjectName', WCHAR_T),
			('pObjectStorage', MINTERFACEPOINTER),
			('ClientImpLevel', DWORD),
			('Mode', DWORD),
			('Interfaces', DWORD),
			('pIIDs', IID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('aRequestedProtseqs', UNSIGNED_SHORT)
		)
class RemoteActivationResponse(NDRCALL):
	structure = (
			('hRpc', HANDLE_T),
			('ORPCthis', ORPCTHIS),
			('Clsid', GUID),
			('pwszObjectName', WCHAR_T),
			('pObjectStorage', MINTERFACEPOINTER),
			('ClientImpLevel', DWORD),
			('Mode', DWORD),
			('Interfaces', DWORD),
			('pIIDs', IID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('aRequestedProtseqs', UNSIGNED_SHORT)
		)
OPNUMS = {0 : 	(RemoteActivation, RemoteActivationResponse)}
#################################################################################
#IRemoteSCMActivator Definition
#################################################################################
MSRPC_UUID_IREMOTESCMACTIVATOR = uuidtup_to_bin(('000001A0-0000-0000-C000-000000000046','0.0'))
class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (
		)
class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (
		)
class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum2NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum2NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class RemoteGetClassObject(NDRCALL):
	OPNUM = 3
	structure = (
			('rpc', HANDLE_T),
			('orpcthis', ORPCTHIS),
			('pActProperties', MINTERFACEPOINTER)
		)
class RemoteGetClassObjectResponse(NDRCALL):
	structure = (
			('rpc', HANDLE_T),
			('orpcthis', ORPCTHIS),
			('pActProperties', MINTERFACEPOINTER)
		)
class RemoteCreateInstance(NDRCALL):
	OPNUM = 4
	structure = (
			('rpc', HANDLE_T),
			('orpcthis', ORPCTHIS),
			('pUnkOuter', MINTERFACEPOINTER),
			('pActProperties', MINTERFACEPOINTER)
		)
class RemoteCreateInstanceResponse(NDRCALL):
	structure = (
			('rpc', HANDLE_T),
			('orpcthis', ORPCTHIS),
			('pUnkOuter', MINTERFACEPOINTER),
			('pActProperties', MINTERFACEPOINTER)
		)
OPNUMS = {0 : 	(Opnum0NotUsedOnWire, Opnum0NotUsedOnWireResponse),1 : 	(Opnum1NotUsedOnWire, Opnum1NotUsedOnWireResponse),2 : 	(Opnum2NotUsedOnWire, Opnum2NotUsedOnWireResponse),3 : 	(RemoteGetClassObject, RemoteGetClassObjectResponse),4 : 	(RemoteCreateInstance, RemoteCreateInstanceResponse)}
#################################################################################
#IObjectExporter Definition
#################################################################################
MSRPC_UUID_IOBJECTEXPORTER = uuidtup_to_bin(('99fcfec4-5260-101b-bbcb-00aa0021347a','0.0'))
class ResolveOxid(NDRCALL):
	OPNUM = 0
	structure = (
			('hRpc', HANDLE_T),
			('pOxid', OXID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('arRequestedProtseqs', UNSIGNED_SHORT)
		)
class ResolveOxidResponse(NDRCALL):
	structure = (
			('hRpc', HANDLE_T),
			('pOxid', OXID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('arRequestedProtseqs', UNSIGNED_SHORT)
		)
class SimplePing(NDRCALL):
	OPNUM = 1
	structure = 		(		('hRpc', HANDLE_T), 		('pSetId', SETID))
class SimplePingResponse(NDRCALL):
	structure = 		(		('hRpc', HANDLE_T), 		('pSetId', SETID))
class ComplexPing(NDRCALL):
	OPNUM = 2
	structure = (
			('hRpc', HANDLE_T),
			('pSetId', SETID),
			('SequenceNum', UNSIGNED_SHORT),
			('cAddToSet', UNSIGNED_SHORT),
			('cDelFromSet', UNSIGNED_SHORT),
			('AddToSet', OID),
			('DelFromSet', OID)
		)
class ComplexPingResponse(NDRCALL):
	structure = (
			('hRpc', HANDLE_T),
			('pSetId', SETID),
			('SequenceNum', UNSIGNED_SHORT),
			('cAddToSet', UNSIGNED_SHORT),
			('cDelFromSet', UNSIGNED_SHORT),
			('AddToSet', OID),
			('DelFromSet', OID)
		)
class ServerAlive(NDRCALL):
	OPNUM = 3
	structure = (
			('hRpc', HANDLE_T)
		)
class ServerAliveResponse(NDRCALL):
	structure = (
			('hRpc', HANDLE_T)
		)
class ResolveOxid2(NDRCALL):
	OPNUM = 4
	structure = (
			('hRpc', HANDLE_T),
			('pOxid', OXID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('arRequestedProtseqs', UNSIGNED_SHORT)
		)
class ResolveOxid2Response(NDRCALL):
	structure = (
			('hRpc', HANDLE_T),
			('pOxid', OXID),
			('cRequestedProtseqs', UNSIGNED_SHORT),
			('arRequestedProtseqs', UNSIGNED_SHORT)
		)
class ServerAlive2(NDRCALL):
	OPNUM = 5
	structure = (
			('hRpc', HANDLE_T)
		)
class ServerAlive2Response(NDRCALL):
	structure = (
			('hRpc', HANDLE_T)
		)
OPNUMS = {0 : 	(ResolveOxid, ResolveOxidResponse),1 : 	(SimplePing, SimplePingResponse),2 : 	(ComplexPing, ComplexPingResponse),3 : 	(ServerAlive, ServerAliveResponse),4 : 	(ResolveOxid2, ResolveOxid2Response),5 : 	(ServerAlive2, ServerAlive2Response)}
#################################################################################
#IUnknown Definition
#################################################################################
MSRPC_UUID_IUNKNOWN = uuidtup_to_bin(('00000000-0000-0000-C000-000000000046','0.0'))
class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (
		)
class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum1NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (
		)
class Opnum1NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum2NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum2NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Opnum0NotUsedOnWire, Opnum0NotUsedOnWireResponse),1 : 	(Opnum1NotUsedOnWire, Opnum1NotUsedOnWireResponse),2 : 	(Opnum2NotUsedOnWire, Opnum2NotUsedOnWireResponse)}
#################################################################################
#IRemUnknown Definition
#################################################################################
MSRPC_UUID_IREMUNKNOWN = uuidtup_to_bin(('00000131-0000-0000-C000-000000000046','0.0'))
class RemQueryInterface(NDRCALL):
	OPNUM = 0
	structure = (
			('ripid', REFIPID),
			('cRefs', UNSIGNED_LONG),
			('cIids', UNSIGNED_SHORT),
			('iids', IID)
		)
class RemQueryInterfaceResponse(NDRCALL):
	structure = (
			('ripid', REFIPID),
			('cRefs', UNSIGNED_LONG),
			('cIids', UNSIGNED_SHORT),
			('iids', IID)
		)
class RemAddRef(NDRCALL):
	OPNUM = 1
	structure = 		(		('cInterfaceRefs', UNSIGNED_SHORT), 		('InterfaceRefs', REMINTERFACEREF))
class RemAddRefResponse(NDRCALL):
	structure = 		(		('cInterfaceRefs', UNSIGNED_SHORT), 		('InterfaceRefs', REMINTERFACEREF))
class RemRelease(NDRCALL):
	OPNUM = 2
	structure = 		(		('cInterfaceRefs', UNSIGNED_SHORT), 		('InterfaceRefs', REMINTERFACEREF))
class RemReleaseResponse(NDRCALL):
	structure = 		(		('cInterfaceRefs', UNSIGNED_SHORT), 		('InterfaceRefs', REMINTERFACEREF))
OPNUMS = {0 : 	(RemQueryInterface, RemQueryInterfaceResponse),1 : 	(RemAddRef, RemAddRefResponse),2 : 	(RemRelease, RemReleaseResponse)}
#################################################################################
#IRemUnknown2 Definition
#################################################################################
MSRPC_UUID_IREMUNKNOWN2 = uuidtup_to_bin(('00000143-0000-0000-C000-000000000046','0.0'))
class RemQueryInterface2(NDRCALL):
	OPNUM = 0
	structure = (
			('ripid', REFIPID),
			('cIids', UNSIGNED_SHORT),
			('iids', IID)
		)
class RemQueryInterface2Response(NDRCALL):
	structure = (
			('ripid', REFIPID),
			('cIids', UNSIGNED_SHORT),
			('iids', IID)
		)
OPNUMS = {0 : 	(RemQueryInterface2, RemQueryInterface2Response)}
#################################################################################
#TYPEDEFS
#################################################################################
VDS_OBJECT_ID = GUID
VDS_H_UNKNOWN = 0
VDS_H_HEALTHY = 1
VDS_H_REBUILDING = 2
VDS_H_STALE = 3
VDS_H_FAILING = 4
VDS_H_FAILING_REDUNDANCY = 5
VDS_H_FAILED_REDUNDANCY = 6
VDS_H_FAILED_REDUNDANCY_FAILING = 7
VDS_H_FAILED = 8
VDS_NTT_UNKNOWN = 0
VDS_NTT_PACK = 10
VDS_NTT_VOLUME = 11
VDS_NTT_DISK = 13
VDS_NTT_PARTITION = 60
VDS_NTT_DRIVE_LETTER = 61
VDS_NTT_FILE_SYSTEM = 62
VDS_NTT_MOUNT_POINT = 63
VDS_NTT_SERVICE = 200
VDS_ASYNCOUT_UNKNOWN = 0
VDS_ASYNCOUT_CREATEVOLUME = 1
VDS_ASYNCOUT_EXTENDVOLUME = 2
VDS_ASYNCOUT_SHRINKVOLUME = 3
VDS_ASYNCOUT_ADDVOLUMEPLEX = 4
VDS_ASYNCOUT_BREAKVOLUMEPLEX = 5
VDS_ASYNCOUT_REMOVEVOLUMEPLEX = 6
VDS_ASYNCOUT_REPAIRVOLUMEPLEX = 7
VDS_ASYNCOUT_RECOVERPACK = 8
VDS_ASYNCOUT_REPLACEDISK = 9
VDS_ASYNCOUT_CREATEPARTITION = 10
VDS_ASYNCOUT_CLEAN = 11
VDS_ASYNCOUT_CREATELUN = 50
VDS_ASYNCOUT_FORMAT = 101
VDS_ASYNCOUT_CREATE_VDISK = 200
VDS_ASYNCOUT_SURFACE_VDISK = 201
VDS_ASYNCOUT_COMPACT_VDISK = 202
VDS_ASYNCOUT_MERGE_VDISK = 203
VDS_ASYNCOUT_EXPAND_VDISK = 204
VDSBusTypeUnknown = 0
VDSBusTypeScsi = 1
VDSBusTypeAtapi = 2
VDSBusTypeAta = 3
VDSBusType1394 = 4
VDSBusTypeSsa = 5
VDSBusTypeFibre = 6
VDSBusTypeUsb = 7
VDSBusTypeRAID = 8
VDSBusTypeiScsi = 9
VDSBusTypeSas = 10
VDSBusTypeSata = 11
VDSBusTypeSd = 12
VDSBusTypeMmc = 13
VDSBusTypeMax = 14
VDSBusTypeVirtual = 14
VDSBusTypeFileBackedVirtual = 15
VDSBusTypeSpaces = 16
VDSBusTypeMaxReserved = 127
VDSStorageIdCodeSetReserved = 0
VDSStorageIdCodeSetBinary = 1
VDSStorageIdCodeSetAscii = 2
VDSStorageIdCodeSetUtf8 = 3
VDSStorageIdTypeVendorSpecific = 0
VDSStorageIdTypeVendorId = 1
VDSStorageIdTypeEUI64 = 2
VDSStorageIdTypeFCPHName = 3
VDSStorageIdTypePortRelative = 4
VDSStorageIdTypeTargetPortGroup = 5
VDSStorageIdTypeLogicalUnitGroup = 6
VDSStorageIdTypeMD5LogicalUnitIdentifier = 7
VDSStorageIdTypeScsiNameString = 8
VDS_IA_UNKNOWN = 0
VDS_IA_FCFS = 1
VDS_IA_FCPH = 2
VDS_IA_FCPH3 = 3
VDS_IA_MAC = 4
VDS_IA_SCSI = 5
VDS_FST_UNKNOWN = 0
VDS_FST_RAW = 1
VDS_FST_FAT = 2
VDS_FST_FAT32 = 3
VDS_FST_NTFS = 4
VDS_FST_CDFS = 5
VDS_FST_UDF = 6
VDS_FST_EXFAT = 7
VDS_FST_CSVFS = 8
VDS_FST_REFS = 9
VDS_FSF_SUPPORT_FORMAT = 1
VDS_FSF_SUPPORT_QUICK_FORMAT = 2
VDS_FSF_SUPPORT_COMPRESS = 4
VDS_FSF_SUPPORT_SPECIFY_LABEL = 8
VDS_FSF_SUPPORT_MOUNT_POINT = 16
VDS_FSF_SUPPORT_REMOVABLE_MEDIA = 32
VDS_FSF_SUPPORT_EXTEND = 64
VDS_FSF_ALLOCATION_UNIT_512 = 65536
VDS_FSF_ALLOCATION_UNIT_1K = 131072
VDS_FSF_ALLOCATION_UNIT_2K = 262144
VDS_FSF_ALLOCATION_UNIT_4K = 524288
VDS_FSF_ALLOCATION_UNIT_8K = 1048576
VDS_FSF_ALLOCATION_UNIT_16K = 2097152
VDS_FSF_ALLOCATION_UNIT_32K = 4194304
VDS_FSF_ALLOCATION_UNIT_64K = 8388608
VDS_FSF_ALLOCATION_UNIT_128K = 16777216
VDS_FSF_ALLOCATION_UNIT_256K = 33554432
VDS_FPF_COMPRESSED = 1
VDS_FSS_DEFAULT = 1
VDS_FSS_PREVIOUS_REVISION = 2
VDS_FSS_RECOMMENDED = 4
VDS_DET_UNKNOWN = 0
VDS_DET_FREE = 1
VDS_DET_DATA = 2
VDS_DET_OEM = 3
VDS_DET_ESP = 4
VDS_DET_MSR = 5
VDS_DET_LDM = 6
VDS_DET_UNUSABLE = 32767
VDS_PST_UNKNOWN = 0
VDS_PST_MBR = 1
VDS_PST_GPT = 2
VDS_PTF_SYSTEM = 1
VDS_VT_UNKNOWN = 0
VDS_VT_SIMPLE = 10
VDS_VT_SPAN = 11
VDS_VT_STRIPE = 12
VDS_VT_MIRROR = 13
VDS_VT_PARITY = 14
VDS_TS_UNKNOWN = 0
VDS_TS_STABLE = 1
VDS_TS_EXTENDING = 2
VDS_TS_SHRINKING = 3
VDS_TS_RECONFIGING = 4
VDS_FSOF_NONE = 0
VDS_FSOF_FORCE = 1
VDS_FSOF_QUICK = 2
VDS_FSOF_COMPRESSION = 4
VDS_FSOF_DUPLICATE_METADATA = 8
VDS_DF_AUDIO_CD = 1
VDS_DF_HOTSPARE = 2
VDS_DF_RESERVE_CAPABLE = 4
VDS_DF_MASKED = 8
VDS_DF_STYLE_CONVERTIBLE = 16
VDS_DF_CLUSTERED = 32
VDS_DF_READ_ONLY = 64
VDS_DF_SYSTEM_DISK = 128
VDS_DF_BOOT_DISK = 256
VDS_DF_PAGEFILE_DISK = 512
VDS_DF_HIBERNATIONFILE_DISK = 1024
VDS_DF_CRASHDUMP_DISK = 2048
VDS_DF_HAS_ARC_PATH = 4096
VDS_DF_DYNAMIC = 8192
VDS_DF_BOOT_FROM_DISK = 16384
VDS_DF_CURRENT_READ_ONLY = 32768
VDS_DS_UNKNOWN = 0
VDS_DS_ONLINE = 1
VDS_DS_NOT_READY = 2
VDS_DS_NO_MEDIA = 3
VDS_DS_OFFLINE = 4
VDS_DS_FAILED = 5
VDS_DS_MISSING = 6
VDS_LRM_NONE = 0
VDS_LRM_EXCLUSIVE_RW = 1
VDS_LRM_EXCLUSIVE_RO = 2
VDS_LRM_SHARED_RO = 3
VDS_LRM_SHARED_RW = 4
VDS_VS_UNKNOWN = 0
VDS_VS_ONLINE = 1
VDS_VS_NO_MEDIA = 3
VDS_VS_OFFLINE = 4
VDS_VS_FAILED = 5
VDS_VF_SYSTEM_VOLUME = 1
VDS_VF_BOOT_VOLUME = 2
VDS_VF_ACTIVE = 4
VDS_VF_READONLY = 8
VDS_VF_HIDDEN = 16
VDS_VF_CAN_EXTEND = 32
VDS_VF_CAN_SHRINK = 64
VDS_VF_PAGEFILE = 128
VDS_VF_HIBERNATION = 256
VDS_VF_CRASHDUMP = 512
VDS_VF_INSTALLABLE = 1024
VDS_VF_LBN_REMAP_ENABLED = 2048
VDS_VF_FORMATTING = 4096
VDS_VF_NOT_FORMATTABLE = 8192
VDS_VF_NTFS_NOT_SUPPORTED = 16384
VDS_VF_FAT32_NOT_SUPPORTED = 32768
VDS_VF_FAT_NOT_SUPPORTED = 65536
VDS_VF_NO_DEFAULT_DRIVE_LETTER = 131072
VDS_VF_PERMANENTLY_DISMOUNTED = 262144
VDS_VF_PERMANENT_DISMOUNT_SUPPORTED = 524288
VDS_VF_SHADOW_COPY = 1048576
VDS_VF_FVE_ENABLED = 2097152
VDS_VF_DIRTY = 4194304
VDS_VF_REFS_NOT_SUPPORTED = 8388608
class VDS_PACK_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = 		(		('ulEvent', UNSIGNED_LONG), 		('packId', VDS_OBJECT_ID))
class VDS_DISK_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = 		(		('ulEvent', UNSIGNED_LONG), 		('diskId', VDS_OBJECT_ID))
class VDS_VOLUME_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = (
			('ulEvent', UNSIGNED_LONG),
			('volumeId', VDS_OBJECT_ID),
			('plexId', VDS_OBJECT_ID),
			('ulPercentCompleted', UNSIGNED_LONG)
		)
class VDS_PARTITION_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = (
			('ulEvent', UNSIGNED_LONG),
			('diskId', VDS_OBJECT_ID),
			('ullOffset', ULONGLONG)
		)
class VDS_DRIVE_LETTER_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = (
			('ulEvent', UNSIGNED_LONG),
			('wcLetter', WCHAR),
			('volumeId', VDS_OBJECT_ID)
		)
class VDS_FILE_SYSTEM_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = (
			('ulEvent', UNSIGNED_LONG),
			('volumeId', VDS_OBJECT_ID),
			('dwPercentCompleted', DWORD)
		)
class VDS_MOUNT_POINT_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = 		(		('ulEvent', UNSIGNED_LONG), 		('volumeId', VDS_OBJECT_ID))
VDS_RA_UNKNOWN = 0
VDS_RA_REFRESH = 1
VDS_RA_RESTART = 2
class VDS_SERVICE_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = 		(		('ulEvent', ULONG), 		('action', VDS_RECOVER_ACTION))
class U0(NDRUNION):
	union = {VDS_NTT_PACK : 		('Pack', VDS_PACK_NOTIFICATION),VDS_NTT_DISK : 		('Disk', VDS_DISK_NOTIFICATION),VDS_NTT_VOLUME : 		('Volume', VDS_VOLUME_NOTIFICATION),VDS_NTT_PARTITION : 		('Partition', VDS_PARTITION_NOTIFICATION),VDS_NTT_DRIVE_LETTER : 		('Letter', VDS_DRIVE_LETTER_NOTIFICATION),VDS_NTT_FILE_SYSTEM : 		('FileSystem', VDS_FILE_SYSTEM_NOTIFICATION),VDS_NTT_MOUNT_POINT : 		('MountPoint', VDS_MOUNT_POINT_NOTIFICATION),VDS_NTT_SERVICE : 		('Service', VDS_SERVICE_NOTIFICATION)}
class VDS_NOTIFICATION(NDRSTRUCT):
	align = 1
	structure = 		(		('objectType', VDS_NOTIFICATION_TARGET_TYPE), 		('u0', U0))
class CP(NDRSTRUCT):
	align = 1
	structure = 		(		('ullOffset', ULONGLONG), 		('volumeId', VDS_OBJECT_ID))
class CV(NDRSTRUCT):
	align = 1
	structure = (
			('pVolumeUnk', IUNKNOWN)
		)
class BVP(NDRSTRUCT):
	align = 1
	structure = (
			('pVolumeUnk', IUNKNOWN)
		)
class SV(NDRSTRUCT):
	align = 1
	structure = (
			('ullReclaimedBytes', ULONGLONG)
		)
class CVD(NDRSTRUCT):
	align = 1
	structure = (
			('pVDiskUnk', IUNKNOWN)
		)
class U0(NDRUNION):
	union = {VDS_ASYNCOUT_CREATE_VDISK : 		('cp', CP),VDS_ASYNCOUT_CREATE_VDISK : 		('cv', CV),VDS_ASYNCOUT_CREATE_VDISK : 		('bvp', BVP),VDS_ASYNCOUT_CREATE_VDISK : 		('sv', SV),VDS_ASYNCOUT_CREATE_VDISK : 		('cvd', CVD)}
class VDS_ASYNC_OUTPUT(NDRSTRUCT):
	align = 1
	structure = 		(		('type', VDS_ASYNC_OUTPUT_TYPE), 		('u0', U0))
class VDS_PARTITION_INFO_MBR(NDRSTRUCT):
	align = 1
	structure = (
			('partitionType', BYTE),
			('bootIndicator', BOOLEAN),
			('recognizedPartition', BOOLEAN),
			('hiddenSectors', DWORD)
		)
class VDS_PARTITION_INFO_GPT(NDRSTRUCT):
	align = 1
	structure = (
			('partitionType', GUID),
			('partitionId', GUID),
			('attributes', ULONGLONG),
			('name', WCHAR)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = BYTE
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = (
			('m_CodeSet', VDS_STORAGE_IDENTIFIER_CODE_SET),
			('m_Type', VDS_STORAGE_IDENTIFIER_TYPE),
			('m_cbIdentifier', UNSIGNED_LONG),
			('m_rgbIdentifier', PTR_UNSIGNED_LONG)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = VDS_STORAGE_IDENTIFIER
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = (
			('m_version', UNSIGNED_LONG),
			('m_cIdentifiers', UNSIGNED_LONG),
			('m_rgIdentifiers', PTR_UNSIGNED_LONG)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = BYTE
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = (
			('m_addressType', VDS_INTERCONNECT_ADDRESS_TYPE),
			('m_cbPort', UNSIGNED_LONG),
			('m_pbPort', BYTE),
			('m_cbAddress', UNSIGNED_LONG),
			('m_pbAddress', PTR_UNSIGNED_LONG)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = VDS_INTERCONNECT
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = (
			('m_version', UNSIGNED_LONG),
			('m_DeviceType', BYTE),
			('m_DeviceTypeModifier', BYTE),
			('m_bCommandQueuing', LONG),
			('m_BusType', VDS_STORAGE_BUS_TYPE),
			('m_szVendorId', CHAR),
			('m_szProductId', CHAR),
			('m_szProductRevision', CHAR),
			('m_szSerialNumber', CHAR),
			('m_diskSignature', GUID),
			('m_deviceIdDescriptor', VDS_STORAGE_DEVICE_ID_DESCRIPTOR),
			('m_cInterconnects', UNSIGNED_LONG),
			('m_rgInterconnects', PTR_UNSIGNED_LONG)
		)
class VDS_FILE_SYSTEM_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('type', VDS_FILE_SYSTEM_TYPE),
			('volumeId', VDS_OBJECT_ID),
			('ulFlags', UNSIGNED_LONG),
			('ullTotalAllocationUnits', ULONGLONG),
			('ullAvailableAllocationUnits', ULONGLONG),
			('ulAllocationUnitSize', UNSIGNED_LONG),
			('pwszLabel', WCHAR)
		)
class PVDS_FILE_SYSTEM_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_FILE_SYSTEM_PROP)
		)
class VDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('ulFlags', UNSIGNED_LONG),
			('usRevision', UNSIGNED_SHORT),
			('ulDefaultUnitAllocationSize', UNSIGNED_LONG),
			('rgulAllowedUnitAllocationSizes', UNSIGNED_LONG),
			('wszName', WCHAR)
		)
class PVDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_FILE_SYSTEM_FORMAT_SUPPORT_PROP)
		)
class VDS_DISK_EXTENT(NDRSTRUCT):
	align = 1
	structure = (
			('diskId', VDS_OBJECT_ID),
			('type', VDS_DISK_EXTENT_TYPE),
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('volumeId', VDS_OBJECT_ID),
			('plexId', VDS_OBJECT_ID),
			('memberIdx', UNSIGNED_LONG)
		)
class PVDS_DISK_EXTENT(NDRPOINTER):
	referent = (
			('Data', VDS_DISK_EXTENT)
		)
class VDS_DISK_FREE_EXTENT(NDRSTRUCT):
	align = 1
	structure = (
			('diskId', VDS_OBJECT_ID),
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG)
		)
class PVDS_DISK_FREE_EXTENT(NDRPOINTER):
	referent = (
			('Data', VDS_DISK_FREE_EXTENT)
		)
class U0(NDRUNION):
	union = {VDS_PST_MBR : 		('Mbr', VDS_PARTITION_INFO_MBR),VDS_PST_GPT : 		('Gpt', VDS_PARTITION_INFO_GPT)}
class VDS_PARTITION_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('PartitionStyle', VDS_PARTITION_STYLE),
			('ulFlags', UNSIGNED_LONG),
			('ulPartitionNumber', UNSIGNED_LONG),
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('u0', U0)
		)
class VDS_INPUT_DISK(NDRSTRUCT):
	align = 1
	structure = (
			('diskId', VDS_OBJECT_ID),
			('ullSize', ULONGLONG),
			('plexId', VDS_OBJECT_ID),
			('memberIdx', UNSIGNED_LONG)
		)
class MBRPARTINFO(NDRSTRUCT):
	align = 1
	structure = 		(		('partitionType', BYTE), 		('bootIndicator', BOOLEAN))
class GPTPARTINFO(NDRSTRUCT):
	align = 1
	structure = (
			('partitionType', GUID),
			('partitionId', GUID),
			('attributes', ULONGLONG),
			('name', WCHAR)
		)
class U0(NDRUNION):
	union = {VDS_PST_GPT : 		('MbrPartInfo', MBRPARTINFO),VDS_PST_GPT : 		('GptPartInfo', GPTPARTINFO)}
class CREATE_PARTITION_PARAMETERS(NDRSTRUCT):
	align = 1
	structure = 		(		('style', VDS_PARTITION_STYLE), 		('u0', U0))
class VIRTUAL_STORAGE_TYPE(NDRSTRUCT):
	align = 1
	structure = 		(		('DeviceId', ULONG), 		('VendorId', GUID))
VDS_PARTITION_STYLE_MBR = 0
VDS_PARTITION_STYLE_GPT = 1
VDS_PARTITION_STYLE_RAW = 2
VDS_OT_UNKNOWN = 0
VDS_OT_PROVIDER = 1
VDS_OT_PACK = 10
VDS_OT_VOLUME = 11
VDS_OT_VOLUME_PLEX = 12
VDS_OT_DISK = 13
VDS_OT_HBAPORT = 90
VDS_OT_INIT_ADAPTER = 91
VDS_OT_INIT_PORTAL = 92
VDS_OT_ASYNC = 100
VDS_OT_ENUM = 101
VDS_OT_VDISK = 200
VDS_OT_OPEN_VDISK = 201
VDS_SVF_SUPPORT_DYNAMIC = 1
VDS_SVF_SUPPORT_FAULT_TOLERANT = 2
VDS_SVF_SUPPORT_GPT = 4
VDS_SVF_SUPPORT_DYNAMIC_1394 = 8
VDS_SVF_CLUSTER_SERVICE_CONFIGURED = 16
VDS_SVF_AUTO_MOUNT_OFF = 32
VDS_SVF_OS_UNINSTALL_VALID = 64
VDS_SVF_EFI = 128
VDS_SVF_SUPPORT_MIRROR = 256
VDS_SVF_SUPPORT_RAIDS = 512
VDS_SVF_SUPPORT_REFS = 1024
VDS_PT_UNKNOWN = 0
VDS_PT_SOFTWARE = 1
VDS_PT_HARDWARE = 2
VDS_PT_VIRTUALDISK = 3
VDS_PT_MAX = 4
VDS_PF_DYNAMIC = 1
VDS_PF_INTERNAL_HARDWARE_PROVIDER = 2
VDS_PF_ONE_DISK_ONLY_PER_PACK = 4
VDS_PF_ONE_PACK_ONLINE_ONLY = 8
VDS_PF_VOLUME_SPACE_MUST_BE_CONTIGUOUS = 16
VDS_PF_SUPPORT_MIRROR = 32
VDS_PF_SUPPORT_RAID5 = 64
VDS_PF_SUPPORT_DYNAMIC_1394 = 536870912
VDS_PF_SUPPORT_FAULT_TOLERANT = 1073741824
VDS_PF_SUPPORT_DYNAMIC = 2147483648
VDS_QUERY_SOFTWARE_PROVIDERS = 1
VDS_QUERY_HARDWARE_PROVIDERS = 2
VDS_QUERY_VIRTUALDISK_PROVIDERS = 4
VDS_DLF_NON_PERSISTENT = 1
VDS_PS_UNKNOWN = 0
VDS_PS_ONLINE = 1
VDS_PS_OFFLINE = 4
VDS_PKF_FOREIGN = 1
VDS_PKF_NOQUORUM = 2
VDS_PKF_POLICY = 4
VDS_PKF_CORRUPTED = 8
VDS_PKF_ONLINE_ERROR = 16
VDSDiskOfflineReasonNone = 0
VDSDiskOfflineReasonPolicy = 1
VDSDiskOfflineReasonRedundantPath = 2
VDSDiskOfflineReasonSnapshot = 3
VDSDiskOfflineReasonCollision = 4
VDSDiskOfflineReasonResourceExhaustion = 5
VDSDiskOfflineReasonWriteFailure = 6
VDSDiskOfflineReasonDIScan = 7
VDS_VPT_UNKNOWN = 0
VDS_VPT_SIMPLE = 10
VDS_VPT_SPAN = 11
VDS_VPT_STRIPE = 12
VDS_VPT_PARITY = 14
VDS_VPS_UNKNOWN = 0
VDS_VPS_ONLINE = 1
VDS_VPS_NO_MEDIA = 3
VDS_VPS_FAILED = 5
VDS_IPT_TEXT = 0
VDS_IPT_IPV4 = 1
VDS_IPT_IPV6 = 2
VDS_IPT_EMPTY = 3
VDS_HPT_UNKNOWN = 1
VDS_HPT_OTHER = 2
VDS_HPT_NOTPRESENT = 3
VDS_HPT_NPORT = 5
VDS_HPT_NLPORT = 6
VDS_HPT_FLPORT = 7
VDS_HPT_FPORT = 8
VDS_HPT_EPORT = 9
VDS_HPT_GPORT = 10
VDS_HPT_LPORT = 20
VDS_HPT_PTP = 21
VDS_HPS_UNKNOWN = 1
VDS_HPS_ONLINE = 2
VDS_HPS_OFFLINE = 3
VDS_HPS_BYPASSED = 4
VDS_HPS_DIAGNOSTICS = 5
VDS_HPS_LINKDOWN = 6
VDS_HPS_ERROR = 7
VDS_HPS_LOOPBACK = 8
VDS_HSF_UNKNOWN = 0
VDS_HSF_1GBIT = 1
VDS_HSF_2GBIT = 2
VDS_HSF_10GBIT = 4
VDS_HSF_4GBIT = 8
VDS_HSF_NOT_NEGOTIATED = 32768
VDS_MPS_UNKNOWN = 0
VDS_MPS_ONLINE = 1
VDS_MPS_FAILED = 5
VDS_MPS_STANDBY = 7
class VDS_REPARSE_POINT_PROP(NDRSTRUCT):
	align = 1
	structure = 		(		('SourceVolumeId', VDS_OBJECT_ID), 		('pwszPath', WCHAR))
class PVDS_REPARSE_POINT_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_REPARSE_POINT_PROP)
		)
class VDS_DRIVE_LETTER_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('wcLetter', WCHAR),
			('volumeId', VDS_OBJECT_ID),
			('ulFlags', UNSIGNED_LONG),
			('bUsed', LONG)
		)
class PVDS_DRIVE_LETTER_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_DRIVE_LETTER_PROP)
		)
VDS_SP_UNKNOWN = 0
VDS_SP_ONLINE = 1
VDS_SP_OFFLINE_SHARED = 2
VDS_SP_OFFLINE = 3
VDS_SP_OFFLINE_INTERNAL = 4
VDS_SP_MAX = 5
class VDS_FILE_SYSTEM_TYPE_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('type', VDS_FILE_SYSTEM_TYPE),
			('wszName', WCHAR),
			('ulFlags', UNSIGNED_LONG),
			('ulCompressionFlags', UNSIGNED_LONG),
			('ulMaxLabelLength', UNSIGNED_LONG),
			('pwszIllegalLabelCharSet', WCHAR)
		)
class PVDS_FILE_SYSTEM_TYPE_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_FILE_SYSTEM_TYPE_PROP)
		)
class MBRPARTINFO(NDRSTRUCT):
	align = 1
	structure = (
			('bootIndicator', BOOLEAN)
		)
class GPTPARTINFO(NDRSTRUCT):
	align = 1
	structure = (
			('attributes', ULONGLONG)
		)
class U0(NDRUNION):
	union = {VDS_PST_GPT : 		('MbrPartInfo', MBRPARTINFO),VDS_PST_GPT : 		('GptPartInfo', GPTPARTINFO)}
class CHANGE_ATTRIBUTES_PARAMETERS(NDRSTRUCT):
	align = 1
	structure = 		(		('style', VDS_PARTITION_STYLE), 		('u0', U0))
class MBRPARTINFO(NDRSTRUCT):
	align = 1
	structure = (
			('partitionType', BYTE)
		)
class GPTPARTINFO(NDRSTRUCT):
	align = 1
	structure = (
			('partitionType', GUID)
		)
class U0(NDRUNION):
	union = {VDS_PST_GPT : 		('MbrPartInfo', MBRPARTINFO),VDS_PST_GPT : 		('GptPartInfo', GPTPARTINFO)}
class CHANGE_PARTITION_TYPE_PARAMETERS(NDRSTRUCT):
	align = 1
	structure = 		(		('style', VDS_PARTITION_STYLE), 		('u0', U0))
class VDS_WWN(NDRSTRUCT):
	align = 1
	structure = (
			('rguchWwn', UNSIGNED_CHAR)
		)
class VDS_IPADDRESS(NDRSTRUCT):
	align = 1
	structure = (
			('type', VDS_IPADDRESS_TYPE),
			('ipv4Address', UNSIGNED_LONG),
			('ipv6Address', UNSIGNED_CHAR),
			('ulIpv6FlowInfo', UNSIGNED_LONG),
			('ulIpv6ScopeId', UNSIGNED_LONG),
			('wszTextAddress', WCHAR),
			('ulPort', UNSIGNED_LONG)
		)
class DATA_UNSIGNED_LONG(NDRUniConformantArray):
	item = UNSIGNED_CHAR
class PTR_UNSIGNED_LONG(NDRPOINTER):
	referent = (
			('Data', DATA_UNSIGNED_LONG)
		)
class UNSIGNED_LONG(NDRSTRUCT):
	align = 1
	structure = 		(		('pSharedSecret', PTR_VDS_ISCSI_SHARED_SECRET), 		('ulSharedSecretSize', UNSIGNED_LONG))
class VDS_SERVICE_PROP(NDRSTRUCT):
	align = 1
	structure = 		(		('pwszVersion', WCHAR), 		('ulFlags', UNSIGNED_LONG))
class VDS_HBAPORT_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('wwnNode', VDS_WWN),
			('wwnPort', VDS_WWN),
			('type', VDS_HBAPORT_TYPE),
			('status', VDS_HBAPORT_STATUS),
			('ulPortSpeed', UNSIGNED_LONG),
			('ulSupportedPortSpeed', UNSIGNED_LONG)
		)
class VDS_ISCSI_INITIATOR_ADAPTER_PROP(NDRSTRUCT):
	align = 1
	structure = 		(		('id', VDS_OBJECT_ID), 		('pwszName', WCHAR))
class VDS_ISCSI_INITIATOR_PORTAL_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('address', VDS_IPADDRESS),
			('ulPortIndex', UNSIGNED_LONG)
		)
class VDS_PROVIDER_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('pwszName', WCHAR),
			('guidVersionId', GUID),
			('pwszVersion', WCHAR),
			('type', VDS_PROVIDER_TYPE),
			('ulFlags', UNSIGNED_LONG),
			('ulStripeSizeFlags', UNSIGNED_LONG),
			('sRebuildPriority', SHORT)
		)
class VDS_PACK_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('pwszName', WCHAR),
			('status', VDS_PACK_STATUS),
			('ulFlags', UNSIGNED_LONG)
		)
class PVDS_PACK_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_PACK_PROP)
		)
class U0(NDRUNION):
	union = {VDS_PST_MBR : 		('dwSignature', DWORD),VDS_PST_GPT : 		('DiskGuid', GUID)}
class VDS_DISK_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('status', VDS_DISK_STATUS),
			('ReserveMode', VDS_LUN_RESERVE_MODE),
			('health', VDS_HEALTH),
			('dwDeviceType', DWORD),
			('dwMediaType', DWORD),
			('ullSize', ULONGLONG),
			('ulBytesPerSector', UNSIGNED_LONG),
			('ulSectorsPerTrack', UNSIGNED_LONG),
			('ulTracksPerCylinder', UNSIGNED_LONG),
			('ulFlags', UNSIGNED_LONG),
			('BusType', VDS_STORAGE_BUS_TYPE),
			('PartitionStyle', VDS_PARTITION_STYLE),
			('u0', U0),
			('pwszDiskAddress', WCHAR),
			('pwszName', WCHAR),
			('pwszFriendlyName', WCHAR),
			('pwszAdaptorName', WCHAR),
			('pwszDevicePath', WCHAR)
		)
class PVDS_DISK_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_DISK_PROP)
		)
class U0(NDRUNION):
	union = {VDS_PST_MBR : 		('dwSignature', DWORD),VDS_PST_GPT : 		('DiskGuid', GUID)}
class VDS_DISK_PROP2(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('status', VDS_DISK_STATUS),
			('ReserveMode', VDS_LUN_RESERVE_MODE),
			('health', VDS_HEALTH),
			('dwDeviceType', DWORD),
			('dwMediaType', DWORD),
			('ullSize', ULONGLONG),
			('ulBytesPerSector', UNSIGNED_LONG),
			('ulSectorsPerTrack', UNSIGNED_LONG),
			('ulTracksPerCylinder', UNSIGNED_LONG),
			('ulFlags', UNSIGNED_LONG),
			('BusType', VDS_STORAGE_BUS_TYPE),
			('PartitionStyle', VDS_PARTITION_STYLE),
			('u0', U0),
			('pwszDiskAddress', WCHAR),
			('pwszName', WCHAR),
			('pwszFriendlyName', WCHAR),
			('pwszAdaptorName', WCHAR),
			('pwszDevicePath', WCHAR),
			('pwszLocationPath', WCHAR)
		)
class PVDS_DISK_PROP2(NDRPOINTER):
	referent = (
			('Data', VDS_DISK_PROP2)
		)
class U0(NDRUNION):
	union = {VDS_PST_MBR : 		('dwSignature', DWORD),VDS_PST_GPT : 		('DiskGuid', GUID)}
class VDS_ADVANCEDDISK_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('pwszId', LPWSTR),
			('pwszPathname', LPWSTR),
			('pwszLocation', LPWSTR),
			('pwszFriendlyName', LPWSTR),
			('pswzIdentifier', LPWSTR),
			('usIdentifierFormat', USHORT),
			('ulNumber', ULONG),
			('pwszSerialNumber', LPWSTR),
			('pwszFirmwareVersion', LPWSTR),
			('pwszManufacturer', LPWSTR),
			('pwszModel', LPWSTR),
			('ullTotalSize', ULONGLONG),
			('ullAllocatedSize', ULONGLONG),
			('ulLogicalSectorSize', ULONG),
			('ulPhysicalSectorSize', ULONG),
			('ulPartitionCount', ULONG),
			('status', VDS_DISK_STATUS),
			('health', VDS_HEALTH),
			('BusType', VDS_STORAGE_BUS_TYPE),
			('PartitionStyle', VDS_PARTITION_STYLE),
			('u0', U0),
			('ulFlags', ULONG),
			('dwDeviceType', DWORD)
		)
class PVDS_ADVANCEDDISK_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_ADVANCEDDISK_PROP)
		)
class VDS_VOLUME_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('type', VDS_VOLUME_TYPE),
			('status', VDS_VOLUME_STATUS),
			('health', VDS_HEALTH),
			('TransitionState', VDS_TRANSITION_STATE),
			('ullSize', ULONGLONG),
			('ulFlags', UNSIGNED_LONG),
			('RecommendedFileSystemType', VDS_FILE_SYSTEM_TYPE),
			('pwszName', WCHAR)
		)
class PVDS_VOLUME_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_VOLUME_PROP)
		)
class DATA_WCHAR(NDRUniConformantArray):
	item = BYTE
class PTR_WCHAR(NDRPOINTER):
	referent = (
			('Data', DATA_WCHAR)
		)
class WCHAR(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('type', VDS_VOLUME_TYPE),
			('status', VDS_VOLUME_STATUS),
			('health', VDS_HEALTH),
			('TransitionState', VDS_TRANSITION_STATE),
			('ullSize', ULONGLONG),
			('ulFlags', UNSIGNED_LONG),
			('RecommendedFileSystemType', VDS_FILE_SYSTEM_TYPE),
			('cbUniqueId', ULONG),
			('pwszName', WCHAR),
			('pUniqueId', PTR_WCHAR)
		)
class VDS_VOLUME_PLEX_PROP(NDRSTRUCT):
	align = 1
	structure = (
			('id', VDS_OBJECT_ID),
			('type', VDS_VOLUME_PLEX_TYPE),
			('status', VDS_VOLUME_PLEX_STATUS),
			('health', VDS_HEALTH),
			('TransitionState', VDS_TRANSITION_STATE),
			('ullSize', ULONGLONG),
			('ulStripeSize', UNSIGNED_LONG),
			('ulNumberOfMembers', UNSIGNED_LONG)
		)
class PVDS_VOLUME_PLEX_PROP(NDRPOINTER):
	referent = (
			('Data', VDS_VOLUME_PLEX_PROP)
		)
CREATE_VIRTUAL_DISK_FLAG_NONE = 0
CREATE_VIRTUAL_DISK_FLAG_FULL_PHYSICAL_ALLOCATION = 1
OPEN_VIRTUAL_DISK_FLAG_NONE = 0
OPEN_VIRTUAL_DISK_FLAG_NO_PARENTS = 1
OPEN_VIRTUAL_DISK_FLAG_BLANK_FILE = 2
OPEN_VIRTUAL_DISK_FLAG_BOOT_DRIVE = 4
class VDS_CREATE_VDISK_PARAMETERS(NDRSTRUCT):
	align = 1
	structure = (
			('UniqueId', GUID),
			('MaximumSize', ULONGLONG),
			('BlockSizeInBytes', ULONG),
			('SectorSizeInBytes', ULONG),
			('pParentPath', LPWSTR),
			('pSourcePath', LPWSTR)
		)
class PVDS_CREATE_VDISK_PARAMETERS(NDRPOINTER):
	referent = (
			('Data', VDS_CREATE_VDISK_PARAMETERS)
		)
VDS_VST_UNKNOWN = 0
VDS_VST_ADDED = 0
VDS_VST_OPEN = 0
VDS_VST_ATTACH_PENDING = 0
VDS_VST_ATTACHED_NOT_OPEN = 0
VDS_VST_ATTACHED = 0
VDS_VST_DETACH_PENDING = 0
VDS_VST_COMPACTING = 0
VDS_VST_MERGING = 0
VDS_VST_EXPANDING = 0
VDS_VST_DELETED = 0
ATTACH_VIRTUAL_DISK_FLAG_NONE = 0
ATTACH_VIRTUAL_DISK_FLAG_READ_ONLY = 1
ATTACH_VIRTUAL_DISK_FLAG_NO_DRIVE_LETTER = 2
ATTACH_VIRTUAL_DISK_FLAG_PERMANENT_LIFETIME = 4
ATTACH_VIRTUAL_DISK_FLAG_NO_LOCAL_HOST = 8
DETACH_VIRTUAL_DISK_FLAG_NONE = 0
COMPACT_VIRTUAL_DISK_FLAG_NONE = 0
MERGE_VIRTUAL_DISK_FLAG_NONE = 0
EXPAND_VIRTUAL_DISK_FLAG_NONE = 0
DEPENDENT_DISK_FLAG_NONE = 0
DEPENDENT_DISK_FLAG_MULT_BACKING_FILES = 1
DEPENDENT_DISK_FLAG_FULLY_ALLOCATED = 2
DEPENDENT_DISK_FLAG_READ_ONLY = 4
DEPENDENT_DISK_FLAG_REMOTE = 8
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME = 16
DEPENDENT_DISK_FLAG_SYSTEM_VOLUME_PARENT = 32
DEPENDENT_DISK_FLAG_REMOVABLE = 64
DEPENDENT_DISK_FLAG_NO_DRIVE_LETTER = 128
DEPENDENT_DISK_FLAG_PARENT = 256
DEPENDENT_DISK_FLAG_NO_HOST_DISK = 512
DEPENDENT_DISK_FLAG_PERMANENT_LIFETIME = 1024
class VDS_VDISK_PROPERTIES(NDRSTRUCT):
	align = 1
	structure = (
			('Id', VDS_OBJECT_ID),
			('State', VDS_VDISK_STATE),
			('VirtualDeviceType', VIRTUAL_STORAGE_TYPE),
			('VirtualSize', ULONGLONG),
			('PhysicalSize', ULONGLONG),
			('pPath', LPWSTR),
			('pDeviceName', LPWSTR),
			('DiskFlag', DEPENDENT_DISK_FLAG),
			('bIsChild', BOOL),
			('pParentPath', LPWSTR)
		)
class PVDS_VDISK_PROPERTIES(NDRPOINTER):
	referent = (
			('Data', VDS_VDISK_PROPERTIES)
		)
VIRTUAL_DISK_ACCESS_SURFACE_RO = 65536
VIRTUAL_DISK_ACCESS_SURFACE_RW = 131072
VIRTUAL_DISK_ACCESS_UNSURFACE = 262144
VIRTUAL_DISK_ACCESS_GET_INFO = 524288
VIRTUAL_DISK_ACCESS_CREATE = 1048576
VIRTUAL_DISK_ACCESS_METAOPS = 2097152
VIRTUAL_DISK_ACCESS_READ = 851968
VIRTUAL_DISK_ACCESS_ALL = 4128768
VIRTUAL_DISK_ACCESS_WRITABLE = 3276800
class PVIRTUAL_STORAGE_TYPE(NDRSTRUCT):
	align = 1
	structure = (
		)
#################################################################################
#CONSTANTS
#################################################################################
IENUMVDSOBJECT = 
IVDSADVISESINK = 
IVDSASYNC = 
IVDSSERVICELOADER = 
IVDSSERVICE = 
IVDSSERVICEINITIALIZATION = 
IVDSSERVICEUNINSTALLDISK = 
IVDSSERVICEHBA = 
IVDSSERVICEISCSI = 
IVDSSERVICESAN = 
IVDSSERVICESW = 
IVDSHBAPORT = 
IVDSISCSIINITIATORADAPTER = 
IVDSISCSIINITIATORPORTAL = 
IVDSPROVIDER = 
IVDSSWPROVIDER = 
IVDSHWPROVIDER = 
IVDSVDPROVIDER = 
IVDSSUBSYSTEMIMPORTTARGET = 
IVDSPACK = 
IVDSPACK2 = 
IVDSDISK = 
IVDSDISK2 = 
IVDSDISK3 = 
IVDSADVANCEDDISK = 
IVDSADVANCEDDISK2 = 
IVDSADVANCEDDISK3 = 
IVDSCREATEPARTITIONEX = 
IVDSDISKONLINE = 
IVDSDISKPARTITIONMF = 
IVDSDISKPARTITIONMF2 = 
IVDSREMOVABLE = 
IVDSVOLUME = 
IVDSVOLUME2 = 
IVDSVOLUMEMF = 
IVDSVOLUMEMF2 = 
IVDSVOLUMEMF3 = 
IVDSVOLUMESHRINK = 
IVDSVOLUMEONLINE = 
IVDSVOLUMEPLEX = 
IVDSVDISK = 
IVDSOPENVDISK = 
VER_VDS_LUN_INFORMATION = 0x00000001
VDS_NF_PACK_ARRIVE = 0x00000001
VDS_NF_PACK_DEPART = 0x00000002
VDS_NF_PACK_MODIFY = 0x00000003
VDS_NF_VOLUME_ARRIVE = 0x00000004
VDS_NF_VOLUME_DEPART = 0x00000005
VDS_NF_VOLUME_MODIFY = 0x00000006
VDS_NF_VOLUME_REBUILDING_PROGRESS = 0x00000007
VDS_NF_DISK_ARRIVE = 0x00000008
VDS_NF_DISK_DEPART = 0x00000009
VDS_NF_DISK_MODIFY = 0x0000000A
VDS_NF_PARTITION_ARRIVE = 0x0000000B
VDS_NF_PARTITION_DEPART = 0x0000000C
VDS_NF_PARTITION_MODIFY = 0x0000000D
VDS_NF_DRIVE_LETTER_FREE = 0x000000C9
VDS_NF_DRIVE_LETTER_ASSIGN = 0x000000CA
VDS_NF_FILE_SYSTEM_MODIFY = 0x000000CB
VDS_NF_FILE_SYSTEM_FORMAT_PROGRESS = 0x000000CC
VDS_NF_MOUNT_POINTS_CHANGE = 0x000000CD
VDS_NF_SERVICE_OUT_OF_SYNC = 0x0000012D
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#IEnumVdsObject Definition
#################################################################################
MSRPC_UUID_IENUMVDSOBJECT = uuidtup_to_bin(('118610b7-8d94-4030-b5b8-500889788e4e','0.0'))
class Next(NDRCALL):
	OPNUM = 0
	structure = (
			('celt', UNSIGNED_LONG)
		)
class NextResponse(NDRCALL):
	structure = (
			('celt', UNSIGNED_LONG)
		)
class Skip(NDRCALL):
	OPNUM = 1
	structure = (
			('celt', UNSIGNED_LONG)
		)
class SkipResponse(NDRCALL):
	structure = (
			('celt', UNSIGNED_LONG)
		)
class Reset(NDRCALL):
	OPNUM = 2
	structure = (
		)
class ResetResponse(NDRCALL):
	structure = (
		)
class Clone(NDRCALL):
	OPNUM = 3
	structure = (
		)
class CloneResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Next, NextResponse),1 : 	(Skip, SkipResponse),2 : 	(Reset, ResetResponse),3 : 	(Clone, CloneResponse)}
#################################################################################
#IVdsAdviseSink Definition
#################################################################################
MSRPC_UUID_IVDSADVISESINK = uuidtup_to_bin(('8326cd1d-cf59-4936-b786-5efc08798e25','0.0'))
class OnNotify(NDRCALL):
	OPNUM = 0
	structure = 		(		('lNumberOfNotifications', LONG), 		('pNotificationArray', VDS_NOTIFICATION))
class OnNotifyResponse(NDRCALL):
	structure = 		(		('lNumberOfNotifications', LONG), 		('pNotificationArray', VDS_NOTIFICATION))
OPNUMS = {0 : 	(OnNotify, OnNotifyResponse)}
#################################################################################
#IVdsAsync Definition
#################################################################################
MSRPC_UUID_IVDSASYNC = uuidtup_to_bin(('d5d23b6d-555-4492-9889-397322bc','0.0'))
class Cancel(NDRCALL):
	OPNUM = 0
	structure = (
		)
class CancelResponse(NDRCALL):
	structure = (
		)
class Wait(NDRCALL):
	OPNUM = 1
	structure = (
		)
class WaitResponse(NDRCALL):
	structure = (
		)
class QueryStatus(NDRCALL):
	OPNUM = 2
	structure = (
		)
class QueryStatusResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Cancel, CancelResponse),1 : 	(Wait, WaitResponse),2 : 	(QueryStatus, QueryStatusResponse)}
#################################################################################
#IVdsServiceLoader Definition
#################################################################################
MSRPC_UUID_IVDSSERVICELOADER = uuidtup_to_bin(('e0393303-904-497-ab71-e9b671ee2729','0.0'))
class LoadService(NDRCALL):
	OPNUM = 0
	structure = (
			('pwszMachineName', LPWSTR)
		)
class LoadServiceResponse(NDRCALL):
	structure = (
			('pwszMachineName', LPWSTR)
		)
OPNUMS = {0 : 	(LoadService, LoadServiceResponse)}
#################################################################################
#IVdsService Definition
#################################################################################
MSRPC_UUID_IVDSSERVICE = uuidtup_to_bin(('0818a8ef-9ba9-40d8-a6f9-e22833cc771e','0.0'))
class IsServiceReady(NDRCALL):
	OPNUM = 0
	structure = (
		)
class IsServiceReadyResponse(NDRCALL):
	structure = (
		)
class WaitForServiceReady(NDRCALL):
	OPNUM = 1
	structure = (
		)
class WaitForServiceReadyResponse(NDRCALL):
	structure = (
		)
class GetProperties(NDRCALL):
	OPNUM = 2
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class QueryProviders(NDRCALL):
	OPNUM = 3
	structure = (
			('masks', DWORD)
		)
class QueryProvidersResponse(NDRCALL):
	structure = (
			('masks', DWORD)
		)
class Opnum07NotUsedOnWire(NDRCALL):
	OPNUM = 4
	structure = (
		)
class Opnum07NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class QueryUnallocatedDisks(NDRCALL):
	OPNUM = 5
	structure = (
		)
class QueryUnallocatedDisksResponse(NDRCALL):
	structure = (
		)
class GetObject(NDRCALL):
	OPNUM = 6
	structure = 		(		('ObjectId', VDS_OBJECT_ID), 		('type', VDS_OBJECT_TYPE))
class GetObjectResponse(NDRCALL):
	structure = 		(		('ObjectId', VDS_OBJECT_ID), 		('type', VDS_OBJECT_TYPE))
class QueryDriveLetters(NDRCALL):
	OPNUM = 7
	structure = 		(		('wcFirstLetter', WCHAR), 		('count', DWORD))
class QueryDriveLettersResponse(NDRCALL):
	structure = 		(		('wcFirstLetter', WCHAR), 		('count', DWORD))
class QueryFileSystemTypes(NDRCALL):
	OPNUM = 8
	structure = (
		)
class QueryFileSystemTypesResponse(NDRCALL):
	structure = (
		)
class Reenumerate(NDRCALL):
	OPNUM = 9
	structure = (
		)
class ReenumerateResponse(NDRCALL):
	structure = (
		)
class Refresh(NDRCALL):
	OPNUM = 10
	structure = (
		)
class RefreshResponse(NDRCALL):
	structure = (
		)
class CleanupObsoleteMountPoints(NDRCALL):
	OPNUM = 11
	structure = (
		)
class CleanupObsoleteMountPointsResponse(NDRCALL):
	structure = (
		)
class Advise(NDRCALL):
	OPNUM = 12
	structure = (
			('pSink', IVDSADVISESINK)
		)
class AdviseResponse(NDRCALL):
	structure = (
			('pSink', IVDSADVISESINK)
		)
class Unadvise(NDRCALL):
	OPNUM = 13
	structure = (
			('dwCookie', DWORD)
		)
class UnadviseResponse(NDRCALL):
	structure = (
			('dwCookie', DWORD)
		)
class Reboot(NDRCALL):
	OPNUM = 14
	structure = (
		)
class RebootResponse(NDRCALL):
	structure = (
		)
class SetFlags(NDRCALL):
	OPNUM = 15
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class SetFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFlags(NDRCALL):
	OPNUM = 16
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
OPNUMS = {0 : 	(IsServiceReady, IsServiceReadyResponse),1 : 	(WaitForServiceReady, WaitForServiceReadyResponse),2 : 	(GetProperties, GetPropertiesResponse),3 : 	(QueryProviders, QueryProvidersResponse),4 : 	(Opnum07NotUsedOnWire, Opnum07NotUsedOnWireResponse),5 : 	(QueryUnallocatedDisks, QueryUnallocatedDisksResponse),6 : 	(GetObject, GetObjectResponse),7 : 	(QueryDriveLetters, QueryDriveLettersResponse),8 : 	(QueryFileSystemTypes, QueryFileSystemTypesResponse),9 : 	(Reenumerate, ReenumerateResponse),10 : 	(Refresh, RefreshResponse),11 : 	(CleanupObsoleteMountPoints, CleanupObsoleteMountPointsResponse),12 : 	(Advise, AdviseResponse),13 : 	(Unadvise, UnadviseResponse),14 : 	(Reboot, RebootResponse),15 : 	(SetFlags, SetFlagsResponse),16 : 	(ClearFlags, ClearFlagsResponse)}
#################################################################################
#IVdsServiceInitialization Definition
#################################################################################
MSRPC_UUID_IVDSSERVICEINITIALIZATION = uuidtup_to_bin(('4afc3636-db01-4052-80c3-03bbcb8d3c69','0.0'))
class Initialize(NDRCALL):
	OPNUM = 0
	structure = (
			('pwszMachineName', WCHAR)
		)
class InitializeResponse(NDRCALL):
	structure = (
			('pwszMachineName', WCHAR)
		)
OPNUMS = {0 : 	(Initialize, InitializeResponse)}
#################################################################################
#IVdsServiceUninstallDisk Definition
#################################################################################
MSRPC_UUID_IVDSSERVICEUNINSTALLDISK = uuidtup_to_bin(('B6B22DA8-F903-4e7-B492-C09D875AC9DA','0.0'))
class GetDiskIdFromLunInfo(NDRCALL):
	OPNUM = 0
	structure = (
			('pLunInfo', VDS_LUN_INFORMATION)
		)
class GetDiskIdFromLunInfoResponse(NDRCALL):
	structure = (
			('pLunInfo', VDS_LUN_INFORMATION)
		)
class UninstallDisks(NDRCALL):
	OPNUM = 1
	structure = (
			('pDiskIdArray', VDS_OBJECT_ID),
			('ulCount', UNSIGNED_LONG),
			('bForce', BOOLEAN)
		)
class UninstallDisksResponse(NDRCALL):
	structure = (
			('pDiskIdArray', VDS_OBJECT_ID),
			('ulCount', UNSIGNED_LONG),
			('bForce', BOOLEAN)
		)
OPNUMS = {0 : 	(GetDiskIdFromLunInfo, GetDiskIdFromLunInfoResponse),1 : 	(UninstallDisks, UninstallDisksResponse)}
#################################################################################
#IVdsServiceHba Definition
#################################################################################
MSRPC_UUID_IVDSSERVICEHBA = uuidtup_to_bin(('0ac13689-3134-47c6-a17c-4669216801be','0.0'))
class QueryHbaPorts(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryHbaPortsResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(QueryHbaPorts, QueryHbaPortsResponse)}
#################################################################################
#IVdsServiceIscsi Definition
#################################################################################
MSRPC_UUID_IVDSSERVICEISCSI = uuidtup_to_bin(('14fbe036-3ed7-4e10-90e9-a5ff991aff01','0.0'))
class GetInitiatorName(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetInitiatorNameResponse(NDRCALL):
	structure = (
		)
class QueryInitiatorAdapters(NDRCALL):
	OPNUM = 1
	structure = (
		)
class QueryInitiatorAdaptersResponse(NDRCALL):
	structure = (
		)
class Opnum05NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum05NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum06NotUsedOnWire(NDRCALL):
	OPNUM = 3
	structure = (
		)
class Opnum06NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum07NotUsedOnWire(NDRCALL):
	OPNUM = 4
	structure = (
		)
class Opnum07NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class SetInitiatorSharedSecret(NDRCALL):
	OPNUM = 5
	structure = 		(		('pInitiatorSharedSecret', VDS_ISCSI_SHARED_SECRET), 		('targetId', VDS_OBJECT_ID))
class SetInitiatorSharedSecretResponse(NDRCALL):
	structure = 		(		('pInitiatorSharedSecret', VDS_ISCSI_SHARED_SECRET), 		('targetId', VDS_OBJECT_ID))
class Opnum09NotUsedOnWire(NDRCALL):
	OPNUM = 6
	structure = (
		)
class Opnum09NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetInitiatorName, GetInitiatorNameResponse),1 : 	(QueryInitiatorAdapters, QueryInitiatorAdaptersResponse),2 : 	(Opnum05NotUsedOnWire, Opnum05NotUsedOnWireResponse),3 : 	(Opnum06NotUsedOnWire, Opnum06NotUsedOnWireResponse),4 : 	(Opnum07NotUsedOnWire, Opnum07NotUsedOnWireResponse),5 : 	(SetInitiatorSharedSecret, SetInitiatorSharedSecretResponse),6 : 	(Opnum09NotUsedOnWire, Opnum09NotUsedOnWireResponse)}
#################################################################################
#IVdsServiceSAN Definition
#################################################################################
MSRPC_UUID_IVDSSERVICESAN = uuidtup_to_bin(('FC5D23E8-A88B-415-8E0-22735630','0.0'))
class GetSANPolicy(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetSANPolicyResponse(NDRCALL):
	structure = (
		)
class SetSANPolicy(NDRCALL):
	OPNUM = 1
	structure = (
			('SanPolicy', VDS_SAN_POLICY)
		)
class SetSANPolicyResponse(NDRCALL):
	structure = (
			('SanPolicy', VDS_SAN_POLICY)
		)
OPNUMS = {0 : 	(GetSANPolicy, GetSANPolicyResponse),1 : 	(SetSANPolicy, SetSANPolicyResponse)}
#################################################################################
#IVdsServiceSw Definition
#################################################################################
MSRPC_UUID_IVDSSERVICESW = uuidtup_to_bin(('15fc031c-0652-4306-b2c3-f558b8f837e2','0.0'))
class GetDiskObject(NDRCALL):
	OPNUM = 0
	structure = (
			('pwszDeviceID', LPCWSTR)
		)
class GetDiskObjectResponse(NDRCALL):
	structure = (
			('pwszDeviceID', LPCWSTR)
		)
OPNUMS = {0 : 	(GetDiskObject, GetDiskObjectResponse)}
#################################################################################
#IVdsHbaPort Definition
#################################################################################
MSRPC_UUID_IVDSHBAPORT = uuidtup_to_bin(('2abd757f-2851-4997-9a13-47d2a885d6ca','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class SetAllPathStatuses(NDRCALL):
	OPNUM = 1
	structure = (
			('status', VDS_PATH_STATUS)
		)
class SetAllPathStatusesResponse(NDRCALL):
	structure = (
			('status', VDS_PATH_STATUS)
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(SetAllPathStatuses, SetAllPathStatusesResponse)}
#################################################################################
#IVdsIscsiInitiatorAdapter Definition
#################################################################################
MSRPC_UUID_IVDSISCSIINITIATORADAPTER = uuidtup_to_bin(('b07fedd4-1682-4440-9189-a39b55194dc5','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class QueryInitiatorPortals(NDRCALL):
	OPNUM = 1
	structure = (
		)
class QueryInitiatorPortalsResponse(NDRCALL):
	structure = (
		)
class Opnum05NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum05NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum06NotUsedOnWire(NDRCALL):
	OPNUM = 3
	structure = (
		)
class Opnum06NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(QueryInitiatorPortals, QueryInitiatorPortalsResponse),2 : 	(Opnum05NotUsedOnWire, Opnum05NotUsedOnWireResponse),3 : 	(Opnum06NotUsedOnWire, Opnum06NotUsedOnWireResponse)}
#################################################################################
#IVdsIscsiInitiatorPortal Definition
#################################################################################
MSRPC_UUID_IVDSISCSIINITIATORPORTAL = uuidtup_to_bin(('38a0a9ab-7cc8-4693-ac07-1f28bd03c3da','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetInitiatorAdapter(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetInitiatorAdapterResponse(NDRCALL):
	structure = (
		)
class Opnum05NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum05NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum06NotUsedOnWire(NDRCALL):
	OPNUM = 3
	structure = (
		)
class Opnum06NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum07NotUsedOnWire(NDRCALL):
	OPNUM = 4
	structure = (
		)
class Opnum07NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetInitiatorAdapter, GetInitiatorAdapterResponse),2 : 	(Opnum05NotUsedOnWire, Opnum05NotUsedOnWireResponse),3 : 	(Opnum06NotUsedOnWire, Opnum06NotUsedOnWireResponse),4 : 	(Opnum07NotUsedOnWire, Opnum07NotUsedOnWireResponse)}
#################################################################################
#IVdsProvider Definition
#################################################################################
MSRPC_UUID_IVDSPROVIDER = uuidtup_to_bin(('10c5e575-7984-4e81-a56b-431f5f92ae42','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse)}
#################################################################################
#IVdsSwProvider Definition
#################################################################################
MSRPC_UUID_IVDSSWPROVIDER = uuidtup_to_bin(('9aa58360-ce33-4f92-b658-ed24b14425b8','0.0'))
class QueryPacks(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryPacksResponse(NDRCALL):
	structure = (
		)
class CreatePack(NDRCALL):
	OPNUM = 1
	structure = (
		)
class CreatePackResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(QueryPacks, QueryPacksResponse),1 : 	(CreatePack, CreatePackResponse)}
#################################################################################
#IVdsHwProvider Definition
#################################################################################
MSRPC_UUID_IVDSHWPROVIDER = uuidtup_to_bin(('d99bdaae-b13a-4178-9db-e27f16b4603e','0.0'))
class QuerySubSystems(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QuerySubSystemsResponse(NDRCALL):
	structure = (
		)
class Opnum04NotUsedOnWire(NDRCALL):
	OPNUM = 1
	structure = (
		)
class Opnum04NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class Opnum05NotUsedOnWire(NDRCALL):
	OPNUM = 2
	structure = (
		)
class Opnum05NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(QuerySubSystems, QuerySubSystemsResponse),1 : 	(Opnum04NotUsedOnWire, Opnum04NotUsedOnWireResponse),2 : 	(Opnum05NotUsedOnWire, Opnum05NotUsedOnWireResponse)}
#################################################################################
#IVdsVdProvider Definition
#################################################################################
MSRPC_UUID_IVDSVDPROVIDER = uuidtup_to_bin(('b481498c-8354-459-840-0dd2832a91f','0.0'))
class QueryVDisks(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryVDisksResponse(NDRCALL):
	structure = (
		)
class CreateVDisk(NDRCALL):
	OPNUM = 1
	structure = (
			('VirtualDeviceType', PVIRTUAL_STORAGE_TYPE),
			('pPath', LPWSTR),
			('pStringSecurityDescriptor', LPWSTR),
			('Flags', CREATE_VIRTUAL_DISK_FLAG),
			('ProviderSpecificFlags', ULONG),
			('Reserved', ULONG),
			('pCreateDiskParameters', PVDS_CREATE_VDISK_PARAMETERS),
			('ppAsync', IVDSASYNC)
		)
class CreateVDiskResponse(NDRCALL):
	structure = (
			('VirtualDeviceType', PVIRTUAL_STORAGE_TYPE),
			('pPath', LPWSTR),
			('pStringSecurityDescriptor', LPWSTR),
			('Flags', CREATE_VIRTUAL_DISK_FLAG),
			('ProviderSpecificFlags', ULONG),
			('Reserved', ULONG),
			('pCreateDiskParameters', PVDS_CREATE_VDISK_PARAMETERS),
			('ppAsync', IVDSASYNC)
		)
class AddVDisk(NDRCALL):
	OPNUM = 2
	structure = 		(		('VirtualDeviceType', PVIRTUAL_STORAGE_TYPE), 		('pPath', LPWSTR))
class AddVDiskResponse(NDRCALL):
	structure = 		(		('VirtualDeviceType', PVIRTUAL_STORAGE_TYPE), 		('pPath', LPWSTR))
class GetDiskFromVDisk(NDRCALL):
	OPNUM = 3
	structure = (
			('pVDisk', IVDSVDISK)
		)
class GetDiskFromVDiskResponse(NDRCALL):
	structure = (
			('pVDisk', IVDSVDISK)
		)
class GetVDiskFromDisk(NDRCALL):
	OPNUM = 4
	structure = (
			('pDisk', IVDSDISK)
		)
class GetVDiskFromDiskResponse(NDRCALL):
	structure = (
			('pDisk', IVDSDISK)
		)
OPNUMS = {0 : 	(QueryVDisks, QueryVDisksResponse),1 : 	(CreateVDisk, CreateVDiskResponse),2 : 	(AddVDisk, AddVDiskResponse),3 : 	(GetDiskFromVDisk, GetDiskFromVDiskResponse),4 : 	(GetVDiskFromDisk, GetVDiskFromDiskResponse)}
#################################################################################
#IVdsSubSystemImportTarget Definition
#################################################################################
MSRPC_UUID_IVDSSUBSYSTEMIMPORTTARGET = uuidtup_to_bin(('83bfb87f-43fb-4903-baa6-127f01029eec','0.0'))
class GetImportTarget(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetImportTargetResponse(NDRCALL):
	structure = (
		)
class SetImportTarget(NDRCALL):
	OPNUM = 1
	structure = (
			('pwszIscsiName', LPWSTR)
		)
class SetImportTargetResponse(NDRCALL):
	structure = (
			('pwszIscsiName', LPWSTR)
		)
OPNUMS = {0 : 	(GetImportTarget, GetImportTargetResponse),1 : 	(SetImportTarget, SetImportTargetResponse)}
#################################################################################
#IVdsPack Definition
#################################################################################
MSRPC_UUID_IVDSPACK = uuidtup_to_bin(('3b69d7f5-9d94-4648-91ca-79939ba263bf','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetProvider(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetProviderResponse(NDRCALL):
	structure = (
		)
class QueryVolumes(NDRCALL):
	OPNUM = 2
	structure = (
		)
class QueryVolumesResponse(NDRCALL):
	structure = (
		)
class QueryDisks(NDRCALL):
	OPNUM = 3
	structure = (
		)
class QueryDisksResponse(NDRCALL):
	structure = (
		)
class CreateVolume(NDRCALL):
	OPNUM = 4
	structure = (
			('type', VDS_VOLUME_TYPE),
			('pInputDiskArray', VDS_INPUT_DISK),
			('lNumberOfDisks', LONG),
			('ulStripeSize', UNSIGNED_LONG)
		)
class CreateVolumeResponse(NDRCALL):
	structure = (
			('type', VDS_VOLUME_TYPE),
			('pInputDiskArray', VDS_INPUT_DISK),
			('lNumberOfDisks', LONG),
			('ulStripeSize', UNSIGNED_LONG)
		)
class AddDisk(NDRCALL):
	OPNUM = 5
	structure = (
			('DiskId', VDS_OBJECT_ID),
			('PartitionStyle', VDS_PARTITION_STYLE),
			('bAsHotSpare', LONG)
		)
class AddDiskResponse(NDRCALL):
	structure = (
			('DiskId', VDS_OBJECT_ID),
			('PartitionStyle', VDS_PARTITION_STYLE),
			('bAsHotSpare', LONG)
		)
class MigrateDisks(NDRCALL):
	OPNUM = 6
	structure = (
			('pDiskArray', VDS_OBJECT_ID),
			('lNumberOfDisks', LONG),
			('TargetPack', VDS_OBJECT_ID),
			('bForce', LONG),
			('bQueryOnly', LONG)
		)
class MigrateDisksResponse(NDRCALL):
	structure = (
			('pDiskArray', VDS_OBJECT_ID),
			('lNumberOfDisks', LONG),
			('TargetPack', VDS_OBJECT_ID),
			('bForce', LONG),
			('bQueryOnly', LONG)
		)
class Opnum10NotUsedOnWire(NDRCALL):
	OPNUM = 7
	structure = (
		)
class Opnum10NotUsedOnWireResponse(NDRCALL):
	structure = (
		)
class RemoveMissingDisk(NDRCALL):
	OPNUM = 8
	structure = (
			('DiskId', VDS_OBJECT_ID)
		)
class RemoveMissingDiskResponse(NDRCALL):
	structure = (
			('DiskId', VDS_OBJECT_ID)
		)
class Recover(NDRCALL):
	OPNUM = 9
	structure = (
		)
class RecoverResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetProvider, GetProviderResponse),2 : 	(QueryVolumes, QueryVolumesResponse),3 : 	(QueryDisks, QueryDisksResponse),4 : 	(CreateVolume, CreateVolumeResponse),5 : 	(AddDisk, AddDiskResponse),6 : 	(MigrateDisks, MigrateDisksResponse),7 : 	(Opnum10NotUsedOnWire, Opnum10NotUsedOnWireResponse),8 : 	(RemoveMissingDisk, RemoveMissingDiskResponse),9 : 	(Recover, RecoverResponse)}
#################################################################################
#IVdsPack2 Definition
#################################################################################
MSRPC_UUID_IVDSPACK2 = uuidtup_to_bin(('13B50BFF-290A-47DD-8558-B7C58DB1A71A','0.0'))
class CreateVolume2(NDRCALL):
	OPNUM = 0
	structure = (
			('type', VDS_VOLUME_TYPE),
			('pInputDiskArray', VDS_INPUT_DISK),
			('lNumberOfDisks', LONG),
			('ulStripeSize', UNSIGNED_LONG),
			('ulAlign', UNSIGNED_LONG)
		)
class CreateVolume2Response(NDRCALL):
	structure = (
			('type', VDS_VOLUME_TYPE),
			('pInputDiskArray', VDS_INPUT_DISK),
			('lNumberOfDisks', LONG),
			('ulStripeSize', UNSIGNED_LONG),
			('ulAlign', UNSIGNED_LONG)
		)
OPNUMS = {0 : 	(CreateVolume2, CreateVolume2Response)}
#################################################################################
#IVdsDisk Definition
#################################################################################
MSRPC_UUID_IVDSDISK = uuidtup_to_bin(('07e5c822-f00c-47a1-8fce-b244da56fd06','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetPack(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetPackResponse(NDRCALL):
	structure = (
		)
class GetIdentificationData(NDRCALL):
	OPNUM = 2
	structure = (
		)
class GetIdentificationDataResponse(NDRCALL):
	structure = (
		)
class QueryExtents(NDRCALL):
	OPNUM = 3
	structure = (
		)
class QueryExtentsResponse(NDRCALL):
	structure = (
		)
class ConvertStyle(NDRCALL):
	OPNUM = 4
	structure = (
			('NewStyle', VDS_PARTITION_STYLE)
		)
class ConvertStyleResponse(NDRCALL):
	structure = (
			('NewStyle', VDS_PARTITION_STYLE)
		)
class SetFlags(NDRCALL):
	OPNUM = 5
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class SetFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFlags(NDRCALL):
	OPNUM = 6
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetPack, GetPackResponse),2 : 	(GetIdentificationData, GetIdentificationDataResponse),3 : 	(QueryExtents, QueryExtentsResponse),4 : 	(ConvertStyle, ConvertStyleResponse),5 : 	(SetFlags, SetFlagsResponse),6 : 	(ClearFlags, ClearFlagsResponse)}
#################################################################################
#IVdsDisk2 Definition
#################################################################################
MSRPC_UUID_IVDSDISK2 = uuidtup_to_bin(('40F73C8B-687D-4a13-8D96-3D7F2E683936','0.0'))
class SetSANMode(NDRCALL):
	OPNUM = 0
	structure = (
			('bEnable', LONG)
		)
class SetSANModeResponse(NDRCALL):
	structure = (
			('bEnable', LONG)
		)
OPNUMS = {0 : 	(SetSANMode, SetSANModeResponse)}
#################################################################################
#IVdsDisk3 Definition
#################################################################################
MSRPC_UUID_IVDSDISK3 = uuidtup_to_bin(('8F4B2F5D-EC15-4357-992F-473EF10975B9','0.0'))
class GetProperties2(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetProperties2Response(NDRCALL):
	structure = (
		)
class QueryFreeExtents(NDRCALL):
	OPNUM = 1
	structure = (
			('ulAlign', ULONG)
		)
class QueryFreeExtentsResponse(NDRCALL):
	structure = (
			('ulAlign', ULONG)
		)
OPNUMS = {0 : 	(GetProperties2, GetProperties2Response),1 : 	(QueryFreeExtents, QueryFreeExtentsResponse)}
#################################################################################
#IVdsAdvancedDisk Definition
#################################################################################
MSRPC_UUID_IVDSADVANCEDDISK = uuidtup_to_bin(('6e6f6b40-977c-4069-bddd-ac710059f8c0','0.0'))
class GetPartitionProperties(NDRCALL):
	OPNUM = 0
	structure = (
			('ullOffset', ULONGLONG)
		)
class GetPartitionPropertiesResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG)
		)
class QueryPartitions(NDRCALL):
	OPNUM = 1
	structure = (
		)
class QueryPartitionsResponse(NDRCALL):
	structure = (
		)
class CreatePartition(NDRCALL):
	OPNUM = 2
	structure = (
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('para', CREATE_PARTITION_PARAMETERS)
		)
class CreatePartitionResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('para', CREATE_PARTITION_PARAMETERS)
		)
class DeletePartition(NDRCALL):
	OPNUM = 3
	structure = (
			('ullOffset', ULONGLONG),
			('bForce', LONG),
			('bForceProtected', LONG)
		)
class DeletePartitionResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('bForce', LONG),
			('bForceProtected', LONG)
		)
class ChangeAttributes(NDRCALL):
	OPNUM = 4
	structure = 		(		('ullOffset', ULONGLONG), 		('para', CHANGE_ATTRIBUTES_PARAMETERS))
class ChangeAttributesResponse(NDRCALL):
	structure = 		(		('ullOffset', ULONGLONG), 		('para', CHANGE_ATTRIBUTES_PARAMETERS))
class AssignDriveLetter(NDRCALL):
	OPNUM = 5
	structure = 		(		('ullOffset', ULONGLONG), 		('wcLetter', WCHAR))
class AssignDriveLetterResponse(NDRCALL):
	structure = 		(		('ullOffset', ULONGLONG), 		('wcLetter', WCHAR))
class DeleteDriveLetter(NDRCALL):
	OPNUM = 6
	structure = 		(		('ullOffset', ULONGLONG), 		('wcLetter', WCHAR))
class DeleteDriveLetterResponse(NDRCALL):
	structure = 		(		('ullOffset', ULONGLONG), 		('wcLetter', WCHAR))
class GetDriveLetter(NDRCALL):
	OPNUM = 7
	structure = (
			('ullOffset', ULONGLONG)
		)
class GetDriveLetterResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG)
		)
class FormatPartition(NDRCALL):
	OPNUM = 8
	structure = (
			('ullOffset', ULONGLONG),
			('type', VDS_FILE_SYSTEM_TYPE),
			('pwszLabel', WCHAR),
			('dwUnitAllocationSize', DWORD),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class FormatPartitionResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('type', VDS_FILE_SYSTEM_TYPE),
			('pwszLabel', WCHAR),
			('dwUnitAllocationSize', DWORD),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class Clean(NDRCALL):
	OPNUM = 9
	structure = (
			('bForce', LONG),
			('bForceOEM', LONG),
			('bFullClean', LONG)
		)
class CleanResponse(NDRCALL):
	structure = (
			('bForce', LONG),
			('bForceOEM', LONG),
			('bFullClean', LONG)
		)
OPNUMS = {0 : 	(GetPartitionProperties, GetPartitionPropertiesResponse),1 : 	(QueryPartitions, QueryPartitionsResponse),2 : 	(CreatePartition, CreatePartitionResponse),3 : 	(DeletePartition, DeletePartitionResponse),4 : 	(ChangeAttributes, ChangeAttributesResponse),5 : 	(AssignDriveLetter, AssignDriveLetterResponse),6 : 	(DeleteDriveLetter, DeleteDriveLetterResponse),7 : 	(GetDriveLetter, GetDriveLetterResponse),8 : 	(FormatPartition, FormatPartitionResponse),9 : 	(Clean, CleanResponse)}
#################################################################################
#IVdsAdvancedDisk2 Definition
#################################################################################
MSRPC_UUID_IVDSADVANCEDDISK2 = uuidtup_to_bin(('9723f420-9355-42de-ab66-e31bb15beeac','0.0'))
class ChangePartitionType(NDRCALL):
	OPNUM = 0
	structure = (
			('ullOffset', ULONGLONG),
			('bForce', LONG),
			('para', CHANGE_PARTITION_TYPE_PARAMETERS)
		)
class ChangePartitionTypeResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('bForce', LONG),
			('para', CHANGE_PARTITION_TYPE_PARAMETERS)
		)
OPNUMS = {0 : 	(ChangePartitionType, ChangePartitionTypeResponse)}
#################################################################################
#IVdsAdvancedDisk3 Definition
#################################################################################
MSRPC_UUID_IVDSADVANCEDDISK3 = uuidtup_to_bin(('3858C0D5-0F35-4BF5-9714-69874963BC36','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetUniqueId(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetUniqueIdResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetUniqueId, GetUniqueIdResponse)}
#################################################################################
#IVdsCreatePartitionEx Definition
#################################################################################
MSRPC_UUID_IVDSCREATEPARTITIONEX = uuidtup_to_bin(('9882f547-cfc3-420b-9750-00dfbec50662','0.0'))
class CreatePartitionEx(NDRCALL):
	OPNUM = 0
	structure = (
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('ulAlign', UNSIGNED_LONG),
			('para', CREATE_PARTITION_PARAMETERS)
		)
class CreatePartitionExResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('ullSize', ULONGLONG),
			('ulAlign', UNSIGNED_LONG),
			('para', CREATE_PARTITION_PARAMETERS)
		)
OPNUMS = {0 : 	(CreatePartitionEx, CreatePartitionExResponse)}
#################################################################################
#IVdsDiskOnline Definition
#################################################################################
MSRPC_UUID_IVDSDISKONLINE = uuidtup_to_bin(('90681B1D-6A7F-48e8-9061-31B7AA125322','0.0'))
class Online(NDRCALL):
	OPNUM = 0
	structure = (
		)
class OnlineResponse(NDRCALL):
	structure = (
		)
class Offline(NDRCALL):
	OPNUM = 1
	structure = (
		)
class OfflineResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Online, OnlineResponse),1 : 	(Offline, OfflineResponse)}
#################################################################################
#IVdsDiskPartitionMF Definition
#################################################################################
MSRPC_UUID_IVDSDISKPARTITIONMF = uuidtup_to_bin(('538684e0-ba3d-4bc0-aca9-164aff85c2a9','0.0'))
class GetPartitionFileSystemProperties(NDRCALL):
	OPNUM = 0
	structure = (
			('ullOffset', ULONGLONG)
		)
class GetPartitionFileSystemPropertiesResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG)
		)
class GetPartitionFileSystemTypeName(NDRCALL):
	OPNUM = 1
	structure = (
			('ullOffset', ULONGLONG)
		)
class GetPartitionFileSystemTypeNameResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG)
		)
class QueryPartitionFileSystemFormatSupport(NDRCALL):
	OPNUM = 2
	structure = (
			('ullOffset', ULONGLONG)
		)
class QueryPartitionFileSystemFormatSupportResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG)
		)
class FormatPartitionEx(NDRCALL):
	OPNUM = 3
	structure = (
			('ullOffset', ULONGLONG),
			('pwszFileSystemTypeName', WCHAR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', WCHAR),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class FormatPartitionExResponse(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('pwszFileSystemTypeName', WCHAR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', WCHAR),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
OPNUMS = {0 : 	(GetPartitionFileSystemProperties, GetPartitionFileSystemPropertiesResponse),1 : 	(GetPartitionFileSystemTypeName, GetPartitionFileSystemTypeNameResponse),2 : 	(QueryPartitionFileSystemFormatSupport, QueryPartitionFileSystemFormatSupportResponse),3 : 	(FormatPartitionEx, FormatPartitionExResponse)}
#################################################################################
#IVdsDiskPartitionMF2 Definition
#################################################################################
MSRPC_UUID_IVDSDISKPARTITIONMF2 = uuidtup_to_bin(('9CBE50CA-F2D2-4bf4-ACE1-96896B729625','0.0'))
class FormatPartitionEx2(NDRCALL):
	OPNUM = 0
	structure = (
			('ullOffset', ULONGLONG),
			('pwszFileSystemTypeName', LPWSTR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', LPWSTR),
			('Options', DWORD)
		)
class FormatPartitionEx2Response(NDRCALL):
	structure = (
			('ullOffset', ULONGLONG),
			('pwszFileSystemTypeName', LPWSTR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', LPWSTR),
			('Options', DWORD)
		)
OPNUMS = {0 : 	(FormatPartitionEx2, FormatPartitionEx2Response)}
#################################################################################
#IVdsRemovable Definition
#################################################################################
MSRPC_UUID_IVDSREMOVABLE = uuidtup_to_bin(('0316560b-5db4-4ed9-bbb5-213436ddc0d9','0.0'))
class QueryMedia(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryMediaResponse(NDRCALL):
	structure = (
		)
class Eject(NDRCALL):
	OPNUM = 1
	structure = (
		)
class EjectResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(QueryMedia, QueryMediaResponse),1 : 	(Eject, EjectResponse)}
#################################################################################
#IVdsVolume Definition
#################################################################################
MSRPC_UUID_IVDSVOLUME = uuidtup_to_bin(('88306bb2-e71f-478c-86a2-79da200a0f11','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetPack(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetPackResponse(NDRCALL):
	structure = (
		)
class QueryPlexes(NDRCALL):
	OPNUM = 2
	structure = (
		)
class QueryPlexesResponse(NDRCALL):
	structure = (
		)
class Extend(NDRCALL):
	OPNUM = 3
	structure = 		(		('pInputDiskArray', VDS_INPUT_DISK), 		('lNumberOfDisks', LONG))
class ExtendResponse(NDRCALL):
	structure = 		(		('pInputDiskArray', VDS_INPUT_DISK), 		('lNumberOfDisks', LONG))
class Shrink(NDRCALL):
	OPNUM = 4
	structure = (
			('ullNumberOfBytesToRemove', ULONGLONG)
		)
class ShrinkResponse(NDRCALL):
	structure = (
			('ullNumberOfBytesToRemove', ULONGLONG)
		)
class AddPlex(NDRCALL):
	OPNUM = 5
	structure = (
			('VolumeId', VDS_OBJECT_ID)
		)
class AddPlexResponse(NDRCALL):
	structure = (
			('VolumeId', VDS_OBJECT_ID)
		)
class BreakPlex(NDRCALL):
	OPNUM = 6
	structure = (
			('plexId', VDS_OBJECT_ID)
		)
class BreakPlexResponse(NDRCALL):
	structure = (
			('plexId', VDS_OBJECT_ID)
		)
class RemovePlex(NDRCALL):
	OPNUM = 7
	structure = (
			('plexId', VDS_OBJECT_ID)
		)
class RemovePlexResponse(NDRCALL):
	structure = (
			('plexId', VDS_OBJECT_ID)
		)
class Delete(NDRCALL):
	OPNUM = 8
	structure = (
			('bForce', LONG)
		)
class DeleteResponse(NDRCALL):
	structure = (
			('bForce', LONG)
		)
class SetFlags(NDRCALL):
	OPNUM = 9
	structure = 		(		('ulFlags', UNSIGNED_LONG), 		('bRevertOnClose', LONG))
class SetFlagsResponse(NDRCALL):
	structure = 		(		('ulFlags', UNSIGNED_LONG), 		('bRevertOnClose', LONG))
class ClearFlags(NDRCALL):
	OPNUM = 10
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetPack, GetPackResponse),2 : 	(QueryPlexes, QueryPlexesResponse),3 : 	(Extend, ExtendResponse),4 : 	(Shrink, ShrinkResponse),5 : 	(AddPlex, AddPlexResponse),6 : 	(BreakPlex, BreakPlexResponse),7 : 	(RemovePlex, RemovePlexResponse),8 : 	(Delete, DeleteResponse),9 : 	(SetFlags, SetFlagsResponse),10 : 	(ClearFlags, ClearFlagsResponse)}
#################################################################################
#IVdsVolume2 Definition
#################################################################################
MSRPC_UUID_IVDSVOLUME2 = uuidtup_to_bin(('72AE6713-DCBB-4a03-B36B-371F6AC6B53D','0.0'))
class GetProperties2(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetProperties2Response(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(GetProperties2, GetProperties2Response)}
#################################################################################
#IVdsVolumeMF Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMEMF = uuidtup_to_bin(('ee2d5ded-6236-4169-931-b9778ce03dc6','0.0'))
class GetFileSystemProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetFileSystemPropertiesResponse(NDRCALL):
	structure = (
		)
class Format(NDRCALL):
	OPNUM = 1
	structure = (
			('type', VDS_FILE_SYSTEM_TYPE),
			('pwszLabel', WCHAR),
			('dwUnitAllocationSize', DWORD),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class FormatResponse(NDRCALL):
	structure = (
			('type', VDS_FILE_SYSTEM_TYPE),
			('pwszLabel', WCHAR),
			('dwUnitAllocationSize', DWORD),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class AddAccessPath(NDRCALL):
	OPNUM = 2
	structure = (
			('pwszPath', WCHAR)
		)
class AddAccessPathResponse(NDRCALL):
	structure = (
			('pwszPath', WCHAR)
		)
class QueryAccessPaths(NDRCALL):
	OPNUM = 3
	structure = (
		)
class QueryAccessPathsResponse(NDRCALL):
	structure = (
		)
class QueryReparsePoints(NDRCALL):
	OPNUM = 4
	structure = (
		)
class QueryReparsePointsResponse(NDRCALL):
	structure = (
		)
class DeleteAccessPath(NDRCALL):
	OPNUM = 5
	structure = 		(		('pwszPath', WCHAR), 		('bForce', LONG))
class DeleteAccessPathResponse(NDRCALL):
	structure = 		(		('pwszPath', WCHAR), 		('bForce', LONG))
class Mount(NDRCALL):
	OPNUM = 6
	structure = (
		)
class MountResponse(NDRCALL):
	structure = (
		)
class Dismount(NDRCALL):
	OPNUM = 7
	structure = 		(		('bForce', LONG), 		('bPermanent', LONG))
class DismountResponse(NDRCALL):
	structure = 		(		('bForce', LONG), 		('bPermanent', LONG))
class SetFileSystemFlags(NDRCALL):
	OPNUM = 8
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class SetFileSystemFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFileSystemFlags(NDRCALL):
	OPNUM = 9
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
class ClearFileSystemFlagsResponse(NDRCALL):
	structure = (
			('ulFlags', UNSIGNED_LONG)
		)
OPNUMS = {0 : 	(GetFileSystemProperties, GetFileSystemPropertiesResponse),1 : 	(Format, FormatResponse),2 : 	(AddAccessPath, AddAccessPathResponse),3 : 	(QueryAccessPaths, QueryAccessPathsResponse),4 : 	(QueryReparsePoints, QueryReparsePointsResponse),5 : 	(DeleteAccessPath, DeleteAccessPathResponse),6 : 	(Mount, MountResponse),7 : 	(Dismount, DismountResponse),8 : 	(SetFileSystemFlags, SetFileSystemFlagsResponse),9 : 	(ClearFileSystemFlags, ClearFileSystemFlagsResponse)}
#################################################################################
#IVdsVolumeMF2 Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMEMF2 = uuidtup_to_bin(('4dbcee9a-6343-4651-b85f-5e75d74d983c','0.0'))
class GetFileSystemTypeName(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetFileSystemTypeNameResponse(NDRCALL):
	structure = (
		)
class QueryFileSystemFormatSupport(NDRCALL):
	OPNUM = 1
	structure = (
		)
class QueryFileSystemFormatSupportResponse(NDRCALL):
	structure = (
		)
class FormatEx(NDRCALL):
	OPNUM = 2
	structure = (
			('pwszFileSystemTypeName', WCHAR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', WCHAR),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
class FormatExResponse(NDRCALL):
	structure = (
			('pwszFileSystemTypeName', WCHAR),
			('usFileSystemRevision', UNSIGNED_SHORT),
			('ulDesiredUnitAllocationSize', UNSIGNED_LONG),
			('pwszLabel', WCHAR),
			('bForce', LONG),
			('bQuickFormat', LONG),
			('bEnableCompression', LONG)
		)
OPNUMS = {0 : 	(GetFileSystemTypeName, GetFileSystemTypeNameResponse),1 : 	(QueryFileSystemFormatSupport, QueryFileSystemFormatSupportResponse),2 : 	(FormatEx, FormatExResponse)}
#################################################################################
#IVdsVolumeMF3 Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMEMF3 = uuidtup_to_bin(('6788FAF9-214E-4b85-BA59-266953616E09','0.0'))
class QueryVolumeGuidPathnames(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryVolumeGuidPathnamesResponse(NDRCALL):
	structure = (
		)
class FormatEx2(NDRCALL):
	OPNUM = 1
	structure = (
			('pwszFileSystemTypeName', LPWSTR),
			('usFileSystemRevision', USHORT),
			('ulDesiredUnitAllocationSize', ULONG),
			('pwszLabel', LPWSTR),
			('Options', DWORD)
		)
class FormatEx2Response(NDRCALL):
	structure = (
			('pwszFileSystemTypeName', LPWSTR),
			('usFileSystemRevision', USHORT),
			('ulDesiredUnitAllocationSize', ULONG),
			('pwszLabel', LPWSTR),
			('Options', DWORD)
		)
class OfflineVolume(NDRCALL):
	OPNUM = 2
	structure = (
		)
class OfflineVolumeResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(QueryVolumeGuidPathnames, QueryVolumeGuidPathnamesResponse),1 : 	(FormatEx2, FormatEx2Response),2 : 	(OfflineVolume, OfflineVolumeResponse)}
#################################################################################
#IVdsVolumeShrink Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMESHRINK = uuidtup_to_bin(('d68168c9-822-485-b6e9-747074958','0.0'))
class QueryMaxReclaimableBytes(NDRCALL):
	OPNUM = 0
	structure = (
		)
class QueryMaxReclaimableBytesResponse(NDRCALL):
	structure = (
		)
class Shrink(NDRCALL):
	OPNUM = 1
	structure = 		(		('ullDesiredNumberOfReclaimableBytes', ULONGLONG), 		('ullMinNumberOfReclaimableBytes', ULONGLONG))
class ShrinkResponse(NDRCALL):
	structure = 		(		('ullDesiredNumberOfReclaimableBytes', ULONGLONG), 		('ullMinNumberOfReclaimableBytes', ULONGLONG))
OPNUMS = {0 : 	(QueryMaxReclaimableBytes, QueryMaxReclaimableBytesResponse),1 : 	(Shrink, ShrinkResponse)}
#################################################################################
#IVdsVolumeOnline Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMEONLINE = uuidtup_to_bin(('1BE2275A-B315-4f70-9E44-879B3A2A53F2','0.0'))
class Online(NDRCALL):
	OPNUM = 0
	structure = (
		)
class OnlineResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Online, OnlineResponse)}
#################################################################################
#IVdsVolumePlex Definition
#################################################################################
MSRPC_UUID_IVDSVOLUMEPLEX = uuidtup_to_bin(('4daa0135-e1d1-40f1-aaa5-3cc1e53221c3','0.0'))
class GetProperties(NDRCALL):
	OPNUM = 0
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetVolume(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetVolumeResponse(NDRCALL):
	structure = (
		)
class QueryExtents(NDRCALL):
	OPNUM = 2
	structure = (
		)
class QueryExtentsResponse(NDRCALL):
	structure = (
		)
class Repair(NDRCALL):
	OPNUM = 3
	structure = 		(		('pInputDiskArray', VDS_INPUT_DISK), 		('lNumberOfDisks', LONG))
class RepairResponse(NDRCALL):
	structure = 		(		('pInputDiskArray', VDS_INPUT_DISK), 		('lNumberOfDisks', LONG))
OPNUMS = {0 : 	(GetProperties, GetPropertiesResponse),1 : 	(GetVolume, GetVolumeResponse),2 : 	(QueryExtents, QueryExtentsResponse),3 : 	(Repair, RepairResponse)}
#################################################################################
#IVdsVDisk Definition
#################################################################################
MSRPC_UUID_IVDSVDISK = uuidtup_to_bin(('1e062b84-e5e6-4b4b-8a25-67b81e8f13e8','0.0'))
class Open(NDRCALL):
	OPNUM = 0
	structure = (
			('AccessMask', VIRTUAL_DISK_ACCESS_MASK),
			('Flags', OPEN_VIRTUAL_DISK_FLAG),
			('ReadWriteDepth', ULONG)
		)
class OpenResponse(NDRCALL):
	structure = (
			('AccessMask', VIRTUAL_DISK_ACCESS_MASK),
			('Flags', OPEN_VIRTUAL_DISK_FLAG),
			('ReadWriteDepth', ULONG)
		)
class GetProperties(NDRCALL):
	OPNUM = 1
	structure = (
		)
class GetPropertiesResponse(NDRCALL):
	structure = (
		)
class GetHostVolume(NDRCALL):
	OPNUM = 2
	structure = (
		)
class GetHostVolumeResponse(NDRCALL):
	structure = (
		)
class GetDeviceName(NDRCALL):
	OPNUM = 3
	structure = (
		)
class GetDeviceNameResponse(NDRCALL):
	structure = (
		)
OPNUMS = {0 : 	(Open, OpenResponse),1 : 	(GetProperties, GetPropertiesResponse),2 : 	(GetHostVolume, GetHostVolumeResponse),3 : 	(GetDeviceName, GetDeviceNameResponse)}
#################################################################################
#IVdsOpenVDisk Definition
#################################################################################
MSRPC_UUID_IVDSOPENVDISK = uuidtup_to_bin(('75c8f324-f715-4fe3-a28e-f9011b61a4a1','0.0'))
class Attach(NDRCALL):
	OPNUM = 0
	structure = (
			('pStringSecurityDescriptor', LPWSTR),
			('Flags', ATTACH_VIRTUAL_DISK_FLAG),
			('ProviderSpecificFlags', ULONG),
			('TimeoutInMs', ULONG)
		)
class AttachResponse(NDRCALL):
	structure = (
			('pStringSecurityDescriptor', LPWSTR),
			('Flags', ATTACH_VIRTUAL_DISK_FLAG),
			('ProviderSpecificFlags', ULONG),
			('TimeoutInMs', ULONG)
		)
class Detach(NDRCALL):
	OPNUM = 1
	structure = 		(		('Flags', DETACH_VIRTUAL_DISK_FLAG), 		('ProviderSpecificFlags', ULONG))
class DetachResponse(NDRCALL):
	structure = 		(		('Flags', DETACH_VIRTUAL_DISK_FLAG), 		('ProviderSpecificFlags', ULONG))
class DetachAndDelete(NDRCALL):
	OPNUM = 2
	structure = 		(		('Flags', DETACH_VIRTUAL_DISK_FLAG), 		('ProviderSpecificFlags', ULONG))
class DetachAndDeleteResponse(NDRCALL):
	structure = 		(		('Flags', DETACH_VIRTUAL_DISK_FLAG), 		('ProviderSpecificFlags', ULONG))
class Compact(NDRCALL):
	OPNUM = 3
	structure = 		(		('Flags', COMPACT_VIRTUAL_DISK_FLAG), 		('Reserved', ULONG))
class CompactResponse(NDRCALL):
	structure = 		(		('Flags', COMPACT_VIRTUAL_DISK_FLAG), 		('Reserved', ULONG))
class Merge(NDRCALL):
	OPNUM = 4
	structure = 		(		('Flags', MERGE_VIRTUAL_DISK_FLAG), 		('MergeDepth', ULONG))
class MergeResponse(NDRCALL):
	structure = 		(		('Flags', MERGE_VIRTUAL_DISK_FLAG), 		('MergeDepth', ULONG))
class Expand(NDRCALL):
	OPNUM = 5
	structure = 		(		('Flags', EXPAND_VIRTUAL_DISK_FLAG), 		('NewSize', ULONGLONG))
class ExpandResponse(NDRCALL):
	structure = 		(		('Flags', EXPAND_VIRTUAL_DISK_FLAG), 		('NewSize', ULONGLONG))
OPNUMS = {0 : 	(Attach, AttachResponse),1 : 	(Detach, DetachResponse),2 : 	(DetachAndDelete, DetachAndDeleteResponse),3 : 	(Compact, CompactResponse),4 : 	(Merge, MergeResponse),5 : 	(Expand, ExpandResponse)}
