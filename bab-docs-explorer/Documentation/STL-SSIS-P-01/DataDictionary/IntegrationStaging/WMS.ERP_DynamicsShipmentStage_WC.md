# WMS.ERP_DynamicsShipmentStage_WC

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 10 | 1 |  |  |  |
| BOL | varchar | 30 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| rec_type | varchar | 4 | 1 |  |  |  |
| ship_date | varchar | 8 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| ordered_qty | int | 4 | 1 |  |  |  |
| shipped_qty | int | 4 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| distribution_no | varchar | 12 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| license_plate | varchar | 100 | 1 |  |  |  |
| insert_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMerchandisingProcessWCStoreShipments](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingProcessWCStoreShipments.md)

