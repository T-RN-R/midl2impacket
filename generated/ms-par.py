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

#TYPEDEFS

#################################################################################

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#IRemoteWinspool Definition

#################################################################################

MSRPC_UUID_IREMOTEWINSPOOL = uuidtup_to_bin(('76F03F96-CDFD-44fc-A22C-64950A001209','0.0'))


BIDI_NULL = 0,
BIDI_INT = 1,
BIDI_FLOAT = 2,
BIDI_BOOL = 3,
BIDI_STRING = 4,
BIDI_TEXT = 5,
BIDI_ENUM = 6,
BIDI_BLOB = 7
        

kRpcPropertyTypeString = 1,
kRpcPropertyTypeInt32 = 1,
kRpcPropertyTypeInt64 = 1,
kRpcPropertyTypeByte = 1
        

kInvalidJobState = 0,
kLogJobPrinted = 0,
kLogJobRendered = 0,
kLogJobError = 0,
kLogJobPipelineError = 0
        
LANGID = UNSIGNED_SHORT
GDI_HANDLE = VOID
PRINTER_HANDLE = VOID
STRING_HANDLE = WCHAR_T

class SIZE(NDRSTRUCT):
    structure = (
        ('cx', LONG),('cy', LONG),
    )


class RECTL(NDRSTRUCT):
    structure = (
        ('left', LONG),('top', LONG),('right', LONG),('bottom', LONG),
    )


class DEVMODE(NDRSTRUCT):
    structure = (
        ('dmDeviceName', WCHAR_T),('dmSpecVersion', UNSIGNED_SHORT),('dmDriverVersion', UNSIGNED_SHORT),('dmSize', UNSIGNED_SHORT),('dmDriverExtra', UNSIGNED_SHORT),('dmFields', DWORD),('dmOrientation', SHORT),('dmPaperSize', SHORT),('dmPaperLength', SHORT),('dmPaperWidth', SHORT),('dmScale', SHORT),('dmCopies', SHORT),('dmDefaultSource', SHORT),('dmPrintQuality', SHORT),('dmColor', SHORT),('dmDuplex', SHORT),('dmYResolution', SHORT),('dmTTOption', SHORT),('dmCollate', SHORT),('dmFormName', WCHAR_T),('reserved0', UNSIGNED_SHORT),('reserved1', DWORD),('reserved2', DWORD),('reserved3', DWORD),('dmNup', DWORD),('reserved4', DWORD),('dmICMMethod', DWORD),('dmICMIntent', DWORD),('dmMediaType', DWORD),('dmDitherType', DWORD),('reserved5', DWORD),('reserved6', DWORD),('reserved7', DWORD),('reserved8', DWORD),
    )


class DOC_INFO_1(NDRSTRUCT):
    structure = (
        ('pDocName', WCHAR_T),('pOutputFile', WCHAR_T),('pDatatype', WCHAR_T),
    )


class DRIVER_INFO_1(NDRSTRUCT):
    structure = (
        ('pName', WCHAR_T),
    )


class DRIVER_INFO_2(NDRSTRUCT):
    structure = (
        ('cVersion', DWORD),('pName', WCHAR_T),('pEnvironment', WCHAR_T),('pDriverPath', WCHAR_T),('pDataFile', WCHAR_T),('pConfigFile', WCHAR_T),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cVersion', DWORD),	('pName', WCHAR_T),	('pEnvironment', WCHAR_T),	('pDriverPath', WCHAR_T),	('pDataFile', WCHAR_T),	('pConfigFile', WCHAR_T),	('pHelpFile', WCHAR_T),	('pMonitorName', WCHAR_T),	('pDefaultDataType', WCHAR_T),	('cchDependentFiles', DWORD),	('pDependentFiles', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cVersion', DWORD),	('pName', WCHAR_T),	('pEnvironment', WCHAR_T),	('pDriverPath', WCHAR_T),	('pDataFile', WCHAR_T),	('pConfigFile', WCHAR_T),	('pHelpFile', WCHAR_T),	('pMonitorName', WCHAR_T),	('pDefaultDataType', WCHAR_T),	('cchDependentFiles', DWORD),	('pDependentFiles', WCHAR_T),	('cchPreviousNames', DWORD),	('pszzPreviousNames', PTR_DWORD),

    )
        

class DATA_WCHAR_T(NDRUniConformantArray):
    item = WCHAR_T

class PTR_WCHAR_T(NDRPOINTER):
    referent = (
        ('Data', DATA_WCHAR_T),
    )

class WCHAR_T(NDRSTRUCT):
    structure = (
	('cVersion', DWORD),	('pName', WCHAR_T),	('pEnvironment', WCHAR_T),	('pDriverPath', WCHAR_T),	('pDataFile', WCHAR_T),	('pConfigFile', WCHAR_T),	('pHelpFile', WCHAR_T),	('pMonitorName', WCHAR_T),	('pDefaultDataType', WCHAR_T),	('cchDependentFiles', DWORD),	('pDependentFiles', WCHAR_T),	('cchPreviousNames', DWORD),	('pszzPreviousNames', PTR_DWORD),
	('ftDriverDate', FILETIME),	('dwlDriverVersion', DWORDLONG),	('pMfgName', WCHAR_T),	('pOEMUrl', WCHAR_T),	('pHardwareID', WCHAR_T),	('pProvider', WCHAR_T),
    )
        

class DATA_DWORDLONG(NDRUniConformantArray):
    item = WCHAR_T

class PTR_DWORDLONG(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORDLONG),
    )

class DWORDLONG(NDRSTRUCT):
    structure = (
	('cVersion', DWORD),	('pName', WCHAR_T),	('pEnvironment', WCHAR_T),	('pDriverPath', WCHAR_T),	('pDataFile', WCHAR_T),	('pConfigFile', WCHAR_T),	('pHelpFile', WCHAR_T),	('pMonitorName', WCHAR_T),	('pDefaultDataType', WCHAR_T),	('cchDependentFiles', DWORD),	('pDependentFiles', WCHAR_T),	('cchPreviousNames', DWORD),	('pszzPreviousNames', WCHAR_T),	('ftDriverDate', FILETIME),	('dwlDriverVersion', DWORDLONG),	('pMfgName', WCHAR_T),	('pOEMUrl', WCHAR_T),	('pHardwareID', WCHAR_T),	('pProvider', WCHAR_T),	('pPrintProcessor', WCHAR_T),	('pVendorSetup', WCHAR_T),	('cchColorProfiles', DWORD),	('pszzColorProfiles', WCHAR_T),	('pInfPath', WCHAR_T),	('dwPrinterDriverAttributes', DWORD),	('cchCoreDependencies', DWORD),	('pszzCoreDriverDependencies', PTR_DWORD),
	('ftMinInboxDriverVerDate', FILETIME),	('dwlMinInboxDriverVerVersion', DWORDLONG),
    )
        

class FORM_INFO_1(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('pName', WCHAR_T),('Size', SIZE),('ImageableArea', RECTL),
    )


class RPC_FORM_INFO_2(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('pName', CONST_WCHAR_T),('Size', SIZE),('ImageableArea', RECTL),('pKeyword', CONST_CHAR),('StringType', DWORD),('pMuiDll', CONST_WCHAR_T),('dwResourceId', DWORD),('pDisplayName', CONST_WCHAR_T),('wLangID', LANGID),
    )


class JOB_INFO_1(NDRSTRUCT):
    structure = (
        ('JobId', DWORD),('pPrinterName', WCHAR_T),('pMachineName', WCHAR_T),('pUserName', WCHAR_T),('pDocument', WCHAR_T),('pDatatype', WCHAR_T),('pStatus', WCHAR_T),('Status', DWORD),('Priority', DWORD),('Position', DWORD),('TotalPages', DWORD),('PagesPrinted', DWORD),('Submitted', SYSTEMTIME),
    )


class JOB_INFO_2(NDRSTRUCT):
    structure = (
        ('JobId', DWORD),('pPrinterName', WCHAR_T),('pMachineName', WCHAR_T),('pUserName', WCHAR_T),('pDocument', WCHAR_T),('pNotifyName', WCHAR_T),('pDatatype', WCHAR_T),('pPrintProcessor', WCHAR_T),('pParameters', WCHAR_T),('pDriverName', WCHAR_T),('pDevMode', DEVMODE),('pStatus', WCHAR_T),('pSecurityDescriptor', SECURITY_DESCRIPTOR),('Status', DWORD),('Priority', DWORD),('Position', DWORD),('StartTime', DWORD),('UntilTime', DWORD),('TotalPages', DWORD),('Size', DWORD),('Submitted', SYSTEMTIME),('Time', DWORD),('PagesPrinted', DWORD),
    )


class JOB_INFO_3(NDRSTRUCT):
    structure = (
        ('JobId', DWORD),('NextJobId', DWORD),('Reserved', DWORD),
    )


class JOB_INFO_4(NDRSTRUCT):
    structure = (
        ('JobId', DWORD),('pPrinterName', WCHAR_T),('pMachineName', WCHAR_T),('pUserName', WCHAR_T),('pDocument', WCHAR_T),('pNotifyName', WCHAR_T),('pDatatype', WCHAR_T),('pPrintProcessor', WCHAR_T),('pParameters', WCHAR_T),('pDriverName', WCHAR_T),('pDevMode', DEVMODE),('pStatus', WCHAR_T),('pSecurityDescriptor', SECURITY_DESCRIPTOR),('Status', DWORD),('Priority', DWORD),('Position', DWORD),('StartTime', DWORD),('UntilTime', DWORD),('TotalPages', DWORD),('Size', DWORD),('Submitted', SYSTEMTIME),('Time', DWORD),('PagesPrinted', DWORD),('SizeHigh', LONG),
    )


class MONITOR_INFO_1(NDRSTRUCT):
    structure = (
        ('pName', WCHAR_T),
    )


class MONITOR_INFO_2(NDRSTRUCT):
    structure = (
        ('pName', WCHAR_T),('pEnvironment', WCHAR_T),('pDLLName', WCHAR_T),
    )


class PORT_INFO_1(NDRSTRUCT):
    structure = (
        ('pPortName', WCHAR_T),
    )


class PORT_INFO_2(NDRSTRUCT):
    structure = (
        ('pPortName', WCHAR_T),('pMonitorName', WCHAR_T),('pDescription', WCHAR_T),('fPortType', DWORD),('Reserved', DWORD),
    )


class PORT_INFO_3(NDRSTRUCT):
    structure = (
        ('dwStatus', DWORD),('pszStatus', WCHAR_T),('dwSeverity', DWORD),
    )


class PORT_INFO_FF(NDRSTRUCT):
    structure = (
        ('pPortName', WCHAR_T),('cbMonitorData', DWORD),('pMonitorData', BYTE),
    )


class PRINTER_INFO_STRESS(NDRSTRUCT):
    structure = (
        ('pPrinterName', WCHAR_T),('pServerName', WCHAR_T),('cJobs', DWORD),('cTotalJobs', DWORD),('cTotalBytes', DWORD),('stUpTime', SYSTEMTIME),('MaxcRef', DWORD),('cTotalPagesPrinted', DWORD),('dwGetVersion', DWORD),('fFreeBuild', DWORD),('cSpooling', DWORD),('cMaxSpooling', DWORD),('cRef', DWORD),('cErrorOutOfPaper', DWORD),('cErrorNotReady', DWORD),('cJobError', DWORD),('dwNumberOfProcessors', DWORD),('dwProcessorType', DWORD),('dwHighPartTotalBytes', DWORD),('cChangeID', DWORD),('dwLastError', DWORD),('Status', DWORD),('cEnumerateNetworkPrinters', DWORD),('cAddNetPrinters', DWORD),('wProcessorArchitecture', UNSIGNED_SHORT),('wProcessorLevel', UNSIGNED_SHORT),('cRefIC', DWORD),('dwReserved2', DWORD),('dwReserved3', DWORD),
    )


class PRINTER_INFO_1(NDRSTRUCT):
    structure = (
        ('Flags', DWORD),('pDescription', WCHAR_T),('pName', WCHAR_T),('pComment', WCHAR_T),
    )


class PRINTER_INFO_2(NDRSTRUCT):
    structure = (
        ('pServerName', WCHAR_T),('pPrinterName', WCHAR_T),('pShareName', WCHAR_T),('pPortName', WCHAR_T),('pDriverName', WCHAR_T),('pComment', WCHAR_T),('pLocation', WCHAR_T),('pDevMode', DEVMODE),('pSepFile', WCHAR_T),('pPrintProcessor', WCHAR_T),('pDatatype', WCHAR_T),('pParameters', WCHAR_T),('pSecurityDescriptor', SECURITY_DESCRIPTOR),('Attributes', DWORD),('Priority', DWORD),('DefaultPriority', DWORD),('StartTime', DWORD),('UntilTime', DWORD),('Status', DWORD),('cJobs', DWORD),('AveragePPM', DWORD),
    )


class PRINTER_INFO_3(NDRSTRUCT):
    structure = (
        ('pSecurityDescriptor', SECURITY_DESCRIPTOR),
    )


class PRINTER_INFO_4(NDRSTRUCT):
    structure = (
        ('pPrinterName', WCHAR_T),('pServerName', WCHAR_T),('Attributes', DWORD),
    )


class PRINTER_INFO_5(NDRSTRUCT):
    structure = (
        ('pPrinterName', WCHAR_T),('pPortName', WCHAR_T),('Attributes', DWORD),('DeviceNotSelectedTimeout', DWORD),('TransmissionRetryTimeout', DWORD),
    )


class PRINTER_INFO_6(NDRSTRUCT):
    structure = (
        ('dwStatus', DWORD),
    )


class PRINTER_INFO_7(NDRSTRUCT):
    structure = (
        ('pszObjectGUID', WCHAR_T),('dwAction', DWORD),
    )


class PRINTER_INFO_8(NDRSTRUCT):
    structure = (
        ('pDevMode', DEVMODE),
    )


class PRINTER_INFO_9(NDRSTRUCT):
    structure = (
        ('pDevMode', DEVMODE),
    )


class SPLCLIENT_INFO_1(NDRSTRUCT):
    structure = (
        ('dwSize', DWORD),('pMachineName', WCHAR_T),('pUserName', WCHAR_T),('dwBuildNum', DWORD),('dwMajorVersion', DWORD),('dwMinorVersion', DWORD),('wProcessorArchitecture', UNSIGNED_SHORT),
    )


class SPLCLIENT_INFO_2(NDRSTRUCT):
    structure = (
        ('notUsed', LONG_PTR),
    )


class SPLCLIENT_INFO_3(NDRSTRUCT):
    structure = (
        ('cbSize', UNSIGNED_INT),('dwFlags', DWORD),('dwSize', DWORD),('pMachineName', WCHAR_T),('pUserName', WCHAR_T),('dwBuildNum', DWORD),('dwMajorVersion', DWORD),('dwMinorVersion', DWORD),('wProcessorArchitecture', UNSIGNED_SHORT),('hSplPrinter', UNSIGNED___INT64),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbBuf', DWORD),	('pDevMode', PTR_DWORD),

    )
        

class DOCINFO(NDRUNION):
    union = {
        1: ('pDocInfo1',DOC_INFO_1),
    }
        

class DOC_INFO_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('DocInfo', DOCINFO),
    )


class DRIVERINFO(NDRUNION):
    union = {
        1: ('Level1',DRIVER_INFO_1),2: ('Level2',DRIVER_INFO_2),3: ('Level3',RPC_DRIVER_INFO_3),4: ('Level4',RPC_DRIVER_INFO_4),6: ('Level6',RPC_DRIVER_INFO_6),8: ('Level8',RPC_DRIVER_INFO_8),
    }
        

class DRIVER_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('DriverInfo', DRIVERINFO),
    )


class FORMINFO(NDRUNION):
    union = {
        1: ('pFormInfo1',FORM_INFO_1),2: ('pFormInfo2',RPC_FORM_INFO_2),
    }
        

class FORM_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('FormInfo', FORMINFO),
    )


class JOBINFO(NDRUNION):
    union = {
        1: ('Level1',JOB_INFO_1),2: ('Level2',JOB_INFO_2),3: ('Level3',JOB_INFO_3),4: ('Level4',JOB_INFO_4),
    }
        

class JOB_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('JobInfo', JOBINFO),
    )


class MONITORINFO(NDRUNION):
    union = {
        1: ('pMonitorInfo1',MONITOR_INFO_1),2: ('pMonitorInfo2',MONITOR_INFO_2),
    }
        

class MONITOR_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('MonitorInfo', MONITORINFO),
    )


class PORTINFO(NDRUNION):
    union = {
        1: ('pPortInfo1',PORT_INFO_1),2: ('pPortInfo2',PORT_INFO_2),3: ('pPortInfo3',PORT_INFO_3),0x00FFFFFF: ('pPortInfoFF',PORT_INFO_FF),
    }
        

class PORT_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('PortInfo', PORTINFO),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbMonitorData', DWORD),	('pMonitorData', PTR_DWORD),

    )
        

class PRINTERINFO(NDRUNION):
    union = {
        0: ('pPrinterInfoStress',PRINTER_INFO_STRESS),1: ('pPrinterInfo1',PRINTER_INFO_1),2: ('pPrinterInfo2',PRINTER_INFO_2),3: ('pPrinterInfo3',PRINTER_INFO_3),4: ('pPrinterInfo4',PRINTER_INFO_4),5: ('pPrinterInfo5',PRINTER_INFO_5),6: ('pPrinterInfo6',PRINTER_INFO_6),7: ('pPrinterInfo7',PRINTER_INFO_7),8: ('pPrinterInfo8',PRINTER_INFO_8),9: ('pPrinterInfo9',PRINTER_INFO_9),
    }
        

class PRINTER_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('PrinterInfo', PRINTERINFO),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbBuf', DWORD),	('pszString', PTR_DWORD),

    )
        

class U(NDRUNION):
    union = {
        BIDI_NULL: ('bData',INT),BIDI_INT: ('iData',LONG),BIDI_STRING: ('sData',WCHAR_T),BIDI_FLOAT: ('fData',FLOAT),BIDI_BLOB: ('biData',RPC_BINARY_CONTAINER),
    }
        

class RPC_BIDI_DATA(NDRSTRUCT):
    structure = (
        ('dwBidiType', DWORD),('u', U),
    )


class RPC_BIDI_REQUEST_DATA(NDRSTRUCT):
    structure = (
        ('dwReqNumber', DWORD),('pSchema', WCHAR_T),('data', RPC_BIDI_DATA),
    )


class RPC_BIDI_RESPONSE_DATA(NDRSTRUCT):
    structure = (
        ('dwResult', DWORD),('dwReqNumber', DWORD),('pSchema', WCHAR_T),('data', RPC_BIDI_DATA),
    )


class RPC_BIDI_REQUEST_CONTAINER(NDRSTRUCT):
    structure = (
        ('Version', DWORD),('Flags', DWORD),('Count', DWORD),('aData', RPC_BIDI_REQUEST_DATA),
    )


class RPC_BIDI_RESPONSE_CONTAINER(NDRSTRUCT):
    structure = (
        ('Version', DWORD),('Flags', DWORD),('Count', DWORD),('aData', RPC_BIDI_RESPONSE_DATA),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbBuf', DWORD),	('pSecurity', PTR_DWORD),

    )
        

class CLIENTINFO(NDRUNION):
    union = {
        1: ('pClientInfo1',SPLCLIENT_INFO_1),2: ('pNotUsed',SPLCLIENT_INFO_2),3: ('pClientInfo3',SPLCLIENT_INFO_3),
    }
        

class SPLCLIENT_CONTAINER(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('ClientInfo', CLIENTINFO),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = WCHAR

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbBuf', DWORD),	('pszString', PTR_DWORD),

    )
        

class SYSTEMTIME_CONTAINER(NDRSTRUCT):
    structure = (
        ('cbBuf', DWORD),('pSystemTime', SYSTEMTIME),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = UNSIGNED_SHORT

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('Type', UNSIGNED_SHORT),	('Reserved0', UNSIGNED_SHORT),	('Reserved1', DWORD),	('Reserved2', DWORD),	('Count', DWORD),	('pFields', PTR_DWORD),

    )
        

class DATA_DWORD(NDRUniConformantArray):
    item = RPC_V2_NOTIFY_OPTIONS_TYPE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('Version', DWORD),	('Reserved', DWORD),	('Count', DWORD),	('pTypes', PTR_DWORD),

    )
        

class RPC_V2_NOTIFY_INFO_DATA_DATA(NDRUNION):
    union = {
        TABLE_STRING: ('String',STRING_CONTAINER),TABLE_DWORD: ('dwData',DWORD),TABLE_TIME: ('SystemTime',SYSTEMTIME_CONTAINER),TABLE_DEVMODE: ('DevMode',DEVMODE_CONTAINER),TABLE_SECURITYDESCRIPTOR: ('SecurityDescriptor',SECURITY_CONTAINER),
    }
        

class RPC_V2_NOTIFY_INFO_DATA(NDRSTRUCT):
    structure = (
        ('Type', UNSIGNED_SHORT),('Field', UNSIGNED_SHORT),('Reserved', DWORD),('Id', DWORD),('Data', RPC_V2_NOTIFY_INFO_DATA_DATA),
    )


class RPC_V2_NOTIFY_INFO(NDRSTRUCT):
    structure = (
        ('Version', DWORD),('Flags', DWORD),('Count', DWORD),('aData', RPC_V2_NOTIFY_INFO_DATA),
    )


class RPC_V2_UREPLY_PRINTER(NDRUNION):
    union = {
        0: ('pInfo',RPC_V2_NOTIFY_INFO),
    }
        

class RPC_BRANCHOFFICEJOBDATAPRINTED(NDRSTRUCT):
    structure = (
        ('Status', DWORD),('pDocumentName', WCHAR_T),('pUserName', WCHAR_T),('pMachineName', WCHAR_T),('pPrinterName', WCHAR_T),('pPortName', WCHAR_T),('Size', LONGLONG),('TotalPages', DWORD),
    )


class RPC_BRANCHOFFICEJOBDATARENDERED(NDRSTRUCT):
    structure = (
        ('Size', LONGLONG),('ICMMethod', DWORD),('Color', SHORT),('PrintQuality', SHORT),('YResolution', SHORT),('Copies', SHORT),('TTOption', SHORT),
    )


class RPC_BRANCHOFFICEJOBDATAERROR(NDRSTRUCT):
    structure = (
        ('LastError', DWORD),('pDocumentName', WCHAR_T),('pUserName', WCHAR_T),('pPrinterName', WCHAR_T),('pDataType', WCHAR_T),('TotalSize', LONGLONG),('PrintedSize', LONGLONG),('TotalPages', DWORD),('PrintedPages', DWORD),('pMachineName', WCHAR_T),('pJobError', WCHAR_T),('pErrorDescription', WCHAR_T),
    )


class RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED(NDRSTRUCT):
    structure = (
        ('pDocumentName', WCHAR_T),('pPrinterName', WCHAR_T),('pExtraErrorInfo', WCHAR_T),
    )


class RPC_BRANCHOFFICELOGOFFLINEFILEFULL(NDRSTRUCT):
    structure = (
        ('pMachineName', WCHAR_T),
    )


class JOBINFO(NDRUNION):
    union = {
        kLogJobPrinted: ('LogJobPrinted',RPC_BRANCHOFFICEJOBDATAPRINTED),kLogJobRendered: ('LogJobRendered',RPC_BRANCHOFFICEJOBDATARENDERED),kLogJobError: ('LogJobError',RPC_BRANCHOFFICEJOBDATAERROR),kLogJobPipelineError: ('LogPipelineFailed',RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED),kLogOfflineFileFull: ('LogOfflineFileFull',RPC_BRANCHOFFICELOGOFFLINEFILEFULL),
    }
        

class RPC_BRANCHOFFICEJOBDATA(NDRSTRUCT):
    structure = (
        ('eEventType', EBRANCHOFFICEJOBEVENTTYPE),('JobId', DWORD),('JobInfo', JOBINFO),
    )


class RPC_BRANCHOFFICEJOBDATACONTAINER(NDRSTRUCT):
    structure = (
        ('cJobDataEntries', DWORD),('JobData', RPC_BRANCHOFFICEJOBDATA),
    )


kPropertyTypeString = 1,
kPropertyTypeInt32 = 1,
kPropertyTypeInt64 = 1,
kPropertyTypeByte = 1,
kPropertyTypeTime = 1,
kPropertyTypeDevMode = 1,
kPropertyTypeSD = 1,
kPropertyTypeNotificationReply = 1,
kPropertyTypeNotificationOptions = 1
        
RMTNTFY_HANDLE = VOID

class NOTIFY_REPLY_CONTAINER(NDRSTRUCT):
    structure = (
        ('pInfo', RPC_V2_NOTIFY_INFO),
    )


class NOTIFY_OPTIONS_CONTAINER(NDRSTRUCT):
    structure = (
        ('pOptions', RPC_V2_NOTIFY_OPTIONS),
    )


class VALUE(NDRUNION):
    union = {
        kPropertyTypeString: ('propertyString',WCHAR_T),kPropertyTypeInt32: ('propertyInt32',LONG),kPropertyTypeInt64: ('propertyInt64',__INT64),kPropertyTypeByte: ('propertyByte',BYTE),kPropertyTypeTime: ('propertyTimeContainer',SYSTEMTIME_CONTAINER),kPropertyTypeDevMode: ('propertyDevModeContainer',DEVMODE_CONTAINER),kPropertyTypeSD: ('propertySDContainer',SECURITY_CONTAINER),kPropertyTypeNotificationReply: ('propertyReplyContainer',NOTIFY_REPLY_CONTAINER),kPropertyTypeNotificationOptions: ('propertyOptionsContainer',NOTIFY_OPTIONS_CONTAINER),
    }
        

class RPCPRINTPROPERTYVALUE(NDRSTRUCT):
    structure = (
        ('ePropertyType', EPRINTPROPERTYTYPE),('value', VALUE),
    )


class RPCPRINTNAMEDPROPERTY(NDRSTRUCT):
    structure = (
        ('propertyName', WCHAR_T),('propertyValue', RPCPRINTPROPERTYVALUE),
    )


class DATA_UNSIGNED_LONG(NDRUniConformantArray):
    item = RPCPRINTNAMEDPROPERTY

class PTR_UNSIGNED_LONG(NDRPOINTER):
    referent = (
        ('Data', DATA_UNSIGNED_LONG),
    )

class UNSIGNED_LONG(NDRSTRUCT):
    structure = (
	('numberOfProperties', UNSIGNED_LONG),	('propertiesCollection', PTR_UNSIGNED_LONG),

    )
        

class CORE_PRINTER_DRIVER(NDRSTRUCT):
    structure = (
        ('CoreDriverGUID', GUID),('ftDriverDate', FILETIME),('dwlDriverVersion', DWORDLONG),('szPackageID', WCHAR_T),
    )


class DATA_DWORD(NDRUniConformantArray):
    item = BYTE

class PTR_DWORD(NDRPOINTER):
    referent = (
        ('Data', DATA_DWORD),
    )

class DWORD(NDRSTRUCT):
    structure = (
	('cbBuf', DWORD),	('pBuf', PTR_DWORD),

    )
        

class VALUE(NDRUNION):
    union = {
        kRpcPropertyTypeString: ('propertyString',WCHAR_T),kRpcPropertyTypeInt32: ('propertyInt32',LONG),kRpcPropertyTypeInt64: ('propertyInt64',LONGLONG),kRpcPropertyTypeByte: ('propertyByte',BYTE),kRpcPropertyTypeBuffer: ('propertyBlob',PROPERTYBLOB),
    }
        

class RPC_PRINTPROPERTYVALUE(NDRSTRUCT):
    structure = (
        ('ePropertyType', RPC_EPRINTPROPERTYTYPE),('value', VALUE),
    )


class RPC_PRINTNAMEDPROPERTY(NDRSTRUCT):
    structure = (
        ('propertyName', WCHAR_T),('propertyValue', RPC_PRINTPROPERTYVALUE),
    )


class RpcAsyncOpenPrinter(NDRCALL):
    opnum = 0
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pPrinterName', WCHAR_T),
		('pDatatype', WCHAR_T),
		('pDevModeContainer', DEVMODE_CONTAINER),
		('AccessRequired', DWORD),
		('pClientInfo', SPLCLIENT_CONTAINER),
    )

class RpcAsyncOpenPrinterResponse(NDRCALL):
    structure = (
		('pHandle', PRINTER_HANDLE),
    )
        

class RpcAsyncAddPrinter(NDRCALL):
    opnum = 1
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pPrinterContainer', PRINTER_CONTAINER),
		('pDevModeContainer', DEVMODE_CONTAINER),
		('pSecurityContainer', SECURITY_CONTAINER),
		('pClientInfo', SPLCLIENT_CONTAINER),
    )

class RpcAsyncAddPrinterResponse(NDRCALL):
    structure = (
		('pHandle', PRINTER_HANDLE),
    )
        

class RpcAsyncSetJob(NDRCALL):
    opnum = 2
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
		('pJobContainer', JOB_CONTAINER),
		('Command', DWORD),
    )

class RpcAsyncSetJobResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncGetJob(NDRCALL):
    opnum = 3
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
		('Level', DWORD),
		('pJob', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncGetJobResponse(NDRCALL):
    structure = (
		('pJob', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncEnumJobs(NDRCALL):
    opnum = 4
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('FirstJob', DWORD),
		('NoJobs', DWORD),
		('Level', DWORD),
		('pJob', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumJobsResponse(NDRCALL):
    structure = (
		('pJob', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncAddJob(NDRCALL):
    opnum = 5
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('Level', DWORD),
		('pAddJob', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncAddJobResponse(NDRCALL):
    structure = (
		('pAddJob', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncScheduleJob(NDRCALL):
    opnum = 6
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
    )

class RpcAsyncScheduleJobResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePrinter(NDRCALL):
    opnum = 7
    structure = (
		('hPrinter', PRINTER_HANDLE),
    )

class RpcAsyncDeletePrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncSetPrinter(NDRCALL):
    opnum = 8
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pPrinterContainer', PRINTER_CONTAINER),
		('pDevModeContainer', DEVMODE_CONTAINER),
		('pSecurityContainer', SECURITY_CONTAINER),
		('Command', DWORD),
    )

class RpcAsyncSetPrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncGetPrinter(NDRCALL):
    opnum = 9
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('Level', DWORD),
		('pPrinter', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncGetPrinterResponse(NDRCALL):
    structure = (
		('pPrinter', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncStartDocPrinter(NDRCALL):
    opnum = 10
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pDocInfoContainer', DOC_INFO_CONTAINER),
    )

class RpcAsyncStartDocPrinterResponse(NDRCALL):
    structure = (
		('pJobId', DWORD),
    )
        

class RpcAsyncStartPagePrinter(NDRCALL):
    opnum = 11
    structure = (
		('hPrinter', PRINTER_HANDLE),
    )

class RpcAsyncStartPagePrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncWritePrinter(NDRCALL):
    opnum = 12
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pBuf', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncWritePrinterResponse(NDRCALL):
    structure = (
		('pcWritten', DWORD),
    )
        

class RpcAsyncEndPagePrinter(NDRCALL):
    opnum = 13
    structure = (
		('hPrinter', PRINTER_HANDLE),
    )

class RpcAsyncEndPagePrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEndDocPrinter(NDRCALL):
    opnum = 14
    structure = (
		('hPrinter', PRINTER_HANDLE),
    )

class RpcAsyncEndDocPrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncAbortPrinter(NDRCALL):
    opnum = 15
    structure = (
		('hPrinter', PRINTER_HANDLE),
    )

class RpcAsyncAbortPrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncGetPrinterData(NDRCALL):
    opnum = 16
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pValueName', WCHAR_T),
		('nSize', DWORD),
    )

class RpcAsyncGetPrinterDataResponse(NDRCALL):
    structure = (
		('pType', DWORD),
		('pData', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncGetPrinterDataEx(NDRCALL):
    opnum = 17
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
		('pValueName', CONST_WCHAR_T),
		('nSize', DWORD),
    )

class RpcAsyncGetPrinterDataExResponse(NDRCALL):
    structure = (
		('pType', DWORD),
		('pData', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncSetPrinterData(NDRCALL):
    opnum = 18
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pValueName', WCHAR_T),
		('Type', DWORD),
		('pData', UNSIGNED_CHAR),
		('cbData', DWORD),
    )

class RpcAsyncSetPrinterDataResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncSetPrinterDataEx(NDRCALL):
    opnum = 19
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
		('pValueName', CONST_WCHAR_T),
		('Type', DWORD),
		('pData', UNSIGNED_CHAR),
		('cbData', DWORD),
    )

class RpcAsyncSetPrinterDataExResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncClosePrinter(NDRCALL):
    opnum = 20
    structure = (
		('phPrinter', PRINTER_HANDLE),
    )

class RpcAsyncClosePrinterResponse(NDRCALL):
    structure = (
		('phPrinter', PRINTER_HANDLE),
    )
        

class RpcAsyncAddForm(NDRCALL):
    opnum = 21
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pFormInfoContainer', FORM_CONTAINER),
    )

class RpcAsyncAddFormResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeleteForm(NDRCALL):
    opnum = 22
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pFormName', WCHAR_T),
    )

class RpcAsyncDeleteFormResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncGetForm(NDRCALL):
    opnum = 23
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pFormName', WCHAR_T),
		('Level', DWORD),
		('pForm', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncGetFormResponse(NDRCALL):
    structure = (
		('pForm', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncSetForm(NDRCALL):
    opnum = 24
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pFormName', WCHAR_T),
		('pFormInfoContainer', FORM_CONTAINER),
    )

class RpcAsyncSetFormResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumForms(NDRCALL):
    opnum = 25
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('Level', DWORD),
		('pForm', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumFormsResponse(NDRCALL):
    structure = (
		('pForm', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncGetPrinterDriver(NDRCALL):
    opnum = 26
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pEnvironment', WCHAR_T),
		('Level', DWORD),
		('pDriver', UNSIGNED_CHAR),
		('cbBuf', DWORD),
		('dwClientMajorVersion', DWORD),
		('dwClientMinorVersion', DWORD),
    )

class RpcAsyncGetPrinterDriverResponse(NDRCALL):
    structure = (
		('pDriver', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pdwServerMaxVersion', DWORD),
		('pdwServerMinVersion', DWORD),
    )
        

class RpcAsyncEnumPrinterData(NDRCALL):
    opnum = 27
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('dwIndex', DWORD),
		('cbValueName', DWORD),
		('cbData', DWORD),
    )

class RpcAsyncEnumPrinterDataResponse(NDRCALL):
    structure = (
		('pValueName', WCHAR_T),
		('pcbValueName', DWORD),
		('pType', DWORD),
		('pData', UNSIGNED_CHAR),
		('pcbData', DWORD),
    )
        

class RpcAsyncEnumPrinterDataEx(NDRCALL):
    opnum = 28
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
		('cbEnumValues', DWORD),
    )

class RpcAsyncEnumPrinterDataExResponse(NDRCALL):
    structure = (
		('pEnumValues', UNSIGNED_CHAR),
		('pcbEnumValues', DWORD),
		('pnEnumValues', DWORD),
    )
        

class RpcAsyncEnumPrinterKey(NDRCALL):
    opnum = 29
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
		('cbSubkey', DWORD),
    )

class RpcAsyncEnumPrinterKeyResponse(NDRCALL):
    structure = (
		('pSubkey', WCHAR_T),
		('pcbSubkey', DWORD),
    )
        

class RpcAsyncDeletePrinterData(NDRCALL):
    opnum = 30
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pValueName', WCHAR_T),
    )

class RpcAsyncDeletePrinterDataResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePrinterDataEx(NDRCALL):
    opnum = 31
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
		('pValueName', CONST_WCHAR_T),
    )

class RpcAsyncDeletePrinterDataExResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePrinterKey(NDRCALL):
    opnum = 32
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pKeyName', CONST_WCHAR_T),
    )

class RpcAsyncDeletePrinterKeyResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncXcvData(NDRCALL):
    opnum = 33
    structure = (
		('hXcv', PRINTER_HANDLE),
		('pszDataName', CONST_WCHAR_T),
		('pInputData', UNSIGNED_CHAR),
		('cbInputData', DWORD),
		('cbOutputData', DWORD),
		('pdwStatus', DWORD),
    )

class RpcAsyncXcvDataResponse(NDRCALL):
    structure = (
		('pOutputData', UNSIGNED_CHAR),
		('pcbOutputNeeded', DWORD),
		('pdwStatus', DWORD),
    )
        

class RpcAsyncSendRecvBidiData(NDRCALL):
    opnum = 34
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pAction', CONST_WCHAR_T),
		('pReqData', RPC_BIDI_REQUEST_CONTAINER),
    )

class RpcAsyncSendRecvBidiDataResponse(NDRCALL):
    structure = (
		('ppRespData', RPC_BIDI_RESPONSE_CONTAINER),
    )
        

class RpcAsyncCreatePrinterIC(NDRCALL):
    opnum = 35
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pDevModeContainer', DEVMODE_CONTAINER),
    )

class RpcAsyncCreatePrinterICResponse(NDRCALL):
    structure = (
		('pHandle', GDI_HANDLE),
    )
        

class RpcAsyncPlayGdiScriptOnPrinterIC(NDRCALL):
    opnum = 36
    structure = (
		('hPrinterIC', GDI_HANDLE),
		('pIn', UNSIGNED_CHAR),
		('cIn', DWORD),
		('cOut', DWORD),
		('ul', DWORD),
    )

class RpcAsyncPlayGdiScriptOnPrinterICResponse(NDRCALL):
    structure = (
		('pOut', UNSIGNED_CHAR),
    )
        

class RpcAsyncDeletePrinterIC(NDRCALL):
    opnum = 37
    structure = (
		('phPrinterIC', GDI_HANDLE),
    )

class RpcAsyncDeletePrinterICResponse(NDRCALL):
    structure = (
		('phPrinterIC', GDI_HANDLE),
    )
        

class RpcAsyncEnumPrinters(NDRCALL):
    opnum = 38
    structure = (
		('hRemoteBinding', HANDLE_T),
		('Flags', DWORD),
		('Name', WCHAR_T),
		('Level', DWORD),
		('pPrinterEnum', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPrintersResponse(NDRCALL):
    structure = (
		('pPrinterEnum', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncAddPrinterDriver(NDRCALL):
    opnum = 39
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pDriverContainer', DRIVER_CONTAINER),
		('dwFileCopyFlags', DWORD),
    )

class RpcAsyncAddPrinterDriverResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumPrinterDrivers(NDRCALL):
    opnum = 40
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('Level', DWORD),
		('pDrivers', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPrinterDriversResponse(NDRCALL):
    structure = (
		('pDrivers', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncGetPrinterDriverDirectory(NDRCALL):
    opnum = 41
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('Level', DWORD),
		('pDriverDirectory', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncGetPrinterDriverDirectoryResponse(NDRCALL):
    structure = (
		('pDriverDirectory', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncDeletePrinterDriver(NDRCALL):
    opnum = 42
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('pDriverName', WCHAR_T),
    )

class RpcAsyncDeletePrinterDriverResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePrinterDriverEx(NDRCALL):
    opnum = 43
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('pDriverName', WCHAR_T),
		('dwDeleteFlag', DWORD),
		('dwVersionNum', DWORD),
    )

class RpcAsyncDeletePrinterDriverExResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncAddPrintProcessor(NDRCALL):
    opnum = 44
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('pPathName', WCHAR_T),
		('pPrintProcessorName', WCHAR_T),
    )

class RpcAsyncAddPrintProcessorResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumPrintProcessors(NDRCALL):
    opnum = 45
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('Level', DWORD),
		('pPrintProcessorInfo', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPrintProcessorsResponse(NDRCALL):
    structure = (
		('pPrintProcessorInfo', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncGetPrintProcessorDirectory(NDRCALL):
    opnum = 46
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('Level', DWORD),
		('pPrintProcessorDirectory', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncGetPrintProcessorDirectoryResponse(NDRCALL):
    structure = (
		('pPrintProcessorDirectory', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
    )
        

class RpcAsyncEnumPorts(NDRCALL):
    opnum = 47
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('Level', DWORD),
		('pPort', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPortsResponse(NDRCALL):
    structure = (
		('pPort', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncEnumMonitors(NDRCALL):
    opnum = 48
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('Level', DWORD),
		('pMonitor', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumMonitorsResponse(NDRCALL):
    structure = (
		('pMonitor', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncAddPort(NDRCALL):
    opnum = 49
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pPortContainer', PORT_CONTAINER),
		('pPortVarContainer', PORT_VAR_CONTAINER),
		('pMonitorName', WCHAR_T),
    )

class RpcAsyncAddPortResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncSetPort(NDRCALL):
    opnum = 50
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pPortName', WCHAR_T),
		('pPortContainer', PORT_CONTAINER),
    )

class RpcAsyncSetPortResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncAddMonitor(NDRCALL):
    opnum = 51
    structure = (
		('hRemoteBinding', HANDLE_T),
		('Name', WCHAR_T),
		('pMonitorContainer', MONITOR_CONTAINER),
    )

class RpcAsyncAddMonitorResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeleteMonitor(NDRCALL):
    opnum = 52
    structure = (
		('hRemoteBinding', HANDLE_T),
		('Name', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('pMonitorName', WCHAR_T),
    )

class RpcAsyncDeleteMonitorResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePrintProcessor(NDRCALL):
    opnum = 53
    structure = (
		('hRemoteBinding', HANDLE_T),
		('Name', WCHAR_T),
		('pEnvironment', WCHAR_T),
		('pPrintProcessorName', WCHAR_T),
    )

class RpcAsyncDeletePrintProcessorResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumPrintProcessorDatatypes(NDRCALL):
    opnum = 54
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pName', WCHAR_T),
		('pPrintProcessorName', WCHAR_T),
		('Level', DWORD),
		('pDatatypes', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPrintProcessorDatatypesResponse(NDRCALL):
    structure = (
		('pDatatypes', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcAsyncAddPerMachineConnection(NDRCALL):
    opnum = 55
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pServer', WCHAR_T),
		('pPrinterName', CONST_WCHAR_T),
		('pPrintServer', CONST_WCHAR_T),
		('pProvider', CONST_WCHAR_T),
    )

class RpcAsyncAddPerMachineConnectionResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeletePerMachineConnection(NDRCALL):
    opnum = 56
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pServer', WCHAR_T),
		('pPrinterName', CONST_WCHAR_T),
    )

class RpcAsyncDeletePerMachineConnectionResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumPerMachineConnections(NDRCALL):
    opnum = 57
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pServer', WCHAR_T),
		('pPrinterEnum', UNSIGNED_CHAR),
		('cbBuf', DWORD),
    )

class RpcAsyncEnumPerMachineConnectionsResponse(NDRCALL):
    structure = (
		('pPrinterEnum', UNSIGNED_CHAR),
		('pcbNeeded', DWORD),
		('pcReturned', DWORD),
    )
        

class RpcSyncRegisterForRemoteNotifications(NDRCALL):
    opnum = 58
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pNotifyFilter', RPCPRINTPROPERTIESCOLLECTION),
    )

class RpcSyncRegisterForRemoteNotificationsResponse(NDRCALL):
    structure = (
		('phRpcHandle', RMTNTFY_HANDLE),
    )
        

class RpcSyncUnRegisterForRemoteNotifications(NDRCALL):
    opnum = 59
    structure = (
		('phRpcHandle', RMTNTFY_HANDLE),
    )

class RpcSyncUnRegisterForRemoteNotificationsResponse(NDRCALL):
    structure = (
		('phRpcHandle', RMTNTFY_HANDLE),
    )
        

class RpcSyncRefreshRemoteNotifications(NDRCALL):
    opnum = 60
    structure = (
		('hRpcHandle', RMTNTFY_HANDLE),
		('pNotifyFilter', RPCPRINTPROPERTIESCOLLECTION),
    )

class RpcSyncRefreshRemoteNotificationsResponse(NDRCALL):
    structure = (
		('ppNotifyData', RPCPRINTPROPERTIESCOLLECTION),
    )
        

class RpcAsyncGetRemoteNotifications(NDRCALL):
    opnum = 61
    structure = (
		('hRpcHandle', RMTNTFY_HANDLE),
    )

class RpcAsyncGetRemoteNotificationsResponse(NDRCALL):
    structure = (
		('ppNotifyData', RPCPRINTPROPERTIESCOLLECTION),
    )
        

class RpcAsyncInstallPrinterDriverFromPackage(NDRCALL):
    opnum = 62
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszInfPath', CONST_WCHAR_T),
		('pszDriverName', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
		('dwFlags', DWORD),
    )

class RpcAsyncInstallPrinterDriverFromPackageResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncUploadPrinterDriverPackage(NDRCALL):
    opnum = 63
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszInfPath', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
		('dwFlags', DWORD),
		('pszDestInfPath', WCHAR_T),
		('pcchDestInfPath', DWORD),
    )

class RpcAsyncUploadPrinterDriverPackageResponse(NDRCALL):
    structure = (
		('pszDestInfPath', WCHAR_T),
		('pcchDestInfPath', DWORD),
    )
        

class RpcAsyncGetCorePrinterDrivers(NDRCALL):
    opnum = 64
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
		('cchCoreDrivers', DWORD),
		('pszzCoreDriverDependencies', CONST_WCHAR_T),
		('cCorePrinterDrivers', DWORD),
    )

class RpcAsyncGetCorePrinterDriversResponse(NDRCALL):
    structure = (
		('pCorePrinterDrivers', CORE_PRINTER_DRIVER),
    )
        

class RpcAsyncCorePrinterDriverInstalled(NDRCALL):
    opnum = 65
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
		('CoreDriverGUID', GUID),
		('ftDriverDate', FILETIME),
		('dwlDriverVersion', DWORDLONG),
    )

class RpcAsyncCorePrinterDriverInstalledResponse(NDRCALL):
    structure = (
		('pbDriverInstalled', INT),
    )
        

class RpcAsyncGetPrinterDriverPackagePath(NDRCALL):
    opnum = 66
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
		('pszLanguage', CONST_WCHAR_T),
		('pszPackageID', CONST_WCHAR_T),
		('pszDriverPackageCab', WCHAR_T),
		('cchDriverPackageCab', DWORD),
    )

class RpcAsyncGetPrinterDriverPackagePathResponse(NDRCALL):
    structure = (
		('pszDriverPackageCab', WCHAR_T),
		('pcchRequiredSize', DWORD),
    )
        

class RpcAsyncDeletePrinterDriverPackage(NDRCALL):
    opnum = 67
    structure = (
		('hRemoteBinding', HANDLE_T),
		('pszServer', CONST_WCHAR_T),
		('pszInfPath', CONST_WCHAR_T),
		('pszEnvironment', CONST_WCHAR_T),
    )

class RpcAsyncDeletePrinterDriverPackageResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncReadPrinter(NDRCALL):
    opnum = 68
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('cbBuf', DWORD),
    )

class RpcAsyncReadPrinterResponse(NDRCALL):
    structure = (
		('pBuf', UNSIGNED_CHAR),
		('pcNoBytesRead', DWORD),
    )
        

class RpcAsyncResetPrinter(NDRCALL):
    opnum = 69
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pDatatype', WCHAR_T),
		('pDevModeContainer', DEVMODE_CONTAINER),
    )

class RpcAsyncResetPrinterResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncGetJobNamedPropertyValue(NDRCALL):
    opnum = 70
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
		('pszName', CONST_WCHAR_T),
    )

class RpcAsyncGetJobNamedPropertyValueResponse(NDRCALL):
    structure = (
		('pValue', RPC_PRINTPROPERTYVALUE),
    )
        

class RpcAsyncSetJobNamedProperty(NDRCALL):
    opnum = 71
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
		('pProperty', RPC_PRINTNAMEDPROPERTY),
    )

class RpcAsyncSetJobNamedPropertyResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncDeleteJobNamedProperty(NDRCALL):
    opnum = 72
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
		('pszName', CONST_WCHAR_T),
    )

class RpcAsyncDeleteJobNamedPropertyResponse(NDRCALL):
    structure = (

    )
        

class RpcAsyncEnumJobNamedProperties(NDRCALL):
    opnum = 73
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('JobId', DWORD),
    )

class RpcAsyncEnumJobNamedPropertiesResponse(NDRCALL):
    structure = (
		('pcProperties', DWORD),
		('ppProperties', RPC_PRINTNAMEDPROPERTY),
    )
        

class RpcAsyncLogJobInfoForBranchOffice(NDRCALL):
    opnum = 74
    structure = (
		('hPrinter', PRINTER_HANDLE),
		('pBranchOfficeJobDataContainer', RPC_BRANCHOFFICEJOBDATACONTAINER),
    )

class RpcAsyncLogJobInfoForBranchOfficeResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (RpcAsyncOpenPrinter,RpcAsyncOpenPrinterResponse),
1 : (RpcAsyncAddPrinter,RpcAsyncAddPrinterResponse),
2 : (RpcAsyncSetJob,RpcAsyncSetJobResponse),
3 : (RpcAsyncGetJob,RpcAsyncGetJobResponse),
4 : (RpcAsyncEnumJobs,RpcAsyncEnumJobsResponse),
5 : (RpcAsyncAddJob,RpcAsyncAddJobResponse),
6 : (RpcAsyncScheduleJob,RpcAsyncScheduleJobResponse),
7 : (RpcAsyncDeletePrinter,RpcAsyncDeletePrinterResponse),
8 : (RpcAsyncSetPrinter,RpcAsyncSetPrinterResponse),
9 : (RpcAsyncGetPrinter,RpcAsyncGetPrinterResponse),
10 : (RpcAsyncStartDocPrinter,RpcAsyncStartDocPrinterResponse),
11 : (RpcAsyncStartPagePrinter,RpcAsyncStartPagePrinterResponse),
12 : (RpcAsyncWritePrinter,RpcAsyncWritePrinterResponse),
13 : (RpcAsyncEndPagePrinter,RpcAsyncEndPagePrinterResponse),
14 : (RpcAsyncEndDocPrinter,RpcAsyncEndDocPrinterResponse),
15 : (RpcAsyncAbortPrinter,RpcAsyncAbortPrinterResponse),
16 : (RpcAsyncGetPrinterData,RpcAsyncGetPrinterDataResponse),
17 : (RpcAsyncGetPrinterDataEx,RpcAsyncGetPrinterDataExResponse),
18 : (RpcAsyncSetPrinterData,RpcAsyncSetPrinterDataResponse),
19 : (RpcAsyncSetPrinterDataEx,RpcAsyncSetPrinterDataExResponse),
20 : (RpcAsyncClosePrinter,RpcAsyncClosePrinterResponse),
21 : (RpcAsyncAddForm,RpcAsyncAddFormResponse),
22 : (RpcAsyncDeleteForm,RpcAsyncDeleteFormResponse),
23 : (RpcAsyncGetForm,RpcAsyncGetFormResponse),
24 : (RpcAsyncSetForm,RpcAsyncSetFormResponse),
25 : (RpcAsyncEnumForms,RpcAsyncEnumFormsResponse),
26 : (RpcAsyncGetPrinterDriver,RpcAsyncGetPrinterDriverResponse),
27 : (RpcAsyncEnumPrinterData,RpcAsyncEnumPrinterDataResponse),
28 : (RpcAsyncEnumPrinterDataEx,RpcAsyncEnumPrinterDataExResponse),
29 : (RpcAsyncEnumPrinterKey,RpcAsyncEnumPrinterKeyResponse),
30 : (RpcAsyncDeletePrinterData,RpcAsyncDeletePrinterDataResponse),
31 : (RpcAsyncDeletePrinterDataEx,RpcAsyncDeletePrinterDataExResponse),
32 : (RpcAsyncDeletePrinterKey,RpcAsyncDeletePrinterKeyResponse),
33 : (RpcAsyncXcvData,RpcAsyncXcvDataResponse),
34 : (RpcAsyncSendRecvBidiData,RpcAsyncSendRecvBidiDataResponse),
35 : (RpcAsyncCreatePrinterIC,RpcAsyncCreatePrinterICResponse),
36 : (RpcAsyncPlayGdiScriptOnPrinterIC,RpcAsyncPlayGdiScriptOnPrinterICResponse),
37 : (RpcAsyncDeletePrinterIC,RpcAsyncDeletePrinterICResponse),
38 : (RpcAsyncEnumPrinters,RpcAsyncEnumPrintersResponse),
39 : (RpcAsyncAddPrinterDriver,RpcAsyncAddPrinterDriverResponse),
40 : (RpcAsyncEnumPrinterDrivers,RpcAsyncEnumPrinterDriversResponse),
41 : (RpcAsyncGetPrinterDriverDirectory,RpcAsyncGetPrinterDriverDirectoryResponse),
42 : (RpcAsyncDeletePrinterDriver,RpcAsyncDeletePrinterDriverResponse),
43 : (RpcAsyncDeletePrinterDriverEx,RpcAsyncDeletePrinterDriverExResponse),
44 : (RpcAsyncAddPrintProcessor,RpcAsyncAddPrintProcessorResponse),
45 : (RpcAsyncEnumPrintProcessors,RpcAsyncEnumPrintProcessorsResponse),
46 : (RpcAsyncGetPrintProcessorDirectory,RpcAsyncGetPrintProcessorDirectoryResponse),
47 : (RpcAsyncEnumPorts,RpcAsyncEnumPortsResponse),
48 : (RpcAsyncEnumMonitors,RpcAsyncEnumMonitorsResponse),
49 : (RpcAsyncAddPort,RpcAsyncAddPortResponse),
50 : (RpcAsyncSetPort,RpcAsyncSetPortResponse),
51 : (RpcAsyncAddMonitor,RpcAsyncAddMonitorResponse),
52 : (RpcAsyncDeleteMonitor,RpcAsyncDeleteMonitorResponse),
53 : (RpcAsyncDeletePrintProcessor,RpcAsyncDeletePrintProcessorResponse),
54 : (RpcAsyncEnumPrintProcessorDatatypes,RpcAsyncEnumPrintProcessorDatatypesResponse),
55 : (RpcAsyncAddPerMachineConnection,RpcAsyncAddPerMachineConnectionResponse),
56 : (RpcAsyncDeletePerMachineConnection,RpcAsyncDeletePerMachineConnectionResponse),
57 : (RpcAsyncEnumPerMachineConnections,RpcAsyncEnumPerMachineConnectionsResponse),
58 : (RpcSyncRegisterForRemoteNotifications,RpcSyncRegisterForRemoteNotificationsResponse),
59 : (RpcSyncUnRegisterForRemoteNotifications,RpcSyncUnRegisterForRemoteNotificationsResponse),
60 : (RpcSyncRefreshRemoteNotifications,RpcSyncRefreshRemoteNotificationsResponse),
61 : (RpcAsyncGetRemoteNotifications,RpcAsyncGetRemoteNotificationsResponse),
62 : (RpcAsyncInstallPrinterDriverFromPackage,RpcAsyncInstallPrinterDriverFromPackageResponse),
63 : (RpcAsyncUploadPrinterDriverPackage,RpcAsyncUploadPrinterDriverPackageResponse),
64 : (RpcAsyncGetCorePrinterDrivers,RpcAsyncGetCorePrinterDriversResponse),
65 : (RpcAsyncCorePrinterDriverInstalled,RpcAsyncCorePrinterDriverInstalledResponse),
66 : (RpcAsyncGetPrinterDriverPackagePath,RpcAsyncGetPrinterDriverPackagePathResponse),
67 : (RpcAsyncDeletePrinterDriverPackage,RpcAsyncDeletePrinterDriverPackageResponse),
68 : (RpcAsyncReadPrinter,RpcAsyncReadPrinterResponse),
69 : (RpcAsyncResetPrinter,RpcAsyncResetPrinterResponse),
70 : (RpcAsyncGetJobNamedPropertyValue,RpcAsyncGetJobNamedPropertyValueResponse),
71 : (RpcAsyncSetJobNamedProperty,RpcAsyncSetJobNamedPropertyResponse),
72 : (RpcAsyncDeleteJobNamedProperty,RpcAsyncDeleteJobNamedPropertyResponse),
73 : (RpcAsyncEnumJobNamedProperties,RpcAsyncEnumJobNamedPropertiesResponse),
74 : (RpcAsyncLogJobInfoForBranchOffice,RpcAsyncLogJobInfoForBranchOfficeResponse),
}
