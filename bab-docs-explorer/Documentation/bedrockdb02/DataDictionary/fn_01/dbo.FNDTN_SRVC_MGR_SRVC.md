# dbo.FNDTN_SRVC_MGR_SRVC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SRVC_INSTNC_ID | smallint | 2 | 0 | YES |  |  |
| SRVC_MGR_ID | smallint | 2 | 0 |  |  |  |
| SRVC_ID | binary | 16 | 0 |  |  |  |
| ACTV_FLAG | bit | 1 | 0 |  |  |  |
| START_TIME | datetime | 8 | 1 |  |  |  |
| STOP_TIME | datetime | 8 | 1 |  |  |  |
| HTTP_PORT_NO | smallint | 2 | 1 |  |  |  |
| TCP_PORT_NO | smallint | 2 | 1 |  |  |  |
| CRNT_STATUS | smallint | 2 | 0 |  |  |  |
| CRNT_PRCS_ID | int | 4 | 1 |  |  |  |
| CRNT_EXEC_ID | int | 4 | 1 |  |  |  |
| STRTP_RQST | smallint | 2 | 0 |  |  |  |
| WCF_HTTP_PORT_NO | smallint | 2 | 1 |  |  |  |
| WCF_NET_TCP_PORT_NO | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_SRVC_CHNG_STTS_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_CHNG_STTS_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_STPD_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_STPD_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_STRTD_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_STRTD_$SP.md)
- [fn_01: dbo.FNDTN_SRVC_UPDTNG_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SRVC_UPDTNG_$SP.md)

