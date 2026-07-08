# dbo.EVNT_FLD_ASCTN

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_TYPE_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| EVNT_FLD_ID | T_INTEGER | 2 | 0 |  |  |  |
| IS_KEY | T_BOOLEAN | 5 | 0 |  |  |  |
| IS_GRP_KEY | T_BOOLEAN | 5 | 0 |  |  |  |
| FLD_ORDR | T_INTEGER | 2 | 0 |  |  |  |
| HAS_SUM | T_BOOLEAN | 5 | 0 |  |  |  |
| HAS_MIN | T_BOOLEAN | 5 | 0 |  |  |  |
| HAS_MAX | T_BOOLEAN | 5 | 0 |  |  |  |
| HAS_FRST | T_BOOLEAN | 5 | 0 |  |  |  |
| HAS_LAST | T_BOOLEAN | 5 | 0 |  |  |  |
| IS_DSPLD_IN_CLMN | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| ROW_ID | T_LONG_INTEGER | 4 | 0 | YES |  |  |
