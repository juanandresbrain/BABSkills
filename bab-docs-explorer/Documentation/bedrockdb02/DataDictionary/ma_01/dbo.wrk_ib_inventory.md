# dbo.wrk_ib_inventory

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| ib_inventory_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| transaction_val_retail_te | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail_te | decimal | 9 | 0 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_ib_inventory_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_ib_inventory_$sp.md)
- [ma_01: dbo.get_current_period_$sp](../../StoredProcedures/ma_01/dbo.get_current_period_$sp.md)
- [ma_01: dbo.get_current_week_$sp](../../StoredProcedures/ma_01/dbo.get_current_week_$sp.md)
- [ma_01: dbo.get_current_year_$sp](../../StoredProcedures/ma_01/dbo.get_current_year_$sp.md)
- [ma_01: dbo.get_max_wrk_ib_inventory_id_$sp](../../StoredProcedures/ma_01/dbo.get_max_wrk_ib_inventory_id_$sp.md)
- [ma_01: dbo.post_wrk_ib_inventory_$sp](../../StoredProcedures/ma_01/dbo.post_wrk_ib_inventory_$sp.md)
- [ma_01: dbo.post_wrk_ib_inventory_org_$sp](../../StoredProcedures/ma_01/dbo.post_wrk_ib_inventory_org_$sp.md)
- [ma_01: dbo.validate_wrk_ib_inventory_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_inventory_$sp.md)
- [ma_01: dbo.wpost_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_cmp_sku_$sp.md)
- [ma_01: dbo.wpost_flash_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_flash_group_$sp.md)
- [ma_01: dbo.wpost_flash_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_flash_style_$sp.md)
- [ma_01: dbo.wpost_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_hist_sku_$sp.md)
- [ma_01: dbo.wpost_hist_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_hist_style_color_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_group_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_style_color_$sp.md)
- [ma_01: dbo.wpost_iv_hist_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_hist_group_$sp.md)
- [ma_01: dbo.wpost_iv_hist_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_hist_style_$sp.md)
- [ma_01: dbo.wpost_oh_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_oh_group_$sp.md)
- [ma_01: dbo.wpost_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_oh_sku_$sp.md)
- [ma_01: dbo.wpost_oh_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_oh_style_$sp.md)
- [ma_01: dbo.wpost_oh_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_oh_style_color_$sp.md)
- [ma_01: dbo.wprep_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.wprep_cmp_sku_$sp.md)
- [ma_01: dbo.wprep_flash_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_flash_group_$sp.md)
- [ma_01: dbo.wprep_flash_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_flash_style_$sp.md)
- [ma_01: dbo.wprep_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.wprep_hist_sku_$sp.md)
- [ma_01: dbo.wprep_hist_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_hist_style_color_$sp.md)
- [ma_01: dbo.wprep_iv_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_iv_cmp_group_$sp.md)
- [ma_01: dbo.wprep_iv_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_iv_cmp_style_$sp.md)
- [ma_01: dbo.wprep_iv_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_iv_cmp_style_color_$sp.md)
- [ma_01: dbo.wprep_iv_hist_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_iv_hist_group_$sp.md)
- [ma_01: dbo.wprep_iv_hist_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_iv_hist_style_$sp.md)
- [ma_01: dbo.wprep_oh_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_oh_group_$sp.md)
- [ma_01: dbo.wprep_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.wprep_oh_sku_$sp.md)
- [ma_01: dbo.wprep_oh_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_oh_style_$sp.md)
- [ma_01: dbo.wprep_oh_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_oh_style_color_$sp.md)

