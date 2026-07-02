# dbo.import_cost_factor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_cost_factor_id | smallint | 2 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| cost_factor_code | nvarchar | 30 | 1 |  |  |  |
| cost_factor_description | nvarchar | 120 | 1 |  |  |  |
| import_flag | bit | 1 | 0 |  |  |  |
| domestic_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| currency_indicator | smallint | 2 | 1 |  |  |  |
| apply_estimate_to | smallint | 2 | 1 |  |  |  |

