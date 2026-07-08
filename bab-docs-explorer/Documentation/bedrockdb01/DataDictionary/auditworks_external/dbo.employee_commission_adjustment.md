# dbo.employee_commission_adjustment

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| commission_adj_id | numeric | 9 | 0 | YES |  |  |
| entry_datetime | datetime | 8 | 0 |  |  |  |
| auto_commission_adj_id | numeric | 5 | 1 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 0 |  |  |  |
| primary_selling_area_no | int | 4 | 0 |  |  |  |
| commission_adj_amount | money | 8 | 0 |  |  |  |
| adjustment_description | nvarchar | 510 | 0 |  |  |  |
| auto_rev_pay_pd_end_datetime | datetime | 8 | 1 |  |  |  |
| adjustment_comment | nvarchar | 2000 | 1 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
| adj_hist_posting_datetime | datetime | 8 | 1 |  |  |  |
