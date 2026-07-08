# dbo.db_install_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | smallint | 2 | 0 |  |  |  |
| module_id | smallint | 2 | 0 |  |  |  |
| object_version_id | int | 4 | 0 |  |  |  |
| object_name | varchar | 200 | 0 |  |  |  |
| object_type_name | varchar | 20 | 0 |  |  |  |
| execution_status | smallint | 2 | 0 |  |  |  |
| error_message | text | 16 | 1 |  |  |  |
