# dbo.ib_future_inventory_reserve

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_future_inventory_reserve_id | bigint | 8 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| reserved_quantity | int | 4 | 0 |  |  |  |
| date_reserved | datetime | 8 | 0 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.ins_ib_future_reserve_$sp](../../StoredProcedures/me_01/dbo.ins_ib_future_reserve_$sp.md)

