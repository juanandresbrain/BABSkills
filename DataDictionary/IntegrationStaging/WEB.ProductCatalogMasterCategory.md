# WEB.ProductCatalogMasterCategory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryID | nvarchar | 400 | 1 |  |  |  |
| Parent | nvarchar | 400 | 1 |  |  |  |
| DisplayName | nvarchar | 104 | 1 |  |  |  |
| CategoryLevel | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spOutputMasterCatalog](../../StoredProcedures/IntegrationStaging/WEB.spOutputMasterCatalog.md)

