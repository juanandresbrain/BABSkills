# dbo.CLNDR

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNDR_ID | T_ID | 16 | 0 | YES |  |  |
| CLNDR_DESC | nvarchar | 510 | 0 |  |  |  |
| AVLBL_DATE | T_DATE | 8 | 1 |  |  |  |
| CLNDR_TMPLT_ID | T_ID | 16 | 1 |  | YES |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |

