# dbo.work_oim_template

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_status_flag | smallint | 2 | 0 |  |  |  |
| all_rejects_fixed | tinyint | 1 | 0 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| validation_id | nvarchar | 510 | 1 |  |  |  |
| validation_description | nvarchar | 510 | 1 |  |  |  |
| tab_delimited_token_list | nvarchar | 510 | 1 |  |  |  |
