# dbo.hist_sku_chn_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| size_master_id | int | 4 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| received_units | int | 4 | 0 |  |  |  |
| return_to_vendor_units | int | 4 | 0 |  |  |  |
| distributions_units | int | 4 | 0 |  |  |  |
| transfer_in_units | int | 4 | 0 |  |  |  |
| transfer_out_units | int | 4 | 0 |  |  |  |
| sales_total_units | int | 4 | 0 |  |  |  |
| return_units | int | 4 | 0 |  |  |  |
| shrink_actual_units | int | 4 | 0 |  |  |  |
| adjustments_total_units | int | 4 | 0 |  |  |  |
| shipped_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_sku_modify_hist_$sp](../../StoredProcedures/ma_01/dbo.hk_sku_modify_hist_$sp.md)
- [ma_01: dbo.hk_style_delete_hist_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_$sp.md)
- [ma_01: dbo.post_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_sku_$sp.md)

