# dbo.cost_factor_estimate

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cost_factor_estimate_id | decimal | 9 | 0 | YES |  |  |
| estimate_rate_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| cost_factor_id | smallint | 2 | 1 |  |  |  |
| estimate_pct | float | 8 | 1 |  |  |  |
| estimate_amt | float | 8 | 1 |  |  |  |
| estimation_method | smallint | 2 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |

