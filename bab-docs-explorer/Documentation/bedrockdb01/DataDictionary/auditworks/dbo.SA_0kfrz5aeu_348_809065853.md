# dbo.SA_0kfrz5aeu_348_809065853

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| display_balancing_entity | varchar | 500 | 0 |  |  |  |
| display_balancing_entity_descr | varchar | 500 | 0 |  |  |  |
| balancing_entity_key | varchar | 500 | 0 |  |  |  |
| rec_amount_type | smallint | 2 | 0 |  |  |  |
| rec_id | numeric | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| current_activity | money | 8 | 0 |  |  |  |
| period_from_date_time | datetime | 8 | 0 |  |  |  |
| period_to_date_time | datetime | 8 | 0 |  |  |  |
| period_expected | money | 8 | 0 |  |  |  |
| period_actual | money | 8 | 1 |  |  |  |
| over_short | money | 8 | 1 |  |  |  |
| rec_store | int | 4 | 0 |  |  |  |
| rec_register | smallint | 2 | 0 |  |  |  |
| bal_cashier | int | 4 | 0 |  |  |  |
| bal_till | smallint | 2 | 0 |  |  |  |
| rec_date | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| reconciled | smallint | 2 | 0 |  |  |  |
| issue_flag | smallint | 2 | 0 |  |  |  |
| audit_activity_flag | smallint | 2 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| foreign_currency_code | varchar | 3 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| reconcilable | tinyint | 1 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 1 |  |  |  |
| date_reconciled | datetime | 8 | 1 |  |  |  |
