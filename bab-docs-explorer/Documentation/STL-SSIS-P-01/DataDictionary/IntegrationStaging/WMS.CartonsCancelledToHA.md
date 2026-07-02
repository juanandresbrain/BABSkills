# WMS.CartonsCancelledToHA

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| warehouse | nvarchar | 200 | 1 |  |  |  |
| containerId | nvarchar | 200 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SentToHa | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeCartonsCancelledToHA](../../StoredProcedures/IntegrationStaging/WMS.spMergeCartonsCancelledToHA.md)

