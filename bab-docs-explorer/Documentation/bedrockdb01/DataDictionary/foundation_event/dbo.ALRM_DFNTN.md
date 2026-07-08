# dbo.ALRM_DFNTN

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_DFNTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| EVNT_TYPE_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ALRM_NAME | nvarchar | 510 | 0 |  |  |  |
| ALRM_DSCRPTN | nvarchar | 510 | 0 |  |  |  |
| ALRM_TEXT | T_SHORT_TEXT | 4000 | 0 |  |  |  |
| SVRTY | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| ENBLD | T_BOOLEAN | 5 | 0 |  |  |  |
| TRGR_TYPE | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| TEST_FRQNCY_MNT | T_INTEGER | 2 | 1 |  |  |  |
| TEST_BCKT_LVL | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| NUM_DAYS_KEEP_ALRM | T_INTEGER | 2 | 0 |  |  |  |
| ALRM_QNTY | T_INTEGER | 2 | 0 |  |  |  |
| ALRM_DRTN | T_INTEGER | 2 | 0 |  |  |  |
| ALRM_QRY | T_SQL | 1000 | 0 |  |  |  |
| LAST_MDFD_DTM | T_DATETIME | 8 | 0 |  |  |  |
| LAST_EVNT_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| LAST_ALRM_DTM | T_DATETIME | 8 | 1 |  |  |  |
