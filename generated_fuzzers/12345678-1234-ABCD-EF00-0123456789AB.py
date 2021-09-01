
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
PWCHAR = NdrCString
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

class OS_TYPE(NdrEnum):
    MAP = ((1 , 'VER_NT_WORKSTATION'),(2 , 'VER_NT_DOMAIN_CONTROLLER'),(3 , 'VER_NT_SERVER'),)        

class BIDI_TYPE(NdrEnum):
    MAP = ((0 , 'BIDI_NULL'),(1 , 'BIDI_INT'),(2 , 'BIDI_FLOAT'),(3 , 'BIDI_BOOL'),(4 , 'BIDI_STRING'),(5 , 'BIDI_TEXT'),(6 , 'BIDI_ENUM'),(7 , 'BIDI_BLOB'),)        

class RPC_EPRINTPROPERTYTYPE(NdrEnum):
    MAP = ((1 , 'kRpcPropertyTypeString'),(2 , 'kRpcPropertyTypeInt32'),(3 , 'kRpcPropertyTypeInt64'),(4 , 'kRpcPropertyTypeByte'),(5 , 'kRpcPropertyTypeBuffer'),)        
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
    MEMBERS = [(DWORD, "JobId"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pDocument"),(PWCHAR_T, "pNotifyName"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pParameters"),(PWCHAR_T, "pDriverName"),(ULONG_PTR, "pDevMode"),(PWCHAR_T, "pStatus"),(ULONG_PTR, "pSecurityDescriptor"),(DWORD, "Status"),(DWORD, "Priority"),(DWORD, "Position"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "TotalPages"),(DWORD, "Size"),(SYSTEMTIME, "Submitted"),(DWORD, "Time"),(DWORD, "PagesPrinted"),]

    

class JOB_INFO_3(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(DWORD, "NextJobId"),(DWORD, "Reserved"),]

    

class JOB_INFO_4(NdrStructure):
    MEMBERS = [(DWORD, "JobId"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pMachineName"),(PWCHAR_T, "pUserName"),(PWCHAR_T, "pDocument"),(PWCHAR_T, "pNotifyName"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pParameters"),(PWCHAR_T, "pDriverName"),(ULONG_PTR, "pDevMode"),(PWCHAR_T, "pStatus"),(ULONG_PTR, "pSecurityDescriptor"),(DWORD, "Status"),(DWORD, "Priority"),(DWORD, "Position"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "TotalPages"),(DWORD, "Size"),(SYSTEMTIME, "Submitted"),(DWORD, "Time"),(DWORD, "PagesPrinted"),(LONG, "SizeHigh"),]

    

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
    MEMBERS = [(PWCHAR_T, "pServerName"),(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pShareName"),(PWCHAR_T, "pPortName"),(PWCHAR_T, "pDriverName"),(PWCHAR_T, "pComment"),(PWCHAR_T, "pLocation"),(ULONG_PTR, "pDevMode"),(PWCHAR_T, "pSepFile"),(PWCHAR_T, "pPrintProcessor"),(PWCHAR_T, "pDatatype"),(PWCHAR_T, "pParameters"),(ULONG_PTR, "pSecurityDescriptor"),(DWORD, "Attributes"),(DWORD, "Priority"),(DWORD, "DefaultPriority"),(DWORD, "StartTime"),(DWORD, "UntilTime"),(DWORD, "Status"),(DWORD, "cJobs"),(DWORD, "AveragePPM"),]

    

class PRINTER_INFO_3(NdrStructure):
    MEMBERS = [(ULONG_PTR, "pSecurityDescriptor"),]

    

class PRINTER_INFO_4(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pServerName"),(DWORD, "Attributes"),]

    

class PRINTER_INFO_5(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pPrinterName"),(PWCHAR_T, "pPortName"),(DWORD, "Attributes"),(DWORD, "DeviceNotSelectedTimeout"),(DWORD, "TransmissionRetryTimeout"),]

    

class PRINTER_INFO_6(NdrStructure):
    MEMBERS = [(DWORD, "dwStatus"),]

    

class PRINTER_INFO_7(NdrStructure):
    MEMBERS = [(PWCHAR_T, "pszObjectGUID"),(DWORD, "dwAction"),]

    

class PRINTER_INFO_8(NdrStructure):
    MEMBERS = [(ULONG_PTR, "pDevMode"),]

    

class PRINTER_INFO_9(NdrStructure):
    MEMBERS = [(ULONG_PTR, "pDevMode"),]

    

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

    

class CORE_PRINTER_DRIVER(NdrStructure):
    MEMBERS = [(GUID, "CoreDriverGUID"),(FILETIME, "ftDriverDate"),(DWORDLONG, "dwlDriverVersion"),(WCHAR_T, "szPackageID"),]

    

class RPC_PRINTPROPERTYVALUE(NdrStructure):
    MEMBERS = [(RPC_EPRINTPROPERTYTYPE, "ePropertyType"),(VALUE, "value"),]

    

class RPC_PRINTNAMEDPROPERTY(NdrStructure):
    MEMBERS = [(PWCHAR_T, "propertyName"),(RPC_PRINTPROPERTYVALUE, "propertyValue"),]

    

class EBRANCHOFFICEJOBEVENTTYPE(NdrEnum):
    MAP = ((0 , 'kInvalidJobState'),(1 , 'kLogJobPrinted'),(2 , 'kLogJobRendered'),(3 , 'kLogJobError'),(4 , 'kLogJobPipelineError'),(5 , 'kLogOfflineFileFull'),)        

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

    
Interface("12345678-1234-ABCD-EF00-0123456789AB", "1.0",[Method("RpcEnumPrinters",
In((DWORD,'Flags')),
In((STRING_HANDLE,'Name')),
In((DWORD,'Level')),
InOut((PBYTE,'pPrinterEnum')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcOpenPrinter",
In((STRING_HANDLE,'pPrinterName')),
Out((PPRINTER_HANDLE,'pHandle')),
In((PWCHAR_T,'pDatatype')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((DWORD,'AccessRequired')),
),Method("RpcSetJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PJOB_CONTAINER,'pJobContainer')),
In((DWORD,'Command')),
),Method("RpcGetJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((DWORD,'Level')),
InOut((PBYTE,'pJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcEnumJobs",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'FirstJob')),
In((DWORD,'NoJobs')),
In((DWORD,'Level')),
InOut((PBYTE,'pJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAddPrinter",
In((STRING_HANDLE,'pName')),
In((PPRINTER_CONTAINER,'pPrinterContainer')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((PSECURITY_CONTAINER,'pSecurityContainer')),
Out((PPRINTER_HANDLE,'pHandle')),
),Method("RpcDeletePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcSetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PPRINTER_CONTAINER,'pPrinterContainer')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((PSECURITY_CONTAINER,'pSecurityContainer')),
In((DWORD,'Command')),
),Method("RpcGetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PBYTE,'pPrinter')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAddPrinterDriver",
In((STRING_HANDLE,'pName')),
In((PDRIVER_CONTAINER,'pDriverContainer')),
),Method("RpcEnumPrinterDrivers",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pDrivers')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcGetPrinterDriver",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pDriver')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcGetPrinterDriverDirectory",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pDriverDirectory')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcDeletePrinterDriver",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pDriverName')),
),Method("RpcAddPrintProcessor",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pPathName')),
In((PWCHAR_T,'pPrintProcessorName')),
),Method("RpcEnumPrintProcessors",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pPrintProcessorInfo')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcGetPrintProcessorDirectory",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pPrintProcessorDirectory')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcStartDocPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PDOC_INFO_CONTAINER,'pDocInfoContainer')),
Out((PDWORD,'pJobId')),
),Method("RpcStartPagePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcWritePrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PBYTE,'pBuf')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcWritten')),
),Method("RpcEndPagePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAbortPrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcReadPrinter",
In((PRINTER_HANDLE,'hPrinter')),
Out((PBYTE,'pBuf')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcNoBytesRead')),
),Method("RpcEndDocPrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAddJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PBYTE,'pAddJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcScheduleJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
),Method("RpcGetPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
Out((PDWORD,'pType')),
Out((PBYTE,'pData')),
In((DWORD,'nSize')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcSetPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
In((DWORD,'Type')),
In((PBYTE,'pData')),
In((DWORD,'cbData')),
),Method("RpcWaitForPrinterChange",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Flags')),
Out((PDWORD,'pFlags')),
),Method("RpcClosePrinter",
InOut((PPRINTER_HANDLE,'phPrinter')),
),Method("RpcAddForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PFORM_CONTAINER,'pFormInfoContainer')),
),Method("RpcDeleteForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
),Method("RpcGetForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
In((DWORD,'Level')),
InOut((PBYTE,'pForm')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcSetForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
In((PFORM_CONTAINER,'pFormInfoContainer')),
),Method("RpcEnumForms",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PBYTE,'pForm')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcEnumPorts",
In((STRING_HANDLE,'pName')),
In((DWORD,'Level')),
InOut((PBYTE,'pPort')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcEnumMonitors",
In((STRING_HANDLE,'pName')),
In((DWORD,'Level')),
InOut((PBYTE,'pMonitor')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("Opnum37NotUsedOnWire",
),Method("Opnum38NotUsedOnWire",
),Method("RpcDeletePort",
In((STRING_HANDLE,'pName')),
In((ULONG_PTR,'hWnd')),
In((PWCHAR_T,'pPortName')),
),Method("RpcCreatePrinterIC",
In((PRINTER_HANDLE,'hPrinter')),
Out((PGDI_HANDLE,'pHandle')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
),Method("RpcPlayGdiScriptOnPrinterIC",
In((GDI_HANDLE,'hPrinterIC')),
In((PBYTE,'pIn')),
In((DWORD,'cIn')),
Out((PBYTE,'pOut')),
In((DWORD,'cOut')),
In((DWORD,'ul')),
),Method("RpcDeletePrinterIC",
InOut((PGDI_HANDLE,'phPrinterIC')),
),Method("Opnum43NotUsedOnWire",
),Method("Opnum44NotUsedOnWire",
),Method("Opnum45NotUsedOnWire",
),Method("RpcAddMonitor",
In((STRING_HANDLE,'Name')),
In((PMONITOR_CONTAINER,'pMonitorContainer')),
),Method("RpcDeleteMonitor",
In((STRING_HANDLE,'Name')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pMonitorName')),
),Method("RpcDeletePrintProcessor",
In((STRING_HANDLE,'Name')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pPrintProcessorName')),
),Method("Opnum49NotUsedOnWire",
),Method("Opnum50NotUsedOnWire",
),Method("RpcEnumPrintProcessorDatatypes",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pPrintProcessorName')),
In((DWORD,'Level')),
InOut((PBYTE,'pDatatypes')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcResetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pDatatype')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
),Method("RpcGetPrinterDriver2",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PBYTE,'pDriver')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
In((DWORD,'dwClientMajorVersion')),
In((DWORD,'dwClientMinorVersion')),
Out((PDWORD,'pdwServerMaxVersion')),
Out((PDWORD,'pdwServerMinVersion')),
),Method("Opnum54NotUsedOnWire",
),Method("Opnum55NotUsedOnWire",
),Method("RpcFindClosePrinterChangeNotification",
In((PRINTER_HANDLE,'hPrinter')),
),Method("Opnum57NotUsedOnWire",
),Method("RpcReplyOpenPrinter",
In((STRING_HANDLE,'pMachine')),
Out((PPRINTER_HANDLE,'phPrinterNotify')),
In((DWORD,'dwPrinterRemote')),
In((DWORD,'dwType')),
In((DWORD,'cbBuffer')),
In((PBYTE,'pBuffer')),
),Method("RpcRouterReplyPrinter",
In((PRINTER_HANDLE,'hNotify')),
In((DWORD,'fdwFlags')),
In((DWORD,'cbBuffer')),
In((PBYTE,'pBuffer')),
),Method("RpcReplyClosePrinter",
InOut((PPRINTER_HANDLE,'phNotify')),
),Method("RpcAddPortEx",
In((STRING_HANDLE,'pName')),
In((PPORT_CONTAINER,'pPortContainer')),
In((PPORT_VAR_CONTAINER,'pPortVarContainer')),
In((PWCHAR_T,'pMonitorName')),
),Method("RpcRemoteFindFirstPrinterChangeNotification",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'fdwFlags')),
In((DWORD,'fdwOptions')),
In((PWCHAR_T,'pszLocalMachine')),
In((DWORD,'dwPrinterLocal')),
In((DWORD,'cbBuffer')),
InOut((PBYTE,'pBuffer')),
),Method("Opnum63NotUsedOnWire",
),Method("Opnum64NotUsedOnWire",
),Method("RpcRemoteFindFirstPrinterChangeNotificationEx",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'fdwFlags')),
In((DWORD,'fdwOptions')),
In((PWCHAR_T,'pszLocalMachine')),
In((DWORD,'dwPrinterLocal')),
In((PRPC_V2_NOTIFY_OPTIONS,'pOptions')),
),Method("RpcRouterReplyPrinterEx",
In((PRINTER_HANDLE,'hNotify')),
In((DWORD,'dwColor')),
In((DWORD,'fdwFlags')),
Out((PDWORD,'pdwResult')),
In((DWORD,'dwReplyType')),
In((RPC_V2_UREPLY_PRINTER,'Reply')),
),Method("RpcRouterRefreshPrinterChangeNotification",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'dwColor')),
In((PRPC_V2_NOTIFY_OPTIONS,'pOptions')),
Out((PPRPC_V2_NOTIFY_INFO,'ppInfo')),
),Method("Opnum68NotUsedOnWire",
),Method("RpcOpenPrinterEx",
In((STRING_HANDLE,'pPrinterName')),
Out((PPRINTER_HANDLE,'pHandle')),
In((PWCHAR_T,'pDatatype')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((DWORD,'AccessRequired')),
In((PSPLCLIENT_CONTAINER,'pClientInfo')),
),Method("RpcAddPrinterEx",
In((STRING_HANDLE,'pName')),
In((PPRINTER_CONTAINER,'pPrinterContainer')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((PSECURITY_CONTAINER,'pSecurityContainer')),
In((PSPLCLIENT_CONTAINER,'pClientInfo')),
Out((PPRINTER_HANDLE,'pHandle')),
),Method("RpcSetPort",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pPortName')),
In((PPORT_CONTAINER,'pPortContainer')),
),Method("RpcEnumPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'dwIndex')),
Out((PWCHAR_T,'pValueName')),
In((DWORD,'cbValueName')),
Out((PDWORD,'pcbValueName')),
Out((PDWORD,'pType')),
Out((PBYTE,'pData')),
In((DWORD,'cbData')),
Out((PDWORD,'pcbData')),
),Method("RpcDeletePrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
),Method("Opnum74NotUsedOnWire",
),Method("Opnum75NotUsedOnWire",
),Method("Opnum76NotUsedOnWire",
),Method("RpcSetPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
In((DWORD,'Type')),
In((PBYTE,'pData')),
In((DWORD,'cbData')),
),Method("RpcGetPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
Out((PDWORD,'pType')),
Out((PBYTE,'pData')),
In((DWORD,'nSize')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcEnumPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
Out((PBYTE,'pEnumValues')),
In((DWORD,'cbEnumValues')),
Out((PDWORD,'pcbEnumValues')),
Out((PDWORD,'pnEnumValues')),
),Method("RpcEnumPrinterKey",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
Out((PWCHAR_T,'pSubkey')),
In((DWORD,'cbSubkey')),
Out((PDWORD,'pcbSubkey')),
),Method("RpcDeletePrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
),Method("RpcDeletePrinterKey",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
),Method("Opnum83NotUsedOnWire",
),Method("RpcDeletePrinterDriverEx",
In((STRING_HANDLE,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pDriverName')),
In((DWORD,'dwDeleteFlag')),
In((DWORD,'dwVersionNum')),
),Method("RpcAddPerMachineConnection",
In((STRING_HANDLE,'pServer')),
In((PWCHAR_T,'pPrinterName')),
In((PWCHAR_T,'pPrintServer')),
In((PWCHAR_T,'pProvider')),
),Method("RpcDeletePerMachineConnection",
In((STRING_HANDLE,'pServer')),
In((PWCHAR_T,'pPrinterName')),
),Method("RpcEnumPerMachineConnections",
In((STRING_HANDLE,'pServer')),
InOut((PBYTE,'pPrinterEnum')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcXcvData",
In((PRINTER_HANDLE,'hXcv')),
In((PWCHAR_T,'pszDataName')),
In((PBYTE,'pInputData')),
In((DWORD,'cbInputData')),
Out((PBYTE,'pOutputData')),
In((DWORD,'cbOutputData')),
Out((PDWORD,'pcbOutputNeeded')),
InOut((PDWORD,'pdwStatus')),
),Method("RpcAddPrinterDriverEx",
In((STRING_HANDLE,'pName')),
In((PDRIVER_CONTAINER,'pDriverContainer')),
In((DWORD,'dwFileCopyFlags')),
),Method("Opnum90NotUsedOnWire",
),Method("Opnum91NotUsedOnWire",
),Method("Opnum92NotUsedOnWire",
),Method("Opnum93NotUsedOnWire",
),Method("Opnum94NotUsedOnWire",
),Method("Opnum95NotUsedOnWire",
),Method("RpcFlushPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PBYTE,'pBuf')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcWritten')),
In((DWORD,'cSleep')),
),Method("RpcSendRecvBidiData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pAction')),
In((PRPC_BIDI_REQUEST_CONTAINER,'pReqData')),
Out((PPRPC_BIDI_RESPONSE_CONTAINER,'ppRespData')),
),Method("Opnum98NotUsedOnWire",
),Method("Opnum99NotUsedOnWire",
),Method("Opnum100NotUsedOnWire",
),Method("Opnum101NotUsedOnWire",
),Method("RpcGetCorePrinterDrivers",
In((STRING_HANDLE,'pszServer')),
In((PWCHAR_T,'pszEnvironment')),
In((DWORD,'cchCoreDrivers')),
In((PWCHAR_T,'pszzCoreDriverDependencies')),
In((DWORD,'cCorePrinterDrivers')),
Out((PCORE_PRINTER_DRIVER,'pCorePrinterDrivers')),
),Method("Opnum103NotUsedOnWire",
),Method("RpcGetPrinterDriverPackagePath",
In((STRING_HANDLE,'pszServer')),
In((PWCHAR_T,'pszEnvironment')),
In((PWCHAR_T,'pszLanguage')),
In((PWCHAR_T,'pszPackageID')),
InOut((PWCHAR_T,'pszDriverPackageCab')),
In((DWORD,'cchDriverPackageCab')),
Out((LPDWORD,'pcchRequiredSize')),
),Method("Opnum105NotUsedOnWire",
),Method("Opnum106NotUsedOnWire",
),Method("Opnum107NotUsedOnWire",
),Method("Opnum108NotUsedOnWire",
),Method("Opnum109NotUsedOnWire",
),Method("RpcGetJobNamedPropertyValue",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PWCHAR_T,'pszName')),
Out((PRPC_PRINTPROPERTYVALUE,'pValue')),
),Method("RpcSetJobNamedProperty",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PRPC_PRINTNAMEDPROPERTY,'pProperty')),
),Method("RpcDeleteJobNamedProperty",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PWCHAR_T,'pszName')),
),Method("RpcEnumJobNamedProperties",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
Out((PDWORD,'pcProperties')),
Out((PPRPC_PRINTNAMEDPROPERTY,'ppProperties')),
),Method("Opnum114NotUsedOnWire",
),Method("Opnum115NotUsedOnWire",
),Method("RpcLogJobInfoForBranchOffice",
In((PRINTER_HANDLE,'hPrinter')),
In((PRPC_BRANCHOFFICEJOBDATACONTAINER,'pBranchOfficeJobDataContainer')),
),Method("RpcRegeneratePrintDeviceCapabilities",
In((PRINTER_HANDLE,'hPrinter')),
),Method("Opnum118NotUsedOnWire",
),Method("RpcIppCreateJobOnPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'jobId')),
In((PWCHAR_T,'pdlFormat')),
In((DWORD,'jobAttributeGroupBufferSize')),
In((PBYTE,'jobAttributeGroupBuffer')),
Out((PDWORD,'ippResponseBufferSize')),
Out((PPBYTE,'ippResponseBuffer')),
),Method("RpcIppGetJobAttributes",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'jobId')),
In((DWORD,'attributeNameCount')),
In((PPWCHAR_T,'attributeNames')),
Out((PDWORD,'ippResponseBufferSize')),
Out((PPBYTE,'ippResponseBuffer')),
),Method("RpcIppSetJobAttributes",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'jobId')),
In((DWORD,'jobAttributeGroupBufferSize')),
In((PBYTE,'jobAttributeGroupBuffer')),
Out((PDWORD,'ippResponseBufferSize')),
Out((PPBYTE,'ippResponseBuffer')),
),Method("RpcIppGetPrinterAttributes",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'attributeNameCount')),
In((PPWCHAR_T,'attributeNames')),
Out((PDWORD,'ippResponseBufferSize')),
Out((PPBYTE,'ippResponseBuffer')),
),Method("RpcIppSetPrinterAttributes",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'jobAttributeGroupBufferSize')),
In((PBYTE,'jobAttributeGroupBuffer')),
Out((PDWORD,'ippResponseBufferSize')),
Out((PPBYTE,'ippResponseBuffer')),
),])