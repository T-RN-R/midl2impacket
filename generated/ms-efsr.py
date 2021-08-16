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
#efsrpc Definition
#################################################################################
MSRPC_UUID_EFSRPC = uuidtup_to_bin(('c681d488-d850-110-852-0004d90f7e','0.0'))
PEXIMPORT_CONTEXT_HANDLE = VOID
EFS_EXIM_PIPE = PIPE UNSIGNED CHAR
class DATA_EFS_RPC_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_EFS_RPC_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_EFS_RPC_BLOB
			)
		)


class EFS_RPC_BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbData',
			DWORD
			),
			(
			'bData',
			PTR_EFS_RPC_BLOB
			)
		)


class EFS_COMPATIBILITY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'EfsVersion',
			DWORD
			)
		)


ALG_ID = UNSIGNED_INT
class DATA_EFS_HASH_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_EFS_HASH_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_EFS_HASH_BLOB
			)
		)


class EFS_HASH_BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbData',
			DWORD
			),
			(
			'bData',
			PTR_EFS_HASH_BLOB
			)
		)


class ENCRYPTION_CERTIFICATE_HASH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbTotalLength',
			DWORD
			),
			(
			'UserSid',
			RPC_SID
			),
			(
			'Hash',
			EFS_HASH_BLOB
			),
			(
			'lpDisplayInformation',
			WCHAR_T
			)
		)


class DATA_ENCRYPTION_CERTIFICATE_HASH_LIST(NDRUniConformantArray):
	item = ENCRYPTION_CERTIFICATE_HASH


class PTR_ENCRYPTION_CERTIFICATE_HASH_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_ENCRYPTION_CERTIFICATE_HASH_LIST
			)
		)


class ENCRYPTION_CERTIFICATE_HASH_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'nCert_Hash',
			DWORD
			),
			(
			'Users',
			PTR_ENCRYPTION_CERTIFICATE_HASH_LIST
			)
		)


class DATA_EFS_CERTIFICATE_BLOB(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PTR_EFS_CERTIFICATE_BLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_EFS_CERTIFICATE_BLOB
			)
		)


class EFS_CERTIFICATE_BLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwCertEncodingType',
			DWORD
			),
			(
			'cbData',
			DWORD
			),
			(
			'bData',
			PTR_EFS_CERTIFICATE_BLOB
			)
		)


class ENCRYPTION_CERTIFICATE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbTotalLength',
			DWORD
			),
			(
			'UserSid',
			RPC_SID
			),
			(
			'CertBlob',
			EFS_CERTIFICATE_BLOB
			)
		)


class DATA_ENCRYPTION_CERTIFICATE_LIST(NDRUniConformantArray):
	item = ENCRYPTION_CERTIFICATE


class PTR_ENCRYPTION_CERTIFICATE_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_ENCRYPTION_CERTIFICATE_LIST
			)
		)


class ENCRYPTION_CERTIFICATE_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'nUsers',
			DWORD
			),
			(
			'Users',
			PTR_ENCRYPTION_CERTIFICATE_LIST
			)
		)


class ENCRYPTED_FILE_METADATA_SIGNATURE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwEfsAccessType',
			DWORD
			),
			(
			'CertificatesAdded',
			ENCRYPTION_CERTIFICATE_HASH_LIST
			),
			(
			'EncryptionCertificate',
			ENCRYPTION_CERTIFICATE
			),
			(
			'EfsStreamSignature',
			EFS_RPC_BLOB
			)
		)


class EFS_KEY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwVersion',
			DWORD
			),
			(
			'Entropy',
			UNSIGNED_LONG
			),
			(
			'Algorithm',
			ALG_ID
			),
			(
			'KeyLength',
			UNSIGNED_LONG
			)
		)


class EFS_DECRYPTION_STATUS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwDecryptionError',
			DWORD
			),
			(
			'dwHashOffset',
			DWORD
			),
			(
			'cbHash',
			DWORD
			)
		)


class EFS_ENCRYPTION_STATUS_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'bHasCurrentKey',
			BOOL
			),
			(
			'dwEncryptionError',
			DWORD
			)
		)


class ENCRYPTION_PROTECTOR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbTotalLength',
			DWORD
			),
			(
			'UserSid',
			RPC_SID
			),
			(
			'lpProtectorDescriptor',
			WCHAR_T
			)
		)


class PENCRYPTION_PROTECTOR(NDRPOINTER):
	referent = (
			(
			'Data',
			ENCRYPTION_PROTECTOR
			)
		)


class DATA_ENCRYPTION_PROTECTOR_LIST(NDRUniConformantArray):
	item = PENCRYPTION_PROTECTOR


class PTR_ENCRYPTION_PROTECTOR_LIST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_ENCRYPTION_PROTECTOR_LIST
			)
		)


class ENCRYPTION_PROTECTOR_LIST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'nProtectors',
			DWORD
			),
			(
			'pProtectors',
			PTR_ENCRYPTION_PROTECTOR_LIST
			)
		)


class EfsRpcOpenFileRaw(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'Flags',
			LONG
			)
		)


class EfsRpcOpenFileRawResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'Flags',
			LONG
			)
		)


class EfsRpcReadFileRaw(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			)
		)


class EfsRpcReadFileRawResponse(NDRCALL):
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			)
		)


class EfsRpcWriteFileRaw(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			),
			(
			'EfsInPipe',
			EFS_EXIM_PIPE
			)
		)


class EfsRpcWriteFileRawResponse(NDRCALL):
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			),
			(
			'EfsInPipe',
			EFS_EXIM_PIPE
			)
		)


class EfsRpcCloseRaw(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			)
		)


class EfsRpcCloseRawResponse(NDRCALL):
	structure = (
			(
			'hContext',
			PEXIMPORT_CONTEXT_HANDLE
			)
		)


class EfsRpcEncryptFileSrv(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcEncryptFileSrvResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcDecryptFileSrv(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'OpenFlag',
			UNSIGNED_LONG
			)
		)


class EfsRpcDecryptFileSrvResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'OpenFlag',
			UNSIGNED_LONG
			)
		)


class EfsRpcQueryUsersOnFile(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcQueryUsersOnFileResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcQueryRecoveryAgents(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcQueryRecoveryAgentsResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcRemoveUsersFromFile(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'Users',
			ENCRYPTION_CERTIFICATE_HASH_LIST
			)
		)


class EfsRpcRemoveUsersFromFileResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'Users',
			ENCRYPTION_CERTIFICATE_HASH_LIST
			)
		)


class EfsRpcAddUsersToFile(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'EncryptionCertificates',
			ENCRYPTION_CERTIFICATE_LIST
			)
		)


class EfsRpcAddUsersToFileResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'EncryptionCertificates',
			ENCRYPTION_CERTIFICATE_LIST
			)
		)


class Opnum10NotUsedOnWire(NDRCALL):
	OPNUM = 10
	structure = (

		)


class Opnum10NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class EfsRpcNotSupported(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'Reserved1',
			WCHAR_T
			),
			(
			'Reserved2',
			WCHAR_T
			),
			(
			'dwReserved1',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'bReserved',
			BOOL
			)
		)


class EfsRpcNotSupportedResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'Reserved1',
			WCHAR_T
			),
			(
			'Reserved2',
			WCHAR_T
			),
			(
			'dwReserved1',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'bReserved',
			BOOL
			)
		)


class EfsRpcFileKeyInfo(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'InfoClass',
			DWORD
			)
		)


class EfsRpcFileKeyInfoResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'InfoClass',
			DWORD
			)
		)


class EfsRpcDuplicateEncryptionInfoFile(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'SrcFileName',
			WCHAR_T
			),
			(
			'DestFileName',
			WCHAR_T
			),
			(
			'dwCreationDisposition',
			DWORD
			),
			(
			'dwAttributes',
			DWORD
			),
			(
			'RelativeSD',
			EFS_RPC_BLOB
			),
			(
			'bInheritHandle',
			BOOL
			)
		)


class EfsRpcDuplicateEncryptionInfoFileResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'SrcFileName',
			WCHAR_T
			),
			(
			'DestFileName',
			WCHAR_T
			),
			(
			'dwCreationDisposition',
			DWORD
			),
			(
			'dwAttributes',
			DWORD
			),
			(
			'RelativeSD',
			EFS_RPC_BLOB
			),
			(
			'bInheritHandle',
			BOOL
			)
		)


class Opnum14NotUsedOnWire(NDRCALL):
	OPNUM = 14
	structure = (

		)


class Opnum14NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class EfsRpcAddUsersToFileEx(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'EncryptionCertificates',
			ENCRYPTION_CERTIFICATE_LIST
			)
		)


class EfsRpcAddUsersToFileExResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'EncryptionCertificates',
			ENCRYPTION_CERTIFICATE_LIST
			)
		)


class EfsRpcFileKeyInfoEx(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'dwFileKeyInfoFlags',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'InfoClass',
			DWORD
			)
		)


class EfsRpcFileKeyInfoExResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'dwFileKeyInfoFlags',
			DWORD
			),
			(
			'Reserved',
			EFS_RPC_BLOB
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'InfoClass',
			DWORD
			)
		)


class Opnum17NotUsedOnWire(NDRCALL):
	OPNUM = 17
	structure = (

		)


class Opnum17NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class EfsRpcGetEncryptedFileMetadata(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcGetEncryptedFileMetadataResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcSetEncryptedFileMetadata(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'OldEfsStreamBlob',
			EFS_RPC_BLOB
			),
			(
			'NewEfsStreamBlob',
			EFS_RPC_BLOB
			),
			(
			'NewEfsSignature',
			ENCRYPTED_FILE_METADATA_SIGNATURE
			)
		)


class EfsRpcSetEncryptedFileMetadataResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'OldEfsStreamBlob',
			EFS_RPC_BLOB
			),
			(
			'NewEfsStreamBlob',
			EFS_RPC_BLOB
			),
			(
			'NewEfsSignature',
			ENCRYPTED_FILE_METADATA_SIGNATURE
			)
		)


class EfsRpcFlushEfsCache(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'binding_h',
			HANDLE_T
			)
		)


class EfsRpcFlushEfsCacheResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			)
		)


class EfsRpcEncryptFileExSrv(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'ProtectorDescriptor',
			WCHAR_T
			),
			(
			'Flags',
			UNSIGNED_LONG
			)
		)


class EfsRpcEncryptFileExSrvResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			),
			(
			'ProtectorDescriptor',
			WCHAR_T
			),
			(
			'Flags',
			UNSIGNED_LONG
			)
		)


class EfsRpcQueryProtectors(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class EfsRpcQueryProtectorsResponse(NDRCALL):
	structure = (
			(
			'binding_h',
			HANDLE_T
			),
			(
			'FileName',
			WCHAR_T
			)
		)


class Opnum23NotUsedOnWire(NDRCALL):
	OPNUM = 23
	structure = (

		)


class Opnum23NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum24NotUsedOnWire(NDRCALL):
	OPNUM = 24
	structure = (

		)


class Opnum24NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum25NotUsedOnWire(NDRCALL):
	OPNUM = 25
	structure = (

		)


class Opnum25NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum26NotUsedOnWire(NDRCALL):
	OPNUM = 26
	structure = (

		)


class Opnum26NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum27NotUsedOnWire(NDRCALL):
	OPNUM = 27
	structure = (

		)


class Opnum27NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum28NotUsedOnWire(NDRCALL):
	OPNUM = 28
	structure = (

		)


class Opnum28NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum29NotUsedOnWire(NDRCALL):
	OPNUM = 29
	structure = (

		)


class Opnum29NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum30NotUsedOnWire(NDRCALL):
	OPNUM = 30
	structure = (

		)


class Opnum30NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum31NotUsedOnWire(NDRCALL):
	OPNUM = 31
	structure = (

		)


class Opnum31NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum32NotUsedOnWire(NDRCALL):
	OPNUM = 32
	structure = (

		)


class Opnum32NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum33NotUsedOnWire(NDRCALL):
	OPNUM = 33
	structure = (

		)


class Opnum33NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum34NotUsedOnWire(NDRCALL):
	OPNUM = 34
	structure = (

		)


class Opnum34NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum35NotUsedOnWire(NDRCALL):
	OPNUM = 35
	structure = (

		)


class Opnum35NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum36NotUsedOnWire(NDRCALL):
	OPNUM = 36
	structure = (

		)


class Opnum36NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum37NotUsedOnWire(NDRCALL):
	OPNUM = 37
	structure = (

		)


class Opnum37NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum38NotUsedOnWire(NDRCALL):
	OPNUM = 38
	structure = (

		)


class Opnum38NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum39NotUsedOnWire(NDRCALL):
	OPNUM = 39
	structure = (

		)


class Opnum39NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum40NotUsedOnWire(NDRCALL):
	OPNUM = 40
	structure = (

		)


class Opnum40NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum41NotUsedOnWire(NDRCALL):
	OPNUM = 41
	structure = (

		)


class Opnum41NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum42NotUsedOnWire(NDRCALL):
	OPNUM = 42
	structure = (

		)


class Opnum42NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum43NotUsedOnWire(NDRCALL):
	OPNUM = 43
	structure = (

		)


class Opnum43NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum44NotUsedOnWire(NDRCALL):
	OPNUM = 44
	structure = (

		)


class Opnum44NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


OPNUMS = {0 : (
	EfsRpcOpenFileRaw,
	EfsRpcOpenFileRawResponse
	),1 : (
	EfsRpcReadFileRaw,
	EfsRpcReadFileRawResponse
	),2 : (
	EfsRpcWriteFileRaw,
	EfsRpcWriteFileRawResponse
	),3 : (
	EfsRpcCloseRaw,
	EfsRpcCloseRawResponse
	),4 : (
	EfsRpcEncryptFileSrv,
	EfsRpcEncryptFileSrvResponse
	),5 : (
	EfsRpcDecryptFileSrv,
	EfsRpcDecryptFileSrvResponse
	),6 : (
	EfsRpcQueryUsersOnFile,
	EfsRpcQueryUsersOnFileResponse
	),7 : (
	EfsRpcQueryRecoveryAgents,
	EfsRpcQueryRecoveryAgentsResponse
	),8 : (
	EfsRpcRemoveUsersFromFile,
	EfsRpcRemoveUsersFromFileResponse
	),9 : (
	EfsRpcAddUsersToFile,
	EfsRpcAddUsersToFileResponse
	),10 : (
	Opnum10NotUsedOnWire,
	Opnum10NotUsedOnWireResponse
	),11 : (
	EfsRpcNotSupported,
	EfsRpcNotSupportedResponse
	),12 : (
	EfsRpcFileKeyInfo,
	EfsRpcFileKeyInfoResponse
	),13 : (
	EfsRpcDuplicateEncryptionInfoFile,
	EfsRpcDuplicateEncryptionInfoFileResponse
	),14 : (
	Opnum14NotUsedOnWire,
	Opnum14NotUsedOnWireResponse
	),15 : (
	EfsRpcAddUsersToFileEx,
	EfsRpcAddUsersToFileExResponse
	),16 : (
	EfsRpcFileKeyInfoEx,
	EfsRpcFileKeyInfoExResponse
	),17 : (
	Opnum17NotUsedOnWire,
	Opnum17NotUsedOnWireResponse
	),18 : (
	EfsRpcGetEncryptedFileMetadata,
	EfsRpcGetEncryptedFileMetadataResponse
	),19 : (
	EfsRpcSetEncryptedFileMetadata,
	EfsRpcSetEncryptedFileMetadataResponse
	),20 : (
	EfsRpcFlushEfsCache,
	EfsRpcFlushEfsCacheResponse
	),21 : (
	EfsRpcEncryptFileExSrv,
	EfsRpcEncryptFileExSrvResponse
	),22 : (
	EfsRpcQueryProtectors,
	EfsRpcQueryProtectorsResponse
	),23 : (
	Opnum23NotUsedOnWire,
	Opnum23NotUsedOnWireResponse
	),24 : (
	Opnum24NotUsedOnWire,
	Opnum24NotUsedOnWireResponse
	),25 : (
	Opnum25NotUsedOnWire,
	Opnum25NotUsedOnWireResponse
	),26 : (
	Opnum26NotUsedOnWire,
	Opnum26NotUsedOnWireResponse
	),27 : (
	Opnum27NotUsedOnWire,
	Opnum27NotUsedOnWireResponse
	),28 : (
	Opnum28NotUsedOnWire,
	Opnum28NotUsedOnWireResponse
	),29 : (
	Opnum29NotUsedOnWire,
	Opnum29NotUsedOnWireResponse
	),30 : (
	Opnum30NotUsedOnWire,
	Opnum30NotUsedOnWireResponse
	),31 : (
	Opnum31NotUsedOnWire,
	Opnum31NotUsedOnWireResponse
	),32 : (
	Opnum32NotUsedOnWire,
	Opnum32NotUsedOnWireResponse
	),33 : (
	Opnum33NotUsedOnWire,
	Opnum33NotUsedOnWireResponse
	),34 : (
	Opnum34NotUsedOnWire,
	Opnum34NotUsedOnWireResponse
	),35 : (
	Opnum35NotUsedOnWire,
	Opnum35NotUsedOnWireResponse
	),36 : (
	Opnum36NotUsedOnWire,
	Opnum36NotUsedOnWireResponse
	),37 : (
	Opnum37NotUsedOnWire,
	Opnum37NotUsedOnWireResponse
	),38 : (
	Opnum38NotUsedOnWire,
	Opnum38NotUsedOnWireResponse
	),39 : (
	Opnum39NotUsedOnWire,
	Opnum39NotUsedOnWireResponse
	),40 : (
	Opnum40NotUsedOnWire,
	Opnum40NotUsedOnWireResponse
	),41 : (
	Opnum41NotUsedOnWire,
	Opnum41NotUsedOnWireResponse
	),42 : (
	Opnum42NotUsedOnWire,
	Opnum42NotUsedOnWireResponse
	),43 : (
	Opnum43NotUsedOnWire,
	Opnum43NotUsedOnWireResponse
	),44 : (
	Opnum44NotUsedOnWire,
	Opnum44NotUsedOnWireResponse
	)}
