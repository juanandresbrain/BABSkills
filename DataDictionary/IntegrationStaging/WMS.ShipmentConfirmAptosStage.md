# WMS.ShipmentConfirmAptosStage

**Database:** IntegrationStaging  

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
| ContainerUnitsShipped | float | 8 | 1 |  |  |  |
| ItemNumber | nvarchar | 200 | 1 |  |  |  |
| OrderedQuantity | float | 8 | 1 |  |  |  |
| OrderedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| OrderNumber | nvarchar | 200 | 1 |  |  |  |
| ShippedQuantity | float | 8 | 1 |  |  |  |
| ShippedUnitOfMeasure | nvarchar | 200 | 1 |  |  |  |
| ToLocation | nvarchar | 200 | 1 |  |  |  |
| ContainerManifestID | nvarchar | 104 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeShipmentConfirmAptos](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipmentConfirmAptos.md)

