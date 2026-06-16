# ERP.UserLoadtoD365multipleLocationsStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WAREHOUSEID | varchar | 50 | 1 |  |  |  |
| WAREHOUSEMOBILEDEVICEUSERID | varchar | 120 | 1 |  |  |  |
| ENTITY | nvarchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spMergeUsersMultipleLocs](../../StoredProcedures/IntegrationStaging/dbo.spMergeUsersMultipleLocs.md)

