# dbo.BlitzFirst

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CheckDate | datetimeoffset | 10 | 1 |  |  |  |
| CheckID | int | 4 | 0 |  |  |  |
| Priority | tinyint | 1 | 0 |  |  |  |
| FindingsGroup | varchar | 50 | 0 |  |  |  |
| Finding | varchar | 200 | 0 |  |  |  |
| URL | varchar | 200 | 0 |  |  |  |
| Details | nvarchar | 8000 | 1 |  |  |  |
| HowToStopIt | xml | -1 | 1 |  |  |  |
| QueryPlan | xml | -1 | 1 |  |  |  |
| QueryText | nvarchar | -1 | 1 |  |  |  |
| StartTime | datetimeoffset | 10 | 1 |  |  |  |
| LoginName | nvarchar | 256 | 1 |  |  |  |
| NTUserName | nvarchar | 256 | 1 |  |  |  |
| OriginalLoginName | nvarchar | 256 | 1 |  |  |  |
| ProgramName | nvarchar | 256 | 1 |  |  |  |
| HostName | nvarchar | 256 | 1 |  |  |  |
| DatabaseID | int | 4 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| OpenTransactionCount | int | 4 | 1 |  |  |  |
| DetailsInt | int | 4 | 1 |  |  |  |
