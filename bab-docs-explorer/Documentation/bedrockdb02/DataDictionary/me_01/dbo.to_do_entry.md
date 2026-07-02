# dbo.to_do_entry

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| to_do_entry_id | T_ID | 16 | 0 | YES |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| distribution_id | bigint | 8 | 1 |  |  |  |
| po_line_id | int | 4 | 1 |  |  |  |
| po_shipment_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| po_line_total_units | int | 4 | 1 |  |  |  |
| receipt_date | smalldatetime | 4 | 1 |  |  |  |
| request_type | smallint | 2 | 1 |  |  |  |
| errors | nvarchar | -1 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| asn_po_location_id | decimal | 9 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |
| to_do_entry_id_as_string | nvarchar | 96 | 0 |  |  |  |
| parent_distribution_id | bigint | 8 | 1 |  |  |  |
| root_distribution_id | bigint | 8 | 1 |  |  |  |
| locked_flag | bit | 1 | 0 |  |  |  |
| locked_by_user_id | int | 4 | 1 |  |  |  |
| locked_by_user_session_id | T_ID | 16 | 1 |  |  |  |
| lock_timestamp | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)

