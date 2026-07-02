# WMS.StoreTransferOrderReceipt

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventorySiteId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseId | nvarchar | 8000 | 1 |  |  |  |
| Entity | nvarchar | 8000 | 1 |  |  |  |
| SourceOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| ContainerId | nvarchar | 8000 | 1 |  |  |  |
| TargetLicensePlateNumber | nvarchar | 8000 | 1 |  |  |  |
| LoadId | nvarchar | 8000 | 1 |  |  |  |
| ShipmentId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseWorkOrderType | nvarchar | 510 | 1 |  |  |  |
| WarehouseWorkStatus | nvarchar | 510 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt_Bak20230926](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt_Bak20230926.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt_BAK20231011](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt_BAK20231011.md)
- [IntegrationStaging: WMS.spStoreShipmentReport](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport.md)
- [IntegrationStaging: WMS.spStoreShipmentReport_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport_Last24hourSnapshot.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotals](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotals.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot.md)

