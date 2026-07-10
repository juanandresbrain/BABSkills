# dbo.TSWeb

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowNumber | int | 4 | 0 | YES |  |  |
| EventClass | int | 4 | 1 |  |  |  |
| TextData | ntext | 16 | 1 |  |  |  |
| DatabaseID | int | 4 | 1 |  |  |  |
| NTUserName | nvarchar | 256 | 1 |  |  |  |
| HostName | nvarchar | 256 | 1 |  |  |  |
| ClientProcessID | int | 4 | 1 |  |  |  |
| ApplicationName | nvarchar | 256 | 1 |  |  |  |
| LoginName | nvarchar | 256 | 1 |  |  |  |
| SPID | int | 4 | 1 |  |  |  |
| Duration | bigint | 8 | 1 |  |  |  |
| StartTime | datetime | 8 | 1 |  |  |  |
| Reads | bigint | 8 | 1 |  |  |  |
| Writes | bigint | 8 | 1 |  |  |  |
| CPU | int | 4 | 1 |  |  |  |
