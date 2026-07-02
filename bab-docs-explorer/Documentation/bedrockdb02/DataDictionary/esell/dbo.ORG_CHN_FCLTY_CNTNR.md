# dbo.ORG_CHN_FCLTY_CNTNR

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CNTNR_ID | T_ID | 16 | 0 | YES |  |  |
| CNTNR_TYPE_CODE | nvarchar | 8 | 0 |  | YES |  |
| CNTNR_DESC | nvarchar | 510 | 0 |  |  |  |
| CNTNR_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| BIN_LOC_ID | T_ID | 16 | 0 |  | YES |  |
| DPTH | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| WDTH | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| HGHT | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| MSR_CODE | nchar | 8 | 0 |  |  |  |

