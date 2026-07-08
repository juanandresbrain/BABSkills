# dbo.work_defer_transaction

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_rejection_reason | smallint | 2 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
