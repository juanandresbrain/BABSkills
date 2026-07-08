# dbo.tblFile

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FileID | numeric | 9 | 0 | YES |  |  |
| FileQueueID | numeric | 9 | 0 |  |  |  |
| FileRemoteNum | numeric | 9 | 0 |  |  |  |
| FileOffset | int | 4 | 1 |  |  |  |
| FileSize | int | 4 | 1 |  |  |  |
| LastXFerSize | int | 4 | 1 |  |  |  |
| FilePercent | smallint | 2 | 1 |  |  |  |
| LocalFileName | varchar | 255 | 0 |  |  |  |
| RemoteFileName | varchar | 255 | 0 |  |  |  |
| CreationDT | datetime | 8 | 1 |  |  |  |
| LastAckDT | datetime | 8 | 1 |  |  |  |
| StartInitXFerDT | datetime | 8 | 1 |  |  |  |
| StartXFerDT | datetime | 8 | 1 |  |  |  |
| EndXFerDT | datetime | 8 | 1 |  |  |  |
| XFerTime | int | 4 | 1 |  |  |  |
| State | varchar | 128 | 0 |  |  |  |
| PostingName | varchar | 80 | 0 |  |  |  |
| CodeState | int | 4 | 1 |  |  |  |
| Origin | smallint | 2 | 1 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
