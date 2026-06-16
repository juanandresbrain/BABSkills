# WEB.ProductStorefrontCategoryMapArchive

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Style | varchar | 6 | 1 |  |  |  |
| PrimaryCategory | int | 4 | 1 |  |  |  |
| ClassificationCategory | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ArchiveDate | datetime | 8 | 1 |  |  |  |
| ChangeType | varchar | 10 | 1 |  |  |  |
| CurrentBatch | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeProductStorefrontCategoryMap](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductStorefrontCategoryMap.md)

