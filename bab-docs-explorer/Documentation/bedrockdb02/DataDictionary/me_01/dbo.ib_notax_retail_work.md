# dbo.ib_notax_retail_work

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_inventory_id | decimal | 9 | 0 | YES |  |  |
| valuation_retail_no_tax | decimal | 9 | 0 |  |  |  |
| selling_retail_no_tax | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ib_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_bak](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_bak.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_modified_fast](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_modified_fast.md)
- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.z_ib_notax_cleanup_$sp](../../StoredProcedures/me_01/dbo.z_ib_notax_cleanup_$sp.md)

