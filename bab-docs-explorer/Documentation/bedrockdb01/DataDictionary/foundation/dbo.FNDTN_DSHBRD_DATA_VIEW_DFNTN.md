# dbo.FNDTN_DSHBRD_DATA_VIEW_DFNTN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_ID | binary | 16 | 0 |  |  |  |
| DATA_SRC_TYPE_ID | smallint | 2 | 0 |  |  |  |
| NAME_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| DESC_RES_NAME | nvarchar | 510 | 1 |  |  |  |
| OWNR_USER_ID | int | 4 | 0 |  |  |  |
| CRTN_DATE | datetime | 8 | 0 |  |  |  |
| ASMBLY_NAME | varchar | 255 | 1 |  |  |  |
| CLS_NAME | varchar | 255 | 1 |  |  |  |
| TITLE_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| DFLT_DSPLY_MODE_ID | smallint | 2 | 0 |  |  |  |
| DS_STATEMENT | nvarchar | -1 | 1 |  |  |  |
| APP_ID | smallint | 2 | 0 |  |  |  |
| PROD_ID | varchar | 30 | 0 |  |  |  |
| ACS_KEY | varchar | 50 | 1 |  |  |  |
| ALWD_DSPLY_MODES | varchar | 255 | 0 |  |  |  |
| CTGRY_ID | smallint | 2 | 0 |  |  |  |
| EXTRNL_ID | varchar | 255 | 1 |  |  |  |
| RANK_CLMN_ID | binary | 16 | 1 |  |  |  |
| RANK_BSD_ON_CLMN_ID | binary | 16 | 1 |  |  |  |
| RANK_DRCTN | tinyint | 1 | 1 |  |  |  |
| RANK_TYPE | tinyint | 1 | 1 |  |  |  |
| RANK_VAL | numeric | 9 | 1 |  |  |  |
| SHOW_PREV_RANK_COL | bit | 1 | 1 |  |  |  |
| MIN_PRD_TYPE_ID | tinyint | 1 | 1 |  |  |  |
| ALW_DATE_RNG_SLCTN | bit | 1 | 1 |  |  |  |
| SHOW_EMPTY_ROWS | bit | 1 | 0 |  |  |  |
| SHOW_EMPTY_CLMNS | bit | 1 | 0 |  |  |  |
| SCRTY_LVL | tinyint | 1 | 0 |  |  |  |
| ORDER_BY | varchar | 30 | 1 |  |  |  |
| ALW_PRD_TYPE_SLCTN | bit | 1 | 0 |  |  |  |
| ALW_NUM_OF_PRDS_SLCTN | bit | 1 | 0 |  |  |  |
| GRP_CLMN_CNT | tinyint | 1 | 1 |  |  |  |
