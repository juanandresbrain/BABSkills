# dbo.tmpWAV000121082

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServiceBusMessageId | bigint | 8 | 0 |  |  |  |
| MessageId | nvarchar | 100 | 0 |  |  |  |
| waveId | nvarchar | 8000 | 1 |  |  |  |
| Sequence | bigint | 8 | 0 |  |  |  |
| MessageTypeId | int | 4 | 0 |  |  |  |
| EnqueuedTimeUTC | datetime | 8 | 0 |  |  |  |

