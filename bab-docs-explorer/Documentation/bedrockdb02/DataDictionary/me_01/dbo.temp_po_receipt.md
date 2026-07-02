# dbo.temp_po_receipt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| po_receipt_id | decimal | 9 | 0 | YES |  |  |
| po_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| advance_shipping_notice_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| ticket_source | smallint | 2 | 0 |  |  |  |
| ticket_status | smallint | 2 | 0 |  |  |  |
| shipped_date | smalldatetime | 4 | 1 |  |  |  |
| track_in_transit_flag | bit | 1 | 0 |  |  |  |
| discrepancy_posted | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)

