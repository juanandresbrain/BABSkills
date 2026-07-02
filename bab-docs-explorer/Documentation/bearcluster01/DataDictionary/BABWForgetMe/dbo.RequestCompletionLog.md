# dbo.RequestCompletionLog

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RequestLogID | int | 4 | 0 | YES |  |  |
| RecordKey | varchar | 26 | 0 |  | YES |  |
| AQKey | int | 4 | 0 |  | YES |  |
| Completed | bit | 1 | 0 |  |  |  |

