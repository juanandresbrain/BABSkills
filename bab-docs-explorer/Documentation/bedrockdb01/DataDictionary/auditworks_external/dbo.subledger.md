# dbo.subledger

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | smallint | 2 | 0 |  |  |  |
| period | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| gl_account_id | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
| units | real | 4 | 0 |  |  |  |
| transaction_qty | int | 4 | 0 |  |  |  |
| store_balance_group | tinyint | 1 | 0 |  |  |  |
| posting_status | tinyint | 1 | 0 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| posting_datetime | datetime | 8 | 1 |  |  |  |
| data_source | tinyint | 1 | 1 |  |  |  |
| gl_posting_datetime | datetime | 8 | 1 |  |  |  |
| last_modified_date_time | datetime | 8 | 1 |  |  |  |
| unit_of_measure | smallint | 2 | 1 |  |  |  |
