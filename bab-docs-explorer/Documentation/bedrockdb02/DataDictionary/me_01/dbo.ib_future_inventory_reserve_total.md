# dbo.ib_future_inventory_reserve_total

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| reserved_quantity | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.adjust_future_reserve_$sp](../../StoredProcedures/me_01/dbo.adjust_future_reserve_$sp.md)
- [me_01: dbo.eom_complete_$sp](../../StoredProcedures/me_01/dbo.eom_complete_$sp.md)
- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.ins_ib_future_reserve_$sp](../../StoredProcedures/me_01/dbo.ins_ib_future_reserve_$sp.md)

