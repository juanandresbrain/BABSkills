# dbo.FNDTN_DSHBRD_PRMTR_INSTNC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DSHBRD_ID | binary | 16 | 0 | YES | YES |  |
| PRMTR_TYPE_ID | int | 4 | 0 | YES | YES |  |
| PRMTR_VALUE | nvarchar | 510 | 0 |  |  |  |
| PRMTR_DSPLY_VALUE | nvarchar | 510 | 0 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| IS_READ_ONLY | bit | 1 | 0 |  |  |  |
| INIT_PRMTR_SLCTN_TYPE | tinyint | 1 | 1 |  |  |  |
| HRCHY_LVL_NUM | int | 4 | 1 |  |  |  |

