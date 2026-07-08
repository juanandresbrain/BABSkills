# dbo.ActiveSubscriptions

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActiveID | uniqueidentifier | 16 | 0 |  |  |  |
| SubscriptionID | uniqueidentifier | 16 | 0 |  |  |  |
| TotalNotifications | int | 4 | 1 |  |  |  |
| TotalSuccesses | int | 4 | 0 |  |  |  |
| TotalFailures | int | 4 | 0 |  |  |  |
