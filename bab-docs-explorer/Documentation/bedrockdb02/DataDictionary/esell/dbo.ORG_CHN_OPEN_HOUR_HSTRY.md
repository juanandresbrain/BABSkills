# dbo.ORG_CHN_OPEN_HOUR_HSTRY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| EFCTV_DATE | T_DATE | 8 | 0 | YES |  |  |
| EXPRTN_DATE | T_DATE | 8 | 1 |  |  |  |
| HOUR_ID | T_ID | 16 | 0 |  | YES |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

