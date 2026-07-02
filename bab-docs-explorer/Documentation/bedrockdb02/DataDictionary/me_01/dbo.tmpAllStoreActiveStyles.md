# dbo.tmpAllStoreActiveStyles

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| location_name | varchar | 52 | 1 |  |  |  |
| style | varchar | 6 | 1 |  |  |  |
| description | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailInactiveSkusValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailInactiveSkusValidation.md)

