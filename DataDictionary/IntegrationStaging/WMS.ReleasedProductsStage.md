# WMS.ReleasedProductsStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| ProductNumber | nvarchar | 8000 | 1 |  |  |  |
| BABEntitySpecificHTS | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeReleasedProducts](../../StoredProcedures/IntegrationStaging/WMS.spMergeReleasedProducts.md)

