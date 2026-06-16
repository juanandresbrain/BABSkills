# WEB.ProductCategoryMapArchive

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Style | nvarchar | 12 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| ArchiveDate | datetime | 8 | 1 |  |  |  |
| ChangeType | varchar | 10 | 1 |  |  |  |
| CurrentBatch | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spOutputMasterCatalog](../../StoredProcedures/IntegrationStaging/WEB.spOutputMasterCatalog.md)

