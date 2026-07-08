# dbo.employee_trans_summary

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| empl_trans_summary_id | numeric | 9 | 0 | YES |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 0 |  |  |  |
| primary_selling_area_no | int | 4 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| transaction_store_no | int | 4 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| employee_commission_code | nvarchar | 40 | 0 |  |  |  |
| item_commission_code | nvarchar | 40 | 0 |  |  |  |
| store_commission_code | nvarchar | 40 | 0 |  |  |  |
| transaction_net_amount | money | 8 | 0 |  |  |  |
| transaction_discount_amount | money | 8 | 0 |  |  |  |
| transaction_units | numeric | 9 | 0 |  |  |  |
| transaction_quantity | money | 8 | 0 |  |  |  |
| transaction_quantity_adj | money | 8 | 0 |  |  |  |
| tier_id | numeric | 5 | 1 |  |  |  |
| commission_rate | numeric | 5 | 1 |  |  |  |
| commission_amount_per_item | money | 8 | 1 |  |  |  |
| source_allocation_type | nvarchar | 40 | 1 |  |  |  |
| source_empl_trans_summary_id | numeric | 9 | 1 |  |  |  |
| transaction_quantity_adj_mdsfe | money | 8 | 1 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
