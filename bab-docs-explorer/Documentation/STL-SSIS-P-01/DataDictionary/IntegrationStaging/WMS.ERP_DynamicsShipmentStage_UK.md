# WMS.ERP_DynamicsShipmentStage_UK

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipment | varchar | 52 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| ship_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 12 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| req_qty | int | 4 | 1 |  |  |  |
| sent_qty | int | 4 | 1 |  |  |  |
| variance_qty | int | 4 | 1 |  |  |  |
| carton_nbr | varchar | 20 | 1 |  |  |  |
| rec_type | varchar | 10 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |
| erd_date | varchar | 30 | 1 |  |  |  |
| insert_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMerchandisingProcessUKStoreShipments](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingProcessUKStoreShipments.md)

