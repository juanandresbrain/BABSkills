# dbo.employee_open_allocation

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| source_empl_trans_summary_id | numeric | 9 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 1 |  |  |  |
| primary_selling_area_no | int | 4 | 1 |  |  |  |
| transaction_store_no_flag | int | 4 | 0 |  |  |  |
| transaction_store_no | int | 4 | 0 |  |  |  |
| item_commission_code | nvarchar | 40 | 1 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| store_commission_code | nvarchar | 40 | 1 |  |  |  |
| transaction_net_amount | money | 8 | 0 |  |  |  |
| transaction_discount_amount | money | 8 | 0 |  |  |  |
| transaction_units | numeric | 9 | 0 |  |  |  |
| source_allocation_type | nvarchar | 40 | 1 |  |  |  |
| comparison_type | smallint | 2 | 0 |  |  |  |
| relationship_type | nvarchar | 40 | 1 |  |  |  |
| relationship_position | nvarchar | 8 | 1 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 0 |  |  |  |
| accumulation_basis | smallint | 2 | 0 |  |  |  |
| accum_basis_calendar_level | smallint | 2 | 0 |  |  |  |
| selling_area_flag | tinyint | 1 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| basis_calendar_period_quantity | smallint | 2 | 0 |  |  |  |
