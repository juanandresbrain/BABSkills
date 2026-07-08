# dbo.work_coalition_interface

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| runtime_datetime | datetime | 8 | 0 |  |  |  |
| record_content | nvarchar | 510 | 0 |  |  |  |
| block_type | smallint | 2 | 0 |  |  |  |
| task_no | int | 4 | 0 |  |  |  |
| record_sequence_no | int | 4 | 0 |  |  |  |
| export_module_name | nvarchar | 510 | 1 |  |  |  |
