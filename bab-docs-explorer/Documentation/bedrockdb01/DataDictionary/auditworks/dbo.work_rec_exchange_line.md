# dbo.work_rec_exchange_line

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| void_flag | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| carryforward_flag | tinyint | 1 | 1 |  |  |  |
| min_rec_type | smallint | 2 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| date_reconciled | smalldatetime | 4 | 1 |  |  |  |
