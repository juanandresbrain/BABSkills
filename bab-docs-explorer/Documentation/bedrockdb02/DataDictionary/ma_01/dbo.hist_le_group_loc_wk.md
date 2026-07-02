# dbo.hist_le_group_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| lost_sales_units | float | 8 | 0 |  |  |  |
| extra_sales_units | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_le_$sp](../../StoredProcedures/ma_01/dbo.post_hist_le_$sp.md)
- [ma_01: dbo.post_hist_le_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_le_group_$sp.md)
- [ma_01: dbo.reclass_hist_le_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_le_$sp.md)

