# dbo.calendar_period

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_period_id | decimal | 9 | 0 | YES |  |  |
| calendar_period_code | tinyint | 1 | 0 |  |  |  |
| calendar_year_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_curr_slpd_ly_$fn](../../StoredProcedures/me_01/dbo.get_curr_slpd_ly_$fn.md)
- [me_01: dbo.get_first_prev_slpd_ly_$fn](../../StoredProcedures/me_01/dbo.get_first_prev_slpd_ly_$fn.md)
- [me_01: dbo.get_first_prev_slpd_ty_$fn](../../StoredProcedures/me_01/dbo.get_first_prev_slpd_ty_$fn.md)
- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

