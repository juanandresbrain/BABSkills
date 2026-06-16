# WMS.InboundShipmentLoad

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShipDate | date | 3 | 1 |  |  |  |
| ExpectedReceiptDate | date | 3 | 1 |  |  |  |
| DeliveryTerms | varchar | 9 | 1 |  |  |  |
| ItemNumber | varchar | 20 | 1 |  |  |  |
| TransferQuantity | int | 4 | 1 |  |  |  |
| UOM | varchar | 2 | 1 |  |  |  |
| BABAptosDistroNumber | varchar | 12 | 1 |  |  |  |
| InventoryStatus | varchar | 5 | 1 |  |  |  |
| LicensePlate | varchar | 100 | 1 |  |  |  |
| ContainerID | varchar | 20 | 1 |  |  |  |
| 3PLDocumentNumber | varchar | 10 | 1 |  |  |  |
| OrderCreateSource | varchar | 20 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| FromWarehouse | varchar | 5 | 1 |  |  |  |
| ToWarehouse | varchar | 10 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 50 | 1 |  |  |  |
| ModeOfDelivery | varchar | 10 | 1 |  |  |  |
| OrderId | varchar | 20 | 1 |  |  |  |
| BABAptosDistroLineNumber | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| SentDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 104 | 1 |  |  |  |
| ParentLicensePlate | varchar | 25 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeInboundShipmentLoad](../../StoredProcedures/IntegrationStaging/WMS.spMergeInboundShipmentLoad.md)
- [IntegrationStaging: WMS.spMergeInboundShipmentLoad_Bak20231030](../../StoredProcedures/IntegrationStaging/WMS.spMergeInboundShipmentLoad_Bak20231030.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt.md)
- [IntegrationStaging: WMS.spMergeStoreTransferOrderReceipt_BAK20231011](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreTransferOrderReceipt_BAK20231011.md)
- [IntegrationStaging: WMS.spStoreShipmentReport](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport.md)
- [IntegrationStaging: WMS.spStoreShipmentReport_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReport_Last24hourSnapshot.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotals](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotals.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot.md)

