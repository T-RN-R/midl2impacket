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
#TYPEDEFS
#################################################################################
#################################################################################
#INTERFACE DEFINITION
#################################################################################
#################################################################################
#winspool Definition
#################################################################################
MSRPC_UUID_WINSPOOL = uuidtup_to_bin(('12345678-1234-ABCD-EF00-0123456789AB','0.0'))
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
RPC_EPrintPropertyType = DWORD__ENUM
kRpcPropertyTypeString = 1
kRpcPropertyTypeInt32 = 1
kRpcPropertyTypeInt64 = 1
kRpcPropertyTypeByte = 1
LANGID = UNSIGNED_SHORT
GDI_HANDLE = VOID
PRINTER_HANDLE = VOID
STRING_HANDLE = WCHAR_T
class SIZE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cx',
			LONG
			),
			(
			'cy',
			LONG
			)
		)


class RECTL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'left',
			LONG
			),
			(
			'top',
			LONG
			),
			(
			'right',
			LONG
			),
			(
			'bottom',
			LONG
			)
		)


class DEVMODE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dmDeviceName',
			WCHAR_T
			),
			(
			'dmSpecVersion',
			UNSIGNED_SHORT
			),
			(
			'dmDriverVersion',
			UNSIGNED_SHORT
			),
			(
			'dmSize',
			UNSIGNED_SHORT
			),
			(
			'dmDriverExtra',
			UNSIGNED_SHORT
			),
			(
			'dmFields',
			DWORD
			),
			(
			'dmOrientation',
			SHORT
			),
			(
			'dmPaperSize',
			SHORT
			),
			(
			'dmPaperLength',
			SHORT
			),
			(
			'dmPaperWidth',
			SHORT
			),
			(
			'dmScale',
			SHORT
			),
			(
			'dmCopies',
			SHORT
			),
			(
			'dmDefaultSource',
			SHORT
			),
			(
			'dmPrintQuality',
			SHORT
			),
			(
			'dmColor',
			SHORT
			),
			(
			'dmDuplex',
			SHORT
			),
			(
			'dmYResolution',
			SHORT
			),
			(
			'dmTTOption',
			SHORT
			),
			(
			'dmCollate',
			SHORT
			),
			(
			'dmFormName',
			WCHAR_T
			),
			(
			'reserved0',
			UNSIGNED_SHORT
			),
			(
			'reserved1',
			DWORD
			),
			(
			'reserved2',
			DWORD
			),
			(
			'reserved3',
			DWORD
			),
			(
			'dmNup',
			DWORD
			),
			(
			'reserved4',
			DWORD
			),
			(
			'dmICMMethod',
			DWORD
			),
			(
			'dmICMIntent',
			DWORD
			),
			(
			'dmMediaType',
			DWORD
			),
			(
			'dmDitherType',
			DWORD
			),
			(
			'reserved5',
			DWORD
			),
			(
			'reserved6',
			DWORD
			),
			(
			'reserved7',
			DWORD
			),
			(
			'reserved8',
			DWORD
			)
		)


class DOC_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDocName',
			WCHAR_T
			),
			(
			'pOutputFile',
			WCHAR_T
			),
			(
			'pDatatype',
			WCHAR_T
			)
		)


class DRIVER_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			WCHAR_T
			)
		)


class DRIVER_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverPath',
			WCHAR_T
			),
			(
			'pDataFile',
			WCHAR_T
			),
			(
			'pConfigFile',
			WCHAR_T
			)
		)


class DATA_RPC_DRIVER_INFO_3(NDRUniConformantArray):
	item = WCHAR_T


class PTR_RPC_DRIVER_INFO_3(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_DRIVER_INFO_3
			)
		)


class RPC_DRIVER_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverPath',
			WCHAR_T
			),
			(
			'pDataFile',
			WCHAR_T
			),
			(
			'pConfigFile',
			WCHAR_T
			),
			(
			'pHelpFile',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			),
			(
			'pDefaultDataType',
			WCHAR_T
			),
			(
			'cchDependentFiles',
			DWORD
			),
			(
			'pDependentFiles',
			PTR_RPC_DRIVER_INFO_3
			)
		)


class DATA_RPC_DRIVER_INFO_4(NDRUniConformantArray):
	item = WCHAR_T


class PTR_RPC_DRIVER_INFO_4(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_DRIVER_INFO_4
			)
		)


class RPC_DRIVER_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverPath',
			WCHAR_T
			),
			(
			'pDataFile',
			WCHAR_T
			),
			(
			'pConfigFile',
			WCHAR_T
			),
			(
			'pHelpFile',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			),
			(
			'pDefaultDataType',
			WCHAR_T
			),
			(
			'cchDependentFiles',
			DWORD
			),
			(
			'pDependentFiles',
			WCHAR_T
			),
			(
			'cchPreviousNames',
			DWORD
			),
			(
			'pszzPreviousNames',
			PTR_RPC_DRIVER_INFO_4
			)
		)


class DATA_RPC_DRIVER_INFO_6(NDRUniConformantArray):
	item = WCHAR_T


class PTR_RPC_DRIVER_INFO_6(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_DRIVER_INFO_6
			)
		)


class RPC_DRIVER_INFO_6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverPath',
			WCHAR_T
			),
			(
			'pDataFile',
			WCHAR_T
			),
			(
			'pConfigFile',
			WCHAR_T
			),
			(
			'pHelpFile',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			),
			(
			'pDefaultDataType',
			WCHAR_T
			),
			(
			'cchDependentFiles',
			DWORD
			),
			(
			'pDependentFiles',
			WCHAR_T
			),
			(
			'cchPreviousNames',
			DWORD
			),
			(
			'pszzPreviousNames',
			PTR_RPC_DRIVER_INFO_6
			),
			(
			'ftDriverDate',
			FILETIME
			),
			(
			'dwlDriverVersion',
			DWORDLONG
			),
			(
			'pMfgName',
			WCHAR_T
			),
			(
			'pOEMUrl',
			WCHAR_T
			),
			(
			'pHardwareID',
			WCHAR_T
			),
			(
			'pProvider',
			WCHAR_T
			)
		)


class DATA_RPC_DRIVER_INFO_8(NDRUniConformantArray):
	item = WCHAR_T


class PTR_RPC_DRIVER_INFO_8(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_DRIVER_INFO_8
			)
		)


class RPC_DRIVER_INFO_8(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cVersion',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverPath',
			WCHAR_T
			),
			(
			'pDataFile',
			WCHAR_T
			),
			(
			'pConfigFile',
			WCHAR_T
			),
			(
			'pHelpFile',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			),
			(
			'pDefaultDataType',
			WCHAR_T
			),
			(
			'cchDependentFiles',
			DWORD
			),
			(
			'pDependentFiles',
			WCHAR_T
			),
			(
			'cchPreviousNames',
			DWORD
			),
			(
			'pszzPreviousNames',
			WCHAR_T
			),
			(
			'ftDriverDate',
			FILETIME
			),
			(
			'dwlDriverVersion',
			DWORDLONG
			),
			(
			'pMfgName',
			WCHAR_T
			),
			(
			'pOEMUrl',
			WCHAR_T
			),
			(
			'pHardwareID',
			WCHAR_T
			),
			(
			'pProvider',
			WCHAR_T
			),
			(
			'pPrintProcessor',
			WCHAR_T
			),
			(
			'pVendorSetup',
			WCHAR_T
			),
			(
			'cchColorProfiles',
			DWORD
			),
			(
			'pszzColorProfiles',
			WCHAR_T
			),
			(
			'pInfPath',
			WCHAR_T
			),
			(
			'dwPrinterDriverAttributes',
			DWORD
			),
			(
			'cchCoreDependencies',
			DWORD
			),
			(
			'pszzCoreDriverDependencies',
			PTR_RPC_DRIVER_INFO_8
			),
			(
			'ftMinInboxDriverVerDate',
			FILETIME
			),
			(
			'dwlMinInboxDriverVerVersion',
			DWORDLONG
			)
		)


class FORM_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'Size',
			SIZE
			),
			(
			'ImageableArea',
			RECTL
			)
		)


class RPC_FORM_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'pName',
			CONST_WCHAR_T
			),
			(
			'Size',
			SIZE
			),
			(
			'ImageableArea',
			RECTL
			),
			(
			'pKeyword',
			CONST_CHAR
			),
			(
			'StringType',
			DWORD
			),
			(
			'pMuiDll',
			CONST_WCHAR_T
			),
			(
			'dwResourceId',
			DWORD
			),
			(
			'pDisplayName',
			CONST_WCHAR_T
			),
			(
			'wLangID',
			LANGID
			)
		)


class JOB_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'pDocument',
			WCHAR_T
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pStatus',
			WCHAR_T
			),
			(
			'Status',
			DWORD
			),
			(
			'Priority',
			DWORD
			),
			(
			'Position',
			DWORD
			),
			(
			'TotalPages',
			DWORD
			),
			(
			'PagesPrinted',
			DWORD
			),
			(
			'Submitted',
			SYSTEMTIME
			)
		)


class JOB_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'pDocument',
			WCHAR_T
			),
			(
			'pNotifyName',
			WCHAR_T
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pPrintProcessor',
			WCHAR_T
			),
			(
			'pParameters',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			),
			(
			'pDevMode',
			ULONG_PTR
			),
			(
			'pStatus',
			WCHAR_T
			),
			(
			'pSecurityDescriptor',
			ULONG_PTR
			),
			(
			'Status',
			DWORD
			),
			(
			'Priority',
			DWORD
			),
			(
			'Position',
			DWORD
			),
			(
			'StartTime',
			DWORD
			),
			(
			'UntilTime',
			DWORD
			),
			(
			'TotalPages',
			DWORD
			),
			(
			'Size',
			DWORD
			),
			(
			'Submitted',
			SYSTEMTIME
			),
			(
			'Time',
			DWORD
			),
			(
			'PagesPrinted',
			DWORD
			)
		)


class JOB_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD
			),
			(
			'NextJobId',
			DWORD
			),
			(
			'Reserved',
			DWORD
			)
		)


class JOB_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'JobId',
			DWORD
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'pDocument',
			WCHAR_T
			),
			(
			'pNotifyName',
			WCHAR_T
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pPrintProcessor',
			WCHAR_T
			),
			(
			'pParameters',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			),
			(
			'pDevMode',
			ULONG_PTR
			),
			(
			'pStatus',
			WCHAR_T
			),
			(
			'pSecurityDescriptor',
			ULONG_PTR
			),
			(
			'Status',
			DWORD
			),
			(
			'Priority',
			DWORD
			),
			(
			'Position',
			DWORD
			),
			(
			'StartTime',
			DWORD
			),
			(
			'UntilTime',
			DWORD
			),
			(
			'TotalPages',
			DWORD
			),
			(
			'Size',
			DWORD
			),
			(
			'Submitted',
			SYSTEMTIME
			),
			(
			'Time',
			DWORD
			),
			(
			'PagesPrinted',
			DWORD
			),
			(
			'SizeHigh',
			LONG
			)
		)


class MONITOR_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			WCHAR_T
			)
		)


class MONITOR_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pName',
			WCHAR_T
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDLLName',
			WCHAR_T
			)
		)


class PORT_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			WCHAR_T
			)
		)


class PORT_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			),
			(
			'pDescription',
			WCHAR_T
			),
			(
			'fPortType',
			DWORD
			),
			(
			'Reserved',
			DWORD
			)
		)


class PORT_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwStatus',
			DWORD
			),
			(
			'pszStatus',
			WCHAR_T
			),
			(
			'dwSeverity',
			DWORD
			)
		)


class PORT_INFO_FF(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPortName',
			WCHAR_T
			),
			(
			'cbMonitorData',
			DWORD
			),
			(
			'pMonitorData',
			BYTE
			)
		)


class PRINTER_INFO_STRESS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pServerName',
			WCHAR_T
			),
			(
			'cJobs',
			DWORD
			),
			(
			'cTotalJobs',
			DWORD
			),
			(
			'cTotalBytes',
			DWORD
			),
			(
			'stUpTime',
			SYSTEMTIME
			),
			(
			'MaxcRef',
			DWORD
			),
			(
			'cTotalPagesPrinted',
			DWORD
			),
			(
			'dwGetVersion',
			DWORD
			),
			(
			'fFreeBuild',
			DWORD
			),
			(
			'cSpooling',
			DWORD
			),
			(
			'cMaxSpooling',
			DWORD
			),
			(
			'cRef',
			DWORD
			),
			(
			'cErrorOutOfPaper',
			DWORD
			),
			(
			'cErrorNotReady',
			DWORD
			),
			(
			'cJobError',
			DWORD
			),
			(
			'dwNumberOfProcessors',
			DWORD
			),
			(
			'dwProcessorType',
			DWORD
			),
			(
			'dwHighPartTotalBytes',
			DWORD
			),
			(
			'cChangeID',
			DWORD
			),
			(
			'dwLastError',
			DWORD
			),
			(
			'Status',
			DWORD
			),
			(
			'cEnumerateNetworkPrinters',
			DWORD
			),
			(
			'cAddNetPrinters',
			DWORD
			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT
			),
			(
			'wProcessorLevel',
			UNSIGNED_SHORT
			),
			(
			'cRefIC',
			DWORD
			),
			(
			'dwReserved2',
			DWORD
			),
			(
			'dwReserved3',
			DWORD
			)
		)


class PRINTER_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'pDescription',
			WCHAR_T
			),
			(
			'pName',
			WCHAR_T
			),
			(
			'pComment',
			WCHAR_T
			)
		)


class PRINTER_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pServerName',
			WCHAR_T
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pShareName',
			WCHAR_T
			),
			(
			'pPortName',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			),
			(
			'pComment',
			WCHAR_T
			),
			(
			'pLocation',
			WCHAR_T
			),
			(
			'pDevMode',
			ULONG_PTR
			),
			(
			'pSepFile',
			WCHAR_T
			),
			(
			'pPrintProcessor',
			WCHAR_T
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pParameters',
			WCHAR_T
			),
			(
			'pSecurityDescriptor',
			ULONG_PTR
			),
			(
			'Attributes',
			DWORD
			),
			(
			'Priority',
			DWORD
			),
			(
			'DefaultPriority',
			DWORD
			),
			(
			'StartTime',
			DWORD
			),
			(
			'UntilTime',
			DWORD
			),
			(
			'Status',
			DWORD
			),
			(
			'cJobs',
			DWORD
			),
			(
			'AveragePPM',
			DWORD
			)
		)


class PRINTER_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pSecurityDescriptor',
			ULONG_PTR
			)
		)


class PRINTER_INFO_4(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pServerName',
			WCHAR_T
			),
			(
			'Attributes',
			DWORD
			)
		)


class PRINTER_INFO_5(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pPortName',
			WCHAR_T
			),
			(
			'Attributes',
			DWORD
			),
			(
			'DeviceNotSelectedTimeout',
			DWORD
			),
			(
			'TransmissionRetryTimeout',
			DWORD
			)
		)


class PRINTER_INFO_6(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwStatus',
			DWORD
			)
		)


class PRINTER_INFO_7(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pszObjectGUID',
			WCHAR_T
			),
			(
			'dwAction',
			DWORD
			)
		)


class PRINTER_INFO_8(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDevMode',
			ULONG_PTR
			)
		)


class PRINTER_INFO_9(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDevMode',
			ULONG_PTR
			)
		)


class SPLCLIENT_INFO_1(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwSize',
			DWORD
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'dwBuildNum',
			DWORD
			),
			(
			'dwMajorVersion',
			DWORD
			),
			(
			'dwMinorVersion',
			DWORD
			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT
			)
		)


class SPLCLIENT_INFO_2(NDRSTRUCT):
	align = 1
	structure = (
			(
			'notUsed',
			LONG_PTR
			)
		)


class SPLCLIENT_INFO_3(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbSize',
			UNSIGNED_INT
			),
			(
			'dwFlags',
			DWORD
			),
			(
			'dwSize',
			DWORD
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'dwBuildNum',
			DWORD
			),
			(
			'dwMajorVersion',
			DWORD
			),
			(
			'dwMinorVersion',
			DWORD
			),
			(
			'wProcessorArchitecture',
			UNSIGNED_SHORT
			),
			(
			'hSplPrinter',
			UNSIGNED___INT64
			)
		)


class DATA_DEVMODE_CONTAINER(NDRUniConformantArray):
	item = BYTE


class PTR_DEVMODE_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_DEVMODE_CONTAINER
			)
		)


class DEVMODE_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pDevMode',
			PTR_DEVMODE_CONTAINER
			)
		)


class DOCINFO(NDRUNION):
	union = {1 : (
		'pDocInfo1',
		DOC_INFO_1
		)}


class DOC_INFO_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'DocInfo',
			DOCINFO
			)
		)


class DRIVERINFO(NDRUNION):
	union = {1 : (
		'pNotUsed',
		DRIVER_INFO_1
		),2 : (
		'Level2',
		DRIVER_INFO_2
		),3 : (
		'Level3',
		RPC_DRIVER_INFO_3
		),4 : (
		'Level4',
		RPC_DRIVER_INFO_4
		),6 : (
		'Level6',
		RPC_DRIVER_INFO_6
		),8 : (
		'Level8',
		RPC_DRIVER_INFO_8
		)}


class DRIVER_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'DriverInfo',
			DRIVERINFO
			)
		)


class FORMINFO(NDRUNION):
	union = {1 : (
		'pFormInfo1',
		FORM_INFO_1
		),2 : (
		'pFormInfo2',
		RPC_FORM_INFO_2
		)}


class FORM_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'FormInfo',
			FORMINFO
			)
		)


class JOBINFO(NDRUNION):
	union = {1 : (
		'Level1',
		JOB_INFO_1
		),2 : (
		'Level2',
		JOB_INFO_2
		),3 : (
		'Level3',
		JOB_INFO_3
		),4 : (
		'Level4',
		JOB_INFO_4
		)}


class JOB_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'JobInfo',
			JOBINFO
			)
		)


class MONITORINFO(NDRUNION):
	union = {1 : (
		'pMonitorInfo1',
		MONITOR_INFO_1
		),2 : (
		'pMonitorInfo2',
		MONITOR_INFO_2
		)}


class MONITOR_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'MonitorInfo',
			MONITORINFO
			)
		)


class PORTINFO(NDRUNION):
	union = {1 : (
		'pPortInfo1',
		PORT_INFO_1
		),2 : (
		'pPortInfo2',
		PORT_INFO_2
		),3 : (
		'pPortInfo3',
		PORT_INFO_3
		),0x00FFFFFF : (
		'pPortInfoFF',
		PORT_INFO_FF
		)}


class PORT_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'PortInfo',
			PORTINFO
			)
		)


class DATA_PORT_VAR_CONTAINER(NDRUniConformantArray):
	item = BYTE


class PTR_PORT_VAR_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_PORT_VAR_CONTAINER
			)
		)


class PORT_VAR_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbMonitorData',
			DWORD
			),
			(
			'pMonitorData',
			PTR_PORT_VAR_CONTAINER
			)
		)


class PRINTERINFO(NDRUNION):
	union = {0 : (
		'pPrinterInfoStress',
		PRINTER_INFO_STRESS
		),1 : (
		'pPrinterInfo1',
		PRINTER_INFO_1
		),2 : (
		'pPrinterInfo2',
		PRINTER_INFO_2
		),3 : (
		'pPrinterInfo3',
		PRINTER_INFO_3
		),4 : (
		'pPrinterInfo4',
		PRINTER_INFO_4
		),5 : (
		'pPrinterInfo5',
		PRINTER_INFO_5
		),6 : (
		'pPrinterInfo6',
		PRINTER_INFO_6
		),7 : (
		'pPrinterInfo7',
		PRINTER_INFO_7
		),8 : (
		'pPrinterInfo8',
		PRINTER_INFO_8
		),9 : (
		'pPrinterInfo9',
		PRINTER_INFO_9
		)}


class PRINTER_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'PrinterInfo',
			PRINTERINFO
			)
		)


class DATA_RPC_BINARY_CONTAINER(NDRUniConformantArray):
	item = BYTE


class PTR_RPC_BINARY_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_BINARY_CONTAINER
			)
		)


class RPC_BINARY_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pszString',
			PTR_RPC_BINARY_CONTAINER
			)
		)


class U(NDRUNION):
	union = {BIDI_NULL : (
		'bData',
		INT
		),BIDI_INT : (
		'iData',
		LONG
		),BIDI_STRING : (
		'sData',
		WCHAR_T
		),BIDI_FLOAT : (
		'fData',
		FLOAT
		),BIDI_BLOB : (
		'biData',
		RPC_BINARY_CONTAINER
		)}


class RPC_BIDI_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwBidiType',
			DWORD
			),
			(
			'u',
			U
			)
		)


class RPC_BIDI_REQUEST_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwReqNumber',
			DWORD
			),
			(
			'pSchema',
			WCHAR_T
			),
			(
			'data',
			RPC_BIDI_DATA
			)
		)


class RPC_BIDI_RESPONSE_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'dwResult',
			DWORD
			),
			(
			'dwReqNumber',
			DWORD
			),
			(
			'pSchema',
			WCHAR_T
			),
			(
			'data',
			RPC_BIDI_DATA
			)
		)


class RPC_BIDI_REQUEST_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'Count',
			DWORD
			),
			(
			'aData',
			RPC_BIDI_REQUEST_DATA
			)
		)


class RPC_BIDI_RESPONSE_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'Count',
			DWORD
			),
			(
			'aData',
			RPC_BIDI_RESPONSE_DATA
			)
		)


class DATA_SECURITY_CONTAINER(NDRUniConformantArray):
	item = BYTE


class PTR_SECURITY_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_SECURITY_CONTAINER
			)
		)


class SECURITY_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pSecurity',
			PTR_SECURITY_CONTAINER
			)
		)


class CLIENTINFO(NDRUNION):
	union = {1 : (
		'pClientInfo1',
		SPLCLIENT_INFO_1
		),2 : (
		'pNotUsed1',
		SPLCLIENT_INFO_2
		),3 : (
		'pNotUsed2',
		SPLCLIENT_INFO_3
		)}


class SPLCLIENT_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Level',
			DWORD
			),
			(
			'ClientInfo',
			CLIENTINFO
			)
		)


class DATA_STRING_CONTAINER(NDRUniConformantArray):
	item = WCHAR


class PTR_STRING_CONTAINER(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_STRING_CONTAINER
			)
		)


class STRING_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pszString',
			PTR_STRING_CONTAINER
			)
		)


class SYSTEMTIME_CONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pSystemTime',
			SYSTEMTIME
			)
		)


class DATA_RPC_V2_NOTIFY_OPTIONS_TYPE(NDRUniConformantArray):
	item = UNSIGNED_SHORT


class PTR_RPC_V2_NOTIFY_OPTIONS_TYPE(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_V2_NOTIFY_OPTIONS_TYPE
			)
		)


class RPC_V2_NOTIFY_OPTIONS_TYPE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Type',
			UNSIGNED_SHORT
			),
			(
			'Reserved0',
			UNSIGNED_SHORT
			),
			(
			'Reserved1',
			DWORD
			),
			(
			'Reserved2',
			DWORD
			),
			(
			'Count',
			DWORD
			),
			(
			'pFields',
			PTR_RPC_V2_NOTIFY_OPTIONS_TYPE
			)
		)


class DATA_RPC_V2_NOTIFY_OPTIONS(NDRUniConformantArray):
	item = RPC_V2_NOTIFY_OPTIONS_TYPE


class PTR_RPC_V2_NOTIFY_OPTIONS(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_RPC_V2_NOTIFY_OPTIONS
			)
		)


class RPC_V2_NOTIFY_OPTIONS(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD
			),
			(
			'Reserved',
			DWORD
			),
			(
			'Count',
			DWORD
			),
			(
			'pTypes',
			PTR_RPC_V2_NOTIFY_OPTIONS
			)
		)


class RPC_V2_NOTIFY_INFO_DATA_DATA(NDRUNION):
	union = {0x2 : (
		'String',
		STRING_CONTAINER
		),0x1 : (
		'dwData',
		DWORD
		),0x4 : (
		'SystemTime',
		SYSTEMTIME_CONTAINER
		),0x3 : (
		'DevMode',
		DEVMODE_CONTAINER
		),0x5 : (
		'SecurityDescriptor',
		SECURITY_CONTAINER
		)}


class RPC_V2_NOTIFY_INFO_DATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Type',
			UNSIGNED_SHORT
			),
			(
			'Field',
			UNSIGNED_SHORT
			),
			(
			'Reserved',
			DWORD
			),
			(
			'Id',
			DWORD
			),
			(
			'Data',
			RPC_V2_NOTIFY_INFO_DATA_DATA
			)
		)


class RPC_V2_NOTIFY_INFO(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Version',
			DWORD
			),
			(
			'Flags',
			DWORD
			),
			(
			'Count',
			DWORD
			),
			(
			'aData',
			RPC_V2_NOTIFY_INFO_DATA
			)
		)


class RPC_V2_UREPLY_PRINTER(NDRUNION):
	union = {0 : (
		'pInfo',
		RPC_V2_NOTIFY_INFO
		)}


class CORE_PRINTER_DRIVER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'CoreDriverGUID',
			GUID
			),
			(
			'ftDriverDate',
			FILETIME
			),
			(
			'dwlDriverVersion',
			DWORDLONG
			),
			(
			'szPackageID',
			WCHAR_T
			)
		)


class DATA_PROPERTYBLOB(NDRUniConformantArray):
	item = BYTE


class PTR_PROPERTYBLOB(NDRPOINTER):
	referent = (
			(
			'Data',
			DATA_PROPERTYBLOB
			)
		)


class PROPERTYBLOB(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cbBuf',
			DWORD
			),
			(
			'pBuf',
			PTR_PROPERTYBLOB
			)
		)


class VALUE(NDRUNION):
	union = {kRpcPropertyTypeString : (
		'propertyString',
		WCHAR_T
		),kRpcPropertyTypeInt32 : (
		'propertyInt32',
		LONG
		),kRpcPropertyTypeInt64 : (
		'propertyInt64',
		LONGLONG
		),kRpcPropertyTypeByte : (
		'propertyByte',
		BYTE
		),kRpcPropertyTypeBuffer : (
		'propertyBlob',
		PROPERTYBLOB
		)}


class RPC_PRINTPROPERTYVALUE(NDRSTRUCT):
	align = 1
	structure = (
			(
			'ePropertyType',
			RPC_EPRINTPROPERTYTYPE
			),
			(
			'value',
			VALUE
			)
		)


class RPC_PRINTNAMEDPROPERTY(NDRSTRUCT):
	align = 1
	structure = (
			(
			'propertyName',
			WCHAR_T
			),
			(
			'propertyValue',
			RPC_PRINTPROPERTYVALUE
			)
		)


EBranchOfficeJobEventType = DWORD__ENUM
kInvalidJobState = 0
kLogJobPrinted = 0
kLogJobRendered = 0
kLogJobError = 0
kLogJobPipelineError = 0
class RPC_BRANCHOFFICEJOBDATAPRINTED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Status',
			DWORD
			),
			(
			'pDocumentName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pPortName',
			WCHAR_T
			),
			(
			'Size',
			LONGLONG
			),
			(
			'TotalPages',
			DWORD
			)
		)


class RPC_BRANCHOFFICEJOBDATARENDERED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'Size',
			LONGLONG
			),
			(
			'ICMMethod',
			DWORD
			),
			(
			'Color',
			SHORT
			),
			(
			'PrintQuality',
			SHORT
			),
			(
			'YResolution',
			SHORT
			),
			(
			'Copies',
			SHORT
			),
			(
			'TTOption',
			SHORT
			)
		)


class RPC_BRANCHOFFICEJOBDATAERROR(NDRSTRUCT):
	align = 1
	structure = (
			(
			'LastError',
			DWORD
			),
			(
			'pDocumentName',
			WCHAR_T
			),
			(
			'pUserName',
			WCHAR_T
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pDataType',
			WCHAR_T
			),
			(
			'TotalSize',
			LONGLONG
			),
			(
			'PrintedSize',
			LONGLONG
			),
			(
			'TotalPages',
			DWORD
			),
			(
			'PrintedPages',
			DWORD
			),
			(
			'pMachineName',
			WCHAR_T
			),
			(
			'pJobError',
			WCHAR_T
			),
			(
			'pErrorDescription',
			WCHAR_T
			)
		)


class RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pDocumentName',
			WCHAR_T
			),
			(
			'pPrinterName',
			WCHAR_T
			),
			(
			'pExtraErrorInfo',
			WCHAR_T
			)
		)


class RPC_BRANCHOFFICELOGOFFLINEFILEFULL(NDRSTRUCT):
	align = 1
	structure = (
			(
			'pMachineName',
			WCHAR_T
			)
		)


class JOBINFO(NDRUNION):
	union = {kLogJobPrinted : (
		'LogJobPrinted',
		RPC_BRANCHOFFICEJOBDATAPRINTED
		),kLogJobRendered : (
		'LogJobRendered',
		RPC_BRANCHOFFICEJOBDATARENDERED
		),kLogJobError : (
		'LogJobError',
		RPC_BRANCHOFFICEJOBDATAERROR
		),kLogJobPipelineError : (
		'LogPipelineFailed',
		RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED
		),kLogOfflineFileFull : (
		'LogOfflineFileFull',
		RPC_BRANCHOFFICELOGOFFLINEFILEFULL
		)}


class RPC_BRANCHOFFICEJOBDATA(NDRSTRUCT):
	align = 1
	structure = (
			(
			'eEventType',
			EBRANCHOFFICEJOBEVENTTYPE
			),
			(
			'JobId',
			DWORD
			),
			(
			'JobInfo',
			JOBINFO
			)
		)


class RPC_BRANCHOFFICEJOBDATACONTAINER(NDRSTRUCT):
	align = 1
	structure = (
			(
			'cJobDataEntries',
			DWORD
			),
			(
			'JobData',
			RPC_BRANCHOFFICEJOBDATA
			)
		)


class RpcEnumPrinters(NDRCALL):
	OPNUM = 0
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'Name',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrinterEnum',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPrintersResponse(NDRCALL):
	structure = (
			(
			'Flags',
			DWORD
			),
			(
			'Name',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrinterEnum',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcOpenPrinter(NDRCALL):
	OPNUM = 1
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'AccessRequired',
			DWORD
			)
		)


class RpcOpenPrinterResponse(NDRCALL):
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'AccessRequired',
			DWORD
			)
		)


class RpcSetJob(NDRCALL):
	OPNUM = 2
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pJobContainer',
			JOB_CONTAINER
			),
			(
			'Command',
			DWORD
			)
		)


class RpcSetJobResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pJobContainer',
			JOB_CONTAINER
			),
			(
			'Command',
			DWORD
			)
		)


class RpcGetJob(NDRCALL):
	OPNUM = 3
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'Level',
			DWORD
			),
			(
			'pJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetJobResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'Level',
			DWORD
			),
			(
			'pJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumJobs(NDRCALL):
	OPNUM = 4
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'FirstJob',
			DWORD
			),
			(
			'NoJobs',
			DWORD
			),
			(
			'Level',
			DWORD
			),
			(
			'pJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumJobsResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'FirstJob',
			DWORD
			),
			(
			'NoJobs',
			DWORD
			),
			(
			'Level',
			DWORD
			),
			(
			'pJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcAddPrinter(NDRCALL):
	OPNUM = 5
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			)
		)


class RpcAddPrinterResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			)
		)


class RpcDeletePrinter(NDRCALL):
	OPNUM = 6
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcDeletePrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcSetPrinter(NDRCALL):
	OPNUM = 7
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			),
			(
			'Command',
			DWORD
			)
		)


class RpcSetPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			),
			(
			'Command',
			DWORD
			)
		)


class RpcGetPrinter(NDRCALL):
	OPNUM = 8
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrinter',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrinter',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcAddPrinterDriver(NDRCALL):
	OPNUM = 9
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER
			)
		)


class RpcAddPrinterDriverResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER
			)
		)


class RpcEnumPrinterDrivers(NDRCALL):
	OPNUM = 10
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDrivers',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPrinterDriversResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDrivers',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrinterDriver(NDRCALL):
	OPNUM = 11
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriver',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrinterDriverResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriver',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrinterDriverDirectory(NDRCALL):
	OPNUM = 12
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriverDirectory',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrinterDriverDirectoryResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriverDirectory',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcDeletePrinterDriver(NDRCALL):
	OPNUM = 13
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			)
		)


class RpcDeletePrinterDriverResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			)
		)


class RpcAddPrintProcessor(NDRCALL):
	OPNUM = 14
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pPathName',
			WCHAR_T
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			)
		)


class RpcAddPrintProcessorResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pPathName',
			WCHAR_T
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			)
		)


class RpcEnumPrintProcessors(NDRCALL):
	OPNUM = 15
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrintProcessorInfo',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPrintProcessorsResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrintProcessorInfo',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrintProcessorDirectory(NDRCALL):
	OPNUM = 16
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrintProcessorDirectory',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetPrintProcessorDirectoryResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pPrintProcessorDirectory',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcStartDocPrinter(NDRCALL):
	OPNUM = 17
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDocInfoContainer',
			DOC_INFO_CONTAINER
			)
		)


class RpcStartDocPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDocInfoContainer',
			DOC_INFO_CONTAINER
			)
		)


class RpcStartPagePrinter(NDRCALL):
	OPNUM = 18
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcStartPagePrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcWritePrinter(NDRCALL):
	OPNUM = 19
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBuf',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcWritePrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBuf',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEndPagePrinter(NDRCALL):
	OPNUM = 20
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcEndPagePrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcAbortPrinter(NDRCALL):
	OPNUM = 21
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcAbortPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcReadPrinter(NDRCALL):
	OPNUM = 22
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcReadPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEndDocPrinter(NDRCALL):
	OPNUM = 23
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcEndDocPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcAddJob(NDRCALL):
	OPNUM = 24
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pAddJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcAddJobResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pAddJob',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcScheduleJob(NDRCALL):
	OPNUM = 25
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			)
		)


class RpcScheduleJobResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			)
		)


class RpcGetPrinterData(NDRCALL):
	OPNUM = 26
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			),
			(
			'nSize',
			DWORD
			)
		)


class RpcGetPrinterDataResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			),
			(
			'nSize',
			DWORD
			)
		)


class RpcSetPrinterData(NDRCALL):
	OPNUM = 27
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			),
			(
			'Type',
			DWORD
			),
			(
			'pData',
			BYTE
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcSetPrinterDataResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			),
			(
			'Type',
			DWORD
			),
			(
			'pData',
			BYTE
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcWaitForPrinterChange(NDRCALL):
	OPNUM = 28
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class RpcWaitForPrinterChangeResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Flags',
			DWORD
			)
		)


class RpcClosePrinter(NDRCALL):
	OPNUM = 29
	structure = (
			(
			'phPrinter',
			PRINTER_HANDLE
			)
		)


class RpcClosePrinterResponse(NDRCALL):
	structure = (
			(
			'phPrinter',
			PRINTER_HANDLE
			)
		)


class RpcAddForm(NDRCALL):
	OPNUM = 30
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER
			)
		)


class RpcAddFormResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER
			)
		)


class RpcDeleteForm(NDRCALL):
	OPNUM = 31
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			)
		)


class RpcDeleteFormResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			)
		)


class RpcGetForm(NDRCALL):
	OPNUM = 32
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pForm',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcGetFormResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pForm',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcSetForm(NDRCALL):
	OPNUM = 33
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER
			)
		)


class RpcSetFormResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pFormName',
			WCHAR_T
			),
			(
			'pFormInfoContainer',
			FORM_CONTAINER
			)
		)


class RpcEnumForms(NDRCALL):
	OPNUM = 34
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pForm',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumFormsResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pForm',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPorts(NDRCALL):
	OPNUM = 35
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPort',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPortsResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pPort',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumMonitors(NDRCALL):
	OPNUM = 36
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pMonitor',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumMonitorsResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'Level',
			DWORD
			),
			(
			'pMonitor',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
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


class RpcDeletePort(NDRCALL):
	OPNUM = 39
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'hWnd',
			ULONG_PTR
			),
			(
			'pPortName',
			WCHAR_T
			)
		)


class RpcDeletePortResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'hWnd',
			ULONG_PTR
			),
			(
			'pPortName',
			WCHAR_T
			)
		)


class RpcCreatePrinterIC(NDRCALL):
	OPNUM = 40
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			)
		)


class RpcCreatePrinterICResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			)
		)


class RpcPlayGdiScriptOnPrinterIC(NDRCALL):
	OPNUM = 41
	structure = (
			(
			'hPrinterIC',
			GDI_HANDLE
			),
			(
			'pIn',
			BYTE
			),
			(
			'cIn',
			DWORD
			),
			(
			'cOut',
			DWORD
			),
			(
			'ul',
			DWORD
			)
		)


class RpcPlayGdiScriptOnPrinterICResponse(NDRCALL):
	structure = (
			(
			'hPrinterIC',
			GDI_HANDLE
			),
			(
			'pIn',
			BYTE
			),
			(
			'cIn',
			DWORD
			),
			(
			'cOut',
			DWORD
			),
			(
			'ul',
			DWORD
			)
		)


class RpcDeletePrinterIC(NDRCALL):
	OPNUM = 42
	structure = (
			(
			'phPrinterIC',
			GDI_HANDLE
			)
		)


class RpcDeletePrinterICResponse(NDRCALL):
	structure = (
			(
			'phPrinterIC',
			GDI_HANDLE
			)
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


class Opnum45NotUsedOnWire(NDRCALL):
	OPNUM = 45
	structure = (

		)


class Opnum45NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcAddMonitor(NDRCALL):
	OPNUM = 46
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pMonitorContainer',
			MONITOR_CONTAINER
			)
		)


class RpcAddMonitorResponse(NDRCALL):
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pMonitorContainer',
			MONITOR_CONTAINER
			)
		)


class RpcDeleteMonitor(NDRCALL):
	OPNUM = 47
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			)
		)


class RpcDeleteMonitorResponse(NDRCALL):
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pMonitorName',
			WCHAR_T
			)
		)


class RpcDeletePrintProcessor(NDRCALL):
	OPNUM = 48
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			)
		)


class RpcDeletePrintProcessorResponse(NDRCALL):
	structure = (
			(
			'Name',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			)
		)


class Opnum49NotUsedOnWire(NDRCALL):
	OPNUM = 49
	structure = (

		)


class Opnum49NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum50NotUsedOnWire(NDRCALL):
	OPNUM = 50
	structure = (

		)


class Opnum50NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcEnumPrintProcessorDatatypes(NDRCALL):
	OPNUM = 51
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDatatypes',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPrintProcessorDatatypesResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrintProcessorName',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDatatypes',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcResetPrinter(NDRCALL):
	OPNUM = 52
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			)
		)


class RpcResetPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			)
		)


class RpcGetPrinterDriver2(NDRCALL):
	OPNUM = 53
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriver',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			),
			(
			'dwClientMajorVersion',
			DWORD
			),
			(
			'dwClientMinorVersion',
			DWORD
			)
		)


class RpcGetPrinterDriver2Response(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'Level',
			DWORD
			),
			(
			'pDriver',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			),
			(
			'dwClientMajorVersion',
			DWORD
			),
			(
			'dwClientMinorVersion',
			DWORD
			)
		)


class Opnum54NotUsedOnWire(NDRCALL):
	OPNUM = 54
	structure = (

		)


class Opnum54NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum55NotUsedOnWire(NDRCALL):
	OPNUM = 55
	structure = (

		)


class Opnum55NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcFindClosePrinterChangeNotification(NDRCALL):
	OPNUM = 56
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcFindClosePrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class Opnum57NotUsedOnWire(NDRCALL):
	OPNUM = 57
	structure = (

		)


class Opnum57NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcReplyOpenPrinter(NDRCALL):
	OPNUM = 58
	structure = (
			(
			'pMachine',
			STRING_HANDLE
			),
			(
			'dwPrinterRemote',
			DWORD
			),
			(
			'dwType',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
		)


class RpcReplyOpenPrinterResponse(NDRCALL):
	structure = (
			(
			'pMachine',
			STRING_HANDLE
			),
			(
			'dwPrinterRemote',
			DWORD
			),
			(
			'dwType',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
		)


class RpcRouterReplyPrinter(NDRCALL):
	OPNUM = 59
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
		)


class RpcRouterReplyPrinterResponse(NDRCALL):
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
		)


class RpcReplyClosePrinter(NDRCALL):
	OPNUM = 60
	structure = (
			(
			'phNotify',
			PRINTER_HANDLE
			)
		)


class RpcReplyClosePrinterResponse(NDRCALL):
	structure = (
			(
			'phNotify',
			PRINTER_HANDLE
			)
		)


class RpcAddPortEx(NDRCALL):
	OPNUM = 61
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPortContainer',
			PORT_CONTAINER
			),
			(
			'pPortVarContainer',
			PORT_VAR_CONTAINER
			),
			(
			'pMonitorName',
			WCHAR_T
			)
		)


class RpcAddPortExResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPortContainer',
			PORT_CONTAINER
			),
			(
			'pPortVarContainer',
			PORT_VAR_CONTAINER
			),
			(
			'pMonitorName',
			WCHAR_T
			)
		)


class RpcRemoteFindFirstPrinterChangeNotification(NDRCALL):
	OPNUM = 62
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'fdwOptions',
			DWORD
			),
			(
			'pszLocalMachine',
			WCHAR_T
			),
			(
			'dwPrinterLocal',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
		)


class RpcRemoteFindFirstPrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'fdwOptions',
			DWORD
			),
			(
			'pszLocalMachine',
			WCHAR_T
			),
			(
			'dwPrinterLocal',
			DWORD
			),
			(
			'cbBuffer',
			DWORD
			),
			(
			'pBuffer',
			BYTE
			)
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


class RpcRemoteFindFirstPrinterChangeNotificationEx(NDRCALL):
	OPNUM = 65
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'fdwOptions',
			DWORD
			),
			(
			'pszLocalMachine',
			WCHAR_T
			),
			(
			'dwPrinterLocal',
			DWORD
			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS
			)
		)


class RpcRemoteFindFirstPrinterChangeNotificationExResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'fdwOptions',
			DWORD
			),
			(
			'pszLocalMachine',
			WCHAR_T
			),
			(
			'dwPrinterLocal',
			DWORD
			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS
			)
		)


class RpcRouterReplyPrinterEx(NDRCALL):
	OPNUM = 66
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE
			),
			(
			'dwColor',
			DWORD
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'dwReplyType',
			DWORD
			),
			(
			'Reply',
			RPC_V2_UREPLY_PRINTER
			)
		)


class RpcRouterReplyPrinterExResponse(NDRCALL):
	structure = (
			(
			'hNotify',
			PRINTER_HANDLE
			),
			(
			'dwColor',
			DWORD
			),
			(
			'fdwFlags',
			DWORD
			),
			(
			'dwReplyType',
			DWORD
			),
			(
			'Reply',
			RPC_V2_UREPLY_PRINTER
			)
		)


class RpcRouterRefreshPrinterChangeNotification(NDRCALL):
	OPNUM = 67
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'dwColor',
			DWORD
			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS
			)
		)


class RpcRouterRefreshPrinterChangeNotificationResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'dwColor',
			DWORD
			),
			(
			'pOptions',
			RPC_V2_NOTIFY_OPTIONS
			)
		)


class Opnum68NotUsedOnWire(NDRCALL):
	OPNUM = 68
	structure = (

		)


class Opnum68NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcOpenPrinterEx(NDRCALL):
	OPNUM = 69
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'AccessRequired',
			DWORD
			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER
			)
		)


class RpcOpenPrinterExResponse(NDRCALL):
	structure = (
			(
			'pPrinterName',
			STRING_HANDLE
			),
			(
			'pDatatype',
			WCHAR_T
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'AccessRequired',
			DWORD
			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER
			)
		)


class RpcAddPrinterEx(NDRCALL):
	OPNUM = 70
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER
			)
		)


class RpcAddPrinterExResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPrinterContainer',
			PRINTER_CONTAINER
			),
			(
			'pDevModeContainer',
			DEVMODE_CONTAINER
			),
			(
			'pSecurityContainer',
			SECURITY_CONTAINER
			),
			(
			'pClientInfo',
			SPLCLIENT_CONTAINER
			)
		)


class RpcSetPort(NDRCALL):
	OPNUM = 71
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPortName',
			WCHAR_T
			),
			(
			'pPortContainer',
			PORT_CONTAINER
			)
		)


class RpcSetPortResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pPortName',
			WCHAR_T
			),
			(
			'pPortContainer',
			PORT_CONTAINER
			)
		)


class RpcEnumPrinterData(NDRCALL):
	OPNUM = 72
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'dwIndex',
			DWORD
			),
			(
			'cbValueName',
			DWORD
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcEnumPrinterDataResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'dwIndex',
			DWORD
			),
			(
			'cbValueName',
			DWORD
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcDeletePrinterData(NDRCALL):
	OPNUM = 73
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			)
		)


class RpcDeletePrinterDataResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pValueName',
			WCHAR_T
			)
		)


class Opnum74NotUsedOnWire(NDRCALL):
	OPNUM = 74
	structure = (

		)


class Opnum74NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum75NotUsedOnWire(NDRCALL):
	OPNUM = 75
	structure = (

		)


class Opnum75NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum76NotUsedOnWire(NDRCALL):
	OPNUM = 76
	structure = (

		)


class Opnum76NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcSetPrinterDataEx(NDRCALL):
	OPNUM = 77
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			),
			(
			'Type',
			DWORD
			),
			(
			'pData',
			BYTE
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcSetPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			),
			(
			'Type',
			DWORD
			),
			(
			'pData',
			BYTE
			),
			(
			'cbData',
			DWORD
			)
		)


class RpcGetPrinterDataEx(NDRCALL):
	OPNUM = 78
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			),
			(
			'nSize',
			DWORD
			)
		)


class RpcGetPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			),
			(
			'nSize',
			DWORD
			)
		)


class RpcEnumPrinterDataEx(NDRCALL):
	OPNUM = 79
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'cbEnumValues',
			DWORD
			)
		)


class RpcEnumPrinterDataExResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'cbEnumValues',
			DWORD
			)
		)


class RpcEnumPrinterKey(NDRCALL):
	OPNUM = 80
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'cbSubkey',
			DWORD
			)
		)


class RpcEnumPrinterKeyResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'cbSubkey',
			DWORD
			)
		)


class RpcDeletePrinterDataEx(NDRCALL):
	OPNUM = 81
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			)
		)


class RpcDeletePrinterDataExResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			),
			(
			'pValueName',
			CONST_WCHAR_T
			)
		)


class RpcDeletePrinterKey(NDRCALL):
	OPNUM = 82
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			)
		)


class RpcDeletePrinterKeyResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pKeyName',
			CONST_WCHAR_T
			)
		)


class Opnum83NotUsedOnWire(NDRCALL):
	OPNUM = 83
	structure = (

		)


class Opnum83NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcDeletePrinterDriverEx(NDRCALL):
	OPNUM = 84
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			),
			(
			'dwDeleteFlag',
			DWORD
			),
			(
			'dwVersionNum',
			DWORD
			)
		)


class RpcDeletePrinterDriverExResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pEnvironment',
			WCHAR_T
			),
			(
			'pDriverName',
			WCHAR_T
			),
			(
			'dwDeleteFlag',
			DWORD
			),
			(
			'dwVersionNum',
			DWORD
			)
		)


class RpcAddPerMachineConnection(NDRCALL):
	OPNUM = 85
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterName',
			CONST_WCHAR_T
			),
			(
			'pPrintServer',
			CONST_WCHAR_T
			),
			(
			'pProvider',
			CONST_WCHAR_T
			)
		)


class RpcAddPerMachineConnectionResponse(NDRCALL):
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterName',
			CONST_WCHAR_T
			),
			(
			'pPrintServer',
			CONST_WCHAR_T
			),
			(
			'pProvider',
			CONST_WCHAR_T
			)
		)


class RpcDeletePerMachineConnection(NDRCALL):
	OPNUM = 86
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterName',
			CONST_WCHAR_T
			)
		)


class RpcDeletePerMachineConnectionResponse(NDRCALL):
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterName',
			CONST_WCHAR_T
			)
		)


class RpcEnumPerMachineConnections(NDRCALL):
	OPNUM = 87
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterEnum',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcEnumPerMachineConnectionsResponse(NDRCALL):
	structure = (
			(
			'pServer',
			STRING_HANDLE
			),
			(
			'pPrinterEnum',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			)
		)


class RpcXcvData(NDRCALL):
	OPNUM = 88
	structure = (
			(
			'hXcv',
			PRINTER_HANDLE
			),
			(
			'pszDataName',
			CONST_WCHAR_T
			),
			(
			'pInputData',
			BYTE
			),
			(
			'cbInputData',
			DWORD
			),
			(
			'cbOutputData',
			DWORD
			),
			(
			'pdwStatus',
			DWORD
			)
		)


class RpcXcvDataResponse(NDRCALL):
	structure = (
			(
			'hXcv',
			PRINTER_HANDLE
			),
			(
			'pszDataName',
			CONST_WCHAR_T
			),
			(
			'pInputData',
			BYTE
			),
			(
			'cbInputData',
			DWORD
			),
			(
			'cbOutputData',
			DWORD
			),
			(
			'pdwStatus',
			DWORD
			)
		)


class RpcAddPrinterDriverEx(NDRCALL):
	OPNUM = 89
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER
			),
			(
			'dwFileCopyFlags',
			DWORD
			)
		)


class RpcAddPrinterDriverExResponse(NDRCALL):
	structure = (
			(
			'pName',
			STRING_HANDLE
			),
			(
			'pDriverContainer',
			DRIVER_CONTAINER
			),
			(
			'dwFileCopyFlags',
			DWORD
			)
		)


class Opnum90NotUsedOnWire(NDRCALL):
	OPNUM = 90
	structure = (

		)


class Opnum90NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum91NotUsedOnWire(NDRCALL):
	OPNUM = 91
	structure = (

		)


class Opnum91NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum92NotUsedOnWire(NDRCALL):
	OPNUM = 92
	structure = (

		)


class Opnum92NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum93NotUsedOnWire(NDRCALL):
	OPNUM = 93
	structure = (

		)


class Opnum93NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum94NotUsedOnWire(NDRCALL):
	OPNUM = 94
	structure = (

		)


class Opnum94NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum95NotUsedOnWire(NDRCALL):
	OPNUM = 95
	structure = (

		)


class Opnum95NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcFlushPrinter(NDRCALL):
	OPNUM = 96
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBuf',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			),
			(
			'cSleep',
			DWORD
			)
		)


class RpcFlushPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBuf',
			BYTE
			),
			(
			'cbBuf',
			DWORD
			),
			(
			'cSleep',
			DWORD
			)
		)


class RpcSendRecvBidiData(NDRCALL):
	OPNUM = 97
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pAction',
			CONST_WCHAR_T
			),
			(
			'pReqData',
			RPC_BIDI_REQUEST_CONTAINER
			)
		)


class RpcSendRecvBidiDataResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pAction',
			CONST_WCHAR_T
			),
			(
			'pReqData',
			RPC_BIDI_REQUEST_CONTAINER
			)
		)


class Opnum98NotUsedOnWire(NDRCALL):
	OPNUM = 98
	structure = (

		)


class Opnum98NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum99NotUsedOnWire(NDRCALL):
	OPNUM = 99
	structure = (

		)


class Opnum99NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum100NotUsedOnWire(NDRCALL):
	OPNUM = 100
	structure = (

		)


class Opnum100NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum101NotUsedOnWire(NDRCALL):
	OPNUM = 101
	structure = (

		)


class Opnum101NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcGetCorePrinterDrivers(NDRCALL):
	OPNUM = 102
	structure = (
			(
			'pszServer',
			STRING_HANDLE
			),
			(
			'pszEnvironment',
			CONST_WCHAR_T
			),
			(
			'cchCoreDrivers',
			DWORD
			),
			(
			'pszzCoreDriverDependencies',
			CONST_WCHAR_T
			),
			(
			'cCorePrinterDrivers',
			DWORD
			)
		)


class RpcGetCorePrinterDriversResponse(NDRCALL):
	structure = (
			(
			'pszServer',
			STRING_HANDLE
			),
			(
			'pszEnvironment',
			CONST_WCHAR_T
			),
			(
			'cchCoreDrivers',
			DWORD
			),
			(
			'pszzCoreDriverDependencies',
			CONST_WCHAR_T
			),
			(
			'cCorePrinterDrivers',
			DWORD
			)
		)


class Opnum103NotUsedOnWire(NDRCALL):
	OPNUM = 103
	structure = (

		)


class Opnum103NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcGetPrinterDriverPackagePath(NDRCALL):
	OPNUM = 104
	structure = (
			(
			'pszServer',
			STRING_HANDLE
			),
			(
			'pszEnvironment',
			CONST_WCHAR_T
			),
			(
			'pszLanguage',
			CONST_WCHAR_T
			),
			(
			'pszPackageID',
			CONST_WCHAR_T
			),
			(
			'pszDriverPackageCab',
			WCHAR_T
			),
			(
			'cchDriverPackageCab',
			DWORD
			)
		)


class RpcGetPrinterDriverPackagePathResponse(NDRCALL):
	structure = (
			(
			'pszServer',
			STRING_HANDLE
			),
			(
			'pszEnvironment',
			CONST_WCHAR_T
			),
			(
			'pszLanguage',
			CONST_WCHAR_T
			),
			(
			'pszPackageID',
			CONST_WCHAR_T
			),
			(
			'pszDriverPackageCab',
			WCHAR_T
			),
			(
			'cchDriverPackageCab',
			DWORD
			)
		)


class Opnum105NotUsedOnWire(NDRCALL):
	OPNUM = 105
	structure = (

		)


class Opnum105NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum106NotUsedOnWire(NDRCALL):
	OPNUM = 106
	structure = (

		)


class Opnum106NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum107NotUsedOnWire(NDRCALL):
	OPNUM = 107
	structure = (

		)


class Opnum107NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum108NotUsedOnWire(NDRCALL):
	OPNUM = 108
	structure = (

		)


class Opnum108NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum109NotUsedOnWire(NDRCALL):
	OPNUM = 109
	structure = (

		)


class Opnum109NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcGetJobNamedPropertyValue(NDRCALL):
	OPNUM = 110
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pszName',
			CONST_WCHAR_T
			)
		)


class RpcGetJobNamedPropertyValueResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pszName',
			CONST_WCHAR_T
			)
		)


class RpcSetJobNamedProperty(NDRCALL):
	OPNUM = 111
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pProperty',
			RPC_PRINTNAMEDPROPERTY
			)
		)


class RpcSetJobNamedPropertyResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pProperty',
			RPC_PRINTNAMEDPROPERTY
			)
		)


class RpcDeleteJobNamedProperty(NDRCALL):
	OPNUM = 112
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pszName',
			CONST_WCHAR_T
			)
		)


class RpcDeleteJobNamedPropertyResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			),
			(
			'pszName',
			CONST_WCHAR_T
			)
		)


class RpcEnumJobNamedProperties(NDRCALL):
	OPNUM = 113
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			)
		)


class RpcEnumJobNamedPropertiesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'JobId',
			DWORD
			)
		)


class Opnum114NotUsedOnWire(NDRCALL):
	OPNUM = 114
	structure = (

		)


class Opnum114NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class Opnum115NotUsedOnWire(NDRCALL):
	OPNUM = 115
	structure = (

		)


class Opnum115NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcLogJobInfoForBranchOffice(NDRCALL):
	OPNUM = 116
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBranchOfficeJobDataContainer',
			RPC_BRANCHOFFICEJOBDATACONTAINER
			)
		)


class RpcLogJobInfoForBranchOfficeResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'pBranchOfficeJobDataContainer',
			RPC_BRANCHOFFICEJOBDATACONTAINER
			)
		)


class RpcRegeneratePrintDeviceCapabilities(NDRCALL):
	OPNUM = 117
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class RpcRegeneratePrintDeviceCapabilitiesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			)
		)


class Opnum118NotUsedOnWire(NDRCALL):
	OPNUM = 118
	structure = (

		)


class Opnum118NotUsedOnWireResponse(NDRCALL):
	structure = (

		)


class RpcIppCreateJobOnPrinter(NDRCALL):
	OPNUM = 119
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'pdlFormat',
			CONST_WCHAR_T
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


class RpcIppCreateJobOnPrinterResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'pdlFormat',
			CONST_WCHAR_T
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


class RpcIppGetJobAttributes(NDRCALL):
	OPNUM = 120
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'attributeNameCount',
			DWORD
			),
			(
			'attributeNames',
			CONST_WCHAR_T
			)
		)


class RpcIppGetJobAttributesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'attributeNameCount',
			DWORD
			),
			(
			'attributeNames',
			CONST_WCHAR_T
			)
		)


class RpcIppSetJobAttributes(NDRCALL):
	OPNUM = 121
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


class RpcIppSetJobAttributesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobId',
			DWORD
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


class RpcIppGetPrinterAttributes(NDRCALL):
	OPNUM = 122
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'attributeNameCount',
			DWORD
			),
			(
			'attributeNames',
			CONST_WCHAR_T
			)
		)


class RpcIppGetPrinterAttributesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'attributeNameCount',
			DWORD
			),
			(
			'attributeNames',
			CONST_WCHAR_T
			)
		)


class RpcIppSetPrinterAttributes(NDRCALL):
	OPNUM = 123
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


class RpcIppSetPrinterAttributesResponse(NDRCALL):
	structure = (
			(
			'hPrinter',
			PRINTER_HANDLE
			),
			(
			'jobAttributeGroupBufferSize',
			DWORD
			),
			(
			'jobAttributeGroupBuffer',
			BYTE
			)
		)


OPNUMS = {0 : (
	RpcEnumPrinters,
	RpcEnumPrintersResponse
	),1 : (
	RpcOpenPrinter,
	RpcOpenPrinterResponse
	),2 : (
	RpcSetJob,
	RpcSetJobResponse
	),3 : (
	RpcGetJob,
	RpcGetJobResponse
	),4 : (
	RpcEnumJobs,
	RpcEnumJobsResponse
	),5 : (
	RpcAddPrinter,
	RpcAddPrinterResponse
	),6 : (
	RpcDeletePrinter,
	RpcDeletePrinterResponse
	),7 : (
	RpcSetPrinter,
	RpcSetPrinterResponse
	),8 : (
	RpcGetPrinter,
	RpcGetPrinterResponse
	),9 : (
	RpcAddPrinterDriver,
	RpcAddPrinterDriverResponse
	),10 : (
	RpcEnumPrinterDrivers,
	RpcEnumPrinterDriversResponse
	),11 : (
	RpcGetPrinterDriver,
	RpcGetPrinterDriverResponse
	),12 : (
	RpcGetPrinterDriverDirectory,
	RpcGetPrinterDriverDirectoryResponse
	),13 : (
	RpcDeletePrinterDriver,
	RpcDeletePrinterDriverResponse
	),14 : (
	RpcAddPrintProcessor,
	RpcAddPrintProcessorResponse
	),15 : (
	RpcEnumPrintProcessors,
	RpcEnumPrintProcessorsResponse
	),16 : (
	RpcGetPrintProcessorDirectory,
	RpcGetPrintProcessorDirectoryResponse
	),17 : (
	RpcStartDocPrinter,
	RpcStartDocPrinterResponse
	),18 : (
	RpcStartPagePrinter,
	RpcStartPagePrinterResponse
	),19 : (
	RpcWritePrinter,
	RpcWritePrinterResponse
	),20 : (
	RpcEndPagePrinter,
	RpcEndPagePrinterResponse
	),21 : (
	RpcAbortPrinter,
	RpcAbortPrinterResponse
	),22 : (
	RpcReadPrinter,
	RpcReadPrinterResponse
	),23 : (
	RpcEndDocPrinter,
	RpcEndDocPrinterResponse
	),24 : (
	RpcAddJob,
	RpcAddJobResponse
	),25 : (
	RpcScheduleJob,
	RpcScheduleJobResponse
	),26 : (
	RpcGetPrinterData,
	RpcGetPrinterDataResponse
	),27 : (
	RpcSetPrinterData,
	RpcSetPrinterDataResponse
	),28 : (
	RpcWaitForPrinterChange,
	RpcWaitForPrinterChangeResponse
	),29 : (
	RpcClosePrinter,
	RpcClosePrinterResponse
	),30 : (
	RpcAddForm,
	RpcAddFormResponse
	),31 : (
	RpcDeleteForm,
	RpcDeleteFormResponse
	),32 : (
	RpcGetForm,
	RpcGetFormResponse
	),33 : (
	RpcSetForm,
	RpcSetFormResponse
	),34 : (
	RpcEnumForms,
	RpcEnumFormsResponse
	),35 : (
	RpcEnumPorts,
	RpcEnumPortsResponse
	),36 : (
	RpcEnumMonitors,
	RpcEnumMonitorsResponse
	),37 : (
	Opnum37NotUsedOnWire,
	Opnum37NotUsedOnWireResponse
	),38 : (
	Opnum38NotUsedOnWire,
	Opnum38NotUsedOnWireResponse
	),39 : (
	RpcDeletePort,
	RpcDeletePortResponse
	),40 : (
	RpcCreatePrinterIC,
	RpcCreatePrinterICResponse
	),41 : (
	RpcPlayGdiScriptOnPrinterIC,
	RpcPlayGdiScriptOnPrinterICResponse
	),42 : (
	RpcDeletePrinterIC,
	RpcDeletePrinterICResponse
	),43 : (
	Opnum43NotUsedOnWire,
	Opnum43NotUsedOnWireResponse
	),44 : (
	Opnum44NotUsedOnWire,
	Opnum44NotUsedOnWireResponse
	),45 : (
	Opnum45NotUsedOnWire,
	Opnum45NotUsedOnWireResponse
	),46 : (
	RpcAddMonitor,
	RpcAddMonitorResponse
	),47 : (
	RpcDeleteMonitor,
	RpcDeleteMonitorResponse
	),48 : (
	RpcDeletePrintProcessor,
	RpcDeletePrintProcessorResponse
	),49 : (
	Opnum49NotUsedOnWire,
	Opnum49NotUsedOnWireResponse
	),50 : (
	Opnum50NotUsedOnWire,
	Opnum50NotUsedOnWireResponse
	),51 : (
	RpcEnumPrintProcessorDatatypes,
	RpcEnumPrintProcessorDatatypesResponse
	),52 : (
	RpcResetPrinter,
	RpcResetPrinterResponse
	),53 : (
	RpcGetPrinterDriver2,
	RpcGetPrinterDriver2Response
	),54 : (
	Opnum54NotUsedOnWire,
	Opnum54NotUsedOnWireResponse
	),55 : (
	Opnum55NotUsedOnWire,
	Opnum55NotUsedOnWireResponse
	),56 : (
	RpcFindClosePrinterChangeNotification,
	RpcFindClosePrinterChangeNotificationResponse
	),57 : (
	Opnum57NotUsedOnWire,
	Opnum57NotUsedOnWireResponse
	),58 : (
	RpcReplyOpenPrinter,
	RpcReplyOpenPrinterResponse
	),59 : (
	RpcRouterReplyPrinter,
	RpcRouterReplyPrinterResponse
	),60 : (
	RpcReplyClosePrinter,
	RpcReplyClosePrinterResponse
	),61 : (
	RpcAddPortEx,
	RpcAddPortExResponse
	),62 : (
	RpcRemoteFindFirstPrinterChangeNotification,
	RpcRemoteFindFirstPrinterChangeNotificationResponse
	),63 : (
	Opnum63NotUsedOnWire,
	Opnum63NotUsedOnWireResponse
	),64 : (
	Opnum64NotUsedOnWire,
	Opnum64NotUsedOnWireResponse
	),65 : (
	RpcRemoteFindFirstPrinterChangeNotificationEx,
	RpcRemoteFindFirstPrinterChangeNotificationExResponse
	),66 : (
	RpcRouterReplyPrinterEx,
	RpcRouterReplyPrinterExResponse
	),67 : (
	RpcRouterRefreshPrinterChangeNotification,
	RpcRouterRefreshPrinterChangeNotificationResponse
	),68 : (
	Opnum68NotUsedOnWire,
	Opnum68NotUsedOnWireResponse
	),69 : (
	RpcOpenPrinterEx,
	RpcOpenPrinterExResponse
	),70 : (
	RpcAddPrinterEx,
	RpcAddPrinterExResponse
	),71 : (
	RpcSetPort,
	RpcSetPortResponse
	),72 : (
	RpcEnumPrinterData,
	RpcEnumPrinterDataResponse
	),73 : (
	RpcDeletePrinterData,
	RpcDeletePrinterDataResponse
	),74 : (
	Opnum74NotUsedOnWire,
	Opnum74NotUsedOnWireResponse
	),75 : (
	Opnum75NotUsedOnWire,
	Opnum75NotUsedOnWireResponse
	),76 : (
	Opnum76NotUsedOnWire,
	Opnum76NotUsedOnWireResponse
	),77 : (
	RpcSetPrinterDataEx,
	RpcSetPrinterDataExResponse
	),78 : (
	RpcGetPrinterDataEx,
	RpcGetPrinterDataExResponse
	),79 : (
	RpcEnumPrinterDataEx,
	RpcEnumPrinterDataExResponse
	),80 : (
	RpcEnumPrinterKey,
	RpcEnumPrinterKeyResponse
	),81 : (
	RpcDeletePrinterDataEx,
	RpcDeletePrinterDataExResponse
	),82 : (
	RpcDeletePrinterKey,
	RpcDeletePrinterKeyResponse
	),83 : (
	Opnum83NotUsedOnWire,
	Opnum83NotUsedOnWireResponse
	),84 : (
	RpcDeletePrinterDriverEx,
	RpcDeletePrinterDriverExResponse
	),85 : (
	RpcAddPerMachineConnection,
	RpcAddPerMachineConnectionResponse
	),86 : (
	RpcDeletePerMachineConnection,
	RpcDeletePerMachineConnectionResponse
	),87 : (
	RpcEnumPerMachineConnections,
	RpcEnumPerMachineConnectionsResponse
	),88 : (
	RpcXcvData,
	RpcXcvDataResponse
	),89 : (
	RpcAddPrinterDriverEx,
	RpcAddPrinterDriverExResponse
	),90 : (
	Opnum90NotUsedOnWire,
	Opnum90NotUsedOnWireResponse
	),91 : (
	Opnum91NotUsedOnWire,
	Opnum91NotUsedOnWireResponse
	),92 : (
	Opnum92NotUsedOnWire,
	Opnum92NotUsedOnWireResponse
	),93 : (
	Opnum93NotUsedOnWire,
	Opnum93NotUsedOnWireResponse
	),94 : (
	Opnum94NotUsedOnWire,
	Opnum94NotUsedOnWireResponse
	),95 : (
	Opnum95NotUsedOnWire,
	Opnum95NotUsedOnWireResponse
	),96 : (
	RpcFlushPrinter,
	RpcFlushPrinterResponse
	),97 : (
	RpcSendRecvBidiData,
	RpcSendRecvBidiDataResponse
	),98 : (
	Opnum98NotUsedOnWire,
	Opnum98NotUsedOnWireResponse
	),99 : (
	Opnum99NotUsedOnWire,
	Opnum99NotUsedOnWireResponse
	),100 : (
	Opnum100NotUsedOnWire,
	Opnum100NotUsedOnWireResponse
	),101 : (
	Opnum101NotUsedOnWire,
	Opnum101NotUsedOnWireResponse
	),102 : (
	RpcGetCorePrinterDrivers,
	RpcGetCorePrinterDriversResponse
	),103 : (
	Opnum103NotUsedOnWire,
	Opnum103NotUsedOnWireResponse
	),104 : (
	RpcGetPrinterDriverPackagePath,
	RpcGetPrinterDriverPackagePathResponse
	),105 : (
	Opnum105NotUsedOnWire,
	Opnum105NotUsedOnWireResponse
	),106 : (
	Opnum106NotUsedOnWire,
	Opnum106NotUsedOnWireResponse
	),107 : (
	Opnum107NotUsedOnWire,
	Opnum107NotUsedOnWireResponse
	),108 : (
	Opnum108NotUsedOnWire,
	Opnum108NotUsedOnWireResponse
	),109 : (
	Opnum109NotUsedOnWire,
	Opnum109NotUsedOnWireResponse
	),110 : (
	RpcGetJobNamedPropertyValue,
	RpcGetJobNamedPropertyValueResponse
	),111 : (
	RpcSetJobNamedProperty,
	RpcSetJobNamedPropertyResponse
	),112 : (
	RpcDeleteJobNamedProperty,
	RpcDeleteJobNamedPropertyResponse
	),113 : (
	RpcEnumJobNamedProperties,
	RpcEnumJobNamedPropertiesResponse
	),114 : (
	Opnum114NotUsedOnWire,
	Opnum114NotUsedOnWireResponse
	),115 : (
	Opnum115NotUsedOnWire,
	Opnum115NotUsedOnWireResponse
	),116 : (
	RpcLogJobInfoForBranchOffice,
	RpcLogJobInfoForBranchOfficeResponse
	),117 : (
	RpcRegeneratePrintDeviceCapabilities,
	RpcRegeneratePrintDeviceCapabilitiesResponse
	),118 : (
	Opnum118NotUsedOnWire,
	Opnum118NotUsedOnWireResponse
	),119 : (
	RpcIppCreateJobOnPrinter,
	RpcIppCreateJobOnPrinterResponse
	),120 : (
	RpcIppGetJobAttributes,
	RpcIppGetJobAttributesResponse
	),121 : (
	RpcIppSetJobAttributes,
	RpcIppSetJobAttributesResponse
	),122 : (
	RpcIppGetPrinterAttributes,
	RpcIppGetPrinterAttributesResponse
	),123 : (
	RpcIppSetPrinterAttributes,
	RpcIppSetPrinterAttributesResponse
	)}
