# dbo.hist_oh_style_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |
| on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |
| on_hand_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc.md)
- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual.md)
- [ma_01: dbo.hk_style_delete_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_oh_$sp.md)
- [ma_01: dbo.hk_style_reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_reclass_hist_oh_$sp.md)
- [ma_01: dbo.post_binv_style_$sp](../../StoredProcedures/ma_01/dbo.post_binv_style_$sp.md)
- [ma_01: dbo.post_hist_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_style_$sp.md)
- [ma_01: dbo.post_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_pd_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_yr_$sp.md)

