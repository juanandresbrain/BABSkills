# dbo.temp_asn_po_location_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| asn_po_location_detail_id | decimal | 9 | 0 |  |  |  |
| asn_po_location_id | decimal | 9 | 0 |  |  |  |
| advance_shipping_notice_id | decimal | 9 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| ship_to_location_id | smallint | 2 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |
| selling_location_id | smallint | 2 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)

