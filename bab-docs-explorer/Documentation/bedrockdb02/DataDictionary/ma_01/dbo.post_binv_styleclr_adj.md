# dbo.post_binv_styleclr_adj

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| adjustment_units | int | 4 | 0 |  |  |  |
| adjustment_retail | decimal | 9 | 0 |  |  |  |
| adjustment_retail_te | decimal | 9 | 0 |  |  |  |
| adjustment_retail_local | decimal | 9 | 1 |  |  |  |
| adjustment_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_binv_stlclr_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_stlclr_adj_hist_$sp.md)
- [ma_01: dbo.post_binv_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_binv_styleclr_$sp.md)
- [ma_01: dbo.post_binv_styleclr_adj_$sp](../../StoredProcedures/ma_01/dbo.post_binv_styleclr_adj_$sp.md)

