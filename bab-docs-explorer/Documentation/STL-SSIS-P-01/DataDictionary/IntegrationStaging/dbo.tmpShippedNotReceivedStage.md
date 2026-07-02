# dbo.tmpShippedNotReceivedStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| LicensePlate | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| Name | varchar | 8000 | 1 |  |  |  |
| FromWarehouse | varchar | 8000 | 1 |  |  |  |
| ToWarehouse | varchar | 8000 | 1 |  |  |  |
| ProductHierarchy | varchar | 8000 | 0 |  |  |  |
| ShipDate | datetime2 | 8 | 1 |  |  |  |
| ItemQty | numeric | 9 | 1 |  |  |  |
| CartonQty | int | 4 | 1 |  |  |  |
| isMiscCarton | int | 4 | 0 |  |  |  |
| MiscCartonDetails | varchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spShippedNotReceivedStoreReportPrep](../../StoredProcedures/IntegrationStaging/WMS.spShippedNotReceivedStoreReportPrep.md)

