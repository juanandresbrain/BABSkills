# dbo.MONITOR_CHG

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MONITOR_CHG_ID | int | 4 | 0 | YES |  |  |
| SERVER_NM | nvarchar | 256 | 0 |  |  |  |
| EVENT_TYPE | nvarchar | -1 | 1 |  |  |  |
| SCHEMA_NM | nvarchar | -1 | 1 |  |  |  |
| OBJECT_NM | nvarchar | -1 | 1 |  |  |  |
| OBJECT_TYPE | nvarchar | -1 | 1 |  |  |  |
| EVENT_DT | datetime | 8 | 1 |  |  |  |
| SYSTEMUSER | varchar | 100 | 1 |  |  |  |
| CURRENTUSER | varchar | 100 | 1 |  |  |  |
| ORIGINALUSER | varchar | 100 | 1 |  |  |  |
| DATABASE_NM | varchar | 100 | 1 |  |  |  |
| TSQLCODE | nvarchar | -1 | 1 |  |  |  |
| EMAILSENT | bit | 1 | 1 |  |  |  |
