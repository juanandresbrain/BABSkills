# dbo.imp_asn_error

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | decimal | 9 | 0 | YES |  |  |
| imp_asn_id | decimal | 9 | 0 | YES |  |  |
| error_code | nvarchar | 20 | 1 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_inter_id_qualifier | nvarchar | 4 | 1 |  |  |  |
| vendor_inter_id_code | nvarchar | 30 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| bol | nvarchar | 40 | 1 |  |  |  |
| imp_file_name | nvarchar | 400 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.resubmit_import_asn_error_$sp](../../StoredProcedures/me_01/dbo.resubmit_import_asn_error_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

