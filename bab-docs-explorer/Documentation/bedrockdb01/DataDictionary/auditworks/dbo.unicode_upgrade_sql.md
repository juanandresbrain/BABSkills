# dbo.unicode_upgrade_sql

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| unicode_upgrade_entry_id | numeric | 9 | 0 | YES |  |  |
| unicode_upgrade_entry_datetime | datetime | 8 | 0 |  |  |  |
| table_name | nvarchar | 510 | 0 |  |  |  |
| table_type | nvarchar | 510 | 0 |  |  |  |
| table_object_name | nvarchar | 510 | 0 |  |  |  |
| drop_sql_cmd | nvarchar | 8000 | 1 |  |  |  |
| drop_sequence | tinyint | 1 | 0 |  |  |  |
| alter_sql_cmd | nvarchar | 8000 | 1 |  |  |  |
| create_sql_cmd | nvarchar | 8000 | 1 |  |  |  |
| create_sql_cmd_suffix | nvarchar | 8000 | 1 |  |  |  |
| create_sequence | tinyint | 1 | 0 |  |  |  |
| drop_done | datetime | 8 | 1 |  |  |  |
| alter_done | datetime | 8 | 1 |  |  |  |
| create_done | datetime | 8 | 1 |  |  |  |
