# dbo.post_cmp_work_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| history_component_id | smallint | 2 | 0 |  |  |  |
| component_units | int | 4 | 0 |  |  |  |
| component_retail | decimal | 9 | 0 |  |  |  |
| component_cost | decimal | 9 | 0 |  |  |  |
| component_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| component_retail_te | decimal | 9 | 1 |  |  |  |
| component_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_cmp_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_styleclr_$sp.md)
- [ma_01: dbo.post_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_cmp_styleclr_$sp.md)

