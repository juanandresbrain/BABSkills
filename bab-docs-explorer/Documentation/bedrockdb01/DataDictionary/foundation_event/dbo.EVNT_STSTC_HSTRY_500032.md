# dbo.EVNT_STSTC_HSTRY_500032

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
| KEY_34 | nvarchar | 100 | 1 |  |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_466_LAST | smallint | 2 | 1 |  |  |  |
| FLD_30_SUM | float | 8 | 1 |  |  |  |
| FLD_30_MAX | bigint | 8 | 1 |  |  |  |
| FLD_32_SUM | float | 8 | 1 |  |  |  |
| FLD_32_MAX | bigint | 8 | 1 |  |  |  |
| FLD_31_SUM | float | 8 | 1 |  |  |  |
| FLD_31_MAX | bigint | 8 | 1 |  |  |  |
| FLD_33_SUM | float | 8 | 1 |  |  |  |
| FLD_33_MAX | bigint | 8 | 1 |  |  |  |
