# WMS.CartonsCreatedToHAStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| waveId | nvarchar | 200 | 1 |  |  |  |
| warehouse | nvarchar | 200 | 1 |  |  |  |
| waveStatus | nvarchar | 200 | 1 |  |  |  |
| numberOfContainers | float | 8 | 1 |  |  |  |
| releasedDateAndTime | nvarchar | 200 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeCartonsCreatedToHA](../../StoredProcedures/IntegrationStaging/WMS.spMergeCartonsCreatedToHA.md)

