# dbo.subledger_work_area

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| store_deposit_destination | smallint | 2 | 0 |  |  |  |
| discounted_line_object | int | 4 | 0 |  |  |  |
| return_from_store | int | 4 | 0 |  |  |  |
| card_type | nchar | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| gl_account_id | int | 4 | 0 |  |  |  |
| transaction_qty | int | 4 | 0 |  |  |  |
| store_balance_group | tinyint | 1 | 0 |  |  |  |
| fiscal_year | smallint | 2 | 0 |  |  |  |
| period | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
| data_source | tinyint | 1 | 1 |  |  |  |
| taxable | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| empl_purch_flag | tinyint | 1 | 0 |  |  |  |
| failed_lookup_type | tinyint | 1 | 1 |  |  |  |
| failed_lookup_value | nvarchar | 510 | 1 |  |  |  |
| invalid_account_no | nvarchar | 320 | 1 |  |  |  |
| unit_of_measure | smallint | 2 | 1 |  |  |  |
| gl_account_reference | nvarchar | 40 | 1 |  |  |  |
