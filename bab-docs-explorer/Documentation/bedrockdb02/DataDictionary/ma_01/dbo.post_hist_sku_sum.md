# dbo.post_hist_sku_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_oh_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_cmp_sku_$sp.md)

