# dbo.mih_sub_trans_line

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
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
| store_balance_group | tinyint | 1 | 0 |  |  |  |
| merchandise_year_no | smallint | 2 | 0 |  |  |  |
| merchandise_month_no | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| units | real | 4 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
| taxable_amount | money | 8 | 0 |  |  |  |
| tax_amount | money | 8 | 0 |  |  |  |
| db_cr_none | smallint | 2 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| balancing_entity_id | numeric | 9 | 1 |  |  |  |
| empl_purch_flag | tinyint | 1 | 1 |  |  |  |
| unit_of_measure | smallint | 2 | 1 |  |  |  |
| gl_account_reference | nvarchar | 40 | 1 |  |  |  |
| applied_by_line_id | numeric | 5 | 1 |  |  |  |
| applied_to_db_cr_none | smallint | 2 | 1 |  |  |  |
