# dbo.CRTFCTN_TRNSCTN_ATRBT

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRTFCTN_TRNSCTN_ATRBT_ID | int | 4 | 0 | YES |  |  |
| ATRBT_NAME | nvarchar | 200 | 0 |  |  |  |
| ATRBT_TYPE | nvarchar | 60 | 0 |  |  |  |
| ATRBT_VAL | nvarchar | 4096 | 0 |  |  |  |
| CRTFCTN_TRNSCTN_ID | int | 4 | 0 |  |  |  |
| CRTFCTN_MSG_ID | int | 4 | 1 |  |  |  |
| CRTN_DTM | datetime | 8 | 0 |  |  |  |
| CRTFCTN_DLTN_ID | int | 4 | 0 |  |  |  |
