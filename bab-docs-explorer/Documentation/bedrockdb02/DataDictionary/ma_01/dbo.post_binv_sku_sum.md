# dbo.post_binv_sku_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_binv_sku_adj_$sp](../../StoredProcedures/ma_01/dbo.post_binv_sku_adj_$sp.md)
- [ma_01: dbo.post_binv_sku_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_sku_adj_hist_$sp.md)

