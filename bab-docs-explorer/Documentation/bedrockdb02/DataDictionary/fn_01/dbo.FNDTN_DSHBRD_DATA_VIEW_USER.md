# dbo.FNDTN_DSHBRD_DATA_VIEW_USER

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 | YES | YES |  |
| USER_ID | int | 4 | 0 | YES |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| DSPLY_MODE_ID | smallint | 2 | 1 |  | YES |  |
| ORDER_BY | varchar | 255 | 1 |  |  |  |
| BASE_CLCLTN_DATE | varchar | 25 | 1 |  |  |  |
| CLNDR_TYPE_ID | tinyint | 1 | 1 |  | YES |  |
| PRD_TYPE | tinyint | 1 | 1 |  | YES |  |
| PRD_COUNT | tinyint | 1 | 1 |  |  |  |
| OPTN_VALUE_LIST | nvarchar | 2000 | 1 |  |  |  |
| GRP_CLMN_CNT | tinyint | 1 | 1 |  |  |  |
| IS_AVLBL_MBL | bit | 1 | 1 |  |  |  |

