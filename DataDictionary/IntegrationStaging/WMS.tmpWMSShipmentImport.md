# WMS.tmpWMSShipmentImport

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipment | nvarchar | 200 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| ship_date | varchar | 30 | 1 |  |  |  |
| distribution_number | bigint | 8 | 1 |  |  |  |
| distribution_line | float | 8 | 1 |  |  |  |
| style_code | nvarchar | 24 | 1 |  |  |  |
| req_qty | float | 8 | 1 |  |  |  |
| sent_qty | float | 8 | 1 |  |  |  |
| variance_qty | float | 8 | 1 |  |  |  |
| carton_nbr | nvarchar | 40 | 1 |  |  |  |
| rec_type | int | 4 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |
| erd_date | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spOutputWMSShipment](../../StoredProcedures/IntegrationStaging/WMS.spOutputWMSShipment.md)
- [IntegrationStaging: WMS.spProcessShipmentAllocationAdjPipelineData](../../StoredProcedures/IntegrationStaging/WMS.spProcessShipmentAllocationAdjPipelineData.md)

