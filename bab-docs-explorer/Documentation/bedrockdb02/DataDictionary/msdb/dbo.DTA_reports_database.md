# dbo.DTA_reports_database

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DatabaseID | int | 4 | 0 | YES |  |  |
| SessionID | int | 4 | 0 |  | YES |  |
| DatabaseName | sysname | 256 | 0 |  |  |  |
| IsDatabaseSelectedToTune | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_add_session](../../StoredProcedures/msdb/dbo.sp_DTA_add_session.md)
- [msdb: dbo.sp_DTA_check_permission](../../StoredProcedures/msdb/dbo.sp_DTA_check_permission.md)
- [msdb: dbo.sp_DTA_column_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_relational.md)
- [msdb: dbo.sp_DTA_column_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_xml.md)
- [msdb: dbo.sp_DTA_database_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_database_access_helper_relational.md)
- [msdb: dbo.sp_DTA_database_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_database_access_helper_xml.md)
- [msdb: dbo.sp_DTA_get_columntableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_columntableids.md)
- [msdb: dbo.sp_DTA_get_databasetableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_databasetableids.md)
- [msdb: dbo.sp_DTA_get_indexableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_indexableids.md)
- [msdb: dbo.sp_DTA_get_pftableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_pftableids.md)
- [msdb: dbo.sp_DTA_get_pstableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_pstableids.md)
- [msdb: dbo.sp_DTA_get_tableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_tableids.md)
- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)
- [msdb: dbo.sp_DTA_index_current_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_current_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_detail_current_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_current_helper_relational.md)
- [msdb: dbo.sp_DTA_index_detail_recommended_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_detail_recommended_helper_relational.md)
- [msdb: dbo.sp_DTA_index_recommended_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_recommended_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_index_usage_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_relational.md)
- [msdb: dbo.sp_DTA_index_usage_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_database](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_database.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_relational.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_xml.md)
- [msdb: dbo.sp_DTA_table_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_relational.md)
- [msdb: dbo.sp_DTA_table_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_xml.md)
- [msdb: dbo.sp_DTA_view_table_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_view_table_helper_relational.md)
- [msdb: dbo.sp_DTA_view_table_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_view_table_helper_xml.md)

