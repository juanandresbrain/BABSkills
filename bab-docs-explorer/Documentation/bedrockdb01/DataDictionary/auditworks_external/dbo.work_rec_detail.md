# dbo.work_rec_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| rec_amount_type | tinyint | 1 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
| rec_amount | money | 8 | 0 |  |  |  |
| rec_quantity | smallint | 2 | 0 |  |  |  |
| rec_exchange | money | 8 | 0 |  |  |  |
| period_from_date_time | datetime | 8 | 0 |  |  |  |
| period_to_date_time | datetime | 8 | 0 |  |  |  |
| rec_id | tran_id_datatype | 9 | 0 |  |  |  |
| rec_date | smalldatetime | 4 | 1 |  |  |  |
| rec_date_time | datetime | 8 | 0 |  |  |  |
| issue_flag | smallint | 2 | 0 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| audit_activity_flag | smallint | 2 | 0 |  |  |  |
| track_qty | tinyint | 1 | 1 |  |  |  |
