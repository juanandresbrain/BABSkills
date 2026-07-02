# dbo.SKUChange

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Reference | varchar | 20 | 1 |  |  |  |
| ASN | varchar | 20 | 1 |  |  |  |
| Style | varchar | 12 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectSKUChangeUDA](../../StoredProcedures/me_01/dbo.spMerchandisingSelectSKUChangeUDA.md)

