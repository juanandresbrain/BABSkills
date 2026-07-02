# dbo.post_hist_le_group

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| lost_sales_units | float | 8 | 0 |  |  |  |
| extra_sales_units | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_le_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_le_group_$sp.md)

