# dbo.FNDTN_DSHBRD_DRL_DWN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DRL_DWN_ID | binary | 16 | 0 | YES |  |  |
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  | YES |  |
| PRTY_ORDR | tinyint | 1 | 0 |  |  |  |
| DRL_DWN_MODE_ID | smallint | 2 | 0 |  | YES |  |
| TRGT_ID | binary | 16 | 1 |  |  |  |
| TRGT_PSTN_ID | tinyint | 1 | 1 |  |  |  |
| TRGR_CLMN_ID | binary | 16 | 1 |  | YES |  |

