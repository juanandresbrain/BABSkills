# dbo.AzureServiceBusTest

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| ExpiresAtUTC | nvarchar | 8000 | 1 |  |  |  |
| Label | nvarchar | 8000 | 1 |  |  |  |
| Message | nvarchar | 100 | 1 |  |  |  |
| MessageId | nvarchar | 8000 | 1 |  |  |  |
| Sequence | bigint | 8 | 1 |  |  |  |
| Size | bigint | 8 | 1 |  |  |  |

