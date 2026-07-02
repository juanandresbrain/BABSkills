# dbo.ADT_TRL_QRY_KEY_PART

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| KEY_PART_CODE | T_SHORT_NAME | 25 | 0 | YES |  |  |
| KEY_PART_RSRC_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| KEY_PART_TYPE | T_LONG_DATA | 255 | 0 |  |  |  |
| KEY_PART_LKP_SQL | T_SHORT_TEXT | 4000 | 1 |  |  |  |
| LKP_APP_ID | T_INTEGER | 2 | 1 |  |  |  |
| LKP_PROD_ID | T_SHORT_NAME | 25 | 1 |  |  |  |

