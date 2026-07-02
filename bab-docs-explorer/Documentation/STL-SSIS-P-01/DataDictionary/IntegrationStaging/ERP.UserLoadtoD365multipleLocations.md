# ERP.UserLoadtoD365multipleLocations

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WAREHOUSEID | varchar | 50 | 1 |  |  |  |
| WAREHOUSEMOBILEDEVICEUSERID | varchar | 120 | 1 |  |  |  |
| ENTITY | nvarchar | 20 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| isDeactivated | int | 4 | 1 |  |  |  |
| isExported | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spMergeUsersMultipleLocs](../../StoredProcedures/IntegrationStaging/dbo.spMergeUsersMultipleLocs.md)

