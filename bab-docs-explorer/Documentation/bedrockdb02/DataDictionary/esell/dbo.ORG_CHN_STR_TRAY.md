# dbo.ORG_CHN_STR_TRAY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TRAY_ID | T_ID | 16 | 0 | YES |  |  |
| TRAY_NUM | T_INTEGER | 2 | 0 |  |  |  |
| TRAY_DESC | nvarchar | 510 | 1 |  |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  | YES |  |
| MAX_ALWD_TNDR_AMT | T_MONEY | 9 | 1 |  |  |  |
| DFLT_OPEN_CASH_BLNC_AMT | T_MONEY | 9 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |

