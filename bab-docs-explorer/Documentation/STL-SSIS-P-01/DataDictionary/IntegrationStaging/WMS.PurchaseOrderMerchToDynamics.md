# WMS.PurchaseOrderMerchToDynamics

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PONumber | varchar | 20 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 10 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| DeliveryDate | datetime | 8 | 1 |  |  |  |
| VendorCode | varchar | 10 | 1 |  |  |  |
| UnitCost | numeric | 17 | 1 |  |  |  |
| FactoryCode | varchar | 10 | 1 |  |  |  |
| POMainLIne | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ExportedToDynamicsDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| NetFinalPrice | numeric | 9 | 1 |  |  |  |
| CancelDate | date | 3 | 1 |  |  |  |
| Warehouse | varchar | 4 | 1 |  |  |  |
| Company | varchar | 4 | 1 |  |  |  |
| StartShipDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntity](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntity.md)
- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123.md)
- [IntegrationStaging: WMS.spEmailPOExportSummary](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummary.md)
- [IntegrationStaging: WMS.spEmailPOExportSummaryBAK20220801](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummaryBAK20220801.md)
- [IntegrationStaging: WMS.spMergePurchaseOrderMerchToDynamics](../../StoredProcedures/IntegrationStaging/WMS.spMergePurchaseOrderMerchToDynamics.md)
- [IntegrationStaging: WMS.spMergeShipmentInvoiceFromPOReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipmentInvoiceFromPOReceipt.md)

