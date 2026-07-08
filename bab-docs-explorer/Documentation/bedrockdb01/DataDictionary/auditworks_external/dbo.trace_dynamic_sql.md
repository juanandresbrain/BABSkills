# dbo.trace_dynamic_sql

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| trace_entry_id | numeric | 9 | 0 | YES |  |  |
| trace_entry_datetime | datetime | 8 | 0 |  |  |  |
| process_name | nvarchar | 200 | 1 |  |  |  |
| sql_command | nvarchar | -1 | 1 |  |  |  |
| errmsg | nvarchar | 4000 | 1 |  |  |  |
| object_name | nvarchar | 510 | 1 |  |  |  |
| operation_name | nvarchar | 200 | 1 |  |  |  |
