# dbo.move_rejection_reason

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| memo1 | nvarchar | 510 | 1 |  |  |  |
| memo2 | nvarchar | 510 | 1 |  |  |  |
| memo3 | nvarchar | 510 | 1 |  |  |  |
