# dbo.UDASuppliesSold

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UPC | nvarchar | 52 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| Cost | decimal | 17 | 1 |  |  |  |
| LocationCost | decimal | 17 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputSuppliesUDA](../../StoredProcedures/me_01/dbo.spMerchandisingOutputSuppliesUDA.md)
- [me_01: dbo.spMerchandisingSelectSuppliesUDA](../../StoredProcedures/me_01/dbo.spMerchandisingSelectSuppliesUDA.md)

