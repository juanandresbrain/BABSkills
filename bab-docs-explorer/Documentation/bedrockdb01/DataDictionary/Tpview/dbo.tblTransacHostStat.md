# dbo.tblTransacHostStat

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransacStatHostID | int | 4 | 0 | YES |  |  |
| MsgType | varchar | 2 | 0 |  |  |  |
| Card | varchar | 2 | 0 |  |  |  |
| Service | varchar | 2 | 0 |  |  |  |
| LastEventTime | datetime | 8 | 0 |  |  |  |
| HourlyNbrTransac | int | 4 | 0 |  |  |  |
| HourlyRespAvg | decimal | 9 | 0 |  |  |  |
| DailyNbrTransac | int | 4 | 0 |  |  |  |
| DailyRespAvg | decimal | 9 | 0 |  |  |  |
| WeeklyNbrTransac | int | 4 | 0 |  |  |  |
| WeeklyRespAvg | decimal | 9 | 0 |  |  |  |
