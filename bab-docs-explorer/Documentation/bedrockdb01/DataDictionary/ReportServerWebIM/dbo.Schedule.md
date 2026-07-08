# dbo.Schedule

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ScheduleID | uniqueidentifier | 16 | 0 |  |  |  |
| Name | nvarchar | 520 | 0 |  |  |  |
| StartDate | datetime | 8 | 0 |  |  |  |
| Flags | int | 4 | 0 |  |  |  |
| NextRunTime | datetime | 8 | 1 |  |  |  |
| LastRunTime | datetime | 8 | 1 |  |  |  |
| EndDate | datetime | 8 | 1 |  |  |  |
| RecurrenceType | int | 4 | 1 |  |  |  |
| MinutesInterval | int | 4 | 1 |  |  |  |
| DaysInterval | int | 4 | 1 |  |  |  |
| WeeksInterval | int | 4 | 1 |  |  |  |
| DaysOfWeek | int | 4 | 1 |  |  |  |
| DaysOfMonth | int | 4 | 1 |  |  |  |
| Month | int | 4 | 1 |  |  |  |
| MonthlyWeek | int | 4 | 1 |  |  |  |
| State | int | 4 | 1 |  |  |  |
| LastRunStatus | nvarchar | 520 | 1 |  |  |  |
| ScheduledRunTimeout | int | 4 | 1 |  |  |  |
| CreatedById | uniqueidentifier | 16 | 0 |  |  |  |
| EventType | nvarchar | 520 | 0 |  |  |  |
| EventData | nvarchar | 520 | 1 |  |  |  |
| Type | int | 4 | 0 |  |  |  |
| ConsistancyCheck | datetime | 8 | 1 |  |  |  |
| Path | nvarchar | 520 | 1 |  |  |  |
