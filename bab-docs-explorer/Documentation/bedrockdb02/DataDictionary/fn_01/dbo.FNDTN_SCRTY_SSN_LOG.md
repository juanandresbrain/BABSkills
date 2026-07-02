# dbo.FNDTN_SCRTY_SSN_LOG

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SSN_ID | T_ID | 16 | 0 | YES |  |  |
| USER_ID | int | 4 | 0 | YES |  |  |
| STRT_TIME | datetime | 8 | 0 | YES |  |  |
| END_TIME | datetime | 8 | 0 |  |  |  |
| MCHN_NAME | varchar | 255 | 0 |  |  |  |
| PID | int | 4 | 0 |  |  |  |
| STS | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_SCRTY_SSN_EX_PS](../../StoredProcedures/fn_01/dbo.FNDTN_SCRTY_SSN_EX_PS.md)
- [fn_01: dbo.FNDTN_SCRTY_SSN_PS](../../StoredProcedures/fn_01/dbo.FNDTN_SCRTY_SSN_PS.md)

