# dbo.WCExport

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store Shipment Number | varchar | 10 | 1 |  |  |  |
| Store Number | varchar | 10 | 0 |  |  |  |
| REC TYPE | varchar | 6 | 0 |  |  |  |
| REC Label | varchar | 20 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMerchandisingReportStoreShipmentExportConfirmationWC](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingReportStoreShipmentExportConfirmationWC.md)

