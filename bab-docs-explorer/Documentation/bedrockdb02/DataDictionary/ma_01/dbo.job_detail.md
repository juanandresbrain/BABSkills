# dbo.job_detail

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| job_step_id | smallint | 2 | 0 | YES |  |  |
| time_stamp | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [ma_01: dbo.post_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_group_$sp.md)
- [ma_01: dbo.post_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_sku_$sp.md)
- [ma_01: dbo.post_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_style_$sp.md)
- [ma_01: dbo.post_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_style_color_$sp.md)
- [ma_01: dbo.post_flash_group_$sp](../../StoredProcedures/ma_01/dbo.post_flash_group_$sp.md)
- [ma_01: dbo.post_flash_style_$sp](../../StoredProcedures/ma_01/dbo.post_flash_style_$sp.md)
- [ma_01: dbo.post_hist_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_$sp.md)
- [ma_01: dbo.post_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_sku_$sp.md)
- [ma_01: dbo.post_hist_style_$sp](../../StoredProcedures/ma_01/dbo.post_hist_style_$sp.md)
- [ma_01: dbo.post_hist_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_hist_style_color_$sp.md)
- [ma_01: dbo.post_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_oh_group_$sp.md)
- [ma_01: dbo.post_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oh_sku_$sp.md)
- [ma_01: dbo.post_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_$sp.md)
- [ma_01: dbo.post_oh_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_color_$sp.md)
- [ma_01: dbo.post_oo_group_$sp](../../StoredProcedures/ma_01/dbo.post_oo_group_$sp.md)
- [ma_01: dbo.post_oo_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oo_sku_$sp.md)
- [ma_01: dbo.post_oo_style_$sp](../../StoredProcedures/ma_01/dbo.post_oo_style_$sp.md)
- [ma_01: dbo.post_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_oo_style_color_$sp.md)
- [ma_01: dbo.return_step_exists_$sp](../../StoredProcedures/ma_01/dbo.return_step_exists_$sp.md)

