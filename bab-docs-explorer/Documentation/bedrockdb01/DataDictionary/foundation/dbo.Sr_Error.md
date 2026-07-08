# dbo.Sr_Error

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| error_id | numeric | 13 | 0 | YES |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| error_code | int | 4 | 1 |  |  |  |
| exe_name | varchar | 30 | 1 |  |  |  |
| class_name | varchar | 30 | 1 |  |  |  |
| function_name | varchar | 30 | 1 |  |  |  |
| message | varchar | 255 | 1 |  |  |  |
| error_datetime | datetime | 8 | 1 |  |  |  |
| extended_message | text | 16 | 1 |  |  |  |
