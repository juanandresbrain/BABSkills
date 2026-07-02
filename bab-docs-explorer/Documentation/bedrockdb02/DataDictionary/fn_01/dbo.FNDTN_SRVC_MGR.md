# dbo.FNDTN_SRVC_MGR

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SRVC_MGR_ID | smallint | 2 | 0 | YES |  |  |
| SRVC_MGR_LBL | nvarchar | 100 | 0 |  |  |  |
| SRVC_MGR_MCHN_NAME | nvarchar | 126 | 0 |  |  |  |
| SRVC_MGR_DSCRPTN | nvarchar | 510 | 1 |  |  |  |
| START_TIME | datetime | 8 | 1 |  |  |  |
| STOP_TIME | datetime | 8 | 1 |  |  |  |
| HTTP_PORT_NO | smallint | 2 | 0 |  |  |  |
| TCP_PORT_NO | smallint | 2 | 0 |  |  |  |
| CRNT_STATUS | numeric | 5 | 0 |  |  |  |
| ALLOW_CMPCT_MD | bit | 1 | 0 |  |  |  |
| INSTL_PATH | nvarchar | 510 | 0 |  |  |  |
| USES_RMTNG | bit | 1 | 0 |  |  |  |
| USES_WCF | bit | 1 | 0 |  |  |  |

