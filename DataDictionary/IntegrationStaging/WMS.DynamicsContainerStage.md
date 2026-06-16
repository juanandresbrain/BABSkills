# WMS.DynamicsContainerStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABStoreNumber | nvarchar | 8000 | 1 |  |  |  |
| ContainerId | nvarchar | 8000 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| DeliveryName | nvarchar | 8000 | 1 |  |  |  |
| Height | float | 8 | 1 |  |  |  |
| ItemId | nvarchar | 8000 | 1 |  |  |  |
| Length | float | 8 | 1 |  |  |  |
| LicensePlateId | nvarchar | 8000 | 1 |  |  |  |
| Qty | float | 8 | 1 |  |  |  |
| ShipmentId | nvarchar | 8000 | 1 |  |  |  |
| Weight | float | 8 | 1 |  |  |  |
| WHSShipmentTable_Address | nvarchar | 8000 | 1 |  |  |  |
| WHSShipmentTable_ShipConfirmUTCDateTime | datetime | 8 | 1 |  |  |  |
| WHSShipmentTable_WaveId | nvarchar | 8000 | 1 |  |  |  |
| Width | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDynamicsContainer](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsContainer.md)

