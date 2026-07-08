# dbo.FNDTN_BLNCNG_GRP

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BLNCNG_GRP_ID | binary | 16 | 0 |  |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| FRST_APP_ID | int | 4 | 0 |  |  |  |
| FRST_CMPNY_ID | int | 4 | 0 |  |  |  |
| FRST_PROD_ID | varchar | 30 | 1 |  |  |  |
| FRST_NAME | nvarchar | 10 | 0 |  |  |  |
| SCND_APP_ID | int | 4 | 0 |  |  |  |
| SCND_CMPNY_ID | int | 4 | 0 |  |  |  |
| SCND_PROD_ID | varchar | 30 | 1 |  |  |  |
| SCND_NAME | nvarchar | 10 | 0 |  |  |  |
| ACTV_FLG | bit | 1 | 0 |  |  |  |
