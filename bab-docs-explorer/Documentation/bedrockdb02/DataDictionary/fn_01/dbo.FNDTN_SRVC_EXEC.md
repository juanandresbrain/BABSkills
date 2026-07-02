# dbo.FNDTN_SRVC_EXEC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EXEC_ID | int | 4 | 0 | YES |  |  |
| SRVC_INSTNC_ID | smallint | 2 | 0 |  |  |  |
| CRNT_STATUS | smallint | 2 | 0 |  |  |  |
| START_TIME | datetime | 8 | 1 |  |  |  |
| EXIT_TIME | datetime | 8 | 1 |  |  |  |
| EXIT_CODE | int | 4 | 1 |  |  |  |
| STP_MTHD_ID | smallint | 2 | 1 |  |  |  |
| STD_ERROR | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_SRVC_CHNG_STTS_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_CHNG_STTS_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_STPD_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_STPD_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_STRTD_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_STRTD_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_UPDTNG_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_UPDTNG_$SP.md)

