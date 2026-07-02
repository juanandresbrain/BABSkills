# dbo.price_status

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_code | nvarchar | 6 | 0 |  |  |  |
| price_status_desc | nvarchar | 40 | 0 |  |  |  |
| alloc_replen_price_point | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.get_retails_MA_$sp](../../StoredProcedures/me_01/dbo.get_retails_MA_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_style_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_styleclr_vld_$sp.md)
- [ma_01: dbo.import_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_group_$sp.md)
- [ma_01: dbo.import_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_sku_$sp.md)
- [ma_01: dbo.import_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_style_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.nsb_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_chain_md_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)

