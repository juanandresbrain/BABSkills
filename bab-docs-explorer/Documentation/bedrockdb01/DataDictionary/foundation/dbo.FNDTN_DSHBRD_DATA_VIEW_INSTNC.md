# dbo.FNDTN_DSHBRD_DATA_VIEW_INSTNC

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  |  |  |
| DATA_VIEW_ID | binary | 16 | 0 |  |  |  |
| DSPLY_MODE_ID | smallint | 2 | 0 |  |  |  |
| ORDER_BY | varchar | 255 | 1 |  |  |  |
| BASE_CLCLTN_DATE | nvarchar | 50 | 1 |  |  |  |
| CLNDR_TYPE_ID | tinyint | 1 | 1 |  |  |  |
| PRD_TYPE | tinyint | 1 | 1 |  |  |  |
| PRD_COUNT | tinyint | 1 | 1 |  |  |  |
| OPTN_VALUE_LIST | nvarchar | 2000 | 1 |  |  |  |
| DSHBRD_ID | binary | 16 | 1 |  |  |  |
| PSTN_ID | tinyint | 1 | 1 |  |  |  |
| IS_ORGNLY_VSBL | bit | 1 | 1 |  |  |  |
| CMPNY_ID | smallint | 2 | 1 |  |  |  |
| GRP_CLMN_CNT | tinyint | 1 | 1 |  |  |  |
| IS_AVLBL_MBL | bit | 1 | 1 |  |  |  |
