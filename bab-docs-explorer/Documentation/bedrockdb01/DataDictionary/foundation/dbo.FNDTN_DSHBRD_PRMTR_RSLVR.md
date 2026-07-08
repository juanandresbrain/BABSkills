# dbo.FNDTN_DSHBRD_PRMTR_RSLVR

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRMTR_TYPE_ID | int | 4 | 0 |  |  |  |
| LVL_NUM | int | 4 | 0 |  |  |  |
| SEQ_NUM | int | 4 | 0 |  |  |  |
| QRY | nvarchar | -1 | 0 |  |  |  |
| RSLVR_TYPE | smallint | 2 | 1 |  |  |  |
| RSLT_DATA_TYPE_NAME | nvarchar | 100 | 1 |  |  |  |
| SRC_APP_ID | int | 4 | 0 |  |  |  |
| TRGT_APP_ID | int | 4 | 0 |  |  |  |
| QRY_APP_ID | int | 4 | 1 |  |  |  |
| QRY_PROD_ID | varchar | 30 | 1 |  |  |  |
| PRMTR_RSLVR_ID | binary | 16 | 0 |  |  |  |
