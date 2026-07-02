# dbo.jurisdiction_tax_ex

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_tax_ex_id | decimal | 9 | 0 | YES |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| jurisdiction_tax_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_tax_ex_type | smallint | 2 | 0 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_size_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_tax_rate_$sp](../../StoredProcedures/me_01/dbo.get_tax_rate_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_bak](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_bak.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_modified_fast](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_modified_fast.md)
- [me_01: dbo.oo_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_populate_notax_retails_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)

