# dbo.po_shipment_udd

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_shipment_udd_id | smallint | 2 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| user_defined_date | smalldatetime | 4 | 0 |  |  |  |
| po_date_type_id | decimal | 9 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_po_shipment_udds_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_shipment_udds_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)

