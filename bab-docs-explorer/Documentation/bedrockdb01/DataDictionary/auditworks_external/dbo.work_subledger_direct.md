# dbo.work_subledger_direct

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
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
| units | real | 4 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
