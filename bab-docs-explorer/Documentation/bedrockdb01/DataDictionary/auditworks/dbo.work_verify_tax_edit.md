# dbo.work_verify_tax_edit

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_level | tinyint | 1 | 1 |  |  |  |
| tax_rate_code | tinyint | 1 | 1 |  |  |  |
| exception_flag | tinyint | 1 | 0 |  |  |  |
