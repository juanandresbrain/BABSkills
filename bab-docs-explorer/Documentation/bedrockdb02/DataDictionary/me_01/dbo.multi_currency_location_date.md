# dbo.multi_currency_location_date

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_ib_cost_factor_discount_$sp](../../StoredProcedures/me_01/dbo.startup_ib_cost_factor_discount_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)

