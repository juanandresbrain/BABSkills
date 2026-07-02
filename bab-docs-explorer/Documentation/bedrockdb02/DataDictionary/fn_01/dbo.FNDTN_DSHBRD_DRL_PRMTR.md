# dbo.FNDTN_DSHBRD_DRL_PRMTR

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DRL_DWN_ID | binary | 16 | 0 | YES | YES |  |
| TRGT_PRMTR_TYPE_ID | int | 4 | 0 | YES | YES |  |
| PRMTR_VALUE | nvarchar | 510 | 1 |  |  |  |
| SRC_PRMTR_TYPE_ID | int | 4 | 1 |  | YES |  |
| SRC_CLMN_ID | binary | 16 | 1 |  | YES |  |
| PRMTR_DSPLY_VALUE | nvarchar | 510 | 1 |  |  |  |
| HRCHY_LVL_NUM | int | 4 | 1 |  |  |  |

