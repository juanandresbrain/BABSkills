# dbo.EVNT_STSTC_500004

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_STSTC_ID | int | 4 | 0 | YES |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| SRVR_NAME | nvarchar | 100 | 0 |  |  |  |
| APP_ID | decimal | 9 | 0 |  |  |  |
| PRDCT_ID | nvarchar | 60 | 0 |  |  |  |
| INSTNC_NUM | smallint | 2 | 0 |  |  |  |
| KEY_1 | smallint | 2 | 1 |  |  |  |
| KEY_2 | smallint | 2 | 1 |  |  |  |
| KEY_4 | smallint | 2 | 1 |  |  |  |
| KEY_5 | smallint | 2 | 1 |  |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_26_SUM | float | 8 | 1 |  |  |  |
| FLD_26_MAX | bigint | 8 | 1 |  |  |  |
| FLD_26_MIN | bigint | 8 | 1 |  |  |  |
| FLD_27_SUM | float | 8 | 1 |  |  |  |
