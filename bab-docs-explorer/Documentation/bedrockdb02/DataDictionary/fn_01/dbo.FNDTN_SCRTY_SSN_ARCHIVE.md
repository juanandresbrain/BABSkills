# dbo.FNDTN_SCRTY_SSN_ARCHIVE

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SSN_ID | T_ID | 16 | 0 |  |  |  |
| USER_ID | int | 4 | 0 |  |  |  |
| APP_ID | int | 4 | 0 |  |  |  |
| CMPNY_ID | int | 4 | 0 |  |  |  |
| CRNT_MDL | varchar | 20 | 1 |  |  |  |
| CRNT_ITEM | int | 4 | 0 |  |  |  |
| STRT_TIME | datetime | 8 | 0 |  |  |  |
| MCHN_NAME | varchar | 255 | 0 |  |  |  |
| PID | int | 4 | 0 |  |  |  |
| LAST_VLDTN | datetime | 8 | 1 |  |  |  |
| LCKD | bit | 1 | 1 |  |  |  |
| CLND | int | 4 | 1 |  |  |  |

