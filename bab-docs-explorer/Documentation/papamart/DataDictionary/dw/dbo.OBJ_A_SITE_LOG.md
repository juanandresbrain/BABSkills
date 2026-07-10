# dbo.OBJ_A_SITE_LOG

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| A_STLOG_N_ID | int | 4 | 0 |  |  |  |
| A_STLOG_N_LOGLEVEL | int | 4 | 1 |  |  |  |
| A_STLOG_D_LOGTIME | datetime | 8 | 1 |  |  |  |
| A_STLOG_C_LOGHOST | varchar | 35 | 0 |  |  |  |
| A_STLOG_C_LOGMODUL | varchar | 35 | 0 |  |  |  |
| A_STLOG_N_LOGPID | int | 4 | 0 |  |  |  |
| A_STLOG_C_LOGINFO | varchar | 75 | 0 |  |  |  |
| A_STLOG_N_CLSTRID | int | 4 | 1 |  |  |  |
