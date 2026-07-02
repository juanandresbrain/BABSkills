# StoreForce.StoreHoursStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store_Id | numeric | 13 | 1 |  |  |  |
| Code | nvarchar | 100 | 1 |  |  |  |
| Date | date | 3 | 1 |  |  |  |
| OpenTime | nvarchar | 510 | 1 |  |  |  |
| CloseTime | nvarchar | 510 | 1 |  |  |  |
| IsHoliday | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: StoreForce.spMergeStoreHours](../../StoredProcedures/IntegrationStaging/StoreForce.spMergeStoreHours.md)

