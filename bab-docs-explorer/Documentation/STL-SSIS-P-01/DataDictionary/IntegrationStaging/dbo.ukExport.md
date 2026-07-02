# dbo.ukExport

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store Shipment Number | bigint | 8 | 1 |  |  |  |
| Aptos or D365 Document Number | varchar | 50 | 0 |  |  |  |
| Store Number | varchar | 10 | 0 |  |  |  |
| REC Type | varchar | 6 | 0 |  |  |  |
| REC Label | varchar | 20 | 1 |  |  |  |
| Style Code | varchar | 20 | 0 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMerchandisingReportStoreShipmentExportConfirmationUK](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingReportStoreShipmentExportConfirmationUK.md)

