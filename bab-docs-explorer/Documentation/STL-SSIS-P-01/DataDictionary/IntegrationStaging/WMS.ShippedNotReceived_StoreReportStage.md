# WMS.ShippedNotReceived_StoreReportStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | nvarchar | 200 | 1 |  |  |  |
| LicensePlate | nvarchar | 200 | 1 |  |  |  |
| ItemNumber | nvarchar | 200 | 1 |  |  |  |
| Name | nvarchar | 200 | 1 |  |  |  |
| FromWarehouse | nvarchar | 200 | 1 |  |  |  |
| ToWarehouse | nvarchar | 200 | 1 |  |  |  |
| ProductHierarchy | nvarchar | 200 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ItemQty | int | 4 | 1 |  |  |  |
| CartonQty | int | 4 | 1 |  |  |  |
| MiscCartonDetails | nvarchar | 200 | 1 |  |  |  |
| isMiscCarton | bit | 1 | 1 |  |  |  |
| ShipConfirmUTCDateTime | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spShippedNotReceivedStoreReportPrep](../../StoredProcedures/IntegrationStaging/WMS.spShippedNotReceivedStoreReportPrep.md)
- [IntegrationStaging: WMS.spStoreShipmentReportD365](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportD365.md)
- [IntegrationStaging: WMS.spStoreShipmentReportD365_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportD365_Last24hourSnapshot.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsD365](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsD365.md)
- [IntegrationStaging: WMS.spStoreShipmentReportTotalsD365_Last24hourSnapshot](../../StoredProcedures/IntegrationStaging/WMS.spStoreShipmentReportTotalsD365_Last24hourSnapshot.md)

