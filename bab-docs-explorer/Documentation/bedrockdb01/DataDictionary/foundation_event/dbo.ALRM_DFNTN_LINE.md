# dbo.ALRM_DFNTN_LINE

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_DFNTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ALRM_DFNTN_LINE_SEQ | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| LGCL_OPRTR | T_CODE3 | 3 | 1 |  |  |  |
| SRC_FNCTN | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| SRC_EVNT_KEY_ID_1 | T_INTEGER | 2 | 1 |  |  |  |
| SRC_EVNT_KEY_ID_2 | T_INTEGER | 2 | 1 |  |  |  |
| CMPRSN_OPRTR | T_LONG_CODE | 20 | 0 |  |  |  |
| DSTNTN_FNCTN | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_ID_1 | T_INTEGER | 2 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_ID_2 | T_INTEGER | 2 | 1 |  |  |  |
| VAL_LIST | nvarchar | 510 | 1 |  |  |  |
| SRC_EVNT_KEY_STSTC_TYPE_1 | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| SRC_EVNT_KEY_STSTC_TYPE_2 | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_STSTC_TYPE_1 | T_SMALL_INTEGER | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_STSTC_TYPE_2 | T_SMALL_INTEGER | 1 | 1 |  |  |  |
