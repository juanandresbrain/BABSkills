# WEB.ProductStorefrontCategoryMapStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| PrimaryCategory | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeProductStorefrontCategoryMap](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductStorefrontCategoryMap.md)

