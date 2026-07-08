# dbo.cust_liab_processing_rule

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rule_id | nvarchar | 6 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| rule_id_description | nvarchar | 510 | 1 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| line_object_offset | smallint | 2 | 0 |  |  |  |
| line_action_offset | tinyint | 1 | 0 |  |  |  |
| line_object_balance | smallint | 2 | 1 |  |  |  |
| line_action_balance | tinyint | 1 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| reference_no_qty_per_trans | numeric | 5 | 0 |  |  |  |
| next_reference_no | nvarchar | 40 | 1 |  |  |  |
| generate_reference_no | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| balance_adjustment_type | smallint | 2 | 1 |  |  |  |
| balance_adjustment_amount | money | 8 | 1 |  |  |  |
| balance_exclusion_column_no | tinyint | 1 | 1 |  |  |  |
| processing_activation_type | smallint | 2 | 1 |  |  |  |
| age_selection_criteria | smallint | 2 | 1 |  |  |  |
| processing_day | tinyint | 1 | 1 |  |  |  |
| last_processing_date | datetime | 8 | 1 |  |  |  |
| inactivity_selection_criteria | smallint | 2 | 1 |  |  |  |
| rule_active_flag | tinyint | 1 | 0 |  |  |  |
| last_updated_by_system | tinyint | 1 | 0 |  |  |  |
