# dbo.EVNT_STSTC_HSTRY_500009

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
| KEY_1 | smallint | 2 | 1 |  |  |  |
| KEY_2 | smallint | 2 | 1 |  |  |  |
| POST_DTM | smalldatetime | 4 | 0 |  |  |  |
| CNT | int | 4 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| CRTD_DTM | smalldatetime | 4 | 0 |  |  |  |
| FLD_53_LAST | smallint | 2 | 1 |  |  |  |
| FLD_54_LAST | datetime | 8 | 1 |  |  |  |
| FLD_51_LAST | datetime | 8 | 1 |  |  |  |
| FLD_52_LAST | datetime | 8 | 1 |  |  |  |
