# dbo.work_auto_complete_trans_hdr

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| reversal_sign | smallint | 2 | 0 |  |  |  |
| not_found_flag | tinyint | 1 | 0 |  |  |  |
| auto_complete_transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
