# dbo.hist_le_style_chn_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| lost_sales_units | float | 8 | 0 |  |  |  |
| extra_sales_units | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_le_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_le_$sp.md)
- [ma_01: dbo.post_hist_le_$sp](../../StoredProcedures/ma_01/dbo.post_hist_le_$sp.md)
- [ma_01: dbo.reclass_hist_le_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_le_$sp.md)

