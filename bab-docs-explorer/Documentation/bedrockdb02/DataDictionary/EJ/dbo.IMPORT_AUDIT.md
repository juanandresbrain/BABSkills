# dbo.IMPORT_AUDIT

**Database:** EJ  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STORENO | int | 4 | 0 |  |  |  |
| RECORDS_EFFECTED | int | 4 | 0 |  |  |  |
| DATE_IMPORTED | datetime | 8 | 0 |  |  |  |
| MESSAGE | char | 100 | 1 |  |  |  |
| SUCCESS | bit | 1 | 0 |  |  |  |
| AUDITID | int | 4 | 0 | YES |  |  |
| FILENAME | char | 30 | 1 |  |  |  |

## Referenced By Stored Procedures

- [EJ: dbo.spTruncateEJHistory](../../StoredProcedures/EJ/dbo.spTruncateEJHistory.md)

