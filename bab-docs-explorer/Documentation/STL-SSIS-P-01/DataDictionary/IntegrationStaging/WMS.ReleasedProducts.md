# WMS.ReleasedProducts

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| ProductNumber | nvarchar | 8000 | 1 |  |  |  |
| BABEntitySpecificHTS | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeReleasedProducts](../../StoredProcedures/IntegrationStaging/WMS.spMergeReleasedProducts.md)

