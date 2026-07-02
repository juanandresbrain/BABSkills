# dbo.DTA_reports_partitionscheme

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartitionSchemeID | int | 4 | 0 | YES |  |  |
| PartitionFunctionID | int | 4 | 0 |  | YES |  |
| PartitionSchemeName | sysname | 256 | 0 |  |  |  |
| PartitionSchemeDefinition | ntext | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_pstableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_pstableids.md)
- [msdb: dbo.sp_DTA_insert_reports_partitionscheme](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_partitionscheme.md)

