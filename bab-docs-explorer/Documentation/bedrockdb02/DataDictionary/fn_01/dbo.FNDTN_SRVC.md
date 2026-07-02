# dbo.FNDTN_SRVC

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SRVC_ID | binary | 16 | 0 | YES |  |  |
| SRVC_LBL | varchar | 50 | 0 |  |  |  |
| SRVC_EXE_NAME | varchar | 255 | 0 |  |  |  |
| APP_ID | smallint | 2 | 0 |  |  |  |
| PROD_ID | varchar | 30 | 1 |  |  |  |
| SRVC_VRSN | varchar | 30 | 0 |  |  |  |
| USES_RMTNG | bit | 1 | 0 |  |  |  |
| USES_WCF | bit | 1 | 0 |  |  |  |
| CLIC_APP_NAME | varchar | 50 | 1 |  |  |  |
| CLIC_TAG_NAME | varchar | 60 | 1 |  |  |  |
| RCV_TCKT | bit | 1 | 0 |  |  |  |
| SND_TCKT | bit | 1 | 0 |  |  |  |

