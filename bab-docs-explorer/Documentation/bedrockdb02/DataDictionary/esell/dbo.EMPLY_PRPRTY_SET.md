# dbo.EMPLY_PRPRTY_SET

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRPRTY_SET_CODE | nchar | 8 | 0 | YES |  |  |
| PRPRTY_SET_DESC | nvarchar | 510 | 0 |  |  |  |
| PRPRTY_SET_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| DSPLY_FRMT | nvarchar | 1020 | 1 |  |  |  |
| VLDTN_MASK | nvarchar | 1020 | 1 |  |  |  |
| VLDTN_ER_MSG | nvarchar | 510 | 1 |  |  |  |
| MNDTRY_ASGNMNT | T_BOOLEAN | 5 | 0 |  |  |  |
| MTLY_EXCLSV | T_BOOLEAN | 5 | 0 |  |  |  |
| DFLT_PRPRTY_VAL_CODE | nchar | 12 | 0 |  |  |  |

