# dbo.sl_history_sum_post

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_hierarchy_group_id | int | 4 | 0 |  |  |  |
| history_period_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| sl_component_id | decimal | 9 | 0 |  |  |  |
| history_value | decimal | 9 | 0 |  |  |  |
| history_value_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ins_slhist_sum_post_$sp](../../StoredProcedures/me_01/dbo.ins_slhist_sum_post_$sp.md)
- [me_01: dbo.rim_post_$sp](../../StoredProcedures/me_01/dbo.rim_post_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

