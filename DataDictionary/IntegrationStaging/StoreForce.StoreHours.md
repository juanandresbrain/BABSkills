# StoreForce.StoreHours

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Code | int | 4 | 1 |  |  |  |
| Date | date | 3 | 1 |  |  |  |
| OpenTime | nvarchar | 510 | 1 |  |  |  |
| CloseTime | nvarchar | 510 | 1 |  |  |  |
| IsHoliday | nvarchar | 510 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: StoreForce.spMergeStoreHours](../../StoredProcedures/IntegrationStaging/StoreForce.spMergeStoreHours.md)

