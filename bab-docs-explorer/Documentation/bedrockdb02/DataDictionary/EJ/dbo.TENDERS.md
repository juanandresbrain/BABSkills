# dbo.TENDERS

**Database:** EJ  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATETIME | datetime | 8 | 0 |  |  |  |
| TRANNO | int | 4 | 0 |  |  |  |
| TILLNO | smallint | 2 | 0 |  |  |  |
| TENDER | int | 4 | 0 |  |  |  |
| STORENO | int | 4 | 0 |  |  |  |
| TRANCAT | char | 3 | 1 |  |  |  |
| AUDITID | int | 4 | 1 |  |  |  |
| ACCT_SRCH_KEY | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [EJ: dbo.spTruncateEJHistory](../../StoredProcedures/EJ/dbo.spTruncateEJHistory.md)

