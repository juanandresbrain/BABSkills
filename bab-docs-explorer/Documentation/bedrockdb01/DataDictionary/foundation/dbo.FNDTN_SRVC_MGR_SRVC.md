# dbo.FNDTN_SRVC_MGR_SRVC

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SRVC_INSTNC_ID | smallint | 2 | 0 |  |  |  |
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
| RMTNG_ACTV_FLAG | bit | 1 | 0 |  |  |  |
| WCF_ACTV_FLAG | bit | 1 | 0 |  |  |  |
