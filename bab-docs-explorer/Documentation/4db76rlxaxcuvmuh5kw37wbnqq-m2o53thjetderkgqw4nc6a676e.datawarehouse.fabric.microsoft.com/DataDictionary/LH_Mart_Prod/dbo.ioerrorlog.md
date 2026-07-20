# dbo.ioerrorlog

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | varchar | 8000 | 1 |  |  |  |
| LogFileName | varchar | 8000 | 1 |  |  |  |
| Occurances | int | 4 | 1 |  |  |  |
| LogDate | datetime2 | 8 | 1 |  |  |  |
| ProcessInfo | varchar | 8000 | 1 |  |  |  |
| ErrorText | varchar | 8000 | 1 |  |  |  |
