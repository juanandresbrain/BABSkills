# dbo.tblWebLatencyStat

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WebLatencyStatID | int | 4 | 0 | YES |  |  |
| RemoteNumber | int | 4 | 0 |  |  |  |
| LastTimeEvent | datetime | 8 | 0 |  |  |  |
| HourlyNbrPing | int | 4 | 0 |  |  |  |
| RTHourlyAvg | decimal | 9 | 0 |  |  |  |
| DailyNbrPing | int | 4 | 0 |  |  |  |
| RTDailyAvg | decimal | 9 | 0 |  |  |  |
| WeeklyNbrPing | int | 4 | 0 |  |  |  |
| RTWeeklyAvg | decimal | 9 | 0 |  |  |  |
| RegisterNumber | int | 4 | 0 |  |  |  |
