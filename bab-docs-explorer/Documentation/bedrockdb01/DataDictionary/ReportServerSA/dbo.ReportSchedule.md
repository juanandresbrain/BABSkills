# dbo.ReportSchedule

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ScheduleID | uniqueidentifier | 16 | 0 |  |  |  |
| ReportID | uniqueidentifier | 16 | 0 |  |  |  |
| SubscriptionID | uniqueidentifier | 16 | 1 |  |  |  |
| ReportAction | int | 4 | 0 |  |  |  |
