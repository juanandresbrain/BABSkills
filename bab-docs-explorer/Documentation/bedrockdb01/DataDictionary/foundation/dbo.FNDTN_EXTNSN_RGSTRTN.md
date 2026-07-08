# dbo.FNDTN_EXTNSN_RGSTRTN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RGSTRTN_ID | T_ID | 16 | 0 |  |  |  |
| MTHD_ID | T_ID | 16 | 0 |  |  |  |
| ON_BFR | bit | 1 | 0 |  |  |  |
| ON_AFTR | bit | 1 | 0 |  |  |  |
| ON_ALL_STEPS | bit | 1 | 0 |  |  |  |
| THRD_SAFE | bit | 1 | 0 |  |  |  |
| CLS_NAME | varchar | 255 | 1 |  |  |  |
| ASMBLY_NAME | varchar | 255 | 1 |  |  |  |
| MSGNG_IDNTFR | varchar | 24 | 1 |  |  |  |
| WRKFLW_KEY_FLD_NAME | nvarchar | 510 | 1 |  |  |  |
| WRKFLW_KEY_LABEL | nvarchar | 510 | 1 |  |  |  |
| WRKFLW_ID | T_ID | 16 | 1 |  |  |  |
| RGSTRTN_TYPE | T_INTEGER | 2 | 0 |  |  |  |
