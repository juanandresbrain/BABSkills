# dbo.CLNDR_TMPLT_INSTNC_DFNTN

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_TMPLT_ID | T_ID | 16 | 0 | YES | YES |  |
| CLNDR_TMPLT_ID | T_ID | 16 | 0 | YES | YES |  |
| PRNT_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 | YES | YES |  |
| CHLD_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 | YES | YES |  |
| CLNDR_TMPLT_INSTNC_SEQ | T_SEQUENCE_NUMBER | 9 | 0 | YES |  |  |
| LBL_TEXT | nvarchar | 510 | 1 |  |  |  |
| CHLD_CNT | T_INTEGER | 2 | 1 |  |  |  |
| CHLD_CNT_ALGRTHM_ID | T_ID | 16 | 1 |  | YES |  |

