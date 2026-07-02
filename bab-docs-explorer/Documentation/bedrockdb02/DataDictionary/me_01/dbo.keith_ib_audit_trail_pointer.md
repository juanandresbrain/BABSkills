# dbo.keith_ib_audit_trail_pointer

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pointer | varchar | 5 | 0 |  |  |  |
| ib_audit_trail_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_keith_ib_audit_trail_pointer](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail_pointer.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)

