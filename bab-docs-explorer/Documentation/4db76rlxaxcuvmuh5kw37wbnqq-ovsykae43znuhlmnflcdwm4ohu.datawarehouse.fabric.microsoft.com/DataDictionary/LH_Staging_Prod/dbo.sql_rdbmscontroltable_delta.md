# dbo.sql_rdbmscontroltable_delta

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ControlID | int | 4 | 1 |  |  |  |
| BusinessArea | varchar | 8000 | 1 |  |  |  |
| SrcConnectionFriendlyName | varchar | 8000 | 1 |  |  |  |
| SrcTableDB | varchar | 8000 | 1 |  |  |  |
| SrcTableSchema | varchar | 8000 | 1 |  |  |  |
| SrcTableName | varchar | 8000 | 1 |  |  |  |
| TgtConnectionFriendlyName | varchar | 8000 | 1 |  |  |  |
| TgtRootContainer | varchar | 8000 | 1 |  |  |  |
| TgtADLSPath | varchar | 8000 | 1 |  |  |  |
| TgtLakehouse | varchar | 8000 | 1 |  |  |  |
| TgtTableName | varchar | 8000 | 1 |  |  |  |
| ColumnList | varchar | 8000 | 1 |  |  |  |
| PrimaryKeyList | varchar | 8000 | 1 |  |  |  |
| AdditionalFilterConditions | varchar | 8000 | 1 |  |  |  |
| Query | varchar | 8000 | 1 |  |  |  |
| CopyMethod | varchar | 8000 | 1 |  |  |  |
| PartitionColumn | varchar | 8000 | 1 |  |  |  |
| LoadType | varchar | 8000 | 1 |  |  |  |
| IsActive | int | 4 | 1 |  |  |  |
| Tag | varchar | 8000 | 1 |  |  |  |
| LatestFilePath | varchar | 8000 | 1 |  |  |  |
| LastRefreshStatus | varchar | 8000 | 1 |  |  |  |
| LastRefreshDate | datetime2 | 8 | 1 |  |  |  |
| RefreshStartDate | datetime2 | 8 | 1 |  |  |  |
| IncRefreshColumn | varchar | 8000 | 1 |  |  |  |
| IncRefreshMaxDate | datetime2 | 8 | 1 |  |  |  |
| ThresholdValue | int | 4 | 1 |  |  |  |
| TgtFileName | varchar | 8000 | 1 |  |  |  |
| merge_status | varchar | 8000 | 1 |  |  |  |
| isdistinctrecords | varchar | 8000 | 1 |  |  |  |
