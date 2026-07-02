# dbo.forecasted_min_max_rule

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecasted_min_max_rule_id | T_ID | 16 | 0 | YES |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| hierarchy_group_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| min_wos | int | 4 | 0 |  |  |  |
| max_wos | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

