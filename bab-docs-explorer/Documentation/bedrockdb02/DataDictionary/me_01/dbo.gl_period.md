# dbo.gl_period

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_period_id | decimal | 9 | 0 | YES |  |  |
| gl_period_code | nvarchar | 40 | 0 |  |  |  |
| gl_period_label | nvarchar | 120 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 0 |  |  |  |
| date_last_sent_to_gl | smalldatetime | 4 | 1 |  |  |  |
| date_closed | smalldatetime | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_closed_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| last_closed_ib_cost_factor_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc.md)
- [me_01: dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual](../../StoredProcedures/me_01/dbo.spMerchandisingReportEOMUnitsOHbyLoc_Manual.md)
- [me_01: dbo.spMerchandisingRoyaltyReports](../../StoredProcedures/me_01/dbo.spMerchandisingRoyaltyReports.md)

