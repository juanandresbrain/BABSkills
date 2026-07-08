# dbo.work_rejection_reason

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| deferred | tinyint | 1 | 0 |  |  |  |
| memo1 | nvarchar | 510 | 1 |  |  |  |
| memo2 | nvarchar | 510 | 1 |  |  |  |
| memo3 | nvarchar | 510 | 1 |  |  |  |
| replace_upc_no | numeric | 9 | 1 |  |  |  |
| replace_line_object | smallint | 2 | 1 |  |  |  |
| replace_line_action | smallint | 2 | 1 |  |  |  |
| process_id | binary | 16 | 1 |  |  |  |
| lookup_key1 | int | 4 | 1 |  |  |  |
