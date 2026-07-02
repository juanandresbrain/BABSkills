# dbo.style_parent

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_level_id | int | 4 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 | YES |  |  |
| parent_hierarchy_group_id | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchAnalyticsReportTrappedCostInTransit](../../StoredProcedures/me_01/dbo.spMerchAnalyticsReportTrappedCostInTransit.md)
- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc.md)
- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual.md)
- [DBAUtility: dbo.spPFTGetOpenToByRollingCountsAndAttributes](../../StoredProcedures/DBAUtility/dbo.spPFTGetOpenToByRollingCountsAndAttributes.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.nsb_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_vendor_analysis_$sp.md)
- [ma_01: dbo.rpt_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)
- [ma_01: dbo.rpt_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_vendor_analysis_$sp.md)
- [ma_01: dbo.spDW_Inventory](../../StoredProcedures/ma_01/dbo.spDW_Inventory.md)
- [ma_01: dbo.spDW_TopStyleTy](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTy.md)
- [ma_01: dbo.spDW_TopStyleTyBACKUP20180108](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTyBACKUP20180108.md)
- [ma_01: dbo.spTimCTopStyleTesting](../../StoredProcedures/ma_01/dbo.spTimCTopStyleTesting.md)

