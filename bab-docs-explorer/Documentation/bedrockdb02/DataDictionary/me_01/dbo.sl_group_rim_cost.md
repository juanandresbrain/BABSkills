# dbo.sl_group_rim_cost

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sl_group_rim_cost_id | decimal | 9 | 0 |  |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| history_period_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| sl_component_id | decimal | 9 | 0 | YES |  |  |
| value | decimal | 9 | 0 |  |  |  |
| value_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.startup_sl_history_single_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_single_jurisdiction_$sp.md)

