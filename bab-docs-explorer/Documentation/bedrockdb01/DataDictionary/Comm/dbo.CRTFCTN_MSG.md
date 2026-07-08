# dbo.CRTFCTN_MSG

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRTFCTN_MSG_ID | int | 4 | 0 | YES |  |  |
| MSG_NAME | nvarchar | 510 | 0 |  |  |  |
| CRTFCTN_TRNSCTN_ID | int | 4 | 0 |  |  |  |
| CRTFCTN_ID | int | 4 | 1 |  |  |  |
| IS_INCMNG | tinyint | 1 | 0 |  |  |  |
| CRTN_DTM | datetime | 8 | 0 |  |  |  |
| CRTFCTN_DLTN_ID | int | 4 | 0 |  |  |  |
