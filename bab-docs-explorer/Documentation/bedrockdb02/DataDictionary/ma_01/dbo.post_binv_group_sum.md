# dbo.post_binv_group_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail_te | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 1 |  |  |  |
| transaction_selling_retail_te | decimal | 9 | 1 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_binv_group_adj_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_adj_$sp.md)
- [ma_01: dbo.post_binv_group_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_adj_hist_$sp.md)

