# dbo.FNDTN_SYNC_LOCK

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SYNC_LOCK_ID | T_ID | 16 | 0 |  |  |  |
| TKN | varchar | 50 | 0 |  |  |  |
| FMLY_ID | int | 4 | 0 |  |  |  |
| SRVC_NAME | varchar | 50 | 1 |  |  |  |
| SGMNT_ID | numeric | 9 | 1 |  |  |  |
| JOB_ID | int | 4 | 1 |  |  |  |
| EXCTN_ID | int | 4 | 1 |  |  |  |
| PRCS_ID | int | 4 | 1 |  |  |  |
| MCHN_NAME | varchar | 50 | 1 |  |  |  |
| STRT_DATE | datetime | 8 | 0 |  |  |  |
| EXPRY_DATE | datetime | 8 | 1 |  |  |  |
