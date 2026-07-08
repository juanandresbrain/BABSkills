# dbo.work_av_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| archive_handling_method | smallint | 2 | 1 |  |  |  |
| exception_flag | tinyint | 1 | 0 |  |  |  |
