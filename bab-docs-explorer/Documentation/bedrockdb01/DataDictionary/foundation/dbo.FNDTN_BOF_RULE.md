# dbo.FNDTN_BOF_RULE

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RULE_ID | T_ID | 16 | 0 |  |  |  |
| ENTTY_INTRFC_NAME | varchar | 255 | 0 |  |  |  |
| SRVR_SIDE | bit | 1 | 0 |  |  |  |
| CLNT_SIDE | bit | 1 | 0 |  |  |  |
| IN_TRANS | bit | 1 | 0 |  |  |  |
| THRD_SAFE | bit | 1 | 0 |  |  |  |
| ACTV | bit | 1 | 0 |  |  |  |
| CLS_NAME | varchar | 255 | 0 |  |  |  |
| ASMBLY_NAME | varchar | 255 | 0 |  |  |  |
| PRPRTY_NAME | varchar | 80 | 1 |  |  |  |
