# dbo.work_tax_trans_template

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| log_tax_override | tinyint | 1 | 0 |  |  |  |
| store_tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| tod_tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| header_override_flag | tinyint | 1 | 1 |  |  |  |
| all_tax_override_flag | tinyint | 1 | 1 |  |  |  |
