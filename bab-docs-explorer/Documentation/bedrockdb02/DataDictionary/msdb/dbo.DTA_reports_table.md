# dbo.DTA_reports_table

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableID | int | 4 | 0 | YES |  |  |
| DatabaseID | int | 4 | 0 |  | YES |  |
| SchemaName | sysname | 256 | 0 |  |  |  |
| TableName | sysname | 256 | 0 |  |  |  |
| IsView | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_column_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_relational.md)
- [msdb: dbo.sp_DTA_column_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_xml.md)
- [msdb: dbo.sp_DTA_get_columntableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_columntableids.md)
- [msdb: dbo.sp_DTA_get_indexableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_indexableids.md)
- [msdb: dbo.sp_DTA_get_tableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_tableids.md)
- [msdb: dbo.sp_DTA_index_current_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_current_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_detail_current_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_current_helper_relational.md)
- [msdb: dbo.sp_DTA_index_detail_recommended_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_recommended_helper_relational.md)
- [msdb: dbo.sp_DTA_index_recommended_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_recommended_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_usage_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_relational.md)
- [msdb: dbo.sp_DTA_index_usage_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_table](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_table.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_relational.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_xml.md)
- [msdb: dbo.sp_DTA_table_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_relational.md)
- [msdb: dbo.sp_DTA_table_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_xml.md)
- [msdb: dbo.sp_DTA_view_table_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_view_table_helper_relational.md)
- [msdb: dbo.sp_DTA_view_table_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_view_table_helper_xml.md)

