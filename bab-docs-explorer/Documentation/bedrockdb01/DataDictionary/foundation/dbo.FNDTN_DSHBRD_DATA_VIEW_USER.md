# dbo.FNDTN_DSHBRD_DATA_VIEW_USER

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  |  |  |
| USER_ID | int | 4 | 0 |  |  |  |
| IS_VSBL | bit | 1 | 0 |  |  |  |
| DSPLY_MODE_ID | smallint | 2 | 1 |  |  |  |
| ORDER_BY | varchar | 255 | 1 |  |  |  |
| BASE_CLCLTN_DATE | varchar | 25 | 1 |  |  |  |
| CLNDR_TYPE_ID | tinyint | 1 | 1 |  |  |  |
| PRD_TYPE | tinyint | 1 | 1 |  |  |  |
| PRD_COUNT | tinyint | 1 | 1 |  |  |  |
| OPTN_VALUE_LIST | nvarchar | 2000 | 1 |  |  |  |
| GRP_CLMN_CNT | tinyint | 1 | 1 |  |  |  |
| IS_AVLBL_MBL | bit | 1 | 1 |  |  |  |
