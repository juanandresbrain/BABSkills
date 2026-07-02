# dbo.post_hist_sku

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
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

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_oh_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_cmp_sku_$sp.md)

