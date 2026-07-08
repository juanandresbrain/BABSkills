# dbo.EVNT_STSTC_HSTRY_500007

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_STSTC_HSTRY_ID | int | 4 | 0 | YES |  |  |
| POST_DAY | tinyint | 1 | 0 |  |  |  |
| POST_WEEK | tinyint | 1 | 0 |  |  |  |
| POST_MNTH | tinyint | 1 | 0 |  |  |  |
| POST_YEAR | smallint | 2 | 0 |  |  |  |
| SRVR_NAME | nvarchar | 100 | 0 |  |  |  |
| APP_ID | decimal | 9 | 0 |  |  |  |
| PRDCT_ID | nvarchar | 60 | 0 |  |  |  |
| INSTNC_NUM | smallint | 2 | 0 |  |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_42_LAST | smallint | 2 | 1 |  |  |  |
