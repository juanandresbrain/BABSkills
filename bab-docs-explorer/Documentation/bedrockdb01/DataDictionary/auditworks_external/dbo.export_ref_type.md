# dbo.export_ref_type

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_range_lookup | tinyint | 1 | 0 |  |  |  |
| default_tracking_id | smallint | 2 | 0 |  |  |  |
| reference_no_datatype | char | 1 | 0 |  |  |  |
| reference_no_length | tinyint | 1 | 0 |  |  |  |
| check_digit_routine_number | tinyint | 1 | 0 |  |  |  |
| unique_by_store_key | tinyint | 1 | 0 |  |  |  |
| history_days | smallint | 2 | 0 |  |  |  |
| history_cleanup_criteria | smallint | 2 | 0 |  |  |  |
| low_stock_qty | smallint | 2 | 0 |  |  |  |
| pos_lookup | tinyint | 1 | 0 |  |  |  |
| pos_amount_1_source_column_no | tinyint | 1 | 0 |  |  |  |
| pos_amount_2_source_column_no | tinyint | 1 | 0 |  |  |  |
| pos_amount_3_source_column_no | tinyint | 1 | 0 |  |  |  |
| stock_flag | tinyint | 1 | 0 |  |  |  |
| track_detail_flag | tinyint | 1 | 0 |  |  |  |
| employee_tracking_id | smallint | 2 | 1 |  |  |  |
| import_tracking_id | smallint | 2 | 1 |  |  |  |
| currency_id | numeric | 9 | 1 |  |  |  |
