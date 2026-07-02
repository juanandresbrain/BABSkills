# dbo.import_store_shipment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_store_shipment_id | decimal | 9 | 0 | YES |  |  |
| action | varchar | 1 | 0 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| from_location_code | varchar | 20 | 0 |  |  |  |
| unit_weight_code | varchar | 10 | 1 |  |  |  |
| document_no | varchar | 20 | 0 |  |  |  |
| document_status | smallint | 2 | 1 |  |  |  |
| state_no | int | 4 | 1 |  |  |  |
| ship_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | varchar | 60 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| external_system_name | varchar | 20 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| imp_file_name | varchar | 200 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailShipmentErrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailShipmentErrors.md)
- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)

