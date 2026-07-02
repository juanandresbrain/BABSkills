# dbo.EMPLY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| SLTN | nvarchar | 50 | 1 |  |  |  |
| FRST_NAME | nvarchar | 100 | 1 |  |  |  |
| MDL_NAME | nvarchar | 100 | 1 |  |  |  |
| LAST_NAME | nvarchar | 100 | 0 |  |  |  |
| SFX | nvarchar | 50 | 1 |  |  |  |
| OFCL_NAME | nvarchar | 100 | 1 |  |  |  |
| MAIL_NAME | nvarchar | 100 | 1 |  |  |  |
| PHNTC_NAME | nvarchar | 100 | 1 |  |  |  |
| SORT_NAME | nvarchar | 100 | 1 |  |  |  |
| GNDR | nvarchar | 8 | 1 |  |  |  |
| DATE_OF_BRTH | T_DATE | 8 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| MRTL_STS | nvarchar | 8 | 1 |  |  |  |
| SHRT_NAME | nvarchar | 50 | 0 |  |  |  |
| HS_ACNT_NUM | nvarchar | 160 | 1 |  |  |  |
| SNRTY_DATE | T_DATE | 8 | 1 |  |  |  |
| SCRTY_CLS_CODE | nchar | 8 | 1 |  |  |  |
| DFLT_ADRS_SEQ | T_SEQUENCE_NUMBER | 9 | 1 |  | YES |  |
| PRFL_ID | T_ID | 16 | 1 |  | YES |  |
| EMPLY_STS_CODE | nvarchar | 8 | 0 |  | YES |  |
| EDCTN_LVL_CODE | nchar | 8 | 1 |  | YES |  |
| AVLBLTY_HOUR_ID | T_ID | 16 | 1 |  | YES |  |
| IMG_ATCHMNT_ID | T_ID | 16 | 1 |  |  |  |
| PRTY_ID | T_ID | 16 | 0 |  | YES |  |
| PRMY_ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  | YES |  |
| TTL_PSTN_CODE | nvarchar | 8 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

