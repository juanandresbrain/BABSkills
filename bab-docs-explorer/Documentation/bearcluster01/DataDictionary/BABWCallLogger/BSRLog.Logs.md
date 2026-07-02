# BSRLog.Logs

**Database:** BABWCallLogger  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 |  |  |  |
| agent_id | int | 4 | 1 |  |  |  |
| actiondesc | varchar | 300 | 1 |  |  |  |
| creationdate | datetime | 8 | 1 |  |  |  |
| errormessage | varchar | 500 | 1 |  |  |  |

