# dbo.tblConnectionStat

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ConnectionStatID | int | 4 | 0 | YES |  |  |
| RemoteNumber | int | 4 | 0 |  |  |  |
| ConnectType | int | 4 | 0 |  |  |  |
| LastConnectTime | datetime | 8 | 0 |  |  |  |
| HourlyNbrConnect | int | 4 | 0 |  |  |  |
| DailyNbrConnect | int | 4 | 0 |  |  |  |
| WeeklyNbrConnect | int | 4 | 0 |  |  |  |
| LastDisconnectTime | datetime | 8 | 0 |  |  |  |
| HourlyNbrDisconnect | int | 4 | 0 |  |  |  |
| DailyNbrDisconnect | int | 4 | 0 |  |  |  |
| WeeklyNbrDisconnect | int | 4 | 0 |  |  |  |
| LastDurationTime | datetime | 8 | 0 |  |  |  |
| HourlyDuration | int | 4 | 0 |  |  |  |
| DailyDuration | int | 4 | 0 |  |  |  |
| WeeklyDuration | int | 4 | 0 |  |  |  |
| RegisterNumber | int | 4 | 0 |  |  |  |
