# dbo.wrk_sku_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
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

- [ma_01: dbo.cleanup_wrk_hist_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_hist_$sp.md)
- [ma_01: dbo.post_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_sku_$sp.md)
- [ma_01: dbo.prep_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.prep_hist_sku_$sp.md)
- [ma_01: dbo.prep_wrk_hist_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_hist_$sp.md)
- [ma_01: dbo.validate_hist_$sp](../../StoredProcedures/ma_01/dbo.validate_hist_$sp.md)
- [ma_01: dbo.wpost_hist_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_hist_sku_$sp.md)

