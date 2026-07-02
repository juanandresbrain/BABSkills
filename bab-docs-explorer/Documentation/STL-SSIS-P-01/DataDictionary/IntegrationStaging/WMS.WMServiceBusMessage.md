# WMS.WMServiceBusMessage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServiceBusMessageId | bigint | 8 | 0 | YES |  |  |
| MessageId | nvarchar | 100 | 0 |  |  |  |
| Message | text | 16 | 1 |  |  |  |
| Sequence | bigint | 8 | 0 |  |  |  |
| MessageTypeId | int | 4 | 0 |  | YES |  |
| EnqueuedTimeUTC | datetime | 8 | 0 |  |  |  |

