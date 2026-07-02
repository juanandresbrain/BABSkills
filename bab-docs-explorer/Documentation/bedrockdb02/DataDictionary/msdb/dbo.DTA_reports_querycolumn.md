# dbo.DTA_reports_querycolumn

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| QueryID | int | 4 | 0 |  | YES |  |
| SessionID | int | 4 | 0 |  | YES |  |
| ColumnID | int | 4 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_column_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_relational.md)
- [msdb: dbo.sp_DTA_column_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_xml.md)
- [msdb: dbo.sp_DTA_insert_reports_querycolumn](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_querycolumn.md)

