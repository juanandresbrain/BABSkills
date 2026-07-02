# dbo.VERSION

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DB_CODE | char | 4 | 0 | YES |  |  |
| VERSION_NO | varchar | 20 | 1 |  |  |  |
| VERSION_DATETIME | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [USICOAL: dbo.GenDbConstants](../../StoredProcedures/USICOAL/dbo.GenDbConstants.md)

