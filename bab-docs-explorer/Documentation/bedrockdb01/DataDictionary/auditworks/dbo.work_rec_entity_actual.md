# dbo.work_rec_entity_actual

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 1 |  |  |  |
| mrt_balancing_entity_id | numeric | 9 | 1 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| track_qty | tinyint | 1 | 0 |  |  |  |
| short_tolerance_amount | money | 8 | 0 |  |  |  |
| short_tolerance_qty | int | 4 | 0 |  |  |  |
| short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| lower_date_time | datetime | 8 | 0 |  |  |  |
| upper_date_time | datetime | 8 | 0 |  |  |  |
| last_activity_date_time | datetime | 8 | 1 |  |  |  |
| last_reconciliation_date_time | datetime | 8 | 1 |  |  |  |
| closeout_balancing_entity_id | numeric | 9 | 1 |  |  |  |
| first_batch_rec_date_time | datetime | 8 | 1 |  |  |  |
| from_transaction_date | smalldatetime | 4 | 0 |  |  |  |
| actual_present_flag | tinyint | 1 | 0 |  |  |  |
