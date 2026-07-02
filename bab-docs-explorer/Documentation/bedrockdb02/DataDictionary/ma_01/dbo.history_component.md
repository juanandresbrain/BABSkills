# dbo.history_component

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| history_component_id | smallint | 2 | 0 | YES |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| reason_price_status_id | smallint | 2 | 0 |  |  |  |
| component_description | nvarchar | 120 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_group_$sp.md)
- [ma_01: dbo.import_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_sku_$sp.md)
- [ma_01: dbo.import_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_style_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.nsb_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_chain_md_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.nsb_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_vendor_analysis_$sp.md)
- [ma_01: dbo.post_cmp_work_group_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_group_$sp.md)
- [ma_01: dbo.post_cmp_work_sku_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_sku_$sp.md)
- [ma_01: dbo.post_cmp_work_style_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_style_$sp.md)
- [ma_01: dbo.post_cmp_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_styleclr_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.rpt_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_vendor_analysis_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_group_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_color_$sp.md)
- [ma_01: dbo.wpost_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_cmp_sku_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_group_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_color_$sp.md)

