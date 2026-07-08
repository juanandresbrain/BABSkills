# dbo.CLNDR_TMPLT_LVL_ASCTN

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_TMPLT_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| CHLD_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| CHLD_CNT | T_INTEGER | 2 | 1 |  |  |  |
| CHLD_CNT_ALGRTHM_ID | T_ID | 16 | 1 |  |  |  |
