# dbo.FNDTN_SCRTY_APP_INFO

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| USER_ID | int | 4 | 0 | YES |  |  |
| APP_ID | int | 4 | 0 | YES |  |  |
| DB_GRP_ID | int | 4 | 0 |  |  |  |
| INSTNCS | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_SCRTY_APP_INFO_EX_PS](../../StoredProcedures/fn_01/dbo.FNDTN_SCRTY_APP_INFO_EX_PS.md)
- [fn_01: dbo.FNDTN_SCRTY_APP_INFO_PS](../../StoredProcedures/fn_01/dbo.FNDTN_SCRTY_APP_INFO_PS.md)

