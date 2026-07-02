# dbo.import_store_shipment_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_store_shipment_detail_id | decimal | 9 | 0 | YES |  |  |
| import_store_shipment_id | decimal | 9 | 0 |  |  |  |
| action | varchar | 1 | 0 |  |  |  |
| from_location_code | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| color_code | varchar | 3 | 0 |  |  |  |
| primary_size_label | varchar | 8 | 0 |  |  |  |
| secondary_size_label | varchar | 8 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |
| allocation_no | varchar | 20 | 1 |  |  |  |
| distribution_no | varchar | 20 | 0 |  |  |  |
| upc_number | varchar | 14 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailShipmentErrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailShipmentErrors.md)
- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)

