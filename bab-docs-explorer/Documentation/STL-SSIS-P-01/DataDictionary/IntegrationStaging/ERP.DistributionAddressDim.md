# ERP.DistributionAddressDim

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AddressID | int | 4 | 0 |  |  |  |
| location_code | int | 4 | 1 |  |  |  |
| ShipToName | varchar | 75 | 1 |  |  |  |
| ShipToStreet | varchar | 75 | 1 |  |  |  |
| ShipToCity | varchar | 40 | 1 |  |  |  |
| ShipToState | varchar | 3 | 1 |  |  |  |
| ShipToZipCode | nvarchar | 30 | 1 |  |  |  |
| ShipToCountry | varchar | 100 | 1 |  |  |  |
| ShipToPhone | varchar | 15 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)
- [IntegrationStaging: ERP.spMergeDistributionAddressDim](../../StoredProcedures/IntegrationStaging/ERP.spMergeDistributionAddressDim.md)
- [IntegrationStaging: ERP.spOutputWMStoreMasterXML](../../StoredProcedures/IntegrationStaging/ERP.spOutputWMStoreMasterXML.md)

