# dbo.work_tax_exception_trans

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_category | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| combined_tax_rate | numeric | 5 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| tax_on_combined_rate | numeric | 5 | 0 |  |  |  |
| tax_amount_collected | money | 8 | 0 |  |  |  |
| tax_amount_expected | money | 8 | 0 |  |  |  |
| history_flag | tinyint | 1 | 1 |  |  |  |
| discrepancy_flag | tinyint | 1 | 0 |  |  |  |
| track_tax | tinyint | 1 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
