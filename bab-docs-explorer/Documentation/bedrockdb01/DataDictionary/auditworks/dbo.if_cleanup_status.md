# dbo.if_cleanup_status

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| max_if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| smartview_cleanup | tinyint | 1 | 0 |  |  |  |
| min_if_entry_cleanup | if_entry_datatype | 9 | 1 |  |  |  |
| interface_cleanup_date | smalldatetime | 4 | 1 |  |  |  |
