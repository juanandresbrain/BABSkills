# dbo.FNDTN_SCRTY_APP_ACS_KEY

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| APP_ID | int | 4 | 0 |  |  |  |
| ACS_KEY | varbinary | 10 | 0 |  |  |  |
| ACS_KEY_LVL | tinyint | 1 | 0 |  |  |  |
| ACS_KEY_DSPLY_ORDR | smallint | 2 | 0 |  |  |  |
| ACS_KEY_NAME | varchar | 50 | 0 |  |  |  |
| ACS_KEY_DESC | varchar | 255 | 1 |  |  |  |
| ACS_KEY_DATA | bit | 1 | 0 |  |  |  |
| ACS_KEY_DATA_MASK | varchar | 64 | 1 |  |  |  |
| ACS_KEY_DATA_CLIP_TEXT | bit | 1 | 0 |  |  |  |
| ACS_KEY_DATA_MLTI_VAL | bit | 1 | 0 |  |  |  |
| ACS_KEY_NAME_RSRC_NAME | varchar | 255 | 1 |  |  |  |
| ACS_KEY_DESC_RSRC_NAME | varchar | 255 | 1 |  |  |  |
