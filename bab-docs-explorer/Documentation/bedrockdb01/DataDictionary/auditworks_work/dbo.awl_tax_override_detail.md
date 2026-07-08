# dbo.awl_tax_override_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_category | smallint | 2 | 0 |  |  |  |
| taxable | tinyint | 1 | 1 |  |  |  |
| exception_tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| tax_exempt_no | nvarchar | 40 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
