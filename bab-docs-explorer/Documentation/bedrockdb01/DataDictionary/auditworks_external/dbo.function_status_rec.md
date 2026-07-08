# dbo.function_status_rec

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 | YES |  |  |
| process_id | binary | 16 | 0 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| rec_status | tinyint | 1 | 0 |  |  |  |
| try_again | tinyint | 1 | 0 |  |  |  |
| edit_process_no | tinyint | 1 | 1 |  |  |  |
