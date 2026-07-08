# dbo.Sr_Trace

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| trace_id | numeric | 13 | 0 | YES |  |  |
| execution_id | int | 4 | 1 |  |  |  |
| exe_name | varchar | 30 | 1 |  |  |  |
| class_name | varchar | 30 | 1 |  |  |  |
| function_name | varchar | 30 | 1 |  |  |  |
| message | varchar | 255 | 1 |  |  |  |
| indent_level | int | 4 | 1 |  |  |  |
| trace_datetime | datetime | 8 | 1 |  |  |  |
| extended_message | text | 16 | 1 |  |  |  |
| severity | smallint | 2 | 0 |  |  |  |
