# dbo.EMPLY_HRCHY_LVL_GRP

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HRCHY_LVL_GRP_ID | T_INTEGER | 2 | 0 | YES |  |  |
| HRCHY_LVL_GRP_DESC | nvarchar | 510 | 0 |  |  |  |
| GRP_MBR_CHNG | T_DATE | 8 | 1 |  |  |  |
| HRCHY_LVL_ID | T_ID | 16 | 0 |  | YES |  |
| HRCHY_ID | T_ID | 16 | 0 |  |  |  |
| PRNT_HRCHY_LVL_GRP_ID | T_INTEGER | 2 | 1 |  | YES |  |

