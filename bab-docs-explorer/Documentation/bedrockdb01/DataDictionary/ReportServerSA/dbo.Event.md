# dbo.Event

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | uniqueidentifier | 16 | 0 |  |  |  |
| EventType | nvarchar | 520 | 0 |  |  |  |
| EventData | nvarchar | 520 | 1 |  |  |  |
| TimeEntered | datetime | 8 | 0 |  |  |  |
| ProcessStart | datetime | 8 | 1 |  |  |  |
| ProcessHeartbeat | datetime | 8 | 1 |  |  |  |
| BatchID | uniqueidentifier | 16 | 1 |  |  |  |
