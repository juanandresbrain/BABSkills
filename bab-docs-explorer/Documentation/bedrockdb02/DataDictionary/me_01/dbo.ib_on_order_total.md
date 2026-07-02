# dbo.ib_on_order_total

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_number | nvarchar | 40 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| total_on_order_units | int | 4 | 0 |  |  |  |
| total_on_order_cost | decimal | 9 | 0 |  |  |  |
| total_on_order_selling_retail | decimal | 9 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| total_on_order_val_retail | decimal | 9 | 0 |  |  |  |
| total_on_order_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_prices_validation_$sp](../../StoredProcedures/me_01/dbo.copy_location_prices_validation_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.ins_ib_on_order_post_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_on_order_post_pc_$sp.md)
- [me_01: dbo.iv_filter_forecasting_styles_$sp](../../StoredProcedures/me_01/dbo.iv_filter_forecasting_styles_$sp.md)
- [me_01: dbo.on_order_update_$sp](../../StoredProcedures/me_01/dbo.on_order_update_$sp.md)
- [me_01: dbo.pcm_pre_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_pre_issue_pc_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_oo_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_oo_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)
- [me_01: dbo.startup_ib_on_order_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_total_$sp.md)

