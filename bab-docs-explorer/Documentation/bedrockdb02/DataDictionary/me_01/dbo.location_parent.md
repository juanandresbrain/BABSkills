# dbo.location_parent

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_level_id | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| parent_hierarchy_group_id | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.init_val_onhand_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_$sp.md)
- [me_01: dbo.init_val_onhand_deltemp_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_deltemp_$sp.md)
- [me_01: dbo.initvalccpergrpgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrp_$sp.md)
- [me_01: dbo.initvalccpergrpgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrpdel_$sp.md)
- [me_01: dbo.initvalccpergrploc_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrploc_$sp.md)
- [me_01: dbo.initvalccpergrplocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrplocdel_$sp.md)
- [me_01: dbo.initvalccperlocgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrp_$sp.md)
- [me_01: dbo.initvalccperlocgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrpdel_$sp.md)
- [me_01: dbo.initvalccperlocloc_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocloc_$sp.md)
- [me_01: dbo.initvalccperloclocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperloclocdel_$sp.md)
- [me_01: dbo.update_location_position_$sp](../../StoredProcedures/me_01/dbo.update_location_position_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.rpt_otb_cost_retail_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_cost_retail_$sp.md)
- [ma_01: dbo.rpt_otb_location_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_location_$sp.md)

