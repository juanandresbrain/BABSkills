# WMS.ShipmentConfirmAptos

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AptosShipmentID | nvarchar | 200 | 1 |  |  |  |
| ModeOfDelivery | nvarchar | 200 | 1 |  |  |  |
| ShipConfirmDateTime | nvarchar | 200 | 1 |  |  |  |
| Warehouse | nvarchar | 200 | 1 |  |  |  |
| ContainerID | nvarchar | 200 | 1 |  |  |  |
| AptosDistributionNumber | bigint | 8 | 1 |  |  |  |
| AptosDistributionDocLineNumber | float | 8 | 1 |  |  |  |
| ContainerUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| ContainerUnitsShipped | int | 4 | 1 |  |  |  |
| ItemNumber | nvarchar | 200 | 1 |  |  |  |
| OrderedQuantity | float | 8 | 1 |  |  |  |
| OrderedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| OrderNumber | nvarchar | 200 | 1 |  |  |  |
| ShippedQuantity | int | 4 | 1 |  |  |  |
| ShippedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| ToLocation | nvarchar | 200 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| SentToPipelineDate | datetime | 8 | 1 |  |  |  |
| ContainerManifestID | nvarchar | 104 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailFedExTracking](../../StoredProcedures/IntegrationStaging/WMS.spEmailFedExTracking.md)
- [IntegrationStaging: WMS.spMergeShipmentConfirmAptos](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipmentConfirmAptos.md)
- [IntegrationStaging: WMS.spProcessShipmentAllocationAdjPipelineData](../../StoredProcedures/IntegrationStaging/WMS.spProcessShipmentAllocationAdjPipelineData.md)
- [IntegrationStaging: WMS.spStoreShipmentReport](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport.md)
- [IntegrationStaging: WMS.spStoreShipmentReport_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport_Last24hourSnapshot.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotals](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotals.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot.md)

