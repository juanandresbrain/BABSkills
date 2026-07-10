# dbo.maint_blocking_log

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| srvname | varchar | 50 | 1 |  |  |  |
| block_spid | int | 4 | 1 |  |  |  |
| blocking_spid | int | 4 | 1 |  |  |  |
| last_batch | datetime | 8 | 1 |  |  |  |
| time_checked | datetime | 8 | 1 |  |  |  |
