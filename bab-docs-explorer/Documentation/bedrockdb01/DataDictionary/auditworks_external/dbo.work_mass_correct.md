# dbo.work_mass_correct

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| if_reject_flag | tinyint | 1 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| calculated_line_object | smallint | 2 | 1 |  |  |  |
| card_type | nchar | 2 | 1 |  |  |  |
| orig_line_object | smallint | 2 | 1 |  |  |  |
| card_no | numeric | 13 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
