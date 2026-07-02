# WMS.DynamicsAPILog

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrationName | nvarchar | 200 | 1 |  |  |  |
| MergedJson | nvarchar | -1 | 1 |  |  |  |
| ContentType | nvarchar | 510 | 1 |  |  |  |
| ContentLength | numeric | 13 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpResponseUrl | nvarchar | 4168 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBody | nvarchar | -1 | 1 |  |  |  |
| ExceptionError | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| AptosDocumentNumber | varchar | 20 | 1 |  |  |  |
| TPMShipmentNumber | nvarchar | 40 | 1 |  |  |  |
| StoreShipmentNumber | varchar | 20 | 1 |  |  |  |
| WebOrderNumber | nvarchar | 20 | 1 |  |  |  |
| PO_OrderAccountNumber | nvarchar | 104 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| MessageID | nvarchar | 200 | 1 |  |  |  |
| CostcoOrderNumber | varchar | 50 | 1 |  |  |  |
| TransferOrderNumber | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailAptosDistributionExportValidation](../../StoredProcedures/IntegrationStaging/WMS.spEmailAptosDistributionExportValidation.md)
- [IntegrationStaging: WMS.spEmailASNExportSummary](../../StoredProcedures/IntegrationStaging/WMS.spEmailASNExportSummary.md)
- [IntegrationStaging: WMS.spEmailPOExportSummary](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummary.md)
- [IntegrationStaging: WMS.spEmailPOExportSummaryBAK20220801](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummaryBAK20220801.md)
- [IntegrationStaging: WMS.spEmailTransferOrderSalesOrderExport](../../StoredProcedures/IntegrationStaging/WMS.spEmailTransferOrderSalesOrderExport.md)
- [IntegrationStaging: WMS.spInsertDynamicsAPILog](../../StoredProcedures/IntegrationStaging/WMS.spInsertDynamicsAPILog.md)
- [IntegrationStaging: WMS.spMergeShipmentInvoiceFromPOReceipt](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipmentInvoiceFromPOReceipt.md)
- [IntegrationStaging: WMS.spReportTPMtoD365errors](../../StoredProcedures/IntegrationStaging/WMS.spReportTPMtoD365errors.md)

