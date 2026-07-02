# dbo.history_period

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| history_period_id | decimal | 9 | 0 | YES |  |  |
| calendar_period_id | decimal | 9 | 0 |  |  |  |
| gl_period_id | decimal | 9 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.cum_val_hist_lowest_loc_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_lowest_loc_$sp.md)
- [me_01: dbo.get_oh_0_slpd_ty_$fn](../../StoredProcedures/me_01/dbo.get_oh_0_slpd_ty_$fn.md)
- [me_01: dbo.get_sl_pdoh_$fn](../../StoredProcedures/me_01/dbo.get_sl_pdoh_$fn.md)
- [me_01: dbo.get_sl_yroh_$fn](../../StoredProcedures/me_01/dbo.get_sl_yroh_$fn.md)
- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
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
- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_oh_$sp.md)
- [me_01: dbo.sl_hist_ins_rim_$sp](../../StoredProcedures/me_01/dbo.sl_hist_ins_rim_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.startup_sl_history_single_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_single_jurisdiction_$sp.md)

