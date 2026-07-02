# dbo.post_oo_all_sku_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_oo_all_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_sku_$sp.md)

