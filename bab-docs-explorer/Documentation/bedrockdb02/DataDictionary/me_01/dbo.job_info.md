# dbo.job_info

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_type | int | 4 | 0 |  |  |  |
| batch_job_name | nvarchar | 60 | 0 |  |  |  |
| job_description | nvarchar | 510 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.validate_wrk_ib_allocation_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_allocation_$sp.md)
- [ma_01: dbo.validate_wrk_ib_cost_fact_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_cost_fact_$sp.md)
- [ma_01: dbo.validate_wrk_ib_inventory_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_inventory_$sp.md)
- [ma_01: dbo.validate_wrk_ib_on_order_$sp](../../StoredProcedures/ma_01/dbo.validate_wrk_ib_on_order_$sp.md)

