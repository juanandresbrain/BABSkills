# dbo.FNDTN_DSHBRD_DRL_PRMTR

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DRL_DWN_ID | binary | 16 | 0 |  |  |  |
| TRGT_PRMTR_TYPE_ID | int | 4 | 0 |  |  |  |
| PRMTR_VALUE | nvarchar | 510 | 1 |  |  |  |
| SRC_PRMTR_TYPE_ID | int | 4 | 1 |  |  |  |
| SRC_CLMN_ID | binary | 16 | 1 |  |  |  |
| PRMTR_DSPLY_VALUE | nvarchar | 510 | 1 |  |  |  |
| HRCHY_LVL_NUM | int | 4 | 1 |  |  |  |
