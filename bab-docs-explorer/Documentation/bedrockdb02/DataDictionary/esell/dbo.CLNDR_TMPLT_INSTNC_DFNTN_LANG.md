# dbo.CLNDR_TMPLT_INSTNC_DFNTN_LANG

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LANG_ID | T_INTEGER | 2 | 0 | YES | YES |  |
| CLNDR_TMPLT_ID | T_ID | 16 | 0 | YES | YES |  |
| CHLD_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 | YES | YES |  |
| PRNT_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 | YES | YES |  |
| CLNDR_TMPLT_INSTNC_SEQ | T_SEQUENCE_NUMBER | 9 | 0 | YES | YES |  |
| LBL_TEXT | nvarchar | 510 | 1 |  |  |  |

