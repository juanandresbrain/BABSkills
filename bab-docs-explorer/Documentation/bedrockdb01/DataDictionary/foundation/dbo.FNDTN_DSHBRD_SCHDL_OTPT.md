# dbo.FNDTN_DSHBRD_SCHDL_OTPT

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SCHDL_OTPT_ID | binary | 16 | 0 |  |  |  |
| SCHDL_ID | binary | 16 | 0 |  |  |  |
| FRMT_TYPE | tinyint | 1 | 0 |  |  |  |
| DLVRY_TYPE | tinyint | 1 | 0 |  |  |  |
| FRMT_MSG_TEXT | nvarchar | 8000 | 1 |  |  |  |
| DLVRY_ADRS | nvarchar | 512 | 0 |  |  |  |
| FRMT_MSG_SBJCT_TEXT | nvarchar | 512 | 1 |  |  |  |
