# WMS.DBSchenkerFullInGateFile

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrder | varchar | 50 | 1 |  |  |  |
| ProductCode | varchar | 50 | 1 |  |  |  |
| ShippedQty | varchar | 50 | 1 |  |  |  |
| FullIngateatLoadPort | varchar | 52 | 1 |  |  |  |
| POL | varchar | 50 | 1 |  |  |  |
| MANUFACTURERCODE | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| POReceiptExportDate | datetime | 8 | 1 |  |  |  |
| Dynamics1200PO | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDBSchenkerFullInGateFile](../../StoredProcedures/IntegrationStaging/WMS.spMergeDBSchenkerFullInGateFile.md)
- [IntegrationStaging: WMS.spOutputPurchaseOrderReceiptDBStoDynamics1200XML](../../StoredProcedures/IntegrationStaging/WMS.spOutputPurchaseOrderReceiptDBStoDynamics1200XML.md)

