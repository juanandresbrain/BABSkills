# dbo.EVNT_300001

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_ID | int | 4 | 0 | YES |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| SRVR_NAME | varchar | 50 | 0 |  |  |  |
| APP_ID | decimal | 9 | 0 |  |  |  |
| PRDCT_ID | varchar | 30 | 0 |  |  |  |
| INSTNC_NUM | smallint | 2 | 0 |  |  |  |
| USER_ID | decimal | 9 | 0 |  |  |  |
| EVNT_POST_DTM | datetime | 8 | 0 |  |  |  |
| EVNT_CRTN_DTM | datetime | 8 | 0 |  |  |  |
| STRG_MCHNSM | nvarchar | 60 | 0 |  |  |  |
| FLD_715 | int | 4 | 1 |  |  |  |
| FLD_418 | nvarchar | 510 | 1 |  |  |  |
| FLD_419 | nvarchar | 510 | 1 |  |  |  |
| FLD_716 | smallint | 2 | 1 |  |  |  |
| FLD_421 | nvarchar | 8000 | 1 |  |  |  |
| FLD_717 | nvarchar | 100 | 1 |  |  |  |
