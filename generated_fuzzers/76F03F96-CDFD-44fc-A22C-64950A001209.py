
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

class BIDI_TYPE(NdrEnum):
    MAP = ((0 , 'BIDI_NULL'),(1 , 'BIDI_INT'),(2 , 'BIDI_FLOAT'),(3 , 'BIDI_BOOL'),(4 , 'BIDI_STRING'),(5 , 'BIDI_TEXT'),(6 , 'BIDI_ENUM'),(7 , 'BIDI_BLOB'),)        

class RPC_EPRINTPROPERTYTYPE(NdrEnum):
    MAP = ((1 , 'kRpcPropertyTypeString'),(2 , 'kRpcPropertyTypeInt32'),(3 , 'kRpcPropertyTypeInt64'),(4 , 'kRpcPropertyTypeByte'),(5 , 'kRpcPropertyTypeBuffer'),)        

class EBRANCHOFFICEJOBEVENTTYPE(NdrEnum):
    MAP = ((0 , 'kInvalidJobState'),(1 , 'kLogJobPrinted'),(2 , 'kLogJobRendered'),(3 , 'kLogJobError'),(4 , 'kLogJobPipelineError'),(5 , 'kLogOfflineFileFull'),)        
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

    

class EPRINTPROPERTYTYPE(NdrEnum):
    MAP = ((1 , 'kPropertyTypeString'),(2 , 'kPropertyTypeInt32'),(3 , 'kPropertyTypeInt64'),(4 , 'kPropertyTypeByte'),(5 , 'kPropertyTypeTime'),(6 , 'kPropertyTypeDevMode'),(7 , 'kPropertyTypeSD'),(8 , 'kPropertyTypeNotificationReply'),(9 , 'kPropertyTypeNotificationOptions'),)        
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

    
Interface("76F03F96-CDFD-44fc-A22C-64950A001209", "1.0",[Method("RpcAsyncOpenPrinter",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pPrinterName')),
Out((PPRINTER_HANDLE,'pHandle')),
In((PWCHAR_T,'pDatatype')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((DWORD,'AccessRequired')),
In((PSPLCLIENT_CONTAINER,'pClientInfo')),
),Method("RpcAsyncAddPrinter",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PPRINTER_CONTAINER,'pPrinterContainer')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((PSECURITY_CONTAINER,'pSecurityContainer')),
In((PSPLCLIENT_CONTAINER,'pClientInfo')),
Out((PPRINTER_HANDLE,'pHandle')),
),Method("RpcAsyncSetJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PJOB_CONTAINER,'pJobContainer')),
In((DWORD,'Command')),
),Method("RpcAsyncGetJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncEnumJobs",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'FirstJob')),
In((DWORD,'NoJobs')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncAddJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pAddJob')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncScheduleJob",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
),Method("RpcAsyncDeletePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAsyncSetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PPRINTER_CONTAINER,'pPrinterContainer')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
In((PSECURITY_CONTAINER,'pSecurityContainer')),
In((DWORD,'Command')),
),Method("RpcAsyncGetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pPrinter')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncStartDocPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PDOC_INFO_CONTAINER,'pDocInfoContainer')),
Out((PDWORD,'pJobId')),
),Method("RpcAsyncStartPagePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAsyncWritePrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PUNSIGNED_CHAR,'pBuf')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcWritten')),
),Method("RpcAsyncEndPagePrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAsyncEndDocPrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAsyncAbortPrinter",
In((PRINTER_HANDLE,'hPrinter')),
),Method("RpcAsyncGetPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
Out((PDWORD,'pType')),
Out((PUNSIGNED_CHAR,'pData')),
In((DWORD,'nSize')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncGetPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
Out((PDWORD,'pType')),
Out((PUNSIGNED_CHAR,'pData')),
In((DWORD,'nSize')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncSetPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
In((DWORD,'Type')),
In((PUNSIGNED_CHAR,'pData')),
In((DWORD,'cbData')),
),Method("RpcAsyncSetPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
In((DWORD,'Type')),
In((PUNSIGNED_CHAR,'pData')),
In((DWORD,'cbData')),
),Method("RpcAsyncClosePrinter",
InOut((PPRINTER_HANDLE,'phPrinter')),
),Method("RpcAsyncAddForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PFORM_CONTAINER,'pFormInfoContainer')),
),Method("RpcAsyncDeleteForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
),Method("RpcAsyncGetForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pForm')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncSetForm",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pFormName')),
In((PFORM_CONTAINER,'pFormInfoContainer')),
),Method("RpcAsyncEnumForms",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pForm')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncGetPrinterDriver",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pDriver')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
In((DWORD,'dwClientMajorVersion')),
In((DWORD,'dwClientMinorVersion')),
Out((PDWORD,'pdwServerMaxVersion')),
Out((PDWORD,'pdwServerMinVersion')),
),Method("RpcAsyncEnumPrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'dwIndex')),
Out((PWCHAR_T,'pValueName')),
In((DWORD,'cbValueName')),
Out((PDWORD,'pcbValueName')),
Out((PDWORD,'pType')),
Out((PUNSIGNED_CHAR,'pData')),
In((DWORD,'cbData')),
Out((PDWORD,'pcbData')),
),Method("RpcAsyncEnumPrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
Out((PUNSIGNED_CHAR,'pEnumValues')),
In((DWORD,'cbEnumValues')),
Out((PDWORD,'pcbEnumValues')),
Out((PDWORD,'pnEnumValues')),
),Method("RpcAsyncEnumPrinterKey",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
Out((PWCHAR_T,'pSubkey')),
In((DWORD,'cbSubkey')),
Out((PDWORD,'pcbSubkey')),
),Method("RpcAsyncDeletePrinterData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pValueName')),
),Method("RpcAsyncDeletePrinterDataEx",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
In((PWCHAR_T,'pValueName')),
),Method("RpcAsyncDeletePrinterKey",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pKeyName')),
),Method("RpcAsyncXcvData",
In((PRINTER_HANDLE,'hXcv')),
In((PWCHAR_T,'pszDataName')),
In((PUNSIGNED_CHAR,'pInputData')),
In((DWORD,'cbInputData')),
Out((PUNSIGNED_CHAR,'pOutputData')),
In((DWORD,'cbOutputData')),
Out((PDWORD,'pcbOutputNeeded')),
InOut((PDWORD,'pdwStatus')),
),Method("RpcAsyncSendRecvBidiData",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pAction')),
In((PRPC_BIDI_REQUEST_CONTAINER,'pReqData')),
Out((PPRPC_BIDI_RESPONSE_CONTAINER,'ppRespData')),
),Method("RpcAsyncCreatePrinterIC",
In((PRINTER_HANDLE,'hPrinter')),
Out((PGDI_HANDLE,'pHandle')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
),Method("RpcAsyncPlayGdiScriptOnPrinterIC",
In((GDI_HANDLE,'hPrinterIC')),
In((PUNSIGNED_CHAR,'pIn')),
In((DWORD,'cIn')),
Out((PUNSIGNED_CHAR,'pOut')),
In((DWORD,'cOut')),
In((DWORD,'ul')),
),Method("RpcAsyncDeletePrinterIC",
InOut((PGDI_HANDLE,'phPrinterIC')),
),Method("RpcAsyncEnumPrinters",
In((HANDLE_T,'hRemoteBinding')),
In((DWORD,'Flags')),
In((PWCHAR_T,'Name')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pPrinterEnum')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncAddPrinterDriver",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PDRIVER_CONTAINER,'pDriverContainer')),
In((DWORD,'dwFileCopyFlags')),
),Method("RpcAsyncEnumPrinterDrivers",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pDrivers')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncGetPrinterDriverDirectory",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pDriverDirectory')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncDeletePrinterDriver",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pDriverName')),
),Method("RpcAsyncDeletePrinterDriverEx",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pDriverName')),
In((DWORD,'dwDeleteFlag')),
In((DWORD,'dwVersionNum')),
),Method("RpcAsyncAddPrintProcessor",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pPathName')),
In((PWCHAR_T,'pPrintProcessorName')),
),Method("RpcAsyncEnumPrintProcessors",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pPrintProcessorInfo')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncGetPrintProcessorDirectory",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pEnvironment')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pPrintProcessorDirectory')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
),Method("RpcAsyncEnumPorts",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pPort')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncEnumMonitors",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pMonitor')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncAddPort",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PPORT_CONTAINER,'pPortContainer')),
In((PPORT_VAR_CONTAINER,'pPortVarContainer')),
In((PWCHAR_T,'pMonitorName')),
),Method("RpcAsyncSetPort",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pPortName')),
In((PPORT_CONTAINER,'pPortContainer')),
),Method("RpcAsyncAddMonitor",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'Name')),
In((PMONITOR_CONTAINER,'pMonitorContainer')),
),Method("RpcAsyncDeleteMonitor",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'Name')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pMonitorName')),
),Method("RpcAsyncDeletePrintProcessor",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'Name')),
In((PWCHAR_T,'pEnvironment')),
In((PWCHAR_T,'pPrintProcessorName')),
),Method("RpcAsyncEnumPrintProcessorDatatypes",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pName')),
In((PWCHAR_T,'pPrintProcessorName')),
In((DWORD,'Level')),
InOut((PUNSIGNED_CHAR,'pDatatypes')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcAsyncAddPerMachineConnection",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pServer')),
In((PWCHAR_T,'pPrinterName')),
In((PWCHAR_T,'pPrintServer')),
In((PWCHAR_T,'pProvider')),
),Method("RpcAsyncDeletePerMachineConnection",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pServer')),
In((PWCHAR_T,'pPrinterName')),
),Method("RpcAsyncEnumPerMachineConnections",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pServer')),
InOut((PUNSIGNED_CHAR,'pPrinterEnum')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcbNeeded')),
Out((PDWORD,'pcReturned')),
),Method("RpcSyncRegisterForRemoteNotifications",
In((PRINTER_HANDLE,'hPrinter')),
In((PRPCPRINTPROPERTIESCOLLECTION,'pNotifyFilter')),
Out((PRMTNTFY_HANDLE,'phRpcHandle')),
),Method("RpcSyncUnRegisterForRemoteNotifications",
InOut((PRMTNTFY_HANDLE,'phRpcHandle')),
),Method("RpcSyncRefreshRemoteNotifications",
In((RMTNTFY_HANDLE,'hRpcHandle')),
In((PRPCPRINTPROPERTIESCOLLECTION,'pNotifyFilter')),
Out((PPRPCPRINTPROPERTIESCOLLECTION,'ppNotifyData')),
),Method("RpcAsyncGetRemoteNotifications",
In((RMTNTFY_HANDLE,'hRpcHandle')),
Out((PPRPCPRINTPROPERTIESCOLLECTION,'ppNotifyData')),
),Method("RpcAsyncInstallPrinterDriverFromPackage",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszInfPath')),
In((PWCHAR_T,'pszDriverName')),
In((PWCHAR_T,'pszEnvironment')),
In((DWORD,'dwFlags')),
),Method("RpcAsyncUploadPrinterDriverPackage",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszInfPath')),
In((PWCHAR_T,'pszEnvironment')),
In((DWORD,'dwFlags')),
InOut((PWCHAR_T,'pszDestInfPath')),
InOut((PDWORD,'pcchDestInfPath')),
),Method("RpcAsyncGetCorePrinterDrivers",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszEnvironment')),
In((DWORD,'cchCoreDrivers')),
In((PWCHAR_T,'pszzCoreDriverDependencies')),
In((DWORD,'cCorePrinterDrivers')),
Out((PCORE_PRINTER_DRIVER,'pCorePrinterDrivers')),
),Method("RpcAsyncCorePrinterDriverInstalled",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszEnvironment')),
In((GUID,'CoreDriverGUID')),
In((FILETIME,'ftDriverDate')),
In((DWORDLONG,'dwlDriverVersion')),
Out((PINT,'pbDriverInstalled')),
),Method("RpcAsyncGetPrinterDriverPackagePath",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszEnvironment')),
In((PWCHAR_T,'pszLanguage')),
In((PWCHAR_T,'pszPackageID')),
InOut((PWCHAR_T,'pszDriverPackageCab')),
In((DWORD,'cchDriverPackageCab')),
Out((PDWORD,'pcchRequiredSize')),
),Method("RpcAsyncDeletePrinterDriverPackage",
In((HANDLE_T,'hRemoteBinding')),
In((PWCHAR_T,'pszServer')),
In((PWCHAR_T,'pszInfPath')),
In((PWCHAR_T,'pszEnvironment')),
),Method("RpcAsyncReadPrinter",
In((PRINTER_HANDLE,'hPrinter')),
Out((PUNSIGNED_CHAR,'pBuf')),
In((DWORD,'cbBuf')),
Out((PDWORD,'pcNoBytesRead')),
),Method("RpcAsyncResetPrinter",
In((PRINTER_HANDLE,'hPrinter')),
In((PWCHAR_T,'pDatatype')),
In((PDEVMODE_CONTAINER,'pDevModeContainer')),
),Method("RpcAsyncGetJobNamedPropertyValue",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PWCHAR_T,'pszName')),
Out((PRPC_PRINTPROPERTYVALUE,'pValue')),
),Method("RpcAsyncSetJobNamedProperty",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PRPC_PRINTNAMEDPROPERTY,'pProperty')),
),Method("RpcAsyncDeleteJobNamedProperty",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
In((PWCHAR_T,'pszName')),
),Method("RpcAsyncEnumJobNamedProperties",
In((PRINTER_HANDLE,'hPrinter')),
In((DWORD,'JobId')),
Out((PDWORD,'pcProperties')),
Out((PPRPC_PRINTNAMEDPROPERTY,'ppProperties')),
),Method("RpcAsyncLogJobInfoForBranchOffice",
In((PRINTER_HANDLE,'hPrinter')),
In((PRPC_BRANCHOFFICEJOBDATACONTAINER,'pBranchOfficeJobDataContainer')),
),])