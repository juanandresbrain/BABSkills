# dbo.cum_val_history

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| calendar_period_id | decimal | 9 | 0 | YES |  |  |
| location_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| cum_val_cost | decimal | 9 | 0 |  |  |  |
| cum_val_retail | decimal | 9 | 0 |  |  |  |
| initial_val_flag | decimal | 5 | 0 | YES |  |  |
| cum_val_cost_local | decimal | 9 | 1 |  |  |  |
| cum_val_retail_local | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.cum_val_hist_lowest_loc_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_lowest_loc_$sp.md)
- [me_01: dbo.init_val_onhand_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_$sp.md)
- [me_01: dbo.init_val_onhand_deltemp_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_deltemp_$sp.md)
- [me_01: dbo.init_val_onhand_deltemp_ll_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_deltemp_ll_$sp.md)
- [me_01: dbo.init_val_onhand_lowestloc_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_lowestloc_$sp.md)
- [me_01: dbo.initvalccpergrpgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrp_$sp.md)
- [me_01: dbo.initvalccpergrpgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrpdel_$sp.md)
- [me_01: dbo.initvalccpergrploc_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrploc_$sp.md)
- [me_01: dbo.initvalccpergrplocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrplocdel_$sp.md)
- [me_01: dbo.initvalccperlocgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrp_$sp.md)
- [me_01: dbo.initvalccperlocgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrpdel_$sp.md)
- [me_01: dbo.initvalccperlocloc_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocloc_$sp.md)
- [me_01: dbo.initvalccperloclocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperloclocdel_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.startup_sl_history_single_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_single_jurisdiction_$sp.md)

