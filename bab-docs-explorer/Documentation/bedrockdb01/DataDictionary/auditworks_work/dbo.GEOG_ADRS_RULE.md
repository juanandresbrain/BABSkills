# dbo.GEOG_ADRS_RULE

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ADRS_RULE_ID | binary | 16 | 0 |  |  |  |
| ADRS_RULE_DESC | varchar | 255 | 1 |  |  |  |
| LINE_1_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_LINE_1_DESC | varchar | 50 | 1 |  |  |  |
| LINE_2_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_LINE_2_DESC | varchar | 50 | 1 |  |  |  |
| LINE_3_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_LINE_3_DESC | varchar | 50 | 1 |  |  |  |
| LINE_4_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_LINE_4_DESC | varchar | 50 | 1 |  |  |  |
| CITY_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_CITY_DESC | varchar | 50 | 1 |  |  |  |
| TRTRY_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_TRTRY_DESC | varchar | 50 | 1 |  |  |  |
| POST_CODE_REQ | numeric | 5 | 0 |  |  |  |
| ADRS_POST_CODE_DESC | varchar | 50 | 1 |  |  |  |
| LINE_1_VLDTN | varchar | 510 | 1 |  |  |  |
| LINE_2_VLDTN | varchar | 510 | 1 |  |  |  |
| LINE_3_VLDTN | varchar | 510 | 1 |  |  |  |
| LINE_4_VLDTN | varchar | 510 | 1 |  |  |  |
| CITY_VLDTN | varchar | 510 | 1 |  |  |  |
| TRTRY_VLDTN | varchar | 510 | 1 |  |  |  |
| POST_CODE_VLDTN | varchar | 510 | 1 |  |  |  |
| POST_CODE_FRMT | varchar | 510 | 1 |  |  |  |
| MAIL_FRMT | nvarchar | 2000 | 1 |  |  |  |
| ADRS_MTCH_KEY_RULE | varchar | 510 | 1 |  |  |  |
| ADRS_DESC_DFLT_INSTRCT | varchar | 50 | 1 |  |  |  |
