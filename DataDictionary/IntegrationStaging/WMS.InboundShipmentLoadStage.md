# WMS.InboundShipmentLoadStage

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

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeInboundShipmentLoad](../../StoredProcedures/IntegrationStaging/WMS.spMergeInboundShipmentLoad.md)
- [IntegrationStaging: WMS.spMergeInboundShipmentLoad_Bak20231030](../../StoredProcedures/IntegrationStaging/WMS.spMergeInboundShipmentLoad_Bak20231030.md)

