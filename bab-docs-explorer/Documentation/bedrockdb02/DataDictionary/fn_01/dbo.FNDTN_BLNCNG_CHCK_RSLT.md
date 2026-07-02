# dbo.FNDTN_BLNCNG_CHCK_RSLT

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BLCNG_CHCK_EXEC_ID | binary | 16 | 0 | YES | YES |  |
| SQNC_NO | int | 4 | 0 | YES |  |  |
| KEY_CLMN_NAMES | nvarchar | 4000 | 1 |  |  |  |
| KEY_VALUES | nvarchar | 4000 | 1 |  |  |  |
| BLNCNG_ISSUE | tinyint | 1 | 0 |  | YES |  |
| SIDE_NAME | varchar | 11 | 1 |  |  |  |
| BLNCNG_ERROR | text | 16 | 1 |  |  |  |
| CLMN_NAMES | nvarchar | 8000 | 1 |  |  |  |
| FRST_ROW_VALUES | nvarchar | 8000 | 1 |  |  |  |
| SCND_ROW_VALUES | nvarchar | 8000 | 1 |  |  |  |
| TLRNC | varchar | 4000 | 1 |  |  |  |

