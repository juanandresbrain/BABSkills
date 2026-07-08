# dbo.ecp_reference_amt

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ecp_reference_amt_id | numeric | 9 | 0 | YES |  |  |
| reference_amount_type | smallint | 2 | 0 |  |  |  |
| effective_from_datetime | datetime | 8 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 1 |  |  |  |
| reference_amount | money | 8 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| selling_area_no | int | 4 | 0 |  |  |  |
| position_code | nvarchar | 8 | 0 |  |  |  |
| auto_adj_id | numeric | 5 | 1 |  |  |  |
| auto_adj_period_end_datetime | datetime | 8 | 1 |  |  |  |
| last_updated_by_transaction_id | numeric | 9 | 1 |  |  |  |
| adj_hist_posting_datetime | datetime | 8 | 1 |  |  |  |
