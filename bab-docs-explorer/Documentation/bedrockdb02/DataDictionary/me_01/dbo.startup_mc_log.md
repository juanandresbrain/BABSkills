# dbo.startup_mc_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_ib_log_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 200 | 0 |  |  |  |
| date_processed | smalldatetime | 4 | 1 |  |  |  |
| start_sku_id | decimal | 9 | 1 |  |  |  |
| end_sku_id | decimal | 9 | 1 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_ib_cost_factor_discount_$sp](../../StoredProcedures/me_01/dbo.startup_ib_cost_factor_discount_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_inventory_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_total_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)
- [me_01: dbo.startup_ib_on_order_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_total_$sp.md)

