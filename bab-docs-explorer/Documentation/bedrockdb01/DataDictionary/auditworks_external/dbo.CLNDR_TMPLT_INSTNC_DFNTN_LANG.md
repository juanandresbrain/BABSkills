# dbo.CLNDR_TMPLT_INSTNC_DFNTN_LANG

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LANG_ID | T_INTEGER | 2 | 0 |  |  |  |
| CLNDR_TMPLT_ID | T_ID | 16 | 0 |  |  |  |
| CHLD_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_CLNDR_LVL_TYPE_ID | T_ID | 16 | 0 |  |  |  |
| CLNDR_TMPLT_INSTNC_SEQ | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| LBL_TEXT | nvarchar | 510 | 1 |  |  |  |
