# dbo.Transactions

**Database:** EJ  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATETIME | datetime | 8 | 0 | YES |  |  |
| TRANNO | int | 4 | 0 | YES |  |  |
| TILLNO | smallint | 2 | 0 | YES |  |  |
| STORENO | int | 4 | 0 | YES |  |  |
| TRANCAT | char | 3 | 1 |  |  |  |
| OPERATOR_LOGIN | varchar | 20 | 1 |  |  |  |
| SALESPERSON_LOGIN | varchar | 20 | 1 |  |  |  |
| TRANAMT | money | 8 | 1 |  |  |  |
| VOID | bit | 1 | 1 |  |  |  |
| EMPDSC | bit | 1 | 1 |  |  |  |
| TRANTYPE | smallint | 2 | 0 |  |  |  |
| MONEYBACK | bit | 1 | 1 |  |  |  |
| PRICECHG | bit | 1 | 1 |  |  |  |
| MARKDOWN | bit | 1 | 1 |  |  |  |
| RETURNFLG | bit | 1 | 1 |  |  |  |
| RECEIPT | ntext | 16 | 1 |  |  |  |
| TRAINMODE | bit | 1 | 1 |  |  |  |
| ABORT | bit | 1 | 1 |  |  |  |
| RESUME | bit | 1 | 1 |  |  |  |
| SUSPEND | bit | 1 | 1 |  |  |  |
| SYS_DATETIME | datetime | 8 | 1 |  |  |  |
| AUDITID | int | 4 | 1 |  |  |  |
| FULL_TEXT_ID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [EJ: dbo.spTruncateEJHistory](../../StoredProcedures/EJ/dbo.spTruncateEJHistory.md)
- [EJ: dbo.usi_GetReceipt](../../StoredProcedures/EJ/dbo.usi_GetReceipt.md)

