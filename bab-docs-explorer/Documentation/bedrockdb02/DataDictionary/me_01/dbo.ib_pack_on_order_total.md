# dbo.ib_pack_on_order_total

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_number | nvarchar | 40 | 0 | YES |  |  |
| pack_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| receipt_date | smalldatetime | 4 | 0 | YES |  |  |
| total_on_order_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.on_order_cancel_pack_$sp](../../StoredProcedures/me_01/dbo.on_order_cancel_pack_$sp.md)
- [me_01: dbo.on_order_pack_update_$sp](../../StoredProcedures/me_01/dbo.on_order_pack_update_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)

