# dbo.tblRemotePollState

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RemotePollStateID | numeric | 9 | 0 | YES |  |  |
| RPSRemoteNum | numeric | 9 | 0 |  |  |  |
| RPSState | int | 4 | 0 |  |  |  |
| ErrorCode | int | 4 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| LogTime | datetime | 8 | 0 |  |  |  |
| Comments | varchar | 80 | 0 |  |  |  |
| NumBusy | int | 4 | 1 |  |  |  |
| RPSIntervalName | varchar | 20 | 0 |  |  |  |
| RPSReason | varchar | 20 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
