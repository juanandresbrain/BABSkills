# dbo.ib_average_cost_pseudo_style_lock

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| locking_application | nvarchar | 10 | 1 |  |  |  |
| lock_timestamp | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.lock_ib_avg_cost_for_sales_posting_$sp](../../StoredProcedures/me_01/dbo.lock_ib_avg_cost_for_sales_posting_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)

