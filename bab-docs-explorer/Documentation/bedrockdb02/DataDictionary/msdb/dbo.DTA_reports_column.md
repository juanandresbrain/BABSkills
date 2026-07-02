# dbo.DTA_reports_column

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ColumnID | int | 4 | 0 | YES |  |  |
| TableID | int | 4 | 0 |  | YES |  |
| ColumnName | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_column_access_helper_relational](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_relational.md)
- [msdb: dbo.sp_DTA_column_access_helper_xml](../../StoredProcedures/msdb/dbo.sp_DTA_column_access_helper_xml.md)
- [msdb: dbo.sp_DTA_get_columntableids](../../StoredProcedures/msdb/dbo.sp_DTA_get_columntableids.md)
- [msdb: dbo.sp_DTA_insert_reports_column](../../StoredProcedures/msdb/dbo.sp_DTA_insert_reports_column.md)

