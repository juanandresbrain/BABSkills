# dbo.imp_cost_factor_estimate

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_cost_factor_estimate_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| estimation_type | smallint | 2 | 1 |  |  |  |
| estimate_rate_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| cost_factor_code | nvarchar | 30 | 1 |  |  |  |
| estimate_pct | float | 8 | 1 |  |  |  |
| estimate_amt | float | 8 | 1 |  |  |  |
| estimation_method | smallint | 2 | 1 |  |  |  |

