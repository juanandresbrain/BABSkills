# dbo.ib_average_cost_location_lock

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| locking_application | nvarchar | 10 | 1 |  |  |  |
| lock_timestamp | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.lock_ib_avg_cost_for_sales_posting_$sp](../../StoredProcedures/me_01/dbo.lock_ib_avg_cost_for_sales_posting_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)

