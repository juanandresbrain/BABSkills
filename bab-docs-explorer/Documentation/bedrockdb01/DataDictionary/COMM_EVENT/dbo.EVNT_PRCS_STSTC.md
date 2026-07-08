# dbo.EVNT_PRCS_STSTC

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ROW_ID | tinyint | 1 | 0 | YES |  |  |
| ENBLD | tinyint | 1 | 1 |  |  |  |
| STRT_DTM | datetime | 8 | 1 |  |  |  |
| END_DTM | datetime | 8 | 1 |  |  |  |
| CNT | int | 4 | 1 |  |  |  |
| TL_TRVL_DRTN | int | 4 | 1 |  |  |  |
| TL_WAIT_DRTN | int | 4 | 1 |  |  |  |
| LAST_ALRM_ID | int | 4 | 1 |  |  |  |
