# dbo.EVNT_STSTC_HSTRY_X

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POST_DAY | tinyint | 1 | 0 |  |  |  |
| POST_WEEK | tinyint | 1 | 0 |  |  |  |
| POST_MNTH | tinyint | 1 | 0 |  |  |  |
| POST_YEAR | smallint | 2 | 0 |  |  |  |
| KEY_1 | int | 4 | 0 |  |  |  |
| KEY_2 | int | 4 | 0 |  |  |  |
| KEY_3 | int | 4 | 0 |  |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| EVNT_STSTC_HSTRY_ID | int | 4 | 0 | YES |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_4_SUM | bigint | 8 | 0 |  |  |  |
| FLD_4_MIN | int | 4 | 0 |  |  |  |
| FLD_4_MAX | int | 4 | 0 |  |  |  |
| FLD_4_FRST | nvarchar | 510 | 0 |  |  |  |
| FLD_4_LAST | nvarchar | 510 | 0 |  |  |  |
