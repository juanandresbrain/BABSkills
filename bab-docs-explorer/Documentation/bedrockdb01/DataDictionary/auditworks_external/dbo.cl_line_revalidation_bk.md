# dbo.cl_line_revalidation_bk

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| reference_no | nvarchar | 510 | 1 |  |  |  |
| validation_id | nvarchar | 510 | 1 |  |  |  |
