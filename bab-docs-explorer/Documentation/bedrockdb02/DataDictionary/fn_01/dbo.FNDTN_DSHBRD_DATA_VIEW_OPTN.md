# dbo.FNDTN_DSHBRD_DATA_VIEW_OPTN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_ID | binary | 16 | 0 | YES | YES |  |
| OPTN_INDX | int | 4 | 0 | YES |  |  |
| NAME_RES_NAME | varchar | 255 | 0 |  |  |  |
| DESC_RES_NAME | varchar | 255 | 1 |  |  |  |
| TRGT_PRPRTY_NAME | varchar | 255 | 1 |  |  |  |
| DFLT_VALUE | nvarchar | 120 | 1 |  |  |  |
| OPTN_TYPE_ID | tinyint | 1 | 0 |  | YES |  |
| DSPLY_LIST | nvarchar | 4000 | 1 |  |  |  |
| VALUE_LIST | varchar | 255 | 1 |  |  |  |

