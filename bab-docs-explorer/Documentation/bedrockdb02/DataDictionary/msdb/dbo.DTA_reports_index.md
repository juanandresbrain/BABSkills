# dbo.DTA_reports_index

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IndexID | int | 4 | 0 | YES |  |  |
| TableID | int | 4 | 0 |  | YES |  |
| IndexName | sysname | 256 | 0 |  |  |  |
| IsClustered | bit | 1 | 0 |  |  |  |
| IsUnique | bit | 1 | 0 |  |  |  |
| IsHeap | bit | 1 | 0 |  |  |  |
| IsExisting | bit | 1 | 0 |  |  |  |
| IsFiltered | bit | 1 | 0 |  |  |  |
| Storage | float | 8 | 0 |  |  |  |
| NumRows | bigint | 8 | 0 |  |  |  |
| IsRecommended | bit | 1 | 0 |  |  |  |
| RecommendedStorage | float | 8 | 0 |  |  |  |
| PartitionSchemeID | int | 4 | 1 |  |  |  |
| SessionUniquefier | int | 4 | 1 |  |  |  |
| FilterDefinition | nvarchar | 2048 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_indexableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_indexableids.md)
- [msdb: dbo.sp_DTA_index_current_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_current_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_detail_current_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_current_helper_relational.md)
- [msdb: dbo.sp_DTA_index_detail_recommended_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_recommended_helper_relational.md)
- [msdb: dbo.sp_DTA_index_recommended_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_recommended_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_usage_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_relational.md)
- [msdb: dbo.sp_DTA_index_usage_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_index](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_index.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_relational.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_xml.md)

