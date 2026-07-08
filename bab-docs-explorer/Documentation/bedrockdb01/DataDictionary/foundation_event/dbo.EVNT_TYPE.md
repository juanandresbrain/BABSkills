# dbo.EVNT_TYPE

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_TYPE_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| EVNT_TYPE_NAME_RSRC | T_LONG_DATA | 255 | 0 |  |  |  |
| EVNT_TYPE_DESC_RSRC | T_LONG_DATA | 255 | 0 |  |  |  |
| EVNT_TYPE_CTGRY_ID | T_INTEGER | 2 | 0 |  |  |  |
| STSTC_LVL | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| NUM_DAYS_KEEP_EVNT | T_INTEGER | 2 | 0 |  |  |  |
| NUM_STSTC_KEEP_YEAR | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| NUM_STSTC_KEEP_MNTH | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| NUM_STSTC_KEEP_WEEK | T_INTEGER | 2 | 1 |  |  |  |
| NUM_STSTC_KEEP_DAY | T_INTEGER | 2 | 1 |  |  |  |
| NUM_STSTC_KEEP_HOUR | T_INTEGER | 2 | 1 |  |  |  |
| CONT_INCTVTY_DLY | T_INTEGER | 2 | 1 |  |  |  |
| ENBL_RPRT | T_BOOLEAN | 5 | 0 |  |  |  |
| EVNT_TBL_CRTD | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| LAST_STSTC_EVNT_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| LAST_HSTRY_EVNT_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| APP_ID | T_INTEGER | 2 | 0 |  |  |  |
| LAST_MDFD_DTM | T_DATETIME | 8 | 0 |  |  |  |
| EVNT_GRP_ID | T_INTEGER | 2 | 1 |  |  |  |
| SRVR_NAME_IS_KEY | T_BOOLEAN | 5 | 1 |  |  |  |
| APP_ID_IS_KEY | T_BOOLEAN | 5 | 1 |  |  |  |
| PRDCT_ID_IS_KEY | T_BOOLEAN | 5 | 1 |  |  |  |
| INSTNC_NUM_IS_KEY | T_BOOLEAN | 5 | 1 |  |  |  |
| USER_ID_IS_KEY | T_BOOLEAN | 5 | 1 |  |  |  |
