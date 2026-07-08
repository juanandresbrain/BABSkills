# dbo.EVNT_PRCS_STSTC

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ROW_ID | T_SMALL_INTEGER | 1 | 0 | YES |  |  |
| ENBLD | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| STRT_DTM | T_DATETIME | 8 | 1 |  |  |  |
| END_DTM | T_DATETIME | 8 | 1 |  |  |  |
| CNT | T_LONG_INTEGER | 4 | 1 |  |  |  |
| TL_TRVL_DRTN | T_LONG_INTEGER | 4 | 1 |  |  |  |
| TL_WAIT_DRTN | T_LONG_INTEGER | 4 | 1 |  |  |  |
| LAST_ALRM_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
