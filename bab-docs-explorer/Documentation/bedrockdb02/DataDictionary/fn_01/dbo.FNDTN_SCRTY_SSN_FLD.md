# dbo.FNDTN_SCRTY_SSN_FLD

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| USER_NAME | varchar | 255 | 0 |  |  |  |
| LOG_TIME | datetime | 8 | 0 |  |  |  |
| MCHN_NAME | varchar | 255 | 0 |  |  |  |
| PID | int | 4 | 0 |  |  |  |
| PC_USER_NAME | varchar | 255 | 1 |  |  |  |
| WNDWS_USER | int | 4 | 1 |  |  |  |
| LGN_ID | T_ID | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_ADD_USER_SSN_EX_PS](../../StoredProcedures/fn_01/dbo.FNDTN_ADD_USER_SSN_EX_PS.md)

