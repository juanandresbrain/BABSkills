# WMS.StoreShipmentExport

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderType | varchar | 15 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 20 | 1 |  |  |  |
| FromWarehouse | varchar | 4 | 1 |  |  |  |
| ToWarehouse | varchar | 4 | 1 |  |  |  |
| ModeOfDelivery | varchar | 52 | 1 |  |  |  |
| DeliveryTerms | varchar | 100 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| AptosDistroNumber | varchar | 20 | 1 |  |  |  |
| AptosDistroLineNumber | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 7 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| UnitOfMeasure | varchar | 20 | 1 |  |  |  |
| InventoryStatus | varchar | 52 | 1 |  |  |  |
| CountryCode | varchar | 5 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| Company | varchar | 4 | 1 |  |  |  |
| SourceCountry | varchar | 4 | 1 |  |  |  |
| DestinationCountry | varchar | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailAptosDistributionExportValidation](../../StoredProcedures/IntegrationStaging/WMS.spEmailAptosDistributionExportValidation.md)
- [IntegrationStaging: WMS.spEmailTransferOrderSalesOrderExport](../../StoredProcedures/IntegrationStaging/WMS.spEmailTransferOrderSalesOrderExport.md)
- [IntegrationStaging: WMS.spMergeStoreShipmentExport](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreShipmentExport.md)
- [IntegrationStaging: WMS.spMergeStoreShipmentExport_BAK20220801](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreShipmentExport_BAK20220801.md)
- [IntegrationStaging: WMS.spMergeStoreShipmentExportParty](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreShipmentExportParty.md)
- [IntegrationStaging: WMS.spProcessShipmentAllocationAdjPipelineData](../../StoredProcedures/IntegrationStaging/WMS.spProcessShipmentAllocationAdjPipelineData.md)

