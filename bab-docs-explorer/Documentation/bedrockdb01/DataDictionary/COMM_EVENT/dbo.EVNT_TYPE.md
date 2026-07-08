# dbo.EVNT_TYPE

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| EVNT_TYPE_NAME_RSRC | nvarchar | 510 | 0 |  |  |  |
| EVNT_TYPE_DESC_RSRC | nvarchar | 510 | 0 |  |  |  |
| EVNT_TYPE_CTGRY_ID | smallint | 2 | 0 |  |  |  |
| STSTC_LVL | tinyint | 1 | 0 |  |  |  |
| NUM_DAYS_KEEP_EVNT | smallint | 2 | 0 |  |  |  |
| NUM_STSTC_KEEP_YEAR | tinyint | 1 | 1 |  |  |  |
| NUM_STSTC_KEEP_MNTH | tinyint | 1 | 1 |  |  |  |
| NUM_STSTC_KEEP_WEEK | smallint | 2 | 1 |  |  |  |
| NUM_STSTC_KEEP_DAY | smallint | 2 | 1 |  |  |  |
| NUM_STSTC_KEEP_HOUR | smallint | 2 | 1 |  |  |  |
| CONT_INCTVTY_DLY | smallint | 2 | 1 |  |  |  |
| ENBL_RPRT | decimal | 5 | 0 |  |  |  |
| EVNT_TBL_CRTD | tinyint | 1 | 0 |  |  |  |
| LAST_STSTC_EVNT_ID | int | 4 | 1 |  |  |  |
| LAST_HSTRY_EVNT_ID | int | 4 | 1 |  |  |  |
| APP_ID | smallint | 2 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| EVNT_GRP_ID | smallint | 2 | 1 |  |  |  |
| SRVR_NAME_IS_KEY | decimal | 5 | 0 |  |  |  |
| APP_ID_IS_KEY | decimal | 5 | 0 |  |  |  |
| PRDCT_ID_IS_KEY | decimal | 5 | 0 |  |  |  |
| INSTNC_NUM_IS_KEY | decimal | 5 | 0 |  |  |  |
| USER_ID_IS_KEY | decimal | 5 | 0 |  |  |  |
