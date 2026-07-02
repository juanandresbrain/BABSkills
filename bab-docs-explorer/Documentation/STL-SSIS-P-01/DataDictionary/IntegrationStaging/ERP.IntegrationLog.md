# ERP.IntegrationLog

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProcessName | nvarchar | 200 | 1 |  |  |  |
| ProcessDateTime | datetime | 8 | 1 |  |  |  |
| TaskName | nvarchar | 200 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| ImportFileName | nvarchar | 2000 | 1 |  |  |  |
| ArchiveFileName | nvarchar | 2000 | 1 |  |  |  |
| ErrorFileName | nvarchar | 2000 | 1 |  |  |  |
| DataStaged | int | 4 | 1 |  |  |  |
| DataMerged | int | 4 | 1 |  |  |  |

