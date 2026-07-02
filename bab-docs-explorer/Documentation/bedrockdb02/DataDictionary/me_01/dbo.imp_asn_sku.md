# dbo.imp_asn_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_asn_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_asn_id | decimal | 9 | 1 |  |  |  |
| action | nchar | 2 | 0 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_inter_id_qualifier | nvarchar | 4 | 1 |  |  |  |
| vendor_inter_id_code | nvarchar | 30 | 1 |  |  |  |
| po_number | nvarchar | 40 | 1 |  |  |  |
| blanket_po_no | nvarchar | 40 | 1 |  |  |  |
| release_no | smallint | 2 | 1 |  |  |  |
| ship_to_location | nvarchar | 40 | 0 |  |  |  |
| selling_location_code | nvarchar | 40 | 1 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style_code | nvarchar | 80 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| units_shipped | int | 4 | 0 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| blanket_po_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_complete_$sp](../../StoredProcedures/me_01/dbo.import_asn_complete_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.purge_imp_asn_$sp](../../StoredProcedures/me_01/dbo.purge_imp_asn_$sp.md)
- [me_01: dbo.resubmit_import_asn_error_$sp](../../StoredProcedures/me_01/dbo.resubmit_import_asn_error_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

