# dbo.work_rec_entity

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| balancing_entity | nvarchar | 510 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| balancing_store_no | int | 4 | 0 |  |  |  |
| balancing_register_no | smallint | 2 | 0 |  |  |  |
| balancing_cashier_no | int | 4 | 0 |  |  |  |
| balancing_till_no | smallint | 2 | 0 |  |  |  |
| balancing_bank_no | smallint | 2 | 0 |  |  |  |
| store_no_factor | tinyint | 1 | 0 |  |  |  |
| register_no_factor | tinyint | 1 | 0 |  |  |  |
| till_no_factor | tinyint | 1 | 0 |  |  |  |
| cashier_no_factor | tinyint | 1 | 0 |  |  |  |
| bank_no_factor | tinyint | 1 | 0 |  |  |  |
| from_transaction_date | smalldatetime | 4 | 0 |  |  |  |
| period_from_date_time | datetime | 8 | 0 |  |  |  |
| period_to_date_time | datetime | 8 | 0 |  |  |  |
| actual_present_flag | tinyint | 1 | 0 |  |  |  |
| not_rec_flag | int | 4 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| track_qty | tinyint | 1 | 0 |  |  |  |
| short_tolerance_amount | money | 8 | 0 |  |  |  |
| short_tolerance_qty | int | 4 | 0 |  |  |  |
| short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| lower_date_time | datetime | 8 | 0 |  |  |  |
| upper_date_time | datetime | 8 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 1 |  |  |  |
| first_unreconciled_date_time | datetime | 8 | 1 |  |  |  |
| last_activity_date_time | datetime | 8 | 1 |  |  |  |
| last_reconciliation_date_time | datetime | 8 | 1 |  |  |  |
| insert_flag | tinyint | 1 | 0 |  |  |  |
| update_flag | tinyint | 1 | 0 |  |  |  |
| delete_flag | tinyint | 1 | 0 |  |  |  |
| new_last_activity_date_time | datetime | 8 | 1 |  |  |  |
| new_last_rec_date_time | datetime | 8 | 1 |  |  |  |
| locked_by_spid | int | 4 | 1 |  |  |  |
| closeout_balancing_entity_id | numeric | 9 | 1 |  |  |  |
| mrs_foreign_currency_id | numeric | 9 | 1 |  |  |  |
| first_batch_rec_date_time | datetime | 8 | 1 |  |  |  |
| first_batch_rec_date_time_out | datetime | 8 | 1 |  |  |  |
