
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
__INT64 = NdrHyper
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
PWCHAR = NdrByte
INT = NdrLong
PVOID = NdrContextHandle
VOID = NdrContextHandle
CONTEXT_HANDLE = NdrContextHandle
PPCONTEXT_HANDLE = NdrContextHandle
LONG = NdrLong
__INT3264 = NdrHyper
UNSIGNED___INT3264 = NdrHyper
UNSIGNED_HYPER = NdrHyper
HYPER = NdrHyper
DWORDLONG = NdrHyper
LONG_PTR = NdrHyper
ULONG_PTR = NdrHyper
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
LANGID = UNSIGNED_SHORT
GDI_HANDLE = VOID
PRINTER_HANDLE = VOID
STRING_HANDLE = WCHAR_T

class SIZE(NdrStructure):
    MEMBERS = [(LONG, "cx"),(LONG, "cy"),]

    

class RECTL(NdrStructure):
    MEMBERS = [(LONG, "left"),(LONG, "top"),(LONG, "right"),(LONG, "bottom"),]

    

class DEVMODE(NdrStructure):
    MEMBERS = [(WCHAR_T, "dmDeviceName"),(UNSIGNED_SHORT, "dmSpecVersion"),(UNSIGNED_SHORT, "dmDriverVersion"),(UNSIGNED_SHORT, "dmSize"),(UNSIGNED_SHORT, "dmDriverExtra"),(DWORD, "dmFields"),(SHORT, "dmOrientation"),(SHORT, "dmPaperSize"),(SHORT, "dmPaperLength"),(SHORT, "dmPaperWidth"),(SHORT, "dmScale"),(SHORT, "dmCopies"),(SHORT, "dmDefaultSource"),(SHORT, "dmPrintQuality"),(SHORT, "dmColor"),(SHORT, "dmDuplex"),(SHORT, "dmYResolution"),(SHORT, "dmTTOption"),(SHORT, "dmCollate"),(WCHAR_T, "dmFormName"),(UNSIGNED_SHORT, "reserved0"),(DWORD, "reserved1"),(DWORD, "reserved2"),(DWORD, "reserved3"),(DWORD, "dmNup"),(DWORD, "reserved4"),(DWORD, "dmICMMethod"),(DWORD, "dmICMIntent"),(DWORD, "dmMediaType"),(DWORD, "dmDitherType"),(DWORD, "reserved5"),(DWORD, "reserved6"),(DWORD, "reserved7"),(DWORD, "reserved8"),]

    

class DOC_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pDocName"),(PWCHAR_T, "pOutputFile"),(PWCHAR_T, "pDatatype"),]

    

class DRIVER_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pName"),]

    

class DRIVER_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "cVersion"),(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDriverPath"),(PWCHAR_T, "pDataFile"),(PWCHAR_T, "pConfigFile"),]

    

class RPC_DRIVER_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "cVersion"),(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDriverPath"),(PWCHAR_T, "pDataFile"),(PWCHAR_T, "pConfigFile"),(PWCHAR_T, "pHelpFile"),(PWCHAR_T, "pMonitorName"),(PWCHAR_T, "pDefaultDataType"),(DWORD, "cchDependentFiles"),(PWCHAR_T, "pDependentFiles"),]

    

class RPC_DRIVER_INFO_4(NdrStructure):
    MEMBERS = [(DWORD, "cVersion"),(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDriverPath"),(PWCHAR_T, "pDataFile"),(PWCHAR_T, "pConfigFile"),(PWCHAR_T, "pHelpFile"),(PWCHAR_T, "pMonitorName"),(PWCHAR_T, "pDefaultDataType"),(DWORD, "cchDependentFiles"),(PWCHAR_T, "pDependentFiles"),(DWORD, "cchPreviousNames"),(PWCHAR_T, "pszzPreviousNames"),]

    

class RPC_DRIVER_INFO_6(NdrStructure):
    MEMBERS = [(DWORD, "cVersion"),(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDriverPath"),(PWCHAR_T, "pDataFile"),(PWCHAR_T, "pConfigFile"),(PWCHAR_T, "pHelpFile"),(PWCHAR_T, "pMonitorName"),(PWCHAR_T, "pDefaultDataType"),(DWORD, "cchDependentFiles"),(PWCHAR_T, "pDependentFiles"),(DWORD, "cchPreviousNames"),(PWCHAR_T, "pszzPreviousNames"),(FILETIME, "ftDriverDate"),(DWORDLONG, "dwlDriverVersion"),(PWCHAR_T, "pMfgName"),(PWCHAR_T, "pOEMUrl"),(PWCHAR_T, "pHardwareID"),(PWCHAR_T, "pProvider"),]

    

class RPC_DRIVER_INFO_8(NdrStructure):
    MEMBERS = [(DWORD, "cVersion"),(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDriverPath"),(PWCHAR_T, "pDataFile"),(PWCHAR_T, "pConfigFile"),(PWCHAR_T, "pHelpFile"),(PWCHAR_T, "pMonitorName"),(PWCHAR_T, "pDefaultDataType"),(DWORD, "cchDependentFiles"),(PWCHAR_T, "pDependentFiles"),(DWORD, "cchPreviousNames"),(PWCHAR_T, "pszzPreviousNames"),(FILETIME, "ftDriverDate"),(DWORDLONG, "dwlDriverVersion"),(PWCHAR_T, "pMfgName"),(PWCHAR_T, "pOEMUrl"),(PWCHAR_T, "pHardwareID"),(PWCHAR_T, "pProvider"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pVendorSetup"),(DWORD, "cchColorProfiles"),(PWCHAR_T, "pszzColorProfiles"),(PWCHAR_T, "pInfPath"),(DWORD, "dwPrinterDriverAttributes"),(DWORD, "cchCoreDependencies"),(PWCHAR_T, "pszzCoreDriverDependencies"),(FILETIME, "ftMinInboxDriverVerDate"),(DWORDLONG, "dwlMinInboxDriverVerVersion"),]

    

class FORM_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(PWCHAR_T, "pName"),(SIZE, "Size"),(RECTL, "ImageableArea"),]

    

class RPC_FORM_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(PWCHAR_T, "pName"),(SIZE, "Size"),(RECTL, "ImageableArea"),(PCHAR, "pKeyword"),(DWORD, "StringType"),(PWCHAR_T, "pMuiDll"),(DWORD, "dwResourceId"),(PWCHAR_T, "pDisplayName"),(LANGID, "wLangID"),]

    

class JOB_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pDocument"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pStatus"),(DWORD, "Status"),(DWORD, "Priority"),(DWORD, "Position"),(DWORD, "TotalPages"),(DWORD, "PagesPrinted"),(SYSTEMTIME, "Submitted"),]

    

class JOB_INFO_2(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pDocument"),(PWCHAR_T, "pNotifyName"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pParameters"),(PWCHAR_T, "pDriverName"),(PDEVMODE, "pDevMode"),(PWCHAR_T, "pStatus"),(PSECURITY_DESCRIPTOR, "pSecurityDescriptor"),(DWORD, "Status"),(DWORD, "Priority"),(DWORD, "Position"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "TotalPages"),(DWORD, "Size"),(SYSTEMTIME, "Submitted"),(DWORD, "Time"),(DWORD, "PagesPrinted"),]

    

class JOB_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(DWORD, "NextJobId"),(DWORD, "Reserved"),]

    

class JOB_INFO_4(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pDocument"),(PWCHAR_T, "pNotifyName"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pParameters"),(PWCHAR_T, "pDriverName"),(PDEVMODE, "pDevMode"),(PWCHAR_T, "pStatus"),(PSECURITY_DESCRIPTOR, "pSecurityDescriptor"),(DWORD, "Status"),(DWORD, "Priority"),(DWORD, "Position"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "TotalPages"),(DWORD, "Size"),(SYSTEMTIME, "Submitted"),(DWORD, "Time"),(DWORD, "PagesPrinted"),(LONG, "SizeHigh"),]

    

class MONITOR_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pName"),]

    

class MONITOR_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pName"),(PWCHAR_T, "pEnvironment"),(PWCHAR_T, "pDLLName"),]

    

class PORT_INFO_1(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPortName"),]

    

class PORT_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPortName"),(PWCHAR_T, "pMonitorName"),(PWCHAR_T, "pDescription"),(DWORD, "fPortType"),(DWORD, "Reserved"),]

    

class PORT_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "dwStatus"),(PWCHAR_T, "pszStatus"),(DWORD, "dwSeverity"),]

    

class PORT_INFO_FF(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPortName"),(DWORD, "cbMonitorData"),(PBYTE, "pMonitorData"),]

    

class PRINTER_INFO_STRESS(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pServerName"),(DWORD, "cJobs"),(DWORD, "cTotalJobs"),(DWORD, "cTotalBytes"),(SYSTEMTIME, "stUpTime"),(DWORD, "MaxcRef"),(DWORD, "cTotalPagesPrinted"),(DWORD, "dwGetVersion"),(DWORD, "fFreeBuild"),(DWORD, "cSpooling"),(DWORD, "cMaxSpooling"),(DWORD, "cRef"),(DWORD, "cErrorOutOfPaper"),(DWORD, "cErrorNotReady"),(DWORD, "cJobError"),(DWORD, "dwNumberOfProcessors"),(DWORD, "dwProcessorType"),(DWORD, "dwHighPartTotalBytes"),(DWORD, "cChangeID"),(DWORD, "dwLastError"),(DWORD, "Status"),(DWORD, "cEnumerateNetworkPrinters"),(DWORD, "cAddNetPrinters"),(UNSIGNED_SHORT, "wProcessorArchitecture"),(UNSIGNED_SHORT, "wProcessorLevel"),(DWORD, "cRefIC"),(DWORD, "dwReserved2"),(DWORD, "dwReserved3"),]

    

class PRINTER_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "Flags"),(PWCHAR_T, "pDescription"),(PWCHAR_T, "pName"),(PWCHAR_T, "pComment"),]

    

class PRINTER_INFO_2(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pServerName"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pShareName"),(PWCHAR_T, "pPortName"),(PWCHAR_T, "pDriverName"),(PWCHAR_T, "pComment"),(PWCHAR_T, "pLocation"),(PDEVMODE, "pDevMode"),(PWCHAR_T, "pSepFile"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pParameters"),(PSECURITY_DESCRIPTOR, "pSecurityDescriptor"),(DWORD, "Attributes"),(DWORD, "Priority"),(DWORD, "DefaultPriority"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "Status"),(DWORD, "cJobs"),(DWORD, "AveragePPM"),]

    

class PRINTER_INFO_3(NdrStructure):
    MEMBERS = [(PSECURITY_DESCRIPTOR, "pSecurityDescriptor"),]

    

class PRINTER_INFO_4(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pServerName"),(DWORD, "Attributes"),]

    

class PRINTER_INFO_5(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pPortName"),(DWORD, "Attributes"),(DWORD, "DeviceNotSelectedTimeout"),(DWORD, "TransmissionRetryTimeout"),]

    

class PRINTER_INFO_6(NdrStructure):
    MEMBERS = [(DWORD, "dwStatus"),]

    

class PRINTER_INFO_7(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszObjectGUID"),(DWORD, "dwAction"),]

    

class PRINTER_INFO_8(NdrStructure):
    MEMBERS = [(PDEVMODE, "pDevMode"),]

    

class PRINTER_INFO_9(NdrStructure):
    MEMBERS = [(PDEVMODE, "pDevMode"),]

    

class SPLCLIENT_INFO_1(NdrStructure):
    MEMBERS = [(DWORD, "dwSize"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(DWORD, "dwBuildNum"),(DWORD, "dwMajorVersion"),(DWORD, "dwMinorVersion"),(UNSIGNED_SHORT, "wProcessorArchitecture"),]

    

class SPLCLIENT_INFO_2(NdrStructure):
    MEMBERS = [(LONG_PTR, "notUsed"),]

    

class SPLCLIENT_INFO_3(NdrStructure):
    MEMBERS = [(UNSIGNED_INT, "cbSize"),(DWORD, "dwFlags"),(DWORD, "dwSize"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(DWORD, "dwBuildNum"),(DWORD, "dwMajorVersion"),(DWORD, "dwMinorVersion"),(UNSIGNED_SHORT, "wProcessorArchitecture"),(UNSIGNED___INT64, "hSplPrinter"),]

    

class DEVMODE_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbBuf"),(PBYTE, "pDevMode"),]

    

class DOC_INFO_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(DOCINFO, "DocInfo"),]

    

class DRIVER_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(DRIVERINFO, "DriverInfo"),]

    

class FORM_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(FORMINFO, "FormInfo"),]

    

class JOB_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(JOBINFO, "JobInfo"),]

    

class MONITOR_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(MONITORINFO, "MonitorInfo"),]

    

class PORT_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(PORTINFO, "PortInfo"),]

    

class PORT_VAR_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbMonitorData"),(PBYTE, "pMonitorData"),]

    

class PRINTER_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(PRINTERINFO, "PrinterInfo"),]

    

class RPC_BINARY_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbBuf"),(PBYTE, "pszString"),]

    

class RPC_BIDI_DATA(NdrStructure):
    MEMBERS = [(DWORD, "dwBidiType"),(U, "u"),]

    

class RPC_BIDI_REQUEST_DATA(NdrStructure):
    MEMBERS = [(DWORD, "dwReqNumber"),(PWCHAR_T, "pSchema"),(RPC_BIDI_DATA, "data"),]

    

class RPC_BIDI_RESPONSE_DATA(NdrStructure):
    MEMBERS = [(DWORD, "dwResult"),(DWORD, "dwReqNumber"),(PWCHAR_T, "pSchema"),(RPC_BIDI_DATA, "data"),]

    

class RPC_BIDI_REQUEST_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "Flags"),(DWORD, "Count"),(RPC_BIDI_REQUEST_DATA, "aData"),]

    

class RPC_BIDI_RESPONSE_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "Flags"),(DWORD, "Count"),(RPC_BIDI_RESPONSE_DATA, "aData"),]

    

class SECURITY_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbBuf"),(PBYTE, "pSecurity"),]

    

class SPLCLIENT_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "Level"),(CLIENTINFO, "ClientInfo"),]

    

class STRING_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbBuf"),(PWCHAR, "pszString"),]

    

class SYSTEMTIME_CONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cbBuf"),(PSYSTEMTIME, "pSystemTime"),]

    

class RPC_V2_NOTIFY_OPTIONS_TYPE(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Type"),(UNSIGNED_SHORT, "Reserved0"),(DWORD, "Reserved1"),(DWORD, "Reserved2"),(DWORD, "Count"),(PUNSIGNED_SHORT, "pFields"),]

    

class RPC_V2_NOTIFY_OPTIONS(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "Reserved"),(DWORD, "Count"),(PRPC_V2_NOTIFY_OPTIONS_TYPE, "pTypes"),]

    

class RPC_V2_NOTIFY_INFO_DATA_DATA(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (STRING_CONTAINER, "String"),2 : (DWORD, "dwData"),3 : (SYSTEMTIME_CONTAINER, "SystemTime"),4 : (DEVMODE_CONTAINER, "DevMode"),5 : (SECURITY_CONTAINER, "SecurityDescriptor"),}

    

class RPC_V2_NOTIFY_INFO_DATA(NdrStructure):
    MEMBERS = [(UNSIGNED_SHORT, "Type"),(UNSIGNED_SHORT, "Field"),(DWORD, "Reserved"),(DWORD, "Id"),(RPC_V2_NOTIFY_INFO_DATA_DATA, "Data"),]

    

class RPC_V2_NOTIFY_INFO(NdrStructure):
    MEMBERS = [(DWORD, "Version"),(DWORD, "Flags"),(DWORD, "Count"),(RPC_V2_NOTIFY_INFO_DATA, "aData"),]

    

class RPC_V2_UREPLY_PRINTER(NdrUnion):
    SWITCHTYPE = DWORD
    MEMBERS = {1 : (PRPC_V2_NOTIFY_INFO, "pInfo"),}

    

class RPC_BRANCHOFFICEJOBDATAPRINTED(NdrStructure):
    MEMBERS = [(DWORD, "Status"),(PWCHAR_T, "pDocumentName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pPortName"),(LONGLONG, "Size"),(DWORD, "TotalPages"),]

    

class RPC_BRANCHOFFICEJOBDATARENDERED(NdrStructure):
    MEMBERS = [(LONGLONG, "Size"),(DWORD, "ICMMethod"),(SHORT, "Color"),(SHORT, "PrintQuality"),(SHORT, "YResolution"),(SHORT, "Copies"),(SHORT, "TTOption"),]

    

class RPC_BRANCHOFFICEJOBDATAERROR(NdrStructure):
    MEMBERS = [(DWORD, "LastError"),(PWCHAR_T, "pDocumentName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pDataType"),(LONGLONG, "TotalSize"),(LONGLONG, "PrintedSize"),(DWORD, "TotalPages"),(DWORD, "PrintedPages"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pJobError"),(PWCHAR_T, "pErrorDescription"),]

    

class RPC_BRANCHOFFICEJOBDATAPIPELINEFAILED(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pDocumentName"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pExtraErrorInfo"),]

    

class RPC_BRANCHOFFICELOGOFFLINEFILEFULL(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pMachineName"),]

    

class RPC_BRANCHOFFICEJOBDATA(NdrStructure):
    MEMBERS = [(EBRANCHOFFICEJOBEVENTTYPE, "eEventType"),(DWORD, "JobId"),(JOBINFO, "JobInfo"),]

    

class RPC_BRANCHOFFICEJOBDATACONTAINER(NdrStructure):
    MEMBERS = [(DWORD, "cJobDataEntries"),(RPC_BRANCHOFFICEJOBDATA, "JobData"),]

    
RMTNTFY_HANDLE = VOID

class NOTIFY_REPLY_CONTAINER(NdrStructure):
    MEMBERS = [(PRPC_V2_NOTIFY_INFO, "pInfo"),]

    

class NOTIFY_OPTIONS_CONTAINER(NdrStructure):
    MEMBERS = [(PRPC_V2_NOTIFY_OPTIONS, "pOptions"),]

    

class RPCPRINTPROPERTYVALUE(NdrStructure):
    MEMBERS = [(EPRINTPROPERTYTYPE, "ePropertyType"),(VALUE, "value"),]

    

class RPCPRINTNAMEDPROPERTY(NdrStructure):
    MEMBERS = [(PWCHAR_T, "propertyName"),(RPCPRINTPROPERTYVALUE, "propertyValue"),]

    

class RPCPRINTPROPERTIESCOLLECTION(NdrStructure):
    MEMBERS = [(UNSIGNED_LONG, "numberOfProperties"),(PRPCPRINTNAMEDPROPERTY, "propertiesCollection"),]

    

class CORE_PRINTER_DRIVER(NdrStructure):
    MEMBERS = [(GUID, "CoreDriverGUID"),(FILETIME, "ftDriverDate"),(DWORDLONG, "dwlDriverVersion"),(WCHAR_T, "szPackageID"),]

    

class RPC_PRINTPROPERTYVALUE(NdrStructure):
    MEMBERS = [(RPC_EPRINTPROPERTYTYPE, "ePropertyType"),(VALUE, "value"),]

    

class RPC_PRINTNAMEDPROPERTY(NdrStructure):
    MEMBERS = [(PWCHAR_T, "propertyName"),(RPC_PRINTPROPERTYVALUE, "propertyValue"),]

    
Method("RpcAsyncOpenPrinter",
In(HANDLE_T),
In(PWCHAR_T),
Out(PPRINTER_HANDLE),
In(PWCHAR_T),
In(PDEVMODE_CONTAINER),
In(DWORD),
In(PSPLCLIENT_CONTAINER),
),Method("RpcAsyncAddPrinter",
In(HANDLE_T),
In(PWCHAR_T),
In(PPRINTER_CONTAINER),
In(PDEVMODE_CONTAINER),
In(PSECURITY_CONTAINER),
In(PSPLCLIENT_CONTAINER),
Out(PPRINTER_HANDLE),
),Method("RpcAsyncSetJob",
In(PRINTER_HANDLE),
In(DWORD),
In(PJOB_CONTAINER),
In(DWORD),
),Method("RpcAsyncGetJob",
In(PRINTER_HANDLE),
In(DWORD),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncEnumJobs",
In(PRINTER_HANDLE),
In(DWORD),
In(DWORD),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncAddJob",
In(PRINTER_HANDLE),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncScheduleJob",
In(PRINTER_HANDLE),
In(DWORD),
),Method("RpcAsyncDeletePrinter",
In(PRINTER_HANDLE),
),Method("RpcAsyncSetPrinter",
In(PRINTER_HANDLE),
In(PPRINTER_CONTAINER),
In(PDEVMODE_CONTAINER),
In(PSECURITY_CONTAINER),
In(DWORD),
),Method("RpcAsyncGetPrinter",
In(PRINTER_HANDLE),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncStartDocPrinter",
In(PRINTER_HANDLE),
In(PDOC_INFO_CONTAINER),
Out(PDWORD),
),Method("RpcAsyncStartPagePrinter",
In(PRINTER_HANDLE),
),Method("RpcAsyncWritePrinter",
In(PRINTER_HANDLE),
In(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncEndPagePrinter",
In(PRINTER_HANDLE),
),Method("RpcAsyncEndDocPrinter",
In(PRINTER_HANDLE),
),Method("RpcAsyncAbortPrinter",
In(PRINTER_HANDLE),
),Method("RpcAsyncGetPrinterData",
In(PRINTER_HANDLE),
In(PWCHAR_T),
Out(PDWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncGetPrinterDataEx",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
Out(PDWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncSetPrinterData",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(DWORD),
In(PUNSIGNED_CHAR),
In(DWORD),
),Method("RpcAsyncSetPrinterDataEx",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(PUNSIGNED_CHAR),
In(DWORD),
),Method("RpcAsyncClosePrinter",
InOut(PPRINTER_HANDLE),
),Method("RpcAsyncAddForm",
In(PRINTER_HANDLE),
In(PFORM_CONTAINER),
),Method("RpcAsyncDeleteForm",
In(PRINTER_HANDLE),
In(PWCHAR_T),
),Method("RpcAsyncGetForm",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncSetForm",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PFORM_CONTAINER),
),Method("RpcAsyncEnumForms",
In(PRINTER_HANDLE),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncGetPrinterDriver",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
In(DWORD),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncEnumPrinterData",
In(PRINTER_HANDLE),
In(DWORD),
Out(PWCHAR_T),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncEnumPrinterDataEx",
In(PRINTER_HANDLE),
In(PWCHAR_T),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncEnumPrinterKey",
In(PRINTER_HANDLE),
In(PWCHAR_T),
Out(PWCHAR_T),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncDeletePrinterData",
In(PRINTER_HANDLE),
In(PWCHAR_T),
),Method("RpcAsyncDeletePrinterDataEx",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncDeletePrinterKey",
In(PRINTER_HANDLE),
In(PWCHAR_T),
),Method("RpcAsyncXcvData",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PUNSIGNED_CHAR),
In(DWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
InOut(PDWORD),
),Method("RpcAsyncSendRecvBidiData",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PRPC_BIDI_REQUEST_CONTAINER),
Out(PPRPC_BIDI_RESPONSE_CONTAINER),
),Method("RpcAsyncCreatePrinterIC",
In(PRINTER_HANDLE),
Out(PGDI_HANDLE),
In(PDEVMODE_CONTAINER),
),Method("RpcAsyncPlayGdiScriptOnPrinterIC",
In(GDI_HANDLE),
In(PUNSIGNED_CHAR),
In(DWORD),
Out(PUNSIGNED_CHAR),
In(DWORD),
In(DWORD),
),Method("RpcAsyncDeletePrinterIC",
InOut(PGDI_HANDLE),
),Method("RpcAsyncEnumPrinters",
In(HANDLE_T),
In(DWORD),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncAddPrinterDriver",
In(HANDLE_T),
In(PWCHAR_T),
In(PDRIVER_CONTAINER),
In(DWORD),
),Method("RpcAsyncEnumPrinterDrivers",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncGetPrinterDriverDirectory",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncDeletePrinterDriver",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncDeletePrinterDriverEx",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(DWORD),
),Method("RpcAsyncAddPrintProcessor",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncEnumPrintProcessors",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncGetPrintProcessorDirectory",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncEnumPorts",
In(HANDLE_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncEnumMonitors",
In(HANDLE_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncAddPort",
In(HANDLE_T),
In(PWCHAR_T),
In(PPORT_CONTAINER),
In(PPORT_VAR_CONTAINER),
In(PWCHAR_T),
),Method("RpcAsyncSetPort",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PPORT_CONTAINER),
),Method("RpcAsyncAddMonitor",
In(HANDLE_T),
In(PWCHAR_T),
In(PMONITOR_CONTAINER),
),Method("RpcAsyncDeleteMonitor",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncDeletePrintProcessor",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncEnumPrintProcessorDatatypes",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcAsyncAddPerMachineConnection",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncDeletePerMachineConnection",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncEnumPerMachineConnections",
In(HANDLE_T),
In(PWCHAR_T),
InOut(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
Out(PDWORD),
),Method("RpcSyncRegisterForRemoteNotifications",
In(PRINTER_HANDLE),
In(PRPCPRINTPROPERTIESCOLLECTION),
Out(PRMTNTFY_HANDLE),
),Method("RpcSyncUnRegisterForRemoteNotifications",
InOut(PRMTNTFY_HANDLE),
),Method("RpcSyncRefreshRemoteNotifications",
In(RMTNTFY_HANDLE),
In(PRPCPRINTPROPERTIESCOLLECTION),
Out(PPRPCPRINTPROPERTIESCOLLECTION),
),Method("RpcAsyncGetRemoteNotifications",
In(RMTNTFY_HANDLE),
Out(PPRPCPRINTPROPERTIESCOLLECTION),
),Method("RpcAsyncInstallPrinterDriverFromPackage",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
),Method("RpcAsyncUploadPrinterDriverPackage",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
InOut(PWCHAR_T),
InOut(PDWORD),
),Method("RpcAsyncGetCorePrinterDrivers",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(DWORD),
In(PWCHAR_T),
In(DWORD),
Out(PCORE_PRINTER_DRIVER),
),Method("RpcAsyncCorePrinterDriverInstalled",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(GUID),
In(FILETIME),
In(DWORDLONG),
Out(PINT),
),Method("RpcAsyncGetPrinterDriverPackagePath",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
InOut(PWCHAR_T),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncDeletePrinterDriverPackage",
In(HANDLE_T),
In(PWCHAR_T),
In(PWCHAR_T),
In(PWCHAR_T),
),Method("RpcAsyncReadPrinter",
In(PRINTER_HANDLE),
Out(PUNSIGNED_CHAR),
In(DWORD),
Out(PDWORD),
),Method("RpcAsyncResetPrinter",
In(PRINTER_HANDLE),
In(PWCHAR_T),
In(PDEVMODE_CONTAINER),
),Method("RpcAsyncGetJobNamedPropertyValue",
In(PRINTER_HANDLE),
In(DWORD),
In(PWCHAR_T),
Out(PRPC_PRINTPROPERTYVALUE),
),Method("RpcAsyncSetJobNamedProperty",
In(PRINTER_HANDLE),
In(DWORD),
In(PRPC_PRINTNAMEDPROPERTY),
),Method("RpcAsyncDeleteJobNamedProperty",
In(PRINTER_HANDLE),
In(DWORD),
In(PWCHAR_T),
),Method("RpcAsyncEnumJobNamedProperties",
In(PRINTER_HANDLE),
In(DWORD),
Out(PDWORD),
Out(PPRPC_PRINTNAMEDPROPERTY),
),Method("RpcAsyncLogJobInfoForBranchOffice",
In(PRINTER_HANDLE),
In(PRPC_BRANCHOFFICEJOBDATACONTAINER),
),