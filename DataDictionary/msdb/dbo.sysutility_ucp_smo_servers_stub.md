# dbo.sysutility_ucp_smo_servers_stub

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| urn | nvarchar | 1024 | 1 |  |  |  |
| powershell_path | nvarchar | 8000 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| AuditLevel | smallint | 2 | 1 |  |  |  |
| BackupDirectory | nvarchar | 520 | 1 |  |  |  |
| BrowserServiceAccount | nvarchar | 256 | 1 |  |  |  |
| BrowserStartMode | smallint | 2 | 1 |  |  |  |
| BuildClrVersionString | nvarchar | 40 | 1 |  |  |  |
| BuildNumber | int | 4 | 1 |  |  |  |
| Collation | nvarchar | 256 | 1 |  |  |  |
| CollationID | int | 4 | 1 |  |  |  |
| ComparisonStyle | int | 4 | 1 |  |  |  |
| ComputerNamePhysicalNetBIOS | nvarchar | 256 | 1 |  |  |  |
| DefaultFile | nvarchar | 520 | 1 |  |  |  |
| DefaultLog | nvarchar | 520 | 1 |  |  |  |
| Edition | nvarchar | 128 | 1 |  |  |  |
| EngineEdition | smallint | 2 | 1 |  |  |  |
| ErrorLogPath | nvarchar | 520 | 1 |  |  |  |
| FilestreamShareName | nvarchar | 520 | 1 |  |  |  |
| InstallDataDirectory | nvarchar | 520 | 1 |  |  |  |
| InstallSharedDirectory | nvarchar | 520 | 1 |  |  |  |
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| IsCaseSensitive | bit | 1 | 1 |  |  |  |
| IsClustered | bit | 1 | 1 |  |  |  |
| IsFullTextInstalled | bit | 1 | 1 |  |  |  |
| IsSingleUser | bit | 1 | 1 |  |  |  |
| Language | nvarchar | 128 | 1 |  |  |  |
| MailProfile | nvarchar | 256 | 1 |  |  |  |
| MasterDBLogPath | nvarchar | 520 | 1 |  |  |  |
| MasterDBPath | nvarchar | 520 | 1 |  |  |  |
| MaxPrecision | tinyint | 1 | 1 |  |  |  |
| Name | nvarchar | 256 | 1 |  |  |  |
| NamedPipesEnabled | bit | 1 | 1 |  |  |  |
| NetName | nvarchar | 256 | 1 |  |  |  |
| NumberOfLogFiles | int | 4 | 1 |  |  |  |
| OSVersion | nvarchar | 64 | 1 |  |  |  |
| PerfMonMode | smallint | 2 | 1 |  |  |  |
| PhysicalMemory | int | 4 | 1 |  |  |  |
| Platform | nvarchar | 64 | 1 |  |  |  |
| Processors | smallint | 2 | 1 |  |  |  |
| ProcessorUsage | int | 4 | 1 |  |  |  |
| Product | nvarchar | 96 | 1 |  |  |  |
| ProductLevel | nvarchar | 64 | 1 |  |  |  |
| ResourceVersionString | nvarchar | 64 | 1 |  |  |  |
| RootDirectory | nvarchar | 520 | 1 |  |  |  |
| ServerType | smallint | 2 | 1 |  |  |  |
| ServiceAccount | nvarchar | 256 | 1 |  |  |  |
| ServiceInstanceId | nvarchar | 128 | 1 |  |  |  |
| ServiceName | nvarchar | 128 | 1 |  |  |  |
| ServiceStartMode | smallint | 2 | 1 |  |  |  |
| SqlCharSet | smallint | 2 | 1 |  |  |  |
| SqlCharSetName | nvarchar | 64 | 1 |  |  |  |
| SqlDomainGroup | nvarchar | 520 | 1 |  |  |  |
| SqlSortOrder | smallint | 2 | 1 |  |  |  |
| SqlSortOrderName | nvarchar | 128 | 1 |  |  |  |
| Status | smallint | 2 | 1 |  |  |  |
| TapeLoadWaitTime | int | 4 | 1 |  |  |  |
| TcpEnabled | bit | 1 | 1 |  |  |  |
| VersionMajor | int | 4 | 1 |  |  |  |
| VersionMinor | int | 4 | 1 |  |  |  |
| VersionString | nvarchar | 64 | 1 |  |  |  |

