# dbo.ALRM_DFNTN_LINE

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_DFNTN_ID | int | 4 | 0 |  |  |  |
| ALRM_DFNTN_LINE_SEQ | tinyint | 1 | 0 |  |  |  |
| LGCL_OPRTR | nchar | 6 | 1 |  |  |  |
| SRC_FNCTN | tinyint | 1 | 1 |  |  |  |
| SRC_EVNT_KEY_ID_1 | smallint | 2 | 1 |  |  |  |
| SRC_EVNT_KEY_ID_2 | smallint | 2 | 1 |  |  |  |
| CMPRSN_OPRTR | nvarchar | 100 | 0 |  |  |  |
| DSTNTN_FNCTN | tinyint | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_ID_1 | smallint | 2 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_ID_2 | smallint | 2 | 1 |  |  |  |
| VAL_LIST | nvarchar | 510 | 1 |  |  |  |
| SRC_EVNT_KEY_STSTC_TYPE_1 | tinyint | 1 | 1 |  |  |  |
| SRC_EVNT_KEY_STSTC_TYPE_2 | tinyint | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_STSTC_TYPE_1 | tinyint | 1 | 1 |  |  |  |
| DSTNTN_EVNT_KEY_STSTC_TYPE_2 | tinyint | 1 | 1 |  |  |  |
