# dbo.SV_ADDRESS

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRTY_ID | binary | 16 | 0 |  |  |  |
| ADRS_ID | binary | 16 | 0 |  |  |  |
| PRTY_ADRS_SEQ | numeric | 9 | 0 |  |  |  |
| ADRS_LINE_1 | varchar | 50 | 1 |  |  |  |
| ADRS_LINE_2 | varchar | 50 | 1 |  |  |  |
| ADRS_LINE_3 | varchar | 50 | 1 |  |  |  |
| ADRS_LINE_4 | varchar | 50 | 1 |  |  |  |
| CITY | varchar | 50 | 1 |  |  |  |
| POST_CODE | varchar | 15 | 1 |  |  |  |
| TRTRY_CODE | char | 3 | 1 |  |  |  |
| CNTRY_CODE_ISO3 | char | 3 | 0 |  |  |  |
| EFCTV_STRT_DATE | datetime | 8 | 0 |  |  |  |
| EFCTV_END_DATE | datetime | 8 | 1 |  |  |  |
| ADRS_EXPRTN_RSN_ID | binary | 16 | 1 |  |  |  |
| PRTY_ADRS_DESC | varchar | 255 | 0 |  |  |  |
| ADRS_FNCTN_CODE | varchar | 4 | 0 |  |  |  |
| ADRS_FNCTN_DESC | varchar | 255 | 1 |  |  |  |
| ADRS_FNCTN_SHRT_DESC | varchar | 50 | 1 |  |  |  |
| LANG_ID | int | 4 | 1 |  |  |  |
