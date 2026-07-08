# dbo.work_trans_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| insertion_date | datetime | 8 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| store_name | nvarchar | 510 | 0 |  |  |  |
| currency_code | nchar | 6 | 1 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_category | nvarchar | 510 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_remark | nvarchar | 2000 | 1 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 1 |  |  |  |
| issue_type | nvarchar | 2000 | 0 |  |  |  |
| void_reason | nvarchar | 510 | 0 |  |  |  |
| language_id | smallint | 2 | 0 |  |  |  |
| tax_override_flag | tinyint | 1 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
