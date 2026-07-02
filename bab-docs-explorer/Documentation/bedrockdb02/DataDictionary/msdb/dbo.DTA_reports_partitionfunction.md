# dbo.DTA_reports_partitionfunction

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartitionFunctionID | int | 4 | 0 | YES |  |  |
| DatabaseID | int | 4 | 0 |  | YES |  |
| PartitionFunctionName | sysname | 256 | 0 |  |  |  |
| PartitionFunctionDefinition | ntext | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_pftableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_pftableids.md)
- [msdb: dbo.sp_DTA_get_pstableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_pstableids.md)
- [msdb: dbo.sp_DTA_insert_reports_partitionfunction](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_partitionfunction.md)

