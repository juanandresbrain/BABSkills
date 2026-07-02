# dbo.post_binv_group_adj

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| adjustment_units | int | 4 | 0 |  |  |  |
| adjustment_cost | decimal | 9 | 0 |  |  |  |
| adjustment_retail | decimal | 9 | 0 |  |  |  |
| adjustment_retail_te | decimal | 9 | 0 |  |  |  |
| adjustment_retail_local | decimal | 9 | 1 |  |  |  |
| adjustment_retail_te_local | decimal | 9 | 1 |  |  |  |
| adjustment_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_binv_group_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_$sp.md)
- [ma_01: dbo.post_binv_group_adj_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_adj_$sp.md)
- [ma_01: dbo.post_binv_group_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_adj_hist_$sp.md)

