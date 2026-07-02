# dbo.DTA_reports_queryindex

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| QueryID | int | 4 | 0 |  | YES |  |
| SessionID | int | 4 | 0 |  | YES |  |
| IndexID | int | 4 | 0 |  | YES |  |
| IsRecommendedConfiguration | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_index_usage_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_relational.md)
- [msdb: dbo.sp_DTA_index_usage_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_queryindex](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_queryindex.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_relational.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_xml.md)

