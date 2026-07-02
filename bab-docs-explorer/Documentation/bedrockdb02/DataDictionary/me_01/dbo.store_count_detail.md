# dbo.store_count_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_count_detail_id | int | 4 | 0 | YES |  |  |
| store_count_id | decimal | 9 | 0 | YES |  |  |
| store_count_area_id | int | 4 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| total_pseudo_cost | decimal | 9 | 1 |  |  |  |
| total_pseudo_retail | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)

