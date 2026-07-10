# audit.CommandLog

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | int | 4 | 0 |  |  |  |
| CommandID | int | 4 | 0 |  |  |  |
| Key | varchar | 50 | 1 |  |  |  |
| Type | varchar | 50 | 1 |  |  |  |
| Value | varchar | -1 | 1 |  |  |  |
| LogTime | datetime | 8 | 1 |  |  |  |
