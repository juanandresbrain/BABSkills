# dbo.work_rec_actual

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| period_to_date_time | datetime | 8 | 0 |  |  |  |
| rec_id | tran_id_datatype | 9 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| rec_group_line_object | smallint | 2 | 1 |  |  |  |
| amt_action | tinyint | 1 | 1 |  |  |  |
| qty_action | tinyint | 1 | 1 |  |  |  |
| exchange_action | tinyint | 1 | 1 |  |  |  |
| actual_flag | tinyint | 1 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 1 |  |  |  |
| rec_amount | money | 8 | 0 |  |  |  |
| rec_quantity | smallint | 2 | 0 |  |  |  |
| rec_exchange | money | 8 | 0 |  |  |  |
| rec_exchange_calc | money | 8 | 0 |  |  |  |
| max_void_flag | smallint | 2 | 0 |  |  |  |
| min_void_flag | smallint | 2 | 0 |  |  |  |
| audit_activity_flag | smallint | 2 | 0 |  |  |  |
| lower_date_time | datetime | 8 | 0 |  |  |  |
| multiple_actual_handling_code | tinyint | 1 | 0 |  |  |  |
| next_closeout_date_time | datetime | 8 | 1 |  |  |  |
| final_rec_date_time | datetime | 8 | 1 |  |  |  |
| final_rec_id | tran_id_datatype | 9 | 1 |  |  |  |
| final_flag | tinyint | 1 | 0 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| track_qty | tinyint | 1 | 1 |  |  |  |
| short_tolerance_amount | money | 8 | 1 |  |  |  |
| short_tolerance_qty | int | 4 | 1 |  |  |  |
| short_tolerance_percent | numeric | 5 | 1 |  |  |  |
| date_reconciled | smalldatetime | 4 | 1 |  |  |  |
| amt_action_object | numeric | 5 | 1 |  |  |  |
| exchange_action_object | numeric | 5 | 1 |  |  |  |
