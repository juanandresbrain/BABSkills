# WEB.ProductCatalogStorefrontCategory

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Parent | nvarchar | 400 | 1 |  |  |  |
| DisplayName | nvarchar | 104 | 1 |  |  |  |
| CategoryLevel | int | 4 | 1 |  |  |  |
| OnlineStart | date | 3 | 1 |  |  |  |
| OnlineEnd | date | 3 | 1 |  |  |  |
| OnlineFlag | int | 4 | 1 |  |  |  |
| Position | numeric | 5 | 1 |  |  |  |
| ShowInMenu | varchar | 5 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeProductCatalogStorefrontCategory](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogStorefrontCategory.md)

