# dbo.employee_commission_rate_tier

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_ecp_rate_id | numeric | 9 | 0 |  |  |  |
| tier_id | numeric | 5 | 0 | YES |  |  |
| tier_amount_from | money | 8 | 1 |  |  |  |
| tier_amount_to | money | 8 | 1 |  |  |  |
| commission_rate | numeric | 5 | 0 |  |  |  |
| commission_amount_per_item | money | 8 | 0 |  |  |  |
