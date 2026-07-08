# dbo.CSTM_PRPRTY

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CSTM_PRPRTY_TYPE | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| CSTM_PRPRTY_CODE | nvarchar | 16 | 0 |  |  |  |
| CSTM_PRPRTY_DESC | nvarchar | 510 | 1 |  |  |  |
| IS_MNDTRY | T_BOOLEAN | 5 | 0 |  |  |  |
| IS_SYSTM_DFND | T_BOOLEAN | 5 | 0 |  |  |  |
| DATA_TYPE | T_CODE1 | 2 | 1 |  |  |  |
| VLDTN_RULE | nvarchar | 510 | 1 |  |  |  |
| VLDTN_ERRMSG | nvarchar | 510 | 1 |  |  |  |
| DSPLY_FRMT | nvarchar | 510 | 1 |  |  |  |
| RNG_FRM | nvarchar | 510 | 1 |  |  |  |
| RNG_TO | nvarchar | 510 | 1 |  |  |  |
| DFLT_VAL | nvarchar | 510 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
