# dbo.CLNDR_TMPLT_INSTNC_DFNTN

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_TMPLT_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| CHLD_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| CLNDR_TMPLT_INSTNC_SEQ | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| LBL_TEXT | nvarchar | 510 | 1 |  |  |  |
| CHLD_CNT | T_INTEGER | 2 | 1 |  |  |  |
| CHLD_CNT_ALGRTHM_ID | T_ID | 16 | 1 |  |  |  |
