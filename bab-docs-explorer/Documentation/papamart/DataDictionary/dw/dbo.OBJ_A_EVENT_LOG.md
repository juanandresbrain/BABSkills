# dbo.OBJ_A_EVENT_LOG

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| A_EVLOG_N_ID | int | 4 | 0 |  |  |  |
| A_EVLOG_N_TYPEID | int | 4 | 0 |  |  |  |
| A_EVLOG_D_STARTIME | datetime | 8 | 0 |  |  |  |
| A_EVLOG_N_DURATION | int | 4 | 0 |  |  |  |
| A_EVLOG_C_USER | varchar | 35 | 0 |  |  |  |
| A_EVLOG_C_SESSION | varchar | 254 | 0 |  |  |  |
| A_EVLOG_N_APPID | int | 4 | 0 |  |  |  |
| A_EVLOG_N_ERRORID | int | 4 | 0 |  |  |  |
| A_EVLOG_C_HOST | varchar | 254 | 0 |  |  |  |
| A_EVLOG_N_CLSTRID | int | 4 | 1 |  |  |  |
