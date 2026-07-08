# dbo.work_upc

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| upc_exist | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
