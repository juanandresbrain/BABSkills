# dbo.advance_shipping_notice

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| advance_shipping_notice_id | decimal | 9 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| container_type_id | smallint | 2 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| bill_of_lading | nvarchar | 40 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| asn_status | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

