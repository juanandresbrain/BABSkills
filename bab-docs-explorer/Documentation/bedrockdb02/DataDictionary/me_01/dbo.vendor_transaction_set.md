# dbo.vendor_transaction_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_transaction_set_id | decimal | 9 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| edi_transaction_set_id | smallint | 2 | 0 |  |  |  |
| live_edi_version_id | tinyint | 1 | 1 |  |  |  |
| test_edi_version_id | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

