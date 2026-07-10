# dbo.IOErrorLog

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | nvarchar | 512 | 0 |  |  |  |
| LogFileName | nvarchar | 8000 | 0 |  |  |  |
| Occurances | int | 4 | 1 |  |  |  |
| LogDate | datetime | 8 | 0 |  |  |  |
| ProcessInfo | nvarchar | 100 | 1 |  |  |  |
| ErrorText | nvarchar | -1 | 1 |  |  |  |
