# dbo.work_attachment_edit

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| attachment_type | smallint | 2 | 0 |  |  |  |
| note_type | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
