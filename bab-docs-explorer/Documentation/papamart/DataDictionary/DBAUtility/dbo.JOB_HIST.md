# dbo.JOB_HIST

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SERVER_NM | nvarchar | 256 | 1 |  |  |  |
| JOB_NM | nvarchar | 256 | 1 |  |  |  |
| STEP_NM | nvarchar | 256 | 1 |  |  |  |
| STEP_ID | int | 4 | 1 |  |  |  |
| STEP_NM_HIST | nvarchar | 256 | 1 |  |  |  |
| RUN_DT | int | 4 | 1 |  |  |  |
| RUN_TM | int | 4 | 1 |  |  |  |
| SQL_SEVERITY | int | 4 | 1 |  |  |  |
| MESSAGE_TXT | varchar | 7000 | 1 |  |  |  |
| INSERT_DT | datetime | 8 | 0 |  |  |  |
