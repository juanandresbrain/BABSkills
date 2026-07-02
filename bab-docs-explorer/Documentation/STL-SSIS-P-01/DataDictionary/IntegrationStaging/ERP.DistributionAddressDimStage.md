# ERP.DistributionAddressDimStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | int | 4 | 1 |  |  |  |
| ShipToName | varchar | 75 | 1 |  |  |  |
| ShipToStreet | varchar | 75 | 1 |  |  |  |
| ShipToCity | varchar | 40 | 1 |  |  |  |
| ShipToState | varchar | 3 | 1 |  |  |  |
| ShipToZipCode | nvarchar | 30 | 1 |  |  |  |
| ShipToCountry | varchar | 100 | 1 |  |  |  |
| ShipToPhone | varchar | 15 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeDistributionAddressDim](../../StoredProcedures/IntegrationStaging/ERP.spMergeDistributionAddressDim.md)

