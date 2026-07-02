# WMS.StoreToStoreTransferLicensePlateStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | varchar | 10 | 1 |  |  |  |
| TargetLicensePlateNumber | nvarchar | 8000 | 1 |  |  |  |
| SourceOrderNumber | varchar | 20 | 1 |  |  |  |
| WarehouseId | varchar | 10 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreToStoreTransferLicensePlate](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreToStoreTransferLicensePlate.md)

