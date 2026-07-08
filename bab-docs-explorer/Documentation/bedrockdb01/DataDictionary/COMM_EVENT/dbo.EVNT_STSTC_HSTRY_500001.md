# dbo.EVNT_STSTC_HSTRY_500001

**Database:** COMM_EVENT  
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
| KEY_1 | smallint | 2 | 1 |  |  |  |
| KEY_2 | smallint | 2 | 1 |  |  |  |
| KEY_4 | smallint | 2 | 1 |  |  |  |
| KEY_5 | smallint | 2 | 1 |  |  |  |
| KEY_6 | smallint | 2 | 1 |  |  |  |
| KEY_15 | smallint | 2 | 1 |  |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_16_SUM | float | 8 | 1 |  |  |  |
| FLD_16_MAX | bigint | 8 | 1 |  |  |  |
| FLD_16_MIN | bigint | 8 | 1 |  |  |  |
| FLD_17_SUM | float | 8 | 1 |  |  |  |
| FLD_17_MAX | bigint | 8 | 1 |  |  |  |
| FLD_17_MIN | bigint | 8 | 1 |  |  |  |
| FLD_18_SUM | float | 8 | 1 |  |  |  |
| FLD_18_MAX | smallint | 2 | 1 |  |  |  |
| FLD_18_MIN | smallint | 2 | 1 |  |  |  |
| FLD_19_SUM | float | 8 | 1 |  |  |  |
| FLD_19_MAX | smallint | 2 | 1 |  |  |  |
| FLD_19_MIN | smallint | 2 | 1 |  |  |  |
| FLD_48_LAST | int | 4 | 1 |  |  |  |
| FLD_49_LAST | nvarchar | 40 | 1 |  |  |  |
