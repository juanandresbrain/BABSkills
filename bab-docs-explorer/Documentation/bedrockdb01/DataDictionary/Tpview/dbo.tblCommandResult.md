# dbo.tblCommandResult

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CommandResultID | int | 4 | 0 | YES |  |  |
| CommandID | int | 4 | 0 |  |  |  |
| RemoteNumber | int | 4 | 0 |  |  |  |
| QueueID | numeric | 9 | 1 |  |  |  |
| ResultCode | int | 4 | 0 |  |  |  |
| Result | varchar | 100 | 0 |  |  |  |
| ResultTime | datetime | 8 | 0 |  |  |  |
