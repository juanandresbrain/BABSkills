# WEB.ProductCatalogMasterDataExceptions

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 6 | 1 |  |  |  |
| onlineFrom | date | 3 | 1 |  |  |  |
| searchable | varchar | 3 | 1 |  |  |  |
| searchableIfUnavailable | varchar | 3 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spUpdateProductMasterCatalogOnlineFlag](../../StoredProcedures/IntegrationStaging/WEB.spUpdateProductMasterCatalogOnlineFlag.md)

