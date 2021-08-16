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
#TsProxyRpcInterface Definition
#################################################################################
MSRPC_UUID_TSPROXYRPCINTERFACE = uuidtup_to_bin(('44e265dd-7daf-42cd-8560-3cdb6e7a2729','0.0'))
PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE = VOID
PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE = VOID
PTUNNEL_CONTEXT_HANDLE_SERIALIZE = PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
PCHANNEL_CONTEXT_HANDLE_SERIALIZE = PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE
RESOURCENAME = WCHAR_T
class DATA_TSENDPOINTINFO(NDRUniConformantArray):
	item = RESOURCENAME


class PTR_TSENDPOINTINFO(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSENDPOINTINFO
			)
		)


class TSENDPOINTINFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'resourceName',
			RESOURCENAME
			),
			(
			'numResourceNames',
			UNSIGNED_LONG
			),
			(
			'alternateResourceNames',
			PTR_TSENDPOINTINFO
			),
			(
			'numAlternateResourceNames',
			UNSIGNED_SHORT
			),
			(
			'Port',
			UNSIGNED_LONG
			)
		)


class TSG_PACKET_HEADER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ComponentId',
			UNSIGNED_SHORT
			),
			(
			'PacketId',
			UNSIGNED_SHORT
			)
		)


class PTSG_PACKET_HEADER(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_HEADER
			)
		)


class TSG_CAPABILITY_NAP(NDRSTRUCT):
	align = 1
	structure = (
			(
			'capabilities',
			UNSIGNED_LONG
			)
		)


class PTSG_CAPABILITY_NAP(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_CAPABILITY_NAP
			)
		)


class TSG_CAPABILITIES_UNION(NDRUNION):
	union = {0x00000001 : (
		'TSGCapNap',
		TSG_CAPABILITY_NAP
		)}


class PTSG_CAPABILITIES_UNION(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_CAPABILITIES_UNION
			)
		)


class TSG_PACKET_CAPABILITIES(NDRSTRUCT):
	align = 1
	structure = (
			(
			'capabilityType',
			UNSIGNED_LONG
			),
			(
			'TSGPacket',
			TSG_CAPABILITIES_UNION
			)
		)


class PTSG_PACKET_CAPABILITIES(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_CAPABILITIES
			)
		)


class TSG_PACKET_VERSIONCAPS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tsgHeader',
			TSG_PACKET_HEADER
			),
			(
			'TSGCaps',
			PTSG_PACKET_CAPABILITIES
			),
			(
			'numCapabilities',
			UNSIGNED_LONG
			),
			(
			'majorVersion',
			UNSIGNED_SHORT
			),
			(
			'minorVersion',
			UNSIGNED_SHORT
			),
			(
			'quarantineCapabilities',
			UNSIGNED_SHORT
			)
		)


class PTSG_PACKET_VERSIONCAPS(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_VERSIONCAPS
			)
		)


class TSG_PACKET_QUARCONFIGREQUEST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			)
		)


class PTSG_PACKET_QUARCONFIGREQUEST(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_QUARCONFIGREQUEST
			)
		)


class DATA_TSG_PACKET_QUARREQUEST(NDRUniConformantArray):
	item = BYTE


class PTR_TSG_PACKET_QUARREQUEST(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSG_PACKET_QUARREQUEST
			)
		)


class TSG_PACKET_QUARREQUEST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'machineName',
			WCHAR_T
			),
			(
			'nameLength',
			UNSIGNED_LONG
			),
			(
			'data',
			PTR_TSG_PACKET_QUARREQUEST
			),
			(
			'dataLen',
			UNSIGNED_LONG
			)
		)


class TSG_REDIRECTION_FLAGS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'enableAllRedirections',
			BOOL
			),
			(
			'disableAllRedirections',
			BOOL
			),
			(
			'driveRedirectionDisabled',
			BOOL
			),
			(
			'printerRedirectionDisabled',
			BOOL
			),
			(
			'portRedirectionDisabled',
			BOOL
			),
			(
			'reserved',
			BOOL
			),
			(
			'clipboardRedirectionDisabled',
			BOOL
			),
			(
			'pnpRedirectionDisabled',
			BOOL
			)
		)


class PTSG_REDIRECTION_FLAGS(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_REDIRECTION_FLAGS
			)
		)


class DATA_TSG_PACKET_RESPONSE(NDRUniConformantArray):
	item = BYTE


class PTR_TSG_PACKET_RESPONSE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSG_PACKET_RESPONSE
			)
		)


class TSG_PACKET_RESPONSE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'reserved',
			UNSIGNED_LONG
			),
			(
			'responseData',
			PTR_TSG_PACKET_RESPONSE
			),
			(
			'responseDataLen',
			UNSIGNED_LONG
			),
			(
			'redirectionFlags',
			TSG_REDIRECTION_FLAGS
			)
		)


class DATA_TSG_PACKET_QUARENC_RESPONSE(NDRUniConformantArray):
	item = WCHAR_T


class PTR_TSG_PACKET_QUARENC_RESPONSE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSG_PACKET_QUARENC_RESPONSE
			)
		)


class TSG_PACKET_QUARENC_RESPONSE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'flags',
			UNSIGNED_LONG
			),
			(
			'certChainLen',
			UNSIGNED_LONG
			),
			(
			'certChainData',
			PTR_TSG_PACKET_QUARENC_RESPONSE
			),
			(
			'nonce',
			GUID
			),
			(
			'versionCaps',
			PTSG_PACKET_VERSIONCAPS
			)
		)


class TSG_PACKET_MSG_REQUEST(NDRSTRUCT):
	align = 1
	structure = (
			(
			'maxMessagesPerBatch',
			UNSIGNED_LONG
			)
		)


class PTSG_PACKET_MSG_REQUEST(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_MSG_REQUEST
			)
		)


class DATA_TSG_PACKET_STRING_MESSAGE(NDRUniConformantArray):
	item = WCHAR_T


class PTR_TSG_PACKET_STRING_MESSAGE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSG_PACKET_STRING_MESSAGE
			)
		)


class TSG_PACKET_STRING_MESSAGE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'isDisplayMandatory',
			LONG
			),
			(
			'isConsentMandatory',
			LONG
			),
			(
			'msgBytes',
			UNSIGNED_LONG
			),
			(
			'msgBuffer',
			PTR_TSG_PACKET_STRING_MESSAGE
			)
		)


class TSG_PACKET_REAUTH_MESSAGE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tunnelContext',
			UNSIGNED___INT64
			)
		)


class PTSG_PACKET_REAUTH_MESSAGE(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_REAUTH_MESSAGE
			)
		)


class TSG_PACKET_TYPE_MESSAGE_UNION(NDRUNION):
	union = {0x00000001 : (
		'consentMessage',
		PTSG_PACKET_STRING_MESSAGE
		),0x00000002 : (
		'serviceMessage',
		PTSG_PACKET_STRING_MESSAGE
		),0x00000003 : (
		'reauthMessage',
		PTSG_PACKET_REAUTH_MESSAGE
		)}


class PTSG_PACKET_TYPE_MESSAGE_UNION(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_TYPE_MESSAGE_UNION
			)
		)


class TSG_PACKET_MSG_RESPONSE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'msgID',
			UNSIGNED_LONG
			),
			(
			'msgType',
			UNSIGNED_LONG
			),
			(
			'isMsgPresent',
			LONG
			),
			(
			'messagePacket',
			TSG_PACKET_TYPE_MESSAGE_UNION
			)
		)


class PTSG_PACKET_MSG_RESPONSE(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_MSG_RESPONSE
			)
		)


class TSG_PACKET_CAPS_RESPONSE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pktQuarEncResponse',
			TSG_PACKET_QUARENC_RESPONSE
			),
			(
			'pktConsentMessage',
			TSG_PACKET_MSG_RESPONSE
			)
		)


class PTSG_PACKET_CAPS_RESPONSE(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_CAPS_RESPONSE
			)
		)


class DATA_TSG_PACKET_AUTH(NDRUniConformantArray):
	item = BYTE


class PTR_TSG_PACKET_AUTH(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_TSG_PACKET_AUTH
			)
		)


class TSG_PACKET_AUTH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'TSGVersionCaps',
			TSG_PACKET_VERSIONCAPS
			),
			(
			'cookieLen',
			UNSIGNED_LONG
			),
			(
			'cookie',
			PTR_TSG_PACKET_AUTH
			)
		)


class TSG_INITIAL_PACKET_TYPE_UNION(NDRUNION):
	union = {0x00005643 : (
		'packetVersionCaps',
		PTSG_PACKET_VERSIONCAPS
		),0x00004054 : (
		'packetAuth',
		PTSG_PACKET_AUTH
		)}


class PTSG_INITIAL_PACKET_TYPE_UNION(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_INITIAL_PACKET_TYPE_UNION
			)
		)


class TSG_PACKET_REAUTH(NDRSTRUCT):
	align = 1
	structure = (
			(
			'tunnelContext',
			UNSIGNED___INT64
			),
			(
			'packetId',
			UNSIGNED_LONG
			),
			(
			'TSGInitialPacket',
			TSG_INITIAL_PACKET_TYPE_UNION
			)
		)


class PTSG_PACKET_REAUTH(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_REAUTH
			)
		)


class TSG_PACKET_TYPE_UNION(NDRUNION):
	union = {0x00004844 : (
		'packetHeader',
		PTSG_PACKET_HEADER
		),0x00005643 : (
		'packetVersionCaps',
		PTSG_PACKET_VERSIONCAPS
		),0x00005143 : (
		'packetQuarConfigRequest',
		PTSG_PACKET_QUARCONFIGREQUEST
		),0x00005152 : (
		'packetQuarRequest',
		PTSG_PACKET_QUARREQUEST
		),0x00005052 : (
		'packetResponse',
		PTSG_PACKET_RESPONSE
		),0x00004552 : (
		'packetQuarEncResponse',
		PTSG_PACKET_QUARENC_RESPONSE
		),0x00004350 : (
		'packetCapsResponse',
		PTSG_PACKET_CAPS_RESPONSE
		),0x00004752 : (
		'packetMsgRequest',
		PTSG_PACKET_MSG_REQUEST
		),0x00004750 : (
		'packetMsgResponse',
		PTSG_PACKET_MSG_RESPONSE
		),0x00004054 : (
		'packetAuth',
		PTSG_PACKET_AUTH
		),0x00005250 : (
		'packetReauth',
		PTSG_PACKET_REAUTH
		)}


class PTSG_PACKET_TYPE_UNION(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET_TYPE_UNION
			)
		)


class TSG_PACKET(NDRSTRUCT):
	align = 1
	structure = (
			(
			'packetId',
			UNSIGNED_LONG
			),
			(
			'TSGPacket',
			TSG_PACKET_TYPE_UNION
			)
		)


class PTSG_PACKET(NDRPOINTER):
	referent = (
			(
			'Data',
			TSG_PACKET
			)
		)


class Opnum0NotUsedOnWire(NDRCALL):
	OPNUM = 0
	structure = (

		)


class Opnum0NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class TsProxyCreateTunnel(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyCreateTunnelResponse(NDRCALL):
	structure = (
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyAuthorizeTunnel(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyAuthorizeTunnelResponse(NDRCALL):
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyMakeTunnelCall(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'procId',
			UNSIGNED_LONG
			),
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyMakeTunnelCallResponse(NDRCALL):
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'procId',
			UNSIGNED_LONG
			),
			(
			'TSGPacket',
			PTSG_PACKET
			)
		)


class TsProxyCreateChannel(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'tsEndPointInfo',
			PTSENDPOINTINFO
			)
		)


class TsProxyCreateChannelResponse(NDRCALL):
	structure = (
			(
			'tunnelContext',
			PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
			),
			(
			'tsEndPointInfo',
			PTSENDPOINTINFO
			)
		)


class Opnum5NotUsedOnWire(NDRCALL):
	OPNUM = 5
	structure = (

		)


class Opnum5NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class TsProxyCloseChannel(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'context',
			PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class TsProxyCloseChannelResponse(NDRCALL):
	structure = (
			(
			'context',
			PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE
			)
		)


class TsProxyCloseTunnel(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'context',
			PTUNNEL_CONTEXT_HANDLE_SERIALIZE
			)
		)


class TsProxyCloseTunnelResponse(NDRCALL):
	structure = (
			(
			'context',
			PTUNNEL_CONTEXT_HANDLE_SERIALIZE
			)
		)


class TsProxySetupReceivePipe(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'pRpcMessage',
			BYTE
			)
		)


class TsProxySetupReceivePipeResponse(NDRCALL):
	structure = (
			(
			'pRpcMessage',
			BYTE
			)
		)


class TsProxySendToServer(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'pRpcMessage',
			BYTE
			)
		)


class TsProxySendToServerResponse(NDRCALL):
	structure = (
			(
			'pRpcMessage',
			BYTE
			)
		)


OPNUMS = {0 : (
	Opnum0NotUsedOnWire,
	Opnum0NotUsedOnWireResponse
	),1 : (
	TsProxyCreateTunnel,
	TsProxyCreateTunnelResponse
	),2 : (
	TsProxyAuthorizeTunnel,
	TsProxyAuthorizeTunnelResponse
	),3 : (
	TsProxyMakeTunnelCall,
	TsProxyMakeTunnelCallResponse
	),4 : (
	TsProxyCreateChannel,
	TsProxyCreateChannelResponse
	),5 : (
	Opnum5NotUsedOnWire,
	Opnum5NotUsedOnWireResponse
	),6 : (
	TsProxyCloseChannel,
	TsProxyCloseChannelResponse
	),7 : (
	TsProxyCloseTunnel,
	TsProxyCloseTunnelResponse
	),8 : (
	TsProxySetupReceivePipe,
	TsProxySetupReceivePipeResponse
	),9 : (
	TsProxySendToServer,
	TsProxySendToServerResponse
	)}
