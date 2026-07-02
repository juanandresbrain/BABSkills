# dbo.style_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_detail_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| total_inventory_units | int | 4 | 0 |  |  |  |
| last_net_po_cost | decimal | 9 | 1 |  |  |  |
| last_net_final_po_cost | decimal | 9 | 1 |  |  |  |
| mix_match_rule_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.extend_pack_skus_$sp](../../StoredProcedures/me_01/dbo.extend_pack_skus_$sp.md)
- [me_01: dbo.get_last_net_final_po_cost_$sp](../../StoredProcedures/me_01/dbo.get_last_net_final_po_cost_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.spAvgCostLoop](../../StoredProcedures/me_01/dbo.spAvgCostLoop.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.SPMerchandisingArchiveAverageCost](../../StoredProcedures/me_01/dbo.SPMerchandisingArchiveAverageCost.md)
- [me_01: dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803](../../StoredProcedures/me_01/dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803.md)
- [me_01: dbo.spMerchandisingEmailSuppliesWithoutPackQty](../../StoredProcedures/me_01/dbo.spMerchandisingEmailSuppliesWithoutPackQty.md)
- [me_01: dbo.SPMerchandisingMewVsWMComparison](../../StoredProcedures/me_01/dbo.SPMerchandisingMewVsWMComparison.md)
- [me_01: dbo.spMerchandisingReportMultipleStdPackQty](../../StoredProcedures/me_01/dbo.spMerchandisingReportMultipleStdPackQty.md)
- [me_01: dbo.spMerchandisingReportSupplies](../../StoredProcedures/me_01/dbo.spMerchandisingReportSupplies.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetStyleBySku](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetStyleBySku.md)

