# audit.StatisticLog

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | int | 4 | 0 |  |  |  |
| ComponentName | varchar | 50 | 0 |  |  |  |
| Rows | int | 4 | 1 |  |  |  |
| TimeMS | int | 4 | 1 |  |  |  |
| MinRowsPerSec | int | 4 | 1 |  |  |  |
| MeanRowsPerSec | int | 4 | 1 |  |  |  |
| MaxRowsPerSec | int | 4 | 1 |  |  |  |
| LogTime | datetime | 8 | 1 |  |  |  |
