# dbo.keith_country

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country_id | decimal | 9 | 0 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |
| country_code | varchar | 3 | 0 |  |  |  |
| country_description | varchar | 50 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| european_union_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingEmailNewCountry](../../StoredProcedures/me_01/dbo.spMerchandisingEmailNewCountry.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)

