# dbo.SA_0ml4diaf4_137_711415862

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_code | varchar | 3 | 1 |  |  |  |
| gl_account_id | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| posting_datetime | datetime | 8 | 1 |  |  |  |
| gl_posting_status | tinyint | 1 | 1 |  |  |  |
| gl_posting_datetime | datetime | 8 | 1 |  |  |  |
| transaction_qty | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| data_source | tinyint | 1 | 1 |  |  |  |
| fiscal_year | smallint | 2 | 0 |  |  |  |
| period | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| store_balance_group | tinyint | 1 | 0 |  |  |  |
| units | real | 4 | 0 |  |  |  |
| unit_of_measure | smallint | 2 | 0 |  |  |  |
| original_amount | money | 8 | 1 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
