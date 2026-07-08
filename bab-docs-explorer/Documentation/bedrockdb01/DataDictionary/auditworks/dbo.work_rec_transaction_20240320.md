# dbo.work_rec_transaction_20240320

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_amount_type | tinyint | 1 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| rec_amount | money | 8 | 0 |  |  |  |
| rec_quantity | smallint | 2 | 0 |  |  |  |
| rec_exchange | money | 8 | 0 |  |  |  |
| void_flag | smallint | 2 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 0 |  |  |  |
| period_from_date_time | datetime | 8 | 0 |  |  |  |
| period_to_date_time | datetime | 8 | 0 |  |  |  |
| balancing_store_no | int | 4 | 0 |  |  |  |
| balancing_register_no | smallint | 2 | 0 |  |  |  |
| balancing_cashier_no | int | 4 | 0 |  |  |  |
| balancing_till_no | smallint | 2 | 0 |  |  |  |
| balancing_bank_no | smallint | 2 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| balancing_entity | nvarchar | 510 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| track_qty | tinyint | 1 | 0 |  |  |  |
| short_tolerance_amount | money | 8 | 0 |  |  |  |
| short_tolerance_qty | int | 4 | 0 |  |  |  |
| short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| store_no_factor | tinyint | 1 | 0 |  |  |  |
| register_no_factor | tinyint | 1 | 0 |  |  |  |
| till_no_factor | tinyint | 1 | 0 |  |  |  |
| cashier_no_factor | tinyint | 1 | 0 |  |  |  |
| bank_no_factor | tinyint | 1 | 0 |  |  |  |
| posted_flag | tinyint | 1 | 0 |  |  |  |
| audit_activity_flag | tinyint | 1 | 0 |  |  |  |
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| date_reconciled | smalldatetime | 4 | 1 |  |  |  |
| deposit_slip | nvarchar | 510 | 1 |  |  |  |
| security_seal | nvarchar | 510 | 1 |  |  |  |
