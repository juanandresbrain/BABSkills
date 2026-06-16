# WMS.StoreTransferOrderReceiptStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActualProcessingTimeSeconds | float | 8 | 1 |  |  |  |
| ContainerId | nvarchar | 8000 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| EstimatedProcessingTimeSeconds | float | 8 | 1 |  |  |  |
| InventorySiteId | nvarchar | 8000 | 1 |  |  |  |
| IsWarehouseWorkBlocked | nvarchar | 510 | 1 |  |  |  |
| IsWarehouseWorkerManuallyAssigned | nvarchar | 510 | 1 |  |  |  |
| LoadId | nvarchar | 8000 | 1 |  |  |  |
| ShipmentId | nvarchar | 8000 | 1 |  |  |  |
| SourceOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| TargetLicensePlateNumber | nvarchar | 8000 | 1 |  |  |  |
| WarehouseId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkCancelledDateTime | datetime | 8 | 1 |  |  |  |
| WarehouseWorkCancellingUserId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkClosedDateTime | datetime | 8 | 1 |  |  |  |
| WarehouseWorkId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkLines | nvarchar | -1 | 1 |  |  |  |
| WarehouseWorkLockingWarehouseMobileDeviceUserId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkManuallyCompletingUserId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkOrderType | nvarchar | 510 | 1 |  |  |  |
| WarehouseWorkPoolId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkPriority | int | 4 | 1 |  |  |  |
| WarehouseWorkProcessingStartDateTime | datetime | 8 | 1 |  |  |  |
| WarehouseWorkStatus | nvarchar | 510 | 1 |  |  |  |
| WaveId | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt_Bak20230926](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt_Bak20230926.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt_BAK20231011](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt_BAK20231011.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotals](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotals.md)

