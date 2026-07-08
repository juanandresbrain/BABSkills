# dbo.FNDTN_CSTMZTN_FLD

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FNDTN_CSTMZTN_SCHM_ID | T_ID | 16 | 0 |  |  |  |
| FLD_ID | T_ID | 16 | 0 |  |  |  |
| FLD_NAME | nvarchar | 100 | 0 |  |  |  |
| CPTN_RES_NAME | nvarchar | 510 | 1 |  |  |  |
| DATA_TYPE | nvarchar | 510 | 0 |  |  |  |
| DATA_LNGTH | int | 4 | 1 |  |  |  |
| DFLT_VAL | nvarchar | 100 | 1 |  |  |  |
| FRMT_MSK | nvarchar | 510 | 1 |  |  |  |
| INPT_MSK | nvarchar | 510 | 1 |  |  |  |
| INPT_RQRD | bit | 1 | 0 |  |  |  |
| VLDTN_REG_EXP | nvarchar | 1000 | 1 |  |  |  |
