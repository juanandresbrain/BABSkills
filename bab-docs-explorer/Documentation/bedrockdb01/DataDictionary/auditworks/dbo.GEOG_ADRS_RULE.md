# dbo.GEOG_ADRS_RULE

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ADRS_RULE_ID | T_ID | 16 | 0 |  |  |  |
| ADRS_RULE_DESC | nvarchar | 510 | 1 |  |  |  |
| LINE_1_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_LINE_1_DESC | nvarchar | 100 | 1 |  |  |  |
| LINE_2_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_LINE_2_DESC | nvarchar | 100 | 1 |  |  |  |
| LINE_3_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_LINE_3_DESC | nvarchar | 100 | 1 |  |  |  |
| LINE_4_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_LINE_4_DESC | nvarchar | 100 | 1 |  |  |  |
| CITY_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_CITY_DESC | nvarchar | 100 | 1 |  |  |  |
| TRTRY_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_TRTRY_DESC | nvarchar | 100 | 1 |  |  |  |
| POST_CODE_REQ | T_FLAG | 5 | 0 |  |  |  |
| ADRS_POST_CODE_DESC | nvarchar | 100 | 1 |  |  |  |
| LINE_1_VLDTN | nvarchar | 510 | 1 |  |  |  |
| LINE_2_VLDTN | nvarchar | 510 | 1 |  |  |  |
| LINE_3_VLDTN | nvarchar | 510 | 1 |  |  |  |
| LINE_4_VLDTN | nvarchar | 510 | 1 |  |  |  |
| CITY_VLDTN | nvarchar | 510 | 1 |  |  |  |
| TRTRY_VLDTN | nvarchar | 510 | 1 |  |  |  |
| POST_CODE_VLDTN | nvarchar | 510 | 1 |  |  |  |
| POST_CODE_FRMT | nvarchar | 510 | 1 |  |  |  |
| MAIL_FRMT | nvarchar | 2000 | 1 |  |  |  |
| ADRS_MTCH_KEY_RULE | nvarchar | 510 | 1 |  |  |  |
| ADRS_DESC_DFLT_INSTRCT | nvarchar | 100 | 1 |  |  |  |
