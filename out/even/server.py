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
from impacket.dcerpc.v5.rpcrt import DCERPC_v5, DCERPCException

from impacket import system_errors
class DCERPCSessionError(DCERPCException):
    def __init__(self, error_string=None, error_code=None, packet=None):
        DCERPCException.__init__(self, error_string, error_code, packet)

    def __str__( self ):
        key = self.error_code
        if key in system_errors.ERROR_MESSAGES:
            error_msg_short = system_errors.ERROR_MESSAGES[key][0]
            error_msg_verbose = system_errors.ERROR_MESSAGES[key][1] 
            return 'MIDL2Impacket SessionError: code: 0x%x - %s - %s' % (self.error_code, error_msg_short, error_msg_verbose)
        else:
            return 'MIDL2Impacket SessionError: unknown error code: 0x%x' % self.error_code


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
UNSIGNEDLONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
WCHAR_T = USHORT
PWCHAR_T = LPWSTR
CHAR = NDRCHAR
INT = NDRLONG
VOID = CONTEXT_HANDLE
LONG = NDRLONG
INT3264 = NDRHYPER
UNSIGNED___INT3264 = NDRUHYPER
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER
DWORDLONG = NDRUHYPER
LONG_PTR = NDRHYPER
ULONG_PTR = NDRUHYPER
LPCSTR = LPSTR
LPCWSTR = LPWSTR
LMSTR = LPWSTR
PWSTR = LPWSTR
WCHAR = USHORT
PWCHAR = WSTR
#################################################################################
#TYPEDEFS
#################################################################################
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#eventlog Definition
#################################################################################
MSRPC_UUID_EVENTLOG = uuidtup_to_bin(('82273FDC-E32A-18C3-3F78-827929DC23EA','0.0'))
class CHAR_ARRAY(NDRUniConformantArray):
	item = CHAR


class PCHAR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			CHAR_ARRAY,

			),

		)

	@property
	def Data(self) -> CHAR_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:CHAR_ARRAY):
		self['Data'] = prop


class RPC_STRING_ARRAY(NDRUniConformantArray):
	item = CHAR


class PRPC_STRING_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_STRING_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_STRING_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_STRING_ARRAY):
		self['Data'] = prop


class RPC_STRING(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Length',
			UNSIGNED_SHORT,

			),
			(
			'MaximumLength',
			UNSIGNED_SHORT,

			),
			(
			'Buffer',
			PCHAR_ARRAY,

			),

		)

	@property
	def Length(self) -> UNSIGNED_SHORT:
		return self['Length']

	@Length.setter
	def Length(self, prop:UNSIGNED_SHORT):
		self['Length'] = prop

	@property
	def MaximumLength(self) -> UNSIGNED_SHORT:
		return self['MaximumLength']

	@MaximumLength.setter
	def MaximumLength(self, prop:UNSIGNED_SHORT):
		self['MaximumLength'] = prop

	@property
	def Buffer(self) -> PCHAR_ARRAY:
		return self['Buffer']

	@Buffer.setter
	def Buffer(self, prop:PCHAR_ARRAY):
		self['Buffer'] = prop


class PRPC_STRING(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_STRING,

			),

		)

	@property
	def Data(self) -> RPC_STRING:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_STRING):
		self['Data'] = prop


class RPC_CLIENT_ID(NDRSTRUCT):
	align = 1
	structure = (
			(
			'UniqueProcess',
			UNSIGNED_LONG,

			),
			(
			'UniqueThread',
			UNSIGNED_LONG,

			),

		)

	@property
	def UniqueProcess(self) -> UNSIGNED_LONG:
		return self['UniqueProcess']

	@UniqueProcess.setter
	def UniqueProcess(self, prop:UNSIGNED_LONG):
		self['UniqueProcess'] = prop

	@property
	def UniqueThread(self) -> UNSIGNED_LONG:
		return self['UniqueThread']

	@UniqueThread.setter
	def UniqueThread(self, prop:UNSIGNED_LONG):
		self['UniqueThread'] = prop


class PRPC_CLIENT_ID(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_CLIENT_ID,

			),

		)

	@property
	def Data(self) -> RPC_CLIENT_ID:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_CLIENT_ID):
		self['Data'] = prop


EVENTLOG_HANDLE_W = PWCHAR_T
class PCHAR(NDRPOINTER):
	referent = (
			(
			'Data',
			CHAR,

			),

		)

	@property
	def Data(self) -> CHAR:
		return self['Data']

	@Data.setter
	def Data(self, prop:CHAR):
		self['Data'] = prop

EVENTLOG_HANDLE_A = PCHAR
class PVOID(NDRPOINTER):
	referent = (
			(
			'Data',
			VOID,

			),

		)

	@property
	def Data(self) -> VOID:
		return self['Data']

	@Data.setter
	def Data(self, prop:VOID):
		self['Data'] = prop

class IELF_HANDLE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Data',
			'20s=""',

			),

		)

	@property
	def Data(self) -> str:
		return self['Data']

	@Data.setter
	def Data(self, prop:str):
		self['Data'] = prop


class PIELF_HANDLE(NDRPOINTER):
	referent = (
			(
			'Data',
			IELF_HANDLE,

			),

		)

	@property
	def Data(self) -> IELF_HANDLE:
		return self['Data']

	@Data.setter
	def Data(self, prop:IELF_HANDLE):
		self['Data'] = prop


class PPVOID(NDRPOINTER):
	referent = (
			(
			'Data',
			PVOID,

			),

		)

	@property
	def Data(self) -> PVOID:
		return self['Data']

	@Data.setter
	def Data(self, prop:PVOID):
		self['Data'] = prop

class PPIELF_HANDLE(NDRPOINTER):
	referent = (
			(
			'Data',
			PIELF_HANDLE,

			),

		)

	@property
	def Data(self) -> PIELF_HANDLE:
		return self['Data']

	@Data.setter
	def Data(self, prop:PIELF_HANDLE):
		self['Data'] = prop


RULONG = UNSIGNED_LONG
class ElfrClearELFW(NDRCALL):
	opnum = 0
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'BackupFileName',
			PRPC_UNICODE_STRING,

			),

		)


class ElfrClearELFWResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrClearELFW(dce, LogHandle: IELF_HANDLE, BackupFileName: PRPC_UNICODE_STRING):
	request = ElfrClearELFW()
	request["LogHandle"] = LogHandle
	request["BackupFileName"] = BackupFileName
	return dce.request(request)

class ElfrBackupELFW(NDRCALL):
	opnum = 1
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'BackupFileName',
			PRPC_UNICODE_STRING,

			),

		)


class ElfrBackupELFWResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrBackupELFW(dce, LogHandle: IELF_HANDLE, BackupFileName: PRPC_UNICODE_STRING):
	request = ElfrBackupELFW()
	request["LogHandle"] = LogHandle
	request["BackupFileName"] = BackupFileName
	return dce.request(request)

class ElfrCloseEL(NDRCALL):
	opnum = 2
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),

		)


class ElfrCloseELResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrCloseEL(dce, LogHandle: IELF_HANDLE):
	request = ElfrCloseEL()
	request["LogHandle"] = LogHandle
	return dce.request(request)

class ElfrDeregisterEventSource(NDRCALL):
	opnum = 3
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),

		)


class ElfrDeregisterEventSourceResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrDeregisterEventSource(dce, LogHandle: IELF_HANDLE):
	request = ElfrDeregisterEventSource()
	request["LogHandle"] = LogHandle
	return dce.request(request)

class PUNSIGNED_LONG(NDRPOINTER):
	referent = (
			(
			'Data',
			UNSIGNED_LONG,

			),

		)

	@property
	def Data(self) -> UNSIGNED_LONG:
		return self['Data']

	@Data.setter
	def Data(self, prop:UNSIGNED_LONG):
		self['Data'] = prop

class ElfrNumberOfRecords(NDRCALL):
	opnum = 4
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),

		)


class ElfrNumberOfRecordsResponse(NDRCALL):
	structure = (
			(
			'NumberOfRecords',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrNumberOfRecords(dce, LogHandle: IELF_HANDLE):
	request = ElfrNumberOfRecords()
	request["LogHandle"] = LogHandle
	return dce.request(request)

class ElfrOldestRecord(NDRCALL):
	opnum = 5
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),

		)


class ElfrOldestRecordResponse(NDRCALL):
	structure = (
			(
			'OldestRecordNumber',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrOldestRecord(dce, LogHandle: IELF_HANDLE):
	request = ElfrOldestRecord()
	request["LogHandle"] = LogHandle
	return dce.request(request)

class ElfrChangeNotify(NDRCALL):
	opnum = 6
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ClientId',
			RPC_CLIENT_ID,

			),
			(
			'Event',
			ULONG,

			),

		)


class ElfrChangeNotifyResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrChangeNotify(dce, LogHandle: IELF_HANDLE, ClientId: RPC_CLIENT_ID, Event: ULONG):
	request = ElfrChangeNotify()
	request["LogHandle"] = LogHandle
	request["ClientId"] = ClientId
	request["Event"] = Event
	return dce.request(request)

class ElfrOpenELW(NDRCALL):
	opnum = 7
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_W,

			),
			(
			'ModuleName',
			PRPC_UNICODE_STRING,

			),
			(
			'RegModuleName',
			PRPC_UNICODE_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrOpenELWResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrOpenELW(dce, UNCServerName: EVENTLOG_HANDLE_W, ModuleName: PRPC_UNICODE_STRING, RegModuleName: PRPC_UNICODE_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrOpenELW()
	request["UNCServerName"] = UNCServerName
	request["ModuleName"] = ModuleName
	request["RegModuleName"] = RegModuleName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class ElfrRegisterEventSourceW(NDRCALL):
	opnum = 8
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_W,

			),
			(
			'ModuleName',
			PRPC_UNICODE_STRING,

			),
			(
			'RegModuleName',
			PRPC_UNICODE_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrRegisterEventSourceWResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrRegisterEventSourceW(dce, UNCServerName: EVENTLOG_HANDLE_W, ModuleName: PRPC_UNICODE_STRING, RegModuleName: PRPC_UNICODE_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrRegisterEventSourceW()
	request["UNCServerName"] = UNCServerName
	request["ModuleName"] = ModuleName
	request["RegModuleName"] = RegModuleName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class ElfrOpenBELW(NDRCALL):
	opnum = 9
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_W,

			),
			(
			'BackupFileName',
			PRPC_UNICODE_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrOpenBELWResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrOpenBELW(dce, UNCServerName: EVENTLOG_HANDLE_W, BackupFileName: PRPC_UNICODE_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrOpenBELW()
	request["UNCServerName"] = UNCServerName
	request["BackupFileName"] = BackupFileName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class PUNSIGNED_CHAR(NDRPOINTER):
	referent = (
			(
			'Data',
			UNSIGNED_CHAR,

			),

		)

	@property
	def Data(self) -> UNSIGNED_CHAR:
		return self['Data']

	@Data.setter
	def Data(self, prop:UNSIGNED_CHAR):
		self['Data'] = prop

class UNSIGNED_CHAR_ARRAY(NDRUniConformantArray):
	item = UNSIGNED_CHAR


class PUNSIGNED_CHAR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),

		)

	@property
	def Data(self) -> UNSIGNED_CHAR_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:UNSIGNED_CHAR_ARRAY):
		self['Data'] = prop


class ElfrReadELW(NDRCALL):
	opnum = 10
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ReadFlags',
			UNSIGNED_LONG,

			),
			(
			'RecordOffset',
			UNSIGNED_LONG,

			),
			(
			'NumberOfBytesToRead',
			RULONG,

			),

		)


class ElfrReadELWResponse(NDRCALL):
	structure = (
			(
			'Buffer',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'NumberOfBytesRead',
			UNSIGNED_LONG,

			),
			(
			'MinNumberOfBytesNeeded',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReadELW(dce, LogHandle: IELF_HANDLE, ReadFlags: UNSIGNED_LONG, RecordOffset: UNSIGNED_LONG, NumberOfBytesToRead: RULONG):
	request = ElfrReadELW()
	request["LogHandle"] = LogHandle
	request["ReadFlags"] = ReadFlags
	request["RecordOffset"] = RecordOffset
	request["NumberOfBytesToRead"] = NumberOfBytesToRead
	return dce.request(request)

class PRPC_UNICODE_STRING_ARRAY(NDRUniFixedArray):
	item = PRPC_UNICODE_STRING

	def getDataLen(self, data, offset=0):
		type_size = len(self.item())
		return * * type_size

	def getData(self, _):
		# This is the length of our fixed array
		containerLength = self.getDataLen(None)
		# Truncate extra data provided beyond the maximum length
		raw = self.fields['Data'][:containerLength]
		# Add padding if necessary
		paddingLength = containerLength - (len(raw) % containerLength)
		raw += b'\x00' * paddingLength
		return raw


class ElfrReportEventW(NDRCALL):
	opnum = 11
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'Time',
			UNSIGNED_LONG,

			),
			(
			'EventType',
			UNSIGNED_SHORT,

			),
			(
			'EventCategory',
			UNSIGNED_SHORT,

			),
			(
			'EventID',
			UNSIGNED_LONG,

			),
			(
			'NumStrings',
			UNSIGNED_SHORT,

			),
			(
			'DataSize',
			UNSIGNED_LONG,

			),
			(
			'ComputerName',
			PRPC_UNICODE_STRING,

			),
			(
			'UserSID',
			PRPC_SID,

			),
			(
			'Strings',
			PRPC_UNICODE_STRING_ARRAY,

			),
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'Flags',
			UNSIGNED_SHORT,

			),
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),

		)


class ElfrReportEventWResponse(NDRCALL):
	structure = (
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReportEventW(dce, LogHandle: IELF_HANDLE, Time: UNSIGNED_LONG, EventType: UNSIGNED_SHORT, EventCategory: UNSIGNED_SHORT, EventID: UNSIGNED_LONG, NumStrings: UNSIGNED_SHORT, DataSize: UNSIGNED_LONG, ComputerName: PRPC_UNICODE_STRING, UserSID: PRPC_SID, Strings: PRPC_UNICODE_STRING_ARRAY, Data: UNSIGNED_CHAR_ARRAY, Flags: UNSIGNED_SHORT, RecordNumber: UNSIGNED_LONG, TimeWritten: UNSIGNED_LONG):
	request = ElfrReportEventW()
	request["LogHandle"] = LogHandle
	request["Time"] = Time
	request["EventType"] = EventType
	request["EventCategory"] = EventCategory
	request["EventID"] = EventID
	request["NumStrings"] = NumStrings
	request["DataSize"] = DataSize
	request["ComputerName"] = ComputerName
	request["UserSID"] = UserSID
	request["Strings"] = Strings
	request["Data"] = Data
	request["Flags"] = Flags
	request["RecordNumber"] = RecordNumber
	request["TimeWritten"] = TimeWritten
	return dce.request(request)

class ElfrClearELFA(NDRCALL):
	opnum = 12
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'BackupFileName',
			PRPC_STRING,

			),

		)


class ElfrClearELFAResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrClearELFA(dce, LogHandle: IELF_HANDLE, BackupFileName: PRPC_STRING):
	request = ElfrClearELFA()
	request["LogHandle"] = LogHandle
	request["BackupFileName"] = BackupFileName
	return dce.request(request)

class ElfrBackupELFA(NDRCALL):
	opnum = 13
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'BackupFileName',
			PRPC_STRING,

			),

		)


class ElfrBackupELFAResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrBackupELFA(dce, LogHandle: IELF_HANDLE, BackupFileName: PRPC_STRING):
	request = ElfrBackupELFA()
	request["LogHandle"] = LogHandle
	request["BackupFileName"] = BackupFileName
	return dce.request(request)

class ElfrOpenELA(NDRCALL):
	opnum = 14
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_A,

			),
			(
			'ModuleName',
			PRPC_STRING,

			),
			(
			'RegModuleName',
			PRPC_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrOpenELAResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrOpenELA(dce, UNCServerName: EVENTLOG_HANDLE_A, ModuleName: PRPC_STRING, RegModuleName: PRPC_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrOpenELA()
	request["UNCServerName"] = UNCServerName
	request["ModuleName"] = ModuleName
	request["RegModuleName"] = RegModuleName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class ElfrRegisterEventSourceA(NDRCALL):
	opnum = 15
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_A,

			),
			(
			'ModuleName',
			PRPC_STRING,

			),
			(
			'RegModuleName',
			PRPC_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrRegisterEventSourceAResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrRegisterEventSourceA(dce, UNCServerName: EVENTLOG_HANDLE_A, ModuleName: PRPC_STRING, RegModuleName: PRPC_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrRegisterEventSourceA()
	request["UNCServerName"] = UNCServerName
	request["ModuleName"] = ModuleName
	request["RegModuleName"] = RegModuleName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class ElfrOpenBELA(NDRCALL):
	opnum = 16
	structure = (
			(
			'UNCServerName',
			EVENTLOG_HANDLE_A,

			),
			(
			'BackupFileName',
			PRPC_STRING,

			),
			(
			'MajorVersion',
			UNSIGNED_LONG,

			),
			(
			'MinorVersion',
			UNSIGNED_LONG,

			),

		)


class ElfrOpenBELAResponse(NDRCALL):
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrOpenBELA(dce, UNCServerName: EVENTLOG_HANDLE_A, BackupFileName: PRPC_STRING, MajorVersion: UNSIGNED_LONG, MinorVersion: UNSIGNED_LONG):
	request = ElfrOpenBELA()
	request["UNCServerName"] = UNCServerName
	request["BackupFileName"] = BackupFileName
	request["MajorVersion"] = MajorVersion
	request["MinorVersion"] = MinorVersion
	return dce.request(request)

class ElfrReadELA(NDRCALL):
	opnum = 17
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'ReadFlags',
			UNSIGNED_LONG,

			),
			(
			'RecordOffset',
			UNSIGNED_LONG,

			),
			(
			'NumberOfBytesToRead',
			RULONG,

			),

		)


class ElfrReadELAResponse(NDRCALL):
	structure = (
			(
			'Buffer',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'NumberOfBytesRead',
			UNSIGNED_LONG,

			),
			(
			'MinNumberOfBytesNeeded',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReadELA(dce, LogHandle: IELF_HANDLE, ReadFlags: UNSIGNED_LONG, RecordOffset: UNSIGNED_LONG, NumberOfBytesToRead: RULONG):
	request = ElfrReadELA()
	request["LogHandle"] = LogHandle
	request["ReadFlags"] = ReadFlags
	request["RecordOffset"] = RecordOffset
	request["NumberOfBytesToRead"] = NumberOfBytesToRead
	return dce.request(request)

class PRPC_STRING_ARRAY(NDRUniFixedArray):
	item = PRPC_STRING

	def getDataLen(self, data, offset=0):
		type_size = len(self.item())
		return * * type_size

	def getData(self, _):
		# This is the length of our fixed array
		containerLength = self.getDataLen(None)
		# Truncate extra data provided beyond the maximum length
		raw = self.fields['Data'][:containerLength]
		# Add padding if necessary
		paddingLength = containerLength - (len(raw) % containerLength)
		raw += b'\x00' * paddingLength
		return raw


class ElfrReportEventA(NDRCALL):
	opnum = 18
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'Time',
			UNSIGNED_LONG,

			),
			(
			'EventType',
			UNSIGNED_SHORT,

			),
			(
			'EventCategory',
			UNSIGNED_SHORT,

			),
			(
			'EventID',
			UNSIGNED_LONG,

			),
			(
			'NumStrings',
			UNSIGNED_SHORT,

			),
			(
			'DataSize',
			UNSIGNED_LONG,

			),
			(
			'ComputerName',
			PRPC_STRING,

			),
			(
			'UserSID',
			PRPC_SID,

			),
			(
			'Strings',
			PRPC_STRING_ARRAY,

			),
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'Flags',
			UNSIGNED_SHORT,

			),
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),

		)


class ElfrReportEventAResponse(NDRCALL):
	structure = (
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReportEventA(dce, LogHandle: IELF_HANDLE, Time: UNSIGNED_LONG, EventType: UNSIGNED_SHORT, EventCategory: UNSIGNED_SHORT, EventID: UNSIGNED_LONG, NumStrings: UNSIGNED_SHORT, DataSize: UNSIGNED_LONG, ComputerName: PRPC_STRING, UserSID: PRPC_SID, Strings: PRPC_STRING_ARRAY, Data: UNSIGNED_CHAR_ARRAY, Flags: UNSIGNED_SHORT, RecordNumber: UNSIGNED_LONG, TimeWritten: UNSIGNED_LONG):
	request = ElfrReportEventA()
	request["LogHandle"] = LogHandle
	request["Time"] = Time
	request["EventType"] = EventType
	request["EventCategory"] = EventCategory
	request["EventID"] = EventID
	request["NumStrings"] = NumStrings
	request["DataSize"] = DataSize
	request["ComputerName"] = ComputerName
	request["UserSID"] = UserSID
	request["Strings"] = Strings
	request["Data"] = Data
	request["Flags"] = Flags
	request["RecordNumber"] = RecordNumber
	request["TimeWritten"] = TimeWritten
	return dce.request(request)

class Opnum19NotUsedOnWire(NDRCALL):
	opnum = 19
	structure = (

		)


class Opnum19NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum19NotUsedOnWire(dce):
	request = Opnum19NotUsedOnWire()
	return dce.request(request)

class Opnum20NotUsedOnWire(NDRCALL):
	opnum = 20
	structure = (

		)


class Opnum20NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum20NotUsedOnWire(dce):
	request = Opnum20NotUsedOnWire()
	return dce.request(request)

class Opnum21NotUsedOnWire(NDRCALL):
	opnum = 21
	structure = (

		)


class Opnum21NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum21NotUsedOnWire(dce):
	request = Opnum21NotUsedOnWire()
	return dce.request(request)

class ElfrGetLogInformation(NDRCALL):
	opnum = 22
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'InfoLevel',
			UNSIGNED_LONG,

			),
			(
			'cbBufSize',
			UNSIGNED_LONG,

			),

		)


class ElfrGetLogInformationResponse(NDRCALL):
	structure = (
			(
			'lpBuffer',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'pcbBytesNeeded',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrGetLogInformation(dce, LogHandle: IELF_HANDLE, InfoLevel: UNSIGNED_LONG, cbBufSize: UNSIGNED_LONG):
	request = ElfrGetLogInformation()
	request["LogHandle"] = LogHandle
	request["InfoLevel"] = InfoLevel
	request["cbBufSize"] = cbBufSize
	return dce.request(request)

class Opnum23NotUsedOnWire(NDRCALL):
	opnum = 23
	structure = (

		)


class Opnum23NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum23NotUsedOnWire(dce):
	request = Opnum23NotUsedOnWire()
	return dce.request(request)

class ElfrReportEventAndSourceW(NDRCALL):
	opnum = 24
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'Time',
			UNSIGNED_LONG,

			),
			(
			'EventType',
			UNSIGNED_SHORT,

			),
			(
			'EventCategory',
			UNSIGNED_SHORT,

			),
			(
			'EventID',
			UNSIGNED_LONG,

			),
			(
			'SourceName',
			PRPC_UNICODE_STRING,

			),
			(
			'NumStrings',
			UNSIGNED_SHORT,

			),
			(
			'DataSize',
			UNSIGNED_LONG,

			),
			(
			'ComputerName',
			PRPC_UNICODE_STRING,

			),
			(
			'UserSID',
			PRPC_SID,

			),
			(
			'Strings',
			PRPC_UNICODE_STRING_ARRAY,

			),
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'Flags',
			UNSIGNED_SHORT,

			),
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),

		)


class ElfrReportEventAndSourceWResponse(NDRCALL):
	structure = (
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'TimeWritten',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReportEventAndSourceW(dce, LogHandle: IELF_HANDLE, Time: UNSIGNED_LONG, EventType: UNSIGNED_SHORT, EventCategory: UNSIGNED_SHORT, EventID: UNSIGNED_LONG, SourceName: PRPC_UNICODE_STRING, NumStrings: UNSIGNED_SHORT, DataSize: UNSIGNED_LONG, ComputerName: PRPC_UNICODE_STRING, UserSID: PRPC_SID, Strings: PRPC_UNICODE_STRING_ARRAY, Data: UNSIGNED_CHAR_ARRAY, Flags: UNSIGNED_SHORT, RecordNumber: UNSIGNED_LONG, TimeWritten: UNSIGNED_LONG):
	request = ElfrReportEventAndSourceW()
	request["LogHandle"] = LogHandle
	request["Time"] = Time
	request["EventType"] = EventType
	request["EventCategory"] = EventCategory
	request["EventID"] = EventID
	request["SourceName"] = SourceName
	request["NumStrings"] = NumStrings
	request["DataSize"] = DataSize
	request["ComputerName"] = ComputerName
	request["UserSID"] = UserSID
	request["Strings"] = Strings
	request["Data"] = Data
	request["Flags"] = Flags
	request["RecordNumber"] = RecordNumber
	request["TimeWritten"] = TimeWritten
	return dce.request(request)

class ElfrReportEventExW(NDRCALL):
	opnum = 25
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'TimeGenerated',
			PFILETIME,

			),
			(
			'EventType',
			UNSIGNED_SHORT,

			),
			(
			'EventCategory',
			UNSIGNED_SHORT,

			),
			(
			'EventID',
			UNSIGNED_LONG,

			),
			(
			'NumStrings',
			UNSIGNED_SHORT,

			),
			(
			'DataSize',
			UNSIGNED_LONG,

			),
			(
			'ComputerName',
			PRPC_UNICODE_STRING,

			),
			(
			'UserSID',
			PRPC_SID,

			),
			(
			'Strings',
			PRPC_UNICODE_STRING_ARRAY,

			),
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'Flags',
			UNSIGNED_SHORT,

			),
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),

		)


class ElfrReportEventExWResponse(NDRCALL):
	structure = (
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReportEventExW(dce, LogHandle: IELF_HANDLE, TimeGenerated: PFILETIME, EventType: UNSIGNED_SHORT, EventCategory: UNSIGNED_SHORT, EventID: UNSIGNED_LONG, NumStrings: UNSIGNED_SHORT, DataSize: UNSIGNED_LONG, ComputerName: PRPC_UNICODE_STRING, UserSID: PRPC_SID, Strings: PRPC_UNICODE_STRING_ARRAY, Data: UNSIGNED_CHAR_ARRAY, Flags: UNSIGNED_SHORT, RecordNumber: UNSIGNED_LONG):
	request = ElfrReportEventExW()
	request["LogHandle"] = LogHandle
	request["TimeGenerated"] = TimeGenerated
	request["EventType"] = EventType
	request["EventCategory"] = EventCategory
	request["EventID"] = EventID
	request["NumStrings"] = NumStrings
	request["DataSize"] = DataSize
	request["ComputerName"] = ComputerName
	request["UserSID"] = UserSID
	request["Strings"] = Strings
	request["Data"] = Data
	request["Flags"] = Flags
	request["RecordNumber"] = RecordNumber
	return dce.request(request)

class ElfrReportEventExA(NDRCALL):
	opnum = 26
	structure = (
			(
			'LogHandle',
			IELF_HANDLE,

			),
			(
			'TimeGenerated',
			PFILETIME,

			),
			(
			'EventType',
			UNSIGNED_SHORT,

			),
			(
			'EventCategory',
			UNSIGNED_SHORT,

			),
			(
			'EventID',
			UNSIGNED_LONG,

			),
			(
			'NumStrings',
			UNSIGNED_SHORT,

			),
			(
			'DataSize',
			UNSIGNED_LONG,

			),
			(
			'ComputerName',
			PRPC_STRING,

			),
			(
			'UserSID',
			PRPC_SID,

			),
			(
			'Strings',
			PRPC_STRING_ARRAY,

			),
			(
			'Data',
			UNSIGNED_CHAR_ARRAY,

			),
			(
			'Flags',
			UNSIGNED_SHORT,

			),
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),

		)


class ElfrReportEventExAResponse(NDRCALL):
	structure = (
			(
			'RecordNumber',
			UNSIGNED_LONG,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hElfrReportEventExA(dce, LogHandle: IELF_HANDLE, TimeGenerated: PFILETIME, EventType: UNSIGNED_SHORT, EventCategory: UNSIGNED_SHORT, EventID: UNSIGNED_LONG, NumStrings: UNSIGNED_SHORT, DataSize: UNSIGNED_LONG, ComputerName: PRPC_STRING, UserSID: PRPC_SID, Strings: PRPC_STRING_ARRAY, Data: UNSIGNED_CHAR_ARRAY, Flags: UNSIGNED_SHORT, RecordNumber: UNSIGNED_LONG):
	request = ElfrReportEventExA()
	request["LogHandle"] = LogHandle
	request["TimeGenerated"] = TimeGenerated
	request["EventType"] = EventType
	request["EventCategory"] = EventCategory
	request["EventID"] = EventID
	request["NumStrings"] = NumStrings
	request["DataSize"] = DataSize
	request["ComputerName"] = ComputerName
	request["UserSID"] = UserSID
	request["Strings"] = Strings
	request["Data"] = Data
	request["Flags"] = Flags
	request["RecordNumber"] = RecordNumber
	return dce.request(request)

OPNUMS = {0 : (
	ElfrClearELFW,
	ElfrClearELFWResponse,

	),1 : (
	ElfrBackupELFW,
	ElfrBackupELFWResponse,

	),2 : (
	ElfrCloseEL,
	ElfrCloseELResponse,

	),3 : (
	ElfrDeregisterEventSource,
	ElfrDeregisterEventSourceResponse,

	),4 : (
	ElfrNumberOfRecords,
	ElfrNumberOfRecordsResponse,

	),5 : (
	ElfrOldestRecord,
	ElfrOldestRecordResponse,

	),6 : (
	ElfrChangeNotify,
	ElfrChangeNotifyResponse,

	),7 : (
	ElfrOpenELW,
	ElfrOpenELWResponse,

	),8 : (
	ElfrRegisterEventSourceW,
	ElfrRegisterEventSourceWResponse,

	),9 : (
	ElfrOpenBELW,
	ElfrOpenBELWResponse,

	),10 : (
	ElfrReadELW,
	ElfrReadELWResponse,

	),11 : (
	ElfrReportEventW,
	ElfrReportEventWResponse,

	),12 : (
	ElfrClearELFA,
	ElfrClearELFAResponse,

	),13 : (
	ElfrBackupELFA,
	ElfrBackupELFAResponse,

	),14 : (
	ElfrOpenELA,
	ElfrOpenELAResponse,

	),15 : (
	ElfrRegisterEventSourceA,
	ElfrRegisterEventSourceAResponse,

	),16 : (
	ElfrOpenBELA,
	ElfrOpenBELAResponse,

	),17 : (
	ElfrReadELA,
	ElfrReadELAResponse,

	),18 : (
	ElfrReportEventA,
	ElfrReportEventAResponse,

	),19 : (
	Opnum19NotUsedOnWire,
	Opnum19NotUsedOnWireResponse,

	),20 : (
	Opnum20NotUsedOnWire,
	Opnum20NotUsedOnWireResponse,

	),21 : (
	Opnum21NotUsedOnWire,
	Opnum21NotUsedOnWireResponse,

	),22 : (
	ElfrGetLogInformation,
	ElfrGetLogInformationResponse,

	),23 : (
	Opnum23NotUsedOnWire,
	Opnum23NotUsedOnWireResponse,

	),24 : (
	ElfrReportEventAndSourceW,
	ElfrReportEventAndSourceWResponse,

	),25 : (
	ElfrReportEventExW,
	ElfrReportEventExWResponse,

	),26 : (
	ElfrReportEventExA,
	ElfrReportEventExAResponse,

	)}
