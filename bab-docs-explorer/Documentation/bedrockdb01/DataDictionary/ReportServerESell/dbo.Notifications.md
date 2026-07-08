# dbo.Notifications

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NotificationID | uniqueidentifier | 16 | 0 |  |  |  |
| SubscriptionID | uniqueidentifier | 16 | 0 |  |  |  |
| ActivationID | uniqueidentifier | 16 | 1 |  |  |  |
| ReportID | uniqueidentifier | 16 | 0 |  |  |  |
| SnapShotDate | datetime | 8 | 1 |  |  |  |
| ExtensionSettings | ntext | 16 | 0 |  |  |  |
| Locale | nvarchar | 256 | 0 |  |  |  |
| Parameters | ntext | 16 | 1 |  |  |  |
| ProcessStart | datetime | 8 | 1 |  |  |  |
| NotificationEntered | datetime | 8 | 0 |  |  |  |
| ProcessAfter | datetime | 8 | 1 |  |  |  |
| Attempt | int | 4 | 1 |  |  |  |
| SubscriptionLastRunTime | datetime | 8 | 0 |  |  |  |
| DeliveryExtension | nvarchar | 520 | 0 |  |  |  |
| SubscriptionOwnerID | uniqueidentifier | 16 | 0 |  |  |  |
| IsDataDriven | bit | 1 | 0 |  |  |  |
| BatchID | uniqueidentifier | 16 | 1 |  |  |  |
| ProcessHeartbeat | datetime | 8 | 1 |  |  |  |
| Version | int | 4 | 0 |  |  |  |
| ReportZone | int | 4 | 0 |  |  |  |
