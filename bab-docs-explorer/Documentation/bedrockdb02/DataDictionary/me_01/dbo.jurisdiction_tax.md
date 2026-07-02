# dbo.jurisdiction_tax

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_tax_id | decimal | 9 | 0 | YES |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| tax_type_id | smallint | 2 | 0 |  |  |  |
| tax_rate_id | smallint | 2 | 0 |  |  |  |
| surtax_id | decimal | 9 | 1 |  |  |  |
| default_flag | bit | 1 | 0 |  |  |  |
| tax_inclusive_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_tax_rate_$sp](../../StoredProcedures/me_01/dbo.get_tax_rate_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_bak](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_bak.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_modified_fast](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_modified_fast.md)
- [me_01: dbo.oo_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_populate_notax_retails_$sp.md)
- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)

