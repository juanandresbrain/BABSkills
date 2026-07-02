# WEB.WebStyleAttributes

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | varchar | 5 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| Type | varchar | 15 | 1 |  |  |  |
| Field | varchar | 40 | 1 |  |  |  |
| Value | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spSelectProductCatalogMasterAttributes](../../StoredProcedures/IntegrationStaging/WEB.spSelectProductCatalogMasterAttributes.md)

