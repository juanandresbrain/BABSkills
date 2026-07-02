# WMS.ERDMatrixStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | nvarchar | 510 | 1 |  |  |  |
| rec_type | int | 4 | 1 |  |  |  |
| days | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeERDMatrix](../../StoredProcedures/IntegrationStaging/WMS.spMergeERDMatrix.md)

