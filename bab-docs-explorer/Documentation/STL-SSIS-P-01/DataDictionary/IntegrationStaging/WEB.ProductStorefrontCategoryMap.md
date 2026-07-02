# WEB.ProductStorefrontCategoryMap

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| PrimaryCategory | int | 4 | 1 |  |  |  |
| ClassificationCategory | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeProductStorefrontCategoryMap](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductStorefrontCategoryMap.md)

