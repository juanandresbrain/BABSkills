# dbo.sl_component_rim_map

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sl_component_rim_map_id | decimal | 9 | 0 | YES |  |  |
| sl_component_id | decimal | 9 | 0 |  |  |  |
| apply_to_sl_component_id | decimal | 9 | 0 |  |  |  |
| operator | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

