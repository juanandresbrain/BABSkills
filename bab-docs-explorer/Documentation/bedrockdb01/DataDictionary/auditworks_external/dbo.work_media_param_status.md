# dbo.work_media_param_status

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| return_status | int | 4 | 0 |  |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| old_effective_from_date | datetime | 8 | 1 |  |  |  |
| ENTRY_ID | binary | 16 | 0 |  |  |  |
