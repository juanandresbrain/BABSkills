# dbo.ap_work_area

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| tax_jurisdiction | char | 5 | 0 |  |  |  |
| store_deposit_destination | smallint | 2 | 0 |  |  |  |
| discounted_line_object | int | 4 | 0 |  |  |  |
| return_from_store | int | 4 | 0 |  |  |  |
| card_type | char | 1 | 0 |  |  |  |
| transaction_date | char | 6 | 0 |  |  |  |
| gl_account_id | int | 4 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| amount | int | 4 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 1 |  |  |  |
