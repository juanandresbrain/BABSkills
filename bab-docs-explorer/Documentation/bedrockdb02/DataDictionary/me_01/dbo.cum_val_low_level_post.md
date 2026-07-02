# dbo.cum_val_low_level_post

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_period_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| merch_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| cost | decimal | 9 | 0 |  |  |  |
| retail | decimal | 9 | 0 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| retail_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.cum_val_hist_lowest_loc_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_lowest_loc_$sp.md)
- [me_01: dbo.ins_cum_val_lowlevel_$sp](../../StoredProcedures/me_01/dbo.ins_cum_val_lowlevel_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

