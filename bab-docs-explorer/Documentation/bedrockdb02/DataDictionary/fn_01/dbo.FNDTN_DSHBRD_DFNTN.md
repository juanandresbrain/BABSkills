# dbo.FNDTN_DSHBRD_DFNTN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DSHBRD_ID | binary | 16 | 0 | YES |  |  |
| DSHBRD_LYT_TMPLT_ID | binary | 16 | 0 |  | YES |  |
| NAME_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| DESC_RES_NAME | nvarchar | 510 | 1 |  |  |  |
| OWNR_USER_ID | int | 4 | 0 |  |  |  |
| CTGRY_ID | smallint | 2 | 0 |  | YES |  |
| CRTN_DATE | datetime | 8 | 0 |  |  |  |
| TITLE_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| SCRTY_LVL | tinyint | 1 | 0 |  |  |  |
| NVGTNL_DATA_VIEW_INSTNC_ID | binary | 16 | 1 |  |  |  |

