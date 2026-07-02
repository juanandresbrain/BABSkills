# dbo.BossWMSLog

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | int | 4 | 0 | YES |  |  |
| Direction | varchar | 250 | 0 |  |  |  |
| Data | varchar | 250 | 1 |  |  |  |
| LogCreatedDate | datetime | 8 | 0 |  |  |  |
| SequenceNumber | int | 4 | 1 |  |  |  |
| ProcessID | int | 4 | 1 |  | YES |  |

