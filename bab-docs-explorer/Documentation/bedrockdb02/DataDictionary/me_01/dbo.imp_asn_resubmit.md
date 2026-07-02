# dbo.imp_asn_resubmit

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | decimal | 9 | 0 |  |  |  |
| imp_asn_id | decimal | 9 | 0 |  |  |  |
| shipment_ref_no | nvarchar | 60 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.resubmit_import_asn_error_$sp](../../StoredProcedures/me_01/dbo.resubmit_import_asn_error_$sp.md)

