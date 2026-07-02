# dbo.temp_asn_po_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| asn_po_location_id | decimal | 9 | 0 |  |  |  |
| advance_shipping_notice_id | decimal | 9 | 0 | YES |  |  |
| po_id | decimal | 9 | 0 | YES |  |  |
| ship_to_location_id | smallint | 2 | 0 | YES |  |  |
| blanket_po_id | decimal | 9 | 1 |  |  |  |
| predistribution_type | smallint | 2 | 0 |  |  |  |
| ticket_source | smallint | 2 | 0 |  |  |  |
| ticket_status | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)

