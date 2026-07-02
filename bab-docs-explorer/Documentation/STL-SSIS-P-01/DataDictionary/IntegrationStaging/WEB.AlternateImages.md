# WEB.AlternateImages

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ImageName | varchar | 100 | 1 |  |  |  |
| BABWProductID | varchar | 6 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeAlternateImages](../../StoredProcedures/IntegrationStaging/WEB.spMergeAlternateImages.md)

