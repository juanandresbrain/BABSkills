# dbo.ib_oo_notax_retail_work

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_on_order_id | decimal | 9 | 0 | YES |  |  |
| valuation_retail_no_tax | decimal | 9 | 0 |  |  |  |
| selling_retail_no_tax | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.oo_cleanup_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_cleanup_notax_retails_$sp.md)
- [me_01: dbo.oo_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_populate_notax_retails_$sp.md)

