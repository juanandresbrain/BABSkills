# dbo.hist_cmp_styleclr_chn_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| merch_year | smallint | 2 | 0 | YES |  |  |
| component_type_code | smallint | 2 | 0 | YES |  |  |
| history_component_id | smallint | 2 | 0 | YES |  |  |
| component_units | int | 4 | 0 |  |  |  |
| component_retail | decimal | 9 | 0 |  |  |  |
| component_cost | decimal | 9 | 0 |  |  |  |
| component_retail_te | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_cmp_$sp.md)
- [ma_01: dbo.post_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_style_color_$sp.md)
- [ma_01: dbo.post_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_styleclr_$sp.md)

