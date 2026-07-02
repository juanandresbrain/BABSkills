# dbo.keith_ib_audit_trail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 1 |  |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| employee_first_name | varchar | 30 | 0 |  |  |  |
| employee_last_name | varchar | 30 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_keith_ib_audit_trail](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail.md)
- [me_01: dbo.sp_keith_ib_audit_trailBACKU20150511](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBACKU20150511.md)
- [me_01: dbo.sp_keith_ib_audit_trailBAK20220801](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBAK20220801.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)

