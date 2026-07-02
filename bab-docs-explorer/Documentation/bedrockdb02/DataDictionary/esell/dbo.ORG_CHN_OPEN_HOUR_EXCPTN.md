# dbo.ORG_CHN_OPEN_HOUR_EXCPTN

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| EXCPTN_DATE | T_DATE | 8 | 0 | YES |  |  |
| START_TIME | T_TIME | 8 | 0 | YES |  |  |
| END_TIME | T_TIME | 8 | 0 | YES |  |  |
| CLSD | T_BOOLEAN | 5 | 0 |  |  |  |
| RSN_ID | T_ID | 16 | 0 |  | YES |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

