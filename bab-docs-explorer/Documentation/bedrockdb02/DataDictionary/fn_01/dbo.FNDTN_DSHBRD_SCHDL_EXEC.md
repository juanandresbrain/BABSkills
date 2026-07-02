# dbo.FNDTN_DSHBRD_SCHDL_EXEC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EXEC_ID | binary | 16 | 0 | YES |  |  |
| SCHDL_ID | binary | 16 | 0 |  |  |  |
| START_DATE_TIME | smalldatetime | 4 | 0 |  |  |  |
| INIT_END_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| EXEC_END_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| RQRMNT_END_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| IS_APLCBL | bit | 1 | 1 |  |  |  |
| OUTPUT_END_DATE_TIME | smalldatetime | 4 | 1 |  |  |  |
| ERR_MSG | nvarchar | -1 | 1 |  |  |  |

