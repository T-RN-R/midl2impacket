
from fuzzer.midl import *
from fuzzer.core import *
ULONGLONG = NdrHyper
BYTE = NdrByte
USHORT = NdrShort
SHORT = NdrShort
UCHAR = NdrByte
PCHAR = NdrByte
PUCHAR = NdrByte
PLONG64 = NdrHyper
ULONG = NdrLong
ULONG64 = NdrHyper
DWORD64 = NdrHyper
PDWORD64 = NdrHyper
DWORD = NdrLong
UINT64 = NdrHyper
WORD = NdrByte
PWCHAR_T = NdrByte
BOOLEAN = NdrBoolean
INT64 = NdrHyper
UNSIGNED_SHORT = NdrShort
UNSIGNED_CHAR = NdrByte
UNSIGNED_LONG = NdrLong
UNSIGNEDLONG = NdrLong
PUNSIGNED_LONG = NdrLong
PUNSIGNED_CHAR = NdrByte
UNSIGNED_INT = NdrLong
UNSIGNED___INT64 = NdrHyper
SIGNED___INT64 = NdrHyper
SIGNED_INT = NdrShort
SIGNED_LONG = NdrLong
SIGNED_CHAR = NdrByte
SIGNED_SHORT = NdrShort
WCHAR_T = NdrWString
CHAR = NdrByte
PWCHAR = NdrCString
INT = NdrLong
PVOID = NdrContextHandle
VOID = NdrContextHandle
CONTEXT_HANDLE = NdrContextHandle
PPCONTEXT_HANDLE = NdrContextHandle
LONG = NdrLong
INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
LARGE_INTEGER = NdrHyper
LPSTR = NdrCString
LPWSTR = NdrWString
LPCSTR = NdrCString
LPCWSTR = NdrWString
LMSTR = NdrWString
PWSTR = NdrWString
WCHAR = NdrWString
PBYTE = NdrByte
DOUBLE = NdrDouble
FLOAT = NdrFloat

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD,'dwLowDateTime'),(LONG,'dwHighDateTime')]

class LUID(NdrStructure):
    MEMBERS = [(DWORD,'LowPart'),(LONG,'HighPart')]

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD,'wYear'),(WORD,'wMonth'),(WORD,'wDayOfWeek'),(WORD,'wDay'),(WORD,'wHour'),(WORD,'wMinute'),(WORD,'wSecond'),(WORD,'wMilliseconds'),]
WCHAR_T = UNSIGNED_SHORT
ADCONNECTION_HANDLE = VOID
BOOL = INT
PPBOOL = INT
PLPBOOL = INT
BYTE = UNSIGNED_CHAR
PPBYTE = UNSIGNED_CHAR
PLPBYTE = UNSIGNED_CHAR
BOOLEAN = BYTE
PPBOOLEAN = BYTE
WCHAR = WCHAR_T
PPWCHAR = WCHAR_T
BSTR = WCHAR
CHAR = CHAR
PPCHAR = CHAR
DOUBLE = DOUBLE
DWORD = UNSIGNED_LONG
PPDWORD = UNSIGNED_LONG
PLPDWORD = UNSIGNED_LONG
DWORD32 = UNSIGNED_INT
DWORD64 = UNSIGNED___INT64
PPDWORD64 = UNSIGNED___INT64
ULONGLONG = UNSIGNED___INT64
DWORDLONG = ULONGLONG
PPDWORDLONG = ULONGLONG
ERROR_STATUS_T = UNSIGNED_LONG
FLOAT = FLOAT
UCHAR = UNSIGNED_CHAR
PPUCHAR = UNSIGNED_CHAR
SHORT = SHORT
HANDLE = VOID
HCALL = DWORD
INT = INT
PLPINT = INT
INT8 = SIGNED_CHAR
INT16 = SIGNED_SHORT
INT32 = SIGNED_INT
INT64 = SIGNED___INT64
LDAP_UDP_HANDLE = VOID
LMCSTR = WCHAR_T
LMSTR = WCHAR
LONG = LONG
PPLONG = LONG
PLPLONG = LONG
LONGLONG = SIGNED___INT64
HRESULT = LONG
LONG_PTR = INT3264
ULONG_PTR = UNSIGNED___INT3264
LONG32 = SIGNED_INT
LONG64 = SIGNED___INT64
PPLONG64 = SIGNED___INT64
LPCSTR = CHAR
LPCVOID = VOID
LPCWSTR = WCHAR_T
PSTR = CHAR
PLPSTR = CHAR
LPWSTR = WCHAR_T
PPWSTR = WCHAR_T
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
PPULONG = UNSIGNED_LONG
DWORD_PTR = ULONG_PTR
SIZE_T = ULONG_PTR
ULONG32 = UNSIGNED_INT
ULONG64 = UNSIGNED___INT64
UNICODE = WCHAR_T
USHORT = UNSIGNED_SHORT
VOID = VOID
PPVOID = VOID
PLPVOID = VOID
WORD = UNSIGNED_SHORT
PPWORD = UNSIGNED_SHORT
PLPWORD = UNSIGNED_SHORT

class FILETIME(NdrStructure):
    MEMBERS = [(DWORD, "dwLowDateTime"),(DWORD, "dwHighDateTime"),]

    
PFILETIME = FILETIME
LPFILETIME = FILETIME

class GUID(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "Data1"),(UNSIGNED_SHORT, "Data2"),(UNSIGNED_SHORT, "Data3"),(BYTE, "Data4"),]

    
UUID = GUID
PGUID = GUID

class LARGE_INTEGER(NdrStructure):
    MEMBERS = [(SIGNED___INT64, "QuadPart"),]

    
PLARGE_INTEGER = LARGE_INTEGER

class EVENT_DESCRIPTOR(NdrStructure):
    MEMBERS = [(USHORT, "Id"),(UCHAR, "Version"),(UCHAR, "Channel"),(UCHAR, "Level"),(UCHAR, "Opcode"),(USHORT, "Task"),(ULONGLONG, "Keyword"),]

    
PEVENT_DESCRIPTOR = EVENT_DESCRIPTOR
PCEVENT_DESCRIPTOR = EVENT_DESCRIPTOR

class S0(NdrStructure):
    MEMBERS = [(ULONG, "KernelTime"),(ULONG, "UserTime"),]

    

class U0(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (S0, "s0"),2 : (ULONG64, "ProcessorTime"),}

    

class EVENT_HEADER(NdrStructure):
    MEMBERS = [(USHORT, "Size"),(USHORT, "HeaderType"),(USHORT, "Flags"),(USHORT, "EventProperty"),(ULONG, "ThreadId"),(ULONG, "ProcessId"),(LARGE_INTEGER, "TimeStamp"),(GUID, "ProviderId"),(EVENT_DESCRIPTOR, "EventDescriptor"),(U0, "u0"),(GUID, "ActivityId"),]

    
PEVENT_HEADER = EVENT_HEADER
LCID = DWORD

class LUID(NdrStructure):
    MEMBERS = [(DWORD, "LowPart"),(LONG, "HighPart"),]

    
PLUID = LUID

class MULTI_SZ(NdrStructure):
    MEMBERS = [(PWCHAR_T, "Value"),(DWORD, "nChar"),]

    

class RPC_UNICODE_STRING(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Length"),(UNSIGNED_SHORT, "MaximumLength"),(PWCHAR, "Buffer"),]

    
PRPC_UNICODE_STRING = RPC_UNICODE_STRING

class SERVER_INFO_100(NdrStructure):
    MEMBERS = [(DWORD, "sv100_platform_id"),(PWCHAR_T, "sv100_name"),]

    
PSERVER_INFO_100 = SERVER_INFO_100
LPSERVER_INFO_100 = SERVER_INFO_100

class SERVER_INFO_101(NdrStructure):
    MEMBERS = [(DWORD, "sv101_platform_id"),(PWCHAR_T, "sv101_name"),(DWORD, "sv101_version_major"),(DWORD, "sv101_version_minor"),(DWORD, "sv101_version_type"),(PWCHAR_T, "sv101_comment"),]

    
PSERVER_INFO_101 = SERVER_INFO_101
LPSERVER_INFO_101 = SERVER_INFO_101

class SYSTEMTIME(NdrStructure):
    MEMBERS = [(WORD, "wYear"),(WORD, "wMonth"),(WORD, "wDayOfWeek"),(WORD, "wDay"),(WORD, "wHour"),(WORD, "wMinute"),(WORD, "wSecond"),(WORD, "wMilliseconds"),]

    
PSYSTEMTIME = SYSTEMTIME

class UINT128(NdrStructure):
    MEMBERS = [(UINT64, "lower"),(UINT64, "upper"),]

    
PUINT128 = UINT128

class ULARGE_INTEGER(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "QuadPart"),]

    
PULARGE_INTEGER = ULARGE_INTEGER

class RPC_SID_IDENTIFIER_AUTHORITY(NdrStructure):
    MEMBERS = [(BYTE, "Value"),]

    
ACCESS_MASK = DWORD
PACCESS_MASK = ACCESS_MASK

class OBJECT_TYPE_LIST(NdrStructure):
    MEMBERS = [(WORD, "Level"),(ACCESS_MASK, "Remaining"),(PGUID, "ObjectType"),]

    
POBJECT_TYPE_LIST = OBJECT_TYPE_LIST

class ACE_HEADER(NdrStructure):
    MEMBERS = [(UCHAR, "AceType"),(UCHAR, "AceFlags"),(USHORT, "AceSize"),]

    
PACE_HEADER = ACE_HEADER

class SYSTEM_MANDATORY_LABEL_ACE(NdrStructure):
    MEMBERS = [(ACE_HEADER, "Header"),(ACCESS_MASK, "Mask"),(DWORD, "SidStart"),]

    
PSYSTEM_MANDATORY_LABEL_ACE = SYSTEM_MANDATORY_LABEL_ACE

class TOKEN_MANDATORY_POLICY(NdrStructure):
    MEMBERS = [(DWORD, "Policy"),]

    
PTOKEN_MANDATORY_POLICY = TOKEN_MANDATORY_POLICY

class MANDATORY_INFORMATION(NdrStructure):
    MEMBERS = [(ACCESS_MASK, "AllowedAccess"),(BOOLEAN, "WriteAllowed"),(BOOLEAN, "ReadAllowed"),(BOOLEAN, "ExecuteAllowed"),(TOKEN_MANDATORY_POLICY, "MandatoryPolicy"),]

    
PMANDATORY_INFORMATION = MANDATORY_INFORMATION

class CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE(NdrStructure):
    MEMBERS = [(DWORD, "Length"),(BYTE, "OctetString"),]

    
PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE = CLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE

class VALUES(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PLONG64, "pInt64"),2 : (PDWORD64, "pUint64"),3 : (PWSTR, "ppString"),4 : (PCLAIM_SECURITY_ATTRIBUTE_OCTET_STRING_RELATIVE, "pOctetString"),}

    

class CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1(NdrStructure):
    MEMBERS = [(DWORD, "Name"),(WORD, "ValueType"),(WORD, "Reserved"),(DWORD, "Flags"),(DWORD, "ValueCount"),(VALUES, "Values"),]

    
PCLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1 = CLAIM_SECURITY_ATTRIBUTE_RELATIVE_V1
SECURITY_INFORMATION = DWORD
PPSECURITY_INFORMATION = DWORD

class RPC_SID(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "Revision"),(UNSIGNED_CHAR, "SubAuthorityCount"),(RPC_SID_IDENTIFIER_AUTHORITY, "IdentifierAuthority"),(UNSIGNED_LONG, "SubAuthority"),]

    
PRPC_SID = RPC_SID
PSID = RPC_SID

class ACL(NdrStructure):
    MEMBERS = [(UNSIGNED_CHAR, "AclRevision"),(UNSIGNED_CHAR, "Sbz1"),(UNSIGNED_SHORT, "AclSize"),(UNSIGNED_SHORT, "AceCount"),(UNSIGNED_SHORT, "Sbz2"),]

    
PACL = ACL

class SECURITY_DESCRIPTOR(NdrStructure):
    MEMBERS = [(UCHAR, "Revision"),(UCHAR, "Sbz1"),(USHORT, "Control"),(PSID, "Owner"),(PSID, "Group"),(PACL, "Sacl"),(PACL, "Dacl"),]

    
PSECURITY_DESCRIPTOR = SECURITY_DESCRIPTOR
PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE = VOID
PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE = VOID
PTUNNEL_CONTEXT_HANDLE_SERIALIZE = PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE
PCHANNEL_CONTEXT_HANDLE_SERIALIZE = PCHANNEL_CONTEXT_HANDLE_NOSERIALIZE
RESOURCENAME = WCHAR_T

class TSENDPOINTINFO(NdrStructure):
    MEMBERS = [(PRESOURCENAME, "resourceName"),(UNSIGNED_LONG, "numResourceNames"),(PRESOURCENAME, "alternateResourceNames"),(UNSIGNED_SHORT, "numAlternateResourceNames"),(UNSIGNED_LONG, "Port"),]

    
PTSENDPOINTINFO = TSENDPOINTINFO

class TSG_PACKET_HEADER(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "ComponentId"),(UNSIGNED_SHORT, "PacketId"),]

    
PTSG_PACKET_HEADER = TSG_PACKET_HEADER

class TSG_CAPABILITY_NAP(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "capabilities"),]

    
PTSG_CAPABILITY_NAP = TSG_CAPABILITY_NAP

class TSG_CAPABILITIES_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (TSG_CAPABILITY_NAP, "TSGCapNap"),}

    
PTSG_CAPABILITIES_UNION = TSG_CAPABILITIES_UNION

class TSG_PACKET_CAPABILITIES(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "capabilityType"),(TSG_CAPABILITIES_UNION, "TSGPacket"),]

    
PTSG_PACKET_CAPABILITIES = TSG_PACKET_CAPABILITIES

class TSG_PACKET_VERSIONCAPS(NdrStructure):
    MEMBERS = [(TSG_PACKET_HEADER, "tsgHeader"),(PTSG_PACKET_CAPABILITIES, "TSGCaps"),(UNSIGNED_LONG, "numCapabilities"),(UNSIGNED_SHORT, "majorVersion"),(UNSIGNED_SHORT, "minorVersion"),(UNSIGNED_SHORT, "quarantineCapabilities"),]

    
PTSG_PACKET_VERSIONCAPS = TSG_PACKET_VERSIONCAPS

class TSG_PACKET_QUARCONFIGREQUEST(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),]

    
PTSG_PACKET_QUARCONFIGREQUEST = TSG_PACKET_QUARCONFIGREQUEST

class TSG_PACKET_QUARREQUEST(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(PWCHAR_T, "machineName"),(UNSIGNED_LONG, "nameLength"),(PBYTE, "data"),(UNSIGNED_LONG, "dataLen"),]

    
PTSG_PACKET_QUARREQUEST = TSG_PACKET_QUARREQUEST

class TSG_REDIRECTION_FLAGS(NdrStructure):
    MEMBERS = [(BOOL, "enableAllRedirections"),(BOOL, "disableAllRedirections"),(BOOL, "driveRedirectionDisabled"),(BOOL, "printerRedirectionDisabled"),(BOOL, "portRedirectionDisabled"),(BOOL, "reserved"),(BOOL, "clipboardRedirectionDisabled"),(BOOL, "pnpRedirectionDisabled"),]

    
PTSG_REDIRECTION_FLAGS = TSG_REDIRECTION_FLAGS

class TSG_PACKET_RESPONSE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "reserved"),(PBYTE, "responseData"),(UNSIGNED_LONG, "responseDataLen"),(TSG_REDIRECTION_FLAGS, "redirectionFlags"),]

    
PTSG_PACKET_RESPONSE = TSG_PACKET_RESPONSE

class TSG_PACKET_QUARENC_RESPONSE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "flags"),(UNSIGNED_LONG, "certChainLen"),(PWCHAR_T, "certChainData"),(GUID, "nonce"),(PTSG_PACKET_VERSIONCAPS, "versionCaps"),]

    
PTSG_PACKET_QUARENC_RESPONSE = TSG_PACKET_QUARENC_RESPONSE

class TSG_PACKET_MSG_REQUEST(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "maxMessagesPerBatch"),]

    
PTSG_PACKET_MSG_REQUEST = TSG_PACKET_MSG_REQUEST

class TSG_PACKET_STRING_MESSAGE(NdrStructure):
    MEMBERS = [(LONG, "isDisplayMandatory"),(LONG, "isConsentMandatory"),(UNSIGNED_LONG, "msgBytes"),(PWCHAR_T, "msgBuffer"),]

    
PTSG_PACKET_STRING_MESSAGE = TSG_PACKET_STRING_MESSAGE

class TSG_PACKET_REAUTH_MESSAGE(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "tunnelContext"),]

    
PTSG_PACKET_REAUTH_MESSAGE = TSG_PACKET_REAUTH_MESSAGE

class TSG_PACKET_TYPE_MESSAGE_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PTSG_PACKET_STRING_MESSAGE, "consentMessage"),2 : (PTSG_PACKET_STRING_MESSAGE, "serviceMessage"),3 : (PTSG_PACKET_REAUTH_MESSAGE, "reauthMessage"),}

    
PTSG_PACKET_TYPE_MESSAGE_UNION = TSG_PACKET_TYPE_MESSAGE_UNION

class TSG_PACKET_MSG_RESPONSE(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "msgID"),(UNSIGNED_LONG, "msgType"),(LONG, "isMsgPresent"),(TSG_PACKET_TYPE_MESSAGE_UNION, "messagePacket"),]

    
PTSG_PACKET_MSG_RESPONSE = TSG_PACKET_MSG_RESPONSE

class TSG_PACKET_CAPS_RESPONSE(NdrStructure):
    MEMBERS = [(TSG_PACKET_QUARENC_RESPONSE, "pktQuarEncResponse"),(TSG_PACKET_MSG_RESPONSE, "pktConsentMessage"),]

    
PTSG_PACKET_CAPS_RESPONSE = TSG_PACKET_CAPS_RESPONSE

class TSG_PACKET_AUTH(NdrStructure):
    MEMBERS = [(TSG_PACKET_VERSIONCAPS, "TSGVersionCaps"),(UNSIGNED_LONG, "cookieLen"),(PBYTE, "cookie"),]

    
PTSG_PACKET_AUTH = TSG_PACKET_AUTH

class TSG_INITIAL_PACKET_TYPE_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PTSG_PACKET_VERSIONCAPS, "packetVersionCaps"),2 : (PTSG_PACKET_AUTH, "packetAuth"),}

    
PTSG_INITIAL_PACKET_TYPE_UNION = TSG_INITIAL_PACKET_TYPE_UNION

class TSG_PACKET_REAUTH(NdrStructure):
    MEMBERS = [(UNSIGNED___INT64, "tunnelContext"),(UNSIGNED_LONG, "packetId"),(TSG_INITIAL_PACKET_TYPE_UNION, "TSGInitialPacket"),]

    
PTSG_PACKET_REAUTH = TSG_PACKET_REAUTH

class TSG_PACKET_TYPE_UNION(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PTSG_PACKET_HEADER, "packetHeader"),2 : (PTSG_PACKET_VERSIONCAPS, "packetVersionCaps"),3 : (PTSG_PACKET_QUARCONFIGREQUEST, "packetQuarConfigRequest"),4 : (PTSG_PACKET_QUARREQUEST, "packetQuarRequest"),5 : (PTSG_PACKET_RESPONSE, "packetResponse"),6 : (PTSG_PACKET_QUARENC_RESPONSE, "packetQuarEncResponse"),7 : (PTSG_PACKET_CAPS_RESPONSE, "packetCapsResponse"),8 : (PTSG_PACKET_MSG_REQUEST, "packetMsgRequest"),9 : (PTSG_PACKET_MSG_RESPONSE, "packetMsgResponse"),10 : (PTSG_PACKET_AUTH, "packetAuth"),11 : (PTSG_PACKET_REAUTH, "packetReauth"),}

    
PTSG_PACKET_TYPE_UNION = TSG_PACKET_TYPE_UNION

class TSG_PACKET(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "packetId"),(TSG_PACKET_TYPE_UNION, "TSGPacket"),]

    
PTSG_PACKET = TSG_PACKET
Interface("44e265dd-7daf-42cd-8560-3cdb6e7a2729", "1.3",[Method("Opnum0NotUsedOnWire",
),Method("TsProxyCreateTunnel",
In((PTSG_PACKET,'TSGPacket')),
Out((PPTSG_PACKET,'TSGPacketResponse')),
Out((PPTUNNEL_CONTEXT_HANDLE_SERIALIZE,'tunnelContext')),
Out((PUNSIGNED_LONG,'tunnelId')),
),Method("TsProxyAuthorizeTunnel",
In((PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE,'tunnelContext')),
In((PTSG_PACKET,'TSGPacket')),
Out((PPTSG_PACKET,'TSGPacketResponse')),
),Method("TsProxyMakeTunnelCall",
In((PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE,'tunnelContext')),
In((UNSIGNED_LONG,'procId')),
In((PTSG_PACKET,'TSGPacket')),
Out((PPTSG_PACKET,'TSGPacketResponse')),
),Method("TsProxyCreateChannel",
In((PTUNNEL_CONTEXT_HANDLE_NOSERIALIZE,'tunnelContext')),
In((PTSENDPOINTINFO,'tsEndPointInfo')),
Out((PPCHANNEL_CONTEXT_HANDLE_SERIALIZE,'channelContext')),
Out((PUNSIGNED_LONG,'channelId')),
),Method("Opnum5NotUsedOnWire",
),Method("TsProxyCloseChannel",
InOut((PPCHANNEL_CONTEXT_HANDLE_NOSERIALIZE,'context')),
),Method("TsProxyCloseTunnel",
InOut((PPTUNNEL_CONTEXT_HANDLE_SERIALIZE,'context')),
),Method("TsProxySetupReceivePipe",
In((BYTE,'pRpcMessage')),
),Method("TsProxySendToServer",
In((BYTE,'pRpcMessage')),
),])