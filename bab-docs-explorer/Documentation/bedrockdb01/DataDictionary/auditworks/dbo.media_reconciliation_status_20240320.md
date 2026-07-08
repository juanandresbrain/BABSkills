# dbo.media_reconciliation_status_20240320

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| balancing_entity_id | numeric | 9 | 0 | YES |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| balancing_entity | nvarchar | 510 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| display_balancing_entity | nvarchar | 1000 | 0 |  |  |  |
| display_balancing_entity_descr | nvarchar | 1000 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| till_no | smallint | 2 | 0 |  |  |  |
| bank_no | smallint | 2 | 0 |  |  |  |
| first_unreconciled_date_time | datetime | 8 | 1 |  |  |  |
| last_activity_date_time | datetime | 8 | 1 |  |  |  |
| last_reconciliation_date_time | datetime | 8 | 1 |  |  |  |
| unreconciled_activity_amount | money | 8 | 0 |  |  |  |
| unreconciled_exchange_amount | money | 8 | 0 |  |  |  |
| current_balance_amount | money | 8 | 0 |  |  |  |
| current_balance_exchange_amt | money | 8 | 0 |  |  |  |
| last_locked_by_process_no | smallint | 2 | 1 |  |  |  |
| locked_by_spid | int | 4 | 1 |  |  |  |
| last_lock_datetime | datetime | 8 | 1 |  |  |  |
| unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| foreign_currency_code | nchar | 6 | 1 |  |  |  |
| last_locked_by_user_id | int | 4 | 1 |  |  |  |
