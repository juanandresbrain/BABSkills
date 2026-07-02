# dbo.multi_currency_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 |  |  |  |
| currency_conversion_type | smallint | 2 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 1 |  |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.populate_multi_currency_location_$sp](../../StoredProcedures/me_01/dbo.populate_multi_currency_location_$sp.md)
- [me_01: dbo.startup_ib_cost_factor_discount_$sp](../../StoredProcedures/me_01/dbo.startup_ib_cost_factor_discount_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)
- [me_01: dbo.startup_ib_on_order_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_total_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

