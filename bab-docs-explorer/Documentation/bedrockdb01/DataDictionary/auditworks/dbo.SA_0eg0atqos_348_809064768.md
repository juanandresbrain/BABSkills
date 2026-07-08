# dbo.SA_0eg0atqos_348_809064768

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
| rec_id | numeric | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| first_unreconciled_date_time | datetime | 8 | 1 |  |  |  |
| last_reconciliation_date_time | datetime | 8 | 1 |  |  |  |
| rec_date | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| till_no | smallint | 2 | 0 |  |  |  |
| bank_no | smallint | 2 | 0 |  |  |  |
| unrec_issue_flag | smallint | 2 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| foreign_currency_code | varchar | 3 | 1 |  |  |  |
| over_short_present | tinyint | 1 | 1 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 1 |  |  |  |
