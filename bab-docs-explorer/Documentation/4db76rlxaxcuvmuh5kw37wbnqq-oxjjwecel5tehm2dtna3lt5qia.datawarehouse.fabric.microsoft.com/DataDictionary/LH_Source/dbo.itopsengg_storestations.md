# dbo.itopsengg_storestations

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | int | 4 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| HostName | varchar | 8000 | 1 |  |  |  |
| MacAddress | varchar | 8000 | 1 |  |  |  |
| ImageStartDate | datetime2 | 8 | 1 |  |  |  |
| ImageCompleteDate | datetime2 | 8 | 1 |  |  |  |
| GoPostCompleteDate | datetime2 | 8 | 1 |  |  |  |
| GoPostReportErrors | int | 4 | 1 |  |  |  |
| DartIPAddress | varchar | 8000 | 1 |  |  |  |
| DartTicketNumber | varchar | 8000 | 1 |  |  |  |
| DartPortNumber | int | 4 | 1 |  |  |  |
| OSDComplete | bit | 1 | 1 |  |  |  |
| POSComplete | bit | 1 | 1 |  |  |  |
| IPAddress | varchar | 8000 | 1 |  |  |  |
| Role | varchar | 8000 | 1 |  |  |  |
| Manufacturer | varchar | 8000 | 1 |  |  |  |
| Model | varchar | 8000 | 1 |  |  |  |
| SerialNumber | varchar | 8000 | 1 |  |  |  |
| OSVersion | varchar | 8000 | 1 |  |  |  |
| ImageVersion | varchar | 8000 | 1 |  |  |  |
| HardDriveFreeSpace | int | 4 | 1 |  |  |  |
| LastValidated | datetime2 | 8 | 1 |  |  |  |
| AjbInitDebitFailDetails | varchar | 8000 | 1 |  |  |  |
| PinPadSerialNumber | varchar | 8000 | 1 |  |  |  |
| OSName | varchar | 8000 | 1 |  |  |  |
| DomainName | varchar | 8000 | 1 |  |  |  |
| DomainTrust | varchar | 8000 | 1 |  |  |  |
| TimeZone | varchar | 8000 | 1 |  |  |  |
| MaintenanceVersion | datetime2 | 8 | 1 |  |  |  |
| MaintenanceStatus | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| HardwareVersion | float | 8 | 1 |  |  |  |
| PrinterModel | varchar | 8000 | 1 |  |  |  |
| CashDrawerModel | varchar | 8000 | 1 |  |  |  |
| ScannerModel | varchar | 8000 | 1 |  |  |  |
| AllowReimage | bit | 1 | 1 |  |  |  |
| POSVersion | varchar | 8000 | 1 |  |  |  |
| Store | varchar | 8000 | 1 |  |  |  |
| RegisterCount | int | 4 | 1 |  |  |  |
| Position | int | 4 | 1 |  |  |  |
| HearMeHardwareVersion | int | 4 | 1 |  |  |  |
| ImageDescription | varchar | 8000 | 1 |  |  |  |
| ScreenOrientation | varchar | 8000 | 1 |  |  |  |
| Office2010Installed | bit | 1 | 1 |  |  |  |
| DefaultPrinter_PosAdmin | varchar | 8000 | 1 |  |  |  |
| DefaultPrinter_posluser | varchar | 8000 | 1 |  |  |  |
| BackupArchiveDate | datetime2 | 8 | 1 |  |  |  |
| LastBootupTime | datetime2 | 8 | 1 |  |  |  |
| GoPostReportWarnings | int | 4 | 1 |  |  |  |
