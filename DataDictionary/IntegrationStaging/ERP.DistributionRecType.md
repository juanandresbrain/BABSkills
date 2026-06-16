# ERP.DistributionRecType

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rectype | int | 4 | 1 |  |  |  |
| reasoncode | nvarchar | 510 | 1 |  |  |  |
| message | nvarchar | 510 | 1 |  |  |  |
| priority | int | 4 | 1 |  |  |  |
| ModeOfDelivery | varchar | 100 | 1 |  |  |  |
| ModeOfDeliveryCA | varchar | 100 | 1 |  |  |  |
| ModeOfDeliveryUK | varchar | 100 | 1 |  |  |  |
| ModeOfDeliveryCN | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)
- [IntegrationStaging: WMS.spProcessShipmentAllocationAdjPipelineData](../../StoredProcedures/IntegrationStaging/WMS.spProcessShipmentAllocationAdjPipelineData.md)

