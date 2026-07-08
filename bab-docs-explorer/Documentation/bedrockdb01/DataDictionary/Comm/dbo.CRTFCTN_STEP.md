# dbo.CRTFCTN_STEP

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRTFCTN_STEP_ID | int | 4 | 0 | YES |  |  |
| STEP_NAME | nvarchar | 510 | 0 |  |  |  |
| STEP_TEXT | nvarchar | 2048 | 0 |  |  |  |
| STEP_STS | smallint | 2 | 0 |  |  |  |
| CRTFCTN_MSG_FLD_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_TRNSCTN_ATRBT_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_PRNT_STEP_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_RAW_DATA_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_MSG_RT_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_MSG_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_TRNSCTN_ID | int | 4 | 1 |  |  |  |
| CRTFCTN_ID | int | 4 | 1 |  |  |  |
| CRTN_DTM | datetime | 8 | 0 |  |  |  |
| CRTFCTN_DLTN_ID | int | 4 | 0 |  |  |  |
