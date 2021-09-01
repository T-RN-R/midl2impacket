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
#winspool Definition
#################################################################################
MSRPC_UUID_WINSPOOL = uuidtup_to_bin(('12345678-1234-ABCD-EF00-0123456789AB','1.0'))
OS_TYPE = DWORD__ENUM
VER_NT_WORKSTATION = 1
VER_NT_DOMAIN_CONTROLLER = 2
VER_NT_SERVER = 3
BIDI_TYPE = DWORD__ENUM
BIDI_NULL = 0
BIDI_INT = 1
BIDI_FLOAT = 2
BIDI_BOOL = 3
BIDI_STRING = 4
BIDI_TEXT = 5
BIDI_ENUM = 6
BIDI_BLOB = 7
RPC_EPRINTPROPERTYTYPE = DWORD__ENUM
kRpcPropertyTypeString = 1
kRpcPropertyTypeInt32 = 2
kRpcPropertyTypeInt64 = 3
kRpcPropertyTypeByte = 4
kRpcPropertyTypeBuffer = 5
LANGID = UNSIGNED_SHORT
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

class GDI_HANDLE(NDRSTRUCT):
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


class PGDI_HANDLE(NDRPOINTER):
	referent = (
			(
			'Data',
			GDI_HANDLE,

			),

		)

	@property
	def Data(self) -> GDI_HANDLE:
		return self['Data']

	@Data.setter
	def Data(self, prop:GDI_HANDLE):
		self['Data'] = prop


class PRINTER_HANDLE(NDRSTRUCT):
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


class PPRINTER_HANDLE(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_HANDLE,

			),

		)

	@property
	def Data(self) -> PRINTER_HANDLE:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_HANDLE):
		self['Data'] = prop


STRING_HANDLE = PWCHAR_T
class SIZE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cx',
			LONG,

			),
			(
			'cy',
			LONG,

			),

		)

	@property
	def cx(self) -> LONG:
		return self['cx']

	@cx.setter
	def cx(self, prop:LONG):
		self['cx'] = prop

	@property
	def cy(self) -> LONG:
		return self['cy']

	@cy.setter
	def cy(self, prop:LONG):
		self['cy'] = prop


class RECTL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'left',
			LONG,

			),
			(
			'top',
			LONG,

			),
			(
			'right',
			LONG,

			),
			(
			'bottom',
			LONG,

			),

		)

	@property
	def left(self) -> LONG:
		return self['left']

	@left.setter
	def left(self, prop:LONG):
		self['left'] = prop

	@property
	def top(self) -> LONG:
		return self['top']

	@top.setter
	def top(self, prop:LONG):
		self['top'] = prop

	@property
	def right(self) -> LONG:
		return self['right']

	@right.setter
	def right(self, prop:LONG):
		self['right'] = prop

	@property
	def bottom(self) -> LONG:
		return self['bottom']

	@bottom.setter
	def bottom(self, prop:LONG):
		self['bottom'] = prop


class WCHAR_T_ARRAY_32(NDRUniFixedArray):
	item = WCHAR_T

	def getDataLen(self, data, offset=0):
		type_size = len(self.item())
		return 32 * type_size

	def getData(self, _):
		# This is the length of our fixed array
		containerLength = self.getDataLen(None)
		# Truncate extra data provided beyond the maximum length
		raw = self.fields['Data'][:containerLength]
		# Add padding if necessary
		paddingLength = containerLength - (len(raw) % containerLength)
		raw += b'\x00' * paddingLength
		return raw


class DEVMODE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dmDeviceName',
			WCHAR_T_ARRAY_32,

			),
			(
			'dmSpecVersion',
			UNSIGNED_SHORT,

			),
			(
			'dmDriverVersion',
			UNSIGNED_SHORT,

			),
			(
			'dmSize',
			UNSIGNED_SHORT,

			),
			(
			'dmDriverExtra',
			UNSIGNED_SHORT,

			),
			(
			'dmFields',
			DWORD,

			),
			(
			'dmOrientation',
			SHORT,

			),
			(
			'dmPaperSize',
			SHORT,

			),
			(
			'dmPaperLength',
			SHORT,

			),
			(
			'dmPaperWidth',
			SHORT,

			),
			(
			'dmScale',
			SHORT,

			),
			(
			'dmCopies',
			SHORT,

			),
			(
			'dmDefaultSource',
			SHORT,

			),
			(
			'dmPrintQuality',
			SHORT,

			),
			(
			'dmColor',
			SHORT,

			),
			(
			'dmDuplex',
			SHORT,

			),
			(
			'dmYResolution',
			SHORT,

			),
			(
			'dmTTOption',
			SHORT,

			),
			(
			'dmCollate',
			SHORT,

			),
			(
			'dmFormName',
			WCHAR_T_ARRAY_32,

			),
			(
			'reserved0',
			UNSIGNED_SHORT,

			),
			(
			'reserved1',
			DWORD,

			),
			(
			'reserved2',
			DWORD,

			),
			(
			'reserved3',
			DWORD,

			),
			(
			'dmNup',
			DWORD,

			),
			(
			'reserved4',
			DWORD,

			),
			(
			'dmICMMethod',
			DWORD,

			),
			(
			'dmICMIntent',
			DWORD,

			),
			(
			'dmMediaType',
			DWORD,

			),
			(
			'dmDitherType',
			DWORD,

			),
			(
			'reserved5',
			DWORD,

			),
			(
			'reserved6',
			DWORD,

			),
			(
			'reserved7',
			DWORD,

			),
			(
			'reserved8',
			DWORD,

			),

		)

	@property
	def dmDeviceName(self) -> WCHAR_T_ARRAY_32:
		return self['dmDeviceName']

	@dmDeviceName.setter
	def dmDeviceName(self, prop:WCHAR_T_ARRAY_32):
		self['dmDeviceName'] = prop

	@property
	def dmSpecVersion(self) -> UNSIGNED_SHORT:
		return self['dmSpecVersion']

	@dmSpecVersion.setter
	def dmSpecVersion(self, prop:UNSIGNED_SHORT):
		self['dmSpecVersion'] = prop

	@property
	def dmDriverVersion(self) -> UNSIGNED_SHORT:
		return self['dmDriverVersion']

	@dmDriverVersion.setter
	def dmDriverVersion(self, prop:UNSIGNED_SHORT):
		self['dmDriverVersion'] = prop

	@property
	def dmSize(self) -> UNSIGNED_SHORT:
		return self['dmSize']

	@dmSize.setter
	def dmSize(self, prop:UNSIGNED_SHORT):
		self['dmSize'] = prop

	@property
	def dmDriverExtra(self) -> UNSIGNED_SHORT:
		return self['dmDriverExtra']

	@dmDriverExtra.setter
	def dmDriverExtra(self, prop:UNSIGNED_SHORT):
		self['dmDriverExtra'] = prop

	@property
	def dmFields(self) -> DWORD:
		return self['dmFields']

	@dmFields.setter
	def dmFields(self, prop:DWORD):
		self['dmFields'] = prop

	@property
	def dmOrientation(self) -> SHORT:
		return self['dmOrientation']

	@dmOrientation.setter
	def dmOrientation(self, prop:SHORT):
		self['dmOrientation'] = prop

	@property
	def dmPaperSize(self) -> SHORT:
		return self['dmPaperSize']

	@dmPaperSize.setter
	def dmPaperSize(self, prop:SHORT):
		self['dmPaperSize'] = prop

	@property
	def dmPaperLength(self) -> SHORT:
		return self['dmPaperLength']

	@dmPaperLength.setter
	def dmPaperLength(self, prop:SHORT):
		self['dmPaperLength'] = prop

	@property
	def dmPaperWidth(self) -> SHORT:
		return self['dmPaperWidth']

	@dmPaperWidth.setter
	def dmPaperWidth(self, prop:SHORT):
		self['dmPaperWidth'] = prop

	@property
	def dmScale(self) -> SHORT:
		return self['dmScale']

	@dmScale.setter
	def dmScale(self, prop:SHORT):
		self['dmScale'] = prop

	@property
	def dmCopies(self) -> SHORT:
		return self['dmCopies']

	@dmCopies.setter
	def dmCopies(self, prop:SHORT):
		self['dmCopies'] = prop

	@property
	def dmDefaultSource(self) -> SHORT:
		return self['dmDefaultSource']

	@dmDefaultSource.setter
	def dmDefaultSource(self, prop:SHORT):
		self['dmDefaultSource'] = prop

	@property
	def dmPrintQuality(self) -> SHORT:
		return self['dmPrintQuality']

	@dmPrintQuality.setter
	def dmPrintQuality(self, prop:SHORT):
		self['dmPrintQuality'] = prop

	@property
	def dmColor(self) -> SHORT:
		return self['dmColor']

	@dmColor.setter
	def dmColor(self, prop:SHORT):
		self['dmColor'] = prop

	@property
	def dmDuplex(self) -> SHORT:
		return self['dmDuplex']

	@dmDuplex.setter
	def dmDuplex(self, prop:SHORT):
		self['dmDuplex'] = prop

	@property
	def dmYResolution(self) -> SHORT:
		return self['dmYResolution']

	@dmYResolution.setter
	def dmYResolution(self, prop:SHORT):
		self['dmYResolution'] = prop

	@property
	def dmTTOption(self) -> SHORT:
		return self['dmTTOption']

	@dmTTOption.setter
	def dmTTOption(self, prop:SHORT):
		self['dmTTOption'] = prop

	@property
	def dmCollate(self) -> SHORT:
		return self['dmCollate']

	@dmCollate.setter
	def dmCollate(self, prop:SHORT):
		self['dmCollate'] = prop

	@property
	def dmFormName(self) -> WCHAR_T_ARRAY_32:
		return self['dmFormName']

	@dmFormName.setter
	def dmFormName(self, prop:WCHAR_T_ARRAY_32):
		self['dmFormName'] = prop

	@property
	def reserved0(self) -> UNSIGNED_SHORT:
		return self['reserved0']

	@reserved0.setter
	def reserved0(self, prop:UNSIGNED_SHORT):
		self['reserved0'] = prop

	@property
	def reserved1(self) -> DWORD:
		return self['reserved1']

	@reserved1.setter
	def reserved1(self, prop:DWORD):
		self['reserved1'] = prop

	@property
	def reserved2(self) -> DWORD:
		return self['reserved2']

	@reserved2.setter
	def reserved2(self, prop:DWORD):
		self['reserved2'] = prop

	@property
	def reserved3(self) -> DWORD:
		return self['reserved3']

	@reserved3.setter
	def reserved3(self, prop:DWORD):
		self['reserved3'] = prop

	@property
	def dmNup(self) -> DWORD:
		return self['dmNup']

	@dmNup.setter
	def dmNup(self, prop:DWORD):
		self['dmNup'] = prop

	@property
	def reserved4(self) -> DWORD:
		return self['reserved4']

	@reserved4.setter
	def reserved4(self, prop:DWORD):
		self['reserved4'] = prop

	@property
	def dmICMMethod(self) -> DWORD:
		return self['dmICMMethod']

	@dmICMMethod.setter
	def dmICMMethod(self, prop:DWORD):
		self['dmICMMethod'] = prop

	@property
	def dmICMIntent(self) -> DWORD:
		return self['dmICMIntent']

	@dmICMIntent.setter
	def dmICMIntent(self, prop:DWORD):
		self['dmICMIntent'] = prop

	@property
	def dmMediaType(self) -> DWORD:
		return self['dmMediaType']

	@dmMediaType.setter
	def dmMediaType(self, prop:DWORD):
		self['dmMediaType'] = prop

	@property
	def dmDitherType(self) -> DWORD:
		return self['dmDitherType']

	@dmDitherType.setter
	def dmDitherType(self, prop:DWORD):
		self['dmDitherType'] = prop

	@property
	def reserved5(self) -> DWORD:
		return self['reserved5']

	@reserved5.setter
	def reserved5(self, prop:DWORD):
		self['reserved5'] = prop

	@property
	def reserved6(self) -> DWORD:
		return self['reserved6']

	@reserved6.setter
	def reserved6(self, prop:DWORD):
		self['reserved6'] = prop

	@property
	def reserved7(self) -> DWORD:
		return self['reserved7']

	@reserved7.setter
	def reserved7(self, prop:DWORD):
		self['reserved7'] = prop

	@property
	def reserved8(self) -> DWORD:
		return self['reserved8']

	@reserved8.setter
	def reserved8(self, prop:DWORD):
		self['reserved8'] = prop


class DOC_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDocName',
			PWCHAR_T,

			),
			(
			'pOutputFile',
			PWCHAR_T,

			),
			(
			'pDatatype',
			PWCHAR_T,

			),

		)

	@property
	def pDocName(self) -> PWCHAR_T:
		return self['pDocName']

	@pDocName.setter
	def pDocName(self, prop:PWCHAR_T):
		self['pDocName'] = prop

	@property
	def pOutputFile(self) -> PWCHAR_T:
		return self['pOutputFile']

	@pOutputFile.setter
	def pOutputFile(self, prop:PWCHAR_T):
		self['pOutputFile'] = prop

	@property
	def pDatatype(self) -> PWCHAR_T:
		return self['pDatatype']

	@pDatatype.setter
	def pDatatype(self, prop:PWCHAR_T):
		self['pDatatype'] = prop


class DRIVER_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			PWCHAR_T,

			),

		)

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop


class DRIVER_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDriverPath',
			PWCHAR_T,

			),
			(
			'pDataFile',
			PWCHAR_T,

			),
			(
			'pConfigFile',
			PWCHAR_T,

			),

		)

	@property
	def cVersion(self) -> DWORD:
		return self['cVersion']

	@cVersion.setter
	def cVersion(self, prop:DWORD):
		self['cVersion'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDriverPath(self) -> PWCHAR_T:
		return self['pDriverPath']

	@pDriverPath.setter
	def pDriverPath(self, prop:PWCHAR_T):
		self['pDriverPath'] = prop

	@property
	def pDataFile(self) -> PWCHAR_T:
		return self['pDataFile']

	@pDataFile.setter
	def pDataFile(self, prop:PWCHAR_T):
		self['pDataFile'] = prop

	@property
	def pConfigFile(self) -> PWCHAR_T:
		return self['pConfigFile']

	@pConfigFile.setter
	def pConfigFile(self, prop:PWCHAR_T):
		self['pConfigFile'] = prop


class WCHAR_T_ARRAY(NDRUniConformantArray):
	item = WCHAR_T


class PWCHAR_T_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			WCHAR_T_ARRAY,

			),

		)

	@property
	def Data(self) -> WCHAR_T_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:WCHAR_T_ARRAY):
		self['Data'] = prop


class RPC_DRIVER_INFO_3_ARRAY(NDRUniConformantArray):
	item = WCHAR_T


class PRPC_DRIVER_INFO_3_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_3_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_3_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_3_ARRAY):
		self['Data'] = prop


class RPC_DRIVER_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDriverPath',
			PWCHAR_T,

			),
			(
			'pDataFile',
			PWCHAR_T,

			),
			(
			'pConfigFile',
			PWCHAR_T,

			),
			(
			'pHelpFile',
			PWCHAR_T,

			),
			(
			'pMonitorName',
			PWCHAR_T,

			),
			(
			'pDefaultDataType',
			PWCHAR_T,

			),
			(
			'cchDependentFiles',
			DWORD,

			),
			(
			'pDependentFiles',
			PWCHAR_T_ARRAY,

			),

		)

	@property
	def cVersion(self) -> DWORD:
		return self['cVersion']

	@cVersion.setter
	def cVersion(self, prop:DWORD):
		self['cVersion'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDriverPath(self) -> PWCHAR_T:
		return self['pDriverPath']

	@pDriverPath.setter
	def pDriverPath(self, prop:PWCHAR_T):
		self['pDriverPath'] = prop

	@property
	def pDataFile(self) -> PWCHAR_T:
		return self['pDataFile']

	@pDataFile.setter
	def pDataFile(self, prop:PWCHAR_T):
		self['pDataFile'] = prop

	@property
	def pConfigFile(self) -> PWCHAR_T:
		return self['pConfigFile']

	@pConfigFile.setter
	def pConfigFile(self, prop:PWCHAR_T):
		self['pConfigFile'] = prop

	@property
	def pHelpFile(self) -> PWCHAR_T:
		return self['pHelpFile']

	@pHelpFile.setter
	def pHelpFile(self, prop:PWCHAR_T):
		self['pHelpFile'] = prop

	@property
	def pMonitorName(self) -> PWCHAR_T:
		return self['pMonitorName']

	@pMonitorName.setter
	def pMonitorName(self, prop:PWCHAR_T):
		self['pMonitorName'] = prop

	@property
	def pDefaultDataType(self) -> PWCHAR_T:
		return self['pDefaultDataType']

	@pDefaultDataType.setter
	def pDefaultDataType(self, prop:PWCHAR_T):
		self['pDefaultDataType'] = prop

	@property
	def cchDependentFiles(self) -> DWORD:
		return self['cchDependentFiles']

	@cchDependentFiles.setter
	def cchDependentFiles(self, prop:DWORD):
		self['cchDependentFiles'] = prop

	@property
	def pDependentFiles(self) -> PWCHAR_T_ARRAY:
		return self['pDependentFiles']

	@pDependentFiles.setter
	def pDependentFiles(self, prop:PWCHAR_T_ARRAY):
		self['pDependentFiles'] = prop


class RPC_DRIVER_INFO_4_ARRAY(NDRUniConformantArray):
	item = WCHAR_T


class PRPC_DRIVER_INFO_4_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_4_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_4_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_4_ARRAY):
		self['Data'] = prop


class RPC_DRIVER_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDriverPath',
			PWCHAR_T,

			),
			(
			'pDataFile',
			PWCHAR_T,

			),
			(
			'pConfigFile',
			PWCHAR_T,

			),
			(
			'pHelpFile',
			PWCHAR_T,

			),
			(
			'pMonitorName',
			PWCHAR_T,

			),
			(
			'pDefaultDataType',
			PWCHAR_T,

			),
			(
			'cchDependentFiles',
			DWORD,

			),
			(
			'pDependentFiles',
			PWCHAR_T_ARRAY,

			),
			(
			'cchPreviousNames',
			DWORD,

			),
			(
			'pszzPreviousNames',
			PWCHAR_T_ARRAY,

			),

		)

	@property
	def cVersion(self) -> DWORD:
		return self['cVersion']

	@cVersion.setter
	def cVersion(self, prop:DWORD):
		self['cVersion'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDriverPath(self) -> PWCHAR_T:
		return self['pDriverPath']

	@pDriverPath.setter
	def pDriverPath(self, prop:PWCHAR_T):
		self['pDriverPath'] = prop

	@property
	def pDataFile(self) -> PWCHAR_T:
		return self['pDataFile']

	@pDataFile.setter
	def pDataFile(self, prop:PWCHAR_T):
		self['pDataFile'] = prop

	@property
	def pConfigFile(self) -> PWCHAR_T:
		return self['pConfigFile']

	@pConfigFile.setter
	def pConfigFile(self, prop:PWCHAR_T):
		self['pConfigFile'] = prop

	@property
	def pHelpFile(self) -> PWCHAR_T:
		return self['pHelpFile']

	@pHelpFile.setter
	def pHelpFile(self, prop:PWCHAR_T):
		self['pHelpFile'] = prop

	@property
	def pMonitorName(self) -> PWCHAR_T:
		return self['pMonitorName']

	@pMonitorName.setter
	def pMonitorName(self, prop:PWCHAR_T):
		self['pMonitorName'] = prop

	@property
	def pDefaultDataType(self) -> PWCHAR_T:
		return self['pDefaultDataType']

	@pDefaultDataType.setter
	def pDefaultDataType(self, prop:PWCHAR_T):
		self['pDefaultDataType'] = prop

	@property
	def cchDependentFiles(self) -> DWORD:
		return self['cchDependentFiles']

	@cchDependentFiles.setter
	def cchDependentFiles(self, prop:DWORD):
		self['cchDependentFiles'] = prop

	@property
	def pDependentFiles(self) -> PWCHAR_T_ARRAY:
		return self['pDependentFiles']

	@pDependentFiles.setter
	def pDependentFiles(self, prop:PWCHAR_T_ARRAY):
		self['pDependentFiles'] = prop

	@property
	def cchPreviousNames(self) -> DWORD:
		return self['cchPreviousNames']

	@cchPreviousNames.setter
	def cchPreviousNames(self, prop:DWORD):
		self['cchPreviousNames'] = prop

	@property
	def pszzPreviousNames(self) -> PWCHAR_T_ARRAY:
		return self['pszzPreviousNames']

	@pszzPreviousNames.setter
	def pszzPreviousNames(self, prop:PWCHAR_T_ARRAY):
		self['pszzPreviousNames'] = prop


class RPC_DRIVER_INFO_6_ARRAY(NDRUniConformantArray):
	item = WCHAR_T


class PRPC_DRIVER_INFO_6_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_6_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_6_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_6_ARRAY):
		self['Data'] = prop


class RPC_DRIVER_INFO_6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDriverPath',
			PWCHAR_T,

			),
			(
			'pDataFile',
			PWCHAR_T,

			),
			(
			'pConfigFile',
			PWCHAR_T,

			),
			(
			'pHelpFile',
			PWCHAR_T,

			),
			(
			'pMonitorName',
			PWCHAR_T,

			),
			(
			'pDefaultDataType',
			PWCHAR_T,

			),
			(
			'cchDependentFiles',
			DWORD,

			),
			(
			'pDependentFiles',
			PWCHAR_T_ARRAY,

			),
			(
			'cchPreviousNames',
			DWORD,

			),
			(
			'pszzPreviousNames',
			PWCHAR_T_ARRAY,

			),
			(
			'ftDriverDate',
			FILETIME,

			),
			(
			'dwlDriverVersion',
			DWORDLONG,

			),
			(
			'pMfgName',
			PWCHAR_T,

			),
			(
			'pOEMUrl',
			PWCHAR_T,

			),
			(
			'pHardwareID',
			PWCHAR_T,

			),
			(
			'pProvider',
			PWCHAR_T,

			),

		)

	@property
	def cVersion(self) -> DWORD:
		return self['cVersion']

	@cVersion.setter
	def cVersion(self, prop:DWORD):
		self['cVersion'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDriverPath(self) -> PWCHAR_T:
		return self['pDriverPath']

	@pDriverPath.setter
	def pDriverPath(self, prop:PWCHAR_T):
		self['pDriverPath'] = prop

	@property
	def pDataFile(self) -> PWCHAR_T:
		return self['pDataFile']

	@pDataFile.setter
	def pDataFile(self, prop:PWCHAR_T):
		self['pDataFile'] = prop

	@property
	def pConfigFile(self) -> PWCHAR_T:
		return self['pConfigFile']

	@pConfigFile.setter
	def pConfigFile(self, prop:PWCHAR_T):
		self['pConfigFile'] = prop

	@property
	def pHelpFile(self) -> PWCHAR_T:
		return self['pHelpFile']

	@pHelpFile.setter
	def pHelpFile(self, prop:PWCHAR_T):
		self['pHelpFile'] = prop

	@property
	def pMonitorName(self) -> PWCHAR_T:
		return self['pMonitorName']

	@pMonitorName.setter
	def pMonitorName(self, prop:PWCHAR_T):
		self['pMonitorName'] = prop

	@property
	def pDefaultDataType(self) -> PWCHAR_T:
		return self['pDefaultDataType']

	@pDefaultDataType.setter
	def pDefaultDataType(self, prop:PWCHAR_T):
		self['pDefaultDataType'] = prop

	@property
	def cchDependentFiles(self) -> DWORD:
		return self['cchDependentFiles']

	@cchDependentFiles.setter
	def cchDependentFiles(self, prop:DWORD):
		self['cchDependentFiles'] = prop

	@property
	def pDependentFiles(self) -> PWCHAR_T_ARRAY:
		return self['pDependentFiles']

	@pDependentFiles.setter
	def pDependentFiles(self, prop:PWCHAR_T_ARRAY):
		self['pDependentFiles'] = prop

	@property
	def cchPreviousNames(self) -> DWORD:
		return self['cchPreviousNames']

	@cchPreviousNames.setter
	def cchPreviousNames(self, prop:DWORD):
		self['cchPreviousNames'] = prop

	@property
	def pszzPreviousNames(self) -> PWCHAR_T_ARRAY:
		return self['pszzPreviousNames']

	@pszzPreviousNames.setter
	def pszzPreviousNames(self, prop:PWCHAR_T_ARRAY):
		self['pszzPreviousNames'] = prop

	@property
	def ftDriverDate(self) -> FILETIME:
		return self['ftDriverDate']

	@ftDriverDate.setter
	def ftDriverDate(self, prop:FILETIME):
		self['ftDriverDate'] = prop

	@property
	def dwlDriverVersion(self) -> DWORDLONG:
		return self['dwlDriverVersion']

	@dwlDriverVersion.setter
	def dwlDriverVersion(self, prop:DWORDLONG):
		self['dwlDriverVersion'] = prop

	@property
	def pMfgName(self) -> PWCHAR_T:
		return self['pMfgName']

	@pMfgName.setter
	def pMfgName(self, prop:PWCHAR_T):
		self['pMfgName'] = prop

	@property
	def pOEMUrl(self) -> PWCHAR_T:
		return self['pOEMUrl']

	@pOEMUrl.setter
	def pOEMUrl(self, prop:PWCHAR_T):
		self['pOEMUrl'] = prop

	@property
	def pHardwareID(self) -> PWCHAR_T:
		return self['pHardwareID']

	@pHardwareID.setter
	def pHardwareID(self, prop:PWCHAR_T):
		self['pHardwareID'] = prop

	@property
	def pProvider(self) -> PWCHAR_T:
		return self['pProvider']

	@pProvider.setter
	def pProvider(self, prop:PWCHAR_T):
		self['pProvider'] = prop


class RPC_DRIVER_INFO_8_ARRAY(NDRUniConformantArray):
	item = WCHAR_T


class PRPC_DRIVER_INFO_8_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_8_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_8_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_8_ARRAY):
		self['Data'] = prop


class RPC_DRIVER_INFO_8(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDriverPath',
			PWCHAR_T,

			),
			(
			'pDataFile',
			PWCHAR_T,

			),
			(
			'pConfigFile',
			PWCHAR_T,

			),
			(
			'pHelpFile',
			PWCHAR_T,

			),
			(
			'pMonitorName',
			PWCHAR_T,

			),
			(
			'pDefaultDataType',
			PWCHAR_T,

			),
			(
			'cchDependentFiles',
			DWORD,

			),
			(
			'pDependentFiles',
			PWCHAR_T_ARRAY,

			),
			(
			'cchPreviousNames',
			DWORD,

			),
			(
			'pszzPreviousNames',
			PWCHAR_T_ARRAY,

			),
			(
			'ftDriverDate',
			FILETIME,

			),
			(
			'dwlDriverVersion',
			DWORDLONG,

			),
			(
			'pMfgName',
			PWCHAR_T,

			),
			(
			'pOEMUrl',
			PWCHAR_T,

			),
			(
			'pHardwareID',
			PWCHAR_T,

			),
			(
			'pProvider',
			PWCHAR_T,

			),
			(
			'pPrintProcessor',
			PWCHAR_T,

			),
			(
			'pVendorSetup',
			PWCHAR_T,

			),
			(
			'cchColorProfiles',
			DWORD,

			),
			(
			'pszzColorProfiles',
			PWCHAR_T_ARRAY,

			),
			(
			'pInfPath',
			PWCHAR_T,

			),
			(
			'dwPrinterDriverAttributes',
			DWORD,

			),
			(
			'cchCoreDependencies',
			DWORD,

			),
			(
			'pszzCoreDriverDependencies',
			PWCHAR_T_ARRAY,

			),
			(
			'ftMinInboxDriverVerDate',
			FILETIME,

			),
			(
			'dwlMinInboxDriverVerVersion',
			DWORDLONG,

			),

		)

	@property
	def cVersion(self) -> DWORD:
		return self['cVersion']

	@cVersion.setter
	def cVersion(self, prop:DWORD):
		self['cVersion'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDriverPath(self) -> PWCHAR_T:
		return self['pDriverPath']

	@pDriverPath.setter
	def pDriverPath(self, prop:PWCHAR_T):
		self['pDriverPath'] = prop

	@property
	def pDataFile(self) -> PWCHAR_T:
		return self['pDataFile']

	@pDataFile.setter
	def pDataFile(self, prop:PWCHAR_T):
		self['pDataFile'] = prop

	@property
	def pConfigFile(self) -> PWCHAR_T:
		return self['pConfigFile']

	@pConfigFile.setter
	def pConfigFile(self, prop:PWCHAR_T):
		self['pConfigFile'] = prop

	@property
	def pHelpFile(self) -> PWCHAR_T:
		return self['pHelpFile']

	@pHelpFile.setter
	def pHelpFile(self, prop:PWCHAR_T):
		self['pHelpFile'] = prop

	@property
	def pMonitorName(self) -> PWCHAR_T:
		return self['pMonitorName']

	@pMonitorName.setter
	def pMonitorName(self, prop:PWCHAR_T):
		self['pMonitorName'] = prop

	@property
	def pDefaultDataType(self) -> PWCHAR_T:
		return self['pDefaultDataType']

	@pDefaultDataType.setter
	def pDefaultDataType(self, prop:PWCHAR_T):
		self['pDefaultDataType'] = prop

	@property
	def cchDependentFiles(self) -> DWORD:
		return self['cchDependentFiles']

	@cchDependentFiles.setter
	def cchDependentFiles(self, prop:DWORD):
		self['cchDependentFiles'] = prop

	@property
	def pDependentFiles(self) -> PWCHAR_T_ARRAY:
		return self['pDependentFiles']

	@pDependentFiles.setter
	def pDependentFiles(self, prop:PWCHAR_T_ARRAY):
		self['pDependentFiles'] = prop

	@property
	def cchPreviousNames(self) -> DWORD:
		return self['cchPreviousNames']

	@cchPreviousNames.setter
	def cchPreviousNames(self, prop:DWORD):
		self['cchPreviousNames'] = prop

	@property
	def pszzPreviousNames(self) -> PWCHAR_T_ARRAY:
		return self['pszzPreviousNames']

	@pszzPreviousNames.setter
	def pszzPreviousNames(self, prop:PWCHAR_T_ARRAY):
		self['pszzPreviousNames'] = prop

	@property
	def ftDriverDate(self) -> FILETIME:
		return self['ftDriverDate']

	@ftDriverDate.setter
	def ftDriverDate(self, prop:FILETIME):
		self['ftDriverDate'] = prop

	@property
	def dwlDriverVersion(self) -> DWORDLONG:
		return self['dwlDriverVersion']

	@dwlDriverVersion.setter
	def dwlDriverVersion(self, prop:DWORDLONG):
		self['dwlDriverVersion'] = prop

	@property
	def pMfgName(self) -> PWCHAR_T:
		return self['pMfgName']

	@pMfgName.setter
	def pMfgName(self, prop:PWCHAR_T):
		self['pMfgName'] = prop

	@property
	def pOEMUrl(self) -> PWCHAR_T:
		return self['pOEMUrl']

	@pOEMUrl.setter
	def pOEMUrl(self, prop:PWCHAR_T):
		self['pOEMUrl'] = prop

	@property
	def pHardwareID(self) -> PWCHAR_T:
		return self['pHardwareID']

	@pHardwareID.setter
	def pHardwareID(self, prop:PWCHAR_T):
		self['pHardwareID'] = prop

	@property
	def pProvider(self) -> PWCHAR_T:
		return self['pProvider']

	@pProvider.setter
	def pProvider(self, prop:PWCHAR_T):
		self['pProvider'] = prop

	@property
	def pPrintProcessor(self) -> PWCHAR_T:
		return self['pPrintProcessor']

	@pPrintProcessor.setter
	def pPrintProcessor(self, prop:PWCHAR_T):
		self['pPrintProcessor'] = prop

	@property
	def pVendorSetup(self) -> PWCHAR_T:
		return self['pVendorSetup']

	@pVendorSetup.setter
	def pVendorSetup(self, prop:PWCHAR_T):
		self['pVendorSetup'] = prop

	@property
	def cchColorProfiles(self) -> DWORD:
		return self['cchColorProfiles']

	@cchColorProfiles.setter
	def cchColorProfiles(self, prop:DWORD):
		self['cchColorProfiles'] = prop

	@property
	def pszzColorProfiles(self) -> PWCHAR_T_ARRAY:
		return self['pszzColorProfiles']

	@pszzColorProfiles.setter
	def pszzColorProfiles(self, prop:PWCHAR_T_ARRAY):
		self['pszzColorProfiles'] = prop

	@property
	def pInfPath(self) -> PWCHAR_T:
		return self['pInfPath']

	@pInfPath.setter
	def pInfPath(self, prop:PWCHAR_T):
		self['pInfPath'] = prop

	@property
	def dwPrinterDriverAttributes(self) -> DWORD:
		return self['dwPrinterDriverAttributes']

	@dwPrinterDriverAttributes.setter
	def dwPrinterDriverAttributes(self, prop:DWORD):
		self['dwPrinterDriverAttributes'] = prop

	@property
	def cchCoreDependencies(self) -> DWORD:
		return self['cchCoreDependencies']

	@cchCoreDependencies.setter
	def cchCoreDependencies(self, prop:DWORD):
		self['cchCoreDependencies'] = prop

	@property
	def pszzCoreDriverDependencies(self) -> PWCHAR_T_ARRAY:
		return self['pszzCoreDriverDependencies']

	@pszzCoreDriverDependencies.setter
	def pszzCoreDriverDependencies(self, prop:PWCHAR_T_ARRAY):
		self['pszzCoreDriverDependencies'] = prop

	@property
	def ftMinInboxDriverVerDate(self) -> FILETIME:
		return self['ftMinInboxDriverVerDate']

	@ftMinInboxDriverVerDate.setter
	def ftMinInboxDriverVerDate(self, prop:FILETIME):
		self['ftMinInboxDriverVerDate'] = prop

	@property
	def dwlMinInboxDriverVerVersion(self) -> DWORDLONG:
		return self['dwlMinInboxDriverVerVersion']

	@dwlMinInboxDriverVerVersion.setter
	def dwlMinInboxDriverVerVersion(self, prop:DWORDLONG):
		self['dwlMinInboxDriverVerVersion'] = prop


class FORM_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'Size',
			SIZE,

			),
			(
			'ImageableArea',
			RECTL,

			),

		)

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def Size(self) -> SIZE:
		return self['Size']

	@Size.setter
	def Size(self, prop:SIZE):
		self['Size'] = prop

	@property
	def ImageableArea(self) -> RECTL:
		return self['ImageableArea']

	@ImageableArea.setter
	def ImageableArea(self, prop:RECTL):
		self['ImageableArea'] = prop


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

class RPC_FORM_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'Size',
			SIZE,

			),
			(
			'ImageableArea',
			RECTL,

			),
			(
			'pKeyword',
			PCHAR,

			),
			(
			'StringType',
			DWORD,

			),
			(
			'pMuiDll',
			PWCHAR_T,

			),
			(
			'dwResourceId',
			DWORD,

			),
			(
			'pDisplayName',
			PWCHAR_T,

			),
			(
			'wLangID',
			LANGID,

			),

		)

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def Size(self) -> SIZE:
		return self['Size']

	@Size.setter
	def Size(self, prop:SIZE):
		self['Size'] = prop

	@property
	def ImageableArea(self) -> RECTL:
		return self['ImageableArea']

	@ImageableArea.setter
	def ImageableArea(self, prop:RECTL):
		self['ImageableArea'] = prop

	@property
	def pKeyword(self) -> PCHAR:
		return self['pKeyword']

	@pKeyword.setter
	def pKeyword(self, prop:PCHAR):
		self['pKeyword'] = prop

	@property
	def StringType(self) -> DWORD:
		return self['StringType']

	@StringType.setter
	def StringType(self, prop:DWORD):
		self['StringType'] = prop

	@property
	def pMuiDll(self) -> PWCHAR_T:
		return self['pMuiDll']

	@pMuiDll.setter
	def pMuiDll(self, prop:PWCHAR_T):
		self['pMuiDll'] = prop

	@property
	def dwResourceId(self) -> DWORD:
		return self['dwResourceId']

	@dwResourceId.setter
	def dwResourceId(self, prop:DWORD):
		self['dwResourceId'] = prop

	@property
	def pDisplayName(self) -> PWCHAR_T:
		return self['pDisplayName']

	@pDisplayName.setter
	def pDisplayName(self, prop:PWCHAR_T):
		self['pDisplayName'] = prop

	@property
	def wLangID(self) -> LANGID:
		return self['wLangID']

	@wLangID.setter
	def wLangID(self, prop:LANGID):
		self['wLangID'] = prop


class JOB_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'pDocument',
			PWCHAR_T,

			),
			(
			'pDatatype',
			PWCHAR_T,

			),
			(
			'pStatus',
			PWCHAR_T,

			),
			(
			'Status',
			DWORD,

			),
			(
			'Priority',
			DWORD,

			),
			(
			'Position',
			DWORD,

			),
			(
			'TotalPages',
			DWORD,

			),
			(
			'PagesPrinted',
			DWORD,

			),
			(
			'Submitted',
			SYSTEMTIME,

			),

		)

	@property
	def JobId(self) -> DWORD:
		return self['JobId']

	@JobId.setter
	def JobId(self, prop:DWORD):
		self['JobId'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def pDocument(self) -> PWCHAR_T:
		return self['pDocument']

	@pDocument.setter
	def pDocument(self, prop:PWCHAR_T):
		self['pDocument'] = prop

	@property
	def pDatatype(self) -> PWCHAR_T:
		return self['pDatatype']

	@pDatatype.setter
	def pDatatype(self, prop:PWCHAR_T):
		self['pDatatype'] = prop

	@property
	def pStatus(self) -> PWCHAR_T:
		return self['pStatus']

	@pStatus.setter
	def pStatus(self, prop:PWCHAR_T):
		self['pStatus'] = prop

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def Priority(self) -> DWORD:
		return self['Priority']

	@Priority.setter
	def Priority(self, prop:DWORD):
		self['Priority'] = prop

	@property
	def Position(self) -> DWORD:
		return self['Position']

	@Position.setter
	def Position(self, prop:DWORD):
		self['Position'] = prop

	@property
	def TotalPages(self) -> DWORD:
		return self['TotalPages']

	@TotalPages.setter
	def TotalPages(self, prop:DWORD):
		self['TotalPages'] = prop

	@property
	def PagesPrinted(self) -> DWORD:
		return self['PagesPrinted']

	@PagesPrinted.setter
	def PagesPrinted(self, prop:DWORD):
		self['PagesPrinted'] = prop

	@property
	def Submitted(self) -> SYSTEMTIME:
		return self['Submitted']

	@Submitted.setter
	def Submitted(self, prop:SYSTEMTIME):
		self['Submitted'] = prop


class JOB_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'pDocument',
			PWCHAR_T,

			),
			(
			'pNotifyName',
			PWCHAR_T,

			),
			(
			'pDatatype',
			PWCHAR_T,

			),
			(
			'pPrintProcessor',
			PWCHAR_T,

			),
			(
			'pParameters',
			PWCHAR_T,

			),
			(
			'pDriverName',
			PWCHAR_T,

			),
			(
			'pDevMode',
			ULONG_PTR,

			),
			(
			'pStatus',
			PWCHAR_T,

			),
			(
			'pSecurityDescriptor',
			ULONG_PTR,

			),
			(
			'Status',
			DWORD,

			),
			(
			'Priority',
			DWORD,

			),
			(
			'Position',
			DWORD,

			),
			(
			'StartTime',
			DWORD,

			),
			(
			'UntilTime',
			DWORD,

			),
			(
			'TotalPages',
			DWORD,

			),
			(
			'Size',
			DWORD,

			),
			(
			'Submitted',
			SYSTEMTIME,

			),
			(
			'Time',
			DWORD,

			),
			(
			'PagesPrinted',
			DWORD,

			),

		)

	@property
	def JobId(self) -> DWORD:
		return self['JobId']

	@JobId.setter
	def JobId(self, prop:DWORD):
		self['JobId'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def pDocument(self) -> PWCHAR_T:
		return self['pDocument']

	@pDocument.setter
	def pDocument(self, prop:PWCHAR_T):
		self['pDocument'] = prop

	@property
	def pNotifyName(self) -> PWCHAR_T:
		return self['pNotifyName']

	@pNotifyName.setter
	def pNotifyName(self, prop:PWCHAR_T):
		self['pNotifyName'] = prop

	@property
	def pDatatype(self) -> PWCHAR_T:
		return self['pDatatype']

	@pDatatype.setter
	def pDatatype(self, prop:PWCHAR_T):
		self['pDatatype'] = prop

	@property
	def pPrintProcessor(self) -> PWCHAR_T:
		return self['pPrintProcessor']

	@pPrintProcessor.setter
	def pPrintProcessor(self, prop:PWCHAR_T):
		self['pPrintProcessor'] = prop

	@property
	def pParameters(self) -> PWCHAR_T:
		return self['pParameters']

	@pParameters.setter
	def pParameters(self, prop:PWCHAR_T):
		self['pParameters'] = prop

	@property
	def pDriverName(self) -> PWCHAR_T:
		return self['pDriverName']

	@pDriverName.setter
	def pDriverName(self, prop:PWCHAR_T):
		self['pDriverName'] = prop

	@property
	def pDevMode(self) -> ULONG_PTR:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:ULONG_PTR):
		self['pDevMode'] = prop

	@property
	def pStatus(self) -> PWCHAR_T:
		return self['pStatus']

	@pStatus.setter
	def pStatus(self, prop:PWCHAR_T):
		self['pStatus'] = prop

	@property
	def pSecurityDescriptor(self) -> ULONG_PTR:
		return self['pSecurityDescriptor']

	@pSecurityDescriptor.setter
	def pSecurityDescriptor(self, prop:ULONG_PTR):
		self['pSecurityDescriptor'] = prop

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def Priority(self) -> DWORD:
		return self['Priority']

	@Priority.setter
	def Priority(self, prop:DWORD):
		self['Priority'] = prop

	@property
	def Position(self) -> DWORD:
		return self['Position']

	@Position.setter
	def Position(self, prop:DWORD):
		self['Position'] = prop

	@property
	def StartTime(self) -> DWORD:
		return self['StartTime']

	@StartTime.setter
	def StartTime(self, prop:DWORD):
		self['StartTime'] = prop

	@property
	def UntilTime(self) -> DWORD:
		return self['UntilTime']

	@UntilTime.setter
	def UntilTime(self, prop:DWORD):
		self['UntilTime'] = prop

	@property
	def TotalPages(self) -> DWORD:
		return self['TotalPages']

	@TotalPages.setter
	def TotalPages(self, prop:DWORD):
		self['TotalPages'] = prop

	@property
	def Size(self) -> DWORD:
		return self['Size']

	@Size.setter
	def Size(self, prop:DWORD):
		self['Size'] = prop

	@property
	def Submitted(self) -> SYSTEMTIME:
		return self['Submitted']

	@Submitted.setter
	def Submitted(self, prop:SYSTEMTIME):
		self['Submitted'] = prop

	@property
	def Time(self) -> DWORD:
		return self['Time']

	@Time.setter
	def Time(self, prop:DWORD):
		self['Time'] = prop

	@property
	def PagesPrinted(self) -> DWORD:
		return self['PagesPrinted']

	@PagesPrinted.setter
	def PagesPrinted(self, prop:DWORD):
		self['PagesPrinted'] = prop


class JOB_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD,

			),
			(
			'NextJobId',
			DWORD,

			),
			(
			'Reserved',
			DWORD,

			),

		)

	@property
	def JobId(self) -> DWORD:
		return self['JobId']

	@JobId.setter
	def JobId(self, prop:DWORD):
		self['JobId'] = prop

	@property
	def NextJobId(self) -> DWORD:
		return self['NextJobId']

	@NextJobId.setter
	def NextJobId(self, prop:DWORD):
		self['NextJobId'] = prop

	@property
	def Reserved(self) -> DWORD:
		return self['Reserved']

	@Reserved.setter
	def Reserved(self, prop:DWORD):
		self['Reserved'] = prop


class JOB_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'pDocument',
			PWCHAR_T,

			),
			(
			'pNotifyName',
			PWCHAR_T,

			),
			(
			'pDatatype',
			PWCHAR_T,

			),
			(
			'pPrintProcessor',
			PWCHAR_T,

			),
			(
			'pParameters',
			PWCHAR_T,

			),
			(
			'pDriverName',
			PWCHAR_T,

			),
			(
			'pDevMode',
			ULONG_PTR,

			),
			(
			'pStatus',
			PWCHAR_T,

			),
			(
			'pSecurityDescriptor',
			ULONG_PTR,

			),
			(
			'Status',
			DWORD,

			),
			(
			'Priority',
			DWORD,

			),
			(
			'Position',
			DWORD,

			),
			(
			'StartTime',
			DWORD,

			),
			(
			'UntilTime',
			DWORD,

			),
			(
			'TotalPages',
			DWORD,

			),
			(
			'Size',
			DWORD,

			),
			(
			'Submitted',
			SYSTEMTIME,

			),
			(
			'Time',
			DWORD,

			),
			(
			'PagesPrinted',
			DWORD,

			),
			(
			'SizeHigh',
			LONG,

			),

		)

	@property
	def JobId(self) -> DWORD:
		return self['JobId']

	@JobId.setter
	def JobId(self, prop:DWORD):
		self['JobId'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def pDocument(self) -> PWCHAR_T:
		return self['pDocument']

	@pDocument.setter
	def pDocument(self, prop:PWCHAR_T):
		self['pDocument'] = prop

	@property
	def pNotifyName(self) -> PWCHAR_T:
		return self['pNotifyName']

	@pNotifyName.setter
	def pNotifyName(self, prop:PWCHAR_T):
		self['pNotifyName'] = prop

	@property
	def pDatatype(self) -> PWCHAR_T:
		return self['pDatatype']

	@pDatatype.setter
	def pDatatype(self, prop:PWCHAR_T):
		self['pDatatype'] = prop

	@property
	def pPrintProcessor(self) -> PWCHAR_T:
		return self['pPrintProcessor']

	@pPrintProcessor.setter
	def pPrintProcessor(self, prop:PWCHAR_T):
		self['pPrintProcessor'] = prop

	@property
	def pParameters(self) -> PWCHAR_T:
		return self['pParameters']

	@pParameters.setter
	def pParameters(self, prop:PWCHAR_T):
		self['pParameters'] = prop

	@property
	def pDriverName(self) -> PWCHAR_T:
		return self['pDriverName']

	@pDriverName.setter
	def pDriverName(self, prop:PWCHAR_T):
		self['pDriverName'] = prop

	@property
	def pDevMode(self) -> ULONG_PTR:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:ULONG_PTR):
		self['pDevMode'] = prop

	@property
	def pStatus(self) -> PWCHAR_T:
		return self['pStatus']

	@pStatus.setter
	def pStatus(self, prop:PWCHAR_T):
		self['pStatus'] = prop

	@property
	def pSecurityDescriptor(self) -> ULONG_PTR:
		return self['pSecurityDescriptor']

	@pSecurityDescriptor.setter
	def pSecurityDescriptor(self, prop:ULONG_PTR):
		self['pSecurityDescriptor'] = prop

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def Priority(self) -> DWORD:
		return self['Priority']

	@Priority.setter
	def Priority(self, prop:DWORD):
		self['Priority'] = prop

	@property
	def Position(self) -> DWORD:
		return self['Position']

	@Position.setter
	def Position(self, prop:DWORD):
		self['Position'] = prop

	@property
	def StartTime(self) -> DWORD:
		return self['StartTime']

	@StartTime.setter
	def StartTime(self, prop:DWORD):
		self['StartTime'] = prop

	@property
	def UntilTime(self) -> DWORD:
		return self['UntilTime']

	@UntilTime.setter
	def UntilTime(self, prop:DWORD):
		self['UntilTime'] = prop

	@property
	def TotalPages(self) -> DWORD:
		return self['TotalPages']

	@TotalPages.setter
	def TotalPages(self, prop:DWORD):
		self['TotalPages'] = prop

	@property
	def Size(self) -> DWORD:
		return self['Size']

	@Size.setter
	def Size(self, prop:DWORD):
		self['Size'] = prop

	@property
	def Submitted(self) -> SYSTEMTIME:
		return self['Submitted']

	@Submitted.setter
	def Submitted(self, prop:SYSTEMTIME):
		self['Submitted'] = prop

	@property
	def Time(self) -> DWORD:
		return self['Time']

	@Time.setter
	def Time(self, prop:DWORD):
		self['Time'] = prop

	@property
	def PagesPrinted(self) -> DWORD:
		return self['PagesPrinted']

	@PagesPrinted.setter
	def PagesPrinted(self, prop:DWORD):
		self['PagesPrinted'] = prop

	@property
	def SizeHigh(self) -> LONG:
		return self['SizeHigh']

	@SizeHigh.setter
	def SizeHigh(self, prop:LONG):
		self['SizeHigh'] = prop


class MONITOR_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			PWCHAR_T,

			),

		)

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop


class MONITOR_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pEnvironment',
			PWCHAR_T,

			),
			(
			'pDLLName',
			PWCHAR_T,

			),

		)

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pEnvironment(self) -> PWCHAR_T:
		return self['pEnvironment']

	@pEnvironment.setter
	def pEnvironment(self, prop:PWCHAR_T):
		self['pEnvironment'] = prop

	@property
	def pDLLName(self) -> PWCHAR_T:
		return self['pDLLName']

	@pDLLName.setter
	def pDLLName(self, prop:PWCHAR_T):
		self['pDLLName'] = prop


class PORT_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			PWCHAR_T,

			),

		)

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop


class PORT_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			PWCHAR_T,

			),
			(
			'pMonitorName',
			PWCHAR_T,

			),
			(
			'pDescription',
			PWCHAR_T,

			),
			(
			'fPortType',
			DWORD,

			),
			(
			'Reserved',
			DWORD,

			),

		)

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop

	@property
	def pMonitorName(self) -> PWCHAR_T:
		return self['pMonitorName']

	@pMonitorName.setter
	def pMonitorName(self, prop:PWCHAR_T):
		self['pMonitorName'] = prop

	@property
	def pDescription(self) -> PWCHAR_T:
		return self['pDescription']

	@pDescription.setter
	def pDescription(self, prop:PWCHAR_T):
		self['pDescription'] = prop

	@property
	def fPortType(self) -> DWORD:
		return self['fPortType']

	@fPortType.setter
	def fPortType(self, prop:DWORD):
		self['fPortType'] = prop

	@property
	def Reserved(self) -> DWORD:
		return self['Reserved']

	@Reserved.setter
	def Reserved(self, prop:DWORD):
		self['Reserved'] = prop


class PORT_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwStatus',
			DWORD,

			),
			(
			'pszStatus',
			PWCHAR_T,

			),
			(
			'dwSeverity',
			DWORD,

			),

		)

	@property
	def dwStatus(self) -> DWORD:
		return self['dwStatus']

	@dwStatus.setter
	def dwStatus(self, prop:DWORD):
		self['dwStatus'] = prop

	@property
	def pszStatus(self) -> PWCHAR_T:
		return self['pszStatus']

	@pszStatus.setter
	def pszStatus(self, prop:PWCHAR_T):
		self['pszStatus'] = prop

	@property
	def dwSeverity(self) -> DWORD:
		return self['dwSeverity']

	@dwSeverity.setter
	def dwSeverity(self, prop:DWORD):
		self['dwSeverity'] = prop


class PORT_INFO_FF(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			PWCHAR_T,

			),
			(
			'cbMonitorData',
			DWORD,

			),
			(
			'pMonitorData',
			PBYTE,

			),

		)

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop

	@property
	def cbMonitorData(self) -> DWORD:
		return self['cbMonitorData']

	@cbMonitorData.setter
	def cbMonitorData(self, prop:DWORD):
		self['cbMonitorData'] = prop

	@property
	def pMonitorData(self) -> PBYTE:
		return self['pMonitorData']

	@pMonitorData.setter
	def pMonitorData(self, prop:PBYTE):
		self['pMonitorData'] = prop


class PRINTER_INFO_STRESS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pServerName',
			PWCHAR_T,

			),
			(
			'cJobs',
			DWORD,

			),
			(
			'cTotalJobs',
			DWORD,

			),
			(
			'cTotalBytes',
			DWORD,

			),
			(
			'stUpTime',
			SYSTEMTIME,

			),
			(
			'MaxcRef',
			DWORD,

			),
			(
			'cTotalPagesPrinted',
			DWORD,

			),
			(
			'dwGetVersion',
			DWORD,

			),
			(
			'fFreeBuild',
			DWORD,

			),
			(
			'cSpooling',
			DWORD,

			),
			(
			'cMaxSpooling',
			DWORD,

			),
			(
			'cRef',
			DWORD,

			),
			(
			'cErrorOutOfPaper',
			DWORD,

			),
			(
			'cErrorNotReady',
			DWORD,

			),
			(
			'cJobError',
			DWORD,

			),
			(
			'dwNumberOfProcessors',
			DWORD,

			),
			(
			'dwProcessorType',
			DWORD,

			),
			(
			'dwHighPartTotalBytes',
			DWORD,

			),
			(
			'cChangeID',
			DWORD,

			),
			(
			'dwLastError',
			DWORD,

			),
			(
			'Status',
			DWORD,

			),
			(
			'cEnumerateNetworkPrinters',
			DWORD,

			),
			(
			'cAddNetPrinters',
			DWORD,

			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT,

			),
			(
			'wProcessorLevel',
			UNSIGNED_SHORT,

			),
			(
			'cRefIC',
			DWORD,

			),
			(
			'dwReserved2',
			DWORD,

			),
			(
			'dwReserved3',
			DWORD,

			),

		)

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pServerName(self) -> PWCHAR_T:
		return self['pServerName']

	@pServerName.setter
	def pServerName(self, prop:PWCHAR_T):
		self['pServerName'] = prop

	@property
	def cJobs(self) -> DWORD:
		return self['cJobs']

	@cJobs.setter
	def cJobs(self, prop:DWORD):
		self['cJobs'] = prop

	@property
	def cTotalJobs(self) -> DWORD:
		return self['cTotalJobs']

	@cTotalJobs.setter
	def cTotalJobs(self, prop:DWORD):
		self['cTotalJobs'] = prop

	@property
	def cTotalBytes(self) -> DWORD:
		return self['cTotalBytes']

	@cTotalBytes.setter
	def cTotalBytes(self, prop:DWORD):
		self['cTotalBytes'] = prop

	@property
	def stUpTime(self) -> SYSTEMTIME:
		return self['stUpTime']

	@stUpTime.setter
	def stUpTime(self, prop:SYSTEMTIME):
		self['stUpTime'] = prop

	@property
	def MaxcRef(self) -> DWORD:
		return self['MaxcRef']

	@MaxcRef.setter
	def MaxcRef(self, prop:DWORD):
		self['MaxcRef'] = prop

	@property
	def cTotalPagesPrinted(self) -> DWORD:
		return self['cTotalPagesPrinted']

	@cTotalPagesPrinted.setter
	def cTotalPagesPrinted(self, prop:DWORD):
		self['cTotalPagesPrinted'] = prop

	@property
	def dwGetVersion(self) -> DWORD:
		return self['dwGetVersion']

	@dwGetVersion.setter
	def dwGetVersion(self, prop:DWORD):
		self['dwGetVersion'] = prop

	@property
	def fFreeBuild(self) -> DWORD:
		return self['fFreeBuild']

	@fFreeBuild.setter
	def fFreeBuild(self, prop:DWORD):
		self['fFreeBuild'] = prop

	@property
	def cSpooling(self) -> DWORD:
		return self['cSpooling']

	@cSpooling.setter
	def cSpooling(self, prop:DWORD):
		self['cSpooling'] = prop

	@property
	def cMaxSpooling(self) -> DWORD:
		return self['cMaxSpooling']

	@cMaxSpooling.setter
	def cMaxSpooling(self, prop:DWORD):
		self['cMaxSpooling'] = prop

	@property
	def cRef(self) -> DWORD:
		return self['cRef']

	@cRef.setter
	def cRef(self, prop:DWORD):
		self['cRef'] = prop

	@property
	def cErrorOutOfPaper(self) -> DWORD:
		return self['cErrorOutOfPaper']

	@cErrorOutOfPaper.setter
	def cErrorOutOfPaper(self, prop:DWORD):
		self['cErrorOutOfPaper'] = prop

	@property
	def cErrorNotReady(self) -> DWORD:
		return self['cErrorNotReady']

	@cErrorNotReady.setter
	def cErrorNotReady(self, prop:DWORD):
		self['cErrorNotReady'] = prop

	@property
	def cJobError(self) -> DWORD:
		return self['cJobError']

	@cJobError.setter
	def cJobError(self, prop:DWORD):
		self['cJobError'] = prop

	@property
	def dwNumberOfProcessors(self) -> DWORD:
		return self['dwNumberOfProcessors']

	@dwNumberOfProcessors.setter
	def dwNumberOfProcessors(self, prop:DWORD):
		self['dwNumberOfProcessors'] = prop

	@property
	def dwProcessorType(self) -> DWORD:
		return self['dwProcessorType']

	@dwProcessorType.setter
	def dwProcessorType(self, prop:DWORD):
		self['dwProcessorType'] = prop

	@property
	def dwHighPartTotalBytes(self) -> DWORD:
		return self['dwHighPartTotalBytes']

	@dwHighPartTotalBytes.setter
	def dwHighPartTotalBytes(self, prop:DWORD):
		self['dwHighPartTotalBytes'] = prop

	@property
	def cChangeID(self) -> DWORD:
		return self['cChangeID']

	@cChangeID.setter
	def cChangeID(self, prop:DWORD):
		self['cChangeID'] = prop

	@property
	def dwLastError(self) -> DWORD:
		return self['dwLastError']

	@dwLastError.setter
	def dwLastError(self, prop:DWORD):
		self['dwLastError'] = prop

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def cEnumerateNetworkPrinters(self) -> DWORD:
		return self['cEnumerateNetworkPrinters']

	@cEnumerateNetworkPrinters.setter
	def cEnumerateNetworkPrinters(self, prop:DWORD):
		self['cEnumerateNetworkPrinters'] = prop

	@property
	def cAddNetPrinters(self) -> DWORD:
		return self['cAddNetPrinters']

	@cAddNetPrinters.setter
	def cAddNetPrinters(self, prop:DWORD):
		self['cAddNetPrinters'] = prop

	@property
	def wProcessorArchitecture(self) -> UNSIGNED_SHORT:
		return self['wProcessorArchitecture']

	@wProcessorArchitecture.setter
	def wProcessorArchitecture(self, prop:UNSIGNED_SHORT):
		self['wProcessorArchitecture'] = prop

	@property
	def wProcessorLevel(self) -> UNSIGNED_SHORT:
		return self['wProcessorLevel']

	@wProcessorLevel.setter
	def wProcessorLevel(self, prop:UNSIGNED_SHORT):
		self['wProcessorLevel'] = prop

	@property
	def cRefIC(self) -> DWORD:
		return self['cRefIC']

	@cRefIC.setter
	def cRefIC(self, prop:DWORD):
		self['cRefIC'] = prop

	@property
	def dwReserved2(self) -> DWORD:
		return self['dwReserved2']

	@dwReserved2.setter
	def dwReserved2(self, prop:DWORD):
		self['dwReserved2'] = prop

	@property
	def dwReserved3(self) -> DWORD:
		return self['dwReserved3']

	@dwReserved3.setter
	def dwReserved3(self, prop:DWORD):
		self['dwReserved3'] = prop


class PRINTER_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD,

			),
			(
			'pDescription',
			PWCHAR_T,

			),
			(
			'pName',
			PWCHAR_T,

			),
			(
			'pComment',
			PWCHAR_T,

			),

		)

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def pDescription(self) -> PWCHAR_T:
		return self['pDescription']

	@pDescription.setter
	def pDescription(self, prop:PWCHAR_T):
		self['pDescription'] = prop

	@property
	def pName(self) -> PWCHAR_T:
		return self['pName']

	@pName.setter
	def pName(self, prop:PWCHAR_T):
		self['pName'] = prop

	@property
	def pComment(self) -> PWCHAR_T:
		return self['pComment']

	@pComment.setter
	def pComment(self, prop:PWCHAR_T):
		self['pComment'] = prop


class PRINTER_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pServerName',
			PWCHAR_T,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pShareName',
			PWCHAR_T,

			),
			(
			'pPortName',
			PWCHAR_T,

			),
			(
			'pDriverName',
			PWCHAR_T,

			),
			(
			'pComment',
			PWCHAR_T,

			),
			(
			'pLocation',
			PWCHAR_T,

			),
			(
			'pDevMode',
			ULONG_PTR,

			),
			(
			'pSepFile',
			PWCHAR_T,

			),
			(
			'pPrintProcessor',
			PWCHAR_T,

			),
			(
			'pDatatype',
			PWCHAR_T,

			),
			(
			'pParameters',
			PWCHAR_T,

			),
			(
			'pSecurityDescriptor',
			ULONG_PTR,

			),
			(
			'Attributes',
			DWORD,

			),
			(
			'Priority',
			DWORD,

			),
			(
			'DefaultPriority',
			DWORD,

			),
			(
			'StartTime',
			DWORD,

			),
			(
			'UntilTime',
			DWORD,

			),
			(
			'Status',
			DWORD,

			),
			(
			'cJobs',
			DWORD,

			),
			(
			'AveragePPM',
			DWORD,

			),

		)

	@property
	def pServerName(self) -> PWCHAR_T:
		return self['pServerName']

	@pServerName.setter
	def pServerName(self, prop:PWCHAR_T):
		self['pServerName'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pShareName(self) -> PWCHAR_T:
		return self['pShareName']

	@pShareName.setter
	def pShareName(self, prop:PWCHAR_T):
		self['pShareName'] = prop

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop

	@property
	def pDriverName(self) -> PWCHAR_T:
		return self['pDriverName']

	@pDriverName.setter
	def pDriverName(self, prop:PWCHAR_T):
		self['pDriverName'] = prop

	@property
	def pComment(self) -> PWCHAR_T:
		return self['pComment']

	@pComment.setter
	def pComment(self, prop:PWCHAR_T):
		self['pComment'] = prop

	@property
	def pLocation(self) -> PWCHAR_T:
		return self['pLocation']

	@pLocation.setter
	def pLocation(self, prop:PWCHAR_T):
		self['pLocation'] = prop

	@property
	def pDevMode(self) -> ULONG_PTR:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:ULONG_PTR):
		self['pDevMode'] = prop

	@property
	def pSepFile(self) -> PWCHAR_T:
		return self['pSepFile']

	@pSepFile.setter
	def pSepFile(self, prop:PWCHAR_T):
		self['pSepFile'] = prop

	@property
	def pPrintProcessor(self) -> PWCHAR_T:
		return self['pPrintProcessor']

	@pPrintProcessor.setter
	def pPrintProcessor(self, prop:PWCHAR_T):
		self['pPrintProcessor'] = prop

	@property
	def pDatatype(self) -> PWCHAR_T:
		return self['pDatatype']

	@pDatatype.setter
	def pDatatype(self, prop:PWCHAR_T):
		self['pDatatype'] = prop

	@property
	def pParameters(self) -> PWCHAR_T:
		return self['pParameters']

	@pParameters.setter
	def pParameters(self, prop:PWCHAR_T):
		self['pParameters'] = prop

	@property
	def pSecurityDescriptor(self) -> ULONG_PTR:
		return self['pSecurityDescriptor']

	@pSecurityDescriptor.setter
	def pSecurityDescriptor(self, prop:ULONG_PTR):
		self['pSecurityDescriptor'] = prop

	@property
	def Attributes(self) -> DWORD:
		return self['Attributes']

	@Attributes.setter
	def Attributes(self, prop:DWORD):
		self['Attributes'] = prop

	@property
	def Priority(self) -> DWORD:
		return self['Priority']

	@Priority.setter
	def Priority(self, prop:DWORD):
		self['Priority'] = prop

	@property
	def DefaultPriority(self) -> DWORD:
		return self['DefaultPriority']

	@DefaultPriority.setter
	def DefaultPriority(self, prop:DWORD):
		self['DefaultPriority'] = prop

	@property
	def StartTime(self) -> DWORD:
		return self['StartTime']

	@StartTime.setter
	def StartTime(self, prop:DWORD):
		self['StartTime'] = prop

	@property
	def UntilTime(self) -> DWORD:
		return self['UntilTime']

	@UntilTime.setter
	def UntilTime(self, prop:DWORD):
		self['UntilTime'] = prop

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def cJobs(self) -> DWORD:
		return self['cJobs']

	@cJobs.setter
	def cJobs(self, prop:DWORD):
		self['cJobs'] = prop

	@property
	def AveragePPM(self) -> DWORD:
		return self['AveragePPM']

	@AveragePPM.setter
	def AveragePPM(self, prop:DWORD):
		self['AveragePPM'] = prop


class PRINTER_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pSecurityDescriptor',
			ULONG_PTR,

			),

		)

	@property
	def pSecurityDescriptor(self) -> ULONG_PTR:
		return self['pSecurityDescriptor']

	@pSecurityDescriptor.setter
	def pSecurityDescriptor(self, prop:ULONG_PTR):
		self['pSecurityDescriptor'] = prop


class PRINTER_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pServerName',
			PWCHAR_T,

			),
			(
			'Attributes',
			DWORD,

			),

		)

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pServerName(self) -> PWCHAR_T:
		return self['pServerName']

	@pServerName.setter
	def pServerName(self, prop:PWCHAR_T):
		self['pServerName'] = prop

	@property
	def Attributes(self) -> DWORD:
		return self['Attributes']

	@Attributes.setter
	def Attributes(self, prop:DWORD):
		self['Attributes'] = prop


class PRINTER_INFO_5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pPortName',
			PWCHAR_T,

			),
			(
			'Attributes',
			DWORD,

			),
			(
			'DeviceNotSelectedTimeout',
			DWORD,

			),
			(
			'TransmissionRetryTimeout',
			DWORD,

			),

		)

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop

	@property
	def Attributes(self) -> DWORD:
		return self['Attributes']

	@Attributes.setter
	def Attributes(self, prop:DWORD):
		self['Attributes'] = prop

	@property
	def DeviceNotSelectedTimeout(self) -> DWORD:
		return self['DeviceNotSelectedTimeout']

	@DeviceNotSelectedTimeout.setter
	def DeviceNotSelectedTimeout(self, prop:DWORD):
		self['DeviceNotSelectedTimeout'] = prop

	@property
	def TransmissionRetryTimeout(self) -> DWORD:
		return self['TransmissionRetryTimeout']

	@TransmissionRetryTimeout.setter
	def TransmissionRetryTimeout(self, prop:DWORD):
		self['TransmissionRetryTimeout'] = prop


class PRINTER_INFO_6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwStatus',
			DWORD,

			),

		)

	@property
	def dwStatus(self) -> DWORD:
		return self['dwStatus']

	@dwStatus.setter
	def dwStatus(self, prop:DWORD):
		self['dwStatus'] = prop


class PRINTER_INFO_7(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pszObjectGUID',
			PWCHAR_T,

			),
			(
			'dwAction',
			DWORD,

			),

		)

	@property
	def pszObjectGUID(self) -> PWCHAR_T:
		return self['pszObjectGUID']

	@pszObjectGUID.setter
	def pszObjectGUID(self, prop:PWCHAR_T):
		self['pszObjectGUID'] = prop

	@property
	def dwAction(self) -> DWORD:
		return self['dwAction']

	@dwAction.setter
	def dwAction(self, prop:DWORD):
		self['dwAction'] = prop


class PRINTER_INFO_8(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDevMode',
			ULONG_PTR,

			),

		)

	@property
	def pDevMode(self) -> ULONG_PTR:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:ULONG_PTR):
		self['pDevMode'] = prop


class PRINTER_INFO_9(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDevMode',
			ULONG_PTR,

			),

		)

	@property
	def pDevMode(self) -> ULONG_PTR:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:ULONG_PTR):
		self['pDevMode'] = prop


class SPLCLIENT_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwSize',
			DWORD,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'dwBuildNum',
			DWORD,

			),
			(
			'dwMajorVersion',
			DWORD,

			),
			(
			'dwMinorVersion',
			DWORD,

			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT,

			),

		)

	@property
	def dwSize(self) -> DWORD:
		return self['dwSize']

	@dwSize.setter
	def dwSize(self, prop:DWORD):
		self['dwSize'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def dwBuildNum(self) -> DWORD:
		return self['dwBuildNum']

	@dwBuildNum.setter
	def dwBuildNum(self, prop:DWORD):
		self['dwBuildNum'] = prop

	@property
	def dwMajorVersion(self) -> DWORD:
		return self['dwMajorVersion']

	@dwMajorVersion.setter
	def dwMajorVersion(self, prop:DWORD):
		self['dwMajorVersion'] = prop

	@property
	def dwMinorVersion(self) -> DWORD:
		return self['dwMinorVersion']

	@dwMinorVersion.setter
	def dwMinorVersion(self, prop:DWORD):
		self['dwMinorVersion'] = prop

	@property
	def wProcessorArchitecture(self) -> UNSIGNED_SHORT:
		return self['wProcessorArchitecture']

	@wProcessorArchitecture.setter
	def wProcessorArchitecture(self, prop:UNSIGNED_SHORT):
		self['wProcessorArchitecture'] = prop


class SPLCLIENT_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'notUsed',
			LONG_PTR,

			),

		)

	@property
	def notUsed(self) -> LONG_PTR:
		return self['notUsed']

	@notUsed.setter
	def notUsed(self, prop:LONG_PTR):
		self['notUsed'] = prop


class SPLCLIENT_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbSize',
			UNSIGNED_INT,

			),
			(
			'dwFlags',
			DWORD,

			),
			(
			'dwSize',
			DWORD,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'dwBuildNum',
			DWORD,

			),
			(
			'dwMajorVersion',
			DWORD,

			),
			(
			'dwMinorVersion',
			DWORD,

			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT,

			),
			(
			'hSplPrinter',
			UNSIGNED___INT64,

			),

		)

	@property
	def cbSize(self) -> UNSIGNED_INT:
		return self['cbSize']

	@cbSize.setter
	def cbSize(self, prop:UNSIGNED_INT):
		self['cbSize'] = prop

	@property
	def dwFlags(self) -> DWORD:
		return self['dwFlags']

	@dwFlags.setter
	def dwFlags(self, prop:DWORD):
		self['dwFlags'] = prop

	@property
	def dwSize(self) -> DWORD:
		return self['dwSize']

	@dwSize.setter
	def dwSize(self, prop:DWORD):
		self['dwSize'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def dwBuildNum(self) -> DWORD:
		return self['dwBuildNum']

	@dwBuildNum.setter
	def dwBuildNum(self, prop:DWORD):
		self['dwBuildNum'] = prop

	@property
	def dwMajorVersion(self) -> DWORD:
		return self['dwMajorVersion']

	@dwMajorVersion.setter
	def dwMajorVersion(self, prop:DWORD):
		self['dwMajorVersion'] = prop

	@property
	def dwMinorVersion(self) -> DWORD:
		return self['dwMinorVersion']

	@dwMinorVersion.setter
	def dwMinorVersion(self, prop:DWORD):
		self['dwMinorVersion'] = prop

	@property
	def wProcessorArchitecture(self) -> UNSIGNED_SHORT:
		return self['wProcessorArchitecture']

	@wProcessorArchitecture.setter
	def wProcessorArchitecture(self, prop:UNSIGNED_SHORT):
		self['wProcessorArchitecture'] = prop

	@property
	def hSplPrinter(self) -> UNSIGNED___INT64:
		return self['hSplPrinter']

	@hSplPrinter.setter
	def hSplPrinter(self, prop:UNSIGNED___INT64):
		self['hSplPrinter'] = prop


class BYTE_ARRAY(NDRUniConformantArray):
	item = BYTE


class PBYTE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			BYTE_ARRAY,

			),

		)

	@property
	def Data(self) -> BYTE_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:BYTE_ARRAY):
		self['Data'] = prop


class DEVMODE_CONTAINER_ARRAY(NDRUniConformantArray):
	item = BYTE


class PDEVMODE_CONTAINER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			DEVMODE_CONTAINER_ARRAY,

			),

		)

	@property
	def Data(self) -> DEVMODE_CONTAINER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:DEVMODE_CONTAINER_ARRAY):
		self['Data'] = prop


class DEVMODE_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pDevMode',
			PBYTE_ARRAY,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pDevMode(self) -> PBYTE_ARRAY:
		return self['pDevMode']

	@pDevMode.setter
	def pDevMode(self, prop:PBYTE_ARRAY):
		self['pDevMode'] = prop


class PDOC_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			DOC_INFO_1,

			),

		)

	@property
	def Data(self) -> DOC_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:DOC_INFO_1):
		self['Data'] = prop

class DOCINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pDocInfo1',
		PDOC_INFO_1,

		)}

	@property
	def pDocInfo1(self) -> PDOC_INFO_1:
		return self['pDocInfo1']

	@pDocInfo1.setter
	def pDocInfo1(self, prop:PDOC_INFO_1):
		self['pDocInfo1'] = prop


class DOC_INFO_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'DocInfo',
			DOCINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def DocInfo(self) -> DOCINFO:
		return self['DocInfo']

	@DocInfo.setter
	def DocInfo(self, prop:DOCINFO):
		self['DocInfo'] = prop


class PDRIVER_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			DRIVER_INFO_1,

			),

		)

	@property
	def Data(self) -> DRIVER_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:DRIVER_INFO_1):
		self['Data'] = prop

class PDRIVER_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			DRIVER_INFO_2,

			),

		)

	@property
	def Data(self) -> DRIVER_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:DRIVER_INFO_2):
		self['Data'] = prop

class PRPC_DRIVER_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_3,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_3:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_3):
		self['Data'] = prop

class PRPC_DRIVER_INFO_4(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_4,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_4:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_4):
		self['Data'] = prop

class PRPC_DRIVER_INFO_6(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_6,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_6:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_6):
		self['Data'] = prop

class PRPC_DRIVER_INFO_8(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_DRIVER_INFO_8,

			),

		)

	@property
	def Data(self) -> RPC_DRIVER_INFO_8:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_DRIVER_INFO_8):
		self['Data'] = prop

class DRIVERINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pNotUsed',
		PDRIVER_INFO_1,

		),2 : (
		'Level2',
		PDRIVER_INFO_2,

		),3 : (
		'Level3',
		PRPC_DRIVER_INFO_3,

		),4 : (
		'Level4',
		PRPC_DRIVER_INFO_4,

		),6 : (
		'Level6',
		PRPC_DRIVER_INFO_6,

		),8 : (
		'Level8',
		PRPC_DRIVER_INFO_8,

		)}

	@property
	def pNotUsed(self) -> PDRIVER_INFO_1:
		return self['pNotUsed']

	@pNotUsed.setter
	def pNotUsed(self, prop:PDRIVER_INFO_1):
		self['pNotUsed'] = prop

	@property
	def Level2(self) -> PDRIVER_INFO_2:
		return self['Level2']

	@Level2.setter
	def Level2(self, prop:PDRIVER_INFO_2):
		self['Level2'] = prop

	@property
	def Level3(self) -> PRPC_DRIVER_INFO_3:
		return self['Level3']

	@Level3.setter
	def Level3(self, prop:PRPC_DRIVER_INFO_3):
		self['Level3'] = prop

	@property
	def Level4(self) -> PRPC_DRIVER_INFO_4:
		return self['Level4']

	@Level4.setter
	def Level4(self, prop:PRPC_DRIVER_INFO_4):
		self['Level4'] = prop

	@property
	def Level6(self) -> PRPC_DRIVER_INFO_6:
		return self['Level6']

	@Level6.setter
	def Level6(self, prop:PRPC_DRIVER_INFO_6):
		self['Level6'] = prop

	@property
	def Level8(self) -> PRPC_DRIVER_INFO_8:
		return self['Level8']

	@Level8.setter
	def Level8(self, prop:PRPC_DRIVER_INFO_8):
		self['Level8'] = prop


class DRIVER_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'DriverInfo',
			DRIVERINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def DriverInfo(self) -> DRIVERINFO:
		return self['DriverInfo']

	@DriverInfo.setter
	def DriverInfo(self, prop:DRIVERINFO):
		self['DriverInfo'] = prop


class PFORM_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			FORM_INFO_1,

			),

		)

	@property
	def Data(self) -> FORM_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:FORM_INFO_1):
		self['Data'] = prop

class PRPC_FORM_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_FORM_INFO_2,

			),

		)

	@property
	def Data(self) -> RPC_FORM_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_FORM_INFO_2):
		self['Data'] = prop

class FORMINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pFormInfo1',
		PFORM_INFO_1,

		),2 : (
		'pFormInfo2',
		PRPC_FORM_INFO_2,

		)}

	@property
	def pFormInfo1(self) -> PFORM_INFO_1:
		return self['pFormInfo1']

	@pFormInfo1.setter
	def pFormInfo1(self, prop:PFORM_INFO_1):
		self['pFormInfo1'] = prop

	@property
	def pFormInfo2(self) -> PRPC_FORM_INFO_2:
		return self['pFormInfo2']

	@pFormInfo2.setter
	def pFormInfo2(self, prop:PRPC_FORM_INFO_2):
		self['pFormInfo2'] = prop


class FORM_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'FormInfo',
			FORMINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def FormInfo(self) -> FORMINFO:
		return self['FormInfo']

	@FormInfo.setter
	def FormInfo(self, prop:FORMINFO):
		self['FormInfo'] = prop


class PJOB_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			JOB_INFO_1,

			),

		)

	@property
	def Data(self) -> JOB_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:JOB_INFO_1):
		self['Data'] = prop

class PJOB_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			JOB_INFO_2,

			),

		)

	@property
	def Data(self) -> JOB_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:JOB_INFO_2):
		self['Data'] = prop

class PJOB_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			JOB_INFO_3,

			),

		)

	@property
	def Data(self) -> JOB_INFO_3:
		return self['Data']

	@Data.setter
	def Data(self, prop:JOB_INFO_3):
		self['Data'] = prop

class PJOB_INFO_4(NDRPOINTER):
	referent = (
			(
			'Data',
			JOB_INFO_4,

			),

		)

	@property
	def Data(self) -> JOB_INFO_4:
		return self['Data']

	@Data.setter
	def Data(self, prop:JOB_INFO_4):
		self['Data'] = prop

class JOBINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'Level1',
		PJOB_INFO_1,

		),2 : (
		'Level2',
		PJOB_INFO_2,

		),3 : (
		'Level3',
		PJOB_INFO_3,

		),4 : (
		'Level4',
		PJOB_INFO_4,

		)}

	@property
	def Level1(self) -> PJOB_INFO_1:
		return self['Level1']

	@Level1.setter
	def Level1(self, prop:PJOB_INFO_1):
		self['Level1'] = prop

	@property
	def Level2(self) -> PJOB_INFO_2:
		return self['Level2']

	@Level2.setter
	def Level2(self, prop:PJOB_INFO_2):
		self['Level2'] = prop

	@property
	def Level3(self) -> PJOB_INFO_3:
		return self['Level3']

	@Level3.setter
	def Level3(self, prop:PJOB_INFO_3):
		self['Level3'] = prop

	@property
	def Level4(self) -> PJOB_INFO_4:
		return self['Level4']

	@Level4.setter
	def Level4(self, prop:PJOB_INFO_4):
		self['Level4'] = prop


class JOB_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'JobInfo',
			JOBINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def JobInfo(self) -> JOBINFO:
		return self['JobInfo']

	@JobInfo.setter
	def JobInfo(self, prop:JOBINFO):
		self['JobInfo'] = prop


class PMONITOR_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			MONITOR_INFO_1,

			),

		)

	@property
	def Data(self) -> MONITOR_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:MONITOR_INFO_1):
		self['Data'] = prop

class PMONITOR_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			MONITOR_INFO_2,

			),

		)

	@property
	def Data(self) -> MONITOR_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:MONITOR_INFO_2):
		self['Data'] = prop

class MONITORINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pMonitorInfo1',
		PMONITOR_INFO_1,

		),2 : (
		'pMonitorInfo2',
		PMONITOR_INFO_2,

		)}

	@property
	def pMonitorInfo1(self) -> PMONITOR_INFO_1:
		return self['pMonitorInfo1']

	@pMonitorInfo1.setter
	def pMonitorInfo1(self, prop:PMONITOR_INFO_1):
		self['pMonitorInfo1'] = prop

	@property
	def pMonitorInfo2(self) -> PMONITOR_INFO_2:
		return self['pMonitorInfo2']

	@pMonitorInfo2.setter
	def pMonitorInfo2(self, prop:PMONITOR_INFO_2):
		self['pMonitorInfo2'] = prop


class MONITOR_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'MonitorInfo',
			MONITORINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def MonitorInfo(self) -> MONITORINFO:
		return self['MonitorInfo']

	@MonitorInfo.setter
	def MonitorInfo(self, prop:MONITORINFO):
		self['MonitorInfo'] = prop


class PPORT_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_INFO_1,

			),

		)

	@property
	def Data(self) -> PORT_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_INFO_1):
		self['Data'] = prop

class PPORT_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_INFO_2,

			),

		)

	@property
	def Data(self) -> PORT_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_INFO_2):
		self['Data'] = prop

class PPORT_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_INFO_3,

			),

		)

	@property
	def Data(self) -> PORT_INFO_3:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_INFO_3):
		self['Data'] = prop

class PPORT_INFO_FF(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_INFO_FF,

			),

		)

	@property
	def Data(self) -> PORT_INFO_FF:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_INFO_FF):
		self['Data'] = prop

class PORTINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pPortInfo1',
		PPORT_INFO_1,

		),2 : (
		'pPortInfo2',
		PPORT_INFO_2,

		),3 : (
		'pPortInfo3',
		PPORT_INFO_3,

		),0x00FFFFFF : (
		'pPortInfoFF',
		PPORT_INFO_FF,

		)}

	@property
	def pPortInfo1(self) -> PPORT_INFO_1:
		return self['pPortInfo1']

	@pPortInfo1.setter
	def pPortInfo1(self, prop:PPORT_INFO_1):
		self['pPortInfo1'] = prop

	@property
	def pPortInfo2(self) -> PPORT_INFO_2:
		return self['pPortInfo2']

	@pPortInfo2.setter
	def pPortInfo2(self, prop:PPORT_INFO_2):
		self['pPortInfo2'] = prop

	@property
	def pPortInfo3(self) -> PPORT_INFO_3:
		return self['pPortInfo3']

	@pPortInfo3.setter
	def pPortInfo3(self, prop:PPORT_INFO_3):
		self['pPortInfo3'] = prop

	@property
	def pPortInfoFF(self) -> PPORT_INFO_FF:
		return self['pPortInfoFF']

	@pPortInfoFF.setter
	def pPortInfoFF(self, prop:PPORT_INFO_FF):
		self['pPortInfoFF'] = prop


class PORT_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'PortInfo',
			PORTINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def PortInfo(self) -> PORTINFO:
		return self['PortInfo']

	@PortInfo.setter
	def PortInfo(self, prop:PORTINFO):
		self['PortInfo'] = prop


class PORT_VAR_CONTAINER_ARRAY(NDRUniConformantArray):
	item = BYTE


class PPORT_VAR_CONTAINER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_VAR_CONTAINER_ARRAY,

			),

		)

	@property
	def Data(self) -> PORT_VAR_CONTAINER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_VAR_CONTAINER_ARRAY):
		self['Data'] = prop


class PORT_VAR_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbMonitorData',
			DWORD,

			),
			(
			'pMonitorData',
			PBYTE_ARRAY,

			),

		)

	@property
	def cbMonitorData(self) -> DWORD:
		return self['cbMonitorData']

	@cbMonitorData.setter
	def cbMonitorData(self, prop:DWORD):
		self['cbMonitorData'] = prop

	@property
	def pMonitorData(self) -> PBYTE_ARRAY:
		return self['pMonitorData']

	@pMonitorData.setter
	def pMonitorData(self, prop:PBYTE_ARRAY):
		self['pMonitorData'] = prop


class PPRINTER_INFO_STRESS(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_STRESS,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_STRESS:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_STRESS):
		self['Data'] = prop

class PPRINTER_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_1,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_1):
		self['Data'] = prop

class PPRINTER_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_2,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_2):
		self['Data'] = prop

class PPRINTER_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_3,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_3:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_3):
		self['Data'] = prop

class PPRINTER_INFO_4(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_4,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_4:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_4):
		self['Data'] = prop

class PPRINTER_INFO_5(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_5,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_5:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_5):
		self['Data'] = prop

class PPRINTER_INFO_6(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_6,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_6:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_6):
		self['Data'] = prop

class PPRINTER_INFO_7(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_7,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_7:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_7):
		self['Data'] = prop

class PPRINTER_INFO_8(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_8,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_8:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_8):
		self['Data'] = prop

class PPRINTER_INFO_9(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_INFO_9,

			),

		)

	@property
	def Data(self) -> PRINTER_INFO_9:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_INFO_9):
		self['Data'] = prop

class PRINTERINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {0 : (
		'pPrinterInfoStress',
		PPRINTER_INFO_STRESS,

		),1 : (
		'pPrinterInfo1',
		PPRINTER_INFO_1,

		),2 : (
		'pPrinterInfo2',
		PPRINTER_INFO_2,

		),3 : (
		'pPrinterInfo3',
		PPRINTER_INFO_3,

		),4 : (
		'pPrinterInfo4',
		PPRINTER_INFO_4,

		),5 : (
		'pPrinterInfo5',
		PPRINTER_INFO_5,

		),6 : (
		'pPrinterInfo6',
		PPRINTER_INFO_6,

		),7 : (
		'pPrinterInfo7',
		PPRINTER_INFO_7,

		),8 : (
		'pPrinterInfo8',
		PPRINTER_INFO_8,

		),9 : (
		'pPrinterInfo9',
		PPRINTER_INFO_9,

		)}

	@property
	def pPrinterInfoStress(self) -> PPRINTER_INFO_STRESS:
		return self['pPrinterInfoStress']

	@pPrinterInfoStress.setter
	def pPrinterInfoStress(self, prop:PPRINTER_INFO_STRESS):
		self['pPrinterInfoStress'] = prop

	@property
	def pPrinterInfo1(self) -> PPRINTER_INFO_1:
		return self['pPrinterInfo1']

	@pPrinterInfo1.setter
	def pPrinterInfo1(self, prop:PPRINTER_INFO_1):
		self['pPrinterInfo1'] = prop

	@property
	def pPrinterInfo2(self) -> PPRINTER_INFO_2:
		return self['pPrinterInfo2']

	@pPrinterInfo2.setter
	def pPrinterInfo2(self, prop:PPRINTER_INFO_2):
		self['pPrinterInfo2'] = prop

	@property
	def pPrinterInfo3(self) -> PPRINTER_INFO_3:
		return self['pPrinterInfo3']

	@pPrinterInfo3.setter
	def pPrinterInfo3(self, prop:PPRINTER_INFO_3):
		self['pPrinterInfo3'] = prop

	@property
	def pPrinterInfo4(self) -> PPRINTER_INFO_4:
		return self['pPrinterInfo4']

	@pPrinterInfo4.setter
	def pPrinterInfo4(self, prop:PPRINTER_INFO_4):
		self['pPrinterInfo4'] = prop

	@property
	def pPrinterInfo5(self) -> PPRINTER_INFO_5:
		return self['pPrinterInfo5']

	@pPrinterInfo5.setter
	def pPrinterInfo5(self, prop:PPRINTER_INFO_5):
		self['pPrinterInfo5'] = prop

	@property
	def pPrinterInfo6(self) -> PPRINTER_INFO_6:
		return self['pPrinterInfo6']

	@pPrinterInfo6.setter
	def pPrinterInfo6(self, prop:PPRINTER_INFO_6):
		self['pPrinterInfo6'] = prop

	@property
	def pPrinterInfo7(self) -> PPRINTER_INFO_7:
		return self['pPrinterInfo7']

	@pPrinterInfo7.setter
	def pPrinterInfo7(self, prop:PPRINTER_INFO_7):
		self['pPrinterInfo7'] = prop

	@property
	def pPrinterInfo8(self) -> PPRINTER_INFO_8:
		return self['pPrinterInfo8']

	@pPrinterInfo8.setter
	def pPrinterInfo8(self, prop:PPRINTER_INFO_8):
		self['pPrinterInfo8'] = prop

	@property
	def pPrinterInfo9(self) -> PPRINTER_INFO_9:
		return self['pPrinterInfo9']

	@pPrinterInfo9.setter
	def pPrinterInfo9(self, prop:PPRINTER_INFO_9):
		self['pPrinterInfo9'] = prop


class PRINTER_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'PrinterInfo',
			PRINTERINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def PrinterInfo(self) -> PRINTERINFO:
		return self['PrinterInfo']

	@PrinterInfo.setter
	def PrinterInfo(self, prop:PRINTERINFO):
		self['PrinterInfo'] = prop


class RPC_BINARY_CONTAINER_ARRAY(NDRUniConformantArray):
	item = BYTE


class PRPC_BINARY_CONTAINER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_BINARY_CONTAINER_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_BINARY_CONTAINER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_BINARY_CONTAINER_ARRAY):
		self['Data'] = prop


class RPC_BINARY_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pszString',
			PBYTE_ARRAY,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pszString(self) -> PBYTE_ARRAY:
		return self['pszString']

	@pszString.setter
	def pszString(self, prop:PBYTE_ARRAY):
		self['pszString'] = prop


class U(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {BIDI_NULL : (
		'bData',
		INT,

		),BIDI_INT : (
		'iData',
		LONG,

		),BIDI_STRING : (
		'sData',
		PWCHAR_T,

		),BIDI_FLOAT : (
		'fData',
		FLOAT,

		),BIDI_BLOB : (
		'biData',
		RPC_BINARY_CONTAINER,

		)}

	@property
	def bData(self) -> INT:
		return self['bData']

	@bData.setter
	def bData(self, prop:INT):
		self['bData'] = prop

	@property
	def iData(self) -> LONG:
		return self['iData']

	@iData.setter
	def iData(self, prop:LONG):
		self['iData'] = prop

	@property
	def sData(self) -> PWCHAR_T:
		return self['sData']

	@sData.setter
	def sData(self, prop:PWCHAR_T):
		self['sData'] = prop

	@property
	def fData(self) -> FLOAT:
		return self['fData']

	@fData.setter
	def fData(self, prop:FLOAT):
		self['fData'] = prop

	@property
	def biData(self) -> RPC_BINARY_CONTAINER:
		return self['biData']

	@biData.setter
	def biData(self, prop:RPC_BINARY_CONTAINER):
		self['biData'] = prop


class RPC_BIDI_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwBidiType',
			DWORD,

			),
			(
			'u',
			U,

			),

		)

	@property
	def dwBidiType(self) -> DWORD:
		return self['dwBidiType']

	@dwBidiType.setter
	def dwBidiType(self, prop:DWORD):
		self['dwBidiType'] = prop

	@property
	def u(self) -> U:
		return self['u']

	@u.setter
	def u(self, prop:U):
		self['u'] = prop


class RPC_BIDI_REQUEST_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwReqNumber',
			DWORD,

			),
			(
			'pSchema',
			PWCHAR_T,

			),
			(
			'data',
			RPC_BIDI_DATA,

			),

		)

	@property
	def dwReqNumber(self) -> DWORD:
		return self['dwReqNumber']

	@dwReqNumber.setter
	def dwReqNumber(self, prop:DWORD):
		self['dwReqNumber'] = prop

	@property
	def pSchema(self) -> PWCHAR_T:
		return self['pSchema']

	@pSchema.setter
	def pSchema(self, prop:PWCHAR_T):
		self['pSchema'] = prop

	@property
	def data(self) -> RPC_BIDI_DATA:
		return self['data']

	@data.setter
	def data(self, prop:RPC_BIDI_DATA):
		self['data'] = prop


class RPC_BIDI_RESPONSE_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwResult',
			DWORD,

			),
			(
			'dwReqNumber',
			DWORD,

			),
			(
			'pSchema',
			PWCHAR_T,

			),
			(
			'data',
			RPC_BIDI_DATA,

			),

		)

	@property
	def dwResult(self) -> DWORD:
		return self['dwResult']

	@dwResult.setter
	def dwResult(self, prop:DWORD):
		self['dwResult'] = prop

	@property
	def dwReqNumber(self) -> DWORD:
		return self['dwReqNumber']

	@dwReqNumber.setter
	def dwReqNumber(self, prop:DWORD):
		self['dwReqNumber'] = prop

	@property
	def pSchema(self) -> PWCHAR_T:
		return self['pSchema']

	@pSchema.setter
	def pSchema(self, prop:PWCHAR_T):
		self['pSchema'] = prop

	@property
	def data(self) -> RPC_BIDI_DATA:
		return self['data']

	@data.setter
	def data(self, prop:RPC_BIDI_DATA):
		self['data'] = prop


class RPC_BIDI_REQUEST_DATA_ARRAY(NDRUniConformantArray):
	item = RPC_BIDI_REQUEST_DATA


class RPC_BIDI_REQUEST_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD,

			),
			(
			'Flags',
			DWORD,

			),
			(
			'Count',
			DWORD,

			),
			(
			'aData',
			RPC_BIDI_REQUEST_DATA_ARRAY,

			),

		)

	@property
	def Version(self) -> DWORD:
		return self['Version']

	@Version.setter
	def Version(self, prop:DWORD):
		self['Version'] = prop

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def Count(self) -> DWORD:
		return self['Count']

	@Count.setter
	def Count(self, prop:DWORD):
		self['Count'] = prop

	@property
	def aData(self) -> RPC_BIDI_REQUEST_DATA_ARRAY:
		return self['aData']

	@aData.setter
	def aData(self, prop:RPC_BIDI_REQUEST_DATA_ARRAY):
		self['aData'] = prop


class RPC_BIDI_RESPONSE_DATA_ARRAY(NDRUniConformantArray):
	item = RPC_BIDI_RESPONSE_DATA


class RPC_BIDI_RESPONSE_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD,

			),
			(
			'Flags',
			DWORD,

			),
			(
			'Count',
			DWORD,

			),
			(
			'aData',
			RPC_BIDI_RESPONSE_DATA_ARRAY,

			),

		)

	@property
	def Version(self) -> DWORD:
		return self['Version']

	@Version.setter
	def Version(self, prop:DWORD):
		self['Version'] = prop

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def Count(self) -> DWORD:
		return self['Count']

	@Count.setter
	def Count(self, prop:DWORD):
		self['Count'] = prop

	@property
	def aData(self) -> RPC_BIDI_RESPONSE_DATA_ARRAY:
		return self['aData']

	@aData.setter
	def aData(self, prop:RPC_BIDI_RESPONSE_DATA_ARRAY):
		self['aData'] = prop


class SECURITY_CONTAINER_ARRAY(NDRUniConformantArray):
	item = BYTE


class PSECURITY_CONTAINER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			SECURITY_CONTAINER_ARRAY,

			),

		)

	@property
	def Data(self) -> SECURITY_CONTAINER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:SECURITY_CONTAINER_ARRAY):
		self['Data'] = prop


class SECURITY_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pSecurity',
			PBYTE_ARRAY,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pSecurity(self) -> PBYTE_ARRAY:
		return self['pSecurity']

	@pSecurity.setter
	def pSecurity(self, prop:PBYTE_ARRAY):
		self['pSecurity'] = prop


class PSPLCLIENT_INFO_1(NDRPOINTER):
	referent = (
			(
			'Data',
			SPLCLIENT_INFO_1,

			),

		)

	@property
	def Data(self) -> SPLCLIENT_INFO_1:
		return self['Data']

	@Data.setter
	def Data(self, prop:SPLCLIENT_INFO_1):
		self['Data'] = prop

class PSPLCLIENT_INFO_2(NDRPOINTER):
	referent = (
			(
			'Data',
			SPLCLIENT_INFO_2,

			),

		)

	@property
	def Data(self) -> SPLCLIENT_INFO_2:
		return self['Data']

	@Data.setter
	def Data(self, prop:SPLCLIENT_INFO_2):
		self['Data'] = prop

class PSPLCLIENT_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			SPLCLIENT_INFO_3,

			),

		)

	@property
	def Data(self) -> SPLCLIENT_INFO_3:
		return self['Data']

	@Data.setter
	def Data(self, prop:SPLCLIENT_INFO_3):
		self['Data'] = prop

class CLIENTINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {1 : (
		'pClientInfo1',
		PSPLCLIENT_INFO_1,

		),2 : (
		'pNotUsed1',
		PSPLCLIENT_INFO_2,

		),3 : (
		'pNotUsed2',
		PSPLCLIENT_INFO_3,

		)}

	@property
	def pClientInfo1(self) -> PSPLCLIENT_INFO_1:
		return self['pClientInfo1']

	@pClientInfo1.setter
	def pClientInfo1(self, prop:PSPLCLIENT_INFO_1):
		self['pClientInfo1'] = prop

	@property
	def pNotUsed1(self) -> PSPLCLIENT_INFO_2:
		return self['pNotUsed1']

	@pNotUsed1.setter
	def pNotUsed1(self, prop:PSPLCLIENT_INFO_2):
		self['pNotUsed1'] = prop

	@property
	def pNotUsed2(self) -> PSPLCLIENT_INFO_3:
		return self['pNotUsed2']

	@pNotUsed2.setter
	def pNotUsed2(self, prop:PSPLCLIENT_INFO_3):
		self['pNotUsed2'] = prop


class SPLCLIENT_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD,

			),
			(
			'ClientInfo',
			CLIENTINFO,

			),

		)

	@property
	def Level(self) -> DWORD:
		return self['Level']

	@Level.setter
	def Level(self, prop:DWORD):
		self['Level'] = prop

	@property
	def ClientInfo(self) -> CLIENTINFO:
		return self['ClientInfo']

	@ClientInfo.setter
	def ClientInfo(self, prop:CLIENTINFO):
		self['ClientInfo'] = prop


class WCHAR_ARRAY(NDRUniConformantArray):
	item = WCHAR


class PWCHAR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			WCHAR_ARRAY,

			),

		)

	@property
	def Data(self) -> WCHAR_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:WCHAR_ARRAY):
		self['Data'] = prop


class STRING_CONTAINER_ARRAY(NDRUniConformantArray):
	item = WCHAR


class PSTRING_CONTAINER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			STRING_CONTAINER_ARRAY,

			),

		)

	@property
	def Data(self) -> STRING_CONTAINER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:STRING_CONTAINER_ARRAY):
		self['Data'] = prop


class STRING_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pszString',
			PWCHAR_ARRAY,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pszString(self) -> PWCHAR_ARRAY:
		return self['pszString']

	@pszString.setter
	def pszString(self, prop:PWCHAR_ARRAY):
		self['pszString'] = prop


class PSYSTEMTIME(NDRPOINTER):
	referent = (
			(
			'Data',
			SYSTEMTIME,

			),

		)

	@property
	def Data(self) -> SYSTEMTIME:
		return self['Data']

	@Data.setter
	def Data(self, prop:SYSTEMTIME):
		self['Data'] = prop

class SYSTEMTIME_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pSystemTime',
			PSYSTEMTIME,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pSystemTime(self) -> PSYSTEMTIME:
		return self['pSystemTime']

	@pSystemTime.setter
	def pSystemTime(self, prop:PSYSTEMTIME):
		self['pSystemTime'] = prop


class UNSIGNED_SHORT_ARRAY(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PUNSIGNED_SHORT_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			UNSIGNED_SHORT_ARRAY,

			),

		)

	@property
	def Data(self) -> UNSIGNED_SHORT_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:UNSIGNED_SHORT_ARRAY):
		self['Data'] = prop


class RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PRPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY):
		self['Data'] = prop


class RPC_V2_NOTIFY_OPTIONS_TYPE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Type',
			UNSIGNED_SHORT,

			),
			(
			'Reserved0',
			UNSIGNED_SHORT,

			),
			(
			'Reserved1',
			DWORD,

			),
			(
			'Reserved2',
			DWORD,

			),
			(
			'Count',
			DWORD,

			),
			(
			'pFields',
			PUNSIGNED_SHORT_ARRAY,

			),

		)

	@property
	def Type(self) -> UNSIGNED_SHORT:
		return self['Type']

	@Type.setter
	def Type(self, prop:UNSIGNED_SHORT):
		self['Type'] = prop

	@property
	def Reserved0(self) -> UNSIGNED_SHORT:
		return self['Reserved0']

	@Reserved0.setter
	def Reserved0(self, prop:UNSIGNED_SHORT):
		self['Reserved0'] = prop

	@property
	def Reserved1(self) -> DWORD:
		return self['Reserved1']

	@Reserved1.setter
	def Reserved1(self, prop:DWORD):
		self['Reserved1'] = prop

	@property
	def Reserved2(self) -> DWORD:
		return self['Reserved2']

	@Reserved2.setter
	def Reserved2(self, prop:DWORD):
		self['Reserved2'] = prop

	@property
	def Count(self) -> DWORD:
		return self['Count']

	@Count.setter
	def Count(self, prop:DWORD):
		self['Count'] = prop

	@property
	def pFields(self) -> PUNSIGNED_SHORT_ARRAY:
		return self['pFields']

	@pFields.setter
	def pFields(self, prop:PUNSIGNED_SHORT_ARRAY):
		self['pFields'] = prop


class RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY(NDRUniConformantArray):
	item = RPC_V2_NOTIFY_OPTIONS_TYPE


class PRPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY):
		self['Data'] = prop


class RPC_V2_NOTIFY_OPTIONS_ARRAY(NDRUniConformantArray):
	item = RPC_V2_NOTIFY_OPTIONS_TYPE


class PRPC_V2_NOTIFY_OPTIONS_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_V2_NOTIFY_OPTIONS_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_V2_NOTIFY_OPTIONS_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_OPTIONS_ARRAY):
		self['Data'] = prop


class RPC_V2_NOTIFY_OPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD,

			),
			(
			'Reserved',
			DWORD,

			),
			(
			'Count',
			DWORD,

			),
			(
			'pTypes',
			PRPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY,

			),

		)

	@property
	def Version(self) -> DWORD:
		return self['Version']

	@Version.setter
	def Version(self, prop:DWORD):
		self['Version'] = prop

	@property
	def Reserved(self) -> DWORD:
		return self['Reserved']

	@Reserved.setter
	def Reserved(self, prop:DWORD):
		self['Reserved'] = prop

	@property
	def Count(self) -> DWORD:
		return self['Count']

	@Count.setter
	def Count(self, prop:DWORD):
		self['Count'] = prop

	@property
	def pTypes(self) -> PRPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY:
		return self['pTypes']

	@pTypes.setter
	def pTypes(self, prop:PRPC_V2_NOTIFY_OPTIONS_TYPE_ARRAY):
		self['pTypes'] = prop


class RPC_V2_NOTIFY_INFO_DATA_DATA(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {0x2 : (
		'String',
		STRING_CONTAINER,

		),0x1 : (
		'dwData',
		DWORD,

		),0x4 : (
		'SystemTime',
		SYSTEMTIME_CONTAINER,

		),0x3 : (
		'DevMode',
		DEVMODE_CONTAINER,

		),0x5 : (
		'SecurityDescriptor',
		SECURITY_CONTAINER,

		)}

	@property
	def String(self) -> STRING_CONTAINER:
		return self['String']

	@String.setter
	def String(self, prop:STRING_CONTAINER):
		self['String'] = prop

	@property
	def dwData(self) -> DWORD:
		return self['dwData']

	@dwData.setter
	def dwData(self, prop:DWORD):
		self['dwData'] = prop

	@property
	def SystemTime(self) -> SYSTEMTIME_CONTAINER:
		return self['SystemTime']

	@SystemTime.setter
	def SystemTime(self, prop:SYSTEMTIME_CONTAINER):
		self['SystemTime'] = prop

	@property
	def DevMode(self) -> DEVMODE_CONTAINER:
		return self['DevMode']

	@DevMode.setter
	def DevMode(self, prop:DEVMODE_CONTAINER):
		self['DevMode'] = prop

	@property
	def SecurityDescriptor(self) -> SECURITY_CONTAINER:
		return self['SecurityDescriptor']

	@SecurityDescriptor.setter
	def SecurityDescriptor(self, prop:SECURITY_CONTAINER):
		self['SecurityDescriptor'] = prop


class RPC_V2_NOTIFY_INFO_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Type',
			UNSIGNED_SHORT,

			),
			(
			'Field',
			UNSIGNED_SHORT,

			),
			(
			'Reserved',
			DWORD,

			),
			(
			'Id',
			DWORD,

			),
			(
			'Data',
			RPC_V2_NOTIFY_INFO_DATA_DATA,

			),

		)

	@property
	def Type(self) -> UNSIGNED_SHORT:
		return self['Type']

	@Type.setter
	def Type(self, prop:UNSIGNED_SHORT):
		self['Type'] = prop

	@property
	def Field(self) -> UNSIGNED_SHORT:
		return self['Field']

	@Field.setter
	def Field(self, prop:UNSIGNED_SHORT):
		self['Field'] = prop

	@property
	def Reserved(self) -> DWORD:
		return self['Reserved']

	@Reserved.setter
	def Reserved(self, prop:DWORD):
		self['Reserved'] = prop

	@property
	def Id(self) -> DWORD:
		return self['Id']

	@Id.setter
	def Id(self, prop:DWORD):
		self['Id'] = prop

	@property
	def Data(self) -> RPC_V2_NOTIFY_INFO_DATA_DATA:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_INFO_DATA_DATA):
		self['Data'] = prop


class RPC_V2_NOTIFY_INFO_DATA_ARRAY(NDRUniConformantArray):
	item = RPC_V2_NOTIFY_INFO_DATA


class RPC_V2_NOTIFY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD,

			),
			(
			'Flags',
			DWORD,

			),
			(
			'Count',
			DWORD,

			),
			(
			'aData',
			RPC_V2_NOTIFY_INFO_DATA_ARRAY,

			),

		)

	@property
	def Version(self) -> DWORD:
		return self['Version']

	@Version.setter
	def Version(self, prop:DWORD):
		self['Version'] = prop

	@property
	def Flags(self) -> DWORD:
		return self['Flags']

	@Flags.setter
	def Flags(self, prop:DWORD):
		self['Flags'] = prop

	@property
	def Count(self) -> DWORD:
		return self['Count']

	@Count.setter
	def Count(self, prop:DWORD):
		self['Count'] = prop

	@property
	def aData(self) -> RPC_V2_NOTIFY_INFO_DATA_ARRAY:
		return self['aData']

	@aData.setter
	def aData(self, prop:RPC_V2_NOTIFY_INFO_DATA_ARRAY):
		self['aData'] = prop


class PRPC_V2_NOTIFY_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_V2_NOTIFY_INFO,

			),

		)

	@property
	def Data(self) -> RPC_V2_NOTIFY_INFO:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_INFO):
		self['Data'] = prop

class RPC_V2_UREPLY_PRINTER(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {0 : (
		'pInfo',
		PRPC_V2_NOTIFY_INFO,

		)}

	@property
	def pInfo(self) -> PRPC_V2_NOTIFY_INFO:
		return self['pInfo']

	@pInfo.setter
	def pInfo(self, prop:PRPC_V2_NOTIFY_INFO):
		self['pInfo'] = prop


class WCHAR_T_ARRAY_260(NDRUniFixedArray):
	item = WCHAR_T

	def getDataLen(self, data, offset=0):
		type_size = len(self.item())
		return 260 * type_size

	def getData(self, _):
		# This is the length of our fixed array
		containerLength = self.getDataLen(None)
		# Truncate extra data provided beyond the maximum length
		raw = self.fields['Data'][:containerLength]
		# Add padding if necessary
		paddingLength = containerLength - (len(raw) % containerLength)
		raw += b'\x00' * paddingLength
		return raw


class CORE_PRINTER_DRIVER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'CoreDriverGUID',
			GUID,

			),
			(
			'ftDriverDate',
			FILETIME,

			),
			(
			'dwlDriverVersion',
			DWORDLONG,

			),
			(
			'szPackageID',
			WCHAR_T_ARRAY_260,

			),

		)

	@property
	def CoreDriverGUID(self) -> GUID:
		return self['CoreDriverGUID']

	@CoreDriverGUID.setter
	def CoreDriverGUID(self, prop:GUID):
		self['CoreDriverGUID'] = prop

	@property
	def ftDriverDate(self) -> FILETIME:
		return self['ftDriverDate']

	@ftDriverDate.setter
	def ftDriverDate(self, prop:FILETIME):
		self['ftDriverDate'] = prop

	@property
	def dwlDriverVersion(self) -> DWORDLONG:
		return self['dwlDriverVersion']

	@dwlDriverVersion.setter
	def dwlDriverVersion(self, prop:DWORDLONG):
		self['dwlDriverVersion'] = prop

	@property
	def szPackageID(self) -> WCHAR_T_ARRAY_260:
		return self['szPackageID']

	@szPackageID.setter
	def szPackageID(self, prop:WCHAR_T_ARRAY_260):
		self['szPackageID'] = prop


class PROPERTYBLOB_ARRAY(NDRUniConformantArray):
	item = BYTE


class PPROPERTYBLOB_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			PROPERTYBLOB_ARRAY,

			),

		)

	@property
	def Data(self) -> PROPERTYBLOB_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:PROPERTYBLOB_ARRAY):
		self['Data'] = prop


class PROPERTYBLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD,

			),
			(
			'pBuf',
			PBYTE_ARRAY,

			),

		)

	@property
	def cbBuf(self) -> DWORD:
		return self['cbBuf']

	@cbBuf.setter
	def cbBuf(self, prop:DWORD):
		self['cbBuf'] = prop

	@property
	def pBuf(self) -> PBYTE_ARRAY:
		return self['pBuf']

	@pBuf.setter
	def pBuf(self, prop:PBYTE_ARRAY):
		self['pBuf'] = prop


class VALUE(NDRUNION):
	commonHdr = (
			(
			'tag',
			DWORD,

			),

		)
	union = {kRpcPropertyTypeString : (
		'propertyString',
		PWCHAR_T,

		),kRpcPropertyTypeInt32 : (
		'propertyInt32',
		LONG,

		),kRpcPropertyTypeInt64 : (
		'propertyInt64',
		LONGLONG,

		),kRpcPropertyTypeByte : (
		'propertyByte',
		BYTE,

		),kRpcPropertyTypeBuffer : (
		'propertyBlob',
		PROPERTYBLOB,

		)}

	@property
	def propertyString(self) -> PWCHAR_T:
		return self['propertyString']

	@propertyString.setter
	def propertyString(self, prop:PWCHAR_T):
		self['propertyString'] = prop

	@property
	def propertyInt32(self) -> LONG:
		return self['propertyInt32']

	@propertyInt32.setter
	def propertyInt32(self, prop:LONG):
		self['propertyInt32'] = prop

	@property
	def propertyInt64(self) -> LONGLONG:
		return self['propertyInt64']

	@propertyInt64.setter
	def propertyInt64(self, prop:LONGLONG):
		self['propertyInt64'] = prop

	@property
	def propertyByte(self) -> BYTE:
		return self['propertyByte']

	@propertyByte.setter
	def propertyByte(self, prop:BYTE):
		self['propertyByte'] = prop

	@property
	def propertyBlob(self) -> PROPERTYBLOB:
		return self['propertyBlob']

	@propertyBlob.setter
	def propertyBlob(self, prop:PROPERTYBLOB):
		self['propertyBlob'] = prop


class RPC_PRINTPROPERTYVALUE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ePropertyType',
			RPC_EPRINTPROPERTYTYPE,

			),
			(
			'value',
			VALUE,

			),

		)

	@property
	def ePropertyType(self) -> RPC_EPRINTPROPERTYTYPE:
		return self['ePropertyType']

	@ePropertyType.setter
	def ePropertyType(self, prop:RPC_EPRINTPROPERTYTYPE):
		self['ePropertyType'] = prop

	@property
	def value(self) -> VALUE:
		return self['value']

	@value.setter
	def value(self, prop:VALUE):
		self['value'] = prop


class RPC_PRINTNAMEDPROPERTY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'propertyName',
			PWCHAR_T,

			),
			(
			'propertyValue',
			RPC_PRINTPROPERTYVALUE,

			),

		)

	@property
	def propertyName(self) -> PWCHAR_T:
		return self['propertyName']

	@propertyName.setter
	def propertyName(self, prop:PWCHAR_T):
		self['propertyName'] = prop

	@property
	def propertyValue(self) -> RPC_PRINTPROPERTYVALUE:
		return self['propertyValue']

	@propertyValue.setter
	def propertyValue(self, prop:RPC_PRINTPROPERTYVALUE):
		self['propertyValue'] = prop


EBRANCHOFFICEJOBEVENTTYPE = DWORD__ENUM
kInvalidJobState = 0
kLogJobPrinted = 1
kLogJobRendered = 2
kLogJobError = 3
kLogJobPipelineError = 4
kLogOfflineFileFull = 5
class RPC_BRANCHOFFICEJOBDATAPRINTED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Status',
			DWORD,

			),
			(
			'pDocumentName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pPortName',
			PWCHAR_T,

			),
			(
			'Size',
			LONGLONG,

			),
			(
			'TotalPages',
			DWORD,

			),

		)

	@property
	def Status(self) -> DWORD:
		return self['Status']

	@Status.setter
	def Status(self, prop:DWORD):
		self['Status'] = prop

	@property
	def pDocumentName(self) -> PWCHAR_T:
		return self['pDocumentName']

	@pDocumentName.setter
	def pDocumentName(self, prop:PWCHAR_T):
		self['pDocumentName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pPortName(self) -> PWCHAR_T:
		return self['pPortName']

	@pPortName.setter
	def pPortName(self, prop:PWCHAR_T):
		self['pPortName'] = prop

	@property
	def Size(self) -> LONGLONG:
		return self['Size']

	@Size.setter
	def Size(self, prop:LONGLONG):
		self['Size'] = prop

	@property
	def TotalPages(self) -> DWORD:
		return self['TotalPages']

	@TotalPages.setter
	def TotalPages(self, prop:DWORD):
		self['TotalPages'] = prop


class RPC_BRANCHOFFICEJOBDATARENDERED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			LONGLONG,

			),
			(
			'ICMMethod',
			DWORD,

			),
			(
			'Color',
			SHORT,

			),
			(
			'PrintQuality',
			SHORT,

			),
			(
			'YResolution',
			SHORT,

			),
			(
			'Copies',
			SHORT,

			),
			(
			'TTOption',
			SHORT,

			),

		)

	@property
	def Size(self) -> LONGLONG:
		return self['Size']

	@Size.setter
	def Size(self, prop:LONGLONG):
		self['Size'] = prop

	@property
	def ICMMethod(self) -> DWORD:
		return self['ICMMethod']

	@ICMMethod.setter
	def ICMMethod(self, prop:DWORD):
		self['ICMMethod'] = prop

	@property
	def Color(self) -> SHORT:
		return self['Color']

	@Color.setter
	def Color(self, prop:SHORT):
		self['Color'] = prop

	@property
	def PrintQuality(self) -> SHORT:
		return self['PrintQuality']

	@PrintQuality.setter
	def PrintQuality(self, prop:SHORT):
		self['PrintQuality'] = prop

	@property
	def YResolution(self) -> SHORT:
		return self['YResolution']

	@YResolution.setter
	def YResolution(self, prop:SHORT):
		self['YResolution'] = prop

	@property
	def Copies(self) -> SHORT:
		return self['Copies']

	@Copies.setter
	def Copies(self, prop:SHORT):
		self['Copies'] = prop

	@property
	def TTOption(self) -> SHORT:
		return self['TTOption']

	@TTOption.setter
	def TTOption(self, prop:SHORT):
		self['TTOption'] = prop


class RPC_BRANCHOFFICEJOBDATAERROR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LastError',
			DWORD,

			),
			(
			'pDocumentName',
			PWCHAR_T,

			),
			(
			'pUserName',
			PWCHAR_T,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pDataType',
			PWCHAR_T,

			),
			(
			'TotalSize',
			LONGLONG,

			),
			(
			'PrintedSize',
			LONGLONG,

			),
			(
			'TotalPages',
			DWORD,

			),
			(
			'PrintedPages',
			DWORD,

			),
			(
			'pMachineName',
			PWCHAR_T,

			),
			(
			'pJobError',
			PWCHAR_T,

			),
			(
			'pErrorDescription',
			PWCHAR_T,

			),

		)

	@property
	def LastError(self) -> DWORD:
		return self['LastError']

	@LastError.setter
	def LastError(self, prop:DWORD):
		self['LastError'] = prop

	@property
	def pDocumentName(self) -> PWCHAR_T:
		return self['pDocumentName']

	@pDocumentName.setter
	def pDocumentName(self, prop:PWCHAR_T):
		self['pDocumentName'] = prop

	@property
	def pUserName(self) -> PWCHAR_T:
		return self['pUserName']

	@pUserName.setter
	def pUserName(self, prop:PWCHAR_T):
		self['pUserName'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pDataType(self) -> PWCHAR_T:
		return self['pDataType']

	@pDataType.setter
	def pDataType(self, prop:PWCHAR_T):
		self['pDataType'] = prop

	@property
	def TotalSize(self) -> LONGLONG:
		return self['TotalSize']

	@TotalSize.setter
	def TotalSize(self, prop:LONGLONG):
		self['TotalSize'] = prop

	@property
	def PrintedSize(self) -> LONGLONG:
		return self['PrintedSize']

	@PrintedSize.setter
	def PrintedSize(self, prop:LONGLONG):
		self['PrintedSize'] = prop

	@property
	def TotalPages(self) -> DWORD:
		return self['TotalPages']

	@TotalPages.setter
	def TotalPages(self, prop:DWORD):
		self['TotalPages'] = prop

	@property
	def PrintedPages(self) -> DWORD:
		return self['PrintedPages']

	@PrintedPages.setter
	def PrintedPages(self, prop:DWORD):
		self['PrintedPages'] = prop

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop

	@property
	def pJobError(self) -> PWCHAR_T:
		return self['pJobError']

	@pJobError.setter
	def pJobError(self, prop:PWCHAR_T):
		self['pJobError'] = prop

	@property
	def pErrorDescription(self) -> PWCHAR_T:
		return self['pErrorDescription']

	@pErrorDescription.setter
	def pErrorDescription(self, prop:PWCHAR_T):
		self['pErrorDescription'] = prop


class RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDocumentName',
			PWCHAR_T,

			),
			(
			'pPrinterName',
			PWCHAR_T,

			),
			(
			'pExtraErrorInfo',
			PWCHAR_T,

			),

		)

	@property
	def pDocumentName(self) -> PWCHAR_T:
		return self['pDocumentName']

	@pDocumentName.setter
	def pDocumentName(self, prop:PWCHAR_T):
		self['pDocumentName'] = prop

	@property
	def pPrinterName(self) -> PWCHAR_T:
		return self['pPrinterName']

	@pPrinterName.setter
	def pPrinterName(self, prop:PWCHAR_T):
		self['pPrinterName'] = prop

	@property
	def pExtraErrorInfo(self) -> PWCHAR_T:
		return self['pExtraErrorInfo']

	@pExtraErrorInfo.setter
	def pExtraErrorInfo(self, prop:PWCHAR_T):
		self['pExtraErrorInfo'] = prop


class RPC_BRANCHOFFICELOGOFFLINEFILEFULL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pMachineName',
			PWCHAR_T,

			),

		)

	@property
	def pMachineName(self) -> PWCHAR_T:
		return self['pMachineName']

	@pMachineName.setter
	def pMachineName(self, prop:PWCHAR_T):
		self['pMachineName'] = prop


class JOBINFO(NDRUNION):
	commonHdr = (
			(
			'tag',
			EBRANCHOFFICEJOBEVENTTYPE,

			),

		)
	union = {kLogJobPrinted : (
		'LogJobPrinted',
		RPC_BRANCHOFFICEJOBDATAPRINTED,

		),kLogJobRendered : (
		'LogJobRendered',
		RPC_BRANCHOFFICEJOBDATARENDERED,

		),kLogJobError : (
		'LogJobError',
		RPC_BRANCHOFFICEJOBDATAERROR,

		),kLogJobPipelineError : (
		'LogPipelineFailed',
		RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED,

		),kLogOfflineFileFull : (
		'LogOfflineFileFull',
		RPC_BRANCHOFFICELOGOFFLINEFILEFULL,

		)}

	@property
	def LogJobPrinted(self) -> RPC_BRANCHOFFICEJOBDATAPRINTED:
		return self['LogJobPrinted']

	@LogJobPrinted.setter
	def LogJobPrinted(self, prop:RPC_BRANCHOFFICEJOBDATAPRINTED):
		self['LogJobPrinted'] = prop

	@property
	def LogJobRendered(self) -> RPC_BRANCHOFFICEJOBDATARENDERED:
		return self['LogJobRendered']

	@LogJobRendered.setter
	def LogJobRendered(self, prop:RPC_BRANCHOFFICEJOBDATARENDERED):
		self['LogJobRendered'] = prop

	@property
	def LogJobError(self) -> RPC_BRANCHOFFICEJOBDATAERROR:
		return self['LogJobError']

	@LogJobError.setter
	def LogJobError(self, prop:RPC_BRANCHOFFICEJOBDATAERROR):
		self['LogJobError'] = prop

	@property
	def LogPipelineFailed(self) -> RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED:
		return self['LogPipelineFailed']

	@LogPipelineFailed.setter
	def LogPipelineFailed(self, prop:RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED):
		self['LogPipelineFailed'] = prop

	@property
	def LogOfflineFileFull(self) -> RPC_BRANCHOFFICELOGOFFLINEFILEFULL:
		return self['LogOfflineFileFull']

	@LogOfflineFileFull.setter
	def LogOfflineFileFull(self, prop:RPC_BRANCHOFFICELOGOFFLINEFILEFULL):
		self['LogOfflineFileFull'] = prop


class RPC_BRANCHOFFICEJOBDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'eEventType',
			EBRANCHOFFICEJOBEVENTTYPE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'JobInfo',
			JOBINFO,

			),

		)

	@property
	def eEventType(self) -> EBRANCHOFFICEJOBEVENTTYPE:
		return self['eEventType']

	@eEventType.setter
	def eEventType(self, prop:EBRANCHOFFICEJOBEVENTTYPE):
		self['eEventType'] = prop

	@property
	def JobId(self) -> DWORD:
		return self['JobId']

	@JobId.setter
	def JobId(self, prop:DWORD):
		self['JobId'] = prop

	@property
	def JobInfo(self) -> JOBINFO:
		return self['JobInfo']

	@JobInfo.setter
	def JobInfo(self, prop:JOBINFO):
		self['JobInfo'] = prop


class RPC_BRANCHOFFICEJOBDATA_ARRAY(NDRUniConformantArray):
	item = RPC_BRANCHOFFICEJOBDATA


class RPC_BRANCHOFFICEJOBDATACONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cJobDataEntries',
			DWORD,

			),
			(
			'JobData',
			RPC_BRANCHOFFICEJOBDATA_ARRAY,

			),

		)

	@property
	def cJobDataEntries(self) -> DWORD:
		return self['cJobDataEntries']

	@cJobDataEntries.setter
	def cJobDataEntries(self, prop:DWORD):
		self['cJobDataEntries'] = prop

	@property
	def JobData(self) -> RPC_BRANCHOFFICEJOBDATA_ARRAY:
		return self['JobData']

	@JobData.setter
	def JobData(self, prop:RPC_BRANCHOFFICEJOBDATA_ARRAY):
		self['JobData'] = prop


class PDWORD(NDRPOINTER):
	referent = (
			(
			'Data',
			DWORD,

			),

		)

	@property
	def Data(self) -> DWORD:
		return self['Data']

	@Data.setter
	def Data(self, prop:DWORD):
		self['Data'] = prop

class RpcEnumPrinters(NDRCALL):
	opnum = 0
	structure = (
			(
			'Flags',
			DWORD,

			),
			(
			'Name',
			STRING_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pPrinterEnum',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPrintersResponse(NDRCALL):
	structure = (
			(
			'pPrinterEnum',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrinters(dce, Flags: DWORD, Name: STRING_HANDLE, Level: DWORD, pPrinterEnum: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPrinters()
	request["Flags"] = Flags
	request["Name"] = Name
	request["Level"] = Level
	request["pPrinterEnum"] = pPrinterEnum
	request["cbBuf"] = cbBuf
	return dce.request(request)

class PDEVMODE_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DEVMODE_CONTAINER,

			),

		)

	@property
	def Data(self) -> DEVMODE_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:DEVMODE_CONTAINER):
		self['Data'] = prop

class RpcOpenPrinter(NDRCALL):
	opnum = 1
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE,

			),
			(
			'pDatatype',
			WSTR,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),
			(
			'AccessRequired',
			DWORD,

			),

		)


class RpcOpenPrinterResponse(NDRCALL):
	structure = (
			(
			'pHandle',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcOpenPrinter(dce, pPrinterName: STRING_HANDLE, pDatatype: WSTR, pDevModeContainer: DEVMODE_CONTAINER, AccessRequired: DWORD):
	request = RpcOpenPrinter()
	request["pPrinterName"] = pPrinterName
	request["pDatatype"] = pDatatype
	request["pDevModeContainer"] = pDevModeContainer
	request["AccessRequired"] = AccessRequired
	return dce.request(request)

class PJOB_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			JOB_CONTAINER,

			),

		)

	@property
	def Data(self) -> JOB_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:JOB_CONTAINER):
		self['Data'] = prop

class RpcSetJob(NDRCALL):
	opnum = 2
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'pJobContainer',
			JOB_CONTAINER,

			),
			(
			'Command',
			DWORD,

			),

		)


class RpcSetJobResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetJob(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD, pJobContainer: JOB_CONTAINER, Command: DWORD):
	request = RpcSetJob()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	request["pJobContainer"] = pJobContainer
	request["Command"] = Command
	return dce.request(request)

class RpcGetJob(NDRCALL):
	opnum = 3
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pJob',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetJobResponse(NDRCALL):
	structure = (
			(
			'pJob',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetJob(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD, Level: DWORD, pJob: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetJob()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	request["Level"] = Level
	request["pJob"] = pJob
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcEnumJobs(NDRCALL):
	opnum = 4
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'FirstJob',
			DWORD,

			),
			(
			'NoJobs',
			DWORD,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pJob',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumJobsResponse(NDRCALL):
	structure = (
			(
			'pJob',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumJobs(dce, hPrinter: PRINTER_HANDLE, FirstJob: DWORD, NoJobs: DWORD, Level: DWORD, pJob: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumJobs()
	request["hPrinter"] = hPrinter
	request["FirstJob"] = FirstJob
	request["NoJobs"] = NoJobs
	request["Level"] = Level
	request["pJob"] = pJob
	request["cbBuf"] = cbBuf
	return dce.request(request)

class PPRINTER_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			PRINTER_CONTAINER,

			),

		)

	@property
	def Data(self) -> PRINTER_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRINTER_CONTAINER):
		self['Data'] = prop

class PSECURITY_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SECURITY_CONTAINER,

			),

		)

	@property
	def Data(self) -> SECURITY_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:SECURITY_CONTAINER):
		self['Data'] = prop

class RpcAddPrinter(NDRCALL):
	opnum = 5
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER,

			),

		)


class RpcAddPrinterResponse(NDRCALL):
	structure = (
			(
			'pHandle',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPrinter(dce, pName: STRING_HANDLE, pPrinterContainer: PRINTER_CONTAINER, pDevModeContainer: DEVMODE_CONTAINER, pSecurityContainer: SECURITY_CONTAINER):
	request = RpcAddPrinter()
	request["pName"] = pName
	request["pPrinterContainer"] = pPrinterContainer
	request["pDevModeContainer"] = pDevModeContainer
	request["pSecurityContainer"] = pSecurityContainer
	return dce.request(request)

class RpcDeletePrinter(NDRCALL):
	opnum = 6
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcDeletePrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinter(dce, hPrinter: PRINTER_HANDLE):
	request = RpcDeletePrinter()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class RpcSetPrinter(NDRCALL):
	opnum = 7
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER,

			),
			(
			'Command',
			DWORD,

			),

		)


class RpcSetPrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetPrinter(dce, hPrinter: PRINTER_HANDLE, pPrinterContainer: PRINTER_CONTAINER, pDevModeContainer: DEVMODE_CONTAINER, pSecurityContainer: SECURITY_CONTAINER, Command: DWORD):
	request = RpcSetPrinter()
	request["hPrinter"] = hPrinter
	request["pPrinterContainer"] = pPrinterContainer
	request["pDevModeContainer"] = pDevModeContainer
	request["pSecurityContainer"] = pSecurityContainer
	request["Command"] = Command
	return dce.request(request)

class RpcGetPrinter(NDRCALL):
	opnum = 8
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pPrinter',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetPrinterResponse(NDRCALL):
	structure = (
			(
			'pPrinter',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinter(dce, hPrinter: PRINTER_HANDLE, Level: DWORD, pPrinter: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetPrinter()
	request["hPrinter"] = hPrinter
	request["Level"] = Level
	request["pPrinter"] = pPrinter
	request["cbBuf"] = cbBuf
	return dce.request(request)

class PDRIVER_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DRIVER_CONTAINER,

			),

		)

	@property
	def Data(self) -> DRIVER_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:DRIVER_CONTAINER):
		self['Data'] = prop

class RpcAddPrinterDriver(NDRCALL):
	opnum = 9
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER,

			),

		)


class RpcAddPrinterDriverResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPrinterDriver(dce, pName: STRING_HANDLE, pDriverContainer: DRIVER_CONTAINER):
	request = RpcAddPrinterDriver()
	request["pName"] = pName
	request["pDriverContainer"] = pDriverContainer
	return dce.request(request)

class RpcEnumPrinterDrivers(NDRCALL):
	opnum = 10
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pDrivers',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPrinterDriversResponse(NDRCALL):
	structure = (
			(
			'pDrivers',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrinterDrivers(dce, pName: STRING_HANDLE, pEnvironment: WSTR, Level: DWORD, pDrivers: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPrinterDrivers()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pDrivers"] = pDrivers
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcGetPrinterDriver(NDRCALL):
	opnum = 11
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pDriver',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetPrinterDriverResponse(NDRCALL):
	structure = (
			(
			'pDriver',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterDriver(dce, hPrinter: PRINTER_HANDLE, pEnvironment: WSTR, Level: DWORD, pDriver: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetPrinterDriver()
	request["hPrinter"] = hPrinter
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pDriver"] = pDriver
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcGetPrinterDriverDirectory(NDRCALL):
	opnum = 12
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pDriverDirectory',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetPrinterDriverDirectoryResponse(NDRCALL):
	structure = (
			(
			'pDriverDirectory',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterDriverDirectory(dce, pName: STRING_HANDLE, pEnvironment: WSTR, Level: DWORD, pDriverDirectory: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetPrinterDriverDirectory()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pDriverDirectory"] = pDriverDirectory
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcDeletePrinterDriver(NDRCALL):
	opnum = 13
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'pDriverName',
			WSTR,

			),

		)


class RpcDeletePrinterDriverResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterDriver(dce, pName: STRING_HANDLE, pEnvironment: WSTR, pDriverName: WSTR):
	request = RpcDeletePrinterDriver()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["pDriverName"] = pDriverName
	return dce.request(request)

class RpcAddPrintProcessor(NDRCALL):
	opnum = 14
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'pPathName',
			WSTR,

			),
			(
			'pPrintProcessorName',
			WSTR,

			),

		)


class RpcAddPrintProcessorResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPrintProcessor(dce, pName: STRING_HANDLE, pEnvironment: WSTR, pPathName: WSTR, pPrintProcessorName: WSTR):
	request = RpcAddPrintProcessor()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["pPathName"] = pPathName
	request["pPrintProcessorName"] = pPrintProcessorName
	return dce.request(request)

class RpcEnumPrintProcessors(NDRCALL):
	opnum = 15
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pPrintProcessorInfo',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPrintProcessorsResponse(NDRCALL):
	structure = (
			(
			'pPrintProcessorInfo',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrintProcessors(dce, pName: STRING_HANDLE, pEnvironment: WSTR, Level: DWORD, pPrintProcessorInfo: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPrintProcessors()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pPrintProcessorInfo"] = pPrintProcessorInfo
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcGetPrintProcessorDirectory(NDRCALL):
	opnum = 16
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pPrintProcessorDirectory',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetPrintProcessorDirectoryResponse(NDRCALL):
	structure = (
			(
			'pPrintProcessorDirectory',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrintProcessorDirectory(dce, pName: STRING_HANDLE, pEnvironment: WSTR, Level: DWORD, pPrintProcessorDirectory: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetPrintProcessorDirectory()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pPrintProcessorDirectory"] = pPrintProcessorDirectory
	request["cbBuf"] = cbBuf
	return dce.request(request)

class PDOC_INFO_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DOC_INFO_CONTAINER,

			),

		)

	@property
	def Data(self) -> DOC_INFO_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:DOC_INFO_CONTAINER):
		self['Data'] = prop

class RpcStartDocPrinter(NDRCALL):
	opnum = 17
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pDocInfoContainer',
			DOC_INFO_CONTAINER,

			),

		)


class RpcStartDocPrinterResponse(NDRCALL):
	structure = (
			(
			'pJobId',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcStartDocPrinter(dce, hPrinter: PRINTER_HANDLE, pDocInfoContainer: DOC_INFO_CONTAINER):
	request = RpcStartDocPrinter()
	request["hPrinter"] = hPrinter
	request["pDocInfoContainer"] = pDocInfoContainer
	return dce.request(request)

class RpcStartPagePrinter(NDRCALL):
	opnum = 18
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcStartPagePrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcStartPagePrinter(dce, hPrinter: PRINTER_HANDLE):
	request = RpcStartPagePrinter()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class RpcWritePrinter(NDRCALL):
	opnum = 19
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pBuf',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcWritePrinterResponse(NDRCALL):
	structure = (
			(
			'pcWritten',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcWritePrinter(dce, hPrinter: PRINTER_HANDLE, pBuf: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcWritePrinter()
	request["hPrinter"] = hPrinter
	request["pBuf"] = pBuf
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcEndPagePrinter(NDRCALL):
	opnum = 20
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcEndPagePrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEndPagePrinter(dce, hPrinter: PRINTER_HANDLE):
	request = RpcEndPagePrinter()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class RpcAbortPrinter(NDRCALL):
	opnum = 21
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcAbortPrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAbortPrinter(dce, hPrinter: PRINTER_HANDLE):
	request = RpcAbortPrinter()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class RpcReadPrinter(NDRCALL):
	opnum = 22
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcReadPrinterResponse(NDRCALL):
	structure = (
			(
			'pBuf',
			BYTE_ARRAY,

			),
			(
			'pcNoBytesRead',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcReadPrinter(dce, hPrinter: PRINTER_HANDLE, cbBuf: DWORD):
	request = RpcReadPrinter()
	request["hPrinter"] = hPrinter
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcEndDocPrinter(NDRCALL):
	opnum = 23
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcEndDocPrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEndDocPrinter(dce, hPrinter: PRINTER_HANDLE):
	request = RpcEndDocPrinter()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class RpcAddJob(NDRCALL):
	opnum = 24
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pAddJob',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcAddJobResponse(NDRCALL):
	structure = (
			(
			'pAddJob',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddJob(dce, hPrinter: PRINTER_HANDLE, Level: DWORD, pAddJob: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcAddJob()
	request["hPrinter"] = hPrinter
	request["Level"] = Level
	request["pAddJob"] = pAddJob
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcScheduleJob(NDRCALL):
	opnum = 25
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),

		)


class RpcScheduleJobResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcScheduleJob(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD):
	request = RpcScheduleJob()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	return dce.request(request)

class RpcGetPrinterData(NDRCALL):
	opnum = 26
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pValueName',
			WSTR,

			),
			(
			'nSize',
			DWORD,

			),

		)


class RpcGetPrinterDataResponse(NDRCALL):
	structure = (
			(
			'pType',
			DWORD,

			),
			(
			'pData',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterData(dce, hPrinter: PRINTER_HANDLE, pValueName: WSTR, nSize: DWORD):
	request = RpcGetPrinterData()
	request["hPrinter"] = hPrinter
	request["pValueName"] = pValueName
	request["nSize"] = nSize
	return dce.request(request)

class RpcSetPrinterData(NDRCALL):
	opnum = 27
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pValueName',
			WSTR,

			),
			(
			'Type',
			DWORD,

			),
			(
			'pData',
			BYTE_ARRAY,

			),
			(
			'cbData',
			DWORD,

			),

		)


class RpcSetPrinterDataResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetPrinterData(dce, hPrinter: PRINTER_HANDLE, pValueName: WSTR, Type: DWORD, pData: BYTE_ARRAY, cbData: DWORD):
	request = RpcSetPrinterData()
	request["hPrinter"] = hPrinter
	request["pValueName"] = pValueName
	request["Type"] = Type
	request["pData"] = pData
	request["cbData"] = cbData
	return dce.request(request)

class RpcWaitForPrinterChange(NDRCALL):
	opnum = 28
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'Flags',
			DWORD,

			),

		)


class RpcWaitForPrinterChangeResponse(NDRCALL):
	structure = (
			(
			'pFlags',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcWaitForPrinterChange(dce, hPrinter: PRINTER_HANDLE, Flags: DWORD):
	request = RpcWaitForPrinterChange()
	request["hPrinter"] = hPrinter
	request["Flags"] = Flags
	return dce.request(request)

class RpcClosePrinter(NDRCALL):
	opnum = 29
	structure = (
			(
			'phPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcClosePrinterResponse(NDRCALL):
	structure = (
			(
			'phPrinter',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcClosePrinter(dce, phPrinter: PRINTER_HANDLE):
	request = RpcClosePrinter()
	request["phPrinter"] = phPrinter
	return dce.request(request)

class PFORM_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			FORM_CONTAINER,

			),

		)

	@property
	def Data(self) -> FORM_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:FORM_CONTAINER):
		self['Data'] = prop

class RpcAddForm(NDRCALL):
	opnum = 30
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER,

			),

		)


class RpcAddFormResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddForm(dce, hPrinter: PRINTER_HANDLE, pFormInfoContainer: FORM_CONTAINER):
	request = RpcAddForm()
	request["hPrinter"] = hPrinter
	request["pFormInfoContainer"] = pFormInfoContainer
	return dce.request(request)

class RpcDeleteForm(NDRCALL):
	opnum = 31
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pFormName',
			WSTR,

			),

		)


class RpcDeleteFormResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeleteForm(dce, hPrinter: PRINTER_HANDLE, pFormName: WSTR):
	request = RpcDeleteForm()
	request["hPrinter"] = hPrinter
	request["pFormName"] = pFormName
	return dce.request(request)

class RpcGetForm(NDRCALL):
	opnum = 32
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pFormName',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pForm',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcGetFormResponse(NDRCALL):
	structure = (
			(
			'pForm',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetForm(dce, hPrinter: PRINTER_HANDLE, pFormName: WSTR, Level: DWORD, pForm: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcGetForm()
	request["hPrinter"] = hPrinter
	request["pFormName"] = pFormName
	request["Level"] = Level
	request["pForm"] = pForm
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcSetForm(NDRCALL):
	opnum = 33
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pFormName',
			WSTR,

			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER,

			),

		)


class RpcSetFormResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetForm(dce, hPrinter: PRINTER_HANDLE, pFormName: WSTR, pFormInfoContainer: FORM_CONTAINER):
	request = RpcSetForm()
	request["hPrinter"] = hPrinter
	request["pFormName"] = pFormName
	request["pFormInfoContainer"] = pFormInfoContainer
	return dce.request(request)

class RpcEnumForms(NDRCALL):
	opnum = 34
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pForm',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumFormsResponse(NDRCALL):
	structure = (
			(
			'pForm',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumForms(dce, hPrinter: PRINTER_HANDLE, Level: DWORD, pForm: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumForms()
	request["hPrinter"] = hPrinter
	request["Level"] = Level
	request["pForm"] = pForm
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcEnumPorts(NDRCALL):
	opnum = 35
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pPort',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPortsResponse(NDRCALL):
	structure = (
			(
			'pPort',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPorts(dce, pName: STRING_HANDLE, Level: DWORD, pPort: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPorts()
	request["pName"] = pName
	request["Level"] = Level
	request["pPort"] = pPort
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcEnumMonitors(NDRCALL):
	opnum = 36
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pMonitor',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumMonitorsResponse(NDRCALL):
	structure = (
			(
			'pMonitor',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumMonitors(dce, pName: STRING_HANDLE, Level: DWORD, pMonitor: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumMonitors()
	request["pName"] = pName
	request["Level"] = Level
	request["pMonitor"] = pMonitor
	request["cbBuf"] = cbBuf
	return dce.request(request)

class Opnum37NotUsedOnWire(NDRCALL):
	opnum = 37
	structure = (

		)


class Opnum37NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum37NotUsedOnWire(dce):
	request = Opnum37NotUsedOnWire()
	return dce.request(request)

class Opnum38NotUsedOnWire(NDRCALL):
	opnum = 38
	structure = (

		)


class Opnum38NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum38NotUsedOnWire(dce):
	request = Opnum38NotUsedOnWire()
	return dce.request(request)

class RpcDeletePort(NDRCALL):
	opnum = 39
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'hWnd',
			ULONG_PTR,

			),
			(
			'pPortName',
			WSTR,

			),

		)


class RpcDeletePortResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePort(dce, pName: STRING_HANDLE, hWnd: ULONG_PTR, pPortName: WSTR):
	request = RpcDeletePort()
	request["pName"] = pName
	request["hWnd"] = hWnd
	request["pPortName"] = pPortName
	return dce.request(request)

class RpcCreatePrinterIC(NDRCALL):
	opnum = 40
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),

		)


class RpcCreatePrinterICResponse(NDRCALL):
	structure = (
			(
			'pHandle',
			GDI_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcCreatePrinterIC(dce, hPrinter: PRINTER_HANDLE, pDevModeContainer: DEVMODE_CONTAINER):
	request = RpcCreatePrinterIC()
	request["hPrinter"] = hPrinter
	request["pDevModeContainer"] = pDevModeContainer
	return dce.request(request)

class RpcPlayGdiScriptOnPrinterIC(NDRCALL):
	opnum = 41
	structure = (
			(
			'hPrinterIC',
			GDI_HANDLE,

			),
			(
			'pIn',
			BYTE_ARRAY,

			),
			(
			'cIn',
			DWORD,

			),
			(
			'cOut',
			DWORD,

			),
			(
			'ul',
			DWORD,

			),

		)


class RpcPlayGdiScriptOnPrinterICResponse(NDRCALL):
	structure = (
			(
			'pOut',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcPlayGdiScriptOnPrinterIC(dce, hPrinterIC: GDI_HANDLE, pIn: BYTE_ARRAY, cIn: DWORD, cOut: DWORD, ul: DWORD):
	request = RpcPlayGdiScriptOnPrinterIC()
	request["hPrinterIC"] = hPrinterIC
	request["pIn"] = pIn
	request["cIn"] = cIn
	request["cOut"] = cOut
	request["ul"] = ul
	return dce.request(request)

class RpcDeletePrinterIC(NDRCALL):
	opnum = 42
	structure = (
			(
			'phPrinterIC',
			GDI_HANDLE,

			),

		)


class RpcDeletePrinterICResponse(NDRCALL):
	structure = (
			(
			'phPrinterIC',
			GDI_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterIC(dce, phPrinterIC: GDI_HANDLE):
	request = RpcDeletePrinterIC()
	request["phPrinterIC"] = phPrinterIC
	return dce.request(request)

class Opnum43NotUsedOnWire(NDRCALL):
	opnum = 43
	structure = (

		)


class Opnum43NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum43NotUsedOnWire(dce):
	request = Opnum43NotUsedOnWire()
	return dce.request(request)

class Opnum44NotUsedOnWire(NDRCALL):
	opnum = 44
	structure = (

		)


class Opnum44NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum44NotUsedOnWire(dce):
	request = Opnum44NotUsedOnWire()
	return dce.request(request)

class Opnum45NotUsedOnWire(NDRCALL):
	opnum = 45
	structure = (

		)


class Opnum45NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum45NotUsedOnWire(dce):
	request = Opnum45NotUsedOnWire()
	return dce.request(request)

class PMONITOR_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			MONITOR_CONTAINER,

			),

		)

	@property
	def Data(self) -> MONITOR_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:MONITOR_CONTAINER):
		self['Data'] = prop

class RpcAddMonitor(NDRCALL):
	opnum = 46
	structure = (
			(
			'Name',
			STRING_HANDLE,

			),
			(
			'pMonitorContainer',
			MONITOR_CONTAINER,

			),

		)


class RpcAddMonitorResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddMonitor(dce, Name: STRING_HANDLE, pMonitorContainer: MONITOR_CONTAINER):
	request = RpcAddMonitor()
	request["Name"] = Name
	request["pMonitorContainer"] = pMonitorContainer
	return dce.request(request)

class RpcDeleteMonitor(NDRCALL):
	opnum = 47
	structure = (
			(
			'Name',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'pMonitorName',
			WSTR,

			),

		)


class RpcDeleteMonitorResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeleteMonitor(dce, Name: STRING_HANDLE, pEnvironment: WSTR, pMonitorName: WSTR):
	request = RpcDeleteMonitor()
	request["Name"] = Name
	request["pEnvironment"] = pEnvironment
	request["pMonitorName"] = pMonitorName
	return dce.request(request)

class RpcDeletePrintProcessor(NDRCALL):
	opnum = 48
	structure = (
			(
			'Name',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'pPrintProcessorName',
			WSTR,

			),

		)


class RpcDeletePrintProcessorResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrintProcessor(dce, Name: STRING_HANDLE, pEnvironment: WSTR, pPrintProcessorName: WSTR):
	request = RpcDeletePrintProcessor()
	request["Name"] = Name
	request["pEnvironment"] = pEnvironment
	request["pPrintProcessorName"] = pPrintProcessorName
	return dce.request(request)

class Opnum49NotUsedOnWire(NDRCALL):
	opnum = 49
	structure = (

		)


class Opnum49NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum49NotUsedOnWire(dce):
	request = Opnum49NotUsedOnWire()
	return dce.request(request)

class Opnum50NotUsedOnWire(NDRCALL):
	opnum = 50
	structure = (

		)


class Opnum50NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum50NotUsedOnWire(dce):
	request = Opnum50NotUsedOnWire()
	return dce.request(request)

class RpcEnumPrintProcessorDatatypes(NDRCALL):
	opnum = 51
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pPrintProcessorName',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pDatatypes',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPrintProcessorDatatypesResponse(NDRCALL):
	structure = (
			(
			'pDatatypes',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrintProcessorDatatypes(dce, pName: STRING_HANDLE, pPrintProcessorName: WSTR, Level: DWORD, pDatatypes: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPrintProcessorDatatypes()
	request["pName"] = pName
	request["pPrintProcessorName"] = pPrintProcessorName
	request["Level"] = Level
	request["pDatatypes"] = pDatatypes
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcResetPrinter(NDRCALL):
	opnum = 52
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pDatatype',
			WSTR,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),

		)


class RpcResetPrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcResetPrinter(dce, hPrinter: PRINTER_HANDLE, pDatatype: WSTR, pDevModeContainer: DEVMODE_CONTAINER):
	request = RpcResetPrinter()
	request["hPrinter"] = hPrinter
	request["pDatatype"] = pDatatype
	request["pDevModeContainer"] = pDevModeContainer
	return dce.request(request)

class RpcGetPrinterDriver2(NDRCALL):
	opnum = 53
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'Level',
			DWORD,

			),
			(
			'pDriver',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),
			(
			'dwClientMajorVersion',
			DWORD,

			),
			(
			'dwClientMinorVersion',
			DWORD,

			),

		)


class RpcGetPrinterDriver2Response(NDRCALL):
	structure = (
			(
			'pDriver',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pdwServerMaxVersion',
			DWORD,

			),
			(
			'pdwServerMinVersion',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterDriver2(dce, hPrinter: PRINTER_HANDLE, pEnvironment: WSTR, Level: DWORD, pDriver: BYTE_ARRAY, cbBuf: DWORD, dwClientMajorVersion: DWORD, dwClientMinorVersion: DWORD):
	request = RpcGetPrinterDriver2()
	request["hPrinter"] = hPrinter
	request["pEnvironment"] = pEnvironment
	request["Level"] = Level
	request["pDriver"] = pDriver
	request["cbBuf"] = cbBuf
	request["dwClientMajorVersion"] = dwClientMajorVersion
	request["dwClientMinorVersion"] = dwClientMinorVersion
	return dce.request(request)

class Opnum54NotUsedOnWire(NDRCALL):
	opnum = 54
	structure = (

		)


class Opnum54NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum54NotUsedOnWire(dce):
	request = Opnum54NotUsedOnWire()
	return dce.request(request)

class Opnum55NotUsedOnWire(NDRCALL):
	opnum = 55
	structure = (

		)


class Opnum55NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum55NotUsedOnWire(dce):
	request = Opnum55NotUsedOnWire()
	return dce.request(request)

class RpcFindClosePrinterChangeNotification(NDRCALL):
	opnum = 56
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcFindClosePrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcFindClosePrinterChangeNotification(dce, hPrinter: PRINTER_HANDLE):
	request = RpcFindClosePrinterChangeNotification()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class Opnum57NotUsedOnWire(NDRCALL):
	opnum = 57
	structure = (

		)


class Opnum57NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum57NotUsedOnWire(dce):
	request = Opnum57NotUsedOnWire()
	return dce.request(request)

class RpcReplyOpenPrinter(NDRCALL):
	opnum = 58
	structure = (
			(
			'pMachine',
			STRING_HANDLE,

			),
			(
			'dwPrinterRemote',
			DWORD,

			),
			(
			'dwType',
			DWORD,

			),
			(
			'cbBuffer',
			DWORD,

			),
			(
			'pBuffer',
			BYTE_ARRAY,

			),

		)


class RpcReplyOpenPrinterResponse(NDRCALL):
	structure = (
			(
			'phPrinterNotify',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcReplyOpenPrinter(dce, pMachine: STRING_HANDLE, dwPrinterRemote: DWORD, dwType: DWORD, cbBuffer: DWORD, pBuffer: BYTE_ARRAY):
	request = RpcReplyOpenPrinter()
	request["pMachine"] = pMachine
	request["dwPrinterRemote"] = dwPrinterRemote
	request["dwType"] = dwType
	request["cbBuffer"] = cbBuffer
	request["pBuffer"] = pBuffer
	return dce.request(request)

class RpcRouterReplyPrinter(NDRCALL):
	opnum = 59
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE,

			),
			(
			'fdwFlags',
			DWORD,

			),
			(
			'cbBuffer',
			DWORD,

			),
			(
			'pBuffer',
			BYTE_ARRAY,

			),

		)


class RpcRouterReplyPrinterResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRouterReplyPrinter(dce, hNotify: PRINTER_HANDLE, fdwFlags: DWORD, cbBuffer: DWORD, pBuffer: BYTE_ARRAY):
	request = RpcRouterReplyPrinter()
	request["hNotify"] = hNotify
	request["fdwFlags"] = fdwFlags
	request["cbBuffer"] = cbBuffer
	request["pBuffer"] = pBuffer
	return dce.request(request)

class RpcReplyClosePrinter(NDRCALL):
	opnum = 60
	structure = (
			(
			'phNotify',
			PRINTER_HANDLE,

			),

		)


class RpcReplyClosePrinterResponse(NDRCALL):
	structure = (
			(
			'phNotify',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcReplyClosePrinter(dce, phNotify: PRINTER_HANDLE):
	request = RpcReplyClosePrinter()
	request["phNotify"] = phNotify
	return dce.request(request)

class PPORT_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_CONTAINER,

			),

		)

	@property
	def Data(self) -> PORT_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_CONTAINER):
		self['Data'] = prop

class PPORT_VAR_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			PORT_VAR_CONTAINER,

			),

		)

	@property
	def Data(self) -> PORT_VAR_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:PORT_VAR_CONTAINER):
		self['Data'] = prop

class RpcAddPortEx(NDRCALL):
	opnum = 61
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pPortContainer',
			PORT_CONTAINER,

			),
			(
			'pPortVarContainer',
			PORT_VAR_CONTAINER,

			),
			(
			'pMonitorName',
			WSTR,

			),

		)


class RpcAddPortExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPortEx(dce, pName: STRING_HANDLE, pPortContainer: PORT_CONTAINER, pPortVarContainer: PORT_VAR_CONTAINER, pMonitorName: WSTR):
	request = RpcAddPortEx()
	request["pName"] = pName
	request["pPortContainer"] = pPortContainer
	request["pPortVarContainer"] = pPortVarContainer
	request["pMonitorName"] = pMonitorName
	return dce.request(request)

class RpcRemoteFindFirstPrinterChangeNotification(NDRCALL):
	opnum = 62
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'fdwFlags',
			DWORD,

			),
			(
			'fdwOptions',
			DWORD,

			),
			(
			'pszLocalMachine',
			WSTR,

			),
			(
			'dwPrinterLocal',
			DWORD,

			),
			(
			'cbBuffer',
			DWORD,

			),
			(
			'pBuffer',
			BYTE_ARRAY,

			),

		)


class RpcRemoteFindFirstPrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'pBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRemoteFindFirstPrinterChangeNotification(dce, hPrinter: PRINTER_HANDLE, fdwFlags: DWORD, fdwOptions: DWORD, pszLocalMachine: WSTR, dwPrinterLocal: DWORD, cbBuffer: DWORD, pBuffer: BYTE_ARRAY):
	request = RpcRemoteFindFirstPrinterChangeNotification()
	request["hPrinter"] = hPrinter
	request["fdwFlags"] = fdwFlags
	request["fdwOptions"] = fdwOptions
	request["pszLocalMachine"] = pszLocalMachine
	request["dwPrinterLocal"] = dwPrinterLocal
	request["cbBuffer"] = cbBuffer
	request["pBuffer"] = pBuffer
	return dce.request(request)

class Opnum63NotUsedOnWire(NDRCALL):
	opnum = 63
	structure = (

		)


class Opnum63NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum63NotUsedOnWire(dce):
	request = Opnum63NotUsedOnWire()
	return dce.request(request)

class Opnum64NotUsedOnWire(NDRCALL):
	opnum = 64
	structure = (

		)


class Opnum64NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum64NotUsedOnWire(dce):
	request = Opnum64NotUsedOnWire()
	return dce.request(request)

class PRPC_V2_NOTIFY_OPTIONS(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_V2_NOTIFY_OPTIONS,

			),

		)

	@property
	def Data(self) -> RPC_V2_NOTIFY_OPTIONS:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_V2_NOTIFY_OPTIONS):
		self['Data'] = prop

class RpcRemoteFindFirstPrinterChangeNotificationEx(NDRCALL):
	opnum = 65
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'fdwFlags',
			DWORD,

			),
			(
			'fdwOptions',
			DWORD,

			),
			(
			'pszLocalMachine',
			WSTR,

			),
			(
			'dwPrinterLocal',
			DWORD,

			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS,

			),

		)


class RpcRemoteFindFirstPrinterChangeNotificationExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRemoteFindFirstPrinterChangeNotificationEx(dce, hPrinter: PRINTER_HANDLE, fdwFlags: DWORD, fdwOptions: DWORD, pszLocalMachine: WSTR, dwPrinterLocal: DWORD, pOptions: RPC_V2_NOTIFY_OPTIONS):
	request = RpcRemoteFindFirstPrinterChangeNotificationEx()
	request["hPrinter"] = hPrinter
	request["fdwFlags"] = fdwFlags
	request["fdwOptions"] = fdwOptions
	request["pszLocalMachine"] = pszLocalMachine
	request["dwPrinterLocal"] = dwPrinterLocal
	request["pOptions"] = pOptions
	return dce.request(request)

class RpcRouterReplyPrinterEx(NDRCALL):
	opnum = 66
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE,

			),
			(
			'dwColor',
			DWORD,

			),
			(
			'fdwFlags',
			DWORD,

			),
			(
			'dwReplyType',
			DWORD,

			),
			(
			'Reply',
			RPC_V2_UREPLY_PRINTER,

			),

		)


class RpcRouterReplyPrinterExResponse(NDRCALL):
	structure = (
			(
			'pdwResult',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRouterReplyPrinterEx(dce, hNotify: PRINTER_HANDLE, dwColor: DWORD, fdwFlags: DWORD, dwReplyType: DWORD, Reply: RPC_V2_UREPLY_PRINTER):
	request = RpcRouterReplyPrinterEx()
	request["hNotify"] = hNotify
	request["dwColor"] = dwColor
	request["fdwFlags"] = fdwFlags
	request["dwReplyType"] = dwReplyType
	request["Reply"] = Reply
	return dce.request(request)

class PPRPC_V2_NOTIFY_INFO(NDRPOINTER):
	referent = (
			(
			'Data',
			PRPC_V2_NOTIFY_INFO,

			),

		)

	@property
	def Data(self) -> PRPC_V2_NOTIFY_INFO:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRPC_V2_NOTIFY_INFO):
		self['Data'] = prop

class RpcRouterRefreshPrinterChangeNotification(NDRCALL):
	opnum = 67
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'dwColor',
			DWORD,

			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS,

			),

		)


class RpcRouterRefreshPrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'ppInfo',
			PRPC_V2_NOTIFY_INFO,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRouterRefreshPrinterChangeNotification(dce, hPrinter: PRINTER_HANDLE, dwColor: DWORD, pOptions: RPC_V2_NOTIFY_OPTIONS):
	request = RpcRouterRefreshPrinterChangeNotification()
	request["hPrinter"] = hPrinter
	request["dwColor"] = dwColor
	request["pOptions"] = pOptions
	return dce.request(request)

class Opnum68NotUsedOnWire(NDRCALL):
	opnum = 68
	structure = (

		)


class Opnum68NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum68NotUsedOnWire(dce):
	request = Opnum68NotUsedOnWire()
	return dce.request(request)

class PSPLCLIENT_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			SPLCLIENT_CONTAINER,

			),

		)

	@property
	def Data(self) -> SPLCLIENT_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:SPLCLIENT_CONTAINER):
		self['Data'] = prop

class RpcOpenPrinterEx(NDRCALL):
	opnum = 69
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE,

			),
			(
			'pDatatype',
			WSTR,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),
			(
			'AccessRequired',
			DWORD,

			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER,

			),

		)


class RpcOpenPrinterExResponse(NDRCALL):
	structure = (
			(
			'pHandle',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcOpenPrinterEx(dce, pPrinterName: STRING_HANDLE, pDatatype: WSTR, pDevModeContainer: DEVMODE_CONTAINER, AccessRequired: DWORD, pClientInfo: SPLCLIENT_CONTAINER):
	request = RpcOpenPrinterEx()
	request["pPrinterName"] = pPrinterName
	request["pDatatype"] = pDatatype
	request["pDevModeContainer"] = pDevModeContainer
	request["AccessRequired"] = AccessRequired
	request["pClientInfo"] = pClientInfo
	return dce.request(request)

class RpcAddPrinterEx(NDRCALL):
	opnum = 70
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER,

			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER,

			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER,

			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER,

			),

		)


class RpcAddPrinterExResponse(NDRCALL):
	structure = (
			(
			'pHandle',
			PRINTER_HANDLE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPrinterEx(dce, pName: STRING_HANDLE, pPrinterContainer: PRINTER_CONTAINER, pDevModeContainer: DEVMODE_CONTAINER, pSecurityContainer: SECURITY_CONTAINER, pClientInfo: SPLCLIENT_CONTAINER):
	request = RpcAddPrinterEx()
	request["pName"] = pName
	request["pPrinterContainer"] = pPrinterContainer
	request["pDevModeContainer"] = pDevModeContainer
	request["pSecurityContainer"] = pSecurityContainer
	request["pClientInfo"] = pClientInfo
	return dce.request(request)

class RpcSetPort(NDRCALL):
	opnum = 71
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pPortName',
			WSTR,

			),
			(
			'pPortContainer',
			PORT_CONTAINER,

			),

		)


class RpcSetPortResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetPort(dce, pName: STRING_HANDLE, pPortName: WSTR, pPortContainer: PORT_CONTAINER):
	request = RpcSetPort()
	request["pName"] = pName
	request["pPortName"] = pPortName
	request["pPortContainer"] = pPortContainer
	return dce.request(request)

class WSTR_ARRAY(NDRUniConformantArray):
	item = WSTR


class PWSTR_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			WSTR_ARRAY,

			),

		)

	@property
	def Data(self) -> WSTR_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:WSTR_ARRAY):
		self['Data'] = prop


class RpcEnumPrinterData(NDRCALL):
	opnum = 72
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'dwIndex',
			DWORD,

			),
			(
			'cbValueName',
			DWORD,

			),
			(
			'cbData',
			DWORD,

			),

		)


class RpcEnumPrinterDataResponse(NDRCALL):
	structure = (
			(
			'pValueName',
			WSTR_ARRAY,

			),
			(
			'pcbValueName',
			DWORD,

			),
			(
			'pType',
			DWORD,

			),
			(
			'pData',
			BYTE_ARRAY,

			),
			(
			'pcbData',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrinterData(dce, hPrinter: PRINTER_HANDLE, dwIndex: DWORD, cbValueName: DWORD, cbData: DWORD):
	request = RpcEnumPrinterData()
	request["hPrinter"] = hPrinter
	request["dwIndex"] = dwIndex
	request["cbValueName"] = cbValueName
	request["cbData"] = cbData
	return dce.request(request)

class RpcDeletePrinterData(NDRCALL):
	opnum = 73
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pValueName',
			WSTR,

			),

		)


class RpcDeletePrinterDataResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterData(dce, hPrinter: PRINTER_HANDLE, pValueName: WSTR):
	request = RpcDeletePrinterData()
	request["hPrinter"] = hPrinter
	request["pValueName"] = pValueName
	return dce.request(request)

class Opnum74NotUsedOnWire(NDRCALL):
	opnum = 74
	structure = (

		)


class Opnum74NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum74NotUsedOnWire(dce):
	request = Opnum74NotUsedOnWire()
	return dce.request(request)

class Opnum75NotUsedOnWire(NDRCALL):
	opnum = 75
	structure = (

		)


class Opnum75NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum75NotUsedOnWire(dce):
	request = Opnum75NotUsedOnWire()
	return dce.request(request)

class Opnum76NotUsedOnWire(NDRCALL):
	opnum = 76
	structure = (

		)


class Opnum76NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum76NotUsedOnWire(dce):
	request = Opnum76NotUsedOnWire()
	return dce.request(request)

class RpcSetPrinterDataEx(NDRCALL):
	opnum = 77
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),
			(
			'pValueName',
			WSTR,

			),
			(
			'Type',
			DWORD,

			),
			(
			'pData',
			BYTE_ARRAY,

			),
			(
			'cbData',
			DWORD,

			),

		)


class RpcSetPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetPrinterDataEx(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR, pValueName: WSTR, Type: DWORD, pData: BYTE_ARRAY, cbData: DWORD):
	request = RpcSetPrinterDataEx()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	request["pValueName"] = pValueName
	request["Type"] = Type
	request["pData"] = pData
	request["cbData"] = cbData
	return dce.request(request)

class RpcGetPrinterDataEx(NDRCALL):
	opnum = 78
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),
			(
			'pValueName',
			WSTR,

			),
			(
			'nSize',
			DWORD,

			),

		)


class RpcGetPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'pType',
			DWORD,

			),
			(
			'pData',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterDataEx(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR, pValueName: WSTR, nSize: DWORD):
	request = RpcGetPrinterDataEx()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	request["pValueName"] = pValueName
	request["nSize"] = nSize
	return dce.request(request)

class RpcEnumPrinterDataEx(NDRCALL):
	opnum = 79
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),
			(
			'cbEnumValues',
			DWORD,

			),

		)


class RpcEnumPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'pEnumValues',
			BYTE_ARRAY,

			),
			(
			'pcbEnumValues',
			DWORD,

			),
			(
			'pnEnumValues',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrinterDataEx(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR, cbEnumValues: DWORD):
	request = RpcEnumPrinterDataEx()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	request["cbEnumValues"] = cbEnumValues
	return dce.request(request)

class RpcEnumPrinterKey(NDRCALL):
	opnum = 80
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),
			(
			'cbSubkey',
			DWORD,

			),

		)


class RpcEnumPrinterKeyResponse(NDRCALL):
	structure = (
			(
			'pSubkey',
			WSTR_ARRAY,

			),
			(
			'pcbSubkey',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPrinterKey(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR, cbSubkey: DWORD):
	request = RpcEnumPrinterKey()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	request["cbSubkey"] = cbSubkey
	return dce.request(request)

class RpcDeletePrinterDataEx(NDRCALL):
	opnum = 81
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),
			(
			'pValueName',
			WSTR,

			),

		)


class RpcDeletePrinterDataExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterDataEx(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR, pValueName: WSTR):
	request = RpcDeletePrinterDataEx()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	request["pValueName"] = pValueName
	return dce.request(request)

class RpcDeletePrinterKey(NDRCALL):
	opnum = 82
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pKeyName',
			WSTR,

			),

		)


class RpcDeletePrinterKeyResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterKey(dce, hPrinter: PRINTER_HANDLE, pKeyName: WSTR):
	request = RpcDeletePrinterKey()
	request["hPrinter"] = hPrinter
	request["pKeyName"] = pKeyName
	return dce.request(request)

class Opnum83NotUsedOnWire(NDRCALL):
	opnum = 83
	structure = (

		)


class Opnum83NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum83NotUsedOnWire(dce):
	request = Opnum83NotUsedOnWire()
	return dce.request(request)

class RpcDeletePrinterDriverEx(NDRCALL):
	opnum = 84
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pEnvironment',
			WSTR,

			),
			(
			'pDriverName',
			WSTR,

			),
			(
			'dwDeleteFlag',
			DWORD,

			),
			(
			'dwVersionNum',
			DWORD,

			),

		)


class RpcDeletePrinterDriverExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePrinterDriverEx(dce, pName: STRING_HANDLE, pEnvironment: WSTR, pDriverName: WSTR, dwDeleteFlag: DWORD, dwVersionNum: DWORD):
	request = RpcDeletePrinterDriverEx()
	request["pName"] = pName
	request["pEnvironment"] = pEnvironment
	request["pDriverName"] = pDriverName
	request["dwDeleteFlag"] = dwDeleteFlag
	request["dwVersionNum"] = dwVersionNum
	return dce.request(request)

class RpcAddPerMachineConnection(NDRCALL):
	opnum = 85
	structure = (
			(
			'pServer',
			STRING_HANDLE,

			),
			(
			'pPrinterName',
			WSTR,

			),
			(
			'pPrintServer',
			WSTR,

			),
			(
			'pProvider',
			WSTR,

			),

		)


class RpcAddPerMachineConnectionResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPerMachineConnection(dce, pServer: STRING_HANDLE, pPrinterName: WSTR, pPrintServer: WSTR, pProvider: WSTR):
	request = RpcAddPerMachineConnection()
	request["pServer"] = pServer
	request["pPrinterName"] = pPrinterName
	request["pPrintServer"] = pPrintServer
	request["pProvider"] = pProvider
	return dce.request(request)

class RpcDeletePerMachineConnection(NDRCALL):
	opnum = 86
	structure = (
			(
			'pServer',
			STRING_HANDLE,

			),
			(
			'pPrinterName',
			WSTR,

			),

		)


class RpcDeletePerMachineConnectionResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeletePerMachineConnection(dce, pServer: STRING_HANDLE, pPrinterName: WSTR):
	request = RpcDeletePerMachineConnection()
	request["pServer"] = pServer
	request["pPrinterName"] = pPrinterName
	return dce.request(request)

class RpcEnumPerMachineConnections(NDRCALL):
	opnum = 87
	structure = (
			(
			'pServer',
			STRING_HANDLE,

			),
			(
			'pPrinterEnum',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),

		)


class RpcEnumPerMachineConnectionsResponse(NDRCALL):
	structure = (
			(
			'pPrinterEnum',
			BYTE_ARRAY,

			),
			(
			'pcbNeeded',
			DWORD,

			),
			(
			'pcReturned',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumPerMachineConnections(dce, pServer: STRING_HANDLE, pPrinterEnum: BYTE_ARRAY, cbBuf: DWORD):
	request = RpcEnumPerMachineConnections()
	request["pServer"] = pServer
	request["pPrinterEnum"] = pPrinterEnum
	request["cbBuf"] = cbBuf
	return dce.request(request)

class RpcXcvData(NDRCALL):
	opnum = 88
	structure = (
			(
			'hXcv',
			PRINTER_HANDLE,

			),
			(
			'pszDataName',
			WSTR,

			),
			(
			'pInputData',
			BYTE_ARRAY,

			),
			(
			'cbInputData',
			DWORD,

			),
			(
			'cbOutputData',
			DWORD,

			),
			(
			'pdwStatus',
			DWORD,

			),

		)


class RpcXcvDataResponse(NDRCALL):
	structure = (
			(
			'pOutputData',
			BYTE_ARRAY,

			),
			(
			'pcbOutputNeeded',
			DWORD,

			),
			(
			'pdwStatus',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcXcvData(dce, hXcv: PRINTER_HANDLE, pszDataName: WSTR, pInputData: BYTE_ARRAY, cbInputData: DWORD, cbOutputData: DWORD, pdwStatus: DWORD):
	request = RpcXcvData()
	request["hXcv"] = hXcv
	request["pszDataName"] = pszDataName
	request["pInputData"] = pInputData
	request["cbInputData"] = cbInputData
	request["cbOutputData"] = cbOutputData
	request["pdwStatus"] = pdwStatus
	return dce.request(request)

class RpcAddPrinterDriverEx(NDRCALL):
	opnum = 89
	structure = (
			(
			'pName',
			STRING_HANDLE,

			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER,

			),
			(
			'dwFileCopyFlags',
			DWORD,

			),

		)


class RpcAddPrinterDriverExResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcAddPrinterDriverEx(dce, pName: STRING_HANDLE, pDriverContainer: DRIVER_CONTAINER, dwFileCopyFlags: DWORD):
	request = RpcAddPrinterDriverEx()
	request["pName"] = pName
	request["pDriverContainer"] = pDriverContainer
	request["dwFileCopyFlags"] = dwFileCopyFlags
	return dce.request(request)

class Opnum90NotUsedOnWire(NDRCALL):
	opnum = 90
	structure = (

		)


class Opnum90NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum90NotUsedOnWire(dce):
	request = Opnum90NotUsedOnWire()
	return dce.request(request)

class Opnum91NotUsedOnWire(NDRCALL):
	opnum = 91
	structure = (

		)


class Opnum91NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum91NotUsedOnWire(dce):
	request = Opnum91NotUsedOnWire()
	return dce.request(request)

class Opnum92NotUsedOnWire(NDRCALL):
	opnum = 92
	structure = (

		)


class Opnum92NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum92NotUsedOnWire(dce):
	request = Opnum92NotUsedOnWire()
	return dce.request(request)

class Opnum93NotUsedOnWire(NDRCALL):
	opnum = 93
	structure = (

		)


class Opnum93NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum93NotUsedOnWire(dce):
	request = Opnum93NotUsedOnWire()
	return dce.request(request)

class Opnum94NotUsedOnWire(NDRCALL):
	opnum = 94
	structure = (

		)


class Opnum94NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum94NotUsedOnWire(dce):
	request = Opnum94NotUsedOnWire()
	return dce.request(request)

class Opnum95NotUsedOnWire(NDRCALL):
	opnum = 95
	structure = (

		)


class Opnum95NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum95NotUsedOnWire(dce):
	request = Opnum95NotUsedOnWire()
	return dce.request(request)

class RpcFlushPrinter(NDRCALL):
	opnum = 96
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pBuf',
			BYTE_ARRAY,

			),
			(
			'cbBuf',
			DWORD,

			),
			(
			'cSleep',
			DWORD,

			),

		)


class RpcFlushPrinterResponse(NDRCALL):
	structure = (
			(
			'pcWritten',
			DWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcFlushPrinter(dce, hPrinter: PRINTER_HANDLE, pBuf: BYTE_ARRAY, cbBuf: DWORD, cSleep: DWORD):
	request = RpcFlushPrinter()
	request["hPrinter"] = hPrinter
	request["pBuf"] = pBuf
	request["cbBuf"] = cbBuf
	request["cSleep"] = cSleep
	return dce.request(request)

class PRPC_BIDI_REQUEST_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_BIDI_REQUEST_CONTAINER,

			),

		)

	@property
	def Data(self) -> RPC_BIDI_REQUEST_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_BIDI_REQUEST_CONTAINER):
		self['Data'] = prop

class PRPC_BIDI_RESPONSE_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_BIDI_RESPONSE_CONTAINER,

			),

		)

	@property
	def Data(self) -> RPC_BIDI_RESPONSE_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_BIDI_RESPONSE_CONTAINER):
		self['Data'] = prop

class PPRPC_BIDI_RESPONSE_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			PRPC_BIDI_RESPONSE_CONTAINER,

			),

		)

	@property
	def Data(self) -> PRPC_BIDI_RESPONSE_CONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRPC_BIDI_RESPONSE_CONTAINER):
		self['Data'] = prop

class RpcSendRecvBidiData(NDRCALL):
	opnum = 97
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pAction',
			WSTR,

			),
			(
			'pReqData',
			RPC_BIDI_REQUEST_CONTAINER,

			),

		)


class RpcSendRecvBidiDataResponse(NDRCALL):
	structure = (
			(
			'ppRespData',
			PRPC_BIDI_RESPONSE_CONTAINER,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSendRecvBidiData(dce, hPrinter: PRINTER_HANDLE, pAction: WSTR, pReqData: RPC_BIDI_REQUEST_CONTAINER):
	request = RpcSendRecvBidiData()
	request["hPrinter"] = hPrinter
	request["pAction"] = pAction
	request["pReqData"] = pReqData
	return dce.request(request)

class Opnum98NotUsedOnWire(NDRCALL):
	opnum = 98
	structure = (

		)


class Opnum98NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum98NotUsedOnWire(dce):
	request = Opnum98NotUsedOnWire()
	return dce.request(request)

class Opnum99NotUsedOnWire(NDRCALL):
	opnum = 99
	structure = (

		)


class Opnum99NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum99NotUsedOnWire(dce):
	request = Opnum99NotUsedOnWire()
	return dce.request(request)

class Opnum100NotUsedOnWire(NDRCALL):
	opnum = 100
	structure = (

		)


class Opnum100NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum100NotUsedOnWire(dce):
	request = Opnum100NotUsedOnWire()
	return dce.request(request)

class Opnum101NotUsedOnWire(NDRCALL):
	opnum = 101
	structure = (

		)


class Opnum101NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum101NotUsedOnWire(dce):
	request = Opnum101NotUsedOnWire()
	return dce.request(request)

class PCORE_PRINTER_DRIVER(NDRPOINTER):
	referent = (
			(
			'Data',
			CORE_PRINTER_DRIVER,

			),

		)

	@property
	def Data(self) -> CORE_PRINTER_DRIVER:
		return self['Data']

	@Data.setter
	def Data(self, prop:CORE_PRINTER_DRIVER):
		self['Data'] = prop

class CORE_PRINTER_DRIVER_ARRAY(NDRUniConformantArray):
	item = CORE_PRINTER_DRIVER


class PCORE_PRINTER_DRIVER_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			CORE_PRINTER_DRIVER_ARRAY,

			),

		)

	@property
	def Data(self) -> CORE_PRINTER_DRIVER_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:CORE_PRINTER_DRIVER_ARRAY):
		self['Data'] = prop


class RpcGetCorePrinterDrivers(NDRCALL):
	opnum = 102
	structure = (
			(
			'pszServer',
			STRING_HANDLE,

			),
			(
			'pszEnvironment',
			WSTR,

			),
			(
			'cchCoreDrivers',
			DWORD,

			),
			(
			'pszzCoreDriverDependencies',
			WSTR_ARRAY,

			),
			(
			'cCorePrinterDrivers',
			DWORD,

			),

		)


class RpcGetCorePrinterDriversResponse(NDRCALL):
	structure = (
			(
			'pCorePrinterDrivers',
			CORE_PRINTER_DRIVER_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetCorePrinterDrivers(dce, pszServer: STRING_HANDLE, pszEnvironment: WSTR, cchCoreDrivers: DWORD, pszzCoreDriverDependencies: WSTR_ARRAY, cCorePrinterDrivers: DWORD):
	request = RpcGetCorePrinterDrivers()
	request["pszServer"] = pszServer
	request["pszEnvironment"] = pszEnvironment
	request["cchCoreDrivers"] = cchCoreDrivers
	request["pszzCoreDriverDependencies"] = pszzCoreDriverDependencies
	request["cCorePrinterDrivers"] = cCorePrinterDrivers
	return dce.request(request)

class Opnum103NotUsedOnWire(NDRCALL):
	opnum = 103
	structure = (

		)


class Opnum103NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum103NotUsedOnWire(dce):
	request = Opnum103NotUsedOnWire()
	return dce.request(request)

class RpcGetPrinterDriverPackagePath(NDRCALL):
	opnum = 104
	structure = (
			(
			'pszServer',
			STRING_HANDLE,

			),
			(
			'pszEnvironment',
			WSTR,

			),
			(
			'pszLanguage',
			WSTR,

			),
			(
			'pszPackageID',
			WSTR,

			),
			(
			'pszDriverPackageCab',
			WSTR_ARRAY,

			),
			(
			'cchDriverPackageCab',
			DWORD,

			),

		)


class RpcGetPrinterDriverPackagePathResponse(NDRCALL):
	structure = (
			(
			'pszDriverPackageCab',
			WSTR_ARRAY,

			),
			(
			'pcchRequiredSize',
			LPDWORD,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetPrinterDriverPackagePath(dce, pszServer: STRING_HANDLE, pszEnvironment: WSTR, pszLanguage: WSTR, pszPackageID: WSTR, pszDriverPackageCab: WSTR_ARRAY, cchDriverPackageCab: DWORD):
	request = RpcGetPrinterDriverPackagePath()
	request["pszServer"] = pszServer
	request["pszEnvironment"] = pszEnvironment
	request["pszLanguage"] = pszLanguage
	request["pszPackageID"] = pszPackageID
	request["pszDriverPackageCab"] = pszDriverPackageCab
	request["cchDriverPackageCab"] = cchDriverPackageCab
	return dce.request(request)

class Opnum105NotUsedOnWire(NDRCALL):
	opnum = 105
	structure = (

		)


class Opnum105NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum105NotUsedOnWire(dce):
	request = Opnum105NotUsedOnWire()
	return dce.request(request)

class Opnum106NotUsedOnWire(NDRCALL):
	opnum = 106
	structure = (

		)


class Opnum106NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum106NotUsedOnWire(dce):
	request = Opnum106NotUsedOnWire()
	return dce.request(request)

class Opnum107NotUsedOnWire(NDRCALL):
	opnum = 107
	structure = (

		)


class Opnum107NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum107NotUsedOnWire(dce):
	request = Opnum107NotUsedOnWire()
	return dce.request(request)

class Opnum108NotUsedOnWire(NDRCALL):
	opnum = 108
	structure = (

		)


class Opnum108NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum108NotUsedOnWire(dce):
	request = Opnum108NotUsedOnWire()
	return dce.request(request)

class Opnum109NotUsedOnWire(NDRCALL):
	opnum = 109
	structure = (

		)


class Opnum109NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum109NotUsedOnWire(dce):
	request = Opnum109NotUsedOnWire()
	return dce.request(request)

class PRPC_PRINTPROPERTYVALUE(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_PRINTPROPERTYVALUE,

			),

		)

	@property
	def Data(self) -> RPC_PRINTPROPERTYVALUE:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_PRINTPROPERTYVALUE):
		self['Data'] = prop

class RpcGetJobNamedPropertyValue(NDRCALL):
	opnum = 110
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'pszName',
			WSTR,

			),

		)


class RpcGetJobNamedPropertyValueResponse(NDRCALL):
	structure = (
			(
			'pValue',
			RPC_PRINTPROPERTYVALUE,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcGetJobNamedPropertyValue(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD, pszName: WSTR):
	request = RpcGetJobNamedPropertyValue()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	request["pszName"] = pszName
	return dce.request(request)

class PRPC_PRINTNAMEDPROPERTY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_PRINTNAMEDPROPERTY,

			),

		)

	@property
	def Data(self) -> RPC_PRINTNAMEDPROPERTY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_PRINTNAMEDPROPERTY):
		self['Data'] = prop

class RpcSetJobNamedProperty(NDRCALL):
	opnum = 111
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'pProperty',
			RPC_PRINTNAMEDPROPERTY,

			),

		)


class RpcSetJobNamedPropertyResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcSetJobNamedProperty(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD, pProperty: RPC_PRINTNAMEDPROPERTY):
	request = RpcSetJobNamedProperty()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	request["pProperty"] = pProperty
	return dce.request(request)

class RpcDeleteJobNamedProperty(NDRCALL):
	opnum = 112
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),
			(
			'pszName',
			WSTR,

			),

		)


class RpcDeleteJobNamedPropertyResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcDeleteJobNamedProperty(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD, pszName: WSTR):
	request = RpcDeleteJobNamedProperty()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	request["pszName"] = pszName
	return dce.request(request)

class PPRPC_PRINTNAMEDPROPERTY(NDRPOINTER):
	referent = (
			(
			'Data',
			PRPC_PRINTNAMEDPROPERTY,

			),

		)

	@property
	def Data(self) -> PRPC_PRINTNAMEDPROPERTY:
		return self['Data']

	@Data.setter
	def Data(self, prop:PRPC_PRINTNAMEDPROPERTY):
		self['Data'] = prop

class RPC_PRINTNAMEDPROPERTY_ARRAY(NDRUniConformantArray):
	item = RPC_PRINTNAMEDPROPERTY


class PRPC_PRINTNAMEDPROPERTY_ARRAY(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_PRINTNAMEDPROPERTY_ARRAY,

			),

		)

	@property
	def Data(self) -> RPC_PRINTNAMEDPROPERTY_ARRAY:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_PRINTNAMEDPROPERTY_ARRAY):
		self['Data'] = prop


class RpcEnumJobNamedProperties(NDRCALL):
	opnum = 113
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'JobId',
			DWORD,

			),

		)


class RpcEnumJobNamedPropertiesResponse(NDRCALL):
	structure = (
			(
			'pcProperties',
			DWORD,

			),
			(
			'ppProperties',
			RPC_PRINTNAMEDPROPERTY_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcEnumJobNamedProperties(dce, hPrinter: PRINTER_HANDLE, JobId: DWORD):
	request = RpcEnumJobNamedProperties()
	request["hPrinter"] = hPrinter
	request["JobId"] = JobId
	return dce.request(request)

class Opnum114NotUsedOnWire(NDRCALL):
	opnum = 114
	structure = (

		)


class Opnum114NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum114NotUsedOnWire(dce):
	request = Opnum114NotUsedOnWire()
	return dce.request(request)

class Opnum115NotUsedOnWire(NDRCALL):
	opnum = 115
	structure = (

		)


class Opnum115NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum115NotUsedOnWire(dce):
	request = Opnum115NotUsedOnWire()
	return dce.request(request)

class PRPC_BRANCHOFFICEJOBDATACONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			RPC_BRANCHOFFICEJOBDATACONTAINER,

			),

		)

	@property
	def Data(self) -> RPC_BRANCHOFFICEJOBDATACONTAINER:
		return self['Data']

	@Data.setter
	def Data(self, prop:RPC_BRANCHOFFICEJOBDATACONTAINER):
		self['Data'] = prop

class RpcLogJobInfoForBranchOffice(NDRCALL):
	opnum = 116
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'pBranchOfficeJobDataContainer',
			RPC_BRANCHOFFICEJOBDATACONTAINER,

			),

		)


class RpcLogJobInfoForBranchOfficeResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcLogJobInfoForBranchOffice(dce, hPrinter: PRINTER_HANDLE, pBranchOfficeJobDataContainer: RPC_BRANCHOFFICEJOBDATACONTAINER):
	request = RpcLogJobInfoForBranchOffice()
	request["hPrinter"] = hPrinter
	request["pBranchOfficeJobDataContainer"] = pBranchOfficeJobDataContainer
	return dce.request(request)

class RpcRegeneratePrintDeviceCapabilities(NDRCALL):
	opnum = 117
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),

		)


class RpcRegeneratePrintDeviceCapabilitiesResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcRegeneratePrintDeviceCapabilities(dce, hPrinter: PRINTER_HANDLE):
	request = RpcRegeneratePrintDeviceCapabilities()
	request["hPrinter"] = hPrinter
	return dce.request(request)

class Opnum118NotUsedOnWire(NDRCALL):
	opnum = 118
	structure = (

		)


class Opnum118NotUsedOnWireResponse(NDRCALL):
	structure = (
			(
			'ErrorCode',
			ULONG,

			),

		)


def hOpnum118NotUsedOnWire(dce):
	request = Opnum118NotUsedOnWire()
	return dce.request(request)

class PPBYTE(NDRPOINTER):
	referent = (
			(
			'Data',
			PBYTE,

			),

		)

	@property
	def Data(self) -> PBYTE:
		return self['Data']

	@Data.setter
	def Data(self, prop:PBYTE):
		self['Data'] = prop

class RpcIppCreateJobOnPrinter(NDRCALL):
	opnum = 119
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'jobId',
			DWORD,

			),
			(
			'pdlFormat',
			WSTR,

			),
			(
			'jobAttributeGroupBufferSize',
			DWORD,

			),
			(
			'jobAttributeGroupBuffer',
			BYTE_ARRAY,

			),

		)


class RpcIppCreateJobOnPrinterResponse(NDRCALL):
	structure = (
			(
			'ippResponseBufferSize',
			DWORD,

			),
			(
			'ippResponseBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcIppCreateJobOnPrinter(dce, hPrinter: PRINTER_HANDLE, jobId: DWORD, pdlFormat: WSTR, jobAttributeGroupBufferSize: DWORD, jobAttributeGroupBuffer: BYTE_ARRAY):
	request = RpcIppCreateJobOnPrinter()
	request["hPrinter"] = hPrinter
	request["jobId"] = jobId
	request["pdlFormat"] = pdlFormat
	request["jobAttributeGroupBufferSize"] = jobAttributeGroupBufferSize
	request["jobAttributeGroupBuffer"] = jobAttributeGroupBuffer
	return dce.request(request)

class PPWCHAR_T(NDRPOINTER):
	referent = (
			(
			'Data',
			PWCHAR_T,

			),

		)

	@property
	def Data(self) -> PWCHAR_T:
		return self['Data']

	@Data.setter
	def Data(self, prop:PWCHAR_T):
		self['Data'] = prop

class RpcIppGetJobAttributes(NDRCALL):
	opnum = 120
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'jobId',
			DWORD,

			),
			(
			'attributeNameCount',
			DWORD,

			),
			(
			'attributeNames',
			WCHAR_T_ARRAY,

			),

		)


class RpcIppGetJobAttributesResponse(NDRCALL):
	structure = (
			(
			'ippResponseBufferSize',
			DWORD,

			),
			(
			'ippResponseBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcIppGetJobAttributes(dce, hPrinter: PRINTER_HANDLE, jobId: DWORD, attributeNameCount: DWORD, attributeNames: WCHAR_T_ARRAY):
	request = RpcIppGetJobAttributes()
	request["hPrinter"] = hPrinter
	request["jobId"] = jobId
	request["attributeNameCount"] = attributeNameCount
	request["attributeNames"] = attributeNames
	return dce.request(request)

class RpcIppSetJobAttributes(NDRCALL):
	opnum = 121
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'jobId',
			DWORD,

			),
			(
			'jobAttributeGroupBufferSize',
			DWORD,

			),
			(
			'jobAttributeGroupBuffer',
			BYTE_ARRAY,

			),

		)


class RpcIppSetJobAttributesResponse(NDRCALL):
	structure = (
			(
			'ippResponseBufferSize',
			DWORD,

			),
			(
			'ippResponseBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcIppSetJobAttributes(dce, hPrinter: PRINTER_HANDLE, jobId: DWORD, jobAttributeGroupBufferSize: DWORD, jobAttributeGroupBuffer: BYTE_ARRAY):
	request = RpcIppSetJobAttributes()
	request["hPrinter"] = hPrinter
	request["jobId"] = jobId
	request["jobAttributeGroupBufferSize"] = jobAttributeGroupBufferSize
	request["jobAttributeGroupBuffer"] = jobAttributeGroupBuffer
	return dce.request(request)

class RpcIppGetPrinterAttributes(NDRCALL):
	opnum = 122
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'attributeNameCount',
			DWORD,

			),
			(
			'attributeNames',
			WCHAR_T_ARRAY,

			),

		)


class RpcIppGetPrinterAttributesResponse(NDRCALL):
	structure = (
			(
			'ippResponseBufferSize',
			DWORD,

			),
			(
			'ippResponseBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcIppGetPrinterAttributes(dce, hPrinter: PRINTER_HANDLE, attributeNameCount: DWORD, attributeNames: WCHAR_T_ARRAY):
	request = RpcIppGetPrinterAttributes()
	request["hPrinter"] = hPrinter
	request["attributeNameCount"] = attributeNameCount
	request["attributeNames"] = attributeNames
	return dce.request(request)

class RpcIppSetPrinterAttributes(NDRCALL):
	opnum = 123
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE,

			),
			(
			'jobAttributeGroupBufferSize',
			DWORD,

			),
			(
			'jobAttributeGroupBuffer',
			BYTE_ARRAY,

			),

		)


class RpcIppSetPrinterAttributesResponse(NDRCALL):
	structure = (
			(
			'ippResponseBufferSize',
			DWORD,

			),
			(
			'ippResponseBuffer',
			BYTE_ARRAY,

			),
			(
			'ErrorCode',
			ULONG,

			),

		)


def hRpcIppSetPrinterAttributes(dce, hPrinter: PRINTER_HANDLE, jobAttributeGroupBufferSize: DWORD, jobAttributeGroupBuffer: BYTE_ARRAY):
	request = RpcIppSetPrinterAttributes()
	request["hPrinter"] = hPrinter
	request["jobAttributeGroupBufferSize"] = jobAttributeGroupBufferSize
	request["jobAttributeGroupBuffer"] = jobAttributeGroupBuffer
	return dce.request(request)

OPNUMS = {0 : (
	RpcEnumPrinters,
	RpcEnumPrintersResponse,

	),1 : (
	RpcOpenPrinter,
	RpcOpenPrinterResponse,

	),2 : (
	RpcSetJob,
	RpcSetJobResponse,

	),3 : (
	RpcGetJob,
	RpcGetJobResponse,

	),4 : (
	RpcEnumJobs,
	RpcEnumJobsResponse,

	),5 : (
	RpcAddPrinter,
	RpcAddPrinterResponse,

	),6 : (
	RpcDeletePrinter,
	RpcDeletePrinterResponse,

	),7 : (
	RpcSetPrinter,
	RpcSetPrinterResponse,

	),8 : (
	RpcGetPrinter,
	RpcGetPrinterResponse,

	),9 : (
	RpcAddPrinterDriver,
	RpcAddPrinterDriverResponse,

	),10 : (
	RpcEnumPrinterDrivers,
	RpcEnumPrinterDriversResponse,

	),11 : (
	RpcGetPrinterDriver,
	RpcGetPrinterDriverResponse,

	),12 : (
	RpcGetPrinterDriverDirectory,
	RpcGetPrinterDriverDirectoryResponse,

	),13 : (
	RpcDeletePrinterDriver,
	RpcDeletePrinterDriverResponse,

	),14 : (
	RpcAddPrintProcessor,
	RpcAddPrintProcessorResponse,

	),15 : (
	RpcEnumPrintProcessors,
	RpcEnumPrintProcessorsResponse,

	),16 : (
	RpcGetPrintProcessorDirectory,
	RpcGetPrintProcessorDirectoryResponse,

	),17 : (
	RpcStartDocPrinter,
	RpcStartDocPrinterResponse,

	),18 : (
	RpcStartPagePrinter,
	RpcStartPagePrinterResponse,

	),19 : (
	RpcWritePrinter,
	RpcWritePrinterResponse,

	),20 : (
	RpcEndPagePrinter,
	RpcEndPagePrinterResponse,

	),21 : (
	RpcAbortPrinter,
	RpcAbortPrinterResponse,

	),22 : (
	RpcReadPrinter,
	RpcReadPrinterResponse,

	),23 : (
	RpcEndDocPrinter,
	RpcEndDocPrinterResponse,

	),24 : (
	RpcAddJob,
	RpcAddJobResponse,

	),25 : (
	RpcScheduleJob,
	RpcScheduleJobResponse,

	),26 : (
	RpcGetPrinterData,
	RpcGetPrinterDataResponse,

	),27 : (
	RpcSetPrinterData,
	RpcSetPrinterDataResponse,

	),28 : (
	RpcWaitForPrinterChange,
	RpcWaitForPrinterChangeResponse,

	),29 : (
	RpcClosePrinter,
	RpcClosePrinterResponse,

	),30 : (
	RpcAddForm,
	RpcAddFormResponse,

	),31 : (
	RpcDeleteForm,
	RpcDeleteFormResponse,

	),32 : (
	RpcGetForm,
	RpcGetFormResponse,

	),33 : (
	RpcSetForm,
	RpcSetFormResponse,

	),34 : (
	RpcEnumForms,
	RpcEnumFormsResponse,

	),35 : (
	RpcEnumPorts,
	RpcEnumPortsResponse,

	),36 : (
	RpcEnumMonitors,
	RpcEnumMonitorsResponse,

	),37 : (
	Opnum37NotUsedOnWire,
	Opnum37NotUsedOnWireResponse,

	),38 : (
	Opnum38NotUsedOnWire,
	Opnum38NotUsedOnWireResponse,

	),39 : (
	RpcDeletePort,
	RpcDeletePortResponse,

	),40 : (
	RpcCreatePrinterIC,
	RpcCreatePrinterICResponse,

	),41 : (
	RpcPlayGdiScriptOnPrinterIC,
	RpcPlayGdiScriptOnPrinterICResponse,

	),42 : (
	RpcDeletePrinterIC,
	RpcDeletePrinterICResponse,

	),43 : (
	Opnum43NotUsedOnWire,
	Opnum43NotUsedOnWireResponse,

	),44 : (
	Opnum44NotUsedOnWire,
	Opnum44NotUsedOnWireResponse,

	),45 : (
	Opnum45NotUsedOnWire,
	Opnum45NotUsedOnWireResponse,

	),46 : (
	RpcAddMonitor,
	RpcAddMonitorResponse,

	),47 : (
	RpcDeleteMonitor,
	RpcDeleteMonitorResponse,

	),48 : (
	RpcDeletePrintProcessor,
	RpcDeletePrintProcessorResponse,

	),49 : (
	Opnum49NotUsedOnWire,
	Opnum49NotUsedOnWireResponse,

	),50 : (
	Opnum50NotUsedOnWire,
	Opnum50NotUsedOnWireResponse,

	),51 : (
	RpcEnumPrintProcessorDatatypes,
	RpcEnumPrintProcessorDatatypesResponse,

	),52 : (
	RpcResetPrinter,
	RpcResetPrinterResponse,

	),53 : (
	RpcGetPrinterDriver2,
	RpcGetPrinterDriver2Response,

	),54 : (
	Opnum54NotUsedOnWire,
	Opnum54NotUsedOnWireResponse,

	),55 : (
	Opnum55NotUsedOnWire,
	Opnum55NotUsedOnWireResponse,

	),56 : (
	RpcFindClosePrinterChangeNotification,
	RpcFindClosePrinterChangeNotificationResponse,

	),57 : (
	Opnum57NotUsedOnWire,
	Opnum57NotUsedOnWireResponse,

	),58 : (
	RpcReplyOpenPrinter,
	RpcReplyOpenPrinterResponse,

	),59 : (
	RpcRouterReplyPrinter,
	RpcRouterReplyPrinterResponse,

	),60 : (
	RpcReplyClosePrinter,
	RpcReplyClosePrinterResponse,

	),61 : (
	RpcAddPortEx,
	RpcAddPortExResponse,

	),62 : (
	RpcRemoteFindFirstPrinterChangeNotification,
	RpcRemoteFindFirstPrinterChangeNotificationResponse,

	),63 : (
	Opnum63NotUsedOnWire,
	Opnum63NotUsedOnWireResponse,

	),64 : (
	Opnum64NotUsedOnWire,
	Opnum64NotUsedOnWireResponse,

	),65 : (
	RpcRemoteFindFirstPrinterChangeNotificationEx,
	RpcRemoteFindFirstPrinterChangeNotificationExResponse,

	),66 : (
	RpcRouterReplyPrinterEx,
	RpcRouterReplyPrinterExResponse,

	),67 : (
	RpcRouterRefreshPrinterChangeNotification,
	RpcRouterRefreshPrinterChangeNotificationResponse,

	),68 : (
	Opnum68NotUsedOnWire,
	Opnum68NotUsedOnWireResponse,

	),69 : (
	RpcOpenPrinterEx,
	RpcOpenPrinterExResponse,

	),70 : (
	RpcAddPrinterEx,
	RpcAddPrinterExResponse,

	),71 : (
	RpcSetPort,
	RpcSetPortResponse,

	),72 : (
	RpcEnumPrinterData,
	RpcEnumPrinterDataResponse,

	),73 : (
	RpcDeletePrinterData,
	RpcDeletePrinterDataResponse,

	),74 : (
	Opnum74NotUsedOnWire,
	Opnum74NotUsedOnWireResponse,

	),75 : (
	Opnum75NotUsedOnWire,
	Opnum75NotUsedOnWireResponse,

	),76 : (
	Opnum76NotUsedOnWire,
	Opnum76NotUsedOnWireResponse,

	),77 : (
	RpcSetPrinterDataEx,
	RpcSetPrinterDataExResponse,

	),78 : (
	RpcGetPrinterDataEx,
	RpcGetPrinterDataExResponse,

	),79 : (
	RpcEnumPrinterDataEx,
	RpcEnumPrinterDataExResponse,

	),80 : (
	RpcEnumPrinterKey,
	RpcEnumPrinterKeyResponse,

	),81 : (
	RpcDeletePrinterDataEx,
	RpcDeletePrinterDataExResponse,

	),82 : (
	RpcDeletePrinterKey,
	RpcDeletePrinterKeyResponse,

	),83 : (
	Opnum83NotUsedOnWire,
	Opnum83NotUsedOnWireResponse,

	),84 : (
	RpcDeletePrinterDriverEx,
	RpcDeletePrinterDriverExResponse,

	),85 : (
	RpcAddPerMachineConnection,
	RpcAddPerMachineConnectionResponse,

	),86 : (
	RpcDeletePerMachineConnection,
	RpcDeletePerMachineConnectionResponse,

	),87 : (
	RpcEnumPerMachineConnections,
	RpcEnumPerMachineConnectionsResponse,

	),88 : (
	RpcXcvData,
	RpcXcvDataResponse,

	),89 : (
	RpcAddPrinterDriverEx,
	RpcAddPrinterDriverExResponse,

	),90 : (
	Opnum90NotUsedOnWire,
	Opnum90NotUsedOnWireResponse,

	),91 : (
	Opnum91NotUsedOnWire,
	Opnum91NotUsedOnWireResponse,

	),92 : (
	Opnum92NotUsedOnWire,
	Opnum92NotUsedOnWireResponse,

	),93 : (
	Opnum93NotUsedOnWire,
	Opnum93NotUsedOnWireResponse,

	),94 : (
	Opnum94NotUsedOnWire,
	Opnum94NotUsedOnWireResponse,

	),95 : (
	Opnum95NotUsedOnWire,
	Opnum95NotUsedOnWireResponse,

	),96 : (
	RpcFlushPrinter,
	RpcFlushPrinterResponse,

	),97 : (
	RpcSendRecvBidiData,
	RpcSendRecvBidiDataResponse,

	),98 : (
	Opnum98NotUsedOnWire,
	Opnum98NotUsedOnWireResponse,

	),99 : (
	Opnum99NotUsedOnWire,
	Opnum99NotUsedOnWireResponse,

	),100 : (
	Opnum100NotUsedOnWire,
	Opnum100NotUsedOnWireResponse,

	),101 : (
	Opnum101NotUsedOnWire,
	Opnum101NotUsedOnWireResponse,

	),102 : (
	RpcGetCorePrinterDrivers,
	RpcGetCorePrinterDriversResponse,

	),103 : (
	Opnum103NotUsedOnWire,
	Opnum103NotUsedOnWireResponse,

	),104 : (
	RpcGetPrinterDriverPackagePath,
	RpcGetPrinterDriverPackagePathResponse,

	),105 : (
	Opnum105NotUsedOnWire,
	Opnum105NotUsedOnWireResponse,

	),106 : (
	Opnum106NotUsedOnWire,
	Opnum106NotUsedOnWireResponse,

	),107 : (
	Opnum107NotUsedOnWire,
	Opnum107NotUsedOnWireResponse,

	),108 : (
	Opnum108NotUsedOnWire,
	Opnum108NotUsedOnWireResponse,

	),109 : (
	Opnum109NotUsedOnWire,
	Opnum109NotUsedOnWireResponse,

	),110 : (
	RpcGetJobNamedPropertyValue,
	RpcGetJobNamedPropertyValueResponse,

	),111 : (
	RpcSetJobNamedProperty,
	RpcSetJobNamedPropertyResponse,

	),112 : (
	RpcDeleteJobNamedProperty,
	RpcDeleteJobNamedPropertyResponse,

	),113 : (
	RpcEnumJobNamedProperties,
	RpcEnumJobNamedPropertiesResponse,

	),114 : (
	Opnum114NotUsedOnWire,
	Opnum114NotUsedOnWireResponse,

	),115 : (
	Opnum115NotUsedOnWire,
	Opnum115NotUsedOnWireResponse,

	),116 : (
	RpcLogJobInfoForBranchOffice,
	RpcLogJobInfoForBranchOfficeResponse,

	),117 : (
	RpcRegeneratePrintDeviceCapabilities,
	RpcRegeneratePrintDeviceCapabilitiesResponse,

	),118 : (
	Opnum118NotUsedOnWire,
	Opnum118NotUsedOnWireResponse,

	),119 : (
	RpcIppCreateJobOnPrinter,
	RpcIppCreateJobOnPrinterResponse,

	),120 : (
	RpcIppGetJobAttributes,
	RpcIppGetJobAttributesResponse,

	),121 : (
	RpcIppSetJobAttributes,
	RpcIppSetJobAttributesResponse,

	),122 : (
	RpcIppGetPrinterAttributes,
	RpcIppGetPrinterAttributesResponse,

	),123 : (
	RpcIppSetPrinterAttributes,
	RpcIppSetPrinterAttributesResponse,

	)}
