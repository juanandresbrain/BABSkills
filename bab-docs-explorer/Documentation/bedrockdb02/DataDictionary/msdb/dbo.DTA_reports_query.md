# dbo.DTA_reports_query

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| QueryID | int | 4 | 0 | YES |  |  |
| SessionID | int | 4 | 0 | YES | YES |  |
| StatementType | smallint | 2 | 0 |  |  |  |
| StatementString | ntext | 16 | 0 |  |  |  |
| CurrentCost | float | 8 | 0 |  |  |  |
| RecommendedCost | float | 8 | 0 |  |  |  |
| Weight | float | 8 | 0 |  |  |  |
| EventString | ntext | 16 | 1 |  |  |  |
| EventWeight | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_column_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_relational.md)
- [msdb: dbo.sp_DTA_column_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_xml.md)
- [msdb: dbo.sp_DTA_database_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_database_access_helper_relational.md)
- [msdb: dbo.sp_DTA_database_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_database_access_helper_xml.md)
- [msdb: dbo.sp_DTA_event_weight_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_event_weight_helper_relational.md)
- [msdb: dbo.sp_DTA_event_weight_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_event_weight_helper_xml.md)
- [msdb: dbo.sp_DTA_index_usage_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_relational.md)
- [msdb: dbo.sp_DTA_index_usage_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_index_usage_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_query](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_query.md)
- [msdb: dbo.sp_DTA_query_cost_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_cost_helper_relational.md)
- [msdb: dbo.sp_DTA_query_cost_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_cost_helper_xml.md)
- [msdb: dbo.sp_DTA_query_costrange_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_costrange_helper_relational.md)
- [msdb: dbo.sp_DTA_query_costrange_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_costrange_helper_xml.md)
- [msdb: dbo.sp_DTA_query_detail_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_detail_helper_relational.md)
- [msdb: dbo.sp_DTA_query_detail_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_detail_helper_xml.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_relational.md)
- [msdb: dbo.sp_DTA_query_indexrelations_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_query_indexrelations_helper_xml.md)
- [msdb: dbo.sp_DTA_table_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_relational.md)
- [msdb: dbo.sp_DTA_table_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_table_access_helper_xml.md)
- [msdb: dbo.sp_DTA_wkld_analysis_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_wkld_analysis_helper_relational.md)
- [msdb: dbo.sp_DTA_wkld_analysis_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_wkld_analysis_helper_xml.md)

