# dbo.ORG_CHN_LOC_HRCHY_LVL

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_ID | T_ID | 16 | 0 | YES |  |  |
| HRCHY_LVL_DESC | nvarchar | 510 | 0 |  |  |  |
| SEQ_NUM | T_SEQUENCE_NUMBER | 9 | 0 |  |  |  |
| AFLTN_PRMTD | T_BOOLEAN | 5 | 0 |  |  |  |
| HRCHY_ID | T_ID | 16 | 0 |  | YES |  |
| PRNT_HRCHY_LVL_ID | T_ID | 16 | 1 |  | YES |  |

