# dbo.TPM_PROCESS_CONTROL

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 1 |  |  |  |
| line_no | int | 4 | 1 |  |  |  |
| po_line_shipment_id | int | 4 | 1 |  |  |  |
| po_status | int | 4 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| process_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingOutputTPMPoXML](../../StoredProcedures/me_01/dbo.spMerchandisingOutputTPMPoXML.md)
- [me_01: dbo.spMerchandisingOutputTPMPoXMLBACKUP20200210](../../StoredProcedures/me_01/dbo.spMerchandisingOutputTPMPoXMLBACKUP20200210.md)

