# dbo.CRTFCTN_MSG_FLD

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRTFCTN_MSG_FLD_ID | int | 4 | 0 | YES |  |  |
| FLD_NAME | nvarchar | 200 | 0 |  |  |  |
| FLD_SEQ | smallint | 2 | 0 |  |  |  |
| FLD_SUB_SEQ | smallint | 2 | 0 |  |  |  |
| HDR_LEN_TYPE | smallint | 2 | 0 |  |  |  |
| HDR_LEN_LEN | smallint | 2 | 0 |  |  |  |
| HDR_LEN_VAL | nvarchar | 100 | 0 |  |  |  |
| HDR_LEN_ENCDNG | int | 4 | 0 |  |  |  |
| HDR_BTMP_LEN | smallint | 2 | 0 |  |  |  |
| HDR_BTMP_VAL | varchar | 66 | 0 |  |  |  |
| HDR_KEY_TYPE | smallint | 2 | 0 |  |  |  |
| HDR_KEY_LEN | smallint | 2 | 0 |  |  |  |
| HDR_KEY_VAL | nvarchar | 100 | 0 |  |  |  |
| HDR_KEY_ENCDNG | int | 4 | 0 |  |  |  |
| FLD_TYPE | smallint | 2 | 0 |  |  |  |
| FLD_LEN | smallint | 2 | 0 |  |  |  |
| FLD_VAL | nvarchar | 4096 | 0 |  |  |  |
| FLD_ENCDNG | int | 4 | 0 |  |  |  |
| FLD_SPRTR_TYPE | smallint | 2 | 0 |  |  |  |
| FLD_SPRTR_LEN | smallint | 2 | 0 |  |  |  |
| FLD_SPRTR_VAL | nvarchar | 100 | 0 |  |  |  |
| FLD_SPRTR_ENCDNG | int | 4 | 0 |  |  |  |
| RAW_DATA_HDR_LEN | smallint | 2 | 0 |  |  |  |
| RAW_DATA_FLD_LEN | smallint | 2 | 0 |  |  |  |
| HAS_SUB_FLD | smallint | 2 | 0 |  |  |  |
| CRTFCTN_MSG_ID | int | 4 | 1 |  |  |  |
| CRTN_DTM | datetime | 8 | 0 |  |  |  |
| CRTFCTN_DLTN_ID | int | 4 | 0 |  |  |  |
